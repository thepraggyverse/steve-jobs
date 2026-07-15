#!/usr/bin/env python3
"""Semantic checks that prevent renamed-template and contract drift."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
ERRORS: list[str] = []
REQUIRED_SECTIONS = (
    "Core Move",
    "Workflow",
    "Read References",
    "Source Grounding",
    "Output",
    "Guardrails",
    "Example Prompt",
)
OLD_GENERIC_TEXT = (
    "Locate or ask for the real artifact, flow, screen, code path, or product claim.",
    "Name the user, the job, and the intended feeling or behavior.",
    "State the current reality in plain facts.",
    "Identify the source, practice, decision, or life pattern under study.",
    "apply this Steve Jobs operating pattern to my task",
    "apply this Jony Ive design studio lens to my task",
)


def section(text: str, title: str, next_title: str | None = None) -> str:
    if next_title:
        pattern = rf"## {re.escape(title)}\n\n(.*?)(?=\n## {re.escape(next_title)}\n)"
    else:
        pattern = rf"## {re.escape(title)}\n\n(.*)"
    match = re.search(pattern, text, flags=re.S)
    return match.group(1).strip() if match else ""


def bullets(block: str) -> list[str]:
    return [line[2:].strip() for line in block.splitlines() if line.startswith("- ")]


skill_paths = sorted(SKILLS.glob("sj-*/SKILL.md"))
if len(skill_paths) != 91:
    ERRORS.append(f"expected 91 skills, found {len(skill_paths)}")

contracts: dict[tuple[str, str], list[str]] = {}
skill_data = {}
claim_ids = []
implicit = []

for path in skill_paths:
    name = path.parent.name
    text = path.read_text()
    for title in REQUIRED_SECTIONS:
        if f"## {title}\n" not in text:
            ERRORS.append(f"{name}: missing {title} section")
    for stale in OLD_GENERIC_TEXT:
        if stale in text:
            ERRORS.append(f"{name}: contains retired generic text: {stale}")

    workflow = section(text, "Workflow", "Read References")
    output = section(text, "Output", "Guardrails")
    guardrails = section(text, "Guardrails", "Example Prompt")
    workflow_steps = re.findall(r"^\d+\.\s+.+", workflow, flags=re.M)
    output_fields = bullets(output)
    guardrail_items = bullets(guardrails)
    if not 5 <= len(workflow_steps) <= 8:
        ERRORS.append(f"{name}: expected 5-8 workflow steps, found {len(workflow_steps)}")
    if not 4 <= len(output_fields) <= 9:
        ERRORS.append(f"{name}: expected 4-9 output fields, found {len(output_fields)}")
    if len(guardrail_items) < 3:
        ERRORS.append(f"{name}: expected at least 3 guardrails, found {len(guardrail_items)}")
    contracts.setdefault((workflow, output), []).append(name)

    claim_match = re.search(r"- Claim: `(SJ-[A-Z]+\d{2})`", text)
    source_match = re.search(r"- Sources: (.+)", text)
    if not claim_match:
        ERRORS.append(f"{name}: missing valid claim ID")
        claim = ""
    else:
        claim = claim_match.group(1)
        claim_ids.append(claim)
    source_ids = re.findall(r"`(S\d{2})`", source_match.group(1)) if source_match else []
    if not source_ids:
        ERRORS.append(f"{name}: missing source IDs")

    metadata_path = path.parent / "agents" / "openai.yaml"
    metadata = metadata_path.read_text() if metadata_path.exists() else ""
    short_match = re.search(r'^  short_description: "(.+)"$', metadata, flags=re.M)
    prompt_match = re.search(r'^  default_prompt: "(.+)"$', metadata, flags=re.M)
    policy_match = re.search(r"allow_implicit_invocation: (true|false)", metadata)
    example = section(text, "Example Prompt")
    if not short_match or not 25 <= len(short_match.group(1)) <= 64:
        ERRORS.append(f"{name}: short_description must be 25-64 characters")
    if not prompt_match or prompt_match.group(1) != example:
        ERRORS.append(f"{name}: default_prompt must equal Example Prompt")
    if policy_match and policy_match.group(1) == "true":
        implicit.append(name)

    skill_data[name] = {
        "claim": claim,
        "outputs": output_fields,
        "guardrails": guardrail_items,
        "example": example,
    }

for names in contracts.values():
    if len(names) > 1:
        ERRORS.append(f"duplicate workflow/output contract: {', '.join(names)}")

duplicates = [claim for claim, count in Counter(claim_ids).items() if count > 1]
if duplicates:
    ERRORS.append(f"duplicate claim IDs: {', '.join(sorted(duplicates))}")
if len(claim_ids) != 91:
    ERRORS.append(f"expected 91 claim IDs, found {len(claim_ids)}")
if implicit != ["sj-core-catalog"]:
    ERRORS.append(f"only sj-core-catalog may be implicit, found: {', '.join(implicit)}")

source_map = (ROOT / "references" / "sj-source-map.md").read_text()
defined_sources = set(re.findall(r"^\| `(S\d{2})` \|", source_map, flags=re.M))
if defined_sources != {f"S{i:02d}" for i in range(1, 16)}:
    ERRORS.append("source map must define exactly S01-S15")

evidence_map = (ROOT / "references" / "sj-evidence-map.md").read_text()
evidence_rows = re.findall(
    r"^\| `(SJ-[A-Z]+\d{2})` \| `\$(sj-[a-z0-9-]+)` \| (.+?) \| `(direct|synthesized|counterexample)` \|",
    evidence_map,
    flags=re.M,
)
if len(evidence_rows) != 91:
    ERRORS.append(f"evidence map must contain 91 rows, found {len(evidence_rows)}")
for claim, name, source_cell, _level in evidence_rows:
    if name not in skill_data:
        ERRORS.append(f"evidence map references unknown skill: {name}")
        continue
    if claim != skill_data[name]["claim"]:
        ERRORS.append(f"{name}: evidence map claim does not match SKILL.md")
    for source in re.findall(r"`(S\d{2})`", source_cell):
        if source not in defined_sources:
            ERRORS.append(f"{name}: evidence map references unknown source {source}")

behavior_path = ROOT / "tests" / "behavior-cases.json"
try:
    behavior = json.loads(behavior_path.read_text())
except Exception as exc:
    ERRORS.append(f"behavior dataset is invalid: {exc}")
    behavior = {"cases": []}
cases = behavior.get("cases", [])
if behavior.get("case_count") != 182 or len(cases) != 182:
    ERRORS.append("behavior dataset must contain exactly 182 cases")
case_counts = Counter(case.get("skill") for case in cases)
mode_pairs = {}
for case in cases:
    name = case.get("skill")
    if name not in skill_data:
        ERRORS.append(f"behavior case references unknown skill: {name}")
        continue
    mode_pairs.setdefault(name, set()).add(case.get("mode"))
    if case.get("claim_id") != skill_data[name]["claim"]:
        ERRORS.append(f"{case.get('id')}: claim ID drift")
    if case.get("required_output_fields") != skill_data[name]["outputs"]:
        ERRORS.append(f"{case.get('id')}: output contract drift")
    if case.get("forbidden_behaviors") != skill_data[name]["guardrails"]:
        ERRORS.append(f"{case.get('id')}: guardrail contract drift")
for name in skill_data:
    if case_counts[name] != 2 or mode_pairs.get(name) != {"positive", "boundary"}:
        ERRORS.append(f"{name}: needs one positive and one boundary case")

router_path = ROOT / "tests" / "router-cases.json"
try:
    router_cases = json.loads(router_path.read_text()).get("cases", [])
except Exception as exc:
    ERRORS.append(f"router dataset is invalid: {exc}")
    router_cases = []
if len(router_cases) < 16:
    ERRORS.append(f"router dataset needs at least 16 ambiguous cases, found {len(router_cases)}")
for case in router_cases:
    names = [case.get("expected_primary"), *case.get("expected_followups", [])]
    for name in names:
        if name not in skill_data:
            ERRORS.append(f"router case {case.get('id')} references unknown skill: {name}")

catalog_text = (ROOT / "references" / "sj-skill-catalog.md").read_text()
reference_text = (ROOT / "docs" / "SKILL_REFERENCE.md").read_text()
reference_rows = re.findall(
    r"^\| `\$(sj-[^`]+)` \| (.+?) \| `(.+?)` \|$",
    reference_text,
    flags=re.M,
)
if len(reference_rows) != 91:
    ERRORS.append(f"SKILL_REFERENCE must contain 91 rows, found {len(reference_rows)}")
for name, purpose, prompt in reference_rows:
    catalog_line = re.search(
        rf"^\d+\. `\${re.escape(name)}` \([^)]+\): (.+)$",
        catalog_text,
        flags=re.M,
    )
    if not catalog_line or purpose != catalog_line.group(1):
        ERRORS.append(f"{name}: SKILL_REFERENCE purpose drift")
    if name in skill_data and prompt != skill_data[name]["example"]:
        ERRORS.append(f"{name}: SKILL_REFERENCE example prompt drift")

if ERRORS:
    for error in ERRORS:
        print(f"ERROR: {error}")
    raise SystemExit(1)

print("Semantic skill quality passed")
print("skills: 91")
print("unique workflow/output contracts: 91")
print("source claims: 91")
print("behavior cases: 182")
print(f"router cases: {len(router_cases)}")
