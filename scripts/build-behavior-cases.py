#!/usr/bin/env python3
"""Build the two-case-per-skill behavioral contract dataset."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
OUTPUT = ROOT / "tests" / "behavior-cases.json"

FIXTURES = {
    "core": "A team must choose how to improve a cluttered AI notes app before a launch in two weeks. It has weak onboarding, an unclear demo, and no durable learning log.",
    "product": "A mobile AI notes app has 14 first-run choices, a five-step setup, 42 percent onboarding completion, and one week for a focused product improvement.",
    "ive": "An AI settings screen is dense, cold, jargon-heavy, and visually finished but emotionally difficult to approach. A working prototype is available.",
    "story": "A research assistant launch claims faster synthesis, cites a benchmark, and has a working demo, but its announcement currently lists nine unrelated features.",
    "people": "A 12-person product team has unclear decision ownership, uneven craft standards, guarded feedback, and a critical release six weeks away.",
    "strategy": "A software company has nine months of runway, four scattered product bets, indirect customer feedback, and one promising but unproven core workflow.",
    "learning": "A builder has complete notes from a book, a difficult recent decision, limited weekly practice time, and wants one reusable lesson without hero worship.",
    "anti": "A funded startup reports rapid channel growth while inventory, incentives, personal rivalry, spending, and end-customer demand remain insufficiently reconciled.",
}


def section(text: str, title: str, next_title: str | None = None) -> str:
    if next_title:
        pattern = rf"## {re.escape(title)}\n\n(.*?)(?=\n## {re.escape(next_title)}\n)"
    else:
        pattern = rf"## {re.escape(title)}\n\n(.*)"
    match = re.search(pattern, text, flags=re.S)
    if not match:
        raise SystemExit(f"Missing section {title}")
    return match.group(1).strip()


def bullet_lines(block: str) -> list[str]:
    return [line[2:].strip() for line in block.splitlines() if line.startswith("- ")]


def build() -> dict:
    cases = []
    for path in sorted(SKILLS.glob("sj-*/SKILL.md")):
        name = path.parent.name
        family = name.split("-", 2)[1]
        text = path.read_text()
        example = section(text, "Example Prompt")
        outputs = bullet_lines(section(text, "Output", "Guardrails"))
        guardrails = bullet_lines(section(text, "Guardrails", "Example Prompt"))
        claim_match = re.search(r"- Claim: `([^`]+)`", text)
        if not claim_match:
            raise SystemExit(f"Missing claim ID in {name}")

        cases.append(
            {
                "id": f"{name}:positive",
                "skill": name,
                "mode": "positive",
                "prompt": f"{example} Context: {FIXTURES[family]}",
                "claim_id": claim_match.group(1),
                "required_output_fields": outputs,
                "forbidden_behaviors": guardrails,
            }
        )
        cases.append(
            {
                "id": f"{name}:boundary",
                "skill": name,
                "mode": "boundary",
                "prompt": (
                    f"Use ${name}. The requested artifact and decision evidence are missing. "
                    "Do not invent facts, quotations, or a Steve Jobs persona. State the missing inputs, "
                    "apply only what is supportable, and preserve every declared guardrail."
                ),
                "claim_id": claim_match.group(1),
                "required_output_fields": outputs,
                "forbidden_behaviors": guardrails,
            }
        )

    return {
        "schema_version": 1,
        "description": "Two behavioral contract cases for every executable sj-* skill.",
        "case_count": len(cases),
        "cases": cases,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = json.dumps(build(), indent=2, ensure_ascii=True) + "\n"

    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text() != expected:
            print("Behavior dataset is stale. Run scripts/build-behavior-cases.py.")
            return 1
        data = json.loads(expected)
        print(f"Behavior dataset verified: {data['case_count']} cases")
        return 0

    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(expected)
    print(f"Behavior dataset built: {len(json.loads(expected)['cases'])} cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
