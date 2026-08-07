from datetime import date, time

from wcv.parser.chat import Chat
from wcv.parser.message import Message


def test_chat_length() -> None:
    chat = Chat(
        messages=[
            Message(date.today(), time(), "A", "Hola"),
            Message(date.today(), time(), "B", "Mundo"),
        ]
    )

    assert len(chat) == 2


def test_chat_iteration() -> None:
    chat = Chat(
        messages=[
            Message(date.today(), time(), "A", "Hola"),
        ]
    )

    assert next(iter(chat)).author == "A"
