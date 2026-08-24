import sqlite3
from config import DB_FILE

def init_all_tables():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS metrics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    cpu REAL,
                    ram REAL,
                    network REAL,
                    latency REAL,
                    risk REAL,
                    status TEXT,
                    rca TEXT
                )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS benchmark_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    total_requests INTEGER,
                    avg_latency_ms REAL,
                    status TEXT
                )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS audit_trail (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    user_role TEXT,
                    action_performed TEXT,
                    ip_address TEXT,
                    status TEXT
                )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS remediation_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    error_event TEXT,
                    remediation_action TEXT,
                    rollback_status TEXT
                )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS automated_test_reports (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    total_failures_detected INTEGER,
                    successfully_recovered INTEGER,
                    avg_mttr_seconds REAL,
                    report_status TEXT
                )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS predictive_ai_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    predicted_event TEXT,
                    confidence_score REAL,
                    time_to_impact_mins INTEGER,
                    approval_status TEXT
                )''')
    conn.commit()
    conn.close()
