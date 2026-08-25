"""
OmniThread OS Configuration Module

This module provides centralized configuration management for the entire application.
It handles environment variables, settings validation, and provides a single source
of truth for all configuration needs.

Usage:
    from src.config import get_settings
    settings = get_settings()
    print(settings.DATABASE_URL)

Security:
    - All SECRET_* variables MUST be set in production
    - No default secrets are provided
    - Application will fail to start in production with missing secrets
"""

from .settings import Settings, get_settings, ConfigurationError

__all__ = ["Settings", "get_settings", "ConfigurationError"]

# Version tracking for this module
__version__ = "1.0.0"
