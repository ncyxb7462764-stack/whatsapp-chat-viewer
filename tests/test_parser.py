from wcv.parser.parser import parse_message


def test_parse_user_message() -> None:
    raw = (
        "21/7/2026, 00:25 - "
        "Néstor David Báez Lovera: Hola"
    )

    message = parse_message(raw)

    assert message.author == "Néstor David Báez Lovera"
    assert message.text == "Hola"
    assert not message.system


def test_parse_system_message() -> None:
    raw = (
        "26/5/2026, 22:05 - "
        "Los mensajes y las llamadas están cifrados..."
    )

    message = parse_message(raw)

    assert message.author is None
    assert message.system


def test_parse_multiline_message() -> None:
    raw = (
        "21/7/2026, 00:26 - "
        "WhatsApp Claro: Del Maestro\n"
        "ubicación: https://maps.google.com/"
    )

    message = parse_message(raw)

    assert "ubicación:" in message.text
