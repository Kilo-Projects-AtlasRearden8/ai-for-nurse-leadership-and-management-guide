"""Build the static HTML site from Markdown docs.

Usage: python build.py

Reads docs/*.md and writes site/*.html plus site/assets/style.css.
Stdlib only. No secrets, no network, no API keys.
"""

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"
ASSETS = SITE / "assets"

# (source markdown file, output html file, page title, nav label, order)
PAGES = [
    ("00-overview.md", "index.html", "AI for Nurse Managers & Leaders", "Overview", 1),
    ("01-staff-education.md", "staff-education.html", "Staff Education", "Staff Education", 2),
    ("02-policy-drafts.md", "policy-drafts.html", "Policy Drafts", "Policy Drafts", 3),
    ("03-meeting-prep.md", "meeting-prep.html", "Meeting Prep", "Meeting Prep", 4),
    ("04-workload-planning.md", "workload-planning.html", "Workload Planning", "Workload Planning", 5),
    ("05-worksheets.md", "worksheets.html", "Printable Worksheets", "Worksheets", 6),
    ("06-disclaimer.md", "disclaimer.html", "Disclaimer: Education Only", "Disclaimer", 7),
]

def md_to_html(text: str) -> str:
    """Convert a subset of Markdown to HTML."""
    lines = text.split("\n")
    out = []
    i = 0
    n = len(lines)

    def inline(s: str) -> str:
        # Escape HTML first, then add markup.
        s = html.escape(s)
        # Code spans
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        # Bold **...**
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        # Italic *...* (not already consumed by bold)
        s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
        # Links [text](url)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        return s

    def blockquote(lines_block):
        inner = "\n".join(l[2:] if l.startswith("> ") else l[1:] for l in lines_block)
        return f"<blockquote>{md_to_html(inner)}</blockquote>"

    while i < n:
        line = lines[i]

        # Blank line
        if line.strip() == "":
            out.append("")
            i += 1
            continue

        # Horizontal rule
        if re.match(r"^(\*\*|---|___)\s*$", line):
            out.append("<hr>")
            i += 1
            continue

        # Heading
        m = re.match(r"^(#{1,6})\s+(.+)$", line)
        if m:
            level = len(m.group(1))
            content = inline(m.group(2).strip())
            out.append(f"<h{level}>{content}</h{level}>")
            i += 1
            continue

        # Blockquote block
        if line.startswith(">"):
            block = []
            while i < n and lines[i].startswith(">"):
                block.append(lines[i])
                i += 1
            out.append(blockquote(block))
            continue

        # Fenced code block
        m = re.match(r"^```(\w*)", line)
        if m:
            lang = m.group(1)
            code_lines = []
            i += 1
            while i < n and not lines[i].startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            code = "\n".join(code_lines)
            out.append(f"<pre><code class=\"lang-{html.escape(lang)}\">{html.escape(code)}</code></pre>")
            continue

        # Table
        if line.startswith("|"):
            rows = []
            while i < n and lines[i].startswith("|"):
                rows.append(lines[i])
                i += 1
            # parse rows
            html_rows = []
            for r_idx, row in enumerate(rows):
                cells = [c.strip() for c in row.strip().strip("|").split("|")]
                tag = "th" if r_idx == 0 else "td"
                # skip separator row (---)
                if all(re.fullmatch(r":?-+:?", c) for c in cells):
                    continue
                html_rows.append(
                    "<tr>" + "".join(f"<{tag}>{inline(c)}</{tag}>" for c in cells) + "</tr>"
                )
            out.append("<table>" + "".join(html_rows) + "</table>")
            continue

        # List block (ordered, unordered, task)
        if re.match(r"^\s*\d+\.\s+", line) or re.match(r"^\s*([*+-])\s+", line):
            items = []
            ordered = bool(re.match(r"^\s*\d+\.\s+", line))
            tag = "ol" if ordered else "ul"
            while i < n:
                l = lines[i]
                om = re.match(r"^(\s*)\d+\.\s+(.*)$", l)
                um = re.match(r"^(\s*)([*+-])\s+(.*)$", l)
                if om:
                    items.append(("li", om.group(2), bool(re.match(r"^\s*\[[ x]\]\s", om.group(2)))))
                    i += 1
                elif um:
                    items.append(("li", um.group(3), bool(re.match(r"^\s*\[[ x]\]\s", um.group(3)))))
                    i += 1
                else:
                    break
            html_items = []
            for _, content, is_task in items:
                if is_task:
                    content = re.sub(r"^\[[ x]\]\s*", "", content)
                    checked = ""
                    html_items.append(f"<li><input type=\"checkbox\" disabled{checked}> {inline(content)}</li>")
                else:
                    html_items.append(f"<li>{inline(content)}</li>")
            out.append(f"<{tag}>" + "".join(html_items) + f"</{tag}>")
            continue

        # Paragraph
        paras = []
        while i < n and lines[i].strip() != "":
            paras.append(lines[i])
            i += 1
        out.append("<p>" + inline(" ".join(paras)) + "</p>")

    return "\n".join(out)


def build_page(source: Path, title: str, active: str) -> str:
    body_md = source.read_text(encoding="utf-8")
    body_html = md_to_html(body_md)

    nav_items = "\n".join(
        f'<li><a href="{href}"{" class=\"active\"" if label == active else ""}>{label}</a></li>'
        for _, href, _, label, _ in sorted(PAGES, key=lambda p: p[4])
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — AI for Nurse Managers &amp; Leaders</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="site-header">
  <div class="wrapper">
    <a class="brand" href="index.html">Asdale Dynamics, LLC</a>
    <nav>
      <ul class="nav-list">
        {nav_items}
      </ul>
    </nav>
  </div>
</header>

<main class="wrapper">
  <article>
    <header class="page-header">
      <h1>{title}</h1>
      <p class="meta">Education only — not medical or HR advice</p>
    </header>
    {body_html}
  </article>

  <aside class="print-hide">
    <h3>Sections</h3>
    <ul>
      <li><a href="index.html">Overview</a></li>
      <li><a href="staff-education.html">Staff Education</a></li>
      <li><a href="policy-drafts.html">Policy Drafts</a></li>
      <li><a href="meeting-prep.html">Meeting Prep</a></li>
      <li><a href="workload-planning.html">Workload Planning</a></li>
      <li><a href="worksheets.html">Printable Worksheets</a></li>
      <li><a href="disclaimer.html">Disclaimer</a></li>
    </ul>
    <p class="small">Print any page with Ctrl+P / Command+P. Worksheets print cleanly.</p>
  </aside>
</main>

<footer class="site-footer">
  <div class="wrapper">
    <p>&copy; 2026 Asdale Dynamics, LLC.</p>
    <p class="small">Beginner-friendly AI education for nurse managers and leaders.</p>
  </div>
</footer>
</body>
</html>"""


CSS = """/* Asdale Dynamics, LLC — AI for Nurse Managers & Leaders */
:root {
  --ink: #111827;
  --muted: #4b5563;
  --bg: #ffffff;
  --paper: #fafafa;
  --line: #e5e7eb;
  --accent: #0f6b4c;
  --accent-hover: #0d5a3f;
  --warn: #7f1d1d;
  --bg-warn: #fef2f2;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
  color: var(--ink);
  background: var(--bg);
  line-height: 1.6;
}
.wrapper { max-width: 900px; margin: 0 auto; padding: 0 20px; }

/* Header */
.site-header {
  background: var(--accent);
  color: #fff;
  border-bottom: 1px solid rgba(255,255,255,0.3);
}
.site-header .wrapper { display: flex; align-items: center; justify-content: space-between; gap: 16px; padding: 14px 20px; }
.brand { font-weight: 700; font-size: 1.25rem; color: #fff; text-decoration: none; }
.nav-list { display: flex; gap: 16px; list-style: none; margin: 0; padding: 0; }
.nav-list a { color: #d1fae5; text-decoration: none; font-size: 0.95rem; padding: 6px 10px; border-radius: 6px; }
.nav-list a:hover, .nav-list a.active { background: rgba(255,255,255,0.15); color: #fff; }

/* Main */
main { display: grid; grid-template-columns: 1fr 260px; gap: 32px; padding: 32px 0; }
article h1 { font-size: 1.75rem; margin: 0 0 4px 0; letter-spacing: -0.01em; }
article h2 { font-size: 1.35rem; margin: 32px 0 10px 0; border-bottom: 1px solid var(--line); padding-bottom: 6px; }
article h3 { font-size: 1.15rem; margin: 24px 0 8px 0; }
article h4 { font-size: 1.05rem; margin: 20px 0 6px 0; }
article p { margin: 0 0 14px 0; }
article ul, article ol { margin: 6px 0 14px 0; padding-left: 22px; }
article li { margin-bottom: 6px; }
article table { width: 100%; border-collapse: collapse; margin: 14px 0; font-size: 0.95rem; }
article th, article td { border: 1px solid var(--line); padding: 8px 10px; text-align: left; }
article th { background: var(--paper); font-weight: 600; }
article code { background: var(--paper); padding: 1px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 0.9em; }
article pre { background: #1e293b; color: #e2e8f0; padding: 14px; border-radius: 8px; overflow-x: auto; margin: 14px 0; }
article pre code { background: inherit; color: inherit; padding: 0; }
article blockquote { border-left: 4px solid var(--accent); margin: 14px 0; padding: 10px 16px; background: var(--paper); font-style: italic; }
article hr { border: none; border-top: 1px solid var(--line); margin: 24px 0; }

.meta { color: var(--muted); font-size: 0.9rem; margin: 4px 0 20px 0; }

/* Aside */
aside h3 { font-size: 1rem; margin-top: 0; border-bottom: 1px solid var(--line); padding-bottom: 6px; }
aside ul { list-style: none; padding: 0; margin: 10px 0 16px 0; }
aside li { margin-bottom: 6px; }
aside a { color: var(--accent); text-decoration: none; }
aside a:hover { text-decoration: underline; }
aside .small { font-size: 0.85rem; color: var(--muted); }

/* Footer */
.site-footer { border-top: 1px solid var(--line); padding: 24px 0; margin-top: 40px; }
.site-footer .wrapper { display: flex; flex-direction: column; gap: 6px; font-size: 0.9rem; color: var(--muted); }

/* Worksheet blocks */
article pre, article code {
  /* worksheet monospace blocks keep their look on screen and paper */
}
.print-hide { display: block; }

/* Callout boxes */
.callout { border-left: 4px solid var(--accent); background: #f0fdfa; padding: 12px 16px; margin: 16px 0; border-radius: 0 8px 8px 0; }
.callout.warn { border-left-color: var(--warn); background: var(--bg-warn); }

/* Print */
@media print {
  .print-hide, .site-header, .site-footer, nav, aside { display: none !important; }
  body { background: #fff; color: #000; }
  a { color: #000; text-decoration: none; }
  article { margin: 0; padding: 0; }
  article h2 { border-bottom: 1px solid #000; }
  pre, blockquote, table { page-break-inside: avoid; }
  @page { margin: 18mm; }
}
@media (max-width: 720px) {
  main { grid-template-columns: 1fr; }
  aside { display: none; }
  .site-header .wrapper { flex-direction: column; align-items: stretch; gap: 10px; }
  .nav-list { justify-content: center; }
}
"""

def main():
    SITE.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)

    # Write CSS
    (ASSETS / "style.css").write_text(CSS, encoding="utf-8")

    # Build pages
    for source_name, out_name, title, label, _ in PAGES:
        source = DOCS / source_name
        if not source.exists():
            raise SystemExit(f"Missing source: {source}")
        html_text = build_page(source, title, label)
        (SITE / out_name).write_text(html_text, encoding="utf-8")
        print(f"built {out_name} <- {source_name}")

    print(f"Built {len(PAGES)} pages into {SITE}")


if __name__ == "__main__":
    main()
