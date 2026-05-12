#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-codex}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

case "$TARGET" in
  codex)
    DEST="$HOME/.codex/skills/radar-guia"
    ;;
  claude)
    DEST="$HOME/.claude/skills/radar-guia"
    ;;
  *)
    echo "Usage: ./install.sh [codex|claude]"
    exit 1
    ;;
esac

rm -rf "$DEST"
mkdir -p "$DEST"

cp -R "$ROOT_DIR/skills/radar-guia/." "$DEST/"
cp -R "$ROOT_DIR/workflows" "$DEST/workflows"
cp -R "$ROOT_DIR/agents" "$DEST/method-agents"
cp -R "$ROOT_DIR/templates" "$DEST/templates"
cp -R "$ROOT_DIR/scripts" "$DEST/scripts"

echo "Installed Radar de Usuarios into $DEST"

