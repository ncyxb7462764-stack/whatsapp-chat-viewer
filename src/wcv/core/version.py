"""
Version handling for WhatsApp Chat Viewer.

This module provides the application's version information.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ReleaseStage(Enum):
    """Supported release stages."""

    DEV = "dev"
    ALPHA = "alpha"
    BETA = "beta"
    RC = "rc"
    STABLE = "stable"


@dataclass(frozen=True, slots=True)
class Version:
    """Immutable representation of a project version."""

    major: int
    minor: int
    patch: int
    stage: ReleaseStage
    build: int = 0

    @property
    def short(self) -> str:
        """Return the semantic version."""

        return f"{self.major}.{self.minor}.{self.patch}"

    @property
    def full(self) -> str:
        """Return the complete version string."""

        if self.stage is ReleaseStage.STABLE:
            return self.short

        return (
            f"{self.major}.{self.minor}.{self.patch}-"
            f"{self.stage.value}{self.build:03d}"
        )

    def __str__(self) -> str:
        """Return the full version string."""

        return self.full


VERSION = Version(
    major=2,
    minor=0,
    patch=0,
    stage=ReleaseStage.DEV,
    build=1,
)

__version__ = str(VERSION)
