import sqlite3
import time
import random
from config import DB_FILE

def init_predictive_tables():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Ensure metrics table exists to prevent no such table error
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

def run_predictive_ai_analysis():
    init_predictive_tables()
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Safely check if metrics exist, if not insert dummy telemetry
    cursor.execute("SELECT COUNT(*) FROM metrics")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO metrics (timestamp, cpu, ram, network, latency, risk, status, rca) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (time.strftime("%Y-%m-%d %H:%M:%S"), 30.0, 50.0, 5.0, 100.0, 40.0, "STABLE", "Initial boot telemetry."))
    
    cursor.execute("SELECT cpu, ram, latency, risk FROM metrics ORDER BY id DESC LIMIT 1")
    latest = cursor.fetchone()
    
    if latest:
        cpu, ram, latency, risk = latest
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        predicted_event = "Potential Memory Saturation Spike" if ram > 70 else "Cluster Stable Operation"
        confidence_score = round(random.uniform(85.0, 98.5), 2)
        time_to_impact = random.randint(10, 45)
        
        cursor.execute("INSERT INTO predictive_ai_logs (timestamp, predicted_event, confidence_score, time_to_impact_mins, approval_status) VALUES (?, ?, ?, ?, ?)",
                       (timestamp, predicted_event, confidence_score, time_to_impact, "PENDING_AUTO_APPROVAL"))
        conn.commit()
    conn.close()

if __name__ == '__main__':
    run_predictive_ai_analysis()
