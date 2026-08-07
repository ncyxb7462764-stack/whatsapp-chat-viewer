"""
High level chat loader.
"""

from __future__ import annotations

from wcv.core.types import PathLike
from wcv.parser.chat import Chat
from wcv.parser.parser import parse_message
from wcv.parser.reader import read_chat


def load_chat(path: PathLike) -> Chat:
    """Load and parse an exported WhatsApp chat."""

    return Chat(
        messages=[
            parse_message(block)
            for block in read_chat(path)
        ]
    )
