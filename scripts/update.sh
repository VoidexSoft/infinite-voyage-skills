#!/usr/bin/env bash
# Update infinite-voyage-skills for Claude Code and/or OpenClaw.
# Run from any directory — auto-detects installed locations.
# Usage: ./update.sh [--claude|--openclaw|--all]

set -euo pipefail

FLAG="${1:---all}"
PLUGIN_NAME="infinite-voyage-skills"
UPDATED=0

update_git_clone() {
  local dir="$1"
  local label="$2"
  if [[ -d "$dir/.git" ]]; then
    echo "Updating $label at $dir ..."
    git -C "$dir" pull --ff-only 2>/dev/null && {
      echo "  Updated to $(git -C "$dir" rev-parse --short HEAD)"
      UPDATED=$((UPDATED + 1))
    } || echo "  Warning: pull failed (check for local changes)"
  elif [[ -L "$dir" ]]; then
    local target
    target="$(readlink -f "$dir")"
    if [[ -d "$target/.git" ]]; then
      echo "Updating $label (symlink -> $target) ..."
      git -C "$target" pull --ff-only 2>/dev/null && {
        echo "  Updated to $(git -C "$target" rev-parse --short HEAD)"
        UPDATED=$((UPDATED + 1))
      } || echo "  Warning: pull failed (check for local changes)"
    fi
  fi
}

# --- Claude Code ---
update_claude() {
  echo "=== Claude Code ==="

  # Method 1: Plugin cache (installed via marketplace)
  CACHE_DIR="$HOME/.claude/plugins/cache"
  if [[ -d "$CACHE_DIR" ]]; then
    FOUND=$(find "$CACHE_DIR" -type d -name "$PLUGIN_NAME" 2>/dev/null | head -1)
    if [[ -n "$FOUND" ]]; then
      echo "Found cached plugin at $FOUND"
      echo "  Clearing cache to force re-download on next startup..."
      rm -rf "$FOUND"
      echo "  Cleared. Restart Claude Code to re-fetch latest version."
      UPDATED=$((UPDATED + 1))
    fi
  fi

  # Method 2: Project .claude/skills/ (symlinked or cloned)
  local project_skills
  for project_skills in ./.claude/skills ../.claude/skills; do
    if [[ -d "$project_skills/$PLUGIN_NAME" ]]; then
      update_git_clone "$project_skills/$PLUGIN_NAME" "Claude Code project skills"
    fi
  done

  # Method 3: Personal skills
  if [[ -d "$HOME/.claude/skills/$PLUGIN_NAME" ]]; then
    update_git_clone "$HOME/.claude/skills/$PLUGIN_NAME" "Claude Code personal skills"
  fi

  echo ""
}

# --- OpenClaw ---
update_openclaw() {
  echo "=== OpenClaw ==="

  # Workspace skills
  if [[ -d "./skills/$PLUGIN_NAME" ]]; then
    update_git_clone "./skills/$PLUGIN_NAME" "OpenClaw workspace skills"
  fi

  # Local/managed skills
  if [[ -d "$HOME/.openclaw/skills/$PLUGIN_NAME" ]]; then
    update_git_clone "$HOME/.openclaw/skills/$PLUGIN_NAME" "OpenClaw local skills"
  fi

  echo ""
}

case "$FLAG" in
  --claude)   update_claude ;;
  --openclaw) update_openclaw ;;
  --all)      update_claude; update_openclaw ;;
  *)          echo "Usage: $0 [--claude|--openclaw|--all]"; exit 1 ;;
esac

if [[ $UPDATED -gt 0 ]]; then
  echo "Done. $UPDATED location(s) updated."
else
  echo "No installations found to update."
  echo ""
  echo "Install first:"
  echo "  Claude Code: /plugin marketplace add VoidexSoft/infinite-voyage-skills"
  echo "  OpenClaw:    git clone git@github.com:VoidexSoft/infinite-voyage-skills.git ~/.openclaw/skills/$PLUGIN_NAME"
fi
