import urllib.request
import urllib.parse
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_URL = "http://127.0.0.1:8000"

def post_form(url, form_dict):
    data_encoded = urllib.parse.urlencode(form_dict).encode('utf-8')
    req = urllib.request.Request(url, data=data_encoded, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def post_json(url, data, token=None):
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
    if token:
        req.add_header('Authorization', f'Bearer {token}')
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def test_ai_bot():
    print("=== Testing Admin AI Assistant Intelligence Bot ===")
    
    # 1. Login as Admin
    admin_login = post_form(f"{BASE_URL}/api/login", {"email": "admin-faisal@gmail.com", "password": "12345678"})
    admin_token = admin_login["token"]
    print("[OK] Logged in as Admin.")
    
    # 2. Login as Employee
    emp_login = post_form(f"{BASE_URL}/api/login", {"email": "f@gmail.com", "password": "12345678"})
    emp_token = emp_login["token"]
    print("[OK] Logged in as Employee.")
    
    # Test 1: Admin asking "مين موجود اليوم؟"
    res1 = post_json(f"{BASE_URL}/api/ai/chat", {"message": "مين موجود اليوم؟"}, admin_token)
    print("\n--- Admin Query: 'مين موجود اليوم؟' ---")
    print(res1["response"])
    
    # Test 2: Admin asking "مين غايب اليوم؟"
    res2 = post_json(f"{BASE_URL}/api/ai/chat", {"message": "مين غايب اليوم؟"}, admin_token)
    print("\n--- Admin Query: 'مين غايب اليوم؟' ---")
    print(res2["response"])

    # Test 3: Admin asking for specific employee "سجل الموظف علاء"
    res3 = post_json(f"{BASE_URL}/api/ai/chat", {"message": "سجل الموظف علاء"}, admin_token)
    print("\n--- Admin Query: 'سجل الموظف علاء' ---")
    print(res3["response"])

    # Test 4: Employee trying to query employee intelligence data (Should be blocked!)
    res4 = post_json(f"{BASE_URL}/api/ai/chat", {"message": "مين غايب اليوم كادر الموظفين؟"}, emp_token)
    print("\n--- Employee Query Attempt (Should be blocked): ---")
    print(res4["response"])

if __name__ == "__main__":
    test_ai_bot()
