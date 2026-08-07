from pathlib import Path

from wcv.core.types import (
    JSONArray,
    JSONObject,
    JSONValue,
    PathLike,
)


def test_pathlike_accepts_str() -> None:
    path: PathLike = "chat.txt"
    assert isinstance(path, str)


def test_pathlike_accepts_path() -> None:
    path: PathLike = Path("chat.txt")
    assert isinstance(path, Path)


def test_json_object() -> None:
    data: JSONObject = {
        "name": "Alice",
        "count": 10,
        "active": True,
    }

    assert data["name"] == "Alice"


def test_json_array() -> None:
    values: JSONArray = ["a", 1, False]

    assert len(values) == 3


def test_json_value() -> None:
    value: JSONValue = {
        "nested": [
            {"id": 1},
            {"id": 2},
        ]
    }

    assert isinstance(value, dict)
