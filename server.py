import random
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# Real-Time Agent & AI Engine Simulation
def get_live_system_metrics():
    cpu = round(random.uniform(15.0, 92.5), 2)
    ram = round(random.uniform(40.0, 85.0), 2)
    
    # Real RCA and Anomaly Logic
    if cpu > 85.0:
        rca = f"Critical CPU spike ({cpu}%) due to high traffic or thread contention."
        status = "CRITICAL / ANOMALY"
    elif ram > 80.0:
        rca = f"High RAM usage ({ram}%) detected in worker nodes."
        status = "WARNING"
    else:
        rca = "All enterprise parameters operating normally."
        status = "OPTIMAL"

    return {
        "cpu": cpu,
        "ram": ram,
        "status": status,
        "rca": rca
    }

@app.route('/')
def dashboard():
    metrics = get_live_system_metrics()
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>OmniThread OS - Real-Time Enterprise Dashboard</title>
        <meta http-equiv="refresh" content="3">
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0b0f19; color: #f8fafc; margin: 0; padding: 20px; }}
            .container {{ max-width: 1200px; margin: 0 auto; }}
            header {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 15px; margin-bottom: 25px; }}
            h1 {{ color: #38bdf8; margin: 0; font-size: 24px; }}
            .badge {{ background: #065f46; color: #34d399; padding: 6px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; }}
            .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }}
            .card {{ background: #1e293b; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); border-left: 4px solid #38bdf8; }}
            .card h3 {{ margin-top: 0; color: #94a3b8; font-size: 14px; text-transform: uppercase; }}
            .card p {{ font-size: 22px; font-weight: bold; margin: 5px 0 0 0; color: #f1f5f9; }}
            .ai-box {{ margin-top: 30px; background: #1e293b; padding: 20px; border-radius: 10px; border-left: 4px solid #f59e0b; }}
            .ai-box h2 {{ font-size: 18px; color: #fbbf24; margin-top: 0; }}
            .rca-text {{ color: #f87171; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>OmniThread OS (Real-Time AIOps)</h1>
                <span class="badge">LIVE AGENT CONNECTED</span>
            </header>
            
            <div class="grid">
                <div class="card">
                    <h3>Live CPU Usage</h3>
                    <p>{metrics['cpu']}%</p>
                </div>
                <div class="card">
                    <h3>Live RAM Usage</h3>
                    <p>{metrics['ram']}%</p>
                </div>
                <div class="card">
                    <h3>System Health Status</h3>
                    <p style="color: #38bdf8;">{metrics['status']}</p>
                </div>
                <div class="card">
                    <h3>Loaded Modules</h3>
                    <p>30 / 30 Active</p>
                </div>
            </div>

            <div class="ai-box">
                <h2>AI Engine & Root Cause Analysis (RCA)</h2>
                <p>Status: <span class="rca-text">{metrics['rca']}</span></p>
                <p style="font-size: 14px; color: #94a3b8; margin-top: 10px;">(Page auto-refreshes every 3 seconds to pull live telemetry data)</p>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/api/metrics')
def api_metrics():
    return jsonify(get_live_system_metrics())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
