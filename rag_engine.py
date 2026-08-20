import os
import re
import math
import json
import urllib.request
from typing import Dict, List, Tuple, Optional

# Load policy.text dynamically
def get_policy_text() -> str:
    try:
        policy_filename = os.getenv("POLICY_FILE_PATH", "policy.text")
        policy_path = os.path.join(os.path.dirname(__file__), policy_filename)
        if os.path.exists(policy_path):
            with open(policy_path, "r", encoding="utf-8") as f:
                return f.read()
    except Exception as e:
        print(f"[RAG Engine] Error reading policy file: {e}")
    return ""

def get_gemini_api_key() -> str:
    """Retrieve Gemini API key from environment or .evn/.env files."""
    key = os.getenv("GEMINI_API_KEY", "")
    if key:
        return key
    for env_path in [
        os.path.join(os.path.dirname(os.path.dirname(__file__)), ".evn"),
        os.path.join(os.path.dirname(__file__), ".evn"),
        os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"),
        os.path.join(os.path.dirname(__file__), ".env"),
    ]:
        if os.path.exists(env_path):
            try:
                with open(env_path, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("GEMINI_API_KEY="):
                            return line.split("=", 1)[1].strip().strip('"').strip("'")
            except Exception:
                pass
    return ""

_QA_MEMORY_CACHE = {}

def call_gemini_llm(prompt: str, system_instruction: Optional[str] = None, timeout: float = 2.0) -> Optional[str]:
    """Call Google Gemini LLM using the user's GEMINI_API_KEY with fast smart timeout."""
    api_key = get_gemini_api_key()
    if not api_key:
        return None
    
    models = ["gemini-2.5-flash", "gemini-1.5-flash", "gemini-flash-latest"]
    for model in models:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
            payload = {
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "temperature": 0.2,
                    "maxOutputTokens": 512
                }
            }
            if system_instruction:
                payload["systemInstruction"] = {
                    "parts": [{"text": system_instruction}]
                }
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"}
            )
            resp = urllib.request.urlopen(req, timeout=timeout)
            if resp.status == 200:
                data = json.loads(resp.read().decode("utf-8"))
                candidates = data.get("candidates", [])
                if candidates:
                    parts = candidates[0].get("content", {}).get("parts", [])
                    if parts:
                        return parts[0].get("text", "").strip()
        except Exception:
            # Continue to next or fallback immediately without blocking the user
            continue
    return None

def normalize_arabic(text: str) -> str:
    """Normalize Arabic text for resilient matching and tokenization."""
    if not text:
        return ""
    t = text.lower()
    t = re.sub(r'[أإآٱ]', 'ا', t)
    t = re.sub(r'ة', 'ه', t)
    t = re.sub(r'ى', 'ي', t)
    t = re.sub(r'[\u064B-\u065F\u0670]', '', t)
    t = re.sub(r'[؟\?!\.,;:\-_/\(\)\[\]"\']', ' ', t)
    return ' '.join(t.split())

def strip_arabic_affixes(word: str) -> str:
    """Strip common Arabic prepositions, conjunctions, and pronominal suffixes to reach core stem."""
    if not word or len(word) <= 2:
        return word
    w = normalize_arabic(word)
    
    # Strip common prefixes (وال, فال, بال, كال, لل, ال, و, ف, ب, ك, ل, س)
    prefixes = ['وال', 'فال', 'بال', 'كال', 'لل', 'ال', 'و', 'ف', 'ب', 'ك', 'ل', 'س']
    for p in prefixes:
        if w.startswith(p) and len(w) - len(p) >= 3:
            w = w[len(p):]
            break
            
    # Strip common suffixes (اتنا, اتكم, اتهم, اتي, تهم, تها, تنا, تكم, هم, هن, كم, نا, ها, ات, ين, ون, ي, ك, ه)
    suffixes = ['اتنا', 'اتكم', 'اتهم', 'اتي', 'تهم', 'تها', 'تنا', 'تكم', 'هم', 'هن', 'كم', 'نا', 'ها', 'ات', 'ين', 'ون', 'ي', 'ك', 'ه']
    for s in suffixes:
        if w.endswith(s) and len(w) - len(s) >= 3:
            w = w[:-len(s)]
            break
            
    return w

def tokenize_text(text: str) -> List[str]:
    """Tokenize Arabic & English text into clean normalized n-grams, words, and stripped stems."""
    if not text:
        return []
    cleaned = normalize_arabic(text)
    words = cleaned.split()
    
    # Include words and stripped stems
    tokens = list(words)
    for word in words:
        stem = strip_arabic_affixes(word)
        if stem and stem != word:
            tokens.append(stem)
            
        # Generate character 3-grams and 4-grams for robust Arabic fuzzy matching
        if len(word) >= 3:
            for i in range(len(word) - 2):
                tokens.append(word[i:i+3])
        if len(word) >= 4:
            for i in range(len(word) - 3):
                tokens.append(word[i:i+4])
    return tokens

def compute_tf_vector(tokens: List[str]) -> Dict[str, float]:
    """Compute term frequency vector."""
    tf = {}
    for t in tokens:
        tf[t] = tf.get(t, 0.0) + 1.0
    total = sum(tf.values()) or 1.0
    return {k: v / total for k, v in tf.items()}

def cosine_similarity(vec1: Dict[str, float], vec2: Dict[str, float]) -> float:
    """Compute Cosine Similarity between two sparse vectors."""
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    
    sum1 = sum([val ** 2 for val in vec1.values()])
    sum2 = sum([val ** 2 for val in vec2.values()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    
    if not denominator:
        return 0.0
    return float(numerator / denominator)

# ==============================================================================
# MODULAR POLICY CHUNKING & IN-MEMORY RAG RETRIEVAL
# ==============================================================================

SECTION_METADATA = {
    "01_WORKING_HOURS": {
        "title_ar": "أيام وساعات العمل الرسمية",
        "title_en": "Official Working Hours & Days",
        "category": "schedule",
        "content_en": """- Official Work Days: Sunday through Thursday.
- Official Working Hours: 9:00 AM to 5:00 PM.
- Total Weekly Load: 40 working hours per week."""
    },
    "02_LATENESS_RULES": {
        "title_ar": "ضوابط الحضور والتأخير والخصومات المالية",
        "title_en": "Lateness Rules, Grace Period & Deductions",
        "category": "penalties",
        "content_en": """- Grace Period: Up to 15 minutes delay is permitted (until 09:15 AM).
- Unexcused Delay (> 60 mins): Lateness exceeding 60 minutes without an approved excuse incurs a half-day salary deduction.
- Emergency Lateness: In case of an emergency, notify the direct supervisor immediately.
- Frequent Lateness: Lateness on 3 or more consecutive days incurs administrative warnings and financial deductions."""
    },
    "03_ATTENDANCE_LOGGING": {
        "title_ar": "تسجيل الحضور والانصراف وإثبات الغياب",
        "title_en": "Attendance Tracking & Absence Rules",
        "category": "checkin",
        "content_en": """- Check-In: Every employee must sign in and log attendance on the portal immediately upon arrival.
- Check-Out: Every employee must log departure upon leaving the premises.
- Absence: Failing to check in on the portal automatically classifies the employee as absent."""
    },
    "04_EXCUSE_TIME_WINDOW": {
        "title_ar": "المهلة الزمنية لتقديم طلبات الأعذار",
        "title_en": "Excuse Submission Window",
        "category": "time_limit",
        "content_en": """- Excuse requests must be submitted during official shift hours (9:00 AM to 5:00 PM) on the same day of the delay."""
    },
    "05_PROOF_REQUIREMENTS": {
        "title_ar": "شرط الإثبات والمرفقات الرسمية",
        "title_en": "Proof & Evidence Requirements",
        "category": "proof",
        "content_en": """- Medical & Health Excuses: Require attaching an official verified medical report for immediate approval.
- Traffic Accidents: Require attaching a police accident report (Kroka) or clear scene photo for immediate verification."""
    },
    "06_EXCUSES_CLASSIFICATION": {
        "title_ar": "تصنيف الأعذار (المقبولة والمرفوضة)",
        "title_en": "Acceptable vs Unacceptable Excuses",
        "category": "classification",
        "content_en": """Officially Acceptable Excuses:
1. Bereavement and family condolences.
2. Traffic accidents (with attached Kroka / police report).
3. Sudden breakdown of vehicle or public transportation en route.
4. Emergency health conditions (with attached medical report).
5. Severe force majeure weather conditions, heavy rains, or snowstorms.

Strictly Unacceptable Excuses (Marked as absence with salary deductions):
1. Waking up late ("I woke up late").
2. Regular traffic congestion ("Heavy traffic").
3. Non-emergency personal matters.
4. Alarm clock failure ("Alarm didn't work").
5. Staying up late / lack of sleep ("Slept late")."""
    },
    "07_EARLY_DEPARTURE_AND_PERMISSIONS": {
        "title_ar": "المغادرات الساعية والاستئذان الطارئ",
        "title_en": "Early Departure & Emergency Permissions",
        "category": "permissions",
        "content_en": """- Short leaves during shift hours are granted exclusively based on the employee's emergency situation.
- The direct supervisor must be notified with the emergency reason and approve before leaving.
- Leaving early or exiting the premises without prior permission and an emergency constitutes a disciplinary violation."""
    },
    "08_LEAVES_AND_VACATIONS": {
        "title_ar": "الإجازات السنوية والمرضية والرسمية",
        "title_en": "Annual & Sick Leaves Policy",
        "category": "leaves",
        "content_en": """- Annual Leave: 14 paid days annually; requests must be submitted at least 48 hours in advance.
- Sick Leave: Granted for health conditions and requires an official medical report within 24 hours of absence."""
    },
    "09_REMOTE_WORK_POLICY": {
        "title_ar": "سياسة العمل عن بُعد ومن المنزل (Remote Work)",
        "title_en": "Remote Work / WFH Policy",
        "category": "remote",
        "content_en": """- Remote work is permitted in emergency cases or up to 2 days per month with prior management approval.
- The employee must remain active and responsive during official shift hours (9:00 AM - 5:00 PM)."""
    },
    "10_BREAKS_AND_PRAYER": {
        "title_ar": "استراحة الغداء وأوقات الصلاة",
        "title_en": "Lunch & Prayer Break Policy",
        "category": "breaks",
        "content_en": """- Daily break duration is 1 hour, flexible between 01:00 PM and 02:30 PM."""
    },
    "11_OVERTIME_POLICY": {
        "title_ar": "ساعات العمل الإضافي (Overtime)",
        "title_en": "Overtime Policy",
        "category": "overtime",
        "content_en": """- Overtime work after 5:00 PM requires prior official management assignment, compensated financially or via compensatory time off."""
    },
    "12_TECHNICAL_ISSUES": {
        "title_ar": "معالجة الأعطال الفنية ونسيان تسجيل الدخول",
        "title_en": "Technical Issues & Missed Log Policy",
        "category": "support",
        "content_en": """- In case of portal technical malfunction or forgetting to log attendance, notify tech support or direct manager before 10:00 AM to register attendance manually and avoid unexcused absence."""
    },
    "13_DRESS_CODE_POLICY": {
        "title_ar": "قواعد اللباس والمظهر العام",
        "title_en": "Dress Code & Professional Appearance",
        "category": "dress_code",
        "content_en": """- All employees are required to maintain an elegant, neat, and proper professional appearance reflecting the company's high standards across all working days."""
    }
}


class PolicyChunk:
    def __init__(self, chunk_id: str, title_ar: str, title_en: str, category: str, content_ar: str, content_en: str = ""):
        self.chunk_id = chunk_id
        self.title_ar = title_ar
        self.title_en = title_en
        self.category = category
        self.content_ar = content_ar.strip()
        self.content_en = content_en.strip() if content_en else content_ar.strip()
        self.tokens = tokenize_text(f"{title_ar} {title_en} {content_ar} {content_en}")
        self.vector = compute_tf_vector(self.tokens)

    def to_dict(self) -> dict:
        return {
            "chunk_id": self.chunk_id,
            "title_ar": self.title_ar,
            "title_en": self.title_en,
            "category": self.category,
            "content": self.content_ar,
            "content_ar": self.content_ar,
            "content_en": self.content_en
        }

# Global list of indexed chunks
INDEXED_POLICY_CHUNKS: List[PolicyChunk] = []

def parse_and_index_policy_chunks() -> List[PolicyChunk]:
    """Parse policy.text by [SECTION: ...] into modular semantic chunks."""
    global INDEXED_POLICY_CHUNKS
    raw_text = get_policy_text()
    chunks = []
    
    if not raw_text:
        return []

    # Regex to split sections by [SECTION: NAME]
    pattern = r'\[SECTION:\s*([A-Za-z0-9_]+)\]([\s\S]*?)(?=(?:\[SECTION:|$))'
    matches = re.findall(pattern, raw_text)

    if matches:
        for section_key, section_body in matches:
            meta = SECTION_METADATA.get(section_key, {
                "title_ar": section_key,
                "title_en": section_key,
                "category": "general",
                "content_en": ""
            })
            chunk = PolicyChunk(
                chunk_id=section_key,
                title_ar=meta["title_ar"],
                title_en=meta["title_en"],
                category=meta["category"],
                content_ar=section_body.strip(),
                content_en=meta.get("content_en", "")
            )
            chunks.append(chunk)
    else:
        # Fallback if no section tags found
        chunk = PolicyChunk(
            chunk_id="00_MASTER_POLICY",
            title_ar="لائحة وسياسات الدوام العامة",
            title_en="General Attendance Policy",
            category="general",
            content_ar=raw_text.strip(),
            content_en=raw_text.strip()
        )
        chunks.append(chunk)

    INDEXED_POLICY_CHUNKS = chunks
    return chunks

# Initialize chunks on module load
parse_and_index_policy_chunks()

def get_all_policy_chunks() -> List[dict]:
    """Get all modular policy chunks as dictionaries."""
    if not INDEXED_POLICY_CHUNKS:
        parse_and_index_policy_chunks()
    return [c.to_dict() for c in INDEXED_POLICY_CHUNKS]

def retrieve_relevant_chunks(query: str, top_k: int = 2) -> List[dict]:
    """Retrieve top-K most relevant policy chunks for a given query."""
    if not INDEXED_POLICY_CHUNKS:
        parse_and_index_policy_chunks()

    query_tokens = tokenize_text(query)
    query_vector = compute_tf_vector(query_tokens)
    
    scored_chunks = []
    for chunk in INDEXED_POLICY_CHUNKS:
        sim = cosine_similarity(query_vector, chunk.vector)
        scored_chunks.append({
            "chunk_id": chunk.chunk_id,
            "title_ar": chunk.title_ar,
            "title_en": chunk.title_en,
            "category": chunk.category,
            "content": chunk.content_ar,
            "content_ar": chunk.content_ar,
            "content_en": chunk.content_en,
            "score": round(sim, 4)
        })

    # Sort by descending similarity score
    scored_chunks.sort(key=lambda x: x["score"], reverse=True)
    return scored_chunks[:top_k]

# ==============================================================================
# POLICY SEMANTIC BENCHMARK CLUSTERS FOR EXCUSE EVALUATION
# ==============================================================================

POLICY_VECTOR_CLUSTERS = {
    "unacceptable": {
        "chunk_id": "06_EXCUSES_CLASSIFICATION",
        "label_ar": "الأعذار المرفوضة قطئياً",
        "label_en": "Unacceptable Excuses",
        "recommendation": "REJECT",
        "badge_ar": "🔴 التقييم الذكي: يُرفض تلقائياً (مطابقة دلالية مع الأعذار غير المقبولة)",
        "badge_en": "🔴 AI Recommendation: Reject (Semantic Match - Unacceptable Excuse)",
        "explanation_ar": "نص العذر يطابق دلالياً الأعذار المرفوضة قطئياً في policy.text (مثل: صحيت متأخر، المنبه، نمت متأخر، أزمة الطريق، الظروف الشخصية).",
        "explanation_en": "Submitted excuse matches unacceptable excuses in policy.text (sleeping late, alarm clock, traffic congestion, personal reasons).",
        "benchmarks": [
            "صحيت متأخر", "نمت متأخر", "المنبه ما اشتغل", "المنبه غدر فيني", "المنبه ما رن", "نسيت اضبط المنبه",
            "أزمة الطريق", "ازدحام سير", "طريق ازمة", "عجقة سير", "أزمة سير خانقة", "ظروف شخصية", "مشوار شخصي", "نسيت الموعد"
        ]
    },
    "vehicle_breakdown": {
        "chunk_id": "06_EXCUSES_CLASSIFICATION",
        "label_ar": "أعطال المركبات ووسائل النقل",
        "label_en": "Vehicle & Transportation Breakdown",
        "recommendation": "APPROVE",
        "badge_ar": "🟢 التقييم الذكي: يُقبل تلقائياً (مطابقة دلالية مع بنود أعطال المركبات)",
        "badge_en": "🟢 AI Recommendation: Approve (Semantic Match - Vehicle Breakdown)",
        "explanation_ar": "نص العذر يتطابق دلالياً مع بند الأعطال المفاجئة للمركبات ووسائل النقل والمقبولة حسب policy.text.",
        "explanation_en": "Excuse matches vehicle/transport breakdown clause per policy.text.",
        "benchmarks": [
            "بنشرت عجلة السيارة على الجسر", "بنشرت السيارة", "بنشر عجل السيارة", "خربت السيارة بالشارع", "عطل بالمركبة",
            "عطل مفاجئ بالسيارة", "تعطلت الحافلة", "وسيلة النقل خربت", "البنزين خلص بالسيارة", "بطارية السيارة فضيت", "عطل فني بالسيارة"
        ]
    },
    "traffic_accident": {
        "chunk_id": "05_PROOF_REQUIREMENTS",
        "label_ar": "حوادث السير والمرور",
        "label_en": "Traffic Accident",
        "recommendation": "REQUIRE_PROOF",
        "badge_ar": "🟡 التقييم الذكي: يتطلب إرفاق الكروكة أو صورة الحادث (شرط الإثبات)",
        "badge_en": "🟡 AI Recommendation: Require Police Report / Kroka Proof",
        "explanation_ar": "نص العذر يتطابق دلالياً مع أعذار حوادث السير. بناءً على شرط الإثبات بـ policy.text يتطلب إرفاق تقرير الشرطة (الكروكة) أو صورة الحادث.",
        "explanation_en": "Traffic accident excuse matches policy.text. Requires Kroka/Police report proof.",
        "benchmarks": [
            "سويت حادث بالسيارة", "حادث سير مروري", "انصدمت السيارة", "صدمت الرصيف بالسيارة", "سيارة صدمتني بالطريق",
            "حادث بالشارع", "كروكة حادث", "تقرير شرطة للحادث", "تصادم مروري"
        ],
        "proof_keywords": ["كروكة", "كروكه", "تقرير حادث", "صورة الحادث", "صوره للحادث", "اثبات", "إثبات", "تقرير شرطة"]
    },
    "health_emergency": {
        "chunk_id": "05_PROOF_REQUIREMENTS",
        "label_ar": "الطوارئ والظروف الصحية",
        "label_en": "Medical & Health Emergency",
        "recommendation": "REQUIRE_PROOF",
        "badge_ar": "🟡 التقييم الذكي: يتطلب إرفاق التقرير الطبي الرسمي (شرط الإثبات)",
        "badge_en": "🟡 AI Recommendation: Require Official Medical Report Proof",
        "explanation_ar": "نص العذر يتطابق دلالياً مع الظروف الصحية والطوارئ الطبية. بناءً على شرط الإثبات بـ policy.text يتطلب إرفاق تقرير طبي رسمي.",
        "explanation_en": "Medical emergency excuse matches policy.text. Requires official medical report proof.",
        "benchmarks": [
            "دخت الصبح وأبوي وداني المستشفى", "وعكة صحية مفاجئة", "تعبت الصبح", "طوارئ المستشفى", "طبيب المستشفى",
            "مرض طارئ", "تقرير طبي رسمي", "علاج بالطوارئ", "إجازة مرضية", "عملية جراحية طارئة"
        ],
        "proof_keywords": ["تقرير", "تقرير طبي", "روشتة", "علاج", "إجازة مرضية", "اجازة مرضية", "وصفة طبيب"]
    },
    "weather_emergency": {
        "chunk_id": "06_EXCUSES_CLASSIFICATION",
        "label_ar": "الظروف الجوية القاهرة",
        "label_en": "Weather Emergency & Force Majeure",
        "recommendation": "APPROVE",
        "badge_ar": "🟢 التقييم الذكي: يُقبل تلقائياً (مطابقة دلالية مع الظروف الجوية القاهرة)",
        "badge_en": "🟢 AI Recommendation: Approve (Semantic Match - Weather Emergency)",
        "explanation_ar": "نص العذر يتطابق دلالياً مع بند الظروف الجوية القاهرة والأمطار/الثلوج المقبولة تلقائياً حسب policy.text.",
        "explanation_en": "Excuse matches weather emergency and force majeure clause per policy.text.",
        "benchmarks": [
            "أمطار غزيرة وسيول بالشارع", "ثلوج وانغلاق الطريق", "عاصفة جوية قاهرة", "ظروف جوية سيئة جداً",
            "انقطاع الطريق بسبب المطر", "انجماد وثلوج"
        ]
    }
}

# Vector Index Initialization for Clusters
INDEXED_CLUSTERS = {}
for cluster_key, cluster_data in POLICY_VECTOR_CLUSTERS.items():
    combined_text = " ".join(cluster_data["benchmarks"])
    tokens = tokenize_text(combined_text)
    INDEXED_CLUSTERS[cluster_key] = compute_tf_vector(tokens)

def evaluate_semantic_excuse(reason: str, lateness_mins: int = 0, has_attachment: bool = False) -> dict:
    """
    Evaluate employee excuse text using Semantic Vector Cosine Similarity against Policy Chunks and Clusters.
    """
    reason_clean = (reason or "").strip()
    if not reason_clean:
        return {
            "recommendation": "PENDING_REVIEW",
            "semantic_match_score": 0.0,
            "badge_ar": "⏳ التقييم الذكي: عذر فارغ يتطلب المراجعة",
            "badge_en": "⏳ AI Recommendation: Empty excuse pending review",
            "explanation_ar": "لم يتم إدخال نص العذر.",
            "explanation_en": "No excuse reason text provided."
        }
        
    query_tokens = tokenize_text(reason_clean)
    query_vector = compute_tf_vector(query_tokens)
    
    # Compute similarity against all clusters
    scores = {}
    for cluster_key, cluster_vector in INDEXED_CLUSTERS.items():
        sim = cosine_similarity(query_vector, cluster_vector)
        scores[cluster_key] = sim

    # Direct Keyword Overrides for High Precision
    reason_lower = reason_clean.lower()
    
    # Check unacceptable direct keywords
    unacceptable_direct = ["صحيت", "نمت", "المنبه", "منبه", "أزمة", "ازمة", "ازدحام", "شخصية", "شخصيه"]
    if any(k in reason_lower for k in unacceptable_direct):
        scores["unacceptable"] += 0.8
        
    # Check vehicle breakdown direct keywords
    if any(k in reason_lower for k in ["بنشر", "بشرت", "خربت", "عطل", "وسيلة نقل", "سيارة", "سياره", "حافلة", "حافله", "بطارية"]):
        scores["vehicle_breakdown"] += 0.6
        
    # Check accident direct keywords
    if any(k in reason_lower for k in ["حادث", "انصدمت", "صدمت", "تصادم", "كروكة", "كروكه"]):
        scores["traffic_accident"] += 0.7

    # Check health direct keywords
    if any(k in reason_lower for k in ["مرض", "صحي", "صحية", "طبيب", "مستشفى", "طوارئ", "تعبت", "دخت", "وعكة"]):
        scores["health_emergency"] += 0.7

    # Find highest scoring cluster
    top_cluster_key = max(scores, key=scores.get)
    max_score = scores[top_cluster_key]
    
    # Convert raw score to confidence percentage (capped at 98.5%)
    confidence_pct = min(round((max_score * 120) + 40, 1), 98.5) if max_score > 0.05 else 50.0
    
    cluster_info = POLICY_VECTOR_CLUSTERS[top_cluster_key]
    rec = cluster_info["recommendation"]
    
    # Retrieve the corresponding policy chunk for grounding
    relevant_chunks = retrieve_relevant_chunks(reason_clean, top_k=1)
    matched_chunk = relevant_chunks[0] if relevant_chunks else None
    
    # Special Proof Check for Accidents & Health (Checked via text keywords OR uploaded attachment)
    if top_cluster_key == "traffic_accident":
        has_proof = has_attachment or any(p in reason_lower for p in cluster_info["proof_keywords"])
        if has_proof:
            rec = "APPROVE"
            badge_ar = f"🟢 التقييم الذكي: يُقبل تلقائياً (مطابقة دلالية {confidence_pct}% - حوادث سير مع إثبات الكروكة/الصورة)"
            badge_en = f"🟢 AI Recommendation: Approve ({confidence_pct}% Semantic Match - Traffic Accident with Proof Attachment)"
            exp_ar = f"نص العذر مطابق دلالياً ({confidence_pct}%) لأعذار حوادث السير ومرفق بإثبات الكروكة/الصورة كالمطلوب بـ [SECTION: 05_PROOF_REQUIREMENTS]."
            exp_en = f"Excuse matches traffic accident policy ({confidence_pct}%) with Kroka/accident photo attached per [SECTION: 05_PROOF_REQUIREMENTS]."
        else:
            badge_ar = f"🟡 التقييم الذكي: يتطلب إرفاق الكروكة أو صورة الحادث (مطابقة دلالية {confidence_pct}%)"
            badge_en = f"🟡 AI Recommendation: Require Kroka/Photo Proof ({confidence_pct}% Semantic Match)"
            exp_ar = cluster_info["explanation_ar"]
            exp_en = cluster_info["explanation_en"]
            
    elif top_cluster_key == "health_emergency":
        has_proof = has_attachment or any(p in reason_lower for p in cluster_info["proof_keywords"])
        if has_proof:
            rec = "APPROVE"
            badge_ar = f"🟢 التقييم الذكي: يُقبل تلقائياً (مطابقة دلالية {confidence_pct}% - عذر صحي مع تقرير طبي)"
            badge_en = f"🟢 AI Recommendation: Approve ({confidence_pct}% Semantic Match - Health Emergency with Medical Report)"
            exp_ar = f"نص العذر مطابق دلالياً ({confidence_pct}%) للأعذار الصحية ومرفق بالتقرير الطبي كما يقتضي [SECTION: 05_PROOF_REQUIREMENTS]."
            exp_en = f"Excuse matches medical policy ({confidence_pct}%) with medical report attached per [SECTION: 05_PROOF_REQUIREMENTS]."
        else:
            badge_ar = f"🟡 التقييم الذكي: يتطلب إرفاق التقرير الطبي الرسمي (مطابقة دلالية {confidence_pct}%)"
            badge_en = f"🟡 AI Recommendation: Require Medical Report ({confidence_pct}% Semantic Match)"
            exp_ar = cluster_info["explanation_ar"]
            exp_en = cluster_info["explanation_en"]
    else:
        badge_ar = cluster_info["badge_ar"].replace("مطابقة دلالية", f"مطابقة دلالية {confidence_pct}%")
        badge_en = cluster_info["badge_en"]
        exp_ar = cluster_info["explanation_ar"]
        exp_en = cluster_info["explanation_en"]


    # Grace Period Fallback for short delays (<= 15 mins) if not explicitly unacceptable
    if top_cluster_key != "unacceptable" and lateness_mins <= 15 and rec != "APPROVE":
        rec = "APPROVE"
        badge_ar = f"🟢 التقييم الذكي: يُقبل تلقائياً (ضمن فترة السماح 15 دقيقة - مطابقة {confidence_pct}%)"
        badge_en = f"🟢 AI Recommendation: Approve (Within 15m Grace Period)"

    return {
        "recommendation": rec,
        "semantic_match_score": confidence_pct,
        "matched_cluster": top_cluster_key,
        "matched_chunk_id": matched_chunk["chunk_id"] if matched_chunk else cluster_info.get("chunk_id", "06_EXCUSES_CLASSIFICATION"),
        "matched_chunk_title": matched_chunk["title_ar"] if matched_chunk else cluster_info["label_ar"],
        "cluster_label_ar": cluster_info["label_ar"],
        "cluster_label_en": cluster_info["label_en"],
        "badge_ar": badge_ar,
        "badge_en": badge_en,
        "explanation_ar": exp_ar,
        "explanation_en": exp_en
    }


# ==============================================================================
# HIGH-PRECISION QUESTION ANSWERING WITH CITATIONS & SOURCES
# ==============================================================================

def answer_qa_with_sources(
    question: str, 
    user_email: Optional[str] = None, 
    user_role: str = "guest", 
    user_logs_summary: Optional[dict] = None, 
    team_stats_summary: Optional[dict] = None,
    lang: str = "ar",
    chat_history: Optional[List[Dict[str, str]]] = None
) -> dict:
    """
    Generate a concise, direct, question-targeted answer for any policy or attendance question,
    accompanied by verifiable sources and citations from policy.text and database records.
    """
    q_clean = (question or "").strip()
    if not q_clean:
        return {
            "success": False,
            "error": "السؤال فارغ، يرجى إدخال نص السؤال." if lang == "ar" else "Question is empty.",
            "question": "",
            "answer": "",
            "sources": []
        }

    q_lower = q_clean.lower()
    q_norm = normalize_arabic(q_clean)
    
    # Detect language
    is_ar = lang.lower() == "ar" or bool(re.search(r'[\u0600-\u06FF]', q_clean))
    
    # Conversational History Context Resolution for Follow-ups (e.g., "في الشهر؟", "واذا تأخرت؟", "كم رصيدها؟", "كيف ابعثو")
    if chat_history and isinstance(chat_history, list) and len(chat_history) > 0:
        last_turn = chat_history[-1] if isinstance(chat_history[-1], dict) else {}
        last_user_msg = normalize_arabic(last_turn.get("content", ""))
        last_bot_msg = normalize_arabic(chat_history[-2].get("content", "") if len(chat_history) >= 2 and isinstance(chat_history[-2], dict) else "")
        
        # If user asks short elliptical question about timeframe (Arabic & English)
        if any(k in q_norm for k in ["في الشهر", "بالشهر", "شهريا"]) or any(k in q_lower for k in ["in a month", "per month", "monthly", "in month"]):
            q_norm = f"كم ساعات العمل في الشهر {q_norm}"
        elif any(k in q_norm for k in ["في الاسبوع", "بالاسبوع", "اسبوعيا"]) or any(k in q_lower for k in ["in a week", "per week", "weekly", "in week"]):
            q_norm = f"كم ساعات العمل في الاسبوع {q_norm}"
        elif (any(k in q_norm for k in ["في اليوم", "باليوم", "يوميا"]) or any(k in q_lower for k in ["in a day", "per day", "daily"])) and not any(k in q_norm for k in ["اجازه", "عذر"]):
            q_norm = f"كم ساعات العمل في اليوم {q_norm}"
        elif any(k in q_norm for k in ["واذا تاخرت", "اذا تاخرت", "لو تاخرت", "والتاخير"]) or any(k in q_lower for k in ["what if i am late", "and if late", "if late"]):
            q_norm = f"عقوبة وخصم التاخير {q_norm}"
        elif any(k in q_norm for k in ["والمرضيه", "ومرضيه", "والاجازات", "ورصيدها"]) or any(k in q_lower for k in ["and sick leaves", "vacation balance"]):
            q_norm = f"رصيد الاجازات المرضيه والسنويه {q_norm}"
        elif any(k in q_norm for k in ["كيف ابعث", "كيف ابعثو", "كيف ابعثه", "كيف ارسلو", "كيف ارفعو", "كيف اسلمو", "وين ابعثو", "وين ارفعو", "وين احطو"]) or any(k in q_lower for k in ["how to send it", "where to send it", "how do i send it", "how to upload it"]):
            q_norm = f"كيف ابعث التقرير والعذر {q_norm}"
        elif any(k in q_norm for k in ["لمين", "عند مين", "مين بستلم"]) or any(k in q_lower for k in ["who to send", "who receives", "who do i send", "to whom"]):
            q_norm = f"لمين ابعثهن {q_norm}"

    sources = []
    answer = ""
    engine_name = "NexusLink Grounded Hybrid RAG"

    # 0. Greetings & Small Talk ("مرحبا", "اهلين", "السلام عليكم", "صباح الخير", "مساء الخير", "هلا", "هاي")
    is_greeting_query = any(k == q_norm or q_norm.startswith(k + " ") or q_norm.endswith(" " + k) for k in [
        "مرحبا", "مرحبتين", "اهلين", "اهل", "اهلا", "أهلا", "أهلين", "هلا", "هلا والله", "يا هلا",
        "السلام عليكم", "سلام عليكم", "سلام", "صباح الخير", "صباح النور", "صباح الورد",
        "مساء الخير", "مساء النور", "مساء الورد", "يعطيك العافيه", "يعطيك العافية", "هاي", "هلو",
        "hello", "hi", "hey", "good morning", "good evening", "greetings"
    ]) and not any(k in q_norm for k in ["عذر", "تاخير", "تاخر", "غياب", "اجازه", "راتب", "ساعه", "ساعات", "دوام", "تقرير", "كروكه", "خروج", "دخول", "خصم", "سماح", "جمعه", "خميس", "احد"])

    # 1. Identity & Profile Query (e.g. "شو اسمي", "مين انا", "حسابي", "ايميلي")
    is_identity_query = any(k in q_norm for k in [
        "شو اسمي", "ايش اسمي", "مين انا", "شو حسابي", "شو ايميلي", "ايميلي",
        "بروفيلي", "معلوماتي", "بياناتي", "who am i", "what is my name", "my profile", "my email"
    ]) or any(k in q_lower for k in ["شو أسمي", "مين أنا"])

    # 2. Cumulative Personal Attendance / Absences Count Query (e.g. "كم غياب عندي", "كم يوم غبت", "كم مرة تاخرت")
    is_cumulative_attendance_query = any(k in q_norm for k in [
        "كم غياب عندي", "كم غياب", "كم يوم غبت", "غياباتي", "كم مره تاخرت",
        "كم تاخير عندي", "كم يوم داومت", "سجل دوامي الاجمالي", "رصيد غيابي",
        "my absences", "how many absences", "how many times late", "my attendance history"
    ])

    # 3. How to Submit an Excuse / Medical Report / Proof Attachment / Attached Pronouns ("كيف ابعثو", "وين ابعث التقرير")
    is_how_to_submit_excuse = any(k in q_norm for k in [
        "كيف اقدم عذر", "طريقه تقديم العذر", "طريقه تقديم عذر", "وين اقدم عذر", "كيف اعبي العذر",
        "كيف اعبي عذر", "كيف اسجل عذر", "خطوات تقديم العذر", "خطوات تقديم عذر", "بدي اقدم عذر",
        "كيف ابعث التقرير", "كيف ابعث التقرير الطبي", "وين ابعث التقرير", "وين ابعث التقرير الطبي",
        "وين ارفع التقرير", "وين ارفع التقرير الطبي", "وين احط التقرير", "وين احط التقرير الطبي",
        "كيف ارفق التقرير", "كيف ارفع التقرير", "كيف ارفق الكروكه", "كيف ابعث الكروكه",
        "وين ارفع الكروكه", "وين ابعث الكروكه", "وين احط الكروكه",
        "وين ارفع الملف", "كيف ارفق ملف", "كيف ارفق صوره", "وين ارفق", "وين ارفع", "وين اسلم",
        "وين احط", "كيف اسلم التقرير", "كيف ارفق", "كيف ابعث عذر", "وين ابعث",
        "كيف ابعثو", "كيف ابعثه", "كيف ابعثها", "كيف ابعثهن", "كيف ارسلو", "كيف ارسله",
        "كيف ارفعو", "كيف ارفعه", "كيف اقدمو", "كيف اقدمه", "كيف احطو", "كيف احطه",
        "وين ابعثو", "وين ابعثه", "وين ارفعو", "وين ارفعه", "وين احطو", "وين احطه",
        "كيف اسلمو", "كيف اسلمه", "كيف اوديه", "كيف اودي"
    ]) or (
        any(k in q_norm for k in ["كيف", "وين", "طريقه", "طريقة", "خطوات"]) and
        any(k in q_norm for k in ["ابعث", "ارفع", "ارسل", "ارفق", "احط", "اسلم", "اودي", "اعبي", "اقدم"]) and
        any(k in q_norm for k in ["تقرير", "كروك", "عذر", "ملف", "صور", "اثبات", "اوراق", "ورق", "مرفق", "ابعثو", "ارفعو", "ارسلو", "احطو", "اسلمو", "اوديه"])
    ) or any(k in q_lower for k in [
        "how to submit", "where to submit", "how to send excuse", "how to send report", "where to send report", "where to upload report",
        "how to attach", "how to upload", "steps to submit", "how do i submit", "how to send it", "where to send it", "how do i send it", "how to upload it"
    ])

    # 3.1 Who Receives the Excuse / Who to send to ("لمين ابعثهن", "لمين ابعث", "مين بشوفهن", "مين بستلم")
    is_who_receives_excuse = any(k in q_norm for k in [
        "لمين ابعثهن", "لمين ابعث", "لمين ارسل", "لمين اودي", "لمين اسلم", "لمين اعطي", "لمين ابعثه", "لمين ابعثها", "لمين ابعثو",
        "لمين بروح الطلب", "لمين الطلب بروح", "مين بشوفهن", "مين بشوف الطلب", "مين بستلم", "مين بستلمهن", "مين بستلمو",
        "مين بوافق", "مين المدير الي بوافق", "مين بعتمد", "مين بدقق", "مين براجع"
    ]) or any(k in q_lower for k in [
        "who to send", "who receives", "who approves", "who checks", "who do i send", "to whom", "who to send it to"
    ])

    # 3.2 Excuse Status Check / Response Time ("متى بردوا علي", "كيف اعرف اذا انقبل", "وين النتيجة")
    is_status_check_query = any(k in q_norm for k in [
        "متي بردو", "متي بردوا", "كيف اعرف اذا انقبل", "كيف اعرف اذا انرفض", "وين بشوف النتيجه",
        "وين الاقي الرد", "كيف اتابع الطلب", "حاله العذر", "نتيجه العذر"
    ]) or any(k in q_lower for k in [
        "how to check excuse", "excuse status", "how do i know if accepted", "how to track excuse"
    ])

    # 3.3 Supported Attachment Formats ("شو نوع الملفات", "ايش الصيغ المقبولة")
    is_file_types_query = any(k in q_norm for k in [
        "نوع الملفات", "صيغه التقرير", "صيغه الكروكه", "حجم الصوره", "شو نوع الملف", "شو الصيغه"
    ]) or any(k in q_lower for k in [
        "supported file types", "file formats", "attachment format", "file types"
    ])

    # 3.4 How to Check-In & Attendance ("كيف اسجل دخول", "وين البصمة", "كيف اسجل حضور")
    is_how_to_checkin_query = any(k in q_norm for k in [
        "كيف اسجل دخول", "وين البصمه", "كيف اسجل حضور", "وين زر الدخول", "كيف ابصم", "كيف اثبت دوامي"
    ]) or any(k in q_lower for k in [
        "how to check in", "where to check in", "how to log attendance", "how to check-in"
    ])

    # 3.5 How to Check-Out ("كيف اسجل خروج", "كيف اسجل انصراف", "وين زر الخروج")
    is_how_to_checkout_query = any(k in q_norm for k in [
        "كيف اسجل خروج", "كيف اسجل انصراف", "وين زر الخروج", "وين زر الانصراف"
    ]) or any(k in q_lower for k in [
        "how to check out", "where to check out", "how to log departure", "how to check-out"
    ])

    # 3.6 How to Request Leave ("كيف اطلب اجازة", "كيف اقدم على اجازة")
    is_how_to_request_leave = any(k in q_norm for k in [
        "كيف اطلب اجازه", "كيف اقدم علي اجازه", "كيف اقدم اجازه", "طريقه طلب الاجازه"
    ]) or any(k in q_lower for k in [
        "how to request leave", "how to apply for leave", "how to take leave", "how to request vacation"
    ])

    # 3.7 Leave Balance & Allowed Days Off ("كم اجازه الي في الشهر", "كم مسموحلي اعطل", "كم يوم عطلة معي")
    is_leave_balance_query = any(k in q_norm for k in [
        "كم اجازه", "كم إجازة", "كم اجازات", "كم إجازات", "كم مسموحلي اعطل", "كم مسموح لي اعطل",
        "كم بقدر اعطل", "كم يوم اعطل", "كم يوم عطلة", "كم يوم عطله", "كم يوم اغيب", "كم مسموحلي اغيب",
        "كم يوم مسموح", "كم اجازه الي", "كم اجازة لي", "رصيد اجازاتي", "رصيد إجازاتي", "رصيد الاجازات",
        "اجازاتي السنوية", "اجازاتي السنويه", "كم يوم بالسنة اعطل", "كم يوم بالسنه اعطل",
        "كم اجازه بالشهر", "كم اجازه في الشهر", "كم إجازة بالشهر", "كم إجازة في الشهر"
    ]) or any(k in q_lower for k in [
        "how many leaves", "how many leave days", "how many days off", "leave balance", "vacation balance",
        "how many days can i take off", "how many days off per month", "how many leaves per year"
    ])

    # 4. Planning to be Absent / If I take a day off / "لو عطلت شو اعمل"
    is_planning_absence_query = not is_leave_balance_query and (any(k in q_norm for k in [
        "لو عطلت شو", "لو غبت شو", "لو غبت شو اعمل", "لو غبت شو اسوي", "لو غبت شو بصير",
        "بدي اعطل", "بدي اغيب", "اذا بدي اغيب", "اذا بدي اعطل", "اذا غبت شو", "اذا عطلت شو",
        "لو ما جيت شو", "what if i am absent", "what if i take a day off", "what to do if absent"
    ]))

    # 6. Team / Admin Workforce Intelligence Query
    is_team_query = any(k in q_norm for k in [
        "مين غايب", "مين متاخر", "مين مداوم", "مين موجود", "ملخص الفريق", "احصائيات الدوام",
        "كادر الموظفين", "من الموظفين", "الموظفين", "الموظفون",
        "who is absent", "who is late", "who is present", "team summary", "roster", "all employees"
    ])

    # 5. Today's Personal Attendance / "Am I late today or not?" (Strictly Personal)
    is_today_attendance_query = not is_team_query and (
        (any(k in q_norm for k in ["اليوم", "today"]) and any(k in q_norm for k in ["متاخر انا", "انا متاخر", "داومت", "حضوري", "دوامي", "سجلي", "متاخر", "متأخر"])) or
        any(k in q_norm for k in ["هل انا متاخر", "متاخر انا", "متاخر ولا", "اليوم متاخر انا", "am i late"])
    )

    # 7. Working Days Query
    is_working_days_query = any(k in q_norm for k in [
        "ايام الدوام", "ايام العمل", "ايام الشغل", "شو الايام", "شو ايام", "ماهي ايام", "ما هي ايام",
        "اي ايام", "ايام الاسبوع", "كم يوم بالاسبوع", "كم يوم في الاسبوع", "كم يوم دوام", "جدول الدوام",
        "مواعيد الايام", "ايام الدوام الرسمي", "working days", "work days", "what days", "work schedule", "days of work"
    ]) or (any(k in q_norm for k in ["الدوام", "العمل", "الشغل"]) and any(k in q_norm for k in ["اي ايام", "ايام شو", "متي الايام", "ايام الاسبوع"]))

    # Fast Cache Check for Static / Policy Inquiries
    cache_key = f"{q_clean.lower()}_{lang}_{user_role}"
    if not (is_greeting_query or is_identity_query or is_cumulative_attendance_query or is_today_attendance_query or is_team_query or is_working_days_query or is_who_receives_excuse or (chat_history and len(chat_history) > 0)):
        if cache_key in _QA_MEMORY_CACHE:
            return dict(_QA_MEMORY_CACHE[cache_key])

    # --- EXECUTE INTENT RESOLUTION ---

    # 0. Friendly Greeting Query
    if is_greeting_query:
        u_name = (user_logs_summary.get("name") if user_logs_summary else None)
        name_str = f" {u_name}" if u_name else ""
        if any(k in q_norm for k in ["صباح الخير", "صباح النور", "صباح الورد", "good morning"]):
            greet_ar = f"صباح الخير والنشاط{name_str}! ☀️"
            greet_en = f"Good morning{name_str}! ☀️"
        elif any(k in q_norm for k in ["مساء الخير", "مساء النور", "مساء الورد", "good evening"]):
            greet_ar = f"مساء الخير والبركة{name_str}! 🌙"
            greet_en = f"Good evening{name_str}! 🌙"
        elif any(k in q_norm for k in ["السلام عليكم", "سلام عليكم"]):
            greet_ar = f"وعليكم السلام ورحمة الله وبركاته{name_str}! 🌿"
            greet_en = f"Peace be upon you{name_str}! 🌿"
        elif any(k in q_norm for k in ["يعطيك العافيه", "يعطيك العافية"]):
            greet_ar = f"الله يعافيك ويسعدك{name_str}! ✨"
            greet_en = f"Thank you and welcome{name_str}! ✨"
        else:
            greet_ar = f"أهلاً وسهلاً بك{name_str}! 👋"
            greet_en = f"Hello and welcome{name_str}! 👋"

        if is_ar:
            answer = f"{greet_ar} أنا مساعدك الذكي في منصة **NexusLink**. كيف يمكنني مساعدتك اليوم بخصوص الدوام، تسجيل الحضور، أو تقديم الأعذار والإجازات؟"
        else:
            answer = f"{greet_en} I am your **NexusLink** Smart Assistant. How can I assist you today with attendance, check-in, or excuse/leave requests?"

        sources.append({
            "document": "nexuslink_assistant",
            "section_id": "00_GREETING",
            "section_title": "مساعد الموظفين التفاعلي",
            "confidence": "100%",
            "exact_snippet": "الترحيب بالموظف وتقديم المساعدة الفورية بخصوص نظام الحضور والغياب وسياسات الشركة."
        })

    # 1. Identity Query
    elif is_identity_query:
        u_name = (user_logs_summary.get("name") if user_logs_summary else None) or "الموظف"
        u_email = (user_logs_summary.get("email") if user_logs_summary else None) or user_email or "غير مسجل"
        u_role_ar = "مدير نظام (Admin)" if user_role == "admin" else ("موظف رسمي" if user_role == "employee" else "مستخدم")
        if is_ar:
            answer = f"أنت مسجل في النظام باسم: **{u_name}**، البريد الإلكتروني: `{u_email}`، بصلاحية: **{u_role_ar}**."
        else:
            answer = f"You are logged in as: **{u_name}**, Email: `{u_email}`, Role: **{user_role.capitalize()}**."

        sources.append({
            "document": "nexuslink.db",
            "table": "user3",
            "record_type": "User Profile Identity",
            "confidence": "100%",
            "exact_snippet": f"User: {u_name} <{u_email}>, Role: {user_role}"
        })

    # 2. Cumulative Personal Attendance
    elif is_cumulative_attendance_query:
        pres_days = user_logs_summary.get("present_days", 0) if user_logs_summary else 0
        abs_days = user_logs_summary.get("absent_days", 0) if user_logs_summary else 0
        l_count = user_logs_summary.get("late_count", 0) if user_logs_summary else 0
        if is_ar:
            answer = f"إحصائيات سجلك الشخصي التراكمي:\n- 🟢 أيام الحضور: **{pres_days} يوم**\n- 🔴 أيام الغياب: **{abs_days} يوم**\n- ⏰ مرات التأخير (>09:15 ص): **{l_count} مرات**"
        else:
            answer = f"Your cumulative attendance summary:\n- 🟢 Present Days: **{pres_days} Days**\n- 🔴 Absent Days: **{abs_days} Days**\n- ⏰ Lateness Instances (>09:15 AM): **{l_count} Times**"

        sources.append({
            "document": "nexuslink.db",
            "table": "attendance",
            "record_type": "Personal Cumulative Attendance",
            "confidence": "100%",
            "exact_snippet": f"Present: {pres_days}, Absent: {abs_days}, Late: {l_count}"
        })

    # 3. Team / Admin Workforce Intelligence
    elif is_team_query:
        if user_role == "admin":
            if team_stats_summary:
                p_cnt = team_stats_summary.get("present_count", 0)
                tot = team_stats_summary.get("total_count", 0)
                abs_cnt = team_stats_summary.get("absent_count", 0)
                late_cnt = team_stats_summary.get("late_count", 0)
                sev_cnt = team_stats_summary.get("severe_late_count", 0)
                
                if is_ar:
                    answer = f"إحصائيات دوام اليوم: حضر {p_cnt} من أصل {tot} موظفاً، الغياب {abs_cnt}، المتأخرين (>09:15) {late_cnt} موظفين، وتأخير شديد (>10:00) {sev_cnt} حالات."
                else:
                    answer = f"Today's stats: {p_cnt}/{tot} present, {abs_cnt} absent, {late_cnt} late (>09:15), and {sev_cnt} severe lateness (>10:00)."
                
                sources.append({
                    "document": "nexuslink.db",
                    "table": "attendance & user3",
                    "record_type": "Admin Team Workforce Intelligence",
                    "confidence": "100%",
                    "exact_snippet": f"Present: {p_cnt}/{tot}, Absent: {abs_cnt}, Late: {late_cnt}, Severe Lateness: {sev_cnt}"
                })
            else:
                if is_ar:
                    answer = "يمكنك مراجعة لوحة تحكم الإدارة للاطلاع على التفاصيل الكاملة لحضور وغياب الموظفين اليوم."
                else:
                    answer = "You can inspect the Admin Dashboard for full real-time attendance breakdown."
                sources.append({
                    "document": "nexuslink.db",
                    "table": "attendance",
                    "record_type": "Workforce Logs",
                    "confidence": "95%",
                    "exact_snippet": "Live attendance records"
                })
        else:
            if is_ar:
                answer = "🔒 تنبيه أمني: سجلات دوام وغياب كادر الموظفين الشاملة مخصصة لحسابات الإدارة (Admin) فقط."
            else:
                answer = "🔒 Security Notice: Team-wide attendance rosters are restricted to Admin accounts only."
            
            sources.append({
                "document": "nexuslink_rbac",
                "policy": "Role-Based Access Control",
                "confidence": "100%",
                "exact_snippet": "Access to all employees roster is restricted to authorized admin users."
            })

    # 4. Who Receives the Excuse / Medical Report ("لمين ابعثهن", "لمين ارسل", "مين بشوفهن", "مين بستلم")
    elif is_who_receives_excuse:
        if is_ar:
            answer = "يتم إرسال العذر والتقرير والمرفقات مباشرة عبر المنصة إلى **مديرك المباشر** و**قسم الموارد البشرية (HR)** للاطلاع والمراجعة والاعتماد الفوري، ولا حاجة لتسليمه يدوياً أو ورقياً."
        else:
            answer = "The excuse, report, and attachments are submitted directly via the platform to your direct manager and the HR department for immediate review and approval, with no manual paperwork required."

        sources.append({
            "document": "nexuslink_platform",
            "section_id": "04_EXCUSE_WORKFLOW",
            "section_title": "نظام سير طلبات الأعذار والاعتماد الإداري",
            "confidence": "99.5%",
            "exact_snippet": "تصل طلبات الأعذار والتقارير الطبية والكروكات مباشرة عبر النظام إلى المدير المباشر وقسم HR للمراجعة والاعتماد الفوري."
        })

    # 4.1 How to Submit an Excuse / Medical Report / Attachments
    elif is_how_to_submit_excuse:
        if is_ar:
            answer = "لإرسال العذر أو التقرير الطبي/الكروكة عبر المنصة:\n1. اضغط على زر '📝 تقديم عذر' في أعلى لوحة التحكم.\n2. اكتب سبب التأخير أو الغياب بدقة.\n3. اضغط على زر '📎 إرفاق ملف' وارفع وثيقة الإثبات (تقرير طبي أو كروكة أو ملف PDF).\n4. أرسل الطلب خلال ساعات الدوام الرسمي (9:00 ص - 5:00 م) ليتم تدقيقه واعتماده مباشرة."
        else:
            answer = "To submit an excuse or medical/accident report on the portal:\n1. Click the '📝 Submit Excuse' button in your dashboard.\n2. Enter the exact reason for delay/absence.\n3. Click '📎 Attach File' to upload proof (medical report, accident Kroka, or PDF).\n4. Submit during shift hours (9:00 AM - 5:00 PM) for direct review and approval."

        sources.append({
            "document": "policy.text",
            "section_id": "04_EXCUSE_TIME_WINDOW",
            "section_title": SECTION_METADATA["04_EXCUSE_TIME_WINDOW"]["title_ar" if is_ar else "title_en"],
            "confidence": "99.0%",
            "exact_snippet": "- يجب تقديم طلب العذر خلال فترة الدوام الرسمي حصراً من الساعة 9:00 صباحاً إلى الساعة 5:00 مساءً من نفس يوم التأخير."
        })
        sources.append({
            "document": "policy.text",
            "section_id": "05_PROOF_REQUIREMENTS",
            "section_title": SECTION_METADATA["05_PROOF_REQUIREMENTS"]["title_ar" if is_ar else "title_en"],
            "confidence": "98.0%",
            "exact_snippet": "- الأعذار الصحية: تقرير طبي رسمي. - حوادث السير: كروكة أو صورة الحادث."
        })

    # 4.2 Excuse Status Check / Response Time
    elif is_status_check_query:
        if is_ar:
            answer = "تظهر نتيجة وحالة طلبك (🟢 مقبول / 🟡 قيد المراجعة / 🔴 مرفوض) فوراً وتلقائياً في جدول **'أعذاري'** في لوحة التحكم الخاصة بك."
        else:
            answer = "Your excuse request status (Approved / Under Review / Rejected) is displayed in real-time in the 'My Excuses' table on your dashboard."

        sources.append({
            "document": "nexuslink_platform",
            "section_id": "04_EXCUSE_STATUS",
            "section_title": "متابعة حالة طلبات الأعذار",
            "confidence": "99.0%",
            "exact_snippet": "تُحدث حالة العذر تلقائياً في جدول أعذاري بمجرد اتخاذ القرار من الإدارة."
        })

    # 4.3 Supported File Types
    elif is_file_types_query:
        if is_ar:
            answer = "تدعم المنصة رفع المستندات الطبية وصور الكروكة بصيغ: (JPG, PNG, PDF) بحجم أقصى 5 ميجابايت للملف."
        else:
            answer = "The platform supports uploading medical reports and accident photos in (JPG, PNG, PDF) formats up to 5MB."

        sources.append({
            "document": "nexuslink_platform",
            "section_id": "05_ATTACHMENT_FORMATS",
            "section_title": "صيغ الملفات المدعومة",
            "confidence": "99.0%",
            "exact_snippet": "الملفات المدعومة للمرفقات: JPG, PNG, PDF بحد أقصى 5MB."
        })

    # 4.4 How to Check-In
    elif is_how_to_checkin_query:
        if is_ar:
            answer = "لتسجيل حضورك في المنصة: اضغط على زر **'تسجيل الدخول (Check-In)'** الأخضر في الشريط العلوي للوحة التحكم فور وصولك عند الساعة 9:00 صباحاً."
        else:
            answer = "To log attendance: Click the green **'Check-In'** button in the dashboard top bar immediately upon arrival at 9:00 AM."

        sources.append({
            "document": "policy.text",
            "section_id": "03_ATTENDANCE_LOGGING",
            "section_title": SECTION_METADATA["03_ATTENDANCE_LOGGING"]["title_ar" if is_ar else "title_en"],
            "confidence": "99.0%",
            "exact_snippet": "- تسجيل الدخول (Check-In): يجب على كل موظف الدخول للموقع وتسجيل الحضور فور الوصول."
        })

    # 4.5 How to Check-Out
    elif is_how_to_checkout_query:
        if is_ar:
            answer = "لتسجيل انصرافك في المنصة: اضغط على زر **'تسجيل الخروج (Check-Out)'** عند مغادرة مقر العمل عند الساعة 5:00 مساءً."
        else:
            answer = "To log departure: Click the **'Check-Out'** button when leaving the workplace at 5:00 PM."

        sources.append({
            "document": "policy.text",
            "section_id": "03_ATTENDANCE_LOGGING",
            "section_title": SECTION_METADATA["03_ATTENDANCE_LOGGING"]["title_ar" if is_ar else "title_en"],
            "confidence": "99.0%",
            "exact_snippet": "- تسجيل الخروج (Check-Out): يجب على كل موظف تسجيل الانصراف عند المغادرة."
        })

    # 4.7 Leave Balance & Allowed Days Off Query ("كم اجازه الي في الشهر", "كم مسموحلي اعطل")
    elif is_leave_balance_query:
        if any(k in q_norm for k in ["في الشهر", "بالشهر", "شهريا"]) or any(k in q_lower for k in ["per month", "in a month", "monthly"]):
            if is_ar:
                answer = "رصيد الإجازات السنوية المعتمد هو 14 يوماً في السنة (بمعدل 1.16 يوم شهرياً)، بالإضافة إلى يومين عمل عن بُعد شهرياً (Remote Work) بموافقة مسبقة من الإدارة."
            else:
                answer = "The annual leave entitlement is 14 days per year (averaging 1.16 days per month), plus up to 2 remote work days per month with prior management approval."
        elif any(k in q_norm for k in ["مرضيه", "مرضية", "مرض"]) or any(k in q_lower for k in ["sick leave", "medical leave"]):
            if is_ar:
                answer = "تُمنح الإجازة المرضية في الحالات الصحية، ويشترط إبلاغ المدير المباشر فوراً وإرفاق تقرير طبي رسمي معتمد خلال 24 ساعة من الانقطاع."
            else:
                answer = "Sick leave is granted for health emergencies and requires notifying your direct manager and attaching an official medical report within 24 hours."
        else:
            if is_ar:
                answer = "رصيد الإجازات السنوية المسموح به هو 14 يوماً سنوياً مدفوعة الأجر (يُشترط تقديم الطلب قبل 48 ساعة على الأقل)، بالإضافة إلى الإجازات المرضية بتقرير طبي، والعطلة الأسبوعية يومي الجمعة والسبت."
            else:
                answer = "The annual leave allowance is 14 paid days per year (must be requested at least 48 hours in advance), plus sick leaves with medical reports, and weekly days off on Friday and Saturday."

        sources.append({
            "document": "policy.text",
            "section_id": "08_LEAVES_AND_VACATIONS",
            "section_title": SECTION_METADATA["08_LEAVES_AND_VACATIONS"]["title_ar" if is_ar else "title_en"],
            "confidence": "99.5%",
            "exact_snippet": "- رصيد الإجازات السنوية: 14 يوماً سنوياً مدفوعة الأجر، ويُشترط تقديم طلب الإجازة قبل 48 ساعة على الأقل.\n- الإجازة المرضية: تمنح في الحالات المرضية وتتطلب إرفاق تقرير طبي رسمي خلال 24 ساعة من الانقطاع."
        })

    # 5. Planning to be Absent / "لو عطلت شو اعمل"
    elif is_planning_absence_query:
        if is_ar:
            answer = "إذا أردت الغياب أو أخذ عطلة، اتبع الإجراءات المعتمدة التالية:\n1. الإجازة المخططة: تقديم طلب إجازة سنوية قبل 48 ساعة على الأقل من رصيدك السنوي (14 يوماً).\n2. الغياب لظرف طارئ أو صحي: إبلاغ المدير المباشر فوراً، وتقديم طلب عذر رسمي عبر المنصة مع إرفاق التقرير الطبي خلال 24 ساعة لتفادي احتساب غياب غير مبرر وخصم الراتب."
        else:
            answer = "If you need to be absent or take a day off, follow official guidelines:\n1. Planned Leave: Submit an annual leave request at least 48 hours in advance (from your 14-day balance).\n2. Emergency/Health Absence: Inform your direct supervisor immediately, and submit an official excuse with medical report within 24 hours to prevent unexcused absence salary deductions."

        sources.append({
            "document": "policy.text",
            "section_id": "08_LEAVES_AND_VACATIONS",
            "section_title": SECTION_METADATA["08_LEAVES_AND_VACATIONS"]["title_ar" if is_ar else "title_en"],
            "confidence": "99.0%",
            "exact_snippet": "- رصيد الإجازات السنوية: 14 يوماً سنوياً (تُطلب قبل 48 ساعة). - الإجازة المرضية: تقرير طبي رسمي خلال 24 ساعة."
        })
        sources.append({
            "document": "policy.text",
            "section_id": "02_LATENESS_RULES",
            "section_title": SECTION_METADATA["02_LATENESS_RULES"]["title_ar" if is_ar else "title_en"],
            "confidence": "97.0%",
            "exact_snippet": "- التأخير غير المبرر (> 60 دقيقة) والغياب غير المبرر يوجب الخصم من الراتب والإنذار الإداري."
        })

    # 6. Today's Personal Attendance (Check-In Status)
    elif is_today_attendance_query:

        if user_logs_summary and user_logs_summary.get("checked_in"):
            t_in = user_logs_summary.get("checkin_time", "--:--")
            is_late = user_logs_summary.get("is_late", False)
            if is_ar:
                if is_late:
                    answer = f"نعم، أنت متأخر اليوم؛ حيث تم تسجيل دخولك في الساعة {t_in} (بعد انتهاء فترة السماح 09:15 ص). يُرجى تقديم عذر رسمي لتفادي الخصم."
                else:
                    answer = f"لا، أنت لست متأخراً اليوم؛ حيث تم تسجيل دخولك في الساعة {t_in} ضمن فترة السماح المحددة (قبل 09:15 ص)."
            else:
                if is_late:
                    answer = f"Yes, you are late today. Checked in at {t_in} past the 09:15 AM grace period. Please submit an excuse with proof."
                else:
                    answer = f"No, you are on time today. Checked in at {t_in} within the allowed grace period (before 09:15 AM)."
            
            sources.append({
                "document": "nexuslink.db",
                "table": "attendance",
                "record_type": "Personal Check-in Record",
                "email": user_email or "Current User",
                "confidence": "100%",
                "exact_snippet": f"Timestamp: {t_in}, Status: {'Late Check-in' if is_late else 'On-time Check-in'}"
            })
            sources.append({
                "document": "policy.text",
                "section_id": "02_LATENESS_RULES",
                "section_title": SECTION_METADATA["02_LATENESS_RULES"]["title_ar" if is_ar else "title_en"],
                "confidence": "90.0%",
                "exact_snippet": "- فترة السماح: يُسمح للموظف بالتأخير كحد أقصى 15 دقيقة (حتى 09:15 ص)."
            })
        elif user_email:
            if is_ar:
                answer = f"لم تقم بتسجيل الدخول اليوم حتى الآن لحسابك ({user_email}). يُرجى تسجيل الدخول فوراً لتفادي احتساب غياب تلقائي."
            else:
                answer = f"You haven't checked in yet today ({user_email}). Please log your check-in to avoid automatic absence."
            
            sources.append({
                "document": "nexuslink.db",
                "table": "attendance",
                "record_type": "Personal Attendance Record",
                "email": user_email,
                "confidence": "100%",
                "exact_snippet": "Check-in: Not recorded today."
            })
            sources.append({
                "document": "policy.text",
                "section_id": "03_ATTENDANCE_LOGGING",
                "section_title": SECTION_METADATA["03_ATTENDANCE_LOGGING"]["title_ar" if is_ar else "title_en"],
                "confidence": "95.0%",
                "exact_snippet": "- الغياب: في حال عدم قيام الموظف بتسجيل الدخول في الموقع يُعتبر الموظف غائباً عن العمل تلقائياً."
            })
        else:
            if is_ar:
                answer = "للاستعلام عن سجل حضورك وتأخيرك الشخصي، يرجى تزويد البريد الإلكتروني أو تسجيل الدخول."
            else:
                answer = "To inspect your personal attendance, please provide your email or log into your account."
            
            sources.append({
                "document": "nexuslink.db",
                "table": "attendance",
                "record_type": "Personal Attendance Record",
                "confidence": "90%",
                "exact_snippet": "Requires user email identifier."
            })

    # 3. Working Days & Work Schedule Inquiries (e.g. "شو ايام الدوام", "ايام العمل", "كم يوم بالاسبوع", "working days")
    elif is_working_days_query:
        if is_ar:
            answer = "أيام العمل الرسمية هي من الأحد إلى الخميس (من الساعة 9:00 صباحاً حتى الساعة 5:00 مساءً)، وعطلة نهاية الأسبوع هي يومي الجمعة والسبت."
        else:
            answer = "Official work days are Sunday through Thursday (9:00 AM to 5:00 PM), with Friday and Saturday as the official weekly days off."
        
        sources.append({
            "document": "policy.text",
            "section_id": "01_WORKING_HOURS",
            "section_title": SECTION_METADATA["01_WORKING_HOURS"]["title_ar" if is_ar else "title_en"],
            "confidence": "99.5%",
            "exact_snippet": "- أيام العمل الرسمية: من الأحد إلى الخميس.\n- ساعات العمل الرسمية: من الساعة 9:00 صباحاً حتى الساعة 5:00 مساءً.\n- إجمالي ساعات العمل الأسبوعية: 40 ساعة عمل أسبوعياً."
        })

    # 3.1 Specific Day Off / Work Day Questions (Direct & Crisp Answers with accurate affirmation/negation)
    # e.g., "الخميس عطلة ولا", "الجمعة دوام؟", "السبت عطلة", "متى العطلة", "الخميس دوام"
    elif any(k in q_norm for k in [
        "الخميس", "الجمعه", "السبت", "الاحد", "الاثنين", "الثلاثاء", "الاربعاء",
        "عطله ولا", "عطله اسبوعيه", "عطله الاسبوع", "عطله الشركه", "متي العطله",
        "day off", "weekend"
    ]) and not any(k in q_norm for k in ["اوفر تايم", "اوفرتايم", "اضافي", "بريك", "غدا", "غداء", "لباس", "مظهر"]):
        is_asking_if_work = any(k in q_norm for k in ["دوام", "شغل", "عمل", "work", "shift"]) and not any(k in q_norm for k in ["عطله", "اجازه", "off"])

        # Friday / Saturday (Weekend days)
        if any(k in q_norm for k in ["الجمعه", "السبت", "friday", "saturday", "عطله اسبوعيه", "عطله الاسبوع"]):
            if is_asking_if_work:
                if is_ar:
                    answer = "لا، يومي الجمعة والسبت هما عطلة أسبوعية رسمية وليس فيهما دوام (أيام العمل الرسمية هي من الأحد إلى الخميس فقط)."
                else:
                    answer = "No, Friday and Saturday are official weekend days off (Work days are Sunday through Thursday only)."
            else:
                if is_ar:
                    answer = "نعم، يومي الجمعة والسبت هما العطلة الأسبوعية الرسمية في الشركة (أيام الدوام الرسمي من الأحد إلى الخميس)."
                else:
                    answer = "Yes, Friday and Saturday are the official weekly weekend days off (Work days are Sunday through Thursday)."

        # Thursday
        elif "الخميس" in q_norm or "thursday" in q_norm:
            if is_asking_if_work:
                if is_ar:
                    answer = "نعم، يوم الخميس هو يوم عمل رسمي من الساعة 9:00 صباحاً حتى الساعة 5:00 مساءً."
                else:
                    answer = "Yes, Thursday is an official working day from 9:00 AM to 5:00 PM."
            else:
                if is_ar:
                    answer = "لا، يوم الخميس ليس عطلة، بل هو يوم عمل رسمي (أيام العمل من الأحد إلى الخميس من 9:00 ص حتى 5:00 م)."
                else:
                    answer = "No, Thursday is not a day off; it is an official working day (Sunday through Thursday, 9:00 AM to 5:00 PM)."

        # Sunday through Wednesday
        elif any(k in q_norm for k in ["الاحد", "الاثنين", "الثلاثاء", "الاربعاء", "sunday", "monday", "tuesday", "wednesday"]):
            if is_asking_if_work:
                if is_ar:
                    answer = "نعم، هو يوم عمل رسمي (ساعات الدوام من الساعة 9:00 صباحاً حتى الساعة 5:00 مساءً)."
                else:
                    answer = "Yes, it is an official working day (Shift hours are 9:00 AM to 5:00 PM)."
            else:
                if is_ar:
                    answer = "لا، ليس عطلة، بل هو يوم عمل رسمي من الأحد إلى الخميس (من 9:00 ص حتى 5:00 م)."
                else:
                    answer = "No, it is not a day off; it is an official working day (Sunday through Thursday, 9:00 AM to 5:00 PM)."
        else:
            if is_ar:
                answer = "أيام العمل الرسمية هي من الأحد إلى الخميس (9:00 ص - 5:00 م)، وعطلة نهاية الأسبوع هي يومي الجمعة والسبت."
            else:
                answer = "Official work days are Sunday through Thursday (9:00 AM - 5:00 PM), and the weekend days off are Friday and Saturday."

        sources.append({
            "document": "policy.text",
            "section_id": "01_WORKING_HOURS",
            "section_title": SECTION_METADATA["01_WORKING_HOURS"]["title_ar" if is_ar else "title_en"],
            "confidence": "99.0%",
            "exact_snippet": "- أيام العمل الرسمية: من الأحد إلى الخميس.\n- ساعات العمل الرسمية: من الساعة 9:00 صباحاً حتى الساعة 5:00 مساءً."
        })

    # 4. Working Hours Specific Questions (Daily, Weekly, Monthly, Shift timing, Slang "الترويحة")
    # e.g., "متى يبدأ الدوام", "متى ينتهي الدوام", "متى الترويحة", "في الشهر كم ساعة", "في الاسبوع كم ساعة"
    elif any(k in q_norm for k in [
        "ساعات العمل", "ساعات الدوام", "ساعات الشغل", "كم ساعه", "اوقات الدوام", "مواعيد الدوام",
        "من اي ساعه", "اي ساعه", "ساعه الدوام", "وقت الدوام", "موعد الدوام",
        "الترويحه", "ترويحه", "متي نروح", "متي بنروح", "متي نطلع", "متي بنخلص", "ساعه الانصراف", "وقت الانصراف",
        "يبدا الدوام", "يبدا الشغل", "ينتهي الدوام", "يخلص الدوام", "متي بنبلش", "في الشهر", "بالشهر",
        "في الاسبوع", "بالاسبوع", "في اليوم", "باليوم", "working hours", "shift hours", "hours per", "how many hours"
    ]) and not any(k in q_norm for k in [
        "عن بعد", "ريموت", "اجازه", "مرضيه", "بريك", "غدا", "غداء", "صلاه", "صلاة",
        "اضافي", "إضافي", "الاضافي", "الإضافي", "اوفر تايم", "اوفرتايم", "overtime", "بعد الدوام",
        "لباس", "مظهر", "يونيفورم", "لبس", "معلق", "مشكله فنيه", "عطل فني"
    ]):
        if any(k in q_norm for k in ["شهر", "شهريا", "month", "monthly"]):
            answer = "معدل ساعات العمل الشهرية حوالي 160 إلى 176 ساعة عمل شهرياً (بمعدل 40 ساعة عمل أسبوعياً، 8 ساعات يومياً من الأحد إلى الخميس)." if is_ar else "Monthly working load is approximately 160 to 176 hours per month (based on 40 hours/week, 8 hours/day Sunday through Thursday)."
        elif any(k in q_norm for k in ["اسبوع", "اسبوعيا", "weekly", "week"]):
            answer = "إجمالي ساعات العمل الأسبوعية هو 40 ساعة عمل أسبوعياً (من الأحد إلى الخميس)." if is_ar else "Total weekly load is 40 working hours per week (Sunday through Thursday)."
        elif any(k in q_norm for k in ["يوم", "يوميا", "باليوم", "daily", "day"]):
            answer = "ساعات العمل اليومية هي 8 ساعات يومياً (من الساعة 9:00 صباحاً حتى الساعة 5:00 مساءً)." if is_ar else "Daily working load is 8 hours per day (from 9:00 AM to 5:00 PM)."
        elif any(k in q_norm for k in ["ينتهي", "يخلص", "نهايه", "انصراف", "الترويحه", "ترويحه", "نروح", "نطلع", "بنخلص", "end", "finish"]):
            answer = "ينتهي الدوام الرسمي (الترويحة والانصراف) عند الساعة 5:00 مساءً." if is_ar else "Official working hours end at 5:00 PM."
        elif any(k in q_norm for k in ["من اي ساعه", "من كم", "من متي", "يبدا", "نبلش", "نجي", "start", "بدايه", "الصبح"]):
            answer = "يبدأ الدوام الرسمي عند الساعة 9:00 صباحاً (وينتهي عند الساعة 5:00 مساءً)." if is_ar else "Official working hours start at 9:00 AM (and end at 5:00 PM)."
        else:
            answer = "ساعات العمل الرسمية من الساعة 9:00 صباحاً حتى الساعة 5:00 مساءً (8 ساعات يومياً)، من الأحد إلى الخميس بإجمالي 40 ساعة أسبوعياً." if is_ar else "Official working hours are 9:00 AM to 5:00 PM (8 hours daily), Sunday through Thursday (40 hours weekly)."
        
        sources.append({
            "document": "policy.text",
            "section_id": "01_WORKING_HOURS",
            "section_title": SECTION_METADATA["01_WORKING_HOURS"]["title_ar" if is_ar else "title_en"],
            "confidence": "99.0%",
            "exact_snippet": "- أيام العمل الرسمية: من الأحد إلى الخميس.\n- ساعات العمل الرسمية: من الساعة 9:00 صباحاً حتى الساعة 5:00 مساءً.\n- إجمالي ساعات العمل الأسبوعية: 40 ساعة عمل أسبوعياً."
        })

    # 6. Excuse Validity & Classification Specific Questions ("لو كانت ازمة الطريق بقبل المدير عذري؟", "صحيت متاخر", "حادث سير", etc.)
    elif any(k in q_norm for k in [
        "عذر مقبول", "عذر مرفوض", "يقبل عذري", "يقبل العذر", "بقبل عذري", "بقبل العذر", "يقبل المدير عذري", "بقبل المدير عذري",
        "صحيت متاخر", "راحت علي نومه", "نمت متاخر", "سهران", "سهرت", "المنبه ما رن", "منبه ما اشتغل", "المنبه", "منبه",
        "ازمه سير", "ازمة سير", "ازمه الطريق", "ازمة الطريق", "ازمه الشارع", "ازمة الشارع", "ازمه", "ازمة", "زحمه", "زحمة", "زحام", "عجقه", "عجقة", "عجقه السير", "عجقة السير",
        "ظرف شخصي", "مشوار شخصي", "مشاوير شخصيه", "مشاوير شخصية",
        "حادث سير", "حادث", "كروكه", "كروكة", "صدمت", "خبطت", "تقرير طبي", "مرض مفاجئ", "دخول مستشفي", "دخول مستشفى", "بالمستشفي", "بالمستشفى", "مريض", "مرضان", "تعبان", "سخنان",
        "سيارتي تعطلت", "سيارتي خربت", "تعطلت سيارتي", "خربت سيارتي", "بنشر بالسيارة", "بنشر بالسياره", "بنشر", "بنشرت", "عطل بالسياره", "عطل بالسيارة", "عطل في السياره", "عطل في السيارة", "الباص تعطل", "خرب الباص",
        "وفاه", "وفاة", "عزاء", "جنازه", "جنازة", "مات", "ثلوج", "ثلج", "امطار غزيره", "امطار غزيرة", "سيول", "عاصفه", "عاصفة", "منخفض",
        "excuse", "acceptable", "unacceptable", "kroka", "medical", "sick", "traffic"
    ]):
        eval_res = evaluate_semantic_excuse(q_clean, lateness_mins=30, has_attachment=False)
        cluster_key = eval_res.get("matched_cluster", "")
        conf = f"{eval_res.get('semantic_match_score', 95.0)}%"

        # 6.1 Unacceptable: Traffic / Congestion / Azmeh
        if any(k in q_norm for k in ["ازمه", "ازمة", "زحمه", "زحمة", "زحام", "عجقه", "عجقة", "traffic", "jam", "congestion"]):
            if is_ar:
                answer = "لا، أزمة وازدحام الطريق العادي تُعتبر من الأعذار المرفوضة قطعياً في لائحة الشركة، وتُسجل كتأخير عادي."
            else:
                answer = "No, regular road and traffic congestion is strictly unacceptable under company policy and is logged as standard lateness."

            sources.append({
                "document": "policy.text",
                "section_id": "06_EXCUSES_CLASSIFICATION",
                "section_title": SECTION_METADATA["06_EXCUSES_CLASSIFICATION"]["title_ar" if is_ar else "title_en"],
                "confidence": "99.5%",
                "exact_snippet": "الأعذار المرفوضة قطئياً: 2. أزمة وازدحام الطريق العادي."
            })

        # 6.2 Unacceptable: Oversleeping / Alarm / Sleeping Late / Personal errands
        elif any(k in q_norm for k in ["صحيت", "نمت", "منبه", "سهران", "سهرت", "راحت علي نومه", "ظرف شخصي", "مشوار", "alarm", "overslept", "woke up late"]):
            if is_ar:
                answer = "لا، الاستيقاظ متأخراً أو عدم رنين المنبه والسهر من الأعذار المرفوضة قطعياً في لائحة الشركة وتطبق عليها الخصومات."
            else:
                answer = "No, oversleeping, alarm failure, and staying up late are strictly unacceptable excuses subject to deductions."

            sources.append({
                "document": "policy.text",
                "section_id": "06_EXCUSES_CLASSIFICATION",
                "section_title": SECTION_METADATA["06_EXCUSES_CLASSIFICATION"]["title_ar" if is_ar else "title_en"],
                "confidence": "99.5%",
                "exact_snippet": "الأعذار المرفوضة قطئياً:\n1. الاستيقاظ متأخراً.\n4. عدم رنين أو ضبط المنبه.\n5. السهر والنوم المتأخر."
            })

        # 6.3 Acceptable: Traffic Accidents & Police Kroka
        elif cluster_key == "traffic_accident" or any(k in q_norm for k in ["حادث", "كروكه", "كروكة", "صدمت", "خبطت", "accident"]):
            if is_ar:
                answer = "نعم، يُقبل عذر حادث السير المروري بشرط إرفاق صورة كروكة الشرطة أو صورة واضحة للحادث لإثبات الواقعة للقبول الفوري."
            else:
                answer = "Yes, traffic accident is an acceptable excuse provided you attach the official police report (Kroka) or clear accident photo."

            sources.append({
                "document": "policy.text",
                "section_id": "05_PROOF_REQUIREMENTS",
                "section_title": SECTION_METADATA["05_PROOF_REQUIREMENTS"]["title_ar" if is_ar else "title_en"],
                "confidence": "99.0%",
                "exact_snippet": "حوادث السير والمرور: تتطلب إرفاق صورة كروكة الشرطة أو صورة واضحة للحادث لإثبات الواقعة للقبول الفوري."
            })

        # 6.4 Acceptable: Vehicle / Public Transport Breakdown
        elif any(k in q_norm for k in ["سيارتي", "السياره", "السيارة", "مركبتي", "المركبه", "المركبة", "الباص", "باص", "بنشر", "بنشرت", "خربت", "تعطلت", "عطل", "breakdown"]):
            if is_ar:
                answer = "نعم، العطل المفاجئ لمركبة الموظف أو وسيلة النقل أثناء الطريق يُعتبر عذراً مقبولاً نظامياً. يرجى تقديم طلب عذر رسمي عبر المنصة لتثبيته."
            else:
                answer = "Yes, sudden vehicle or transport breakdown en route is an acceptable excuse. Please submit an official excuse on the portal to record it."

            sources.append({
                "document": "policy.text",
                "section_id": "06_EXCUSES_CLASSIFICATION",
                "section_title": SECTION_METADATA["06_EXCUSES_CLASSIFICATION"]["title_ar" if is_ar else "title_en"],
                "confidence": "99.0%",
                "exact_snippet": "الأعذار المقبولة نظامياً: 3. العطل المفاجئ لوسيلة النقل أو المركبة أثناء الطريق."
            })

        # 6.5 Acceptable: Medical Emergency & Sick Leaves
        elif any(k in q_norm for k in ["مريض", "مرضان", "تعبان", "سخنان", "مرض", "طبيب", "دكتور", "مستشفي", "مستشفى", "بالمستشفي", "بالمستشفى", "طوارئ", "عمليه", "عملية", "sick", "medical"]):
            if is_ar:
                answer = "نعم، يُقبل العذر الصحي والإجازة المرضية بشرط إبلاغ المدير المباشر وإرفاق تقرير طبي رسمي معتمد خلال 24 ساعة من الانقطاع."
            else:
                answer = "Yes, medical excuses and sick leaves are accepted provided you inform your manager and attach an official medical report within 24 hours."

            sources.append({
                "document": "policy.text",
                "section_id": "08_LEAVES_AND_VACATIONS",
                "section_title": SECTION_METADATA["08_LEAVES_AND_VACATIONS"]["title_ar" if is_ar else "title_en"],
                "confidence": "99.0%",
                "exact_snippet": "- الإجازة المرضية: تمنح في الحالات المرضية وتتطلب إرفاق تقرير طبي رسمي خلال 24 ساعة من الانقطاع."
            })
            sources.append({
                "document": "policy.text",
                "section_id": "05_PROOF_REQUIREMENTS",
                "section_title": SECTION_METADATA["05_PROOF_REQUIREMENTS"]["title_ar" if is_ar else "title_en"],
                "confidence": "98.0%",
                "exact_snippet": "الأعذار الصحية والطبية: تتطلب إرفاق تقرير طبي رسمي معتمد للقبول الفوري."
            })

        # 6.6 Acceptable: Bereavement / Funeral / Death
        elif any(k in q_norm for k in ["وفاه", "وفاة", "عزاء", "جنازه", "جنازة", "مات", "bereavement", "death"]):
            if is_ar:
                answer = "نعم، حالات الوفاة والعزاء العائلي تُعتبر من الأعذار المقبولة نظامياً دون أي خصومات مالية."
            else:
                answer = "Yes, bereavement and family condolences are officially accepted excuses without salary deductions."

            sources.append({
                "document": "policy.text",
                "section_id": "06_EXCUSES_CLASSIFICATION",
                "section_title": SECTION_METADATA["06_EXCUSES_CLASSIFICATION"]["title_ar" if is_ar else "title_en"],
                "confidence": "99.5%",
                "exact_snippet": "الأعذار المقبولة نظامياً: 1. حالات الوفاة وحالات العزاء العائلي."
            })

        # 6.7 Acceptable: Severe Weather Conditions (Snow, heavy rain)
        elif any(k in q_norm for k in ["ثلوج", "ثلج", "سيول", "امطار غزيره", "امطار غزيرة", "عاصفه", "عاصفة", "منخفض", "weather", "snow"]):
            if is_ar:
                answer = "نعم، صعوبة الظروف الجوية القاهرة والأمطار الغزيرة والثلوج تُعتبر من الأعذار المقبولة نظامياً."
            else:
                answer = "Yes, severe force majeure weather conditions such as heavy snow and floods are acceptable excuses."

            sources.append({
                "document": "policy.text",
                "section_id": "06_EXCUSES_CLASSIFICATION",
                "section_title": SECTION_METADATA["06_EXCUSES_CLASSIFICATION"]["title_ar" if is_ar else "title_en"],
                "confidence": "99.0%",
                "exact_snippet": "الأعذار المقبولة نظامياً: 5. صعوبة الظروف الجوية القاهرة والأمطار الغزيرة والثلوج."
            })

        elif cluster_key == "unacceptable":
            if is_ar:
                answer = "لا، هذا العذر مرفوض قطعياً في لائحة الشركة وتطبق عليه الخصومات."
            else:
                answer = "No, this excuse is strictly unacceptable per company policy."

            sources.append({
                "document": "policy.text",
                "section_id": "06_EXCUSES_CLASSIFICATION",
                "section_title": SECTION_METADATA["06_EXCUSES_CLASSIFICATION"]["title_ar" if is_ar else "title_en"],
                "confidence": conf,
                "exact_snippet": "الأعذار المرفوضة قطئياً (يُسجل غياب وتطبق الخصومات)"
            })

        else:
            if is_ar:
                answer = "الأعذار المقبولة: الوفاة، حوادث السير (مع كروكة)، عطل المركبة، والظروف الصحية (مع تقرير طبي). الأعذار المرفوضة: النوم المتأخر، المنبه، وأزمة الطريق."
            else:
                answer = "Acceptable excuses: Bereavement, accidents (with Kroka), vehicle breakdown, medical issues (with report). Unacceptable: sleeping late, alarm, traffic."

            sources.append({
                "document": "policy.text",
                "section_id": "06_EXCUSES_CLASSIFICATION",
                "section_title": SECTION_METADATA["06_EXCUSES_CLASSIFICATION"]["title_ar" if is_ar else "title_en"],
                "confidence": "98.0%",
                "exact_snippet": SECTION_METADATA["06_EXCUSES_CLASSIFICATION"]["content_en" if not is_ar else "title_ar"]
            })

    # 5.0 With Valid Excuse Submitted (General "واذا كان معي عذر", "لو كان في عذر", "معي عذر", "عندي عذر", "لو قدمت عذر")
    elif (
        any(k in q_norm for k in [
            "معي عذر", "عندي عذر", "مع عذر", "في عذر", "كان في عذر", "بوجود عذر", "قدمت عذر", "لو قدمت عذر", "اذا قدمت عذر",
            "اذا كان في عذر", "لو كان في عذر", "واذا كان في عذر", "واذا كان معي عذر", "اذا في عذر", "لو في عذر",
            "لو عندي عذر", "اذا عندي عذر", "اذا معي عذر", "لو معي عذر", "لو العذر مقبول", "اذا العذر مقبول",
            "with excuse", "if i have an excuse", "if excuse is submitted", "having an excuse"
        ]) or (
            any(k in q_norm for k in ["عذر", "عذري", "اعذار", "عذرا", "excuse"]) and
            any(k in q_norm for k in ["معي", "عندي", "معنا", "عنده", "في", "كان", "مع", "بوجود", "قدمت", "مقبول", "رسمي", "with", "have"])
        )
    ) and not any(k in q_norm for k in ["حادث", "كروك", "مريض", "مرض", "سيارت", "عطلت", "اثبات", "تقرير", "كيف اقدم", "وين اقدم", "خطوات", "ما سجلت", "ما قدمت", "بدون عذر", "دون عذر", "ما معي", "ما عندي", "غير مبرر", "مرفوض", "منبه", "صحيت", "نمت", "ازم", "ازمة", "زحم", "زحمة", "عجق", "عجقة", "unexcused", "no excuse"]):
        if is_ar:
            answer = "في حال وجود عذر رسمي مقبول أو ظرف طارئ، لا يتم تطبيق أي خصم مالي، ويجب إبلاغ المدير المباشر فوراً وتقديم طلب العذر مع الإثبات خلال ساعات الدوام (9:00 ص - 5:00 م)."
        else:
            answer = "In case of a valid accepted excuse or emergency, no salary deductions are applied. You must notify your direct manager promptly and submit the excuse request with proof during working hours (9:00 AM - 5:00 PM)."

        sources.append({
            "document": "policy.text",
            "section_id": "02_LATENESS_RULES",
            "section_title": SECTION_METADATA["02_LATENESS_RULES"]["title_ar" if is_ar else "title_en"],
            "confidence": "99.0%",
            "exact_snippet": "- التأخير غير المبرر (> 60 دقيقة): إذا تأخر الموظف لأكثر من 60 دقيقة دون عذر مقبول يتم خصم نصف يوم من الراتب (أما مع العذر المقبول فيعفى من الخصم)."
        })
        sources.append({
            "document": "policy.text",
            "section_id": "04_EXCUSE_TIME_WINDOW",
            "section_title": SECTION_METADATA["04_EXCUSE_TIME_WINDOW"]["title_ar" if is_ar else "title_en"],
            "confidence": "98.0%",
            "exact_snippet": "- يجب تقديم طلب العذر خلال فترة الدوام الرسمي حصراً من الساعة 9:00 صباحاً إلى الساعة 5:00 مساءً."
        })

    # 5. Grace Period & Lateness Rules Specific Questions
    # e.g., "لو تاخرت 30 دقيقة بصير خصم", "كم فترة السماح", "عقوبة التأخير أكثر من ساعة", "خصم التأخير"
    elif any(k in q_norm for k in [
        "سماح", "فتره السماح", "مهله السماح", "تاخير", "تاخر", "تاخرت",
        "خصم", "خصومات", "عقوبه التاخير", "خصم التاخير", "نصف يوم", "نص يوم", "30 دقيقه", "20 دقيقه",
        "40 دقيقه", "45 دقيقه", "نص ساعه", "نصف ساعه", "ساعه", "grace period", "late", "lateness", "deduction"
    ]) and not any(k in q_norm for k in ["ما سجلت عذر", "ما قدمت عذر", "غير مبرر", "عذر", "عذري", "صحيت", "منبه", "نمت", "حادث", "مريض", "excuse"]):
        if any(k in q_lower for k in ["30", "نص ساعة", "نصف ساعة", "20", "25", "35", "40", "45", "50", "أقل من ساعة", "اقل من ساعه"]):
            if "خصم" in q_lower or "بصير خصم" in q_lower or "في خصم" in q_lower or "deduction" in q_lower:
                answer = "لا، التأخير لمدة أقل من 60 دقيقة لا يترتب عليه خصم مالي مباشر (الخصم يطبق فقط إذا تجاوز التأخير 60 دقيقة دون عذر مقبول)، ولكنه يُسجل كتأخير عادي." if is_ar else "No, a delay under 60 minutes does not incur direct salary deductions (deductions apply only if delay exceeds 60 minutes unexcused), but is logged as standard lateness."
            else:
                answer = "التأخير لمدة أقل من 60 دقيقة يُسجل كتأخير عادي ولا يوجب خصماً مالياً إلا إذا تجاوز 60 دقيقة دون عذر مقبول أو تكرر لـ 3 أيام متتالية." if is_ar else "Lateness under 60 minutes is logged as regular delay without immediate deductions unless it exceeds 60 minutes unexcused."
        elif any(k in q_lower for k in ["سماح", "grace", "كم دقيقة مسموح", "كم مسموح"]):
            answer = "فترة السماح هي 15 دقيقة فقط (حتى الساعة 09:15 صباحاً) لتسجيل الدخول دون أي خصم." if is_ar else "The grace period is 15 minutes max (until 09:15 AM) to check in without penalties."
        elif any(k in q_lower for k in ["60", "أكثر من ساعة", "اكثر من ساعه", "ساعة", "ساعه", "نصف يوم", "خصم نصف"]):
            answer = "إذا تأخر الموظف لأكثر من 60 دقيقة دون عذر مقبول، يتم خصم نصف يوم من الراتب." if is_ar else "Unexcused delay exceeding 60 minutes incurs a half-day salary deduction."
        elif any(k in q_lower for k in ["3 أيام", "3 ايام", "تكرار", "إنذار", "انذار"]):
            answer = "تكرار تأخير الموظف لأكثر من 3 أيام متتالية يوجب الإنذار الإداري والخصم المالي." if is_ar else "Consecutive lateness for 3+ days triggers administrative warnings and salary deductions."
        else:
            answer = "فترة السماح 15 دقيقة دون خصم (حتى 09:15 ص). والتأخير غير المبرر لأكثر من 60 دقيقة يوجب خصم نصف يوم من الراتب." if is_ar else "Grace period is 15 mins (until 09:15 AM). Unexcused delay >60 mins incurs half-day deduction."
        
        sources.append({
            "document": "policy.text",
            "section_id": "02_LATENESS_RULES",
            "section_title": SECTION_METADATA["02_LATENESS_RULES"]["title_ar" if is_ar else "title_en"],
            "confidence": "98.5%",
            "exact_snippet": "- فترة السماح: يُسمح للموظف بالتأخير كحد أقصى 15 دقيقة (حتى 09:15 ص).\n- التأخير غير المبرر (> 60 دقيقة): إذا تأخر الموظف لأكثر من 60 دقيقة دون عذر مقبول يتم خصم نصف يوم من الراتب."
        })

    # 5.1 Penalty for NOT Submitting an Excuse / Unexcused Lateness & Absence
    # e.g., "واذا ما سجلت عذر رسمي", "لو ما قدمت عذر", "بدون عذر", "عدم تقديم عذر", "what if i don't submit an excuse"
    elif any(k in q_lower for k in [
        "ما سجلت عذر", "ما قدمت عذر", "واذا ما سجلت", "اذا ما سجلت", "لو ما سجلت", "واذا ما قدمت", "اذا ما قدمت", "لو ما قدمت",
        "عدم تقديم عذر", "عدم تسجيل عذر", "بدون عذر", "إذا لم أقدم عذر", "في حال عدم تقديم عذر", "عقوبة عدم تقديم",
        "شو بصير لو ما", "شو بصير اذا ما", "ما عندي عذر", "لو ما في عذر", "دون عذر", "غير مبرر", "غير مبررة",
        "what if i don't submit an excuse", "without excuse", "unexcused", "no excuse", "failing to submit excuse"
    ]):
        if is_ar:
            answer = "في حال عدم تقديم أو تسجيل عذر رسمي مقبول، يُعتبر التأخير/الغياب غير مبرر ويترتب عليه:\n1. خصم نصف يوم عمل من الراتب إذا تجاوز التأخير 60 دقيقة.\n2. احتساب اليوم كـ غياب غير مبرر تلقائياً في حال عدم تسجيل الدخول.\n3. توجيه إنذار إداري وخصومات مالية في حال تكرار التأخير لأكثر من 3 أيام متتالية."
        else:
            answer = "If you do not submit an official acceptable excuse, the lateness/absence is classified as unexcused and results in:\n1. A mandatory half-day salary deduction if delay exceeds 60 minutes.\n2. Automatic unexcused absence if check-in was missed.\n3. Formal administrative warnings and financial deductions for 3+ consecutive days of repeated lateness."

        sources.append({
            "document": "policy.text",
            "section_id": "02_LATENESS_RULES",
            "section_title": SECTION_METADATA["02_LATENESS_RULES"]["title_ar" if is_ar else "title_en"],
            "confidence": "99.0%",
            "exact_snippet": "- التأخير غير المبرر (> 60 دقيقة): إذا تأخر الموظف لأكثر من 60 دقيقة دون عذر مقبول يتم خصم نصف يوم من الراتب.\n- تكرار التأخير: إذا تكرر تأخير الموظف لأكثر من 3 أيام متتالية يخضع للإنذار الإداري والخصم المالي."
        })
        sources.append({
            "document": "policy.text",
            "section_id": "03_ATTENDANCE_LOGGING",
            "section_title": SECTION_METADATA["03_ATTENDANCE_LOGGING"]["title_ar" if is_ar else "title_en"],
            "confidence": "96.0%",
            "exact_snippet": "- الغياب: في حال عدم قيام الموظف بتسجيل الدخول في الموقع يُعتبر الموظف غائباً عن العمل تلقائياً."
        })

    # 5.2 Forgetting or Missing Check-In / Check-Out
    elif any(k in q_lower for k in [
        "نسيت اسجل دخول", "نسيت اسجل خروج", "ما سجلت دخول", "ما سجلت خروج", "نسيت تسجيل الدخول", "نسيت تسجيل الخروج",
        "لو نسيت اسجل", "forgot check-in", "forgot check-out", "missed check-in"
    ]):
        if any(k in q_lower for k in ["خروج", "انصراف", "check-out"]):
            answer = "يجب تسجيل الانصراف (Check-Out) عند مغادرة مقر العمل عند الساعة 5:00 مساءً لإثبات الالتزام بساعات الدوام كاملة." if is_ar else "Check-out must be logged upon departure at 5:00 PM to verify full shift completion."
        else:
            answer = "عدم تسجيل الدخول في الموقع يُعتبر الموظف غائباً عن العمل تلقائياً. يجب تسجيل الحضور فور الوصول عند الساعة 9:00 ص." if is_ar else "Failing to log check-in classifies the employee as automatically absent. Check-in must be logged immediately upon arrival at 9:00 AM."

        sources.append({
            "document": "policy.text",
            "section_id": "03_ATTENDANCE_LOGGING",
            "section_title": SECTION_METADATA["03_ATTENDANCE_LOGGING"]["title_ar" if is_ar else "title_en"],
            "confidence": "98.0%",
            "exact_snippet": "- تسجيل الدخول (Check-In): يجب على كل موظف الدخول للموقع وتسجيل الحضور فور الوصول.\n- تسجيل الخروج (Check-Out): يجب على كل موظف تسجيل الانصراف عند المغادرة.\n- الغياب: في حال عدم قيام الموظف بتسجيل الدخول في الموقع يُعتبر الموظف غائباً عن العمل تلقائياً."
        })

    # 7. Check-in / Check-out & Excuse Submission Window
    elif any(k in q_lower for k in ["تسجيل الدخول", "تسجيل الخروج", "تسجيل الحضور", "تسجيل الانصراف", "check-in", "check-out", "مهلة تقديم العذر", "وقت تقديم العذر"]):
        if any(k in q_lower for k in ["مهلة", "تقديم العذر", "وقت تقديم", "submission window"]):
            answer = "يجب تقديم طلب العذر خلال فترة الدوام الرسمي حصراً (من الساعة 9:00 ص إلى 5:00 م) من نفس يوم التأخير." if is_ar else "Excuse requests must be submitted during official shift hours (9:00 AM to 5:00 PM) on the same day."
            sources.append({
                "document": "policy.text",
                "section_id": "04_EXCUSE_TIME_WINDOW",
                "section_title": SECTION_METADATA["04_EXCUSE_TIME_WINDOW"]["title_ar" if is_ar else "title_en"],
                "confidence": "97.0%",
                "exact_snippet": "- يجب تقديم طلب العذر خلال فترة الدوام الرسمي حصراً من الساعة 9:00 صباحاً إلى الساعة 5:00 مساءً من نفس يوم التأخير."
            })
        else:
            answer = "يجب تسجيل الحضور (Check-In) فور الوصول وتسجيل الانصراف (Check-Out) عند المغادرة. عدم التسجيل يُعد غياباً تلقائياً." if is_ar else "Must check in immediately upon arrival and check out upon departure. Failing to log check-in classifies as automatic absence."
            sources.append({
                "document": "policy.text",
                "section_id": "03_ATTENDANCE_LOGGING",
                "section_title": SECTION_METADATA["03_ATTENDANCE_LOGGING"]["title_ar" if is_ar else "title_en"],
                "confidence": "96.0%",
                "exact_snippet": "- تسجيل الدخول: فور الوصول. - تسجيل الخروج: عند المغادرة. - الغياب: عدم تسجيل الدخول يُعد غياباً تلقائياً."
            })

    # 8. Early Departure & Emergency Permissions
    # e.g., "بقدر اغادر بدري اليوم", "استئذان طارئ", "المغادرة أثناء الدوام"
    elif any(k in q_lower for k in [
        "مغادرة", "مغادره", "المغادرة", "اغادر", "أغادر", "استئذان", "استاذن", "استأذن", "اطلع بدري",
        "خروج بدري", "خروج مبكر", "انصراف مبكر", "اذن ساعي", "إذن ساعي", "إذن طارئ", "اذن طارئ",
        "leave early", "early departure", "short leave", "permission"
    ]):
        if is_ar:
            answer = "تُمنح المغادرات الساعية أثناء الدوام حصراً بحسب الظرف الطارئ للموظف، ويشترط إبلاغ المدير المباشر والحصول على موافقته مسبقاً قبل المغادرة."
        else:
            answer = "Short leaves during shift hours are granted exclusively based on the employee's emergency situation, requiring prior notification and approval from the direct supervisor."

        sources.append({
            "document": "policy.text",
            "section_id": "07_EARLY_DEPARTURE_AND_PERMISSIONS",
            "section_title": SECTION_METADATA["07_EARLY_DEPARTURE_AND_PERMISSIONS"]["title_ar" if is_ar else "title_en"],
            "confidence": "98.5%",
            "exact_snippet": "- تمنح المغادرات الساعية أثناء وقت الدوام حصراً بحسب الظرف الطارئ للموظف.\n- يشترط إبلاغ المدير المباشر بالظرف الطارئ والحصول على الموافقة قبل المغادرة."
        })

    # 9. Leaves & Vacations (Annual & Sick)
    # e.g., "كم رصيد إجازاتي السنوية", "الإجازة المرضية"
    elif any(k in q_lower for k in [
        "إجازة", "اجازة", "إجازات", "اجازات", "سنوية", "سنويه", "مرضية", "مرضيه", "رصيد إجازاتي", "رصيد اجازاتي",
        "annual leave", "sick leave", "vacation"
    ]):
        if is_ar:
            answer = "رصيد الإجازات السنوية هو 14 يوماً سنوياً مدفوعة الأجر (يُشترط تقديم الطلب قبل 48 ساعة على الأقل). والإجازة المرضية تتطلب إرفاق تقرير طبي رسمي خلال 24 ساعة من الانقطاع."
        else:
            answer = "Annual leave balance is 14 paid days per year (must be requested at least 48 hours in advance). Sick leave requires a verified medical report within 24 hours."

        sources.append({
            "document": "policy.text",
            "section_id": "08_LEAVES_AND_VACATIONS",
            "section_title": SECTION_METADATA["08_LEAVES_AND_VACATIONS"]["title_ar" if is_ar else "title_en"],
            "confidence": "98.5%",
            "exact_snippet": "- رصيد الإجازات السنوية: 14 يوماً سنوياً مدفوعة الأجر، ويُشترط تقديم طلب الإجازة قبل 48 ساعة على الأقل.\n- الإجازة المرضية: تمنح في الحالات المرضية وتتطلب إرفاق تقرير طبي رسمي خلال 24 ساعة من الانقطاع."
        })

    # 10. Remote Work / Work from Home
    # e.g., "في شغل من البيت", "الدوام عن بعد", "اشتغل من البيت"
    elif any(k in q_lower for k in [
        "من البيت", "من المنزل", "عن بعد", "عن بُعد", "ريموت", "اشتغل من", "اداوم من", "دوام عن بعد",
        "remote work", "work from home", "wfh", "remotely"
    ]):
        if is_ar:
            answer = "يُسمح بالعمل عن بُعد في الحالات الطارئة أو بحد أقصى يومين شهرياً بموافقة مسبقة من الإدارة، مع الالتزام بالتواجد والتفاعل خلال ساعات الدوام الرسمي (9:00 ص - 5:00 م)."
        else:
            answer = "Remote work is permitted in emergency cases or up to 2 days per month with prior management approval, requiring active presence during official shift hours (9:00 AM - 5:00 PM)."

        sources.append({
            "document": "policy.text",
            "section_id": "09_REMOTE_WORK_POLICY",
            "section_title": SECTION_METADATA["09_REMOTE_WORK_POLICY"]["title_ar" if is_ar else "title_en"],
            "confidence": "98.5%",
            "exact_snippet": "- يُسمح بالعمل عن بُعد في الحالات الطارئة أو بحد أقصى يومين شهرياً بموافقة مسبقة من الإدارة.\n- يشترط تواجد الموظف وتفاعله خلال ساعات العمل الرسمية (9:00 ص - 5:00 م)."
        })

    # 11. Lunch & Prayer Breaks
    # e.g., "كم مدة استراحة الغداء", "بريك الغدا", "وقت الصلاة"
    elif any(k in q_lower for k in [
        "بريك", "الغدا", "الغداء", "استراحة", "استراحه", "صلاة", "الصلاة", "lunch break", "prayer break", "break time"
    ]):
        if is_ar:
            answer = "فترة استراحة الغداء والصلاة مدتها ساعة واحدة يومياً، وهي مرنة بين الساعة 01:00 ظهراً والساعة 02:30 ظهراً."
        else:
            answer = "Daily lunch and prayer break duration is 1 hour, flexible between 01:00 PM and 02:30 PM."

        sources.append({
            "document": "policy.text",
            "section_id": "10_BREAKS_AND_PRAYER",
            "section_title": SECTION_METADATA["10_BREAKS_AND_PRAYER"]["title_ar" if is_ar else "title_en"],
            "confidence": "98.5%",
            "exact_snippet": "- فترة الاستراحة اليومية مدتها ساعة واحدة، وهي مرنة بين الساعة 01:00 ظهراً والساعة 02:30 ظهراً."
        })

    # 12. Overtime Policy
    # e.g., "في اوفر تايم", "ساعات العمل الإضافي"
    elif any(k in q_lower for k in [
        "اوفر تايم", "أوفر تايم", "اوفرتايم", "أوفرتايم", "إضافي", "اضافي", "إضافية", "اضافية",
        "شغل بعد الدوام", "overtime", "extra hours"
    ]):
        if is_ar:
            answer = "العمل الإضافي بعد الساعة 5:00 مساءً يتم بتكليف رسمي مسبق من الإدارة، ويُعوض مالياً أو بأيام راحة بديلة."
        else:
            answer = "Overtime work after 5:00 PM requires prior official management assignment, compensated financially or via compensatory time off."

        sources.append({
            "document": "policy.text",
            "section_id": "11_OVERTIME_POLICY",
            "section_title": SECTION_METADATA["11_OVERTIME_POLICY"]["title_ar" if is_ar else "title_en"],
            "confidence": "98.5%",
            "exact_snippet": "- العمل الإضافي بعد الساعة 5:00 مساءً يتم بتكليف رسمي مسبق من الإدارة، ويُعوض مالياً أو بأيام راحة بديلة."
        })

    # 13. Technical Issues & Missed Log (Website / Portal / System Only)
    # e.g., "الموقع معلق", "مشكلة فنية في الموقع", "مشكلة بالسيستم"
    elif any(k in q_lower for k in [
        "الموقع معلق", "السيستم معلق", "مشكلة فنية", "مشكله فنيه", "عطل فني بالموقع", "مشكلة بالموقع", "مشكلة في الموقع",
        "الموقع مش شغال", "السيستم مش شغال", "مشكلة بالسيستم", "البصمة معلقة", "technical issue", "system error", "portal down"
    ]):
        if is_ar:
            answer = "في حال حدوث عطل فني في الموقع أو نسيان تسجيل الحضور، يجب إبلاغ الدعم الفني أو المدير المباشر قبل الساعة 10:00 صباحاً لتثبيت القيد يدوياً وتفادي احتساب الغياب."
        else:
            answer = "In case of portal technical malfunction or forgetting to log attendance, notify tech support or your manager before 10:00 AM to register manually and avoid unexcused absence."

        sources.append({
            "document": "policy.text",
            "section_id": "12_TECHNICAL_ISSUES",
            "section_title": SECTION_METADATA["12_TECHNICAL_ISSUES"]["title_ar" if is_ar else "title_en"],
            "confidence": "98.5%",
            "exact_snippet": "- في حال مواجهة مشكلة تقنية في الموقع أو نسيان تسجيل الحضور، يجب إبلاغ الدعم الفني أو المدير المباشر قبل الساعة 10:00 صباحاً لتثبيت القيد يدوياً وتفادي احتساب الغياب."
        })

    # 14. Dress Code Policy
    # e.g., "شو نظام اللباس", "قواعد اللباس والمظهر", "هل يوجد للبس معين للموظف", "شو البس", "اللبس"
    elif any(k in q_norm for k in [
        "لبس", "اللبس", "للبس", "باللبس", "لباس", "اللباس", "للباس", "باللباس",
        "ملابس", "الملابس", "بالمابس", "للملابس", "مظهر", "المظهر", "بالمظهر", "للمظهر",
        "زي", "الزي", "بالزي", "للزي", "يونيفورم", "شو البس", "شو نلبس", "ايش نلبس",
        "كاجوال", "رسمي", "ثياب", "الثياب", "dress code", "attire", "outfit", "appearance"
    ]):
        if is_ar:
            answer = "يلتزم جميع الموظفين بالظهور بمظهر أنيق، مرتب، ولائق يعكس الصورة المهنية الراقية للشركة في جميع أيام العمل."
        else:
            answer = "All employees are required to maintain an elegant, neat, and proper professional appearance reflecting the company's high standards across all working days."

        sources.append({
            "document": "policy.text",
            "section_id": "13_DRESS_CODE_POLICY",
            "section_title": SECTION_METADATA["13_DRESS_CODE_POLICY"]["title_ar" if is_ar else "title_en"],
            "confidence": "99.0%",
            "exact_snippet": "- يلتزم جميع الموظفين بالظهور بمظهر أنيق، مرتب، ولائق يعكس الصورة المهنية الراقية للشركة في جميع أيام العمل."
        })


    # 15. Gemini LLM Synthesis & Fallback (Grounded by Full policy.text + Role Context)
    if not answer:
        policy_full = get_policy_text()
        if is_ar:
            sys_prompt = f"""أنت المساعد الذكي لمؤسسة NexusLink Systems لنظام الحضور والدوام.
المستخدم الحالي بصلاحية: {user_role} ({'مدير نظام ومسؤول إداري' if user_role == 'admin' else 'موظف'}).
اللائحة الرسمية للدوام (policy.text):
{policy_full}

القواعد الإلزامية:
1. أجب بدقة واختصار شديد ومباشرة على قد السؤال فقط دون إطالة.
2. إذا كان المستخدم كـ Admin يسأل عن سياسات أو إجراءات، خاطبه بنبرة إدارية توجيهية.
3. افهم جميع اللهجات العربية والعامية الأردنية والخليجية ومصطلحات العمل.
4. إذا لم يكن السؤال متعلقاً بأنظمة الشركة والدوام أو كان غير مفهوم، اطلب منه بلطف توضيح سؤاله بخصوص سياسات الدوام أو الموظفين."""
        else:
            sys_prompt = f"""You are the intelligent HR & Operations Assistant for NexusLink Systems.
Current user role: {user_role} ({'Executive Administrator' if user_role == 'admin' else 'Employee'}).
Official Company Policy (policy.text):
{policy_full}

MANDATORY RULES:
1. Respond in 100% fluent, concise, professional English.
2. Answer precisely and directly to the question asked without unnecessary elaboration.
3. If the user is an Admin asking about policies, address them with executive clarity.
4. If the question is outside attendance policies or unclear, politely ask for clarification regarding shift hours, lateness, or excuse rules."""

        gemini_reply = call_gemini_llm(q_clean, system_instruction=sys_prompt, timeout=7)
        if gemini_reply:
            answer = gemini_reply
            chunks = retrieve_relevant_chunks(q_clean, top_k=1)
            if chunks:
                top_chunk = chunks[0]
                sources.append({
                    "document": "policy.text",
                    "section_id": top_chunk.get("chunk_id", "POLICY_DOC"),
                    "section_title": top_chunk.get("title_ar" if is_ar else "title_en", "NexusLink Policy"),
                    "confidence": "98.0%",
                    "exact_snippet": (top_chunk.get("content_ar" if is_ar else "content_en") or "")[:200]
                })

    # 16. Semantic Fallback (General RAG Vector Matching if Gemini unavailable)
    if not answer:
        chunks = retrieve_relevant_chunks(q_clean, top_k=2)
        if chunks:
            top_chunk = chunks[0]
            sec_title = top_chunk.get("title_ar" if is_ar else "title_en", "Policy Section")
            content = (top_chunk.get("content_ar" if is_ar else "content_en") or top_chunk.get("content", "")).strip()
            lines = [l.strip() for l in content.split('\n') if l.strip() and not l.strip().startswith('عنوان البند:') and not l.strip().startswith('Section Title:')]
            
            # Find the single most relevant line that answers the query
            best_line = ""
            best_score = -1.0
            q_tokens = set(tokenize_text(q_clean))
            for l in lines:
                l_clean = l.lstrip('-*• ').strip()
                l_tokens = set(tokenize_text(l_clean))
                overlap = len(q_tokens & l_tokens)
                if overlap > best_score and len(l_clean) > 8:
                    best_score = overlap
                    best_line = l_clean
                    
            if best_line and best_score > 0:
                answer = best_line
            elif lines:
                answer = lines[0].lstrip('-*• ').strip()
            else:
                answer = content[:150]
            
            for c in chunks:
                raw_c_title = c.get("title_ar" if is_ar else "title_en", "Policy")
                raw_c_content = (c.get("content_ar" if is_ar else "content_en") or c.get("content", "")).strip()
                score_pct = f"{round(c.get('score', 0.8) * 100, 1)}%"
                sources.append({
                    "document": "policy.text",
                    "section_id": c.get("chunk_id", "POLICY_DOC"),
                    "section_title": raw_c_title,
                    "confidence": score_pct,
                    "exact_snippet": raw_c_content
                })
        else:
            answer = "لم يتم العثور على بند مطابق في لائحة الدوام. يمكنك الاستفسار عن ساعات العمل، قواعد التأخير، أو شروط الأعذار." if is_ar else "No matching section found in policy. Please ask about shift hours, lateness rules, or excuse criteria."


    res_obj = {
        "success": True,
        "question": q_clean,
        "answer": answer,
        "sources": sources,
        "user_role": user_role,
        "engine": engine_name
    }
    if not (is_identity_query or is_cumulative_attendance_query or is_today_attendance_query or is_team_query):
        _QA_MEMORY_CACHE[cache_key] = res_obj
    return res_obj


