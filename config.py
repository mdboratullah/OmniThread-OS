import os

# Enterprise Configuration Core
PORT = int(os.getenv("PORT", 8080))
DB_FILE = os.getenv("DB_FILE", "omnithread_enterprise.db")
ENVIRONMENT = os.getenv("ENVIRONMENT", "production")
SECRET_ENCRYPTION_KEY = os.getenv("SECRET_KEY", "omni_sec_enterprise_master_999")
