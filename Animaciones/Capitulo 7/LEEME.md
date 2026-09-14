# Animaciones — Capítulo 7: Modelos Probabilísticos

Complemento visual del capítulo 7 del apunte de Procesamiento de Señales
(Oppenheim, *Signals, Systems & Inference*).

Son dos cosas distintas:

- **8 videos** hechos con [Manim](https://www.manim.community/), uno por concepto, más un video completo que los une.
- **8 scripts interactivos** con sliders, para experimentar con los parámetros en vez de mirar.

---

## Ver el video completo

```powershell
Invoke-Item "C:\Users\Nacho\Documents\Animaciones\Capitulo 7\salida\Capitulo7-completo-1080p60.mp4"
```

## Ver un concepto suelto

Los videos individuales quedan en `media\videos\<archivo>\1080p60\<Escena>.mp4`:

```powershell
Invoke-Item "media\videos\s01_bayes\1080p60\Bayes.mp4"
```

## Volver a generar todo

```powershell
cd "C:\Users\Nacho\Documents\Animaciones\Capitulo 7"
.\render.ps1
```

| Comando | Qué hace |
|---|---|
| `.\render.ps1` | Renderiza las 8 en 1080p60 y las une |
| `.\render.ps1 -Calidad ql` | Borrador rápido en 480p15 (segundos por escena) |
| `.\render.ps1 -SoloUnir` | No re-renderiza, solo vuelve a concatenar |

## Renderizar una sola escena

El flag `-p` la abre al terminar:

```powershell
manim -pqh s07_correlacion.py Correlacion
```

---

## Las 8 escenas

| # | Archivo | Escena | Concepto |
|---|---|---|---|
| 1 | `s01_bayes.py` | `Bayes` | Probabilidad condicional y regla de Bayes. Cierra con el test médico: con una enfermedad rara, la mayoría de los positivos son sanos |
| 2 | `s02_cdf_pdf.py` | `CDFyPDF` | CDF, PDF y PMF: los tres casos (continua, discreta, mixta) y el impulso de Dirac |
| 3 | `s03_media_varianza.py` | `MediaYVarianza` | La media como punto de equilibrio, la varianza como desparramo, y la identidad $\sigma^2=E[X^2]-\mu^2$ paso a paso |
| 4 | `s04_chebyshev.py` | `Chebyshev` | La cota $1/\alpha^2$ contra la masa real, en tres distribuciones distintas |
| 5 | `s05_torre.py` | `EsperanzaIterada` | $E[X]=E[E[X\mid Y]]$ con el ejemplo de alturas por grupo |
| 6 | `s06_conjunta.py` | `Conjunta` | Conjunta y marginales: proyectar es integrar, y las marginales **no** determinan la conjunta |
| 7 | `s07_correlacion.py` | `Correlacion` | Covarianza, $\rho$, y la trampa: no correlacionadas ≠ independientes |
| 8 | `s08_vectorial.py` | `Vectorial` | Las variables aleatorias como vectores: $\rho=\cos\theta$. Es el puente al capítulo 8 |

---

## Los 8 interactivos

Se abren en una ventana con sliders. No necesitan Manim ni ffmpeg, solo
matplotlib.

```powershell
python "interactivo\i01_bayes.py"
```

| Archivo | Qué podés mover |
|---|---|
| `i01_bayes.py` | Prevalencia, sensibilidad, especificidad → P(enfermo \| +) |
| `i02_cdf_pdf.py` | Tipo de variable y la banda [a, b] → CDF y PDF/PMF |
| `i03_media_varianza.py` | $\mu$, $\sigma$ y la forma → equilibrio y verificación de la identidad |
| `i04_chebyshev.py` | $\alpha$ y la distribución → cota contra masa real |
| `i05_torre.py` | Proporciones y medias de cada grupo → la media total |
| `i06_conjunta.py` | $\rho$, $\sigma_X$, $\sigma_Y$ → conjunta y marginales |
| `i07_correlacion.py` | $\rho$ y cinco casos patológicos con $\rho\approx0$ |
| `i08_vectorial.py` | $\rho$ y los desvíos → el ángulo entre los vectores |

> El más recomendable para jugar es `i01_bayes.py`: bajá la prevalencia y
> mirá cómo se derrumba la probabilidad de estar enfermo aunque el test
> sea excelente. Y `i07_correlacion.py`, para ver de golpe que $\rho$ solo
> mide la parte lineal de la relación.

---

## Estructura

```
Capitulo 7\
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

`comun.py` y `estilo_int.py` son copias de los del capítulo 11, más los
helpers propios de este capítulo (nubes de puntos, elipses de nivel).
Se duplican a propósito: así cada carpeta de capítulo es autónoma y se
puede mover o compartir sin arrastrar la de al lado.

## Requisitos

Los mismos que el capítulo 11, ya instalados en esta máquina:

```powershell
winget install --id Gyan.FFmpeg   -e --scope user
winget install --id MiKTeX.MiKTeX -e --scope user
python -m pip install manim
initexmf --set-config-value='[MPM]AutoInstall=1'
```

> Si `manim` o `ffmpeg` "no se reconocen" en una consola recién abierta,
> es que el PATH quedó viejo. `render.ps1` lo relee solo; para usarlos a
> mano, abrí una consola nueva.

## Nota sobre las fuentes

Los glifos `⟹` y `⟺` (U+27F9 y U+27FA) **no existen** en la fuente que usa
`Text()` de Manim y salen como cajas vacías. Las flechas de implicación van
siempre por `MathTex` (`\Longrightarrow`, `\not\Longrightarrow`). Las
flechas simples `⇒ ⇔ → ≠ ≈ ≤ ≥` sí están y se pueden usar en `Text()`.
