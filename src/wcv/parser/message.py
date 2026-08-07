"""
WhatsApp message model.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, time


@dataclass(frozen=True, slots=True)
class Message:
    """Represents a parsed WhatsApp message."""

    date: date
    time: time
    author: str | None
    text: str
    system: bool = False
