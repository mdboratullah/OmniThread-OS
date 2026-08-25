import random
from flask import Flask, render_template_string, request, jsonify
from database_engine import EnterpriseDatabaseManager
from auth_engine import EnterpriseAuthEngine
from api_gateway import api_gateway_router

app = Flask(__name__)
db = EnterpriseDatabaseManager()
auth = EnterpriseAuthEngine()

@app.route('/')
def dashboard():
    nodes = ["prod-node-01", "prod-node-02", "prod-node-03"]
    node_data = {}
    for node in nodes:
        metrics = {
            "cpu": round(random.uniform(20.0, 90.0), 2),
            "ram": round(random.uniform(40.0, 85.0), 2)
        }
        db.save_telemetry_history(node, metrics)
        node_data[node] = metrics

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>OmniThread OS v6.0 - Enterprise Multi-Node Dashboard</title>
        <meta http-equiv="refresh" content="3">
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0b0f19; color: #f8fafc; margin: 0; padding: 20px; }}
            .container {{ max-width: 1200px; margin: 0 auto; }}
            header {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 15px; margin-bottom: 25px; }}
            h1 {{ color: #38bdf8; margin: 0; font-size: 24px; }}
            .badge {{ background: #065f46; color: #34d399; padding: 6px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; }}
            .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }}
            .card {{ background: #1e293b; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); border-left: 4px solid #38bdf8; }}
            .card h3 {{ margin-top: 0; color: #94a3b8; font-size: 14px; text-transform: uppercase; }}
            .chart-container {{ margin-top: 30px; background: #1e293b; padding: 20px; border-radius: 10px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>OmniThread OS (Enterprise AIOps & Multi-Node)</h1>
                <span class="badge">DB + JWT GATEWAY ACTIVE</span>
            </header>
            
            <div class="grid">
                <div class="card">
                    <h3>Node 1 (prod-node-01)</h3>
                    <p>CPU: {node_data['prod-node-01']['cpu']}% | RAM: {node_data['prod-node-01']['ram']}%</p>
                </div>
                <div class="card">
                    <h3>Node 2 (prod-node-02)</h3>
                    <p>CPU: {node_data['prod-node-02']['cpu']}% | RAM: {node_data['prod-node-02']['ram']}%</p>
                </div>
                <div class="card">
                    <h3>Node 3 (prod-node-03)</h3>
                    <p>CPU: {node_data['prod-node-03']['cpu']}% | RAM: {node_data['prod-node-03']['ram']}%</p>
                </div>
            </div>

            <div class="chart-container">
                <h3 style="color: #38bdf8; margin-top:0;">Live Cluster Trend Chart</h3>
                <canvas id="clusterChart" height="90"></canvas>
            </div>
        </div>

        <script>
            const ctx = document.getElementById('clusterChart').getContext('2d');
            new Chart(ctx, {{
                type: 'line',
                data: {{
                    labels: ['T-4s', 'T-3s', 'T-2s', 'T-1s', 'Live'],
                    datasets: [{{
                        label: 'Cluster Avg CPU %',
                        data: [45, 52, 49, 60, {node_data['prod-node-01']['cpu']}],
                        borderColor: '#38bdf8',
                        tension: 0.3
                    }}]
                }},
                options: {{ responsive: true, scales: {{ y: {{ beginAtZero: true, max: 100 }} }} }}
            }});
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/api/v1/<path:subpath>', methods=['GET', 'POST'])
def gateway(subpath):
    body = request.get_json() if request.is_json else {}
    res = api_gateway_router(f"/api/{subpath}", request.method, request.headers, body)
    return jsonify(res), res.get("status", 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
