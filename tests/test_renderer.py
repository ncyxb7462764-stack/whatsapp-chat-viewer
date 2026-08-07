from pathlib import Path

from wcv.parser.loader import load_chat
from wcv.renderer.html import HtmlRenderer


def test_html_renderer() -> None:
    chat = load_chat(
        Path("tests/data/android/chat_simple.txt")
    )

    renderer = HtmlRenderer()

    html = renderer.render(chat)

    assert "<html" in html
    assert "</html>" in html
    assert "WhatsApp Chat Viewer" in html