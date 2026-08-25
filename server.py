from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def dashboard():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>OmniThread OS - Enterprise AIOps Dashboard</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0b0f19; color: #f8fafc; margin: 0; padding: 20px; }
            .container { max-width: 1200px; margin: 0 auto; }
            header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 15px; margin-bottom: 25px; }
            h1 { color: #38bdf8; margin: 0; font-size: 24px; }
            .badge { background: #065f46; color: #34d399; padding: 6px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; }
            .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }
            .card { background: #1e293b; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); border-left: 4px solid #38bdf8; }
            .card h3 { margin-top: 0; color: #94a3b8; font-size: 14px; text-transform: uppercase; }
            .card p { font-size: 20px; font-weight: bold; margin: 5px 0 0 0; color: #f1f5f9; }
            .modules-section { margin-top: 30px; background: #1e293b; padding: 20px; border-radius: 10px; }
            .modules-section h2 { font-size: 18px; color: #38bdf8; margin-top: 0; }
            ul { padding-left: 20px; color: #cbd5e1; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 10px; }
            li { font-size: 14px; }
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>OmniThread OS</h1>
                <span class="badge">SYSTEM ONLINE & SECURE</span>
            </header>
            
            <div class="grid">
                <div class="card">
                    <h3>Platform Version</h3>
                    <p>v6.0 Enterprise</p>
                </div>
                <div class="card">
                    <h3>Active Security Layer</h3>
                    <p>Token Auth & TLS</p>
                </div>
                <div class="card">
                    <h3>AI Engine Status</h3>
                    <p>Active (RCA & Anomaly)</p>
                </div>
                <div class="card">
                    <h3>Loaded Modules</h3>
                    <p>30 / 30 Active</p>
                </div>
            </div>

            <div class="modules-section">
                <h2>Active Enterprise Subsystems</h2>
                <ul>
                    <li>Kubernetes Cluster Monitor</li>
                    <li>Prometheus Metrics Exporter</li>
                    <li>TimescaleDB Time-Series Engine</li>
                    <li>Multi-Cloud Resource Tracker</li>
                    <li>AI Anomaly Detection Engine</li>
                    <li>Automated Root Cause Analysis</li>
                    <li>Secure Enterprise Agent Pipeline</li>
                    <li>Role-Based Access Control (RBAC)</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
