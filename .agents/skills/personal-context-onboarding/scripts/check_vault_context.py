#!/usr/bin/env python3
"""Assess whether the vault still looks like starter boilerplate.

The script deliberately reports counts and area labels only. It reads a small
set of expected starter files, but it never prints note contents.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path.cwd()

BOILERPLATE_PATTERNS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in [
        r"^use this (note|folder)\b",
        r"^this folder holds\b",
        r"^start here:?$",
        r"^keep this folder private\b",
        r"^prompts:?$",
        r"^examples:?$",
        r"^keep entries factual:?$",
        r"^suggested (note )?(sections|project note sections)\b",
        r"^add one line per\b",
        r"^format:?$",
        r"^track personal projects\b",
        r"^use one folder\b",
        r"^what should an assistant know\b",
        r"^what context is safe\b",
        r"^what should never be assumed\b",
        r"^i prefer direct feedback over vague encouragement\.$",
        r"^i want plans to end in concrete next actions\.$",
        r"^i do not want private notes quoted unless i ask\.$",
        r"^newest first\b",
        r"^internal link:",
        r"^external link:",
    ]
]

LABEL_ONLY = re.compile(
    r"^[-*]?\s*(?:-\s*)?(?:\[\s?\]\s*)?"
    r"(goal|outcome|why it matters|success metric|next review date|why parked|"
    r"stakeholders|current state|risks|next actions?|links|status|blockers|"
    r"short summary|main insight|concern|what would reduce uncertainty|topic|"
    r"why i am learning it|current level|next practice step|resources|questions|"
    r"title|type|key ideas|quotes or moments|actions or follow-up):\s*$",
    re.IGNORECASE,
)

INDEX_LINK = re.compile(r"^[-*]\s*\[\[[^\]]+\]\]\s*$")

IGNORE_FILENAMES = {"README.md", "Index.md", "AGENTS.md"}


AREAS = [
    {
        "id": "profile",
        "label": "Profile, preferences, and boundaries",
        "paths": ["Me/Bio.md", "Me/Operating Principles.md", "Me/Concerns.md"],
        "directories": [],
        "threshold": 3,
    },
    {
        "id": "goals",
        "label": "Goals and desired outcomes",
        "paths": ["Me/Goals.md"],
        "directories": [],
        "threshold": 2,
    },
    {
        "id": "projects",
        "label": "Personal projects",
        "paths": ["Projects/Index.md"],
        "directories": ["Projects"],
        "threshold": 2,
    },
    {
        "id": "work",
        "label": "Work context",
        "paths": ["Work/Projects/README.md"],
        "directories": ["Work/Projects"],
        "threshold": 2,
    },
    {
        "id": "journal",
        "label": "Journal history",
        "paths": ["Journal/Index.md"],
        "directories": ["Journal/Daily", "Journal/Decisions", "Journal/Incidents"],
        "threshold": 1,
    },
    {
        "id": "learning",
        "label": "Learning interests",
        "paths": ["Learning/Index.md"],
        "directories": ["Learning"],
        "threshold": 2,
    },
    {
        "id": "media",
        "label": "Media taste and references",
        "paths": ["Media/Index.md"],
        "directories": ["Media"],
        "threshold": 2,
    },
]


def is_meaningful(line: str) -> bool:
    line = line.strip()
    plain_line = re.sub(r"^[-*]\s*(?:\[\s?\]\s*)?", "", line)
    if not line:
        return False
    if line.startswith("#"):
        return False
    if line in {"---", "```"}:
        return False
    if LABEL_ONLY.match(line) or LABEL_ONLY.match(plain_line):
        return False
    if INDEX_LINK.match(line):
        return False
    if re.match(r"^[-*]\s*$", line):
        return False
    return not any(
        pattern.search(line) or pattern.search(plain_line)
        for pattern in BOILERPLATE_PATTERNS
    )


def count_meaningful_lines(path: Path) -> int:
    if not path.exists() or not path.is_file():
        return 0

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()

    count = 0
    in_fence = False
    for raw in lines:
        line = raw.strip()
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if is_meaningful(line):
            count += 1
    return count


def count_custom_notes(directory: Path) -> int:
    if not directory.exists() or not directory.is_dir():
        return 0

    count = 0
    for path in directory.rglob("*.md"):
        if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        if path.name in IGNORE_FILENAMES:
            continue
        count += 1
    return count


def area_report(area: dict[str, object]) -> dict[str, object]:
    meaningful_lines = sum(
        count_meaningful_lines(ROOT / path) for path in area["paths"]  # type: ignore[index]
    )
    custom_notes = sum(
        count_custom_notes(ROOT / path) for path in area["directories"]  # type: ignore[index]
    )
    threshold = int(area["threshold"])
    filled = meaningful_lines >= threshold or custom_notes > 0
    return {
        "id": area["id"],
        "label": area["label"],
        "filled": filled,
        "meaningful_lines": meaningful_lines,
        "custom_notes": custom_notes,
        "threshold": threshold,
    }


def main() -> None:
    areas = [area_report(area) for area in AREAS]
    filled_count = sum(1 for area in areas if area["filled"])
    meaningful_lines = sum(int(area["meaningful_lines"]) for area in areas)
    custom_notes = sum(int(area["custom_notes"]) for area in areas)

    sparse = filled_count < 3 or (meaningful_lines < 10 and custom_notes < 2)
    next_best_areas = [area["label"] for area in areas if not area["filled"]][:3]

    print(
        json.dumps(
            {
                "status": "sparse" if sparse else "ready",
                "filled_area_count": filled_count,
                "area_count": len(areas),
                "meaningful_line_count": meaningful_lines,
                "custom_note_count": custom_notes,
                "next_best_areas": next_best_areas,
                "areas": areas,
                "privacy": "Counts only; no note contents are printed.",
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
