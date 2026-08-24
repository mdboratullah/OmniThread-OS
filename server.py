import http.server
import sqlite3
import time
import urllib.parse
from config import PORT, DB_FILE
from template import get_html
import engine
import benchmark
import security
import remediation
import test_report
import ai_predictive

class PredictiveAIOpsHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if urllib.parse.urlparse(self.path).path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            
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
            
            latest = history if history else (time.strftime("%Y-%m-%d %H:%M:%S"), 25.0, 45.0, 5.0, 120.0, 35.0, "STABLE", "OmniThread OS v6.0 AI predictive core operational.")
            self.wfile.write(get_html(latest, benchmarks, audits, remediations, reports, predictions).encode('utf-8'))

if __name__ == '__main__':
    server = http.server.HTTPServer(('0.0.0.0', PORT), PredictiveAIOpsHandler)
    print(f"OmniThread OS v6.0 Predictive AI Server running at http://localhost:{PORT}")
    server.serve_forever()
