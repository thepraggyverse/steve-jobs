#!/usr/bin/env python3
"""Generate and verify source-to-claim-to-skill provenance."""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REFERENCES = ROOT / "references"

PREFIXES = {
    "core": "C",
    "product": "P",
    "ive": "I",
    "story": "ST",
    "people": "PE",
    "strategy": "S",
    "learning": "L",
    "anti": "A",
}

DEFAULT_SOURCES = {
    "core": "S02, S07, S08",
    "product": "S02, S03, S07, S09",
    "ive": "S10, S11, S13, S14, S15",
    "story": "S06, S07",
    "people": "S03, S04, S07",
    "strategy": "S04, S05, S08",
    "learning": "S02, S07, S08",
    "anti": "S04, S05, S08",
}

SOURCE_OVERRIDES = {
    "sj-core-catalog": "S02, S03, S04, S06, S07, S08, S09, S10, S13, S14",
    "sj-core-compound-learning": "S02, S07, S08",
    "sj-core-learning-refresh": "S02, S07, S08",
    "sj-product-apple-experience-audit": "S02, S03, S07",
    "sj-product-back-of-cabinet-quality": "S03, S04, S07",
    "sj-product-beautiful-object-standard": "S02, S03, S10, S15",
    "sj-product-bicycle-for-the-mind": "S01, S02, S07",
    "sj-product-concrete-artifact-review": "S03, S07, S14",
    "sj-product-creative-selection": "S03, S10, S14",
    "sj-product-customer-backwards": "S01, S02, S07",
    "sj-product-design-is-how-it-works": "S02, S03, S07",
    "sj-product-founder-workbench": "S03, S04, S08",
    "sj-product-hack-away-unessential": "S02, S07, S09",
    "sj-product-liberal-arts-technology": "S01, S02, S07",
    "sj-product-make-something-wonderful": "S02, S07, S08",
    "sj-product-no-second-rate-products": "S03, S04, S07",
    "sj-product-pixel-polish": "S03, S10, S15",
    "sj-product-raw-work-no-filters": "S03, S04, S07",
    "sj-product-reputation-credits": "S04, S05, S07",
    "sj-product-simple-stick": "S02, S07, S09",
    "sj-product-simplify-to-one": "S02, S07, S09",
    "sj-product-skepticism-hierarchy": "S01, S03, S08",
    "sj-product-speaks-for-itself": "S02, S03, S09",
    "sj-product-speed-as-feature": "S03, S07, S09",
    "sj-product-taste-review": "S03, S04, S11",
    "sj-product-telegraph-to-telephone": "S01, S02, S09",
    "sj-ive-design-story": "S10, S13, S15",
    "sj-ive-humanize-technology": "S10, S11, S13",
    "sj-ive-first-touch-moment": "S10, S12, S15",
    "sj-ive-prototype-volume": "S10, S14, S15",
    "sj-ive-material-honesty": "S10, S12, S15",
    "sj-ive-manufacturing-as-design": "S10, S12, S15",
    "sj-ive-care-is-felt": "S10, S11, S13",
    "sj-ive-better-not-different": "S11, S12, S13",
    "sj-ive-fragile-idea-protection": "S10, S13, S14",
    "sj-ive-future-without-betrayal": "S12, S13, S15",
    "sj-story-number-context": "S06, S07",
    "sj-story-historical-analogy": "S06, S08",
    "sj-story-demo-rehearsal-loop": "S06, S07",
    "sj-story-values-marketing": "S02, S06, S07",
    "sj-story-missionary-pr": "S04, S06, S07",
    "sj-story-old-story-new-tool": "S01, S06, S07",
    "sj-people-andy-grove-correction": "S04, S05, S08",
    "sj-people-bob-iger-trust": "S04, S05",
    "sj-people-ed-catmull-patience": "S04, S05, S08",
    "sj-people-permanent-ensemble": "S04, S05, S10",
    "sj-strategy-ambush-distribution": "S04, S06, S08",
    "sj-strategy-build-for-yourself": "S02, S05, S08",
    "sj-strategy-direct-channel": "S04, S07, S08",
    "sj-strategy-focus-matrix": "S04, S05, S09",
    "sj-strategy-pivot-to-core": "S04, S05, S08",
    "sj-strategy-reality-is-malleable": "S02, S05, S07",
    "sj-strategy-synthesizer-strategy": "S01, S04, S07",
    "sj-strategy-web-as-community": "S01, S05, S07",
    "sj-learning-balanced-builder-audit": "S02, S04, S07",
    "sj-learning-biographies-as-mentors": "S04, S05, S08",
    "sj-learning-mortality-lens": "S02, S07",
    "sj-learning-progressive-summarization": "S02, S07, S08",
    "sj-anti-channel-stuffing-check": "S04, S05",
    "sj-anti-revenge-motive-check": "S04, S05, S08",
    "sj-anti-too-much-money-check": "S04, S05, S08",
}


def catalog_order() -> list[str]:
    text = (REFERENCES / "sj-skill-catalog.md").read_text()
    names = re.findall(r"\$([a-z0-9-]+)`", text)
    if len(names) != 91 or len(set(names)) != 91:
        raise SystemExit("Catalog must contain exactly 91 unique skill names")
    return names


def family_for(name: str) -> str:
    family = name.split("-", 2)[1]
    if family not in PREFIXES:
        raise SystemExit(f"Unknown family for {name}")
    return family


def core_move(name: str) -> str:
    text = (SKILLS / name / "SKILL.md").read_text()
    match = re.search(r"## Core Move\n\n(.+?)\n", text)
    if not match:
        raise SystemExit(f"Missing Core Move in {name}")
    return match.group(1).strip()


def records() -> list[tuple[str, str, str, str, str]]:
    counts: dict[str, int] = defaultdict(int)
    rows = []
    for name in catalog_order():
        family = family_for(name)
        counts[family] += 1
        claim_id = f"SJ-{PREFIXES[family]}{counts[family]:02d}"
        sources = SOURCE_OVERRIDES.get(name, DEFAULT_SOURCES[family])
        level = "counterexample" if family == "anti" else "synthesized"
        rows.append((claim_id, name, family, sources, level))
    return rows


def evidence_map(rows: list[tuple[str, str, str, str, str]]) -> str:
    lines = [
        "# SJ Evidence Map",
        "",
        "This index connects each executable skill to a stable operating claim and the bounded sources used to synthesize it.",
        "The mapping is provenance at the idea level, not a substitute for checking the original source when historical precision matters.",
        "",
        "| Claim | Skill | Sources | Level | Operating claim |",
        "|---|---|---|---|---|",
    ]
    for claim_id, name, _family, sources, level in rows:
        source_cells = ", ".join(f"`{item.strip()}`" for item in sources.split(","))
        lines.append(
            f"| `{claim_id}` | `${name}` | {source_cells} | `{level}` | {core_move(name)} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Claim IDs are stable handles for documentation, tests, and durable learning notes.",
            "- Source IDs resolve through `sj-source-map.md`.",
            "- A synthesized claim may combine several episodes and should not be presented as a verbatim statement by Steve Jobs or Jony Ive.",
            "- Counterexample claims deliberately convert failure patterns into safeguards.",
            "- The public repository contains no source transcripts or book text.",
            "",
        ]
    )
    return "\n".join(lines)


def grounding_block(claim_id: str, sources: str, level: str) -> str:
    source_list = ", ".join(f"`{item.strip()}`" for item in sources.split(","))
    return (
        "## Source Grounding\n\n"
        f"- Claim: `{claim_id}`\n"
        f"- Sources: {source_list}\n"
        f"- Evidence level: `{level}`\n"
        "- Resolve IDs in `references/sj-source-map.md` and the claim row in "
        "`references/sj-evidence-map.md`.\n\n"
    )


def local_source_map(sources: str) -> str:
    source_ids = {item.strip() for item in sources.split(",")}
    root_text = (REFERENCES / "sj-source-map.md").read_text()
    rows = [
        line
        for line in root_text.splitlines()
        if any(line.startswith(f"| `{source_id}` |") for source_id in source_ids)
    ]
    return "\n".join(
        [
            "# SJ Source Map",
            "",
            "Portable source subset for this skill.",
            "Source IDs identify bounded provenance without redistributing the underlying books or transcripts.",
            "",
            "| ID | Source | Format | Primary contribution |",
            "|---|---|---|---|",
            *rows,
            "",
            "Evidence levels: `direct` is explicit, `synthesized` combines material, and `counterexample` grounds a warning.",
            "Use concise paraphrase and inspect the original source when historical precision matters.",
            "",
        ]
    )


def local_evidence_map(claim_id: str, name: str, sources: str, level: str) -> str:
    source_cells = ", ".join(f"`{item.strip()}`" for item in sources.split(","))
    return "\n".join(
        [
            "# SJ Evidence Map",
            "",
            "Portable evidence row for this skill.",
            "",
            "| Claim | Skill | Sources | Level | Operating claim |",
            "|---|---|---|---|---|",
            f"| `{claim_id}` | `${name}` | {source_cells} | `{level}` | {core_move(name)} |",
            "",
            "This is idea-level provenance, not a verbatim quotation or a substitute for checking the original source.",
            "",
        ]
    )


def expected_skill_text(name: str, claim_id: str, sources: str, level: str) -> str:
    path = SKILLS / name / "SKILL.md"
    text = path.read_text()
    text = re.sub(r"## Source Grounding\n.*?(?=## Output\n)", "", text, flags=re.S)
    marker = "## Output\n"
    if marker not in text:
        raise SystemExit(f"Missing Output section in {name}")
    return text.replace(marker, grounding_block(claim_id, sources, level) + marker, 1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    rows = records()
    generated_map = evidence_map(rows)
    evidence_path = REFERENCES / "sj-evidence-map.md"
    failures = []

    if args.check:
        if not evidence_path.exists() or evidence_path.read_text() != generated_map:
            failures.append("references/sj-evidence-map.md is stale")
    else:
        evidence_path.write_text(generated_map)

    for claim_id, name, _family, sources, level in rows:
        skill_path = SKILLS / name / "SKILL.md"
        expected = expected_skill_text(name, claim_id, sources, level)
        if args.check:
            if skill_path.read_text() != expected:
                failures.append(f"{name}: Source Grounding is stale")
        else:
            skill_path.write_text(expected)

        refs = SKILLS / name / "references"
        if not args.check:
            refs.mkdir(exist_ok=True)
        local_files = {
            "sj-source-map.md": local_source_map(sources),
            "sj-evidence-map.md": local_evidence_map(claim_id, name, sources, level),
        }
        for filename, expected_local in local_files.items():
            local_path = refs / filename
            if args.check:
                if not local_path.exists() or local_path.read_text() != expected_local:
                    failures.append(f"{name}: {filename} is stale")
            else:
                local_path.write_text(expected_local)

    if failures:
        print("Source grounding check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    action = "verified" if args.check else "synchronized"
    print(f"Source grounding {action}: {len(rows)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
