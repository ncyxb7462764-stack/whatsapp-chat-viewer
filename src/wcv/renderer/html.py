"""
HTML renderer.
"""

from __future__ import annotations

from wcv.parser.chat import Chat
from wcv.renderer.templates import (
    MESSAGE_TEMPLATE,
    PAGE_TEMPLATE,
    SYSTEM_TEMPLATE,
)


class HtmlRenderer:
    """Render a Chat object as HTML."""

    def render(self, chat: Chat) -> str:
        blocks: list[str] = []

        for message in chat:

            if message.system:
                blocks.append(
                    SYSTEM_TEMPLATE.format(
                        text=message.text,
                    )
                )
            else:
                blocks.append(
                    MESSAGE_TEMPLATE.format(
                        author=message.author,
                        text=message.text,
                    )
                )

        return PAGE_TEMPLATE.format(
            content="\n".join(blocks)
        )