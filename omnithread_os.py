import os
import json
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread

# Continuous State & Single-File Database Architecture
DATA_FILE = "omnithread_state.json"

def load_state():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {"status": "ACTIVE", "execution_count": 0, "logs": ["System Initialized"]}

def save_state(state):
    with open(DATA_FILE, "w") as f:
        json.dump(state, f, indent=4)

state = load_state()

def background_kernel():
    while True:
        state["execution_count"] += 1
        state["logs"].append(f"Heartbeat tick {state['execution_count']} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        if len(state["logs"]) > 20:
            state["logs"].pop(0)
        save_state(state)
        time.sleep(5)

class StaticDashboardHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>OmniThread OS Dashboard</title>
            <style>
                body {{ font-family: sans-serif; background: #0f172a; color: #f8fafc; padding: 20px; }}
                .card {{ background: #1e293b; padding: 20px; border-radius: 8px; max-width: 600px; margin: auto; }}
                h1 {{ color: #38bdf8; }}
                .log {{ background: #0f172a; padding: 10px; border-radius: 4px; height: 150px; overflow-y: scroll; font-family: monospace; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>OmniThread OS Core</h1>
                <p><strong>Status:</strong> {state['status']}</p>
                <p><strong>Persistent Executions:</strong> {state['execution_count']}</p>
                <h3>System Logs:</h3>
                <div class="log">
                    {'<br>'.join(state['logs'])}
                </div>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

    def log_message(self, format, *args):
        return

if __name__ == "__main__":
    t = Thread(target=background_kernel, daemon=True)
    t.start()
    server = HTTPServer(("0.0.0.0", 8080), StaticDashboardHandler)
    print("OmniThread OS running on http://localhost:8080")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        save_state(state)
        print("System safely stopped with state preserved.")
