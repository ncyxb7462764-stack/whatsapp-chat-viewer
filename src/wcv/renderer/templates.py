"""
HTML templates.
"""

from __future__ import annotations

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>WhatsApp Chat Viewer</title>
</head>
<body>

{content}

</body>
</html>
"""

MESSAGE_TEMPLATE = """
<div class="message">
    <strong>{author}</strong><br>
    {text}
</div>
"""

SYSTEM_TEMPLATE = """
<div class="system">
    {text}
</div>
"""