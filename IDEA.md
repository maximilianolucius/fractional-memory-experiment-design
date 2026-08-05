# IDEA — fractional-memory-experiment-design

> Brief AUTORITATIVO. El CHIEF lo lee integro en el primer turno y rige TODO el proyecto.
> Este brief NO es una plantilla: el operador cargo un PACK MATEMATICO COMPLETO y verificado.
> Ese pack manda. Donde el pack contradiga a este brief, gana el pack.

## 0. Fuente de verdad (LEER ANTES DE ESCRIBIR NADA)

El material real del paper vive en el repo, ya cargado por el operador:

- `source_pack/` — PACK MATEMATICO COMPLETO (21 archivos). Es la reconstruccion rigurosa
  del paper. Orden de lectura recomendado el primer turno:
  1. `source_pack/README.md` — respuesta directa, identidad del paper, mapa de archivos.
  2. `source_pack/THEOREM_INDEX.md` — inventario de los 27 resultados con su archivo.
  3. `source_pack/15_PAPER_BLUEPRINT_AND_CLAIM_MATRIX.md` — estructura del manuscrito,
     set de teoremas T1..T17, matriz de claims (permitido / requiere simulacion /
     requiere experimento real / PROHIBIDO), y contribucion minima publicable.
  4. `source_pack/02_MAIN_DRAFT_MATHEMATICAL_AUDIT.md` — los 16 errores del `main.pdf`
     viejo que NO se deben repetir (son las mismas trampas que hundieron al paper hermano).
  5. `source_pack/01_RESEARCH_POSITIONING.md` — la novedad defendible y el grafo de dependencia.
  6. `source_pack/16_IMPLEMENTATION_AND_VALIDATION_SPEC.md` — contrato de implementacion,
     tests unitarios analiticos, gates de aceptacion de resultados numericos.
  7. Los teoremas en detalle: `source_pack/03..14_*.md` (modelo controlado, algebra exacta
     del strong-Allee, controlabilidad/observabilidad, teoremas de discriminacion, mixturas
     exponenciales e imposibilidad, diseno optimo de input y de observacion, Fisher/orden,
     complejidad muestral, diseno seguro, extension Bayesiana no lineal, disenos ecologicos).
- Bibliografia y posicionamiento (raiz del repo, version EXTENDIDA — usar estas, no las cortas):
  `17_BIBLIOGRAPHY.md` (bib verificada, ~60 refs con DOI + regla de uso por claim),
  `18_CITATION_MAP.md` (mapa claim -> citas), `19_BIBLIOGRAPHIC_AUDIT.md` (que citas del
  `main.pdf` viejo se eliminan/reemplazan), `20_RELATED_WORK_POSITIONING.md` (novedad vs prior art).
- `fractional-memory-experiment-design_PROPOSAL.md` (== `source_pack/00_SOURCE_PROPOSAL.md`):
  el proposal original. Su MOTIVACION y taxonomia sirven; sus formulas se subordinan al pack.

## 1. Identidad del paper (YA DECIDIDA por el pack — no reabrir)

- Tipo: paper TEORICO dirigido por teoremas (optimal experimental design) CON un benchmark
  de simulacion controlado y reproducible. NO es un paper puramente empirico ni una perspective.
- Titulo recomendado: **Optimal Excitation for Distinguishing Fractional, Delayed, and Latent
  Ecological Memory**.
- Companion de `fractional-memory-identifiability`. Aquel caracterizo CUANDO los datos pueden
  distinguir memoria fraccionaria; este responde COMO EXCITAR Y OBSERVAR el sistema para que la
  distincion sea posible. Usa el modelo predador-presa strong-Allee CERTIFICADO (del paper de
  dinamica validado) como digital twin, NO re-certifica dinamica.

## 2. Columna vertebral matematica (las tres capas)

1. Separacion estructural exacta (ideal, banda-ancha, sin ruido): una funcion de transferencia
   Caputo de orden no entero NO es igual a ninguna transferencia racional finito-dimensional
   (latente) ni a una de retardo finito (DDE). (T4, T5, T6 en `06_*`.)
2. Barrera de aproximacion en horizonte finito: el kernel fraccionario ES una mixtura continua
   de exponenciales (T7, `07_*`); se aproxima por sumas exponenciales finitas con cota L1 explicita
   (T9); por lo tanto con dimension latente NO acotada existe un modelo latente por debajo de
   cualquier piso de ruido (no-free-lunch, T10) -> el problema es mal-puesto sin restriccion.
3. Separacion activa optima: dada una clase restringida de alternativas, limites de actuador,
   costo de observacion y piso de ruido, se optimizan input y muestreo (eigenvector principal del
   operador diferencia, T11; diseno espectral robusto de soporte finito P+1, T12; tiempos de
   muestreo optimos, T13) para maximizar KL / informacion mutua / minima separacion pareada robusta.

## 3. Set de teoremas (todos ya PROBADOS o DERIVADOS en el pack — hay que redactarlos, no re-inventarlos)

T1 equilibrio de coexistencia y Jacobiano exactos; T2 traza/det/discriminante y alpha*(A);
T3 controlabilidad/observabilidad por canal (prey-only y predator-only bastan); T4 Caputo != racional
finito; T5 Caputo != DDE finito; T6 firma de fase/amplitud en alta frecuencia (gap (1-alpha)pi/2);
T7 representacion exponencial continua exacta; T8 no hay aproximacion uniforme en t=0; T9 aproximacion
L1 finita constructiva; T10 no-free-lunch con latente no acotado; T11 input optimo pareado
(eigenvector principal); T12 diseno espectral robusto de soporte finito; T13 tiempos de muestreo
optimos; T14 sensibilidades de orden fraccionario / Fisher; T15 error Gaussiano exacto y complejidad
muestral (replicas); T16 existencia de perturbacion segura e informativa; T17 rectangulo invariante
inward-pointing (seguridad). Ubicaciones exactas en `source_pack/THEOREM_INDEX.md`.

## 4. MVP: empezar por lo restringido y bien-puesto

Cuatro modelos: M_ODE, M_Caputo, M_DDE, M_latente con DIMENSION LATENTE MAXIMA m FIJA Y EXPLICITA.
Modelo strong-Allee certificado, orden comun alpha, dos canales de intervencion (prey / predator),
tres regimenes de observacion (prey-only, predator-only, ambas). NO arrancar con orden distribuido ni
kernels aprendidos sin restriccion: sin tope de complejidad la discriminacion es mal-puesta (T10).
Baseline justo y estable para frequency-response: A=1/4 (ODE y todo 0<alpha<=1 localmente estables);
baseline de veredicto de estabilidad (stress-test): A=3/10, alpha*=0.9690122761517084.

## 5. Matriz de claims (respetar sin excepcion — ver `15_*` seccion "Claim matrix")

- Permitido tras analisis solo: formulas exactas del modelo y frontera de estabilidad; no-equivalencia
  estructural bajo el canal directo; aproximacion finita e imposibilidad; teoremas de optimalidad para
  modelos lineal-Gaussianos fijos; existencia de seguridad y condiciones barrera suficientes.
- Requiere ARTEFACTOS DE SIMULACION: que forma de onda gana bajo un presupuesto; tasas de confusion;
  recuperacion/cobertura de alpha/tau/tasas latentes; robustez a ruido y priors; costo computacional.
- Requiere EXPERIMENTOS REALES: evidencia ecologica de memoria fraccionaria genuina; factibilidad de
  laboratorio; validez externa; interpretacion biologica de alpha.
- PROHIBIDO escribir (fueron los errores del `main.pdf` viejo): "un alpha<1 ajustado prueba memoria
  biologica"; "una gamma con tasa ->0 converge a power-law"; "un sistema Caputo no lineal se vuelve ODE
  con t->t^alpha"; "la estabilidad de orden distribuido depende solo del orden medio"; "ordenes por
  componente usan cunas de Matignon independientes"; "un cruce de Matignon crea un ciclo limite" en la
  clase Caputo autonoma estandar; y CUALQUIER numero empirico no generado por el pipeline liberado.

## 6. Reglas duras (precondiciones de cada turno)

- El manuscrito se escribe en INGLES, un solo idioma, sin anotaciones internas ni texto corrupto.
  Los archivos operativos (research_state.md, assignments/CURRENT.md, worker_reports) pueden ir en
  espanol. Escribir research_state.md y assignments/CURRENT.md SIN backslashes (evita corrupcion del relay).
- Tras CUALQUIER edicion el paper DEBE seguir compilando: `paper/main.pdf`, build exit 0. Es PRECONDICION.
- Honestidad: lo que el loop NO pueda ejecutar de verdad (simulaciones a gran escala, reproduccion por
  terceros en entorno limpio) -> producir la ESPECIFICACION + intento best-effort y marcarlo
  PENDING-HUMAN. NO inventar numeros. NO declarar "proved"/"probado" lo que no este demostrado.
- Reproducibilidad: todo resultado numerico entra al paper solo si pasa los gates de
  `source_pack/16_*` (config+seed guardados, tests analiticos pasan, refinamiento de solver dentro de
  tolerancia, re-simulacion independiente, cada tabla/figura generada desde artefactos, cero numeros a mano).
- Citas: cada afirmacion con la cita correcta segun `18_CITATION_MAP.md`; nunca una fuente fuera de su
  alcance; usar `[[CITE-NEEDED: claim exacto]]` antes que inventar una referencia.
- Novedad: NO afirmar "primer OED para sistemas fraccionarios" (FOED01-FOED04 ya existen). La novedad es
  la de `20_*` seccion 2: discriminacion activa y segura entre memoria Caputo/DDE/latente ecologica, con
  separacion exacta, barrera de horizonte finito y diseno optimo alrededor de un equilibrio certificado.

## 7. Preguntas centrales que el paper responde

1. Que perturbacion (pulso, tren multiescala log-espaciado, chirp, multiseno robusto, adaptativa) separa
   mejor Caputo de DDE y latente, bajo presupuesto de energia y restriccion de seguridad.
2. Que variables observar y a que tiempos (colocado alta-tasa en el pulso; cruzado a menor tasa;
   covariable ambiental solo cuando la condicion PBH del modo latente es debil).
3. Cuantas replicas / que horizonte para una probabilidad de error objetivo (T15).
4. Como se rompe el confounding memoria-fraccionaria vs latente/retardo/ruido-coloreado/deriva.
5. Protocolo reproducible de diseno + criterio go/no-go de seguridad antes de recoleccion costosa.
