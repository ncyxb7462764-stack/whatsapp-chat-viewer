"""
Custom exceptions for WhatsApp Chat Viewer.
"""

from __future__ import annotations


class WCVError(Exception):
    """Base exception for all project-specific errors."""


class ConfigurationError(WCVError):
    """Raised when the application configuration is invalid."""


class ParserError(WCVError):
    """Raised when a chat cannot be parsed."""


class UnsupportedFormatError(ParserError):
    """Raised when the chat format is not supported."""


class InvalidChatError(ParserError):
    """Raised when the chat content is malformed."""


class MediaError(WCVError):
    """Base exception for media-related errors."""


class MediaNotFoundError(MediaError):
    """Raised when a referenced media file cannot be found."""


class RenderingError(WCVError):
    """Raised when HTML rendering fails."""


__all__ = [
    "WCVError",
    "ConfigurationError",
    "ParserError",
    "UnsupportedFormatError",
    "InvalidChatError",
    "MediaError",
    "MediaNotFoundError",
    "RenderingError",
]
