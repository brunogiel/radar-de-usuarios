# Empat.ia

> Installable method to **guide you through a user discovery project**, using [Claude](https://claude.com/claude-code) or Codex. A tandem between YOU + Artificial Intelligence to carry out a Design Thinking project.

Empat.ia is a co-pilot that guides you through an empathic design process following the Design Thinking methodology. The final deliverable is **design principles** traceable to evidence, which you'll use to decide on product, user communication, and strategy.

## ⚠️ Before you use it

- **It's a co-pilot.** It doesn't replace fieldwork. If you don't talk to real users, the method doesn't work.
- **It takes time: at least a week of serious dedication + 10-12 interviews done by you.** The Guide puts together the interview guides, helps you recruit, and organizes the evidence, but it doesn't interview for you.
- **It doesn't replace professional judgment in high-stakes research** (medical, legal, financial, user vulnerability). Consult with a senior researcher.


## What it does

- It walks you through building **design principles** traceable to evidence. That is the central deliverable.
- It creates a `discovery/` folder inside your project with persistent documents (state, assumptions, decisions, interviews, synthesis).
- It guides you step by step through 10 stages, from initial alignment to evidence-based synthesis.
- It separates facts, assumptions, and inferences. It doesn't let you confuse them.
- It turns raw interview material into traceable atomic evidence before writing insights and principles.
- It offers you a council of agents (economist, sociologist, philosopher, artist, SME owner, cab driver, and others) when a decision needs more pressure.
- It keeps the project state visible at all times: where you are, what you've done, what's next.

## Who it's for

For anyone willing to learn from their users and ready to do the work. In particular: early-stage founders, Product Managers, UX Researchers, SME owners rethinking a service, students, and innovation teams.

Minimum requirements:

| What you need                          | What for                                       |
| -------------------------------------- | ---------------------------------------------- |
| Paid Claude or Codex account           | So an assistant can run the method with you    |
| 10-12 interviews with real users       | You do the fieldwork; it can't be delegated    |
| At least 1 week of dedication          | Without time, the method doesn't pay off       |

## How to use it

Tell your assistant (Claude or Codex), by copying this message:

```text
Install this repo for me: https://github.com/brunogiel/Empat.ia
```

Your assistant downloads the method, explains what it's about, and gets started with you.

At any point you can ask _"how's it going"_ or _"status"_ and it shows you where you are.

### Installing as a global skill

Optional, if you want it available across all your projects without pasting the link every time:

```bash
./install.sh claude   # copies the skill to ~/.claude/skills/discovery-guide
./install.sh codex    # copies the skill to ~/.codex/skills/discovery-guide
```

Then you invoke it with _"use Empat.ia"_ from any project.

## The 10 stages

| Stage | What happens | Estimated time | Deliverable |
|---|---|---|---|
| 1. Start | Alignment, context, decision to unblock | 30-60 min | Initial `discovery-document.md` |
| 2. Design Challenge | Framing the problem without putting in a solution | 30-90 min | Challenge in the main document |
| 3. Market research | Category, substitutes, references (when applicable) | 1-3 hrs | `market-research.md` with sources |
| 4. Knowledge base | What we know, what we assume, what's left to learn | 30-60 min | `knowledge-base.md` |
| 5. Users and sample | Roles, profiles, and qualitative sample | 30-90 min | `users-and-sample.md` |
| 6. Interview guides | One guide per profile, cheat sheet not questionnaire | 1-2 hrs | `interview-guides.md` |
| 7. Recruitment | Channels, messages, tracker | 2-5 days | `recruitment.md` updating as you go |
| 8. Field checklist | Before, during, after each interview | 30 min | `field-checklist.md` |
| 9. Interview capture | Transcripts, notes, consents, atomic evidence | 1-3 weeks | Populated `interviews/` |
| 10. Synthesis | From evidence to **design principles** + insights, patterns, and HMW | 3-5 hrs | `synthesis.md` |

**Final deliverable**: a set of **design principles** traceable to interview quotes and evidence. Decision rules that you'll then use to guide:

- **Product**: what to build and what to leave out, how to prioritize features, how to resolve design dilemmas when they come up.
- **User communication**: what words to use, what to promise, what not to promise, how to speak to different profiles.
- **Strategy**: where to bet, which segment to prioritize, which opportunities are worth pursuing and which aren't.

The principles come with patterns, insights, top quotes, and "How might we..." (HMW) questions that open the next ideation phase. The principles are what you keep when the method ends.

The gated stages (1, 2, 3, 4, 5, 6, 9, 10) require updating the state before advancing. The method won't let you skip.

You can also use Empat.ia for a single stage. If you already have interviews done and just want synthesis, you can start straight at stage 10.

## The Guide's four actions

At every gate, the Guide recommends an action:

- **Advance**: the material is enough, we move to the next stage.
- **Deepen**: there's a base but more depth is needed before moving on.
- **Question**: there are dangerous assumptions or loose definitions, let's pressure-test them before advancing.
- **Council**: the decision deserves bringing in outside voices with different lenses.

The Guide proposes. You choose. You can always override the recommendation, and the Guide will show you the risks of doing so.

## The council

When a decision is hard, you can call the council: a multidisciplinary team that pressures you from different lenses. As in an IDEO team, we mix profiles that don't think alike:

- An **economist** who looks at incentives and costs.
- A **sociologist** who challenges cultural context.
- A **philosopher** who fights for definitions and assumptions.
- An **artist** who opens up analogies and non-obvious possibilities.
- An **SME owner** who brings operational reality.
- A **growth specialist** who looks at channels and language.
- And others: technologist, industry expert, uxer, qualitative researcher, and even a **cab driver** for when the team gets too expert-heavy and a lateral perspective is needed.

The Guide proposes 3-5 based on the project and the gate, and helps you choose. You can also add or remove agents by hand. The rule: combine at least three different lenses to force useful disagreement. The council shows you the angles you can't see on your own.

## Privacy and sources

The public repository contains only generic method files. Private projects, client work, and specific examples are kept out.

The method was built on proprietary facilitation material, external human-centered design references (IDEO, Acumen, and others), and **years of experience running this method manually, pre-AI**. References are listed in [`docs/reference-map.md`](docs/reference-map.md). Source documents remain with their original owners.

## License

MIT, see [`LICENSE`](LICENSE).
