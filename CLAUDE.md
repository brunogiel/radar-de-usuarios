# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

Radar de Usuarios is **not an application**. It is an installable user discovery method packaged as a skill bundle for AI coding assistants (Codex and Claude Code). The "code" is a small Python initializer plus a corpus of markdown/YAML files (skill prompt, workflow step files, agent definitions, document templates) that an assistant loads and follows to guide a human-centered research process.

Two distinct consumers must be kept in mind when editing:

1. **Method authors** (you, working in this repo): edit the bundle — `skills/`, `workflows/`, `agents/`, `templates/`, `scripts/`, `docs/`.
2. **End users**: install the bundle, then their assistant materializes a `radar/` workspace inside *their* project using `scripts/init_project.py`. The `radar/` folder belongs to user projects, never to this repo.

## Commands

There is no build, lint, or test suite. The only executable code paths:

```bash
# Install the bundle into the assistant's local skills directory.
./install.sh codex     # → ~/.codex/skills/radar-guia
./install.sh claude    # → ~/.claude/skills/radar-guia

# Initialize a radar/ workspace inside a target project (run from anywhere).
python3 scripts/init_project.py --project-root <path> --method-root <repo-root>
python3 scripts/init_project.py --project-root <path> --method-root <repo-root> --force  # overwrite
```

`install.sh` performs `rm -rf` on the destination before copying — re-running is the supported way to refresh an installed bundle. It also renames `agents/` to `method-agents/` at the destination; preserve that mapping if you touch the installer.

`init_project.py` copies templates with date and project-name substitution into `state.yaml`, and creates the full `radar/` and `radar/interviews/` directory tree. It skips existing files unless `--force` is passed.

## Architecture

The bundle has five layers; each plays a distinct role at runtime:

1. **`skills/radar-guia/SKILL.md`** — entry point. Frontmatter declares the skill; the body defines Bruno's persona (warm, direct, didactic, evidence-first), activation contract, hard principles, gate menu, response format, and the path it must take to bootstrap a session: locate the project, run `init_project.py` if `radar/` is missing, then read `state.yaml` + `documento-discovery.md` + `assumptions.md` + the active step file.
2. **`workflows/user-discovery/steps/01-..10-*.md`** — ten ordered step files. The skill instructs the assistant to **read only the active step file**, never the full set. Each step declares: objective, documents to touch, guide questions, template usage, gate criteria, and recommended status transitions.
3. **`agents/*.md`** — selectable perspectives ("council") with explicit contracts (tension, inputs, questions, output, success metrics). Bruno picks 3–5 per important gate. `agents/README.md` encodes the selection heuristics; do not assume all agents are convoked by default.
4. **`templates/*.md` and `templates/state.yaml`** — copied verbatim into a user's `radar/` by `init_project.py`. **Templates are not blank placeholders**: they embed working instructions the assistant follows when filling each document. Edit them as you would edit prompts.
5. **`scripts/init_project.py`** — the only executable. It hard-codes the list of templates and the interview subfolder layout. Adding a new top-level template requires updating `TEMPLATE_FILES`; adding an interviews-folder template requires `INTERVIEW_TEMPLATE_FILES`.

`docs/method-architecture.md` and `docs/source-distillate.md` document the method itself and are the authoritative reference for principles. `skills/radar-guia/references/method-summary.md` is the in-bundle copy the installed skill reads when it can't see `docs/`.

### Runtime state model

Per-project state lives in `radar/state.yaml` (templated from `templates/state.yaml`). Valid `current_status` values are fixed: `not_started`, `capturing`, `drafted`, `validated`, `advanced_with_assumptions`. Each step has a boolean `gate`. Gates close with one of four recommended actions: `Avanzar`, `Profundizar`, `Cuestionar`, `Concilio`. Keep these vocabularies aligned across `state.yaml`, `SKILL.md`, step files, and docs — divergence will silently break the guide's loop.

### Document responsibilities

The `radar/` workspace is intentionally split so raw material, decisions, and synthesis stay separate:

- `documento-discovery.md` is the index and executive summary.
- `assumptions.md` and `decision-log.md` are append-only journals.
- One file per stage (`research-mercado.md`, `usuarios-y-muestra.md`, etc.).
- `interviews/` enforces the chain: `incoming/` → `transcripts/` + `notes/` → `evidence-ledger.md` → `sintesis.md`. No insight without traceable evidence.

## Conventions That Matter When Editing The Bundle

- **Language**: all method content (SKILL.md, step files, agent definitions, templates, in-bundle references) is written in Spanish, intentionally without accents in the prompt body. README and `docs/` are in English. Match the surrounding language when editing a file.
- **Bruno's voice**: first person, warm but direct, didactic, no methodological jargon when a plain phrase works. Don't soften the hard principles in `SKILL.md` (no inventing data, no skipping gates, no "canvas" framing, mark inferences as `Lectura del copiloto`).
- **Gate menu wording**: present options by name (`Avanzar`/`Profundizar`/`Cuestionar`/`Concilio`), never as A/B/C.
- **Step files are atomic units**: an assistant only loads the active one. Don't introduce cross-step dependencies that require reading siblings.
- **Templates carry instructions**: when adding fields, write them as guidance for the assistant to follow, not as empty form fields.
- **Council selection rules**: `tecnologo` only for tech-relevant projects; `experto-industria` is configured at runtime with the real industry; `dueno-pyme` and `taxista` have specific triggers documented in `agents/README.md` and `SKILL.md`. Keep these triggers consistent across both files.
- **Privacy boundary**: `.gitignore` excludes `source-materials/`, `private/`, and `*.pdf`. The public repo contains generic method files only; never commit client work, transcripts, or proprietary references.

## Branch

Active development branch for this work: `claude/add-claude-documentation-phxDE`. Push only to the designated branch.
