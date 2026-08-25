from auth_engine import EnterpriseAuthEngine
from database_engine import EnterpriseDatabaseManager

auth = EnterpriseAuthEngine()
db = EnterpriseDatabaseManager()

def api_gateway_router(path, method, headers, body=None):
    auth_header = headers.get("Authorization", "")
    if path.startswith("/api/") and path != "/api/login":
        if not auth_header.startswith("Bearer "):
            return {"status": 401, "error": "Unauthorized: Missing or invalid token"}
        token = auth_header.split(" ")[1]
        decoded = auth.decode_jwt_token(token)
        if not decoded:
            return {"status": 403, "error": "Forbidden: Token expired or invalid"}

    if path == "/api/login" and method == "POST":
        email = body.get("email")
        pwd = body.get("password")
        if auth.verify_password(email, pwd):
            token = auth.generate_jwt_token(email)
            return {"status": 200, "token": token, "message": "Login successful"}
        return {"status": 401, "error": "Invalid credentials"}

    elif path == "/api/telemetry" and method == "GET":
        return {"status": 200, "data": db.redis_cache["live_metrics"]}

    return {"status": 404, "error": "API Route Not Found"}
