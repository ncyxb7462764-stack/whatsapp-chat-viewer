from wcv.core.constants import (
    MediaExtensions,
    ParserDefaults,
    WorkspaceNames,
)


def test_flac_supported() -> None:
    assert ".flac" in MediaExtensions.AUDIO


def test_jpg_supported() -> None:
    assert ".jpg" in MediaExtensions.IMAGES


def test_workspace_names() -> None:
    assert WorkspaceNames.HTML == "html"
    assert WorkspaceNames.MEDIA == "media"


def test_default_encoding() -> None:
    assert ParserDefaults.ENCODING == "utf-8"


def test_date_formats() -> None:
    assert len(ParserDefaults.DATE_FORMATS) >= 4
