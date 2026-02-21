#!/usr/bin/env bash
# Bump plugin version and push — triggers auto-update for all consumers.
# Usage: ./scripts/publish.sh [major|minor|patch]
#   patch (default): 1.0.0 -> 1.0.1
#   minor:           1.0.0 -> 1.1.0
#   major:           1.0.0 -> 2.0.0

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PLUGIN_JSON="$REPO_ROOT/.claude-plugin/plugin.json"
MARKETPLACE_JSON="$REPO_ROOT/.claude-plugin/marketplace.json"
BUMP_TYPE="${1:-patch}"

if [[ ! -f "$PLUGIN_JSON" ]]; then
  echo "Error: $PLUGIN_JSON not found"
  exit 1
fi

# Extract current version
CURRENT_VERSION=$(grep '"version"' "$PLUGIN_JSON" | head -1 | sed 's/.*"\([0-9]*\.[0-9]*\.[0-9]*\)".*/\1/')
IFS='.' read -r MAJOR MINOR PATCH <<< "$CURRENT_VERSION"

case "$BUMP_TYPE" in
  major) MAJOR=$((MAJOR + 1)); MINOR=0; PATCH=0 ;;
  minor) MINOR=$((MINOR + 1)); PATCH=0 ;;
  patch) PATCH=$((PATCH + 1)) ;;
  *) echo "Usage: $0 [major|minor|patch]"; exit 1 ;;
esac

NEW_VERSION="$MAJOR.$MINOR.$PATCH"

# Update version in plugin.json
sed -i '' "s/\"version\": \"$CURRENT_VERSION\"/\"version\": \"$NEW_VERSION\"/" "$PLUGIN_JSON"

# Update version in marketplace.json
if [[ -f "$MARKETPLACE_JSON" ]]; then
  sed -i '' "s/\"version\": \"$CURRENT_VERSION\"/\"version\": \"$NEW_VERSION\"/" "$MARKETPLACE_JSON"
fi

echo "Bumped version: $CURRENT_VERSION -> $NEW_VERSION"

# Stage, commit, push
cd "$REPO_ROOT"
git add .claude-plugin/plugin.json .claude-plugin/marketplace.json
git commit -m "Release v$NEW_VERSION"
git push

echo ""
echo "Published v$NEW_VERSION"
echo "  Claude Code: consumers will auto-update on next startup"
echo "  OpenClaw:    consumers should run update.sh or git pull"
