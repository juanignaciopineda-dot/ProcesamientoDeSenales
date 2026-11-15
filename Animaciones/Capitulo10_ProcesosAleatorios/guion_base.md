# Capítulo 10 — Procesos aleatorios

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

Guion para las 29 escenas del capítulo.

**Fuentes:**
- `Apuntes/PROCESAMIENTO DE SEÑALES.md`, sección "Procesos Aleatorios"
  (líneas 689–955, sin los Ejercicios Propuestos ni las Actividades).
- `Apuntes/PROCESAMIENTO DE SEÑALES - Cap 10 en profundidad.md`:
  - Parte 1.1: SSS ⇒ WSS y el contraejemplo gaussiana/uniforme.
  - Parte 1.2: la parábola, con los números del sensor.
  - Parte 1.4: la varianza del promedio temporal y las pilas.
  - Parte 2.1: la onda telegráfica, con la verificación numérica.
  - Parte 2.3: el filtrado con números.
  - Parte 3.1: el tamaño de muestra efectivo.
  - Parte 4: las conexiones.
- **Figuras de referencia:** `c10-ensemble.svg`, `c10-estacionariedad.svg`,
  `c10-telegrafica.svg`, `c10p-contraejemplo-sss.svg`,
  `c10p-ergodicidad-varianza.svg`, `c10p-telegrafica-verificada.svg` y
  `c10p-filtrado-numerico.svg`.

**Qué se da por sabido**, recordado en una frase y con el mismo dibujo donde
se usa (README §3, regla 2):
- **Del capítulo 7:**
  - variable aleatoria y su escalera (escenas 09 y 10);
  - densidad y la uniforme (11 y 12);
  - esperanza y su linealidad (13), varianza (14) y grandes números (16);
  - tabla y nube conjuntas (17 y 18);
  - correlación, covarianza y "cero no es nada" (21 a 23);
  - la varianza de una suma con el término de la covarianza (24);
  - las variables como flechas y rho como coseno (25 a 27);
  - la parábola de Cauchy-Schwarz, |ρ| ≤ 1 y su caso de igualdad (28).
- **Del capítulo 8:** la mejor estimación lineal como proyección, con el
  error perpendicular al dato y MMSE = σ²(1 − ρ²), y las ecuaciones normales.
  El capítulo 8 todavía no tiene guion base: aquí se recuerda desde el apunte.
  Si al escribirlo cambia el dibujo de las flechas, hay que ajustar las
  escenas 21, 23 y 24.
- **De Señales y Sistemas:** sistema LTI, respuesta al impulso, convolución,
  transformada de Fourier, ganancia en continua y autocorrelación
  determinista. El capítulo 7 dejó dicho que la convolución y Fourier "se
  vuelven a explicar con calma en los capítulos 10 y 11": la escena 25 lo
  cumple.

**Cómo está escrito** (README §3, "Explicar de forma explícita"):
- Cada concepto sigue el mismo camino: un caso concreto, la cuenta a mano con
  números pequeños, el dibujo, la fórmula leída como resumen y una
  comprobación.
- Las herramientas matemáticas se explican donde aparecen: integral de un
  coseno en un período, producto de cosenos, distribución de Poisson,
  factorial, exponencial, serie geométrica, convolución y Fourier.
- Las deducciones cortas se hacen enteras. De las largas se hace el paso clave
  y se remite al apunte en profundidad.

Castellano de España.

## Reparto en episodios

| Episodio | Escenas | Idea fuerza |
|---|---|---|
| E1 · Mil grabaciones del mismo ruido | 01 SenalesQueNoSeRepiten, 02 NaveDeOsciladores, 03 DosMiradas, 04 FamiliaDeVariables | Un proceso aleatorio es una familia de variables aleatorias, una por cada instante |
| E2 · ¿Qué recuerda una señal? | 05 FuncionMedia, 06 Autocorrelacion, 07 Autocovarianza, 08 PorQueAlcanza | Con la media y la autocorrelación basta, y la autocovarianza es la memoria del proceso |
| E3 · Da igual cuándo mires | 09 Estacionariedad, 10 EstrictaYAmplia, 11 OsciladorConFase, 12 PropiedadesDeR | Si la estadística solo depende de la separación, la autocorrelación es par y tiene su pico en cero |
| E4 · ¿Cuánto tarda el azar en olvidar? | 13 Interruptor, 14 ParOImpar, 15 MemoriaQueSeBorra, 16 UnaSolaGrabacion | La memoria de la onda telegráfica se borra como una exponencial; y una grabación sola, ¿basta? |
| E5 · ¿Basta con una sola grabación? | 17 Pilas, 18 VarianzaDelPromedio, 19 CriterioErgodico, 20 MuestraEfectiva | Promediar en el tiempo funciona si la memoria se borra, pero mil muestras con memoria pueden valer como doscientas cincuenta |
| E6 · Adivinar el futuro, limpiar el presente | 21 Prediccion, 22 HorizonteDePrediccion, 23 FiltroDeUnaMuestra, 24 EcuacionesNormales | Proyectar y dejar el error perpendicular sirve para predecir y para quitar ruido, y solo hacen falta autocorrelaciones |
| E7 · ¿Qué le hace un filtro al ruido? | 25 RepasoConvolucion, 26 MediaDeSalida, 27 CorrelacionDeSalida, 28 VarianzaDeSalida, 29 EnFrecuencia | El azar entra en el filtro, pero su autocorrelación sale calculada de forma determinista |

Narración base por episodio (sin gancho ni cierre): E1 ≈ 1.180 palabras,
E2 ≈ 1.220, E3 ≈ 1.280, E4 ≈ 1.250, E5 ≈ 1.190, E6 ≈ 1.240 y E7 ≈ 1.390 (el
más largo, como el E7 del capítulo 7). Son unos 8–9 min de voz; con gancho y
cierre, ~9–10,5 min.

El gancho y el cierre de cada episodio **no** están aquí: se escriben al armar
el `guion.md` del episodio (README §2, paso 8). Cada cierre anuncia el
episodio siguiente por su título. La última escena de cada episodio ya deja
planteada la pregunta que abre el siguiente.
- El E1 lo anuncia el cierre del último episodio del capítulo 9.
- El cierre de E7 anuncia el E1 del capítulo 11, «¿En qué frecuencias vive el
  azar?», con la escena 29, que deja dicho lo que pide el guion base del
  capítulo 11: que S_yy = |H|² S_xx se parece a la densidad espectral de
  energía.

## Hilos que cruzan el capítulo

Para quien arme cada episodio: estos bucles ya están sembrados en la
narración y hay que respetarlos (y retomarlos en ganchos y cierres).

- **Los ejemplos que vuelven** (mismo dibujo y mismos números siempre):
  - **Los cuatro osciladores desfasados**:
    - amplitud 1, misma frecuencia, fases 0°, 90°, 180° y 270°, cada uno con
      probabilidad ¼;
    - en t = 0 valen 1, 0, −1, 0, y un cuarto de período después, 0, −1, 0, 1;
    - la autocorrelación es ½ en la misma posición, 0 a un cuarto de período
      y −½ a medio período;
    - las parejas de un cuarto de período forman un rombo;
    - aparecen en las escenas 03 a 07, 09, 11, 12 y 16;
    - su variante son los osciladores que arrancan a la vez, con amplitudes
      1 y 3, cuya media es 2cos (escenas 05 y 09).
  - **La moneda ±1**: es el proceso i.i.d. sin memoria.
    - En la escena 02 se presenta.
    - En la 04 se calcula que tres tiradas concretas tienen probabilidad ⅛.
    - En la 07 su autocorrelación es un impulso.
    - En la 09 es estacionaria en sentido estricto.
    - En la 22 tiene horizonte cero.
    - En la 23 es el ruido.
    - En las 27 y 29 entra al promediador y sirve para identificar el sistema.
  - **El sensor de temperatura**: media 20, varianza 4 y la correlación se
    multiplica por 0,6 en cada paso (C = 4, 2,4, 1,44…).
    - Escena 07: se presenta.
    - Escena 09: es WSS.
    - Escena 12: parábola 4 − 4,8λ + 4λ², con mínimo 2,56.
    - Escena 18: varianza del promedio 3,2 con N = 2 y 2,72 con N = 3.
    - Escena 19: 0,725, 0,157 y 0,008.
    - Escena 20: N_eff = 250.
    - Escena 22: predicción 21,8 y 2,56, después 20,65 y 3,81.
    - Escenas 23 y 24: señal del filtro, con h = 0,8 y después 0,74 y 0,12.
    - Escena 26: el promediador le deja la media 20.
  - **El interruptor (onda telegráfica) con λ = 1**:
    - escena 13: la Poisson a medio segundo;
    - escena 14: 0,684 − 0,316 = 0,368 = e⁻¹;
    - escena 15: la exponencial;
    - escena 28: entra al pasabajos y sale con varianza 0,6.
  - **Las pilas**: varianza 4, en las escenas 17 a 20 y 22. El capítulo 11
    las recuerda por ese nombre.
  - **El promediador de dos muestras** (h = ½, ½), en las escenas 25 a 27
    y 29.
- **Los tres tipos de memoria** (escena 07): la moneda no recuerda, el sensor
  olvida poco a poco y los osciladores no olvidan. Vuelven en la escena 15 (el
  interruptor es la versión continua del sensor), en la 17 (la pila
  recuerda más que nadie) y en la 22 (el horizonte de predicción de cada uno).
- **"Correlación cero no es independencia"**: viene del capítulo 7 (escena
  23) y se ve con el rombo de los osciladores (escena 06). Se usa para la
  trampa de "no correlacionados" (escena 08).
- **La promesa de los grandes números** (capítulo 7, escena 16): "promediaremos
  a lo largo de una sola grabación". La plantea la escena 16 (E4) y la pagan
  las escenas 17 a 19 (E5), con el mismo dibujo de las corridas del promedio.
- **La memoria tiene tres caras**:
  - se borra, y por eso promediar funciona (escena 19);
  - mientras dura, cada muestra cuenta menos (escena 20);
  - permite predecir (escena 21).

  Las escenas 20 y 21 van enlazadas por esa frase.
- **La proyección del capítulo 8**: predecir (escena 21) y filtrar (escenas 23
  y 24) son la misma proyección. Hay que usar el mismo dibujo de flechas.
- **"Lo demostraremos en el último episodio"**: la escena 08 promete que los
  momentos de la salida de un LTI salen de los de la entrada, y el E7 lo paga.
  La escena 26 promete que la salida es conjuntamente WSS, y la 27 lo muestra.
- **Puentes a otros capítulos** (Parte 4 del "en profundidad"):
  - **Capítulo 11**:
    - la onda telegráfica reaparece con su "dos lambda" como ancho de banda
      (escena 15). El capítulo 11 llama alfa a ese dos lambda: con λ = 1,
      α = 2;
    - las pilas vuelven como el permiso para estimar espectros;
    - el filtro que le da forma al ruido blanco (escena 29) anuncia el filtro
      modelador.
  - **Capítulo 12**: las ecuaciones normales del FIR (escena 24) son el germen
    del filtro de Wiener.
  - **Capítulo 13**: la autocorrelación determinista R_hh (escena 27) vuelve
    en el filtro adaptado. No se anuncia en la narración.
- **La parábola de Cauchy-Schwarz**: viene del capítulo 7 (escena 28) y
  reaparece en la escena 12 (E3) con los números del sensor.
  - Tiene que ser la misma pieza.
  - Su punto más bajo, 2,56 en λ = 0,6, se paga en la escena 22 (E6): es el
    error de predecir un paso.
  - Las apariciones siguientes son el capítulo 11 (escena 30) y el 13.
  - **Ojo:** la escena 28 del capítulo 7 dice que la parábola «volverá dos
    veces más», y con este capítulo son tres. Hay que cambiar esa frase del
    capítulo 7 (por ejemplo, «volverá varias veces»).
- **Cierre del capítulo**: la escena 29 termina nombrando la densidad espectral
  de potencia → capítulo 11.

## Recortes decididos

- **La serie de la exponencial en la onda telegráfica**: se nombra y se
  comprueba con números, pero no se desarrolla (está en la Parte 2.1).
- **La prueba con épsilon del criterio de ergodicidad**: se da la idea del
  triángulo y los números, y se remite al complemento.
- **Fubini y la estabilidad BIBO**: son "la letra pequeña" de la escena 26.
- **La fórmula del vector gaussiano**: solo se dice que media y covarianza
  determinan el proceso.
- **La deducción completa de R_yy**: se hace el paso de R_yx entero y se dice
  que R_yy sale "repitiendo el mismo paso".
- **Del complemento quedan fuera**:
  - los estimadores sesgado e insesgado de la autocorrelación (Parte 3.2);
  - la simulación de un AR(1) (Parte 3.3): el sensor es un AR(1), pero no se
    nombra;
  - el chequeo de estacionariedad por bloques y la receta práctica
    (Partes 3.4 y 3.5).
- **Se cambian los números de la predicción**: la del complemento (2.2) usa
  otro proceso (media 10, varianza 9, 0,7). Se rehace con el sensor, para no
  sumar un ejemplo nuevo.
- **El ejemplo del FIR con números** (escenas 23 y 24) es propio: el apunte no
  trae números. Sale del sensor más ruido blanco de varianza 1.
- **Lo que no se resuelve**:
  - los Ejercicios Propuestos y las Actividades (10.3 y 10.16);
  - la probabilidad condicional de la telegráfica (ejercicio 1);
  - los ensembles de tres o cuatro funciones de los ejercicios 2 y 3. Los
    cuatro osciladores son un ejemplo propio.

## Pronunciación

Probar de oído antes de sintetizar (README §9). En la narración se dicen los
nombres y en pantalla van las siglas:
- «en sentido estricto» → SSS;
- «en sentido amplio» → WSS;
- «lineal e invariante en el tiempo» → LTI.

A probar:
- **Palabras**: ensemble (¿se oye bien tal cual?), ergódico, Poisson,
  factorial, lag, gaussiano, Wiener, Fourier.
- **Siglas**: i.i.d. (¿lo lee bien o hay que escribir «i, i, de»?), LTI, FIR
  («fir» o «efe, i, erre»).
- **Letras y símbolos**: «tau», «lambda», «theta», «fi», «omega», «omega
  cero», «jota omega», «mu», «rho», «hache», «hache sub ka», «uve», «ka»,
  «ele», «eme», «ene», «erre sub equis equis», «ce sub equis equis», «ese sub
  equis equis», «erre sub hache hache».

## Piezas visuales nuevas

Van a `comun/figuras.py` (sección «capítulo 10, episodio N»):
- **`Realizaciones`** (prevista en README §7): N señales apiladas con semilla
  fija. Incluye:
  - `corte(t)`: línea vertical con los puntos de corte resaltados y sus
    valores;
  - `desplazar_cortes(α)`;
  - `promedio_temporal(i)`: un contador que recorre una realización.
- **Nave de osciladores**: una fila de generadores, cada uno con su seno en
  miniatura. La versión de cuatro, con sus fases escritas (0°, 90°, 180° y
  270°).
- **Tabla de cortes**: una columna por instante, una fila por realización, con
  probabilidades y un renglón de promedio que se llena (para las cuentas a mano
  de las escenas 03 a 07).
- **Rombo**: las cuatro parejas de los osciladores como puntos en el plano.
- **Tira de moneda**: ±1 que aparecen de uno en uno.
- **Curva R(τ)** con un cursor de lag. Arriba, una realización con dos marcas
  separadas τ.
- **Onda telegráfica** con saltos de Poisson (semilla fija), marcas de los
  cambios entre dos instantes y un contador de par/impar.
- **Barras de Poisson**: P(k) para k = 0…4, con λT como parámetro.
- **Matriz de covarianzas** N × N con las diagonales coloreadas, que se
  convierte en el triángulo de pesos.
- **Corridas del promedio**: se reusan las del capítulo 7 (escena 16). Se
  añade una corrida plana que no converge (la pila).
- **Gráfica log-log** de la varianza del promedio contra N (como
  `c10p-ergodicidad-varianza.svg`).
- **Icono `pila`** (en `iconos.py`) y un cajón de pilas.
- **Flechas de la proyección** del capítulo 8, con el error perpendicular (si
  el capítulo 8 aún no la creó).
- **`BloqueLTI`** (previsto): una caja con h y flechas de entrada y salida,
  por la que puede pasar una señal o una curva R(τ).
- **Convolución discreta**: h dada la vuelta que se desliza sobre la entrada,
  con los productos escritos.
- **Solapamiento de h consigo misma**, con el área sombreada (R_hh).
- **`Espectro`** (previsto; también lo usa el capítulo 11): la curva plana de
  la moneda, |H|² del promediador y su producto.

---

# Escena 01 — SenalesQueNoSeRepiten

**Objetivo:** dar el salto de variable aleatoria a proceso aleatorio: una
regla que a cada resultado le asigna una señal entera. Presentar realización,
ensemble y la notación X(t) / X[n].

**Qué hace falta saber antes:** capítulo 7, escena 09 (variable aleatoria como
regla) y escena 03 (el mensaje con ruido); del repaso del capítulo 7, tiempo
continuo y discreto.

**Visual:**
- Un dado que da un número; un bit que se envía y otro que se recibe (el canal
  del capítulo 7, en miniatura).
- Un receptor del que sale una señal larga que se dibuja sola; tres ejemplos:
  ruido de canal, sensor, voz.
- La misma grabación repetida: dos curvas distintas.
- La regla del capítulo 7 (resultados → recta numérica) se transforma:
  resultados → gráficas enteras.
- Muchas curvas apiladas: «ensemble». Una de ellas resaltada: «realización».
- «X(t)» con una curva continua; «X[n]» con puntos.

## Narración

<!-- b1 -->
En el capítulo anterior, todo lo aleatorio eran números. Tiras un dado y
sale un número. Envías un bit y recibes otro. Como mucho, dos variables a la
vez, con su tabla o su nube de puntos. Pero piensa en lo que llega de verdad
a un receptor: no es un número, es una señal que dura segundos, minutos u
horas.

<!-- b2 -->
El ruido de un canal, la tensión que mide un sensor durante una tarde, una
grabación de voz. Cada una es una curva entera, con un valor en cada
instante. Y no sabemos de antemano qué curva nos va a tocar: si grabas el
mismo ruido dos veces, obtienes dos curvas distintas. Necesitamos una forma
de describir el azar de una curva completa.

<!-- b3 -->
Recuerda cómo describíamos el azar de un número. Una variable aleatoria es
una regla: a cada resultado del experimento le pone un número. Si el dado cae
en la cara tres, le pone un tres. Pues un proceso aleatorio es la misma idea
con un paso más: una regla que a cada resultado del experimento le pone una
señal entera.

<!-- b4 -->
Cada una de las señales posibles se llama realización del proceso: es una
grabación concreta, la que ha salido esta vez. Y el conjunto de todas las
realizaciones posibles, cada una con su probabilidad, se llama el ensemble.
Imagínalo como mil grabaciones del mismo fenómeno, dibujadas una encima de
otra.

<!-- b5 -->
Se escribe equis mayúscula de te cuando el tiempo es continuo, y equis
mayúscula de ene, entre corchetes, cuando es discreto: una muestra en cada
instante entero. La mayúscula recuerda lo mismo que en el capítulo anterior:
todavía no ha salido nada. Para verlo con algo concreto, vamos a visitar una
nave llena de osciladores.

---

# Escena 02 — NaveDeOsciladores

**Objetivo:** presentar el ejemplo de los osciladores del apunte. Se elige uno
al azar y la señal que sale es determinista: X(t) = A sin(Φt + Θ). Un trozo
basta para conocer el resto. Contrastarlo con la moneda ±1, donde un trozo no
dice nada. Presentar los dos ejemplos que vuelven.

**Qué hace falta saber antes:** escena 01 (realización, ensemble).

**Visual:**
- Una nave con una fila de generadores, cada uno con su seno en miniatura. Una
  mano elige uno; su seno crece y ocupa la pantalla.
- «X(t) = A sin(Φt + Θ)», con A, Φ y Θ en ámbar.
- Un trozo corto del seno (dos oscilaciones); tres flechas miden amplitud,
  período y fase; el resto se dibuja en punteado.
- Una moneda que gira: «cara → +1», «cruz → −1». Una tira de ±1 que crece; en
  la posición 11, un «?» con «½ | ½».
- Los dos procesos en los extremos de una barra: «un trozo lo dice todo» ↔
  «un trozo no dice nada»; un punto en medio: «las señales reales».

## Narración

<!-- b1 -->
Imagina una nave con cientos de osciladores, cada uno con su propia
amplitud, su propia frecuencia y su propia fase. El experimento consiste en
entrar, elegir uno al azar y conectarlo al osciloscopio. En cuanto lo eliges,
lo que sale es un seno de toda la vida, como los de Señales y Sistemas: sabes
cuánto vale en cada instante.

<!-- b2 -->
Entonces, ¿dónde está el azar? No está en la forma de la señal, que es un seno
perfecto. Está en cuál de todos los senos te ha tocado. Por eso se escribe
así: equis de te es A por el seno de fi por te más theta. La amplitud A, la
frecuencia fi y la fase theta son variables aleatorias. Una vez que salen, la
señal queda fijada para siempre.

<!-- b3 -->
Este proceso tiene una propiedad curiosa. Mira solo un trozo pequeño de la
realización, un par de oscilaciones. Con eso ya puedes medir la amplitud, la
frecuencia y la fase, y sabes qué oscilador es. A partir de ahí puedes dibujar
todo lo que viene después, sin ningún error. Un trozo basta para conocer el
resto.

<!-- b4 -->
Ahora, otro experimento. Una vez por segundo tiras una moneda y anotas más
uno si sale cara y menos uno si sale cruz. La realización es una fila de más
unos y menos unos. Aquí, por muchas tiradas que hayas visto, la siguiente
sigue siendo mitad y mitad. Las diez primeras tiradas no dicen nada de la
undécima.

<!-- b5 -->
Son dos procesos en los extremos: en uno, un trozo lo dice todo; en el otro,
no dice nada. Las señales reales suelen estar en medio: lo que valen ahora
dice algo de lo que valdrán dentro de un momento, pero no todo. Para medir
eso hay que mirar el ensemble de otra manera. Y los osciladores y la moneda
nos van a acompañar todo el capítulo.

---

# Escena 03 — DosMiradas

**Objetivo:** presentar las dos lecturas del ensemble con el ejemplo de los
cuatro osciladores desfasados.
- Si se congela el tiempo, se obtiene una variable aleatoria: con t = 0 salen
  los valores 1, 0, −1 y 0, con probabilidades ¼, ½ y ¼.
- Si se congela el resultado, se obtiene una señal determinista.

**Qué hace falta saber antes:** escena 02 (la nave); capítulo 7, escenas 09 y
10 (variable discreta, su escalera).

**Visual:**
- Cuatro generadores con sus fases escritas: «0°», «90°», «180°», «270°»; cada
  uno con «¼». Sus cuatro cosenos apilados (la pieza `Realizaciones`).
- Una línea vertical en t = 0 baja por las cuatro curvas; en cada cruce
  aparece el valor: «1», «0», «−1», «0».
- Los valores se deslizan a una recta numérica y forman barras: «¼» en 1,
  «½» en 0, «¼» en −1. Rótulo: «X(0)», la escalera del capítulo 7 en pequeño.
- Las demás curvas se apagan; queda solo la de 90°, recorrida por un punto de
  izquierda a derecha: «señal determinista».
- Dos flechas cruzadas: vertical «variable aleatoria», horizontal «señal».

## Narración

<!-- b1 -->
Para hacer cuentas a mano, simplifiquemos la nave. Quedémonos con cuatro
osciladores con la misma amplitud, uno, y la misma frecuencia. Solo cambia la
fase: uno arranca en cero grados, otro en noventa, otro en ciento ochenta y
otro en doscientos setenta. Elegimos uno al azar, así que cada uno tiene
probabilidad un cuarto. Dibujamos las cuatro realizaciones, una encima de
otra.

<!-- b2 -->
Este dibujo se puede leer de dos maneras. La primera: congela el tiempo en
un instante, por ejemplo te igual a cero, y mira hacia abajo, a través de las
cuatro grabaciones. El primer coseno vale uno. El segundo, desfasado noventa
grados, vale cero. El tercero, menos uno. El cuarto, otra vez cero.

<!-- b3 -->
En ese corte vertical hay un número por cada realización, cada uno con su
probabilidad. Uno, con probabilidad un cuarto. Cero, con probabilidad un
medio, porque sale en dos de las cuatro. Menos uno, con probabilidad un
cuarto. Eso es una variable aleatoria discreta: equis de cero. Y todo lo del
capítulo anterior le vale tal cual: su escalera, su media, su varianza.

<!-- b4 -->
La segunda lectura es la contraria: congela el resultado. Quédate con un
solo oscilador, por ejemplo el que arranca en noventa grados, y recórrelo de
izquierda a derecha. Eso no tiene nada de aleatorio: es una señal normal y
corriente, un coseno desplazado. Cada realización, mirada sola, es una señal
determinista.

<!-- b5 -->
Así que un proceso tiene dos caras. En vertical, en cada instante, es una
variable aleatoria. En horizontal, en cada realización, es una señal. Casi
todo lo que viene en este capítulo consiste en pasar de una lectura a la
otra. Pero antes: ¿qué pasa si hacemos más de un corte a la vez?

---

# Escena 04 — FamiliaDeVariables

**Objetivo:** con dos cortes se obtiene una distribución conjunta: las cuatro
parejas de los osciladores, que forman un rombo. Con muchos cortes, el proceso
es una familia de variables indexada por el tiempo. La descripción completa es
inmanejable, salvo en el caso i.i.d. (la moneda: P(+1, +1, −1) = ⅛).

**Qué hace falta saber antes:** escena 03 (corte vertical); capítulo 7,
escenas 17 y 18 (tabla y nube conjuntas) y escena 06 (independencia: regla
del producto).

**Visual:**
- Los cuatro cosenos con dos cortes: t = 0 y un cuarto de período. Una tabla
  de cuatro filas se llena: «(1, 0)», «(0, −1)», «(−1, 0)», «(0, 1)», cada una
  con «¼».
- Las cuatro parejas saltan a un plano: cuatro puntos en rombo.
- Tres, cuatro, muchos cortes: aparece «una familia de variables aleatorias,
  una por instante».
- Una fórmula de densidad conjunta que crece con subíndices hasta salirse de
  la pantalla y se tacha.
- La tira de la moneda: «+1, +1, −1» → «½ · ½ · ½ = ⅛»; se desliza a otras
  tres posiciones y el «⅛» se repite.
- Rótulo «i.i.d.» que se despliega: «independiente e idénticamente
  distribuido».

## Narración

<!-- b1 -->
Hagamos dos cortes: uno en te igual a cero y otro un cuarto de período más
tarde. Cada oscilador da ahora una pareja de números. El que arranca en cero
da uno y cero. El de noventa, cero y menos uno. El de ciento ochenta, menos
uno y cero. Y el de doscientos setenta, cero y uno. Cuatro parejas, cada una
con probabilidad un cuarto.

<!-- b2 -->
Esas parejas son una distribución conjunta, como la tabla de lo enviado y lo
recibido del capítulo anterior. Si las dibujas como puntos en el plano,
forman los cuatro vértices de un rombo. Con dos cortes tienes dos variables
aleatorias con su conjunta. Con tres cortes, tres variables. Con mil cortes,
mil variables, todas repartidas a la vez.

<!-- b3 -->
De ahí sale la forma más útil de pensar un proceso aleatorio: una familia de
variables aleatorias, una por cada instante, con una distribución conjunta. El
tiempo hace de etiqueta: dice de qué variable de la familia hablamos. Y
conocer el proceso del todo significaría conocer la conjunta de cualquier
grupo de instantes, de cualquier tamaño.

<!-- b4 -->
Eso, en general, es imposible de manejar. Pero hay un caso en el que es
fácil: la moneda. Cada tirada es independiente de las demás y siempre tiene
las mismas probabilidades. ¿Qué probabilidad hay de ver más uno, más uno y
menos uno en tres tiradas seguidas? Un medio por un medio por un medio: un
octavo. La conjunta es el producto de las de cada instante.

<!-- b5 -->
A un proceso así se le llama i.i.d.: independiente e idénticamente
distribuido. Es el modelo de ruido más sencillo que existe. Pero las señales
interesantes tienen memoria, y para ellas la conjunta completa es
inmanejable. Hay que resumir, igual que en el capítulo anterior resumimos
una curva entera en su media y su varianza.

---

# Escena 05 — FuncionMedia

**Objetivo:** presentar la función media como la media de cada corte. Con los
cuatro osciladores sale 0 en cualquier instante (se calcula a mano en tres
instantes). Con los osciladores que arrancan a la vez, de amplitudes 1 y 3,
la media es 2cos: sube y baja. Fórmula: μ_X(t) = E[X(t)].

**Qué hace falta saber antes:** escena 03 (el corte en t = 0); capítulo 7,
escena 13 (esperanza como punto de equilibrio y como suma de valor por
probabilidad).

**Visual:**
- Tabla de cortes: columnas «t = 0», «¼ período», «⅛ período»; las cuatro
  filas se llenan y el renglón «promedio» da «0», «0», «0».
- A la derecha, los cuatro cosenos con una línea ámbar plana en cero.
- Cambio de experimento: cuatro cosenos en fase, dos pequeños (amplitud 1) y
  dos grandes (amplitud 3). La tabla da «2», «0», «−2». La línea ámbar se
  dibuja como un coseno de amplitud 2.
- «μ_X(t) = E[X(t)]», construida por piezas.
- Las dos líneas ámbar lado a lado: «plana» | «oscila».

## Narración

<!-- b1 -->
Empecemos por lo más sencillo: la media. En el capítulo anterior, la media
de una variable era su punto de equilibrio. Aquí, en cada instante hay una
variable, así que en cada instante hay una media. Calculémosla con los cuatro
osciladores. En te igual a cero valen uno, cero, menos uno y cero. Su
promedio es cero.

<!-- b2 -->
Probemos un cuarto de período más tarde: cero, menos uno, cero y uno. Otra
vez cero. Y en un instante cualquiera, por ejemplo a un octavo de período,
valen cero coma siete uno, menos cero coma siete uno, menos cero coma siete
uno y cero coma siete uno. De nuevo, cero. En este proceso, la media vale cero
en todos los instantes.

<!-- b3 -->
Pero no tiene por qué ser así. Cambiemos el experimento: los cuatro
osciladores arrancan a la vez, con fase cero, pero dos tienen amplitud uno y
dos tienen amplitud tres. En te igual a cero, la media es dos. Un cuarto de
período después, todos valen cero, y la media es cero. Medio período después,
menos dos. La media sube y baja: es otro coseno, de amplitud dos.

<!-- b4 -->
Así que la media de un proceso es una función del tiempo. Se escribe mu sub
equis de te, y es la esperanza de equis de te. En cada instante se toma la
variable de ese corte y se calcula su media: cada valor por su probabilidad,
todo sumado, o la integral con la densidad si la variable es continua.

<!-- b5 -->
Mírala como una curva que pasa por el centro del ensemble: en cada instante
dice alrededor de qué valor se mueven las grabaciones. En los osciladores
desfasados es plana; en los que arrancan a la vez, oscila. Guarda esta
diferencia, porque va a ser importante. Pero la media no dice nada de la
memoria. Para eso hay que mirar dos instantes a la vez.

---

# Escena 06 — Autocorrelacion

**Objetivo:** presentar la autocorrelación como la esperanza del producto de
dos cortes. Con los cuatro osciladores se calcula a mano: ½ en el mismo
instante, 0 a un cuarto de período y −½ a medio período. Fórmula:
R_XX(t₁, t₂) = E[X(t₁)X(t₂)]. Trampa: correlación cero con dependencia total
(el rombo).

**Qué hace falta saber antes:** escena 05 (media por cortes); escena 04 (el
rombo); capítulo 7, escenas 21 y 23 (correlación como esperanza del producto;
cero no es independencia).

**Visual:**
- La tabla de cortes con dos columnas y una tercera «producto». Tres rondas:
  - (0, 0): productos «1, 0, 1, 0» → «½»;
  - (0, ¼): «0, 0, 0, 0» → «0»;
  - (0, ½): «−1, 0, −1, 0» → «−½».
- Sobre los cosenos, las dos marcas de corte que se separan en cada ronda.
- «R_XX(t₁, t₂) = E[X(t₁) X(t₂)]», construida por piezas; «auto» resaltado.
- «t₁ = t₂ → E[X²] = ½».
- El rombo de la escena 04: «correlación 0». Se ilumina el punto (1, 0): «si
  X(0) = 1 → X(¼) = 0». Sello «dependen».

## Narración

<!-- b1 -->
La pregunta es esta: si sé cuánto vale la señal en un instante, ¿qué me dice
eso de otro instante? En el capítulo anterior, para ver si dos variables se
mueven juntas, multiplicábamos una por la otra y promediábamos: la
correlación, la esperanza del producto. Hagamos lo mismo con dos cortes del
ensemble.

<!-- b2 -->
Primero, los dos cortes en el mismo instante, te igual a cero. Los productos
son uno por uno, cero por cero, menos uno por menos uno y cero por cero: uno,
cero, uno y cero. El promedio es un medio. Ahora, te igual a cero y un cuarto
de período más tarde: uno por cero, cero por menos uno, menos uno por cero y
cero por uno. Todos cero. El promedio es cero.

<!-- b3 -->
Por último, te igual a cero y medio período más tarde. El primer oscilador
pasa de uno a menos uno; el tercero, de menos uno a uno; los otros dos valen
cero. Los productos son menos uno, cero, menos uno y cero, y el promedio es
menos un medio. Medio período después, la señal está al revés de como
estaba.

<!-- b4 -->
Eso es la autocorrelación: erre sub equis equis de te uno, te dos, la
esperanza de equis de te uno por equis de te dos. El prefijo auto dice que
las dos muestras son del mismo proceso. Y cuando los dos instantes coinciden,
es la esperanza del cuadrado, lo que en el capítulo anterior llamábamos
segundo momento: aquí, un medio.

<!-- b5 -->
Ojo con una trampa que ya conoces. Entre cero y un cuarto de período, la
autocorrelación es cero. Y sin embargo, si el primer valor es uno, sabes con
seguridad que el segundo es cero. Los puntos del rombo dependen totalmente
unos de otros, aunque no estén en línea recta. Correlación cero no quiere
decir que no haya relación: quiere decir que no hay relación en línea recta.

---

# Escena 07 — Autocovarianza

**Objetivo:** definir la autocovarianza, C = R − μ(t₁)μ(t₂), con la deducción
del capítulo 7. Calcularla en tres ejemplos que muestran tres memorias:
- la moneda: R = impulso, no recuerda;
- el sensor: media 20, varianza 4 y la correlación se multiplica por 0,6 en
  cada paso, así que olvida poco a poco;
- los osciladores: ½ otra vez al cabo de un período, no olvidan.

**Qué hace falta saber antes:** escena 06 (autocorrelación); capítulo 7,
escena 22 (covarianza y su fórmula práctica) y escena 27 (rho).

**Visual:**
- «C_XX(t₁, t₂) = E[(X(t₁) − μ(t₁))(X(t₂) − μ(t₂))]» → desarrollar → «R_XX −
  μ(t₁)μ(t₂)». Rótulo: «como en el capítulo 7».
- La moneda: cuatro parejas «(+, +) (+, −) (−, +) (−, −)», productos «+1, −1,
  −1, +1» → «0». Una gráfica de barras con un solo palito en cero: «impulso».
- Un termómetro con «20 °C» y una señal que serpentea alrededor.
  «C[0] = 4», «C[1] = 2,4», «C[2] = 1,44»; divididas entre 4: «1», «0,6»,
  «0,36». Flechas «× 0,6».
- Tres gráficas de C contra la separación, lado a lado:
  - la moneda: un palito;
  - el sensor: barras que decaen;
  - los osciladores: un coseno que nunca se apaga.

  Rótulos: «no recuerda», «olvida poco a poco», «no olvida».

## Narración

<!-- b1 -->
Como en el capítulo anterior, hay una versión con las medias restadas. Antes
de multiplicar, a cada muestra se le resta la media de su instante. Eso es la
autocovarianza, ce sub equis equis de te uno, te dos. Y desarrollando el
producto con la linealidad, como hicimos con la covarianza, sale la fórmula
práctica: la autocorrelación menos el producto de las dos medias.

<!-- b2 -->
En los cuatro osciladores la media es cero, así que autocovarianza y
autocorrelación coinciden. Veamos la moneda. Su media también es cero. En el
mismo instante, el producto es siempre uno: vale uno. En dos instantes
distintos hay cuatro parejas igual de probables: más por más, más por menos,
menos por más y menos por menos. Los productos se cancelan: cero.

<!-- b3 -->
La moneda solo se parece a sí misma en el mismo instante: su autocovarianza
es un pico solitario en separación cero, un impulso. Ahora, un tercer
ejemplo que nos va a acompañar: un sensor de temperatura. Media, veinte
grados. Varianza, cuatro. Y con memoria: la covarianza entre dos muestras
seguidas es dos coma cuatro, y con dos pasos de separación, uno coma cuatro
cuatro.

<!-- b4 -->
¿Qué quieren decir esos números? Divide entre la varianza y obtienes el
coeficiente de correlación: cero coma seis entre muestras seguidas, cero coma
tres seis con dos pasos de separación. En cada paso, la correlación se
multiplica por cero coma seis. Si ahora hace calor, dentro de un momento
probablemente también, pero cada vez es menos seguro.

<!-- b5 -->
La autocovarianza es la memoria del proceso, y ya tenemos tres tipos. La
moneda no recuerda nada. El sensor recuerda y va olvidando poco a poco. Y los
osciladores no olvidan nunca: un período entero después, la autocovarianza
vuelve a valer un medio, igual que al principio. Los tres van a volver.

---

# Escena 08 — PorQueAlcanza

**Objetivo:** presentar los momentos cruzados y el significado de "no
correlacionados" (covarianza cero, no independencia). Dar las dos razones por
las que basta con la media y la autocorrelación: procesos gaussianos y
sistemas LTI (se promete la demostración para el último episodio).

**Qué hace falta saber antes:** escenas 06 y 07; capítulo 7, escena 12 (la
gaussiana queda dibujada con μ y σ) y escena 23 (la excepción gaussiana).

**Visual:**
- Dos ensembles lado a lado: lo enviado (`SENAL`, azul) y lo recibido
  (`MEDIDA`, cian), con un corte en cada uno en instantes distintos.
- «R_XY(t₁, t₂) = E[X(t₁) Y(t₂)]» y «C_XY = R_XY − μ_X μ_Y».
- «no correlacionados ⇔ C_XY = 0»; debajo, «≠ independientes», con el rombo
  en miniatura.
- Una balanza: a un lado, una pila de densidades conjuntas; al otro, dos
  piezas pequeñas, «μ(t)» y «R(t₁, t₂)». Un «?».
- Razón 1: la campana del capítulo 7 con «μ» y «σ»; al lado, un ensemble
  gaussiano con «μ(t)» y «C».
- Razón 2: una caja «LTI» con «μ, R» entrando y «μ, R» saliendo. Etiqueta:
  «episodio 7».

## Narración

<!-- b1 -->
Muchas veces hay dos procesos a la vez: lo que se envía y lo que se recibe, o
la voz y el ruido que la tapa. Entre ellos se definen los mismos momentos,
pero cruzados. La correlación cruzada, erre sub equis i griega, es la
esperanza de equis en un instante por i griega en otro. Y la covarianza
cruzada es lo mismo con las medias restadas.

<!-- b2 -->
Si la covarianza cruzada vale cero para cualquier pareja de instantes, se
dice que los dos procesos están no correlacionados. Fíjate en el nombre: se
dice así cuando la covarianza es cero, no la correlación. Y, como acabamos de
ver con el rombo, eso no quiere decir que sean independientes: solo que no
hay relación en línea recta.

<!-- b3 -->
Queda una duda razonable. Hemos cambiado la descripción completa del
proceso, la conjunta de todos los instantes, por dos funciones: la media y la
autocorrelación. ¿No estamos tirando demasiada información? Hay dos razones
por las que no, y conviene tenerlas presentes, porque sostienen todo lo que
queda de asignatura.

<!-- b4 -->
La primera es la gaussiana. En el capítulo anterior vimos que una campana
queda dibujada entera con solo dos números: su media y su varianza. Con los
procesos pasa lo mismo. Si cualquier grupo de muestras es conjuntamente
gaussiano, la media y la autocovarianza determinan el proceso por completo.
No falta nada. Y el ruido de los aparatos suele ser gaussiano.

<!-- b5 -->
La segunda son los filtros. Casi siempre vamos a pasar las señales por
sistemas lineales e invariantes en el tiempo, los que en Señales y Sistemas
llamábamos LTI. Y resulta que la media y la autocorrelación de la salida se
calculan directamente con las de la entrada, sin ninguna densidad. Es el
resultado central del capítulo, y lo demostraremos en el último episodio.

---

# Escena 09 — Estacionariedad

**Objetivo:** presentar las dos versiones de la estacionariedad.
- En sentido estricto: la conjunta no cambia al desplazar los cortes (la
  moneda: ⅛ en cualquier trío).
- En sentido amplio: la media es constante y la autocorrelación depende solo
  del lag τ. Se comprueba a mano con los cuatro osciladores; el sensor
  también lo es; los osciladores que arrancan a la vez, no.

**Qué hace falta saber antes:** escenas 04 a 07 (conjunta, media,
autocorrelación y los tres ejemplos).

**Visual:**
- Dos grabaciones de ruido de habitación con un reloj: «10:00» y «17:00».
  Distintas en el detalle, iguales en la textura.
- `Realizaciones` con tres cortes que se desplazan juntos (flecha «+α»); sus
  densidades no cambian. Rótulo «SSS». La tira de la moneda con «⅛» en dos
  posiciones.
- «WSS»: dos casillas, «μ_X(t) = μ_X» y «R_XX(t₁, t₂) depende solo de
  t₁ − t₂». «τ = t₁ − t₂».
- Tabla de cortes de los osciladores: columnas «¼» y «½», productos «0, 0, 0,
  0» → «0», igual que entre «0» y «¼». Tilde.
- «R_XX(τ)». El sensor con un tilde; los osciladores en fase (media 2cos) con
  una cruz.

## Narración

<!-- b1 -->
Graba el ruido de fondo de una habitación hoy a las diez, y otra vez mañana
a las cinco. Las grabaciones son distintas, pero se parecen mucho: el mismo
murmullo, igual de fuerte, con la misma textura. Su estadística no depende
de la hora a la que las mires. A esa propiedad se le llama estacionariedad, y
viene en dos versiones.

<!-- b2 -->
La versión fuerte es la estacionariedad en sentido estricto. Toma varios
cortes del ensemble y desplázalos todos a la vez, la misma cantidad. Si la
conjunta de esos cortes no cambia, para cualquier grupo de cortes y cualquier
desplazamiento, el proceso es estacionario en sentido estricto. La moneda lo
es: más uno, más uno y menos uno tiene probabilidad un octavo en cualquier
trío de tiradas seguidas.

<!-- b3 -->
La versión débil es la estacionariedad en sentido amplio, y es la que
usaremos casi siempre. Solo pide dos cosas. Primera: que la media sea una
constante, la misma en todos los instantes. Segunda: que la autocorrelación
entre dos instantes dependa solo de la separación entre ellos, y no de dónde
estén. Esa separación se llama retardo, o lag, y se escribe tau.

<!-- b4 -->
Comprobémoslo con los cuatro osciladores desfasados. La media es cero en
todos los instantes: primera condición. La autocorrelación entre cero y un
cuarto de período era cero. Entre un cuarto y medio período, la separación es
la misma, así que debería dar lo mismo. Los valores son cero, menos uno, cero
y uno, y después menos uno, cero, uno y cero. Todos los productos son cero.
Cumplido.

<!-- b5 -->
Cuando se cumplen las dos condiciones, la autocorrelación se escribe con un
solo argumento: erre sub equis equis de tau. El sensor de temperatura
también es estacionario en sentido amplio: su media es veinte siempre, y su
covarianza solo depende de cuántos pasos separan las muestras. En cambio,
los osciladores que arrancan a la vez no lo son: su media sube y baja.

---

# Escena 10 — EstrictaYAmplia

**Objetivo:** demostrar en dos pasos que SSS ⇒ WSS. Mostrar que el recíproco
es falso con el contraejemplo gaussiana/uniforme; la uniforme en ±√3 tiene
varianza 1, y se hace la cuenta. Ver que para procesos gaussianos son lo
mismo.

**Qué hace falta saber antes:** escena 09 (las dos definiciones); capítulo 7,
escena 12 (gaussiana y uniforme) y escena 14 (varianza de la uniforme: el
ancho al cuadrado entre doce).

**Visual:**
- Paso 1: un solo corte que se desplaza; su densidad es la misma → «μ
  constante».
- Paso 2: dos cortes en t₁ y t₂ que se desplazan juntos hasta que el primero
  cae en 0: «(X(0), X(t₂ − t₁))» → «solo depende de t₂ − t₁».
- «SSS ⇒ WSS», con una flecha verde.
- El contraejemplo (como `c10p-contraejemplo-sss.svg`): una tira de muestras,
  campanas en las pares y rectángulos en las impares. La cuenta
  «(2√3)² / 12 = 12 / 12 = 1». Debajo de todas, «μ = 0, σ² = 1».
- Una flecha de desplazamiento de un paso: la campana se convierte en
  rectángulo. «WSS ⇏ SSS», en rojo.
- «gaussiano: WSS ⇔ SSS», con la campana.

## Narración

<!-- b1 -->
¿Cómo se relacionan las dos versiones? La estricta implica la amplia, y se
ve en dos pasos. Primer paso, con un solo corte: la estricta dice que la
densidad de cada instante es la misma que la de cualquier otro. Y si la
densidad es la misma, la media también. La media es constante.

<!-- b2 -->
Segundo paso, con dos cortes, en te uno y en te dos. Desplázalos los dos
hacia atrás, hasta que el primero caiga en cero. La estricta dice que la
conjunta no cambia: es la misma que la de la pareja en cero y en te dos menos
te uno. Solo depende de la separación. Y la autocorrelación, que se calcula
con esa conjunta, también. Las dos condiciones de la amplia se cumplen.

<!-- b3 -->
Al revés no funciona, y hay un contraejemplo muy claro. Toma muestras
independientes, todas con media cero y varianza uno. En los instantes pares,
cada muestra es gaussiana. En los impares, uniforme entre menos raíz de tres
y raíz de tres. ¿Por qué ese intervalo? Porque la varianza de una uniforme es
el ancho al cuadrado entre doce: dos raíz de tres, al cuadrado, es doce; entre
doce, uno.

<!-- b4 -->
La media es cero siempre. La autocorrelación vale uno en el mismo instante y
cero entre instantes distintos, porque son independientes. Así que es
estacionario en sentido amplio. Pero desplaza un solo paso y una campana se
convierte en un rectángulo: en sentido estricto, no lo es. La amplia solo
mira la media y la autocorrelación, y la forma de la densidad le resulta
invisible.

<!-- b5 -->
Hay un caso en el que las dos versiones son exactamente lo mismo: el proceso
gaussiano. Como la media y la autocovarianza lo determinan entero, si esas
dos no cambian al desplazar, no cambia nada. Por eso casi nadie trabaja con
la estricta: con ruido gaussiano, la amplia ya lo dice todo, y es mucho más
fácil de comprobar.

---

# Escena 11 — OsciladorConFase

**Objetivo:** resolver el oscilador del apunte, X(t) = A cos(ω₀t + Θ), con la
fase uniforme en toda la vuelta.
- La media es 0, porque la integral de un coseno en un período es cero.
- La autocorrelación es E[A²]/2 · cos(ω₀τ), con la identidad del producto de
  cosenos, comprobada en α = β = 0.

Comprobar que con A = 1 da lo mismo que las cuentas a mano de la escena 06.
Moraleja: la fase aleatoria borra el origen de tiempos.

**Qué hace falta saber antes:** escenas 05, 06 y 09 (las cuentas a mano, WSS);
capítulo 7, escena 11 (integral = área).

**Visual:**
- La nave con muchos osciladores de la misma frecuencia y fases repartidas
  por toda una vuelta (un círculo de fases). «X(t) = A cos(ω₀t + Θ)», con
  Θ uniforme en [0°, 360°).
- Los cuatro osciladores de antes, resaltados entre todos: «la versión
  pequeña».
- Un coseno sobre una vuelta completa con el área de arriba en verde y la de
  abajo en rojo, del mismo tamaño: «∫ = 0». «μ_X(t) = 0».
- La identidad «cos α cos β = ½ cos(α − β) + ½ cos(α + β)» y su comprobación
  «1 · 1 = ½ + ½».
- El término de la suma se tacha («promedia a 0»); queda «E[A²]/2 ·
  cos(ω₀τ)».
- Con A = 1: «½ cos(ω₀τ)» y la tabla de la escena 06 al lado: «½», «0», «−½»
  coinciden. Sello «WSS».
- Un reloj con un «0» marcado que se borra.

## Narración

<!-- b1 -->
Volvamos a la nave, ahora con infinitos osciladores. Todos tienen la misma
frecuencia, omega cero, y la fase se reparte de manera uniforme por toda la
vuelta, de cero a trescientos sesenta grados. La amplitud también puede ser
aleatoria, siempre que sea independiente de la fase. Los cuatro osciladores
desfasados eran una versión pequeña de esto. ¿Sigue siendo estacionario?

<!-- b2 -->
La media, en un instante cualquiera, es el promedio de los cosenos de todas
las fases posibles. Con cuatro fases sumábamos cuatro valores. Con
infinitas, integramos. Y la integral de un coseno a lo largo de una vuelta
completa es cero: el área que queda por encima del eje es igual a la que
queda por debajo. La media es cero, en todos los instantes.

<!-- b3 -->
Para la autocorrelación hay que multiplicar dos cosenos, y ayuda una
identidad del colegio: el producto de dos cosenos es la mitad del coseno de
la diferencia más la mitad del coseno de la suma. Compruébala con los dos
ángulos a cero: uno por uno es uno, y un medio más un medio también es uno.

<!-- b4 -->
El término de la suma lleva la fase dentro dos veces, así que al promediar
sobre todas las fases vuelve a ser un coseno que recorre vueltas completas:
da cero. El de la diferencia no tiene fase, porque se cancela al restar.
Queda la esperanza de A al cuadrado, dividida entre dos, por el coseno de
omega cero por tau.

<!-- b5 -->
Con amplitud uno, un medio por el coseno: un medio en cero, cero a un cuarto
de período y menos un medio a medio período, lo mismo que calculamos a mano.
Es estacionario en sentido amplio. La moraleja: si todos los osciladores
arrancan a la vez, el reloj tiene un instante especial, el de la salida. La
fase aleatoria lo borra, y sin él, la estadística ya no puede depender de la
hora.

---

# Escena 12 — PropiedadesDeR

**Objetivo:** presentar las dos propiedades de la autocorrelación de un
proceso WSS.
- Es par: se justifica cambiando el orden del producto, y se comprueba con
  los osciladores y con el sensor.
- Su máximo está en el origen: |C(τ)| ≤ C(0). Se demuestra con la parábola
  del capítulo 7, con los números del sensor:
  - g(λ) = 4 − 4,8λ + 4λ²;
  - su discriminante vale −40,96;
  - su mínimo es 2,56 en λ = 0,6. Se guarda para la escena 22.

La igualdad ocurre cuando la señal se repite exactamente, como los
osciladores al cabo de un período.

**Qué hace falta saber antes:** escena 09 (R(τ)); escena 07 (el sensor);
capítulo 7, escena 28 (la parábola de Cauchy-Schwarz y su discriminante).

**Visual:**
- Una realización con dos marcas separadas τ; se intercambian los papeles
  (una flecha que se da la vuelta): «R(−τ) = R(τ)».
- La curva «½ cos(ω₀τ)» y las barras del sensor «0,6^|m|», las dos reflejadas
  en el eje vertical.
- La parábola del capítulo 7 (la misma pieza): «g(λ) = E[(x̃[n] −
  λx̃[n + 1])²] ≥ 0» → «4 − 4,8λ + 4λ²». Se dibuja por encima del eje.
- «b² − 4ac = 23,04 − 64 = −40,96 < 0». El punto más bajo se marca en
  «λ = 0,6», con «2,56» y una etiqueta «volverá».
- «|C(τ)| ≤ C(0)», con recuadro. Las barras del sensor «4, 2,4, 1,44…» bajo
  una línea horizontal en 4.
- Los osciladores: dos marcas separadas un período exacto que caen sobre el
  mismo valor en cada realización. «ρ = 1».
- La curva que cae desde su pico, con la palabra «olvido».

## Narración

<!-- b1 -->
La autocorrelación de un proceso estacionario tiene dos propiedades que se
usan todo el tiempo. La primera es la simetría. Erre de tau compara cada
instante con el que viene tau segundos después. Erre de menos tau, con el de
tau segundos antes. Pero es la misma pareja de instantes vista desde el otro
lado, y el producto no cambia al darle la vuelta.

<!-- b2 -->
Por eso la autocorrelación es par: vale lo mismo en tau que en menos tau, y
su dibujo es simétrico respecto del eje vertical. Con los osciladores, un
medio por el coseno de omega cero tau, y el coseno es par. Con el sensor,
cero coma seis elevado al número de pasos de separación, que se cuenta sin
signo.

<!-- b3 -->
La segunda propiedad: el máximo está en tau igual a cero. Ninguna muestra se
parece tanto a la señal como la propia señal en el mismo instante. Lo
demostramos con el truco de la parábola del capítulo anterior. Con el sensor
centrado, toma la muestra de ahora menos lambda veces la siguiente, y eleva
al cuadrado. Su esperanza nunca es negativa, porque es la de un cuadrado.

<!-- b4 -->
Desarrollada con los números del sensor, es cuatro menos cuatro coma ocho
lambda más cuatro lambda al cuadrado: una parábola. Como nunca baja de cero,
su discriminante no puede ser positivo. Cuatro coma ocho al cuadrado menos
cuatro por cuatro por cuatro: menos cuarenta coma nueve seis. Con letras, lo
mismo da la cota: el valor absoluto de la autocovarianza en tau nunca supera
su valor en cero.

<!-- b5 -->
¿Y si se alcanza el máximo? La parábola toca el cero, y una muestra es
exactamente un múltiplo de la otra, sin nada de azar: es lo que pasa con los
osciladores al cabo de un período. Guarda también el punto más bajo de la
parábola del sensor, dos coma cinco seis, porque volverá. Y en general, la
autocorrelación cae desde su pico. Hay un proceso donde esa caída se ve muy
bien.

---

# Escena 13 — Interruptor

**Objetivo:** presentar la onda telegráfica aleatoria (±1, con cambios de
signo en instantes de Poisson y ritmo λ = 1 por segundo). Explicar la
distribución de Poisson desde cero, con la cuenta a mano para λT = 0,5:
P(0) = 0,61, P(1) = 0,30, P(2) = 0,08 y el resto, algo más del 1 %.

**Qué hace falta saber antes:** escena 12 (la autocorrelación cae desde su
pico); capítulo 7, escena 12 (distribuciones discretas).

**Visual:**
- Un interruptor que una mano acciona en momentos irregulares. La señal ±1 se
  dibuja con saltos (como `c10-telegrafica.svg`).
- Marcas de cambio sobre el eje de tiempos; un contador «λ = 1 cambio/s, de
  media».
- Una ventana de medio segundo que se desliza: a veces 0 cambios, a veces 1,
  a veces 2.
- «P(k) = (λT)^k e^(−λT) / k!», construida por piezas. Al lado, «e ≈ 2,718»,
  «2! = 2», «3! = 6».
- Barras de Poisson que se levantan con sus números: «0,61», «0,30», «0,08»,
  «0,01»… y «Σ = 1».

## Narración

<!-- b1 -->
Imagina un interruptor que alguien acciona en momentos al azar, sin ningún
patrón. La señal vale más uno o menos uno, y cada vez que alguien toca el
interruptor, cambia de signo. Los cambios llegan, de media, una vez por
segundo, y sin ponerse de acuerdo entre ellos. A esta señal se le llama la
onda telegráfica aleatoria.

<!-- b2 -->
Para trabajar con ella hay que saber cuántos cambios caben en un intervalo.
Llamemos lambda al ritmo medio: aquí, un cambio por segundo. En un intervalo
de medio segundo esperamos, de media, lambda por te: medio cambio. Pero a
veces habrá cero cambios, a veces uno, a veces dos. ¿Con qué probabilidad
cada cosa?

<!-- b3 -->
La respuesta es la distribución de Poisson, la de los sucesos que llegan al
azar a un ritmo fijo. La probabilidad de ver ka cambios es lambda te
elevado a ka, por e elevado a menos lambda te, dividido entre ka factorial.
La e es el número dos coma siete uno ocho. Y ka factorial es uno por dos por
tres, así hasta ka: el factorial de dos es dos, y el de tres, seis.

<!-- b4 -->
Hagamos la cuenta con medio segundo. Cero cambios: e elevado a menos cero
coma cinco, que es cero coma seis uno. Un cambio: cero coma cinco por eso,
cero coma tres cero. Dos cambios: cero coma cinco al cuadrado, por cero coma
seis uno, entre dos: cero coma cero ocho. Tres o más: algo más del uno por
ciento. Y todo junto suma uno, como debe ser.

<!-- b5 -->
En medio segundo, lo más probable es que no haya ningún cambio, y dos o más
son raros. Si el intervalo es más largo, las probabilidades se van hacia
muchos cambios. Con esto ya podemos calcular la autocorrelación de la onda:
cuánto se parece la señal a sí misma medio segundo después.

---

# Escena 14 — ParOImpar

**Objetivo:** deducir la autocorrelación de la onda telegráfica. La media es
0, el producto vale ±1 y R = P(par) − P(impar). Cuenta a mano a medio
segundo: 0,684 − 0,316 = 0,368. Resultado general: e^(−2λ|τ|). Comprobación:
e⁻¹ = 0,368. Es WSS.

**Qué hace falta saber antes:** escena 13 (Poisson); escena 06
(autocorrelación como esperanza del producto).

**Visual:**
- Dos instantes separados τ sobre la onda; sus valores, «+1 · +1 = +1» o
  «+1 · −1 = −1».
- Entre los dos instantes, los cambios se cuentan: con 2 cambios, la señal
  vuelve igual (tilde verde); con 1 o 3, sale al revés (cruz roja).
- «R = (+1) · P(par) + (−1) · P(impar)».
- Las barras de Poisson de la escena 13 coloreadas: pares en verde (0, 2, 4),
  impares en rojo (1, 3). «0,684 − 0,316 = 0,368».
- «R_xx(τ) = e^(−2λ|τ|)», construida por piezas. «λ = 1, τ = 0,5 → e⁻¹ ≈
  0,368». Tilde.
- Nota pequeña: «serie completa: apunte en profundidad, Parte 2.1».

## Narración

<!-- b1 -->
Primero, la media. En cualquier instante, más uno y menos uno son igual de
probables, porque los cambios no prefieren ningún signo. La media es cero.
Ahora, la autocorrelación entre dos instantes separados tau. Las dos
muestras valen más uno o menos uno, así que su producto también: más uno si
tienen el mismo signo, y menos uno si tienen signos distintos.

<!-- b2 -->
¿Cuándo tienen el mismo signo? Cada cambio le da la vuelta a la señal. Con un
cambio, está al revés. Con dos, vuelve a estar como al principio. Con tres,
al revés otra vez. Así que las dos muestras coinciden cuando entre ellas ha
habido un número par de cambios, y no coinciden cuando ha habido un número
impar.

<!-- b3 -->
Entonces, la esperanza del producto es más uno por la probabilidad de un
número par de cambios, más menos uno por la probabilidad de un número impar.
A medio segundo, sumando con todos sus decimales, los casos pares dan cero
coma seis ocho cuatro, y los impares, cero coma tres uno seis. La
autocorrelación a medio segundo es la diferencia: cero coma tres seis ocho.

<!-- b4 -->
Si se hace la misma cuenta con un tau cualquiera, aparece una suma de
términos de Poisson con los signos alternados: más, menos, más, menos. Esa
suma alternada es una serie conocida, la de la exponencial, y da e elevado a
menos lambda tau. Multiplicada por el e elevado a menos lambda tau que ya
llevaba cada término, queda e elevado a menos dos lambda por el valor
absoluto de tau.

<!-- b5 -->
Comprobémoslo con medio segundo y lambda igual a uno: e elevado a menos uno,
que es uno entre dos coma siete uno ocho, cero coma tres seis ocho. Lo mismo
que la cuenta a mano. Y la fórmula solo depende de la separación, así que,
con la media constante, la onda es estacionaria en sentido amplio. La serie
completa está en el apunte en profundidad.

---

# Escena 15 — MemoriaQueSeBorra

**Objetivo:** leer e^(−2λ|τ|) como una memoria que se borra, con valores a
mano (1; 0,37; 0,14; 0,02). Comparar interruptores nerviosos y tranquilos:
2λ es la velocidad de olvido. Verla como la versión continua del sensor y
sembrar el capítulo 11 (2λ es un ancho de banda). Abrir la pregunta de la
grabación única.

**Qué hace falta saber antes:** escena 14 (la fórmula); escena 07 (el sensor
y los tres tipos de memoria).

**Visual:**
- La curva «e^(−2|τ|)» de dos lados. Un cursor en τ = 0; 0,5; 1 y 2 deja
  marcas «1», «0,37», «0,14», «0,02». Arriba, dos marcas sobre la onda que se
  separan al mismo ritmo.
- Rótulo sobre la curva: «memoria».
- Tres interruptores: nervioso (λ = 5, curva estrecha, «0,007» a medio
  segundo), el nuestro (λ = 1) y tranquilo (λ = ¼, curva ancha, «0,78»).
  «velocidad de olvido = 2λ».
- Las barras del sensor (× 0,6 por paso) superpuestas a la exponencial.
- Un rótulo pequeño: «2λ → capítulo 11: ancho de banda».
- Para el puente: el ensemble entero se apaga y queda una sola grabación.

## Narración

<!-- b1 -->
Leamos la fórmula. El valor absoluto quita el signo: da igual mirar hacia
delante o hacia atrás. Y una exponencial negativa es una curva que se divide
entre dos coma siete uno ocho cada vez que el exponente avanza una unidad.
Con lambda uno vale uno en cero, cero coma tres siete a medio segundo, cero
coma uno cuatro a un segundo y cero coma cero dos a dos segundos.

<!-- b2 -->
La curva cuenta una historia. Con tau muy pequeño, casi seguro que no ha
habido ningún cambio: la señal se acuerda perfectamente de sí misma. Cuanto
más lejos, más cambios caben entre medias, y el signo de antes dice cada vez
menos del de ahora. La exponencial es la memoria del interruptor,
borrándose. A dos segundos, prácticamente no queda nada.

<!-- b3 -->
¿Y si el interruptor es más nervioso? Con cinco cambios por segundo, la
curva cae cinco veces más deprisa: a medio segundo ya vale siete milésimas.
Con un cambio cada cuatro segundos, a medio segundo todavía vale cero coma
siete ocho. Dos lambda es la velocidad a la que el proceso olvida. Un
interruptor nervioso olvida deprisa; uno tranquilo, despacio.

<!-- b4 -->
Es la versión continua del sensor de temperatura. En el sensor, la
correlación se multiplicaba por cero coma seis en cada paso. Aquí se
multiplica por un mismo factor cada vez que pasa un mismo tiempo. Las dos son
memorias que se borran poco a poco, al contrario que la de los osciladores. Y
ese dos lambda volverá en el capítulo siguiente, disfrazado de ancho de
banda.

<!-- b5 -->
Hasta aquí, todas las cuentas del capítulo han sido promedios sobre el
ensemble: en cada corte, a través de todas las realizaciones. Pero en un
laboratorio nadie tiene mil interruptores ni mil sensores. Tienes un sensor,
una grabación, una tarde de datos. Y la pregunta es inevitable: ¿basta con
eso?

---

# Escena 16 — UnaSolaGrabacion

**Objetivo:** contraponer el promedio vertical (el del ensemble) con el
horizontal (el temporal, con una sola realización). Recordar la promesa del
capítulo 7. Definir la ergodicidad en media, con su límite, y en
correlación. Comprobar a mano que los osciladores son ergódicos en media.

**Qué hace falta saber antes:** escena 03 (las dos lecturas); escena 05
(función media); capítulo 7, escena 16 (grandes números y su promesa).

**Visual:**
- `Realizaciones` con un corte vertical y una flecha «promedio del
  ensemble». Todas se apagan menos una: «lo que tienes». Una flecha
  horizontal la recorre y un contador va acumulando su promedio.
- Las corridas del promedio del capítulo 7 (el mismo dibujo), con la banda
  que se angosta y el eje «n» cambiado por «tiempo».
- «promedio temporal = ¿media del ensemble?».
- «lim_{T→∞} (1/2T) ∫_{−T}^{T} x(t) dt = μ_x», con la ventana [−T, T] que se
  ensancha.
- Un coseno de los osciladores sobre un período con las áreas verde y roja
  iguales: «promedio temporal = 0 = media del ensemble». Tilde.
- «ergódico en correlación»: la señal y su copia retrasada τ, multiplicadas
  y promediadas → «R_xx(τ)».
- Un sello «se suele suponer» y, al final, un «pero…».

## Narración

<!-- b1 -->
La media de un proceso es un promedio vertical: en un instante fijo, a
través de todas las realizaciones. Para calcularla con datos harían falta
miles de grabaciones hechas a la vez. Lo que sí puedes hacer con una sola
grabación es un promedio horizontal: recorrerla a lo largo del tiempo, sumar
sus valores y dividir entre la duración. Es el promedio temporal.

<!-- b2 -->
La pregunta es si los dos promedios coinciden. Ya nos la planteamos con la
ley de los grandes números: el promedio de muchas medidas independientes se
pega a la media, y dijimos que la idea volvería al promediar a lo largo de
una sola grabación. Aquí está. La diferencia es que las muestras de una
grabación no son independientes: tienen memoria.

<!-- b3 -->
Cuando la respuesta es sí, el proceso se llama ergódico. Ergódico en media
quiere decir que el promedio temporal, calculado sobre una ventana cada vez
más larga, se acerca a la media del ensemble. Se escribe como un límite: uno
entre dos te, por la integral de la señal entre menos te y te, cuando te
crece sin fin.

<!-- b4 -->
Probémoslo con los cuatro osciladores. Coge uno cualquiera y promedia a lo
largo del tiempo. En cada período, el coseno pasa el mismo tiempo por encima
del cero que por debajo, y las áreas se cancelan: el promedio temporal es
cero. La media del ensemble también era cero. Coinciden. Y se habla de
ergodicidad en correlación cuando, además, promediar en el tiempo la señal
por su copia retrasada da la autocorrelación.

<!-- b5 -->
Si un proceso es ergódico, una grabación larga vale tanto como el ensemble
entero, y podemos medir su estadística con datos reales. Es tan cómodo que
en la práctica se suele dar por supuesto, salvo que haya pruebas en contra.
Pero no es automático. Hay procesos perfectamente estacionarios en los que
una grabación, por larga que sea, no dice casi nada.

---

# Escena 17 — Pilas

**Objetivo:** el contraejemplo de las pilas: cada realización es una
constante, el proceso es SSS pero no ergódico, y su autocovarianza vale 4
para cualquier separación. Se pregunta con pausa. Separar estacionariedad de
ergodicidad.

**Qué hace falta saber antes:** escena 16 (ergodicidad); escena 09
(estacionariedad); escena 07 (autocovarianza como memoria).

**Visual:**
- Un cajón con pilas (icono `pila`), cada una con su voltaje escrito
  respecto del nominal: «+1», «−2», «+2», «0»… Una sale al azar y un
  voltímetro dibuja una recta horizontal.
- `Realizaciones` de rectas a alturas distintas; un corte vertical da su
  densidad: «μ = 0», «σ² = 4».
- Dos preguntas en pantalla con casillas vacías: «¿estacionario?» y
  «¿ergódico?». Pausa. Se marcan: «sí» y «no».
- El promedio temporal de la pila «+2»: el contador se queda clavado en 2.
  La media del cajón, «0», en otra altura, inalcanzable.
- «C(τ) = 4» para todo τ: una recta horizontal donde antes caía la
  exponencial.
- El ensemble como franjas: cada realización encerrada en la suya.

## Narración

<!-- b1 -->
Un cajón lleno de pilas, cada una con un voltaje un poco distinto. El
experimento: sacas una al azar y mides su voltaje durante una hora. La
grabación es una línea recta, porque el voltaje de esa pila no cambia.
Cada realización es una constante, y cada pila da una constante
diferente. Supón que los voltajes, medidos respecto del nominal, tienen media
cero y varianza cuatro.

<!-- b2 -->
Antes de seguir, dos preguntas: ¿este proceso es estacionario? ¿Y es
ergódico? Piénsalo un momento. Estacionario lo es, y en el sentido más
fuerte: la estadística no cambia nunca, porque nada cambia nunca. Da igual
cuándo hagas el corte: la densidad de los voltajes es siempre la misma.

<!-- b3 -->
Ahora promedia tu grabación a lo largo del tiempo. Da el voltaje de tu
pila, sea el que sea. Si te tocó una de dos voltios por encima, el
promedio temporal es dos, por mucho que alargues la medida. Nunca se acerca a
cero, la media del cajón. No es ergódico: una sola pila no te enseña nada
de las demás.

<!-- b4 -->
La autocovarianza lo explica. La muestra de ahora y la de dentro de una hora
son el mismo número, así que su covarianza es la varianza: cuatro. Y eso vale
para cualquier separación: cuatro a un segundo, cuatro a un año. Los
osciladores tampoco olvidaban, pero al menos cada uno recorría todos sus
valores en cada período. Cada pila se queda quieta en el suyo.

<!-- b5 -->
Así que estacionario y ergódico son cosas distintas. Estacionario dice que la
estadística no cambia con el tiempo. Ergódico dice que una sola realización
recorre todo lo que el ensemble puede hacer. La pila es estacionaria, pero
cada realización se queda encerrada en su valor. ¿Qué tiene que pasar para
que el promedio temporal sí funcione?

---

# Escena 18 — VarianzaDelPromedio

**Objetivo:** calcular a mano la varianza del promedio de N muestras con
memoria, con la fórmula de la varianza de una suma del capítulo 7.
- N = 2: el sensor da 3,2 (con muestras independientes serían 2) y la pila
  da 4.
- N = 3: el sensor da 2,72, contando las parejas en una tabla de 3 × 3.

Descubrir el triángulo de pesos y enunciar la fórmula general.

**Qué hace falta saber antes:** escena 07 (el sensor: 4, 2,4, 1,44); escena
17 (la pila); capítulo 7, escena 24 (varianza de una suma con el término
de la covarianza) y escena 16 (dividir entre n divide la varianza entre n²).

**Visual:**
- «Var((x₁ + x₂)/2) = (σ² + σ² + 2C[1]) / 4», construida por piezas.
- Tres columnas que se llenan:
  - sensor: «(4 + 4 + 4,8)/4 = 3,2»;
  - independientes: «(4 + 4 + 0)/4 = 2»;
  - pila: «(4 + 4 + 8)/4 = 4».
- Una tabla de 3 × 3 de covarianzas: la diagonal «4, 4, 4» en ámbar, las
  vecinas «2,4» en cian y las esquinas «1,44» en magenta. «(12 + 9,6 +
  2,88)/9 = 2,72».
- Las diagonales se deslizan hacia abajo y forman barras de alturas 1, 2, 3,
  2, 1: un triángulo.
- La fórmula general, «Var = (1/N²) Σ (N − |k|) C[k]», y su versión continua
  con la integral, más pequeña.

## Narración

<!-- b1 -->
Para responder, midamos cuánto se dispersa el promedio temporal, empezando
por lo más pequeño: el promedio de dos muestras seguidas. En el capítulo
anterior vimos la varianza de una suma: la varianza de la primera, más la de
la segunda, más dos veces su covarianza. Y al dividir entre dos, la varianza
se divide entre cuatro.

<!-- b2 -->
Con el sensor: cuatro más cuatro más dos por dos coma cuatro da doce coma
ocho; entre cuatro, tres coma dos. Si las muestras fueran independientes, la
covarianza sería cero y quedaría dos. Y con la pila, la covarianza es
cuatro: cuatro más cuatro más ocho, dieciséis; entre cuatro, cuatro.
Promediar dos muestras de una pila no sirve de nada.

<!-- b3 -->
Con tres muestras se ve el patrón. Hay que sumar las covarianzas de todas las
parejas, que caben en una tabla de tres por tres. En la diagonal hay tres
varianzas: tres por cuatro. Junto a la diagonal, cuatro parejas a un paso:
cuatro por dos coma cuatro. En las esquinas, dos parejas a dos pasos: dos por
uno coma cuatro cuatro. En total, veinticuatro coma cuatro ocho; entre nueve,
dos coma siete dos.

<!-- b4 -->
Fíjate en cuántas parejas hay de cada separación. Tres a separación cero.
Dos a un paso, a cada lado. Una a dos pasos, a cada lado. Uno, dos, tres,
dos, uno: un triángulo. Con ene muestras pasa lo mismo. La varianza del
promedio es la suma de la autocovarianza en cada separación, pesada por ese
triángulo, y dividida entre ene al cuadrado.

<!-- b5 -->
Para el tiempo continuo es lo mismo, con una integral en lugar de la suma. Y
ahora se ve qué lo decide todo. Si la autocovarianza se queda grande en todas
las separaciones, como en la pila, el triángulo entero pesa y la varianza
no baja. Pero si la autocovarianza se va apagando con la separación, la cosa
cambia.

---

# Escena 19 — CriterioErgodico

**Objetivo:** enunciar el criterio: si el proceso es WSS con varianza finita
y C(τ) → 0, es ergódico en media. Dar la idea (la zona grande se diluye) y
verlo con números: el sensor da 0,725, 0,157, 0,032 y 0,008, contra 4 de la
pila; Monte Carlo cae encima. Terminar con la sorpresa: con veinte
muestras, 0,725 frente a 0,2 si fueran independientes.

**Qué hace falta saber antes:** escena 18 (el triángulo y la fórmula); escena
17 (la pila).

**Visual:**
- «WSS + varianza finita + C(τ) → 0 ⇒ ergódico en media», construida por
  piezas.
- El triángulo de pesos que se estira con N mientras C solo es alta cerca del
  cero: la zona sombreada se hace una fracción cada vez menor.
- Tabla que se llena: N = 20, 100, 500, 2.000 → «0,725», «0,157», «0,032»,
  «0,008» | pila «4», «4», «4», «4».
- Gráfica log-log (como `c10p-ergodicidad-varianza.svg`): la curva del sensor
  que baja, los puntos de Monte Carlo encima y la recta plana de la pila.
- Una grabación larga partida en trozos de colores: «trozos casi
  independientes».
- «20 independientes: 4/20 = 0,2» frente a «20 del sensor: 0,725». Un «¿?».

## Narración

<!-- b1 -->
El criterio es este: un proceso estacionario en sentido amplio, con varianza
finita, cuya autocovarianza tiende a cero cuando la separación crece, es
ergódico en media. La idea: al alargar la ventana, el triángulo se estira,
pero la autocovarianza solo es grande cerca del cero. Esa zona pesa cada vez
menos frente al total, y la varianza del promedio se va a cero.

<!-- b2 -->
Con el sensor. Con veinte muestras, la varianza del promedio es cero coma
siete dos. Con cien, cero coma uno seis. Con quinientas, cero coma cero tres.
Con dos mil, menos de una centésima. Y la pila, en todos los casos,
cuatro. Una baja sin parar; la otra no se mueve.

<!-- b3 -->
No son solo cuentas. Si se simulan miles de sensores y se mide de verdad
cuánto se dispersan sus promedios, los puntos caen exactamente sobre la
fórmula. El promedio temporal de una grabación larga del sensor se pega a la
media del ensemble. El sensor es ergódico; la pila, no. Y la diferencia
está en la memoria: una se borra y la otra no.

<!-- b4 -->
La cuenta completa, con el límite hecho con cuidado, está en el apunte en
profundidad. Pero la intuición es sencilla. Si las muestras muy separadas se
olvidan unas de otras, una grabación larga contiene muchos trozos que se
comportan casi como realizaciones independientes. Promediar en el tiempo es,
en el fondo, promediar muchas realizaciones disfrazadas de una sola.

<!-- b5 -->
Y aquí hay una sorpresa. Con veinte muestras independientes de varianza
cuatro, la varianza del promedio sería cuatro entre veinte: cero coma dos.
Con el sensor es cero coma siete dos, más de tres veces más. Promediar
funciona, pero más despacio. Veinte muestras con memoria no valen lo que
veinte independientes. ¿Cuánto valen, entonces?

---

# Escena 20 — MuestraEfectiva

**Objetivo:** presentar el tamaño de muestra efectivo con una pregunta con
pausa y tres opciones. Sumar a mano los coeficientes de correlación del
sensor: 1 + 2 · (0,6 + 0,36 + 0,216 + …) = 1 + 2 · 1,5 = 4, así que
N_eff = N/4 y mil muestras valen como doscientas cincuenta. Con 0,9 por paso,
la suma da 19. Lección práctica y las tres caras de la memoria.

**Qué hace falta saber antes:** escenas 18 y 19 (varianza del promedio y la
sorpresa); escena 07 (los coeficientes del sensor).

**Visual:**
- «1.000 muestras del sensor ≈ ¿? independientes». Tres opciones: «1.000»,
  «500», «250». Pausa; se tachan las dos primeras.
- «Var ≈ (σ²/N) · Σ ρ[k]».
- Barras de ρ[k] a los dos lados del cero: «1» en el centro; «0,6», «0,36»,
  «0,216»… a cada lado. Un contador de la suma del lado derecho: «0,6»,
  «0,96», «1,18», «1,3» → «1,5». Los dos lados: «3»; con el centro: «4».
- «N_eff = N / Σ ρ[k] = 1.000 / 4 = 250». Una fila de mil puntos que se
  agrupan de cuatro en cuatro.
- «ρ = 0,9 por paso → Σ = 19».
- Una etiqueta «error ± σ/√N» tachada, con «σ/√N_eff» al lado.
- Tres caras de la memoria en tres tarjetas: «se borra → promediar funciona»,
  «dura → cada muestra cuenta menos» y una tercera boca abajo.

## Narración

<!-- b1 -->
Tienes mil muestras del sensor. Si fueran independientes, la varianza de su
promedio sería cuatro entre mil. Pero tienen memoria. ¿A cuántas muestras
independientes equivalen? ¿Mil? ¿Quinientas? ¿Doscientas cincuenta?
Piénsalo un momento antes de seguir.

<!-- b2 -->
Para un registro largo, el triángulo es casi plano en la zona donde la
autocovarianza importa. Así que la varianza del promedio queda como la
varianza entre ene, multiplicada por la suma de los coeficientes de
correlación en todas las separaciones: la de cero, las de un lado y las del
otro. Esa suma dice cuántas veces se repite, en la práctica, cada dato.

<!-- b3 -->
Sumémosla para el sensor. En separación cero, uno. A un paso, cero coma seis
a cada lado. A dos pasos, cero coma tres seis. A tres, cero coma dos uno
seis. El lado derecho va sumando cero coma nueve seis, uno coma uno ocho,
uno coma tres, y se va acercando a uno coma cinco. Los dos lados dan tres, y
con el uno del centro, cuatro.

<!-- b4 -->
Así que la varianza del promedio es cuatro veces la que tendrías con datos
independientes. Dicho de otra manera, mil muestras del sensor valen como mil
entre cuatro: doscientas cincuenta independientes. A eso se le llama tamaño
de muestra efectivo: el número de muestras dividido entre la suma de los
coeficientes de correlación. Con una memoria más larga, de cero coma nueve
por paso, la suma da diecinueve.

<!-- b5 -->
Es un error muy común calcular el error de una media como si los datos fueran
independientes cuando tienen memoria: el resultado parece mucho más preciso
de lo que es. Así que la memoria tiene dos caras. Gracias a que se borra,
promediar en el tiempo funciona. Pero mientras dura, cada muestra cuenta
menos. Y todavía le queda una tercera cara.

---

# Escena 21 — Prediccion

**Objetivo:** plantear la predicción lineal. El sensor marca 23 y hay que
predecir m pasos más adelante. Recordar la mejor estimación lineal del
capítulo 8 como proyección de flechas:
- ŷ = μ_Y + (σ_XY/σ_X²)(x − μ_X);
- MMSE = σ²(1 − ρ²).

Traducirla a procesos:
x̂[n₀ + m] = μ_x + (C_xx[m]/C_xx[0])(x[n₀] − μ_x).

**Qué hace falta saber antes:** escena 20 (la tercera cara); escena 09 (el
sensor es WSS); capítulo 7, escenas 25 a 27 (flechas, producto escalar,
perpendicular); capítulo 8 (estimación lineal óptima).

**Visual:**
- La grabación del sensor hasta ahora (azul), con el último valor «23 °C» y
  la línea de la media en 20. A la derecha, el futuro en gris con un «?».
- «x̂ = a · x[n₀] + b».
- Las flechas del capítulo 8 (el mismo dibujo): la flecha del futuro, la del
  presente y la sombra de una sobre la otra; el error, perpendicular.
- «ŷ = μ_Y + (σ_XY / σ_X²)(x − μ_X)» y «MMSE = σ_Y² (1 − ρ²)».
- La traducción pieza a pieza: «μ_Y → μ_x», «σ_XY → C_xx[m]», «σ_X² →
  C_xx[0]». Queda «x̂[n₀ + m] = μ_x + (C_xx[m]/C_xx[0]) (x[n₀] − μ_x)».
- El cociente en ámbar: «= ρ». Un dial de ρ: en 1, la predicción sigue al
  dato; en 0, se queda en la media.

## Narración

<!-- b1 -->
La tercera cara: si un proceso recuerda, se puede predecir. El sensor marca
ahora veintitrés grados, tres por encima de su media. ¿Cuánto marcará en el
paso siguiente? No podemos saberlo seguro, pero podemos dar la mejor apuesta.
La buscaremos entre las más sencillas, una recta: la predicción es a por el
dato de ahora, más be.

<!-- b2 -->
Este problema ya lo resolvimos en el capítulo de estimación: la mejor
estimación lineal de una variable a partir de otra. Recuerda la idea con
flechas. Las variables centradas son flechas. Estimar el futuro a partir del
presente es buscar el múltiplo de la flecha del presente que queda más cerca
de la flecha del futuro. Y el más cercano es la proyección: el error queda
perpendicular al dato.

<!-- b3 -->
De esa proyección salía la fórmula. La estimación es la media de lo que se
quiere adivinar, más la covarianza entre las dos variables dividida entre la
varianza del dato, multiplicada por lo que el dato se aparta de su media. Y
el error cuadrático medio que queda es la varianza por uno menos rho al
cuadrado.

<!-- b4 -->
Traducido a procesos: lo que se quiere adivinar es la muestra que llegará
eme pasos más adelante, y el dato es la de ahora. Como el proceso es
estacionario, las dos tienen la misma media y la misma varianza, y su
covarianza es la autocovarianza en eme. La predicción queda así: la media,
más la autocovarianza en eme dividida entre la autocovarianza en cero, por
lo que el dato se aparta de la media.

<!-- b5 -->
Ese cociente es el coeficiente de correlación entre el presente y el futuro.
Y la fórmula dice algo muy razonable. Si el presente y el futuro están muy
correlacionados, le hacemos caso al dato. Si casi no lo están, nos quedamos
con la media. Veamos cuánto caso le hacemos en el sensor.

---

# Escena 22 — HorizonteDePrediccion

**Objetivo:** hacer la predicción del sensor con números.
- m = 1: 21,8, con error 2,56 (frente a 4 sin el dato).
- m = 3: 20,65, con error 3,81.
- m = 10: 20,02, con error ≈ 4.

El predictor tira hacia la media. La predicción tiene un horizonte, que marca
la memoria: la moneda tiene horizonte cero y la pila, infinito.

**Qué hace falta saber antes:** escena 21 (la fórmula del predictor y del
error); escena 07 (el sensor); escena 12 (la parábola del sensor y su mínimo
2,56).

**Visual:**
- La grabación con el «23» y la media «20». Una flecha de «+3» se proyecta un
  paso adelante y se encoge a «+1,8»: «x̂ = 21,8». Una banda de error
  alrededor.
- «MMSE = 4 (1 − 0,36) = 2,56» frente a «sin dato: 4».
- Tres pasos adelante: «0,6³ = 0,216», «x̂ ≈ 20,65», «MMSE ≈ 3,81».
- Diez pasos adelante: «0,6¹⁰ ≈ 0,006», «x̂ ≈ 20,02», «MMSE ≈ 4».
- La predicción como una curva que baja desde el 23 hacia el 20, con la banda
  de error que se ensancha hasta ±2. Una línea vertical: «horizonte».
- Tres miniaturas: moneda (horizonte 0), sensor e interruptor (horizonte
  finito) y pila (horizonte ∞).

## Narración

<!-- b1 -->
Un paso adelante. La correlación es cero coma seis, y la predicción, veinte
más cero coma seis por tres: veintiuno coma ocho grados. El error cuadrático
medio es cuatro por uno menos cero coma tres seis: dos coma cinco seis. Sin
mirar el dato, apostando a la media, el error sería la varianza entera,
cuatro. Mirar el presente ha reducido el error en más de un tercio.

<!-- b2 -->
Fíjate en que el predictor no se atreve a proyectar los tres grados enteros:
solo uno coma ocho. Tira hacia la media. ¿Y ese dos coma cinco seis? Ya lo
habíamos visto: era el punto más bajo de la parábola del sensor, y se
alcanzaba justo en lambda igual a cero coma seis. Aquella parábola era, sin
decirlo, el error de predecir una muestra a partir de otra.

<!-- b3 -->
Tres pasos adelante. La correlación es cero coma seis al cubo, cero coma dos
uno seis. La predicción, veinte más cero coma dos uno seis por tres, da unos
veinte coma seis cinco grados. El error: cuatro por uno menos cero coma dos
uno seis al cuadrado, tres coma ocho uno. El dato ya casi no ayuda.

<!-- b4 -->
Diez pasos adelante. Cero coma seis elevado a diez son unas seis milésimas.
La predicción es prácticamente la media, veinte coma cero dos, y el error es
prácticamente cuatro, la varianza entera. Da igual lo que marque ahora el
sensor: dentro de diez pasos, la mejor apuesta es veinte grados.

<!-- b5 -->
La predicción lineal tiene un horizonte, y lo marca la memoria del proceso.
Con la moneda, el horizonte es cero: ni un paso adelante. Con la pila es
infinito: el valor de ahora es el de siempre. Y la misma idea, proyectar y
dejar el error perpendicular, sirve para algo todavía más útil que predecir:
limpiar una señal.

---

# Escena 23 — FiltroDeUnaMuestra

**Objetivo:** plantear el filtrado de r[n] = s[n] + d[n]: la señal es el
sensor centrado y el ruido es blanco, de varianza 1, sin relación con la
señal. Presentar el filtro FIR. Resolver a mano el caso de una sola muestra
por ortogonalidad: h = E[sr]/E[r²] = 4/5 = 0,8, con error 0,8 frente a 1 si
no se filtra.

**Qué hace falta saber antes:** escena 21 (proyección, error perpendicular);
escena 07 (el sensor y la moneda); escena 08 (no correlacionados).

**Visual:**
- Diagrama:
  - «s[n]» (azul, `SENAL`) y «d[n]» (magenta, `RUIDO`) entran a un sumador;
  - sale «r[n]» (cian, `MEDIDA`) hacia una caja «h»;
  - de la caja sale «ŝ[n]» (ámbar, `ESTIMACION`).
- La temperatura centrada (sin los 20 °C) y encima el ruido, que la ensucia.
- «ŝ[n] = Σ h[k] r[n − k]», con una ventana de L muestras que se desliza
  sobre r[n]. Después, L = 1: «ŝ = h · r».
- Flechas: r, s y la proyección de s sobre r; el error, perpendicular.
  «E[(s − h r) r] = 0» → «h = E[s r] / E[r²]».
- La cuenta: «E[s r] = E[s²] + E[s d] = 4 + 0», «E[r²] = 4 + 1 = 5» → «h = 0,8».
- Dos barras de error: «sin filtrar: 1» y «h = 0,8: 0,8».

## Narración

<!-- b1 -->
Ahora, el problema que da sentido a toda la asignatura. El sensor mide la
temperatura, pero el cable le suma un ruido. Lo que recibimos, erre de ene,
es la señal, ese de ene, más el ruido, de de ene. El ruido es como la moneda:
sin memoria, de media cero, con varianza uno y sin relación con la
temperatura. Queremos recuperar la señal a partir de lo recibido.

<!-- b2 -->
Para simplificar, trabajemos con la temperatura centrada, restándole sus
veinte grados: la señal tiene media cero y varianza cuatro. La herramienta es
un filtro FIR: la estimación es una suma de las últimas ele muestras
recibidas, cada una multiplicada por un coeficiente, hache de ka. Empecemos
por el filtro más pequeño posible, con una sola muestra.

<!-- b3 -->
La estimación es hache por lo recibido ahora. ¿Qué hache? El que haga mínimo
el error cuadrático medio. La regla es la de la proyección: el error, la
señal menos hache por lo recibido, tiene que ser perpendicular al dato. Es
decir, la esperanza del error por lo recibido tiene que ser cero. Despejando,
hache es la esperanza de la señal por lo recibido, entre la esperanza de lo
recibido al cuadrado.

<!-- b4 -->
Hagamos las cuentas. La señal por lo recibido es la señal al cuadrado más la
señal por el ruido. La primera esperanza es la varianza, cuatro; la segunda
es cero, porque no están relacionados. Lo recibido al cuadrado da la varianza
de la señal más la del ruido: cuatro más uno, cinco. Hache vale cuatro
quintos: cero coma ocho.

<!-- b5 -->
El filtro se fía de lo recibido, pero no del todo: lo encoge un veinte por
ciento, porque sabe que una parte es ruido. El error que queda es cero coma
ocho. Si nos quedáramos con lo recibido tal cual, el error sería todo el
ruido: uno. Con una sola muestra ya mejoramos. ¿Y si usamos también la
muestra anterior?

---

# Escena 24 — EcuacionesNormales

**Objetivo:** con L muestras hay L condiciones de ortogonalidad, que dan las
ecuaciones normales Σ h[k] R_rr[m − k] = R_sr[m]. Con ruido no correlacionado,
R_sr = R_ss y R_rr = R_ss + R_dd. Resolver a mano el caso L = 2 con el
sensor: h ≈ (0,74; 0,12) y el error baja de 0,8 a 0,74. Solo hacen falta
autocorrelaciones. Sembrar el filtro de Wiener (capítulo 12).

**Qué hace falta saber antes:** escena 23 (el caso de una muestra); capítulo
8 (ecuaciones normales).

**Visual:**
- «Σ h[k] R_rr[m − k] = R_sr[m], m = 0 … L − 1», construida por piezas. Sello
  «ecuaciones normales».
- «R_sr = R_ss» y «R_rr = R_ss + R_dd», con los colores de señal y ruido.
- Barras de autocorrelación:
  - señal: «4», «2,4»;
  - ruido: «1», «0»;
  - recibido: «5», «2,4».
- El sistema de 2 × 2: «5 h₀ + 2,4 h₁ = 4» y «2,4 h₀ + 5 h₁ = 2,4» → «h₀ ≈
  0,74», «h₁ ≈ 0,12».
- Dos coeficientes como barras sobre r[n] y r[n − 1], uno alto y otro bajo.
  Error: «0,8 → 0,74».
- Un rótulo: «Wiener → capítulo 12».

## Narración

<!-- b1 -->
Con ele muestras, el error tiene que ser perpendicular a cada una de ellas:
son ele condiciones, una por muestra. Si se desarrolla cada condición como
antes, aparecen autocorrelaciones. La suma de cada coeficiente, hache de ka,
por la autocorrelación de lo recibido en eme menos ka, tiene que ser igual a
la correlación cruzada entre la señal y lo recibido en eme.

<!-- b2 -->
Son las ecuaciones normales del capítulo de estimación, ahora con procesos:
ele ecuaciones con ele incógnitas. Y como la señal y el ruido no están
relacionados, se simplifican. La correlación cruzada entre la señal y lo
recibido es la autocorrelación de la señal. Y la autocorrelación de lo
recibido es la de la señal más la del ruido.

<!-- b3 -->
Con dos muestras. La autocorrelación de la señal vale cuatro en cero y dos
coma cuatro a un paso; la del ruido, uno en cero y nada más. La de lo
recibido, cinco y dos coma cuatro. Primera ecuación: cinco por hache cero más
dos coma cuatro por hache uno igual a cuatro. Segunda: dos coma cuatro por
hache cero más cinco por hache uno igual a dos coma cuatro.

<!-- b4 -->
Resolviendo el sistema, hache cero vale cero coma siete cuatro, y hache
uno, cero coma uno dos. El filtro usa sobre todo la muestra de ahora, y un
poco la anterior, porque la temperatura recuerda y el ruido no. El error baja
de cero coma ocho a cero coma siete cuatro. Con más muestras seguiría
bajando, cada vez menos.

<!-- b5 -->
Fíjate en lo que ha hecho falta para diseñar el filtro: solo la memoria de la
señal y la del ruido, sus autocorrelaciones. Ninguna densidad. Esto es el
germen del filtro de Wiener, que veremos en el capítulo doce. Pero deja una
pregunta más general: una vez que el filtro existe, ¿qué le hace a un proceso
aleatorio que pasa por él?

---

# Escena 25 — RepasoConvolucion

**Objetivo:** recordar desde cero lo que hace falta de Señales y Sistemas.
- Un LTI queda descrito por su respuesta al impulso.
- La convolución, con el promediador h = (½, ½) y la entrada 2, 4, 6, que da
  1, 3, 5, y su fórmula discreta y continua.
- Fourier y H(jω): la convolución se vuelve producto.
- H(0), la ganancia en continua, es la suma o el área de h.

**Qué hace falta saber antes:** del repaso del capítulo 7 (sistema LTI,
Fourier, filtros); escena 23 (el FIR como suma pesada).

**Visual:**
- `BloqueLTI`: entra un golpe y sale «h». El promediador: «h[0] = ½»,
  «h[1] = ½».
- Convolución a mano: la entrada «2, 4, 6» y h dada la vuelta que se desliza
  debajo; en cada posición, los productos y la suma: «½·2 = 1», «½·4 + ½·2 =
  3», «½·6 + ½·4 = 5».
- «y[n] = Σ h[k] x[n − k]» → «y(t) = ∫ h(v) x(t − v) dv»: los palitos se
  estrechan hasta ser una curva.
- Una señal que se descompone en senos; «H(jω)» como una curva de ganancia.
  «convolución ↔ producto».
- «H(0) = Σ h = ∫ h». Promediador: «½ + ½ = 1». Entra «2, 2, 2» y sale
  «2, 2, 2».

## Narración

<!-- b1 -->
Recordemos cómo funciona un sistema lineal e invariante en el tiempo. Queda
descrito entero por su respuesta al impulso, hache: lo que sale cuando entra
un golpe instantáneo. Tomemos uno sencillo, en tiempo discreto: el que
promedia las dos últimas muestras. Su respuesta al impulso vale un medio en
cero, un medio en uno, y nada más.

<!-- b2 -->
Entra la secuencia dos, cuatro, seis. La primera salida es un medio por dos:
uno, porque antes no había nada. La segunda, un medio por cuatro más un medio
por dos: tres. La tercera, un medio por seis más un medio por cuatro: cinco.
Cada salida es una suma de entradas recientes, cada una pesada por un valor de
hache. Eso es la convolución.

<!-- b3 -->
Escrita en general: la salida en ene es la suma, para cada ka, de hache de ka
por la entrada en ene menos ka. La entrada de hace ka pasos pesa hache de ka.
En tiempo continuo, la suma se convierte en una integral: i griega de te es
la integral de hache de uve por equis de te menos uve.

<!-- b4 -->
La otra forma de verlo es en frecuencia. La transformada de Fourier
descompone una señal en senos de todas las frecuencias. La de la respuesta
al impulso, hache de jota omega, dice cuánto amplifica el sistema cada
frecuencia. Y la gran ventaja: una convolución en el tiempo se convierte en
una multiplicación en frecuencia.

<!-- b5 -->
Un valor nos va a interesar: hache en cero, la ganancia en continua. Es la
suma de todos los valores de hache, o su integral, y una entrada constante
sale multiplicada por ella. En el promediador, un medio más un medio: uno.
Entra un dos constante y sale un dos.

---

# Escena 26 — MediaDeSalida

**Objetivo:** deducir paso a paso μ_y = H(0) μ_x (la esperanza es lineal y
entra en la suma; la media, constante, sale fuera). Comprobarlo con el sensor
y el promediador (media 20) y con el filtro que resta la muestra anterior
(media 0). Nombrar la letra pequeña (sistema estable, varianza finita) y
anunciar que la salida es conjuntamente WSS.

**Qué hace falta saber antes:** escena 25 (convolución, H(0)); capítulo 7,
escena 13 (linealidad de la esperanza); escena 09 (WSS).

**Visual:**
- El ensemble de entrada entra al `BloqueLTI` y sale otro ensemble.
- Deducción en cuatro renglones:
  - «E[y[n]] = E[Σ h[k] x[n − k]]»;
  - «= Σ h[k] E[x[n − k]]» («linealidad»);
  - «= Σ h[k] μ_x» («estacionaria»);
  - «= μ_x Σ h[k] = H(0) μ_x».
- «μ_y = H(0) μ_x», con recuadro.
- Comprobación 1: el sensor (media 20) por el promediador (H(0) = 1) → «20».
- Comprobación 2: «h = (1, −1)», «H(0) = 0» → «μ_y = 0».
- Dos casillas pequeñas: «sistema estable», «varianza finita». Un rótulo:
  «apunte en profundidad».
- Un sello «WSS» en la salida y un rótulo «¿conjuntamente WSS? → ahora».

## Narración

<!-- b1 -->
Si a la entrada llega una realización de un proceso, a la salida sale otra
señal aleatoria: un proceso nuevo. Empecemos por su media. La media de la
salida es la esperanza de una suma de entradas pesadas por hache. Y la
esperanza es lineal: la esperanza de una suma es la suma de las esperanzas, y
los números que multiplican salen fuera.

<!-- b2 -->
Así que la esperanza entra en la suma y se queda con cada entrada. Si la
entrada es estacionaria, la esperanza de cada una es la misma media, que sale
fuera también. Dentro queda la suma de todos los hache: la ganancia en
continua. La media de la salida es hache en cero por la media de la entrada.

<!-- b3 -->
Compruébalo con el sensor y el promediador. La temperatura tiene media
veinte, y el promediador, ganancia uno en continua: la salida tiene media
veinte. Promediar dos temperaturas no cambia la temperatura media. Y con el
filtro que resta la muestra anterior, cuya respuesta es uno y menos uno, la
ganancia en continua es cero: la salida tiene media cero, sea cual sea la
entrada.

<!-- b4 -->
La media atraviesa el sistema como si fuera una señal constante, que es lo
que es: la parte que no cambia. En tiempo continuo, la deducción es idéntica,
con una integral, y la letra pequeña es que el sistema sea estable y la
entrada tenga varianza finita. Y hay algo más: la correlación cruzada entre
entrada y salida solo depende de la separación. Lo veremos en la cuenta
siguiente, que es la importante.

---

# Escena 27 — CorrelacionDeSalida

**Objetivo:** deducir entera R_yx(τ) = h(τ) * R_xx(τ), que no depende de t,
así que la salida es conjuntamente WSS. Obtener R_yy = R_hh * R_xx
"repitiendo el paso". Explicar R_hh con el promediador: ½ en cero y ¼ a un
paso. Comprobarlo con la moneda en el promediador: la salida vale 1, 0 o −1
con probabilidades ¼, ½ y ¼, y su varianza es ½.

**Qué hace falta saber antes:** escena 26 (la esperanza entra en la suma);
escena 25 (convolución, promediador); escena 07 (la moneda: R = impulso).

**Visual:**
- Deducción en renglones:
  - «E[y(t + τ) x(t)]»;
  - «= E[∫ h(v) x(t + τ − v) dv · x(t)]»;
  - «= ∫ h(v) E[x(t + τ − v) x(t)] dv»;
  - «= ∫ h(v) R_xx(τ − v) dv».

  Se tacha cualquier «t» que sobre: «no aparece t».
- «R_yx(τ) = h(τ) * R_xx(τ)», con recuadro. Por el `BloqueLTI` pasa la curva
  R_xx en lugar de una señal.
- Dos bloques en cadena, «h(−τ)» y «h(τ)», que se funden en «R_hh(τ)».
  «R_yy = R_hh * R_xx», con recuadro.
- El promediador deslizándose sobre sí mismo: sin desplazar, «¼ + ¼ = ½»;
  desplazado un paso, «¼».
- La moneda en el promediador: una tabla de cuatro parejas de tiradas → «1»,
  «0», «0», «−1» → «¼, ½, ¼» → «Var = ½». Tilde junto a «R_hh[0] = ½».

## Narración

<!-- b1 -->
Calculemos la correlación cruzada entre la salida en te más tau y la entrada
en te. La salida es una integral de la entrada, así que el producto también
es una integral. La esperanza vuelve a entrar en ella, y dentro queda la
esperanza del producto de dos entradas separadas tau menos uve: la
autocorrelación de la entrada en tau menos uve.

<!-- b2 -->
El resultado es la integral de hache de uve por erre sub equis equis de tau
menos uve. Eso es una convolución: la correlación cruzada es hache
convolucionada con la autocorrelación de la entrada. Y en el resultado no
aparece te por ningún lado, solo tau: entrada y salida son conjuntamente
estacionarias, como habíamos anunciado.

<!-- b3 -->
Fíjate en lo que acaba de pasar. Las señales son aleatorias, pero la relación
entre sus correlaciones es determinista: la convolución de siempre, con la
autocorrelación haciendo de señal de entrada. Repitiendo el mismo paso con la
segunda hache sale la autocorrelación de la salida: la de la entrada,
convolucionada con erre sub hache hache, la autocorrelación determinista de
la respuesta al impulso.

<!-- b4 -->
Erre sub hache hache se obtiene deslizando hache sobre sí misma y sumando los
productos donde se solapa. En el promediador, sin desplazar: un medio al
cuadrado más un medio al cuadrado, un medio. Desplazado un paso, solo se
solapa un término: un cuarto. Y con la moneda a la entrada, cuya
autocorrelación es un impulso, la salida tiene justo esa autocorrelación.

<!-- b5 -->
Comprobémoslo a mano. La salida es la media de dos tiradas: vale uno, cero o
menos uno, con probabilidades un cuarto, un medio y un cuarto. La esperanza
del cuadrado es un cuarto más un cuarto: un medio. Coincide.

---

# Escena 28 — VarianzaDeSalida

**Objetivo:** hacer el ejemplo continuo del complemento. La onda telegráfica
(λ = 1, R_xx = e^(−2|τ|)) entra al pasabajos h(t) = 3e^(−3t)u(t), que tiene
H(0) = 1.
- R_hh = (3/2)e^(−3|τ|), que se deduce.
- R_yy(0) = ∫ R_hh R_xx = (3/2)(2/5) = 0,6. La simulación da 0,61.

Lectura: el pasabajos quita potencia, en una carrera entre dos memorias:
β/(α + β) = 3/5.

**Qué hace falta saber antes:** escena 27 (R_yy = R_hh * R_xx, R_hh como
solapamiento); escena 14 (la onda telegráfica); escena 25 (H(0) = área de h).

**Visual:**
- La onda telegráfica entra a un `BloqueLTI` con la curva «3e^(−3t)» dibujada
  dentro; sale una señal suavizada. «área de h = 1».
- h deslizándose sobre sí misma a una distancia τ, con el solapamiento
  sombreado: «9 e^(−3τ) ∫ e^(−6t) dt = 9 e^(−3τ) · ⅙ = (3/2) e^(−3τ)».
- Las dos curvas «e^(−2|s|)» y «(3/2) e^(−3|s|)», y su producto
  «(3/2) e^(−5|s|)» con el área sombreada: «⅕ + ⅕ = ⅖», «(3/2)(2/5) = 3/5 =
  0,6».
- Tilde: «simulación: 0,61».
- Dos barras de potencia: entrada «1», salida «0,6».
- «β/(α + β) = 3/(2 + 3)»: un deslizador del filtro (β) que mueve la barra de
  salida entre 0 y 1.

## Narración

<!-- b1 -->
Ahora, un ejemplo continuo. A la entrada ponemos la onda telegráfica con
lambda igual a uno: su autocorrelación es e elevado a menos dos por el valor
absoluto de tau, y su varianza, uno. El filtro es un pasabajos sencillo: hache
de te es tres por e elevado a menos tres te, a partir de te igual a cero. Su
área vale uno: ganancia uno en continua.

<!-- b2 -->
Primero, la autocorrelación determinista del filtro. Deslizamos hache sobre
sí misma una distancia tau, multiplicamos y medimos el área donde se solapan.
Queda nueve por e elevado a menos tres tau, por el área de e elevado a menos
seis te, que es un sexto. Resultado: tres medios por e elevado a menos tres
por el valor absoluto de tau.

<!-- b3 -->
La varianza de la salida es su autocorrelación en cero: la convolución de
las dos autocorrelaciones evaluada en cero, que resulta ser el área del
producto de las dos curvas. Al multiplicar las exponenciales, los exponentes
se suman: tres medios por e elevado a menos cinco por el valor absoluto de
tau. Su área es un quinto a cada lado; por tres medios, tres quintos: cero
coma seis.

<!-- b4 -->
Una simulación, filtrando la onda de verdad, da cero coma seis uno: la
cuenta funciona. El filtro le ha quitado potencia al proceso, porque un
pasabajos recorta las variaciones rápidas. Cuánto quita depende de una
carrera entre dos memorias, la del filtro y la del proceso: tres entre tres
más dos. Un filtro mucho más rápido lo deja casi intacto; uno mucho más lento
se lo come casi entero.

---

# Escena 29 — EnFrecuencia

**Objetivo:** pasar a frecuencia: S_xx = F{R_xx}, S_yx = H S_xx y
S_yy = |H|² S_xx. Explicar el módulo al cuadrado sin números complejos (los
desfases se cancelan). Ejemplo de la moneda en el promediador: entra plano y
sale pasabajos, así que el filtro le da forma al ruido. Aplicación:
identificar un sistema con la moneda (R_yx = h = ½, ½, 0). Cierre: la
analogía con la densidad espectral de energía abre el capítulo 11.

**Qué hace falta saber antes:** escena 27 (R_yx = h * R_xx; la moneda en el
promediador); escena 25 (Fourier: convolución ↔ producto).

**Visual:**
- «S_xx(jω) = F{R_xx(τ)}». Las fórmulas de la escena 27 se transforman:
  «*» → «·». «S_yx = H S_xx», «S_yy = |H|² S_xx», con recuadro.
- Dos flechas «h» y «h dada la vuelta» con sus desfases «+φ» y «−φ» que se
  cancelan: «|H|²».
- `Espectro`:
  - la moneda, plana;
  - encima, |H|² del promediador: 1 en la continua y 0 en la frecuencia más
    rápida (la tira +1, −1, +1… que el promediador anula);
  - el producto, una curva que cae.

  Rótulo: «el filtro le da forma al ruido».
- Identificación: una caja negra «h = ?». Entra la tira de la moneda; un
  correlador entre la entrada y la salida dibuja «½», «½», «0». Tilde junto a
  la h del promediador.
- «|H|² S_xx» al lado de la fórmula de la densidad espectral de energía de
  Señales y Sistemas. S_xx se colorea en ámbar y aparece «densidad espectral
  de potencia».

## Narración

<!-- b1 -->
Las convoluciones son incómodas, así que pasemos a frecuencia. Llamemos ese
sub equis equis de jota omega a la transformada de Fourier de la
autocorrelación. Cada convolución se vuelve un producto: la correlación
cruzada se transforma en hache de jota omega por ese sub equis equis, y la
autocorrelación de la salida, en el módulo de hache al cuadrado por ese sub
equis equis.

<!-- b2 -->
¿Por qué al cuadrado? Porque hache aparece dos veces, una tal cual y otra
dada la vuelta, y en frecuencia sus desfases se cancelan. En cada frecuencia,
el filtro multiplica por el cuadrado de su ganancia, y la fase no importa. En
tiempo discreto, exactamente igual.

<!-- b3 -->
Con la moneda y el promediador. La moneda no tiene memoria: su
autocorrelación es un impulso, cuya transformada es plana, igual en todas las
frecuencias. El promediador deja pasar la continua y anula la frecuencia más
rápida, la que alterna más uno y menos uno. A la salida, la curva plana cae
hacia las frecuencias altas: el filtro le ha dado forma al ruido.

<!-- b4 -->
Y una aplicación preciosa. La correlación cruzada era hache convolucionada
con la autocorrelación de la entrada. Si la entrada es la moneda, esa
autocorrelación es un impulso, y la correlación cruzada es directamente
hache: un medio, un medio y cero, justo el promediador. Metes ruido en un
sistema desconocido, mides la correlación entre lo que entra y lo que sale,
y tienes su respuesta al impulso.

<!-- b5 -->
Por último, mira otra vez el módulo de hache al cuadrado por ese sub equis
equis. En Señales y Sistemas, así se transformaba la densidad espectral de
energía de una señal al pasar por un filtro. No es casualidad. Ese sub equis
equis dice cómo se reparte la potencia del proceso entre las frecuencias, y
su nombre es densidad espectral de potencia.
