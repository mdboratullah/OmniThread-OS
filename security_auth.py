import sqlite3
import hashlib
import secrets
from config import DB_FILE

def init_auth_table():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS api_tokens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    role TEXT,
                    api_token TEXT,
                    status TEXT
                )''')
    # Default Admin Token creation if not exists
    cursor.execute("SELECT COUNT(*) FROM api_tokens")
    if cursor.fetchone()[0] == 0:
        default_token = "omnithread_sec_token_999"
        cursor.execute("INSERT INTO api_tokens (username, role, api_token, status) VALUES (?, ?, ?, ?)",
                       ("admin_master", "ENTERPRISE_ADMIN", default_token, "ACTIVE"))
    conn.commit()
    conn.close()

def verify_api_token(token):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT role, status FROM api_tokens WHERE api_token = ?", (token,))
    result = cursor.fetchone()
    conn.close()
    if result and result[1] == "ACTIVE":
        return True, result[0]
    return False, "UNAUTHORIZED"

init_auth_table()
