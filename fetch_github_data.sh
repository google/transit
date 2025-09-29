#!/usr/bin/env bash
set -euo pipefail

OWNER="google"
REPO="transit"
OUTDIR="./github_export"

mkdir -p "$OUTDIR"
function fetch_all() {
  local endpoint="$1"
  local file="$2"
  local page=1
  local per_page=100
  echo "Fetching $endpoint ..."

  : > "$file"   # vide le fichier
  while true; do
    echo "Page $page..."
    resp=$(curl -s -H "Authorization: token $GITHUB_TOKEN" \
      "https://api.github.com/repos/$OWNER/$REPO/$endpoint?state=all&per_page=$per_page&page=$page")

    count=$(echo "$resp" | jq 'length')
    if [[ "$count" -eq 0 ]]; then
      break
    fi

    # Convertit le tableau en JSON Lines
    echo "$resp" | jq -c '.[]' >> "$file"

    page=$((page+1))
  done
}


fetch_all "issues" "$OUTDIR/issues.json"
fetch_all "pulls" "$OUTDIR/pulls.json"
fetch_all "issues/comments" "$OUTDIR/issues_comments.json"
fetch_all "pulls/comments" "$OUTDIR/pr_comments.json"

echo "✅ Export terminé dans $OUTDIR"
#!/usr/bin/env bash
set -euo pipefail

OWNER="google"
REPO="transit"
OUTDIR="./github_export"

mkdir -p "$OUTDIR"

function fetch_all() {
  local endpoint="$1"
  local file="$2"
  local page=1
  local per_page=100
  echo "Fetching $endpoint ..."

  : > "$file"   # vide le fichier
  while true; do
    echo "Page $page..."
    resp=$(curl -s -H "Authorization: token $GITHUB_TOKEN" \
      "https://api.github.com/repos/$OWNER/$REPO/$endpoint?state=all&per_page=$per_page&page=$page")

    count=$(echo "$resp" | jq '. | length')
    if [[ "$count" -eq 0 ]]; then
      break
    fi

    echo "$resp" | jq '.' >> "$file"
    page=$((page+1))
  done
}

fetch_all "issues" "$OUTDIR/issues.json"
fetch_all "pulls" "$OUTDIR/pulls.json"
fetch_all "issues/comments" "$OUTDIR/issues_comments.json"
fetch_all "pulls/comments" "$OUTDIR/pr_comments.json"

echo "✅ Export terminé dans $OUTDIR"
