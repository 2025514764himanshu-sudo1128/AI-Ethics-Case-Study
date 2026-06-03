# Experiment 10: AI Ethics, Safety and Biases in Mechanical Systems

---

## Aim
To critically evaluate safety, ethical implications, and data biases in AI-driven mechanical systems such as autonomous vehicles and automated manufacturing systems.

---

## Concepts Covered
- Types of AI failures — Sensor bias, Algorithmic bias, HMI issues
- Real-world case study — Boeing 737 MAX MCAS failure
- Safety checklist for AI deployment
- Accountability framework
- Workforce adaptation strategies
- Ethical manifesto for AI engineers

---

## Software Required

| Software | Purpose | Download Link |
|---|---|---|
| Python 3.x | Programming language | https://www.python.org/downloads/ |
| VS Code | Code editor | https://code.visualstudio.com/ |
| Git | Version control | https://git-scm.com/ |

> Note: This experiment is a case study and does NOT require
> running any Python code. The main file is a Markdown (.md)
> document. You can read it directly on GitHub.

---

## How to View

**Option 1 — On GitHub:**
Simply open the repository on github.com and click `ai_ethics_notes.md`
GitHub renders Markdown beautifully with tables and formatting.

**Option 2 — In VS Code:**
```bash
git clone https://github.com/2025514764himanshu-sudo1128/AI-Ethics-Case-Study.git
cd AI-Ethics-Case-Study
code ai_ethics_notes.md
```
Then press `Ctrl + Shift + V` in VS Code to preview Markdown.

**Option 3 — Convert to PDF:**
```bash
pip install markdown weasyprint
python -c "
import markdown, pathlib
md = pathlib.Path('ai_ethics_notes.md').read_text()
html = markdown.markdown(md, extensions=['tables'])
pathlib.Path('ai_ethics.html').write_text(html)
print('Saved as ai_ethics.html — open in browser and print as PDF')
"
```

---

## Case Study Summary

### Boeing 737 MAX — MCAS Failure

| Factor | Observation |
|---|---|
| Sensor Bias | Single faulty AoA sensor — no redundancy |
| Algorithm Issue | Repeated nose-down commands without validation |
| HMI Issue | Pilots not trained on override procedure |

**Root cause:** Over-reliance on a single sensor without fail-safe mechanisms.

---

## Key Takeaways
- AI systems must be **safe, transparent and reliable**
- Bias in data can lead to **catastrophic failures**
- **Human override** must always exist in safety-critical systems
- Responsibility is **shared** across engineers, companies and regulators

---

## Author
**Himanshu Kumar** (2025514764)
Department of Electrical, Electronics and Communication Engineering
Sharda University, Greater Noida
