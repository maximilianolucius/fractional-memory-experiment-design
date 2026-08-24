# Plan de trabajo — 10 pasos para levantar el desk rejection

**Manuscrito:** *Safe active discrimination of fractional, delayed, and finite latent memory in a
strong-Allee predator–prey model* · **Autor:** Ibrahim Alraddadi (Islamic University of Madinah)
**Plan fuente (leer si falta detalle):** `PLAN_LEVANTAR_DESK_REJECTION_AIMS_2026-08-24.md` (937 líneas)
**Estado/infra del proyecto:** `HANDOFF.md` · **Auditoría previa:** `audits/`

---

## 0. Cómo trabajar (leer antes del Paso 1)

### 0.1 Diagnóstico
Fue **desk rejection**, no peer review. El editor **no** señaló un error matemático: falló el
screening de **novelty / scope / general significance**. Por eso NO se arregla con mejor redacción ni
agregando páginas: hay que **invertir la jerarquía científica** del paper, de *estudio computacional
ecológico* a *teoría general de límites de discriminación en horizonte finito*, con la ecología como
aplicación certificada.

### 0.2 North-star claim
Un editor que lea solo título + abstract + 1.5 páginas debe poder resumirlo así:
> Los mecanismos de memoria fraccionaria, con retardo y latente-finita pueden ser **estructuralmente
> distintos** y a la vez **estadísticamente indistinguibles** en horizonte finito bajo excitación
> acotada; imponer una restricción de **seguridad de estado** puede endurecer esa imposibilidad. Se
> prueba en un marco general de sistemas hereditarios y se certifica en un modelo strong-Allee.

### 0.3 PROTOCOLO DE CÓMPUTO — regla dura
**Vos (agente) NO ejecutás cómputo.** Si un paso lo requiere:
1. Escribí/actualizá **`COMPUTOS_NECESARIOS.md`** con el formato de §0.4.
2. Anotá en `PLAN_PROGRESO.md` el paso y el estado `BLOCKED-COMPUTE`.
3. **DETENÉ el trabajo y reportá al operador.** Él asignará otro agente al cómputo.
4. Cuando vuelvan los resultados, retomá desde donde quedaste y verificá los entregables.

**Cuenta como cómputo (⇒ pedir y parar):** correr o re-correr simulaciones y barridos; regenerar
figuras desde datos nuevos; validar numéricamente una cota o tasa; aritmética de intervalos /
certificados; auditorías estadísticas que requieran re-ejecutar ajustes (BIC, sensibilidades,
Monte Carlo); clean-run de reproducibilidad end-to-end.

**NO cuenta como cómputo (hacelo vos):** leer y auditar código sin ejecutarlo; compilar LaTeX
(`paper/build_all.sh`) y leer el log; editar texto, teoremas y pruebas; escribir matrices y
auditorías en Markdown; búsqueda y verificación bibliográfica; reordenar figuras/tablas ya existentes.

### 0.4 Formato obligatorio de `COMPUTOS_NECESARIOS.md`
Un bloque **autocontenido por pedido** (el agente de cómputo no ve esta conversación):
```
## [C-n] <título corto>            (estado: PENDIENTE | EN CURSO | LISTO)
Paso del plan:        <n>
Objetivo:             <qué se quiere obtener, 1-2 líneas>
Por qué se necesita:  <qué claim/teorema/gate del paper depende de esto>
Inputs (rutas exactas): <archivos de código y datos a usar>
Qué computar:         <especificación precisa: modelo, rango de parámetros, nº réplicas,
                       tolerancias, seeds, qué se varía y qué queda fijo>
Entregables:          <rutas y formato exactos: JSON/PDF/tabla + qué campos debe tener>
Criterio de aceptación: <cómo se sabe que el resultado es válido/correcto>
Recursos:             Orion — `ssh orion`, dir `~/fmed_work/`, venv `~/fmi_venv/bin/python`,
                      ~300 de 344 workers (dejar margen: corre un vLLM de terceros).
                      Smoke test obligatorio antes del run grande: `benchmark/smoke_test.py`.
Restricciones:        no romper la calibración congelada (`bench.py`: AMP=0.10, DDE_TAU=0.35,
                      LAT_G=0.15) sin decirlo explícitamente; el benchmark v3 está CONGELADO
                      (macro-accuracy 0.537, azar 0.25) — cualquier cambio debe justificarse.
```

### 0.5 Reglas transversales
- **Honestidad de claims:** nunca llamar teorema a lo que no está probado, ni "safe" a una celda por
  una simulación. Separar siempre: *certificado riguroso* / *condición analítica suficiente* /
  *diagnóstico numérico* / *tasa observada*.
- **El paper compila siempre:** tras cada edición, `paper/build_all.sh` debe terminar en exit 0, sin
  referencias ni citas colgantes. (Ojo: sin `figures/aims_mathematics_logo.png` el build FALLA.)
- **Bitácora:** mantené `PLAN_PROGRESO.md` con una línea por paso: `PASO n — DONE | IN-PROGRESS |
  BLOCKED-COMPUTE | BLOCKED-DECISION` + evidencia (archivo/commit).
- **No tocar** `orchestrator/` ni pushear el repo local (tiene secretos en su historia; ver `HANDOFF.md` §8/§11).

---

# Paso 1 — Congelar baseline y mapear la novedad (adversarial)

**Objetivo.** Saber, con evidencia, qué es realmente nuevo antes de escribir una sola línea nueva.

**Necesita.** La versión rechazada (PDF + fuentes en `paper/`); `source_pack/`; `audits/PAPER_AUDIT.md`;
`17_BIBLIOGRAPHY.md`; `18_CITATION_MAP.md`; `JOURNAL_POSITIONING.md`; acceso a búsqueda bibliográfica.

**Hacer.**
1. Congelar la versión rechazada como baseline inmutable (copia fechada + hash; no volver a editarla).
2. Búsqueda **adversarial** y actualizada (énfasis 2024–2026) en las 10 áreas: identificación de
   sistemas fraccionarios; discriminación fraccionario-vs-retardo; aproximación diffusive /
   suma-de-exponenciales de kernels fraccionarios; aproximación racional de transferencias
   fraccionarias; identificabilidad en horizonte finito; testing minimax en sistemas dinámicos;
   active model discrimination; safe experiment design / safe identification; adquisición de
   información con restricción de seguridad; predador-presa fraccionario con retardo.
3. Por cada trabajo cercano completar una fila con: cita · clase de modelo · identificabilidad
   estructural (s/n) · aproximación en horizonte finito (s/n) · presupuesto explícito de complejidad
   *m* (s/n) · cota estadística (s/n) · uniformidad sobre inputs acotados (s/n) · restricción de
   seguridad de estado (s/n) · certificado riguroso (s/n) · **qué prueban** · **qué agregamos nosotros**.
4. Auditar en particular las referencias `P01`, `SAFE26A`, `SAFE26B` (¿publicadas? ¿preprint? ¿qué
   prueban exactamente?) — el plan fuente marca que safe experiment design **ya existe** como teoría
   general: la novedad no puede ser "safe design per se".

**Entregable.** `NOVELTY_MATRIX.md`.

**Gate 1.** Ninguna claim de novedad sobrevive si ya existe esencialmente en la literatura. Para cada
contribución que se mantenga: está citado el **competidor más cercano** (no el más cómodo) y la
diferencia es verificable en una frase.

**Cómputo.** No.

---

# Paso 2 — Elevar los cuatro resultados a teoremas generales (A–D)

**Objetivo.** Que exista al menos un teorema **general** (fuera del caso strong-Allee). Este paso
decide el resto del plan y el journal.

**Necesita.** `source_pack/` (teoremas T1–T17 con sus derivaciones); teoremas vivos del manuscrito
(T4–T7, T8–T10, T11–T13, T16–T17, T20–T22, Lema R6.1, T23 + corolario prey-response);
`audits/MATHEMATICAL_REPAIR_NOTES.md` (enunciados de reemplazo ya redactados);
`research_rounds/` (R1–R6 y el chief-audit).

**Hacer.** Reformular cada resultado **independiente del predador-presa**, sobre una clase hereditaria
bien definida:
- **Teorema A — no-equivalencia estructural exacta.** Especificar sin ambigüedad: clase fraccionaria;
  clase racional/latente de estado finito; clase retarded-delay admitida; dominio analítico común;
  condición `CB≠0`; qué significa igualdad exacta; casos excluidos. **Búsqueda obligatoria de
  contraejemplos:** `CB=0`, canales no colocados, cancelaciones polo-cero, transferencias impropias,
  múltiples retardos, observación parcial.
- **Teorema B — aproximación cuantitativa en horizonte finito.** Pasar de existencia a **ley de
  complejidad**: `m ≥ m(ε,T,α,…) ⟹ ‖k_α − k_m‖_{L¹(0,T)} ≤ ε`, con tasa explícita o, como mínimo,
  cotas superior/inferior útiles en *m*.
- **Teorema C — obstrucción de testing uniforme.** Unificar aproximación + presupuesto de input +
  ruido: `E_m → 0 ⟹ inf_tests P_e(m,u) → 1/2`, **uniformemente** sobre los inputs admisibles.
  Re-auditar de cero los factores: muestreo, covarianza de ruido, nº de observaciones, operador de
  observación, cotas L¹/L² de convolución, KL / variación total / Pinsker, priors iguales vs desiguales.
- **Teorema D — techo de información bajo seguridad** (la mejora de mayor impacto potencial).
  Encadenar: condición de seguridad `x(t) ≥ A+δ` → restricción suficiente sobre el conjunto de
  perturbaciones admisibles → cota superior de la separación observable → cota inferior de error de C.

**Entregable.** Sección de teoría reescrita (enunciados + pruebas) + `CONTRAEJEMPLOS_AUDIT.md` con lo
que se intentó romper y qué sobrevivió.

**Gate 2.** Cada teorema declara **explícitamente** qué es uniforme, respecto de qué clase de
experimentos, y de qué depende (`m, T, σ, U, C_obs`). **Regla de honestidad:** si D no se prueba con
generalidad suficiente, **NO se vende como teorema** — queda como fenómeno certificado/numérico y eso
cambia el journal objetivo (Paso 7).

**Cómputo.** **Probable.** Si hace falta validar numéricamente la tasa de B, la uniformidad de C o el
techo de D (o buscar contraejemplos por barrido), escribí `COMPUTOS_NECESARIOS.md` y **DETENÉ**.

---

# Paso 3 — Reordenar la arquitectura: teoría al frente, ecología como aplicación

**Objetivo.** Que la señal editorial diga "paper matemático", no "informe de benchmark".

**Necesita.** Resultado del Paso 2; `paper/main.tex` y `paper/sections/`; el supplement; inventario
actual de figuras (`paper/figures/`) y tablas.

**Hacer.**
1. Renombrar la sección analítica: **no** "Analytical backbone: four results used by the experiments"
   (subordina la matemática a la simulación). Usar algo como *"Finite-horizon discrimination limits for
   hereditary mechanisms"*.
2. Imponer el orden narrativo: **teorema general → marco de discriminación hereditaria segura →
   especialización strong-Allee → consecuencias numéricas certificadas**. Nunca al revés.
3. **Subir al main las pruebas completas de los teoremas headline** (o al menos todas las partes no
   estándar). Bajar al supplement: derivaciones repetitivas, detalles de solver, inventarios de
   grillas, lemas secundarios, tablas extensas.
4. Reducir densidad visual del main: de ~19 figuras / ~11 tablas a **7–10 figuras y 4–7 tablas**
   (orientativo, no exigencia del journal). Candidatos a mover: figura de workflow, esquemas
   redundantes de familias de modelos, galería completa de waveforms, grillas secundarias,
   visualizaciones repetidas de barridos de retardo, convergencia detallada del solver, paneles extra
   de parámetros. **Quedan en el main solo las figuras que demuestran una claim central.**
5. La ecología debe leerse como: aplicación no trivial + sistema donde la seguridad tiene significado
   dinámico real + test bed certificado + prueba de que el teorema general produce números concretos.

**Entregable.** `main.tex` reestructurado + supplement actualizado + build en exit 0 + tabla de
mapeo "figura/tabla → claim que sostiene → main o supplement".

**Gate 3.** El editor **no** necesita abrir el supplement para entender por qué el paper importa. Toda
figura/tabla del main tiene una claim central asignada.

**Cómputo.** Solo si hay que **regenerar** figuras (no si solo se mueven o se recortan). En ese caso:
pedir y **DETENER**.

---

# Paso 4 — Reescribir título, abstract y las primeras 1.5 páginas

**Objetivo.** Que la novedad se comunique antes que la provenance y las limitaciones.

**Necesita.** `NOVELTY_MATRIX.md` (Paso 1); teoremas finales (Paso 2); abstract e introducción actuales.

**Hacer.**
1. **Título:** sentence case, front-load del **resultado** (no de la aplicación). El sistema
   strong-Allee puede ir en subtítulo o al final. Candidatos del plan fuente: *"Finite-horizon limits
   of discriminating fractional, delayed and latent memory under safety constraints"*; *"When
   fractional memory is structurally identifiable but experimentally indistinguishable"*.
2. **Abstract 180–240 palabras** (máx. 300, sin citas): 1 frase de problema general; 1–2 de novedad a
   nivel teorema; 1 de la consecuencia de seguridad; 1–2 de la aplicación certificada; 1 de
   significancia. **Solo 2–4 números.** **Eliminar:** "inherited", "not claimed as new", la narrativa
   del companion, inventarios de grillas y el exceso de métricas del benchmark.
3. **Primeras 1.5 páginas** deben responder, en orden: ¿cuál es el problema matemático? ¿qué se
   desconocía? ¿qué teorema probamos? ¿por qué importa fuera de la ecología predador-presa? ¿por qué
   la especialización strong-Allee es una especialización difícil y útil?
4. **Eliminar de la introducción la tabla** "Relationship between the previously submitted companion
   paper and the present manuscript" (cumple función defensiva, no científica) → reemplazar por **un
   párrafo conciso de provenance**; el detalle va a cover letter y disclosure interno.
5. **Contribuciones como claims falsables:** "We prove…", "We derive…", "We certify…", "We show that
   no admissible experiment can… under…", "We obtain an explicit complexity-dependent bound…".
   **Prohibido** como contribución principal: "we simulate…", "we benchmark…", "we provide figures…",
   "we study…" sin resultado.

**Entregable.** Título, abstract e introducción nuevos + lista de 3–4 contribuciones falsables.

**Gate 4.** Conteo de palabras del abstract en rango, ≤4 números, cero menciones defensivas del
companion; cada contribución es una afirmación que podría ser refutada.

**Cómputo.** No.

---

# Paso 5 — Cerrar provenance, overlap y self-containment

**Objetivo.** Eliminar la inconsistencia de autoría y que el paper se verifique sin depender de un
manuscrito no publicado.

**Necesita.** `RELATED_PAPER_DISCLOSURE.md`; `OVERLAP_AUDIT_PREVIOUS_SUBMISSION.md`; entrada `P01` de
la bibliografía; el companion; `paper/sections/` (buscar "companion", "our previous", "inherited").

**Hacer.**
1. **Corregir la inconsistencia:** el manuscrito tiene un solo autor (**Ibrahim Alraddadi**) mientras
   `P01` figura con **Maximiliano Lucius**. ⇒ **prohibido "our previous paper" / "our companion
   paper"**. Usar formulación factual: *"The ecological backbone follows the companion study [X]…"* y
   decir exactamente qué material se reutiliza.
2. **Autosuficiencia:** reproducir en el paper las ecuaciones necesarias, parámetros, equilibrio,
   Jacobiano, supuestos de estabilidad usados y cualquier lema indispensable. Citar el trabajo previo
   por provenance, **nunca como dependencia de una prueba faltante**.
3. **Auditoría de similitud:** comparar contra el companion; identificar coincidencias inevitables de
   ecuaciones; reescribir el texto descriptivo reutilizado; etiquetar el material idéntico; auditar
   captions, methods y descripciones del backbone ecológico. No perseguir un porcentaje: **cada
   coincidencia debe ser explicable y legítima**.

**Entregable.** `OVERLAP_PROVENANCE_AUDIT.md` (ecuaciones / parámetros / figuras / texto compartidos +
justificación + dónde se declara cada uno) + secciones corregidas.

**Gate 5.** `grep -ri "our previous\|our companion" paper/sections/` no devuelve nada; ningún resultado
del paper depende del companion para su prueba; idealmente cero figuras compartidas.

**Cómputo.** No (la auditoría de similitud es lectura/comparación).

---

# Paso 6 — Auditar estadística, seguridad y reproducibilidad

**Objetivo.** Que la evidencia numérica resista a un referee computacional, sin convertir el paper en
un informe.

**Necesita.** `benchmark/` (`core.py`, `designs.py`, `bench.py`, `run_all.py`, `validate_results.py`,
`fractional_delay_experiments.py`); `benchmark/results/*.json`; `artifacts/manifests/manifest.json`;
`FINAL_REPRODUCIBILITY.md`; `FINAL_CLAIM_EVIDENCE_MATRIX.md`.

**Hacer.**
1. **Auditoría estadística** (leyendo el código): implementación de BIC; nº efectivo de observaciones;
   normalización de la likelihood; priors de clase; ajuste de parámetros por modelo candidato; equidad
   de las penalizaciones de complejidad; intervalos de confianza / incertidumbre Monte Carlo;
   sensibilidad a SNR, horizonte, cadencia de muestreo y presupuesto latente *m*. Agregar barras de
   error **solo donde cambien la interpretación**.
2. **Auditoría de seguridad:** separar taxativamente (a) certificado riguroso, (b) condición analítica
   suficiente, (c) diagnóstico numérico de no-cruce, (d) tasa de cruce observada. **Nunca** llamar
   "safe" a una celda por una simulación si el enunciado pretende ser riguroso.
3. **Reproducibilidad fuerte:** definir un clean-run que parta de un checkout/zip limpio, recree
   resultados numéricos, recree figuras y tablas, compile main + supplement, verifique hashes o
   tolerancias, y reporte entorno y dependencias.
4. **Ledger de claims:** cada número del paper apuntando al artefacto que lo genera.

**Entregable.** `REPRODUCIBILITY.md`, `requirements.txt` / lock de entorno, `run_all.py` (o `make all`),
política de seeds, política de tolerancias numéricas, sanity tests independientes de máquina,
`CLAIM_EVIDENCE_LEDGER.md` actualizado.

**Gate 6.** Ninguna claim numérica sin artefacto trazable; los cuatro niveles de seguridad
correctamente etiquetados en todo el texto; el clean-run está **especificado** (ejecutarlo es cómputo).

**Cómputo.** **Sí, casi seguro** — ejecutar el clean-run, re-correr sensibilidades o recalcular
intervalos. Escribí `COMPUTOS_NECESARIOS.md` (un bloque `[C-n]` por auditoría) y **DETENÉ**.

---

# Paso 7 — Decision gate del journal (después del Paso 2, no antes)

**Objetivo.** Elegir el journal por **el paper que finalmente existe**, no por el que se querría tener.

**Necesita.** Resultado real de los teoremas A–D (Paso 2) y del Gate 2; `JOURNAL_POSITIONING.md`.

**Hacer.** Clasificar el resultado en un escenario y escribirlo con su justificación:
- **Escenario 1 — se logró el upgrade a nivel teorema:** existe un teorema general de
  no-discriminación en horizonte finito, con dependencia explícita en *m* y, preferentemente, una cota
  bajo restricción de seguridad ⇒ apuntar a un journal matemático general / applied-math exigente.
- **Escenario 2 — la teoría no se generalizó:** el resultado central queda específico del canal prey,
  mayormente numérico, dirigido por BIC/benchmark y sin teorema general de safety/information ⇒ **no
  venderlo como de significancia matemática general**; elegir journal especializado (dinámica no
  lineal / fraccionaria, identificación de sistemas, o biología matemática).

**Entregable.** `JOURNAL_DECISION.md`: escenario elegido, evidencia que lo sustenta, journal objetivo,
y qué claims quedan explícitamente fuera de alcance.

**Gate 7.** La decisión cita los teoremas efectivamente probados. **Prohibido** afirmar generalidad sin
un teorema general.

**Cómputo.** No. **Sí es un punto de parada por decisión** si el operador debe elegir el journal:
marcá `BLOCKED-DECISION` y consultá.

---

# Paso 8 — Migrar al template oficial y alcanzar ≥99% de compliance

**Objetivo.** Que no quede ningún motivo **evitable** para detener el manuscrito antes del peer review.

**Necesita.** El journal elegido (Paso 7); `AIMS_MATHEMATICS_TEMPLATE_NOTES.md`; fuentes oficiales
(descargarlas **el día del trabajo**): guía de submission del journal, template TeX oficial, portal de
submission (para AIMS: sciopen submission guidelines · aimspress.com/math · aimspress.jams.pub).

**Hacer.**
1. **Descargar instrucciones y template vigentes ese mismo día** — no trabajar de memoria. **No usar
   `aims_math_style.sty` como sustituto del template oficial.** Migrar el source al template.
2. **LaTeX/legibilidad para referees:** `\usepackage{lineno}` + `\linenumbers` según la instrucción
   vigente; compilación limpia sin warnings relevantes; cero referencias/citas rotas; todas las
   ecuaciones y símbolos visibles.
3. **Front matter:** título conciso en **sentence case** (capitalización correcta tras dos puntos);
   nombres completos de autores; afiliaciones en superíndice con departamento, organización, ciudad y
   país; corresponding con `*`, **dirección exacta, email y teléfono**; headings sentence case, máx. 4
   niveles; abstract <300 palabras sin citas y con contexto/método/hallazgos/significancia; **5–10
   keywords**; lista de abreviaturas antes de la introducción si corresponde; unidades SI.
4. **End matter, en este orden:** Author contributions (roles CRediT si hay varios autores) → heading
   **exacto** *"Use of Generative-AI tools declaration"* (declaración coherente con el uso real) →
   Acknowledgments → funding (declararlo incluso si no hubo) → conflict of interest → data
   availability si el template lo pide.
5. **Referencias:** numeradas **por orden de primera citación** (no alfabético) ⇒ **eliminar
   `\bibliographystyle{plain}`** y usar el mecanismo del template; citas en corchetes; nombres de
   journal en abreviatura **ISO 4**; máx. primeros 6 autores + "et al."; DOI cuando corresponda;
   reemplazar preprints por versiones peer-reviewed si existen; **auditar `P01`, `SAFE26A`, `SAFE26B`**
   contra la política vigente; verificar que cada referencia respalde exactamente la claim donde se usa.
6. **Figuras y tablas:** insertadas en el texto **y** entregadas como archivos separados;
   EPS/PNG/PDF/JPEG; ≥300 dpi si raster; RGB; llamadas en orden; caption de figura **abajo**, de tabla
   **arriba**; permisos para material reutilizado; fuentes legibles al tamaño final.
7. **Supplement:** solo material genuinamente secundario; ninguna claim principal depende de una
   prueba escondida; cross-references correctas; código/datos vinculados.

**Entregable.** `JOURNAL_COMPLIANCE_MATRIX.md` con columnas: requisito · fuente oficial · ¿obligatorio? ·
¿aplicable? · estado actual · evidencia/archivo · fix · PASS final.

**Gate 8.** **100% de los requisitos obligatorios en PASS (cero excepciones)** y
`compliance = PASS/aplicables ≥ 0.99`. Una desviación solo se admite si es advisory, está documentada
y no afecta peer review, metadata, referencias, ética, IA, figuras ni producción.

**Cómputo.** No (compilar LaTeX lo hacés vos).

---

# Paso 9 — Pre-review adversarial (tres mock reviews independientes)

**Objetivo.** Encontrar los contraejemplos y objeciones **antes** que el referee real.

**Necesita.** Manuscrito ya reestructurado (Pasos 3–5) y compilando; `audits/PAPER_AUDIT.md` como
ejemplo del nivel de dureza esperado.

**Hacer.** Tres revisiones **separadas**, cada una con su informe:
1. **H1 — Mock editor, 90 segundos.** Se le da **solo** título, abstract, primeras 1.5 páginas y
   conclusión. Debe contestar sin ayuda: ¿cuál es la novedad en una frase? ¿cuál es el teorema
   central? ¿por qué es general? ¿por qué encaja en este journal? ¿qué cambia respecto de la
   literatura previa? **Si no las contesta → FAIL:** volver al Paso 4 (o al 2 si falta el teorema).
2. **H2 — Mock referee matemático.** Atacar: supuestos; branch cuts; dominios analíticos; asintóticas
   de alta frecuencia; aproximación cerca de `t=0`; la tasa en *m*; la uniformidad de la cota de
   testing; modelo de ruido; operador de observación; el teorema de seguridad; el uso de Pinsker;
   aritmética de intervalos; reproducibilidad de los certificados.
3. **H3 — Mock referee aplicado/computacional.** Atacar: interpretación ecológica; realismo de las
   perturbaciones; sensibilidad paramétrica; equidad de la comparación de modelos; BIC; SNR; muestreo;
   cruce de seguridad; precisión del solver; implementación fractional-delay; calibración del modelo
   latente.

**Entregable.** `MOCK_EDITOR_REPORT.md`, `MOCK_REFEREE_MATH.md`, `MOCK_REFEREE_APPLIED.md`, cada uno
con objeciones, severidad y acción tomada.

**Gate 9.** H1 en PASS; toda objeción de H2/H3 está resuelta en el texto o declarada explícitamente
como limitación abierta.

**Cómputo.** Solo si una objeción exige un cálculo nuevo ⇒ pedir y **DETENER**.

---

# Paso 10 — Cover letter, paquete final y refresh gate de 24 h

**Objetivo.** Enviar una sola vez, sin ningún incumplimiento conocido.

**Necesita.** Todo lo anterior; `FINAL_PRE_SUBMISSION_GATE.md`; los campos reales del sistema de
submission del journal.

**Hacer.**
1. **Cover letter** corta y estratégica: 1 párrafo (problema + resultado central); **máx. 3 bullets**
   de novedad a nivel teorema; 1 párrafo de por qué le importa a los lectores del journal **fuera** del
   caso ecológico; 1 párrafo de relación con el companion, con frontera exacta y sin ambigüedad de
   autoría; confirmaciones de open access / exclusividad / permisos; reviewers sugeridos solo si
   ayudan y no tienen conflicto. **Prohibido:** "agregamos muchas simulaciones", "extendimos N páginas".
   Mensaje central: *la revisión no es cosmética; el paper ahora formula y demuestra un límite general
   de discriminación de mecanismos hereditarios bajo horizonte finito y excitación acotada, con una
   aplicación certificada donde la seguridad vuelve el límite operacionalmente relevante.*
2. **Armar el paquete:** `main.tex`/`main.pdf` sobre el template oficial; `supplement.tex`/`.pdf`;
   cover letter; `NOVELTY_MATRIX.md`; `CLAIM_EVIDENCE_LEDGER.md`; `OVERLAP_PROVENANCE_AUDIT.md`;
   `JOURNAL_COMPLIANCE_MATRIX.md`; `REPRODUCIBILITY.md`; código reproducible; figuras separadas;
   auditoría bibliográfica; reporte de clean build; ZIP final; los tres informes de mock review.
3. **Refresh gate, 24 h antes de enviar:** reabrir las instrucciones oficiales; volver a descargar el
   template; comparar versión/fecha/SHA si es posible; recorrer el checklist completo; inspeccionar
   los campos reales del sistema de submission; comprobar si apareció algún statement obligatorio
   nuevo; **regenerar el PDF desde una carpeta limpia**.

**Entregable.** ZIP de submission + `SUBMISSION_READY.md` con el estado de los gates G0–G8.

**Gate 10 (G0–G8, todos GREEN).** G0 scope explicado · G1 cada contribución con su prior-work más
cercano y diferencia demostrable · G2 al menos una contribución central existe fuera del caso
strong-Allee · G3 los teoremas headline sobreviven la auditoría adversarial · G4 sin dependencia
matemática de un companion no publicado · G5 reproducibilidad y auditorías numéricas en PASS · G6
título/abstract/introducción comunican novedad antes que provenance y limitaciones · G7 100% de los
obligatorios + ≥99% del checklist total, con template e instrucciones refrescados dentro de las 24 h ·
G8 el paquete compila desde cero con metadata, bibliografía y figuras correctas.
**Sin G0–G8 en GREEN no se envía.**

**Cómputo.** Solo el clean build final (LaTeX) ⇒ lo hacés vos. Regenerar resultados numéricos ⇒ pedir
y **DETENER**.

---

# Prohibiciones explícitas (del plan fuente)

- No reenviar esencialmente el mismo paper con cambios de template.
- No "resolver" el rechazo agregando 6–8 páginas.
- No aumentar el número de figuras.
- No poner más disclaimers sobre el companion en el abstract.
- No afirmar generalidad sin un teorema general.
- No esconder la matemática principal en el supplement.
- No tratar un no-cruce numérico como prueba de seguridad.
- No usar el template final publicado en lugar del template de **submission**.
- No fijar el journal antes de saber qué paper existe.
- No enviar con una sola desviación obligatoria conocida.
