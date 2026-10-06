#!/usr/bin/env python3
"""Generate docs/quiz/index.html — 'Hype Check' daily quiz from the research archive.

Parses every research markdown file, extracts one hype-claim per video (claims,
receipts, verdict), and injects them into scripts/quiz_template.html.
Rerun after research updates: python scripts/build_quiz.py
"""
import glob
import json
import os
import random
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
RESEARCH = os.path.join(DOCS, "research")
TEMPLATE = os.path.join(ROOT, "scripts", "quiz_template.html")
OUT = os.path.join(ROOT, "docs", "quiz", "index.html")

BAD_START = re.compile(
    r"^(\[|\(?\s*(create|build|use|focus|test|try|make|add|run|start|set up|check|"
    r"track|post|pick|avoid|choose|action|step|week|day)\b)",
    re.I,
)


def md2t(s):
    s = re.sub(r"`([^`]+)`", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", s)
    s = re.sub(r"\*+", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def clip(s, n):
    s = md2t(s)
    if len(s) <= n:
        return s
    return s[: n - 1].rsplit(" ", 1)[0] + "\u2026"


def classify(vtxt):
    if re.search(r"\bSkip\b", vtxt, re.I):
        return "Skip"
    if re.search(r"\bMixed\b", vtxt, re.I):
        return "Mixed"
    if re.search(r"Worth\s*(Trying|a try|it)", vtxt, re.I):
        return "Worth Trying"
    return None


def research_url(src):
    """Link back to the published research page for a question's source file."""
    return "../research/" + src + ".html"


def extract_questions():
    files = sorted(glob.glob(os.path.join(RESEARCH, "*.md")))
    qs = []
    for fp in files:
        src = os.path.basename(fp)[: -len(".md")]
        text = open(fp, encoding="utf-8", errors="replace").read()
        for part in re.split(r"^### ", text, flags=re.M)[1:]:
            nl = part.find("\n")
            title, body = part[:nl], part[nl:]
            title = re.sub(r"\s*\{#[^}]*\}\s*$", "", title).strip()

            vm = re.search(r"\*\*Verdict[^*]*\*\*[^\S\n]*([^\n]*)\n?(.{0,300})", body)
            if not vm:
                continue
            vtxt = md2t(vm.group(1) + " " + vm.group(2))
            answer = classify(vtxt)
            if not answer:
                continue
            score = re.search(r"(\d+(?:\.\d+)?)/10", vtxt)

            rm = re.search(
                r"\*\*Receipts?[^*]*\*\*:?\s*(.{0,400}?)(?=\n\*\*|\n#{2,4} |\Z)",
                body,
                re.S,
            )
            receipts = clip(rm.group(1), 300) if rm else ""

            bullets = [md2t(b) for b in re.findall(r"^[-*] (.+)$", body, flags=re.M)]
            money = [
                b for b in bullets
                if re.search(r"[$\u20ac\u00a3]\s?\d", b) and not BAD_START.match(b)
                and 55 < len(b) < 240
            ]
            nummy = [
                b for b in bullets
                if re.search(r"\b\d[\d,.]*\s?(K|M|%|k)\b", b) and not BAD_START.match(b)
                and 55 < len(b) < 230
            ]
            if money:
                claim = money[0]
            elif nummy:
                claim = nummy[0]
            elif len(receipts) > 70:
                claim = receipts
                receipts = ""  # shown as the claim already; avoid duplicating
            else:
                continue

            rationale = re.sub(
                r"^\W*(Skip|Mixed|Worth Trying)\b[.:\-\u2014! ]*", "", vtxt
            ).strip()[:230]

            qs.append({
                "video": clip(re.sub(r"^Video \d+:\s*", "", title), 95),
                "show": clip(claim, 245),
                "receipts": receipts,
                "answer": answer,
                "score": score.group(1) if score else "",
                "rationale": rationale,
                "src": src,
                "link": research_url(src),
            })
    return qs


def dedupe(qs):
    seen, out = set(), []
    for q in qs:
        key = re.sub(r"^video \d+:\s*", "", q["video"].lower())[:55]
        if key in seen:
            continue
        seen.add(key)
        out.append(q)
    return out


def build():
    qs = dedupe(extract_questions())
    random.seed(7)
    random.shuffle(qs)

    template = open(TEMPLATE, encoding="utf-8").read()
    build_stamp = "question bank: %d claims from %d research reports" % (
        len(qs), len(glob.glob(os.path.join(RESEARCH, "*.md"))),
    )
    html = template.replace(
        "/*__QUESTIONS__*/[]/*__END__*/", json.dumps(qs, ensure_ascii=False)
    )
    html = html.replace("__BUILD__", build_stamp)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)

    from collections import Counter
    print("questions: %d %s" % (len(qs), dict(Counter(q["answer"] for q in qs))))
    print("wrote %s (%d KB)" % (os.path.relpath(OUT, ROOT), os.path.getsize(OUT) // 1024))
    print(build_stamp)


if __name__ == "__main__":
    build()
