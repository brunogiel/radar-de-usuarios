# Method Architecture

Empat.ia (Diseño con Empatía y la IA) is an installable user discovery method for AI coding assistants. Its central deliverable is a set of **design principles** traceable to evidence: actionable decision rules the user applies to product choices, communication with users and strategic priorities.

## Layers

1. Main skill: `descubrimiento-guia`.
2. Workflow steps: `workflows/user-discovery/steps/`.
3. Agents: `agents/`.
4. Templates: `templates/`.
5. Project initializer: `scripts/init_project.py`.

## State

Project state lives in `descubrimiento/state.yaml`.

Valid statuses:

- `not_started`
- `capturing`
- `drafted`
- `validated`
- `advanced_with_assumptions`

## Persistent Documents

The work lives in `descubrimiento/`.

`documento-discovery.md` acts as the main index and executive summary. Stage-specific files keep raw material, decisions and synthesis from collapsing into one long conversation.

Documents:

- `documento-discovery.md`: living index and executive summary.
- `state.yaml`: current step, status, available agents and recommended action.
- `assumptions.md`: active, validated and discarded assumptions.
- `decision-log.md`: decisions and tradeoffs.
- `base-conocimiento.md`: knowns, unknowns and learning goals.
- `research-mercado.md`: market research with sources.
- `usuarios-y-muestra.md`: roles, participant profiles and sample.
- `guias-entrevista.md`: interview guides by profile.
- `reclutamiento.md`: outreach, channels and recruiting tracker.
- `checklist-campo.md`: before, during and after fieldwork.
- `guia-contexto.md`: observation, experts, analogies and immersion.
- `sintesis.md`: facts, patterns, insights, design principles and HMW questions.
- `interviews/README.md`: intake and processing flow for field material.
- `interviews/index.md`: interview tracker, files, consent and gaps.
- `interviews/evidence-ledger.md`: atomic evidence by interview before synthesis.
- `interviews/notes/_template-notas.md`: structured note template for each interview.

## Gates

Each gate ends with a recommended action:

- Avanzar
- Profundizar
- Cuestionar
- Concilio

The guide can recommend moving forward with assumptions, as long as the assumptions are recorded and visible.

## Council And Agents

Agents are selectable perspectives with clear contracts. Each agent defines:

- The tension it brings.
- Inputs it needs.
- Questions it asks.
- Expected output.
- Success metrics.

**The Guide proposes, the user decides.** For each council, the Guide suggests 3-5 agents with a short justification each. The user can confirm, add or remove agents before the council is convened. `dueno-pyme` is proposed when small business reality affects adoption, budget, operations or decision-making. `filosofo` is proposed when the council needs to question assumptions, sharpen definitions or surface ethical risks. `taxista` is proposed when the council needs lateral thinking, plain language, analogies or a non-expert perspective.

## Method Sources

See `docs/source-distillate.md` for the generalized method principles used to shape templates and workflow steps.
