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
import security_auth

class SecureEnterpriseHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        query_params = urllib.parse.parse_qs(parsed_path.query)
        
        # Security Token Check for Sensitive Endpoints
        token = query_params.get("token", [None])[0]
        
        if path == '/':
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
            
            latest = history if history else (time.strftime("%Y-%m-%d %H:%M:%S"), 25.0, 45.0, 5.0, 120.0, 35.0, "STABLE", "Secure operational.")
            self.wfile.write(get_html(latest, benchmarks, audits, remediations, reports, predictions).encode('utf-8'))
            
        elif path == '/health':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status": "UP", "security": "RBAC & Token Enforced"}')
            
        elif path == '/metrics':
            # Strict Token Verification for Metrics & API Control
            if not token:
                self.send_response(401)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(b'{"error": "Unauthorized: Missing API Token. Use ?token=YOUR_TOKEN"}')
                return
                
            is_valid, role = security_auth.verify_api_token(token)
            if not is_valid:
                self.send_response(403)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(b'{"error": "Forbidden: Invalid Enterprise API Token"}')
                return

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(f'omnithread_cluster_health_status 1\nauthorized_role {role}\n'.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

if __name__ == '__main__':
    server = http.server.HTTPServer(('0.0.0.0', PORT), SecureEnterpriseHandler)
    print(f"Secure OmniThread OS Server running at http://0.0.0.0:{PORT}")
    server.serve_forever()
