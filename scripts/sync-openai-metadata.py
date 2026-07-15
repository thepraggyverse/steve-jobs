#!/usr/bin/env python3
"""Synchronize Codex UI metadata with each skill's executable contract."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

SHORT_OVERRIDES = {
    "sj-core-compound-learning": "Capture approved reusable lessons after each SJ skill run",
    "sj-core-learning-refresh": "Audit saved SJ lessons for drift and duplication",
    "sj-ive-better-not-different": "Test whether novelty makes the product genuinely better",
    "sj-ive-care-is-felt": "Audit whether users can sense care in the artifact",
    "sj-ive-design-story": "Find the product design story before debating features",
    "sj-ive-first-touch-moment": "Audit the first user touchpoint as a trust moment",
    "sj-ive-fragile-idea-protection": "Protect promising rough ideas before premature judgment",
    "sj-ive-future-without-betrayal": "Modernize without losing the soul users trust",
    "sj-ive-humanize-technology": "Make technology approachable and emotionally legible",
    "sj-ive-manufacturing-as-design": "Treat production constraints as part of design",
    "sj-ive-material-honesty": "Treat material and sensory qualities as part of the idea",
    "sj-ive-prototype-volume": "Replace debate with many concrete prototypes",
    "sj-product-simplify-to-one": "Reduce competing priorities to one clear product path",
}


def section_line(text: str, title: str) -> str:
    match = re.search(rf"## {re.escape(title)}\n\n(.+?)\n", text)
    if not match:
        raise SystemExit(f"Missing {title} section")
    return match.group(1).strip()


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def short_description(name: str, core_move: str) -> str:
    value = SHORT_OVERRIDES.get(name, core_move.rstrip("."))
    if len(value) > 64:
        words = value.split()
        kept = []
        for word in words:
            candidate = " ".join([*kept, word])
            if len(candidate) > 64:
                break
            kept.append(word)
        value = " ".join(kept).rstrip(" ,;:")
    if len(value) < 25:
        value = f"{value} with a concrete review"
    if not 25 <= len(value) <= 64:
        raise SystemExit(f"Cannot create valid short description: {value!r}")
    return value


def display_name(name: str) -> str:
    words = name.removeprefix("sj-").split("-")
    return " ".join(word.upper() if word == "sj" else word.title() for word in words)


def expected_metadata(skill_dir: Path) -> str:
    text = (skill_dir / "SKILL.md").read_text()
    core_move = section_line(text, "Core Move")
    prompt = section_line(text, "Example Prompt")
    implicit = "true" if skill_dir.name == "sj-core-catalog" else "false"
    return (
        "interface:\n"
        f"  display_name: {yaml_quote(display_name(skill_dir.name))}\n"
        f"  short_description: {yaml_quote(short_description(skill_dir.name, core_move))}\n"
        f"  default_prompt: {yaml_quote(prompt)}\n\n"
        "policy:\n"
        f"  allow_implicit_invocation: {implicit}\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    failures = []
    skill_dirs = sorted(path.parent for path in SKILLS.glob("sj-*/SKILL.md"))

    for skill_dir in skill_dirs:
        path = skill_dir / "agents" / "openai.yaml"
        expected = expected_metadata(skill_dir)
        if args.check:
            if not path.exists() or path.read_text() != expected:
                failures.append(f"{skill_dir.name}: agents/openai.yaml is stale")
        else:
            path.parent.mkdir(exist_ok=True)
            path.write_text(expected)

    if failures:
        print("OpenAI metadata check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    action = "verified" if args.check else "synchronized"
    print(f"OpenAI metadata {action}: {len(skill_dirs)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
