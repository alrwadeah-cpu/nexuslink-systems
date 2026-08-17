import urllib.request
import urllib.parse
import json
import sys
import random

BASE_URL = "http://127.0.0.1:8000"

def run_tests():
    # Reconfigure stdout to use UTF-8 to handle Arabic text on Windows
    if hasattr(sys.stdout, 'reconfigure'):
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass

    print("=== NexusLink Attendance API Test Suite ===")
    
    # 0. Test unauthorized access (should fail)
    print("\n0. Testing unauthorized access to protected endpoints...")
    all_url = f"{BASE_URL}/api/attendance/all"
    try:
        req = urllib.request.Request(all_url)
        with urllib.request.urlopen(req) as response:
            print("ERROR: Successfully accessed protected endpoint without token!")
            sys.exit(1)
    except urllib.error.HTTPError as e:
        print(f"Status Code: {e.code} (Correctly rejected request)")
        assert e.code in [401, 403], f"Expected 401 or 403, got {e.code}"
    except Exception as e:
        print(f"Error during unauthorized check: {e}")
        sys.exit(1)

    # 1. Log in to acquire JWT token
    print("\n1. Testing POST /api/login to acquire JWT token")
    login_url = f"{BASE_URL}/api/login"
    login_data = urllib.parse.urlencode({
        "email": "admin@nexus.com",
        "password": "12345678"
    }).encode('utf-8')
    
    token = None
    try:
        req = urllib.request.Request(
            login_url, 
            data=login_data, 
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode('utf-8')
            print(f"Status Code: {response.status}")
            res_json = json.loads(res_body)
            assert res_json.get("success") is True, "Login failed"
            token = res_json.get("token")
            assert token is not None, "Token was not returned"
            print("Successfully authenticated and acquired JWT token.")
    except Exception as e:
        print(f"Error during login: {e}")
        sys.exit(1)

    headers_with_token = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    # Generate a random email to bypass same-day check-in limits in tests
    rand_id = random.randint(10000, 99999)
    test_email = f"test_user_{rand_id}@nexuslink.com"
    print(f"Randomized email generated for this test run: {test_email}")

    # 2. Create a check-in attendance record
    print("\n2. Testing POST /api/attendance/create (with JWT token)")
    create_url = f"{BASE_URL}/api/attendance/create"
    test_payload = {
        "email": test_email,
        "type": "check-in",
        "name": "Test User"
    }
    
    try:
        data = json.dumps(test_payload).encode('utf-8')
        req = urllib.request.Request(
            create_url, 
            data=data, 
            headers=headers_with_token
        )
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode('utf-8')
            print(f"Status Code: {response.status}")
            print(f"Response: {res_body}")
            res_json = json.loads(res_body)
            assert res_json.get("success") is True, "Create record failed"
    except Exception as e:
        print(f"Error during POST /api/attendance/create: {e}")
        sys.exit(1)
        
    # 3. Get all attendance logs
    print("\n3. Testing GET /api/attendance/all (with JWT token)")
    try:
        req = urllib.request.Request(all_url, headers=headers_with_token)
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode('utf-8')
            print(f"Status Code: {response.status}")
            records = json.loads(res_body)
            print(f"Found {len(records)} records in total.")
            # Verify if our test record is in the list
            found = False
            for record in records:
                if record.get("email") == test_email:
                    found = True
                    print(f"Found created record in database list: {record}")
                    break
            assert found, "Created record was not found in read list!"
    except Exception as e:
        print(f"Error during GET /api/attendance/all: {e}")
        sys.exit(1)

    # 4. Get logs specifically for the randomized test email
    print("\n4. Testing GET /api/logs (Single User, as admin)")
    logs_url = f"{BASE_URL}/api/logs?email={test_email}"
    try:
        req = urllib.request.Request(logs_url, headers=headers_with_token)
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode('utf-8')
            print(f"Status Code: {response.status}")
            logs = json.loads(res_body)
            print(f"Logs for {test_email}: {logs}")
            assert len(logs) > 0, "No logs found for the test user!"
    except Exception as e:
        print(f"Error during GET /api/logs: {e}")
        sys.exit(1)

    # 5. Test limit constraint: Try creating a SECOND check-in for the same user on the same day (should fail)
    print("\n5. Testing double check-in limit constraint (should fail with 400)")
    try:
        data = json.dumps(test_payload).encode('utf-8')
        req = urllib.request.Request(
            create_url, 
            data=data, 
            headers=headers_with_token
        )
        with urllib.request.urlopen(req) as response:
            print("ERROR: Successfully created duplicate attendance record!")
            sys.exit(1)
    except urllib.error.HTTPError as e:
        print(f"Status Code: {e.code} (Correctly rejected duplicate request)")
        assert e.code == 400, f"Expected status code 400, got {e.code}"
        res_body = e.read().decode('utf-8')
        res_json = json.loads(res_body)
        print(f"Server rejection details: {res_json}")
    except Exception as e:
        print(f"Error during duplicate check: {e}")
        sys.exit(1)
        
    # 6. Test registration API
    print("\n6. Testing POST /api/register to create a new user...")
    register_url = f"{BASE_URL}/api/register"
    reg_name = "New Test Employee"
    reg_email = f"emp_{random.randint(10000, 99999)}@nexuslink.com"
    reg_password = "securepassword123"
    
    register_data = urllib.parse.urlencode({
        "name": reg_name,
        "email": reg_email,
        "password": reg_password
    }).encode('utf-8')
    
    try:
        req = urllib.request.Request(
            register_url,
            data=register_data,
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode('utf-8')
            print(f"Status Code: {response.status}")
            res_json = json.loads(res_body)
            assert res_json.get("success") is True, f"Registration failed: {res_json}"
            print(f"Successfully registered user: {reg_name} ({reg_email})")
    except Exception as e:
        print(f"Error during registration: {e}")
        sys.exit(1)

    # 7. Test registration duplicate email prevention
    print("\n7. Testing POST /api/register with duplicate email (should return success=False)...")
    try:
        req = urllib.request.Request(
            register_url,
            data=register_data,
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode('utf-8')
            print(f"Status Code: {response.status}")
            res_json = json.loads(res_body)
            assert res_json.get("success") is False, "Duplicate email registration allowed!"
            assert res_json.get("error") == "email_exists", f"Expected error 'email_exists', got: {res_json.get('error')}"
            print("Duplicate email registration correctly rejected.")
    except Exception as e:
        print(f"Error during duplicate registration test: {e}")
        sys.exit(1)

    # 8. Test logging in with newly registered user
    print("\n8. Testing POST /api/login with newly registered credentials...")
    new_login_data = urllib.parse.urlencode({
        "email": reg_email,
        "password": reg_password
    }).encode('utf-8')
    try:
        req = urllib.request.Request(
            login_url,
            data=new_login_data,
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode('utf-8')
            print(f"Status Code: {response.status}")
            res_json = json.loads(res_body)
            assert res_json.get("success") is True, f"Login failed for newly registered user: {res_json}"
            assert res_json.get("token") is not None, "Token was not returned for new user login"
            print("Successfully authenticated using the new registered user credentials.")
    except Exception as e:
        print(f"Error logging in with new user: {e}")
        sys.exit(1)
        
    print("\n=== All JWT Security and API Tests Passed Successfully! ===")

if __name__ == "__main__":
    run_tests()
