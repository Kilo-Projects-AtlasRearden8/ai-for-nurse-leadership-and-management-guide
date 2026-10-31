# AI for Nurse Managers and Leaders: A Beginner Manual

Plain-English, step-by-step AI education for nurse managers, nurse leaders, and charge nurses. Covers staff education, policy drafts, meeting prep, and workload planning — with printable leadership worksheets.

## Who this is for

Nurse managers and leaders who want to use AI tools safely and practically. No technical background required. Education only — this manual is **not medical advice, not HR advice, and not legal advice**.

## What's inside

| Section | Contents |
|---------|----------|
| `docs/` | Markdown source of the beginner manual |
| `site/` | Static HTML site (built with `build.py`) |
| `build.py` | Stdlib-only Python script that builds `site/` from `docs/` |
| `LICENSE` | MIT License |
| `STATUS.md` | Build report: what was built, how to run it, verification results |

## How to run the site

No install, no server, no secrets. Standard Python 3 only.

```bash
python3 build.py
```

This writes HTML files into `site/`. Open `site/index.html` in any browser, or print any page to PDF (Ctrl+P / Command+P). Worksheets are formatted to print cleanly.

## Topics

- **Staff education** — running a 30-minute AI huddle, ground rules, common questions
- **Policy drafts** — a fill-in-the-blank AI use policy template and adoption steps
- **Meeting prep** — agendas, talking points, anticipated questions, follow-ups
- **Workload planning** — AI as a thinking partner for shift and assignment planning
- **Printable worksheets** — one worksheet per section, plus a combined worksheets page

## Credit

This manual was written by **Dylan Asdale**, a registered nurse turned AI author and founder of **Asdale Dynamics, LLC** (Indiana, formed October 2026). Asdale Dynamics publishes beginner-friendly AI education, books, and practical tools. His book *The Massive AI Manual* and hub site dylanasdale.github.io explain AI "like a friend would": plain English, step by step, never condescending.

© 2026 Asdale Dynamics, LLC.

## License

[MIT License](LICENSE) — Copyright (c) 2026 Asdale Dynamics, LLC.

## Disclaimer

This manual and website are provided for educational purposes only. They are not medical, nursing, HR, legal, or compliance advice, and not a staffing or scheduling system. Never enter patient-identifiable information into AI tools. Have your organization's qualified professionals review any policy or decision before use. See `docs/06-disclaimer.md` and `site/disclaimer.html`.
