> WARN ====== ADDENDUM DEL OPERADOR — BENCHMARK NO-LINEAL v3 CALIBRADO-SEGURO YA DISPONIBLE [OP-BENCH-V3] ======
> ACTUALIZA la instruccion de la seccion 10 de OP-AUDIT-FIX (abajo): el benchmark no-lineal YA NO es
> "ilustrativo/sin calibrar". Se re-corrio en Orion (2026-08-05, v3) CALIBRADO Y SEGURO, cerrando P0.5/P0.6/P0.7/P0.9.
> Numeros REALES (usar exactamente; fuente: benchmark/results/nonlinear_confusion.json + artifacts/manifests/manifest.json):
>  - Rivales CALIBRADOS a un backbone comun (mismo equilibrio/Jacobiano; DDE tau=0.35 estable, latente acople 0.15);
>    input con TOPE DE AMPLITUD |u|<=0.10 (restriccion de seguridad, pack T8.2). n_diverged=0.
>  - Tarea PRINCIPAL memory-shape STABLE-ONLY (A en {0.20,0.25}, A<2/7): macro-accuracy 0.537, micro 0.491 (azar 0.25).
>    Recall por clase ODE 0.97 / Caputo 0.52 / DDE 0.41 / latent3 0.24; precision ODE 0.23 / Caputo 0.98 / DDE 0.73 / latent3 0.85.
>    Reportar matriz 5-clases y 4-clases (en el json). El latente-1 es el mas dificil (mimicry, no-free-lunch T10).
>  - Estratificado (stable): por alpha 0.70(a=0.7) -> 0.31(a=0.95); por SNR hi 0.76 / med 0.44 / lo 0.27; por canal both>prey>pred.
>  - Tarea VERDICT (A en {0.30,0.40}, A>2/7) reportada APARTE: macro 0.574 (detecta estabilidad, no forma de memoria).
>  - HALLAZGO DE SEGURIDAD (reportar con enfasis, con los margenes numericos min(x-A)): a igual amplitud, los diseños
>    TRANSITORIOS son SEGUROS pero debiles (multiscale: 0% cruce Allee, margen +0.29, pero es el PEOR discriminador 0.32;
>    pulse 7% cruce) y los diseños SOSTENIDOS/banda-ancha discriminan mejor pero son INSEGUROS (prbs/sinusoid 100% cruce Allee,
>    chirp 93%, multisine 36%). Es el TRADE-OFF seguridad-informatividad: la discriminacion SEGURA de memoria sutil es dificil,
>    lo que motiva el DISEÑO OPTIMO CON RESTRICCION DE SEGURIDAD (future work).
>  - El resultado computacional PRIMARIO sigue siendo la discriminacion lineal-Gaussiana EXACTA (linear_factorial.json,
>    ranking prbs>pulse>multiscale>multisine>sinusoid>chirp); el no-lineal v3 es la CONFIRMACION honesta (BIC / criterio de
>    informacion, NO Bayesiano implementado — mantener ese etiquetado de P0.3).
> manifest artifacts/manifests/manifest.json = status PASS (v3). Integrar TODO esto en la seccion 10 con honestidad;
> nada de "0.749" viejo (superseded). Compilar (main.pdf exit 0).
> ==========================================================================================
> WARN ====== DIRECTIVA DEL OPERADOR — RECONSTRUCCION SEGUN DICTAMEN DE REFEREE [OP-AUDIT-FIX] ======
> Un referee academico dicto RECHAZO + reconstruccion mayor. FUENTE DE VERDAD: leer COMPLETOS al inicio de
> cada tanda audits/PAPER_AUDIT.md, audits/MATHEMATICAL_REPAIR_NOTES.md, audits/PROPOSAL_COMPLIANCE_MATRIX.md.
> PROHIBIDO churn (turno de solo-contador = FALLIDO) y PROHIBIDO cerrar en falso. Cada item se cierra con
> evidencia (seccion editada + build main.pdf exit 0). Escribir research_state.md y assignments/CURRENT.md SIN backslashes.
>
> DECISION DE ALCANCE (Opcion A, la que recomienda el audit): el paper es DISCRIMINACION ESTRUCTURAL
> LINEALIZADA + benchmark no-lineal stable-only por criterio de informacion (BIC), descrito honestamente
> como frecuentista/IC (NO Bayesiano implementado). La capa Bayesiana secuencial completa (evidencia,
> EIG, adaptativo, SBC) y un benchmark no-lineal con rivales CALIBRADOS y diseños AMPLITUD-restringidos
> SEGUROS se declaran FUTURE WORK explicito. Retitular sin "definitive":
>   "Safe Active Discrimination of Fractional, Delayed, and Finite Latent Memory in a Strong-Allee Predator-Prey Model".
>
> P0 (bloqueantes, cerrar primero):
>  P0.1 Teorema 9.3 es FALSO (KL de la posterior esperada = 0 por tower property). Reemplazar por la
>       identidad de KL ESPERADA de MATHEMATICAL_REPAIR_NOTES seccion 6, y corregir Eq(67), discusion y
>       conclusion. Quitar el claim de que el greedy 1-paso "minimiza el numero de experimentos".
>  P0.2 Reconstruir el apendice (Seccion 14) TEOREMA POR TEOREMA; prohibido dos proofs incompatibles del
>       mismo resultado. Usar los reemplazos de MATHEMATICAL_REPAIR_NOTES (7.1 eigenvector u*=sqrt(E)v_max +
>       attainment/compacidad; 7.5 Caratheodory soporte finito + limitacion composite; 5.4 banda compacta;
>       8.4 desigualdad inward-pointing ESTRICTA con margen eta; 9.1 pasar a proposicion + caso lineal-Gaussiano).
>  P0.3 El benchmark usa BIC, NO el pipeline Bayesiano. Describirlo como IC-based; quitar todo claim de que
>       se implemento OED Bayesiano adaptativo/posterior-odds/EIG. Mover eso a future work.
>  P0.6 (metodo) Separar dos tareas: (A) MEMORY-SHAPE stable-vs-stable (A<2/7); (B) STABILITY-VERDICT (A>2/7)
>       como stress-test aparte. NO promediar ambas en un headline. Estratificar toda metrica por regimen.
>  P0.5/0.9 (HONESTIDAD CRITICA — resultado del operador en Orion 2026-08-05): el benchmark NO-LINEAL actual
>       tiene rivales NO CALIBRADOS (el DDE colapsa la presa a x~0 con cualquier energia) y diseños NO SEGUROS
>       (pulsos cruzan el umbral Allee: p.ej. a energia 0.03 el multiscale lleva min_x del ODE a 0.48 pero del
>       DDE a 0.06 con A=0.28). Por lo tanto: (i) el resultado COMPUTACIONAL PRIMARIO del paper pasa a ser la
>       DISCRIMINACION LINEAL-GAUSSIANA EXACTA (benchmark/results/linear_factorial.json: ranking de diseños por
>       min-pairwise-KL prbs>pulse>multiscale>multisine>sinusoid>chirp), que es rigurosa y segura por construccion
>       (linealizada, perturbacion local); (ii) el benchmark no-lineal BIC se presenta SOLO como ilustracion con
>       caveats explicitos (rivales sin calibrar, diseños sin restriccion de amplitud -> cruzan Allee), NO como
>       validacion del metodo; (iii) reportar la SEGURIDAD con MARGENES NUMERICOS (min(x-A), distancia a las caras
>       del rectangulo), no "divergencia 0"; el hallazgo honesto es que la discriminacion segura EXIGE diseños con
>       amplitud restringida (ceiling rho/Gamma_T), y eso queda como limitacion/future work.
>  P0.7 Reconciliar la matriz de confusion con el texto: ODE<->Caputo bidireccional = 290+20331 = 20621 (NO 34621);
>       fila Caputo = 81000 (NO 80854). Reportar matriz 5-clases (ODE,Caputo,DDE,latent1,latent3) Y 4-clases
>       colapsada, con su baseline de azar cada una, y metricas BALANCEADAS (macro-accuracy, recall/precision por clase).
>  P0.8 No afirmar "diseño teoricamente optimo validado": el benchmark compara familias heuristicas (PRBS, pulse,
>       multiscale, multisine, sinusoid, chirp), no computo el eigenvector principal ni resolvi el LP maximin.
>       Decir "las familias banda-ancha rindieron mejor en esta grilla". Incluir PRBS tambien en el no-lineal o
>       explicar su exclusion.
>  P0.10 Teorema 8.4: usar desigualdad inward-pointing ESTRICTA (margen eta>0) + condicion inicial interior + un
>       principio de extremo de Caputo bien citado (MATHEMATICAL_REPAIR_NOTES seccion 5).
>  P0.11 No-free-lunch: describir Corolario 6.6 como resultado LINEALIZADO de input FIJO; el salto a la clase
>       no-lineal exige la extension de Volterra/Gronwall (MATHEMATICAL_REPAIR_NOTES seccion 3) o se acota el claim.
>  P0.12 Bibliografia: regenerar desde BibTeX verificado (arreglar "Caputo and M." -> "Caputo, M.", ISBN/paginas
>       rotos, entrada Chaos malformada, Oikos duplicada) y MOVERLA AL FINAL (despues de conclusion y apendice).
>       El manuscrito predecesor project-pack no puede ser la referencia [1] sin metadatos completos.
>
> P1 (matematicos/metodologicos): aplicar P1.1..P1.12 del audit — conteo de modelos y "orden compartido"
>  (backbone comun, solo difiere el operador de memoria); 5.4 banda compacta; 7.1 attainment; 7.5 composite;
>  5.2 clase exacta retarded-DDE (no "cualquier retardo"); 7.6 fase de canal cruzado; 9.8 prehistoria Caputo;
>  m<=5 como presupuesto de complejidad (NO interpretacion biologica); 9.1 proposicion; robust-KL puede ser 0
>  en degeneraciones; proyeccion de seguridad NO es el optimo restringido; "divergencia 0" NO es metrica de seguridad.
>
> EDITORIAL: eliminar tokens crudos (citeP01 -> cite{P01}, refsec:* -> ref{...}, textttsource_pack/...); la
>  "Minimum simulation matrix" en tabla LaTeX (no markdown crudo); hyperref con hidelinks; abstract cuantitativo
>  y calificado (problema, resultados con salvedades, 1-2 numeros verificados, limitacion principal), sin "definitive";
>  quitar proofs duplicados; corregir typos (Gaussanity, Dagnooptimization, Salien, etc.).
>
> COMPLIANCE (PROPOSAL_COMPLIANCE_MATRIX): decir explicitamente que esto es el "minimum viable paper", NO el
>  proposal completo; mover a future work distributed-order, kernels aprendidos, ruido coloreado, parametros
>  variables, recuperacion de parametros, EIG, adaptativo, prior-sensitivity, missing-data, no-Gaussian,
>  covariable ambiental, validacion de laboratorio. No afirmar que se ejecuto lo que no se ejecuto.
>
> GATES DE SUBMISSION (checklist final en research_state.md, todos en true antes de declarar DONE): Teorema 9.3
>  corregido; apendice coincide con cada teorema; 8.4 con supuestos validos; no-free-lunch acotado; fixed vs
>  composite separados; ecuaciones exactas de DDE/latente dadas (estan en benchmark/bench.py, documentarlas);
>  regimenes stable/verdict separados; matriz de confusion consistente; PRBS consistente lineal/no-lineal;
>  claims Bayesianos = metodo implementado (BIC); codigo/datos/JSON adjuntos (estan en benchmark/); seguridad con
>  margenes numericos; sin tokens LaTeX crudos; bibliografia reconstruida y al final; abstract/conclusion solo
>  resultados demostrados; figuras prometidas incluidas o marcadas pendientes.
>
> Cuando el manuscrito refleje TODO esto y compile (main.pdf exit 0), escribir OP-AUDIT-FIX: DONE en
> research_state.md con el checklist de gates + evidencia, y la linea "AUDIT ADDRESSED - awaiting operator".
> ==========================================================================================

# assignments/CURRENT.md — AUDIT RECONSTRUCTION (OP-AUDIT-FIX)

PRIMERA TAREA: leer audits/PAPER_AUDIT.md y audits/MATHEMATICAL_REPAIR_NOTES.md COMPLETOS. Luego corregir
el defecto matematico critico P0.1 (Teorema 9.3): reemplazar por la identidad de informacion secuencial
correcta de MATHEMATICAL_REPAIR_NOTES seccion 6 (KL ESPERADA de la posterior, no KL de la posterior esperada),
y corregir Eq(67), la discusion y la conclusion que dependen de el; quitar el claim de que el greedy 1-paso
minimiza el numero de experimentos. Compilar (main.pdf exit 0) y registrar en un worker_report.
NO tocar contadores. Recien cerrado P0.1 pasar a P0.3/P0.5/P0.9 (reframe seccion 10) y seguir el orden de research_state.md.
