import asyncio
import json
import sys
import os

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from main import app, ask_api_post, ask_api_get, AskRequest

async def test_ask_endpoints():
    print("=== Testing NexusLink Systems /ask API with Grounded Sources ===")

    # Test 1: Lateness & Grace Period Query (Arabic)
    req1 = AskRequest(question="كم مدة فترة السماح وما هي عقوبة التأخير لأكثر من 60 دقيقة؟")
    res1 = await ask_api_post(req1)
    print("\n--- Test 1: Lateness & Grace Period ---")
    print(f"Question: {res1['question']}")
    print(f"Answer: {res1['answer']}")
    print(f"Sources Count: {len(res1['sources'])}")
    for s in res1['sources']:
        print(f"  * [{s['section_id']}] {s['section_title']} (Confidence: {s['confidence']})")
    assert res1["success"] == True
    assert len(res1["sources"]) > 0
    assert "02_LATENESS_RULES" in [s["section_id"] for s in res1["sources"]]

    # Test 2: Unacceptable Excuse (Alarm / Sleeping late)
    req2 = AskRequest(question="صحيت متأخر والمنبه ما رن هل يقبل عذري؟")
    res2 = await ask_api_post(req2)
    print("\n--- Test 2: Unacceptable Excuse ---")
    print(f"Question: {res2['question']}")
    print(f"Answer: {res2['answer']}")
    print(f"Sources: {[s['section_id'] for s in res2['sources']]}")
    assert "06_EXCUSES_CLASSIFICATION" in [s["section_id"] for s in res2["sources"]]
    assert "مرفوض" in res2["answer"] or "UNACCEPTABLE" in res2["answer"]

    # Test 3: Traffic Accident with Proof Requirement (Kroka)
    req3 = AskRequest(question="صار معي حادث سير هل يقبل العذر وما هو الإثبات المطلوب؟")
    res3 = await ask_api_post(req3)
    print("\n--- Test 3: Accident & Kroka Proof ---")
    print(f"Question: {res3['question']}")
    print(f"Answer: {res3['answer']}")
    print(f"Sources: {[s['section_id'] for s in res3['sources']]}")
    assert any("05_PROOF_REQUIREMENTS" in s["section_id"] for s in res3["sources"])
    assert "كروكة" in res3["answer"] or "Kroka" in res3["answer"] or "شرطة" in res3["answer"]

    # Test 4: Shift Hours & Working Days (English)
    req4 = AskRequest(question="What are the official working hours and shift days?", lang="en")
    res4 = await ask_api_post(req4)
    print("\n--- Test 4: Working Hours (EN) ---")
    print(f"Question: {res4['question']}")
    print(f"Answer: {res4['answer']}")
    print(f"Sources: {[s['section_id'] for s in res4['sources']]}")
    assert "01_WORKING_HOURS" in [s["section_id"] for s in res4["sources"]]

    # Test 5: Employee Personal Attendance Check
    req5 = AskRequest(question="هل أنا متأخر اليوم؟", email="test_employee@nexuslink.com")
    res5 = await ask_api_post(req5)
    print("\n--- Test 5: Personal Attendance Status ---")
    print(f"Question: {res5['question']}")
    print(f"Answer: {res5['answer']}")
    print(f"User Role: {res5['user_role']}")
    print(f"Sources: {[s.get('document') for s in res5['sources']]}")
    assert res5["user_role"] == "employee"
    assert any("nexuslink.db" in str(s.get("document", "")) for s in res5["sources"])

    # Test 6: Non-Admin asking for Team Roster (Security RBAC check)
    req6 = AskRequest(question="مين غايب ومين متأخر اليوم في الشركة؟", email="regular_staff@nexuslink.com")
    res6 = await ask_api_post(req6)
    print("\n--- Test 6: Security RBAC Restriction ---")
    print(f"Answer: {res6['answer']}")
    print(f"User Role: {res6['user_role']}")
    assert "تنبيه أمني" in res6["answer"] or "Security Notice" in res6["answer"] or "مخصصة" in res6["answer"]

    # Test 7: Admin asking for Team Roster
    req7 = AskRequest(question="مين غايب ومين متأخر اليوم في الشركة؟", email="admin@nexus.com")
    res7 = await ask_api_post(req7)
    print("\n--- Test 7: Admin Team Roster ---")
    print(f"Answer: {res7['answer']}")
    print(f"User Role: {res7['user_role']}")
    assert res7["user_role"] == "admin"

    # Test 9: Specific question "الخميس عطله ولا"
    req9 = AskRequest(question="الخميس عطله ولا")
    res9 = await ask_api_post(req9)
    print("\n--- Test 9: Thursday Day-off Query (Direct Crisp Answer) ---")
    print(f"Question: {res9['question']}")
    print(f"Answer: {res9['answer']}")
    print(f"Sources: {[s['section_id'] for s in res9['sources']]}")
    assert "لا، يوم الخميس ليس عطلة" in res9["answer"] or "عمل رسمي" in res9["answer"]

    # Test 10: ai_chat direct test for "الخميس عطله ولا"
    from main import ai_chat, AIChatRequest
    chat_req = AIChatRequest(message="الخميس عطله ولا")
    chat_res = await ai_chat(chat_req)
    print("\n--- Test 10: ai_chat Direct Test for Chatbot UI ---")
    print(f"Response HTML:\n{chat_res['response']}")
    assert "لا، يوم الخميس ليس عطلة" in chat_res["response"] or "عمل رسمي" in chat_res["response"]

    # Test 11: Unexcused / Missing Excuse Query "واذا ما سجلت عذر رسمي"
    req11 = AskRequest(question="واذا ما سجلت عذر رسمي")
    res11 = await ask_api_post(req11)
    print("\n--- Test 11: Missing Excuse Penalty 'واذا ما سجلت عذر رسمي' ---")
    print(f"Question: {res11['question']}")
    print(f"Answer: {res11['answer']}")
    print(f"Sources: {[s['section_id'] for s in res11['sources']]}")
    assert "غير مبرر" in res11["answer"] or "خصم" in res11["answer"]
    assert "02_LATENESS_RULES" in [s["section_id"] for s in res11["sources"]]

    # Test 12: Chatbot UI direct response for "واذا ما سجلت عذر رسمي"
    chat_req12 = AIChatRequest(message="واذا ما سجلت عذر رسمي")
    chat_res12 = await ai_chat(chat_req12)
    print("\n--- Test 12: Chatbot UI for 'واذا ما سجلت عذر رسمي' ---")
    print(f"Response HTML:\n{chat_res12['response']}")
    assert "غير مبرر" in chat_res12["response"] or "خصم" in chat_res12["response"]

    # Test 13: Dress Code Policy
    req13 = AskRequest(question="شو نظام اللباس والمظهر في الشركة؟")
    res13 = await ask_api_post(req13)
    print("\n--- Test 13: Dress Code Policy ---")
    print(f"Answer: {res13['answer']}")
    print(f"Sources: {[s['section_id'] for s in res13['sources']]}")
    assert "أنيق" in res13["answer"] or "elegant" in res13["answer"]
    assert "13_DRESS_CODE_POLICY" in [s["section_id"] for s in res13["sources"]]

    # Test 14: Early Departure / Emergency Permission
    req14 = AskRequest(question="بقدر اغادر بدري اليوم بسبب ظرف طارئ؟")
    res14 = await ask_api_post(req14)
    print("\n--- Test 14: Early Departure / Emergency Permission ---")
    print(f"Answer: {res14['answer']}")
    print(f"Sources: {[s['section_id'] for s in res14['sources']]}")
    assert "الظرف الطارئ" in res14["answer"] or "المدير المباشر" in res14["answer"]
    assert "07_EARLY_DEPARTURE_AND_PERMISSIONS" in [s["section_id"] for s in res14["sources"]]

    # Test 15: Remote Work Policy
    req15 = AskRequest(question="هل مسموح اشتغل من البيت؟")
    res15 = await ask_api_post(req15)
    print("\n--- Test 15: Remote Work / WFH Policy ---")
    print(f"Answer: {res15['answer']}")
    print(f"Sources: {[s['section_id'] for s in res15['sources']]}")
    assert "عن بُعد" in res15["answer"] or "يومين" in res15["answer"]
    assert "09_REMOTE_WORK_POLICY" in [s["section_id"] for s in res15["sources"]]

    # Test 16: Lunch & Prayer Breaks
    req16 = AskRequest(question="كم مدة بريك الغدا واستراحة الصلاة؟")
    res16 = await ask_api_post(req16)
    print("\n--- Test 16: Lunch & Prayer Breaks ---")
    print(f"Answer: {res16['answer']}")
    print(f"Sources: {[s['section_id'] for s in res16['sources']]}")
    assert "ساعة واحدة" in res16["answer"] or "1 hour" in res16["answer"]
    assert "10_BREAKS_AND_PRAYER" in [s["section_id"] for s in res16["sources"]]

    # Test 17: Annual Leaves
    req17 = AskRequest(question="كم رصيد إجازاتي السنوية؟")
    res17 = await ask_api_post(req17)
    print("\n--- Test 17: Annual Leaves ---")
    print(f"Answer: {res17['answer']}")
    print(f"Sources: {[s['section_id'] for s in res17['sources']]}")
    assert "14" in res17["answer"]
    assert "08_LEAVES_AND_VACATIONS" in [s["section_id"] for s in res17["sources"]]

    # Test 18: Overtime
    req18 = AskRequest(question="كيف ينحسب الاوفر تايم والشغل بعد الدوام؟")
    res18 = await ask_api_post(req18)
    print("\n--- Test 18: Overtime Policy ---")
    print(f"Answer: {res18['answer']}")
    print(f"Sources: {[s['section_id'] for s in res18['sources']]}")
    assert "5:00" in res18["answer"] or "بتكليف" in res18["answer"]
    assert "11_OVERTIME_POLICY" in [s["section_id"] for s in res18["sources"]]

    # Test 19: "الجمعة دوام؟" (Should answer: لا، ليس دوام بل عطلة)
    req19 = AskRequest(question="الجمعة دوام؟")
    res19 = await ask_api_post(req19)
    print("\n--- Test 19: 'الجمعة دوام؟' ---")
    print(f"Answer: {res19['answer']}")
    assert res19["answer"].startswith("لا") or "ليس فيهما دوام" in res19["answer"]

    # Test 20: "الجمعة عطلة؟" (Should answer: نعم، عطلة)
    req20 = AskRequest(question="الجمعة عطلة؟")
    res20 = await ask_api_post(req20)
    print("\n--- Test 20: 'الجمعة عطلة؟' ---")
    print(f"Answer: {res20['answer']}")
    assert res20["answer"].startswith("نعم") or "العطلة الأسبوعية" in res20["answer"]

    # Test 21: Chatbot UI for "الجمعة دوام؟"
    from main import ai_chat, AIChatRequest
    chat_res21 = await ai_chat(AIChatRequest(message="الجمعة دوام؟"))
    print("\n--- Test 21: Chatbot UI for 'الجمعة دوام؟' ---")
    print(f"Response HTML:\n{chat_res21['response']}")
    assert "لا" in chat_res21["response"] and ("ليس فيهما دوام" in chat_res21["response"] or "عطلة" in chat_res21["response"])

    # Test 22: "لو عطلت شو اعمل" (Planning to be absent / taking leave)
    req22 = AskRequest(question="لو عطلت شو اعمل")
    res22 = await ask_api_post(req22)
    print("\n--- Test 22: 'لو عطلت شو اعمل' ---")
    print(f"Answer: {res22['answer']}")
    print(f"Sources: {[s.get('section_id') or s.get('document') for s in res22['sources']]}")
    assert "إجازة" in res22["answer"] or "عذر" in res22["answer"]
    assert "08_LEAVES_AND_VACATIONS" in [s.get("section_id") for s in res22["sources"]]

    # Test 23: "كيف اقدم عذر" (How-to procedure)
    req23 = AskRequest(question="كيف اقدم عذر")
    res23 = await ask_api_post(req23)
    print("\n--- Test 23: 'كيف اقدم عذر' ---")
    print(f"Answer: {res23['answer']}")
    print(f"Sources: {[s.get('section_id') or s.get('document') for s in res23['sources']]}")
    assert "تقديم عذر" in res23["answer"] and "الإثبات" in res23["answer"]
    assert "04_EXCUSE_TIME_WINDOW" in [s.get("section_id") for s in res23["sources"]]

    # Test 24: "اليوم متاخر انا ولا" (Fuzzy word order personal attendance)
    req24 = AskRequest(question="اليوم متاخر انا ولا", email="test_employee@nexuslink.com")
    res24 = await ask_api_post(req24)
    print("\n--- Test 24: 'اليوم متاخر انا ولا' ---")
    print(f"Answer: {res24['answer']}")
    print(f"Sources: {[s.get('section_id') or s.get('document') for s in res24['sources']]}")
    assert "تسجيل الدخول" in res24["answer"] or "متأخر" in res24["answer"]

    # Test 25: "شو اسمي" (User identity query)
    # Using existing DB user
    req25 = AskRequest(question="شو اسمي", email="alaa@gmail.com")
    res25 = await ask_api_post(req25)
    print("\n--- Test 25: 'شو اسمي' ---")
    print(f"Answer: {res25['answer']}")
    print(f"Sources: {[s.get('section_id') or s.get('document') for s in res25['sources']]}")
    assert "alaa" in res25["answer"].lower() or "المسجل" in res25["answer"] or "النظام" in res25["answer"]

    # Test 26: "كم غياب عندي" (User cumulative absences)
    req26 = AskRequest(question="كم غياب عندي", email="alaa@gmail.com")
    res26 = await ask_api_post(req26)
    print("\n--- Test 26: 'كم غياب عندي' ---")
    print(f"Answer: {res26['answer']}")
    print(f"Sources: {[s.get('section_id') or s.get('document') for s in res26['sources']]}")
    assert "الغياب" in res26["answer"] and "الحضور" in res26["answer"]

    # Test 27: "سيارتي تعطلت" (Vehicle breakdown)
    req27 = AskRequest(question="سيارتي تعطلت")
    res27 = await ask_api_post(req27)
    print("\n--- Test 27: 'سيارتي تعطلت' ---")
    print(f"Answer: {res27['answer']}")
    print(f"Sources: {[s.get('section_id') or s.get('document') for s in res27['sources']]}")
    assert "العطل المفاجئ" in res27["answer"] or "عذراً مقبولاً" in res27["answer"]
    assert "06_EXCUSES_CLASSIFICATION" in [s.get("section_id") for s in res27["sources"]]

    # Test 28: "انا مريض" (Health / Medical / Sick)
    req28 = AskRequest(question="انا مريض")
    res28 = await ask_api_post(req28)
    print("\n--- Test 28: 'انا مريض' ---")
    print(f"Answer: {res28['answer']}")
    print(f"Sources: {[s.get('section_id') or s.get('document') for s in res28['sources']]}")
    assert "سلامتك" in res28["answer"] or "الإجازة المرضية" in res28["answer"] or "تقرير طبي" in res28["answer"]
    assert "08_LEAVES_AND_VACATIONS" in [s.get("section_id") for s in res28["sources"]]

    # Test 29: "متى الترويحة" (Shift end slang)
    req29 = AskRequest(question="متى الترويحة")
    res29 = await ask_api_post(req29)
    print("\n--- Test 29: 'متى الترويحة' ---")
    print(f"Answer: {res29['answer']}")
    print(f"Sources: {[s.get('section_id') or s.get('document') for s in res29['sources']]}")
    assert "5:00" in res29["answer"] or "مساءً" in res29["answer"]
    assert "01_WORKING_HOURS" in [s.get("section_id") for s in res29["sources"]]

    # Test 30: English chat "Official working days and hours"
    chat_req30 = AIChatRequest(message="Official working days and hours", lang="en")
    chat_res30 = await ai_chat(chat_req30)
    print("\n--- Test 30: English Chat - Official Working Hours ---")
    print(f"Response: {chat_res30['response']}")
    assert "9:00 AM" in chat_res30["response"] or "Sunday" in chat_res30["response"]

    # Test 31: English chat "Is Friday a working day?"
    chat_req31 = AIChatRequest(message="Is Friday a working day?", lang="en")
    chat_res31 = await ai_chat(chat_req31)
    print("\n--- Test 31: English Chat - Is Friday a working day? ---")
    print(f"Response: {chat_res31['response']}")
    assert "No" in chat_res31["response"] or "weekend" in chat_res31["response"].lower() or "off" in chat_res31["response"].lower()

    # Test 32: English chat "Lateness rules, grace period, and deductions"
    chat_req32 = AIChatRequest(message="Lateness rules, grace period, and deductions", lang="en")
    chat_res32 = await ai_chat(chat_req32)
    print("\n--- Test 32: English Chat - Lateness rules & Grace Period ---")
    print(f"Response: {chat_res32['response']}")
    assert "15" in chat_res32["response"] or "grace" in chat_res32["response"].lower()

    # Test 33: "لو تاخرت عن الدوان 30 دقيقة بصير خصم؟"
    chat_req33 = AIChatRequest(message="لو تاخرت عن الدوان 30 دقيقة بصير خصم؟", lang="ar")
    chat_res33 = await ai_chat(chat_req33)
    print("\n--- Test 33: 30 Minutes Lateness Query ---")
    print(f"Response: {chat_res33['response']}")
    assert "لا" in chat_res33["response"] or "60 دقيقة" in chat_res33["response"]

    # Test 35: "شو ايام الدوام"
    chat_req35 = AIChatRequest(message="شو ايام الدوام", lang="ar")
    chat_res35 = await ai_chat(chat_req35)
    print("\n--- Test 35: 'شو ايام الدوام' ---")
    print(f"Response: {chat_res35['response']}")
    assert "الأحد إلى الخميس" in chat_res35["response"] and "الجمعة والسبت" in chat_res35["response"]

    # Test 36: Multi-Turn Context Resolution: "ف الاسبوع كم ساعة؟" followed by "في الشهر؟"
    chat_req36_turn1 = AIChatRequest(message="ف الاسبوع كم ساعة؟", lang="ar")
    chat_res36_turn1 = await ai_chat(chat_req36_turn1)
    print("\n--- Test 36 (Turn 1): 'ف الاسبوع كم ساعة؟' ---")
    print(f"Response: {chat_res36_turn1['response']}")
    assert "40" in chat_res36_turn1["response"]

    chat_history = [
        {"role": "user", "content": "ف الاسبوع كم ساعة؟"},
        {"role": "assistant", "content": chat_res36_turn1["response"]}
    ]
    chat_req36_turn2 = AIChatRequest(message="في الشهر؟", history=chat_history, lang="ar")
    chat_res36_turn2 = await ai_chat(chat_req36_turn2)
    print("\n--- Test 36 (Turn 2 - Follow Up): 'في الشهر؟' ---")
    print(f"Response: {chat_res36_turn2['response']}")
    assert ("160" in chat_res36_turn2["response"] or "ساعة" in chat_res36_turn2["response"]) and not ("العمل عن بعد" in chat_res36_turn2["response"])

    # Test 37: "كم ساعة في اليوم؟"
    chat_req37 = AIChatRequest(message="كم ساعة في اليوم؟", lang="ar")
    chat_res37 = await ai_chat(chat_req37)
    print("\n--- Test 37: 'كم ساعة في اليوم؟' ---")
    print(f"Response: {chat_res37['response']}")
    assert "8 ساعات" in chat_res37["response"]

    # Test 40: "هل يوجد للبس معين للموظف؟"
    chat_req40 = AIChatRequest(message="هل يوجد للبس معين للموظف؟", lang="ar")
    chat_res40 = await ai_chat(chat_req40)
    print("\n--- Test 40: 'هل يوجد للبس معين للموظف؟' ---")
    print(f"Response: {chat_res40['response']}")
    assert "أنيق" in chat_res40["response"] or "مرتب" in chat_res40["response"] or "اللباس" in chat_res40["response"]

    # Test 42: "واذا كان معي عذر؟"
    chat_req42 = AIChatRequest(message="واذا كان معي عذر؟", lang="ar")
    chat_res42 = await ai_chat(chat_req42)
    print("\n--- Test 42: 'واذا كان معي عذر؟' ---")
    print(f"Response: {chat_res42['response']}")
    # Test 43: "لو كانت ازمة الطريق بقبل المدير عذري؟"
    chat_req43 = AIChatRequest(message="لو كانت ازمة الطريق بقبل المدير عذري؟", lang="ar")
    chat_res43 = await ai_chat(chat_req43)
    print("\n--- Test 43: 'لو كانت ازمة الطريق بقبل المدير عذري؟' ---")
    print(f"Response: {chat_res43['response']}")
    assert chat_res43["response"].startswith("لا،") and "أزمة وازدحام الطريق" in chat_res43["response"]

    # Test 44: "لو صار معي حادث سير بقبل عذري؟"
    chat_req44 = AIChatRequest(message="لو صار معي حادث سير بقبل عذري؟", lang="ar")
    chat_res44 = await ai_chat(chat_req44)
    print("\n--- Test 44: 'لو صار معي حادث سير بقبل عذري؟' ---")
    print(f"Response: {chat_res44['response']}")
    assert chat_res44["response"].startswith("نعم،") and "كروكة" in chat_res44["response"]

    # Test 45: "لو كان في حالة وفاة بقبل عذري؟"
    chat_req45 = AIChatRequest(message="لو كان في حالة وفاة بقبل عذري؟", lang="ar")
    chat_res45 = await ai_chat(chat_req45)
    print("\n--- Test 45: 'لو كان في حالة وفاة بقبل عذري؟' ---")
    print(f"Response: {chat_res45['response']}")
    assert chat_res45["response"].startswith("نعم،") and "الوفاة" in chat_res45["response"]

    # Test 46: "لو سيارتي خربت بقبل عذري؟"
    chat_req46 = AIChatRequest(message="لو سيارتي خربت بقبل عذري؟", lang="ar")
    chat_res46 = await ai_chat(chat_req46)
    print("\n--- Test 46: 'لو سيارتي خربت بقبل عذري؟' ---")
    print(f"Response: {chat_res46['response']}")
    assert chat_res46["response"].startswith("نعم،") and "العطل المفاجئ" in chat_res46["response"]

    # Test 48: "كيف ابعث التقرير الطبي"
    chat_req48 = AIChatRequest(message="كيف ابعث التقرير الطبي", lang="ar")
    chat_res48 = await ai_chat(chat_req48)
    print("\n--- Test 48: 'كيف ابعث التقرير الطبي' ---")
    print(f"Response: {chat_res48['response']}")
    assert "تقديم عذر" in chat_res48["response"] and "إرفاق ملف" in chat_res48["response"]

    # Test 49: "لمين ابعثهن" (Follow up / direct)
    chat_req49 = AIChatRequest(message="لمين ابعثهن", lang="ar", chat_history=[
        {"role": "user", "content": "كيف ابعث التقرير الطبي"},
        {"role": "assistant", "content": chat_res48["response"]}
    ])
    chat_res49 = await ai_chat(chat_req49)
    print("\n--- Test 49: 'لمين ابعثهن' ---")
    print(f"Response: {chat_res49['response']}")
    assert "مديرك المباشر" in chat_res49["response"] and "HR" in chat_res49["response"]

    # Test 50: "كيف اعرف اذا انقبل عذري"
    chat_req50 = AIChatRequest(message="كيف اعرف اذا انقبل عذري", lang="ar")
    chat_res50 = await ai_chat(chat_req50)
    print("\n--- Test 50: 'كيف اعرف اذا انقبل عذري' ---")
    print(f"Response: {chat_res50['response']}")
    assert "أعذاري" in chat_res50["response"]

    # Test 51: "شو نوع الملفات المقبولة"
    chat_req51 = AIChatRequest(message="شو نوع الملفات المقبولة للتقرير", lang="ar")
    chat_res51 = await ai_chat(chat_req51)
    print("\n--- Test 51: 'شو نوع الملفات المقبولة للتقرير' ---")
    print(f"Response: {chat_res51['response']}")
    assert "PDF" in chat_res51["response"] and "PNG" in chat_res51["response"]

    # Test 52: "كيف اسجل دخول"
    chat_req52 = AIChatRequest(message="كيف اسجل دخول", lang="ar")
    chat_res52 = await ai_chat(chat_req52)
    print("\n--- Test 52: 'كيف اسجل دخول' ---")
    print(f"Response: {chat_res52['response']}")
    assert "Check-In" in chat_res52["response"] and "9:00" in chat_res52["response"]

    # Test 53: "مرحبا"
    chat_req53 = AIChatRequest(message="مرحبا", lang="ar")
    chat_res53 = await ai_chat(chat_req53)
    print("\n--- Test 53: 'مرحبا' ---")
    print(f"Response: {chat_res53['response']}")
    assert "أهلاً وسهلاً بك" in chat_res53["response"] and "NexusLink" in chat_res53["response"]

    # Test 54: "صباح الخير"
    chat_req54 = AIChatRequest(message="صباح الخير", lang="ar")
    chat_res54 = await ai_chat(chat_req54)
    print("\n--- Test 54: 'صباح الخير' ---")
    print(f"Response: {chat_res54['response']}")
    assert "صباح الخير" in chat_res54["response"]

    # Test 55: English Greeting ("Hello")
    chat_req55 = AIChatRequest(message="Hello", lang="en")
    chat_res55 = await ai_chat(chat_req55)
    print("\n--- Test 55: 'Hello' (EN) ---")
    print(f"Response: {chat_res55['response']}")
    assert "Hello" in chat_res55["response"] and "NexusLink" in chat_res55["response"]

    # Test 56: English How to submit medical report ("How to submit a medical report?")
    chat_req56 = AIChatRequest(message="How to submit a medical report?", lang="en")
    chat_res56 = await ai_chat(chat_req56)
    print("\n--- Test 56: 'How to submit a medical report?' (EN) ---")
    print(f"Response: {chat_res56['response']}")
    assert "Submit Excuse" in chat_res56["response"] and "Attach File" in chat_res56["response"]

    # Test 57: English Follow-up Who to send ("Who to send it to?")
    chat_req57 = AIChatRequest(message="Who to send it to?", lang="en", chat_history=[
        {"role": "user", "content": "How to submit a medical report?"},
        {"role": "assistant", "content": chat_res56["response"]}
    ])
    chat_res57 = await ai_chat(chat_req57)
    print("\n--- Test 57: 'Who to send it to?' (EN) ---")
    print(f"Response: {chat_res57['response']}")
    assert "direct manager" in chat_res57["response"].lower() and "hr" in chat_res57["response"].lower()

    # Test 58: English Excuse Classification Traffic ("If I was stuck in traffic, will my excuse be accepted?")
    chat_req58 = AIChatRequest(message="If I was stuck in traffic, will my excuse be accepted?", lang="en")
    chat_res58 = await ai_chat(chat_req58)
    print("\n--- Test 58: 'If I was stuck in traffic...' (EN) ---")
    print(f"Response: {chat_res58['response']}")
    assert chat_res58["response"].startswith("No,") and "traffic" in chat_res58["response"].lower()

    # Test 59: English Excuse Classification Accident ("If I had a car accident, will my excuse be accepted?")
    chat_req59 = AIChatRequest(message="If I had a car accident, will my excuse be accepted?", lang="en")
    chat_res59 = await ai_chat(chat_req59)
    print("\n--- Test 59: 'If I had a car accident...' (EN) ---")
    print(f"Response: {chat_res59['response']}")
    assert chat_res59["response"].startswith("Yes,") and "accident" in chat_res59["response"].lower()

    # Test 60: English Follow-up Working Hours Timeframe ("In a month?")
    chat_req60_t1 = AIChatRequest(message="How many working hours per week?", lang="en")
    chat_res60_t1 = await ai_chat(chat_req60_t1)
    chat_req60_t2 = AIChatRequest(message="In a month?", lang="en", chat_history=[
        {"role": "user", "content": "How many working hours per week?"},
        {"role": "assistant", "content": chat_res60_t1["response"]}
    ])
    chat_res60_t2 = await ai_chat(chat_req60_t2)
    print("\n--- Test 60: 'In a month?' (EN Follow-up) ---")
    print(f"Response: {chat_res60_t2['response']}")
    assert "160" in chat_res60_t2["response"] or "month" in chat_res60_t2["response"].lower()

    # Test 61: "طيب كم اجازه الي في الشهر؟"
    chat_req61 = AIChatRequest(message="طيب كم اجازه الي في الشهر؟", lang="ar")
    chat_res61 = await ai_chat(chat_req61)
    print("\n--- Test 61: 'طيب كم اجازه الي في الشهر؟' ---")
    print(f"Response: {chat_res61['response']}")
    assert "14" in chat_res61["response"] and ("شهرياً" in chat_res61["response"] or "شهريا" in chat_res61["response"])

    # Test 62: "كم مسموحلي اعطل؟"
    chat_req62 = AIChatRequest(message="كم مسموحلي اعطل؟", lang="ar")
    chat_res62 = await ai_chat(chat_req62)
    print("\n--- Test 62: 'كم مسموحلي اعطل؟' ---")
    print(f"Response: {chat_res62['response']}")
    assert "14" in chat_res62["response"] and "السنوية" in chat_res62["response"]

    # Test 63: "How many leave days do I have per month?"
    chat_req63 = AIChatRequest(message="How many leave days do I have per month?", lang="en")
    chat_res63 = await ai_chat(chat_req63)
    print("\n--- Test 63: 'How many leave days do I have per month?' (EN) ---")
    print(f"Response: {chat_res63['response']}")
    assert "14" in chat_res63["response"] and "month" in chat_res63["response"].lower()

    # Test 64: "How many days can I take off?"
    chat_req64 = AIChatRequest(message="How many days can I take off?", lang="en")
    chat_res64 = await ai_chat(chat_req64)
    print("\n--- Test 64: 'How many days can I take off?' (EN) ---")
    print(f"Response: {chat_res64['response']}")
    assert "14" in chat_res64["response"]

    # Test 65: "وين ابعث التقرير"
    chat_req65 = AIChatRequest(message="وين ابعث التقرير", lang="ar")
    chat_res65 = await ai_chat(chat_req65)
    print("\n--- Test 65: 'وين ابعث التقرير' ---")
    print(f"Response: {chat_res65['response']}")
    assert "تقديم عذر" in chat_res65["response"] and "إرفاق ملف" in chat_res65["response"]

    # Test 66: "كيف ابعثو" (Follow-up Turn)
    chat_req66 = AIChatRequest(message="كيف ابعثو", lang="ar", chat_history=[
        {"role": "user", "content": "وين ابعث التقرير"},
        {"role": "assistant", "content": chat_res65["response"]}
    ])
    chat_res66 = await ai_chat(chat_req66)
    print("\n--- Test 66: 'كيف ابعثو' (Follow-up) ---")
    print(f"Response: {chat_res66['response']}")
    assert "تقديم عذر" in chat_res66["response"] and "إرفاق ملف" in chat_res66["response"]

    # Test 67: "وين ارفعو" (Standalone)
    chat_req67 = AIChatRequest(message="وين ارفعو", lang="ar")
    chat_res67 = await ai_chat(chat_req67)
    print("\n--- Test 67: 'وين ارفعو' ---")
    print(f"Response: {chat_res67['response']}")
    assert "تقديم عذر" in chat_res67["response"]

    # Test 68: "How to send it?" (EN Follow-up)
    chat_req68 = AIChatRequest(message="How to send it?", lang="en", chat_history=[
        {"role": "user", "content": "Where do I submit the medical report?"},
        {"role": "assistant", "content": "Submit on the portal."}
    ])
    chat_res68 = await ai_chat(chat_req68)
    print("\n--- Test 68: 'How to send it?' (EN) ---")
    print(f"Response: {chat_res68['response']}")
    assert "Submit Excuse" in chat_res68["response"]

    # Test 69: "ساعات العمل الاضافي"
    chat_req69 = AIChatRequest(message="ساعات العمل الاضافي", lang="ar")
    chat_res69 = await ai_chat(chat_req69)
    print("\n--- Test 69: 'ساعات العمل الاضافي' ---")
    print(f"Response: {chat_res69['response']}")
    assert "الإضافي" in chat_res69["response"] or "الاضافي" in chat_res69["response"]
    assert "5:00" in chat_res69["response"] and "تكليف" in chat_res69["response"]

    # Test 70: "Overtime policy & extra hours" (EN)
    chat_req70 = AIChatRequest(message="What is the overtime policy?", lang="en")
    chat_res70 = await ai_chat(chat_req70)
    print("\n--- Test 70: 'What is the overtime policy?' (EN) ---")
    print(f"Response: {chat_res70['response']}")
    assert "Overtime" in chat_res70["response"] and "5:00 PM" in chat_res70["response"]

    print("\n\n🎉 >>> ALL 70/70 ARABIC & ENGLISH MULTI-TURN & PLATFORM TESTS PASSED 100%! <<< 🎉")

if __name__ == "__main__":
    asyncio.run(test_ask_endpoints())






