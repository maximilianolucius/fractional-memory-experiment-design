"""
designs.py — experiment designs d=(u, T_sample, C): input waveforms, observation
channels, sampling schedules, SNR-based noise. Follows source_pack/{06,08,09,14}.
"""
import numpy as np

# ---- input waveforms u(t), energy-normalized to unit L2 on [0,T] then scaled ----
def u_pulse(t, T, amp=1.0):
    w = 0.06 * T
    return amp * (np.abs(t - 0.15 * T) < w).astype(float)

def u_multiscale_pulse(t, T, amp=1.0):
    """log-spaced pulse train (source_pack/14 Design C)."""
    out = np.zeros_like(t)
    t0, q = 0.05 * T, 1.9
    tk = t0
    while tk < 0.9 * T:
        out += (np.abs(t - tk) < 0.02 * T).astype(float)
        tk *= q
    return amp * out

def u_sinusoid(t, T, amp=1.0, w=0.49):
    """optimized single sinusoid near omega*tau0~0.49 (source_pack/14 Design B)."""
    return amp * np.sin(w * t)

def u_multisine(t, T, amp=1.0, ws=(0.12, 0.49, 1.6)):
    """robust multisine: finite support (source_pack/08 Thm 2, P+1 freqs)."""
    return amp * sum(np.sin(w * t + 0.5 * k) for k, w in enumerate(ws)) / np.sqrt(len(ws))

def u_chirp(t, T, amp=1.0, f0=0.05, k=0.03):
    return amp * np.sin(2 * np.pi * (f0 * t + 0.5 * k * t * t / T))

def u_prbs(t, T, amp=1.0, nseg=15, seed=0):
    rng = np.random.default_rng(seed)
    seg = rng.integers(0, 2, nseg) * 2 - 1
    idx = np.clip((t / T * nseg).astype(int), 0, nseg - 1)
    return amp * seg[idx]

INPUTS = {
    "pulse": u_pulse,
    "multisine": u_multisine,       # "robust multisine"
    "sinusoid": u_sinusoid,         # "optimized sinusoid"
    "multiscale": u_multiscale_pulse,  # proxy for "adaptive"/multiscale
    "chirp": u_chirp,
    "prbs": u_prbs,
}

def energy_normalize(uvals, dt, E=1.0):
    e = np.sqrt(np.sum(uvals**2) * dt)
    return uvals * (np.sqrt(E) / e) if e > 0 else uvals

# ---- observation channels C ----
CHANNELS = {
    "prey": np.array([[1.0, 0.0]]),
    "pred": np.array([[0.0, 1.0]]),
    "both": np.array([[1.0, 0.0], [0.0, 1.0]]),
}

# ---- horizon / SNR / sampling ----
HORIZON = {"short": 6.0, "med": 12.0, "long": 24.0}
SNR_DB = {"hi": 20.0, "med": 10.0, "lo": 3.0}
A_GRID = [0.25, 0.30, 0.40]
ALPHA_GRID = [0.70, 0.85, 0.95]
LATENT_CAP = [1, 3, 6]
TRUE_MODELS = ["ODE", "Caputo", "DDE", "latent1", "latent3"]

def sample_times(T, n=120):
    return np.linspace(T / n, T, n)

def noise_sigma(signal, snr_db):
    p_sig = np.mean(signal**2)
    return np.sqrt(p_sig / (10.0 ** (snr_db / 10.0))) + 1e-9
