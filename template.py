def get_html(latest, benchmarks, audits, remediations):
    return f"""<!DOCTYPE html>
<html>
<head>
    <title>OmniThread OS Enterprise Pro [AIOps Auto-Healing]</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ background-color: #0b0f19; color: #f8fafc; font-family: monospace; margin: 0; padding: 15px; }}
        .header {{ background: #1e293b; padding: 15px; border-radius: 8px; border-left: 4px solid #10b981; margin-bottom: 15px; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(110px, 1fr)); gap: 10px; margin-bottom: 15px; }}
        .card {{ background: #1e293b; padding: 12px; border-radius: 8px; text-align: center; border: 1px solid #334155; }}
        .card h4 {{ margin: 0 0 5px 0; font-size: 12px; color: #94a3b8; }}
        .card p {{ margin: 0; font-size: 16px; font-weight: bold; color: #38bdf8; }}
        .section {{ background: #1e293b; padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #334155; }}
        table {{ width: 100%; border-collapse: collapse; font-size: 11px; }}
        th, td {{ padding: 8px; text-align: left; border-bottom: 1px solid #334155; }}
        th {{ color: #94a3b8; }}
    </style>
</head>
<body>
    <div class="header">
        <h3 style="margin:0;">⚡ OmniThread OS [K8s Auto-Healing & Remediation Live]</h3>
        <p style="margin:5px 0 0 0; font-size:11px; color:#34d399;">Status: Automated Rollback Verified | Live Prometheus Ingestion</p>
    </div>
    <div class="grid">
        <div class="card"><h4>CPU (K8s)</h4><p>{latest[1]}%</p></div>
        <div class="card"><h4>RAM</h4><p>{latest[2]}%</p></div>
        <div class="card"><h4>Network</h4><p>{latest[3]} MB/s</p></div>
        <div class="card"><h4>Latency</h4><p>{latest[4]}ms</p></div>
        <div class="card"><h4>Risk Index</h4><p style="color:#ef4444;">{latest[5]}%</p></div>
    </div>
    <div class="section" style="background:#172554; border-color:#1d4ed8;">
        <h4 style="margin:0 0 5px 0; color:#93c5fd;">🔍 Real-Time K8s Telemetry & RCA Report:</h4>
        <p style="margin:0; font-size:12px;">{latest[7]}</p>
    </div>
    <div class="section">
        <h4 style="margin-top:0; color:#f59e0b;">🛠️ Automated Error Capture & Rollback Log</h4>
        <table>
            <tr><th>Timestamp</th><th>Captured Error Event</th><th>Remediation Action</th><th>Rollback Status</th></tr>
            {"".join(f"<tr><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td><span style='color:#34d399;'>{r[4]}</span></td></tr>" for r in remediations)}
        </table>
    </div>
    <div class="section">
        <h4 style="margin-top:0; color:#10b981;">🔒 Security Audit Trail & RBAC</h4>
        <table>
            <tr><th>Timestamp</th><th>Role</th><th>Action</th><th>Status</th></tr>
            {"".join(f"<tr><td>{a[1]}</td><td>{a[2]}</td><td>{a[3]}</td><td><span style='color:#34d399;'>{a[5]}</span></td></tr>" for a in audits)}
        </table>
    </div>
</body>
</html>
"""
