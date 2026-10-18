# Capítulo 7 — Modelos probabilísticos

> **Guion base: narración de todo el capítulo. No se renderiza.**
> Es la fuente de texto para los 7 episodios (ver `../README.md` §1 para qué
> escenas van en cada uno). Cada episodio copia de aquí su narración a su
> propio `E<N>_.../guion.md`, que es el que lleva gancho, cierre y momentos, y
> el que se anima. Las secciones "Visual" son ideas iniciales, no
> especificación.
>
> **Estado:** narración completa (**segunda versión**, más explícita y con el
> repaso inicial pedido por el usuario), **esperando la aprobación del usuario**.
> Mientras no esté aprobada, cualquier ajuste de texto que pida el usuario se
> hace aquí primero, y después se copia al `guion.md` del episodio.

Guion para las 29 escenas del capítulo. Fuentes: `Apuntes/PROCESAMIENTO DE
SEÑALES.md` (sección "Modelos probabilísticos", líneas 1–239, sin los
Ejercicios Propuestos) y `Apuntes/PROCESAMIENTO DE SEÑALES - Cap 7 en
profundidad.md`: Parte 1 (demostraciones), Parte 2 (ejemplos numéricos),
Parte 3.3 y 3.4 (grandes números, trampas de la correlación) y Parte 4
(conexiones con los capítulos 8 a 13). Figuras de referencia:
`c7p-cauchy-schwarz.svg`, `c7p-vectores-angulo.svg`,
`c7p-varianza-total.svg`, `c7p-lln-chebyshev.svg`, `c7p-cuarteto.svg`.

**Es el primer capítulo de la serie y no da nada por sabido.** Arranca con un
repaso de unos tres minutos, muy por encima, de Señales y Sistemas y de
Probabilidad y Estadística (escenas 01 y 02), solo para ubicar a quien mira.
Después, todo lo que se usa se explica en el momento en que hace falta,
incluidas las herramientas matemáticas (derivada como pendiente, integral como
área, sumatoria, vector, producto escalar, parábola y discriminante).

Cómo está escrito (README §3, "Explicar de forma explícita"): cada concepto
nuevo sigue el mismo camino. Una pregunta o un caso concreto; la cuenta hecha a
mano con números pequeños; el dibujo; y recién al final la fórmula, leída
término a término, como resumen de lo que ya se hizo. Las deducciones cortas se
hacen enteras, paso a paso, diciendo qué regla se usa en cada paso. Los
ejemplos que vuelven (el dado, el test médico, el canal que confunde bits, la
altura) son siempre los mismos, para que quien mira no tenga que aprender un
ejemplo nuevo cada vez.

Convención: cada escena tiene Objetivo, qué hace falta saber antes, qué se ve,
y la narración partida en bloques `<!-- bN -->` que se sincronizan uno a uno
con un tramo de animación. Castellano de España.

## Reparto en episodios

| Episodio | Escenas | Idea fuerza |
|---|---|---|
| E1 · Lo que no se puede predecir | 01 RepasoSenales, 02 RepasoAzar, 03 PorQueProbabilidad, 04 ModeloProbabilistico | Una señal con ruido no se puede calcular, pero sí se pueden conocer sus reglas |
| E2 · Cuando sabes algo más | 05 ProbabilidadCondicional, 06 Independencia, 07 TestMedico, 08 Bayes | Saber algo nuevo achica el mundo, y Bayes le da la vuelta a la pregunta |
| E3 · La forma del azar | 09 VariableAleatoria, 10 Acumulada, 11 Densidad, 12 DistribucionesClave | Todo lo que se puede saber de una variable aleatoria cabe en una curva |
| E4 · Dos números para resumirlo todo | 13 Esperanza, 14 Varianza, 15 Chebyshev, 16 GrandesNumeros | Con la media y la varianza ya se puede acotar cualquier cosa, y por eso promediar funciona |
| E5 · Dos variables a la vez | 17 TablaConjunta, 18 DensidadConjunta, 19 EsperanzaCondicional, 20 VarianzaTotal | De la tabla de lo enviado y lo recibido sale todo: marginales, condicionales y lo que una explica de la otra |
| E6 · Lo que una variable sabe de otra | 21 Correlacion, 22 Covarianza, 23 CeroNoEsNada, 24 CombinacionLineal | Covarianza cero no quiere decir que no haya relación |
| E7 · Variables que son flechas | 25 ProductoEscalar, 26 EspacioVectorial, 27 RhoEsCoseno, 28 CauchySchwarz, 29 TrampasDeRho | La correlación es, literalmente, el coseno de un ángulo |

Narración base por episodio (sin gancho ni cierre): ~1.050–1.250 palabras,
unos 7–8 min de voz; con gancho y cierre, ~9–10 min. E1 empieza con el
repaso (escenas 01 y 02, ~3 min en total).

El gancho y el cierre de cada episodio **no** están aquí: se escriben al
armar el `guion.md` del episodio (README §2, paso 8). Cada cierre anuncia el
episodio siguiente por su título; el cierre de E7 anuncia el E1 del capítulo 8
(Estimación), cuyo título se decide al escribir el guion base del capítulo 8.

## Hilos que cruzan el capítulo

Para quien arme cada episodio: estos bucles ya están sembrados en la
narración y hay que respetarlos (y retomarlos en ganchos y cierres).

- **Los ejemplos que vuelven** (mismo dibujo siempre):
  - **el dado** (escenas 04, 05, 06, 09, 10, 13, 14): espacio muestral,
    condicional, independencia, acumulada en escalera, media 3,5, varianza 2,92;
  - **el canal que confunde bits** (escenas 08, 17, 19, 21, 22): se envía un 0
    con probabilidad 0,7 y un 1 con 0,3, y el canal cambia el bit un 10 % de las
    veces. En la escena 08 se calcula Bayes (0,79); en la 17 se convierte en la
    tabla conjunta (0,63 · 0,07 · 0,03 · 0,27); en la 19, en esperanza
    condicional; en las 21 y 22, en correlación (0,27) y covarianza (0,168).
    Es el mismo planteo de los capítulos 8, 9 y 13: tiene que ser el mismo dibujo;
  - **el test médico** (escena 07, una de cada seis): vuelve en el capítulo 9;
  - **la altura** (escenas 19 y 20): 40 % hombres de media 175 cm, 60 % mujeres
    de media 162 cm;
  - **el ejemplo 6, 4, 3** (escenas 24, 26, 27, 28): varianzas 6 y 4, covarianza 3,
    flechas de largo √6 y 2, unos 52 grados.
- **Señal enviada y señal recibida**: se nombra en la escena 03 como la razón de
  ser de la materia; el canal de bits la vuelve concreta.
- **El centro de masa**: la media como punto de equilibrio (escena 13), reusado
  para la nube (escena 18).
- **"Las varianzas se suman"**: se usa en la escena 16 (E4) con la promesa de
  demostrarlo, y se paga en la escena 24 (E6). Bucle abierto a propósito.
- **Chebyshev → grandes números** (escenas 15 y 16). Puente al capítulo 10
  (promediar en el tiempo), sin nombrar la ergodicidad.
- **Varianza total** (escena 20): "lo que el grupo explica" y "lo que no" siembra
  el error del mejor estimador del capítulo 8.
- **Teorema del coseno**: la fórmula de la escena 24 se revela como geometría en
  la escena 27. Es el pago del E7.
- **La parábola de Cauchy-Schwarz** (escena 28): se anuncia que reaparece en los
  capítulos 11 y 13.
- **Cierre del capítulo** (la escena 29 ya lo prepara; cierre de E7, a escribir):
  si las variables son flechas, estimar una a partir de otra es proyectar una
  flecha sobre otra → capítulo 8.

## Recortes decididos

- El repaso de Señales y Sistemas y de Probabilidad y Estadística es de tres
  minutos y **muy por encima**, como pidió el usuario: cada tema en una o dos
  frases con su dibujo. Fourier, convolución y muestreo se vuelven a explicar
  con calma en los capítulos que los usan (10 y 11).
- No entran: la definición formal de álgebra de eventos; las variables mixtas con
  impulsos de Dirac (solo el dibujo de la curva con un salto); la demostración de
  la torre con Fubini (se hace con la tabla y con la altura, que es lo mismo con
  números); los estimadores muestrales y el n − 1 (Parte 3.1–3.2 del complemento).
- Los Ejercicios Propuestos no se resuelven (los números del canal de bits no
  son los del ejercicio 6).

## Pronunciación

Probar de oído antes de sintetizar (README §9): Bayes, Chebyshev, Markov,
Gauss, Cauchy-Schwarz, Fourier. Letras que se leen en voz alta: «equis»,
«i griega», «zeta», «mu», «sigma», «rho», «alfa», «beta», «lambda», «theta»,
«épsilon».

## Piezas visuales nuevas

Van a `comun/figuras.py` (sección «capítulo 07, episodio N»):
- repaso: señal senoidal y señal muestreada (puntos), caja de sistema con
  entrada y salida, espectro de barras;
- dado de seis caras dentro de un rectángulo (el espacio muestral), óvalos de
  eventos, y el rectángulo que se encoge al condicionar;
- árbol de probabilidades de dos niveles (para el test y el canal);
- grilla de personas (`persona` de `iconos.py`) con recolor por grupo;
- escalera de la acumulada y curva continua, cursor que barre, recta tangente que
  muestra la pendiente, área que se rellena bajo la curva;
- histograma que se llena muestra a muestra hasta parecerse a la densidad (`Curva`);
- placa sobre un filo (media como punto de equilibrio);
- corridas del promedio con la banda de Chebyshev que se angosta;
- tabla conjunta 2 × 2 con sumas de filas y columnas (marginales);
- nube de puntos bivariada con sus proyecciones sobre los ejes y rebanadas;
- par de flechas con ángulo, cuadrícula para Pitágoras, parábola con su discriminante;
- cuatro nubes con el mismo rho (como `c7p-cuarteto.svg`).

---

# Escena 01 — RepasoSenales

**Objetivo:** en un minuto y medio, ubicar a quien mira con lo que se vio en
Señales y Sistemas: qué es una señal, continua y discreta, qué es un sistema,
los sistemas lineales e invariantes, y la mirada en frecuencia. Muy por encima:
solo nombres y dibujos, con la promesa de volver a cada cosa cuando haga falta.

**Qué hace falta saber antes:** nada.

**Visual:**
- Un micrófono y la onda de voz que sale de él: una curva que cambia con el tiempo.
- La misma curva convertida en puntos equiespaciados: tiempo continuo → discreto.
- Una caja con una flecha que entra y otra que sale: entra una señal, sale otra.
- La caja se etiqueta «lineal» (dos entradas sumadas → salidas sumadas) e
  «invariante» (la misma entrada más tarde → la misma salida más tarde).
- Un seno que entra y sale más pequeño y corrido; luego una señal que se descompone
  en varios senos y aparece un espectro de barras. Una barra se apaga: un filtro.

## Narración

<!-- b1 -->
Antes de empezar, un repaso rápido de lo que se vio en Señales y Sistemas,
muy por encima. Una señal es algo que cambia con el tiempo y lleva
información: la voz que capta un micrófono, la tensión en un cable, la
temperatura de una habitación. Matemáticamente, es una función: a cada
instante le toca un valor.

<!-- b2 -->
Si la señal tiene un valor en cada instante, sin huecos, es de tiempo
continuo. Si solo la miramos cada cierto tiempo, por ejemplo mil veces por
segundo, se convierte en una lista de números: es de tiempo discreto, y es la
que manejan los ordenadores. Pasar de una a otra se llama muestrear.

<!-- b3 -->
Un sistema es cualquier cosa que recibe una señal y entrega otra: un
amplificador, un altavoz, un programa que limpia una grabación. Los más
útiles son los lineales e invariantes en el tiempo. Lineales: si sumas dos
entradas, se suman sus salidas. Invariantes: si metes la misma entrada más
tarde, sale lo mismo, pero más tarde.

<!-- b4 -->
Y la gran idea de esa materia: cualquier señal se puede ver como una suma de
senos de distintas frecuencias. Eso es la transformada de Fourier, y el
dibujo de cuánto hay de cada frecuencia es el espectro. Un filtro es un
sistema que deja pasar unas frecuencias y frena otras. Todo esto volverá,
explicado con calma, cuando lo necesitemos.

---

# Escena 02 — RepasoAzar

**Objetivo:** en un minuto y medio, ubicar a quien mira con lo que se vio en
Probabilidad y Estadística: experimento aleatorio, probabilidad como
frecuencia a largo plazo, variable aleatoria, distribución y media. Dejar
claro que en este capítulo todo se vuelve a construir despacio.

**Qué hace falta saber antes:** nada.

**Visual:**
- Una moneda que se lanza una y otra vez; debajo, un contador de caras que se
  estabiliza cerca de «0,5».
- Un dado; sus seis caras van a una recta numérica (variable aleatoria).
- Barras de un histograma que suben; encima, la campana de Gauss.
- Un punto de equilibrio bajo la campana: «media».

## Narración

<!-- b1 -->
Y ahora, el repaso de Probabilidad y Estadística, también muy por encima. Un
experimento aleatorio es uno cuyo resultado no puedes saber de antemano,
aunque lo repitas en las mismas condiciones: lanzar una moneda, tirar un
dado, medir el ruido de un aparato.

<!-- b2 -->
La probabilidad de un resultado es la fracción de veces que ocurriría si
repitieras el experimento muchísimas veces. Lanza una moneda diez veces y
quizá salgan siete caras. Lánzala diez mil y la fracción de caras se pega al
cincuenta por ciento. Ese número al que se acerca es la probabilidad.

<!-- b3 -->
Una variable aleatoria es un número que depende del resultado del
experimento: lo que marca el dado, la tensión que se mide. Su distribución
dice qué valores puede tomar y con qué probabilidad, y se suele dibujar como
una curva. La más famosa es la campana de Gauss. Y la media es el valor
alrededor del cual se reparten los resultados.

<!-- b4 -->
Si todo esto te suena, perfecto. Si no, no pasa nada: en este capítulo
vamos a construir cada una de estas ideas desde cero, con ejemplos y con
números, porque todo el resto de la materia se apoya en ellas. Y la primera
pregunta es la más importante: ¿por qué una materia de señales necesita
tanta probabilidad?

---

# Escena 03 — PorQueProbabilidad

**Objetivo:** contar por qué la materia necesita probabilidad: las señales
que importan no se pueden predecir, pero tienen reglas. Presentar el problema
de fondo de toda la materia (señal enviada, ruido, señal recibida) y las dos
grandes tareas: estimar y detectar.

**Qué hace falta saber antes:** escenas 01 y 02.

**Visual:**
- Un seno perfecto que se repite igual; al lado, una grabación de ruido que cada
  vez sale distinta.
- Una antena envía una señal limpia (azul); por el camino se le suma ruido
  (magenta); la antena receptora recibe la suma (cian).
- Dos tarjetas: «estimar» (una curva que intenta seguir a la señal limpia) y
  «detectar» (una pregunta: ¿hay señal o solo ruido? con un «sí» y un «no»).
- Un mapa del curso: capítulos 7 a 13 como estaciones de una línea.

## Narración

<!-- b1 -->
En Señales y Sistemas las señales se conocían de antemano. Un seno vale lo
mismo hoy que mañana: puedes calcular cuánto valdrá dentro de un año. Pero
las señales que de verdad importan no son así. Nadie sabe qué palabras dirás
en tu próxima llamada, ni qué forma exacta tendrá el ruido que se cuele en
ella. Si lo supiéramos, no haría falta enviar nada.

<!-- b2 -->
Piensa en un mensaje que viaja por el aire. Lo que sale de la antena es
limpio. Por el camino se le suma ruido: interferencias, calor en los
circuitos, otras señales. Y lo que llega al otro lado es la suma de las dos
cosas. El ruido es distinto cada vez, así que no se puede restar sin más,
como si fuera un número conocido.

<!-- b3 -->
Lo que sí se puede es conocer sus reglas: qué valores suele tomar, cuáles
son raros, cómo se relaciona con lo que se envió. Con esas reglas hacemos
dos cosas, que son las dos grandes tareas de esta materia. Estimar:
adivinar lo mejor posible cuánto valía la señal. Y detectar: decidir si en
lo que llegó hay señal o solo ruido, o si se envió un uno o un cero.

<!-- b4 -->
Las dos cosas se hacen con probabilidad. Por eso la materia empieza aquí:
en este capítulo construimos el lenguaje, en los siguientes aprendemos a
estimar y a decidir, y al final lo aplicamos a señales enteras que cambian
en el tiempo. Empecemos por lo más básico: cómo se describe, con
matemáticas, algo que no se puede predecir.

---

# Escena 04 — ModeloProbabilistico

**Objetivo:** presentar el modelo probabilístico en sus tres piezas
(espacio muestral, eventos y probabilidad) con el dado, y las tres reglas que
tiene que cumplir cualquier probabilidad, con la regla del complementario
como consecuencia.

**Qué hace falta saber antes:** escena 02 (probabilidad como frecuencia).

**Visual:**
- Las seis caras del dado dentro de un rectángulo: «espacio muestral».
- Un óvalo rodea 2, 4 y 6: «evento: sale par». Otro rodea 5 y 6: «sale más de 4».
- Cada cara con «1/6»; el óvalo de los pares suma «3/6 = 1/2».
- Las tres reglas aparecen de a una, cada una con su dibujo: una barra de 0 a 1;
  el rectángulo entero con «1»; dos óvalos separados cuyas probabilidades se suman.
- El complementario: el óvalo de «sale 6» y todo lo de fuera en otro color: «1 − 1/6».

## Narración

<!-- b1 -->
Para describir algo que no se puede predecir hacen falta tres piezas. La
primera es el espacio muestral: la lista de todo lo que puede pasar. Si
tiras un dado, son las seis caras. Lo dibujamos como un rectángulo con los
seis resultados dentro. Pase lo que pase, el resultado estará ahí.

<!-- b2 -->
La segunda pieza son los eventos: grupos de resultados que nos interesan.
Que salga un número par es un evento, y está formado por el dos, el cuatro y
el seis. Que salga más de cuatro es otro, formado por el cinco y el seis. Un
evento ocurre si el resultado cae dentro de su grupo.

<!-- b3 -->
La tercera pieza es la probabilidad: un número que le asignamos a cada
evento. Con un dado bien hecho, cada cara vale un sexto. Y la probabilidad
de un evento es la suma de las de sus caras: sale par tiene tres caras, así
que vale tres sextos, es decir, un medio.

<!-- b4 -->
No vale cualquier número. Toda probabilidad cumple tres reglas. Primera:
está entre cero y uno. Cero es imposible, uno es seguro. Segunda: el espacio
muestral entero vale uno, porque algo tiene que pasar. Tercera: si dos
eventos no pueden ocurrir a la vez, la probabilidad de que ocurra uno u otro
es la suma de sus probabilidades.

<!-- b5 -->
De esas tres reglas sale una muy útil. La probabilidad de que algo no pase
es uno menos la probabilidad de que pase. ¿Qué probabilidad hay de no sacar
un seis? Uno menos un sexto: cinco sextos. Con estas piezas ya podemos
hacernos la primera pregunta interesante: ¿qué le pasa a una probabilidad
cuando recibimos información nueva?

---

# Escena 05 — ProbabilidadCondicional

**Objetivo:** construir la probabilidad condicional contando, con el dado:
saber que ocurrió B deja fuera todo lo que no es B. Llegar a la fórmula como
resumen de la cuenta, leída término a término.

**Qué hace falta saber antes:** escena 04 (espacio muestral, eventos, las tres reglas).

**Visual:**
- El dado: la cara del seis resaltada, «P(6) = 1/6».
- «Ha salido par»: las caras impares se apagan y el rectángulo se encoge
  alrededor del 2, el 4 y el 6. El «1/6» se transforma en «1/3».
- La cuenta en pantalla: «casos favorables dentro del mundo nuevo / tamaño del
  mundo nuevo» = 1/3.
- La misma cuenta con probabilidades: «(1/6) / (1/2) = 1/3».
- La fórmula construida por piezas: «P(A | B)», «=», «P(A y B)», fracción, «P(B)».
  La barra vertical se ilumina: «dado».

## Narración

<!-- b1 -->
Tiras un dado. ¿Qué probabilidad hay de que salga un seis? Un sexto: seis
caras y todas pesan lo mismo. Ahora alguien mira el dado antes que tú y te
dice una sola cosa: ha salido un número par. Te hago la misma pregunta. ¿Qué
probabilidad hay de que sea un seis? Piénsalo un momento antes de seguir.

<!-- b2 -->
La respuesta es un tercio. Lo que ha pasado es que el mundo se ha hecho más
pequeño. El uno, el tres y el cinco ya no son posibles: quedan el dos, el
cuatro y el seis. El seis sigue siendo una cara, pero ahora es una entre
tres. El dado no ha cambiado. Ha cambiado el universo dentro del cual
medimos.

<!-- b3 -->
Hagamos la misma cuenta con probabilidades, para poder repetirla en
cualquier situación. La probabilidad de que salga un seis y además sea par
es un sexto. La probabilidad de que salga par es un medio. Si dividimos un
sexto entre un medio, sale un tercio. Lo mismo que al contar.

<!-- b4 -->
Eso es la probabilidad condicional. Se escribe P de A, barra vertical, B, y
se lee: la probabilidad de A dado B. Se calcula dividiendo la probabilidad de
que ocurran A y B a la vez entre la probabilidad de B. El numerador es lo que
queda de A dentro del mundo nuevo. El denominador mide el mundo nuevo, para
que vuelva a valer uno entero.

<!-- b5 -->
Una condición: B tiene que ser posible, porque no se puede dividir entre
cero. Y fíjate en que, dándole la vuelta a la fórmula, obtenemos otra muy
útil: la probabilidad de que ocurran A y B es la probabilidad de B por la de
A dado B. Primero pasa B, y después, sabiendo eso, pasa A. La usaremos en
un minuto.

---

# Escena 06 — Independencia

**Objetivo:** definir independencia como "saber B no cambia la
probabilidad de A", y su consecuencia práctica (la probabilidad conjunta es el
producto). Un ejemplo independiente y uno que no lo es, con las cuentas.

**Qué hace falta saber antes:** escena 05 (probabilidad condicional y la regla del producto).

**Visual:**
- Un dado y una moneda. «P(6) = 1/6»; «me dicen: salió cara»; el «1/6» no cambia.
- La regla del producto de la escena 05 con P(A | B) reemplazado por P(A):
  «P(A y B) = P(A) · P(B)». Cuenta: «1/6 · 1/2 = 1/12», y una cuadrícula de 12
  casillas con una iluminada.
- El dado solo: «par» y «más de 3». «P(par) = 1/2», «P(más de 3) = 1/2»,
  «P(las dos) = 2/6 = 1/3» frente a «1/2 · 1/2 = 1/4»: una cruz roja.

## Narración

<!-- b1 -->
A veces la información nueva no cambia nada. Tiras un dado y lanzas una
moneda. Alguien te dice que la moneda ha salido cara. ¿Cambia en algo la
probabilidad de sacar un seis? No: el dado no sabe qué hizo la moneda. Sigue
siendo un sexto.

<!-- b2 -->
Cuando saber B no cambia la probabilidad de A, decimos que A y B son
independientes. Y entonces pasa algo cómodo. La regla que acabamos de ver
decía que la probabilidad de A y B es la de B por la de A dado B. Si son
independientes, la de A dado B es simplemente la de A. Así que la
probabilidad de que ocurran las dos cosas es el producto de sus
probabilidades.

<!-- b3 -->
Comprobémoslo contando. Un dado y una moneda dan doce combinaciones, todas
igual de probables. Seis con cara es solo una de ellas: un doceavo. Y un
sexto por un medio da un doceavo. Encaja.

<!-- b4 -->
Pero cuidado, porque no todo es independiente. Con un solo dado, piensa en
dos eventos: sale par, y sale más de tres. Cada uno tiene probabilidad un
medio. Si fueran independientes, que ocurran los dos valdría un cuarto. Pero
los números pares mayores que tres son el cuatro y el seis: dos de seis
caras, un tercio. No es un cuarto. Saber que salió par hace más probable que
sea grande.

<!-- b5 -->
La independencia no se supone porque sí: se comprueba o se justifica.
Cuando la tengamos, las cuentas se simplificarán muchísimo. Y cuando no la
tengamos, la probabilidad condicional nos puede dar sorpresas enormes. Vamos
a ver una que engaña a casi todo el mundo, incluidos muchos médicos.

---

# Escena 07 — TestMedico

**Objetivo:** mostrar con números que la probabilidad de A dado B no es la
de B dado A, con el test médico contado sobre mil personas. Es la motivación
de Bayes.

**Qué hace falta saber antes:** escena 05 (probabilidad condicional).

**Visual:**
- Los tres datos aparecen como tarjetas: «1 de cada 100 enfermo», «si estás
  enfermo, positivo el 99 %», «si estás sano, positivo el 5 %».
- La pregunta: «P(enfermo | positivo) = ?». Una encuesta: «99 %», «95 %», «50 %», «17 %».
- Grilla de mil personas: diez en rojo. Se reparten en dos grupos, 10 y 990.
- De las 10 enfermas, 10 con «+» (en rigor 9,9). De las 990 sanas, 49,5 ≈ 50 con «+».
- Un recuadro rodea todos los positivos (~60): dentro, 10 rojos. «10 / 60 ≈ 1/6 ≈ 17 %».
- Las dos condicionales enfrentadas: «P(+ | enfermo) = 99 %» y «P(enfermo | +) ≈ 17 %».

## Narración

<!-- b1 -->
Una enfermedad la tiene una persona de cada cien. Existe un test muy
bueno: si estás enfermo, da positivo el noventa y nueve por ciento de las
veces. Si estás sano, se equivoca y da positivo solo un cinco por ciento de
las veces. Te haces el test y da positivo. ¿Qué probabilidad hay de que
estés enfermo? Elige una respuesta antes de seguir.

<!-- b2 -->
La mayoría dice noventa y nueve, o noventa y cinco. Hagamos la cuenta con
mil personas, que es más fácil que con porcentajes. Una de cada cien está
enferma: son diez. Las otras novecientas noventa están sanas.

<!-- b3 -->
De las diez enfermas, el test detecta prácticamente a todas: diez
positivos. Ahora las sanas. El cinco por ciento de novecientas noventa es
casi cincuenta. Cincuenta personas sanas que reciben un positivo. En total,
unos sesenta positivos.

<!-- b4 -->
Y de esos sesenta, solo diez están enfermos. Diez entre sesenta es un
sexto: más o menos un diecisiete por ciento. Con un test que acierta el
noventa y nueve por ciento de las veces, un positivo significa que lo más
probable es que estés sano. La razón es que hay tantísimos más sanos que
sus pocos errores superan a todos los enfermos juntos.

<!-- b5 -->
El noventa y nueve por ciento era la probabilidad de dar positivo dado que
estás enfermo. Lo que tú querías saber era la probabilidad de estar enfermo
dado que has dado positivo. Son preguntas distintas, con respuestas muy
distintas. Contar personas funciona, pero no siempre tendremos mil personas
que contar. Necesitamos una fórmula que le dé la vuelta a la pregunta.

---

# Escena 08 — Bayes

**Objetivo:** deducir la regla de Bayes en dos pasos a partir de la regla del
producto, nombrar sus piezas (a priori, verosimilitud, a posteriori), llegar a
la ley de probabilidad total como el denominador, y aplicarla al canal que
confunde bits. Sembrar la decisión óptima de los capítulos 9 y 13.

**Qué hace falta saber antes:** escenas 05 (regla del producto) y 07 (el test).

**Visual:**
- Deducción en tres renglones: «P(A y B) = P(A | B) · P(B)» y
  «P(A y B) = P(B | A) · P(A)»; se igualan; se despeja P(A | B).
- Etiquetas bajo cada pieza: «a priori» (antes de mirar), «verosimilitud»,
  «a posteriori» (después de mirar).
- Árbol de dos niveles para el denominador: enfermo / sano, y cada rama con + y −.
  Se iluminan las dos ramas que acaban en «+» y se suman.
- El canal: un emisor envía «0» (70 %) o «1» (30 %); en el cable, un rayo que
  cambia el bit el 10 % de las veces. Árbol: 0,3 · 0,9 = 0,27; 0,7 · 0,1 = 0,07;
  suma 0,34; cociente 0,27 / 0,34 ≈ 0,79.

## Narración

<!-- b1 -->
La fórmula sale de algo que ya tenemos. La probabilidad de que ocurran A y
B se puede escribir de dos maneras: primero B y después A dado B, o primero
A y después B dado A. Las dos dan lo mismo, porque es el mismo suceso. Así
que igualamos las dos expresiones y despejamos la probabilidad de A dado B.

<!-- b2 -->
Queda así: la probabilidad de A dado B es la probabilidad de B dado A, por
la probabilidad de A, dividida entre la probabilidad de B. Esta es la regla
de Bayes. Cada pieza tiene nombre. La probabilidad de A sola se llama a
priori: lo que creías antes de mirar. La de B dado A es la verosimilitud: lo
compatible que es lo que viste con A. Y el resultado, la probabilidad a
posteriori: lo que crees después de mirar.

<!-- b3 -->
Falta el denominador, la probabilidad de B. En el test, ¿de cuántas formas
se puede dar positivo? Estando enfermo o estando sano. Cada camino vale su
probabilidad por la probabilidad de dar positivo por ese camino, y se
suman. Eso se llama ley de probabilidad total: partes el mundo en casos que
no se solapan, calculas cada caso, y sumas.

<!-- b4 -->
Ahora un ejemplo de señales. Un emisor envía ceros y unos: un cero el
setenta por ciento de las veces, un uno el treinta. El cable tiene ruido y
cambia el bit un diez por ciento de las veces. Llega un uno. ¿Qué
probabilidad hay de que se enviara un uno?

<!-- b5 -->
Hay dos caminos para recibir un uno. Por el primero: se envió un uno y
llegó bien, cero coma tres por cero coma nueve, cero coma veintisiete. Por el
otro: se envió un cero y el ruido lo cambió, cero coma siete por cero coma
uno, cero coma cero siete.

<!-- b6 -->
La probabilidad de recibir un uno es la suma: cero coma treinta y cuatro. Y
Bayes dice que la probabilidad de que se enviara un uno es cero coma
veintisiete entre cero coma treinta y cuatro: casi un ochenta por ciento.
Así que, si tuvieras que apostar, dirías que se envió un uno. Elegir la
explicación más probable después de mirar es, exactamente, lo que haremos
para detectar señales dentro de unos capítulos.

---

# Escena 09 — VariableAleatoria

**Objetivo:** presentar la variable aleatoria como una regla que le pone un
número a cada resultado; distinguir la variable (X mayúscula) del valor (x
minúscula); separar discretas y continuas.

**Qué hace falta saber antes:** escena 04 (espacio muestral).

**Visual:**
- Una moneda con «cara» y «cruz»; flechas que van a «1» y «0» en una recta.
- El dado: flechas desde las caras a 1…6. Otra regla distinta sobre el mismo dado:
  «vale 1 si sale par, 0 si no»: el mismo experimento, otra variable.
- «X» grande en ámbar (la regla) y «x» pequeña sobre la recta (un valor).
  Aparece «X = 4»: «el experimento salió y la variable valió 4».
- Dos columnas: discreta (puntos sueltos, se pueden contar) y continua (un tramo lleno,
  la tensión en un cable).

## Narración

<!-- b1 -->
Los resultados de un experimento no siempre son números. Una moneda da cara
o cruz. Un paciente está sano o enfermo. Para poder hacer cuentas
necesitamos una regla que le ponga un número a cada resultado. Esa regla se
llama variable aleatoria. Por ejemplo: cara vale uno y cruz vale cero.

<!-- b2 -->
Sobre un mismo experimento se pueden definir muchas variables. Con el
dado, una variable puede ser el número que sale. Otra, que valga uno si sale
par y cero si sale impar. El experimento es el mismo; lo que cambia es la
pregunta que le hacemos. Por eso una variable aleatoria no es el dado: es
una forma de leerlo.

<!-- b3 -->
Una cuestión de notación que se usa en todo el curso. La equis mayúscula es
la variable: la regla, el experimento que todavía no ha ocurrido. La equis
minúscula es un número concreto, uno de los valores posibles. Cuando
escribimos equis mayúscula igual a cuatro, estamos diciendo: el experimento
ha salido, y la variable ha valido cuatro.

<!-- b4 -->
Algunas variables toman valores que se pueden contar uno a uno: las caras
de un dado, los bits de un mensaje. Se llaman discretas. Otras pueden tomar
cualquier valor dentro de un intervalo: la tensión en un cable, la
temperatura. Se llaman continuas. En señales aparecen las dos, y necesitamos
una forma de describir cualquiera de ellas con la misma herramienta.

---

# Escena 10 — Acumulada

**Objetivo:** construir la función de distribución acumulada con el dado,
calculando su valor en varios puntos a mano; ver la escalera, la versión
continua y la mixta; y deducir la regla del intervalo.

**Qué hace falta saber antes:** escenas 04 y 09.

**Visual:**
- Ejes. Un cursor vertical en x = 0,5: «P(X ≤ 0,5) = 0». Se mueve a 1: «1/6».
  A 2,5: «2/6». A 6: «1». A 10: «1». Cada valor deja un punto.
- Los puntos se unen en una escalera de seis peldaños.
- Continua: una curva en forma de ese de 0 a 1. Mixta: la curva con un salto.
- Dos cursores en a = 2 y b = 5 sobre la escalera: «F(5) − F(2) = 5/6 − 2/6 = 3/6».
  Se iluminan las caras 3, 4 y 5.

## Narración

<!-- b1 -->
Vamos a construir una curva que describe cualquier variable aleatoria. La
idea es hacerse siempre la misma pregunta: ¿qué probabilidad hay de que la
variable salga menor o igual que un número dado? Hagámoslo con el dado. ¿Qué
probabilidad hay de sacar menos de cero coma cinco? Ninguna: cero.

<!-- b2 -->
¿Y de sacar uno o menos? Solo vale el uno: un sexto. ¿Dos coma cinco o
menos? El uno y el dos: dos sextos. ¿Seis o menos? Todas las caras: uno. ¿Y
diez o menos? También uno, porque ya no hay más caras que sumar. Si
dibujamos todas estas respuestas, sale una escalera, con un peldaño de un
sexto en cada cara.

<!-- b3 -->
Esa curva se llama función de distribución acumulada. Se escribe efe
mayúscula sub equis de equis, y es la probabilidad de que la variable no
pase de equis. En una variable continua no hay peldaños: sube suave de cero
a uno. Y a veces es una mezcla: una curva suave con un salto, como un
sensor que a veces se satura y devuelve siempre el mismo valor.

<!-- b4 -->
Hay dos cosas que se cumplen siempre. La acumulada nunca baja: si la
variable no pasa de tres, tampoco pasa de cuatro, así que la segunda
probabilidad es por lo menos la primera. Y empieza en cero y termina en uno:
muy a la izquierda no hay nada, y muy a la derecha está todo.

<!-- b5 -->
Y de regalo, una regla práctica. ¿Qué probabilidad hay de que el dado caiga
entre dos y cinco, sin incluir el dos? Es lo acumulado hasta cinco, cinco
sextos, menos lo acumulado hasta dos, dos sextos: tres sextos. Las caras
tres, cuatro y cinco. En general: la probabilidad de caer entre a y b es la
acumulada en b menos la acumulada en a.

---

# Escena 11 — Densidad

**Objetivo:** presentar la densidad como la pendiente de la acumulada
(explicando qué es una derivada) y la probabilidad de un intervalo como área
bajo la densidad (explicando qué es una integral). Llegar a ella también
desde el histograma. Deducir sus dos propiedades.

**Qué hace falta saber antes:** escena 10 (acumulada).

**Visual:**
- La acumulada continua; una recta tangente que la recorre. Donde la curva sube
  deprisa, la recta se empina. Debajo se dibuja la altura de esa pendiente: la campana.
- Rótulo breve: «derivada = pendiente».
- Un histograma: mediciones de una tensión con ruido que caen en columnas.
  Con 100, irregular; con 10.000, suave, y la campana se superpone.
- El área entre a y b se rellena con rectángulos finos que se funden en una
  sola área: «integral = área». «P(a < X ≤ b) = área».
- Las dos propiedades: la campana nunca por debajo del eje; el área total «= 1».

## Narración

<!-- b1 -->
Mira la acumulada de una variable continua y fíjate en dónde sube deprisa
y dónde apenas se mueve. Donde sube deprisa se acumula mucha probabilidad
en poco espacio: son los valores que más salen. Lo rápido que sube una curva
en cada punto es su pendiente, y en matemáticas se llama derivada.

<!-- b2 -->
Si dibujamos la pendiente de la acumulada en cada punto, aparece una curva
nueva: la función de densidad de probabilidad, efe minúscula sub equis de
equis. Es alta donde la acumulada sube deprisa, y baja donde sube despacio.
La densidad nos dice, de un vistazo, dónde se concentran los valores.

<!-- b3 -->
Hay otra forma de llegar a la misma curva, más física. Mide una tensión con
ruido muchas veces y apila cada medida en una columna según su valor. Con
cien medidas, sale un dibujo irregular. Con diez mil, las columnas dibujan
una forma suave. Esa forma es la densidad: donde es alta caen muchas
medidas, y donde es baja, casi ninguna.

<!-- b4 -->
¿Y cómo se calcula ahora la probabilidad de caer entre a y b? Es el área
bajo la densidad entre a y b. Imagina el área cortada en rectángulos muy
finos y sumados: esa suma, cuando los rectángulos se hacen infinitamente
finos, se llama integral. Así que la probabilidad de un intervalo es la
integral de la densidad entre a y b.

<!-- b5 -->
Las dos propiedades de la acumulada se traducen solas. Como la acumulada
nunca baja, su pendiente nunca es negativa: la densidad siempre está por
encima del eje. Y como la acumulada va de cero a uno, el área total bajo la
densidad vale exactamente uno. Ojo con un detalle: la densidad no es una
probabilidad. Una probabilidad es siempre un área.

---

# Escena 12 — DistribucionesClave

**Objetivo:** presentar las distribuciones que vuelven en toda la materia,
cada una con su dibujo, sus parámetros y dónde aparece en señales: Bernoulli
(discreta), uniforme y gaussiana (continuas).

**Qué hace falta saber antes:** escena 11 (densidad, área = probabilidad);
escena 10 (la escalera de las discretas).

**Visual:**
- Bernoulli: dos barras, «0» con altura 1 − p y «1» con altura p. Un bit que llega.
- Uniforme en [a, b]: un rectángulo plano. Su altura se calcula en pantalla:
  «ancho · alto = 1 → alto = 1/(b − a)».
- Gaussiana: la campana. Un deslizador mueve «μ» (la campana se traslada) y otro
  «σ» (la campana se ensancha y se aplana, conservando área 1).
- Una tira con aplicaciones: bit (Bernoulli), fase y error de redondeo (uniforme),
  ruido de un circuito (gaussiana).

## Narración

<!-- b1 -->
Hay unas pocas distribuciones que vamos a encontrarnos todo el tiempo, así
que conviene conocerlas por su nombre. La más sencilla es discreta: la de
Bernoulli. La variable solo puede valer cero o uno, como un bit. Vale uno
con probabilidad pe, y cero con probabilidad uno menos pe. Su dibujo son dos
barras.

<!-- b2 -->
La primera continua es la uniforme: todos los valores de un intervalo,
entre a y b, son igual de probables. Su densidad es un rectángulo plano. ¿Qué
altura tiene? El área total tiene que ser uno, y el área de un rectángulo es
ancho por alto. Así que el alto es uno dividido entre el ancho, b menos a.
Aparece cuando algo puede caer en cualquier sitio, como el error al
redondear una señal.

<!-- b3 -->
Y la reina de todas: la gaussiana, o campana de Gauss. Tiene dos
parámetros. Mu dice dónde está el centro: si cambias mu, la campana se
desplaza sin deformarse. Sigma dice lo ancha que es: si aumentas sigma, la
campana se ensancha y se aplana, porque el área tiene que seguir valiendo
uno.

<!-- b4 -->
¿Por qué es tan importante? Porque cuando se suman muchos efectos pequeños
e independientes, el resultado tiende a tener forma de campana, sea cual sea
la forma de cada efecto. Y el ruido de un circuito es justamente eso: la
suma de millones de electrones moviéndose al azar. Por eso casi todo el ruido
de esta materia será gaussiano.

<!-- b5 -->
Una curva describe una variable por completo. Pero muchas veces no conocemos
la curva entera, o es demasiada información para trabajar con ella. En el
próximo paso vamos a resumir cualquier distribución en solo dos números. Y
vamos a descubrir que, sorprendentemente, esos dos números alcanzan para
mucho.

---

# Escena 13 — Esperanza

**Objetivo:** construir la esperanza con el dado (media 3,5 calculada a
mano), interpretarla como punto de equilibrio, pasar a la integral para las
continuas, y mostrar la linealidad con un ejemplo.

**Qué hace falta saber antes:** escenas 09 a 11 (variable, densidad, integral como área).

**Visual:**
- Un contador que promedia tiradas de dado: 4, 2, 6, 1, 5… el promedio va hacia «3,5».
- La cuenta: «1·(1/6) + 2·(1/6) + … + 6·(1/6) = 21/6 = 3,5», término a término.
- Seis pesas iguales sobre una regla en 1…6: el filo de equilibrio en 3,5.
- La densidad recortada como una placa sobre un filo que se mueve hasta el
  equilibrio: «μ». La fórmula por piezas: «E[X] =», «∫», «x», «f_X(x) dx».
- Linealidad: «E[2X + 1] = 2·3,5 + 1 = 8».

## Narración

<!-- b1 -->
Tira un dado muchas veces y ve haciendo el promedio de lo que sale. Al
principio salta, pero enseguida se estabiliza alrededor de un número: tres
coma cinco. Fíjate en que el dado nunca saca tres coma cinco. Es el valor
alrededor del cual se reparten los resultados. Se llama media, o esperanza.

<!-- b2 -->
Se puede calcular sin tirar el dado. Cada valor se multiplica por su
probabilidad, y se suma todo. Uno por un sexto, más dos por un sexto, y así
hasta seis por un sexto. Uno más dos más tres más cuatro más cinco más seis
son veintiuno, y veintiuno entre seis da tres coma cinco. En general, la
esperanza es la suma de cada valor por su probabilidad.

<!-- b3 -->
Tiene una imagen física muy clara. Pon seis pesas iguales sobre una regla,
en las posiciones del uno al seis. ¿Dónde tienes que apoyarla para que no
caiga? En tres coma cinco. La esperanza es el punto de equilibrio de la
distribución. Si la variable es continua, se recorta la densidad como una
placa, y el punto de equilibrio se calcula con una integral: equis por la
densidad, sumado a lo largo de todo el eje.

<!-- b4 -->
Se escribe E de equis, o mu. Y tiene una propiedad que usaremos sin parar:
es lineal. Si multiplicas la variable por un número, la esperanza se
multiplica por ese número. Si le sumas algo, la esperanza sube lo mismo. La
esperanza de dos veces el dado más uno es dos por tres coma cinco más uno:
ocho. Y la esperanza de una suma es la suma de las esperanzas, siempre.

<!-- b5 -->
Pero la media no lo cuenta todo. Un dado y una variable que siempre vale
tres coma cinco tienen la misma media, y no se parecen en nada: una salta
de uno a seis y la otra no se mueve. Nos falta un segundo número que diga
cuánto se aleja la variable de su media.

---

# Escena 14 — Varianza

**Objetivo:** definir la varianza como el promedio de la distancia a la media
al cuadrado (explicando por qué al cuadrado), calcularla para el dado, deducir
paso a paso la fórmula práctica, y dar el resultado de la uniforme.

**Qué hace falta saber antes:** escena 13 (esperanza, linealidad).

**Visual:**
- Dos campanas con la misma media: una estrecha y otra ancha.
- Las distancias del dado a 3,5: «−2,5, −1,5, −0,5, 0,5, 1,5, 2,5». Sumadas dan
  0 (se cancelan). Al cuadrado: «6,25, 2,25, 0,25, 0,25, 2,25, 6,25»; promedio «≈ 2,92».
- «σ² ≈ 2,92», «σ ≈ 1,71». Flechas de ± σ alrededor de 3,5.
- La deducción en cuatro renglones, cada uno con la regla usada al margen:
  «E[(X − μ)²]» → «E[X² − 2μX + μ²]» (desarrollar el cuadrado) →
  «E[X²] − 2μE[X] + μ²» (linealidad) → «E[X²] − μ²» (E[X] = μ).
- Comprobación con el dado: «91/6 − 3,5² ≈ 15,17 − 12,25 = 2,92». Uniforme: «(b − a)²/12».

## Narración

<!-- b1 -->
Queremos medir cuánto se aleja una variable de su media. La primera idea es
promediar las distancias a la media. Con el dado, las distancias a tres
coma cinco son menos dos coma cinco, menos uno coma cinco, menos cero coma
cinco, y las mismas en positivo. Súmalas: dan cero. Las de un lado cancelan
a las del otro. Así no sirve.

<!-- b2 -->
La solución es elevar cada distancia al cuadrado, para que todas sean
positivas. Seis coma veinticinco, dos coma veinticinco, cero coma
veinticinco, y lo mismo por el otro lado. Su promedio es dos coma noventa y
dos. Eso es la varianza: la esperanza de la distancia a la media, al
cuadrado. Se escribe sigma cuadrado.

<!-- b3 -->
El problema de la varianza es que está en unidades al cuadrado: si la
variable son voltios, la varianza son voltios al cuadrado. Por eso se usa
también su raíz, sigma, que se llama desviación estándar y vuelve a estar en
las unidades de la variable. Para el dado, uno coma siete uno: los
resultados se alejan de tres coma cinco, típicamente, algo menos de dos
puntos.

<!-- b4 -->
Hay una forma más cómoda de calcularla, y vale la pena ver de dónde sale.
Primero desarrollamos el cuadrado: equis al cuadrado, menos dos mu equis,
más mu al cuadrado. Después usamos la linealidad para repartir la esperanza
en cada término. Como la esperanza de equis es mu, el término del medio
queda menos dos mu al cuadrado. Y al juntar todo: la varianza es la
esperanza de equis al cuadrado menos mu al cuadrado.

<!-- b5 -->
Comprobémoslo con el dado. La esperanza del cuadrado es uno más cuatro más
nueve más dieciséis más veinticinco más treinta y seis, entre seis: quince
coma diecisiete. Menos tres coma cinco al cuadrado, doce coma veinticinco.
Da dos coma noventa y dos, lo mismo que antes. Y un resultado que usaremos:
para una uniforme entre a y b, la varianza es el ancho al cuadrado dividido
entre doce.

---

# Escena 15 — Chebyshev

**Objetivo:** llegar a la desigualdad de Chebyshev en dos pasos (Markov
primero, con un ejemplo de sueldos y su razonamiento), entender que es
universal y por eso floja, y verla puesta a prueba con números.

**Qué hace falta saber antes:** escenas 13 y 14 (media, varianza, desviación estándar).

**Visual:**
- Markov: una balanza con la media «1.000 €»; si el 20 % cobrara 10.000 €,
  la media subiría al menos a «2.000 €»: imposible. Queda «como mucho 10 %».
- La desigualdad de Markov por piezas: «P(Y ≥ a) ≤ E[Y] / a».
- El truco: «Y = (X − μ)²», con media «σ²». Se sustituye y aparece Chebyshev:
  «P(|X − μ| ≥ α σ) ≤ 1/α²».
- Tabla que se llena: «α = 2 → ≤ 25 %», «α = 3 → ≤ 11 %»; y la prueba con la
  uniforme: «α = 1,5: cota 0,444, real 0,134».

## Narración

<!-- b1 -->
Empecemos con una pregunta de sueldos. En una empresa el sueldo medio es de
mil euros, y nadie cobra un sueldo negativo. ¿Qué fracción de la plantilla
puede cobrar diez mil euros o más? Piénsalo así: si el veinte por ciento
cobrara diez mil, solo ellos ya harían que la media fuera de dos mil. Como
mucho, puede ser un diez por ciento.

<!-- b2 -->
Eso es la desigualdad de Markov. Si una variable nunca es negativa, la
probabilidad de que supere un valor a es, como mucho, su media dividida
entre a. Una variable que no puede ser negativa y que tiene una media
pequeña no puede tomar valores grandes muy a menudo.

<!-- b3 -->
Chebyshev tuvo una idea muy simple: aplicar Markov a la distancia a la
media, elevada al cuadrado. Esa cantidad nunca es negativa, y su media es,
por definición, la varianza. Con eso, la cuenta sale en dos líneas: la
probabilidad de alejarse de la media más de alfa desviaciones estándar es,
como mucho, uno dividido entre alfa al cuadrado.

<!-- b4 -->
Con alfa igual a dos: como mucho el veinticinco por ciento de las veces la
variable cae a más de dos sigmas de su media. Con alfa igual a tres, como
mucho un once por ciento. Y esto vale para cualquier distribución, tenga la
forma que tenga. Solo hacen falta la media y la varianza.

<!-- b5 -->
El precio de valer para todo es que suele quedarse corta. Para una uniforme
entre cero y uno, con alfa igual a uno coma cinco, Chebyshev asegura que la
probabilidad no pasa de cero coma cuatro cuatro. La real es cero coma uno
tres: más de tres veces menos. Pero justamente porque no necesita conocer la
curva, sirve para demostrar algo que usamos todos los días sin pensarlo: que
promediar funciona.

---

# Escena 16 — GrandesNumeros

**Objetivo:** mostrar que la varianza del promedio de n medidas
independientes es sigma cuadrado sobre n (usando que las varianzas de
independientes se suman, con la promesa de demostrarlo en la escena 24), y
aplicar Chebyshev para llegar a la ley de los grandes números. Sembrar el
capítulo 10.

**Qué hace falta saber antes:** escenas 14 y 15 (varianza, Chebyshev); escena 06 (independencia).

**Visual:**
- Tres corridas del promedio de medidas con ruido que empiezan saltando y se
  estabilizan cerca del valor verdadero (como `c7p-lln-chebyshev.svg`).
- La cuenta de la varianza del promedio en tres renglones: suma de n medidas →
  varianza n·σ² → dividir entre n (al cuadrado: n²) → «σ²/n». Con una etiqueta
  «(lo demostramos en el episodio 6)» junto a «las varianzas se suman».
- Chebyshev aplicado al promedio: «P(|X̄ₙ − μ| ≥ ε) ≤ σ² / (n ε²)», y una flecha «→ 0».
- Una banda ámbar alrededor de μ que se angosta al crecer n.

## Narración

<!-- b1 -->
Mide la misma tensión con ruido muchas veces y haz el promedio. Con dos
medidas, el promedio todavía salta bastante. Con cien, se mueve poco. Con
diez mil, apenas tiembla alrededor del valor verdadero. Todos lo hemos
visto. Vamos a demostrarlo, con lo que ya tenemos.

<!-- b2 -->
Primero, cuánto se dispersa el promedio. Si las medidas son
independientes, la varianza de su suma es la suma de sus varianzas. Esto lo
demostraremos dentro de dos episodios; de momento, créetelo. Con n medidas
de varianza sigma cuadrado, la suma tiene varianza n por sigma cuadrado.

<!-- b3 -->
El promedio es la suma dividida entre n. Y cuando divides una variable
entre un número, la varianza se divide entre ese número al cuadrado, porque
la varianza mide distancias al cuadrado. Así que la varianza del promedio es
n por sigma cuadrado dividido entre n al cuadrado: sigma cuadrado dividido
entre n. Cuantas más medidas, menos se dispersa el promedio.

<!-- b4 -->
Ahora le aplicamos Chebyshev al promedio. La probabilidad de que se aleje
de la media verdadera más de una distancia épsilon, tan pequeña como
quieras, es como mucho sigma cuadrado dividido entre n por épsilon al
cuadrado. Y cuando n crece, eso se va a cero. Es la ley de los grandes
números: el promedio acaba pegándose a la media.

<!-- b5 -->
No hemos necesitado saber nada de la forma del ruido: solo su varianza.
Esta idea volverá con fuerza cuando estudiemos señales que cambian en el
tiempo, donde promediaremos a lo largo de una sola grabación. Y ahora
pasamos a lo más interesante: en señales nunca hay una sola variable. Está
lo que se envió y lo que se recibió.

---

# Escena 17 — TablaConjunta

**Objetivo:** presentar dos variables a la vez con el canal de bits de la
escena 08 convertido en una tabla conjunta de cuatro casillas; sacar las
marginales sumando filas y columnas; y leer una condicional de la tabla.

**Qué hace falta saber antes:** escena 08 (el canal), escena 05 (condicional), escena 04 (reglas).

**Visual:**
- El canal de la escena 08 (mismo dibujo). Se construye una tabla 2 × 2: filas
  «enviado 0 / 1», columnas «recibido 0 / 1».
- Cada casilla se calcula con la regla del producto: «0,7·0,9 = 0,63»,
  «0,7·0,1 = 0,07», «0,3·0,1 = 0,03», «0,3·0,9 = 0,27». Las cuatro suman «1».
- Suma de cada fila a la derecha: «0,7», «0,3» (lo enviado). Suma de cada
  columna abajo: «0,66», «0,34» (lo recibido). Rótulo: «marginales».
- Una columna iluminada (recibido 1): «0,27 / 0,34 ≈ 0,79». Es el mismo número de Bayes.

## Narración

<!-- b1 -->
Volvamos al canal que confunde bits. Llamemos ese a lo que se envió, y erre a
lo que se recibió. Ahora nos interesan las dos variables a la vez: qué pareja
sale cada vez. Hay cuatro parejas posibles, y podemos poner sus
probabilidades en una tabla: filas para lo enviado, columnas para lo
recibido.

<!-- b2 -->
Cada casilla se calcula con la regla del producto. Enviar un cero y recibir
un cero: cero coma siete por cero coma nueve, cero coma sesenta y tres.
Enviar un cero y recibir un uno: cero coma siete por cero coma uno, cero coma
cero siete. Enviar un uno y recibir un cero: cero coma cero tres. Y enviar
un uno y recibir un uno: cero coma veintisiete. Las cuatro juntas suman uno.

<!-- b3 -->
Esta tabla se llama distribución conjunta, y contiene todo. Por ejemplo, si
solo te importa lo que se envió, suma cada fila: cero coma siete y cero coma
tres, las probabilidades de partida. Si solo te importa lo recibido, suma
cada columna: cero coma sesenta y seis y cero coma treinta y cuatro. A estas
sumas, que se escriben en los márgenes de la tabla, se les llama marginales.

<!-- b4 -->
Y también salen las condicionales. Si sabes que se recibió un uno, te
quedas solo con esa columna: el mundo se achica, como con el dado. Dentro de
la columna, el uno enviado pesa cero coma veintisiete de un total de cero
coma treinta y cuatro: cero coma setenta y nueve. Es el mismo número que nos
dio Bayes, ahora leído directamente de la tabla.

<!-- b5 -->
Un detalle importante: de la tabla conjunta siempre puedes sacar las
marginales, sumando. Pero al revés, no: sabiendo solo cuánto se envía y
cuánto se recibe, no sabes cómo se relacionan. Esa relación es justamente lo
que nos interesa. Y cuando las variables son continuas, la tabla se
convierte en otra cosa.

---

# Escena 18 — DensidadConjunta

**Objetivo:** pasar de la tabla a las variables continuas: la nube de
puntos, la densidad conjunta como una colina, la probabilidad de una región
como un volumen, y las marginales como la colina aplastada contra un eje.

**Qué hace falta saber antes:** escena 17 (tabla conjunta, marginales); escena 11 (densidad, integral).

**Visual:**
- Pares (X, Y) que caen como puntos: X lo enviado (una tensión), Y lo recibido
  (X más ruido). La nube se alarga en diagonal.
- La tabla de la escena 17 se transforma en una cuadrícula cada vez más fina, y
  las casillas en columnas de altura variable: una colina.
- Una región del plano sombreada: «P((X, Y) ∈ R)» = volumen encima.
- La colina se aplasta contra el eje horizontal: aparece la densidad de X; contra
  el vertical, la de Y. Rótulo: «sumar filas → integrar».
- El centro de masa de la nube: «(E[X], E[Y])».

## Narración

<!-- b1 -->
Ahora lo que se envía no es un bit, sino una tensión cualquiera, equis. Y lo
que se recibe, i griega, es esa tensión más un ruido. Cada envío da una
pareja de números, que es un punto en el plano. Repitiendo muchas veces,
aparece una nube alargada: cuando se envía más, suele recibirse más, pero
con dispersión.

<!-- b2 -->
Ya no hay cuatro casillas: hay infinitas parejas posibles. Imagina la tabla
cada vez más fina, con casillas más y más pequeñas. En el límite, en lugar
de números en casillas, tenemos una superficie sobre el plano, como una
colina. Es alta donde caen muchos puntos y baja donde caen pocos. Se llama
densidad conjunta, efe sub equis i griega.

<!-- b3 -->
Con una variable, la probabilidad era un área bajo una curva. Ahora es un
volumen bajo la colina: la probabilidad de que la pareja caiga en una
región del plano es el volumen de colina que hay encima de esa región. Se
calcula con una integral doble, que es sumar a lo largo de los dos ejes. Y
el volumen total vuelve a valer uno.

<!-- b4 -->
Las marginales se sacan igual que en la tabla. Allí sumábamos cada fila;
aquí, para cada valor de equis, sumamos toda la colina a lo largo de i
griega, es decir, integramos. Es como aplastar la colina contra el eje de
las equis: lo que queda es la densidad de equis sola. Y aplastando contra el
otro eje, la de i griega.

<!-- b5 -->
La nube también tiene su punto de equilibrio: el centro de masa, con la
media de equis en un eje y la media de i griega en el otro. Pero lo más
interesante no es el centro: es qué pasa dentro de la nube cuando ya sabes
cuánto vale una de las dos variables.

---

# Escena 19 — EsperanzaCondicional

**Objetivo:** presentar la esperanza condicional con la tabla (dos números)
y con la nube (una curva), entender que es una variable aleatoria, y llegar
a la propiedad de la torre comprobándola con la tabla y con el ejemplo de la
altura.

**Qué hace falta saber antes:** escenas 17 y 18 (tabla, nube); escena 13 (esperanza).

**Visual:**
- La tabla del canal. Columna «recibido 1»: «E[S | R = 1] = 0,79». Columna
  «recibido 0»: «E[S | R = 0] = 0,03/0,66 ≈ 0,045».
- La torre con la tabla: «0,34 · 0,79 + 0,66 · 0,045 ≈ 0,27 + 0,03 = 0,30 = E[S]».
- La nube cortada en rebanadas verticales; en cada una, un punto en su centro.
  Los puntos forman una curva: «g(x) = E[Y | X = x]».
- Dos campanas de alturas: hombres (175 cm, 40 %), mujeres (162 cm, 60 %).
  «0,4 · 175 + 0,6 · 162 = 70 + 97,2 = 167,2».
- La fórmula por piezas: «E[X] = E[ E[X | Y] ]».

## Narración

<!-- b1 -->
En la tabla del canal, fíjate solo en la columna de recibir un uno. Dentro
de esa columna, lo enviado vale uno con probabilidad cero coma setenta y
nueve. Así que, sabiendo que se recibió un uno, la media de lo enviado es
cero coma setenta y nueve. Es la esperanza condicional: la media de una
variable dentro del mundo achicado por lo que sabemos.

<!-- b2 -->
Si se recibió un cero, la columna es otra, y la media de lo enviado es
mucho más pequeña: cero coma cero cuatro cinco. Dos respuestas distintas,
según lo que se reciba. Y como lo que se recibe es aleatorio, la esperanza
condicional es, a su vez, una variable aleatoria: un número que depende de
lo que salga.

<!-- b3 -->
Ahora hagamos el promedio de esos promedios, cada uno pesado por lo
probable que es su columna. Cero coma treinta y cuatro por cero coma setenta
y nueve, más cero coma sesenta y seis por cero coma cero cuatro cinco. Da cero
coma tres. ¡Es exactamente la media de lo enviado! Promediar por grupos y
después promediar los grupos da lo mismo que promediar todo de golpe. Se
llama propiedad de la torre.

<!-- b4 -->
Con la nube pasa lo mismo, en continuo. Corta la nube en rebanadas finas,
una para cada valor de equis, y marca el centro de cada rebanada. Esos
centros forman una curva: la esperanza de i griega dado equis. Es, rebanada
a rebanada, lo que cabe esperar de lo recibido sabiendo lo que se envió.

<!-- b5 -->
Un ejemplo cotidiano de la torre. En una población, el cuarenta por ciento
son hombres, con una altura media de ciento setenta y cinco centímetros, y
el sesenta por ciento son mujeres, con ciento sesenta y dos. La altura media
de todos es cero coma cuatro por ciento setenta y cinco más cero coma seis
por ciento sesenta y dos: ciento sesenta y siete coma dos. Y con la varianza
pasa algo todavía más bonito.

---

# Escena 20 — VarianzaTotal

**Objetivo:** partir la varianza de la altura en dos trozos con números
(dentro de los grupos y entre los grupos), enunciar la ley de la varianza
total y leerla como "lo que el grupo explica y lo que no". Sembrar el error
del mejor estimador del capítulo 8.

**Qué hace falta saber antes:** escena 19 (torre, altura); escena 14 (varianza).

**Visual:**
- Las dos campanas de la altura, con sus anchos: «σ_H = 7 cm», «σ_M = 6 cm».
- Primer trozo: «0,4 · 7² + 0,6 · 6² = 19,6 + 21,6 = 41,2» (dispersión dentro de cada grupo).
- Segundo trozo: las dos medias como puntos alrededor de 167,2; distancias al
  cuadrado: «0,4 · 7,8² + 0,6 · 5,2² = 24,34 + 16,22 = 40,56».
- Dos barras apiladas: «41,2 + 40,56 = 81,76»; «σ ≈ 9 cm».
- La ley por piezas: «Var(X) = E[Var(X | Y)] + Var(E[X | Y])», con rótulos
  «lo que no explica el grupo» y «lo que explica el grupo».

## Narración

<!-- b1 -->
Las alturas varían por dos motivos distintos. Uno: dentro de cada grupo
hay gente más alta y más baja. Digamos que la desviación estándar es de siete
centímetros en los hombres y de seis en las mujeres. Dos: los grupos tienen
medias distintas, ciento setenta y cinco y ciento sesenta y dos. ¿Cuánto
aporta cada motivo a la varianza total?

<!-- b2 -->
El primer trozo es la varianza dentro de cada grupo, promediada con los
pesos de los grupos. Cero coma cuatro por siete al cuadrado, diecinueve coma
seis. Más cero coma seis por seis al cuadrado, veintiuno coma seis. En
total, cuarenta y uno coma dos.

<!-- b3 -->
El segundo trozo es cuánto se dispersan las medias de los grupos alrededor
de la media total. La media de los hombres está a siete coma ocho
centímetros de ciento sesenta y siete coma dos, y la de las mujeres, a cinco
coma dos. Al cuadrado y con sus pesos: veinticuatro coma treinta y cuatro más
dieciséis coma veintidós. Cuarenta coma cinco seis.

<!-- b4 -->
La varianza total de la altura es la suma de los dos trozos: ochenta y uno
coma setenta y seis, una desviación estándar de unos nueve centímetros. Casi
mitad y mitad. Esto es la ley de la varianza total: la varianza de una
variable es la media de las varianzas dentro de los grupos, más la varianza
de las medias de los grupos.

<!-- b5 -->
Léelo de otra forma. El segundo trozo es lo que saber el grupo explica de
la altura. El primero es lo que sigue sin saberse aunque conozcas el grupo.
Guarda esta idea, porque volverá: cuando intentemos adivinar una variable a
partir de otra, el error que cometeremos, incluso haciéndolo lo mejor
posible, será exactamente ese primer trozo.

---

# Escena 21 — Correlacion

**Objetivo:** presentar la correlación (esperanza del producto) como una
forma de medir la inclinación de la nube, calcularla con la tabla del canal,
y advertir que no es el producto de las esperanzas.

**Qué hace falta saber antes:** escenas 17 y 18 (tabla, nube); escena 13 (esperanza).

**Visual:**
- La nube inclinada; en cada punto aparece el producto x · y.
- La tabla del canal: solo la casilla (1, 1) tiene producto distinto de cero:
  «1 · 1 · 0,27». «E[SR] = 0,27».
- Frente a frente: «E[SR] = 0,27» y «E[S] · E[R] = 0,3 · 0,34 = 0,102». Un «≠».
- La fórmula por piezas: «r_XY = E[XY]», y la versión continua con la integral doble.

## Narración

<!-- b1 -->
¿Cómo medimos si dos variables tienden a moverse juntas? Una idea
sencilla: multiplicar equis por i griega en cada caso y promediar. Si cuando
una es grande la otra también lo es, los productos serán grandes, y el
promedio también. Esa esperanza del producto se llama correlación.

<!-- b2 -->
Calculémosla con el canal. Hay que multiplicar lo enviado por lo recibido
en cada casilla, y pesarlo con su probabilidad. Pero si alguno de los dos
es cero, el producto es cero. Así que solo cuenta la casilla en la que se
envió un uno y se recibió un uno: uno por uno por cero coma veintisiete. La
correlación es cero coma veintisiete.

<!-- b3 -->
Ahora, atención a una trampa. La esperanza del producto no es el producto
de las esperanzas. La media de lo enviado es cero coma tres, y la de lo
recibido, cero coma treinta y cuatro. Su producto es cero coma uno cero dos.
Y la correlación es cero coma veintisiete: bastante más.

<!-- b4 -->
Esa diferencia no es un error: es la información que buscamos. El producto
de las medias es lo que saldría si las dos variables fueran por libre. Si la
correlación es mayor, es porque cuando se envía un uno suele recibirse un
uno: las variables se mueven juntas más de lo que harían por casualidad.

<!-- b5 -->
Para variables continuas la idea es la misma: se multiplica equis por i
griega, se pesa con la densidad conjunta y se suma sobre todo el plano, con
una integral doble. Y esa diferencia entre la correlación y el producto de
las medias es tan importante que tiene nombre propio.

---

# Escena 22 — Covarianza

**Objetivo:** definir la covarianza como la correlación de las variables
centradas, ver su signo con los cuatro cuadrantes, deducir la fórmula
práctica, calcularla con el canal, y demostrar que independientes implica
covarianza cero.

**Qué hace falta saber antes:** escena 21 (correlación); escena 14 (la
deducción de la varianza); escena 06 (independencia).

**Visual:**
- La nube con los ejes movidos a su centro de masa: cuadrantes arriba-derecha y
  abajo-izquierda en verde (producto positivo), los otros en rojo.
- Tres nubes: inclinada hacia arriba (positiva), redonda (cero), inclinada hacia
  abajo (negativa).
- Deducción en tres renglones: «E[(X − μ_X)(Y − μ_Y)]» → desarrollar →
  «E[XY] − μ_X μ_Y». Rótulo: «como con la varianza».
- El canal: «σ_SR = 0,27 − 0,102 = 0,168».
- Independencia: «E[XY] = E[X]·E[Y]» → «σ_XY = 0».

## Narración

<!-- b1 -->
Movamos el origen al centro de la nube: a cada variable le restamos su
media. Ahora el plano queda dividido en cuatro cuadrantes. Arriba a la
derecha y abajo a la izquierda, el producto es positivo. En los otros dos,
negativo. Si la nube sube hacia la derecha, ganan los positivos. Si baja,
ganan los negativos. Si es redonda, se compensan.

<!-- b2 -->
La esperanza de ese producto, medido desde el centro, es la covarianza. Y
con la misma cuenta que hicimos para la varianza, desarrollando el producto
y usando la linealidad, sale la fórmula práctica: la covarianza es la
correlación menos el producto de las medias. Justo la diferencia que vimos
antes. De hecho, la varianza es la covarianza de una variable consigo misma.

<!-- b3 -->
Para el canal: cero coma veintisiete menos cero coma uno cero dos. La
covarianza entre lo enviado y lo recibido es cero coma uno seis ocho. Es
positiva, como tenía que ser: lo enviado y lo recibido tienden a ir en la
misma dirección.

<!-- b4 -->
¿Y si las variables son independientes? Entonces la probabilidad de cada
pareja es el producto de las probabilidades de cada una. Y al calcular la
esperanza del producto, la suma se separa en dos: la esperanza de equis por
la de i griega. La correlación es exactamente el producto de las medias, y
la covarianza da cero.

<!-- b5 -->
Independientes, entonces, significa covarianza cero. Es tentador leerlo al
revés: si la covarianza es cero, serán independientes. Parece lógico, y es
uno de los errores más comunes de toda la estadística. Vamos a ver por qué.

---

# Escena 23 — CeroNoEsNada

**Objetivo:** mostrar con el contraejemplo de la parábola (X uniforme entre
−1 y 1, Y = X²) que covarianza cero no implica independencia, con las
cuentas; explicar que la covarianza solo ve lo lineal; y sembrar la
excepción gaussiana.

**Qué hace falta saber antes:** escena 22 (covarianza, independencia ⇒ cero).

**Visual:**
- X uniforme entre −1 y 1; los puntos (x, x²) dibujan una parábola perfecta.
- «Si X = 0,7 → Y = 0,49» con certeza: un sello «totalmente dependientes».
- Cuentas: «E[X] = 0» (simetría), «E[XY] = E[X³] = 0» (simetría: lo de la
  izquierda cancela lo de la derecha); «σ_XY = 0 − 0 · 1/3 = 0».
- Mitad izquierda con una flecha bajando, mitad derecha con una flecha subiendo;
  se cancelan. La recta de mejor ajuste queda plana.
- Rótulo: «covarianza = relación en línea recta».
- Dos gaussianas conjuntas: «aquí sí: covarianza 0 ⇒ independientes».

## Narración

<!-- b1 -->
Toma una variable equis uniforme entre menos uno y uno, y define i griega
como equis al cuadrado. Estas dos variables son todo lo dependientes que
pueden ser: si te digo que equis vale cero coma siete, sabes sin ninguna
duda que i griega vale cero coma cuarenta y nueve. La nube ni siquiera es
una nube: es una parábola perfecta.

<!-- b2 -->
Calculemos su covarianza. La media de equis es cero, porque la uniforme es
simétrica alrededor de cero. Así que la covarianza es simplemente la
esperanza de equis por i griega, que es la esperanza de equis al cubo. Y
equis al cubo es negativo a la izquierda y positivo a la derecha, en la
misma medida. Su media es cero. La covarianza es cero.

<!-- b3 -->
Dependencia total, y covarianza cero. ¿Cómo puede ser? Mira la parábola.
En la mitad izquierda, cuando equis sube, i griega baja. En la mitad
derecha, cuando equis sube, i griega sube. La covarianza solo pregunta si,
en conjunto, suben o bajan juntas. Y las dos mitades se cancelan: no hay una
tendencia en línea recta.

<!-- b4 -->
Esa es la clave: la covarianza solo detecta la parte en línea recta de una
relación. Si la relación es una curva, la covarianza puede no verla en
absoluto. Por eso, covarianza cero se dice "no correlacionadas", y no
"independientes". No es lo mismo.

<!-- b5 -->
Hay una excepción, y es muy importante para nosotros. Si las dos variables
son gaussianas a la vez, entonces covarianza cero sí quiere decir
independencia. Como el ruido suele ser gaussiano, esa excepción la vamos a
usar muchísimo. Pero hay que acordarse de que es una excepción.

---

# Escena 24 — CombinacionLineal

**Objetivo:** deducir paso a paso la media y la varianza de Z = αX + βY,
pagar la promesa de la escena 16 (varianzas de independientes se suman), y
resolver el ejemplo 6, 4, 3. Dejar planteado que la fórmula "se parece a
algo" (se paga en la escena 27).

**Qué hace falta saber antes:** escenas 13, 14 y 22 (linealidad, varianza, covarianza).

**Visual:**
- «Z = αX + βY» por piezas. Media: «E[Z] = αE[X] + βE[Y]» (linealidad).
- Deducción: «Z − μ_Z = α(X − μ_X) + β(Y − μ_Y)»; al cuadrado, como
  (a + b)² = a² + 2ab + b²; esperanza de cada término:
  «σ_Z² = α²σ_X² + β²σ_Y² + 2αβσ_XY». El término cruzado en ámbar.
- «Si σ_XY = 0: σ_Z² = α²σ_X² + β²σ_Y²» y un tilde junto a la etiqueta de la escena 16.
- El ejemplo: «σ_X² = 6», «σ_Y² = 4», «σ_XY = 3», α = 2, β = −3; los tres
  términos «24», «36», «−36» y el resultado «24».

## Narración

<!-- b1 -->
En señales combinamos variables todo el tiempo: la señal más el ruido, el
promedio de dos medidas, la diferencia entre dos sensores. Así que
conviene saber qué pasa con la media y la varianza de una combinación:
zeta igual a alfa por equis más beta por i griega. La media es fácil: por
linealidad, es alfa por la media de equis más beta por la media de i
griega.

<!-- b2 -->
La varianza hay que deducirla. Restamos la media: zeta menos su media es
alfa por equis centrada más beta por i griega centrada. Lo elevamos al
cuadrado, igual que se desarrolla a más be al cuadrado: el primero al
cuadrado, más el segundo al cuadrado, más dos veces el producto. Y tomamos
la esperanza de cada término.

<!-- b3 -->
Quedan tres términos. Alfa al cuadrado por la varianza de equis. Beta al
cuadrado por la varianza de i griega. Y un término cruzado: dos por alfa por
beta por la covarianza. Si las variables no tienen covarianza, el término
cruzado desaparece y las varianzas simplemente se suman. Esta es la promesa
que dejamos pendiente hace dos episodios, al hablar de promedios.

<!-- b4 -->
Un ejemplo con números. La varianza de equis es seis, la de i griega es
cuatro, y su covarianza es tres. Calculemos la varianza de dos equis menos
tres i griega. Primer término: dos al cuadrado por seis, veinticuatro.
Segundo: tres al cuadrado por cuatro, treinta y seis. Término cruzado: dos
por dos por menos tres por tres, menos treinta y seis. En total,
veinticuatro.

<!-- b5 -->
Fíjate en el signo. La covarianza es positiva: equis e i griega suelen
subir juntas. Pero al restarlas, sus movimientos se compensan, y por eso el
término cruzado resta. Y otra cosa: una fórmula con dos cuadrados y un
término cruzado seguramente te suena de otro sitio. No es casualidad. Para
verlo hay que dejar de pensar en las variables como números, y empezar a
pensarlas como flechas.

---

# Escena 25 — ProductoEscalar

**Objetivo:** repasar desde cero lo que hace falta de vectores: flecha,
componentes, largo (Pitágoras), producto escalar como suma de productos y
como largos por coseno, y perpendicularidad. Sin esto, el E7 no se entiende.

**Qué hace falta saber antes:** nada (geometría del colegio).

**Visual:**
- Una flecha desde el origen hasta (3, 4) sobre una cuadrícula; sus componentes.
- Pitágoras: un triángulo rectángulo de catetos 3 y 4; «largo = √(9 + 16) = 5».
- Dos flechas u = (3, 4) y v = (4, 0): «u · v = 3·4 + 4·0 = 12».
- La misma cuenta como «|u| · |v| · cos θ = 5 · 4 · cos θ = 12 → cos θ = 0,6», y el
  arco del ángulo (~53°).
- La flecha u consigo misma: «u · u = 9 + 16 = 25 = 5²».
- Dos flechas perpendiculares: «producto = 0».

## Narración

<!-- b1 -->
Un repaso rápido de vectores, porque lo vamos a necesitar. Un vector es
una flecha que sale del origen. En el plano se describe con dos números,
sus componentes: cuánto avanza en horizontal y cuánto en vertical. La
flecha tres, cuatro avanza tres a la derecha y cuatro hacia arriba.

<!-- b2 -->
¿Cuánto mide? La flecha es la hipotenusa de un triángulo rectángulo con
catetos tres y cuatro. Por Pitágoras, su largo al cuadrado es tres al
cuadrado más cuatro al cuadrado: veinticinco. El largo es cinco.

<!-- b3 -->
Ahora, dos flechas. Su producto escalar se calcula multiplicando
componente a componente y sumando. Para tres, cuatro y cuatro, cero: tres
por cuatro más cuatro por cero, doce. Y ese mismo número se puede calcular
de otra forma: el largo de una por el largo de la otra por el coseno del
ángulo que forman. Cinco por cuatro por el coseno da doce, así que el
coseno vale cero coma seis.

<!-- b4 -->
El producto escalar tiene dos lecturas que vamos a usar. La primera: el
producto escalar de una flecha consigo misma es su largo al cuadrado. Tres
por tres más cuatro por cuatro, veinticinco. La segunda: si dos flechas son
perpendiculares, el coseno de noventa grados es cero, y su producto escalar
también. Producto cero significa perpendiculares.

<!-- b5 -->
Largos, ángulos, perpendiculares. Todo sale del producto escalar. Y aquí
viene la idea atrevida: ¿y si pudiéramos definir un producto escalar entre
variables aleatorias? Entonces tendrían largo, formarían ángulos y podrían
ser perpendiculares. Resulta que se puede.

---

# Escena 26 — EspacioVectorial

**Objetivo:** definir el producto escalar entre variables aleatorias como la
esperanza del producto, comprobar las tres reglas, traducir largo y
perpendicularidad, y ver que con las variables centradas el producto escalar
es la covarianza y el largo es la desviación estándar.

**Qué hace falta saber antes:** escena 25 (producto escalar); escenas 21 y 22
(correlación, covarianza).

**Visual:**
- Dos columnas enfrentadas: «flechas» | «variables aleatorias».
  «u · v» | «E[XY]»; «|u|² = u · u» | «E[X²]»; «u · v = 0» | «E[XY] = 0: ortogonales».
- Tres casillas con tilde: «no importa el orden», «es lineal», «X · X > 0».
- Las variables centradas: «X − μ_X»; las casillas cambian a «σ_XY», «σ_X²».
- El ejemplo 6, 4, 3 de la escena 24: dos flechas de largo «√6 ≈ 2,45» y «2», con
  producto escalar «3».

## Narración

<!-- b1 -->
Definamos el producto escalar de dos variables aleatorias como la
esperanza de su producto: la correlación. Para que merezca ese nombre, y no
sea solo un parecido, tiene que cumplir las mismas reglas que el producto
escalar de flechas. Son tres.

<!-- b2 -->
Primera: no importa el orden. La esperanza de equis por i griega es la de i
griega por equis. Segunda: es lineal. Si una de las variables es una
combinación de otras, el producto se reparte, gracias a la linealidad de la
esperanza. Tercera: el producto de una variable consigo misma es positivo,
porque es la esperanza de un cuadrado. Las tres se cumplen.

<!-- b3 -->
Así que las variables aleatorias, si solo miramos sus medias, varianzas y
covarianzas, se comportan como flechas. El largo al cuadrado de una variable
es la esperanza de su cuadrado. Y dos variables cuya esperanza del producto
es cero son perpendiculares: se dice que son ortogonales. No es una forma de
hablar. Es la misma condición que en el plano.

<!-- b4 -->
Ahora centremos las variables, restando a cada una su media. Con eso, el
producto escalar se convierte en la covarianza, y el largo al cuadrado, en
la varianza. Es decir: el largo de cada flecha es su desviación estándar, y
el producto escalar entre dos flechas es su covarianza.

<!-- b5 -->
Volvamos al ejemplo de antes. Una variable con varianza seis es una flecha
de largo raíz de seis, algo menos de dos coma cinco. Otra con varianza
cuatro es una flecha de largo dos. Y su covarianza, tres, es su producto
escalar. Dos flechas con un largo cada una y un producto escalar. Entre
ellas tiene que haber un ángulo.

---

# Escena 27 — RhoEsCoseno

**Objetivo:** despejar el coseno del ángulo y reconocer en él el coeficiente
de correlación; calcular el ángulo del ejemplo; leer los casos 1, 0 y −1; y
pagar el teorema del coseno de la escena 24.

**Qué hace falta saber antes:** escenas 25 y 26 (producto escalar como largos
por coseno; covarianza como producto escalar); escena 24 (el ejemplo).

**Visual:**
- «u · v = |u| |v| cos θ» se transforma en «σ_XY = σ_X σ_Y cos θ», y se despeja
  «cos θ = σ_XY / (σ_X σ_Y) = ρ».
- El ejemplo: «ρ = 3 / (√6 · 2) ≈ 0,612», el arco «θ ≈ 52°».
- Un deslizador de ρ: 1 (flechas alineadas, nube en recta que sube), 0
  (perpendiculares, nube redonda), −1 (opuestas, recta que baja).
- El canal de bits: «ρ ≈ 0,77» (se enseña sin cuenta larga).
- El triángulo formado por 2X y −3Y; la fórmula de la escena 24 al lado del
  teorema del coseno: coinciden término a término.

## Narración

<!-- b1 -->
En el plano, el producto escalar es el largo de una flecha por el largo de
la otra por el coseno del ángulo. Traducido a variables: la covarianza es
sigma de equis por sigma de i griega por el coseno del ángulo. Despejando,
el coseno del ángulo es la covarianza dividida entre las dos desviaciones
estándar.

<!-- b2 -->
Ese cociente es un número nuevo, que mide cuánto se parecen las dos variables, y tiene nombre: el coeficiente de correlación, rho. Así que
rho es, literalmente, el coseno del ángulo entre las dos variables
centradas. En el ejemplo, tres dividido entre raíz de seis por dos da cero
coma seis uno dos. Las dos flechas forman unos cincuenta y dos grados.

<!-- b3 -->
Ahora rho se lee de un vistazo. Si vale uno, las flechas apuntan hacia el
mismo lado: la nube es una recta que sube. Si vale cero, son perpendiculares:
no hay ninguna relación en línea recta. Si vale menos uno, apuntan en
sentidos opuestos: la nube es una recta que baja. Para el canal de bits,
por cierto, sale cero coma setenta y siete.

<!-- b4 -->
Y ahora el pago prometido. La varianza de dos equis menos tres i griega era
el largo al cuadrado de la flecha dos equis menos tres i griega. Esa flecha
es el tercer lado de un triángulo. Y el teorema del coseno dice que el
cuadrado de ese lado es la suma de los cuadrados de los otros dos, más un
término cruzado con el coseno del ángulo.

<!-- b5 -->
Es exactamente la fórmula de la varianza de una combinación: los dos
cuadrados son las varianzas, y el término cruzado es la covarianza. Aquella
cuenta era geometría todo el tiempo. Queda una pregunta pendiente: ¿quién
garantiza que rho no pueda valer, por ejemplo, uno coma cinco?

---

# Escena 28 — CauchySchwarz

**Objetivo:** demostrar que |ρ| ≤ 1 con la parábola de Cauchy-Schwarz,
explicando desde cero qué es el discriminante; ver que la igualdad significa
una relación en línea recta exacta; y anunciar que el truco vuelve en los
capítulos 11 y 13.

**Qué hace falta saber antes:** escena 27 (ρ = cos θ); escena 14 (desarrollar un cuadrado).

**Visual:**
- «g(λ) = E[(U − λV)²] ≥ 0»: la esperanza de un cuadrado, nunca negativa.
- Desarrollo: «g(λ) = E[U²] − 2λE[UV] + λ²E[V²]»: una parábola en λ que se dibuja.
- Recordatorio del colegio: «aλ² + bλ + c = 0 → λ = (−b ± √(b² − 4ac)) / 2a».
  Tres parábolas: dos cortes (b² − 4ac > 0), un toque (= 0), ningún corte (< 0).
- La nuestra no puede cortar dos veces: «b² − 4ac ≤ 0» → «E[UV]² ≤ E[U²] E[V²]».
- Con variables centradas: «σ_XY² ≤ σ_X² σ_Y²» → «|ρ| ≤ 1».
- Con los números del ejemplo: «g(λ) = 6 − 6λ + 4λ²», discriminante «36 − 96 = −60 < 0».
- Si la parábola toca el eje: la nube se vuelve una recta exacta: «|ρ| = 1».

## Narración

<!-- b1 -->
Un coseno siempre está entre menos uno y uno. Pero aquí rho está definido
con esperanzas, así que hay que demostrar que también lo cumple. La
demostración es preciosa. Toma dos variables, la u y la ve, y un número cualquiera,
lambda. Mira la esperanza de u menos lambda por v, todo al cuadrado. Es la
esperanza de algo al cuadrado, así que nunca puede ser negativa.

<!-- b2 -->
Desarrollemos el cuadrado: la esperanza de u al cuadrado, menos dos lambda
por la esperanza de u por v, más lambda al cuadrado por la esperanza de v al
cuadrado. Si lo miras como una función de lambda, es una parábola: un número
por lambda al cuadrado, más otro por lambda, más otro. Y sabemos que esta
parábola nunca baja de cero.

<!-- b3 -->
Recuerda la ecuación de segundo grado del colegio. Las soluciones tienen
una raíz cuadrada de be al cuadrado menos cuatro a ce, que se llama
discriminante. Si es positivo, la parábola corta el eje dos veces. Si es
cero, lo toca en un punto. Y si es negativo, no lo toca. Nuestra parábola
nunca baja de cero, así que no puede cortarlo dos veces: su discriminante no
puede ser positivo.

<!-- b4 -->
Escribimos esa condición, simplificamos, y queda la desigualdad de
Cauchy-Schwarz: la esperanza de u por v, al cuadrado, nunca supera la
esperanza de u al cuadrado por la de v al cuadrado. Con variables
centradas: la covarianza nunca supera el producto de las desviaciones
estándar. Es decir, rho está entre menos uno y uno. Con los números del
ejemplo, el discriminante vale menos sesenta: la parábola ni se acerca al eje.

<!-- b5 -->
¿Y si el discriminante es justo cero? Entonces la parábola toca el eje: hay
un lambda para el que u menos lambda por v vale cero siempre. Es decir, una
variable es exactamente una recta de la otra, sin nada de azar. Eso es rho
igual a uno o a menos uno. Y guarda este truco de la parábola: volverá varias
veces más en el curso, cuando menos lo esperes.

---

# Escena 29 — TrampasDeRho

**Objetivo:** advertir que rho resume una nube entera en un número y puede
engañar (relaciones curvas, datos atípicos). Dejar la regla "mirar siempre la
nube". Cerrar el capítulo con la pregunta geométrica que abre el capítulo 8.

**Qué hace falta saber antes:** escenas 27 (rho como coseno) y 23 (la
covarianza no ve lo curvo).

**Visual:**
- Cuatro nubes en una cuadrícula de 2 × 2, todas con «ρ ≈ 0,85» encima: una
  recta con ruido, una curva perfecta, una recta perfecta con un punto
  escapado, y una columna vertical con un punto lejísimos.
- El punto atípico se aparta y el «0,85» cae; vuelve y sube.
- Una lupa sobre la nube, y el lema «mirar la nube antes que el número».
- Para el cierre: la flecha Y, la flecha X, y la sombra de Y sobre X.

## Narración

<!-- b1 -->
Rho es un número muy cómodo: una nube entera resumida en un coseno. Pero
resumir tanto tiene un precio. Mira estas cuatro nubes. Las cuatro tienen
casi el mismo rho, alrededor de cero coma ocho cinco. Y no se parecen en
nada.

<!-- b2 -->
La primera es lo que esperas: una relación en línea recta con algo de
ruido. La segunda es una curva perfecta, sin ruido ninguno: rho no avisa de
que una recta es el modelo equivocado. La tercera es una recta perfecta con
un solo punto escapado, que baja el rho sin que nada lo indique. Y en la
cuarta no hay relación ninguna: todos los puntos están en una columna, y un
único punto, muy lejos, se inventa toda la correlación.

<!-- b3 -->
La covarianza es un promedio de productos, así que un solo punto muy
lejano puede dominarla. Y ya sabemos que solo ve la parte en línea recta. La
regla práctica es sencilla: antes de creerte un rho, mira la nube. El número
viene después.

<!-- b4 -->
Esta forma de mirar las variables como flechas es la que ordena media
asignatura. Si queremos adivinar una variable a partir de otra, la
pregunta se convierte en geométrica: cuál es el punto de una flecha que
queda más cerca de otra. Y a esa pregunta la geometría le tiene una
respuesta desde hace siglos: la proyección.
