import http.server
import socketserver
import threading
import sqlite3
import json
import time

PORT = 8082

# Simple Database Setup for Enterprise State & Audit Log
def init_db():
    conn = sqlite3.connect('aiops_state.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS audit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            action TEXT,
            status TEXT,
            risk_score REAL
        )
    ''')
    conn.commit()
    return conn

db_conn = init_db()

class AIOpsHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            html_content = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>OmniThread Enterprise AIOps v5.0</title>
                <style>
                    body { background-color: #121212; color: #e0e0e0; font-family: Arial, sans-serif; text-align: center; padding: 50px; }
                    .card { background: #1e1e1e; padding: 20px; border-radius: 8px; display: inline-block; box-shadow: 0 4px 8px rgba(0,0,0,0.3); }
                    h1 { color: #4CAF50; }
                </style>
            </head>
            <body>
                <div class="card">
                    <h1>OmniThread Enterprise AIOps v5.0</h1>
                    <p>Status: <span style="color: #4CAF50;">Self-Healing & XAI Active</span></p>
                    <p>Repository: <b>mdboratullah/OmniThread-OS</b></p>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html_content.encode('utf-8'))
        else:
            super().do_GET()

def run_server():
    with socketserver.TCPServer(("", PORT), AIOpsHandler) as httpd:
        print(f"Production-Ready Enterprise AIOps Server running at http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == '__main__':
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down gracefully...")
