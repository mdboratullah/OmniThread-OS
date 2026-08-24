import sqlite3
import secrets
from config import DB_FILE

def create_new_token(username, role):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Generate secure random API token
    token = f"omni_{secrets.token_hex(16)}"
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS api_tokens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    role TEXT,
                    api_token TEXT,
                    status TEXT
                )''')
                
    cursor.execute("INSERT INTO api_tokens (username, role, api_token, status) VALUES (?, ?, ?, ?)",
                   (username, role, token, "ACTIVE"))
    conn.commit()
    conn.close()
    print(f"Success! Generated new token for {username} ({role}): {token}")
    return token

def revoke_token(token):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE api_tokens SET status = 'REVOKED' WHERE api_token = ?", (token,))
    conn.commit()
    conn.close()
    print(f"Token revoked successfully.")

if __name__ == '__main__':
    # Example: Creating an operator token
    create_new_token("enterprise_operator", "OPERATOR")
