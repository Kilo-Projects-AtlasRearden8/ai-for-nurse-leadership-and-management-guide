# AI for Nurse Managers and Leaders: A Beginner Manual

Plain-English, step-by-step AI education for nurse managers, nurse leaders, and charge nurses. Covers staff education, policy drafts, meeting prep, and workload planning — with printable leadership worksheets you can use right away.

## Who this is for

You're a nurse manager or leader and you keep hearing about AI. Maybe your staff are asking about it. Maybe your organization is talking about it. You don't need to be a coder or a tech person to use AI well — you just need a safe, simple starting point.

This manual is written for nurse managers, nurse leaders, charge nurses, and anyone leading a nursing team. No technical background required.

**Education only.** This manual is not medical advice, not HR advice, and not legal advice. It will never tell you how to care for a patient or how to manage a person. See the disclaimer.

## What's inside

| Section | What you'll do |
|---------|----------------|
| Staff education | Run a 30-minute AI huddle with your team, set ground rules, answer common questions |
| Policy drafts | Draft a fill-in-the-blank AI use policy for your unit and adopt it step by step |
| Meeting prep | Use AI to draft agendas, talking points, anticipated questions, and follow-ups |
| Workload planning | Use AI as a thinking partner for shifts and assignments (you still make the calls) |
| Printable worksheets | One worksheet per section, plus a combined page you can print and fill in by hand |

Each section is plain English, step by step, and ends with a printable worksheet.

## Repository contents

- `docs/` — Markdown source of the beginner manual
- `site/` — the finished static HTML site (7 pages + stylesheet)
- `build.py` — builds `site/` from `docs/` (Python standard library only)
- `test_build.py` — verifies the build and site structure
- `LICENSE` — MIT License
- `README.md` — this file
- `STATUS.md` — what was built, how to run it, verification results, known gaps

## How to run the site

No install, no server, no account, no secrets. You just need Python 3.

```bash
python3 build.py
```

This writes HTML files into `site/`. Open `site/index.html` in any browser. To print, open any page and press Ctrl+P (or Command+P) — worksheets print cleanly, with navigation hidden.

## Credit

This manual was written by **Dylan Asdale**, a registered nurse turned AI author and founder of **Asdale Dynamics, LLC** (Indiana, formed October 2026). Asdale Dynamics publishes beginner-friendly AI education, books, and practical tools. His book *The Massive AI Manual* and hub site dylanasdale.github.io explain AI "like a friend would": plain English, step by step, never condescending.

© 2026 Asdale Dynamics, LLC.

## License

[MIT License](LICENSE) — Copyright (c) 2026 Asdale Dynamics, LLC.

## Disclaimer

This manual and website are provided for educational purposes only. They are not medical, nursing, HR, legal, or compliance advice, and not a staffing or scheduling system. Never enter patient-identifiable information into AI tools. Have your organization's qualified professionals review any policy or decision before use. See `docs/06-disclaimer.md` and `site/disclaimer.html`.
