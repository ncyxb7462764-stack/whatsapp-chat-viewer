from pathlib import Path

from wcv.core.paths import WorkspacePaths


def test_workspace_paths() -> None:
    workspace = WorkspacePaths(Path("workspace"))

    assert workspace.html == Path("workspace/html")
    assert workspace.media == Path("workspace/media")
    assert workspace.reports == Path("workspace/reports")
    assert workspace.temp == Path("workspace/temp")


def test_workspace_creation(tmp_path) -> None:
    workspace = WorkspacePaths(tmp_path)

    workspace.create()

    assert workspace.html.exists()
    assert workspace.media.exists()
    assert workspace.reports.exists()
    assert workspace.temp.exists()
