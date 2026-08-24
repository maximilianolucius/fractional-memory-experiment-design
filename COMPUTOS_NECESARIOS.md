# Cómputos necesarios

Cola de pedidos de cómputo del plan `PLAN_10_PASOS_DESK_REJECTION.md`.
**El agente que trabaja el plan NO ejecuta cómputo:** escribe acá un bloque `[C-n]` autocontenido,
marca el paso como `BLOCKED-COMPUTE` en `PLAN_PROGRESO.md` y **DETIENE**. El operador asigna
manualmente otro agente. Cada bloque debe entenderse **sin** ver la conversación que lo originó.

Estados: `PENDIENTE` → `EN CURSO` → `LISTO` (o `DESCARTADO` + motivo).

---

## Plantilla (copiar y completar)

```
## [C-n] <título corto>            (estado: PENDIENTE)
Paso del plan:        <n>
Objetivo:             <qué se quiere obtener, 1-2 líneas>
Por qué se necesita:  <qué claim/teorema/gate depende de esto>
Inputs (rutas exactas): <código y datos a usar>
Qué computar:         <especificación precisa: modelo, rango de parámetros, nº réplicas,
                       tolerancias, seeds, qué se varía y qué queda fijo>
Entregables:          <rutas y formato exactos: JSON/PDF/tabla + campos que debe tener>
Criterio de aceptación: <cómo se verifica que el resultado es válido>
Recursos:             Orion — `ssh orion`, dir `~/fmed_work/`, venv `~/fmi_venv/bin/python`,
                      ~300 de 344 workers (dejar margen: corre un vLLM de terceros).
                      Smoke test obligatorio antes del run grande: `benchmark/smoke_test.py`.
                      Traer resultados con tar + md5sum en ambos extremos.
Restricciones:        no alterar la calibración congelada (`benchmark/bench.py`: AMP=0.10,
                      DDE_TAU=0.35, LAT_G=0.15) sin declararlo; el benchmark v3 está CONGELADO
                      (macro-accuracy 0.537, azar 0.25); reportar resultados aunque contradigan
                      lo esperado.
Notas/gotchas:        ver `HANDOFF.md` §9 (energía vs amplitud, calibración del DDE, resume por
                      JSONL, mark_stage tras refactors).
```

---

## Cola

_(vacía — el primer pedido va acá)_
