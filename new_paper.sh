#!/usr/bin/env bash
# Crea un paper nuevo copiando esta base a un directorio destino, EXCLUYENDO todo
# el estado runtime (agentes, binding de Letta, logs, git, build). Así la copia
# arranca limpia y el primer run_loop.sh le crea sus propios agentes.
#
#   ./new_paper.sh /ruta/al/nuevo-paper
#
# Después: editar <destino>/INITIAL_PROMPT.md y correr <destino>/orchestrator/run_loop.sh
set -euo pipefail
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DST="${1:?uso: ./new_paper.sh /ruta/al/nuevo-paper}"

[ -e "$DST" ] && { echo "ERROR: '$DST' ya existe"; exit 1; }
mkdir -p "$DST"

rsync -a \
  --exclude '.git/' \
  --exclude '.letta/' \
  --exclude 'orchestrator/logs/' \
  --exclude 'orchestrator/.env' \
  --exclude 'orchestrator/STOP' \
  --exclude 'orchestrator/.agent_*' \
  --exclude 'orchestrator/.cycle' \
  --exclude 'orchestrator/.turn_idx' \
  --exclude 'orchestrator/.digest' \
  --exclude 'orchestrator/.handoff*' \
  --exclude 'orchestrator/.initial_injected' \
  --exclude 'paper/build/' \
  --exclude '__pycache__/' \
  "$SRC"/ "$DST"/

# arrancar de cero el estado canónico visible (opcional pero recomendado)
echo "Base copiada a: $DST"
echo "Siguiente:"
echo "  1) editá $DST/INITIAL_PROMPT.md (brief + rúbrica del paper)"
echo "  2) (opcional) cp $DST/orchestrator/.env.example $DST/orchestrator/.env  y ajustá PAPER_SLUG/modelos"
echo "  3) $DST/orchestrator/run_loop.sh -n 3"
