from wcv.core.exceptions import (
    InvalidChatError,
    MediaNotFoundError,
    ParserError,
    RenderingError,
    WCVError,
)


def test_parser_error_inherits_base() -> None:
    assert issubclass(ParserError, WCVError)


def test_invalid_chat_inherits_parser() -> None:
    assert issubclass(InvalidChatError, ParserError)


def test_media_error_can_be_raised() -> None:
    try:
        raise MediaNotFoundError("missing")
    except WCVError:
        assert True


def test_rendering_error_can_be_raised() -> None:
    try:
        raise RenderingError("render failed")
    except WCVError:
        assert True