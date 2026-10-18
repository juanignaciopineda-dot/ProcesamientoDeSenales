# Animaciones — videoclases de Procesamiento de Señales

Videoclases narradas y animadas para YouTube, hechas con **Manim** +
**manim-voiceover** + una voz neuronal gratuita (`es-ES-XimenaNeural`, por
**Azure Speech** o, si no hay clave, por **edge-tts**: §9). Cada video es un **episodio de ~10 minutos** con
dinámica de retención alta, al estilo de TikTok y YouTube. Cubren los
capítulos 7 a 13 de *Signals, Systems & Inference* (Oppenheim y Verghese),
en el orden del apunte de la materia.

El método, el motor y las pautas son los mismos de las videoclases de
Programación Concurrente (`C:\Users\Nacho\Documents\ProgramacionConcurrente\Animaciones`),
donde ya se produjeron y subieron episodios completos. Este README es
autosuficiente: **no hace falta abrir aquel repositorio**.

> **Si eres un agente nuevo:** este archivo es la fuente de verdad. Con él y
> el `guion_base.md` o el `guion.md` en curso alcanza para seguir trabajando.
> Lee §0 (reglas), §1 (estado: qué sigue) y §2 (flujo) antes de tocar nada.
> El resto se consulta según haga falta.

> **Aviso (12/10/2026): la voz vuelve a funcionar.** El `403` de edge-tts ya no
> bloquea nada: la voz sale por **Azure Speech** con la misma Ximena (§9).
> - No hay que configurar nada: `ritmo.py`, `render.py` y `voces_prueba/` usan
>   Azure solos. La clave está en `Animaciones/.env` (no va al repo: no
>   mostrarla, copiarla ni subirla).
> - **No usar más `CURSO_VOZ_SIN_RED`.** Si quedó puesta en la terminal,
>   quitarla (PowerShell: `Remove-Item Env:CURSO_VOZ_SIN_RED`).
> - Toda nota de §1 o de un `guion.md` que diga «edge-tts da 403», «sin voz
>   real», «voz de prueba» o «voz simulada» está **vieja**: ese paso ya se puede
>   hacer. Correr `ritmo.py` y renderizar el borrador con la voz real (los
>   tiempos cambian respecto de los estimados: revisar avisos y hojas de
>   contacto de nuevo) y después corregir esa nota.
> - El audio real que ya estaba en caché (Caps. 10 a 13) se reutiliza tal cual.

---

## Índice

0. [Reglas de oro](#0-reglas-de-oro)
1. [Estado del proyecto](#1-estado-del-proyecto)
2. [Flujo de trabajo](#2-flujo-de-trabajo)
3. [Pautas de contenido](#3-pautas-de-contenido)
4. [Pautas visuales y de ritmo](#4-pautas-visuales-y-de-ritmo)
5. [Formato del guion_base.md](#5-formato-del-guion_basemd)
6. [Formato del guion.md](#6-formato-del-guionmd)
7. [Arquitectura del código y API](#7-arquitectura-del-código-y-api)
8. [Herramientas: render, ritmo y controles](#8-herramientas-render-ritmo-y-controles)
9. [Voz, pronunciación y fórmulas dichas](#9-voz-pronunciación-y-fórmulas-dichas)
10. [Entorno y trampas conocidas](#10-entorno-y-trampas-conocidas)
11. [Checklist antes de entregar](#11-checklist-antes-de-entregar)
12. [Cómo trabajar con el usuario](#12-cómo-trabajar-con-el-usuario)

---

## 0. Reglas de oro

1. **Cada cosa que dice la voz se ve.** Una animación anclada a la frase cada ~2–3 s.
2. **Toda fórmula que se nombra se construye en pantalla**, término a término,
   mientras la voz la nombra. Nunca una fórmula entera de golpe que nadie lee.
3. **La imagen llega con la voz, nunca detrás.** Las animaciones son cortas (0,3–1,5 s)
   y arrancan 0,3 s antes de la palabra (lo hace `en()` solo).
4. **Nada de texto de relleno.** En pantalla solo hay términos clave, fórmulas, números o preguntas.
5. **Explícito y sin dar nada por sabido** (§3, "Explicar de forma explícita"):
   caso concreto → cuenta a mano con números → dibujo → fórmula como resumen.
   Las deducciones cortas se hacen enteras, paso a paso, en pantalla.
6. **Castellano de España** en todo lo que se narra (la voz es española).
7. **El texto nuevo de narración lo aprueba el usuario** antes de animar.
8. **La pronunciación se elige de oído**: nunca inventar grafías fonéticas sin que el usuario las escuche.
9. **Antes de entregar**: `ritmo.py` sin huecos grandes, render sin avisos y
   hojas de contacto revisadas (§11).

---

## 1. Estado del proyecto

**Orden de los capítulos** (es el orden del libro y del apunte; no cambiarlo).
Las líneas son las de `../Apuntes/PROCESAMIENTO DE SEÑALES.md`, **sin** contar
la sección "Ejercicios Propuestos" de cada capítulo, que no se narra.

| Cap. | Tema | Carpeta | Apunte (líneas) | Complemento | Estado |
|---|---|---|---|---|---|
| 7 | Modelos probabilísticos | `Capitulo07_Probabilidad/` | 1–239 | `Cap 7 en profundidad.md` | `guion_base.md` escrito, **esperando la aprobación del usuario** |
| 8 | Estimación | `Capitulo08_Estimacion/` | 289–403 | `Cap 8 en profundidad.md` | `guion_base.md` escrito, **esperando la aprobación del usuario** |
| 9 | Pruebas de hipótesis | `Capitulo09_PruebasDeHipotesis/` | 504–596 | `Cap 9 en profundidad.md` | `guion_base.md` escrito, **esperando la aprobación del usuario** |
| 10 | Procesos aleatorios | `Capitulo10_ProcesosAleatorios/` | 689–955 | `Cap 10 en profundidad.md` | `guion_base.md` escrito, **esperando la aprobación del usuario** |
| 11 | Densidad espectral de potencia | `Capitulo11_DensidadEspectral/` | 1087–1289 | `Cap 11 en profundidad.md` | `guion_base.md` escrito, **esperando la aprobación del usuario** |
| 12 | Estimación de señales | `Capitulo12_EstimacionDeSenales/` | 1425–1695 | `Cap 12 en profundidad.md` | `guion_base.md` escrito, **esperando la aprobación del usuario** |
| 13 | Detección de señales | `Capitulo13_DeteccionDeSenales/` | 1880–2122 | `Cap 13 en profundidad.md` | `guion_base.md` escrito, **esperando la aprobación del usuario** |

Cuando un capítulo tiene guion base, se le agrega aquí una subsección propia
(`### Capítulo NN (Tema)`) con la tabla de episodios, igual que esta:

| Episodio | Carpeta | Escenas de `guion_base.md` | Estado |
|---|---|---|---|
| E1 · Título | `E1_nombre_corto/` | 01 …, 02 …, 03 … | (qué está hecho y qué falta, con duración y avisos si hay render) |

y debajo, en viñetas: bucles que cruzan episodios, pronunciaciones pendientes,
piezas nuevas de `figuras.py`, y cualquier decisión que un chat nuevo tenga que conocer.

**Reglas que cruzan todo el curso:**
- Cada cierre anuncia el episodio siguiente **por su título**, también entre
  capítulos: el cierre del último episodio del Cap. 7 anuncia el E1 del Cap. 8.
- El E1 del Cap. 7 es el primer vídeo de la serie: su gancho presenta la
  materia entera ("señales que no se pueden predecir") y arranca con un
  **repaso de ~3 minutos, muy por encima**, de Señales y Sistemas y de
  Probabilidad y Estadística (lo pidió el usuario). No hay un "capítulo de
  repaso": lo que cada capítulo necesita de esas materias se explica en ese
  capítulo, en el momento en que hace falta.
- El apunte ya marca los puentes entre capítulos (Parte 4 de cada "en
  profundidad": "qué de este capítulo alimenta a cuál"). Son los **bucles
  largos** del curso: se siembran en un capítulo y se pagan en otro.

### Capítulo 7 (Modelos probabilísticos)

En 7 episodios. `Capitulo07_Probabilidad/guion_base.md` tiene la narración
de las 29 escenas (con objetivo, qué hace falta saber antes y visual), el
reparto, los hilos, los recortes, las pronunciaciones y las piezas visuales
nuevas. Es el primer capítulo de la serie y sirve de **ejemplo de formato y de
nivel de explicitud** para los guiones base de los demás capítulos.

Segunda versión: la primera (16 escenas en 4 episodios) al usuario no le
gustó por poco explícita y por dar cosas por sabidas. Esta rehace todo con las
pautas de §3 ("Explicar de forma explícita") y suma el repaso inicial.

| Episodio | Carpeta | Escenas de `guion_base.md` | Estado |
|---|---|---|---|
| E1 · Lo que no se puede predecir | `E1_Lo_que_no_se_puede_predecir/` | 01 Repaso de señales, 02 Repaso de azar, 03 Por qué probabilidad, 04 Modelo probabilístico | **Subido a YouTube en privado** el 17/10/2026: render final 1080p60 de 7:22, con título, descripción con `capitulos.txt`, subtítulos `.srt`, categoría Educación y «no es para niños» (https://youtu.be/6sebWkz3paI). Residuos limpiados el 17/10/2026; se rehace con `python rehacer.py Capitulo07_Probabilidad`. La caché de voz versionada (`media/voiceovers/`) se volvió a sintetizar después de la subida: un render nuevo es reproducible, pero la voz puede diferir un poco de la del vídeo subido. **Falta**: publicarlo (lo hace el usuario). |
| E2 · Cuando sabes algo más | `E2_Cuando_sabes_algo_mas/` | 05 Probabilidad condicional, 06 Independencia, 07 Test médico, 08 Bayes | **Subido a YouTube en privado** el 17/10/2026: render final 1080p60 de 8:54, con título, descripción con `capitulos.txt`, subtítulos `.srt`, categoría Educación y «no es para niños» (https://youtu.be/43BeCcP9gUQ). Lo subió el usuario sin el visto bueno que figuraba pendiente acá (texto ⭐ / mp4 / pronunciaciones): la aprobación queda en su revisión antes de publicarlo. Residuos limpiados el 17/10/2026; se rehace con `python rehacer.py Capitulo07_Probabilidad`. La caché de voz versionada (`media/voiceovers/`) se volvió a sintetizar después de la subida: un render nuevo es reproducible, pero la voz puede diferir un poco de la del vídeo subido. **Falta**: publicarlo (lo hace el usuario). |
| E3 · La forma del azar | `E3_La_forma_del_azar/` | 09 Variable aleatoria, 10 Acumulada, 11 Densidad, 12 Distribuciones clave | **Subido a YouTube en privado** el 17/10/2026: render final 1080p60 de 8:17, con título, descripción con `capitulos.txt`, subtítulos `.srt`, categoría Educación y «no es para niños» (https://youtu.be/TVyUsukj6qU). Residuos limpiados el 17/10/2026; se rehace con `python rehacer.py Capitulo07_Probabilidad`. La caché de voz versionada (`media/voiceovers/`) se volvió a sintetizar después de la subida: un render nuevo es reproducible, pero la voz puede diferir un poco de la del vídeo subido. **Falta**: publicarlo (lo hace el usuario). |
| E4 · Dos números para resumirlo todo | `E4_Dos_numeros_para_resumirlo_todo/` | 13 Esperanza, 14 Varianza, 15 Chebyshev, 16 Grandes números | **Subido a YouTube en privado** el 17/10/2026: render final 1080p60 de 9:04, con título, descripción con `capitulos.txt`, subtítulos `.srt`, categoría Educación y «no es para niños» (https://youtu.be/tkpbJTO0JOo). Lo subió el usuario sin el visto bueno que figuraba pendiente acá (texto ⭐ / mp4 / pronunciaciones): la aprobación queda en su revisión antes de publicarlo. Residuos limpiados el 17/10/2026; se rehace con `python rehacer.py Capitulo07_Probabilidad`. La caché de voz versionada (`media/voiceovers/`) se volvió a sintetizar después de la subida: un render nuevo es reproducible, pero la voz puede diferir un poco de la del vídeo subido. **Falta**: publicarlo (lo hace el usuario). |
| E5 · Dos variables a la vez | `E5_Dos_variables_a_la_vez/` | 17 Tabla conjunta, 18 Densidad conjunta, 19 Esperanza condicional, 20 Varianza total | **Subido a YouTube en privado** el 17/10/2026: render final 1080p60 de 9:01, con título, descripción con `capitulos.txt`, subtítulos `.srt`, categoría Educación y «no es para niños» (https://youtu.be/yOGhkgYWskI). Lo subió el usuario sin el visto bueno que figuraba pendiente acá (texto ⭐ / mp4 / pronunciaciones): la aprobación queda en su revisión antes de publicarlo. Residuos limpiados el 17/10/2026; se rehace con `python rehacer.py Capitulo07_Probabilidad`. La caché de voz versionada (`media/voiceovers/`) se volvió a sintetizar después de la subida: un render nuevo es reproducible, pero la voz puede diferir un poco de la del vídeo subido. **Falta**: publicarlo (lo hace el usuario). |
| E6 · Lo que una variable sabe de otra | `E6_Lo_que_una_variable_sabe_de_otra/` | 21 Correlación, 22 Covarianza, 23 Cero no es nada, 24 Combinación lineal | **Subido a YouTube en privado** el 17/10/2026: render final 1080p60 de 8:53, con título, descripción con `capitulos.txt`, subtítulos `.srt`, categoría Educación y «no es para niños» (https://youtu.be/MAd5jyBUiaM). Residuos limpiados el 17/10/2026; se rehace con `python rehacer.py Capitulo07_Probabilidad`. La caché de voz versionada (`media/voiceovers/`) se volvió a sintetizar después de la subida: un render nuevo es reproducible, pero la voz puede diferir un poco de la del vídeo subido. **Falta**: publicarlo (lo hace el usuario). |
| E7 · Variables que son flechas | `E7_Variables_que_son_flechas/` | 25 Producto escalar, 26 Espacio vectorial, 27 Rho es coseno, 28 Cauchy-Schwarz, 29 Trampas de rho | **Subido a YouTube en privado** el 17/10/2026: render final 1080p60 de 10:25, con título, descripción con `capitulos.txt`, subtítulos `.srt`, categoría Educación y «no es para niños» (https://youtu.be/-_chXp6KYSo). Lo subió el usuario sin el visto bueno que figuraba pendiente acá (texto ⭐ / mp4 / pronunciaciones): la aprobación queda en su revisión antes de publicarlo. Residuos limpiados el 17/10/2026; se rehace con `python rehacer.py Capitulo07_Probabilidad`. La caché de voz versionada (`media/voiceovers/`) se volvió a sintetizar después de la subida: un render nuevo es reproducible, pero la voz puede diferir un poco de la del vídeo subido. **Falta**: publicarlo (lo hace el usuario). Piezas nuevas en `figuras.py` (cap. 7, E7): `cuadricula7`, `vec7`, `punto7`, `arco7`, `nube7`, `casilla7`, `COL_U7`, `COL_V7` |

- Narración base de ~970–1.370 palabras por episodio (6,5–9 min de voz); con
  gancho y cierre, ~8–10,5 min. E7 es el más largo.
- E1 empieza con el repaso de ~3 min (escenas 01 y 02).
- Ejemplos que vuelven con el **mismo dibujo**: el dado, el canal que confunde
  bits (0,7/0,3 y 10 % de error: Bayes 0,79, tabla 0,63/0,07/0,03/0,27,
  covarianza 0,168, ρ ≈ 0,77), el test médico (vuelve en el Cap. 9), la
  altura y el ejemplo 6, 4, 3 (flechas de √6 y 2, ~52°).
- Bucle a propósito: la escena 16 (E4) usa "las varianzas se suman" y la
  escena 24 (E6) lo demuestra.
- El cierre de E7 anuncia el E1 del capítulo 8 (estimar = proyectar una flecha sobre otra).
- Pronunciaciones a probar antes de sintetizar: Bayes, Chebyshev, Markov, Gauss,
  Cauchy-Schwarz, Fourier y las letras griegas (§9).

### Capítulo 8 (Estimación)

En 5 episodios. `Capitulo08_Estimacion/guion_base.md` tiene la narración de
las 21 escenas, escrita con las pautas de §3 ("Explicar de forma explícita"),
más el reparto, los hilos, los recortes, las pronunciaciones y las piezas
visuales nuevas. Es un capítulo corto en el apunte (115 líneas), por eso son 5
episodios y no 7.

| Episodio | Carpeta | Escenas de `guion_base.md` | Estado |
|---|---|---|---|
| E1 · ¿Cuál es tu mejor apuesta? | `E1_Cual_es_tu_mejor_apuesta/` | 01 Adivinar un número, 02 Probar apuestas, 03 Completar el cuadrado, 04 Otras formas de fallar | `guion.md` con 15 escenas y momentos; escenas `s01`–`s15` animadas; borrador aprobado por el usuario y **render final 1080p60 hecho** (9:06, 1 aviso menor en la escena 8). Falta subirlo a YouTube y limpiar residuos (paso 17). Piezas nuevas en `figuras.py` (cap. 8, E1): `Mesa8`, `ParabolaApuestas8`, `BarrasLlamadas8`, `casilla8` |
| E2 · Lo que el dato te cuenta | `E2_Lo_que_el_dato_te_cuenta/` | 05 La altura otra vez, 06 Media condicional, 07 El estimador es aleatorio, 08 El error sin patrón | `guion.md` con 16 escenas y momentos (`ritmo.py` sin huecos > 4,2 s); escenas `s01`–`s16` animadas; borrador 480p15 aprobado y **render final 1080p60 hecho** (9:09, 0 avisos). Falta subirlo a YouTube y limpiar residuos (paso 17). Antes: borrador de 9:13 (texto ya sin dos puntos en la narración); hojas de contacto revisadas. Se hizo de una tacada («completalo, después lo reviso»): **falta** la revisión del texto ⭐ (gancho, cierre y dos retoques), el visto bueno del usuario al mp4 (paso 15), las pronunciaciones de oído («equis», «i griega», «efe de tres») y el render final. Piezas nuevas en `figuras.py` (cap. 8, E2): `CANAL8`, `puerta8`, `PuntosErr8`, `Nube8`, `parabola8` |
| E3 · ¿Y si solo vale una recta? | `E3_Y_si_solo_vale_una_recta/` | 09 La carpa, 10 El termómetro, 11 La fórmula de la recta, 12 Leer la recta | `guion.md` con 14 escenas y momentos (~9:25); escenas `s01`–`s14` animadas; borrador 480p15: escenas 11–14 sin avisos, escenas 03, 04, 05, 08 y 10 corregidas **sin re-renderizar** (esperar «renderizá»). Falta revisar texto ⭐, hojas de contacto, visto bueno y render final. Piezas en `comun/figuras_cap08_e3.py` (`CarpaE3`, `NubeRhoE3`, `puntos_carpa_e3`, `carpa_mini_e3`) |
| E4 · La sombra de una flecha | `E4_La_sombra_de_una_flecha/` | 13 La sombra, 14 Dos condiciones, 15 Pitágoras, 16 Cuando la recta basta | `guion.md` con 11 escenas y momentos (`ritmo.py` sin huecos > 4,1 s); escenas `s01`–`s11` animadas; borrador 480p15 de 8:52 con **0 avisos** y hojas de contacto revisadas. **Falta**: revisión del texto ⭐ (gancho, cierre y dos retoques, paso 9), visto bueno del usuario al mp4 (paso 15) y render final. Piezas nuevas en `comun/figuras_c8e4.py` (módulo aparte porque otra sesión sobrescribió `figuras.py`; las escenas lo importan): `flechas8`, `en_recta8`, `AnguloVivo8`, `K8`, `ANG8` |
| E5 · ¿Dos termómetros mejor que uno? | *(crear)* | 17 Dos termómetros, 18 Ecuaciones normales, 19 El segundo termómetro, 20 Llega un dato nuevo, 21 De la teoría a los datos | Narración en `guion_base.md`, esperando aprobación |

- Narración base de ~1.150–1.480 palabras por episodio; con gancho y cierre,
  ~9–11 min. **E5 es el más largo**: cierre corto, y si pasa de ~10,5 min, se
  recorta el bloque b1 de la escena 21.
- Ejemplos que vuelven con el **mismo dibujo y los mismos números**: el dado
  (apuestas 3 y 4 → 3,17; 3,5 → 2,92), las llamadas (media 1,7, mediana 1, moda
  0), la altura del Cap. 7 (81,76 → 41,2), el canal de bits del Cap. 7 (0,79 y
  0,045; error 0,084 contra 0,21), la carpa (1/24 contra 1/18) y **el
  termómetro**: temperatura de media 20 y varianza 4, ruido 1; parábola
  4 − 8h + 5h², h = 0,8, error 0,8, apuesta 22,4; flechas 2 y √5 a ~27°; con un
  segundo termómetro de ruido 4, pesos ⅔ y ⅙, error ⅔, apuesta 22,33.
- El termómetro es el **sensor de los Caps. 10 y 12** (media 20, varianza 4,
  ruido 1): la escena 02 del Cap. 12 recuerda este capítulo con h = 0,8 y la
  misma parábola. Por eso la pendiente se llama **h**, no a como en el libro.
- Bucles: la promesa de la escena 20 del Cap. 7 (el error del mejor estimador es
  el primer trozo de la varianza total) se paga en la escena 05; la regla de
  ortogonalidad (08 → 14 → 17); «0,79 no es un bit» (06 → 21 → Cap. 9); la
  actualización con ganancia ⅙ (20 → Kalman del Cap. 12).
- El cierre del E7 del Cap. 7 tiene que anunciar el E1 de este capítulo por su
  título: **«¿Cuál es tu mejor apuesta?»**. El cierre de E5 anuncia el E1 del
  Cap. 9 por su título: **«¿Un cero o un uno?»**.
- La parábola del error de este capítulo no es la de Cauchy-Schwarz: no cambia
  la cuenta de «volverá dos veces más» de la escena 28 del Cap. 7.
- El dibujo de flechas (Y, X, la sombra de Y sobre X y el error a 90°) es el que
  ya usan las escenas 21, 23 y 24 del Cap. 10 y `flechas_xy` del Cap. 12.
- Pronunciaciones a probar: «hache», «be», «i griega sombrero», Pitágoras,
  Kalman, «gaussiano», «veinticuatroavo», «dieciochoavo» (§9). Las siglas MMSE
  y LMMSE no se dicen: solo van en pantalla.

### Capítulo 9 (Pruebas de hipótesis)

En 6 episodios. `Capitulo09_PruebasDeHipotesis/guion_base.md` tiene la
narración de las 28 escenas, escrita con las pautas de §3 ("Explicar de forma
explícita"), más el reparto, los hilos, los recortes, las pronunciaciones y
las piezas visuales nuevas. El apunte es corto (93 líneas), pero el "en
profundidad" trae las demostraciones, los ejemplos y toda la parte de decidir
con datos: por eso son 6 episodios.

| Episodio | Carpeta | Escenas de `guion_base.md` | Estado |
|---|---|---|---|
| E1 · ¿Un cero o un uno? | `E1_Un_cero_o_un_uno/` | 01 Elegir no es estimar, 02 Cuatro reglas, 03 El canal por dentro, 04 Curvas escaladas, 05 Por qué es la mejor | Narración del guion base **aprobada** (con dos retoques en 01·b5 y 02·b6). `guion.md` armado con 14 escenas atómicas, sin momentos. **Falta** la revisión del texto ⭐ (gancho y cierre, paso 9); después momentos y `ritmo.py`. Estimado ~10,5–11 min: si se pasa, recortar la escena 13 b2 (tres hipótesis) |
| E2 · Dos maneras de equivocarse | `E2_Dos_maneras_de_equivocarse/` | 06 Falsa alarma y fallo, 07 El área de la cola, 08 Mover el umbral, 09 El test médico vuelve, 10 La prevalencia manda | `guion.md` con 13 escenas atómicas y momentos (texto ⭐ y narración base aprobados); `ritmo.py` sin huecos de más de 4 s, voz de 10:45. Sigue animar `s01`–`s13` (paso 12). Si se quiere bajar a ~10,5 min, recortar el b3 de la escena 12 |
| E3 · Un número y un umbral | `E3_Un_numero_y_un_umbral/` | 11 Razón de verosimilitud, 12 La cuenta con campanas, 13 Dos umbrales, 14 Sin probabilidades a priori, 15 El presupuesto | Narración base aprobada (con «voltios» en 14·b5). `guion.md` con 16 escenas atómicas (paso 8), sin momentos todavía, ~1.635 palabras (≈ 10:50). **Esperando que el usuario revise el texto ⭐** (gancho, título, cierre y retoque en la escena 04, paso 9). Si pasa de ~10,5 min, recortar el b2 de la escena 09 |
| E4 · La curva de todos los umbrales | *(crear)* | 16 Curva ROC, 17 Leer la curva, 18 La pendiente es el umbral, 19 El punto de Bayes | Narración en `guion_base.md`, esperando aprobación |
| E5 · ¿Cuánto cuesta equivocarse? | *(crear)* | 20 Errores que no cuestan igual, 21 El umbral del riesgo, 22 Riesgo no es error, 23 Decidir y estimar | Narración en `guion_base.md`, esperando aprobación |
| E6 · Decidir con datos de verdad | *(crear)* | 24 ROC con datos, 25 Área bajo la curva, 26 Ordenar no es cortar, 27 Cuántas pruebas, 28 De un número a una señal | Narración en `guion_base.md`, esperando aprobación |

- Narración base de ~1.090–1.520 palabras por episodio (7–10 min de voz); con
  gancho y cierre, ~8,5–11 min. **E1, E2 y E3 son los más largos** (cinco
  escenas): ganchos y cierres cortos, y los recortes candidatos están anotados
  en el guion base (bloques 05·b5, 10·b6 y 13·b6).
- Casi todo el capítulo corre sobre **un solo par de campanas** (centros 0 y 2
  voltios, desvío 1) con los a priori del canal del Cap. 7 (0,7 y 0,3) y la
  medición 1,3. Números que vuelven: alturas 0,17 y 0,31 (razón 1,82); umbral 1
  con a priori iguales (falsa alarma = fallo = 0,159); umbral 1,42 con 0,7/0,3
  (0,077 · 0,28 · error 0,139); razón de verosimilitud e^(2r − 2); falsa alarma
  fija en 5 % → umbral 1,645, detección 0,64; con costes (fallo 5, falsa alarma
  1) → η = 0,47, umbral 0,62, error 0,21, coste 0,31 contra 0,48; área bajo la
  curva 0,92. La medición 1,3 cambia de decisión tres veces (uno, cero, uno).
- Otros ejemplos que vuelven con el **mismo dibujo**: el canal de bits del
  Cap. 7 (las cuatro reglas: 0,10 · 0,30 · 0,70 · 0,90), el test médico del
  Cap. 7 (17 %; con otra prevalencia 2 % · 69 % · 95 %; repitiendo, 80 % y
  99 %), la campana ancha contra la estrecha (umbrales −2,57 y 1,24), la mochila
  de cinco niveles (detección 0,70 contra 0,15) y los ocho casos (área 13/16).
- Bucles: «lo mejor sería no hacer el test» (09 → 20, con promesa explícita de
  «dentro de tres episodios»); «en cada columna, lo que menos falla» (02 → 05);
  mover el umbral cambia un error por otro (08 → 16 → 19 → 22); el presupuesto
  (15 → 18); un número y un umbral (11, 15, 21 → los tres puntos de la 22).
- Paga dos bucles del Cap. 8: «0,79 no es un bit» y «acertar o fallar da la
  moda» (escena 01), y cierra el círculo en la escena 23 (coste cuadrático →
  media condicional).
- El cierre del E5 del Cap. 8 tiene que anunciar **«¿Un cero o un uno?»**. El
  cierre de E6 anuncia el E1 del Cap. 10, «Mil grabaciones del mismo ruido».
- **Para el Cap. 13**: su guion base recuerda este capítulo entero porque se
  escribió antes. Con este guion, sus escenas 01, 02, 10 y 12 pasan a ser
  repaso (mismas palabras: «fallo», «falsa alarma», «la función cu»). No hace
  falta tocarlas, pero pueden acortarse si esos episodios quedan largos.
- Cambios respecto del "en profundidad" (anotados en «Recortes»): a priori
  0,7/0,3 en vez de 0,6/0,4, varianzas distintas con centros 0 y 2, y
  Neyman-Pearson con las campanas en vez de exponenciales. Todo comprobado con
  Python.
- Pronunciaciones a probar: Neyman-Pearson, Bayes, Youden, «hache cero», «pe
  cero», «erre», «eta», «lambda mayúscula», «la función cu», «miss», «curva
  ROC» (§9). Las siglas MAP, AUC, PAM y LRT no se dicen: solo van en pantalla.

### Capítulo 10 (Procesos aleatorios)

En 7 episodios. `Capitulo10_ProcesosAleatorios/guion_base.md` tiene la
narración de las 29 escenas, escrita con las pautas de §3 ("Explicar de forma
explícita"), más el reparto, los hilos, los recortes, las pronunciaciones y
las piezas visuales nuevas. Se escribió antes que los de los Caps. 8 y 9: el
Cap. 8 se recuerda desde el apunte (proyección, ecuaciones normales).

| Episodio | Carpeta | Escenas de `guion_base.md` | Estado |
|---|---|---|---|
| E1 · Mil grabaciones del mismo ruido | `E1_Mil_grabaciones_del_mismo_ruido/` | 01 Señales que no se repiten, 02 Nave de osciladores, 03 Dos miradas, 04 Familia de variables | `guion.md` con momentos y 13 escenas animadas; borrador 480p de 9:08 sin avisos, **esperando el visto bueno del usuario** (paso 15) |
| E2 · ¿Qué recuerda una señal? | `E2_Que_recuerda_una_senal/` | 05 Función media, 06 Autocorrelación, 07 Autocovarianza, 08 Por qué alcanza | `guion.md` (15 escenas atómicas) y escenas `s01`–`s15` escritas. Borrador 480p15 de 9:24, **0 avisos**, hojas de contacto revisadas. Falta: visto bueno del usuario al mp4 (paso 15) y render final |
| E3 · Da igual cuándo mires | `E3_Da_igual_cuando_mires/` | 09 Estacionariedad, 10 Estricta y amplia, 11 Oscilador con fase, 12 Propiedades de R | `guion.md` con 17 escenas y momentos; 17 escenas animadas; borrador 480p15 de 9:33 con 0 avisos; falta el visto bueno del usuario (paso 15) y la revisión ⭐ del gancho y el cierre |
| E4 · ¿Cuánto tarda el azar en olvidar? | `E4_Cuanto_tarda_el_azar_en_olvidar/` | 13 Interruptor, 14 Par o impar, 15 Memoria que se borra, 16 Una sola grabación | Borrador 480p15 renderizado (16 escenas, 9:15, 2 avisos menores); falta el visto bueno del usuario y el render final |
| E5 · ¿Basta con una sola grabación? | `E5_Basta_con_una_sola_grabacion/` | 17 Pilas, 18 Varianza del promedio, 19 Criterio ergódico, 20 Muestra efectiva | 23 escenas animadas; borrador 480p15 de 9:30 con 0 avisos. Falta: revisión del texto ⭐ (gancho, cierre, retoque «capítulo siete» en la escena 08), visto bueno del borrador y render final |
| E6 · Adivinar el futuro, limpiar el presente | `E6_Adivinar_el_futuro_limpiar_el_presente/` | 21 Predicción, 22 Horizonte de predicción, 23 Filtro de una muestra, 24 Ecuaciones normales | Escenas `s01`–`s12` animadas; borrador 480p15 de 9:00, 0 avisos; falta el visto bueno del usuario y revisar el texto ⭐ (gancho y cierre) |
| E7 · ¿Qué le hace un filtro al ruido? | `E7_Que_le_hace_un_filtro_al_ruido/` | 25 Repaso de convolución, 26 Media de salida, 27 Correlación de salida, 28 Varianza de salida, 29 En frecuencia | `guion.md` (17 escenas) y escenas `s01`–`s17` animadas; borrador 480p15 renderizado con 0 avisos (10:21). Falta el visto bueno del usuario (paso 15) y la revisión del texto ⭐ (gancho y cierre); después, render final |

- Narración base de ~1.180–1.390 palabras por episodio; con gancho y cierre,
  ~9–10,5 min. E7 es el más largo.
- Ejemplos que vuelven con el **mismo dibujo y los mismos números**:
  - los cuatro osciladores desfasados (fases 0°, 90°, 180° y 270°;
    R = ½, 0, −½; el rombo);
  - la moneda ±1 (i.i.d., R = impulso);
  - el sensor de temperatura: media 20, varianza 4, × 0,6 por paso. Da la
    parábola con mínimo 2,56, las varianzas del promedio 3,2, 2,72 y 0,725,
    N_eff = 250, la predicción 21,8 y los filtros 0,8 y 0,74/0,12;
  - el interruptor con λ = 1 (0,368 = e⁻¹; el Cap. 11 lo usa con α = 2);
  - las pilas (varianza 4, no ergódicas);
  - el promediador h = (½, ½).
- Bucles:
  - la parábola (12 → 22: su mínimo es el error de predicción);
  - grandes números del Cap. 7 (escena 16) → escenas 16 a 19;
  - "lo demostraremos en el último episodio" (08 → E7);
  - las tres caras de la memoria (19 → 20 → 21).
- La escena 28 del Cap. 7 dice que la parábola «volverá dos veces más», y con
  el Cap. 10 son tres: hay que corregir esa frase.
- El cierre de E7 anuncia el E1 del Cap. 11, «¿En qué frecuencias vive el
  azar?». La escena 29 ya deja dicho que S_yy = |H|² S_xx se parece a la
  densidad espectral de energía.
- Pronunciaciones a probar: ensemble, ergódico, Poisson, factorial, lag,
  i.i.d., FIR, LTI y Wiener, además de las letras (§9).
- E1: el gancho (11 s) y el cierre son texto nuevo, por revisar. «i.i.d.» se sintetizó
  tal cual, sin probar de oído (§9): hay que escucharlo.

### Capítulo 11 (Densidad espectral de potencia)

En 7 episodios. `Capitulo11_DensidadEspectral/guion_base.md` tiene la
narración de las 32 escenas, escrita con las pautas de §3 ("Explicar de forma
explícita"), más el reparto, los hilos, los recortes, las pronunciaciones y
las piezas visuales nuevas. Empalma con el guion base del Cap. 10: retoma su
nombre para la densidad espectral (escena 29 del Cap. 10), la telegráfica
(dos lambda = ancho de banda), las pilas, la moneda, el promediador (½, ½) y el sensor de
temperatura del 0,6 (el eco de las escenas 26 y 27).

| Episodio | Carpeta | Escenas de `guion_base.md` | Estado |
|---|---|---|---|
| E1 · ¿En qué frecuencias vive el azar? | `E1_En_que_frecuencias_vive_el_azar/` | 01 La pregunta, 02 Sin transformada, 03 Potencia esperada, 04 Transformar la autocorrelación, 05 Filtro pasabanda | `guion.md` con 14 escenas y momentos; escenas `s01`–`s14` animadas; borrador 480p15 de 10:17 con 0 avisos; **esperando el visto bueno del usuario** (paso 15) y la revisión ⭐ del gancho y el cierre |
| E2 · Lo que un espectro no puede hacer | `E2_Lo_que_un_espectro_no_puede_hacer/` | 06 Nunca negativa, 07 Real y par, 08 Examen de tres preguntas, 09 Correlación a un paso, 10 Bochner | `guion.md` con 13 escenas atómicas y momentos (gancho y cierre aprobados por el usuario); escenas `s01`–`s13` escritas; `ritmo.py` sin huecos; borrador 480p15 de 10:24 con 0 avisos y hojas de contacto revisadas, **esperando el visto bueno del usuario** (paso 15) |
| E3 · El color del ruido | `E3_El_color_del_ruido/` | 11 Fluctuaciones y media, 12 La cuenta de la telegráfica, 13 Memoria y ancho, 14 Ruido blanco, 15 Las sorpresas del blanco | `guion.md` con 15 escenas y 15 escenas animadas (`s01`–`s15`); borrador 480p15 de 10:10 con 0 avisos; falta el visto bueno del usuario (paso 15) y el render final |
| E4 · Un espectro a partir de datos | `E4_Un_espectro_a_partir_de_datos/` | 16 Periodograma, 17 El desenfoque, 18 Periodograma ruidoso, 19 Promediar trozos | `guion.md` con 11 escenas y momentos; 11 escenas animadas; borrador 480p15 de 8:08 sin avisos, **esperando el visto bueno del usuario** (paso 15) |
| E5 · Cortar sin romper | `E5_Cortar_sin_romper/` | 20 Fuga, 21 Decibelios, 22 Ventanas, 23 Rellenar con ceros, 24 Welch | `guion.md` con 14 escenas; escenas `s01`–`s14` escritas; borrador 480p15 de 9:37 con 0 avisos y sin huecos de ritmo; **falta el visto bueno del usuario al mp4 (paso 15)** y el render final |
| E6 · Fabricar el color y quitarlo | `E6_Fabricar_el_color_y_quitarlo/` | 25 Picos que delatan, 26 Filtro modelador, 27 Filtro blanqueador, 28 Fase mínima | `guion.md` con 13 escenas y momentos; 13 escenas animadas; borrador 480p15 de 8:35 con 0 avisos, hojas de contacto revisadas. Texto ⭐ aprobado; falta el visto bueno del usuario al mp4 (paso 15) |
| E7 · Dos procesos, frecuencia a frecuencia | `E7_Dos_procesos_frecuencia_a_frecuencia/` | 29 Densidad cruzada, 30 Cauchy-Schwarz por frecuencia, 31 Coherencia, 32 La trampa de la coherencia | `guion.md` con 18 escenas y momentos, 18 escenas animadas (`s01`–`s18`); borrador 480p15 de 8:36 con 0 avisos. Falta: revisión del texto ⭐ (gancho y cierre, paso 9) y el visto bueno del usuario al mp4 (paso 15) |

- Narración base de ~1.040–1.370 palabras por episodio (7–9 min de voz); con
  gancho y cierre, ~8–10,5 min. E1 a E3 son los más largos.
- Ejemplos que vuelven con el **mismo dibujo**: la voz y el murmullo (01 → 31),
  la onda telegráfica con α = 2 (densidad 4/(4 + ω²): se usa en la escena 04 y
  se calcula en la 12), las tres barras ρ = 0,4 (espectro 1 + 0,8 cos Ω, filtros
  (2, 1) y (1, 2) entre √5), el eco del 0,6 del Cap. 10 (tabla simulada: 0,60 ·
  0,36 · 0,22 · 0,13 → 0,00 · 0,003 · −0,001 · 0,00), la moneda, los tonos de 50 y
  50,5 Hz.
- Bucles: el rectángulo deslizante (08 → 16), Bochner (10 → 26), la cuenta de la
  telegráfica (04 → 12), la parábola de Cauchy-Schwarz (Cap. 7 → Cap. 10 → escena
  30 → Cap. 13). Ojo: la escena 28 del Cap. 7 dice que la parábola «volverá dos
  veces más», y con el Cap. 10 son tres.
- El cierre del último episodio del Cap. 10 anuncia el E1 de este capítulo. El
  cierre de E7 anuncia el E1 del capítulo 12, «¿Cuál es el mejor filtro?»
  (separar la voz del murmullo = estimar frecuencia por frecuencia).
- Pronunciaciones a probar: Fourier, Parseval, Einstein, Wiener, Khinchin,
  Bochner, Herglotz, Welch, Hann, Blackman, Dirac; «FFT», «sinc», «jota»,
  «hercios», «decibelios» (§9).

### Capítulo 12 (Estimación de señales)

En 7 episodios. `Capitulo12_EstimacionDeSenales/guion_base.md` tiene la
narración de las 29 escenas, escrita con las pautas de §3 ("Explicar de forma
explícita"), más el reparto, los hilos, los recortes, las pronunciaciones, las
piezas visuales nuevas y una tabla de "Números del sensor" (comprobados con
Python). Se resuelve todo con **el sensor de los Caps. 10 y 11** (varianza 4,
0,6 por paso, ruido blanco de varianza 1), no con el sistema de juguete del
"en profundidad": completa lo que el Cap. 10 dejó a mano (h = 0,8 y h ≈ (0,74;
0,12)).

| Episodio | Carpeta | Escenas de `guion_base.md` | Estado |
|---|---|---|---|
| E1 · ¿Cuál es el mejor filtro? | `E1_Cual_es_el_mejor_filtro/` | 01 La pregunta, 02 Proyección otra vez, 03 De variables a procesos, 04 Ecuaciones normales | `guion.md` aprobado (gancho y cierre ⭐ incluidos) con 11 escenas animadas `s01`–`s11`; borrador 480p15 de 9:33 con **0 avisos** y hojas de contacto revisadas, **esperando el visto bueno del usuario** (paso 15) y después render final |
| E2 · Lo que sabe el pasado | `E2_Lo_que_sabe_el_pasado/` | 05 Cuánto pasado hace falta, 06 Yule-Walker, 07 El proceso bandeado, 08 Por qué sirve la vieja | `guion.md` con 11 escenas y momentos; escenas `s01`–`s11` animadas; borrador 480p15 de 8:50 con 0 avisos; falta el visto bueno del usuario (paso 15) y la revisión ⭐ del gancho y el cierre |
| E3 · Mirar el registro entero | `E3_Mirar_el_registro_entero/` | 09 Todo el registro, 10 Una división por frecuencia, 11 Repartir la ganancia, 12 El error y la coherencia, 13 Deshacer el borrón | `guion.md` con 13 escenas atómicas y momentos (gancho y cierre aprobados por el usuario); escenas `s01`–`s13` animadas; borrador 480p15 de 10:30 con 0 avisos y hojas de contacto revisadas, **esperando el visto bueno del usuario** (paso 15) |
| E4 · El futuro no está disponible | `E4_El_futuro_no_esta_disponible/` | 14 Solo para m ≥ 0, 15 Mediciones blancas, 16 Blanquear primero, 17 La fórmula causal | `guion.md` con 20 escenas atómicas y momentos (gancho y cierre aprobados); escenas `s01`–`s20` animadas; borrador 480p15 de 9:10 con 0 avisos y hojas de contacto revisadas, **esperando el visto bueno del usuario** (paso 15) |
| E5 · El sensor, de punta a punta | `E5_El_sensor_de_punta_a_punta/` | 18 El modelador del sensor, 19 La parte causal, 20 El filtro por dentro, 21 El precio de la causalidad | `guion.md` con 12 escenas (texto ⭐ aprobado); escenas `s01`–`s12` animadas; borrador 480p15 de 9:48 con 0 avisos; falta el visto bueno del usuario (paso 15) y el render final |
| E6 · Lo nuevo y lo que ya sabías | `E6_Lo_nuevo_y_lo_que_ya_sabias/` | 22 La innovación, 23 Tirar lo impredecible, 24 Filtrar no es predecir, 25 Los tres sabores | `guion.md` con 17 escenas y momentos; escenas `s01`–`s17` animadas; borrador 480p15 de 8:36 con 0 avisos y hojas de contacto revisadas. Falta la revisión del texto ⭐ (gancho y cierre, paso 9), el visto bueno del usuario al mp4 (paso 15) y el render final |
| E7 · De Wiener a Kalman | `E7_De_Wiener_a_Kalman/` | 26 El sensor como sistema, 27 El observador es el filtro, 28 Sin conocer las correlaciones, 29 Todo es una proyección | `guion.md` con 17 escenas y momentos (texto ⭐ aprobado por el usuario); escenas `s01`–`s17` animadas; borrador 480p15 de 9:45 con 0 avisos y hojas de contacto revisadas. Falta: visto bueno del usuario al mp4 (paso 15), pronunciaciones de oído y render final |

- Narración base de ~1.200–1.480 palabras por episodio (8–10 min de voz); con
  gancho y cierre, ~9–11 min. **E3 es el más largo** (1.480): si al armar su
  `guion.md` pasa de ~10,5 min, la escena 13 (deconvolución) es la candidata a
  recortarse.
- Números que vuelven con el **mismo dibujo**: error sin datos 4; una muestra
  0,8; dos 0,74; FIR largo y filtro causal 0,7386 (coeficientes 0,7386 · 0,1158
  · 0,0182…, cociente 0,157); no causal 0,686 (H = 0,94 · 0,65 · 0,5 en Ω = 0,
  π/2, π); factorización 3,92 − 0,6 (z + 1/z) con raíz 0,157 y varianza de la
  innovación 3,826; predictor 0,443 z⁻¹/(1 − 0,157 z⁻¹) con error 2,826;
  ganancia de Kalman 0,7386 = 2,826/3,826. Además el eco del 0,6 (predicción
  0,6, error 2,56), las tres barras ρ = 0,4 (proceso bandeado: h = (0,476;
  −0,190), error 0,810) y el promediador (½, ½) (deconvolución).
- Bucles: «¿a qué se acerca el error y por qué 0,157?» (05 → 19), «se resuelve
  con una división porque la igualdad vale en todo el eje» (09 → 14), blanquear
  primero (Cap. 11 escena 27 → 16 → Cap. 13), fase mínima con (2, 1) y (1, 2)
  (Cap. 11 escena 28 → 16), la parábola del error (02 → 28), «guarda 0,443 y
  0,157» (24 → 27) y la muestra de ahora vale más que todo el futuro (21 → 25).
- El cierre del último episodio del Cap. 11 tiene que anunciar el E1 de este
  capítulo por su título: **«¿Cuál es el mejor filtro?»**. El cierre de E7
  anuncia el E1 del Cap. 13: **«Más datos no bastan»**.
- La escena 28 del Cap. 7 dice que la parábola de Cauchy-Schwarz «volverá dos
  veces más», y con los Caps. 10, 11 y 13 son más: hay que corregir esa frase.
- Pronunciaciones a probar: Wiener, Kalman, Levinson, Durbin, Toeplitz,
  Yule-Walker, Paley, Riccati, «uve», «omega mayúscula», «épsilon», «innovación»,
  «LMS» (§9).

### Capítulo 13 (Detección de señales)

En 7 episodios. `Capitulo13_DeteccionDeSenales/guion_base.md` tiene la
narración de las 31 escenas, escrita con las pautas de §3 ("Explicar de forma
explícita"), más el reparto, los hilos, los recortes, las pronunciaciones y las
piezas visuales nuevas. Se escribió sin que existan los guiones base de los
Caps. 8, 9 y 12: lo del capítulo 9 (hipótesis, MAP, ROC, Neyman-Pearson) se
recuerda entero dentro del guion, y del 12 solo se nombran Wiener y la
proyección.

| Episodio | Carpeta | Escenas de `guion_base.md` | Estado |
|---|---|---|---|
| E1 · Más datos no bastan | `E1_Mas_datos_no_bastan/` | 01 El radar, 02 Una medición, 03 Dos mediciones, 04 Promediar destruye | `guion.md` con 12 escenas y momentos; escenas `s01`–`s12` animadas; borrador 480p15 de 8:44 con 0 avisos y hojas de contacto revisadas. Falta la revisión del texto ⭐ (gancho y cierre, paso 9), el visto bueno del usuario al mp4 (paso 15) y el render final |
| E2 · Toda la señal en un solo número | `E2_Toda_la_senal_en_un_solo_numero/` | 05 Señal conocida, 06 La cuenta, 07 El umbral, 08 Un número que basta | `guion.md` con 11 escenas y momentos; escenas `s01`–`s11` animadas; borrador 480p15 de 9:15 con 0 avisos y hojas de contacto revisadas. Falta: revisión del texto ⭐ (gancho, cierre, retoque en la escena 10), visto bueno del usuario al mp4 (paso 15) y render final |
| E3 · ¿Cuánto nos equivocamos? | `E3_Cuanto_nos_equivocamos/` | 09 Dos campanas, 10 Función Q, 11 El prior, 12 Curva ROC, 13 Solo la energía | `guion.md` con 13 escenas y momentos; escenas `s01`–`s13` animadas; borrador 480p15 de 11:20 con 0 avisos, hojas de contacto de todas las escenas revisadas. **Falta la revisión del texto ⭐** (gancho, cierre y retoque «priors» → «probabilidades» en la escena 12) y el visto bueno del usuario al mp4 (paso 15); el render salió largo (11:20): candidato a recorte, el bloque b3 de la escena 12 |
| E4 · El filtro que es la señal al revés | `E4_El_filtro_que_es_la_senal_al_reves/` | 14 El filtro al revés, 15 El pico es la autocorrelación, 16 La lectura en frecuencia, 17 Nadie la supera, 18 Cuánto se pierde | `guion.md` con 19 escenas y momentos; escenas `s01`–`s19` animadas; borrador 480p15 de 10:36 con 0 avisos y hojas de contacto revisadas. Falta la revisión del texto ⭐ (gancho y cierre, paso 9), el visto bueno del usuario al mp4 (paso 15) y el render final. Piezas nuevas en `figuras.py` (cap. 13, E4): `S13`/`H13`/`R13`/`SAL13`/`AUT13`, `valores_sobre13`, `CasillasSalida13`, `alarma13`, `interrogante13`, `cos13` |
| E5 · Cuando el ruido tiene memoria | `E5_Cuando_el_ruido_tiene_memoria/` | 19 La memoria del ruido, 20 Blanquear y adaptar, 21 Dónde viva la señal, 22 Ruido en la práctica | `guion.md` con 12 escenas y momentos; escenas `s01`–`s12` animadas; borrador 480p15 de 8:42 con 0 avisos y hojas de contacto revisadas. **Falta el visto bueno del usuario al texto ⭐** (gancho, cierre y dos retoques, paso 9) y al mp4 (paso 15); después render final |
| E6 · ¿Cuándo llegó el eco? | `E6_Cuando_llego_el_eco/` | 23 El eco que llega, 24 Pulso que se comprime, 25 Chirp y resolución, 26 Buscar tiene precio | `guion.md` con 22 escenas atómicas; escenas `s01`–`s22` animadas; borrador 480p15 de 8:45 con 0 avisos. Falta la revisión del texto ⭐ (gancho y cierre, paso 9), el visto bueno del usuario al mp4 (paso 15) y el render final |
| E7 · ¿Cuál de ellas mandaron? | `E7_Cual_de_ellas_mandaron/` | 27 Varias señales, 28 La diferencia, 29 Antipodal gana, 30 Receptor de módem, 31 El mapa del curso | `guion.md` con 19 escenas; escenas `s01`–`s19` animadas; borrador 480p15 de 11:05 con 0 avisos. Falta la revisión del texto ⭐ (gancho y cierre de la serie, paso 9), el visto bueno del usuario (paso 15) y el render final |

- Narración base de ~1.100–1.490 palabras por episodio (7–10 min de voz); con
  gancho y cierre, ~8–10,5 min. E3, E4 y E7 son los más largos y admiten recortes.
- Un solo ejemplo atraviesa el capítulo, con **el mismo dibujo y los mismos
  números**: el pulso `s = (2, 2, 1)` con `σ² = 1` y energía 9 (umbral 4,5, dos
  campanas en 0 y 9 con desvío 3, `P_e` = 0,0668, filtro `(1, 2, 2)` con salida
  `(3, 7, 10, 6, 4)` y autocorrelación `(2, 6, 9, 6, 2)`, las tres señalizaciones
  0,0668 · 0,0170 · 0,00135). Se le suman las dos mediciones uniformes del E1
  (1/4, 3/16, 1/4), el eco del 0,6 del Cap. 11 con dos muestras (E5: `(2, 0)`,
  varianza 0,64, `d²` 6,25 frente a 4), Barker-13 y el rectángulo de 13 (E6) y tres
  señales de energía 2 (E7).
- Bucles: «más datos no bastan» (E1 → escena 08 → 18), «la forma no importa solo la
  energía» (13 → se matiza a propósito en la 21), el pico como autocorrelación (15 →
  23 a 25), buscar cuesta (23 → 26), y **la parábola de Cauchy-Schwarz**: es su
  **cuarta aparición** (Caps. 7, 10 y 11, y la escena 17 de este). Ojo: la escena 28
  del Cap. 7 dice que «volverá dos veces más», y son tres.
- El E1 lo anuncia el cierre del último episodio del Cap. 12 (ya tiene guion base, y su
  escena 29 termina con ese título): su cierre tiene que anunciar «Más datos no bastan». El cierre de E7 cierra
  **toda la serie** (no anuncia nada).
- Una **inconsistencia del apunte** anotada en el guion base: la tabla de la Parte
  2.3 del "en profundidad" da 0,889 para «una muestra» con `(2, 2, 1)`; el valor
  correcto es 4/9 = 0,444 (−3,52 dB), como dice la Parte 1.4. El guion usa 0,444.
- Pronunciaciones a probar: Neyman-Pearson, Cauchy-Schwarz, Barker, Nyquist, Wiener,
  Bayes, «la función cu», «curva ROC», «miss», «chirp», «coseno alzado» (§9).

---

## 2. Flujo de trabajo

Tres fases. Hay tres puntos donde se frena a esperar al usuario (🟡).

### Fase A — Guion base del capítulo (`Capitulo<NN>_<Tema>/guion_base.md`)

Se hace una vez por capítulo, antes de cualquier episodio. Hay un agente
preparado para esto: `.claude/agents/redactor-guion-base.md`.

1. **Leer las fuentes**, en este orden:
   - la sección del capítulo en `../Apuntes/PROCESAMIENTO DE SEÑALES.md` (líneas en §1);
   - `../Apuntes/PROCESAMIENTO DE SEÑALES - Cap NN en profundidad.md` (demostraciones,
     ejemplos numéricos, "intuición y conexiones");
   - el libro (`../Libros/Signals, Systems  Inference.pdf`) solo para dudas puntuales;
   - las figuras de `../Apuntes/imagenes/` (`cNN-*.svg`, `cNNp-*.svg`) como ideas visuales;
   - el `guion_base.md` del capítulo anterior (sus hilos y su cierre).
2. **Decidir el reparto en episodios**: los que hagan falta para explicarlo
   todo de forma explícita (§3), sin comprimir; el Cap. 7 quedó en 7. Cada
   episodio de ~10 min lleva de 4 a 5 escenas de guion base de ~1,5–2 min
   (~250–300 palabras) y ~1.050–1.250 palabras de narración base. Cada episodio
   tiene una **idea fuerza** de una línea.
3. **Escribir cada escena** con el formato de §5: Objetivo, qué hace falta
   saber antes, Visual y Narración en bloques `<!-- bN -->`.
4. **Registrar** los hilos que cruzan el capítulo, los recortes decididos y
   las pronunciaciones a probar.
5. **Actualizar §1** de este README (fila del capítulo y subsección nueva).
6. 🟡 **El usuario aprueba el guion base, episodio por episodio.** Mientras no
   esté aprobado, todo ajuste de texto se hace en el guion base primero.

### Fase B — Guion del episodio (`Capitulo<NN>_<Tema>/E<N>_<nombre_corto>/guion.md`)

7. **Crear la carpeta** del episodio.
8. **Armar el `guion.md`** (formato en §6):
   - copiar la narración de las escenas del guion base que le tocan;
   - partir en **escenas atómicas** de 30–90 s (en concurrente, 3 escenas de
     guion base se volvieron 9–14 escenas atómicas);
   - escribir un **gancho** de 5–15 s (escena 01) y un **cierre** que anuncie el
     episodio siguiente (última escena), marcados con ⭐ en las notas;
   - ajustar las frases que ya no aplican al formato por episodios (por ejemplo,
     "en la próxima escena" → "más adelante");
   - poner `**Capítulo YouTube:**` en cada escena.
9. 🟡 **El usuario revisa el texto nuevo** (gancho, cierre y retoques). Mostrar solo eso, marcado.
10. **Escribir los momentos** de cada bloque: uno cada ~2–3 s de voz, describiendo qué se ve.
11. **Validar el guion y medir el ritmo:** `python ritmo.py <carpeta_episodio>` (§8).
    Agregar momentos hasta que ningún tramo pase de ~4 s.

### Fase C — Animación y entrega

12. **Escribir las escenas** `sNN_<nombre>.py` (§7). Reutilizar `iconos.py` y
    `figuras.py`, y sumar ahí los íconos o piezas nuevos (no dentro de la escena).
13. **Renderizar el borrador** (480p15): `python render.py <carpeta_episodio>`. Arreglar
    todos los **avisos de los controles** (§8).
14. **Revisar a ojo** con hojas de contacto (§8): huecos, tamaños, fórmulas
    ilegibles, cosas que no se entienden, rellenos macizos. Arreglar y volver a
    renderizar solo esas escenas (`--escenas 03,07`) y después `--solo-unir`.
15. 🟡 **Mandar el mp4 al usuario** y esperar su visto bueno o sus comentarios.
16. **Render final:** `python render.py <carpeta_episodio> --calidad qh`. Entregar el mp4,
    el `.srt` y `capitulos.txt` de `salida/`.
17. **Subir a YouTube y limpiar** (antes de pushear al repositorio):
    - subir el mp4 de 1080p a YouTube (título, descripción con `capitulos.txt`);
      - **título** (lo pidió el usuario): primero el tema principal tal como alguien
        lo buscaría, después el episodio: `<Tema buscable> - Ep N <Título del episodio>`.
        Ej.: `Probabilidad condicional y regla de Bayes - Ep 2 Cuando sabes algo más`.
        El E1 del Cap. 7 es `Introducción al procesamiento de señales - Ep 1 …`;
      - **descripción**: arranca aclarando el libro, «Vídeo basado en el capítulo N
        («<título del capítulo en inglés>») del libro «Signals, Systems & Inference», de
        Alan V. Oppenheim y George C. Verghese.», sigue con «Procesamiento de Señales ·
        Capítulo N, <Tema> · Episodio K de M.» y cierra con «Capítulos:» y `capitulos.txt`;
      - subtítulos: el `.srt` de `salida/` (idioma Español (España)); categoría
        Educación; «no es para niños»; visibilidad la que diga el usuario (Cap. 7: privado);
    - verificar en Studio que quedó subido y procesado (duración correcta, 1080p);
    - **limpiar los residuos**: borrar `salida/`, `__pycache__/`, `render.log`,
      `lista.txt` y todo `media/` **menos `media/voiceovers/`** (la caché de voz).
      Lo borrado es regenerable y está en `.gitignore`;
    - **la caché de voz no se borra nunca: va al repositorio.** Azure no sintetiza dos
      veces el mismo audio, así que sin ella el vídeo cambia (tiempos, entonación).
      Con ella, el render no sintetiza nada y sale el mismo vídeo;
    - dejar el episodio **listo para rehacerse con un solo comando**:
      `python rehacer.py <Capitulo> [E<N>]` (llama a `render.py --calidad qh` por cada
      episodio). Quedan `guion.md`, las escenas `sNN_*.py` y `media/voiceovers/`, y
      cualquier pieza compartida nueva va en `comun/` (que también va al repositorio);
    - recién entonces `git add`, commit y push, y anotar en §1 que está subido.

    Los vídeos nunca van al repositorio: el código y la caché de voz son la fuente y
    el mp4 se regenera. Entorno con las versiones exactas: `requirements.txt` (§10);
    la clave de Azure (`.env`, ver `.env.example`) solo hace falta para voz nueva.

**Después de cada paso, actualizar §1** (fila del episodio) y la línea
`**Estado:**` del `guion.md` o `guion_base.md`. Un chat nuevo decide qué hacer
leyendo solo eso: si el estado quedó viejo, el chat siguiente repite o salta trabajo.

---

## 3. Pautas de contenido

### Tono
- **Narrado como historia**, no como lista de definiciones: se arranca de un
  caso, una pregunta o una imagen concreta y desde ahí se llega al concepto.
- **Metáforas cotidianas** (usar estas y mantenerlas en todo el curso):
  - señal aleatoria = un fenómeno del que conoces las reglas pero no el resultado (el dado, la lluvia);
  - ruido = el murmullo de fondo que tapa la voz;
  - ensemble = mil grabaciones del mismo fenómeno, una encima de otra;
  - filtro = un colador que deja pasar unas frecuencias y retiene otras;
  - estimar = adivinar lo mejor posible con lo que se ve; detectar = decidir sí o no;
  - variable aleatoria como vector = una flecha; correlación = el ángulo entre dos flechas.
- **No se resuelven los Ejercicios Propuestos**: eso es de los solucionarios.
  Los ejemplos numéricos del vídeo salen del apunte o del complemento, o se
  inventan con números redondos.
- Se habla en primera persona del plural ("veamos", "imaginemos") y de tú
  cuando se interpela ("puedes tirar el dado mil veces").

### Explicar de forma explícita (lo que más pide el usuario)
La primera versión del guion del Cap. 7 no le gustó al usuario por **poco
explícita** y por **dar cosas por sabidas**. Estas reglas son el estándar:

1. **Cada concepto nuevo sigue el mismo camino**, sin saltarse pasos:
   1. una pregunta o un caso concreto ("tiras un dado y te dicen que salió par");
   2. **la cuenta hecha a mano con números pequeños**, en voz alta y en
      pantalla ("quedan tres caras: un tercio");
   3. el dibujo que lo muestra;
   4. recién entonces **la fórmula, como resumen** de lo que ya se hizo, leída
      término a término y diciendo qué significa cada pieza;
   5. una comprobación: la fórmula aplicada al mismo ejemplo da lo mismo que la cuenta.
2. **No dar nada por sabido, tampoco de matemáticas.** La primera vez que
   aparece una herramienta, se explica en una o dos frases con su dibujo:
   derivada = pendiente, integral = área (suma de rectángulos finos),
   sumatoria, vector y producto escalar, parábola y discriminante, números
   complejos, logaritmos, decibelios… Lo que venía de Señales y Sistemas o de
   Probabilidad y Estadística se recuerda **donde se usa**, no se supone.
3. **Las deducciones cortas se hacen enteras**, un paso por renglón, y la voz
   dice qué regla se usa en cada paso ("desarrollamos el cuadrado", "por
   linealidad", "como la esperanza de equis es mu"). Si una demostración es
   larga, se hace el paso clave y se dice qué se salta y dónde está (el apunte
   "en profundidad"). Nunca "se puede demostrar que" sin más.
4. **Ejemplos que vuelven.** Pocos ejemplos, reutilizados con el mismo
   dibujo y los mismos números a lo largo del capítulo (y entre capítulos): así
   cada concepto nuevo se aplica a algo que quien mira ya entiende. Anotarlos en
   "Hilos" del guion base.
5. **Advertir las trampas**: lo que se confunde siempre se dice explícitamente
   ("la esperanza del producto no es el producto de las esperanzas", "covarianza
   cero no es independencia", "la densidad no es una probabilidad").
6. **Dinámico, no lento.** Explícito no quiere decir pesado: bloques cortos,
   un cambio visual cada pocos segundos, y recursos para que quien mira
   participe:
   - **preguntas con pausa** antes de revelar ("piénsalo un momento antes de seguir");
   - **predicción y sorpresa** (el test médico: casi todos dicen 99 %, y es 17 %);
   - **encuestas visuales** (varias respuestas en pantalla, se tacha las falsas);
   - **bucles** anunciados y pagados ("esto lo demostraremos en dos episodios").
7. **Una promesa pendiente se paga siempre**, y en el sitio anunciado.

### Repaso de materias previas
El E1 del Cap. 7 abre con un repaso de ~3 minutos, **muy por encima**, de
Señales y Sistemas (señal, continua y discreta, sistema lineal e invariante,
Fourier y filtros) y de Probabilidad y Estadística (experimento, probabilidad
como frecuencia, variable aleatoria, distribución, media). Es solo para
ubicar: todo lo que se necesite de verdad se vuelve a explicar con calma
(regla 2) en el capítulo que lo usa. No se hacen episodios de repaso aparte.

### Castellano de España (obligatorio en lo narrado)
| No | Sí |
|---|---|
| voseo: podés, fijate, tenés | tuteo: puedes, fíjate, tienes |
| acá | aquí |
| computadora (¡ojo al género!: *un* ordenador) | ordenador |
| chico/chiquito (= pequeño) | pequeño |
| video | vídeo |
| celular | móvil |
| manejar (un coche) | conducir |
| "o ordenadores" | "u ordenadores" (o → u antes de o-) |
| "decibeles" | "decibelios" |

Al reemplazar palabras, **revisar la concordancia** de artículos y adjetivos.
Ojo: el apunte está escrito en rioplatense ("tomá", "fijate", "chico"): **no copiar
frases del apunte sin pasarlas a castellano de España**.

### Estructura de un episodio (~10 min, ~1.300–1.500 palabras)
1. **Gancho** (5–15 s): lo más fuerte del episodio (un resultado sorprendente,
   una pregunta, un número). Después, el título solo (≤2 s).
2. Escenas atómicas, cada una con su capítulo de YouTube.
3. **Bucles abiertos**: anunciar lo que viene y pagarlo después.
4. **Micro-recompensa** al final de cada escena: una idea en una línea.
5. **Cierre**: resumen corto + la pregunta que abre el episodio siguiente.

---

## 4. Pautas visuales y de ritmo

### Retención
1. **Cambio visual cada 2–4 s**: algo aparece, se mueve, hace zoom o cambia de color.
2. **Cada frase se ve**: si la voz dice "mil grabaciones", aparecen muchas curvas apiladas.
3. **A veces manda la animación**: el dibujo va primero y la voz lo explica.
4. **Tipografía cinética**: la palabra clave aparece de golpe (`pop`) cuando se dice.
5. **Un plano, una idea**: nada de título + subtítulo apilados ni rótulos de relleno.
6. **Cortes secos** (`corte()`) para cambiar de idea; fundidos (`limpiar()`) al cerrar una escena.
7. **Sonido**: efectos cortos en los momentos clave, siempre por debajo de la voz.
8. **Tensión y continuidad**: retomar elementos de escenas y capítulos anteriores
   con el **mismo dibujo** (la misma campana, el mismo par de flechas).

### Gráficas y fórmulas (propio de esta materia)
- **Las gráficas se animan, no se muestran**: la curva se dibuja (`Create`), el
  área se rellena, un parámetro se mueve con un `ValueTracker` y la curva
  cambia en vivo. Una gráfica quieta más de ~4 s es un hueco.
- **Muestras aleatorias**: con semilla fija (`np.random.default_rng(semilla)`),
  para que el render sea siempre igual.
- **Fórmulas**: con `formula(...)` de `estilo.py`, partidas en piezas, y cada
  pieza aparece cuando la voz la nombra. Se colorean con los papeles fijos.
  Una fórmula en pantalla no pasa de ~2/3 del ancho; si es más larga, se parte.
- **Papeles fijos de color** (en `estilo.py`; el mismo objeto, el mismo color en todo el curso):
  - `SENAL` (azul) = la señal o variable que interesa;
  - `RUIDO` (magenta) = el ruido o lo que molesta;
  - `MEDIDA` (cian) = lo observado (señal + ruido);
  - `ESTIMACION` (ámbar) = la estimación o la decisión;
  - `ERROR` (rojo) = el error, la probabilidad de equivocarse.
- Y los de siempre: `AMBAR` = el concepto que se está presentando, `VERDE` =
  correcto, `INK` = secundario (ejes), `TXT` = texto principal.

### Ritmo técnico
- Animaciones de **0,3–1,5 s**. **Nunca** estirar una animación a `t.duration`
  para "llenar": se ancla y después queda quieta o con `flotar()`. Excepción:
  movimientos continuos (zoom lento, un `ValueTracker` que barre, un contador),
  que pueden durar `self.margen()`.
- **Densidad**: un momento cada ~2–3 s de voz. Se acepta hasta ~4 s si adentro
  corre una animación de ≥1 s.
- La voz va a ~150 palabras/min (con `VELOCIDAD = "-5%"`). Pasarse un poco de 10 min está bien.
- ~1 s de respiro al final de cada escena (`self.wait(1.0)` antes de `limpiar()`).

### Estética
- Fondo `#12141a`. Paleta en `comun/estilo.py` (la misma de las figuras del apunte).
- Tipografía **Segoe UI** (sans) para texto, LaTeX (`MathTex`) para fórmulas y
  **Consolas** si alguna vez hace falta código.
- **Tamaños**: el elemento principal ocupa el **40–70 % del alto** (la pantalla
  mide 14,2 × 8 unidades). En el borrador de 480p lo chico no se ve: una
  fórmula con `escala` < 0,8 suele ser ilegible.
- Íconos planos y geométricos, propios (`comun/iconos.py`). **No se descargan imágenes.**
- **Todo texto que se escribe en pantalla empieza con mayúscula** («Test», «Sano», «Regla del producto»), también las etiquetas sueltas y las cajas. Las palabras dentro de una fórmula (`	ext{par}`) siguen como van en la matemática.
- Números en formato español: `1000` o `1.000`, `0,34` (nunca `1,000` ni `0.34`).
  En texto, `num(0.34)`; en `MathTex`, `num_tex(0.34)` → `0{,}34`.

---

## 5. Formato del `guion_base.md`

Uno por capítulo, en `Capitulo<NN>_<Tema>/guion_base.md`. **No se renderiza**:
es la fuente de texto de todos los episodios del capítulo. Plantilla:

```markdown
# Capítulo NN — Tema

> **Guion base: narración de todo el capítulo. No se renderiza.**
> Es la fuente de texto para los N episodios (ver `../README.md` §1). Cada
> episodio copia de aquí su narración a su propio `E<N>_.../guion.md`, que es
> el que lleva gancho, cierre y momentos, y el que se anima. Las secciones
> "Visual" son ideas iniciales, no especificación.
>
> **Estado:** narración completa, **esperando la aprobación del usuario**.
> Mientras no esté aprobada, cualquier ajuste de texto que pida el usuario se
> hace aquí primero, y después se copia al `guion.md` del episodio.

Fuentes: apunte (líneas X–Y), "en profundidad" (partes que se usan), figuras.
Qué se da por sabido de capítulos anteriores. Convención y tono (una línea).

## Reparto en episodios

| Episodio | Escenas | Idea fuerza |
|---|---|---|
| E1 · Título | 01 NombreClase, 02 …, 03 … | una línea |

(El gancho y el cierre de cada episodio NO están aquí: se escriben al armar
el `guion.md` del episodio. Cada cierre anuncia el episodio siguiente por su título.)

## Hilos que cruzan el capítulo

- **Nombre del hilo**: se abre en la escena X (E1) y se paga en la escena Y (E3).
- **Ejemplo que vuelve**: se presenta en X; tiene que ser el mismo dibujo en Y.
- **Puentes a otros capítulos**: qué se siembra aquí para el capítulo Z.
- **Cierre del capítulo**: qué pregunta abre el capítulo siguiente.

## Recortes decididos

Qué no entra o solo se menciona (y por qué, si no es obvio).

## Pronunciación

Palabras a probar de oído antes de sintetizar (§9): nombres, siglas, letras griegas.

## Piezas visuales nuevas

Qué hay que sumar a `figuras.py` / `iconos.py` antes de animar.

---

# Escena 01 — NombreClase

**Objetivo:** qué tiene que entender quien mira al terminar la escena.

**Qué hace falta saber antes:** escenas o capítulos previos (para no dar nada por sabido).

**Visual:**
- ideas de qué se ve, en viñetas (no es especificación: los momentos del
  `guion.md` son la especificación).

## Narración

<!-- b1 -->
Texto que se lee en voz alta, en castellano de España, con las fórmulas
dichas en palabras (§9)...

<!-- b2 -->
...

---

# Escena 02 — OtraClase
...
```

Reglas:
- `NombreClase` en CamelCase: es el nombre de la clase de Manim.
- Bloques de 10–30 s de voz (~25–75 palabras). Cada bloque, una sola idea.
- Cada escena del guion base dura ~1,5–2 min (~250–300 palabras, 4–6 bloques):
  al pasar al `guion.md` queda como una o dos escenas atómicas.
- Cada escena respeta el camino de §3 ("Explicar de forma explícita"): caso,
  cuenta a mano, dibujo, fórmula, comprobación. El "Visual" dice qué cuenta y
  qué deducción se ven en pantalla, renglón por renglón.
- Ejemplo real de referencia: `Capitulo07_Probabilidad/guion_base.md`.

---

## 6. Formato del `guion.md`

Uno por episodio, en `Capitulo<NN>_<Tema>/E<N>_<nombre_corto>/guion.md`.

```markdown
# Episodio 1 — Título del episodio

Capítulo 7 (Modelos probabilísticos), episodio 1 de N. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 01 a 03), más un gancho y un cierre nuevos.

**Estado:** (qué paso del §2 está hecho y cuál sigue)

Texto nuevo, para revisar (marcado con ⭐):
- Escena 01 (gancho): …
- Escena NN (cierre): anuncia E2, «Título de E2».

---

# Escena 03 — Bayes

**Capítulo YouTube:** La regla de Bayes
**Objetivo:** (opcional) qué tiene que entender quien mira

## Narración

<!-- b1 -->
Un test da positivo. ¿Cuál es la probabilidad de que estés enfermo?
La respuesta sorprende: depende de cuánta gente tiene la enfermedad.

- «Un test da positivo» → `test`: el test entra con un «+» en rojo
- «¿Cuál es la probabilidad» → `pregunta`: aparece «P(enfermo | +) = ?»
- «cuánta gente» → `poblacion`: una grilla de cien personas, dos en rojo

<!-- b2 -->
...
```

Reglas (`comun/guion.py` las valida y falla con un mensaje claro si no se cumplen):
- `# Escena NN — NombreClase`: `NN` es el orden en el vídeo y el archivo
  `sNN_*.py`; `NombreClase` es la clase de Manim dentro de ese archivo.
- `**Capítulo YouTube:**` es el título de esa marca en `capitulos.txt`.
- Bloques `<!-- b1 -->`, `<!-- b2 -->`…: cada uno es una sola síntesis de voz.
  Conviene partir en bloques de 10–30 s.
- **Momentos**: `- «frase» → \`marca\`: descripción`
  - la frase aparece **literal** en la narración del bloque (con tildes y signos,
    ej. «¿cuál es?»);
  - los momentos van **en el orden** en que se dicen; se busca desde el momento
    anterior (cuidado con palabras repetidas);
  - la marca es `[a-z0-9_]` (**siempre minúsculas**, ver §10) y no se repite dentro del bloque;
  - la descripción es para humanos: dice qué se ve (sirve de especificación de la escena).
- Las líneas de momentos no se leen en voz alta. `---` separa escenas.

---

## 7. Arquitectura del código y API

```
Animaciones/
├── README.md, CLAUDE.md    documentación (CLAUDE.md solo apunta aquí)
├── render.py               renderiza un episodio: escenas → mp4 + srt + capitulos.txt
├── ritmo.py                linter de ritmo: cuándo cae cada momento y qué huecos quedan
├── comun/                  código compartido por todas las escenas
│   ├── escena.py           EscenaCurso: clase base (voz, marcas, sonido, cámara, controles)
│   ├── guion.py            parser del guion.md (narración + momentos → bookmarks)
│   ├── voz.py              servicios de voz (Azure Speech y edge-tts) para manim-voiceover + VOZ y VELOCIDAD del curso
│   ├── pronunciacion.py    reemplazos que solo afectan al audio
│   ├── sfx.py              efectos de sonido sintetizados con numpy
│   ├── estilo.py           paleta, papeles de color, fuente, caja(), flecha(), ejes(), formula(), num()
│   ├── iconos.py           pictogramas (personas, objetos, máquinas, marcas)
│   └── figuras.py          piezas técnicas (curvas, densidades, espectros, bloques)
├── sfx/                    wav generados por sfx.py (se regeneran solos; ignorado en git)
├── musica/                 opcional: una pista de fondo (YouTube Audio Library); render.py la mezcla
├── voces_prueba/           scripts para elegir pronunciaciones de oído
└── Capitulo07_Probabilidad/
    ├── guion_base.md       narración de todo el capítulo (fuente de texto)
    └── E1_<nombre_corto>/
        ├── guion.md        guion del episodio (orden, narración y momentos)
        ├── s01_gancho.py … sNN_cierre.py   una escena por archivo
        ├── media/          salida de Manim, caché de voz, informes (ignorado en git)
        └── salida/         episodio final: mp4, srt, capitulos.txt (ignorado en git)
```

**Cómo fluye todo:** `render.py` lee el orden de `guion.md` y corre Manim
escena por escena. Cada escena es una `EscenaCurso`, que carga su parte del
guion (`guion.py`), inserta las marcas (`<bookmark/>`) y aplica la
pronunciación. Después sintetiza cada bloque con el motor de voz (`voz.py`, con caché
y tiempos por palabra), anima esperando cada marca con `en()` y, al terminar,
escribe un informe de controles. Al final, `render.py` concatena, une los
subtítulos, genera los capítulos y resume los informes.

### Una escena

```python
"""Escena 04 — Gaussiana: la campana y sus dos parámetros."""
from comun.escena import *          # manim + EscenaCurso + paleta + iconos + figuras


class Gaussiana(EscenaCurso):
    ESCENA = "04"                    # número en el guion.md de esta carpeta

    def construct(self):
        self.campana()               # un método por bloque, si la escena es larga
        self.wait(1.0)
        self.limpiar()

    def campana(self):
        with self.narrar("b1"):                      # voz del bloque b1
            self.en("curva")                         # espera a «la campana» (−0,3 s)
            c = Curva(gaussiana, x_rango=(-4, 4), y_max=0.5, x_label="x", y_label="f_X(x)")
            self.play(Create(c.ejes), run_time=0.5)
            self.play(Create(c.grafica), run_time=1.0)

            self.en("media")                         # «su centro»
            f = formula(r"\mu", "=", "0", colores={0: AMBAR}).next_to(c, UP)
            self.pop(f)                              # entrada con rebote + sonido

            self.en("cola")                          # «la cola»
            self.play(FadeIn(c.area(2, 4, ERROR)), run_time=0.5)
        # al salir del with, espera a que termine el audio del bloque
```

### `EscenaCurso` (`comun/escena.py`)
| Método | Para qué |
|---|---|
| `narrar(bloque)` | context manager: reproduce la voz del bloque con sus marcas |
| `en(marca)` | espera hasta la frase anclada (0,3 s antes: `ANTICIPO`) y anota si llegó tarde |
| `margen()` | segundos disponibles hasta la próxima marca (para dimensionar animaciones continuas) |
| `dur(x)` | `run_time` de `x` s como mucho, sin pasarse de la próxima marca (evita los atrasos) |
| `sfx(nombre, gain=-14, offset=0)` | efecto de sonido ahora (o `offset` s después) |
| `pop(*mobs, sonido="pop")` | entrada con rebote (tipografía cinética) |
| `palabra(txt, color, escala)` | palabra clave en negrita, lista para `pop` |
| `texto_centrado(*lineas)` | varias líneas centradas entre sí |
| `resaltar(*mobs, color)` | resalta agrandando y coloreando **solo el borde** (usar en vez de `Indicate`) |
| `flotar(m)` | movimiento sutil mientras sigue la voz (llamar `m.clear_updaters()` antes de moverlo) |
| `rafaga(teclas)` | teclas que se encienden en ráfaga, con tecleo |
| `corte(*mantener)` | corte seco a plano nuevo (vacía la escena) |
| `limpiar()` | fundido de todo |
| `fuera(*mobs)` | salida rápida |
| `zoom(obj, ancho)` / `zoom_reset()` | cámara (`self.camera.frame` también se puede animar directo) |

### Estilo (`comun/estilo.py`)
- Paleta: `INK`, `AZUL`, `AMBAR`, `VERDE`, `MAGENTA`, `ROJO`, `CIAN`, `TXT`, `FONDO`;
  papeles: `SENAL`, `RUIDO`, `MEDIDA`, `ESTIMACION`, `ERROR` (§4).
- `ejes(x_rango, y_rango, ancho, alto, x_label, y_label)` → `(Axes, etiquetas)`; etiquetas en `MathTex`.
- `formula(*partes, escala, colores={i: color})`: `MathTex` partido en piezas `f[i]`.
- `num(x)` → `"0,5"`; `num_tex(x)` → `"0{,}5"` (para `MathTex`).
- `caja(txt, color, ancho, alto)` (rectángulo con texto), `flecha()`, `titulo()`, `etiqueta()`, `nota()`.

### Íconos (`comun/iconos.py`)
Devuelven un `VGroup` de ~1 unidad de alto (se agrandan con `.scale()`). Las
partes animables quedan como atributos. Vienen del curso de concurrente:
- **Personas**: `persona`, `ingeniero`, `paciente_acostado`, `burbuja_pensamiento(contenido)`.
- **Objetos**: `teclado` (`.teclas`), `monitor_signos`, `avion`, `cohete` (`.llama`), `misil`,
  `banco`, `reloj` (`.minutero`, `.aro`), `chip(color, texto)`, `boton`, `documento`,
  `cruz_hospital`, `lupa` (`.vidrio`), `disco`, `receta`, `tarta`, `horno(contenido)`,
  `ventana_app(titulo, color, contenido)`, `nota_musical`, `triangulo_play`.
- **Ordenadores, casa y seguridad**: `ordenador` (`.pantalla`), `batuta`, `casa`, `llave`, `escudo`,
  `candado(abierto=)`, `barrera` (`.brazo`), `burbuja_dialogo`, `ojo`.
- **Azar, errores y tráfico**: `dado` (`.cara`, `.puntos`), `bicho`, `semaforo` (`.luces`), `bandera`.
- **Mensajes y mecanismos**: `sobre` (`.cuerpo`, `.solapa`), `engranaje`, `matraz` (`.liquido`),
  `cajero` (`.pantalla`), `sello(texto, color)`.
- **Cotidianos**: `torniquete`, `moneda(texto)`, `lata`, `expendedora`, `rayo`, `sol`, `coche`,
  `reloj_arena`, `cilindro_bd`, `senal_alto`, `plato`, `pizarra`, `lapiz`.
- **Marcas**: `tilde`, `cruz`, `tachar(m)` (línea que tacha).
- Los íconos nuevos de esta materia van al final, en la sección «Procesamiento de Señales».

### Piezas técnicas (`comun/figuras.py`)
Se completa episodio por episodio (una sección por episodio al final del
archivo). **Cada pieza nueva se anota aquí**, con sus atributos.
- **Base**: `gaussiana(x, mu, sigma)` (la densidad, para graficar);
  `Curva(f, x_rango, y_max, ancho, alto, color, x_label, y_label)`: ejes + curva
  (`.ejes`, `.etiquetas`, `.grafica`; `area(desde, hasta, color)` devuelve el área
  sombreada, `punto(x)` un punto sobre la curva; `ejes.c2p(x, y)` da coordenadas de pantalla).
- **Capítulo 10, episodio 2** (`figuras.py`): `CuatroEnFase` (osciladores en fase, amplitudes 1, 1, 3, 3; misma API que `CuatroCosenos`); `TablaCortes` (tabla de cortes con `armazon()`, `enc()`, `celda()`, `prom()`, `marco()`; piezas sueltas para animar una a una); `Rombo` (las cuatro parejas de los osciladores, `.puntos`, `.p(x, y)`); `Palitos` (autocovarianza contra separación, `.tallos`, `.puntos`, `.pos(k)`); `termometro()`; `balancin()`.
- **Cap. 10, E7**: `BloqueLTI(rotulo, centro, ancho, alto, color, largo)` (caja de un sistema con flecha de entrada y de salida: `.caja`, `.rot`, `.ent`, `.sal`, `p_ent()`, `p_sal()`) y `Tallos(valores, centro, paso, unidad, color, k0, indices, extra)` (secuencia de palitos: `.base`, `.tallos`, `.puntos`, `pos(i)`, `x(i)`, `palito(i)`).
- **Capítulo 11, episodio 5** (al final de `figuras.py`): `tijeras()`, `bombilla()`, `lienzo_f(f0, f1, alto, ...)` (lienzo de frecuencias en Hz, con el cero en `base_y`), `lienzo_db(ancho, alto, x_max, top, ...)` (0 dB arriba), `regla_db(L, valores)`, `sinc_abs(f, f0)`, `valores_ventana(tipo, n)` y `nucleo_db(tipo, x)` / `nucleo_lin(tipo, x)` (núcleos de 'rect', 'hann' y 'blackman', calculados con la FFT), `picos_laterales(tipo, x_max)`, `ventana_t`, `copias_trozo(L, f)`, `fichas(textos)`, `trozos_solapados(L, ...)` (registro, marcos y campanas de Hann), `datos_dos_tonos(n)` y `espectro_fft(x, relleno)`. Colores de ventanas: `COLOR_VENTANA` (rectangular ámbar, Hann verde, Blackman azul).
- **Previstas** (crearlas cuando las pida un episodio, con estos nombres):
  histograma que se llena muestra a muestra; nube de puntos bivariada con su
  elipse; par de vectores con ángulo (ρ = cos θ); `Realizaciones` (ensemble de
  un proceso, con corte vertical en t); `Espectro` (una PSD con su área = potencia);
  `BloqueLTI` (caja con entrada y salida, h(t) / H(jω)); proyección ortogonal
  (vector, subespacio y error perpendicular); regiones de decisión con umbral;
  curva ROC que se traza al mover el umbral.

- **Cap. 12, E6** (al final de `figuras.py`): `Balanza(centro, semi)` (balanza de dos platillos: `.viga`, `.izq`, `.der`; `inclinar("izq"|"der")` devuelve las animaciones y las pesas de cada platillo se desplazan aparte `±semi·sen(ang)`), `FilaMuestras(rotulos, centro, lado, color, escala)` (casillas x[n−1], x[n]…: `.cas`, `.rots`, `x(i)`, `marco(i0, i1, color)`), `barra_h(valor, y, x0, esc, color)` (barra horizontal de error) y `eco_x` (realización del eco 0,6; sin usar por ahora).
- **Capítulo 13, episodio 7** (al final de `figuras.py`): `AZUL_C7` (azul claro de la «otra» señal s₀), `modem7()`, `campana7(cx, y0, s, alto, color)` y `cola7(...)` (campana y su cola sombreada), `planito7()`, `pulso7(valores, ...)` (`Tallos` con la escala del episodio). Además `EscenaCurso.paso(marca, *anims, t)` en `escena.py`: espera la marca y entra los objetos con `FadeIn`.
- **Capítulo 7, episodio 1** (al final de `figuras.py`): `Cursor7(L, t, v)` (cursor vertical con punto sobre una curva: `.linea`, `.punto`, `mover(t)`, `barrer(t0, t1)`), `CajaSistema7(rotulo, centro, ancho, alto)` (caja de un sistema con rótulo de texto: `.caja`, `.rot`, `.ent`, `.sal`, `nuevo_rotulo(txt)`), `EspacioDado(centro)` (las seis caras del dado dentro de un rectángulo, dispuestas 2 4 6 / 1 3 5 para que «par» sea la fila de arriba y «más de 4» la columna de la derecha: `.rect`, `.caras[n]`, `p(n)`, `fracciones()`, `marco_par()`, `marco_mas4()`), `Mapa7(centro)` (el mapa del curso, capítulos 7 a 13: `.circ`, `.nums`, `.rot`, `luz(i, color)`), `movil7()`, `serie_monedas7()` / `fraccion_caras7()` (lanzamientos de la moneda: los diez primeros dan siete caras) y `fila_monedas7(caras, n)`.
- **Capítulo 7, episodio 3** (al final de `figuras.py`): `cdf_normal(x, mu, sigma)` (acumulada de la normal), `RectaNum(x0, x1, centro, ancho, marcas)` (recta numérica con marcas: `.base`, `.ticks`, `.nums`, `p(x)`), `AcumDado(centro, ancho, alto)` (ejes de la acumulada del dado y su escalera: `.ax`, `.peldanos`, `.llenos`, `.huecos`, `.nums_x`, `.nums_y`, `p(x, y)`, `cursor(x)`) y `huecos_tres(llenos)` (fila de huecos Bernoulli / uniforme / gaussiana).
- **Capítulo 12, episodio 7** (al final de `figuras.py`): `ParabolaJ(centro, ancho, alto)` (la parábola J(h) = 4 − 8h + 5h² del E1: `.eje`, `.curva`, `.vertice`, `p(h)`, `punto(h, color)`, `pendiente(h)`), `auriculares()` (`.arco`, `.copas`) y `brujula()` (`.aro`, `.aguja`).
- **Capítulo 13, episodio 3** (al final de `figuras.py`): `lienzo_g3` (lienzo de las dos campanas de g), `dens3(L, mu, sigma, color)` (campana con altura de densidad), `cola3(L, mu, sigma, desde, hasta)` (cola sombreada), `umbral3(L, g)` (marca γ: `.linea`, `.rot`), `eje_g3(L, marcas)` (`.base`, `.nums`), `hoja3()`, `rejilla3(rojos)` (cien puntos), `casilla_h3(k, texto)` (casilla de hipótesis).
- **Capítulo 12, episodio 4** (al final de `figuras.py`): `H_NO_CAUSAL`, `H_CAUSAL` (coeficientes del sensor), `COLOR_PASO` (1 CIAN · 2 ÁMBAR · 3 VERDE), `corona()`, `tira_blanca(valores, lado)` (la moneda ±1), `eje_muestras(y, n_pasado, n_futuro)` (`.base`, `.pasado`, `.futuro`), `cadena_cajas(rots, centro, colores, ancho, hueco)` → `(grupo, cajas, flechas)`, `tres_casillas(centro)` (`.casillas`), `COL_X` y `tabla_blanca()` (`.ms`, `.cs`, `.hs`, `.rots`, `col(i)`).
- **Capítulo 13, episodio 5** (al final de `figuras.py`): `PlanoV(centro, lado, esc, rot0, rot1)` (plano de dos muestras de ruido: `.ejes`, `.rot0`, `.rot1`, `p(a, b)`, `elipse(rho, k, sx, sy)`, `puntos(rho, n, semilla)`), `ruido_ar(n, a, semilla)`, `d_ruido(w, a)` (densidad del ruido con memoria `a`, máximo 1), `s2_lento(w)` / `s2_rapido(w)` (|S|² de (1, 1) y (1, −1)), `lienzo_w(ancho, alto, base_y)` y `eje_w(L)` (lienzo de Ω de 0 a π), `nube_lluvia()`, `aviso_triangulo()`, `avion_arriba()` (el `avion` de `iconos.py` se ve como un yunque: no usarlo), `datos_celdas(n, i0, i1, sig_lluvia, semilla)` y `umbral_local(x, k, vecinas)` (el radar con lluvia: semilla 8 da 6 falsas alarmas con umbral fijo y 0 con el que se adapta).
- **Capítulo 13, episodio 1** (al final de `figuras.py`): `RectaR(centro, ancho, x_rango, rotulo)` (recta de una medición: `.base`, `.rot`, `p(x)`, `marca(x, tex)`), `rect_dens` / `tri_dens` (densidad uniforme o triangular sobre la recta), `Plano2(centro, u)` (plano r₁, r₂ con `.grande` de lado 2 y `.pequeno` de lado 1, `p(x, y)`), `barras_senal(valores, ...)` (`.base`, `.barras`), `casillas(n, rojas, ...)` (`.cas`), `barra_v` y `TablaDecision(centro, lado)` (tabla 2 × 2 de realidad contra decisión: `.cel`, `.enc`, `.titulos`, `c(i, j)`).
- **Capítulo 12, episodio 1** (al final de `figuras.py`): `sensor12(n, semilla)` (el sensor centrado: `t, y, v, x`), `suavizada(x)` (una «estimación» limpia para los dibujos), `flechas_xy(origen, largo, angulo)` (el dibujo del capítulo 8 con las letras x, y, ŷ, e: devuelve `(F, rotulos)`) y `MatrizT(valores, centro, lado, escala)` (matriz de textos con `.celdas`, `.corchetes`, `.diag(k)` y `.p(i, j)`, para la de Toeplitz).
- **Capítulo 12, episodio 3** (al final de `figuras.py`): curvas del sensor y de la deconvolución `s_senal(w)` (16 · 1,88 · 1), `h_wiener(w)` (0,94 · 0,65 · 0,5), `g_prom(w)`, `h_inverso(w, tope)`, `h_wiener_dec(w)`; `lienzo_omega(...)` (lienzo de Ω de 0 a π) y `eje_omega(L, v1, completo, escala)` (eje con 0, π/2, π o −π, 0, π; `.h`, `.v`, `.rotulos`); `columna_ecuaciones` y `columna_incognitas` (la columna infinita de ecuaciones y de h[j]); `registro_e3(n, semilla)` → `(y, v, x)`; `rebanadas_omega(L, n, alto)` (rebanadas del eje de frecuencias).
- **Cap. 12, E5** (`figuras.py`): `dos_colas(...)` (secuencia K·0,6^m / K·0,157^|m| como `Tallos`, `.m(k)`), `PlanoZ` (`.p(x, y)`, `.circ`), `marca_x`/`marca_o` (polo/cero), `DiagramaRecursion` (ŷ[n] = 0,157 ŷ[n−1] + 0,7386 x[n]: `.amp1`, `.suma`, `.retardo`, `.amp2`, `.P`), `ficha_numero`, `barras_error`, `recuadro_mini` (los tres pasos); constante `H_CAUSAL_5`.
- **Capítulo 13, episodio 6** (al final de `figuras.py`): constantes `PULSO13`, `FILTRO13`, `BARKER13`; `autocorr13(a, b)`, `chirp13(n)`, `radar13()` (`.plato`, `.ondas`), `celdas13(n, ancho, centro, alto)` (tira de celdas), `grilla13(n, filas, lado, centro)` (100 casillas), `autocorr_tallos13`, `curva_barras13`, `avion_lejano13`.
- **Capítulo 7, episodio 5** (al final de `figuras.py`): `canal7(centro, ancho, escala)` (el canal que confunde bits: `.caja`, `.rot`, `.ent`, `.sal`, `p_ent()`, `p_sal()`), `Tabla2x2(centro, lado)` (tabla conjunta S × R: `.cel[i][j]`, `.rot_f`, `.rot_c`, `c(i, j)`, `p_fila(i)`, `p_col(j)`, `marco(i, j)`, `valor(i, j, tex)`), `nube_xy7(n, semilla)` (pares (x, y) con y = x + ruido), `Colina(centro, rho, ancho, prof, alto, n)` (densidad conjunta como colina en perspectiva oblicua con líneas ocultas: `.base`, `.filas`, `P(u, v, h)`, `h(u, v)`, `region(u0, u1, v0, v1)`, `corte_u(u)`, `curva_fila(v)`; todo lleva `permitir_encima`), `Alturas7(centro, ancho, alto)` (campanas de hombres y mujeres: `.base`, `.h`, `.m`, `x(cm)`, `y(d)`, `marca(cm)`) y `BarrasVar7(origen, esc)` (barra de varianza partida en 41,2 y 40,56: `.dentro`, `.entre`).
- **Capítulo 11, episodio 1** (al final de `figuras.py`): `seno_t`, `ruido_t`, `voz_t`/`voz_valores`, `espectro_ruidoso`, `colador()` (`.cuerpo`, `.agujeros`), `BarrasF` (espectro de barras: `.base`, `.barras`, `.puntas`, `.rot`, `x(f)`, `simetrico=True`), `area_bajo(L, t, v)`, `psd_tele(w)` y `autocorr_tele(t)` (la telegráfica con α = 2).
- **Capítulo 11, episodio 7** (al final de `figuras.py`): `microfono()`, `flecha_c(o, largo, grados)` (número complejo como flecha), `plano_c(centro, radio)` (ejes + circunferencia, `.circ`), `parabola_l(centro, ancho, alto, fondo)` (la parábola de Cauchy-Schwarz; `.eje`, `.curva`, `.L`) y `nube_puntos()`.
- **Capítulo 11, episodio 6** (al final de `figuras.py`): `psd_eco`, `ecg_t`, `pulsaciones_t`, `lentas_t`, `pecho()`, `altavoz()`, `antena()`, `muro()`, `luz_blanca()`, `barras_imp`, `cadena_bloques`.
- **Capítulo 7, episodio 6** (al final de `figuras.py`): `CANAL6` (tabla 0,63 · 0,07 · 0,03 · 0,27), `TablaCanal(centro, lado, esc, probs)` (tabla conjunta del canal con S en filas y R en columnas: `.cel`, `.prob`, `.enc_f`, `.enc_c`, `c(i, j)`, `armazon()`, `probs()`, `marco(i, j, color)`, `texto(i, j, txt)`; `probs=` permite otra tabla, por ejemplo la independiente), `puntos_corr(rho, n, semilla)` (pares normales con correlación rho) y `nube6(centro, sx, sy, a, b)` (esos puntos como `Dot`s).
- **Capítulo 7, episodio 2** (al final de `figuras.py`): `EspacioDado07(centro, lado)` (rectángulo con las seis caras: `.marco`, `.caras`, `p(i)`, `aros(idx, color, margen)`), `GrillaMil07(centro)` (mil personas en filas de 60; `.pts`, `.fila0`, `recuadro(i0, i1, color)`), `Arbol07(raiz, nivel1, nivel2, p1, p2, ...)` (árbol de dos niveles: `.raiz`, `.n1`, `.hojas`, `.l1`, `.l2`, `rama(i, j, color)`) y `tira_test07(escala)` (la tira del test: `.cuerpo`, `.ventana`).
- **Capítulo 7, episodio 4** (al final de `figuras.py`): `Regla7(centro, ancho, v0, v1, valores, rotulos)` (recta de valores del dado con marcas: `.base`, `.marcas`, `.rots`, `p(v)`), `caras7(regla, escala, altura)` (las seis caras sobre la regla: `.caras`), `promedios_dado(n, semilla)` y `promedios_ruido(n, semilla, sigma)` (promedios acumulados), `fila_personas7(n, centro, paso, escala)` (`.personas`), `campana7(cx, cy, sigma, color, ancho, alto, mu, x_max)` y `cola7(cx, cy, sigma, desde, hasta, color, ancho, alto)` (campana y su cola sombreada, en pantalla).
- **Capítulo 8, episodio 2** (al final de `figuras.py`): `CANAL8` (valores de la tabla del canal en `MathTex`), `puerta8(alto)` (`.marco`, `.pomo`), `PuntosErr8(centro, ancho, alto, n, semilla, desplaz)` (errores sueltos alrededor de una línea de cero: `.cero`, `.pts`, `y(v)`), `Nube8(centro, ancho, alto, n, semilla)` (nube y = x + ruido sobre ejes: `.ax`, `.etq`, `.pts`, `p(x, y)`, `rebanada(x, ancho)`, `en_rebanada(x, ancho)`) y `parabola8(centro, ancho, alto)` → `(curva, punto_minimo, p)` (U con el mínimo en el centro).
- **Capítulo 10, episodio 1** (al final de `figuras.py`): `serie(semilla, n, a)` (serie con
  memoria `a`, `a=0` ruido blanco), `traza(x, y, ...)`, `Lienzo` (mapa (t, v) → pantalla:
  `.curva`, `.base`, `.vertical`, `.p`), `pila_de_curvas`, `generador` (oscilador con su seno),
  `dado_n(n)`, `caja_tex`, `tira_pm1` (la moneda ±1) y `CuatroCosenos` (los cuatro osciladores
  desfasados; `.corte(t)`, `.punto(i, t)`, `.rotulos`).

### Efectos de sonido (`comun/sfx.py`)
`pop`, `whoosh`, `tick`, `tecla`, `impacto`, `alarma`, `exito`, `error`, `latido`.
Se sintetizan con numpy; para agregar uno se escribe una función y se registra en `EFECTOS`.

### Convenciones
- Un método por bloque en escenas largas. Comentar con la frase anclada (`# «la campana»`).
- Íconos o piezas que podrían reutilizarse → a `iconos.py` o `figuras.py`, no dentro de la escena.
- Lo que sale de cuadro a propósito: `m.permitir_fuera = True` (en cada texto de la familia).
- Lo que pasa por encima de texto a propósito (lupa, foco de luz): `m.permitir_encima = True`.

---

## 8. Herramientas: render, ritmo y controles

Todos los comandos se corren desde `Animaciones/` con el Python correcto (§10).

### `ritmo.py`: densidad de momentos, antes de animar
```powershell
python ritmo.py Capitulo07_Probabilidad/E1_nombre [--max 3.0] [--escenas 03,04]
```
Sintetiza la voz (o la toma del caché) y lista en qué segundo cae cada momento,
y los tramos de más de `--max` s sin ninguno. También sirve para validar el guion.

### `render.py`: el episodio
```powershell
python render.py <carpeta_episodio>                    # borrador 480p15, todo el episodio
python render.py <carpeta_episodio> --escenas 03,07    # solo esas escenas
python render.py <carpeta_episodio> --solo-unir        # concatena lo ya renderizado
python render.py <carpeta_episodio> --calidad qh       # final 1080p60
```
Deja en `<carpeta>/salida/`: `<carpeta>-<res>.mp4`, el `.srt` unido y
`capitulos.txt` para la descripción de YouTube. Si hay música en `musica/`,
genera además `-musica.mp4` con la pista mezclada a ~−23 dB (`--sin-musica` para evitarlo).
El detalle de Manim queda en `<carpeta>/render.log`.

### Controles automáticos (en cada render)
`EscenaCurso` revisa todo mientras renderiza y `render.py` imprime un resumen:
- **atraso**: la animación llegó más de 0,2 s tarde a su frase. Se acortan los
  `run_time` o se usa `margen()`.
- **silencio de voz**: las animaciones de un bloque duraron más que su audio.
- **encimado**: un texto **o una fórmula** tocado *parcialmente* por otra forma,
  otro texto u otra fórmula. Contener por completo (texto dentro de su caja) no
  cuenta. Cada `MathTex` se mide entero: sus piezas no se comparan entre sí.
- **fuera de cuadro**: texto o fórmula que se sale de la pantalla (solo sin zoom).

Informes por escena en `media/informes/<Clase>.json`. **Meta: 0 avisos.**

### Hojas de contacto: revisar a ojo sin mirar el vídeo entero
```bash
ffmpeg -v error -y -i Escena.mp4 -vf "fps=1,scale=256:-1,pad=260:148:2:2:white,tile=8x7" -frames:v 1 hoja.png
ffmpeg -v error -y -ss 12.5 -i Escena.mp4 -frames:v 1 cuadro.png     # un instante puntual
```
El borde blanco (`pad`) separa las celdas, porque sin él es fácil mezclar filas.
Buscar lo que los controles **no** ven: celdas casi vacías, elementos chicos,
fórmulas ilegibles, bloques de color macizos (ver `Indicate` en §10), íconos que
no se entienden, curvas que no se distinguen del fondo.

### `voces_prueba/`
- `probar_voces.py`: el mismo párrafo con varias voces (así se eligió Ximena, en concurrente).
- `probar_nombres.py`: nombres propios de la materia (Bayes, Chebyshev, Wiener…).
- `probar_anglicismos.py`: variantes numeradas de siglas, anglicismos y letras
  griegas ("Opción uno… Opción dos…") para que el usuario elija.
  **Así se decide toda pronunciación nueva.** Uso: `python probar_anglicismos.py roc psd`.

---

## 9. Voz, pronunciación y fórmulas dichas

- `comun/voz.py`: `VOZ_POR_DEFECTO = "es-ES-XimenaNeural"`, `VELOCIDAD = "-5%"`.
  Cambiarlas ahí cambia todo el curso (y vuelve a sintetizar todo el audio).
- **Motor de voz**: si existen `AZURE_SUBSCRIPTION_KEY` y `AZURE_SERVICE_REGION`
  (variables de entorno o `Animaciones/.env`, que está en `.gitignore`), la voz
  sale por **Azure Speech** (servicio oficial, plan gratuito F0, la misma
  Ximena); si no, por edge-tts. El audio que edge-tts ya dejó en caché se
  reutiliza tal cual: Azure solo sintetiza los bloques nuevos o cambiados.
  `.env` son dos líneas: `AZURE_SUBSCRIPTION_KEY=...` y `AZURE_SERVICE_REGION=...`
  (la región es el nombre corto del recurso). **Configurado el 12/10/2026**:
  recurso `vidProcSenales` en `northcentralus`, suscripción Azure for Students
  del usuario, plan Free F0.
  - Probado: el mismo bloque por edge-tts y por Azure dura 14,38 s y 14,30 s, con
    las 31 palabras ubicadas y ~0,05 s de diferencia. Es la misma voz.
  - Cupo: 500.000 caracteres por mes (un episodio gasta ~8.000–10.000). Lo que
    está en caché no gasta.
  - El plan gratuito limita las peticiones por minuto: `voz.py` espera y
    reintenta solo ante un 429, así que varias sesiones a la vez solo van más lento.
  - Un error 401 es la clave o la región mal puestas en `.env`: avisar al
    usuario (la clave se copia o se regenera en el portal de Azure, en el
    recurso → «Claves y punto de conexión»). Nunca imprimir el contenido de `.env`.
  - `sintetizar_mp3(texto, destino, voz)` de `voz.py` da un mp3 suelto con el
    mismo motor: lo usan los scripts de `voces_prueba/`.
- Caché en `media/voiceovers/` de cada episodio: un bloque solo se vuelve a
  sintetizar si cambia su texto hablado. Cambiar momentos no regenera audio.
- `comun/pronunciacion.py`: reemplazos **solo para el audio**; los subtítulos
  muestran el texto del guion. Estado actual: Fourier y Bayes (ver abajo).
- Palabra nueva dudosa → agregarla a `probar_nombres.py` o `probar_anglicismos.py`,
  generar, mandar los mp3 y que el usuario elija un número. No adivinar.
- **Decidido de oído:** Bayes → «Báyes» (variante 5 de `voces_prueba/probar_bayes.py`), ya en `comun/pronunciacion.py`.
- **Pendientes de probar de oído** (antes del primer episodio que las use):
  Chebyshev, Markov, Gauss, Cauchy-Schwarz, Neyman-Pearson, Wiener,
  Khinchin, Kalman, Bochner, Welch, Parseval; siglas ROC, PSD, WSS, LTI, FIR,
  MMSE, LMMSE, MAP, SNR; letras griegas (tau, omega, sigma, rho, mu, lambda, theta).
  Anotar aquí lo que se decida (**tal cual** / **reemplazado** → «grafía»).
  Decidido: **Bernoulli** → «Bernulí» (variante 3 de `voces_prueba/probar_bernoulli.py`; está en `comun/pronunciacion.py`).
  Decidido: **Fourier** → dicho **con fonemas**, «fu-ri-ér» (variante 5 de `probar_fourier_ipa.py`; las grafías «Furiér» y «Fuhriér» se descartaron).
- **Fonemas**: cuando ninguna grafía suena bien, la palabra se dice con fonemas
  IPA (`FONEMAS` en `pronunciacion.py`). El texto y los subtítulos no cambian;
  `voz.py` envuelve la palabra en `<phoneme>` al sintetizar y mete los fonemas
  en la clave del caché. Solo funciona con Azure Speech (edge-tts no acepta SSML).

### Cómo se escriben las fórmulas en la narración
La voz lee texto plano: las fórmulas se escriben **en palabras, tal como se
dicen**, y el símbolo va en pantalla (en el momento). Los subtítulos muestran
lo mismo que se oye.

| En pantalla | En la narración |
|---|---|
| $P(A\mid B)$ | «la probabilidad de A dado B» |
| $f_X(x)$ | «la densidad de equis» (la primera vez: «efe sub equis de equis») |
| $E[X]$, $\mu_X$ | «la esperanza de equis», «la media» |
| $\sigma_X^2$ | «la varianza de equis», «sigma cuadrado» |
| $\sigma_{XY}$ | «la covarianza entre equis e i griega» |
| $\rho_{XY}$ | «el coeficiente de correlación», «rho» |
| $R_{XX}(\tau)$ | «la autocorrelación, erre sub equis equis de tau» |
| $S_{xx}(j\omega)$ | «la densidad espectral de potencia» |
| $\hat{X}$ | «equis sombrero», «la estimación de equis» |
| $1/\alpha^2$ | «uno sobre alfa al cuadrado» |
| $0{,}05$ | «cero coma cero cinco» o «un cinco por ciento» |

- Preferir **el nombre del concepto** al deletreo del símbolo ("la varianza"
  mejor que "sigma sub equis al cuadrado"). El deletreo, solo la primera vez que
  aparece un símbolo, para atarlo a su nombre.
- Letras sueltas: «equis», «i griega», «zeta», «a», «be». Si una letra suena
  mal (ej. «be» se confunde con «ve»), se prueba de oído.
- Números: siempre en palabras en la narración si son decimales o raros
  («cero coma seis uno»); los enteros simples pueden ir en cifra.

---

## 10. Entorno y trampas conocidas

### Entorno (Windows)
- **Python correcto**: `C:\Users\Nacho\AppData\Local\Programs\Python\Python312\python.exe`.
  El `python` del PATH puede resolver a MSYS2 (3.14, sin Manim ni pip).
- Instalado: Manim 0.21, manim-voiceover 0.4.0, edge-tts 7.2,
  azure-cognitiveservices-speech 1.52, ffmpeg (winget), MiKTeX. Las versiones
  exactas están en `requirements.txt` (`python -m pip install -r requirements.txt`).
- `PYTHONPATH` = `Animaciones/` (render.py y ritmo.py lo ponen solos; para correr
  `manim` a mano: `$env:PYTHONPATH = "C:\Users\Nacho\Documents\ProcesamientoDeSenales\Animaciones"`).
- La voz (Azure Speech o edge-tts) necesita internet. No hay GPU NVIDIA: los TTS locales serían lentos.
- El aviso "SoX could not be found" es inofensivo. También el de MiKTeX
  "you have not checked for MiKTeX updates".
- En la consola de Windows los acentos se ven rotos (`�`): es la consola, los
  archivos están bien en UTF-8. Para imprimir bien: `PYTHONIOENCODING=utf-8`.
- En bash, los heredocs con código Python van con `<<'EOF'` (entre comillas): sin
  comillas, `\b` y `\\` se rompen.

### Manim
- **Animar una parte de un grupo** (ej. `tecla.animate`) saca esa parte a la
  lista de la escena: `self.remove(grupo)` la deja en pantalla. Para cambiar de
  plano usar `self.corte()` o `self.limpiar()`.
- **`Indicate(...)` y `.set_color(...)` sobre un grupo pintan también el
  relleno**: una caja con fondo oscuro queda como un bloque macizo y el texto
  desaparece. Usar `self.resaltar(m)` o `caja.set_stroke(color)`.
- **`.set_opacity(x)` sobre un grupo también pisa el relleno**: `set_opacity(1)`
  deja las cajas macizas (y un `Arc` relleno). Para atenuar y volver: `m.save_state()`,
  `m.animate.fade(0.65)` y después `Restore(m)`; o una copia nueva en vez de "desatenuar".
- Para sacar de cuadro algo con textos, `FadeOut(grupo, shift=...)`: un `shift` que los
  deja fuera de pantalla dispara el aviso de fuera de cuadro aunque después haya un corte.
- `always_redraw` o updaters: `clear_updaters()` antes de `FadeOut` o de moverlo.
- No anclar un texto a algo que rota (su caja envolvente cambia y el texto salta):
  usar una posición fija.
- `VGroup(...)` no acepta objetos no vectoriales: para "todo lo que hay en
  pantalla" usar `Group(*[m for m in self.mobjects if m is not self.camera.frame])`.
- `Text("")` vacío puede romper. `Text` con `\n` alinea a la izquierda: usar `texto_centrado`.
- Números: `Integer(..., group_with_commas=False)`; decimales con coma a mano (`num()`).
- Después de `zoom()`, lo nuevo tiene que caber en el encuadre reducido; cerrar con `zoom_reset()`.
- Un zoom muy profundo dentro de una forma rellena deja la pantalla de un solo
  color: hacer zoom hasta que el objeto se vea entero, no más.
- Una copia que vuelve a su original tiene que volver a la **misma escala**, si
  no queda encimada a medias.
- `FadeIn`/`FadeOut`/`Create` sobre una **parte** de un grupo que ya está en escena
  parte el grupo en pedazos en la lista de la escena, y después moverlo entero
  falla. Para piezas que crecen: agregar la parte al grupo y animarla con
  `MoveToTarget`/`.animate`; para sacarla, quitarla del grupo, `escena.add(parte)` y recién
  ahí animar su salida.
- `self.remove(VGroup(a, b))` con un grupo armado al vuelo no saca `a` ni `b` de la escena:
  hay que pasar los objetos que se agregaron (`self.remove(a, b)`).
- `FadeOut` sobre una parte de un grupo que sigue en escena la deja invisible
  para siempre y un `FadeIn` posterior no la trae de vuelta: usar `save_state()`,
  `.animate.fade(1)` y `Restore`.
- Varias `.animate` sobre el mismo mobject dentro de un solo `play` se pisan
  (la última gana): agrupar en una sola cadena `m.animate.a().b()`.
- Un diagrama con flecha o etiqueta a un costado: `move_to` centra la caja
  envolvente, no la pieza principal. Centrar a mano la pieza que importa.
- Un `self.corte()` entre dos bloques deja la pantalla vacía hasta la primera marca del
  bloque siguiente (a veces 2–3 s): cortar **dentro** del bloque nuevo, en su primera marca.

### Fórmulas y gráficas (propio de esta materia)
- `MathTex` compila con LaTeX (MiKTeX): la primera vez de cada fórmula tarda;
  después queda en caché en `media/Tex/`. Un error de LaTeX corta el render:
  mirar `render.log`.
- **Piezas de `MathTex`**: `MathTex("a", "=", "b")` da `f[0]`, `f[1]`, `f[2]`. Una
  sola cadena larga es **una** pieza: para animar términos por separado hay que
  partirla. Una llave `{` no puede quedar abierta en una pieza y cerrarse en otra.
- **Transformar una fórmula en otra**: `TransformMatchingTex` empareja por pieza
  igual; con piezas distintas, `ReplacementTransform` pieza a pieza.
- La coma decimal en `MathTex` va entre llaves (`0{,}5`), si no LaTeX agrega un espacio.
- `get_area` y `plot` necesitan que el rango esté dentro de `x_range` de los ejes.
- Curvas con muchos puntos (ruido, realizaciones largas) hacen lento el render:
  usar `plot_line_graph` con ~200–400 puntos, no miles.
- **Encimado con fórmulas**: el control mide la caja envolvente de cada `MathTex`
  entero. Una fórmula junto a una curva que la cruza da aviso: moverla o usar
  `permitir_encima` solo si es a propósito.

### manim-voiceover + edge-tts
- manim-voiceover 0.4.0 **no trae** servicio de edge-tts: el nuestro está en `voz.py`.
- **edge-tts da 403** (`WSServerHandshakeError`) cada vez que Microsoft cambia el
  token de Edge; desde el 10/10/2026 falla con la última versión (7.2.8, issue
  #490 de `rany2/edge-tts`). No es el reloj ni la instalación: se usa Azure
  Speech (§9) y `voz.py` (`AzureSpeechService`) hace el resto. Mientras edge-tts
  no vuelva, **no borrar `media/voiceovers/`** de un episodio sin tener la clave de Azure.
- edge-tts ≥ 7 manda por defecto límites de **oración**; `voz.py` pide
  `boundary="WordBoundary"` (sin eso no hay marcas) y ubica cada palabra en el texto.
- El caché se indexa por el texto **sin** marcas; `voz.py` devuelve el texto
  actual para que las marcas nuevas existan.
- **Bloque que empieza con un signo** («¿Qué…»): `voz.py` lo corrige solo
  (`_desde_el_principio`); sin eso, la primera marca se iba al final del audio.
- Algo tenue que no debe contar para el control de **encimado** (una guía
  "fantasma"): opacidad **< 0,1**. Con 0,1 exacto cuenta. Ojo: `stroke_width=0`
  no alcanza, el control mira la **opacidad** del borde: pasar también `stroke_opacity=0`.
- **Marca con mayúsculas en el guion** (`` `enA` ``): el parser solo reconoce `[a-z0-9_]`, así
  que esa línea de momento **no falla: se lee en voz alta como narración** y el bloque dura el
  doble (`ritmo.py` lo delata: un hueco enorme entre la última marca y el fin). Marcas siempre
  en minúsculas.
- Con varios renders de Manim **a la vez** sobre el mismo episodio, chocan en
- **voz sin red** (**ya no hace falta**: desde el 12/10/2026 la voz sale por Azure, §9; queda solo como último recurso si no hay internet, y todo lo renderizado así hay que rehacerlo con la voz real): cuando edge-tts respondía `403` (pasó en el E1 y en el E5 del Cap. 7), con `CURSO_VOZ_SIN_RED=1` (en PowerShell: `$env:CURSO_VOZ_SIN_RED='1'`) `servicio_voz()` devuelve `SinRedService` (`comun/voz.py`): audio **mudo** con tiempos de palabra estimados (~14 caracteres por segundo) y otra clave de caché, así que nunca se confunde con la voz real. Sirve para correr `ritmo.py` y `render.py`, revisar imágenes y ver huecos; los tiempos reales cambian un poco y el mp4 sale sin voz. Para el borrador que se manda al usuario y el render final hay que volver a renderizar sin esa variable cuando edge-tts funcione.
  `media/texts/*.svg` (`PermissionError [WinError 32]`): renderizar de a uno.

---

## 11. Checklist antes de entregar

- [ ] `ritmo.py` sin tramos de más de ~4 s (o cubiertos por una animación de ≥1 s).
- [ ] Render sin errores y **0 avisos** en los controles automáticos.
- [ ] Hojas de contacto revisadas: sin huecos, sin elementos chicos, fórmulas legibles en 480p, sin bloques macizos.
- [ ] Duración ~10 min (`render.py` la informa).
- [ ] Castellano de España en todo el texto nuevo (nada de voseo del apunte); números en formato español.
- [ ] Cada fórmula que se nombra se ve; cada fórmula que se ve se nombra.
- [ ] Cada escena tiene `**Capítulo YouTube:**` y la primera empieza en 0:00.
- [ ] El cierre anuncia el episodio siguiente por su título.
- [ ] README §1 y la línea `**Estado:**` del guion actualizados.
- [ ] README actualizado si apareció una trampa nueva, una pieza nueva o una herramienta nueva.
- [ ] Antes de pushear: vídeo subido y verificado en YouTube, residuos limpiados
      (`salida/`, `__pycache__/`, `render.log`, `lista.txt` y `media/` salvo
      `media/voiceovers/`, que se versiona) y el episodio rehacible con
      `python rehacer.py <Capitulo> <E N>` (§2, paso 17).

---

## 12. Cómo trabajar con el usuario

- El usuario escribe en español rioplatense; los vídeos van en castellano de España.
- Mostrar avances con archivos (mp3, mp4, `guion.md`), no descripciones.
  Borradores en 480p; el 1080p va solo al final.
- **Aprueba**: el guion base de cada capítulo, el texto narrado nuevo de cada
  episodio, las pronunciaciones (de oído) y cada episodio en borrador antes del render final.
- **No hace falta preguntarle**: detalles de animación, íconos, colores, efectos
  y correcciones que surgen de los controles. Se deciden siguiendo este README.
- Lo que más valora (según su feedback en concurrente): animaciones rápidas y
  sincronizadas, que todo lo dicho se vea, nada de relleno en pantalla y ~10 min por episodio.
- Si autoriza trabajar "de noche sin esperar aprobación", el texto nuevo igual
  se marca con ⭐ en las notas del `guion.md` para que lo revise después.
