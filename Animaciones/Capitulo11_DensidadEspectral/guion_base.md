# Capítulo 11 — Densidad espectral de potencia

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

Guion para las 32 escenas del capítulo. Fuentes: `Apuntes/PROCESAMIENTO DE
SEÑALES.md` (sección "Densidad Espectral De Potencia", líneas 1087–1289, sin
los Ejercicios Propuestos) y `Apuntes/PROCESAMIENTO DE SEÑALES - Cap 11 en
profundidad.md`: Parte 1 (no negatividad con el filtro pasabanda, Bochner con
el rectángulo y el triángulo, EWK con el triángulo de la ventana, desigualdad
cruzada), Parte 2 (la exponencial, el proceso correlacionado a un paso por dos
caminos, factorización y blanqueador), Parte 3 (fuga, zero-padding, ventanas,
Welch, la trampa de la coherencia), Parte 4 (de quién es el espectro,
ergodicidad, los tres males del estimador, Paley-Wiener, hacia dónde va todo).
Figuras de referencia: `c11-psd-pasabanda.svg`, `c11-psd-exponencial.svg`,
`c11-blanco-vs-coloreado.svg`, `c11-periodograma.svg`, `c11p-ewk.svg`,
`c11p-pasabanda-filtro.svg`, `c11p-leakage.svg`, `c11p-zeropadding.svg`,
`c11p-ventanas.svg`, `c11p-welch.svg`, `c11p-sesgo-varianza.svg`,
`c11p-factorizacion.svg`.

**Qué se recuerda y dónde** (README §3, regla 2: nada se da por sabido, se
recuerda donde se usa, con su dibujo):
- de Señales y Sistemas: Fourier y el espectro como barras (escena 01), la
  energía como área del cuadrado (02), la transformada con la exponencial
  compleja y su inversa (04), el espectro simétrico de una señal real (05), la
  convolución como "deslizar y medir el área común" y su transformada (08), el
  espectro periódico en tiempo discreto (07), Parseval (16), la dualidad pulso
  estrecho ↔ espectro ancho (13), el escalón que necesita todas las
  frecuencias (20), el teorema del muestreo (25);
- de matemáticas: funciones par e impar y el área de una impar (07), la
  integral de una exponencial que decae (12), sumar fracciones y jota al
  cuadrado igual a menos uno (12), el impulso como pico de área fija (11),
  logaritmos y decibelios (21), los números complejos como flechas con módulo
  y ángulo (29);
- del capítulo 7: la varianza como esperanza del cuadrado menos la media al
  cuadrado (11), la varianza del promedio (19), rho entre menos uno y uno (09),
  la parábola de Cauchy-Schwarz (30), rho con dos puntos (32);
- del capítulo 10: estacionario (02), ensemble (02), autocorrelación y
  autocovarianza (03, 11), la onda telegráfica (03), la sinusoide de fase
  aleatoria (13), la correlación cruzada (29), la ergodicidad y las pilas
  (24), el eco del 0,6 (26), y lo que hace un filtro con la densidad
  espectral (05), que es con lo que cierra el capítulo 10 y le da nombre.

Cómo está escrito (README §3, "Explicar de forma explícita"): cada concepto
sigue el camino caso → cuenta a mano con números pequeños → dibujo → fórmula
como resumen → comprobación. Las deducciones cortas se hacen enteras, diciendo
qué regla se usa en cada paso; las largas (Einstein-Wiener-Khinchin, la
desigualdad cruzada con retardo) se hacen en su paso clave y se remite al
apunte "en profundidad". Hay preguntas con pausa y encuestas visuales en las
escenas 01, 06, 08, 09, 13, 15, 18, 23 y 32. Castellano de España.

Convención: cada escena tiene Objetivo, qué hace falta saber antes, qué se ve,
y la narración partida en bloques `<!-- bN -->` que se sincronizan uno a uno
con un tramo de animación.

## Reparto en episodios

| Episodio | Escenas | Idea fuerza |
|---|---|---|
| E1 · ¿En qué frecuencias vive el azar? | 01 LaPregunta, 02 SinTransformada, 03 PotenciaEsperada, 04 TransformarLaAutocorrelacion, 05 FiltroPasabanda | Una señal aleatoria no tiene espectro, pero su potencia esperada sí, y el área de esa curva sobre una banda es la potencia que hay en ella |
| E2 · Lo que un espectro no puede hacer | 06 NuncaNegativa, 07 RealYPar, 08 ExamenDeTresPreguntas, 09 CorrelacionAUnPaso, 10 Bochner | Como la potencia no puede ser negativa, hay curvas que no son espectros y correlaciones que no pueden existir |
| E3 · El color del ruido | 11 FluctuacionesYMedia, 12 LaCuentaDeLaTelegrafica, 13 MemoriaYAncho, 14 RuidoBlanco, 15 LasSorpresasDelBlanco | La forma del espectro es la memoria del proceso vista desde la frecuencia: sin memoria, el espectro es plano |
| E4 · Un espectro a partir de datos | 16 Periodograma, 17 ElDesenfoque, 18 PeriodogramaRuidoso, 19 PromediarTrozos | Con datos finitos el espectro sale desenfocado y tembloroso, y con una grabación fija no se pueden arreglar las dos cosas a la vez |
| E5 · Cortar sin romper | 20 Fuga, 21 Decibelios, 22 Ventanas, 23 RellenarConCeros, 24 Welch | Cortar derrama potencia a las frecuencias vecinas; una ventana suave lo frena a cambio de resolución, y la resolución solo se compra con tiempo |
| E6 · Fabricar el color y quitarlo | 25 PicosQueDelatan, 26 FiltroModelador, 27 FiltroBlanqueador, 28 FaseMinima | Un filtro pinta el ruido blanco del color que quieras, y su inverso lo devuelve a blanco, si no explota |
| E7 · Dos procesos, frecuencia a frecuencia | 29 DensidadCruzada, 30 CauchySchwarzPorFrecuencia, 31 Coherencia, 32 LaTrampaDeLaCoherencia | En cada frecuencia, dos procesos son solo dos variables aleatorias: misma desigualdad, mismo rho |

Narración base por episodio (sin gancho ni cierre): E1 ≈ 1.350 palabras, E2 ≈ 1.370,
E3 ≈ 1.340, E4 ≈ 1.040, E5 ≈ 1.300, E6 ≈ 1.090, E7 ≈ 1.130: entre 7 y 9 min
de voz; con gancho y cierre, ~8–10,5 min. E1 a E3 son los más largos.

El gancho y el cierre de cada episodio **no** están aquí: se escriben al
armar el `guion.md` del episodio (README §2, paso 8). Cada cierre anuncia el
episodio siguiente por su título. El E1 lo anuncia el cierre del último
episodio del capítulo 10 (su escena 29 ya lo prepara y anuncia este título: bautiza la densidad
espectral de potencia porque la ganancia al cuadrado por ella «se parece a la
densidad espectral de energía»; la escena 04 de aquí retoma ese nombre).
El cierre de E7 anuncia el E1 del capítulo 12 (Estimación de señales), cuyo
título se decide al escribir su guion base.

## Hilos que cruzan el capítulo

Para quien arme cada episodio: estos bucles ya están sembrados en la
narración y hay que respetarlos (y retomarlos en ganchos y cierres).

- **Los ejemplos que vuelven** (mismo dibujo y mismos números siempre):
  - **la voz y el murmullo** (escenas 01 y 31): la pregunta del capítulo se
    abre con una voz (azul) tapada por un murmullo (magenta) y se paga con la
    coherencia: en qué frecuencias el micrófono dice algo de la voz;
  - **la onda telegráfica con alfa igual a dos** (escenas 02, 03, 04, 05, 06,
    12, 13, 16, 17): salta entre más uno y menos uno, potencia uno,
    autocorrelación e elevado a menos dos por el valor absoluto de tau (0,37 a
    medio segundo), densidad espectral cuatro sobre cuatro más omega al
    cuadrado (vale 1 en cero y 0,5 en omega igual a dos), y la mitad de su
    potencia entre menos dos y dos. La densidad se usa en la escena 04 con la
    promesa de calcularla, y la cuenta se hace en la escena 12 (**bucle E1 →
    E3**);
  - **las tres barras rho, uno, rho con rho igual a 0,4** (escenas 07, 09, 10,
    26, 28): espectro uno más cero coma ocho por el coseno de omega (1,8 · 1 ·
    0,2); rho igual a 0,6 no puede existir (−0,2); se fabrica con el filtro
    (2, 1) dividido entre raíz de cinco, y también con el (1, 2): el mismo
    proceso con dos filtros, cuyas inversas se apagan (½, −¼, ⅛) o explotan
    (1, −2, 4, −8);
  - **el eco del 0,6** (escenas 26 y 27): el sensor de temperatura del
    capítulo 10 (autocovarianza 4 · 0,6 elevado a |m|: se multiplica por 0,6 en cada paso),
    ahora como salida igual a 0,6 por la salida anterior más una moneda;
    correlaciones 0,60 · 0,36 · 0,22 · 0,13; el
    blanqueador las deja en 0,00 · 0,003 · −0,001 · 0,00 (simulado con 400.000
    muestras, semilla 11);
  - **la moneda** (escenas 10, 14, 15, 26): más uno o menos uno en cada
    instante, el ruido blanco discreto;
  - **los dos tonos de 50 y 50,5 hercios** (escenas 17, 19, 22, 23): se
    separan con dos segundos de grabación, no con uno;
  - **la tensión de cinco voltios** (escena 11): potencia 26 = 25 + 1.
- **"La potencia no puede ser negativa"**: el argumento del capítulo. Se planta
  en las escenas 05 y 06 y se reusa en la 08 (el rectángulo), la 09 (rho no
  pasa de un medio), la 15 (el blanco tiene media cero) y la 30
  (Cauchy-Schwarz por frecuencia).
- **El rectángulo que se desliza sobre otro**: en la escena 08 (E2) arma el
  triángulo por convolución, y se anuncia que volverá. **Se paga en la escena
  16 (E4)**: el triángulo de la ventana. Mismo dibujo.
- **Bochner = el filtro modelador**: la escena 10 (E2) fabrica rho igual a 0,4
  con un filtro y anuncia que ese filtro volverá; **la escena 26 (E6)** lo
  revela como filtro modelador y como la demostración del teorema.
- **Memoria corta, espectro ancho**: escena 13 (E3). Se reusa en la 14 (sin
  memoria, plano) y en la 27 (el blanqueador borra la memoria).
- **Promediar = grandes números**: la escena 19 (E4) recuerda la varianza del
  promedio del capítulo 7 con el mismo dibujo de la banda que se angosta.
- **Ergodicidad = el permiso para estimar**: la escena 18 lo insinúa (un
  periodograma es una sola muestra del ensemble) y la 24 lo paga con las
  pilas del capítulo 10.
- **"Mirar la nube antes que el número"** (capítulo 7): vuelve en la escena 24
  (repetir con otro tramo) y en la 32 (la coherencia con un solo trozo da uno,
  como rho con dos puntos).
- **La parábola de Cauchy-Schwarz**: viene del capítulo 7 y ya volvió en el
  capítulo 10 (escena 12, acotando la autocovarianza del sensor). **Esta es su tercera
  aparición** (escena 30, E7), con el mismo dibujo. La última es el filtro
  adaptado del capítulo 13. (Ojo: la escena 28 del capítulo 7 dice que
  «volverá dos veces más», y con el capítulo 10 son tres.)
- **Puentes a otros capítulos** (Parte 4.5 del "en profundidad"):
  - capítulo 12: la coherencia dice en qué frecuencias fiarse del micrófono
    (escena 31), que es la idea del filtro de Wiener; la fase mínima es el
    paso del Wiener causal (escena 28); "no se puede blanquear lo que no
    existe" es la condición de Paley-Wiener (escena 28, sin nombrarla);
  - capítulo 13: blanquear primero y aplicar lo que ya sabemos después
    (escena 27).
- **Cierre del capítulo** (la escena 32 ya lo prepara; cierre de E7, a
  escribir): si en cada frecuencia dos procesos son dos variables, separar la
  voz del murmullo es estimar una variable a partir de otra, frecuencia por
  frecuencia → capítulo 12.

## Recortes decididos

- La sutileza del límite cuando la banda se estrecha (Parte 1.1): se dice "tan
  estrecha como quieras" y basta.
- La cuenta de la integral del rectángulo y del arco tangente de la mitad de
  la potencia de la telegráfica: se dan los resultados y se dice dónde está la
  cuenta. La integral de la exponencial sí se hace (escena 12).
- El teorema de Einstein-Wiener-Khinchin: se hace el paso clave (el
  solapamiento de las ventanas es un triángulo), no la demostración entera.
- La desigualdad cruzada: se hace con la parábola; el truco del retardo solo
  se nombra ("sirve para girar la flecha").
- El efecto de reja y los −3,9 dB del zero-padding; la ventana de Hamming; la
  normalización de Welch por la potencia de la ventana; por qué la ventana de
  Hann suma una constante al solaparse por la mitad.
- La PSD compleja en zeta, los polos y ceros en el plano zeta y el pasa-todo:
  la fase mínima se explica con dos filtros de dos coeficientes y sus
  inversas calculadas a mano.
- La condición de Paley-Wiener como fórmula (solo la idea).
- El ruido térmico de Johnson-Nyquist como fórmula (se nombra como ejemplo).
- El muestreo de procesos limitados en banda se reduce a un bloque de la
  escena 25.
- Las diferencias de notación entre tiempo continuo y discreto: se narra en
  continuo, y los ejemplos discretos (tres barras, moneda, eco) se presentan
  como tales, con la frecuencia de menos pi a pi, sin más.
- Los estimadores sesgado e insesgado de la autocorrelación (el capítulo 10
  los dejó para aquí): quedan para el apunte; el capítulo estima el espectro
  por el periodograma.
- Los Ejercicios Propuestos no se resuelven (tampoco los ejercicios 11.2 y
  11.17 de las actividades del apunte); los números de los ejemplos son del
  "en profundidad" o inventados con números redondos (rho igual a 0,4, el eco
  del 0,6, los tonos de 50 y 50,5 hercios, la tensión de 5 voltios, la
  coherencia 3 a 1).

## Pronunciación

Probar de oído antes de sintetizar (README §9): Fourier, Parseval, Einstein,
Wiener, Khinchin, Bochner, Herglotz, Welch, Hann, Blackman, Dirac,
Cauchy-Schwarz. Siglas: FFT (en la narración se dice «la FFT»: probar), FSD
(se evita en la narración: «la densidad de las fluctuaciones»). Palabras
técnicas: «periodograma», «sinc» (se dice «la función sinc»: probar),
«zero-padding» y «leakage» (en la narración: «rellenar con ceros» y «fuga»;
el término en inglés solo en pantalla). Letras y símbolos que se leen en voz
alta: «tau», «omega», «alfa», «rho», «sigma», «gamma», «lambda», «pi», «jota».
Unidades: «hercios», «radianes por segundo», «decibelios», «voltios».

## Piezas visuales nuevas

Van a `comun/figuras.py` (sección «capítulo 11, episodio N»):
- espectro de barras de una suma de senos, con un filtro que apaga barras (E1);
- `Realizaciones` (prevista en el README) con la onda telegráfica, y una
  ventana rectangular que recorta un tramo de una de ellas (E1, E4);
- `Espectro`: una densidad sobre el eje omega, par, con el cero al centro;
  `banda(w0, ancho)` sombrea las dos ventanitas simétricas; admite impulsos
  (flechas verticales) en cero o en más y menos omega cero (E1–E3);
- par autocorrelación ↔ espectro lado a lado, con un `ValueTracker` que
  comparte alfa (al estrecharse una se ensancha la otra) (E3);
- función par por función impar con las áreas que se cancelan (E2);
- rectángulo que se desliza sobre otro y dibuja el triángulo punto a punto
  (E2, y el mismo en E4);
- las tres barras rho, uno, rho y su espectro con un `ValueTracker` sobre rho
  que hunde el mínimo bajo cero en rojo (E2);
- `BloqueLTI` (previsto en el README) con coeficientes a la vista y una moneda
  a la entrada (E2, E6);
- prisma: luz blanca que se abre en colores (E3);
- periodograma ruidoso sobre la densidad verdadera, y el promedio de M trozos
  (E4); dos tonos que se funden o se separan según el largo de la ventana
  (E4, E5);
- escala de decibelios (una regla vertical con ×10, ×100, ×1.000.000) (E5);
- núcleo de una ventana en decibelios para rectangular, Hann y Blackman (E5);
- registro partido en trozos solapados, cada uno con su campana de Hann (E5);
- tabla de correlaciones por distancia que se llena (E6);
- respuesta al impulso de un filtro inverso que se apaga o explota (E6);
- número complejo como flecha con módulo y ángulo, que gira (E7);
- la parábola de Cauchy-Schwarz del capítulo 7 (misma pieza), repetida a lo
  largo del eje omega (E7).

---

# Escena 01 — LaPregunta

**Objetivo:** plantear la pregunta del capítulo (en qué frecuencias vive el
ruido) y recordar Fourier, el espectro y el filtro con un ejemplo de dos
senos. Dejar planteado que transformar el ruido "no funciona".

**Qué hace falta saber antes:** nada del capítulo; de Señales y Sistemas, que
una señal se puede descomponer en senos (se recuerda aquí).

**Visual:**
- Una onda de voz (azul) con un murmullo encima (magenta); un colador entre
  las dos.
- Un seno lento (2 Hz) y uno rápido (5 Hz) que se suman en una forma rara;
  Fourier los separa: dos barras en «2 Hz» y «5 Hz». «hercio = veces por segundo».
- Un filtro multiplica cada barra por su ganancia: la barra de 5 Hz por cero,
  desaparece, y en el tiempo queda solo el seno lento.
- El espectro de la voz (un bulto entre cientos y miles de hercios) y el del
  murmullo: primero separados (el colador funciona), luego encimados (no).
- «¿Cómo calcularías el espectro del ruido?» con una pausa.

## Narración

<!-- b1 -->
Imagina una grabación en la que alguien habla y, de fondo, hay un murmullo
constante. Queremos limpiarla. Para eso existe una herramienta de Señales y
Sistemas: el filtro, un colador que deja pasar unas frecuencias y retiene
otras. Pero para diseñar el colador hay que saber algo antes: en qué
frecuencias vive la voz, y en cuáles vive el ruido.

<!-- b2 -->
Recordemos qué quiere decir eso. Toma un seno lento, que se repite dos veces
por segundo, y súmale uno rápido, que se repite cinco veces por segundo. La
suma tiene una forma rara, difícil de leer. Pero la transformada de Fourier
la desarma: dice que hay un seno de dos hercios y otro de cinco. Un hercio es
una vez por segundo.

<!-- b3 -->
El dibujo de cuánto hay de cada frecuencia es el espectro: aquí, dos barras.
Y un filtro actúa sobre ese dibujo: multiplica cada barra por un número, su
ganancia. Si la ganancia en cinco hercios es cero, esa barra desaparece, y en
el tiempo queda solo el seno lento. Eso es el colador.

<!-- b4 -->
Con la voz pasa lo mismo, solo que su espectro no son dos barras sino un
bulto, entre unos cientos y unos miles de hercios. Si el murmullo vive en
otras frecuencias, el colador los separa sin problema. Si viven en las
mismas, no hay colador que valga. Todo depende de conocer el espectro del
ruido.

<!-- b5 -->
Así que la pregunta es: ¿cómo calcularías el espectro de un ruido? Piénsalo
un momento antes de seguir. La respuesta obvia es grabarlo y aplicarle
Fourier, como a los dos senos. Parece fácil. No funciona. Y entender por qué
es la mitad de este capítulo.

---

# Escena 02 — SinTransformada

**Objetivo:** ver los tres problemas de transformar una realización: dura
para siempre, tiene energía infinita (con la cuenta hecha) y es distinta cada
vez. Proponer el cambio: potencia en vez de energía, promedio del ensemble en
vez de una realización.

**Qué hace falta saber antes:** escena 01; capítulo 10 (proceso
estacionario, ensemble), que se recuerdan aquí.

**Visual:**
- Un pulso de altura 1 que dura 3 s; su cuadrado sombreado: «energía = 3».
- La onda telegráfica (más uno, menos uno) que se extiende hacia los dos
  lados; su cuadrado es una línea plana en 1. Un contador de energía: «10 s →
  10», «1.000 s → 1.000», «→ ∞».
- Tres realizaciones del ensemble apiladas, cada una con su espectro al lado:
  todos distintos.
- Tres cruces rojas: «no empieza ni termina», «energía infinita», «cada vez
  distinta».

## Narración

<!-- b1 -->
Empecemos por la energía. En Señales y Sistemas, la energía de una señal es
el área bajo su cuadrado. Un pulso que vale uno durante tres segundos tiene
energía tres. Las señales que empiezan y terminan tienen energía finita, y
para ellas la transformada de Fourier existe y se puede dibujar.

<!-- b2 -->
Ahora toma un ruido estacionario, que es como llamamos en el capítulo
anterior a un proceso cuyas reglas no cambian con el tiempo. Por ejemplo, la
onda telegráfica: una señal que salta entre más uno y menos uno en instantes
al azar. No empieza ni termina. Y su cuadrado vale uno en todo momento.

<!-- b3 -->
Hagamos la cuenta. Al cabo de diez segundos, el área bajo el cuadrado vale
diez. Al cabo de mil segundos, mil. Y la señal sigue para siempre, así que
la energía total es infinita. Una señal de energía infinita no tiene una
transformada que se pueda dibujar: como mucho, algo lleno de impulsos. Primer
camino cerrado.

<!-- b4 -->
Y hay un problema peor. Aunque pudiéramos transformarla, sería el espectro
de esa grabación. Recuerda el ensemble: mil grabaciones del mismo fenómeno,
una encima de otra. Cada una tiene su propio espectro, distinto en todos los
detalles. Lo que buscamos es una propiedad del fenómeno, no de una de sus
grabaciones.

<!-- b5 -->
Tres problemas: dura para siempre, tiene energía infinita y es distinta cada
vez. Y los tres se resuelven cambiando dos palabras. En lugar de energía,
vamos a mirar potencia. Y en lugar de una grabación, vamos a promediar sobre
todo el ensemble.

---

# Escena 03 — PotenciaEsperada

**Objetivo:** pasar de energía a potencia con la cuenta de la telegráfica
(potencia uno), definir la potencia instantánea, promediarla sobre el
ensemble y reconocer ahí la autocorrelación en cero. Recordar la
autocorrelación de la telegráfica y ver que, a diferencia de la señal, se
apaga.

**Qué hace falta saber antes:** escena 02; capítulo 10 (autocorrelación),
que se recuerda aquí.

**Visual:**
- «energía / tiempo»: «10 / 10 = 1», «1.000 / 1.000 = 1». La potencia es una
  línea que se queda quieta mientras la energía sube.
- Una resistencia de 1 Ω con la señal como tensión: «x²(t)» aparece como
  potencia instantánea.
- Las realizaciones apiladas con un corte vertical en t; los cuadrados se
  promedian: «E[x²(t)]».
- La señal y una copia desplazada τ: «R_xx(τ) = E[x(t) x(t − τ)]»; en τ = 0,
  las dos coinciden: «R_xx(0) = E[x²(t)]».
- La autocorrelación de la telegráfica, «e^{−2|τ|}», con los puntos «1» en
  cero, «0,37» en medio segundo y «0,14» en un segundo.

## Narración

<!-- b1 -->
La potencia es energía por unidad de tiempo. Con la onda telegráfica: diez
de energía en diez segundos da potencia uno. Mil en mil segundos, potencia
uno otra vez. La energía crece sin parar, pero la potencia se queda quieta.
Es finita, aunque la señal dure para siempre. Primer problema resuelto.

<!-- b2 -->
Si la señal fuera la tensión sobre una resistencia de un ohmio, su cuadrado
sería la potencia que se disipa en cada instante: la potencia instantánea.
Ahora el segundo cambio: en un instante cualquiera, promediamos esa potencia
sobre todas las grabaciones del ensemble. Es la esperanza de equis al
cuadrado.

<!-- b3 -->
Y esa esperanza ya tiene nombre. En el capítulo anterior definimos la
autocorrelación: tomas la señal y una copia desplazada un tiempo tau, las
multiplicas y promedias. Mide cuánto se parece la señal a sí misma tau
segundos después. Con tau igual a cero, la copia coincide con la señal, y
queda justo la esperanza de equis al cuadrado.

<!-- b4 -->
Así que la potencia esperada es la autocorrelación en cero. Y como el
proceso es estacionario, da igual en qué instante la midas. Para la onda
telegráfica, si salta en promedio una vez por segundo, la autocorrelación es
e elevado a menos dos por el valor absoluto de tau. En cero vale uno: la
potencia que contamos a mano.

<!-- b5 -->
Fíjate en la forma de esa curva. A medio segundo vale cero coma tres siete;
a un segundo, cero coma uno cuatro; y sigue bajando hacia cero. La señal no
se apaga nunca, pero su autocorrelación sí. Es una función con área finita,
y una función así sí tiene transformada de Fourier. Ahí está la salida.

---

# Escena 04 — TransformarLaAutocorrelacion

**Objetivo:** definir la densidad espectral de potencia como la transformada
de la autocorrelación, recordando qué hace la transformada y qué es la
exponencial compleja. Deducir con la fórmula de inversión que la potencia
total es el área dividida entre dos pi, y comprobarlo con la telegráfica
(prometiendo la cuenta de su densidad para el episodio 3).

**Qué hace falta saber antes:** escena 03 (autocorrelación, potencia = su
valor en cero); de Señales y Sistemas, la transformada (se recuerda aquí).

**Visual:**
- La autocorrelación de la telegráfica multiplicada por un coseno de
  frecuencia omega; el área del producto se sombrea: «¿cuánto hay de esta
  frecuencia?». Omega cambia y el área cambia.
- «e^{jθ} = cos θ + j sen θ», con «j = √−1».
- La definición por piezas: «S_xx(jω) =», «∫ R_xx(τ)», «e^{−jωτ} dτ».
- La inversa: «R_xx(τ) = (1/2π) ∫ S_xx(jω) e^{jωτ} dω»; τ se reemplaza por 0,
  la exponencial se vuelve «1», y queda «R_xx(0) = (1/2π) ∫ S_xx(jω) dω».
- La curva «4/(4 + ω²)» con su área rellenada: «área = 2π», «2π / 2π = 1» ✓.

## Narración

<!-- b1 -->
Recordemos qué hace la transformada de Fourier. Para cada frecuencia omega,
multiplica la función por una oscilación de esa frecuencia y calcula el área
del producto. Si la función tiene mucho de esa frecuencia, el área es grande;
si no tiene nada, el área es cero. Es una forma de preguntar, frecuencia por
frecuencia, cuánto hay.

<!-- b2 -->
La oscilación se escribe con una exponencial compleja: e elevado a jota por
un ángulo. La jota es la unidad imaginaria, la raíz de menos uno, y esa
exponencial es una forma compacta de escribir un coseno y un seno a la vez.
Así la transformada mide de una vez las dos oscilaciones de cada frecuencia.

<!-- b3 -->
Al final del capítulo anterior le pusimos nombre a la transformada de la
autocorrelación: densidad espectral de potencia. Se escribe ese sub equis
equis de jota omega, y es la integral de la autocorrelación por e elevado a
menos jota omega tau. Una curva sobre el eje de frecuencias. Ahora vamos a
ver por qué se merece ese nombre.

<!-- b4 -->
La transformada tiene inversa: la autocorrelación es uno sobre dos pi por la
integral de la densidad por e elevado a jota omega tau. Pongamos tau igual a
cero. La exponencial de cero vale uno, y desaparece. Queda que la potencia,
la autocorrelación en cero, es el área bajo la densidad espectral dividida
entre dos pi.

<!-- b5 -->
Comprobémoslo con la telegráfica. Su densidad espectral es cuatro dividido
entre cuatro más omega al cuadrado: haremos la cuenta en dos episodios. El
área bajo esa curva vale dos pi. Dividida entre dos pi, da uno: la potencia
que contamos a mano. El área total es la potencia total.

---

# Escena 05 — FiltroPasabanda

**Objetivo:** justificar el nombre "densidad": con un filtro pasabanda ideal,
el área de la PSD sobre una banda es la potencia del proceso en esa banda.
Recordar por qué la banda viene de a dos (espectro simétrico de una señal
real) y por qué un filtro multiplica la densidad por la ganancia al cuadrado.
Ejemplo: la mitad de la potencia de la telegráfica está entre menos dos y dos.

**Qué hace falta saber antes:** escena 04 (área total = potencia total);
escena 01 (el filtro multiplica cada barra por su ganancia).

**Visual:**
- La densidad de la telegráfica. Encima, el colador: dos ventanitas de
  altura 1 en más y menos omega cero (como `c11p-pasabanda-filtro.svg`).
- Un seno de 5 Hz y su espectro: dos barras, en «+5» y «−5».
- Un seno que pasa por una ganancia 3: la amplitud se triplica, la potencia
  se multiplica por «9». «S_yy = |H|² S_xx».
- La densidad recortada a las dos ventanitas; el área se sombrea en ámbar:
  «potencia en la banda = área / 2π».
- El colador se ensancha a «−2 < ω < 2»: «½» de la potencia; el resto, «½»,
  repartido hasta el infinito. «2π rad/s = 1 Hz».

## Narración

<!-- b1 -->
Que el área total sea la potencia total no basta para llamar densidad a esta
curva. Queremos más: que cada trozo de área sea la potencia de ese trozo de
frecuencias. Para comprobarlo usamos un colador ideal: deja pasar tal cual
una franja estrecha alrededor de una frecuencia, omega cero, y borra todo lo
demás.

<!-- b2 -->
Un detalle: el espectro de una señal real es simétrico. Un seno de cinco
hercios aparece como dos barras, en más cinco y en menos cinco. Así que el
colador también tiene que ser simétrico: una ventanita en más omega cero y
su reflejo en menos omega cero.

<!-- b3 -->
¿Qué hace un filtro con la potencia? Multiplica la amplitud de cada
frecuencia por su ganancia. Y la potencia va con el cuadrado de la amplitud:
si la ganancia es tres, la potencia se multiplica por nueve. Por eso, como
vimos al final del capítulo anterior, a la salida la densidad espectral es
la de la entrada por el módulo de la ganancia al cuadrado.

<!-- b4 -->
Dentro de las ventanitas, la ganancia es uno, y uno al cuadrado es uno: la
curva queda intacta. Fuera, es cero, y la curva desaparece. La potencia de
la salida es el área de lo que queda, dividida entre dos pi. Y eso vale para
cualquier banda: el área sobre una banda es la potencia que el proceso tiene
en ella.

<!-- b5 -->
Con la telegráfica: si el colador deja pasar de menos dos a dos radianes por
segundo, el área que queda da justo la mitad de la potencia. La otra mitad
está repartida por todas las demás frecuencias, hasta el infinito. Esa es la
herramienta del capítulo: una curva que dice cuánta potencia hay en cada
banda.

---

# Escena 06 — NuncaNegativa

**Objetivo:** deducir que la densidad espectral nunca es negativa, con una
curva imaginaria que baja de cero y el colador puesto encima (cuenta hecha).
Enunciar la fórmula y comprobarla con la telegráfica.

**Qué hace falta saber antes:** escena 05 (área sobre la banda = potencia de
la banda); capítulo 7 (la esperanza de un cuadrado no es negativa).

**Visual:**
- «¿Puede una densidad espectral valer −0,5 en alguna frecuencia?» y una
  pausa.
- Una curva inventada que se hunde a «−0,5» entre 3 y 4 rad/s (y en su
  reflejo). El colador se coloca justo ahí.
- La cuenta por renglones: «área ≈ −0,5 × 1 × 2 = −1», «potencia ≈ −1 / 2π ≈
  −0,16». Un sello rojo: «potencia negativa».
- «E[y²] ≥ 0»: el cuadrado de algo, nunca negativo.
- La parte negativa se estrecha y el colador también: siempre la atrapa.
- «S_xx(jω) ≥ 0 para todo ω»; comprobación con «4/(4 + ω²)»: arriba positivo,
  abajo positivo ✓.

## Narración

<!-- b1 -->
Una pregunta antes de seguir. ¿Puede una densidad espectral valer menos cero
coma cinco en alguna frecuencia? Piénsalo un momento. Tienes todo lo
necesario: sabes qué pasa cuando pones un colador encima de una banda.

<!-- b2 -->
Supongamos que sí. Una curva que se hunde hasta menos cero coma cinco entre
tres y cuatro radianes por segundo, y lo mismo en su reflejo. Ponemos el
colador justo ahí. El área que queda es aproximadamente altura por ancho, dos
veces: menos cero coma cinco por uno, por dos. Menos uno. Dividido entre dos
pi, una potencia de menos cero coma uno seis.

<!-- b3 -->
Pero la potencia de la salida es la esperanza de un cuadrado, y un cuadrado
nunca es negativo. Una potencia negativa es imposible. Así que esa curva no
puede ser la densidad espectral de ningún proceso. Y si la parte negativa
fuera estrechísima, daría igual: el colador se puede estrechar tanto como
quieras, hasta atraparla.

<!-- b4 -->
La conclusión, como fórmula: la densidad espectral es mayor o igual que cero
en todas las frecuencias. Comprobémoslo con la telegráfica: cuatro dividido
entre cuatro más omega al cuadrado. El numerador es positivo, y el
denominador es cuatro más un cuadrado, también positivo. Nunca baja de cero.

<!-- b5 -->
Esta propiedad sale de la potencia. Hay otras dos que salen de la
autocorrelación, y con las tres juntas vamos a poder hacer algo muy útil:
decidir si una función cualquiera puede ser, o no, la autocorrelación de un
proceso.

---

# Escena 07 — RealYPar

**Objetivo:** demostrar que la densidad espectral es real y par: la
autocorrelación es par, el seno es impar, y el área de un par por impar es
cero (con la cuenta en dos puntos). Comprobarlo con las tres barras rho, uno,
rho (rho = 0,4), donde las jotas se cancelan a la vista; de paso, recordar
que en tiempo discreto la frecuencia va de menos pi a pi.

**Qué hace falta saber antes:** escena 04 (la exponencial compleja como
coseno y seno); capítulo 10 (la autocorrelación es real y par).

**Visual:**
- La autocorrelación de la telegráfica y su espejo: «R(−τ) = R(τ)»: «par».
- Un seno: el valor en −τ es el opuesto: «impar».
- El producto R por seno: a la derecha de cero, área positiva; a la
  izquierda, la misma área negativa. Dos puntos: «τ = 1: +0,1», «τ = −1:
  −0,1», «suma 0».
- «e^{−jωτ} = cos(ωτ) − j sen(ωτ)»; el término con j se tacha: «S_xx =
  ∫ R_xx(τ) cos(ωτ) dτ».
- Tres barras «0,4 · 1 · 0,4» en −1, 0 y 1. La transformada:
  «0,4 e^{jΩ} + 1 + 0,4 e^{−jΩ}»; las partes con j se cancelan y queda
  «1 + 0,8 cos Ω», dibujada entre −π y π.

## Narración

<!-- b1 -->
Del capítulo anterior sabemos que la autocorrelación es real y par. Par
quiere decir simétrica como en un espejo: vale lo mismo en tau que en menos
tau. Tiene sentido: parecerse a uno mismo un segundo después es lo mismo que
parecerse a uno mismo un segundo antes.

<!-- b2 -->
Ahora mira la transformada. La exponencial compleja es un coseno menos jota
por un seno, así que la transformada tiene dos partes. La que lleva jota es
el área de la autocorrelación multiplicada por un seno. Y el seno es impar:
en menos tau vale lo contrario que en tau. Par por impar da una función
impar.

<!-- b3 -->
Y el área de una función impar es cero, porque lo de la izquierda cancela lo
de la derecha. Si en tau igual a uno el producto vale cero coma uno, en menos
uno vale menos cero coma uno. Así en cada pareja de puntos. La parte con jota
desaparece, y queda solo el área de la autocorrelación por un coseno: un
número real.

<!-- b4 -->
Además, el coseno no cambia si le das la vuelta a omega. Así que la densidad
espectral vale lo mismo en omega que en menos omega: es par. Real y par,
demostrado. Esa es la razón de la simetría de las dos ventanitas del
colador.

<!-- b5 -->
Veámoslo en un ejemplo de tiempo discreto, donde la frecuencia solo va de
menos pi a pi. Una autocorrelación de tres barras: cero coma cuatro, uno,
cero coma cuatro. Su transformada tiene dos exponenciales, una con más jota y
otra con menos jota. Al sumarlas, los senos se cancelan y queda uno más cero
coma ocho por el coseno de omega. Real y par, a la vista.

---

# Escena 08 — ExamenDeTresPreguntas

**Objetivo:** usar las tres propiedades como examen, con una encuesta: el
rectángulo no puede ser una autocorrelación (su transformada, una sinc, se
hace negativa: cuenta en un punto) y el triángulo sí (es un rectángulo
convolucionado consigo mismo, y su transformada es una sinc al cuadrado).
Recordar la convolución como "deslizar y medir el área común". Advertir la
trampa (parecer razonable no basta) y anunciar que el rectángulo deslizante
volverá.

**Qué hace falta saber antes:** escenas 06 y 07 (las tres propiedades); de
Señales y Sistemas, la convolución y su transformada (se recuerdan aquí).

**Visual:**
- Encuesta: un rectángulo (1 entre −1 y 1) y un triángulo (2 en el cero, 0 en
  ±2). «¿Cuál puede ser una autocorrelación?»: «las dos», «ninguna», «solo
  una». Pausa.
- El rectángulo: tres casillas, «real ✓», «par ✓», «≥ 0 ?». Su transformada
  «2 sen ω / ω» se dibuja; en «ω ≈ 4,7» vale «−0,42»: los lóbulos negativos en
  rojo. Cruz.
- Dos rectángulos, uno se desliza sobre el otro; el área común se anota:
  «desplazamiento 0 → 2», «1 → 1», «2 → 0». Los puntos dibujan el triángulo.
- «F{a ∗ b} = F{a} · F{b}» → «sinc · sinc = sinc²», toda por encima del eje.
  Tilde.

## Narración

<!-- b1 -->
Te proponen dos funciones y te preguntan cuál puede ser la autocorrelación
de algún proceso. Un rectángulo, que vale uno entre menos uno y uno, y cero
fuera. Y un triángulo, que vale dos en el origen y baja en línea recta hasta
cero en más y menos dos. ¿Las dos, ninguna, o solo una? Piénsalo antes de
seguir.

<!-- b2 -->
El rectángulo es real, es par, y vale lo máximo en el origen. Parece que lo
tiene todo. Falta la tercera pregunta, que se contesta en frecuencia. Su
transformada es dos por el seno de omega dividido entre omega: una función
que se llama sinc. Oscila, y no siempre por encima de cero.

<!-- b3 -->
Con un número: en omega igual a cuatro coma siete, el seno vale menos uno, y
la transformada da unos menos cero coma cuatro dos. Negativa. En esa
frecuencia, la densidad espectral sería negativa, y eso es imposible. Así
que el rectángulo, por razonable que parezca, no es la autocorrelación de
ningún proceso.

<!-- b4 -->
El triángulo esconde un truco. Recuerda la convolución de Señales y
Sistemas: deslizas una función sobre otra y, en cada posición, mides el área
común. Desliza el rectángulo sobre sí mismo. Sin desplazamiento, el área
común es dos. Desplazado uno, es uno. Desplazado dos, cero. Sube y baja en
línea recta: el triángulo.

<!-- b5 -->
Y la transformada de una convolución es el producto de las transformadas:
sinc por sinc, la sinc al cuadrado. Un cuadrado nunca es negativo, así que el
triángulo aprueba. Guarda el dibujo del rectángulo deslizándose sobre otro:
volverá cuando intentemos medir un espectro con datos, y será la causa de
casi todos los problemas.

---

# Escena 09 — CorrelacionAUnPaso

**Objetivo:** aplicar el examen a un proceso que solo recuerda a su vecino:
las tres barras rho, uno, rho. Con rho = 0,4 el espectro vale 1,8 · 1 · 0,2 y
es válido; con rho = 0,6 baja a −0,2 y no existe. Deducir que rho no pasa de
un medio (la sorpresa frente al capítulo 7) y explicar por qué tiene sentido.

**Qué hace falta saber antes:** escena 07 (el espectro de las tres barras);
capítulo 7 (rho entre menos uno y uno).

**Visual:**
- Una secuencia de muestras donde cada una se parece a sus vecinas; la
  autocovarianza: tres barras «ρ · 1 · ρ».
- «¿Puede ρ valer 0,6?» y una pausa.
- «1 + 2ρ cos Ω» con ρ = 0,4: tabla «Ω = 0 → 1,8», «π/2 → 1», «π → 0,2». La
  curva, positiva: tilde.
- Un `ValueTracker` sube ρ: el mínimo en π baja, toca cero en «ρ = ½» y en
  «ρ = 0,6» se hunde a «−0,2» en rojo.
- «1 − 2|ρ| ≥ 0 → |ρ| ≤ ½»; al lado, «capítulo 7: |ρ| ≤ 1», tachado a la mitad.

## Narración

<!-- b1 -->
Imagina un proceso en tiempo discreto en el que cada muestra se parece a sus
vecinas inmediatas, con un coeficiente de correlación rho, y no tiene ninguna
relación con las demás. Su autocovarianza son tres barras: rho, uno, rho. En
el capítulo siete vimos que rho puede ir de menos uno a uno. ¿Puede valer
aquí cero coma seis?

<!-- b2 -->
Pasemos el examen. Ya sabemos que el espectro de esas tres barras es uno más
dos rho por el coseno de omega. Con rho igual a cero coma cuatro, en
frecuencia cero vale uno coma ocho; en pi medios, uno; y en pi, cero coma
dos. Siempre positivo: el proceso existe. Y tiene más potencia en las
frecuencias bajas, porque vecinas parecidas dan una señal que cambia
despacio.

<!-- b3 -->
Ahora con cero coma seis. En frecuencia pi, el coseno vale menos uno: uno
menos uno coma dos, menos cero coma dos. Negativo. Ese proceso no puede
existir. En general, el punto más bajo es uno menos dos veces el valor
absoluto de rho, y para que no baje de cero, rho tiene que estar entre menos
un medio y un medio.

<!-- b4 -->
Es una sorpresa: el capítulo siete permitía llegar hasta uno, y aquí solo
llegamos a la mitad. ¿Por qué? Si cada muestra se pareciera muchísimo a la
siguiente, y esa a la siguiente, la primera tendría que parecerse también a
la tercera. Pero hemos dicho que a dos pasos no hay ninguna relación. Pedir
las dos cosas a la vez es contradictorio.

<!-- b5 -->
El examen dice qué es imposible. Pero ¿y lo que aprueba? Que el espectro
salga positivo, ¿garantiza que existe de verdad un proceso con rho igual a
cero coma cuatro? ¿Y cómo se fabricaría?

---

# Escena 10 — Bochner

**Objetivo:** enunciar el teorema de Bochner (la vuelta del examen) y
comprobarlo fabricando rho = 0,4 con un filtro de dos coeficientes (2, 1)
dividido entre raíz de cinco alimentado con una moneda (cuentas hechas).
Intentar rho = 0,6 y ver que el mismo límite aparece como "un cuadrado
negativo". Los extremos: promediar y restar. Anunciar que el filtro volverá.

**Qué hace falta saber antes:** escena 09 (el límite de un medio); capítulo 7
(independientes: la esperanza del producto es el producto de las esperanzas).

**Visual:**
- «Bochner»: una flecha de ida (autocorrelación → real, par, ≥ 0) y otra de
  vuelta (real, par, ≥ 0 → existe un proceso).
- Una moneda que se tira en cada instante: «+1, −1, −1, +1…».
- Un bloque «y[n] = (2 w[n] + w[n−1]) / √5».
- Cuentas por renglones: «E[y²] = (4 + 1)/5 = 1»; «y[n] y y[n−1] comparten
  w[n−1]: 2 · 1 / 5 = 0,4» ✓.
- Con ρ = 0,6: «a² + b² = 1», «ab = 0,6», «(a − b)² = 1 − 1,2 = −0,2» en
  rojo: «un cuadrado negativo».
- Dos filtros: «a = b»: la salida se suaviza (promedia); «a = −b»: alterna
  de signo (resta).

## Narración

<!-- b1 -->
La respuesta es sí, y tiene nombre: el teorema de Bochner, o de Herglotz en
tiempo discreto. Dice que la vuelta también vale: cualquier función real,
par, que nunca baja de cero y con área finita es la densidad espectral de
algún proceso. Y lo mejor es que se puede comprobar fabricándolo. Vamos a
construir rho igual a cero coma cuatro.

<!-- b2 -->
El ingrediente es una moneda: en cada instante sale más uno o menos uno, y
cada tirada es independiente de las demás. Con ella montamos un filtro de dos
coeficientes: la salida es dos veces la moneda de ahora más una vez la
moneda anterior, todo dividido entre raíz de cinco.

<!-- b3 -->
Hagamos las cuentas. La potencia de la salida: dos al cuadrado más uno al
cuadrado, cinco, dividido entre cinco: uno. Los productos cruzados se
promedian a cero porque las monedas son independientes. Y dos salidas
vecinas comparten una moneda, que aparece con peso uno en una y dos en la
otra: dos por uno entre cinco, cero coma cuatro. Fabricado.

<!-- b4 -->
¿Y si intentamos cero coma seis? Con coeficientes a y be, necesitamos que a
al cuadrado más be al cuadrado valga uno, y a por be, cero coma seis.
Entonces a menos be, al cuadrado, vale uno menos dos por cero coma seis:
menos cero coma dos. Un cuadrado negativo. No hay números que lo cumplan: el
mismo límite que dio el espectro.

<!-- b5 -->
No es casualidad: preguntar si el espectro es positivo y preguntar si existe
un filtro que fabrique el proceso es la misma pregunta. Eso dice Bochner. Y
mira los extremos: con rho igual a un medio, los dos coeficientes son
iguales y el filtro promedia vecinas, como el promediador del capítulo
anterior; con menos un medio, las resta. Guarda este filtro: volverá.

---

# Escena 11 — FluctuacionesYMedia

**Objetivo:** separar media y fluctuaciones: la densidad de las fluctuaciones
(FSD) es la transformada de la autocovarianza, y la PSD es la FSD más un
impulso en el origen con la potencia de la media. Con la tensión de 5 V y
desviación 1 V: potencia 26 = 25 + 1, y la comprobación con las áreas.
Explicar qué es un impulso. Por qué se resta la media antes de estimar.

**Qué hace falta saber antes:** escena 04 (área = potencia); capítulo 7
(varianza = esperanza del cuadrado menos la media al cuadrado); capítulo 10
(autocovarianza).

**Visual:**
- Una tensión que oscila alrededor de «5 V»; la línea de la media se separa
  de las oscilaciones: «media» y «fluctuaciones».
- La cuenta: «E[x²] = μ² + σ² = 25 + 1 = 26».
- «R_xx(τ) = C_xx(τ) + μ²»: la autocovarianza sobre un escalón constante de
  altura 25.
- Un pico que se estrecha y crece manteniendo su área: el impulso «δ».
- «S_xx = D_xx + 2π μ² δ(ω)»: la curva de las fluctuaciones y una flecha
  vertical en cero. Áreas: «D_xx: 2π → 1», «impulso: 2π·25 → 25», «total 26» ✓.
- La flecha enorme tapa el resto del espectro; «restar la media» y desaparece.

## Narración

<!-- b1 -->
Muchas señales no oscilan alrededor de cero. Piensa en una tensión que
fluctúa alrededor de cinco voltios, con una desviación típica de un voltio.
Hay dos cosas mezcladas: un valor medio que no cambia nunca, y unas
fluctuaciones que van y vienen alrededor de él. ¿Cuánta potencia tiene?

<!-- b2 -->
Del capítulo siete: la varianza es la esperanza del cuadrado menos la media
al cuadrado. Despejando, la potencia es la media al cuadrado más la
varianza: veinticinco más uno, veintiséis. Veinticinco son de la parte
constante, lo que en electrónica se llama la continua. Solo uno es de las
fluctuaciones.

<!-- b3 -->
Con las autocorrelaciones pasa lo mismo: la autocorrelación es la
autocovarianza más la media al cuadrado. La autocovarianza mide solo las
fluctuaciones, así que su transformada es la densidad espectral de las
fluctuaciones. Se escribe de sub equis equis. ¿Y la media al cuadrado? Es
una constante, y la transformada de una constante es un impulso.

<!-- b4 -->
Un impulso es un pico infinitamente estrecho con un área fija: toda la
potencia concentrada en un solo punto, la frecuencia cero. Así que la
densidad espectral es la de las fluctuaciones más un impulso en el origen de
área dos pi por la media al cuadrado. Comprobación: la curva aporta uno, el
impulso aporta veinticinco. Veintiséis.

<!-- b5 -->
Esto tiene una consecuencia práctica. Si la media es grande, ese impulso se
lleva casi toda la potencia, y cuando se estima el espectro con datos,
derrama sobre las frecuencias vecinas y tapa lo que queríamos ver. Por eso,
antes de estimar un espectro, lo primero es restar la media.

---

# Escena 12 — LaCuentaDeLaTelegrafica

**Objetivo:** pagar la promesa de la escena 04: calcular la densidad de la
telegráfica, dos alfa sobre alfa al cuadrado más omega al cuadrado, paso a
paso (partir en dos mitades, integrar una exponencial que decae, sumar
fracciones, jota al cuadrado igual a menos uno). Con alfa igual a dos, sale
cuatro sobre cuatro más omega al cuadrado. Pasar el examen y ver la media
altura en omega igual a alfa.

**Qué hace falta saber antes:** escena 04 (definición y la promesa); escena
03 (autocorrelación de la telegráfica).

**Visual:**
- «R_xx(τ) = e^{−α|τ|}»; el eje partido en cero: «τ < 0» y «τ > 0».
- Recordatorio: «∫₀^∞ e^{−aτ} dτ = 1/a» con «a = 2 → ½» (el área bajo una
  exponencial que decae).
- Mitad derecha: «∫₀^∞ e^{−(α + jω)τ} dτ = 1/(α + jω)»; mitad izquierda, su
  espejo: «1/(α − jω)».
- La suma con denominador común, por renglones: numerador «(α − jω) + (α +
  jω) = 2α»; denominador «α² − (jω)² = α² + ω²» con «j² = −1» resaltado.
- «2α/(α² + ω²)»; con α = 2: «4/(4 + ω²)», la de la escena 04 ✓.
- Puntos: «ω = 0 → 1», «ω = 2 → 4/8 = ½».

## Narración

<!-- b1 -->
Hace dos episodios prometimos una cuenta: la densidad espectral de la onda
telegráfica. Su autocorrelación es e elevado a menos alfa por el valor
absoluto de tau, donde alfa es dos lambda, el doble del ritmo de saltos. El valor absoluto obliga a partir la integral en dos
mitades: a la derecha del cero, donde tau es positivo, y a la izquierda,
donde es negativo.

<!-- b2 -->
Una herramienta primero: el área bajo una exponencial que decae, e elevado a
menos a por tau, desde cero hasta infinito, vale uno sobre a. Con a igual a
dos, un medio. En la mitad derecha, la autocorrelación por la exponencial
compleja da e elevado a menos alfa más jota omega, por tau. Es lo mismo con
a igual a alfa más jota omega: uno sobre alfa más jota omega.

<!-- b3 -->
La mitad izquierda es su espejo, y da uno sobre alfa menos jota omega. Ahora
sumamos las dos fracciones con denominador común. Arriba: alfa menos jota
omega más alfa más jota omega. Las jotas se cancelan y queda dos alfa.
Abajo: alfa al cuadrado menos jota omega al cuadrado.

<!-- b4 -->
Y jota al cuadrado es menos uno, porque jota es la raíz de menos uno. Menos
por menos: alfa al cuadrado más omega al cuadrado. Resultado: dos alfa
dividido entre alfa al cuadrado más omega al cuadrado. Con alfa igual a dos,
cuatro dividido entre cuatro más omega al cuadrado. La que usamos. Promesa
cumplida.

<!-- b5 -->
Pasa el examen: es real, es par porque solo aparece omega al cuadrado, y
nunca es negativa. Y miremos dos puntos. En frecuencia cero vale uno. En
omega igual a dos, cuatro entre ocho: un medio. La curva cae a la mitad
justo en omega igual a alfa. Y eso le da a alfa un segundo significado.

---

# Escena 13 — MemoriaYAncho

**Objetivo:** ver con el `ValueTracker` que alfa es a la vez la velocidad de
olvido y el ancho de banda: memoria corta, espectro ancho (cuentas con alfa =
8 y alfa = 0,5). Recordar la dualidad pulso estrecho ↔ espectro ancho. En el
extremo, la sinusoide de fase aleatoria: memoria infinita, espectro de
líneas. Dejar la pregunta de qué da memoria cero, con encuesta.

**Qué hace falta saber antes:** escena 12 (la densidad y su media altura en
alfa); capítulo 10 (sinusoide de fase aleatoria), que se recuerda.

**Visual:**
- Par autocorrelación ↔ espectro lado a lado con un `ValueTracker` en α.
- «α = 8»: «R(0,5) = e^{−4} ≈ 0,02»; «S(0) = 2/8 = 0,25», media altura en 8:
  bajo y ancho. «α = 0,5»: «S(0) = 4», media altura en 0,5: alto y estrecho.
  El área se mantiene: «potencia = 1».
- Rótulos «memoria corta ↔ espectro ancho», «memoria larga ↔ espectro
  estrecho». Un pulso estrecho con espectro ancho, como recordatorio.
- Una sinusoide de fase aleatoria; su autocorrelación, un coseno que no
  decae; su espectro, dos flechas en «±ω₀».
- Encuesta: «memoria cero → ¿una raya en cero?, ¿nada?, ¿plano?». Pausa.

## Narración

<!-- b1 -->
En el capítulo anterior, dos lambda era la velocidad a la que el interruptor
olvida, y prometimos que reaparecería disfrazada de ancho de banda. Aquí
está: alfa, que es dos lambda, también es la frecuencia donde el espectro
cae a la mitad. Movamos alfa y veamos
las dos curvas a la vez.

<!-- b2 -->
Con alfa igual a ocho, la señal salta muy a menudo. A medio segundo, la
autocorrelación ya vale cero coma cero dos: casi lo ha olvidado todo. Y el
espectro vale cero coma dos cinco en el origen y cae a la mitad en ocho:
bajo y ancho. Con alfa igual a cero coma cinco, al revés: la señal recuerda
mucho, y el espectro es alto y estrecho.

<!-- b3 -->
Fíjate en que el área no cambia: la potencia sigue siendo uno. Lo que el
espectro pierde en altura lo gana en anchura. La regla es esta: memoria
corta, espectro ancho; memoria larga, espectro estrecho. Es la dualidad de
Fourier de Señales y Sistemas, la del pulso estrecho con espectro ancho,
aplicada a la memoria de un proceso.

<!-- b4 -->
Llevémoslo al extremo. Una sinusoide con fase al azar, del capítulo
anterior, tiene como autocorrelación un coseno que no decae nunca: recuerda
para siempre. Y su espectro son solo dos rayas, dos impulsos en más y menos
su frecuencia. Toda la potencia en dos puntos. Se llama espectro de líneas.

<!-- b5 -->
Memoria infinita, dos rayas. ¿Y un proceso que no recuerda absolutamente
nada, en el que cada instante no tiene relación con ningún otro? ¿Su
espectro sería una raya en cero, no tendría nada, o sería plano? Piénsalo.

---

# Escena 14 — RuidoBlanco

**Objetivo:** presentar el ruido blanco con la moneda: cuentas de la
potencia (uno) y de la correlación entre vecinas (cero); autocovarianza de
una sola barra y espectro plano. Explicar el impulso discreto delta de m.
El nombre (luz blanca) y el de coloreado.

**Qué hace falta saber antes:** escena 13 (la pregunta); escena 10 (la
moneda); escena 07 (transformada en discreto).

**Visual:**
- La moneda: «+1, −1, −1, +1, −1…».
- Cuentas: «x² = 1 siempre → E[x²] = 1». Vecinas: cuatro combinaciones «(+,+)
  → +1», «(+,−) → −1», «(−,+) → −1», «(−,−) → +1», promedio «0».
- La autocovarianza: una sola barra en cero, «δ[m]: 1 en m = 0, 0 fuera».
- Su transformada: «1 · e⁰ = 1» en todas las frecuencias: una línea
  horizontal de −π a π.
- Un prisma: luz blanca que se abre en todos los colores con la misma
  intensidad. Al lado, los espectros de la telegráfica y de ρ = 0,4:
  «coloreados» (como `c11-blanco-vs-coloreado.svg`).
- «C_xx[m] = K δ[m] ⟷ D_xx = K».

## Narración

<!-- b1 -->
Vuelve a la moneda: en cada instante, más uno o menos uno, cada tirada
independiente. Su potencia es fácil: más uno o menos uno, al cuadrado, dan
siempre uno. ¿Y cuánto se parecen dos tiradas vecinas? Hay cuatro
combinaciones igual de probables. Si coinciden, el producto es más uno; si
no, menos uno. Dos y dos: el promedio es cero.

<!-- b2 -->
Y lo mismo a cualquier distancia. Así que la autocovarianza es una única
barra de altura uno en el origen, y cero en todo lo demás. Eso se escribe
delta de eme: vale uno cuando eme es cero y cero en otro caso. Su
transformada tiene un solo término, uno por e elevado a cero: uno, para
todas las frecuencias.

<!-- b3 -->
El espectro es completamente plano: la misma potencia en todas las
frecuencias. Esa era la respuesta: memoria cero, espectro plano. Y si cada
muestra tuviera varianza ka en lugar de uno, el espectro sería plano a
altura ka. Una barra de altura ka en el tiempo, una línea de altura ka en
frecuencia.

<!-- b4 -->
A este proceso se lo llama ruido blanco, por analogía con la luz: la luz
blanca es una mezcla de todos los colores con la misma intensidad. Un
proceso cuyo espectro tiene forma, con más potencia en unas frecuencias que
en otras, se llama coloreado. La onda telegráfica y el proceso de rho igual
a cero coma cuatro son ruidos coloreados.

<!-- b5 -->
El blanco es el ingrediente básico de todo el curso: con él fabricamos el
proceso del episodio anterior, y con él fabricaremos cualquier otro color.
Pero tiene dos sorpresas guardadas, y una de ellas es que, en cierto sentido,
no existe.

---

# Escena 15 — LasSorpresasDelBlanco

**Objetivo:** dos sorpresas. Primera: un espectro plano obliga a media cero
(encuesta; el impulso negativo en la FSD, con la cuenta para media 5).
Segunda: en tiempo continuo, un espectro plano tiene área infinita (cuentas
con 1.000 y un millón de rad/s): el blanco continuo es una idealización,
como el impulso de Dirac, y el ruido térmico se le parece mucho. En discreto,
existe.

**Qué hace falta saber antes:** escena 14 (blanco); escena 11 (PSD = FSD +
impulso de la media); escena 06 (nunca negativa).

**Visual:**
- Encuesta: «¿puede un ruido de espectro plano tener media 5?»: «sí», «no»,
  «depende». Pausa.
- Renglones: «S_xx = K (plano)»; «D_xx = S_xx − 2π μ² δ»; «= K − 2π·25·δ»: la
  línea plana con una flecha hacia abajo en rojo en el cero. Sello: «FSD
  negativa: imposible» → «μ = 0».
- Tiempo continuo: la línea plana de altura 1 que se extiende; el área se
  anota: «hasta 1.000 rad/s → 2.000», «hasta 1.000.000 → 2.000.000», «→ ∞».
- Un impulso de Dirac al lado: «idealización».
- Una resistencia: «ruido térmico: plano hasta billones de hercios». Un
  aparato real que corta mucho antes.

## Narración

<!-- b1 -->
Primera sorpresa. ¿Puede un ruido de espectro plano tener media cinco? Sí,
no, ¿depende? Piénsalo con lo que sabemos de la media: aparece en el
espectro como un impulso en el origen.

<!-- b2 -->
La respuesta es no. Si el espectro es plano a altura ka y la media fuera
cinco, la densidad de las fluctuaciones sería el espectro menos el impulso
de la media: ka menos dos pi por veinticinco en el origen. Un impulso que
apunta hacia abajo: una densidad negativa en frecuencia cero. Imposible. Así
que un espectro plano obliga a que la media sea cero.

<!-- b3 -->
Segunda sorpresa, en tiempo continuo. Allí la frecuencia no se acaba en pi:
llega hasta el infinito. Un espectro plano de altura uno hasta mil radianes
por segundo, contando las negativas, tiene área dos mil. Hasta un millón,
dos millones. Hasta el infinito, área infinita. Es decir, potencia infinita.
El ruido blanco continuo no puede existir.

<!-- b4 -->
Y aun así lo usamos, igual que usamos el impulso de Dirac, que tampoco
existe: es una idealización cómoda que da buenos resultados si se interpreta
bien. El ruido térmico de una resistencia es plano hasta frecuencias de
billones de hercios. Cualquier aparato real corta mucho antes, y en lo que
deja pasar, es indistinguible del blanco.

<!-- b5 -->
En tiempo discreto, en cambio, el blanco existe de verdad: la moneda. Resumen
del episodio: sin memoria, espectro plano, media cero. Hasta aquí hemos
trabajado con autocorrelaciones conocidas. Pero en la vida real nadie te da
la autocorrelación. Te dan un archivo con datos.

---

# Escena 16 — Periodograma

**Objetivo:** el camino del laboratorio: recortar la realización a una
ventana, recordar Parseval, definir el periodograma y comprobar su área con
la telegráfica; tomar esperanza y alargar la ventana (Einstein-Wiener-
Khinchin). El paso clave: el solapamiento de la ventana con su copia
desplazada es el triángulo de la escena 08 (bucle pagado).

**Qué hace falta saber antes:** escena 02 (por qué no se transforma una
realización); escena 08 (el rectángulo deslizante y el triángulo).

**Visual:**
- Una grabación larga de la telegráfica; una ventana de «−T» a «T» recorta un
  tramo de 10 s; el resto se apaga.
- Parseval: «energía = (1/2π) ∫ |X_T(jω)|² dω»: |X_T|² reparte la energía por
  frecuencia.
- «periodograma = |X_T(jω)|² / 2T»; comprobación: «energía 10 / 10 s = 1» ✓.
- La fórmula de EWK por piezas: «S_xx(jω) =», «lím T→∞», «(1/2T) E[|X_T(jω)|²]».
- El producto «x(σ) x(σ − τ)» solo existe donde la ventana y su copia
  desplazada se solapan: los dos rectángulos de la escena 08, deslizándose.
  Aparece el triángulo. «E[periodograma] ⟷ R_xx(τ) · triángulo».

## Narración

<!-- b1 -->
Tienes una grabación de ruido de diez segundos y quieres su espectro. La
idea del laboratorio es la del principio, con una corrección: si la
realización entera no tiene transformada, recortemos un trozo. Una ventana
de menos te a te. Lo que queda dentro empieza y termina, tiene energía
finita, y su transformada existe.

<!-- b2 -->
De Señales y Sistemas, el teorema de Parseval: la energía de una señal es el
área bajo el módulo al cuadrado de su transformada, dividida entre dos pi.
Así que ese módulo al cuadrado reparte la energía del trozo por frecuencias.
Si lo dividimos entre la duración, dos te, reparte la potencia. Eso se llama
periodograma.

<!-- b3 -->
Comprobémoslo con la telegráfica: en diez segundos, energía diez; entre diez
segundos, potencia uno. El área del periodograma dividida entre dos pi da
uno. Ahora tomamos esperanza, para no depender de la grabación concreta, y
alargamos la ventana hasta el infinito. Sale la densidad espectral de
siempre. Es el teorema de Einstein, Wiener y Khinchin.

<!-- b4 -->
El camino del laboratorio y el de la autocorrelación llegan al mismo sitio.
Pero en el laboratorio la ventana nunca es infinita, así que lo que importa
es qué medimos antes del límite. Y aquí vuelve el dibujo que prometimos. La
autocorrelación compara la señal con su copia desplazada tau. Dentro de la
ventana, eso solo se puede hacer donde la ventana y su copia se solapan.

<!-- b5 -->
Y el solapamiento de dos rectángulos que se deslizan es un triángulo: el de
hace dos episodios. Así que con una ventana finita no medimos la
autocorrelación, sino la autocorrelación multiplicada por un triángulo. El
paso completo está en el apunte en profundidad. Lo importante es qué le hace
ese triángulo al espectro.

---

# Escena 17 — ElDesenfoque

**Objetivo:** cuentas del triángulo con una ventana de 10 s; multiplicar por
el triángulo en el tiempo es convolucionar con una sinc al cuadrado en
frecuencia, explicado como desenfoque (promedio ponderado de vecinos).
Resolución: con una ventana de L segundos no se separan tonos más cercanos
que 1/L hercios; los tonos de 50 y 50,5 Hz con 1 s y con 4 s.

**Qué hace falta saber antes:** escena 16 (el triángulo); escena 08 (sinc al
cuadrado; transformada de un producto y de una convolución).

**Visual:**
- El triángulo de una ventana de 10 s: «τ = 0 → 1», «τ = 5 s → ½», «τ = 10 s
  → 0». Encima, la autocorrelación de la telegráfica, que muere en 2 s,
  donde el triángulo vale casi 1.
- «producto en el tiempo ⟷ convolución en frecuencia»: la densidad
  verdadera y una sinc al cuadrado que se desliza; cada punto se reemplaza
  por el promedio ponderado de sus vecinos: una foto que se desenfoca.
- Dos rayas de «50 Hz» y «50,5 Hz»; con «1 s», dos campanas de ancho «1 Hz»
  que se funden en un bulto; con «4 s», campanas de «0,25 Hz» separadas.
- «resolución ≈ 1 / duración».

## Narración

<!-- b1 -->
Pongamos números. Con una ventana de diez segundos, el triángulo vale uno en
tau igual a cero, un medio en cinco segundos y cero en diez. La
autocorrelación de la telegráfica ya se ha apagado a los dos segundos, y
ahí el triángulo casi no ha bajado. Con una ventana larga, el triángulo
apenas estropea nada.

<!-- b2 -->
Pero ¿qué hace en frecuencia? Multiplicar en el tiempo es convolucionar en
frecuencia. Y convolucionar con una campana estrecha es desenfocar: cada
punto del espectro se reemplaza por un promedio ponderado de sus vecinos,
como una foto movida. Aquí la campana es la transformada del triángulo, una
sinc al cuadrado.

<!-- b3 -->
Lo que medimos, en promedio, es el espectro verdadero desenfocado. Y el
desenfoque depende de la ventana: cuanto más larga, más estrecha es la sinc
al cuadrado y más nítido el resultado. Cuando la ventana crece sin límite,
el desenfoque desaparece, y eso es exactamente lo que dice el teorema.

<!-- b4 -->
El desenfoque tiene una consecuencia muy concreta. Dos tonos, uno de
cincuenta hercios y otro de cincuenta y medio. Con un segundo de grabación,
cada tono se convierte en una campana de un hercio de ancho, y las dos se
funden en un solo bulto. Con cuatro segundos, las campanas miden un cuarto de
hercio, y se ven dos picos.

<!-- b5 -->
La regla: con una ventana de ele segundos, no se distinguen tonos más
cercanos que uno sobre ele hercios. Para separar cincuenta y cincuenta y
medio, hacen falta al menos dos segundos. La resolución la da el tiempo de
grabación. Pero hay un problema peor, que alargar la ventana no arregla.

---

# Escena 18 — PeriodogramaRuidoso

**Objetivo:** mostrar que un periodograma crudo tiembla tanto como vale
(encuesta con tres opciones) y que grabar más no lo arregla: afina los picos
pero no los baja, porque cada frecuencia sigue siendo una sola muestra.
Relacionarlo con el capítulo 7 (una medida sola no se acerca a la media) y
dejar insinuado que es una sola muestra del ensemble.

**Qué hace falta saber antes:** escena 16 (periodograma); capítulo 7 (el
promedio de muchas medidas se acerca a la media).

**Visual:**
- La densidad verdadera de la moneda (plana a 1) y su periodograma de 1 s: un
  bosque de picos y valles.
- Encuesta: «grabas diez veces más: A) se aplana, B) picos más finos pero
  igual de altos, C) no cambia nada». Pausa. Se tachan A y C.
- El periodograma de 10 s: picos más finos y más numerosos, igual de altos.
- Una frecuencia aislada: su valor cambia en cada grabación; «media 1,
  desviación 1».
- Una grabación sola frente al ensemble de mil: «una muestra del ensemble».

## Narración

<!-- b1 -->
Calcula el periodograma de un segundo de la moneda. El espectro verdadero es
plano, a altura uno. Lo que sale es un bosque de picos y valles: algunos
llegan a tres o cuatro, otros casi a cero, y ninguno significa nada. Ahora
la pregunta: si grabas diez veces más, ¿se aplana, los picos se hacen más
finos pero igual de altos, o no cambia nada?

<!-- b2 -->
Los picos se hacen más finos, pero igual de altos. El bosque se vuelve más
denso, pero no más bajo. En cada frecuencia, el periodograma sale en promedio
uno, que es lo correcto, pero tiembla alrededor de ese uno con una
desviación típica de uno: tanto como vale.

<!-- b3 -->
¿Por qué no ayuda grabar más? Porque una grabación más larga permite ver
más frecuencias, más juntas, pero cada una sigue siendo una sola medida. Es
lo del capítulo siete: una única medida con ruido no se acerca a la media
por mucho que la mires. Hacen falta muchas medidas, y promediarlas.

<!-- b4 -->
Hay otra forma de verlo. La densidad espectral es un promedio sobre el
ensemble, sobre mil grabaciones posibles. Un periodograma usa una sola. Es
estimar un promedio con una única muestra. Lo raro sería que saliera bien.

<!-- b5 -->
La solución también la conocemos del capítulo siete: promediar muchas
medidas. Pero aquí tenemos una sola grabación, y un periodograma por
grabación. ¿Qué podemos promediar, entonces?

---

# Escena 19 — PromediarTrozos

**Objetivo:** partir la grabación en M trozos, promediar sus periodogramas y
ver que la varianza cae como 1/M (recordando sigma cuadrado sobre n del
capítulo 7). Con 16 s de grabación: 16 trozos de 1 s (suave, 1 Hz de
resolución) contra 4 de 4 s (ruidoso, separa los tonos). Las dos perillas y
el compromiso: solo más datos mejoran las dos cosas.

**Qué hace falta saber antes:** escenas 17 (resolución = 1/duración) y 18
(ruido del periodograma); capítulo 7 (varianza del promedio, banda de
Chebyshev que se angosta).

**Visual:**
- La grabación partida en M trozos; sus periodogramas se apilan y se
  promedian; el promedio se pega a la densidad verdadera (como
  `c11-periodograma.svg`).
- La banda del capítulo 7 que se angosta, ahora alrededor del espectro:
  «varianza / M», «desviación / √M».
- Grabación de «16 s»: «16 trozos de 1 s → desviación ¼, resolución 1 Hz»;
  «4 trozos de 4 s → desviación ½, resolución 0,25 Hz»; «1 trozo de 16 s →
  desviación 1». Los tonos de 50 y 50,5 Hz en cada caso.
- Dos perillas: «M → temblor», «duración de cada trozo → resolución».
  «M × duración = grabación total».

## Narración

<!-- b1 -->
Partimos la grabación en trozos, calculamos el periodograma de cada uno y
los promediamos. Del capítulo siete: la varianza del promedio de ene medidas
independientes es la varianza de una dividida entre ene, y la desviación
típica se divide entre la raíz de ene. Aquí igual: con eme trozos, la
varianza se divide entre eme.

<!-- b2 -->
Con números. Tienes dieciséis segundos de grabación. Si haces dieciséis
trozos de un segundo, la desviación se divide entre raíz de dieciséis,
cuatro: el espectro tiembla un cuarto de lo que temblaba. Una curva suave.
Pero cada trozo dura un segundo, y la resolución es de un hercio: los tonos
de cincuenta y cincuenta y medio salen fundidos.

<!-- b3 -->
Si haces cuatro trozos de cuatro segundos, la resolución es de un cuarto de
hercio, y los dos tonos se separan. Pero solo promedias cuatro: la
desviación se divide entre dos, y la curva tiembla bastante. Y con un solo
trozo de dieciséis segundos, la resolución es excelente, pero vuelves al
bosque de picos.

<!-- b4 -->
Hay dos perillas, y conviene no confundirlas. El número de trozos controla
cuánto tiembla la estimación. La duración de cada trozo controla la
resolución y el desenfoque. Y el número de trozos por la duración de cada
uno es la grabación entera: con una grabación fija, subir una perilla baja
la otra.

<!-- b5 -->
O una curva suave con los picos borrosos, o picos nítidos ahogados en
temblor. Ninguna elección gana en todo, y la única forma de mejorar las dos
cosas es grabar durante más tiempo. Y todavía queda un tercer problema, que
aparece en el momento mismo de cortar la señal con tijeras.

---

# Escena 20 — Fuga

**Objetivo:** explicar la fuga (leakage): la FFT trata el trozo como
periódico; con un tono de 10 Hz en 1 s pega perfecto, con 10,5 Hz queda un
salto, y un salto tiene todas las frecuencias. En frecuencia: raya → sinc con
lóbulos laterales. Advertir la trampa: en el caso de 10 Hz la fuga también
está, pero no se ve. Motivar los decibelios.

**Qué hace falta saber antes:** escena 17 (la ventana desenfoca); escena 08
(la sinc y sus lóbulos); de Señales y Sistemas, que un escalón necesita
todas las frecuencias (se recuerda).

**Visual:**
- Un tono de 10 Hz en 1 s: caben 10 ciclos exactos. El trozo se repite a
  continuación de sí mismo: la unión es perfecta. FFT: una raya limpia.
- Un tono de 10,5 Hz: diez ciclos y medio; al repetir el trozo, queda un
  salto en la unión, en rojo.
- Un escalón y su espectro, que no se acaba nunca: «un salto tiene todas las
  frecuencias».
- En frecuencia: la raya se convierte en un lóbulo principal con faldas a los
  lados (como `c11p-leakage.svg`). «fuga (leakage)».
- El caso de 10 Hz otra vez: la misma sinc de fondo, con los puntos de la FFT
  cayendo justo en sus ceros.

## Narración

<!-- b1 -->
Graba un tono puro de diez hercios durante un segundo y calcula su espectro
con la FFT, el algoritmo que usa cualquier ordenador para hacer Fourier con
datos. Sale una raya limpia en diez hercios. Ahora repite con un tono de diez
hercios y medio. La raya ya no es limpia: tiene unas faldas que se extienden
a los lados.

<!-- b2 -->
La explicación está en cómo trabaja la FFT: trata el trozo como si se
repitiera para siempre, pegado a sí mismo. Con diez hercios, en un segundo
caben diez ciclos exactos, y la unión es perfecta. Con diez y medio, caben
diez ciclos y medio: al pegar el final con el principio, queda un salto.

<!-- b3 -->
Y un salto, como un escalón, necesita todas las frecuencias para dibujarse.
Así que en el espectro aparece potencia donde no debería haber: la raya se
convierte en una sinc, con un lóbulo principal y lóbulos laterales que bajan
muy despacio. Esa potencia que se escapa a los lados se llama fuga.

<!-- b4 -->
Una trampa: en el caso de diez hercios, la fuga también está. La sinc es la
misma. Lo que pasa es que la FFT solo mira el espectro en algunos puntos, y
esos puntos caen justo en los ceros de la sinc. No es que no haya fuga: es
que no la estás mirando. En datos reales, esa coincidencia no ocurre nunca.

<!-- b5 -->
La fuga es peligrosa cuando hay un tono fuerte y otro débil cerca: las
faldas del fuerte pueden tapar al débil. ¿Cuánto más débil? Para hablar de
potencias tan distintas necesitamos una escala adecuada.

---

# Escena 21 — Decibelios

**Objetivo:** explicar los decibelios desde cero (diez veces el logaritmo en
base diez del cociente; ×10 → 10 dB, ×100 → 20 dB, ×1.000.000 → 60 dB,
mitad → −3 dB, recordando la media altura de la telegráfica). Aplicarlo a la
fuga: el primer lóbulo lateral de la rectangular está a −13 dB; un tono 60 dB
más débil queda enterrado.

**Qué hace falta saber antes:** escena 20 (fuga y lóbulos laterales); escena
12 (la media altura en omega igual a alfa).

**Visual:**
- Dos tonos, uno de potencia 1 y otro de una millonésima, en escala lineal:
  el pequeño no se ve.
- Una regla vertical: «×10 → 10 dB», «×100 → 20 dB», «×1.000 → 30 dB»,
  «×1.000.000 → 60 dB». La fórmula «10 log₁₀(P₁/P₂)».
- «½ → 10 · log₁₀ 0,5 ≈ −3 dB», con la curva de la telegráfica y su media
  altura: «−3 dB».
- El núcleo de la ventana rectangular en dB: lóbulo principal a 0, primer
  lateral «−13 dB» («≈ 1/20»), los siguientes más abajo.
- Un tono débil a «−60 dB» al lado de uno fuerte cuyas faldas pasan por «−30
  dB»: el débil, tapado.

## Narración

<!-- b1 -->
Si un tono tiene potencia uno y otro una millonésima, en una gráfica normal
el pequeño es invisible: una millonésima de la altura. Para ver a la vez
cosas tan distintas se cuentan ceros, es decir, se usa el logaritmo. Los
decibelios son exactamente eso: diez veces el logaritmo en base diez del
cociente entre dos potencias.

<!-- b2 -->
Con números. Diez veces más potencia son diez decibelios, porque el
logaritmo de diez es uno. Cien veces, veinte. Mil veces, treinta. Un millón,
sesenta. Cada diez decibelios, un cero más. Y la mitad de la potencia son
unos menos tres decibelios: el punto de media altura de la telegráfica, en
omega igual a alfa, estaba a menos tres decibelios.

<!-- b3 -->
Ahora miremos la fuga con esta regla. Con la ventana rectangular, el primer
lóbulo lateral está a menos trece decibelios del pico: más o menos una
vigésima parte. Y los siguientes bajan, pero despacio: bastante lejos del
pico, las faldas siguen a treinta o cuarenta decibelios por debajo.

<!-- b4 -->
Pongamos un tono débil, sesenta decibelios por debajo del fuerte, una
millonésima de su potencia, al lado. Allí las faldas del fuerte están a
menos treinta: mil veces por encima del débil. El tono débil queda
enterrado. Si buscas un armónico pequeño en una señal, cortar con una
ventana rectangular te lo esconde.

<!-- b5 -->
Hace falta, entonces, una forma de cortar que derrame menos. Y la idea es
sencilla: el problema era el salto en los bordes. Si no cortamos de golpe,
no hay salto.

---

# Escena 22 — Ventanas

**Objetivo:** las ventanas suaves (Hann, Blackman): multiplicar el trozo por
una campana que baja a cero en los bordes. Lóbulos laterales −13 / −31 / −58
dB, a cambio de un lóbulo principal más ancho (1, 2, 3 veces): el
compromiso. Cuándo usar cada una, con los tonos de 50 y 50,5 Hz.

**Qué hace falta saber antes:** escenas 20 y 21 (fuga, decibelios); escena
17 (resolución).

**Visual:**
- El trozo del tono de 10,5 Hz multiplicado por una campana (Hann, un coseno
  levantado): los bordes bajan a cero, el salto desaparece.
- Tres ventanas en el tiempo (rectangular, Hann, Blackman) y sus núcleos en
  dB; una tabla que se llena: «−13 dB · ancho 1», «−31 dB · ancho 2», «−58 dB ·
  ancho 3» (como `c11p-ventanas.svg`).
- El tono a −60 dB: con Hann asoma apenas; con Blackman se distingue.
- Los tonos de 50 y 50,5 Hz con 2 s: con la rectangular, dos picos; con Hann,
  un bulto; con 4 s y Hann, dos picos.
- Tres fichas: «Hann: por defecto», «Blackman: algo pequeño junto a algo
  enorme», «rectangular: máxima resolución, amplitudes parecidas».

## Narración

<!-- b1 -->
En lugar de cortar de golpe, multiplicamos el trozo por una campana que
empieza en cero, sube suave y vuelve a cero en los bordes. Así el final y el
principio del trozo valen los dos cero, y al pegarlos no hay salto. A esa
campana se la llama ventana. La más usada es la de Hann, que tiene forma de
coseno levantado.

<!-- b2 -->
El efecto en la fuga es enorme. Con la ventana rectangular, el primer lóbulo
lateral estaba a menos trece decibelios. Con la de Hann, a menos treinta y
uno. Con otra todavía más suave, la de Blackman, a menos cincuenta y ocho.
Con Blackman, el tono débil de antes, sesenta decibelios por debajo, por fin
tiene una oportunidad de asomar.

<!-- b3 -->
Pero no hay nada gratis. Cuanto más suave es la ventana, más ancho es su
lóbulo principal: el de Hann mide el doble que el de la rectangular, y el de
Blackman, el triple. Y un lóbulo principal más ancho es más desenfoque.
Menos fuga a cambio de peor resolución.

<!-- b4 -->
Con los tonos de cincuenta y cincuenta y medio y dos segundos de grabación,
la rectangular los separa justo. Con la de Hann, el doble de ancha, se
funden, y hacen falta cuatro segundos. Así que cada ventana tiene su uso. La
de Hann, por defecto. La de Blackman, cuando hay algo pequeño junto a algo
enorme. La rectangular, cuando manda la resolución y las amplitudes se
parecen.

<!-- b5 -->
La ventana decide cómo se deforma el espectro, y la resolución la sigue
dando el tiempo grabado. Pero hay un atajo muy tentador, y muy extendido,
para mejorar la resolución sin grabar más. Veamos si funciona.

---

# Escena 23 — RellenarConCeros

**Objetivo:** desmontar la confusión clásica del zero-padding con una
encuesta: rellenar con ceros suaviza la curva pero no separa dos tonos que la
ventana fundió (64 muestras contra 64 + relleno contra 256). Por qué: la
curva de fondo ya la fijaron los datos; los ceros solo la evalúan en más
puntos. Para qué sí sirve.

**Qué hace falta saber antes:** escena 20 (la FFT mira el espectro en
algunos puntos); escena 17 (resolución = tiempo grabado).

**Visual:**
- 64 muestras de dos tonos muy cercanos; su FFT: unos pocos puntos y un solo
  bulto.
- Encuesta: «añades 2.000 ceros al final y repites la FFT: ¿aparecen dos
  picos?»: «sí», «no». Pausa.
- Con el relleno: una curva suave y completa… con un solo bulto. Sin datos
  nuevos: «interpolación, no información».
- 256 muestras reales: dos picos, justo en las dos frecuencias (como
  `c11p-zeropadding.svg`).
- La curva de fondo de las 64 muestras dibujada en gris: la FFT sin relleno
  toca pocos puntos de ella; con relleno, muchos; la curva es la misma.
- Dos tildes: «ubicar un pico único», «no subestimar su altura»; una cruz:
  «separar dos picos».

## Narración

<!-- b1 -->
Tienes sesenta y cuatro muestras de dos tonos muy cercanos, y la FFT te da
unos pocos puntos con un solo bulto. Alguien te sugiere añadir dos mil ceros
al final de los datos y volver a calcular la FFT, que así tendrá muchos más
puntos. ¿Aparecerán los dos picos? Piénsalo.

<!-- b2 -->
No. La curva sale mucho más suave, bonita y completa. Y sigue siendo un solo
bulto. En cambio, si en lugar de ceros tienes doscientas cincuenta y seis
muestras de verdad, aparecen dos picos, justo en las dos frecuencias.

<!-- b3 -->
La razón es la de la fuga: la FFT mira el espectro en algunos puntos. Con
sesenta y cuatro muestras, el espectro que hay debajo ya está decidido,
desenfocado por una ventana de sesenta y cuatro. Los ceros no son datos: no
cambian esa curva, solo hacen que la FFT la mire en más puntos. Es
interpolación, no información.

<!-- b4 -->
¿Entonces rellenar con ceros no sirve? Sí sirve, para dos cosas: ubicar con
más precisión un pico que ya sabes que es único, y no subestimar su altura
cuando cae entre dos puntos de la FFT. Lo que no hace nunca es separar dos
cosas que la ventana ya fundió.

<!-- b5 -->
La regla, otra vez: la resolución solo se compra con tiempo grabado. Y con
esto ya tenemos todas las piezas. Falta juntarlas en el método que se usa
de verdad.

---

# Escena 24 — Welch

**Objetivo:** el método de Welch: restar la media, trozos solapados por la
mitad, ventana de Hann, promedio. Por qué solapar (bordes y más trozos: de 8
a 15, desviación 1,4 veces menor). El permiso de la ergodicidad (las pilas
del capítulo 10). La regla de repetir con otro tramo.

**Qué hace falta saber antes:** escenas 19, 22 (trozos, Hann); escena 11
(restar la media); capítulo 10 (ergodicidad, pilas), que se recuerda.

**Visual:**
- Cuatro fichas que se encienden: «restar la media», «trozos solapados a la
  mitad», «ventana de Hann», «promediar».
- Un registro partido en trozos solapados, cada uno con su campana de Hann
  (como `c11p-welch.svg`); lo que en uno cae en el borde, en el siguiente cae
  en el centro.
- «sin solapar: 8 trozos → con solapamiento: 15»; «√(15/8) ≈ 1,4».
- Las pilas (mismo icono y cajón que en el capítulo 10): cada realización es una línea constante; el promedio en el
  tiempo de una da su propio voltaje, no el del ensemble. «ergodicidad =
  permiso».
- Dos estimaciones de dos tramos distintos: un pico que está en las dos
  (tilde) y otro que solo está en una (cruz).

## Narración

<!-- b1 -->
El método que se usa en la práctica junta todo lo que hemos visto, y se
llama método de Welch. Primero, se resta la media. Segundo, se parte la
grabación en trozos que se solapan por la mitad. Tercero, a cada trozo se le
aplica una ventana de Hann. Y cuarto, se promedian todos los periodogramas.

<!-- b2 -->
¿Por qué solapar? La ventana de Hann aplasta los bordes de cada trozo, así
que sin solapamiento esas muestras casi no cuentan. Solapando, lo que en un
trozo cae en el borde, en el siguiente cae en el centro. Y de paso salen casi
el doble de trozos: de ocho a quince, y la desviación se divide entre uno
coma cuatro. Una mejora modesta, pero gratis.

<!-- b3 -->
Detrás del método hay un salto que conviene mirar de frente. La densidad
espectral es un promedio sobre el ensemble, sobre todas las grabaciones
posibles. Y nosotros estamos promediando trozos de una sola grabación, a lo
largo del tiempo. ¿Con qué permiso?

<!-- b4 -->
Con el de la ergodicidad, del capítulo anterior. Recuerda las pilas: cada
realización es una tensión constante, y promediar en el tiempo da el voltaje
de esa pila, no el de todas. Si el proceso no es ergódico, promediar más
tiempo no te acerca a la densidad espectral del ensemble, sino a la del trozo
de ensemble que te ha tocado.

<!-- b5 -->
Y una regla práctica, de la misma familia que "mira la nube antes que el
número". Si en una estimación aparece un pico llamativo, repítela con otro
tramo de datos. Lo que es real vuelve a aparecer; el temblor del estimador,
no. Con esto ya sabemos medir un espectro. Lo siguiente es usarlo.

---

# Escena 25 — PicosQueDelatan

**Objetivo:** para qué sirve un espectro: el electrocardiograma, con un pico
en 0,166 Hz que delata la respiración (cuenta: 6 s, 10 respiraciones por
minuto). En un bloque, el teorema del muestreo para procesos limitados en
banda (error de potencia cero). Plantear la pregunta de fabricar un proceso
con el espectro que se quiera.

**Qué hace falta saber antes:** escena 24 (estimar con Welch); escena 13
(espectro de líneas); de Señales y Sistemas, el teorema del muestreo (se
recuerda).

**Visual:**
- Un electrocardiograma que late (efecto `latido`); debajo, la frecuencia
  cardíaca instantánea: «70, 68, 72, 69…», una línea que sube y baja sin orden.
- Su espectro estimado: un pico nítido en «0,166 Hz».
- Cuentas: «1 / 0,166 ≈ 6 s», «60 / 6 = 10 respiraciones por minuto». Un pecho
  que sube y baja al ritmo del pico.
- Un espectro nulo por encima de «B»; muestras «más de 2B por segundo» y la
  reconstrucción: «E[(x − x̂)²] = 0».
- Un altavoz en pruebas y un canal de comunicaciones: «¿cómo fabrico un ruido
  con este espectro?».

## Narración

<!-- b1 -->
Un electrocardiograma registra los latidos del corazón. A partir de él se
calcula la frecuencia cardíaca instante a instante: setenta, sesenta y ocho,
setenta y dos. Vista en el tiempo, parece una línea que sube y baja sin
ningún orden. Pero si le estimamos la densidad espectral, aparece algo que a
simple vista no se ve.

<!-- b2 -->
Un pico nítido en cero coma uno seis seis hercios. Una oscilación que se
repite cada uno entre cero coma uno seis seis segundos: unos seis segundos.
Diez veces por minuto. Y diez veces por minuto es justo el ritmo al que
respiraba la persona. El espectro revela que al respirar el corazón acelera
y frena.

<!-- b3 -->
Un pico marcado en un espectro delata algo que se repite, como las rayas de
la sinusoide de hace unos episodios. Otra herramienta de Señales y Sistemas
que sobrevive al azar es el teorema del muestreo: si una señal no tiene
frecuencias por encima de be, basta con tomar más de dos be muestras por
segundo para reconstruirla.

<!-- b4 -->
Con procesos pasa lo mismo: si la densidad espectral vale cero por encima de
be, las muestras bastan. No se reconstruye cada realización punto a punto,
pero el error tiene potencia cero, y en la práctica eso es lo mismo.

<!-- b5 -->
Hasta aquí hemos usado el espectro para mirar. También sirve para fabricar.
Si quieres probar un altavoz con un ruido de una forma concreta, o simular el
ruido de un canal de comunicaciones, necesitas generar un proceso con la
densidad espectral que tú elijas. ¿Cómo se consigue?

---

# Escena 26 — FiltroModelador

**Objetivo:** fabricar un proceso con la PSD que se quiera: ruido blanco por
un filtro cuyo módulo al cuadrado es esa PSD (el filtro modelador, un factor
espectral). Comprobarlo con el filtro (2, 1)/√5 de la escena 10 (su módulo al
cuadrado es 1 + 0,8 cos Ω) y con el eco del 0,6 del capítulo 10
(correlaciones 0,6, 0,36, 0,22). Pagar Bochner: construir así el proceso es la demostración del
teorema.

**Qué hace falta saber antes:** escena 05 (el filtro multiplica la densidad
por la ganancia al cuadrado); escena 10 (el filtro que fabricó rho = 0,4);
escena 14 (la moneda es blanca).

**Visual:**
- La moneda entra en un `BloqueLTI` «H»: el espectro plano entra, sale uno con
  forma. Luz blanca por un vidrio de color.
- «D_xx = |H|² · 1» → «|H| = √D_xx».
- El filtro de la escena 10: «|2 + e^{−jΩ}|² / 5 = (4 + 1 + 4 cos Ω)/5 = 1 +
  0,8 cos Ω» ✓, junto al espectro de la escena 09.
- El eco (el sensor de temperatura del capítulo 10, correlación × 0,6 por paso, mismo dibujo):
  «x[n] = 0,6 x[n−1] + w[n]»; una cadena de muestras donde cada una arrastra
  el 60 % de la anterior; correlaciones «0,6», «0,6 · 0,6 = 0,36», «0,22»; su
  espectro, concentrado en frecuencias bajas.
- El rótulo «Bochner» de la escena 10 vuelve y se le pega el bloque del
  filtro: «la demostración».

## Narración

<!-- b1 -->
Empezamos por lo fácil: el ruido blanco, la moneda, con su espectro plano de
altura uno. Lo pasamos por un filtro. La densidad espectral de la salida es
la ganancia al cuadrado por la de la entrada, que es uno. Así que si quiero
una densidad concreta, necesito un filtro cuya ganancia al cuadrado sea esa
densidad. Como pasar luz blanca por un vidrio de color.

<!-- b2 -->
Ya lo hemos hecho sin decirlo. El filtro que fabricó rho igual a cero coma
cuatro, dos veces la moneda más la anterior entre raíz de cinco, tiene una
ganancia al cuadrado que, desarrollada, es cuatro más uno más cuatro por el
coseno de omega, entre cinco. Es decir, uno más cero coma ocho por el coseno
de omega. El espectro de aquel proceso.

<!-- b3 -->
Otro ejemplo, con eco: las fluctuaciones del sensor de temperatura del
capítulo anterior. La salida es cero
coma seis veces la salida anterior más una moneda nueva: cada muestra
arrastra el sesenta por ciento de la anterior. Las vecinas se parecen cero
coma seis; a dos pasos, cero coma seis al cuadrado, cero coma tres seis; a
tres, cero coma dos dos. Memoria que se borra poco a poco, y un espectro
concentrado en las frecuencias bajas.

<!-- b4 -->
Un filtro así se llama modelador, porque le da forma al espectro plano del
blanco, y su ganancia es una especie de raíz cuadrada de la densidad: se la
llama factor espectral. Siempre existe, porque la densidad nunca es negativa
y se le puede sacar la raíz.

<!-- b5 -->
Y ahora vuelve al teorema de Bochner: toda función real, par y no negativa
es la densidad de algún proceso. La demostración es exactamente esto. Le
sacas la raíz, construyes el filtro, le metes ruido blanco, y lo que sale
es ese proceso. Cada vez que se colorea un ruido con un filtro, se está
ejecutando la demostración.

---

# Escena 27 — FiltroBlanqueador

**Objetivo:** el problema inverso: blanquear un ruido coloreado. Para qué
(capítulos 12 y 13: blanquear primero). El blanqueador tiene ganancia al
cuadrado igual a una constante sobre la PSD: es el inverso del modelador.
Con el eco: la resta x[n] − 0,6 x[n−1] devuelve la moneda exacta (cuenta) y
la tabla simulada lo confirma.

**Qué hace falta saber antes:** escena 26 (modelador, eco del 0,6); escena 13
(la memoria está en la autocorrelación).

**Visual:**
- Dos cadenas de bloques: «blanco → H → coloreado» y «coloreado → 1/H →
  blanco».
- «|H_w|² = σ_w² / S_xx»: el espectro coloreado y la ganancia del
  blanqueador, alta donde el espectro es bajo; su producto, plano.
- Renglones: «x[n] = 0,6 x[n−1] + w[n]» → «u[n] = x[n] − 0,6 x[n−1]» → «u[n] =
  w[n]».
- Una tabla que se llena distancia a distancia: «x: 1 · 0,60 · 0,36 · 0,22 ·
  0,13» y «u: 1 · 0,00 · 0,003 · −0,001 · 0,00» (400.000 muestras).
- Una flecha hacia los capítulos 12 y 13: «blanquear primero».

## Narración

<!-- b1 -->
Ahora el camino contrario, que es el que más vamos a usar en los dos
capítulos siguientes. Tengo un ruido coloreado y quiero convertirlo en
blanco. ¿Para qué? Porque muchos problemas de estimación y de detección
tienen solución conocida cuando el ruido es blanco. La estrategia es
blanquear primero y aplicar después lo que ya sabemos.

<!-- b2 -->
El filtro que lo hace se llama blanqueador, y su ganancia al cuadrado es una
constante dividida entre la densidad espectral. Amplifica donde el ruido
tiene poca potencia y atenúa donde tiene mucha, hasta dejarlo plano. Si el
modelador convertía blanco en coloreado, el blanqueador es su inverso.

<!-- b3 -->
Con el eco se ve a mano. El modelador hacía: equis de ene es cero coma seis
por la equis anterior, más la moneda. Pues el blanqueador hace: equis de ene
menos cero coma seis por la equis anterior. Sustituye la primera ecuación en
la segunda: el cero coma seis se cancela, y lo que queda es la moneda. Exacta.

<!-- b4 -->
Comprobémoslo con datos: cuatrocientas mil muestras simuladas. Antes del
blanqueador, las correlaciones con las vecinas son cero coma seis, cero coma
tres seis, cero coma dos dos, cero coma uno tres. Después: cero, cero
coma cero cero tres, menos cero coma cero cero uno, cero. Toda la memoria,
borrada.

<!-- b5 -->
Modelador y blanqueador son uno el inverso del otro. Pero hay un detalle que
hemos pasado por alto. El factor espectral, la raíz cuadrada del espectro,
no es único. Hay más de un filtro que fabrica el mismo proceso. Y a la hora
de deshacerlo, no todos sirven.

---

# Escena 28 — FaseMinima

**Objetivo:** ver con números que el factor espectral no es único: los
filtros (2, 1) y (1, 2) divididos entre raíz de cinco fabrican el mismo
proceso (rho = 0,4). Invertirlos a mano: uno se apaga (½, −¼, ⅛) y el otro
explota (1, −2, 4, −8). Fase mínima = el factor cuya inversa no explota,
causal y estable. Y la idea de Paley-Wiener: no se puede blanquear lo que no
existe. Sembrar el capítulo 12.

**Qué hace falta saber antes:** escena 10 (filtro de dos coeficientes, rho =
0,4); escena 27 (blanqueador = inverso).

**Visual:**
- Dos bloques: «(2 w[n] + w[n−1]) / √5» y «(w[n] + 2 w[n−1]) / √5». Cuentas de
  los dos: «(4 + 1)/5 = 1», «2 · 1 / 5 = 0,4». El mismo espectro «1 + 0,8 cos Ω»
  debajo de los dos.
- Inversa del primero: «w[n] = (√5 y[n] − w[n−1]) / 2»; su respuesta a un
  impulso: barras «½, −¼, ⅛, −1/16…» que se apagan. Tilde.
- Inversa del segundo: «w[n] = √5 y[n] − 2 w[n−1]»: barras «1, −2, 4, −8, 16…»
  que se salen de la pantalla. Cruz.
- «fase mínima»: «el que tiene el coeficiente grande primero», «su inverso
  no explota: causal y estable».
- Un espectro que vale cero en toda una banda: el blanqueador tendría que
  multiplicar por infinito. Cruz. «no se puede blanquear lo que no existe».

## Narración

<!-- b1 -->
Volvamos al filtro que fabricó rho igual a cero coma cuatro: dos veces la
moneda de ahora más la anterior, entre raíz de cinco. Ahora dale la vuelta a
los coeficientes: una vez la de ahora más dos veces la anterior. Potencia:
uno más cuatro, entre cinco, uno. Vecinas: uno por dos, entre cinco, cero
coma cuatro. El mismo proceso, con otro filtro.

<!-- b2 -->
Los dos sirven como modelador. Veamos si sirven como blanqueador:
intentemos recuperar la moneda a partir de la salida. Con el primero,
despejando, cada moneda es la salida menos la moneda anterior, dividido
entre dos. Si le metemos un único impulso, la respuesta es un medio, menos un
cuarto, un octavo: cada vez la mitad. Se apaga. Funciona.

<!-- b3 -->
Con el segundo, cada moneda es la salida menos dos veces la moneda anterior.
Ahora el impulso da uno, menos dos, cuatro, menos ocho, dieciséis: cada vez
el doble. Explota. Ese blanqueador es inestable: cualquier pequeño error se
multiplica hasta el infinito. El filtro modela bien, pero no se puede
deshacer.

<!-- b4 -->
De todos los filtros que fabrican el mismo proceso, hay uno cuya inversa no
explota: aquí, el que pone el coeficiente grande primero. Se llama factor de
fase mínima, y es el único que permite blanquear en tiempo real, con un
filtro causal y estable. En el próximo capítulo será una pieza central.

<!-- b5 -->
Y un límite que ningún blanqueador puede saltarse. Si el proceso no tiene
nada de potencia en toda una banda, para dejarlo plano habría que
multiplicar esa banda por infinito. No se puede blanquear lo que no existe.
En el capítulo que viene esta idea tendrá nombre propio.

---

# Escena 29 — DensidadCruzada

**Objetivo:** dos procesos: la correlación cruzada (recordada) y su
transformada, la densidad espectral cruzada, que puede ser compleja porque
la cruzada no es par. Explicar los números complejos como flechas con módulo
y ángulo, y multiplicar por la exponencial como girar. Con el micrófono que
capta la voz retrasada medio segundo: módulo = la densidad de la voz, ángulo
= −0,5 ω (media vuelta en 1 Hz).

**Qué hace falta saber antes:** escena 07 (si la función no es par, la parte
con jota no se cancela); escena 04 (exponencial compleja); capítulo 10
(correlación cruzada), que se recuerda.

**Visual:**
- La voz «x» y un micrófono lejano que la capta medio segundo tarde: «y(t) =
  x(t − 0,5)».
- «R_yx(τ) = E[y(t) x(t − τ)]»: la correlación cruzada, con el pico en «τ =
  0,5»: no es par.
- Un número complejo como flecha: «módulo» (largo) y «ángulo»; «e^{−jθ}»:
  girar θ sin cambiar el largo.
- «S_yx(jω) = S_xx(jω) · e^{−jω·0,5}»: en cada frecuencia, una flecha de largo
  S_xx que gira más cuanto mayor es ω; en «ω = 2π (1 Hz)»: ángulo «−π», media
  vuelta.
- Dos rótulos: «módulo = cuánto comparten», «ángulo = desfase».

## Narración

<!-- b1 -->
Hasta ahora hemos mirado un proceso cada vez. Pero en señales casi siempre
hay dos: lo que se envía y lo que se recibe, la voz y lo que capta un
micrófono lejano. Del capítulo anterior, la correlación cruzada mide cuánto
se parece uno a una copia desplazada del otro. Su transformada se llama
densidad espectral cruzada.

<!-- b2 -->
Un ejemplo: el micrófono capta la voz medio segundo tarde. La correlación
cruzada tiene su pico en tau igual a cero coma cinco, no en cero: ya no es
par. Y si no es par, la parte con jota de la transformada no se cancela. La
densidad cruzada es un número complejo en cada frecuencia.

<!-- b3 -->
Un número complejo se puede ver como una flecha en el plano: tiene un largo,
que se llama módulo, y un ángulo. Y multiplicar por e elevado a menos jota
por un ángulo es girar la flecha ese ángulo, sin cambiar su largo. Es la
forma más cómoda de pensar en ellos.

<!-- b4 -->
En el ejemplo, la densidad cruzada es la densidad de la voz por e elevado a
menos jota omega por cero coma cinco. El módulo es la densidad de la voz:
cuánta potencia comparten las dos señales en esa frecuencia. El ángulo es
menos cero coma cinco por omega: en un hercio, omega es dos pi, y la flecha
gira media vuelta.

<!-- b5 -->
Así que la densidad cruzada dice dos cosas en cada frecuencia: cuánto se
parecen las dos señales, en el módulo, y cuánto están desfasadas, en el
ángulo. Y como con las variables del capítulo siete, hay un límite a cuánto
pueden parecerse. Recuerda la parábola.

---

# Escena 30 — CauchySchwarzPorFrecuencia

**Objetivo:** pagar la promesa del capítulo 7: la desigualdad |D_yx|² ≤ D_xx
D_yy es Cauchy-Schwarz con la misma parábola, en cada frecuencia (la
densidad de la mezcla no puede ser negativa → discriminante ≤ 0). El retardo
solo se nombra. Comprobar la igualdad con el micrófono sin ruido: una copia
exacta es como rho igual a uno.

**Qué hace falta saber antes:** capítulo 7 (la parábola de Cauchy-Schwarz y
el discriminante), que se recuerda; escena 06 (nunca negativa); escena 29
(densidad cruzada, módulo).

**Visual:**
- La parábola del capítulo 7 (mismo dibujo): «Var(X + λY) ≥ 0»,
  «λ²σ_Y² + 2λσ_XY + σ_X² ≥ 0», «discriminante ≤ 0 → σ_XY² ≤ σ_X² σ_Y²».
- Ahora con procesos: «z = x + α y (retrasada)»; «D_zz(ω) = D_yy α² + 2(…) α
  + D_xx ≥ 0»: la misma parábola, repetida en varias frecuencias a lo largo del
  eje omega.
- «|D_yx(jω)|² ≤ D_xx(jω) D_yy(jω)» construida por piezas, alineada debajo de
  la del capítulo 7.
- Comprobación con el micrófono: «|S_yx|² = S_xx²», «S_yy = S_xx»:
  «S_xx · S_xx»: igualdad. La parábola toca el eje: «como ρ = 1».

## Narración

<!-- b1 -->
En el capítulo siete demostramos que la covarianza al cuadrado nunca supera
el producto de las varianzas. El truco era mezclar las dos variables con un
número lambda: la varianza de la mezcla nunca es negativa, y desarrollada es
una parábola en lambda. Una parábola que nunca baja de cero tiene el
discriminante menor o igual que cero. De ahí salía todo.

<!-- b2 -->
Ahora con procesos. Mezclamos equis con una versión de i griega multiplicada
por un número alfa, y a veces retrasada. La densidad espectral de la mezcla,
en una frecuencia cualquiera, es una parábola en alfa: la densidad de i
griega por alfa al cuadrado, más un término con la cruzada por alfa, más la
densidad de equis.

<!-- b3 -->
Y la densidad espectral de la mezcla nunca es negativa. Es la misma
parábola que nunca baja de cero, en cada frecuencia por separado. Su
discriminante da la desigualdad: el módulo de la densidad cruzada al
cuadrado no supera el producto de las dos densidades. El retardo sirve para
girar la flecha y quedarse con el módulo entero: el detalle está en el
apunte en profundidad.

<!-- b4 -->
Es la parábola de Cauchy-Schwarz del capítulo siete, la misma que en el
capítulo anterior acotó la autocovarianza. Y aún volverá una vez más, en el
capítulo trece. Comprobémoslo con el
micrófono. El módulo de la cruzada es la densidad de la voz, y al cuadrado,
la densidad de la voz al cuadrado. La densidad del micrófono es la misma que
la de la voz, porque retrasar no cambia la potencia.

<!-- b5 -->
Así que los dos lados son iguales: la parábola toca el eje. En el capítulo
siete, tocar el eje era rho igual a uno, una variable exactamente una recta
de la otra. Aquí es lo mismo: el micrófono es una copia exacta de la voz,
sin nada de azar añadido. Cuanto más ruido añada la sala, más se separarán
los dos lados. Y eso tiene una medida.

---

# Escena 31 — Coherencia

**Objetivo:** definir la coherencia (un rho por frecuencia, |γ| ≤ 1) y su
cuadrado como la fracción de la potencia del micrófono que explica la voz.
Con el micrófono que capta la voz más ruido independiente de la sala: 3 a 1
da 0,75 y 1 a 3 da 0,25 (cuentas hechas). La idea del capítulo: en cada
frecuencia, dos procesos son dos variables. Pagar la pregunta de la escena
01.

**Qué hace falta saber antes:** escena 30 (la desigualdad); capítulo 7 (rho
como coseno, y estimar = proyectar).

**Visual:**
- «γ_yx = D_yx / √(D_xx D_yy)», «|γ| ≤ 1»; al lado, «ρ = σ_XY / (σ_X σ_Y)» del
  capítulo 7.
- El micrófono: «y = voz + ruido de la sala» (azul y magenta).
- Dos frecuencias con sus barras: «voz 3, ruido 1»: «|γ|² = 3² / (3 · 4) =
  0,75»; «voz 1, ruido 3»: «1² / (1 · 4) = 0,25».
- La coherencia dibujada a lo largo del eje omega: alta donde manda la voz,
  baja donde manda el murmullo.
- El eje omega partido en rebanadas; en cada rebanada, dos flechas con un
  ángulo (el dibujo del capítulo 7).
- La voz y el murmullo de la escena 01 con el colador: donde la coherencia es
  alta, pasa; donde es baja, se atenúa.

## Narración

<!-- b1 -->
Si dividimos la densidad cruzada entre la raíz del producto de las dos
densidades, sale un número que nunca pasa de uno en módulo: la coherencia.
Es exactamente lo que era rho en el capítulo siete, la covarianza dividida
entre las desviaciones típicas, pero calculado en cada frecuencia. Un
rho para cada frecuencia.

<!-- b2 -->
Un ejemplo con números. Ahora el micrófono capta la voz más el ruido de la
sala, que no tiene nada que ver con la voz. En una frecuencia, la voz tiene
potencia tres y el ruido, uno. La cruzada solo recoge la voz: módulo tres.
El micrófono tiene tres más uno, cuatro. Coherencia al cuadrado: tres al
cuadrado entre tres por cuatro. Cero coma siete cinco.

<!-- b3 -->
En otra frecuencia, al revés: voz uno, ruido tres. Uno al cuadrado entre uno
por cuatro: cero coma dos cinco. La coherencia al cuadrado es la fracción de
lo que capta el micrófono que viene de la voz. En la primera frecuencia, el
micrófono es casi todo voz; en la segunda, casi todo ruido.

<!-- b4 -->
Esta es la idea que se lleva el capítulo: en frecuencia, dos procesos se
analizan, en cada frecuencia por separado, como dos variables aleatorias.
Mismo rho, misma desigualdad, las mismas dos flechas con un ángulo. Y ya
sabemos qué se hace con dos variables: estimar una a partir de la otra,
proyectando una flecha sobre la otra.

<!-- b5 -->
Vuelve a la grabación del principio: la voz y el murmullo. Donde la
coherencia es alta, fíate del micrófono y déjalo pasar. Donde es baja,
atenúalo. Eso es casi el colador que buscábamos en la primera escena. Pero
antes de usar la coherencia, hay que saber estimarla sin engañarse.

---

# Escena 32 — LaTrampaDeLaCoherencia

**Objetivo:** la trampa de estimar coherencia con un solo trozo: da siempre
uno (encuesta; cuenta con X = 3, Y = 4), como rho con dos puntos. Con M
trozos, dos señales sin relación dan una coherencia aparente de uno sobre M
(M = 8 → 0,12, simulado). La regla práctica. Dejar preparado el puente al
capítulo 12.

**Qué hace falta saber antes:** escena 31 (coherencia); escena 19 (promediar
trozos); capítulo 7 (rho con dos puntos, mirar la nube).

**Visual:**
- Dos grabaciones sin ninguna relación (dos ruidos distintos). Encuesta:
  «coherencia estimada con un solo trozo: 0, 0,5 o 1». Pausa.
- La cuenta: «X = 3, Y = 4», «|X · Y*| = 12», «√(|X|² |Y|²) = √(9 · 16) = 12»,
  «12 / 12 = 1». Con otros números, lo mismo.
- Dos puntos con una recta que pasa por ellos: «ρ = ±1 siempre» (capítulo 7).
- Una tabla: «M = 1 → 1», «2 → 0,5», «8 → 0,12», «64 → 0,016»: «≈ 1/M».
- La regla: «creer solo coherencias bastante mayores que 1/M»; «menos de ~10
  trozos: no reportar».
- Para el cierre: la voz, el murmullo y el colador que cambia de forma
  frecuencia a frecuencia.

## Narración

<!-- b1 -->
La coherencia se estima igual que la densidad espectral: partiendo en trozos
y promediando. Pero tiene una trampa. Toma dos grabaciones que no tienen
absolutamente nada que ver. Estima su coherencia con un solo trozo. ¿Qué
sale: cero, cero coma cinco, o uno? Piénsalo.

<!-- b2 -->
Sale uno. Siempre. Con un solo trozo, en cada frecuencia hay un número
complejo para cada señal; pongamos que sus módulos son tres y cuatro.
Arriba, el módulo del producto: doce. Abajo, la raíz de nueve por dieciséis:
doce. Doce entre doce, uno. Con cualquier otro par de números pasa lo mismo:
arriba y abajo es el mismo número.

<!-- b3 -->
No es un resultado experimental, es una identidad: da uno aunque las señales
no tengan ninguna relación. Es la misma trampa que un rho calculado con dos
puntos, que siempre vale uno o menos uno, porque por dos puntos siempre pasa
una recta. Otra vez: mira la nube antes que el número.

<!-- b4 -->
Promediar lo arregla, pero despacio. Con dos grabaciones sin relación, la
coherencia al cuadrado estimada con eme trozos sale, en promedio, uno sobre
eme. Con ocho trozos, cero coma uno dos: parece que hay algo, y no hay nada.
La regla: solo creer coherencias bastante mayores que uno sobre eme, y con
menos de unos diez trozos, no creer ninguna.

<!-- b5 -->
Con esto el capítulo tiene todas sus herramientas: un espectro para cada
proceso, uno cruzado para cada pareja, y una forma honesta de medirlos. Y en
cada frecuencia, dos procesos son dos variables. Separar la voz del murmullo
es, entonces, estimar una variable a partir de otra, frecuencia por
frecuencia.
