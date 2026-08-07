"""
Workspace path management for WhatsApp Chat Viewer.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from wcv.core.constants import WorkspaceNames


@dataclass(frozen=True, slots=True)
class WorkspacePaths:
    """Represents the directory structure of a workspace."""

    root: Path

    @property
    def html(self) -> Path:
        return self.root / WorkspaceNames.HTML

    @property
    def media(self) -> Path:
        return self.root / WorkspaceNames.MEDIA

    @property
    def reports(self) -> Path:
        return self.root / WorkspaceNames.REPORTS

    @property
    def temp(self) -> Path:
        return self.root / WorkspaceNames.TEMP

    def create(self) -> None:
        """Create every workspace directory."""

        self.root.mkdir(parents=True, exist_ok=True)

        self.html.mkdir(parents=True, exist_ok=True)
        self.media.mkdir(parents=True, exist_ok=True)
        self.reports.mkdir(parents=True, exist_ok=True)
        self.temp.mkdir(parents=True, exist_ok=True)
