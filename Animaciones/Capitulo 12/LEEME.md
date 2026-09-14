# Animaciones — Capítulo 12: Estimación de Señales (Filtro de Wiener)

Complemento visual del capítulo 12 del apunte de Procesamiento de Señales
(Oppenheim, *Signals, Systems & Inference*).

Son dos cosas distintas:

- **8 videos** hechos con [Manim](https://www.manim.community/), uno por concepto, más un video completo que los une.
- **6 scripts interactivos** con sliders, para experimentar con los parámetros en vez de mirar.

---

## Ver el video completo

```powershell
Invoke-Item "C:\Users\Nacho\Documents\Animaciones\Capitulo 12\salida\Capitulo12-completo-1080p60.mp4"
```

## Ver un concepto suelto

Los videos individuales quedan en `media\videos\<archivo>\1080p60\<Escena>.mp4`. Por ejemplo:

```powershell
Invoke-Item "media\videos\s07_causal\1080p60\WienerCausal.mp4"
```

## Volver a generar todo

```powershell
cd "C:\Users\Nacho\Documents\Animaciones\Capitulo 12"
.\render.ps1
```

Opciones útiles:

| Comando | Qué hace |
|---|---|
| `.\render.ps1` | Renderiza las 8 en 1080p60 y las une |
| `.\render.ps1 -Calidad ql` | Borrador rápido en 480p15 (segundos por escena) |
| `.\render.ps1 -SoloUnir` | No re-renderiza, solo vuelve a concatenar |

## Renderizar una sola escena

El flag `-p` la abre al terminar:

```powershell
manim -pqh s08_kalman.py Kalman
```

---

## Las 8 escenas

| # | Archivo | Escena | Concepto |
|---|---|---|---|
| 1 | `s01_problema.py` | `ProblemaEstimacion` | Estimar un proceso a partir de otro: el LMMSE del cap. 8, ahora como filtro LTI |
| 2 | `s02_ortogonalidad.py` | `Ortogonalidad` | El error del mejor estimador es ortogonal a los datos → ecuaciones normales |
| 3 | `s03_fir.py` | `WienerFIR` | Las ecuaciones normales L×L (Yule–Walker) y por qué "no correlacionado ≠ inútil" |
| 4 | `s04_no_causal.py` | `NoCausal` | Pidiendo ortogonalidad en todo el eje, el problema se desacopla en frecuencia; coherencia |
| 5 | `s05_senal_en_ruido.py` | `SenalEnRuido` | $H = D_{yy}/(D_{yy}+D_{vv})$: el filtro reparte ganancia según el SNR de cada banda |
| 6 | `s06_deconvolucion.py` | `Deconvolucion` | Por qué $1/G$ no alcanza: primero limpiar, después invertir |
| 7 | `s07_causal.py` | `WienerCausal` | Blanquear (fase mínima), resolver, deshacer; precio de la causalidad; innovaciones |
| 8 | `s08_kalman.py` | `Kalman` | El Wiener causal como observador: factorización espectral → ganancia → filtro de Kalman |

---

## Los 6 interactivos

Se abren en una ventana con sliders. No necesitan Manim ni ffmpeg, solo
matplotlib.

```powershell
python "interactivo\i05_senal_en_ruido.py"
```

| Archivo | Qué podés mover | Qué se ve |
|---|---|---|
| `i03_fir.py` | Tipo de proceso (exp / bandeado), correlación $\rho$, taps $L$ | La matriz Toeplitz resuelta: pesos $h[j]$ y la reducción de MMSE |
| `i04_no_causal.py` | Centro y ancho de banda de la señal, nivel de ruido | $H = D_{yy}/D_{xx}$ y la coherencia $|\gamma_{yx}|^2$ banda por banda |
| `i05_senal_en_ruido.py` | Color de la señal $\rho$, nivel de ruido $\sigma_v^2$ | Espectros de señal y ruido, y la ganancia del filtro siguiendo al SNR |
| `i06_deconvolucion.py` | Polo del sensor (borroneo), nivel de ruido | $\lvert G\rvert$, $\lvert 1/G\rvert$ y $\lvert H_{\text{Wiener}}\rvert$: el inverso explota, Wiener no |
| `i07_causal.py` | Coeficiente $b$ de $x[n]=w[n]+b\,w[n-1]$ | El cero cruzando el círculo unidad, el factor de fase mínima y $\text{MMSE}=f_0^2$ |
| `i08_kalman.py` | Polo de la planta $a$, relación de ruidos $r=\sigma_w^2/\sigma_v^2$ | Polo del observador $p$ (de la Riccati escalar), $\lvert H(e^{j\Omega})\rvert$ y la ganancia $\ell$ |

---

## Estructura

```
Capitulo 12\
├── comun.py              paleta y helpers compartidos por las escenas
├── sNN_*.py              las 8 escenas de Manim
├── interactivo\
│   ├── estilo_int.py     estilo compartido de los interactivos
│   └── iNN_*.py          los 6 scripts con sliders
├── render.ps1            renderiza todo y concatena
├── lista.txt             orden de concatenación (lo genera render.ps1)
├── media\                salida de Manim (videos individuales y parciales)
└── salida\               el video completo
```

## Requisitos

Ya están instalados en esta máquina, pero por si hay que rehacerlo:

```powershell
winget install --id Gyan.FFmpeg   -e --scope user
winget install --id MiKTeX.MiKTeX -e --scope user
python -m pip install manim
initexmf --set-config-value='[MPM]AutoInstall=1'
```

Manim usa LaTeX para las fórmulas (`MathTex`), de ahí MiKTeX. La primera
compilación baja paquetes sola y tarda un poco; las siguientes ya van rápido.

> Si `manim` o `ffmpeg` "no se reconocen" en una consola recién abierta,
> es que el PATH quedó viejo. `render.ps1` lo relee solo; para usarlos a
> mano, abrí una consola nueva.
