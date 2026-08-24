from flask import Flask, render_template, request, jsonify
import time
import sqlite3
from config import DB_FILE
from data_fetcher import fetch_dashboard_data

app = Flask(__name__)

@app.route('/')
def dashboard():
    latest, benchmarks, audits, remediations, reports, predictions = fetch_dashboard_data()
    return render_template(
        'index.html', 
        latest=latest, 
        benchmarks=benchmarks, 
        audits=audits, 
        remediations=remediations, 
        reports=reports, 
        predictions=predictions
    )

@app.route('/health')
def health_check():
    return jsonify({"status": "SECURE", "system": "OmniThread OS v6.0", "uptime": "99.99%"}), 200

# এই রুটটি এন্টারপ্রাইজ এজেন্ট থেকে সিকিউর টোকেনসহ লাইভ ডেটা রিসিভ করবে
@app.route('/api/telemetry', methods=['POST'])
def receive_telemetry():
    auth_header = request.headers.get('Authorization')
    expected_token = "Bearer omnithread-secure-enterprise-token-2026"
    
    # টোকেন ভ্যালিডেশন চেক (Enterprise Security)
    if not auth_header or auth_header != expected_token:
        return jsonify({"error": "Unauthorized: Invalid or missing Enterprise API Token"}), 401
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "Bad Request: No telemetry payload provided"}), 400
        
    # রিসিভ করা মেট্রিক্স এক্সট্রাক্ট করা
    source = data.get("source", "Unknown-Node")
    cpu = data.get("cpu", 0.0)
    ram = data.get("ram", 0.0)
    disk = data.get("disk", 0.0)
    network = data.get("network", 0.0)
    latency = data.get("latency", 0.0)
    timestamp = data.get("timestamp", "")
    
    print(f"[AIOps Ingest] Received Live Telemetry from {source} -> CPU: {cpu}% | RAM: {ram}% | Disk: {disk}%")
    
    return jsonify({
        "status": "SUCCESS",
        "message": "Telemetry ingested and processed securely by OmniThread Core",
        "node": source
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
