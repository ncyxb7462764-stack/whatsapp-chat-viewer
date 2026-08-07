from wcv.core.version import (
    ReleaseStage,
    VERSION,
    Version,
    __version__,
)


def test_short_version() -> None:
    assert VERSION.short == "2.0.0"


def test_full_version() -> None:
    assert VERSION.full == "2.0.0-dev001"


def test_string_conversion() -> None:
    assert str(VERSION) == "2.0.0-dev001"


def test_public_version() -> None:
    assert __version__ == "2.0.0-dev001"


def test_stable_version() -> None:
    stable = Version(
        major=2,
        minor=0,
        patch=0,
        stage=ReleaseStage.STABLE,
    )

    assert stable.full == "2.0.0"