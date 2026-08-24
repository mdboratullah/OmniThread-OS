import sqlite3
import os

PORT = int(os.environ.get("PORT", 8082))
DB_FILE = "enterprise_production.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS metrics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT, cpu REAL, ram REAL, 
                    network REAL, latency REAL, risk REAL, 
                    status TEXT, rca TEXT
                )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS benchmark_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT, total_requests INTEGER, avg_latency_ms REAL, status TEXT
                )''')
    conn.commit()
    conn.close()

init_db()
