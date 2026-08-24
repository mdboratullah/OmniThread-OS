import http.server
import urllib.parse
from config import PORT
from template import get_html
from database import init_all_tables
from data_fetcher import fetch_dashboard_data
import security_auth

class SecureEnterpriseHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        query_params = urllib.parse.parse_qs(parsed_path.query)
        token = query_params.get("token", [None])[0]
        
        if path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            
            init_all_tables()
            latest, benchmarks, audits, remediations, reports, predictions = fetch_dashboard_data()
            self.wfile.write(get_html(latest, benchmarks, audits, remediations, reports, predictions).encode('utf-8'))
            
        elif path == '/health':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status": "UP", "security": "RBAC & Token Enforced"}')
            
        elif path == '/metrics':
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
    init_all_tables()
    server = http.server.HTTPServer(('0.0.0.0', PORT), SecureEnterpriseHandler)
    print(f"Secure OmniThread OS Server running at http://0.0.0.0:{PORT}")
    server.serve_forever()
