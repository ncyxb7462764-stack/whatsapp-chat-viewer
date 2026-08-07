"""
Shared constants for WhatsApp Chat Viewer.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class MediaExtensions:
    """Supported media file extensions."""

    IMAGES = frozenset({
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".webp",
        ".bmp",
    })

    AUDIO = frozenset({
        ".aac",
        ".amr",
        ".m4a",
        ".mp3",
        ".ogg",
        ".opus",
        ".wav",
        ".flac",
    })

    VIDEO = frozenset({
        ".mp4",
        ".avi",
        ".mov",
        ".mkv",
        ".3gp",
        ".webm",
    })

    DOCUMENTS = frozenset({
        ".pdf",
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
        ".txt",
        ".csv",
        ".zip",
        ".rar",
        ".7z",
    })


@dataclass(frozen=True, slots=True)
class WorkspaceNames:
    """Workspace directory names."""

    HTML = "html"
    MEDIA = "media"
    REPORTS = "reports"
    TEMP = "temp"


@dataclass(frozen=True, slots=True)
class ParserDefaults:
    """Default parser configuration."""

    ENCODING = "utf-8"

    DATE_FORMATS = (
        "%d/%m/%Y, %H:%M",
        "%d/%m/%y, %H:%M",
        "%d/%m/%Y %H:%M",
        "%d/%m/%y %H:%M",
    )


__all__ = [
    "MediaExtensions",
    "WorkspaceNames",
    "ParserDefaults",
]
