import http.server
import sqlite3
import time
import urllib.parse
from config import PORT, DB_FILE
from template import get_html
import engine
import benchmark

class ProductionHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if urllib.parse.urlparse(self.path).path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            
            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            cur.execute("SELECT timestamp, cpu, ram, network, latency, risk, status, rca FROM metrics ORDER BY id DESC LIMIT 1")
            history = cur.fetchone()
            
            cur.execute("SELECT timestamp, total_requests, avg_latency_ms, status FROM benchmark_logs ORDER BY id DESC LIMIT 5")
            benchmarks = cur.fetchall()
            conn.close()
            
            latest = history if history else (time.strftime("%Y-%m-%d %H:%M:%S"), 25.0, 45.0, 5.0, 120.0, 35.0, "STABLE", "Initial boot check passed.")
            self.wfile.write(get_html(latest, benchmarks).encode('utf-8'))

if __name__ == '__main__':
    server = http.server.HTTPServer(('0.0.0.0', PORT), ProductionHandler)
    print(f"Enterprise Production Server running at http://localhost:{PORT}")
    server.serve_forever()
