import os
import logging
from logging.handlers import RotatingFileHandler

# ১) Professional Folder Structure Setup
def create_project_structure():
    folders = [
        "config",
        "logs",
        "database",
        "agents",
        "api",
        "security",
        "tests",
        "docs"
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    print("[Structure] Enterprise folder structure created successfully.")

# ২) Configuration & Environment Management
class EnterpriseConfig:
    def __init__(self):
        # Environment variables with default fallback for production readiness
        self.ENV = os.getenv("OMNITHREAD_ENV", "production")
        self.DEBUG = os.getenv("OMNITHREAD_DEBUG", "False").lower() == "true"
        self.HOST = os.getenv("OMNITHREAD_HOST", "0.0.0.0")
        self.PORT = int(os.getenv("OMNITHREAD_PORT", "8080"))
        self.SECRET_KEY = os.getenv("OMNITHREAD_SECRET", "super-secure-enterprise-key-2026")

# ৩) Centralized Professional Logging System
def setup_logging():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "omnithread_enterprise.log")

    logger = logging.getLogger("OmniThreadEnterprise")
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        # Rotating file handler to manage log size (Max 5MB per file, up to 3 backups)
        file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
        file_formatter = logging.Formatter('%(asctime)s [%(levelname)s] [%(name)s]: %(message)s')
        file_handler.setFormatter(file_formatter)

        # Console handler for real-time terminal output
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(file_formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

if __name__ == "__main__":
    # Initialize Step 1 Components
    create_project_structure()
    
    config = EnterpriseConfig()
    logger = setup_logging()
    
    logger.info("OmniThread OS v6.0 Enterprise Infrastructure Initialized.")
    logger.info(f"Environment: {config.ENV} | Host: {config.HOST}:{config.PORT}")
    logger.info("Step 1 (Project Structure, Config & Logging) completed successfully.")
