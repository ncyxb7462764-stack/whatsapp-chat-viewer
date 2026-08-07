from dataclasses import FrozenInstanceError
from datetime import date, time

import pytest

from wcv.parser.message import Message


def test_slots_and_frozen() -> None:
    message = Message(
        date=date.today(),
        time=time(),
        author="User",
        text="Test",
    )

    with pytest.raises(FrozenInstanceError):
        message.text = "Otro"
