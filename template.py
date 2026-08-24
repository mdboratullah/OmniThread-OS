def get_html(latest, benchmarks, audits, remediations, reports, predictions):
    return f"""<!DOCTYPE html>
<html>
<head>
    <title>OmniThread OS v6.0 [AI Predictive Autonomous Operations]</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ background-color: #0b0f19; color: #f8fafc; font-family: monospace; margin: 0; padding: 15px; }}
        .header {{ background: #1e293b; padding: 15px; border-radius: 8px; border-left: 4px solid #8b5cf6; margin-bottom: 15px; }}
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
        <h3 style="margin:0;">🔮 OmniThread OS v6.0 [AI Predictive Autonomous Operations]</h3>
        <p style="margin:5px 0 0 0; font-size:11px; color:#c084fc;">Status: Proactive Anomaly Forecasting & Approval Workflow Active</p>
    </div>
    <div class="grid">
        <div class="card"><h4>CPU (K8s)</h4><p>{latest[1]}%</p></div>
        <div class="card"><h4>RAM</h4><p>{latest[2]}%</p></div>
        <div class="card"><h4>Network</h4><p>{latest[3]} MB/s</p></div>
        <div class="card"><h4>Latency</h4><p>{latest[4]}ms</p></div>
        <div class="card"><h4>Risk Index</h4><p style="color:#ef4444;">{latest[5]}%</p></div>
    </div>
    <div class="section" style="background:#2e1065; border-color:#7c3aed;">
        <h4 style="margin:0 0 5px 0; color:#d8b4fe;">⚡ AI Predictive Operations Insight:</h4>
        <p style="margin:0; font-size:12px;">{latest[7]}</p>
    </div>
    <div class="section">
        <h4 style="margin-top:0; color:#c084fc;">🤖 AI Proactive Anomaly Forecasting (Next 10 Mins)</h4>
        <table>
            <tr><th>Timestamp</th><th>Predicted Risk Event</th><th>AI Confidence</th><th>Time to Impact</th><th>Status / Approval</th></tr>
            {"".join(f"<tr><td>{p[1]}</td><td>{p[2]}</td><td>{p[3]}%</td><td>~{p[4]} mins</td><td><span style='color:#facc15;'>{p[5]}</span></td></tr>" for p in predictions)}
        </table>
    </div>
    <div class="section">
        <h4 style="margin-top:0; color:#38bdf8;">📊 Automated Test Report & MTTR Performance</h4>
        <table>
            <tr><th>Timestamp</th><th>Failures Detected</th><th>Successfully Recovered</th><th>Avg MTTR</th><th>Status</th></tr>
            {"".join(f"<tr><td>{tp[1]}</td><td>{tp[2]}</td><td>{tp[3]}</td><td>{tp[4]}s</td><td><span style='color:#34d399;'>{tp[5]}</span></td></tr>" for tp in reports)}
        </table>
    </div>
</body>
</html>
"""
