#!/usr/bin/env python3
"""Static-site validation for UGN GTA VI Guide. No third-party packages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
errors = []
warnings = []
pages = sorted(ROOT.glob("*.html"))
class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()
        self.duplicates = []
        self.title = []
        self.in_title = False
        self.description = False
        self.canonicals = []
        self.robots = []
        self.og_urls = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "meta" and a.get("name", "").lower() == "description" and a.get("content", "").strip():
            self.description = True
        if tag == "link" and a.get("rel", "").lower() == "canonical":
            self.canonicals.append(a.get("href", ""))
        if tag == "meta" and a.get("name", "").lower() == "robots":
            self.robots.append(a.get("content", ""))
        if tag == "meta" and a.get("property", "").lower() == "og:url":
            self.og_urls.append(a.get("content", ""))
        if "id" in a:
            if a["id"] in self.ids:
                self.duplicates.append(a["id"])
            self.ids.add(a["id"])
        if tag in ("a", "link", "script", "img"):
            url = a.get("href") if tag in ("a", "link") else a.get("src")
            if url:
                self.links.append((tag, url))
    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)

for page in pages:
    parser = PageParser()
    try:
        parser.feed(page.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{page.name}: HTML parse failed: {exc}")
        continue
    if not "".join(parser.title).strip():
        errors.append(f"{page.name}: missing title")
    if not parser.description:
        warnings.append(f"{page.name}: missing meta description")
    expected_canonical = "https://universal-gaming.github.io/GTA-6-Guide/" + ("" if page.name == "index.html" else page.name)
    if parser.canonicals != [expected_canonical]:
        errors.append(f"{page.name}: expected one correct canonical URL, got {parser.canonicals}")
    if parser.og_urls and parser.og_urls != [expected_canonical]:
        errors.append(f"{page.name}: Open Graph URL differs from canonical")
    if any("noindex" in value.lower() for value in parser.robots):
        warnings.append(f"{page.name}: noindex directive blocks search visibility")
    for duplicate in parser.duplicates:
        errors.append(f"{page.name}: duplicate HTML id '{duplicate}'")
    for tag, url in parser.links:
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc or url.startswith("//") or url.startswith("mailto:") or url.startswith("tel:"):
            continue
        local_path = unquote(parsed.path)
        target = (page.parent / local_path).resolve() if local_path else page.resolve()
        if local_path.endswith("/"):
            target = target / "index.html"
        if not target.is_relative_to(ROOT.resolve()):
            errors.append(f"{page.name}: link escapes repository: {url}")
            continue
        if not target.exists():
            errors.append(f"{page.name}: broken {tag} path: {url}")
            continue
        if parsed.fragment and target.suffix == ".html":
            # Validate fragments on the target document, not only the source.
            check = PageParser()
            check.feed(target.read_text(encoding="utf-8"))
            if unquote(parsed.fragment) not in check.ids:
                warnings.append(f"{page.name}: missing anchor target: {url}")
try:
    tree = ET.parse(ROOT / "sitemap.xml")
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap_urls = [e.text for e in tree.findall(".//s:loc", namespace)]
    if len(sitemap_urls) != len(set(sitemap_urls)):
        errors.append("sitemap.xml: duplicate URLs")
    for page in pages:
        expected = "https://universal-gaming.github.io/GTA-6-Guide/" + ("" if page.name == "index.html" else page.name)
        if expected not in sitemap_urls:
            warnings.append(f"sitemap.xml: {page.name} is not indexed")
    for url in sitemap_urls:
        parsed = urlsplit(url)
        if parsed.netloc != "universal-gaming.github.io" or not parsed.path.startswith("/GTA-6-Guide/"):
            errors.append(f"sitemap.xml: unexpected site URL: {url}")
            continue
        path = parsed.path.removeprefix("/GTA-6-Guide/") or "index.html"
        if not (ROOT / path).exists():
            errors.append(f"sitemap.xml: URL does not resolve to a file: {url}")
except Exception as exc:
    errors.append(f"sitemap.xml: XML parsing failed: {exc}")

for warning in warnings:
    print("WARNING:", warning)
for error in errors:
    print("ERROR:", error)
print(f"Checked {len(pages)} HTML pages, {len(warnings)} warnings, {len(errors)} errors.")
sys.exit(1 if errors else 0)
