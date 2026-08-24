import time
import random
import threading
import sqlite3
from config import DB_FILE

def telemetry_engine():
    while True:
        # Simulating Real Prometheus / K8s Pod Telemetry
        cpu = round(random.uniform(15.0, 85.0), 1)
        ram = round(random.uniform(30.0, 90.0), 1)
        network = round(random.uniform(1.2, 25.4), 2)
        latency = round(random.uniform(20.0, 300.0), 1)
        
        # Explainable AI Risk Formula
        risk = round((cpu * 0.4) + (ram * 0.3) + (latency * 0.1), 2)
        
        if risk > 65.0:
            status = "CRITICAL [K8S POD WARNING]"
            rca = f"Prometheus Alert: High resource saturation. Risk score {risk}%."
        else:
            status = "STABLE [PROD HEALTHY]"
            rca = "All Kubernetes nodes and AWS CloudWatch connectors operating normally."

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO metrics (timestamp, cpu, ram, network, latency, risk, status, rca) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (timestamp, cpu, ram, network, latency, risk, status, rca))
        conn.commit()
        conn.close()
        time.sleep(10)

threading.Thread(target=telemetry_engine, daemon=True).start()
