"""Ec. 2 (dos pasadas) contra la modulación corregida (una pasada): los números de la escena 28.

    python comparar_modulaciones.py <carpeta con lora/>     # una vez con el trabajo práctico (Ec. 2)
                                                            # y otra con la rama corregida (lora-phy)

Imprime, para SF = 8 en canal plano: el peine sin ruido de la correlación con el preámbulo (picos
laterales), el FER del detector de preámbulo completo, los errores del inicio a −18 dB en 1.500
tramas y el BER en un punto. Escribe `cmp_<carpeta>.json` en el directorio actual. Las constantes
`CMP_*` de `comun/figuras_lora.py` salen de aquí.
"""
import sys, json, numpy as np
rep=sys.argv[1]; sys.path.insert(0, rep)
from lora import LoRaParams, channel, detection, simulation, tx, seed, params
p=LoRaParams(SF=8,B=125e3); PFA=1/60*p.Ts
out={}
# peine sin ruido: correlación del preámbulo con la plantilla de 8 chirps
pre=tx.preamble(p); x=np.concatenate([np.zeros(10*p.M,complex),pre,np.zeros(4*p.M,complex)])
T=detection.preamble_correlation(x,p); k0=10*p.M
out["peine"]={str(d):float(T[k0+int(d*p.M)]/T[k0]) for d in (-2,-1.5,-1,-0.5,0,0.5,1,1.5)}
print(rep,"peine",out["peine"])
seed(0)
S=np.arange(-24.0,-9.0,1.0)
out["snr"]=S.tolist()
out["fer"]=[float(v) for v in simulation.fer_vs_snr(detection.detect_full,S,channel.FLAT,p,PFA,2000,num_symbols=10,gap=5,min_errors=60)]
print(rep,"FER",[round(v,3) for v in out["fer"]],flush=True)
# errores de inicio a -18 dB
seed(1); e=[]
for _ in range(1500):
    r=simulation.transmit_frame(params.rng.integers(0,p.M,size=10),5,p,-18.0,channel.FLAT)
    d=detection.detect_full(r,p,simulation.noise_power(p,-18.0),PFA)
    e.append(None if d is None else int(d-5*p.M))
import collections
c=collections.Counter(e); out["timing_m18"]={str(k):v for k,v in c.items()}
print(rep,"timing -18:",sorted(((k if k is not None else -9999),v) for k,v in c.items()))
p7=LoRaParams(SF=7,B=125e3); seed(2)
out["ber_plano_m9"]=float(simulation.ber_vs_snr(p7,np.array([-9.0]),channel.FLAT,300)[0]); out["ber_eco_m7"]=float(simulation.ber_vs_snr(p7,np.array([-7.0]),channel.FREQ_SELECTIVE,300)[0])
print(rep,"BER plano -9:",out["ber_plano_m9"],"eco -7:",out["ber_eco_m7"])
json.dump(out,open(f"cmp_{rep}.json","w"))
