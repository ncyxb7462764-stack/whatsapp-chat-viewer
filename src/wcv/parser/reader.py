"""
Raw WhatsApp export reader.
"""

from __future__ import annotations

import re

from wcv.core.types import PathLike

_MESSAGE_START = re.compile(
    r"^\d{1,2}/\d{1,2}/\d{4},\s\d{2}:\d{2}\s-"
)


def read_chat(path: PathLike) -> list[str]:
    """
    Read a WhatsApp exported chat and split it into raw message blocks.
    """

    with open(path, encoding="utf-8") as file:
        lines = file.read().splitlines()

    messages: list[str] = []

    current: list[str] = []

    for line in lines:

        if _MESSAGE_START.match(line):

            if current:
                messages.append("\n".join(current))

            current = [line]

        else:

            current.append(line)

    if current:
        messages.append("\n".join(current))

    return messages
