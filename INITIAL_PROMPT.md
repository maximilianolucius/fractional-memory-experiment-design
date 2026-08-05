# INITIAL_PROMPT — brief + rubrica (fractional-memory-experiment-design)

> El CHIEF lee esto en el PRIMER turno y lo convierte en paper/outline.md, research_state.md,
> decisions/DECISION_LOG.md y la primera assignments/CURRENT.md. Lee IDEA.md integro PRIMERO.

## Contexto (importante)
NO es un proyecto vacio. El operador ya cargo un PACK MATEMATICO COMPLETO y verificado en
`source_pack/` (21 archivos) mas la bibliografia extendida en la raiz (`17_BIBLIOGRAPHY.md`,
`18_CITATION_MAP.md`, `19_BIBLIOGRAPHIC_AUDIT.md`, `20_RELATED_WORK_POSITIONING.md`). Ese pack
ES la fuente de verdad del paper. El tipo de paper, el titulo, el set de 17 teoremas (ya probados
o derivados) y la matriz de claims YA ESTAN DECIDIDOS ahi. Tu trabajo NO es re-inventarlos: es
REDACTAR el manuscrito riguroso a partir de ellos y montar el benchmark de simulacion reproducible.

## Tarea del PRIMER turno CHIEF (ejecuta, no propongas)
1. Lee IDEA.md integro. Lee, en source_pack/, al menos: README.md, THEOREM_INDEX.md,
   15_PAPER_BLUEPRINT_AND_CLAIM_MATRIX.md, 02_MAIN_DRAFT_MATHEMATICAL_AUDIT.md,
   16_IMPLEMENTATION_AND_VALIDATION_SPEC.md. Hojea 01, 03..14 y la bibliografia raiz.
2. Escribi AHORA:
   - `paper/outline.md`: la estructura de manuscrito de `15_*` (14 secciones), y por seccion:
     el claim, la evidencia (que teorema Txx la respalda, o que artefacto de simulacion la requiere),
     y su estado en la matriz de claims (permitido-tras-analisis / requiere-simulacion /
     requiere-experimento / prohibido).
   - `research_state.md`: tesis (la novedad defendible de `20_*` seccion 2), tipo de paper
     (teorico dirigido por teoremas + benchmark de simulacion), fase actual, y plan por prioridad.
   - `decisions/DECISION_LOG.md`: rubrica CONGELADA (las reglas duras de IDEA.md seccion 6 +
     la matriz de claims + el MVP de 4 modelos con dimension latente maxima m fija).
   - `assignments/CURRENT.md`: la PRIMERA tarea acotada para el RESEARCHER. Sugerencia de arranque:
     montar `paper/` compilable (esqueleto LaTeX de las 14 secciones con abstract + front matter),
     o formalizar T1-T2 (equilibrio/Jacobiano/alpha*(A) exactos de `04_*`) como primera seccion de
     resultados con su prueba y su test unitario analitico (x*=2/3, T(A), D(A), alpha*(0.3)).

## Rubrica
Paper academico riguroso, honesto y reproducible, EN INGLES. Separar lo probado de lo conjeturado;
toda afirmacion con su cita correcta (`18_CITATION_MAP.md`); NO usar "proof"/"proved" hasta demostrar;
resultados computacionales solo si pasan los gates de `source_pack/16_*`; el PDF debe compilar tras
cada turno; nada de los 7 claims PROHIBIDOS de IDEA.md seccion 5; PENDING-HUMAN para lo no ejecutable.
Escribir research_state.md y assignments/CURRENT.md SIN backslashes.
