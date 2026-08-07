from pathlib import Path

from wcv.parser.reader import read_chat


def test_reader_returns_messages() -> None:

    chat = Path("tests/data/android/chat_simple.txt")

    messages = read_chat(chat)

    assert len(messages) > 0


def test_first_message_is_system() -> None:

    chat = Path("tests/data/android/chat_simple.txt")

    messages = read_chat(chat)

    assert "Los mensajes y las llamadas" in messages[0]


def test_multiline_message() -> None:

    chat = Path("tests/data/android/chat_simple.txt")

    messages = read_chat(chat)

    multiline = next(
        message
        for message in messages
        if "Del Maestro" in message
    )

    assert "ubicación:" in multiline
