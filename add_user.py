
import sqlite3

def add_new_user():
    print("=== NexusLink Systems: Add New User to SQL DB ===")
    email = input("Enter Employee Email (e.g. name@nexuslink.com): ").strip()
    name = input("Enter Employee Full Name: ").strip()
    password = input("Enter Password: ").strip()

    if not email or not name or not password:
        print("Error: All fields are required!")
        return

    db_path = "nexuslink.db"
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Insert statement
        cursor.execute(
            "INSERT INTO user3 (email, name, password) VALUES (?, ?, ?)", 
            (email.lower(), name, password)
        )
        conn.commit()
        conn.close()
        
        print(f"\n[SUCCESS] Successfully added {name} ({email}) to the database!")
        print("They can now log in to the dashboard immediately.")
    except Exception as e:
        print(f"\n[ERROR] Failed to insert user: {e}")

if __name__ == "__main__":
    add_new_user()
