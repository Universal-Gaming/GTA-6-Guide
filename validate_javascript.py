#!/usr/bin/env python3
"""Check inline JavaScript in all HTML pages using Node.js, without dependencies."""
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys
import tempfile

class Scripts(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.chunks = []
        self.scripts = []
    def handle_starttag(self, tag, attrs):
        if tag == "script":
            data = dict(attrs)
            self.active = not data.get("src") and data.get("type", "text/javascript") in ("text/javascript", "module")
            self.chunks = []
    def handle_data(self, data):
        if self.active:
            self.chunks.append(data)
    def handle_endtag(self, tag):
        if tag == "script" and self.active:
            self.scripts.append("".join(self.chunks))
            self.active = False

root = Path(__file__).resolve().parent
checked = 0
failed = 0
with tempfile.TemporaryDirectory() as directory:
    target = Path(directory) / "inline.js"
    for page in sorted(root.glob("*.html")):
        parser = Scripts()
        parser.feed(page.read_text(encoding="utf-8"))
        for index, script in enumerate(parser.scripts, 1):
            if not script.strip():
                continue
            target.write_text(script, encoding="utf-8")
            result = subprocess.run(["node", "--check", str(target)], capture_output=True, text=True)
            checked += 1
            if result.returncode:
                failed += 1
                print(f"ERROR: {page.name} script {index}: {result.stderr.strip()}")
print(f"Checked {checked} inline JavaScript blocks; {failed} errors.")
sys.exit(bool(failed))
