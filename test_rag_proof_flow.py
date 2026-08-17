import os
import sys
import json
import asyncio
from unittest.mock import MagicMock
from starlette.datastructures import UploadFile, Headers

# Ensure python io encoding
os.environ["PYTHONIOENCODING"] = "utf-8"

from main import submit_excuse, get_all_excuses, get_my_excuses, ai_chat, AIChatRequest, ExcuseSubmitRequest
from rag_engine import evaluate_semantic_excuse

async def run_all_tests():
    print("=== Testing NexusLink Systems RAG & Proof Attachment Engine ===")

    # 1. Test evaluate_semantic_excuse without proof (> 15m delay)
    eval_accident_no_proof = evaluate_semantic_excuse("صار معي حادث سير بالطريق واصطدمت بالسيارة", lateness_mins=30, has_attachment=False)
    assert eval_accident_no_proof["recommendation"] == "REQUIRE_PROOF", f"Expected REQUIRE_PROOF, got {eval_accident_no_proof}"
    print(" [1/5] RAG Accident without attachment -> REQUIRE_PROOF correctly.")

    # 2. Test evaluate_semantic_excuse with proof attachment
    eval_accident_with_proof = evaluate_semantic_excuse("صار معي حادث سير بالطريق واصطدمت بالسيارة", lateness_mins=30, has_attachment=True)
    assert eval_accident_with_proof["recommendation"] == "APPROVE", f"Expected APPROVE, got {eval_accident_with_proof}"
    print(" [2/5] RAG Accident WITH attachment -> APPROVE correctly.")

    # 3. Test submit_excuse via JSON (medical with no attachment)
    req_json = MagicMock()
    req_json.headers = {"content-type": "application/json"}
    req_json.json = async_return({
        "email": "employee@nexuslink.com",
        "reason": "كنت بالطوارئ في المستشفى",
        "checkin_time": "10:00:00"
    })
    res3 = await submit_excuse(req_json, current_user={"email": "employee@nexuslink.com"})
    assert res3["success"] == True
    assert res3["ai_evaluation"]["recommendation"] == "REQUIRE_PROOF"
    print(" [3/5] submit_excuse JSON without proof -> REQUIRE_PROOF correctly.")

    # 4. Test submit_excuse via FormData with Kroka attachment
    fake_upload = UploadFile(filename="kroka_sketch_test.jpg", file=open("policy.text", "rb"))
    req_form = MagicMock()
    req_form.headers = {"content-type": "multipart/form-data"}
    form_data = {
        "email": "employee@nexuslink.com",
        "reason": "صار معي حادث سير على الدوار",
        "checkin_time": "10:30:00",
        "file": fake_upload
    }
    req_form.form = async_return(form_data)
    res4 = await submit_excuse(req_form, current_user={"email": "employee@nexuslink.com"})
    assert res4["success"] == True
    assert res4["status"] == "approved"
    assert res4["ai_evaluation"]["recommendation"] == "APPROVE"
    assert res4["attachment"] is not None
    assert "/uploads/proof_" in res4["attachment"]
    print(" [4/5] submit_excuse FormData with Kroka attachment -> APPROVE & attachment saved.")

    # 5. Test AI chat query for excuses with Kroka preview
    chat_req = AIChatRequest(message="شو وضع طلبات الأعذار والكروكة اليوم؟", email="admin@nexus.com")
    chat_res = await ai_chat(chat_req, current_user={"email": "admin@nexus.com"})
    assert chat_res["success"] == True
    assert "متابعة وتقييم طلبات الأعذار الذكية" in chat_res["response"]
    assert "معاينة وثيقة الإثبات" in chat_res["response"]
    print(" [5/5] ai_chat query returns excuse dossier with proof lightbox button.")

    print("\n>>> ALL 5/5 RAG PROOF & ATTACHMENT TESTS PASSED 100%! <<<")

def async_return(val):
    async def _f():
        return val
    return _f

if __name__ == "__main__":
    asyncio.run(run_all_tests())
