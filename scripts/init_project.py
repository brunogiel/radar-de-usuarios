#!/usr/bin/env python3
"""Initialize Radar de Usuarios project documents."""

from __future__ import annotations

import argparse
import datetime as dt
import shutil
from pathlib import Path


TEMPLATE_FILES = [
    "documento-discovery.md",
    "state.yaml",
    "assumptions.md",
    "decision-log.md",
    "base-conocimiento.md",
    "research-mercado.md",
    "usuarios-y-muestra.md",
    "guias-entrevista.md",
    "reclutamiento.md",
    "checklist-campo.md",
    "guia-contexto.md",
    "sintesis.md",
]

INTERVIEW_TEMPLATE_FILES = {
    "interviews-readme.md": "README.md",
    "interview-index.md": "index.md",
    "evidence-ledger.md": "evidence-ledger.md",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize Radar de Usuarios documents.")
    parser.add_argument("--project-root", default=".", help="Project directory to initialize.")
    parser.add_argument("--method-root", default=None, help="Radar bundle root. Defaults to script parent/..")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files.")
    args = parser.parse_args()

    project_root = Path(args.project_root).expanduser().resolve()
    method_root = Path(args.method_root).expanduser().resolve() if args.method_root else Path(__file__).resolve().parents[1]
    templates_dir = method_root / "templates"
    radar_dir = project_root / "radar"

    if not templates_dir.exists():
        raise SystemExit(f"Templates not found: {templates_dir}")

    radar_dir.mkdir(parents=True, exist_ok=True)
    (radar_dir / "inputs").mkdir(exist_ok=True)
    (radar_dir / "interviews").mkdir(exist_ok=True)
    (radar_dir / "interviews" / "incoming").mkdir(exist_ok=True)
    (radar_dir / "interviews" / "transcripts").mkdir(exist_ok=True)
    (radar_dir / "interviews" / "notes").mkdir(exist_ok=True)
    (radar_dir / "interviews" / "artifacts").mkdir(exist_ok=True)
    (radar_dir / "interviews" / "consent").mkdir(exist_ok=True)
    (radar_dir / "interviews" / "processed").mkdir(exist_ok=True)

    now = dt.date.today().isoformat()
    created = []
    skipped = []

    for name in TEMPLATE_FILES:
        src = templates_dir / name
        dest = radar_dir / name
        if dest.exists() and not args.force:
            skipped.append(name)
            continue
        shutil.copyfile(src, dest)
        if name == "state.yaml":
            text = dest.read_text(encoding="utf-8")
            text = text.replace('created_at: ""', f'created_at: "{now}"')
            text = text.replace('updated_at: ""', f'updated_at: "{now}"')
            text = text.replace('project_name: ""', f'project_name: "{project_root.name}"')
            dest.write_text(text, encoding="utf-8")
        created.append(name)

    for src_name, dest_name in INTERVIEW_TEMPLATE_FILES.items():
        src = templates_dir / src_name
        dest = radar_dir / "interviews" / dest_name
        if dest.exists() and not args.force:
            skipped.append(f"interviews/{dest_name}")
            continue
        shutil.copyfile(src, dest)
        created.append(f"interviews/{dest_name}")

    note_template_src = templates_dir / "interview-note-template.md"
    note_template_dest = radar_dir / "interviews" / "notes" / "_template-notas.md"
    if note_template_src.exists() and (args.force or not note_template_dest.exists()):
        shutil.copyfile(note_template_src, note_template_dest)
        created.append("interviews/notes/_template-notas.md")

    print(f"Radar initialized at {radar_dir}")
    if created:
        print("Created: " + ", ".join(created))
    if skipped:
        print("Skipped existing: " + ", ".join(skipped))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
