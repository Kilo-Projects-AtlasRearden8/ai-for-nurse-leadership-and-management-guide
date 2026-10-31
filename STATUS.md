# STATUS

## What was built

A beginner manual on AI for nurse managers and leaders, delivered as Markdown source plus a static HTML site.

**Repository contents**
- `docs/` — Markdown source of the manual:
  - `00-overview.md` — purpose, what AI is, golden rule for healthcare, how to use
  - `01-staff-education.md` — 30-minute staff huddle plan, ground rules, FAQ, worksheet
  - `02-policy-drafts.md` — fill-in-the-blank AI use policy template, adoption steps, worksheet
  - `03-meeting-prep.md` — step-by-step meeting prep workflow, example, do's/don'ts, worksheet
  - `04-workload-planning.md` — AI as a thinking partner for shift/assignment planning, safety checklist, worksheet
  - `05-worksheets.md` — combined printable worksheets page
  - `06-disclaimer.md` — education-only disclaimer
- `site/` — static HTML site (7 pages + `assets/style.css`):
  - `index.html`, `staff-education.html`, `policy-drafts.html`, `meeting-prep.html`,
    `workload-planning.html`, `worksheets.html`, `disclaimer.html`
- `build.py` — stdlib-only Python script converting `docs/*.md` to `site/*.html`
- `README.md` — overview, how to run, credits, license, disclaimer
- `LICENSE` — MIT License
- `STATUS.md` — this file

**Audiences and topics covered**
- Staff education on AI (huddle plan, ground rules)
- AI use policy drafts for a nursing unit
- Meeting prep (agendas, talking points, anticipated questions)
- Workload planning (shift and assignment planning thinking partner)
- Printable leadership worksheets (one per section + combined page)
- Education only: no medical advice, no HR advice, no legal advice

**Credit**
- Written by Dylan Asdale, RN, founder of Asdale Dynamics, LLC (Indiana, formed October 2026).
- Asdale Dynamics, LLC credited in `README.md` and on every page.
- `LICENSE` copyright line: `Copyright (c) 2026 Asdale Dynamics, LLC` (exact).

## How to run it

No install, no server, no network, no secrets. Python 3 standard library only.

```bash
python3 build.py
```

This writes the HTML site into `site/`. Open `site/index.html` in any browser, or print any page to PDF (Ctrl+P / Command+P). Worksheets are styled to print cleanly (print CSS hides navigation/header/footer).

## Verification results

- `python3 build.py` runs cleanly and builds all 7 HTML pages plus `assets/style.css`.
- Every page has `<title>`, closing `</html>`, and links to `assets/style.css`.
- `LICENSE` line 3 is exactly `Copyright (c) 2026 Asdale Dynamics, LLC`.
- `README.md` credits Asdale Dynamics, LLC (multiple places) and links the MIT license.
- No `.github/workflows` directory or files.
- No secrets, API keys, passwords, or personal data in any file (scanned for `api_key`, `secret`, `sk-`, `password`, `token` patterns — only prose mentions of "no secrets").
- All markdown converts to HTML without errors (headings, tables, lists, code blocks, blockquotes, links).

## Known gaps

- Site is static and single-folder (no search, no sitemap.xml, no RSS) — intentional, keeps it simple and printable.
- Build script implements a small Markdown subset (headings, bold/italic, code, links, lists incl. task lists, blockquotes, tables, fenced code, horizontal rules). Unusual markdown edge cases may not convert perfectly.
- No automated test suite; verification is manual (build run + structural grep checks).
- Policy templates must be reviewed by the user's organization's legal/compliance/HR/nursing leadership before adoption (stated in disclaimer).
- Not tested in a real browser; HTML/CSS is simple and standards-based.
