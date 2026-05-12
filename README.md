# Radar de Usuarios

An installable user discovery method for Codex and Claude.

Radar helps an AI assistant guide a human-centered research process with persistent project documents, explicit state, assumptions tracking, interview intake, evidence handling, and a selectable council of specialist agents.

## What It Does

- Creates a `radar/` workspace inside the active project.
- Guides discovery step by step, from project alignment to evidence-backed synthesis.
- Keeps assumptions, decisions, market research, interview guides, recruiting, fieldwork and synthesis in separate files.
- Stores interview transcripts, notes, consent records and field materials in a traceable folder structure.
- Converts raw interview material into an evidence ledger before writing patterns or insights.
- Lets the guide call a small council of agents when a decision needs more pressure, context or lateral thinking.
- Supports market research as a dedicated flow with cited sources.

## Install

From the repository root:

```bash
./install.sh codex
```

or:

```bash
./install.sh claude
```

The installer copies the `radar-guia` skill and packages the workflows, agents, templates and scripts required to run the method.

## Start A Project

In the project where you want to run the method, ask your assistant:

```text
Use Radar de Usuarios to start a user discovery process.
```

The guide initializes this workspace:

```text
radar/
├── documento-discovery.md
├── state.yaml
├── assumptions.md
├── decision-log.md
├── base-conocimiento.md
├── research-mercado.md
├── usuarios-y-muestra.md
├── guias-entrevista.md
├── reclutamiento.md
├── checklist-campo.md
├── guia-contexto.md
├── sintesis.md
├── inputs/
└── interviews/
    ├── README.md
    ├── index.md
    ├── evidence-ledger.md
    ├── incoming/
    ├── notes/
    │   └── _template-notas.md
    ├── transcripts/
    ├── artifacts/
    ├── consent/
    └── processed/
```

## Guide Actions

At each gate, the guide recommends one action:

- `Avanzar`
- `Profundizar`
- `Cuestionar`
- `Concilio`

Progress is flexible and explicit. If the project moves forward with incomplete information, Radar records that state as `advanced_with_assumptions` and keeps the open assumptions visible.

## V1 Scope

Radar V1 delivers evidence-backed user understanding:

- Initial alignment and project maturity.
- Design Challenge.
- Knowledge base and unknowns.
- Market research when relevant.
- Target users and qualitative sample.
- Interview guides.
- Recruiting and fieldwork checklist.
- Interview transcripts, notes and field materials.
- Synthesis with facts, patterns, insights, design principles and HMW questions.

## Sources And Privacy

The public repository contains generic method files only. Private projects, client work and company-specific examples are excluded.

The method uses author-owned facilitation patterns and external human-centered design references as background. External references are listed by category in `docs/reference-map.md`; source documents remain with their original owners.
