import http.server, socketserver, json, os, time, threading, urllib.request, urllib.parse
from datetime import datetime

STATE_FILE = "omnithread_state.json"
PORT = 8080

default_state = {
    "system_status": "ACTIVE",
    "total_executions": 0,
    "monitored_targets": [
        {"id": 1, "name": "Google", "url": "https://www.google.com", "status": "UNKNOWN", "last_check": "N/A"},
        {"id": 2, "name": "GitHub", "url": "https://github.com", "status": "UNKNOWN", "last_check": "N/A"}
    ],
    "logs": []
}

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f: return json.load(f)
        except Exception: return default_state
    return default_state

def save_state(data):
    with open(STATE_FILE, "w") as f: json.dump(data, f, indent=4)

state = load_state()

def add_log(msg):
    log_entry = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    state["logs"].append(log_entry)
    if len(state["logs"]) > 100: state["logs"].pop(0)
    save_state(state)

def background_engine():
    while True:
        try:
            state["total_executions"] += 1
            now_str = datetime.now().strftime("%I:%M:%S %p")
            for t in state["monitored_targets"]:
                t["last_check"] = now_str
                try:
                    req = urllib.request.Request(t["url"], headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req, timeout=5) as res:
                        t["status"] = "ONLINE (200 OK)" if res.status == 200 else f"WARN ({res.status})"
                except Exception: t["status"] = "OFFLINE (CRITICAL)"
            add_log(f"Cycle #{state['total_executions']} executed.")
            save_state(state)
        except Exception as err: add_log(f"Engine Error: {err}")
        time.sleep(10)
class EnterpriseHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            t_rows = "".join([f"<tr><td><b>{t['name']}</b></td><td><a href='{t['url']}' target='_blank' style='color:#4fc3f7;'>{t['url']}</a></td><td style='color:{'#00e676' if 'ONLINE' in t['status'] else '#ff5252'};font-weight:bold;'>{t['status']}</td><td>{t['last_check']}</td><td><form method='POST' action='/delete' style='display:inline;'><input type='hidden' name='id' value='{t['id']}'><button type='submit' style='background:#ff5252;color:#fff;border:none;padding:5px 10px;border-radius:4px;'>Delete</button></form></td></tr>" for t in state["monitored_targets"]])
            logs_html = "".join([f"<li>{l}</li>" for l in reversed(state["logs"])])
            html = f"""<!DOCTYPE html><html><head><title>OmniThread OS</title><meta http-equiv="refresh" content="5"><style>body{{font-family:sans-serif;background:#0f172a;color:#f8fafc;padding:20px;}}.card{{background:#1e293b;padding:20px;border-radius:12px;margin-bottom:20px;border:1px solid #334155;}}h1{{color:#38bdf8;}}table{{width:100%;border-collapse:collapse;}}th,td{{padding:12px;border-bottom:1px solid #334155;}}input{{padding:8px;border-radius:6px;border:1px solid #334155;background:#0f172a;color:#fff;margin-right:8px;}}button.btn-add{{background:#22c55e;color:#fff;border:none;padding:8px 16px;border-radius:6px;font-weight:bold;}}ul{{list-style-type:none;padding:10px;max-height:250px;overflow-y:auto;font-family:monospace;background:#0f172a;border-radius:6px;}}</style></head><body><div class="card"><h1>🚀 OmniThread OS Enterprise</h1><p>Status: <b style="color:#22c55e;">● {state['system_status']}</b> | Cycles: <b>{state['total_executions']}</b></p></div><div class="card"><h3>Add Target</h3><form method="POST" action="/add"><input type="text" name="name" placeholder="Name" required><input type="url" name="url" placeholder="https://example.com" required><button type="submit" class="btn-add">+ Add</button></form></div><div class="card"><h3>Monitored Services</h3><table><thead><tr><th>Name</th><th>URL</th><th>Status</th><th>Last Check</th><th>Action</th></tr></thead><tbody>{t_rows}</tbody></table></div><div class="card"><h3>Logs</h3><ul>{logs_html}</ul></div></body></html>"""
            self.wfile.write(html.encode('utf-8'))
        elif self.path == '/api/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(state).encode('utf-8'))
        else: self.send_error(404)

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        params = urllib.parse.parse_qs(self.rfile.read(length).decode('utf-8'))
        if self.path == '/add':
            name, url = params.get('name', [''])[0], params.get('url', [''])[0]
            if name and url:
                new_id = max([t['id'] for t in state['monitored_targets']], default=0) + 1
                state['monitored_targets'].append({"id": new_id, "name": name, "url": url, "status": "CHECKING...", "last_check": "JUST NOW"})
                add_log(f"Added target: {name}")
                save_state(state)
        elif self.path == '/delete':
            target_id = int(params.get('id', [0])[0])
            state['monitored_targets'] = [t for t in state['monitored_targets'] if t['id'] != target_id]
            add_log(f"Deleted ID #{target_id}")
            save_state(state)
        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()

if __name__ == "__main__":
    add_log("OmniThread OS Ultimate Active.")
    threading.Thread(target=background_engine, daemon=True).start()
    print(f"Running on http://localhost:{PORT}")
    socketserver.TCPServer(("", PORT), EnterpriseHandler).serve_forever()
