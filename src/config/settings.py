"""
Settings Configuration Module

Manages all application configuration from environment variables with proper
validation, type conversion, and sensible defaults.

Environment variables are read from:
1. .env file (via python-dotenv)
2. System environment variables
3. Hardcoded defaults (ONLY for non-sensitive, development values)

Security Model:
- No default secrets are hardcoded anywhere
- Production mode REQUIRES explicit SECRET_KEY and API_TOKEN
- Application fails fast if critical secrets are missing in production
- Uses Python logging instead of print statements
- Sensitive values are masked in logs and exports

Singleton Pattern:
- Only one Settings instance is created per application lifetime
- Use get_settings() to access configuration globally
"""

import os
import sys
import logging
from typing import List, Optional
from pathlib import Path

# Configure logger for this module
logger = logging.getLogger(__name__)


class ConfigurationError(Exception):
    """Raised when configuration is invalid or missing required values."""
    pass


class Settings:
    """
    Centralized settings class for OmniThread OS.
    
    All configuration should be read through this class, never directly
    from os.environ in application code.
    
    Security:
    - No default secrets provided
    - Production deployments MUST set SECRET_KEY and API_TOKEN
    - Invalid configuration in production raises ConfigurationError
    
    Example:
        settings = Settings()
        print(settings.DATABASE_URL)
        print(settings.is_production)
    """
    
    # =========================================================================
    # Environment & Deployment (Safe Defaults)
    # =========================================================================
    ENVIRONMENT: str = "development"
    DEBUG: bool = False
    PORT: int = 8080
    HOST: str = "0.0.0.0"
    
    # =========================================================================
    # Security (CRITICAL - NO DEFAULTS FOR SECRETS)
    # =========================================================================
    # These MUST be set explicitly in production via environment variables
    SECRET_KEY: Optional[str] = None
    ENCRYPTION_ALGORITHM: str = "HS256"
    API_TOKEN: Optional[str] = None
    
    # =========================================================================
    # Database Configuration
    # =========================================================================
    DATABASE_URL: str = "sqlite:///./omnithread_enterprise.db"
    DB_FILE: str = "omnithread_enterprise.db"
    DB_ECHO: bool = False  # SQL query logging
    DB_POOL_SIZE: int = 20
    DB_MAX_OVERFLOW: int = 40
    
    # =========================================================================
    # API & Timeouts
    # =========================================================================
    API_TIMEOUT: int = 30
    CORS_ORIGINS: List[str] = None  # Will be populated from env
    
    # =========================================================================
    # JWT Configuration
    # =========================================================================
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24
    JWT_REFRESH_EXPIRATION_DAYS: int = 30
    
    # =========================================================================
    # Logging Configuration
    # =========================================================================
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/omnithread.log"
    LOG_FORMAT: str = "json"  # or "text"
    
    # =========================================================================
    # Monitoring & Telemetry
    # =========================================================================
    TELEMETRY_ENABLED: bool = True
    TELEMETRY_INTERVAL_SECONDS: int = 60
    
    # =========================================================================
    # Node Configuration
    # =========================================================================
    NODE_NAME: str = "local-node-01"
    NODE_ID: str = "node-001"
    CLUSTER_ENABLED: bool = True
    
    # =========================================================================
    # Multi-Tenancy
    # =========================================================================
    MULTI_TENANT_ENABLED: bool = True
    DEFAULT_TENANT: str = "default"
    
    # =========================================================================
    # Third-Party Integrations
    # =========================================================================
    SLACK_WEBHOOK_URL: Optional[str] = None
    TELEGRAM_BOT_TOKEN: Optional[str] = None
    TELEGRAM_CHAT_ID: Optional[str] = None
    SMTP_SERVER: Optional[str] = None
    SMTP_PORT: int = 587
    SMTP_USERNAME: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    
    # =========================================================================
    # Kubernetes Integration
    # =========================================================================
    K8S_ENABLED: bool = False
    K8S_NAMESPACE: str = "default"
    K8S_CONFIG_PATH: str = os.path.expanduser("~/.kube/config")
    
    # =========================================================================
    # Redis Configuration (Optional)
    # =========================================================================
    REDIS_ENABLED: bool = False
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # =========================================================================
    # Feature Flags
    # =========================================================================
    ENABLE_PROMETHEUS_EXPORT: bool = True
    ENABLE_AUTO_REMEDIATION: bool = True
    ENABLE_AI_PREDICTIONS: bool = True
    
    def __init__(self):
        """
        Initialize settings from environment variables.
        
        Reads from .env file (if present) and system environment.
        Falls back to class defaults if not found.
        
        Raises:
            ConfigurationError: If required production settings are missing
        """
        # Set up logging first
        self._setup_logging()
        
        # Load from environment
        self._load_from_env()
        
        # Validate configuration
        self._validate_configuration()
    
    @staticmethod
    def _setup_logging():
        """Configure logging for the Settings module."""
        if not logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
    
    def _load_from_env(self):
        """Load configuration from environment variables."""
        # Try to load .env file if python-dotenv is available
        try:
            from dotenv import load_dotenv
            env_file = Path(".env")
            if env_file.exists():
                load_dotenv(env_file)
                logger.debug(f"Loaded configuration from {env_file}")
            else:
                logger.debug(".env file not found, using system environment variables")
        except ImportError:
            logger.warning(
                "python-dotenv not installed. Install with: pip install python-dotenv"
            )
        
        # Read environment variables and update instance attributes
        self.ENVIRONMENT = os.getenv("ENVIRONMENT", self.ENVIRONMENT).lower()
        self.DEBUG = os.getenv("DEBUG", str(self.DEBUG)).lower() in ("true", "1", "yes")
        self.PORT = int(os.getenv("PORT", self.PORT))
        self.HOST = os.getenv("HOST", self.HOST)
        
        # Security settings - No defaults for secrets
        self.SECRET_KEY = os.getenv("SECRET_KEY", None)
        self.ENCRYPTION_ALGORITHM = os.getenv("ENCRYPTION_ALGORITHM", self.ENCRYPTION_ALGORITHM)
        self.API_TOKEN = os.getenv("API_TOKEN", None)
        
        # Database settings
        self.DATABASE_URL = os.getenv("DATABASE_URL", self.DATABASE_URL)
        self.DB_FILE = os.getenv("DB_FILE", self.DB_FILE)
        self.DB_ECHO = os.getenv("DB_ECHO", str(self.DB_ECHO)).lower() in ("true", "1", "yes")
        self.DB_POOL_SIZE = int(os.getenv("DB_POOL_SIZE", self.DB_POOL_SIZE))
        self.DB_MAX_OVERFLOW = int(os.getenv("DB_MAX_OVERFLOW", self.DB_MAX_OVERFLOW))
        
        # API settings
        self.API_TIMEOUT = int(os.getenv("API_TIMEOUT", self.API_TIMEOUT))
        cors_origins = os.getenv("CORS_ORIGINS")
        if cors_origins:
            self.CORS_ORIGINS = [o.strip() for o in cors_origins.split(",")]
        else:
            self.CORS_ORIGINS = ["http://localhost:3000", "http://localhost:8080"]
        
        # JWT settings
        self.JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", self.JWT_ALGORITHM)
        self.JWT_EXPIRATION_HOURS = int(os.getenv("JWT_EXPIRATION_HOURS", self.JWT_EXPIRATION_HOURS))
        self.JWT_REFRESH_EXPIRATION_DAYS = int(os.getenv("JWT_REFRESH_EXPIRATION_DAYS", self.JWT_REFRESH_EXPIRATION_DAYS))
        
        # Logging settings
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", self.LOG_LEVEL).upper()
        self.LOG_FILE = os.getenv("LOG_FILE", self.LOG_FILE)
        self.LOG_FORMAT = os.getenv("LOG_FORMAT", self.LOG_FORMAT).lower()
        
        # Telemetry settings
        self.TELEMETRY_ENABLED = os.getenv("TELEMETRY_ENABLED", str(self.TELEMETRY_ENABLED)).lower() in ("true", "1", "yes")
        self.TELEMETRY_INTERVAL_SECONDS = int(os.getenv("TELEMETRY_INTERVAL_SECONDS", self.TELEMETRY_INTERVAL_SECONDS))
        
        # Node configuration
        self.NODE_NAME = os.getenv("NODE_NAME", self.NODE_NAME)
        self.NODE_ID = os.getenv("NODE_ID", self.NODE_ID)
        self.CLUSTER_ENABLED = os.getenv("CLUSTER_ENABLED", str(self.CLUSTER_ENABLED)).lower() in ("true", "1", "yes")
        
        # Multi-tenancy
        self.MULTI_TENANT_ENABLED = os.getenv("MULTI_TENANT_ENABLED", str(self.MULTI_TENANT_ENABLED)).lower() in ("true", "1", "yes")
        self.DEFAULT_TENANT = os.getenv("DEFAULT_TENANT", self.DEFAULT_TENANT)
        
        # Third-party integrations
        self.SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
        self.TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
        self.TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
        self.SMTP_SERVER = os.getenv("SMTP_SERVER")
        self.SMTP_PORT = int(os.getenv("SMTP_PORT", self.SMTP_PORT))
        self.SMTP_USERNAME = os.getenv("SMTP_USERNAME")
        self.SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
        
        # Kubernetes
        self.K8S_ENABLED = os.getenv("K8S_ENABLED", str(self.K8S_ENABLED)).lower() in ("true", "1", "yes")
        self.K8S_NAMESPACE = os.getenv("K8S_NAMESPACE", self.K8S_NAMESPACE)
        self.K8S_CONFIG_PATH = os.getenv("K8S_CONFIG_PATH", self.K8S_CONFIG_PATH)
        
        # Redis
        self.REDIS_ENABLED = os.getenv("REDIS_ENABLED", str(self.REDIS_ENABLED)).lower() in ("true", "1", "yes")
        self.REDIS_URL = os.getenv("REDIS_URL", self.REDIS_URL)
        
        # Feature flags
        self.ENABLE_PROMETHEUS_EXPORT = os.getenv("ENABLE_PROMETHEUS_EXPORT", str(self.ENABLE_PROMETHEUS_EXPORT)).lower() in ("true", "1", "yes")
        self.ENABLE_AUTO_REMEDIATION = os.getenv("ENABLE_AUTO_REMEDIATION", str(self.ENABLE_AUTO_REMEDIATION)).lower() in ("true", "1", "yes")
        self.ENABLE_AI_PREDICTIONS = os.getenv("ENABLE_AI_PREDICTIONS", str(self.ENABLE_AI_PREDICTIONS)).lower() in ("true", "1", "yes")
        
        logger.info(f"Configuration loaded: ENVIRONMENT={self.ENVIRONMENT}, DEBUG={self.DEBUG}")
    
    def _validate_configuration(self):
        """
        Validate that configuration is correct and safe.
        
        In production mode, this method is strict:
        - Requires SECRET_KEY to be set
        - Requires API_TOKEN to be set
        - Rejects DEBUG=True
        
        Raises:
            ConfigurationError: If critical configuration is missing/invalid
        """
        if self.is_production:
            errors = []
            
            # Check for missing secrets
            if not self.SECRET_KEY:
                errors.append(
                    "SECRET_KEY environment variable is REQUIRED in production. "
                    "Generate with: python -c \"import secrets; print(secrets.token_urlsafe(32))\""
                )
            
            if not self.API_TOKEN:
                errors.append(
                    "API_TOKEN environment variable is REQUIRED in production. "
                    "Generate with: python -c \"import secrets; print(secrets.token_urlsafe(32))\""
                )
            
            # Check for unsafe settings
            if self.DEBUG:
                errors.append("DEBUG=True is not allowed in production. Set DEBUG=False.")
            
            if errors:
                error_message = "\n".join(errors)
                logger.critical(f"Configuration validation failed in production mode:\n{error_message}")
                raise ConfigurationError(f"Invalid production configuration:\n{error_message}")
            
            logger.info("Production configuration validated successfully")
        else:
            # Development/Staging: provide helpful warnings if secrets are missing
            if not self.SECRET_KEY:
                logger.warning(
                    "SECRET_KEY not set. Using development default. "
                    "Set SECRET_KEY environment variable before deploying to production."
                )
            
            if not self.API_TOKEN:
                logger.warning(
                    "API_TOKEN not set. Using development default. "
                    "Set API_TOKEN environment variable before deploying to production."
                )
            
            if self.DEBUG:
                logger.warning("DEBUG mode is enabled. Disable in production (DEBUG=False)")
    
    # =========================================================================
    # Computed Properties
    # =========================================================================
    
    @property
    def is_development(self) -> bool:
        """Check if running in development mode."""
        return self.ENVIRONMENT in ("development", "dev", "local")
    
    @property
    def is_staging(self) -> bool:
        """Check if running in staging mode."""
        return self.ENVIRONMENT in ("staging", "stage", "preprod")
    
    @property
    def is_production(self) -> bool:
        """Check if running in production mode."""
        return self.ENVIRONMENT in ("production", "prod")
    
    @property
    def database_is_sqlite(self) -> bool:
        """Check if using SQLite database."""
        return "sqlite" in self.DATABASE_URL.lower()
    
    @property
    def database_is_postgres(self) -> bool:
        """Check if using PostgreSQL database."""
        return "postgresql" in self.DATABASE_URL.lower() or "postgres" in self.DATABASE_URL.lower()
    
    @property
    def app_url(self) -> str:
        """Get the application base URL."""
        return f"http://{self.HOST}:{self.PORT}"
    
    def __repr__(self) -> str:
        """String representation of settings (safe for logging)."""
        db_type = "sqlite" if self.database_is_sqlite else ("postgres" if self.database_is_postgres else "unknown")
        return f"<Settings(env={self.ENVIRONMENT}, debug={self.DEBUG}, db={db_type})>"
    
    def to_dict(self, include_sensitive=False) -> dict:
        """
        Convert settings to dictionary.
        
        Args:
            include_sensitive: Include SECRET_KEY, API_TOKEN, etc. (default: False for safety)
        
        Returns:
            Dictionary of all settings with sensitive values masked by default
        """
        result = {}
        for key in dir(self):
            if key.startswith("_"):
                continue
            value = getattr(self, key)
            if callable(value):
                continue
            
            # Mask sensitive values by default
            if not include_sensitive and key in [
                "SECRET_KEY", "API_TOKEN", "SMTP_PASSWORD", 
                "REDIS_URL", "DATABASE_URL", "TELEGRAM_BOT_TOKEN"
            ]:
                result[key] = "***MASKED***"
            else:
                result[key] = value
        
        return result


# ============================================================================
# Singleton Instance Management
# ============================================================================

_settings_instance: Optional[Settings] = None


def get_settings() -> Settings:
    """
    Get the global settings instance (singleton pattern).
    
    This ensures only one Settings object is created and reused throughout
    the application, preventing multiple environment variable reads.
    
    Returns:
        Settings: The global settings instance
    
    Raises:
        ConfigurationError: If configuration validation fails
    
    Example:
        settings = get_settings()
        print(settings.DATABASE_URL)
    """
    global _settings_instance
    if _settings_instance is None:
        _settings_instance = Settings()
    return _settings_instance


def reset_settings():
    """
    Reset the global settings instance (mainly for testing).
    
    WARNING: Only use this in unit tests!
    """
    global _settings_instance
    _settings_instance = None
