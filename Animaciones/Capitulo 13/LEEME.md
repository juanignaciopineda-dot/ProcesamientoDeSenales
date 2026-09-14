# Animaciones — Capítulo 13: Detección de Señales

Complemento visual del capítulo 13 del apunte de Procesamiento de Señales
(Oppenheim, *Signals, Systems & Inference*).

Son dos cosas distintas:

- **8 videos** hechos con [Manim](https://www.manim.community/), uno por concepto, más un video completo que los une.
- **6 scripts interactivos** con sliders, para experimentar con los parámetros en vez de mirar.

---

## Ver el video completo

```powershell
Invoke-Item "C:\Users\Nacho\Documents\Animaciones\Capitulo 13\salida\Capitulo13-completo-1080p60.mp4"
```

## Ver un concepto suelto

Los videos individuales quedan en `media\videos\<archivo>\1080p60\<Escena>.mp4`. Por ejemplo:

```powershell
Invoke-Item "media\videos\s04_filtro_adaptado\1080p60\FiltroAdaptado.mp4"
```

## Volver a generar todo

```powershell
cd "C:\Users\Nacho\Documents\Animaciones\Capitulo 13"
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
manim -pqh s04_filtro_adaptado.py FiltroAdaptado
```

---

## Las 8 escenas

| # | Archivo | Escena | Concepto |
|---|---|---|---|
| 1 | `s01_problema.py` | `Problema` | De una medición (cap. 9) a una señal entera: MAP con el vector $\mathbf r$; más datos no ayudan si no se procesan bien |
| 2 | `s02_derivacion.py` | `Derivacion` | La derivación completa: ln, desarrollar el cuadrado, cancelar $\sum r^2[n]$ → $g=\sum r[n]s[n]\gtrless\gamma$ |
| 3 | `s03_desempeno.py` | `Desempeno` | $g$ es gaussiana bajo cada hipótesis, separadas por $E$; $P_e=Q(\sqrt E/2\sigma)$ depende solo de $E/\sigma^2$, no de la forma |
| 4 | `s04_filtro_adaptado.py` | `FiltroAdaptado` | $g$ es lineal → se calcula con un filtro LTI: $h[k]=s[-k]$, el filtro adaptado; su salida con $s$ a la entrada es $R_{ss}[n]$ |
| 5 | `s05_por_que.py` | `PorQueFunciona` | Dos lecturas: en frecuencia, módulo y fase alinean todo en $n=0$; sin gaussianidad, Cauchy-Schwarz da el SNR máximo |
| 6 | `s06_coloreado.py` | `RuidoColoreado` | Ruido coloreado: blanquear y adaptar, $H=S^*/(D_{vv}/\sigma^2)$; ahora la forma de $s[n]$ sí importa; pulsos de Nyquist |
| 7 | `s07_compresion.py` | `CompresionPulso` | El retardo se lee del máximo de $R_{ss}$; Barker-13 y el chirp dan picos nítidos donde el rectangular los funde |
| 8 | `s08_antipodal.py` | `OnOffAntipodal` | $M$ señales → banco de adaptados; caso binario → adaptado a $s_1-s_0$; antipodal duplica el argumento de la $Q$ gratis en potencia de pico |

---

## Los 6 interactivos

Se abren en una ventana con sliders. No necesitan Manim ni ffmpeg, solo
matplotlib.

```powershell
python "interactivo\i04_filtro_adaptado.py"
```

| Archivo | Qué podés mover | Qué se ve |
|---|---|---|
| `i03_desempeno.py` | SNR $E/\sigma^2$ (dB), a priori $p_1$ | Las dos gaussianas de $g$, el umbral óptimo, $P_{FA}$, $P_M$, $P_e$ y la curva $P_e$ vs SNR |
| `i04_filtro_adaptado.py` | Forma del pulso, nivel de ruido, botón de nuevo ruido | $r[n]$, $h[k]=s[-k]$ y la salida $g[n]$ con el veredicto contra $\gamma$ |
| `i05_cauchy_schwarz.py` | Ángulo $\theta$ entre $h$ y $s$ | $\text{SNR}_{out}=\text{SNR}_{in}\cos^2\theta$: máximo solo con el filtro adaptado |
| `i06_coloreado.py` | Centro de banda de la señal, color del ruido | $\lvert S\rvert^2$, $D_{vv}$, $\lvert H\rvert$ y $E_p/\sigma^2$ contra el caso de ruido blanco |
| `i07_compresion.py` | Forma del pulso, separación entre dos ecos, ruido | Si la salida del adaptado resuelve los dos ecos o los funde |
| `i08_antipodal.py` | SNR (dB), $X/E$ entre $-1$ (antipodal) y $+1$ | $P_e$ en función del SNR y de qué tan parecidas son las dos señales |

---

## Estructura

```
Capitulo 13\
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

Ya están instalados en esta máquina (mismos que los capítulos anteriores).
Por si hay que rehacerlo:

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
