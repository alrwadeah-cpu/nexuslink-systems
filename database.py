import sqlite3
import time

import os

DB_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nexuslink.db')

def get_db_connection():
    conn = sqlite3.connect(DB_NAME, timeout=30.0)
    try:
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA busy_timeout=30000;")
    except Exception:
        pass
    conn.row_factory = sqlite3.Row
    return conn

def execute_query(query, params=()):
    for attempt in range(5):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return
        except sqlite3.OperationalError as e:
            if "locked" in str(e).lower() and attempt < 4:
                time.sleep(0.1 * (attempt + 1))
                continue
            raise
        finally:
            if conn:
                try:
                    conn.close()
                except Exception:
                    pass

def fetch_query(query, params=()):
    for attempt in range(5):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except sqlite3.OperationalError as e:
            if "locked" in str(e).lower() and attempt < 4:
                time.sleep(0.1 * (attempt + 1))
                continue
            raise
        finally:
            if conn:
                try:
                    conn.close()
                except Exception:
                    pass