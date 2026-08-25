"""
OmniThread OS - Core Module

This module contains core functionality, utilities, and application metadata.
It serves as the foundation for all other modules.

Module Structure:
    - Version tracking
    - Logger initialization
    - Utility functions
    - Application constants
"""

import os
import sys
import logging
import warnings
from pathlib import Path
from typing import Optional

# Application Metadata
__title__ = "OmniThread OS"
__description__ = "High-performance, self-healing, multi-node enterprise AIaaS and cluster monitoring OS"
__version__ = "2.0.0"  # Bumped from 1.0.0 for production-readiness
__author__ = "mdboratullah"
__author_email__ = "mdboratullah@example.com"
__license__ = "Other"
__url__ = "https://github.com/mdboratullah/OmniThread-OS"

# ============================================================================
# Paths
# ============================================================================

# Root directory of the project
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Source directory
SRC_DIR = PROJECT_ROOT / "src"

# Logs directory
LOGS_DIR = PROJECT_ROOT / "logs"

# Ensure logs directory exists
LOGS_DIR.mkdir(exist_ok=True)

# Configure module logger
logger = logging.getLogger(__name__)


# ============================================================================
# Logger Setup
# ============================================================================

def get_logger(name: str):
    """
    Get a logger instance for a module.
    
    This function provides proper logging configuration for all modules.
    Logging level is controlled via LOG_LEVEL environment variable.
    
    Args:
        name: Logger name (typically __name__)
    
    Returns:
        A logger instance configured with StreamHandler
    
    Example:
        from src.core import get_logger
        logger = get_logger(__name__)
        logger.info("Application started")
    """
    logger_instance = logging.getLogger(name)
    
    # Only configure if this is a new logger without handlers
    if not logger_instance.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger_instance.addHandler(handler)
        logger_instance.setLevel(logging.INFO)
    
    return logger_instance


# ============================================================================
# Version Info
# ============================================================================

def get_version() -> str:
    """Get the application version."""
    return __version__


# ============================================================================
# Health Check
# ============================================================================

class AppHealth:
    """Application health check utility."""
    
    @staticmethod
    def check_dependencies() -> dict:
        """Check if critical dependencies are installed."""
        dependencies = {
            "flask": "Flask web framework",
            "psutil": "System monitoring",
            "dotenv": "Environment configuration",
        }
        
        result = {}
        for dep, description in dependencies.items():
            try:
                __import__(dep.replace("-", "_"))
                result[dep] = f"✓ {description}"
            except ImportError:
                result[dep] = f"✗ {description} (not installed)"
        
        return result
    
    @staticmethod
    def check_directories() -> dict:
        """Check if required directories exist."""
        dirs = {
            "logs": LOGS_DIR.exists(),
            "src": SRC_DIR.exists(),
            "src/config": (SRC_DIR / "config").exists(),
        }
        return {k: "✓ Exists" if v else "✗ Missing" for k, v in dirs.items()}
    
    @staticmethod
    def get_health_report() -> dict:
        """Get complete health report."""
        return {
            "version": get_version(),
            "python_version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
            "environment": os.getenv("ENVIRONMENT", "unknown"),
            "dependencies": AppHealth.check_dependencies(),
            "directories": AppHealth.check_directories(),
        }


# ============================================================================
# Backward Compatibility Bridge (DEPRECATED)
# ============================================================================

def legacy_config_bridge():
    """
    Provide backward compatibility for old config.py imports.
    
    DEPRECATED: This function is maintained for backward compatibility only.
    New code should use: from src.config import get_settings
    
    Existing code like `from config import PORT` will still work through
    the old config.py file, but those imports now pull from the new
    centralized configuration system.
    
    This is a temporary bridge during migration. Old code should be
    updated to use the new settings system.
    
    Warning:
        Deprecation warning is logged when this function is called.
    
    Returns:
        Dictionary of legacy configuration values (for old config.py)
    """
    warnings.warn(
        "legacy_config_bridge() is deprecated. "
        "Use 'from src.config import get_settings' instead.",
        DeprecationWarning,
        stacklevel=2
    )
    
    logger.warning(
        "Legacy config.py imports detected. "
        "This is deprecated. Migrate to: from src.config import get_settings"
    )
    
    from src.config import get_settings
    settings = get_settings()
    
    # Export the old config module's attributes for compatibility
    return {
        "PORT": settings.PORT,
        "DB_FILE": settings.DB_FILE,
        "ENVIRONMENT": settings.ENVIRONMENT,
        "SECRET_ENCRYPTION_KEY": settings.SECRET_KEY,
        "API_TOKEN": settings.API_TOKEN,
    }


__all__ = [
    "get_logger",
    "get_version",
    "AppHealth",
    "legacy_config_bridge",
    "PROJECT_ROOT",
    "SRC_DIR",
    "LOGS_DIR",
    "__version__",
    "__title__",
    "__description__",
]
