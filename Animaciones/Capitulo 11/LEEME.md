# Animaciones — Capítulo 11: Densidad Espectral de Potencia

Complemento visual del capítulo 11 del apunte de Procesamiento de Señales
(Oppenheim, *Signals, Systems & Inference*).

Son dos cosas distintas:

- **8 videos** hechos con [Manim](https://www.manim.community/), uno por concepto, más un video completo que los une.
- **7 scripts interactivos** con sliders, para experimentar con los parámetros en vez de mirar.

---

## Ver el video completo

```powershell
Invoke-Item "C:\Users\Nacho\Documents\Animaciones\Capitulo 11\salida\Capitulo11-completo-1080p60.mp4"
```

## Ver un concepto suelto

Los videos individuales quedan en `media\videos\<archivo>\1080p60\<Escena>.mp4`. Por ejemplo:

```powershell
Invoke-Item "media\videos\s02_pasabanda\1080p60\PSDPasabanda.mp4"
```

## Volver a generar todo

```powershell
cd "C:\Users\Nacho\Documents\Animaciones\Capitulo 11"
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
manim -pqh s04_bochner.py Bochner
```

---

## Las 8 escenas

| # | Archivo | Escena | Concepto |
|---|---|---|---|
| 1 | `s01_problema.py` | `Problema` | Por qué no alcanza con transformar una realización |
| 2 | `s02_pasabanda.py` | `PSDPasabanda` | La PSD como densidad: el argumento del filtro pasabanda |
| 3 | `s03_dualidad.py` | `Dualidad` | $R_{xx}(\tau)$ y $S_{xx}(j\omega)$ como par de transformadas |
| 4 | `s04_bochner.py` | `Bochner` | Qué puede y qué no puede ser una autocorrelación |
| 5 | `s05_blanco_coloreado.py` | `BlancoColoreado` | Procesos blancos y coloreados |
| 6 | `s06_periodograma.py` | `Periodograma` | Einstein–Wiener–Khinchin y el promediado |
| 7 | `s07_resolucion.py` | `Resolucion` | El compromiso resolución ↔ varianza |
| 8 | `s08_modelador.py` | `ModeladorBlanqueador` | Filtros modeladores y blanqueadores |

---

## Los 7 interactivos

Se abren en una ventana con sliders. No necesitan Manim ni ffmpeg, solo
matplotlib.

```powershell
python "interactivo\i03_dualidad.py"
```

| Archivo | Qué podés mover |
|---|---|
| `i02_pasabanda.py` | Posición y ancho de la banda → potencia que contiene |
| `i03_dualidad.py` | $\alpha$ → la autocorrelación y el espectro a la vez |
| `i04_bochner.py` | Forma de $R(\tau)$ y su ancho → veredicto de validez |
| `i05_coloreado.py` | $\rho$ → realización, autocovarianza y espectro |
| `i06_periodograma.py` | $M$ y $T$ → estimado contra PSD verdadera |
| `i07_resolucion.py` | Separación de los tonos y $T$ → cuándo se resuelven |
| `i08_modelador.py` | Polo del filtro → espectro y señal generada |

---

## Estructura

```
Capitulo 11\
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
