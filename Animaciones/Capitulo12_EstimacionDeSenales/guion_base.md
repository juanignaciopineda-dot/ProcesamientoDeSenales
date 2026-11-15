# Capítulo 12 — Estimación de señales

> **Guion base: narración de todo el capítulo. No se renderiza.**
> Es la fuente de texto para los 7 episodios (ver `../README.md` §1 para qué
> escenas van en cada uno). Cada episodio copia de aquí su narración a su
> propio `E<N>_.../guion.md`, que es el que lleva gancho, cierre y momentos, y
> el que se anima. Las secciones "Visual" son ideas iniciales, no
> especificación.
>
> **Estado:** narración completa, **esperando la aprobación del usuario**.
> Mientras no esté aprobada, cualquier ajuste de texto que pida el usuario se
> hace aquí primero, y después se copia al `guion.md` del episodio.

Guion para las 29 escenas del capítulo. Fuentes: `Apuntes/PROCESAMIENTO DE
SEÑALES.md` (sección "Estimación De Señales", líneas 1425–1695, sin los
Ejercicios Propuestos ni las actividades 12.5 y 12.16) y `Apuntes/PROCESAMIENTO
DE SEÑALES - Cap 12 en profundidad.md`: Parte 1 (de la ortogonalidad a las
ecuaciones normales, por qué el no causal se transforma y el causal no, el
causal por innovaciones, el precio de la causalidad, la factorización de
Kalman con su factor de escala), Parte 2 (las tres versiones y la tabla de
errores, filtrar contra predecir, deconvolución, el mismo sistema como
Kalman), Parte 3 (correlaciones estimadas, Levinson-Durbin, LMS) y Parte 4
(los tres sabores, el proceso bandeado, la proyección otra vez, Kalman contra
Wiener, el puente al capítulo 13). Figuras de referencia:
`c12-tres-wiener.svg`, `c12-respuesta-wiener.svg`, `c12-wiener-filtrado.svg`,
`c12p-proyeccion.svg`, `c12p-innovaciones.svg`, `c12p-factorizacion-kalman.svg`,
`c12p-fir-convergencia.svg`, `c12p-tres-sabores.svg`, `c12p-deconvolucion.svg`.

**Un cambio deliberado respecto del "en profundidad".** El apunte resuelve
todo con un sistema de juguete (autorregresivo de coeficiente 0,7 y ruido
0,3). Aquí se resuelve con **el sensor de temperatura de los capítulos 10 y
11** (varianza 4, coeficiente 0,6, ruido blanco de varianza 1), que el
capítulo 10 ya dejó a medias: ahí salieron a mano h = 0,8 (una muestra) y h ≈
(0,74; 0,12) (dos muestras). Este capítulo los completa y los generaliza. Los
números **no** son los del "en profundidad": se calcularon de nuevo con Python
(matrices de Toeplitz, factorización, integral de la coherencia) y se
comprobaron entre sí (ver "Números del sensor"). La estructura de las tres
versiones, la fórmula y los resultados generales sí son las del apunte.

**Qué se recuerda y dónde** (README §3, regla 2: nada se da por sabido, se
recuerda donde se usa, con su dibujo):
- de Señales y Sistemas: la convolución como suma de entradas recientes
  pesadas (03, 09), su transformada como producto, y la frecuencia Ω de −π a π
  con π como la más rápida (09), la respuesta en frecuencia como curva de
  ganancia (10, 13), el retardo z⁻¹, el filtro descrito por un cociente en z,
  polos y ceros y por qué un polo dentro del círculo decae (16), la fase
  mínima con los dos filtros de dos coeficientes (16), Parseval (21), el
  observador de estados (26);
- de matemáticas: parábola y vértice, derivada como pendiente (02), sistema de
  dos ecuaciones (04, 06, 07), matriz y diagonales constantes (04),
  conjugado de un número complejo (12), fracciones y ecuación de segundo grado
  (18), suma de una progresión geométrica (21), gradiente (28);
- del capítulo 7: variables como flechas, correlación como coseno, estimar =
  proyectar, la varianza del promedio, mirar la nube (02, 29);
- del capítulo 8: la mejor estimación lineal, la perpendicularidad del error,
  las ecuaciones normales y σ²(1 − ρ²) (02, 10, 12);
- del capítulo 10: el sensor y su ruido (01, 02, 04…), el filtro de una y dos
  muestras (0,8 y 0,74), estacionario y conjuntamente estacionario (03),
  la predicción a m pasos con su horizonte (06, 23), la parábola del error
  (02, 28), la convolución y el promediador (½, ½) (13);
- del capítulo 11: la densidad espectral y la cruzada (09–12), la coherencia y
  γ ≤ 1 (12), el filtro modelador y el blanqueador (16, 18), la fase mínima
  con el rho de 0,4 y los coeficientes (2, 1) y (1, 2) (07, 08, 16), «no se
  puede blanquear lo que no existe» (16), las tres barras ρ, 1, ρ (07, 08).

Cómo está escrito (README §3, "Explicar de forma explícita"): cada concepto
sigue el camino caso → cuenta a mano con números pequeños → dibujo → fórmula
como resumen → comprobación. Las deducciones cortas se hacen enteras, diciendo
qué regla se usa en cada paso (escenas 02, 04, 12); las largas (la fórmula
causal por innovaciones, la ecuación de Kalman con su factor de escala) se
hacen en su paso clave con el sensor y se remite al apunte "en profundidad".
Hay preguntas con pausa y sorpresas en las escenas 03, 05, 06, 07, 09, 14, 16,
21, 24 y 28. Castellano de España.

Convención: cada escena tiene Objetivo, qué hace falta saber antes, qué se ve,
y la narración partida en bloques `<!-- bN -->` que se sincronizan uno a uno
con un tramo de animación. En pantalla, la densidad espectral se escribe
**S** (como en los capítulos 10 y 11; el apunte de este capítulo la llama D).
Letras: **y** es la señal que se quiere (azul, `SENAL`), **v** el ruido
(magenta, `RUIDO`), **x** lo medido (cian, `MEDIDA`), **ŷ** la estimación
(ámbar, `ESTIMACION`) y **e** el error (rojo, `ERROR`). El capítulo 10 las
llamaba s, d y r; la escena 01 avisa del cambio.

## Reparto en episodios

| Episodio | Escenas | Idea fuerza |
|---|---|---|
| E1 · ¿Cuál es el mejor filtro? | 01 LaPregunta, 02 ProyeccionOtraVez, 03 DeVariablesAProcesos, 04 EcuacionesNormales | El mejor filtro lineal es el que deja el error perpendicular a todo lo que ve; escrito con correlaciones, es un sistema de ecuaciones |
| E2 · Lo que sabe el pasado | 05 CuantoPasadoHaceFalta, 06 YuleWalker, 07 ElProcesoBandeado, 08 PorQueSirveLaVieja | Más pasado baja el error cada vez menos, y un dato puede servir aunque no se parezca a lo que buscas, si ayuda a limpiar otro |
| E3 · Mirar el registro entero | 09 TodoElRegistro, 10 UnaDivisionPorFrecuencia, 11 RepartirLaGanancia, 12 ElErrorYLaCoherencia, 13 DeshacerElBorron | Con el registro entero, el sistema infinito se resuelve con una división en cada frecuencia: la misma cuenta del capítulo 8, frecuencia a frecuencia |
| E4 · El futuro no está disponible | 14 SoloParaMayorOIgualACero, 15 MedicionesBlancas, 16 BlanquearPrimero, 17 LaFormulaCausal | Sin el futuro ya no se puede transformar; se arregla blanqueando primero, y por eso hace falta el factor de fase mínima |
| E5 · El sensor, de punta a punta | 18 ElModeladorDelSensor, 19 LaParteCausal, 20 ElFiltroPorDentro, 21 ElPrecioDeLaCausalidad | El filtro causal del sensor sale de una ecuación de segundo grado; es el límite del FIR y se implementa con dos multiplicaciones |
| E6 · Lo nuevo y lo que ya sabías | 22 LaInnovacion, 23 TirarLoImpredecible, 24 FiltrarNoEsPredecir, 25 LosTresSabores | Cada muestra trae algo nuevo e imposible de predecir; predecir es tirarlo, y la muestra de ahora vale más que todo el futuro |
| E7 · De Wiener a Kalman | 26 ElSensorComoSistema, 27 ElObservadorEsElFiltro, 28 SinConocerLasCorrelaciones, 29 TodoEsUnaProyeccion | El filtro de Wiener causal es un observador con la ganancia bien puesta; sin correlaciones conocidas, un filtro que se adapta baja por la parábola |

Narración base por episodio (sin gancho ni cierre): E1 ≈ 1.290 palabras, E2 ≈
1.200, E3 ≈ 1.480, E4 ≈ 1.250, E5 ≈ 1.330, E6 ≈ 1.200, E7 ≈ 1.365: entre 8 y
10 min de voz; con gancho y cierre, ~9–11 min. E3 es el más largo: si al armar
su `guion.md` pasa de ~10,5 min, la escena 13 (deconvolución) es la candidata
a recortarse. El gancho y el cierre de cada episodio **no** están aquí: se
escriben al armar el `guion.md` del episodio (README §2, paso 8). Cada cierre
anuncia el episodio siguiente por su título. El E1 lo anuncia el cierre del
último episodio del capítulo 11 (su escena 32 ya deja dicho que separar la voz
del murmullo es estimar una variable a partir de otra, frecuencia por
frecuencia). **El título de este E1, «¿Cuál es el mejor filtro?», es el que
tiene que decir ese cierre** (el README del capítulo 11 lo dejaba abierto).
El cierre de E7 anuncia el E1 del capítulo 13 (Detección de señales), que ya
tiene guion base y se titula **«Más datos no bastan»** (empieza con el radar):
la escena 29 ya deja preparado «estimar es adivinar lo mejor; detectar es
decidir sí o no» y termina con ese título.

## Números del sensor (comprobados con Python)

Señal y: media 0 (centrada), autocovarianza 4 · 0,6^|m| (varianza 4). Ruido v:
blanco, varianza 1, sin relación con y. Medida x = y + v. Autocorrelación de x:
5, 2,4, 1,44… Correlación cruzada de y con x: 4, 2,4, 1,44… Densidad de la
señal S_yy = 2,56 / |1 − 0,6 e^{−jΩ}|² (la del eco del capítulo 11).

| Qué | Valor |
|---|---|
| Error sin mirar nada (estimar por la media) | 4 |
| FIR, L = 1 · 2 · 3 · más | 0,8 · 0,7401 · 0,7387 · 0,7386 |
| Coeficientes del FIR largo | 0,7386 · 0,1158 · 0,0182 · 0,0028 (cociente 0,157 cada vez) |
| FIR de L = 3 | h = (0,739; 0,116; 0,020) |
| No causal: S_yy en Ω = 0, π/2, π | 16 · 1,88 · 1 |
| No causal: H = S_yy/(S_yy + 1), coherencia² | 0,94 · 0,65 · 0,5 |
| No causal: error total (media de S_ee = H) | 0,686 |
| Filtro no causal, coeficientes | h[0] = 0,686; h[±1] = 0,108; h[±2] = 0,017 |
| Factorización: 3,92 − 0,6 (z + 1/z) | raíces 6,377 y 0,1568 |
| Cero de F, polo de F | 0,1568 y 0,6 |
| Varianza de la innovación | 3,826 |
| Filtro causal H(z) | 0,7386 / (1 − 0,1568 z⁻¹) |
| Recursión | ŷ[n] = 0,157 ŷ[n − 1] + 0,739 x[n] |
| Error causal (filtrado) | 0,7386 |
| Lo que se tira al ser causal | 0,0526 (= 0,7386 − 0,686) |
| Predictor de un paso de y desde el pasado de x | 0,443 z⁻¹ / (1 − 0,157 z⁻¹); error 2,826 |
| Predictor con una sola muestra x[n − 1] | 0,48; error 2,848 |
| Predicción de x sin ruido (eco del 0,6) | 0,6 · x[n]; error 2,56 |
| Kalman: ganancia | 0,7386 = 2,826 / (2,826 + 1) |
| Observador: ℓ, polo | ℓ = −0,443; polo 0,157 |
| Proceso bandeado ρ = 0,4, predecir x[n+1] | L = 1: 0,4, error 0,84; L = 2: (0,476; −0,190), error 0,810 |
| Deconvolución (promediador ½, ½): 1/\|G\| en 0,1π · 0,5π · 0,9π | 1,01 · 1,41 · 6,39 |
| Wiener de la deconvolución en 0,9π (señal 1, ruido 0,1) | factor 0,20, ganancia 1,26 |

Comprobaciones cruzadas: la potencia de x = σ_ε² · (1 + 0,443²/0,64) = 3,826 ·
1,307 = 5 ✓; el error de filtrado 0,7386 = ganancia de Kalman × varianza del
ruido; la ganancia de Kalman = 0,6 (1 − K) da el polo 0,157 ✓.

## Hilos que cruzan el capítulo

Para quien arme cada episodio: estos bucles ya están sembrados en la
narración y hay que respetarlos (y retomarlos en ganchos y cierres).

- **El ejemplo que vuelve: el sensor con su cable ruidoso** (escenas 01 a
  28): mismo dibujo y mismos números que el capítulo 10 (varianza 4, 0,6 por
  paso, ruido de varianza 1). El capítulo 10 dejó **0,8** y **0,74** a mano; aquí
  se generaliza (04, 05) y se termina en 0,7386 (20). **Bucle E1 → E5**.
- **«¿A qué se acerca el error?»** (escena 05, E2): el error del FIR baja a
  0,7386 y los coeficientes decaen con cociente 0,157, no 0,6. Se paga en la
  escena 19 (E5): 0,157 es el cero de la factorización, y 0,7386 el error del
  filtro causal. **Bucle E2 → E5** (largo, a propósito).
- **«Se resuelve con una división»** (escena 09, E3): la igualdad vale en
  todo el eje, por eso se puede transformar. Se anuncia que «en el episodio
  cuarto veremos qué pasa cuando no». **Se paga en la escena 14 (E4)**.
- **Blanquear primero** (capítulo 11, escena 27): se sembró allí. La escena 16
  lo usa como estrategia del filtro causal y la 29 lo lanza al capítulo 13 (con
  el filtro adaptado).
- **Fase mínima** (capítulo 11, escena 28): los coeficientes (2, 1) y (1, 2),
  con inversas que se apagan o explotan. La escena 16 los retoma con el mismo
  dibujo y dice para qué servía: «era la pieza del capítulo doce».
- **Las tres barras ρ, 1, ρ con ρ = 0,4** (capítulos 11 y aquí escenas 07 y
  08): el proceso bandeado del apunte es el mismo que se fabricó con el filtro
  (2, 1) dividido entre √5. Mismo dibujo.
- **El eco del 0,6** (capítulo 11 escena 26, aquí escenas 06, 22 y 23): la
  salida es 0,6 por la anterior más una moneda. Ahí «solo importa la última
  muestra» (06) y la innovación es la moneda (22).
- **El promediador (½, ½)** (capítulo 10 escena 25, aquí escena 13): el
  borroneo. Su ganancia se anula en π.
- **La parábola del error** (capítulo 10, escenas 12 y 22: mínimo 2,56): en la
  escena 02 sale otra vez, ahora como error en función del coeficiente, y su
  vértice es «error perpendicular al dato»; en la 28 el filtro adaptativo baja
  rodando por ella. **Bucle E1 → E7**.
- **Proyección ortogonal, tercera vez** (capítulos 7 y 8): escena 02 (con
  variables) y escena 29 (cierre del capítulo). Mismo dibujo de las flechas.
- **«No correlacionado no es inútil»** (capítulo 8, ejemplo de regresión):
  escena 08.
- **La coherencia** (capítulo 11, escenas 31 y 32): escena 12 paga la
  promesa: «un rho por frecuencia» es lo que decide cuánto error queda. Y
  γ ≤ 1 (la parábola de Cauchy-Schwarz) es lo que garantiza que el error no
  sea negativo. (Ojo: el capítulo 7 dice que esa parábola «volverá dos veces
  más» y con los capítulos 10 y 11 son más: hay que corregir la frase.)
- **La muestra de ahora vale más que todo el futuro** (escenas 21, 24, 25):
  0,7386 frente a 0,686 (poder mirar el futuro) y frente a 2,826 (no tener la
  muestra actual).
- **Kalman = Wiener** (escenas 26 y 27): el 0,443 y el 0,157 del predictor de
  la escena 24 son el observador de la 27, y el 0,7386 del filtro es la
  ganancia de Kalman. **Bucle E6 → E7**.
- **Puentes a otros capítulos** (Parte 4.5 del "en profundidad"):
  - capítulo 13: la factorización espectral y el blanqueador 1/F son el
    primer paso de la detección en ruido coloreado (escena 29);
  - capítulo 6 (control): el observador (escena 26).
- **Cierre del capítulo** (escena 29): estimar es adivinar lo mejor; el
  capítulo 13 decide sí o no, y su E1 se titula «Más datos no bastan».

## Recortes decididos

- La derivación completa de la fórmula causal por innovaciones y de su
  rearmado (Parte 1.3): se hace en el sensor, con las dos colas, y se remite
  al apunte. La condición de Paley-Wiener solo como idea («no se puede
  blanquear lo que no existe», ya sembrada en el capítulo 11).
- El factor de escala que el resumen se come en la ecuación de Kalman
  (Parte 1.5): se dice «con un factor de escala que se calcula» y se remite al
  apunte; con el sensor sale 3,826 = varianza de la innovación (escena 18).
- La ecuación de Riccati: solo se nombra (escena 27).
- El caso x = 2y + v del apunte (ejemplo canónico): no entra; el sensor con x = y + v
  basta para ver el reparto de ganancia (escena 11).
- El estimador de las correlaciones con sesgo y varianza y Levinson-Durbin con
  los coeficientes de reflexión: se dicen las ideas y el coste (escena 28), no
  la recursión.
- Los filtros adaptativos (RLS, NLMS): solo el LMS, con la parábola y una
  iteración a mano.
- La actividad 12.5 (pérdida aleatoria de muestras), la 12.16 (predicción con
  el cero fuera del círculo) y los Ejercicios Propuestos no se resuelven; los
  números son del sensor de los capítulos anteriores, del "en profundidad"
  (proceso bandeado) o inventados redondos (deconvolución, LMS).
- Suavizado con retardo fijo y todo lo demás de la Parte 4.1: solo la tabla.
- El tiempo continuo: tres fórmulas dichas en una escena (29). El
  ruido blanco continuo como idealización se nombra.

## Pronunciación

Probar de oído antes de sintetizar (README §9): Wiener, Kalman, Levinson,
Durbin, Toeplitz, Yule-Walker, Paley, Riccati, Parseval, Fourier. Siglas: FIR
(«fir», ya probada en el capítulo 10), LMS («ele, eme, ese»), MMSE («eme eme
ese e»: se evita, «el error cuadrático medio mínimo»). Letras: «uve» (para v),
«i griega sombrero», «omega mayúscula» (Ω), «zeta», «alfa» (α), «beta», «kappa»,
«épsilon» (ε, la innovación), «gamma» (γ), «hache» (h), «ele» (L), «eme» (m),
«ka» (k), «jota» (j), «mu» (μ). Palabras: «innovación», «observador»,
«autorregresivo», «Toeplitz» (la más dudosa), «deconvolución»,
«blanqueador». «z a la menos uno» para z⁻¹.

## Piezas visuales nuevas

Van a `comun/figuras.py` (sección «capítulo 12, episodio N»):
- el sensor con su cable: `y` (azul) más `v` (magenta) da `x` (cian); una
  realización con las tres curvas (E1, todo el capítulo);
- la parábola del error J(h) con un punto que se desliza y una pendiente
  (E1, E7);
- flechas de proyección (las del capítulo 8: y, x, la sombra y el error a 90°)
  (E1, E7);
- `BloqueLTI` con «−μx» a la entrada y «+μy» a la salida y una ventana de L
  muestras que se desliza sobre x[n] (E1) (prevista en el README);
- matriz de Toeplitz con las diagonales pintadas (E1, E2);
- barras de error por tamaño de ventana, que bajan y se quedan planas (E2);
- las tres barras ρ, 1, ρ y el par de monedas w[n−1], w[n], w[n+1] con qué
  contiene cada muestra (E2);
- `Espectro` (prevista): densidad S_yy del sensor con la ganancia H del filtro
  como curva ámbar encima, con `ValueTracker` sobre Ω (E3) y coherencia² como
  curva (E3);
- dos secuencias que coinciden en m ≥ 0 y difieren en m < 0 con sus
  transformadas (E4);
- una secuencia de dos colas (m ≥ 0 y m < 0) con tijera que corta la de m < 0
  (E4, E5);
- el plano z con el círculo unidad, polos (×) y ceros (○) que se mueven
  dentro y fuera (E4, E5, E7);
- cadena de bloques «w blanca → F → x» y «x → 1/F → ε blanca» (E4, E6);
- tabla de errores que se llena: media, predicción, filtrado, suavizado (E6);
- espacio de estados como cajitas con un observador que predice y corrige
  (E7);
- corte transversal del registro: tres ventanas (pasado, pasado + presente,
  todo) (E1, E6).

---

# Escena 01 — LaPregunta

**Objetivo:** plantear la pregunta del capítulo (cuál es el mejor filtro
lineal para recuperar una señal contaminada), cobrar la promesa del capítulo
11 (estimar una variable a partir de otra) y fijar el escenario: el sensor de
temperatura con su cable ruidoso, las letras y, v, x, ŷ, e, y el mapa de las
tres versiones del filtro.

**Qué hace falta saber antes:** capítulo 11 (escena 32: en cada frecuencia,
dos procesos son dos variables); capítulo 10 (el sensor de varianza 4 y
memoria 0,6, y el ruido de varianza 1 de la escena 23).

**Visual:**
- La voz (azul) y el murmullo (magenta) del capítulo 11, con un colador y un
  signo de interrogación; se funden en el sensor.
- El sensor: una curva lenta azul (la temperatura), un ruido magenta rápido y
  encima la suma cian, que es lo que llega al ordenador.
- Rótulos con los papeles fijos: «y[n] = la señal» (azul), «v[n] = el ruido»
  (magenta), «x[n] = y[n] + v[n]» (cian), «ŷ[n] = la estimación» (ámbar).
  Aviso: «antes: s, d, r».
- «error cuadrático medio = E[(y − ŷ)²]» con el error en rojo.
- Tres puertas con una ventana cada una: «unas pocas muestras (FIR)», «todo el
  registro» y «presente y pasado». Detrás de la última, un rótulo «Wiener».
  Una silueta de cohete al fondo: «Kalman».

## Narración

<!-- b1 -->
El capítulo anterior terminó con una promesa: en cada frecuencia, dos procesos
son dos variables aleatorias, y separar la voz del murmullo es estimar una
variable a partir de otra. Hoy la cumplimos, y con un ejemplo que ya
conoces. El sensor de temperatura: media de veinte grados, varianza cuatro y
una memoria de cero coma seis por paso.

<!-- b2 -->
Ahora el cable le suma un ruido: blanco, sin memoria, de varianza uno y sin
relación con la temperatura. Lo que llega al ordenador es la temperatura más
el ruido. Y queremos recuperarla. Cambiamos las letras para coincidir con el
libro. La temperatura es i griega de ene, en azul. El ruido es uve de ene, en
magenta. Y lo medido es equis de ene, en cian: la suma de las dos.

<!-- b3 -->
Buscamos un filtro que reciba equis y devuelva una estimación de i griega,
que escribimos i griega con sombrero. ¿Cuál es la mejor? La medida de siempre:
el error cuadrático medio, la media del cuadrado de la diferencia entre la
temperatura verdadera y la estimada. Y el filtro tiene que ser lineal: una suma
de muestras de equis, cada una multiplicada por un coeficiente.

<!-- b4 -->
El problema tiene tres versiones, de dificultad creciente, según cuántas
muestras pueda mirar el filtro. Primera: unas pocas muestras recientes. Segunda:
el registro entero, con pasado y futuro. Tercera: el presente y todo el
pasado, pero nada del futuro, que es lo que puede hacer un aparato en tiempo
real, y es la difícil. La resolvió Norbert Wiener a principios de los años
cuarenta, y por eso se llama filtro de Wiener.

<!-- b5 -->
Y al final habrá una sorpresa: ese filtro, escrito de otra manera, es el que
sigue a un cohete en pleno vuelo, el filtro de Kalman. Pero empecemos por
algo que ya sabemos, porque es la clave de todo el capítulo: este problema es,
exactamente, el que resolvimos en el capítulo ocho con variables aleatorias.

---

# Escena 02 — ProyeccionOtraVez

**Objetivo:** recordar la mejor estimación lineal con el caso más pequeño, una
sola medición del sensor, y ver que las tres formas de pensarla son la misma:
minimizar la parábola del error, derivar e igualar a cero, y pedir que el error
sea perpendicular al dato. Resultado: h = 4/5 = 0,8, error 0,8 (el del capítulo
10). Dejar dicho que con varias mediciones salen las ecuaciones normales y el
error σ²(1 − ρ²).

**Qué hace falta saber antes:** escena 01; capítulo 8 (estimación lineal,
flechas y perpendicular); capítulo 10 (escena 23: h = 0,8, y la parábola de las
escenas 12 y 22); derivada = pendiente (se recuerda aquí).

**Visual:**
- «ŷ = h · x» y el error «e = y − h x». Una parábola J(h) con un punto que
  se desliza por ella al mover h (`ValueTracker`).
- Renglones, uno por regla: «(y − h x)² = y² − 2h y x + h² x²», «E[y²] = 4»,
  «E[y x] = 4 + 0 = 4», «E[x²] = 4 + 1 = 5» → «J(h) = 4 − 8h + 5h²».
- La pendiente en el punto (una recta tangente que rota); en el vértice está
  horizontal: «pendiente = −8 + 10 h = 0 → h = 0,8», «J(0,8) = 0,8».
- Las flechas del capítulo 8, mismo dibujo: y, x, la sombra de y sobre x y el
  error a 90°. «E[e x] = 0».
- «C_xx a = c» y «MMSE = σ_y² − cᵀ C_xx⁻¹ c = σ_y² (1 − ρ²)».

## Narración

<!-- b1 -->
Recordemos el capítulo ocho con una sola medición. Trabajamos con la temperatura
ya centrada, restándole sus veinte grados, y la estimación es un múltiplo de lo
medido: i griega con sombrero igual a hache por equis. Probemos valores de
hache y midamos el error cuadrático medio: la media de i griega menos hache por
equis, todo al cuadrado.

<!-- b2 -->
Desarrollamos el cuadrado: i griega al cuadrado, menos dos hache por i griega
por equis, más hache al cuadrado por equis al cuadrado. Tomamos la media de
cada término, por linealidad. La de i griega al cuadrado es la varianza:
cuatro. La de i griega por equis: equis es i griega más ruido, y el ruido no
se relaciona con la temperatura, así que también cuatro. La de equis al
cuadrado, cuatro más uno: cinco.

<!-- b3 -->
El error queda cuatro, menos ocho hache, más cinco hache al cuadrado: una
parábola. Una parábola abierta hacia arriba tiene su punto más bajo donde la
pendiente es cero, y la pendiente es la derivada: menos ocho más diez hache.
Igualada a cero, hache vale ocho décimos: cero coma ocho. Y el error ahí es
cero coma ocho, el resultado del capítulo diez.

<!-- b4 -->
Ahora, lo mismo con flechas. Esa derivada, escrita con medias, es menos dos
por la media del error por equis. Que valga cero significa que el error es
perpendicular al dato. La mejor estimación es la proyección de la flecha de i
griega sobre la flecha de equis, con el error en ángulo recto. Es la geometría
de los capítulos siete y ocho: la parábola y la perpendicular son la misma
condición.

<!-- b5 -->
Con varias mediciones hay que pedir esa perpendicularidad con cada una. Salen
las ecuaciones normales: la matriz de covarianzas de las mediciones, por los
coeficientes, igual al vector de covarianzas con lo que se estima. Y el error
es la varianza menos lo que la proyección explica: la varianza por uno menos
rho al cuadrado. Todo el capítulo es este resultado. La única novedad es que las
mediciones van a ser muestras de un proceso.

---

# Escena 03 — DeVariablesAProcesos

**Objetivo:** pasar de variables a procesos. Con la ventana de las L muestras
más recientes de x, la estimación es una suma pesada; como y y x son
conjuntamente estacionarios, los coeficientes son los mismos para todo n, y eso
convierte la estimación en un filtro LTI (FIR). Recordar qué hacer con las
medias. Presentar los tres sabores según qué muestras se usan (predecir,
filtrar, suavizar).

**Qué hace falta saber antes:** escena 02; capítulo 10 (escena 09:
estacionario; escena 25: convolución como suma de entradas recientes pesadas);
capítulo 10 (escenas 26 y 27: conjuntamente estacionarios, la relación entre
dos procesos depende solo de la distancia) y capítulo 11 (escena 29:
correlación cruzada).

**Visual:**
- La curva cian x[n] con una ventana de L = 3 muestras marcadas («x[n]»,
  «x[n−1]», «x[n−2]»), cada una con su coeficiente en ámbar: «ŷ[n] = h₀ x[n]
  + h₁ x[n−1] + h₂ x[n−2]».
- La ventana se desliza una muestra a la derecha y los coeficientes **no
  cambian**; un candado sobre los h.
- «BloqueLTI»: «x[n] → (−μ_x) → h → (+μ_y) → ŷ[n]».
- Tres cortes del registro: predecir (solo antes del ahora), filtrar (hasta el
  ahora) y suavizar (todo). Un reloj para «tiempo real» y una cinta de vídeo
  para «grabación ya hecha».
- Pregunta: «3 coeficientes → ¿cuántas condiciones?».

## Narración

<!-- b1 -->
Ahora las mediciones no son variables sueltas, sino muestras de un proceso.
Para estimar la temperatura en el instante ene, usamos las ele últimas muestras
medidas: la de ahora, la anterior, la anterior a esa. La estimación es una
suma: hache cero por equis de ene, más hache uno por equis de ene menos uno,
y así hasta ele muestras.

<!-- b2 -->
Ahora avanzamos un instante. La ventana se desliza una muestra y hay que
volver a estimar. ¿Cambian los coeficientes? No. Como la temperatura y lo medido
son conjuntamente estacionarios, su relación depende solo de la distancia entre
muestras, no del instante en que miremos. La cuenta sale igual, y los mismos
coeficientes valen siempre.

<!-- b3 -->
Eso es lo que convierte un problema de estimación en un filtro. Una suma de
muestras recientes con coeficientes fijos es una convolución, como la del
promediador del capítulo diez: un filtro lineal e invariante en el tiempo, con
respuesta al impulso hache. Si las señales tienen media, se le resta a la
entrada la de equis, y se le suma a la salida la de i griega.

<!-- b4 -->
Fíjate en qué muestras se usan, porque de ahí salen tres problemas. Estimar i
griega de ene con equis de ene y las anteriores se llama filtrar. Usar solo
las anteriores, sin la de ahora, es predecir. Y usar todo el registro, incluso
lo que viene después, es suavizar, y solo sirve para grabaciones que ya están
hechas. El capítulo entero es una pregunta con tres tamaños de ventana.

<!-- b5 -->
Ahora, una pregunta antes de seguir. Con tres coeficientes por encontrar, ¿cuántas
condiciones de perpendicularidad tendremos? Piénsalo un momento. Tres: una
por cada muestra de la ventana. Tres ecuaciones y tres incógnitas. Vamos a
escribirlas, esta vez sin saltarnos ninguna cuenta.

---

# Escena 04 — EcuacionesNormales

**Objetivo:** deducir entera la condición de ortogonalidad y las ecuaciones
normales del filtro FIR, ver que la matriz es de Toeplitz y simétrica, resolver
el sensor con L = 3, y dar el error con el filtro óptimo (sin repetir la
cuenta de cada término: se apoya en «el error es perpendicular a la
estimación»).

**Qué hace falta saber antes:** escena 03; escena 02 (parábola, derivada,
perpendicular); capítulo 10 (escena 24: 0,74 con dos muestras); sistema de
ecuaciones y matriz (se recuerdan aquí).

**Visual:**
- «J(h) = E[(y − Σ h_k x[n−k])²]». Renglones de la derivada respecto de h_j
  → «−2 E[e[n] x[n−j]] = 0», «e ⟂ x[n−j]» con la flecha a 90°.
- Se mete ŷ: «E[y x[n−j]] = Σ h_k E[x[n−k] x[n−j]]» → «C_yx[j] = Σ h_k
  C_xx[j−k]». Sello «ecuaciones normales».
- La matriz 3 × 3 con las diagonales pintadas del mismo color (Toeplitz),
  simétrica; «cada elemento depende solo de la distancia».
- Con el sensor: matriz «5, 2,4, 1,44 / 2,4, 5, 2,4 / 1,44, 2,4, 5», vector «4,
  2,4, 1,44», resultado «0,739 · 0,116 · 0,020» como tres barras sobre x[n],
  x[n−1], x[n−2].
- «error = C_yy[0] − Σ h C_yx» y la cifra «0,74».

## Narración

<!-- b1 -->
Queremos los coeficientes que hacen mínimo el error cuadrático medio, que
depende de los ele coeficientes a la vez. Es como la parábola de antes, pero
con varias dimensiones: tiene un único punto más bajo, donde la pendiente
respecto de cada coeficiente es cero. Derivamos respecto de hache de jota y sale
menos dos por la media del error por equis de ene menos jota. Igualamos a
cero.

<!-- b2 -->
Eso dice que el error es perpendicular a cada muestra de la ventana, para jota
desde cero hasta ele menos uno. Metemos dentro la estimación y pasamos la suma
al otro lado. A la izquierda queda la correlación cruzada entre i griega y
equis, a distancia jota. A la derecha, la suma de hache de ka por la
autocorrelación de equis, a distancia jota menos ka.

<!-- b3 -->
Esas son las ecuaciones normales: para cada jota, la suma de hache de ka por la
autocorrelación en jota menos ka es la correlación cruzada en jota. Escritas
ordenadas, forman una matriz cuadrada en la que cada elemento depende solo de
la distancia entre su fila y su columna. Por eso cada diagonal es constante.
Se llama matriz de Toeplitz, y además es simétrica.

<!-- b4 -->
Con el sensor y tres muestras. La autocorrelación de lo medido vale cinco en
cero, dos coma cuatro a un paso y uno coma cuatro cuatro a dos: la de la
temperatura, más el uno del ruido en el cero. La correlación cruzada es solo
la de la temperatura: cuatro, dos coma cuatro, uno coma cuatro cuatro.
Resolvemos: cero coma siete tres nueve, cero coma uno uno seis y cero coma
cero dos cero.

<!-- b5 -->
La muestra de ahora manda, la anterior aporta un poco y la de hace dos pasos
casi nada. El error que queda es la varianza menos lo que el filtro explica, y
sale cero coma siete cuatro. Con una muestra eran cero coma ocho; sin mirar
nada, cuatro. Y aquí viene la pregunta que abre el siguiente episodio: si
seguimos añadiendo muestras, ¿hasta dónde baja?

---

# Escena 05 — CuantoPasadoHaceFalta

**Objetivo:** ver cómo baja el error al aumentar L (4, 0,8, 0,74, 0,7387, 0,7386),
por qué nunca sube y por qué baja cada vez menos (la memoria de 0,6). Ver que los
coeficientes decaen con cociente 0,157 (no 0,6) y sembrar el bucle: ¿a qué filtro
se acerca? (se paga en la escena 19). Regla práctica para elegir L.

**Qué hace falta saber antes:** escena 04.

**Visual:**
- Barras de error a medida que L crece: «0 muestras: 4», «L = 1: 0,8», «L = 2:
  0,740», «L = 3: 0,7387», «L = ∞: 0,7386». Las barras bajan y se aplanan
  (`c12p-fir-convergencia.svg`).
- «L + 1 puede imitar a L con h_L = 0»: una casilla nueva a cero.
- Los coeficientes como barras cada vez más chicas: «0,7386 · 0,1158 · 0,0182 ·
  0,0028», con un cociente entre cada par: «× 0,157 · × 0,157 · × 0,157». Un
  «¿por qué 0,157 y no 0,6?» en ámbar con una pausa.
- Un candado con «filtro de Wiener causal» y una etiqueta «episodio 5».

## Narración

<!-- b1 -->
¿Cuántas muestras hacen falta? Sin mirar ninguna, el error es cuatro. Con una
muestra, cero coma ocho. Con dos, cero coma siete cuatro cero. Con tres, cero
coma siete tres ocho siete. Y con cuatro, cinco, diez, cero coma siete tres
ocho seis: deja de bajar. Añadir muestras sirve cada vez menos.

<!-- b2 -->
Dos razones. La primera: añadir una muestra nunca empeora nada, porque el
filtro nuevo puede imitar al anterior poniendo a cero el coeficiente extra. La
segunda: la temperatura recuerda cero coma seis por paso, así que lo que pasó hace
cinco pasos, cero coma seis a la quinta, unos ocho por ciento, casi no dice
nada de hoy.

<!-- b3 -->
Mira ahora los coeficientes: cero coma siete tres ocho seis, cero coma uno uno
cinco ocho, cero coma cero uno ocho dos, cero coma cero cero dos ocho. Divide
cada uno entre el anterior: cero coma uno cinco siete, cero coma uno cinco siete,
cero coma uno cinco siete. Una progresión geométrica perfecta. Y aquí va la
sorpresa: ¿por qué cero coma uno cinco siete y no cero coma seis? Piénsalo.

<!-- b4 -->
No lo vamos a contar todavía: lo descubriremos en el episodio cinco, y saldrá
de una ecuación de segundo grado. Y el número al que se acerca el error, cero
coma siete tres ocho seis, tampoco es casual: es el error del mejor filtro que
puede usar todo el pasado. Ese filtro tiene nombre: es el filtro de Wiener
causal.

<!-- b5 -->
Regla práctica: aumentar ele hasta que el error deje de bajar o el último
coeficiente sea despreciable. Pero hemos estado estimando la temperatura de
ahora. Estas mismas ecuaciones sirven para algo todavía más tentador: adivinar
lo que todavía no ha ocurrido.

---

# Escena 06 — YuleWalker

**Objetivo:** escribir las ecuaciones normales de la predicción (Yule-Walker):
la misma matriz, y el lado derecho son las autocorrelaciones a distancia 1,
2, … L. Resolver a mano con el eco del 0,6 (proceso sin ruido): h = (0,6; 0),
solo cuenta la última muestra. Dejar la pregunta de si pasa siempre.

**Qué hace falta saber antes:** escena 04 (ecuaciones normales); capítulo 10
(escenas 21 y 22: predecir con una muestra, el sensor y el error 2,56);
capítulo 11 (escena 26: el eco del 0,6).

**Visual:**
- «x̂[n+1] = h₀ x[n] + h₁ x[n−1]»; una ventana sobre x[n], x[n−1] y una flecha
  hacia x[n+1] con un «?».
- La matriz de las escenas anteriores, ahora con el vector «C[1], C[2]».
  Sello «Yule-Walker».
- Con el eco sin ruido: «C[m] = 4 · 0,6^|m|»: «4, 2,4, 1,44». Sistema:
  «4 h₀ + 2,4 h₁ = 2,4», «2,4 h₀ + 4 h₁ = 1,44». Comprobación con «h = (0,6;
  0)»: «2,4 ✓», «1,44 ✓».
- Una barra alta sobre x[n] y otra vacía sobre x[n−1]. «error = 2,56».
- Una interrogación sobre otro proceso.

## Narración

<!-- b1 -->
Ahora sin ruido. Tenemos el proceso equis y queremos adivinar la muestra que
viene, equis de ene más uno, con las ele últimas. Hacemos la misma cuenta: el
error tiene que ser perpendicular a cada muestra usada. La única diferencia es
lo que estimamos: la correlación de la derecha ya no es la cruzada, sino la
autocorrelación de equis a distancia uno, dos, hasta ele.

<!-- b2 -->
Con una muestra, el coeficiente es la autocorrelación en uno entre la
autocorrelación en cero, es decir, el coeficiente de correlación: es el
predictor del capítulo diez. Con dos muestras, la misma matriz de antes, y a la
derecha, la correlación en uno y la correlación en dos. Estas ecuaciones se
llaman de Yule-Walker.

<!-- b3 -->
Aparecen en muchos sitios: para modelar una señal como el resultado de filtrar
ruido, lo que se llama un modelo autorregresivo, y en la codificación de la
voz, donde cada muestra se predice con las anteriores y solo se guarda lo que
falta. Probémoslas con el eco del cero coma seis, sin ruido: autocorrelación
cuatro, dos coma cuatro y uno coma cuatro cuatro.

<!-- b4 -->
Las dos ecuaciones: cuatro hache cero más dos coma cuatro hache uno igual a dos
coma cuatro, y dos coma cuatro hache cero más cuatro hache uno igual a uno
coma cuatro cuatro. Probamos hache cero igual a cero coma seis y hache uno igual
a cero. Primera: dos coma cuatro. Segunda: uno coma cuatro cuatro. Las dos
salen. Solo importa la última muestra.

<!-- b5 -->
Tiene sentido: el eco es cero coma seis por la salida anterior más una moneda
nueva, así que la última muestra ya lo contiene todo. El error es dos coma cinco
seis, el mínimo de la parábola del capítulo diez. Pero cuidado con generalizar.
Existe un proceso en el que una muestra sin ninguna relación con el futuro tiene
un coeficiente distinto de cero. ¿Te atreves a imaginar cuál?

---

# Escena 07 — ElProcesoBandeado

**Objetivo:** el caso que rompe la intuición: el proceso con correlación solo
a un paso (las tres barras ρ, 1, ρ con ρ = 0,4 del capítulo 11). Predecir x[n+1]
con L = 1 (h = 0,4, error 0,84) y con L = 2 (h = (0,476; −0,190), error 0,810).
La muestra x[n−1] tiene correlación cero con x[n+1] y aun así se usa, con signo
negativo.

**Qué hace falta saber antes:** escena 06; capítulo 11 (escenas 07 a 10: las
tres barras y el filtro (2, 1)/√5).

**Visual:**
- Las tres barras del capítulo 11: «ρ, 1, ρ» con ρ = 0,4 y ceros a partir de
  dos pasos. Se resalta «distancia 2 → 0».
- L = 1: «h = ρ = 0,4» y «error = 1 − 0,4² = 0,84».
- L = 2: sistema «h₀ + 0,4 h₁ = 0,4» y «0,4 h₀ + h₁ = 0».
  Eliminación a mano: «h₁ = −0,4 h₀», «h₀ (1 − 0,16) = 0,4», «h₀ = 0,476»,
  «h₁ = −0,190».
- Barras sobre x[n] (positiva) y x[n−1] (negativa, en rojo). «error = 1 −
  0,476 · 0,4 = 0,810».
- Un cartel «correlación con x[n+1]: 0» junto a x[n−1] y un signo de
  interrogación.

## Narración

<!-- b1 -->
Recordemos el proceso de las tres barras, el de ro igual a cero coma cuatro,
que fabricamos en el capítulo once con el filtro de dos coeficientes. Cada
muestra se parece solo a sus vecinas inmediatas: correlación uno consigo misma,
cero coma cuatro con la de al lado y cero con cualquiera a dos pasos o más.

<!-- b2 -->
Predecimos equis de ene más uno. Con una sola muestra, equis de ene: el
coeficiente es la correlación, cero coma cuatro, y el error, uno menos cero coma
cuatro al cuadrado: cero coma ocho cuatro. Y ahora añadimos la anterior, equis de
ene menos uno. Pero ojo: entre equis de ene menos uno y equis de ene más uno hay
dos pasos, así que su correlación es cero.

<!-- b3 -->
Las ecuaciones: hache cero más cero coma cuatro hache uno igual a cero coma
cuatro, y cero coma cuatro hache cero más hache uno igual a cero. La segunda
dice que hache uno es menos cero coma cuatro hache cero. Lo llevamos a la
primera: hache cero por uno menos cero coma dieciséis, igual a cero coma
cuatro. Hache cero: cero coma cuatro siete seis.

<!-- b4 -->
Y hache uno, menos cero coma cuatro por cero coma cuatro siete seis: menos cero
coma uno nueve. ¡No es cero! La muestra de hace dos pasos, que no tiene ninguna
correlación con la que queremos adivinar, recibe un coeficiente, y negativo. Y se
nota en el error: uno menos cero coma cuatro siete seis por cero coma cuatro, cero
coma ocho uno. Baja.

<!-- b5 -->
Piénsalo un momento: ¿cómo puede servir un dato que no se parece en nada a lo
que buscas? No es un truco de las cuentas ni un error. Hay una explicación
sencilla, y para verla hay que abrir las muestras y mirar qué monedas
contiene cada una.

---

# Escena 08 — PorQueSirveLaVieja

**Objetivo:** explicar por qué sirve una muestra no correlacionada con el
objetivo. Abrir el proceso: x[n] = (2w[n] + w[n−1])/√5. x[n+1] contiene w[n];
x[n] contiene w[n] contaminada con w[n−1]; x[n−1] contiene w[n−1] y no tiene
nada de x[n+1]: sirve para restar la contaminación. Generalizar: no importan
las correlaciones con el objetivo una a una, sino C⁻¹c. Cerrar el episodio.

**Qué hace falta saber antes:** escena 07; capítulo 11 (escena 10: el filtro
(2, 1)/√5 con la moneda w); capítulo 8 (regresión: variable de control).

**Visual:**
- Tres monedas seguidas: «w[n−1]», «w[n]», «w[n+1]» (más «w[n−2]» a la
  izquierda), y debajo las tres muestras como sumas: «x[n+1] = (2 w[n+1] + w[n])/√5»,
  «x[n] = (2 w[n] + w[n−1])/√5», «x[n−1] = (2 w[n−1] + w[n−2])/√5».
- Se colorea cada moneda: «w[n+1]: nueva, imposible» (rojo); «w[n]: lo que
  ya se puede saber» (verde); «w[n−1]»: contaminación (magenta).
- Una resta dibujada: «x[n] − 0,4 x[n−1]» limpia w[n−1].
- «h = C_xx⁻¹ c» con «c = (0,4; 0)» y el «0» tachado con «no manda solo».
- El mapa del capítulo hasta aquí (una ventana finita hacia atrás) y la
  siguiente ventana, entera, con «¿y el futuro?».

## Narración

<!-- b1 -->
Abramos las muestras. El proceso sale de una moneda, w, pasada por el filtro de
dos coeficientes: equis de ene es dos veces la moneda de ahora más la anterior,
entre raíz de cinco. Entonces, equis de ene más uno contiene la moneda nueva,
w de ene más uno, imposible de saber, y también la moneda w de ene, que sí
ocurrió ya.

<!-- b2 -->
Y equis de ene, la muestra de ahora, contiene esa misma moneda, w de ene, con
más fuerza. Pero no la trae limpia: viene mezclada con la moneda anterior, w de
ene menos uno. Para predecir equis de ene más uno, esa moneda anterior es
basura: ensucia la única pista que tenemos.

<!-- b3 -->
Ahora mira la muestra de hace dos pasos, equis de ene menos uno. Contiene
justo esa moneda anterior, w de ene menos uno, y otra más antigua. No tiene
ninguna moneda en común con equis de ene más uno, y por eso la correlación es
cero. Pero nos dice cuánta basura lleva equis de ene. Restándola, limpiamos la
pista. De ahí el coeficiente negativo.

<!-- b4 -->
Es lo que pasa en la regresión: una variable de control no se parece al
objetivo, pero ayuda a quitar lo que ensucia a otra variable. Lo que decide un
coeficiente no es la correlación de esa muestra con el objetivo, sino el
resultado de resolver todo el sistema: la inversa de la matriz mezcla los
datos entre sí. No correlacionado no significa inútil.

<!-- b5 -->
Resumamos. Hasta aquí, una ventana finita hacia atrás, y sabemos calcular sus
coeficientes y su error. Pero si la grabación ya está hecha, no hay razón para
mirar solo el pasado: podemos usar todo el registro. Entonces el sistema de
ecuaciones se hace infinito, y ocurre algo que parece magia: se resuelve con una
división.

---

# Escena 09 — TodoElRegistro

**Objetivo:** el filtro sin restricciones (pasado y futuro). La ortogonalidad
se pide con todas las muestras (todo m), lo que da h ∗ C_xx = C_yx para todo m:
una convolución en todo el eje, sin matriz finita. Recordar la convolución y su
transformada (producto) y la frecuencia discreta Ω de −π a π. Como la igualdad
vale en todo m, se puede transformar: H · S_xx = S_yx. Dejar marcada la
condición «vale en todo el eje» para la escena 14.

**Qué hace falta saber antes:** escenas 03 y 04; capítulo 10 (escena 25: la
convolución; su transformada es un producto); capítulo 11 (escena 29: densidad
cruzada, la transformada de la correlación cruzada).

**Visual:**
- La grabación entera, con una ventana que se abre a los dos lados de x[n]:
  «ŷ[n] = Σ h[j] x[n−j], j de −∞ a +∞».
- «e ⟂ x[n−m], para todo m» (una flecha a 90° por cada muestra, hacia los dos
  lados). Se repite el desarrollo: «Σ h[j] C_xx[m−j] = C_yx[m]» → «h ∗ C_xx =
  C_yx», con «para todo m» resaltado en ámbar.
- Una matriz que crece hasta salirse de la pantalla en las dos direcciones:
  «no hay matriz que invertir».
- Dos palitos que se deslizan (la convolución) y la caja de Fourier: «∗ ↔ ×».
- El eje de la frecuencia Ω de −π a π: «0 = continua», «π = la más rápida: + −
  + −».
- «H(Ω) · S_xx(Ω) = S_yx(Ω)» y un pequeño rótulo «todo el eje → se puede
  transformar».

## Narración

<!-- b1 -->
Si la grabación ya está hecha, podemos usar todo el registro: el pasado, el
presente y también lo que vendrá después. La estimación es una suma con
infinitos coeficientes, de menos infinito a infinito: hache de jota por equis
de ene menos jota. Ya no hay ninguna matriz finita que valga.

<!-- b2 -->
La condición es la de siempre: el error, perpendicular a cada muestra que
usamos. Y ahora usamos todas, así que la pedimos para todo eme entero, hacia los
dos lados. Se repite el mismo desarrollo de antes. Sale: la suma de hache de
jota por la autocorrelación en eme menos jota es la correlación cruzada en eme.
Y eso es una convolución: hache convolucionado con la autocorrelación de equis
es la correlación cruzada.

<!-- b3 -->
Recuerda qué hace Fourier con una convolución, de Señales y Sistemas: la
convierte en un producto. En tiempo discreto, la frecuencia, que escribimos
omega mayúscula, va de menos pi a pi. Cero es la continua, sin variación, y pi es
la más rápida: la señal que alterna más, menos, más, menos, en cada muestra.
Ese es el eje sobre el que vamos a trabajar.

<!-- b4 -->
Aquí viene el punto clave. La igualdad, hache convolucionado con la
autocorrelación igual a la correlación cruzada, se cumple para todo eme. Si
dos secuencias son iguales en todas sus muestras, sus transformadas son iguales
en todas las frecuencias. Así que podemos transformar los dos lados: el
producto de hache por la densidad espectral de equis, igual a la densidad
cruzada de i griega con equis.

<!-- b5 -->
Ahora cada frecuencia es una ecuación con una sola incógnita, y se despeja
dividiendo. Un sistema infinito, resuelto con una división. Pero guarda esto
que acabamos de usar: «la igualdad vale para todo eme». En el episodio cuarto
veremos qué pasa cuando no vale, y por qué entonces todo se complica.

---

# Escena 10 — UnaDivisionPorFrecuencia

**Objetivo:** el filtro de Wiener no causal, H = S_yx / S_xx, y su paralelo
con el capítulo 8: con una variable, h = covarianza / varianza = 4/5 = 0,8;
con procesos, en cada frecuencia, densidad cruzada / densidad. Cobrar la
promesa del capítulo 11: en cada frecuencia, dos procesos son dos variables.

**Qué hace falta saber antes:** escena 09; capítulo 11 (escenas 29 a 32:
densidad cruzada y coherencia); escena 02 (h = 0,8).

**Visual:**
- Recuadro: «H(Ω) = S_yx(Ω) / S_xx(Ω)». Sello «filtro de Wiener no causal».
- A la izquierda, el caso de una variable: «h = E[y x] / E[x²] = 4 / 5 =
  0,8» (el dibujo de la escena 02).
- A la derecha, el mismo dibujo por rebanadas: el eje Ω partido en rebanadas y
  en cada una «h(Ω) = S_yx / S_xx».
- El paralelo con el capítulo 8: «a = C_xx⁻¹ c» → «H = S_xx⁻¹ S_yx».
  «S_xx: la matriz de covarianzas», «S_yx: el vector de covarianzas
  cruzadas».
- La voz y el murmullo del capítulo 11 con el colador: «un colador que
  sabe cuánto fiarse de cada frecuencia».

## Narración

<!-- b1 -->
Ya tenemos el filtro: hache de omega es la densidad cruzada entre i griega y
equis, dividida entre la densidad espectral de equis. Se llama filtro de Wiener
no causal, porque usa también el futuro. Es una fórmula muy corta para un
problema con infinitos coeficientes. Y merece que la miremos despacio, porque
no es nueva.

<!-- b2 -->
Recuerda la escena de una sola medición. El coeficiente era la media de i
griega por equis, entre la media de equis al cuadrado: cuatro entre cinco, cero
coma ocho. Una covarianza cruzada dividida entre una varianza. Pues esta es la
misma división, pero hecha en cada frecuencia: la densidad cruzada, que es la
covarianza entre los dos procesos en esa frecuencia, entre la densidad de
equis, que es su varianza.

<!-- b3 -->
Con varias variables, el coeficiente era la inversa de la matriz de
covarianzas por el vector de covarianzas cruzadas. Aquí, la densidad de equis
hace de matriz y la cruzada de vector: la misma fórmula. Es lo que anunciaba
el capítulo once: en cada frecuencia, dos procesos son dos variables.

<!-- b4 -->
Hay una razón profunda. Al pasar a frecuencia, el filtro actúa por separado en
cada omega: lo que hace en una frecuencia no afecta a las demás. Estimar un
proceso a partir de otro se reduce, frecuencia por frecuencia, a estimar una
variable a partir de otra.

<!-- b5 -->
Pongámoslo a prueba con el sensor y su cable ruidoso. Piénsalo antes de
seguir: si la temperatura cambia despacio y el ruido cambia deprisa, ¿en qué
frecuencias te fiarías más de lo medido?

---

# Escena 11 — RepartirLaGanancia

**Objetivo:** aplicar H = S_yx/S_xx al sensor. La señal y el ruido no tienen
relación: S_yx = S_yy y S_xx = S_yy + S_vv, H = S_yy/(S_yy + 1). Con S_yy = 2,56 /
|1 − 0,6 e^{−jΩ}|²: H = 0,94 en Ω = 0; 0,65 en π/2; 0,5 en π. El filtro reparte
ganancia según la relación señal/ruido de cada banda. El estimador «tira hacia
la media».

**Qué hace falta saber antes:** escena 10; capítulo 11 (escena 26: la
densidad del eco del 0,6 y la del ruido blanco, plana); capítulo 10 (escena
22: predecir tira hacia la media).

**Visual:**
- La densidad de la señal S_yy (una montaña en Ω = 0 que baja hacia π) y la del
  ruido S_vv (plana, en 1); la suma S_xx encima.
- «S_yx = S_yy» (el ruido no aporta) y «S_xx = S_yy + S_vv» (las potencias se
  suman). «H = S_yy / (S_yy + S_vv)».
- Tres frecuencias con sus cuentas: «Ω = 0: 16 / 17 = 0,94», «Ω = π/2:
  1,88 / 2,88 = 0,65», «Ω = π: 1 / 2 = 0,5».
- La curva H(Ω) dibujada entera, ámbar, cayendo suavemente. Debajo, lo medido
  y lo estimado en el tiempo: la estimación es más lisa y de menor amplitud
  (`c12-wiener-filtrado.svg`).
- «señal domina → H → 1: deja pasar», «ruido domina → H → 0: corta».

## Narración

<!-- b1 -->
Apliquemos la fórmula al sensor. La temperatura y el ruido no tienen ninguna
relación, así que la densidad cruzada entre i griega y equis es solo la de la
temperatura: el ruido no aporta. Y la densidad de lo medido es la de la
temperatura más la del ruido, porque las potencias de dos señales sin relación
se suman. El filtro queda: la densidad de la señal, entre esa densidad más uno.

<!-- b2 -->
Es una fracción en cada frecuencia: la parte de lo medido que es señal. La
densidad de la temperatura es la del eco del capítulo once: dos coma cinco seis
entre el módulo al cuadrado de uno menos cero coma seis e elevado a menos jota
omega. En omega cero vale dieciséis. En pi medios, uno coma ocho ocho. En pi,
uno. El ruido vale uno en todas.

<!-- b3 -->
Hacemos las cuentas. En frecuencia cero: dieciséis entre diecisiete, cero coma
nueve cuatro. En pi medios: uno coma ocho ocho entre dos coma ocho ocho, cero
coma seis cinco. En pi: uno entre dos, cero coma cinco. Un filtro suave que
deja pasar casi todo en las frecuencias bajas y va cerrándose, sin cortar de
golpe. La temperatura cambia despacio; el ruido, deprisa.

<!-- b4 -->
Lo que hace el filtro es repartir la ganancia según cuánta señal hay en cada
banda. Donde la señal domina, la ganancia se acerca a uno y deja pasar. Donde
manda el ruido, se acerca a cero y corta.

<!-- b5 -->
Fíjate en otra cosa: la ganancia nunca llega a uno. La estimación tiene menos
amplitud que la señal verdadera. No es un error: el estimador siempre tira
hacia la media, como la predicción del capítulo diez, porque cuando duda,
prefiere no arriesgar. Cuanta más información tiene, menos tira.

---

# Escena 12 — ElErrorYLaCoherencia

**Objetivo:** el error del filtro no causal en frecuencia: S_ee = S_yy − |S_yx|²/S_xx
= S_yy (1 − |γ|²), con γ la coherencia. Hacer el desarrollo entero. Es el
σ²(1 − ρ²) del capítulo 8, un rho por frecuencia; como |γ| ≤ 1 (la parábola del
capítulo 11), nunca es negativo. Con el sensor: S_ee = H (porque S_vv = 1): 0,94,
0,65, 0,5 y media 0,686. Interpretación de la coherencia.

**Qué hace falta saber antes:** escenas 10 y 11; capítulo 11 (escenas 30 y 31:
la coherencia y |γ| ≤ 1); capítulo 8 (σ²(1 − ρ²)); conjugado de un número
complejo (se recuerda aquí).

**Visual:**
- «e = y − ŷ» y su densidad. Renglones: «S_ee = S_yy − H S_xy − H* S_yx + |H|²
  S_xx» con cada término coloreado (cómo sale: desarrollar el cuadrado y transformar).
- Se sustituye «H = S_yx / S_xx»: los tres términos con «−|S_yx|²/S_xx», «−|S_yx|²/S_xx»,
  «+|S_yx|²/S_xx». La suma: «= S_yy − |S_yx|²/S_xx».
- «= S_yy (1 − |γ|²)» con «γ = S_yx / √(S_xx S_yy)». Al lado, «σ_y² (1 − ρ²)» del
  capítulo 8 (el mismo dibujo del capítulo 11, escena 31).
- El sensor: la curva S_ee(Ω) (0,94 · 0,65 · 0,5) y su media 0,686 como una
  línea horizontal ámbar. «γ² = 0,94 · 0,65 · 0,5».
- Un cartel: «γ ≈ 1: se estima bien», «γ ≈ 0: el filtro no puede hacer nada».

## Narración

<!-- b1 -->
Ahora, el error: i griega menos su estimación. Desarrollamos el cuadrado como
siempre, con cuatro términos: la densidad de i griega; menos hache por la
cruzada de equis con i griega; menos hache conjugada por la de i griega con
equis; y más el módulo de hache al cuadrado por la densidad de equis.

<!-- b2 -->
Sustituimos hache por su valor: la cruzada entre la densidad de equis. El
segundo término da menos el módulo de la cruzada al cuadrado, entre la
densidad de equis. El tercero, lo mismo. Y el cuarto da más ese mismo cociente.
Dos veces menos y una vez más: queda menos uno. El error es la densidad de i
griega, menos ese cociente.

<!-- b3 -->
Sacamos factor común la densidad de i griega. Queda uno menos el módulo de la
cruzada al cuadrado, entre el producto de las dos densidades. Ese cociente es la
coherencia al cuadrado, el rho de cada frecuencia que vimos en el capítulo
once. El error es la densidad de i griega por uno menos la coherencia al
cuadrado: la varianza por uno menos rho al cuadrado del capítulo ocho, hecho
frecuencia a frecuencia.

<!-- b4 -->
Y como la coherencia nunca pasa de uno, gracias a la parábola de Cauchy-Schwarz
del capítulo once, el error nunca es negativo. Con el sensor, como el ruido vale
uno, el error en cada frecuencia coincide con la ganancia: cero coma nueve
cuatro, cero coma seis cinco y cero coma cinco. El error total es la media de
esa curva sobre todas las frecuencias: cero coma seis ocho seis.

<!-- b5 -->
Donde la coherencia es cercana a uno, la estimación es buena en esa banda;
donde es cercana a cero, el filtro no puede hacer nada. Y ese cero coma seis
ocho seis es lo mejor que puede hacer cualquier filtro lineal con el registro
entero. Compáralo con el cero coma siete tres ocho seis del pasado: mirar el
futuro ayuda, pero menos de lo que parece.

---

# Escena 13 — DeshacerElBorron

**Objetivo:** deconvolución. La señal pasa por un sistema G que la emborrona
(el promediador ½, ½) y se le suma ruido. El filtro inverso 1/G amplifica el
ruido justo donde G es pequeño. Con los números: |G| = 0,99, 0,71, 0,16, 0 en
0,1π, 0,5π, 0,9π, π, así que 1/|G| = 1,01, 1,41, 6,39, ∞. Wiener: H =
(1/G) · S_rr/(S_rr + S_vv), con señal 1 y ruido 0,1: en 0,9π ganancia 1,26 en vez
de 6,39. Primero limpiar, luego invertir.

**Qué hace falta saber antes:** escena 11 (ganancia repartida por banda);
capítulo 10 (escena 25: el promediador ½, ½ y su convolución); número complejo
como flecha con módulo (capítulo 11, escena 29).

**Visual:**
- Cadena: «y[n] → G (promediador) → r[n]; + v[n] → x[n] → H → ŷ[n]»
  (`c12p-deconvolucion.svg`). Una foto movida y un sensor con inercia como
  ejemplos.
- La curva de ganancia del promediador |G(Ω)| = |cos(Ω/2)|: 1 en 0, 0,71 en π/2,
  0,16 en 0,9π, 0 en π.
- El filtro inverso 1/|G| que sube y se sale de la pantalla en π; en 0,9π un
  cartel «× 6,39; potencia del ruido × 41».
- La ganancia de Wiener en ámbar debajo de la del inverso: «= (1/G) × S_rr / (S_rr +
  S_vv)»: el factor 0,20 en 0,9π y 0,91 en 0,1π.
- Dos renglones: «primero: quitar el ruido», «después: deshacer el borroneo».

## Narración

<!-- b1 -->
Otro caso. Ahora la temperatura llega emborronada por un sistema, que llamamos
ge, y encima con ruido. Como una foto movida, o un sensor con inercia. Tomemos
el emborronador más sencillo, el promediador de dos muestras del capítulo
diez: cada medida es la media de la temperatura de ahora y la anterior.

<!-- b2 -->
Su ganancia es uno en las frecuencias lentas, cero coma siete uno en pi
medios, cero coma uno seis en cero coma nueve pi y cero en pi: las altas casi
desaparecen. La idea ingenua para deshacerlo es el inverso, uno entre ge, que
multiplica cada frecuencia por lo contrario.

<!-- b3 -->
Y con ruido, eso es un desastre. En cero coma nueve pi, el inverso
multiplica por seis coma tres nueve; la potencia se multiplica por unos
cuarenta y uno. Pero ahí la señal casi no llegó, así que lo que estamos
multiplicando por seis es el ruido. En pi, donde la ganancia de ge es cero,
habría que multiplicar por infinito.

<!-- b4 -->
El filtro de Wiener sale de la misma fórmula: el inverso, uno entre ge, por un
factor, la potencia de la señal emborronada entre esa potencia más la del
ruido. Con señal uno y ruido cero coma uno: en cero coma nueve pi el factor es
cero coma dos, y la ganancia baja de seis coma tres nueve a uno coma dos seis.
En cero coma uno pi vale cero coma nueve: casi el inverso puro.

<!-- b5 -->
Se lee muy bien: primero limpiar el ruido, con ese factor que se apaga donde la
señal se perdió, y después deshacer el emborronado. Nadie le ha dicho al filtro
dónde parar: cuando la señal desaparece, deja de invertir. Hasta aquí, todo lo
que se podía hacer mirando el registro entero. Falta lo difícil: un filtro que
no puede ver el futuro.

---

# Escena 14 — SoloParaMayorOIgualACero

**Objetivo:** el filtro causal. Solo se puede exigir perpendicularidad con los
datos que se tienen (m ≥ 0), así que h ∗ C_xx = C_yx vale solo para m ≥ 0. Ver
con dos secuencias pequeñas que dos secuencias iguales en media recta no tienen
la misma transformada, y con el sensor que cortar el filtro no causal no da el
óptimo (0,686 frente a 0,7386 en h[0]). Cobrar la promesa de la escena 09.

**Qué hace falta saber antes:** escenas 09 a 11 (no causal, sus coeficientes
h[0] = 0,686; h[±1] = 0,108; h[±2] = 0,017).

**Visual:**
- Un aparato en tiempo real: un reloj y una flecha «el futuro no ha llegado».
  «h[j] = 0 para j < 0».
- «e ⟂ x[n−m]» solo para «m ≥ 0» (las flechas del futuro, tachadas). «h ∗
  C_xx = C_yx, solo para m ≥ 0» con «solo» en rojo.
- Dos secuencias: p (un 1 en m = 0) y q (un 1 en m = 0 y un 3 en m = −1).
  Coinciden para m ≥ 0. Sus transformadas: «P = 1» y «Q = 1 + 3 e^{jΩ}»,
  distintas. Rótulo: «iguales en media recta ≠ misma transformada».
- Para m < 0, el lado izquierdo «(h ∗ C_xx)[m]» con un signo de interrogación
  y el derecho con otro: «no coinciden, y no sabemos cuánto valen».
- Los coeficientes del no causal (simétricos, 0,017 · 0,108 · 0,686 · 0,108 ·
  0,017) y los del causal (0,7386 · 0,1158 · 0,0182): tijera sobre los
  negativos y «no son iguales».

## Narración

<!-- b1 -->
Ahora, lo difícil. Un aparato que filtra en tiempo real no puede usar el
futuro: solo tiene el presente y el pasado. El filtro tiene que ser causal:
hache de jota vale cero para jota negativa. Y entonces la condición cambia:
solo podemos exigir que el error sea perpendicular a las muestras que
tenemos, las de eme mayor o igual que cero.

<!-- b2 -->
La ecuación es la misma, hache convolucionado con la autocorrelación igual a la
correlación cruzada, pero ahora vale solo para eme mayor o igual que cero. Y ese
solo lo estropea todo. Recuerda la escena anterior: transformamos porque la
igualdad valía en todo el eje. Ahora no. Veamos con dos secuencias muy
pequeñas qué se rompe.

<!-- b3 -->
La primera vale uno en cero y nada más. La segunda vale uno en cero y tres en la
posición menos uno. Coinciden para todo eme mayor o igual que cero, pero sus
transformadas son distintas: la primera es uno; la segunda, uno más tres e
elevado a jota omega. Dos secuencias iguales solo en la mitad del eje no tienen,
en general, la misma transformada.

<!-- b4 -->
Además, para eme negativo los dos lados no coinciden, y el izquierdo depende
de un hache que aún no conocemos: no podemos transformar y dividir. ¿Y si
tomamos el filtro no causal del sensor y le cortamos los coeficientes de eme
negativo? Vale cero coma seis ocho seis en el cero y cero coma uno cero ocho a
cada lado. Pero el óptimo causal empieza en cero coma siete tres ocho seis:
distinto.

<!-- b5 -->
Tiene sentido: sin poder ver el futuro, el coeficiente de la muestra de ahora
tiene que trabajar más. Cortar sin más no sirve. Pero hay un caso en el que
cortar sí funciona, y es la clave de todo el episodio. Ese caso ocurre cuando
las mediciones no tienen memoria.

---

# Escena 15 — MedicionesBlancas

**Objetivo:** el caso fácil: si x es blanca, C_xx = σ²δ, la ecuación se
desacopla: σ² h[m] = C_yx[m], para m ≥ 0, y los de m < 0 son simplemente
otras ecuaciones que no molestan. Ejemplo con números inventados: σ² = 2,
C_yx = (1, 2, 1, 0,5) en m = −1, 0, 1, 2; el no causal h = (0,5; 1; 0,5;
0,25) y el causal, cortado, (1; 0,5; 0,25). Regla: se calcula el no causal y se
corta.

**Qué hace falta saber antes:** escena 14; capítulo 10 (moneda: ruido blanco,
sin memoria).

**Visual:**
- La moneda: cada muestra independiente de las otras. C_xx = impulso en 0, con
  σ² = 2.
- La ecuación «Σ h[k] C_xx[m − k] = C_yx[m]» donde de toda la suma solo
  sobrevive un término: «σ² h[m] = C_yx[m]». Una matriz diagonal.
- La tabla: «m: −1, 0, 1, 2», «C_yx: 1, 2, 1, 0,5», «h = C_yx / 2: 0,5, 1, 0,5,
  0,25». Los de m < 0 se apagan con una tijera.
- La idea: cada muestra blanca trae información propia, sin repetir: la suma
  de proyecciones independientes.
- Una regla en ámbar: «no causal → cortar → causal (solo si x es blanca)».
- Una interrogación: «¿y si x no es blanca?».

## Narración

<!-- b1 -->
Si las mediciones son blancas, como la moneda, sin ninguna memoria, no hay
drama. La autocorrelación vale sigma cuadrado en cero y nada en el resto, así
que en la suma de la ecuación solo sobrevive un término: sigma cuadrado por
hache de eme igual a la correlación cruzada en eme. Cada coeficiente se
despeja por separado.

<!-- b2 -->
Con números inventados. Sigma cuadrado vale dos, y la correlación cruzada vale
uno en menos uno, dos en cero, uno en uno y cero coma cinco en dos. Dividimos
entre dos: los coeficientes valen cero coma cinco, uno, cero coma cinco y cero
coma dos cinco. Ese es el filtro no causal, que usa una muestra del futuro, la de
posición menos uno.

<!-- b3 -->
Y el causal: las ecuaciones de eme negativo son otras ecuaciones, para
coeficientes que ahora valen cero, y no molestan a las demás. Los coeficientes
de eme mayor o igual que cero salen igual: uno, cero coma cinco y cero coma
dos cinco. Basta calcular la solución no causal y cortarle la parte no causal.

<!-- b4 -->
¿Por qué se puede cortar? Porque cada muestra blanca trae información propia,
que no repite la de las otras. Cada coeficiente solo escucha a su muestra, y
quitar unas no cambia lo que dicen las demás. Es la suma de varias
proyecciones sobre flechas perpendiculares entre sí: no se estorban.

<!-- b5 -->
El problema es que casi nada es blanco: el sensor tiene memoria, y sus muestras
se parecen unas a otras. Pero la idea da una salida: si lo que medimos no es
blanco, ¿y si lo convertimos en blanco antes de empezar? Eso ya lo sabemos
hacer: es el blanqueador del capítulo once.

---

# Escena 16 — BlanquearPrimero

**Objetivo:** la estrategia del filtro causal: blanquear, resolver el caso
fácil y deshacer el blanqueo. Condición: el blanqueador tiene que ser causal
y su inverso también. Para eso, explicar z⁻¹ (el retardo) y el filtro como
cociente, polos y ceros, por qué un polo dentro del círculo unidad decae, y la
fase mínima con los coeficientes (2, 1) y (1, 2) del capítulo 11. Enunciar la
factorización S_xx = σ² F(z) F(z⁻¹) (el filtro modelador del capítulo 11) y la
idea de que existe si el espectro no se anula en una banda.

**Qué hace falta saber antes:** escena 15; capítulo 11 (escenas 26 a 28:
modelador, blanqueador, fase mínima con las inversas ½, −¼, ⅛ y 1, −2, 4, −8).

**Visual:**
- Tres cajas encadenadas: «x → [blanquear] → ε (blanca) → [resolver el fácil]
  → [deshacer] → ŷ». El nombre «innovación ε».
- «z⁻¹ = retardo de una muestra». El filtro como suma: «F(z) = f₀ + f₁ z⁻¹ +
  f₂ z⁻²…». El eco: «F(z) = 1 / (1 − 0,6 z⁻¹) = 1 + 0,6 z⁻¹ + 0,36 z⁻² + …».
  «polo = 0,6».
- El plano z con el círculo unidad: un polo dentro (× que decae) y uno fuera
  (× que explota: 1, 2, 4, 8…).
- Dos filtros del capítulo 11: «(2 + z⁻¹)/√5» con el cero en −0,5 (dentro) y
  «(1 + 2 z⁻¹)/√5» con el cero en −2 (fuera). Las inversas: barras que se apagan
  y barras que explotan (mismo dibujo). «fase mínima = polos y ceros dentro».
- «S_xx(Ω) = σ² |F(e^{jΩ})|²» = «σ² F(z) F(z⁻¹)». «σ² = 3,8: varianza de la
  moneda».
- Un cartel para la condición: «espectro nulo en una banda → no existe».

## Narración

<!-- b1 -->
La estrategia: blanquear primero. Convertimos lo medido en ruido blanco, con un
filtro. Resolvemos el problema fácil con esa señal blanca. Y deshacemos el
blanqueo. Pero hay una condición, y es lo que hace difícil el asunto: el
blanqueador tiene que ser causal, y su inverso, el que deshace el blanqueo,
también. Si no, mezclaríamos pasado y futuro.

<!-- b2 -->
Un poco de notación. Zeta a la menos uno es un retardo de una muestra, y un
filtro se escribe como suma de retardos con sus coeficientes: hache cero, más
hache uno zeta a la menos uno, y así. El eco del cero coma seis es uno entre
uno menos cero coma seis zeta a la menos uno: uno, más cero coma seis
retardado, más cero coma treinta y seis retardado dos veces, y así. Tiene un
polo en cero coma seis.

<!-- b3 -->
El polo es la base de la caída. Si su módulo es menor que uno, dentro del
círculo unidad, los coeficientes se apagan; si fuera dos, valdrían uno, dos,
cuatro, ocho: explotan. Así se entiende el capítulo once. Dos más zeta a la
menos uno tiene su cero en menos un medio, dentro: su inverso se apaga. Uno
más dos zeta a la menos uno lo tiene fuera: su inverso explota.

<!-- b4 -->
Fase mínima es el filtro con todos sus polos y ceros dentro del círculo: es
causal y estable, y su inverso también. Y aquí aparece la factorización: la
densidad de lo medido es una constante por F de zeta, el filtro de fase
mínima, por F de zeta a la menos uno, el mismo filtro dado la vuelta en el
tiempo. En el círculo es su ganancia al cuadrado: el modelador del capítulo
once.

<!-- b5 -->
Existe siempre que la densidad no se anule en toda una banda: no se puede
blanquear lo que no existe. La señal blanqueada, la que sale de aplicar uno
entre F a lo medido, se llama innovación, épsilon, y es blanca. Nos falta un
último ingrediente: relacionar la señal que buscamos con esa innovación. Y eso
lo hace la fórmula del filtro causal.

---

# Escena 17 — LaFormulaCausal

**Objetivo:** la fórmula H(z) = 1/(σ² F(z)) [S_yx(z)/F(z⁻¹)]₊ en sus tres pasos
(blanquear, quedarse con la parte causal, deshacer). Explicar S_yε = S_yx/F(z⁻¹) (la
cruzada con una señal filtrada se multiplica por el conjugado de su respuesta:
en el círculo, F(z⁻¹) es el conjugado de F) y qué es «la parte causal» (m ≥ 0).
Dos comprobaciones: con x blanca sale el corte de la escena 15, y sin cortar sale
el no causal.

**Qué hace falta saber antes:** escenas 14 a 16; escena 12 (conjugado);
capítulo 11 (densidad cruzada).

**Visual:**
- La fórmula construida por piezas, de derecha a izquierda, con un color por
  paso: «S_yx / F(z⁻¹)» (1, blanquear), «[ · ]₊» (2, parte causal), «1 /
  (σ² F(z))» (3, deshacer). Sello «filtro de Wiener causal».
- La cadena «x → 1/F → ε» y una lupa sobre la correlación cruzada de y con ε:
  «S_yε = S_yx · (1/F)* = S_yx / F(z⁻¹)».
- «[ · ]₊»: una secuencia de dos colas; una tijera que corta la de m < 0 y deja
  m ≥ 0.
- Comprobación 1: «F = 1, σ² → h = C_yx/σ² para m ≥ 0» (escena 15).
- Comprobación 2: «sin [ ]₊: 1/(σ² F) · S_yx / F(z⁻¹) = S_yx / S_xx» (el no
  causal).
- Una flecha hacia la siguiente escena: «con el sensor».

## Narración

<!-- b1 -->
Vamos a construir la fórmula en tres pasos, con la ayuda de la innovación.
Primer paso: blanquear lo medido con uno entre F. Necesitamos saber cómo se
relaciona ahora la señal que buscamos, i griega, con la señal blanqueada. La
regla: la densidad cruzada con una señal filtrada se multiplica por el conjugado
de la respuesta del filtro. Y el conjugado de uno entre F es uno entre F de zeta
a la menos uno.

<!-- b2 -->
La cruzada entre i griega y la innovación vale, entonces, la cruzada entre
i griega y equis, dividida entre F de zeta a la menos uno. Segundo paso: con la
señal blanca aplicamos lo de la escena quince, calcular la solución sin restricción y
cortar la parte de eme negativo. Lo escribimos con un corchete más: la parte
causal, la de las posiciones cero y positivas.

<!-- b3 -->
Tercer paso: deshacer el blanqueo, multiplicando por uno entre F. El filtro
completo es uno entre sigma cuadrado por F de zeta, por la parte causal de la
cruzada dividida entre F de zeta a la menos uno. Se lee de derecha a izquierda:
blanquear, quedarse con lo causal y deshacer. Justo lo que anunciamos.

<!-- b4 -->
Dos comprobaciones. Si lo medido ya fuera blanco, F sería uno, y la fórmula
dice que hache es la cruzada dividida entre sigma cuadrado, cortada: es el caso
de la escena quince. Y si no cortásemos nada, el corchete desaparecería y quedaría
la cruzada entre sigma cuadrado por F por F al revés, que es la densidad de
lo medido: el filtro no causal de siempre.

<!-- b5 -->
La fórmula es el filtro no causal con una diferencia: el corchete. Lo que se
pierde por ser causal está escondido ahí. La parte causal parece un truco, pero
solo se ve al hacer las cuentas. Vamos a hacerlas, con el sensor, de principio a
fin. Es lo que hacemos en el próximo episodio.

---

# Escena 18 — ElModeladorDelSensor

**Objetivo:** factorizar la densidad del sensor medido, a mano. S_xx = S_yy + 1 =
[2,56 + (1,36 − 0,6 (z + z⁻¹))] / (1,36 − 0,6 (z + z⁻¹)) = [3,92 − 0,6 (z + z⁻¹)]
/ (1,36 − 0,6 (z + z⁻¹)). Buscar κ (1 − ρ z⁻¹)(1 − ρ z) igualando: κρ = 0,6 y κ(1 + ρ²)
= 3,92 → ρ² − 6,53 ρ + 1 = 0 → ρ = 0,157 o 6,377 (pares recíprocos; se elige el de
dentro). κ = 3,826. F(z) = (1 − 0,157 z⁻¹)/(1 − 0,6 z⁻¹), σ² = 3,826. Comprobación de
potencia: 3,826 · (1 + 0,443²/0,64) = 5.

**Qué hace falta saber antes:** escenas 11 y 16; ecuación de segundo grado y
producto de raíces (se recuerdan aquí).

**Visual:**
- «S_xx = S_yy + 1 = 2,56 / |1 − 0,6 e^{−jΩ}|² + 1». «|1 − 0,6 e^{−jΩ}|² = 1,36
  − 0,6 (z + z⁻¹)» (desarrollo: 1 + 0,36 − 0,6 (e^{jΩ} + e^{−jΩ})).
- La suma en una sola fracción: numerador «3,92 − 0,6 (z + z⁻¹)».
- «κ (1 − ρ z⁻¹)(1 − ρ z) = κ (1 + ρ²) − κ ρ (z + z⁻¹)»; «κρ = 0,6»,
  «κ (1 + ρ²) = 3,92». La división: «(1 + ρ²)/ρ = 6,53». La ecuación de segundo
  grado.
- Dos raíces sobre el eje real: 0,157 (dentro del círculo) y 6,377 (fuera);
  «producto = 1: vienen en parejas». Se elige la de dentro.
- «F(z) = (1 − 0,157 z⁻¹) / (1 − 0,6 z⁻¹)», con el cero «○ 0,157» y el polo «×
  0,6», los dos dentro. «σ² = 3,826».
- Respuesta al impulso de F: «1, 0,443, 0,266, 0,160…». Comprobación: «3,826 ·
  1,307 = 5».

## Narración

<!-- b1 -->
Factoricemos, a mano, la densidad de lo medido en el sensor: la de la
temperatura, dos coma cinco seis entre el módulo al cuadrado de uno menos cero
coma seis e elevado a menos jota omega, más el uno del ruido. Ese denominador
vale uno coma tres seis menos cero coma seis por zeta más zeta a la menos uno.
Al sumar las fracciones, el numerador queda tres coma nueve dos menos cero
coma seis por esa misma suma.

<!-- b2 -->
Queremos escribir ese numerador como una constante, kappa, por uno menos ro zeta a
la menos uno, por uno menos ro zeta. Al multiplicar, aparece kappa por uno más ro
al cuadrado, menos kappa ro por la suma. Igualamos: kappa por ro vale cero coma seis, y
kappa por uno más ro al cuadrado, tres coma nueve dos.

<!-- b3 -->
Dividimos una entre la otra y desaparece kappa: uno más ro al cuadrado, entre ro,
es seis coma cinco tres. Una ecuación de segundo grado. Tiene dos soluciones: seis
coma tres siete siete y cero coma uno cinco siete. Su producto es uno: vienen siempre
en parejas, una dentro y otra fuera del círculo. Nos quedamos con la de dentro, la
de fase mínima. Kappa vale tres coma ocho dos seis.

<!-- b4 -->
El filtro de fase mínima es F de zeta igual a uno menos cero coma uno cinco
siete zeta a la menos uno, entre uno menos cero coma seis zeta a la menos uno.
Tiene un polo en cero coma seis, la memoria de la temperatura, y un cero en cero
coma uno cinco siete, que pone el ruido. Los dos, dentro. Y sigma cuadrado vale
tres coma ocho dos seis.

<!-- b5 -->
Comprobémoslo con la potencia. La respuesta de F al impulso es uno, cero coma
cuatro cuatro tres, cero coma dos seis seis, y así; la suma de sus cuadrados vale
uno coma tres cero siete. Multiplicada por tres coma ocho dos seis da cinco: justo la
potencia de lo medido, cuatro más uno. Lo medido se comporta como una moneda pasada
por este filtro. Ahora falta la parte causal.

---

# Escena 19 — LaParteCausal

**Objetivo:** aplicar la fórmula al sensor. S_yx/F(z⁻¹) = 2,56 / [(1 − 0,6 z⁻¹)(1
− 0,157 z)]: una secuencia con dos colas, K·0,6^m para m ≥ 0 y K·0,157^{−m}
para m < 0, con K = 2,56/(1 − 0,6 · 0,157) = 2,826 (comprobación en m = 0 con la
progresión geométrica). Cortar m < 0: queda K/(1 − 0,6 z⁻¹). Deshacer: H(z) =
(1/3,826) · [(1 − 0,6 z⁻¹)/(1 − 0,157 z⁻¹)] · 2,826/(1 − 0,6 z⁻¹) =
0,7386/(1 − 0,157 z⁻¹). Coeficientes 0,7386 · 0,1158 · 0,0182 · 0,0028: los de la
escena 05. Pago del bucle.

**Qué hace falta saber antes:** escenas 17 y 18; escena 05 (coeficientes con
cociente 0,157); suma de progresión geométrica (se recuerda aquí).

**Visual:**
- Recuadro con los tres pasos otra vez, uno por color.
- Paso 1: «S_yx = S_yy = 2,56 / [(1 − 0,6 z⁻¹)(1 − 0,6 z)]», se divide entre
  «F(z⁻¹) = (1 − 0,157 z)/(1 − 0,6 z)» → «2,56 / [(1 − 0,6 z⁻¹)(1 − 0,157 z)]».
- Una secuencia con dos colas: a la derecha «K · 0,6^m» (azul), a la izquierda
  «K · 0,157^|m|» (magenta), pico común en m = 0 con «K = 2,826». Cuenta: «2,56 ·
  (1 + 0,094 + 0,094² + …) = 2,56 / 0,906 = 2,826».
- Paso 2: la tijera corta la cola izquierda. Queda «K / (1 − 0,6 z⁻¹)».
- Paso 3: «H = (1 − 0,6 z⁻¹) / (3,826 (1 − 0,157 z⁻¹)) · 2,826 / (1 − 0,6 z⁻¹)»: el
  factor «(1 − 0,6 z⁻¹)» se tacha arriba y abajo. Resultado: «H(z) = 0,7386 / (1 −
  0,157 z⁻¹)».
- Sus coeficientes como barras: «0,7386 · 0,1158 · 0,0182 · 0,0028…», encima
  las de la escena 05, idénticas. «¡0,157!».

## Narración

<!-- b1 -->
Primer paso: la cruzada entre i griega y lo medido es la densidad de la
temperatura, porque el ruido no aporta. Dividida entre F de zeta a la menos
uno, sale dos coma cinco seis entre uno menos cero coma seis zeta a la menos uno, por uno
menos cero coma uno cinco siete zeta. Es un producto de dos fracciones, y en el
tiempo eso es una secuencia con dos colas.

<!-- b2 -->
A la derecha, para eme mayor o igual que cero, cae como cero coma seis elevado a
eme. A la izquierda, cae como cero coma uno cinco siete elevado al valor
absoluto de eme. Y en el centro, el valor común: dos coma cinco seis por la suma de
una progresión geométrica de razón cero coma cero nueve cuatro, es decir, dos coma cinco seis
entre cero coma nueve cero seis: dos coma ocho dos seis.

<!-- b3 -->
Segundo paso: quedarnos con la parte causal. La cola de la izquierda,
la de eme negativo, se corta. Queda la de la derecha, dos coma ocho dos seis por cero
coma seis elevado a eme, que en zeta es dos coma ocho dos seis entre uno menos cero coma seis zeta a
la menos uno.

<!-- b4 -->
Tercer paso: deshacer el blanqueo, multiplicando por uno entre tres coma ocho dos
seis F. Uno menos cero coma seis zeta a la menos uno, arriba, se cancela con el mismo
factor del segundo paso. Queda cero coma siete tres ocho seis entre uno menos cero
coma uno cinco siete zeta a la menos uno. Un filtro de un solo polo.

<!-- b5 -->
Su respuesta al impulso: cero coma siete tres ocho seis; cero coma uno uno cinco
ocho; cero coma cero uno ocho dos; cero coma cero cero dos ocho. ¡Son los
coeficientes de la escena cinco! Cada uno es cero coma uno cinco siete veces el
anterior, y ahora sabemos por qué: es el cero de la factorización. El filtro de
Wiener causal es exactamente el límite del filtro finito.

---

# Escena 20 — ElFiltroPorDentro

**Objetivo:** implementar el filtro: ŷ[n] = 0,157 ŷ[n−1] + 0,7386 x[n] (dos
multiplicaciones para un filtro de infinitos coeficientes). Una iteración a
mano. Su error es 0,7386, el límite del FIR de la escena 05. Por qué el polo del
filtro (0,157) no es el de la señal (0,6): con menos ruido, el polo se acerca a
0 (fiarse del dato de ahora); con más, a 0,6 (fiarse de la memoria).

**Qué hace falta saber antes:** escenas 05 y 19.

**Visual:**
- «H(z) = 0,7386 / (1 − 0,157 z⁻¹)» y su equivalente en el tiempo: «ŷ[n] − 0,157
  ŷ[n−1] = 0,7386 x[n]» → «ŷ[n] = 0,157 ŷ[n−1] + 0,7386 x[n]». Un bloque con
  retroalimentación.
- Una iteración: «ŷ[n−1] = 1; x[n] = 2» → «0,157 · 1 + 0,7386 · 2 = 1,634».
- Una comparación: el FIR de ele muestras (una suma larga de barras) y el
  filtro con retroalimentación (dos números): equivalentes.
- Las barras de error: «0 muestras: 4 → L = 1: 0,8 → L = 2: 0,740 → L = 3: 0,7387 → causal
  de Wiener: 0,7386».
- Dos casos extremos, con el polo del filtro sobre el eje entre 0 y 0,6: «poco
  ruido → polo cerca de 0», «mucho ruido → polo cerca de 0,6».
- La ganancia en continua: «0,7386 / (1 − 0,157) = 0,88», al lado de «0,94 (no
  causal)».

## Narración

<!-- b1 -->
Un filtro con un polo se implementa con muy pocas cuentas. La ecuación que lo
describe es esta: la estimación de ahora es cero coma uno cinco siete por la
estimación anterior, más cero coma siete tres ocho seis por lo que acaba de
llegar. Dos multiplicaciones y una suma, para un filtro con infinitos
coeficientes.

<!-- b2 -->
Probémoslo. Supongamos que la estimación anterior era uno y llega una medición de
dos. La nueva estimación es cero coma uno cinco siete por uno, más cero coma siete
tres ocho seis por dos: uno coma seis tres cuatro. La estimación anterior aporta una
memoria pequeña, y casi todo el peso lo lleva la medición nueva.

<!-- b3 -->
Y el error de este filtro es cero coma siete tres ocho seis: el número al que
convergía el filtro finito. Con tres coeficientes ya estábamos en cero coma siete
tres ocho siete. Es decir, el filtro de Wiener causal no es un filtro distinto al
que resolvíamos con matrices; es aquel, con la ventana llevada hasta el infinito,
y calculado de un golpe.

<!-- b4 -->
Queda una pregunta: ¿por qué el polo del filtro, cero coma uno cinco siete, no
es el de la señal, cero coma seis? Mira los extremos. Con muy poco ruido, el
filtro se fía del dato de ahora y casi no usa el pasado: el polo se acerca a cero.
Con muchísimo ruido, se fía de la memoria de la señal y el polo se acerca a cero
coma seis.

<!-- b5 -->
Una última comprobación: la ganancia en continua del filtro es cero coma ocho
ocho. Menor que la del filtro no causal, cero coma nueve cuatro: sin poder mirar
el futuro, duda más y tira más hacia la media. Ese cero coma siete tres ocho seis
frente a cero coma seis ocho seis del no causal es lo que cuesta no ver el
futuro. Vamos a ponerle precio exacto.

---

# Escena 21 — ElPrecioDeLaCausalidad

**Objetivo:** cuantificar lo que cuesta ser causal. En el dominio de las
innovaciones, el error de cualquier estimador es σ_y² − 2Σ g R + σ² Σ g²; cada
término depende de un solo g[m]; el óptimo es g = R/σ²; el causal no puede usar
m < 0. La diferencia es (1/σ²) Σ_{m<0} R_yε[m]² = la energía de la cola que se
tira (Parseval). Con el sensor: (K²/σ²) · 0,157²/(1 − 0,157²) = 0,0526 = 0,7386 −
0,686. Solo un 7 %.

**Qué hace falta saber antes:** escenas 12, 19 y 20 (0,686; 0,7386; las dos
colas); suma de una progresión geométrica; Parseval (energía en el tiempo = área
en frecuencia, se recuerda aquí).

**Visual:**
- «error de un estimador g sobre la innovación = σ_y² − 2 Σ g[m] R[m] + σ²
  Σ g[m]²». Cada m es un renglón separado (porque ε es blanca).
- El mínimo de cada renglón: una parábola pequeña por cada m, con su vértice
  en «g = R/σ²», contribuyendo «−R²/σ²».
- Error no causal: «σ_y² − (1/σ²) Σ_{todo m} R²». Error causal: «σ_y² −
  (1/σ²) Σ_{m ≥ 0} R²». La diferencia: solo las m < 0, coloreadas.
- La secuencia de dos colas de la escena 19, con la cola izquierda coloreada
  en rojo y una balanza: «energía de lo que se tira».
- La cuenta: «(2,826²/3,826) · (0,157²/(1 − 0,157²)) = 2,087 · 0,0252 = 0,0526»;
  «0,7386 − 0,0526 = 0,686 ✓».
- Una barra: «7 % del error». Frase: «lo que pierdes por ser causal = lo que
  hubieras aprovechado del futuro».
- Un rótulo: «Parseval: energía de la secuencia = área bajo el espectro».

## Narración

<!-- b1 -->
Pongamos precio a la causalidad. Trabajamos con la señal blanqueada, donde todo
es más limpio. El error de un estimador que suma coeficientes por la innovación
es la varianza de la señal, menos dos veces la suma de cada coeficiente por su
correlación, más sigma cuadrado por la suma de los coeficientes al cuadrado.
Como la innovación es blanca, cada posición aporta su propio término, sin
mezclarse con las demás.

<!-- b2 -->
Cada término es una parábola en su coeficiente, y su punto más bajo está en la
correlación dividida entre sigma cuadrado. Ahí aporta menos la correlación al
cuadrado, entre sigma cuadrado. El filtro no causal puede colocar todos los coeficientes en su
punto óptimo. El causal solo puede hacerlo con los de eme mayor o igual que cero:
los de eme negativo tienen que valer cero, y ese término se pierde.

<!-- b3 -->
La diferencia entre los dos errores es, entonces, exactamente la suma de la
correlación al cuadrado, para eme negativo, entre sigma cuadrado. Es la
energía de la cola que hemos cortado. Y por Parseval, esa energía también es
el área de su espectro. Lo que pierdes por ser causal es justo lo que habrías
aprovechado del futuro.

<!-- b4 -->
Con el sensor, la cola de la izquierda cae como cero coma uno cinco siete elevado
a eme. Su energía es dos coma ocho dos seis al cuadrado entre tres coma ocho dos
seis, que es dos coma cero ocho siete, por la suma de los cuadrados de la cola: una
progresión de razón cero coma cero dos cinco que da cero coma cero dos cinco dos.
Resultado: cero coma cero cinco dos seis.

<!-- b5 -->
Cero coma siete tres ocho seis menos cero coma cero cinco dos seis es cero coma
seis ocho seis: justo el error del filtro no causal. Todo encaja. Y la sorpresa: mirar
todo el futuro solo mejora un siete por ciento. ¿Dónde está, entonces, la diferencia
grande? En una decisión mucho más pequeña: usar o no la muestra de ahora.

---

# Escena 22 — LaInnovacion

**Objetivo:** la interpretación por innovaciones, con el eco del 0,6 sin ruido
(el del capítulo 11): x[n] = 0,6 x[n−1] + w[n], con w blanca de varianza 2,56.
Cada muestra nueva trae algo genuinamente nuevo (la moneda w) y algo que ya se
sabía. Con números pequeños: w = 1, 2 → x = 1; 2,6, y de x se recupera w
(x[1] − 0,6 x[0] = 2). Conocer x hasta ahora equivale a conocer w hasta ahora
porque F es de fase mínima; y la parte nueva, blanca, es imposible de
predecir.

**Qué hace falta saber antes:** escenas 16 y 18 (F de fase mínima, blanqueador);
capítulo 11 (escena 26: el eco del 0,6, y 27: el blanqueador x[n] − 0,6 x[n−1]).

**Visual:**
- Una moneda w[n] (varianza 2,56) que entra al bloque del eco y sale x[n].
  «x[n] = 0,6 x[n−1] + w[n]».
- Dos filas con la tabla: «w: 1, 2», «x: 1, 2,6». Una flecha de vuelta:
  «x[1] − 0,6 x[0] = 2,6 − 0,6 = 2 = w[1]». Dos bloques uno inverso del otro.
- «x[n+1] = w[n+1] + 0,6 x[n]»: «lo nuevo» en rojo (impredecible) y «lo que ya sé» en
  verde.
- Un conjunto grande dividido en dos: «x[k], k ≤ n» ↔ «w[k], k ≤ n» con «=».
  Y una versión con un filtro que no es de fase mínima (cero fuera), tachada:
  «la equivalencia se rompe».
- «w[n+1] blanca: no correlacionada con todo lo que sé».

## Narración

<!-- b1 -->
Hay otra forma de entender el filtro causal, con la innovación. Volvamos al eco
del cero coma seis, sin ruido. Cada muestra es cero coma seis por la anterior,
más una moneda nueva, w. Así que la muestra siguiente, equis de ene más uno,
tiene dos partes: cero coma seis por equis de ene, que ya conocemos, y w de ene
más uno, que todavía no ha llegado.

<!-- b2 -->
Veámoslo con números. Si las monedas fueron uno y dos, las muestras son uno, y
cero coma seis por uno más dos: dos coma seis. Al revés: dos coma seis menos cero
coma seis por uno vale dos, la moneda. Es el blanqueador del capítulo once. De
las muestras se recuperan las monedas, y de las monedas, las muestras.

<!-- b3 -->
Es un hecho general, y depende de la fase mínima. Si F es de fase mínima, su
inverso es causal, y conocer las muestras hasta ahora equivale a conocer las
monedas hasta ahora: son la misma información. Con un filtro que no fuese de fase
mínima, el inverso miraría al futuro y esto se rompería.

<!-- b4 -->
Entonces la muestra siguiente es lo que ya sé más lo genuinamente nuevo, w de ene
más uno. Y lo nuevo, por ser blanco, no está correlacionado con nada de lo que
conozco. No hay forma lineal de adivinarlo: por eso se llama innovación. Es
lo que la muestra nueva trae que las anteriores no decían.

<!-- b5 -->
Pausa para pensar: si lo nuevo no se puede adivinar, ¿cuál es la mejor
predicción posible? ¿Y cuánto error queda? La respuesta cabe en una línea, y
además explica de golpe lo que vimos con las ecuaciones de Yule-Walker.

---

# Escena 23 — TirarLoImpredecible

**Objetivo:** el mejor predictor es lo que ya se sabe, tirando la innovación; el
error es la varianza de lo tirado: f₀² σ². Con el eco: predictor 0,6 x[n], error
2,56. En forma de filtro: H = (1/F) [z F]₊; con el eco sale H = 0,6, que es lo
que dieron las ecuaciones de Yule-Walker (escena 06). El filtro modelador de
fase mínima separa lo que ya sé de lo genuinamente nuevo.

**Qué hace falta saber antes:** escenas 06, 17 y 22.

**Visual:**
- «x[n+1] = f₀ w[n+1] + (lo que ya sé)». Una tijera sobre «f₀ w[n+1]». «x̂[n+1]
  = lo que ya sé».
- «error = varianza de lo que se tira = f₀² σ²». Con el eco: «f₀ = 1»,
  «σ² = 2,56», «error = 2,56» (la parábola del capítulo 10, su mínimo).
- El filtro «H = (1/F) [z F]₊» construido en tres piezas, con secuencias:
  «F: 1, 0,6, 0,36, 0,216…»; «z F» = adelantar una muestra: «(1), 0,6, 0,36, 0,216…» con el 1
  saliéndose a la izquierda (m = −1); «[ ]₊» deja «0,6, 0,36, 0,216…» =
  «0,6 / (1 − 0,6 z⁻¹)».
- «H = (1 − 0,6 z⁻¹) · 0,6 / (1 − 0,6 z⁻¹) = 0,6». Un tilde: «el resultado de
  Yule-Walker».
- «F, el filtro modelador: separa lo que ya sabía de lo nuevo».

## Narración

<!-- b1 -->
La mejor predicción es tirar lo que no se puede predecir y quedarnos con lo
demás: la parte que ya sabemos. Y el error es la varianza de lo tirado. Si la
innovación entra multiplicada por efe cero, el error es efe cero al cuadrado por
la varianza de la moneda. Con el eco, efe cero es uno y la moneda tiene varianza
dos coma cinco seis: el error es dos coma cinco seis.

<!-- b2 -->
Es el mismo número que salió de la parábola del capítulo diez, en su punto más
bajo, y el de las ecuaciones de Yule-Walker. No es casualidad: aquellas cuentas
buscaban, con matrices, exactamente lo que aquí se ve de un vistazo. La mejor
predicción de un paso tiene un error igual a la varianza de la innovación, y
ninguna otra puede mejorarlo.

<!-- b3 -->
Escribámoslo como filtro con la fórmula de antes. Blanquear con uno entre F.
Adelantar F una muestra: la respuesta de F al impulso es uno, cero coma seis,
cero coma treinta y seis; adelantada, el uno sale por la izquierda, a la posición
menos uno, y queda cero coma seis, cero coma treinta y seis, y así. Es la parte
que ya se sabe, la causal.

<!-- b4 -->
Esa secuencia es cero coma seis entre uno menos cero coma seis zeta a la menos uno. Y
el filtro es el blanqueador, uno menos cero coma seis zeta a la menos uno,
multiplicado por ella: se cancela todo y queda cero coma seis. Predecir es
multiplicar la última muestra por cero coma seis. Es justo lo que dieron las
ecuaciones de Yule-Walker, en una línea.

<!-- b5 -->
Lo importante no es el caso del eco, sino el reparto: el filtro modelador de
fase mínima separa cada muestra en lo que ya sabía y lo genuinamente nuevo. Pero
el sensor real no es el eco: su medida lleva ruido. Y ahí predecir y filtrar dejan
de ser lo mismo.

---

# Escena 24 — FiltrarNoEsPredecir

**Objetivo:** en el sensor con ruido, predecir y[n] con x[n−1], x[n−2], … no es lo
mismo que filtrar. La cuenta es igual con un retardo de más, y h[0] = 0. Con una
sola muestra x[n−1]: 0,48, error 2,848. Con todo el pasado: H = 0,443 z⁻¹/(1 −
0,157 z⁻¹), error 2,826. Comparado con filtrar (0,7386): casi cuatro veces más.
Por qué: la muestra actual da una mirada directa (ruidosa) a y[n]. Dejar
sembrados el 0,443 y el 0,157 para el episodio 7.

**Qué hace falta saber antes:** escenas 19, 20 y 23; capítulo 10 (escena 22:
predecir a un paso tira hacia la media).

**Visual:**
- Dos ventanas: «filtrar: x[n], x[n−1], …» y «predecir: x[n−1], x[n−2], …» con la
  muestra actual marcada y tachada en la segunda.
- Una muestra sola: «h = C_yx[1] / C_xx[0] = 2,4 / 5 = 0,48», «error = 4 − 2,4 ·
  0,48 = 2,848». Comparar con «filtrar con una muestra: 0,8».
- Todo el pasado: «H_pred(z) = 0,443 z⁻¹ / (1 − 0,157 z⁻¹)», con el z⁻¹ de más y
  «h[0] = 0» resaltado; sus coeficientes «0 · 0,443 · 0,0695 · 0,0109…».
  «error = 2,826».
- Tabla corta: «filtrar 0,7386 · predecir 2,826 (×3,8)».
- Un ojo sobre x[n] mirando a y[n] con el ruido: «una mirada directa, aunque
  ruidosa».
- Dos números en ámbar: «0,443» y «0,157» con «guárdalos».

## Narración

<!-- b1 -->
Ahora predecir en el sensor con ruido: estimar la temperatura de ahora usando solo
las mediciones hasta el instante anterior. No es lo mismo que filtrar, que usa
también la de ahora. La cuenta es igual, pero con un retardo de más: el
coeficiente de la muestra de ahora vale cero, hache de cero igual a cero, y todo
empieza una posición después.

<!-- b2 -->
Con una sola muestra, la anterior. El coeficiente es la correlación cruzada a
un paso, dos coma cuatro, entre la autocorrelación de lo medido, cinco: cero coma cuatro
ocho. Y el error, cuatro menos dos coma cuatro por cero coma cuatro ocho: dos coma
ocho cuatro ocho. Comparado con el cero coma ocho de filtrar con una muestra, es mucho más.

<!-- b3 -->
Con todo el pasado, el resultado es cero coma cuatro cuatro tres, zeta a la
menos uno, entre uno menos cero coma uno cinco siete zeta a la menos uno. Se
parece al filtro, con el mismo polo, pero con ese retardo de más: el primer
coeficiente es cero. Y el error queda en dos coma ocho dos seis. Mirar todo el pasado
mejora muy poco lo que daba una sola muestra: dos coma ocho cuatro ocho.

<!-- b4 -->
Filtrar daba cero coma siete tres ocho seis; predecir, dos coma ocho dos seis:
casi cuatro veces más error. La razón es sencilla. Con la muestra de ahora tienes
una mirada directa, aunque ruidosa, de la temperatura de ahora. Sin ella,
tienes que extrapolar desde el pasado, y la temperatura solo se acuerda un
cero coma seis de lo anterior. Un paso de extrapolación ya cuesta mucho.

<!-- b5 -->
Guarda dos números: cero coma cuatro cuatro tres y cero coma uno cinco siete, los
del predictor. Volverán en el último episodio, en un sitio en el que no los esperas.
Ahora tenemos casi todo para comparar de una vez las tres cosas que hemos aprendido:
predecir, filtrar y suavizar.

---

# Escena 25 — LosTresSabores

**Objetivo:** la tabla comparativa con el sensor: por la media 4; predicción de
un paso 2,826; filtrado 0,7386; suavizado 0,686. Orden siempre: suavizado ≤
filtrado ≤ predicción ≤ varianza. El salto grande está entre predecir y filtrar,
no entre filtrar y suavizar. Cuándo se usa cada uno (tiempo real, post-proceso).
Encuesta al principio.

**Qué hace falta saber antes:** escenas 12, 21 y 24; escena 03 (los tres sabores).

**Visual:**
- Encuesta: «¿qué salto es mayor?»: «(A) de predecir a filtrar (poder usar la
  muestra de ahora)», «(B) de filtrar a suavizar (poder usar el futuro)». Pausa.
- La tabla que se llena fila a fila (`c12p-tres-sabores.svg`): «por la media
  (sin datos): 4», «predicción: 2,826», «filtrado: 0,7386», «suavizado: 0,686»,
  con barras. Flechas entre barras: «−1,17», «−2,09», «−0,05».
- Tres ventanas con sus rótulos: «x[k], k ≤ n − 1», «x[k], k ≤ n», «x[k], todo k».
- «suavizado ≤ filtrado ≤ predicción ≤ Var(y)». Más datos, menos error.
- Iconos: «reloj» (tiempo real → filtrar o predecir) y «cinta de vídeo»
  (grabación → suavizar).
- Porcentajes: «29 %, 82 %, 83 % del error desaparecido».

## Narración

<!-- b1 -->
Una encuesta rápida. Para bajar el error del sensor, ¿qué salto es mayor? La
opción A: poder usar la muestra de ahora, pasar de predecir a filtrar. La opción B:
poder usar además el futuro, pasar de filtrar a suavizar. Piénsalo antes de mirar
los números.

<!-- b2 -->
La tabla. Sin usar ningún dato, el error es la varianza, cuatro. Prediciendo con todo
el pasado, sin la muestra de ahora, dos coma ocho dos seis. Filtrando, cero coma
siete tres ocho seis. Suavizando, con todo el registro, cero coma seis ocho seis. De
cuatro a dos coma ocho: se ha eliminado el veintinueve por ciento del error. Filtrando, el
ochenta y dos. Suavizando, el ochenta y tres.

<!-- b3 -->
Respuesta: la A, y de lejos. Pasar de predecir a filtrar baja el error más de
dos unidades; pasar de filtrar a suavizar, solo cinco centésimas. La muestra
de ahora vale más que todo el futuro junto. Y el orden se cumple siempre: el
suavizado es menor o igual que el filtrado, este que la predicción, y esta que la
varianza. Más datos, menos error.

<!-- b4 -->
Cuál usar depende de cuándo necesitas la respuesta. Si limpias una señal a medida
que llega, en tiempo real, filtras. Si tienes que adelantarte, como un control que
actúa antes de que pase algo, predices. Y si ya tienes la grabación entera y
puedes esperar, suavizas: es lo mejor que se puede hacer.

<!-- b5 -->
Con esto tenemos las tres versiones del filtro y los tres sabores. Pero la
fórmula causal, con sus polos y sus ceros, tiene un parecido raro con otra cosa
que ya conoces: un sistema de control con un observador. Y nos lo van a explicar
en el último episodio.

---

# Escena 26 — ElSensorComoSistema

**Objetivo:** el planteo en espacio de estados: q[n+1] = A q[n] + b w[n], y[n] =
cᵀ q[n], x[n] = y[n] + v[n]. El sensor es de orden 1: A = 0,6, b = c = 1, σ_w² =
2,56, σ_v² = 1. Con G = β/a y r = σ_w²/σ_v² = 2,56, la ecuación α(z)α(z⁻¹) = r
β β* + a a* da el mismo numerador que la escena 18: 3,92 − 0,6 (z + z⁻¹), y α(z) =
z − 0,157. Observador: una copia del modelo que predice y se corrige con la
sorpresa (x − x̂); la ganancia G se elige para que el polo del observador caiga
en 0,157: G = 0,6 − 0,157 = 0,443.

**Qué hace falta saber antes:** escenas 18 y 24; observadores (capítulo 6,
control: un modelo de la planta que se corrige con lo medido; se recuerda aquí).

**Visual:**
- Cajas: «w[n] → planta: q[n+1] = A q[n] + b w[n] → y[n] = cᵀ q[n] → + v[n] →
  x[n]». Un cohete pequeño con «posición y velocidad» (estado de dos números)
  al lado, y el sensor (estado de un número).
- El sensor: «q[n+1] = 0,6 q[n] + w[n]», «y = q», «σ_w² = 2,56», «σ_v² = 1».
- «G(z) = 1 / (z − 0,6) = β / a», «a(z) = z − 0,6», «β = 1», «r = 2,56».
- «α(z)α(z⁻¹) = r β(z)β(z⁻¹) + a(z)a(z⁻¹) = 2,56 + [1,36 − 0,6 (z + z⁻¹)] = 3,92
  − 0,6 (z + z⁻¹)»: el mismo numerador de la escena 18, resaltado. «α(z) = z −
  0,157». «(con un factor de escala: 3,826)».
- El observador: una copia del sistema con «q̂[n+1] = 0,6 q̂[n] + G (x[n] −
  q̂[n])» y la sorpresa «x[n] − q̂[n]» resaltada. Un dial de G: G = 0 (ignora
  las medidas), G = 1 (se fía del dato).
- Pregunta: «¿G para que el polo (0,6 − G) sea 0,157?».

## Narración

<!-- b1 -->
Vamos con la sorpresa que anunciamos al principio. El filtro de Wiener parte de
espectros. La otra forma de ver el mismo problema parte de un modelo de cómo
nace la señal: un sistema en espacio de estados. Un estado es el conjunto de
números que resumen lo que el sistema recuerda: en un cohete, la posición y la
velocidad. En el sensor, solo un número.

<!-- b2 -->
El sensor es el estado q de ene más uno igual a cero coma seis por q de ene, más la
moneda w, de varianza dos coma cinco seis. La temperatura, i griega, es ese estado.
Y lo medido es i griega más el ruido, de varianza uno. Es exactamente el sensor de
siempre: la varianza de la temperatura sigue siendo cuatro. Lo que cambia es la
manera de describirlo.

<!-- b3 -->
En este lenguaje, el numerador de la densidad de lo medido es erre, el
cociente entre la potencia de la moneda y la del ruido, dos coma cinco seis,
más a de zeta por a de zeta a la menos uno, con a de zeta igual a zeta menos
cero coma seis. Da tres coma nueve dos menos cero coma seis por zeta más zeta
a la menos uno: ¡el numerador de la escena dieciocho! Y alfa de zeta vale zeta
menos cero coma uno cinco siete.

<!-- b4 -->
El observador es una copia del modelo dentro del ordenador. Predice con el modelo:
cero coma seis por su estimación de ahora. Y se corrige con la sorpresa: lo que se
mide menos lo que esperaba, multiplicado por una ganancia, ge. Si lo medido coincide
con lo esperado, no hay corrección. Con ge igual a cero, ignora las medidas; con ge
igual a uno, se fía solo del dato.

<!-- b5 -->
¿Qué ganancia elegir? La estimación evoluciona con un polo en cero coma seis menos ge.
Si queremos que caiga justo en el cero coma uno cinco siete de la factorización, ge
tiene que valer cero coma seis menos cero coma uno cinco siete. Haz la cuenta antes de
seguir: cero coma cuatro cuatro tres. ¿Te suena ese número?

---

# Escena 27 — ElObservadorEsElFiltro

**Objetivo:** la estimación del observador con G = 0,443 es q̂[n+1] = 0,157 q̂[n] +
0,443 x[n]: su transferencia 0,443 z⁻¹/(1 − 0,157 z⁻¹) es el predictor de la escena
24. En general: H = (α − a)/α, y con ℓ elegida para que el polinomio característico
sea α, el observador es el Wiener causal (predictor). El filtro (que usa x[n]) es
el paso de corrección: K = 0,7386 = h[0] = 2,826/(2,826 + 1). Tabla Wiener contra
Kalman: mismo resultado, distinto camino; Kalman admite sistemas variantes en el
tiempo, inestables y varias entradas, y sustituye la factorización por la
ecuación de Riccati.

**Qué hace falta saber antes:** escenas 19, 24, 26.

**Visual:**
- «q̂[n+1] = 0,6 q̂ + 0,443 (x − q̂) = 0,157 q̂ + 0,443 x». Su transferencia
  «0,443 z⁻¹ / (1 − 0,157 z⁻¹)» al lado de la del predictor de la escena 24:
  se superponen; los números 0,443 y 0,157 iluminados. «¡son el mismo!».
- General: «H_obs = (α(z) − a(z)) / α(z) = ((z − 0,157) − (z − 0,6)) / (z − 0,157)
  = 0,443 / (z − 0,157)». Dial de la ganancia ℓ y el polo que se mueve.
- El paso de corrección: «q̂[n|n] = q̂[n|n−1] + K (x[n] − q̂[n|n−1])» con K =
  0,7386 = «h[0] de la escena 19». Comprobación: «0,6 (1 − K) = 0,157».
- La fracción: «K = 2,826 / (2,826 + 1) = 0,7386»: barra de error de predicción y
  barra de ruido.
- Tabla de dos columnas: «Wiener: parte de la densidad → factorización → α(z) →
  ganancia» y «Kalman: parte del modelo de estados → el estimador aparece como
  observador». Filas: «estacionario», «variante en el tiempo», «cómo se
  resuelve: factorización / Riccati».
- Un cohete con su estimación de posición y velocidad.

## Narración

<!-- b1 -->
Con esa ganancia, la estimación del observador es cero coma uno cinco siete por su
valor anterior, más cero coma cuatro cuatro tres por lo que llega. Su transferencia
es cero coma cuatro cuatro tres, zeta a la menos uno, entre uno menos cero coma uno
cinco siete zeta a la menos uno. ¡Son los números del predictor de la escena
veinticuatro! El observador y el filtro de Wiener son el mismo filtro.

<!-- b2 -->
No es una casualidad del sensor. En general, con una ganancia elegida para
que el polinomio del observador sea alfa de zeta, la transferencia es alfa menos a,
entre alfa. Con nuestros números, zeta menos cero coma uno cinco siete menos zeta
más cero coma seis: cero coma cuatro cuatro tres. El filtro de Wiener causal se
implementa como un observador. Eso sí: es el predictor, el que no usa la muestra de
ahora.

<!-- b3 -->
Para el filtro, el que sí la usa, añadimos un paso. Primero se predice; después,
se corrige con lo que llega, con una ganancia, k. Esa ganancia vale cero coma
siete tres ocho seis, el primer coeficiente del filtro de la escena diecinueve.
Comprobación: cero coma seis por uno menos k da justo el polo cero coma uno cinco
siete.

<!-- b4 -->
Y tiene una lectura sencilla. El error de la predicción es dos coma ocho dos seis y
el ruido, uno. De la sorpresa que trae cada medición, la parte que viene de la
señal es dos coma ocho dos seis entre tres coma ocho dos seis: cero coma siete tres ocho
seis. Justo la ganancia. Corregimos con más fuerza cuando el ruido molesta menos.

<!-- b5 -->
Este filtro se llama de Kalman. Desde Wiener se llega por la factorización;
Kalman parte del modelo de estados y le sale la forma de observador. Kalman va más
lejos: admite sistemas que cambian con el tiempo, inestables, con varias entradas y
salidas, y en vez de factorizar resuelve la ecuación de Riccati. Es el filtro que
sigue a un cohete. Y es lo que acabamos de hacer con un sensor.

---

# Escena 28 — SinConocerLasCorrelaciones

**Objetivo:** lo que pasa en la práctica: hay un registro y ninguna correlación.
(1) Las correlaciones se estiman y heredan sesgo y varianza del capítulo 11:
N ≫ L. (2) Resolver el sistema: invertir cuesta L³ y puede estar mal
condicionado; Levinson-Durbin, aprovechando Toeplitz, cuesta L², da todos los
órdenes de paso y sus coeficientes de reflexión (entre −1 y 1) son un
control gratis. (3) LMS: bajar rodando por la parábola de la escena 02, con la
pendiente instantánea: h ← h + μ e x. Con μ = 0,1: h = 0 → 0,3 → 0,35. Compromiso
velocidad-precisión.

**Qué hace falta saber antes:** escenas 02, 04 y 05; capítulo 11 (sesgo y
varianza del estimador de la autocorrelación, escenas 16 a 19).

**Visual:**
- Un registro con la etiqueta «solo datos», y «C_xx[m] = ?» estimada: la curva
  ruidosa con sesgo y varianza (el dibujo del capítulo 11).
- «N ≫ L»: un registro largo y una ventana corta.
- Dos contadores: «invertir: L³ (L = 1.000 → mil millones)» y «Levinson: L² (→ un
  millón)», con una escalera que resuelve orden 1, 2, 3… (como la tabla de la
  escena 05). Los coeficientes de reflexión: una barra entre −1 y 1.
- La parábola de la escena 02: «J(h) = 4 − 8h + 5h²». Un punto que baja por ella.
  «pendiente verdadera: −2 E[e x]»; «pendiente de esta muestra: −2 e[n] x[n]».
- Iteraciones: «μ = 0,1; h = 0», «x = 2, y = 1,5 → e = 1,5 → h = 0,3», «x = −1, y =
  −0,8 → e = −0,5 → h = 0,35».
- Dos trayectorias: paso grande (rápido, tembloroso) y paso chico (lento,
  fino).
- Iconos de aplicaciones: cancelación de eco, auriculares con cancelación de ruido.

## Narración

<!-- b1 -->
Todo lo que hemos hecho supone que conocemos las correlaciones. En la práctica
solo tenemos un registro. Hay que estimarlas, con los mismos problemas del capítulo
once: sesgo y varianza, sobre todo en los desfases grandes. El filtro que sale
hereda esos errores. Regla práctica: un registro mucho más largo que la ventana,
al menos diez veces.

<!-- b2 -->
Luego hay que resolver las ecuaciones. Invertir una matriz de ele por ele cuesta
ele al cubo operaciones: con mil coeficientes, mil millones. Y si el proceso está
cerca de ser determinista, la matriz está mal condicionada y se pierde precisión.
Pero es de Toeplitz, y para eso existe el algoritmo de Levinson-Durbin: ele
al cuadrado, un millón, y de paso da la solución de todos los órdenes, como la
tabla de la escena cinco.

<!-- b3 -->
Y hay otra vía que no necesita estimar correlaciones. Recuerda la parábola del
error de la escena dos, cuatro menos ocho hache más cinco hache al cuadrado. El
filtro adaptativo baja rodando por ella: en cada muestra, mueve hache un poco en
contra de la pendiente. La pendiente verdadera es menos dos veces la media del
error por el dato. El truco: usar la de esta sola muestra, sin la media. Es el
algoritmo LMS.

<!-- b4 -->
Con un paso de cero coma uno, empezando en cero. Llega equis igual a dos, y la
temperatura era uno coma cinco: el error es uno coma cinco y hache pasa a cero
coma tres. Llega menos uno, la temperatura era menos cero coma ocho: el error es
menos cero coma cinco y hache sube a cero coma tres cinco. Se acerca al cero
coma ocho que sabemos que es el óptimo.

<!-- b5 -->
El paso marca el compromiso de siempre entre velocidad y precisión: grande, converge
deprisa pero tiembla lejos del óptimo; chico, converge despacio pero fino. Con
esto se cancelan los ecos de una llamada o el ruido en unos auriculares. El
filtro de Wiener es el norte; el LMS es cómo llegar hasta él sin mapa.

---

# Escena 29 — TodoEsUnaProyeccion

**Objetivo:** cierre del capítulo. La geometría de la proyección por tercera
vez (capítulos 7, 8, 12): lo único que cambia es el tamaño del subespacio
(finito, semiinfinito para el causal, infinito para el no causal). Resumen con
el sensor: 4 → 0,8 → 0,7386 (causal) / 0,686 (no causal). El colador de la voz
y el murmullo era H. Tiempo continuo: mismas tres fórmulas. Puente al capítulo
13: blanquear con 1/F y luego lo que ya sabemos (el filtro adaptado). Cierre:
estimar es adivinar lo mejor; detectar es decidir sí o no.

**Qué hace falta saber antes:** todas las escenas; capítulo 7 (escenas 25 a
27, flechas); capítulo 11 (escena 27: blanquear primero).

**Visual:**
- Las flechas del capítulo 7 y del 8, mismo dibujo: y, x₁, x₂ y su proyección con
  el error a 90°. Tres planos cada vez más grandes: «capítulo 7: dos flechas»,
  «capítulo 8: el plano de X₁…X_L», «capítulo 12: el espacio de x[n−k]»:
  finito, semiinfinito (causal), infinito (no causal).
- El sensor, con el recuadro: «sin datos: 4 → una muestra: 0,8 → causal: 0,7386 →
  no causal: 0,686».
- La voz y el murmullo del capítulo 11 con el colador: la curva H(Ω) de la
  escena 11 pasando por el medio.
- Tres fórmulas en tiempo continuo, apareadas con las discretas: «H(jω) =
  S_yx / S_xx», «H = (1/F) [S_yx / F(−jω)]₊», «H(s) = (1/F) [e^{sT} F]₊».
- Un rótulo: «ruido blanco continuo: potencia infinita, una idealización».
- Una cadena: «x → 1/F → señal en ruido blanco → filtro adaptado (capítulo 13)».
- Un radar con un punto: «¿hay un avión? sí / no».

## Narración

<!-- b1 -->
Miremos el capítulo desde arriba. En el siete, las variables eran flechas y la
correlación, el coseno de un ángulo. En el ocho, estimar era proyectar una
flecha sobre el plano de las mediciones, con el error en ángulo recto. Aquí,
lo mismo, con un plano que ha crecido: el de las muestras de la ventana,
finito en el FIR, hacia el pasado en el causal, hacia los dos lados en el no
causal.

<!-- b2 -->
Recuerda el sensor: sin datos, cuatro. Con una muestra, cero coma ocho. Con el
filtro causal, cero coma siete tres ocho seis. Con todo el registro, cero coma
seis ocho seis. Y aquel colador que buscábamos en el capítulo once, para separar
la voz del murmullo, es esta curva: la ganancia que reparte, en cada frecuencia,
cuánto fiarse de lo medido.

<!-- b3 -->
Todo el capítulo se ha hecho en tiempo discreto, pero en tiempo continuo pasa lo
mismo, con demostraciones análogas. No causal: hache es la cruzada entre la
densidad. Causal: uno entre F, por la parte causal de la cruzada entre F de menos jota
omega. Y predecir con antelación te segundos: uno entre F, por la parte causal
de e elevado a ese te por F. La diferencia: el ruido blanco continuo tiene potencia
infinita; es una idealización.

<!-- b4 -->
Y una pieza se ha quedado suelta a propósito: la factorización, con su filtro de
fase mínima y su blanqueador. Volverá. Cuando lo que hay que hacer es detectar
una señal conocida en un ruido con memoria, la estrategia empieza igual: blanquear
con uno entre F y aplicar después lo que ya sabemos sobre ruido blanco.

<!-- b5 -->
Hasta aquí hemos estimado: adivinar lo mejor posible un valor que no vemos
limpio. Pero a veces la pregunta no es cuánto, sino sí o no. ¿Hay un avión en el
radar o solo ruido? Ya no se trata de acertar un valor, sino de decidir, sabiendo
que te puedes equivocar de dos maneras distintas. Eso es detectar, y empieza con
una idea que suena a broma: más datos no bastan.
