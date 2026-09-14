# Animaciones — Capítulo 8: Estimación

Complemento visual del capítulo 8 del apunte de Procesamiento de Señales
(Oppenheim, *Signals, Systems & Inference*).

Son dos cosas distintas:

- **8 videos** hechos con [Manim](https://www.manim.community/), uno por concepto, más un video completo que los une.
- **8 scripts interactivos** con sliders, para experimentar con los parámetros en vez de mirar.

---

## Ver el video completo

```powershell
Invoke-Item "C:\Users\Nacho\Documents\Animaciones\Capitulo 8\salida\Capitulo8-completo-1080p60.mp4"
```

## Ver un concepto suelto

Los videos individuales quedan en `media\videos\<archivo>\1080p60\<Escena>.mp4`. Por ejemplo:

```powershell
Invoke-Item "media\videos\s06_ortogonalidad\1080p60\Ortogonalidad.mp4"
```

## Volver a generar todo

```powershell
cd "C:\Users\Nacho\Documents\Animaciones\Capitulo 8"
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
manim -pqh s06_ortogonalidad.py Ortogonalidad
```

---

## Las 8 escenas

| # | Archivo | Escena | Concepto |
|---|---|---|---|
| 1 | `s01_mmse.py` | `MMSE` | Sin medir nada: el mejor $\hat{y}$ es la media, y el error es la varianza |
| 2 | `s02_condicional.py` | `Condicional` | Medir $X=x$: el estimador es $E[Y\mid X=x]$, el error es la varianza condicional |
| 3 | `s03_estimador.py` | `Estimador` | Estimación (un número) contra estimador (una variable aleatoria) |
| 4 | `s04_lmmse.py` | `LMMSE` | Obligar al estimador a ser una recta $aX+b$ y optimizar $a$, $b$ |
| 5 | `s05_rho.py` | `Correlacion` | $\text{LMMSE}=\sigma_Y^2(1-\rho^2)$: cuánto sirve medir depende de $\rho$ |
| 6 | `s06_ortogonalidad.py` | `Ortogonalidad` | Estimar linealmente = proyectar ortogonalmente. $\rho=\cos\theta$ |
| 7 | `s07_lineal_o_no.py` | `LinealONo` | Cuándo la recta alcanza (gaussiano) y cuándo no ($Y=X^2$) |
| 8 | `s08_multiples.py` | `Multiples` | Varias mediciones: las ecuaciones normales $C_{XX}\mathbf{a}=\mathbf{c}_{XY}$ |

---

## Los 8 interactivos

Se abren en una ventana con sliders. No necesitan Manim ni ffmpeg, solo
matplotlib.

```powershell
python "interactivo\i05_rho.py"
```

| Archivo | Qué podés mover |
|---|---|
| `i01_mmse.py` | El candidato $\hat{y}$ → el error, con mínimo en la media |
| `i02_condicional.py` | $\rho$ y $x$ observado → nube, corte y densidad condicional |
| `i03_estimador.py` | $\rho$ y $x$ → cómo $\hat{Y}$ recorre su propia densidad |
| `i04_lmmse.py` | $a$ y $b$ → la recta y el error cuadrático medio |
| `i05_rho.py` | $\rho$ → la nube y las dos barras (sin medir vs midiendo) |
| `i06_ortogonalidad.py` | $a$, $\rho$, $\sigma_X$, $\sigma_Y$ → los vectores y la proyección |
| `i07_lineal_o_no.py` | La relación X–Y (lineal, parábola, seno, escalón) y el ruido |
| `i08_multiples.py` | Las tres correlaciones → los pesos $a_1$, $a_2$ y la redundancia |

---

## Estructura

```
Capitulo 8\
├── comun.py              paleta y helpers compartidos por las escenas
├── sNN_*.py              las 8 escenas de Manim
├── interactivo\
│   ├── estilo_int.py     estilo compartido de los interactivos
│   └── iNN_*.py          los 8 scripts con sliders
├── render.ps1            renderiza todo y concatena
├── lista.txt             orden de concatenación (lo genera render.ps1)
├── media\                salida de Manim (videos individuales y parciales)
└── salida\               el video completo
```

## Requisitos

Ya están instalados en esta máquina (ffmpeg, MiKTeX, manim). Si hay que rehacerlo:

```powershell
winget install --id Gyan.FFmpeg   -e --scope user
winget install --id MiKTeX.MiKTeX -e --scope user
python -m pip install manim
initexmf --set-config-value='[MPM]AutoInstall=1'
```

> Si `manim` o `ffmpeg` "no se reconocen" en una consola recién abierta,
> es que el PATH quedó viejo. `render.ps1` lo relee solo; para usarlos a
> mano, abrí una consola nueva.
