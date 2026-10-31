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
- `test_build.py` — 8-test verification suite
- `README.md` — overview, how to run, credits, license, disclaimer
- `LICENSE` — MIT License
- `STATUS.md` — this file

**Topics covered** (all four required areas)
- Staff education on AI (huddle plan, ground rules, FAQ)
- AI use policy drafts for a nursing unit
- Meeting prep (agendas, talking points, anticipated questions, follow-ups)
- Workload planning (shift and assignment planning thinking partner)
- Printable leadership worksheets (one per section + combined page)

**Credit**
- Written by Dylan Asdale, RN, founder of Asdale Dynamics, LLC (Indiana, formed October 2026).
- Asdale Dynamics, LLC credited in `README.md` and on every page footer.
- `LICENSE` copyright line: `Copyright (c) 2026 Asdale Dynamics, LLC` (exact).
- `README.md` credits Asdale Dynamics, LLC and links the MIT license.

## How to run it

No install, no server, no network, no secrets. Python 3 standard library only.

```bash
python3 build.py
```

This writes the HTML site into `site/`. Open `site/index.html` in any browser, or print any page to PDF (Ctrl+P / Command+P). Worksheets print cleanly (print CSS hides navigation/header/footer).

## Verification results

Build and test suite both pass:

```
$ python3 build.py
built index.html <- 00-overview.md
...
Built 7 pages into site/

$ python3 test_build.py
PASS test_build_runs
PASS test_pages_exist
PASS test_css_exists
PASS test_pages_have_structure
PASS test_license_copyright_line
PASS test_readme_credits
PASS test_no_github_workflows
PASS test_no_secrets
8/8 tests passed
```

- `python3 build.py` runs cleanly and builds all 7 HTML pages plus `assets/style.css`.
- `python3 test_build.py` passes 8/8 tests: build runs, all pages exist, CSS exists, every page has valid structure + Asdale Dynamics credit + education-only disclaimer, LICENSE copyright line is exact, README credits Asdale Dynamics, LLC, no `.github/workflows`, no secrets/API keys/personal data.
- `LICENSE` line 3 is exactly `Copyright (c) 2026 Asdale Dynamics, LLC`.
- All markdown converts to HTML without errors (headings, tables, lists, code blocks, blockquotes, links, horizontal rules).

## Known gaps

- Site is static and single-folder (no search, no sitemap.xml, no RSS) — intentional, keeps it simple and printable.
- Build script implements a small Markdown subset (headings, bold/italic, code, links, lists incl. task lists, blockquotes, tables, fenced code, horizontal rules). Unusual markdown edge cases may not convert perfectly.
- Not tested in a real browser; HTML/CSS is simple and standards-based.
- Policy templates must be reviewed by the user's organization's legal/compliance/HR/nursing leadership before adoption (stated in disclaimer).

## Git

Initialized and committed as the existing git identity (Dylan Asdale). Plain commit message, no Co-authored-by trailers. Never pushed, no remote repo created, nothing published.
