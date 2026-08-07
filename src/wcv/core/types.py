from __future__ import annotations

from pathlib import Path

type PathLike = str | Path

type JSONPrimitive = str | int | float | bool | None

type JSONValue = (
    JSONPrimitive
    | dict[str, JSONValue]
    | list[JSONValue]
)

type JSONObject = dict[str, JSONValue]
type JSONArray = list[JSONValue]

__all__ = [
    "JSONArray",
    "JSONObject",
    "JSONPrimitive",
    "JSONValue",
    "PathLike",
]

