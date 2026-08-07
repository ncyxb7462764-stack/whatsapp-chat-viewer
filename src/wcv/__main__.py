"""
Application entry point for WhatsApp Chat Viewer.
"""

from __future__ import annotations

from wcv.core.version import VERSION


def main() -> int:
    """Run the application."""

    print("WhatsApp Chat Viewer")
    print(f"Version {VERSION.full}")
    print()
    print("Ready.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
