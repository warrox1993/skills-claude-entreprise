#!/usr/bin/env bash
# Teste un skill en conditions réelles avec Claude Code en mode non interactif.
#
# Le prompt envoyé est le contenu de exemples/entree.md, sans jamais nommer le skill :
# on vérifie ainsi que Claude le déclenche seul, à partir de sa description.
# Les huit plugins du dépôt sont chargés ensemble pour que les skills soient en concurrence.
# Seuls les réglages du projet sont lus (--setting-sources project) : les plugins, skills
# et hooks personnels de la machine n'interfèrent pas avec le test.
#
# Utilisation : scripts/tester-skill.sh <dossier-du-skill> <dossier-de-sortie>
# Produit dans <dossier-de-sortie> : <skill>.jsonl (flux complet), <skill>.md (réponse finale)
# et une ligne de verdict sur la sortie standard.

set -euo pipefail

skill_dir=$(cd "$1" && pwd)
sortie=$(mkdir -p "$2" && cd "$2" && pwd)
depot=$(cd "$(dirname "$0")/.." && pwd)
skill=$(basename "$skill_dir")

args=()
for plugin in "$depot"/plugins/*/; do
  args+=(--plugin-dir "$plugin")
done

travail=$(mktemp -d)
trap 'rm -rf "$travail"' EXIT
cd "$travail"

debut=$(date +%s)
claude -p \
  --setting-sources project \
  "${args[@]}" \
  --output-format stream-json --verbose \
  --no-session-persistence \
  "$(cat "$skill_dir/exemples/entree.md")" \
  < /dev/null > "$sortie/$skill.jsonl" 2> "$sortie/$skill.err" || true
duree=$(( $(date +%s) - debut ))

python3 - "$sortie/$skill.jsonl" "$sortie/$skill.md" "$skill" "$duree" <<'EOF'
import json, sys
flux, reponse, skill, duree = sys.argv[1:5]
declenches, resultat, cout = [], "", None
for ligne in open(flux, encoding="utf-8"):
    try:
        evt = json.loads(ligne)
    except json.JSONDecodeError:
        continue
    if evt.get("type") == "assistant":
        for bloc in evt.get("message", {}).get("content", []):
            if bloc.get("type") == "tool_use" and bloc.get("name") == "Skill":
                declenches.append(bloc.get("input", {}).get("skill", ""))
    if evt.get("type") == "result":
        resultat = evt.get("result") or ""
        cout = evt.get("total_cost_usd")
open(reponse, "w", encoding="utf-8").write(resultat)
ok = any(d.split(":")[-1] == skill for d in declenches)
print(f"{skill}\tdeclenche={'oui' if ok else 'non'}\tskills_appeles={','.join(declenches) or '-'}\t"
      f"duree={duree}s\tcout_usd={cout}\tlongueur={len(resultat)}")
EOF
