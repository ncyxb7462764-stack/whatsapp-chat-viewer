"""
WhatsApp message parser.
"""

from __future__ import annotations

from datetime import datetime

from wcv.parser.message import Message


def parse_message(block: str) -> Message:
    """
    Parse one raw WhatsApp message block.
    """

    lines = block.split("\n")

    header, *body = lines

    timestamp, rest = header.split(" - ", maxsplit=1)

    dt = datetime.strptime(timestamp, "%d/%m/%Y, %H:%M")

    if ": " in rest:

        author, first_text = rest.split(": ", maxsplit=1)

        text = "\n".join([first_text, *body]).strip()

        return Message(
            date=dt.date(),
            time=dt.time(),
            author=author,
            text=text,
            system=False,
        )

    text = "\n".join([rest, *body]).strip()

    return Message(
        date=dt.date(),
        time=dt.time(),
        author=None,
        text=text,
        system=True,
    )
