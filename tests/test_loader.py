from pathlib import Path

from wcv.parser.loader import load_chat


def test_load_chat() -> None:
    chat = load_chat(
        Path("tests/data/android/chat_simple.txt")
    )

    assert len(chat) > 0
