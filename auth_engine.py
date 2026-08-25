import hashlib
import jwt
import datetime

SECRET_KEY = "super-secret-enterprise-jwt-key-2026"

class EnterpriseAuthEngine:
    def __init__(self):
        self.users_db = {
            "admin@omnithread.io": hashlib.sha256("Admin@2026".encode()).hexdigest()
        }

    def verify_password(self, email, password):
        hashed = hashlib.sha256(password.encode()).hexdigest()
        return self.users_db.get(email) == hashed

    def generate_jwt_token(self, email, role="Admin"):
        payload = {
            "sub": email,
            "role": role,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=8)
        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    def decode_jwt_token(self, token):
        try:
            return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return None
