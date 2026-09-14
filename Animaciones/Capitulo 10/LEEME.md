# Animaciones — Capítulo 10: Procesos Aleatorios

Complemento visual del capítulo 10 del apunte de Procesamiento de Señales
(Oppenheim, *Signals, Systems & Inference*).

Son dos cosas distintas:

- **8 videos** hechos con [Manim](https://www.manim.community/), uno por concepto, más un video completo que los une.
- **7 scripts interactivos** con sliders, para experimentar con los parámetros en vez de mirar.

---

## Ver el video completo

```powershell
Invoke-Item "C:\Users\Nacho\Documents\Animaciones\Capitulo 10\salida\Capitulo10-completo-1080p60.mp4"
```

## Ver un concepto suelto

Los videos individuales quedan en `media\videos\<archivo>\1080p60\<Escena>.mp4`. Por ejemplo:

```powershell
Invoke-Item "media\videos\s04_oscilador\1080p60\Oscilador.mp4"
```

## Volver a generar todo

```powershell
cd "C:\Users\Nacho\Documents\Animaciones\Capitulo 10"
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
manim -pqh s05_autocorrelacion.py Autocorrelacion
```

---

## Las 8 escenas

| # | Archivo | Escena | Concepto |
|---|---|---|---|
| 1 | `s01_ensemble.py` | `Ensemble` | Qué es un proceso: el ensemble y sus dos lecturas |
| 2 | `s02_momentos.py` | `Momentos` | Media $\mu_X(t)$ y autocorrelación $R_{XX}(t_1,t_2)$ |
| 3 | `s03_estacionariedad.py` | `Estacionariedad` | Estacionariedad estricta contra WSS |
| 4 | `s04_oscilador.py` | `Oscilador` | $X(t)=A\cos(\omega_0 t+\Theta)$: por qué la fase aleatoria importa |
| 5 | `s05_autocorrelacion.py` | `Autocorrelacion` | $R_{xx}(\tau)$ como solapamiento deslizante; simetría y máximo en 0 |
| 6 | `s06_ergodicidad.py` | `Ergodicidad` | Promedio temporal contra promedio de ensemble |
| 7 | `s07_prediccion.py` | `Prediccion` | Predicción LMMSE y filtrado FIR → ecuaciones normales |
| 8 | `s08_filtrado.py` | `Filtrado` | Filtrado LTI de procesos WSS: $S_{yy}=|H|^2 S_{xx}$ |

---

## Los 7 interactivos

Se abren en una ventana con sliders. No necesitan Manim ni ffmpeg, solo
matplotlib.

```powershell
python "interactivo\i05_autocorrelacion.py"
```

| Archivo | Qué podés mover |
|---|---|
| `i01_ensemble.py` | N.º de realizaciones y el instante $t^*$ → la v.a. del corte |
| `i02_momentos.py` | $t_1$ y $t_2$ → la nube de dispersión $X(t_1)$ vs $X(t_2)$ y $\rho$ |
| `i03_estacionariedad.py` | Posición de la ventana y "deriva" → media y desvío locales |
| `i04_oscilador.py` | $\omega_0$ y la dispersión de fase → la media se aplana o no |
| `i05_autocorrelacion.py` | $\tau$ y $\alpha$ → copia corrida, producto y $R_{xx}(\tau)$ |
| `i06_prediccion.py` | Horizonte $m$ y correlación $\alpha$ → peso $\alpha^m$ y banda |
| `i07_filtrado.py` | Corte del filtro y ancho de $S_{xx}$ → $S_{yy}$ y potencia que pasa |

---

## Estructura

```
Capitulo 10\
├── comun.py              paleta y helpers compartidos por las escenas
├── sNN_*.py              las 8 escenas de Manim
├── interactivo\
│   ├── estilo_int.py     estilo compartido de los interactivos
│   └── iNN_*.py          los 7 scripts con sliders
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
