import os
import csv
import sqlite3

def main():
    db_path = "nexuslink.db"
    csv_file = "attendance_full_logs.csv"
    
    if not os.path.exists(db_path):
        print(f"Database {db_path} not found. Please run this script in the Site directory.")
        return

    # Connect to db
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Get user mappings (email -> name)
    cursor.execute("SELECT email, name FROM user3")
    user_rows = cursor.fetchall()
    user_map = {}
    for row in user_rows:
        email = row['email'].strip().lower() if row['email'] else ""
        name = row['name'].strip() if row['name'] else "غير معروف"
        user_map[email] = name
        
    # Also fetch from users table as fallback
    cursor.execute("SELECT email, name FROM users")
    users_rows = cursor.fetchall()
    for row in users_rows:
        email = row['email'].strip().lower() if row['email'] else ""
        name = row['name'].strip() if row['name'] else "غير معروف"
        if email not in user_map:
            user_map[email] = name
            
    # Always mapping admin fallback just in case
    user_map["admin@nexus.com"] = "Admin User"
    
    # Retrieve all attendance records
    cursor.execute("SELECT email, type, time FROM attendance ORDER BY id ASC")
    logs = cursor.fetchall()
    
    conn.close()
    
    print(f"Found {len(logs)} records in database.")
    
    # Format and write to Excel CSV
    try:
        with open(csv_file, mode="w", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["اسم الموظف", "البريد الإلكتروني", "الحركة", "التاريخ", "الوقت"])
            
            for log in logs:
                email = log['email']
                email_lower = email.strip().lower() if email else ""
                name = user_map.get(email_lower, "غير معروف")
                
                # Map type to Arabic
                log_type = log['type']
                type_ar = "تسجيل دخول" if log_type == "check-in" else "تسجيل خروج"
                
                # Parse datetime
                full_time = log['time']
                date_str = ""
                time_str = ""
                if full_time:
                    parts = full_time.split(" ")
                    if len(parts) >= 1:
                        date_str = parts[0]
                    if len(parts) >= 2:
                        time_str = parts[1]
                        
                writer.writerow([name, email, type_ar, date_str, time_str])
                
        print(f"Successfully wrote {len(logs)} records to {csv_file} with proper columns!")
    except PermissionError:
        print("\n[ERROR] Permission Denied: Please close 'attendance_full_logs.csv' in Excel or any other program and try again.")
        exit(1)

if __name__ == "__main__":
    main()
