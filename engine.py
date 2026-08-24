import sqlite3
import time
import random
from config import DB_FILE

def init_db():
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
    conn.commit()
    conn.close()

def record_cluster_telemetry():
    init_db()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    cpu = round(random.uniform(20.0, 78.0), 2)
    ram = round(random.uniform(35.0, 82.0), 2)
    network = round(random.uniform(2.0, 15.0), 2)
    latency = round(random.uniform(40.0, 140.0), 2)
    
    risk = round((cpu * 0.4) + (ram * 0.4) + (latency * 0.2) / 2, 2)
    status = "WARNING [HIGH LOAD]" if risk > 60.0 else "OPTIMIZED [PRODUCTION STABLE]"
    rca = "Cluster operating within normal telemetry thresholds." if risk <= 60.0 else "Resource saturation detected. Recommended auto-scaling."

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO metrics (timestamp, cpu, ram, network, latency, risk, status, rca) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (timestamp, cpu, ram, network, latency, risk, status, rca))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    record_cluster_telemetry()
