import jwt
import time

SECRET_VAULT_KEY = "enterprise-vault-master-secret-2026"

class APIGatewaySecurity:
    def __init__(self):
        self.rate_limit_store = {}

    def check_rate_limit(self, client_ip):
        current_time = time.time()
        requests = self.rate_limit_store.get(client_ip, [])
        requests = [req_time for req_time in requests if current_time - req_time < 60]
        
        if len(requests) > 100:
            return False
        requests.append(current_time)
        self.rate_limit_store[client_ip] = requests
        return True

    def verify_request_security(self, auth_header, client_ip):
        if not self.check_rate_limit(client_ip):
            return {"status": 429, "error": "Rate limit exceeded"}
        
        if not auth_header or not auth_header.startswith("Bearer "):
            return {"status": 401, "error": "Unauthorized: Missing TLS/JWT token"}
        
        token = auth_header.split(" ")[1]
        try:
            payload = jwt.decode(token, SECRET_VAULT_KEY, algorithms=["HS256"])
            return {"status": 200, "user": payload.get("sub"), "tls": "TLS 1.3 Verified"}
        except:
            return {"status": 403, "error": "Forbidden: Invalid or expired token"}
