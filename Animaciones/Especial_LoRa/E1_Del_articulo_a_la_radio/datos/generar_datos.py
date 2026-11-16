"""De dónde salen los números del episodio (constantes de `comun/figuras_lora.py` y `captura_pluto.npz`).

    python generar_datos.py <carpeta del trabajo práctico>     # la que tiene lora/ y captures/

Corre el paquete `lora` del trabajo práctico (semilla 0) y sus capturas del ADALM-Pluto, imprime
las curvas y vuelve a escribir `captura_pluto.npz` (un recorte de `captures/thermal.npz`). No hace
falta para renderizar: el episodio usa las constantes ya copiadas. Sirve para rehacerlas si el
cuaderno cambia (está en desarrollo). Tarda un par de minutos.
"""
import sys
from pathlib import Path

import numpy as np

TP = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(TP))
from lora import LoRaParams, channel, detection, sdr, seed, simulation  # noqa: E402

AQUI = Path(__file__).resolve().parent
seed(0)

# --- BER contra SNR (SF = 7, 500 transmisiones de 100 símbolos por punto): BER_SNR, BER_PLANO, BER_ECO
p = LoRaParams(SF=7, B=125e3)
snr = np.arange(-12.0, -5.0)
print("BER_SNR  ", snr)
print("BER_PLANO", simulation.ber_vs_snr(p, snr, channel.FLAT, 500))
print("BER_ECO  ", simulation.ber_vs_snr(p, snr, channel.FREQ_SELECTIVE, 500))

# --- Pluto (SF = 8, B = 1 MHz): ATEN_*, TERMICO_* y el recorte de la captura
p_sdr = LoRaParams(SF=8, B=1e6)
P_FA = 1 / 60 * p_sdr.Ts
c, m = sdr.load(TP / "captures" / "atten.npz")
ev = sdr.evaluate_all(c, m, p_sdr, P_FA)
print("ATEN_DB", m["attens_dB"], "ATEN_GANANCIA", m["gain"], "ATEN_SNR", [round(e.snr, 1) for e in ev])
c, m = sdr.load(TP / "captures" / "thermal.npz")
ev = sdr.evaluate_all(c, m, p_sdr, P_FA)
print("TERMICO_SNR", [round(e.snr, 1) for e in ev])
print("TERMICO_FER", [float(e.errors.mean()) for e in ev])

i = list(m["scales_dB"]).index(-28.0)             # escala de −28 dB: SNR medido de −13,7 dB
inicio = int(ev[i].starts[3])                      # cuarta trama detectada
rec = c[i][inicio - 6 * p_sdr.M: inicio + 22 * p_sdr.M]   # 6 símbolos de silencio y la trama entera
np.savez_compressed(AQUI / "captura_pluto.npz", iq=np.stack([rec.real, rec.imag], -1).astype(np.int16),
                    inicio=6 * p_sdr.M, snr_db=ev[i].snr, escala_db=-28.0)

# --- FER simulado con el mismo detector y parámetros que el Pluto: FER_SIM
snr = np.arange(-24.0, -7.0, 1.0)
print("FER_SIM", simulation.fer_vs_snr(detection.detect_full, snr, channel.FLAT, p_sdr, P_FA, 2000,
                                       num_symbols=10, gap=5, min_errors=30))

# --- FER de los tres detectores (SF = 8, B = 125 kHz, canal plano): FER3_*
p8 = LoRaParams(SF=8, B=125e3)
snr = np.arange(-24.0, -3.0, 1.0)
for nombre, det in (("FER3_COMPLETO", detection.detect_full), ("FER3_PICOS", detection.detect_peaks),
                    ("FER3_DEMOD", detection.detect_freq)):
    print(nombre, simulation.fer_vs_snr(det, snr, channel.FLAT, p8, 1 / 60 * p8.Ts, 600, num_symbols=10, gap=5,
                                         min_errors=30))
