# R3-H — v4 safe-benchmark: completion and reproducibility control

**Round 03, researcher deliverable. Status: v4 complete at all three amplitudes.
The frozen v3 benchmark reproduces to four decimals. Round-02's amplitude hypothesis fails.**

The chief instructed that the running `amp = 0.100` job must finish without being
restarted. It did: the shard completed on Aureus (`DONE`, 756/756 cells, 0 divergences).
The two low-amplitude shards had already completed on Orion. No run was restarted and no
cell was recomputed.

---

## 1. Reproducibility control: v4 @ amp=0.100 vs frozen v3

Same model set, same 756-cell grid, same 200→100 replicate seeding scheme, same BIC
decision rule, independent host (Aureus vs the original Orion run).

| quantity | manuscript (v3, frozen) | v4 @ amp=0.100 | Δ |
|---|---:|---:|---:|
| macro-accuracy | 0.537 | **0.5369** | −0.0001 |
| prbs accuracy | 0.584 | **0.5836** | −0.0004 |
| multisine accuracy | 0.583 | **0.5829** | −0.0001 |
| multiscale accuracy | 0.324 | **0.3235** | −0.0005 |
| prbs crossing rate | 1.000 | **1.000** | 0 |
| multisine crossing rate | 0.357 | **0.357** | 0 |
| multiscale crossing rate | 0.000 | **0.000** | 0 |
| divergences | 0 | **0** | 0 |

**Verdict: PASS.** The manuscript's headline benchmark numbers are reproducible on a
different machine under a re-implemented driver. Whatever else is wrong with the paper,
the v3 benchmark is not fabricated and not host-dependent.

---

## 2. Full three-amplitude result

Amplitudes 0.050 and 0.063 are **linear-certificate diagnostics**, per the chief's Round-02
naming instruction. They are *not* a "nonlinear-safe benchmark", and §3 shows why that
naming was necessary.

| amp | cells | macro | micro | best design | divergences | crossing rate (all cells) |
|---:|---:|---:|---:|---|---:|---:|
| 0.050 | 756 | 0.4570 | 0.4084 | prbs | 0 | 32.1% |
| 0.063 | 756 | 0.4712 | 0.4253 | prbs | 0 | 45.2% |
| 0.100 | 756 | 0.5369 | 0.4910 | prbs | 0 | 56.0% |

Per-class recall:

| amp | ODE | Caputo | DDE | latent3 |
|---:|---:|---:|---:|---:|
| 0.050 | 0.9799 | 0.4119 | 0.2292 | 0.2072 |
| 0.063 | 0.9742 | 0.4454 | 0.2635 | 0.2016 |
| 0.100 | 0.9716 | 0.5236 | 0.4103 | 0.2422 |

Two things to state plainly:

- **`latent3` recall is at or below chance (0.25) at every amplitude** (0.207, 0.202, 0.242).
  BIC essentially never selects the finite-latent model when it is true. This is consistent
  with Lemma B.2 / R3-A (a positive exponential mixture of modest order reproduces the
  fractional kernel to within noise on `[0,T]`), but it also means the four-class benchmark
  is effectively a three-class problem plus a decoy.
- **ODE recall ≈ 0.97 at every amplitude.** The classifier's default explanation is the
  memoryless one, and weak excitation makes that default nearly absorbing.

---

## 3. The Round-02 amplitude hypothesis is refuted

Round 02 proposed lowering amplitude as the route to a genuinely safe benchmark. **It does
not work.** Per design, crossing rate and worst-case margin as amplitude falls:

| design | cross @0.050 | cross @0.063 | cross @0.100 | min margin @0.050 | @0.063 | @0.100 |
|---|---:|---:|---:|---:|---:|---:|
| prbs | 0.714 | 0.929 | 1.000 | −0.2516 | −0.2824 | −0.3139 |
| sinusoid | 0.714 | 0.929 | 1.000 | −0.2744 | −0.2839 | −0.3058 |
| chirp | 0.500 | 0.714 | 0.929 | −0.2291 | −0.2661 | −0.3012 |
| multisine | 0.000 | 0.143 | 0.357 | +0.2334 | −0.1219 | −0.2405 |
| pulse | 0.000 | 0.000 | 0.071 | +0.3455 | +0.3232 | −0.1207 |
| multiscale | 0.000 | 0.000 | 0.000 | +0.3543 | +0.3381 | +0.2921 |

Halving the amplitude takes prbs from 100% crossings to 71.4% — still unsafe in a large
majority of cells — while its accuracy advantage is *retained* (prbs is the top design at
all three amplitudes). Only multiscale is safe at all three amplitudes, and only multisine
and pulse change safety status across the range (multisine crosses over between 0.050 and
0.063; pulse between 0.063 and 0.100).

**Conclusion: amplitude is the wrong knob.** This is the negative result that makes R3-F's
positive result meaningful — the trade-off cannot be dissolved by shrinking the input, only
by changing its *shape*.

---

## 4. Realised gain: the linear certificate is violated, and worse at low amplitude

`realized_gain = max_t |z(t) − z*| / amp`, logged per cell. The linear response certificate
gives `Γ_T = 5.78`.

| design | max gain @0.050 | @0.063 | @0.100 |
|---|---:|---:|---:|
| prbs | **28.074** | 22.623 | 14.462 |
| sinusoid | 19.163 | 16.811 | 11.745 |
| chirp | 12.915 | 10.838 | 7.704 |
| multisine | 4.456 | 8.549 | 7.383 |
| pulse | 1.766 | 2.064 | 5.374 |
| multiscale | 1.541 | 1.474 | 1.814 |

Peak violation factor over `Γ_T`: **28.074 / 5.78 = 4.86×** at `amp = 0.050`, versus
2.50× at `amp = 0.100`.

The gain *increases* as amplitude *decreases* for the four crossing designs. That is the
signature of a response whose large component is **not proportional to the input**: once a
trajectory escapes the Allee basin, `max|z − z*|` is set by the basin geometry, not by
`amp`, so the ratio scales like `1/amp`. Whereas the two designs that never cross
(multiscale, and pulse at low amplitude) have gains of 1.5–2.1, essentially
amplitude-independent, as a genuinely linear response should.

So the realised gain cleanly separates linear-regime cells from escape cells, and it
confirms that the linear certificate `Γ_T = 5.78` **cannot** be used to justify safety for
any of the crossing designs at any of the three amplitudes. This is the quantitative
content of the Round-02 finding, now measured across the full amplitude range.

---

## 5. Artifacts

| file | content |
|---|---|
| `rescue_compute/v4_safe_benchmark.py` | driver (amplitude-sharded via `FMED_AMPS`) |
| `rescue_compute/r3_v4/v4_all_amplitudes.json` | merged official summaries, 3 amplitudes |
| `rescue_compute/r3_v4/state_v4_amp050_063.jsonl` | 1512 raw cells (Orion) |
| `rescue_compute/r3_v4/state_v4_amp100.jsonl` | 756 raw cells (Aureus) |

Total 2268 cells, 0 divergences. Frozen v3 artifacts untouched.
