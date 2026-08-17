import os
import re
import math
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

def tokenize_text(text: str) -> List[str]:
    """Tokenize Arabic & English text into clean n-grams and words."""
    if not text:
        return []
    cleaned = re.sub(r'[^\w\s]', ' ', text.lower())
    words = cleaned.split()
    
    # Generate character 3-grams and 4-grams for robust Arabic fuzzy / morphological matching
    ngrams = list(words)
    for word in words:
        if len(word) >= 3:
            for i in range(len(word) - 2):
                ngrams.append(word[i:i+3])
        if len(word) >= 4:
            for i in range(len(word) - 3):
                ngrams.append(word[i:i+4])
    return ngrams

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
        "category": "schedule"
    },
    "02_LATENESS_RULES": {
        "title_ar": "ضوابط الحضور والتأخير والخصومات المالية",
        "title_en": "Lateness Rules, Grace Period & Deductions",
        "category": "penalties"
    },
    "03_ATTENDANCE_LOGGING": {
        "title_ar": "تسجيل الحضور والانصراف وإثبات الغياب",
        "title_en": "Attendance Tracking & Absence Rules",
        "category": "checkin"
    },
    "04_EXCUSE_TIME_WINDOW": {
        "title_ar": "المهلة الزمنية لتقديم طلبات الأعذار",
        "title_en": "Excuse Submission Window",
        "category": "time_limit"
    },
    "05_PROOF_REQUIREMENTS": {
        "title_ar": "شرط الإثبات والمرفقات الرسمية",
        "title_en": "Proof & Evidence Requirements",
        "category": "proof"
    },
    "06_EXCUSES_CLASSIFICATION": {
        "title_ar": "تصنيف الأعذار (المقبولة والمرفوضة)",
        "title_en": "Acceptable vs Unacceptable Excuses",
        "category": "classification"
    }
}

class PolicyChunk:
    def __init__(self, chunk_id: str, title_ar: str, title_en: str, category: str, content: str):
        self.chunk_id = chunk_id
        self.title_ar = title_ar
        self.title_en = title_en
        self.category = category
        self.content = content.strip()
        self.tokens = tokenize_text(f"{title_ar} {title_en} {content}")
        self.vector = compute_tf_vector(self.tokens)

    def to_dict(self) -> dict:
        return {
            "chunk_id": self.chunk_id,
            "title_ar": self.title_ar,
            "title_en": self.title_en,
            "category": self.category,
            "content": self.content
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
                "category": "general"
            })
            chunk = PolicyChunk(
                chunk_id=section_key,
                title_ar=meta["title_ar"],
                title_en=meta["title_en"],
                category=meta["category"],
                content=section_body.strip()
            )
            chunks.append(chunk)
    else:
        # Fallback if no section tags found
        chunk = PolicyChunk(
            chunk_id="00_MASTER_POLICY",
            title_ar="لائحة وسياسات الدوام العامة",
            title_en="General Attendance Policy",
            category="general",
            content=raw_text.strip()
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
            "content": chunk.content,
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
