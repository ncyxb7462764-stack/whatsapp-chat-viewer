"""
Chat domain model.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass

from wcv.parser.message import Message


@dataclass(frozen=True, slots=True)
class Chat:
    messages: list[Message]

    def __len__(self) -> int:
        return len(self.messages)

    def __iter__(self) -> Iterator[Message]:
        return iter(self.messages)
