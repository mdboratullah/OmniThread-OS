import sqlite3
import time
from config import DB_FILE

def fetch_dashboard_data():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    
    cur.execute("SELECT timestamp, cpu, ram, network, latency, risk, status, rca FROM metrics ORDER BY id DESC LIMIT 1")
    history = cur.fetchone()
    
    cur.execute("SELECT timestamp, total_requests, avg_latency_ms, status FROM benchmark_logs ORDER BY id DESC LIMIT 2")
    benchmarks = cur.fetchall()

    cur.execute("SELECT id, timestamp, user_role, action_performed, ip_address, status FROM audit_trail ORDER BY id DESC LIMIT 2")
    audits = cur.fetchall()

    cur.execute("SELECT id, timestamp, error_event, remediation_action, rollback_status FROM remediation_logs ORDER BY id DESC LIMIT 2")
    remediations = cur.fetchall()

    cur.execute("SELECT id, timestamp, total_failures_detected, successfully_recovered, avg_mttr_seconds, report_status FROM automated_test_reports ORDER BY id DESC LIMIT 2")
    reports = cur.fetchall()

    cur.execute("SELECT id, timestamp, predicted_event, confidence_score, time_to_impact_mins, approval_status FROM predictive_ai_logs ORDER BY id DESC LIMIT 3")
    predictions = cur.fetchall()
    
    conn.close()
    
    latest = history if history else (time.strftime("%Y-%m-%d %H:%M:%S"), 25.0, 45.0, 5.0, 120.0, 35.0, "STABLE", "Secure operational.")
    return latest, benchmarks, audits, remediations, reports, predictions
