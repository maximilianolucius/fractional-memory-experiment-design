# Plan de trabajo para levantar el desk rejection
## Manuscrito: *Safe active discrimination of fractional, delayed, and finite latent memory in a strong-Allee predator–prey model*

**Fecha del plan:** 2026-08-24  
**Objetivo:** convertir el manuscrito rechazado editorialmente en una versión **theorem-first, self-contained, claramente novedosa, reproducible y prácticamente impecable para el journal objetivo**, atacando de forma explícita las tres dimensiones mencionadas por el editor: **discipline/scope, novelty y general significance**.

> **Regla de submission:** no enviar la nueva versión hasta que alcance **100% de cumplimiento de todos los requisitos obligatorios** y **≥99% de cumplimiento del checklist total vigente del journal objetivo**. Las instrucciones y el template deben verificarse de nuevo inmediatamente antes de la submission.

---

# 1. Diagnóstico que guía el rescate

El rechazo recibido es un **desk rejection**, no un rechazo posterior a peer review. El editor no reportó un error matemático específico; la señal principal es que el manuscrito no convenció suficientemente en el screening de **novelty/general significance**.

La versión actual tiene varios puntos fuertes —cuatro resultados analíticos, validación numérica, benchmark amplio, fractional-delay bridge y un safety–informativeness trade-off—, pero la presentación editorial permite una lectura menos favorable:

1. El paper puede parecer **primero computacional/aplicado y recién después matemático**.
2. Los resultados más generales no están suficientemente elevados a una tesis matemática de alcance amplio.
3. El ecological backbone y el companion paper aparecen demasiadas veces en el abstract, Introduction y Discussion.
4. El manuscrito enfatiza repetidamente qué **“no es nuevo”**, justo en las páginas donde el editor decide si hay novelty.
5. En el main paper hay aproximadamente **19 figuras + 11 tablas en 21 páginas, frente a 4 teoremas principales**, y las pruebas completas están mayormente relegadas al Supplementary Material. Visualmente puede percibirse como un benchmark/case study con teoría de soporte.
6. El formato actual **imita** AIMS mediante `aims_math_style.sty`, pero no está montado directamente sobre el template TeX oficial.
7. Hay desviaciones concretas de las instrucciones vigentes de AIMS Mathematics: line numbers, sentence case, bibliografía, contacto del corresponding author, encabezado exacto de Generative-AI, etc.
8. Hay una inconsistencia de provenance que debe eliminarse: el manuscript es de Ibrahim Alraddadi, mientras que `P01` figura bibliográficamente con Maximiliano Lucius, pero el texto usa repetidamente “our previously submitted companion paper”.

**Conclusión estratégica:** no alcanza con “mejorar redacción” o “agregar páginas”. Hay que **cambiar la jerarquía científica del paper**: de *ecological computational discrimination study* a *general finite-horizon impossibility / discrimination theory with a certified strong-Allee application*.

---

# 2. North-star scientific claim

La nueva versión debe poder ser resumida por un editor, después de leer solamente título + abstract + primeras 1.5 páginas, aproximadamente así:

> **Fractional, delayed and finite-latent memory mechanisms can be structurally distinct while becoming statistically indistinguishable on finite horizons under bounded excitation; imposing a state-safety constraint can tighten this impossibility. The paper proves this phenomenon in a general hereditary-system framework and then certifies it in a strong-Allee predator–prey model.**

La aplicación ecológica debe ser importante, pero **no debe ser la única fuente de general significance**.

---

# 3. Workstream A — reconstruir la novelty matemática

## A1. Crear una `NOVELTY_MATRIX.md`

Antes de reescribir, hacer una búsqueda bibliográfica adversarial y actualizada de los trabajos más cercanos en:

- fractional system identification;
- fractional vs delay model discrimination;
- diffusive / exponential-sum approximation of fractional kernels;
- rational approximation of fractional transfer functions;
- finite-horizon identifiability;
- minimax hypothesis testing for dynamical systems;
- active model discrimination;
- safe experiment design / safe identification;
- safety-constrained information acquisition;
- predator–prey fractional-delay systems.

Para cada paper cercano registrar:

| Campo | Contenido |
|---|---|
| Citation | paper |
| Model class | fractional / delay / latent / nonlinear |
| Structural identifiability | sí/no |
| Finite-horizon approximation | sí/no |
| Explicit complexity budget \(m\) | sí/no |
| Statistical lower bound | sí/no |
| Uniform over bounded inputs | sí/no |
| State-safety constraint | sí/no |
| Rigorous certificate | sí/no |
| What they prove | resultado exacto |
| What we add | diferencia verificable |

**Gate A1:** ninguna novelty claim debe sobrevivir si ya existe esencialmente en literatura previa. La Introduction debe citar al competidor más cercano, no al más conveniente.

---

## A2. Generalizar los cuatro resultados actuales

La Section 3 no debería titularse “Analytical backbone: Four results used by the experiments”. Esa frase subordina la matemática a la simulación.

Reestructurarla como una sección central de teoría, por ejemplo:

**“Finite-horizon discrimination limits for hereditary mechanisms”**

Objetivo de arquitectura:

### Theorem A — Exact structural non-equivalence

Formular el resultado de separación de forma independiente del predator–prey model, para una clase bien definida de sistemas linealizados/hereditarios con entrada y observación.

Debe quedar perfectamente especificado:

- clase fractional;
- clase rational/finite-state latent;
- clase retarded-delay admitida;
- dominio analítico común;
- condición \(CB\neq0\);
- qué significa igualdad exacta;
- casos excluidos.

**Auditoría adversarial obligatoria:** buscar contraejemplos cuando \(CB=0\), canales no collocated, cancellation, improper transfer functions, múltiples delays y observaciones parciales.

---

### Theorem B — Quantitative finite-horizon approximation

La versión actual prueba/explota que una mezcla positiva de exponenciales aproxima el kernel de Caputo en \(L^1(0,T)\).

**Upgrade prioritario:** intentar pasar de mera existencia a un resultado **cuantitativo**:

\[
m \ge m(\varepsilon,T,\alpha,\ldots)
\quad\Longrightarrow\quad
\|k_\alpha-k_m\|_{L^1(0,T)}\le\varepsilon.
\]

Idealmente obtener una tasa explícita, o al menos upper/lower bounds útiles en \(m\).

Eso transforma “a latent model can approximate” en una **complexity law**.

---

### Theorem C — Uniform finite-experiment testing obstruction

Unificar aproximación + input budget + noise en un theorem general.

Objetivo conceptual:

\[
E_m\to0
\quad\Rightarrow\quad
\inf_{\text{tests}}
P_e(m,u)
\to \frac12
\]

**uniformemente sobre los inputs admisibles** con un budget especificado, con constantes derivadas rigurosamente para el observation model utilizado.

No fijar la fórmula final antes de reauditar los factores de:

- sampling;
- noise covariance;
- number of observations;
- observation operator;
- \(L^1/L^2\) convolution bounds;
- KL / total variation / Pinsker;
- equal vs unequal priors.

**Gate A2:** la versión final del theorem debe indicar explícitamente qué es uniforme, respecto de qué clase de experimentos, y qué depende de \(m,T,\sigma,U,C_{\rm obs}\).

---

### Theorem D — Safety-constrained information ceiling

Éste puede convertirse en la mejora más importante del paper.

Actualmente el safety–informativeness trade-off es parcialmente numérico. Intentar demostrar un resultado que conecte:

1. una condición de seguridad del estado, por ejemplo  
   \[
   x(t)\ge A+\delta,
   \]
2. una restricción suficiente sobre la clase de perturbaciones seguras;
3. un upper bound sobre la separación observable / información disponible;
4. el lower bound de error de Theorem C.

La meta es obtener un statement del tipo:

> **Safety restricts the admissible excitation set; under this restriction, sufficiently rich latent rivals cannot be uniformly discriminated from fractional memory on a finite horizon.**

Si se prueba, debe convertirse en uno de los resultados headline.

Si **no** puede probarse con suficiente generalidad, no venderlo como theorem: mantenerlo como certified/numerical phenomenon y ajustar el journal target.

---

## A3. Convertir la ecología en corolario/aplicación

El strong-Allee model debe aparecer como:

- una aplicación no trivial;
- un sistema donde el safety constraint tiene significado dinámico real;
- un test bed certificado;
- una demostración de que el theorem general produce números concretos.

La lógica narrativa debe ser:

\[
\text{general theorem}
\rightarrow
\text{safe hereditary discrimination framework}
\rightarrow
\text{strong-Allee specialization}
\rightarrow
\text{certified numerical consequences}.
\]

No al revés.

---

## A4. Llevar las pruebas importantes al main paper

Actualmente se declara que las “complete proofs” están en Supplementary Material.

Para un journal matemático y un desk rejection por novelty/significance:

- dejar en el **main paper las pruebas completas de los teoremas headline**, o al menos todas las partes intelectualmente no estándar;
- mover al supplement derivaciones repetitivas, tablas extensas, solver details, grid inventories y secondary lemmas.

**Principio:** el editor/referee no debe tener que abrir un suplemento para descubrir por qué el paper es matemáticamente importante.

---

# 4. Workstream B — reconstruir la narrativa editorial

## B1. Nuevo título

El título debe ser **sentence case** y debe front-load el resultado, no sólo la aplicación.

Candidatos a explorar:

1. **Finite-horizon limits of discriminating fractional, delayed and latent memory under safety constraints**
2. **When fractional memory is structurally identifiable but experimentally indistinguishable**
3. **Safe discrimination of hereditary mechanisms under bounded experiments: Fractional, delayed and latent memory**

El strong-Allee system puede quedar en subtítulo o en la última parte del título si el journal privilegia aplicaciones.

---

## B2. Nuevo abstract: 180–240 palabras

Objetivo:

- 1 frase: problema general;
- 1–2 frases: theorem-level novelty;
- 1 frase: safety consequence;
- 1–2 frases: strong-Allee certified application;
- 1 frase: significance.

**Reducir drásticamente** la cantidad de cifras del abstract. Mantener sólo 2–4 números indispensables.

Eliminar del abstract:

- “inherited”;
- “not claimed as new”;
- narrativa del companion paper;
- inventario exhaustivo de grids;
- exceso de métricas benchmark.

La provenance se maneja correctamente en Introduction + cover letter, no consumiendo el novelty budget del abstract.

---

## B3. Rehacer las primeras 1.5 páginas

La Introduction debe responder de inmediato:

1. **What is the mathematical problem?**
2. **What was previously unknown?**
3. **What theorem do we prove?**
4. **Why does it matter beyond predator–prey ecology?**
5. **Why is the strong-Allee application a hard/useful specialization?**

Eliminar del main introduction la tabla actual **“Relationship between the previously submitted companion paper and the present manuscript”**.

Esa tabla cumple una función defensiva, no científica. Sustituirla por **un único párrafo conciso de provenance** y trasladar el detalle a:

- cover letter;
- related-paper disclosure interno;
- eventualmente Supplementary Material si el journal lo requiere.

---

## B4. “Main contributions” con claims falsables

Reescribir las contribuciones como 3–4 claims verificables, evitando listas de actividades.

Evitar:

- “we simulate…” como contribución principal;
- “we benchmark…” como headline;
- “we provide figures…”;
- “we study…” sin resultado.

Preferir:

- “We prove…”
- “We derive…”
- “We certify…”
- “We show that no admissible experiment can… under…”
- “We obtain an explicit complexity-dependent bound…”

---

# 5. Workstream C — resolver completamente provenance, overlap y self-containment

## C1. Corregir la inconsistencia “our companion paper”

El manuscript actual tiene un único autor, Ibrahim Alraddadi, mientras `P01` aparece con Maximiliano Lucius.

No usar “our previous paper” salvo que la autoría/provenance realmente lo justifique.

Usar una formulación factual, por ejemplo:

> “The ecological backbone follows the companion study [X]…”

y explicar exactamente qué material se reutiliza.

---

## C2. Hacer el paper autosuficiente

El lector debe poder verificar todos los resultados del paper **sin depender de un manuscript no publicado/companion**.

Reproducir en forma autocontenida:

- ecuaciones necesarias;
- parámetros;
- equilibrium;
- Jacobian;
- stability assumptions usadas;
- cualquier lemma indispensable.

Citar el trabajo previo por provenance, pero no usarlo como un missing proof dependency.

---

## C3. Auditoría de similarity / iThenticate

Antes de submission:

- comparar contra el companion;
- identificar coincidencias de ecuaciones inevitables;
- reescribir texto descriptivo reutilizado;
- etiquetar correctamente cualquier material idéntico;
- auditar captions, methods y ecological-backbone descriptions.

No perseguir ciegamente un porcentaje arbitrario: cada coincidencia material debe ser **explicable y legítima**.

Crear:

**`OVERLAP_PROVENANCE_AUDIT.md`**

con:

- shared equations;
- shared parameters;
- shared figures (idealmente ninguno salvo necesidad);
- shared text;
- justification;
- citation/disclosure location.

---

# 6. Workstream D — fortalecer la evidencia numérica sin convertir el paper en un informe

## D1. Reducir la densidad visual del main paper

La versión actual tiene aproximadamente:

- **19 figuras**;
- **11 tablas**;
- **4 teoremas principales**;
- **21 páginas**.

Para un paper que quiere ser percibido como matemáticamente significativo, invertir esa señal editorial.

Target orientativo —no requisito del journal—:

- 7–10 figuras principales;
- 4–7 tablas principales;
- resto al Supplement.

Candidatos típicos para Supplement:

- workflow figure;
- model-family schematic redundante;
- waveform gallery completa;
- grids secundarios;
- repeated delay-sweep visualizations;
- detailed solver convergence;
- extra parameter panels.

Mantener en main sólo las figuras que **demuestran una claim central**.

---

## D2. Reproducibilidad fuerte

Crear un clean-run que:

1. parte de un checkout/zip limpio;
2. recrea numerical results;
3. recrea figures/tables;
4. compila main + supplement;
5. verifica hashes o tolerancias numéricas;
6. reporta environment/dependencies.

Entregables:

- `REPRODUCIBILITY.md`
- `requirements.txt` / environment lock
- `run_all.py` o `make all`
- seed policy
- numerical tolerance policy
- machine-independent sanity tests

---

## D3. Statistical audit

Auditar:

- BIC implementation;
- number of effective observations;
- likelihood normalization;
- class priors;
- parameter fitting per candidate model;
- fairness of model complexity penalties;
- confidence intervals / Monte Carlo uncertainty;
- sensitivity to SNR;
- sensitivity to horizon;
- sensitivity to sampling cadence;
- sensitivity to latent budget \(m\).

Agregar error bars / uncertainty sólo donde cambien la interpretación.

---

## D4. Safety audit

Separar con absoluta claridad:

- **rigorous safety certificate**;
- **sufficient analytical condition**;
- **numerical non-crossing diagnostic**;
- **observed crossing rate**.

Nunca llamar “safe” a una celda basándose sólo en una simulación si el statement pretende ser riguroso.

---

# 7. Workstream E — cumplimiento ≥99% del journal objetivo

## Regla de oro

**El día de preparar la submission se vuelven a descargar/releer las instrucciones y el template oficiales.**

No trabajar de memoria.

### Source of truth para AIMS Mathematics (verificado 2026-08-24)

- Submission Guidelines:  
  https://www.sciopen.com/journal/join_journal/submission_guidelines?id=1876451867993092098&issn=2473-6988
- AIMS Mathematics portal:  
  https://www.aimspress.com/math
- JAMS submission system:  
  https://aimspress.jams.pub/
- Usar el enlace **“Tex Template”** de las Submission Guidelines para obtener el template vigente.

Si el journal final cambia, reemplazar estos documentos por los del journal elegido y repetir el audit desde cero.

---

## E1. Definición operativa de “99% compliant”

### Requisitos obligatorios
**100% PASS. Cero excepciones conocidas.**

### Checklist total
\[
\text{Compliance score}=
\frac{\text{items PASS}}{\text{items aplicables}}
\ge 0.99.
\]

Una desviación sólo puede existir si:

- es meramente advisory/no obligatoria;
- está documentada;
- no afecta peer review, metadata, referencias, ética, AI, figuras o producción.

Crear:

**`JOURNAL_COMPLIANCE_MATRIX.md`**

con columnas:

| Requirement | Official source | Mandatory? | Applicable? | Current status | Evidence/file | Fix | Final PASS |
|---|---|---:|---:|---|---|---|---|

---

## E2. AIMS Mathematics — checklist obligatorio actual

### Submission package

- [ ] Cover letter.
- [ ] Full text con Figures y Tables.
- [ ] Submission vía JAMS.
- [ ] Si se usa LaTeX, entregar el formato requerido y compilar desde el **template oficial vigente**.
- [ ] No usar `aims_math_style.sty` como sustituto del template oficial en la nueva versión.

### LaTeX / referee usability

- [ ] Añadir `\usepackage{lineno}` y `\linenumbers` según la instrucción vigente/template.
- [ ] Clean compile sin warnings relevantes.
- [ ] No broken references/citations.
- [ ] Todas las ecuaciones y símbolos visibles correctamente.

### Title

- [ ] Conciso e informativo.
- [ ] **Sentence case**.
- [ ] Capitalización correcta después de colon.
- [ ] Grammar/articles revisados.

### Authors and affiliations

- [ ] Full author names.
- [ ] Superscript affiliations.
- [ ] Department, organization, city, country.
- [ ] Corresponding author con `*`.
- [ ] **Exact contact address**.
- [ ] Email.
- [ ] **Telephone number**.

### Headings

- [ ] Máximo 4 niveles.
- [ ] Sentence case.
- [ ] Typography exactamente según template/instrucciones vigentes.

### Abstract / keywords

- [ ] Abstract <300 words.
- [ ] Context/purpose.
- [ ] Method sin exceso de detalle.
- [ ] Main findings.
- [ ] Significance.
- [ ] Sin citations.
- [ ] Abbreviations minimizadas.
- [ ] 5–10 keywords.

### Body

- [ ] Body font/spacing exactamente según template/instrucciones.
- [ ] List of abbreviations antes de Introduction si corresponde.
- [ ] SI units.
- [ ] Introduction.
- [ ] Materials and methods / equivalente apropiado para paper matemático.
- [ ] Results.
- [ ] Discussion.
- [ ] Conclusions.

### End matter

- [ ] Author contributions.
- [ ] Para múltiples autores: CRediT roles.
- [ ] Heading exacto: **“Use of Generative-AI tools declaration”**.
- [ ] Declaración Generative-AI coherente con el uso real.
- [ ] Generative-AI declaration **antes de Acknowledgments**.
- [ ] Acknowledgments.
- [ ] Funding disclosure, incluso si es “no external funding” si el template lo solicita.
- [ ] Conflict of interest.
- [ ] Data availability statement si el template/journal lo pide o si es apropiado para el computational package.

### References

- [ ] Numeradas en **orden de primera citación**, no alfabéticamente.
- [ ] Citations en square brackets.
- [ ] Bibliografía finalizada antes de submission.
- [ ] Journal names en abreviatura ISO 4.
- [ ] Máximo primeros 6 autores + “et al.” cuando corresponda.
- [ ] DOI cuando corresponda.
- [ ] Formato journal article/book/online según AIMS.
- [ ] Verificar el status de cada preprint/unpublished reference frente a la política vigente.
- [ ] Reemplazar preprints por versiones peer-reviewed cuando existan.
- [ ] Auditar especialmente `P01`, `SAFE26A` y `SAFE26B`.
- [ ] Eliminar `\bibliographystyle{plain}` y usar el mecanismo compatible con el template/style oficial.

### Figures and tables

- [ ] Figures insertadas en main text.
- [ ] También entregadas como files separados.
- [ ] EPS/PNG/PDF/JPEG.
- [ ] ≥300 dpi cuando raster.
- [ ] RGB.
- [ ] Figuras llamadas en orden.
- [ ] Tablas llamadas en orden.
- [ ] Figure caption debajo.
- [ ] Table caption arriba.
- [ ] Permissions para cualquier material reutilizado.
- [ ] Fonts/labels legibles al tamaño final.

### Supplement

- [ ] Sólo material verdaderamente secundario.
- [ ] Main claims no dependen de proofs escondidas.
- [ ] Cross-references correctas.
- [ ] Code/data/software claramente vinculados.

---

## E3. Refresh gate antes de enviar

**24 horas antes de la submission:**

1. abrir nuevamente las instrucciones oficiales;
2. descargar nuevamente el template;
3. comparar SHA/date/version si es posible;
4. recorrer todo el checklist;
5. inspeccionar los campos reales de JAMS;
6. comprobar si apareció algún nuevo mandatory statement;
7. re-generar PDF desde un folder limpio.

**No submission si el checklist no está GREEN.**

---

# 8. Workstream F — bibliography y literature positioning

La bibliografía actual usa:

```latex
\bibliographystyle{plain}
```

Eso ordena alfabéticamente y no cumple el esquema actual de AIMS de numeración por orden de citación.

Acciones:

1. Migrar completamente al bibliography style soportado por el template oficial.
2. Reordenar citations por primera aparición.
3. DOI audit.
4. ISO-4 journal abbreviation audit.
5. Verificar que cada reference respalde exactamente la claim donde se usa.
6. Actualizar literature 2024–2026.
7. Sustituir referencias preprint por artículos publicados si ya existen.
8. No usar el companion como sustituto de literatura primaria.
9. Incluir papers que podrían competir con la novelty claim, aunque sean incómodos.

**Gate F:** un referee especialista no debería poder decir “the authors ignore the closest literature”.

---

# 9. Workstream G — cover letter diseñada contra el desk rejection

La cover letter nueva debe ser corta y estratégica.

Estructura:

1. **1 paragraph:** problema y resultado central.
2. **3 bullets máximo:** theorem-level novelty.
3. **1 paragraph:** por qué importa a lectores del journal, fuera del ecological case.
4. **1 paragraph:** relación con companion work, con boundary exacta y sin ambigüedad de autoría.
5. Open-access/exclusivity/permissions confirmations exigidas.
6. Suggested reviewers sólo si ayudan y cumplen conflictos.

No mencionar defensivamente “we added many simulations” o “we extended by N pages”.

Mensaje central:

> La revisión no es cosmética; el paper ahora formula y demuestra un límite general de discriminación de mecanismos hereditarios bajo horizonte finito/bounded excitation, con una aplicación certificada donde safety vuelve el límite operacionalmente relevante.

---

# 10. Workstream H — adversarial pre-review

Antes de submission, hacer tres mock reviews separados.

## H1. Mock editor — 90 segundos

Dar sólo:

- title;
- abstract;
- first 1.5 pages;
- conclusion.

Preguntas:

- ¿Cuál es la novelty en una frase?
- ¿Cuál es el theorem central?
- ¿Por qué es general?
- ¿Por qué encaja en el journal?
- ¿Qué cambia respecto de literatura previa?

Si el mock editor no responde correctamente sin ayuda, **FAIL**.

---

## H2. Mock mathematical referee

Atacar:

- assumptions;
- branch cuts;
- analytic domains;
- high-frequency asymptotics;
- approximation near \(t=0\);
- rate in \(m\);
- uniformity of testing bound;
- noise model;
- observation operator;
- safety theorem;
- use of Pinsker;
- interval arithmetic;
- reproducibility of certificates.

Objetivo: producir counterexamples antes que el referee real.

---

## H3. Mock applied/computational referee

Atacar:

- ecological interpretation;
- realism of perturbations;
- parameter sensitivity;
- fairness of model comparison;
- BIC;
- SNR;
- sampling;
- safety crossing;
- solver accuracy;
- fractional-delay implementation;
- latent model calibration.

---

# 11. Nueva arquitectura recomendada del manuscript

Una estructura posible:

1. **Introduction**
   - scientific gap;
   - closest prior work;
   - theorem-level contributions;
   - one concise provenance paragraph.

2. **General hereditary discrimination framework**
   - input/output model;
   - admissible fractional/delay/latent classes;
   - finite horizon;
   - noise;
   - safety set.

3. **Structural separation and finite-horizon approximation**
   - Theorem A;
   - Theorem B;
   - proofs.

4. **Statistical limits under bounded and safe excitation**
   - Theorem C;
   - candidate Theorem D;
   - proofs.

5. **Strong-Allee specialization**
   - model;
   - operating point;
   - safety geometry;
   - certified surrogate construction.

6. **Numerical methods and validation**

7. **Fractional-delay and active-design results**

8. **Model-discrimination benchmark**
   - fewer but stronger figures.

9. **Discussion**

10. **Conclusions**

11. **Author contributions**

12. **Use of Generative-AI tools declaration**

13. **Acknowledgments / Funding**

14. **Data availability**

15. **Conflict of interest**

16. **References**

17. **Supplementary material**

---

# 12. Qué NO hacer

- No reenviar esencialmente el mismo paper con cambios de template.
- No “resolver” el rechazo agregando 6–8 páginas.
- No aumentar el número de figuras.
- No poner más disclaimers sobre el companion en el abstract.
- No afirmar generality sin un theorem general.
- No esconder la matemática principal en Supplement.
- No tratar un numerical non-crossing como safety proof.
- No usar el template final publicado como sustituto del **submission template**.
- No fijar el journal primero y forzar el paper si el perfil científico final no coincide.
- No enviar con una sola desviación obligatoria conocida de las instrucciones.

---

# 13. Decision gate sobre el journal

Después del Workstream A:

## Escenario 1 — se logra el theorem-level upgrade

Si se obtiene:

- theorem general de finite-horizon non-discrimination;
- explicit complexity dependence;
- y, preferentemente, safety-constrained bound;

entonces el paper puede apuntar nuevamente a un journal matemático general/applied-math de mayor exigencia.

## Escenario 2 — la teoría no se generaliza

Si el resultado central permanece:

- prey-channel-specific;
- largely numerical;
- BIC/benchmark-driven;
- sin un theorem general de safety/information;

entonces **no conviene venderlo como un paper de general mathematical significance**. Seleccionar un journal especializado en nonlinear/fractional dynamics, system identification o mathematical biology.

El journal debe elegirse por el **paper que finalmente exista**, no por el paper que queremos que exista.

---

# 14. Deliverables finales

El proyecto de rescate se considera terminado sólo si existen:

- `main.tex` sobre template oficial actual;
- `main.pdf`;
- `supplement.tex`;
- `supplement.pdf`;
- `cover_letter.md` / versión final requerida;
- `NOVELTY_MATRIX.md`;
- `CLAIM_EVIDENCE_LEDGER.md`;
- `OVERLAP_PROVENANCE_AUDIT.md`;
- `JOURNAL_COMPLIANCE_MATRIX.md`;
- `REPRODUCIBILITY.md`;
- source code reproducible;
- figures separadas;
- bibliography audit;
- clean-build report;
- final submission ZIP;
- mock-editor report;
- mock-referee reports.

---

# 15. Definition of done — GREEN gates

## G0 — Scope
El abstract y la cover letter explican claramente por qué el paper pertenece al journal.

## G1 — Novelty
Cada contribution tiene un closest-prior-work explícito y una diferencia demostrable.

## G2 — General significance
Al menos una contribución central existe fuera del strong-Allee case.

## G3 — Mathematical correctness
Los theorems headline sobreviven auditoría adversarial y counterexample search.

## G4 — Self-containment
No hay dependencia matemática crítica de un companion no publicado.

## G5 — Numerical credibility
Clean reproducibility + solver/statistical/safety audits PASS.

## G6 — Editorial presentation
Title/abstract/Introduction comunican novelty antes que provenance/limitations.

## G7 — Journal compliance
- **100% de mandatory requirements: PASS**
- **≥99% del checklist total aplicable: PASS**
- template e instrucciones refrescados dentro de las 24 h previas.

## G8 — Submission package
Compila desde cero, metadata completa, bibliography correcta, figures correctas, cover letter lista.

**Sólo con G0–G8 en GREEN se envía.**

---

# 16. Prioridad inmediata — primeras tareas

Orden recomendado:

1. **Congelar la versión rechazada** como baseline.
2. Crear `NOVELTY_MATRIX.md`.
3. Auditar y fortalecer Theorems A–D.
4. Intentar obtener explicit \(m\)-vs-\(\varepsilon\) complexity.
5. Intentar cerrar un safety-constrained information theorem.
6. Reescribir title + abstract + first 1.5 pages.
7. Eliminar la tabla de companion-paper de Introduction.
8. Resolver provenance/self-containment.
9. Reducir figuras/tablas del main y mover proofs principales al main.
10. Reauditar numerics/reproducibility.
11. Elegir journal final.
12. Descargar instrucciones/template **actuales** del journal final.
13. Migrar el source al template oficial.
14. Construir `JOURNAL_COMPLIANCE_MATRIX.md`.
15. Mock editor + dos mock referees.
16. Clean build final.
17. Compliance refresh 24 h antes de enviar.
18. Submission.

---

## Fuentes oficiales consultadas para el compliance AIMS

**Consultadas el 2026-08-24. Deben revalidarse antes de enviar.**

- AIMS Mathematics — Submission Guidelines:  
  https://www.sciopen.com/journal/join_journal/submission_guidelines?id=1876451867993092098&issn=2473-6988
- AIMS Mathematics:  
  https://www.aimspress.com/math
- JAMS submission portal:  
  https://aimspress.jams.pub/

La guía vigente exige, entre otros puntos, cover letter + full text, recomienda `lineno` para LaTeX, title/headings en sentence case, abstract <300 palabras, 5–10 keywords, estructura completa del manuscript, declaración **“Use of Generative-AI tools declaration”**, acknowledgments/funding, conflict of interest, referencias numéricas por orden de primera citación y figuras separadas de calidad adecuada.

---

**Strategic principle:** el objetivo no es “hacer que parezca AIMS”. El objetivo es que, científicamente, un editor vea una contribución matemática general y novedosa en menos de dos minutos, y que, técnicamente, no encuentre ningún motivo evitable para detener el manuscript antes del peer review.
