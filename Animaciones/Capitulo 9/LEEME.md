# Animaciones — Capítulo 9: Prueba de Hipótesis

Complemento visual del capítulo 9 del apunte de Procesamiento de Señales
(Oppenheim, *Signals, Systems & Inference*).

Son dos cosas distintas:

- **8 videos** hechos con [Manim](https://www.manim.community/), uno por concepto, más un video completo que los une.
- **7 scripts interactivos** con sliders, para experimentar con los parámetros en vez de mirar.

---

## Ver el video completo

```powershell
Invoke-Item "C:\Users\Nacho\Documents\Animaciones\Capitulo 9\salida\Capitulo9-completo-1080p60.mp4"
```

## Ver un concepto suelto

Los videos individuales quedan en `media\videos\<archivo>\1080p60\<Escena>.mp4`. Por ejemplo:

```powershell
Invoke-Item "media\videos\s07_roc\1080p60\CurvaROC.mp4"
```

## Volver a generar todo

```powershell
cd "C:\Users\Nacho\Documents\Animaciones\Capitulo 9"
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
manim -pqh s03_errores.py Errores
```

---

## Las 8 escenas

| # | Archivo | Escena | Concepto |
|---|---|---|---|
| 1 | `s01_pam.py` | `PAMenRuido` | De dónde sale el problema: PAM binario en ruido |
| 2 | `s02_map.py` | `ReglaMAP` | La regla MAP: decidir por la más probable |
| 3 | `s03_errores.py` | `Errores` | Falsa alarma, miss y detección; el compromiso |
| 4 | `s04_medico.py` | `TestMedico` | La misma teoría en tests médicos; la trampa de la prevalencia |
| 5 | `s05_verosimilitud.py` | `RazonVerosimilitud` | El test de razón de verosimilitud |
| 6 | `s06_neyman.py` | `NeymanPearson` | Cuando no conocés los a priori |
| 7 | `s07_roc.py` | `CurvaROC` | La curva ROC: el retrato del detector |
| 8 | `s08_riesgo.py` | `RiesgoMinimo` | Decisiones de riesgo mínimo |

---

## Los 7 interactivos

Se abren en una ventana con sliders. No necesitan Manim ni ffmpeg, solo
matplotlib.

```powershell
python "interactivo\i04_medico.py"
```

| Archivo | Qué podés mover |
|---|---|
| `i02_map.py` | A priori y separación → el umbral MAP |
| `i03_errores.py` | Umbral, SNR y a priori → las cuatro probabilidades y $P_e$ |
| `i04_medico.py` | Prevalencia, sensibilidad y especificidad → valor predictivo positivo |
| `i05_verosimilitud.py` | El umbral $\eta$ → el umbral equivalente en $r$ |
| `i06_neyman.py` | La cota $\alpha$ de falsa alarma → $P_D$ máximo alcanzable |
| `i07_roc.py` | Separación entre hipótesis → la forma de la ROC |
| `i08_riesgo.py` | Costo de miss y de falsa alarma → el umbral se corre |

---

## Estructura

```
Capitulo 9\
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

Ya están instalados en esta máquina (mismos que el Capítulo 11). Por si hay
que rehacerlo:

```powershell
winget install --id Gyan.FFmpeg   -e --scope user
winget install --id MiKTeX.MiKTeX -e --scope user
python -m pip install manim
initexmf --set-config-value='[MPM]AutoInstall=1'
```

Manim usa LaTeX para las fórmulas (`MathTex`), de ahí MiKTeX.

> Si `manim` o `ffmpeg` "no se reconocen" en una consola recién abierta,
> es que el PATH quedó viejo. `render.ps1` lo relee solo; para usarlos a
> mano, abrí una consola nueva.
