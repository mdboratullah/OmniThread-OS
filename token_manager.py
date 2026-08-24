import sqlite3
import secrets
import hashlib
import time
from config import DB_FILE

def init_token_table():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS api_tokens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    role TEXT,
                    token_hash TEXT,
                    expires_at INTEGER,
                    status TEXT
                )''')
    conn.commit()
    conn.close()

def create_secure_token(username, role, validity_days=30):
    init_token_table()
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    raw_token = f"omni_{secrets.token_hex(16)}"
    # Hash the token before storing in database for enterprise security
    token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
    
    # Calculate expiry timestamp (Current time + validity days in seconds)
    expires_at = int(time.time()) + (validity_days * 86400)
    
    cursor.execute("INSERT INTO api_tokens (username, role, token_hash, expires_at, status) VALUES (?, ?, ?, ?, ?)",
                   (username, role, token_hash, expires_at, "ACTIVE"))
    conn.commit()
    conn.close()
    
    print(f"Success! Generated secure token for {username} ({role}), valid for {validity_days} days.")
    print(f"RAW TOKEN (Save this securely, it won't be shown again): {raw_token}")
    return raw_token

if __name__ == '__main__':
    create_secure_token("enterprise_admin_pro", "ADMIN", validity_days=60)
