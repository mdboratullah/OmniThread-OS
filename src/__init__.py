"""
OmniThread OS - Application Package

This is the main application package. All modules and sub-packages are
orchestrated from here.
"""

from src.core import get_version

__version__ = get_version()

__all__ = ["__version__"]
