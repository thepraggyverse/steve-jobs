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

POSITIVE_CONTEXTS = {
    "sj-core-catalog": "A team has a cluttered AI notes app, weak onboarding, an unclear launch demo, and no durable learning loop. Choose the smallest useful sequence.",
    "sj-core-compound-learning": "A completed onboarding review showed that one clear first action raised test completion from 42 to 61 percent. The user has not yet approved saving anything.",
    "sj-core-learning-refresh": "The project has three saved SJ lessons: two repeat the same simplification advice, one cites a superseded flow, and one has low confidence.",
    "sj-product-make-something-wonderful": "A reliable medication reminder works but feels generic; users miss doses when traveling and say the app feels scolding.",
    "sj-product-customer-backwards": "Engineers propose an embeddings dashboard, while users only want to find the note that answered a prior client question in under ten seconds.",
    "sj-product-bicycle-for-the-mind": "An AI spreadsheet assistant currently advertises model size and tool calls; its real benefit is helping shop owners forecast cash without formulas.",
    "sj-product-liberal-arts-technology": "A technically strong family-history app organizes records well but has no sense of memory, ritual, voice, or emotional continuity.",
    "sj-product-speaks-for-itself": "New users need a seven-step tooltip tour to create their first project, and 38 percent cannot repeat the task after the tour disappears.",
    "sj-product-design-is-how-it-works": "A polished analytics dashboard has beautiful charts, but filtering resets selections and comparison requires opening three separate screens.",
    "sj-product-simplify-to-one": "An MVP serves students, recruiters, and researchers with six primary actions; the strongest repeated need is turning one source set into a cited brief.",
    "sj-product-simple-stick": "A two-page product memo circles among collaboration, intelligence, speed, and trust without naming the user or decision.",
    "sj-product-hack-away-unessential": "A roadmap has 28 items; only search reliability, citation accuracy, and export are required for the paid pilot in six weeks.",
    "sj-product-speed-as-feature": "A code search tool returns accurate results in 4.8 seconds; users abandon repeated queries after the third wait, while cached results arrive in 300 milliseconds.",
    "sj-product-apple-experience-audit": "Audit the path from pricing page through signup, email verification, import, first result, billing receipt, and cancellation for a research tool.",
    "sj-product-back-of-cabinet-quality": "A finance app displays correct totals, but exported CSV columns change order, audit logs omit timezone, and recovery scripts are untested.",
    "sj-product-taste-review": "Two music-player prototypes meet the same metrics: one exposes every control, while the other reveals queue editing only when a song is moved.",
    "sj-product-pixel-polish": "A checkout screen is available at mobile and desktop sizes with uneven alignment, clipped translated labels, weak focus states, and a jumping total row.",
    "sj-product-no-second-rate-products": "A team plans to ship a calendar integration with duplicate events, unclear conflict handling, and no offline recovery because the launch date is fixed.",
    "sj-product-beautiful-object-standard": "Review a desk timer prototype whose plastic shell flexes, button travel feels inconsistent, display blooms at night, and internal layout is otherwise repairable.",
    "sj-product-telegraph-to-telephone": "A database backup tool asks ordinary shop owners to choose regions, retention classes, snapshots, encryption keys, and restore topology before protecting data.",
    "sj-product-founder-workbench": "A founder debates whether voice capture is central but has not recorded, corrected, searched, and shared ten real voice notes end to end.",
    "sj-product-reputation-credits": "A subscription flow promises a free trial, requests a card late, sends no reminder, makes cancellation hard to find, and responds quickly to support.",
    "sj-product-skepticism-hierarchy": "Feedback includes one accessibility blocker from a screen-reader user, ten vague dislike comments, one security report with a reproduction, and a loud executive preference.",
    "sj-product-raw-work-no-filters": "Executives review weekly slide summaries while users encounter a broken import; support tickets, session recordings, and the failing build are available.",
    "sj-product-creative-selection": "Three working onboarding prototypes differ in account timing, sample data, and first action; five representative users can test them tomorrow.",
    "sj-product-concrete-artifact-review": "The team is arguing about a new editor from a concept memo; a clickable prototype and two representative documents are ready for direct review.",
    "sj-ive-design-story": "A home energy display can show consumption, cost, and carbon impact; the intended story is helping a family make one calm daily choice together.",
    "sj-ive-humanize-technology": "An AI settings screen is dense, cold, jargon-heavy, and technically complete; a working prototype exposes temperature, context window, tools, and sampling controls.",
    "sj-ive-first-touch-moment": "A sleep ring arrives in a plain shipping pouch, requires charging before setup, flashes an unexplained red light, and asks for six permissions on first launch.",
    "sj-ive-prototype-volume": "A team is split between bottom navigation, a command palette, and a canvas for a tablet editor; only one static mock of each exists.",
    "sj-ive-material-honesty": "A premium speaker uses a metal-look plastic grille, glossy touch surface, hollow tap sound, visible seams, and a genuinely solid recycled-aluminum frame.",
    "sj-ive-manufacturing-as-design": "A seamless lamp concept requires a hidden hinge, replaceable battery, waterproof seal, repair access, and a supplier limited to two aluminum draws.",
    "sj-ive-care-is-felt": "A journaling app saves reliably but opens with a spinner, uses abrupt keyboard motion, loses scroll position, and sends thoughtful recovery copy after a sync error.",
    "sj-ive-better-not-different": "A redesigned camera replaces the familiar shutter with a squeeze gesture; it looks novel but is slower with gloves and has no proven accessibility gain.",
    "sj-ive-fragile-idea-protection": "An early ambient calendar prototype has delighted three testers, but metrics, security, battery use, and implementation are too rough for a launch decision.",
    "sj-ive-future-without-betrayal": "Modernize an iconic sports car dashboard while preserving driver focus and mechanical trust, not its obsolete gauges, switches, or combustion-era layout.",
    "sj-story-one-message-marketing": "A research assistant launch page claims citations, speed, collaboration, privacy, multiple models, exports, templates, automation, and lower cost.",
    "sj-story-sell-the-improvement": "Rewrite features including automatic citations, source comparison, and export around a consultant producing a trustworthy client brief before a morning meeting.",
    "sj-story-three-act-launch": "A launch has a working cited-answer demo, a customer story, and availability today, but its current run of show starts with architecture and ends without a clear action.",
    "sj-story-number-context": "A benchmark reports 37 percent faster synthesis on 120 English reports, from 8.1 to 5.1 minutes, with no quality difference detected in that sample.",
    "sj-story-historical-analogy": "Position an AI coding assistant using a transition from manual lookup to interactive tools while explicitly avoiding claims that adoption is inevitable.",
    "sj-story-demo-rehearsal-loop": "A seven-minute keynote demo imports sources, asks a question, and exports a brief; import fails one in five runs and the current rehearsal lasts nine minutes.",
    "sj-story-values-marketing": "A privacy campaign claims user control; the product supports local deletion and export but defaults to training consent buried in settings.",
    "sj-story-missionary-pr": "Create a useful PR angle around how small nonprofits can verify AI-generated grant research, supported by a public checklist and a transparent demo.",
    "sj-story-old-story-new-tool": "Explain an AI voice archive through the enduring human wish to preserve a grandparent's stories, while keeping consent and editing responsibility visible.",
    "sj-people-a-player-bar": "A product designer candidate shipped two accessible mobile flows, improved activation by 18 percent, challenges weak premises respectfully, and lacks enterprise experience.",
    "sj-people-missionaries-not-mercenaries": "A senior engineer values the mission, has stayed through difficult customer work, asks hard questions about strategy, expects market pay, and protects family time.",
    "sj-people-pushback-interview": "Design an interview for a platform lead who must challenge a founder's unsafe launch shortcut without becoming reflexively oppositional.",
    "sj-people-small-a-team": "A six-week pilot needs mobile UX, API integration, security review, customer onboarding, and one accountable product decision; 14 people currently attend every meeting.",
    "sj-people-one-owner-no-committees": "Seven leaders can block a pricing decision due Friday; product has the data but finance, sales, and legal inputs are not separated from vetoes.",
    "sj-people-blunt-truth-review": "A launch video is visually polished but hides the slow core task and makes an unsupported accuracy claim; the editor needs actionable feedback today.",
    "sj-people-no-seagull-management": "A CEO joins monthly, reverses decisions after five-minute demos, leaves criticism unowned, and causes two weeks of rework after each visit.",
    "sj-people-management-by-values": "A distributed team escalates speed-versus-quality, privacy-versus-growth, and autonomy-versus-consistency decisions because its values are abstract nouns.",
    "sj-people-ideas-from-anywhere": "Frontline support has three recurring onboarding ideas, but only directors present in product review and rejected contributors receive no explanation.",
    "sj-people-founder-soul-guardian": "A beloved writing tool considers ads and engagement loops; its enduring promise is private, calm thinking, while the founder personally dislikes all subscriptions.",
    "sj-people-ceo-at-bottom": "Support agents need approval for refunds under $50 while executives receive daily custom reports that take operators six hours to prepare.",
    "sj-people-confidant-board": "A founder needs counsel on product taste, financing, people conflict, and personal sustainability; current advisers are two investors who usually agree.",
    "sj-people-ask-for-help": "Draft a request to an experienced accessibility lead about one unresolved focus-order decision after two prototypes and a user test.",
    "sj-people-smart-people-can-leave": "A critical engineer has no growth path, carries undocumented deployment knowledge, reports chronic on-call load, and has declined a counteroffer discussion.",
    "sj-people-permanent-ensemble": "A studio repeatedly builds launch films using the same director and editor but replaces design, sound, research, and production teams every project.",
    "sj-people-truth-to-founder": "Bad-news metrics are softened before reaching the founder; one security warning was delayed and two dissenters stopped speaking after public rebukes.",
    "sj-people-ed-catmull-patience": "An engineering lead doubts a new prototype because of latency and reliability; shared user goals exist and a two-week instrumented pilot can test both concerns.",
    "sj-people-andy-grove-correction": "A respected operator says the founder's roadmap reviews reward certainty and punish early warnings; three recent decisions show late surprise and rework.",
    "sj-people-bob-iger-trust": "Two companies want a content partnership after a prior reporting breach; rights, customer data, decision authority, and a reversible pilot need explicit terms.",
    "sj-strategy-focus-matrix": "Four products consume 42, 28, 18, and 12 percent of staff; only two share the target customer, one grows, and runway is nine months.",
    "sj-strategy-differentiation-or-death": "A meeting transcription startup claims better AI, while buyers compare it with bundled tools on accuracy, consent, workflow fit, and switching cost.",
    "sj-strategy-innovate-out": "A storage product faces commoditized pricing, but the team owns trusted compliance workflows and customers struggle to prove retention policies.",
    "sj-strategy-direct-channel": "A hardware company sells through distributors and receives quarterly summaries; customers need setup education and the team cannot see activation or failures.",
    "sj-strategy-ambush-distribution": "Independent designers already gather in three template marketplaces and two weekly critique streams; paid search is expensive and incumbents ignore those workflows.",
    "sj-strategy-say-yes-then-learn": "A hospital requests a six-week pilot; the team knows workflow software but lacks clinical safety expertise and can stage a non-diagnostic test with an adviser.",
    "sj-strategy-reality-is-malleable": "The team says procurement forbids a pilot, but nobody has read the policy; security review is real, budget timing is negotiable, and patient data cannot be used.",
    "sj-strategy-failure-apprenticeship": "A launch missed targets after ignored beta churn, a late pricing change, one platform outage, and an assumption that waitlist size predicted paid use.",
    "sj-strategy-startup-discipline": "A company has $1.2 million cash, $145,000 monthly burn, weak retention, nine open roles, and one enterprise pilot that could prove the core workflow.",
    "sj-strategy-pivot-to-core": "A failed website builder has one internal collaboration engine that three agencies repeatedly ask to license; legacy hosting commitments remain.",
    "sj-strategy-synthesizer-strategy": "Combine speech recognition, citations, CRM context, and approval workflows into one outcome for account managers preparing a verified follow-up.",
    "sj-strategy-do-not-overplay-hand": "A supplier delay gives temporary leverage in renewal talks; the company has one alternative, needs the relationship next year, and is considering an ultimatum.",
    "sj-strategy-build-for-yourself": "The founding team uses its own developer notebook daily and loves keyboard control, while external researchers need collaboration and have not validated willingness to pay.",
    "sj-strategy-company-as-invention": "A company promises exceptional end-to-end privacy but security reviews happen late, incentives reward launch count, and customer incidents lack one owner.",
    "sj-strategy-web-as-community": "A 40,000-person newsletter wants to become a community; readers share a professional practice but currently cannot help, recognize, or govern one another.",
    "sj-learning-biographies-as-mentors": "Use three episodes from a builder biography to study how they responded to failure; include contradictory behavior and differences in capital and power.",
    "sj-learning-regret-vs-mistake": "A founder declined a role two years ago using good family information, later envied the company's success, and can pursue similar work now.",
    "sj-learning-mortality-lens": "A builder is choosing between a prestigious expansion and completing meaningful work, while supporting dependents and managing a reversible six-month option.",
    "sj-learning-avocation-to-vocation": "A weekend furniture maker has practiced for four years, receives repeat commissions, dislikes sales, and has six months of savings for bounded paid experiments.",
    "sj-learning-endurance-loop": "Design 100 writing reps for clearer product memos using weekly editor feedback, a sustainable three-day cadence, and a stop rule for declining sleep.",
    "sj-learning-fundamentals-practice": "A designer's polished screens still have weak hierarchy; create a drill around spacing and type scale, then retest on a real settings page.",
    "sj-learning-progressive-summarization": "Process complete notes from a 12-chapter book and two interviews into sourced claims, contradictions, and no more than three reusable operating practices.",
    "sj-learning-balanced-builder-audit": "A launch plan requires 70-hour weeks for three months, has already reduced sleep and family time, and can cut two secondary markets or hire support.",
    "sj-learning-all-glory-fleeting": "After a public award, a founder is ignoring user complaints, overcommitting to press, and skipping the craft review that produced the winning work.",
    "sj-anti-revenge-motive-check": "A founder wants to enter a former partner's market after a public insult; customer pull is weak and a neutral adjacent market has stronger evidence.",
    "sj-anti-channel-stuffing-check": "Quarterly shipments rose 40 percent, partner inventory doubled, discounts increased, returns lag by 60 days, and end-customer activation grew 6 percent.",
    "sj-anti-too-much-money-check": "After raising $30 million, a pre-retention startup plans 45 hires, three offices, and a national campaign before its six-month retention cohort matures.",
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
    skill_paths = sorted(SKILLS.glob("sj-*/SKILL.md"))
    skill_names = {path.parent.name for path in skill_paths}
    if set(POSITIVE_CONTEXTS) != skill_names:
        missing = sorted(skill_names - set(POSITIVE_CONTEXTS))
        extra = sorted(set(POSITIVE_CONTEXTS) - skill_names)
        raise SystemExit(f"Positive context coverage drift. Missing={missing}; extra={extra}")

    for path in skill_paths:
        name = path.parent.name
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
                "prompt": f"{example} Context: {POSITIVE_CONTEXTS[name]}",
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
