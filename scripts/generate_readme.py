#!/usr/bin/env python3
"""Generate a compact paper index from papers.yaml.

This script intentionally keeps generation simple. The main README remains
hand-curated, while this script can be used to inspect or regenerate sections
once the metadata becomes the source of truth.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
PAPERS_FILE = ROOT / "papers.yaml"
CATEGORY_ORDER = [
    "Survey",
    "Benchmark",
    "Agent System",
    "Memory",
    "Reasoning & Planning",
    "Active",
    "Navigation",
    "EQA",
    "Manipulation",
    "Related Lists",
    # Legacy metadata categories kept so older papers.yaml entries still render.
    "Surveys and Position Papers",
    "Benchmarks and Evaluation",
    "Embodied Memory",
    "Embodied Reasoning and Planning",
    "Embodied Exploration",
    "Embodied Navigation Agents",
    "Embodied Question Answering",
    "Manipulation Agents",
]


def load_papers() -> list[dict]:
    try:
        import yaml  # type: ignore
    except ImportError:
        print("PyYAML is required. Install it with: python -m pip install pyyaml", file=sys.stderr)
        raise SystemExit(1)

    with PAPERS_FILE.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or []

    if not isinstance(data, list):
        raise SystemExit("papers.yaml must contain a list of paper entries.")

    return data


def format_links(links: dict) -> str:
    parts = []
    for label in ("paper", "project", "code"):
        url = (links or {}).get(label) or ""
        if url:
            parts.append(f"[[{label}]({url})]")
    return " ".join(parts)


def main() -> None:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for paper in load_papers():
        grouped[paper.get("category") or "Uncategorized"].append(paper)

    ordered_categories = [category for category in CATEGORY_ORDER if category in grouped]
    ordered_categories.extend(sorted(set(grouped) - set(ordered_categories)))

    for category in ordered_categories:
        print(f"## {category}\n")
        # Python's sort is stable, so entries with the same year keep the
        # hand-curated order from papers.yaml.
        papers = sorted(grouped[category], key=lambda item: -(item.get("year") or 0))
        for paper in papers:
            links = format_links(paper.get("links", {}))
            year = paper.get("year") or "????"
            suffix = f" {links}" if links else ""
            print(f"* [{year}] {paper['title']}{suffix}")
        print()


if __name__ == "__main__":
    main()
