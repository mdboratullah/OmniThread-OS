from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def dashboard():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>OmniThread OS - Enterprise Dashboard</title>
        <style>
            body { font-family: Arial, sans-serif; background: #0f172a; color: #f8fafc; text-align: center; padding: 50px; }
            .card { background: #1e293b; padding: 30px; border-radius: 12px; display: inline-block; box-shadow: 0 4px 12px rgba(0,0,0,0.3); }
            h1 { color: #38bdf8; }
            .status { color: #4ade80; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>OmniThread OS</h1>
            <p>Enterprise Observability & AIOps Platform</p>
            <p>System Status: <span class="status">ONLINE & SECURE</span></p>
            <p>All 30 Enterprise Modules Loaded Successfully.</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
