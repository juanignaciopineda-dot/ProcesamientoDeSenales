# Episodio 6 — ¿Cuándo llegó el eco?

Capítulo 13 (Detección de señales), episodio 6 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 23 a 26), más un gancho y un cierre nuevos.

**Estado:** escenas `s01`–`s22` animadas; borrador 480p15 de 8:45 con 0 avisos y `ritmo.py` sin huecos de más de 4 s. Falta: revisión del texto ⭐ (gancho y cierre, paso 9), visto bueno del usuario al mp4 (paso 15), pronunciaciones de oído y render final.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Dos pulsos con la misma energía detectan un avión igual de bien. Pero con uno de ellos, dos aviones cercanos parecen uno solo.»
- ⭐ Escena 22 (cierre), bloque 1: «Hoy hemos visto que, si no sabes cuándo llega el eco, el pico de la salida lo mide; que un pulso largo con la autocorrelación estrecha lo vuelve nítido y separa dos ecos; y que buscar en muchos sitios cuesta señal.» Bloque 2: «Hasta ahora decidíamos solo entre «hay señal» y «no hay». ¿Y si mandaron una entre varias señales posibles, y hay que decir cuál? Ese es el próximo episodio: ¿cuál de ellas mandaron?» Anuncia el E7 por su título.

Retoques de frases del guion base, porque el episodio se ve suelto:
- escena 26, bloque 5: se parte en dos. Hasta «comparaciones múltiples» queda como segundo bloque de la escena 21. El resto («Hasta ahora decidíamos… Ese es el último episodio») pasa al cierre (escena 22), que anuncia el E7 por su título: «Ese es el último episodio» → «Ese es el próximo episodio: ¿cuál de ellas mandaron?».
- escena 25, bloque 5: «Ya lo vimos: solo importa la energía» se mantiene (se dijo en el E3, escena 13).

Reparto de las escenas del guion base: 23 → escenas 03 a 07; 24 → 08 a 12; 25 → 13 a 17; 26 → 18 a 21 (con el primer tramo del bloque 5 en la 21); el cierre es la 22.
Solo se partieron bloques enteros en escenas atómicas: el resto del texto del guion base no cambia.

Bucles de este episodio: el pico de la salida es la autocorrelación (E4, escena 15 → escenas 03 a 05 y 08); «la forma no importa, solo la energía» (E3, escena 13 → escena 17, que lo recuerda con ruido blanco; el E5 lo matizó con ruido con memoria); el pulso `(2, 2, 1)` y el filtro `(1, 2, 2)` con su salida `(2, 6, 9, 6, 2)` (escenas 04 y 05); los decibelios del Cap. 11 (escenas 12 y 21); la cola de la campana y la función Q del E3 (escenas 20 y 21); buscar cuesta (escena 03 → 18 a 21); el cierre abre el E7 («¿Cuál de ellas mandaron?»).

---

# Escena 01 — Gancho

**Capítulo YouTube:** Dos pulsos, un solo avión

## Narración

<!-- b1 -->
Dos pulsos con la misma energía detectan un avión igual de bien. Pero con uno de ellos, dos aviones cercanos parecen uno solo.

- «Dos pulsos» → `dos`: entran dos pulsos, uno rectangular de unos y uno con signos alternados, uno encima del otro
- «la misma energía» → `energia`: a ambos se les pone «E = 13» en ámbar
- «detectan un avión igual de bien» → `igual`: un avión con una tilde verde junto a cada pulso
- «Pero con uno de ellos» → `pero`: el pulso rectangular se resalta
- «dos aviones cercanos» → `cercanos`: dos aviones juntos aparecen junto al pulso rectangular
- «parecen uno solo» → `uno`: la salida del filtro es una meseta única y los dos aviones se funden en uno

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** ¿Cuándo llegó el eco?

## Narración

<!-- b1 -->
¿Cuándo llegó el eco?

- «¿Cuándo» → `t1`: «¿Cuándo» entra con rebote
- «llegó el eco?» → `t2`: «llegó el eco?» entra debajo, con la etiqueta «Capítulo 13 · Detección de señales»

---

# Escena 03 — ElRadar

**Capítulo YouTube:** El radar y el retardo del eco
**Objetivo:** que quien mira entienda que el retardo del eco es lo que se quiere medir y cómo se traduce en distancia.

## Narración

<!-- b1 -->
Un radar mide distancias con el tiempo. El pulso sale, choca con el avión y vuelve; cuanto más tarde en volver, más lejos está. Con la velocidad de la luz, un milisegundo de ida y vuelta son ciento cincuenta kilómetros. Así que el retardo del eco no es un dato, es lo que queremos medir.

- «Un radar mide distancias» → `radar`: entra el radar (antena) a la izquierda
- «con el tiempo» → `tiempo`: un reloj pequeño junto al radar
- «El pulso sale» → `sale`: del radar sale hacia la derecha un pulso de tres barras azules
- «choca con el avión» → `choca`: el pulso llega a un avión lejano con un destello
- «y vuelve» → `vuelve`: del avión regresa el eco, más tenue
- «cuanto más tarde en volver» → `tarde`: el minutero del reloj gira y una línea de tiempo marca la ida y la vuelta
- «más lejos está» → `lejos`: el avión se aleja un poco a la derecha
- «Con la velocidad de la luz» → `luz`: aparece «300.000 km/s»
- «un milisegundo de ida y vuelta» → `ms`: «1 ms» sobre la línea de tiempo
- «ciento cincuenta kilómetros» → `km`: la cuenta «300.000 · 0,001 / 2 = 150 km»
- «el retardo del eco» → `retardo`: una llave sobre la línea de tiempo con «D»
- «es lo que queremos medir» → `medir`: «D = ?» en ámbar, grande

---

# Escena 04 — ElRegistroConRetardo

**Capítulo YouTube:** Un eco a mano, sin ruido
**Objetivo:** ver con números cómo la salida del filtro adaptado es la autocorrelación desplazada.

## Narración

<!-- b1 -->
Veámoslo con números, sin ruido. Nuestro pulso, dos, dos, uno, llega con un retardo de tres muestras: el registro es cero, cero, cero, dos, dos, uno, cero, cero. Lo pasamos por el filtro adaptado, uno, dos, dos. La salida es cero, cero, cero, dos, seis, nueve, seis, dos, cero, cero. Es la misma autocorrelación de antes, solo que desplazada.

- «Veámoslo con números» → `numeros`: se limpia la pantalla y aparece una tira de muestras n = 0 a 7
- «sin ruido» → `sinruido`: una etiqueta «sin ruido» en cian
- «Nuestro pulso, dos, dos, uno» → `pulso`: las barras (2, 2, 1) en azul entran a la izquierda de la tira
- «llega con un retardo de tres muestras» → `retardo3`: las barras se desplazan tres lugares, con una llave «D = 3»
- «el registro es cero, cero, cero» → `ceros`: los tres primeros casilleros marcan 0
- «dos, dos, uno, cero, cero» → `resto`: se completa el registro con 2, 2, 1, 0, 0
- «Lo pasamos por el filtro adaptado» → `filtro`: entra el bloque del filtro con h dentro
- «uno, dos, dos» → `h`: dentro del bloque se dibujan las barras (1, 2, 2)
- «La salida es cero, cero, cero» → `salida0`: la tira de salida empieza a llenarse con tres ceros
- «dos, seis, nueve» → `sube`: aparecen 2, 6 y 9, el 9 más alto
- «seis, dos, cero, cero» → `baja`: se completa con 6, 2, 0, 0
- «la misma autocorrelación de antes» → `autocorr`: al lado se dibuja la autocorrelación (2, 6, 9, 6, 2) del E4 y las dos coinciden
- «solo que desplazada» → `desplazada`: una flecha de la autocorrelación a la salida con «desplazada 3»

---

# Escena 05 — ElPicoDaElRetardo

**Capítulo YouTube:** El máximo de la salida mide el retardo
**Objetivo:** que el instante del pico, menos el retardo del filtro, es el retardo del eco.

## Narración

<!-- b1 -->
El pico está en el instante cinco. Restamos el retardo del propio filtro, dos muestras, y sale tres: justo el retardo con el que llegó el pulso. En general, si el eco llega con cierto retardo, la salida es la autocorrelación corrida esas mismas muestras. Buscamos el máximo de la salida, y su posición nos dice el retardo.

- «El pico está» → `pico`: se resalta el 9 de la salida
- «en el instante cinco» → `cinco`: bajo el 9 aparece «n = 5»
- «Restamos el retardo del propio filtro» → `resta`: aparece el filtro con una marca «retardo del filtro»
- «dos muestras» → `dosm`: «− 2» junto a n = 5
- «y sale tres» → `tres`: «5 − 2 = 3» en verde
- «justo el retardo con el que llegó el pulso» → `justo`: una flecha lleva el 3 hasta la llave «D = 3» y coinciden
- «con el que llegó el pulso» → `llego`: el pulso del registro se ilumina en la posición 3
- «si el eco llega con cierto retardo» → `cierto`: la «D = 3» pasa a ser una «D» genérica
- «la salida es la autocorrelación» → `salidar`: se escribe «salida = R_ss»
- «corrida esas mismas muestras» → `corrida`: se completa «R_ss[n − D]» y la curva se desliza
- «Buscamos el máximo de la salida» → `maximo`: una marca «máx» sobre el pico
- «su posición nos dice el retardo» → `posicion`: una flecha del pico al eje, con «D»

---

# Escena 06 — ConRuidoSeComplica

**Capítulo YouTube:** Con ruido, el máximo se equivoca
**Objetivo:** ver que el ruido puede correr el máximo a un vecino y que la amplitud también es desconocida.

## Narración

<!-- b1 -->
Con ruido, la historia se complica. A la salida se le suma ruido, y el máximo puede caer en una posición vecina: medimos mal el retardo. Y hay un segundo problema: la amplitud del eco también es desconocida, porque un avión lejano da un eco más débil. Por eso el umbral no se puede fijar a ojo.

- «Con ruido» → `ruido`: se agrega ruido magenta sobre el registro
- «la historia se complica» → `complica`: la salida del filtro se vuelve irregular
- «A la salida se le suma ruido» → `suma`: ruido magenta sobre las barras de la salida
- «el máximo puede caer» → `cae`: el máximo se resalta
- «en una posición vecina» → `vecina`: la marca salta a la barra de al lado, en rojo
- «medimos mal el retardo» → `mal`: «D = 2» con una cruz roja
- «un segundo problema» → `segundo`: aparece un «2» grande
- «la amplitud del eco» → `amplitud`: las barras del eco con alturas distintas
- «también es desconocida» → `desconocida`: «A = ?» en ámbar
- «un avión lejano» → `lejano`: un avión pequeño, muy lejos
- «un eco más débil» → `debil`: las barras del eco bajan, tenues
- «el umbral no se puede fijar a ojo» → `umbral`: una línea de umbral que oscila con un «?»

---

# Escena 07 — LoNitidoDelPico

**Capítulo YouTube:** ¿Qué pulso da el pico más estrecho?
**Objetivo:** plantear la pregunta de diseño y nombrar la compresión de pulso.

## Narración

<!-- b1 -->
Todo depende de lo nítido que sea el pico. Si el pico es ancho, con un poco de ruido el máximo resbala a un vecino y la distancia sale mal. Si es estrecho, no. Pregunta: ¿qué pulso da el pico más estrecho posible? La respuesta se llama compresión de pulso.

- «Todo depende» → `depende`: se limpia y entra un pico con un foco
- «lo nítido que sea el pico» → `nitido`: aparecen dos picos lado a lado, uno ancho y uno estrecho
- «Si el pico es ancho» → `ancho`: el ancho se resalta, con ruido encima
- «el máximo resbala a un vecino» → `resbala`: la marca roja del máximo resbala al vecino
- «la distancia sale mal» → `mal`: «distancia ✗» en rojo
- «Si es estrecho, no» → `estrecho`: el pico estrecho se resalta y la marca verde se queda firme
- «Pregunta» → `pregunta`: un «?» ámbar crece en el centro
- «¿qué pulso da el pico más estrecho posible?» → `quepulso`: la pregunta escrita en grande, con tres pulsos tenues debajo
- «La respuesta» → `respuesta`: la pregunta sube y se atenúa
- «compresión de pulso» → `compresion`: la palabra «compresión de pulso» entra en ámbar, con un pulso largo que se encoge a un pico

---

# Escena 08 — ElRectanguloYSuTriangulo

**Capítulo YouTube:** El pulso rectangular: pico ancho
**Objetivo:** calcular a mano la autocorrelación del rectángulo de trece y ver por qué el pico es poco nítido.

## Narración

<!-- b1 -->
Tomemos un pulso rectangular de trece muestras, trece unos. Su autocorrelación sale sola: al desplazarlo una muestra, coinciden doce; dos, once; y así. Un triángulo ancho. El pico vale trece, pero el vecino vale doce: casi igual. Con un poco de ruido, no hay manera de saber cuál es el bueno.

- «un pulso rectangular» → `rect`: un rectángulo azul
- «de trece muestras» → `trece`: se divide en trece barras
- «trece unos» → `unos`: sobre cada barra aparece un «1»
- «Su autocorrelación sale sola» → `sale`: debajo aparece un eje de desplazamientos
- «al desplazarlo una muestra» → `una`: una copia del pulso se corre un lugar
- «coinciden doce» → `doce`: las doce barras que se solapan se marcan y sale «12»
- «dos, once» → `once`: la copia se corre otro lugar y sale «11»
- «y así» → `asi`: los valores van bajando, un tallo por desplazamiento
- «Un triángulo ancho» → `triangulo`: el triángulo se completa
- «El pico vale trece» → `pico13`: «13» sobre el pico
- «el vecino vale doce» → `vecino`: «12» sobre el tallo de al lado
- «casi igual» → `casiigual`: un «≈» entre ambos
- «Con un poco de ruido» → `conruido`: ruido magenta sobre los dos tallos más altos
- «no hay manera de saber cuál es el bueno» → `cual`: «¿cuál?» entre los dos tallos

---

# Escena 09 — LasSimulaciones

**Capítulo YouTube:** Cuánto falla el rectangular
**Objetivo:** cuantificar con simulaciones lo que se vio a mano.

## Narración

<!-- b1 -->
Las simulaciones lo confirman. Con cuarenta mil pruebas, una relación señal-ruido de trece y un registro de sesenta y cuatro muestras, el rectangular falla el retardo exacto cincuenta y seis veces de cada cien. Casi siempre falla por poco, pero falla.

- «Las simulaciones» → `sims`: entra un ordenador con una pantalla de simulación
- «lo confirman» → `confirman`: una tilde verde sobre la pantalla
- «cuarenta mil pruebas» → `pruebas`: un contador sube hasta «40.000»
- «una relación señal-ruido de trece» → `snr`: aparece «energía / varianza = 13»
- «un registro de sesenta y cuatro muestras» → `registro`: una tira de 64 muestras
- «el rectangular falla» → `falla`: junto a la tira, el pulso rectangular con una barra que crece
- «el retardo exacto» → `exacto`: una diana sobre el retardo verdadero
- «cincuenta y seis veces de cada cien» → `cincuenta`: una grilla de cien casillas con cincuenta y seis en rojo y «56 %»
- «Casi siempre falla por poco» → `poco`: un histograma de errores concentrado en ±1 y ±2
- «pero falla» → `pero`: un sello rojo «falla»

---

# Escena 10 — CompresionDePulso

**Capítulo YouTube:** Compresión de pulso
**Objetivo:** plantear el problema de diseño: pulso largo, autocorrelación estrecha.

## Narración

<!-- b1 -->
Queremos un pulso largo, porque la energía es el largo por la amplitud, y la amplitud del transmisor está limitada. Pero también queremos una autocorrelación estrecha: grande en el origen y pequeña en todos los demás desplazamientos. Un pulso largo que a la salida del filtro se comprime en un pico estrecho. Eso se llama compresión de pulso.

- «Queremos un pulso largo» → `largo`: un pulso largo y bajo
- «la energía es el largo por la amplitud» → `energia`: «E = largo × amplitud» y el rectángulo marca su área
- «la amplitud del transmisor» → `transmisor`: un transmisor pequeño con el pulso saliendo
- «está limitada» → `limitada`: una línea de tope sobre la amplitud
- «Pero también queremos» → `tambien`: la pantalla pasa a la autocorrelación
- «una autocorrelación estrecha» → `estrecha`: un pico fino se dibuja
- «grande en el origen» → `origen`: «grande» sobre el tallo central
- «pequeña en todos los demás desplazamientos» → `demas`: los tallos laterales, mínimos
- «Un pulso largo» → `pl`: a la izquierda, un pulso largo entra en el filtro
- «se comprime en un pico estrecho» → `comprime`: el pulso se encoge visualmente hasta ser un pico fino a la salida
- «compresión de pulso» → `compresion`: la palabra «compresión de pulso» en ámbar

---

# Escena 11 — LaSecuenciaDeBarker

**Capítulo YouTube:** La secuencia de Barker de trece
**Objetivo:** presentar Barker-13 y comprobar a mano un desplazamiento de su autocorrelación.

## Narración

<!-- b1 -->
Una solución clásica es la secuencia de Barker de trece: más, más, más, más, más, menos, menos, más, más, menos, más, menos, más. Su autocorrelación vale trece en el origen y, en cualquier otro desplazamiento, cero o uno. Por ejemplo, con un desplazamiento: doce productos, seis valen uno y seis valen menos uno. Suma cero.

- «Una solución clásica» → `clasica`: se limpia y entra una insignia «Barker»
- «la secuencia de Barker de trece» → `barker`: título «Barker-13» y el eje de trece posiciones
- «más, más, más, más, más» → `cinco`: cinco barras hacia arriba, en azul
- «menos, menos» → `menos2`: dos barras hacia abajo, en rojo
- «más, más» → `mas2`: dos barras hacia arriba
- «menos, más, menos, más» → `resto`: las cuatro últimas, alternadas
- «Su autocorrelación vale trece» → `trece`: aparece un tallo central de altura «13»
- «cualquier otro desplazamiento» → `otro`: los tallos laterales aparecen
- «cero o uno» → `cerouno`: alturas 0 y 1 alternadas, muy bajas
- «Por ejemplo, con un desplazamiento» → `ejemplo`: la secuencia y su copia desplazada una muestra, una debajo de la otra
- «doce productos» → `doce`: los doce pares solapados se marcan con producto
- «seis valen uno» → `seis1`: seis productos se pintan de verde con «+1»
- «seis valen menos uno» → `seis2`: los otros seis se pintan de rojo con «−1»
- «Suma cero» → `suma0`: «6 − 6 = 0» y el tallo de desplazamiento 1 baja a cero

---

# Escena 12 — LosLobulosLaterales

**Capítulo YouTube:** Barker contra rectangular, en decibelios
**Objetivo:** cuantificar la mejora en decibelios y avisar de que sus errores son raros pero grandes.

## Narración

<!-- b1 -->
El lóbulo lateral más alto es uno, contra un pico de trece: unos veintidós decibelios por debajo. El rectangular, menos de uno. Con las mismas simulaciones, Barker falla el retardo exacto doce veces de cada cien. Aunque hay un matiz: cuando el ruido le gana, salta a un lóbulo lateral lejano, y el error es grande. Errores raros pero grandes, contra errores frecuentes pero pequeños.

- «El lóbulo lateral más alto es uno» → `lobulo`: en la autocorrelación de Barker el lóbulo más alto de los laterales se resalta, «1»
- «contra un pico de trece» → `pico`: el tallo central «13»
- «unos veintidós decibelios por debajo» → `db22`: «20 · log(1/13) ≈ −22 dB»
- «El rectangular, menos de uno» → `rect`: en el triángulo del rectangular, «20 · log(12/13) ≈ −0,7 dB»
- «Con las mismas simulaciones» → `mismas`: vuelve la pantalla de simulaciones
- «Barker falla el retardo exacto» → `barkerfalla`: una barra de Barker crece
- «doce veces de cada cien» → `doce`: la grilla de cien casillas con doce en rojo, «12 %» frente al «56 %» del rectangular
- «Aunque hay un matiz» → `matiz`: aparece un «pero…» ámbar
- «cuando el ruido le gana» → `gana`: el ruido magenta sube y supera al pico
- «salta a un lóbulo lateral lejano» → `salta`: la marca del máximo salta lejos del pico
- «el error es grande» → `grande`: una flecha larga en rojo
- «Errores raros pero grandes» → `raros`: histograma de Barker, casi todo en cero y unas pocas barras lejanas
- «contra errores frecuentes pero pequeños» → `frecuentes`: histograma del rectangular, ancho y bajo, cerca del centro

---

# Escena 13 — ElBarridoDeFrecuencia

**Capítulo YouTube:** La señal con barrido de frecuencia
**Objetivo:** la segunda forma de comprimir, que no tiene el tope de Barker.

## Narración

<!-- b1 -->
Las secuencias de Barker no pasan de trece. Para pulsos más largos, hay otra idea: una sinusoide cuya frecuencia va subiendo poco a poco. Un barrido de frecuencia, un chirrido, lo que se llama un chirp. Como cada tramo tiene una frecuencia distinta, ningún tramo se parece a otro desplazado, y la autocorrelación se estrecha.

- «no pasan de trece» → `tope13`: la secuencia de Barker con un «13» como tope
- «Para pulsos más largos» → `maslargos`: aparece un pulso largo con un «?»
- «hay otra idea» → `idea`: una bombilla
- «una sinusoide» → `sinus`: una sinusoide azul
- «cuya frecuencia va subiendo poco a poco» → `sube`: la sinusoide se va apretando de izquierda a derecha
- «Un barrido de frecuencia» → `barrido`: debajo, una recta ascendente en un espectrograma sencillo
- «un chirrido» → `chirrido`: un altavoz con la onda
- «un chirp» → `chirp`: la palabra «chirp» en pantalla
- «cada tramo tiene una frecuencia distinta» → `tramos`: tres tramos de la onda en tres colores
- «ningún tramo se parece a otro desplazado» → `ninguno`: una copia desplazada no coincide con la original, con una cruz
- «la autocorrelación se estrecha» → `estrecha`: aparece un pico fino de un solo tallo

---

# Escena 14 — SinTopeDeLargo

**Capítulo YouTube:** Largo sin tope
**Objetivo:** dar las cifras de sesenta y cuatro muestras y avisar de que la ventaja mayor es otra.

## Narración

<!-- b1 -->
Con sesenta y cuatro muestras, el pico ocupa un solo desplazamiento y los lóbulos laterales quedan unos veintiún decibelios más abajo. Y se puede hacer tan largo como se quiera, cosa que no pasa con Barker. Pero la ventaja mayor de comprimir el pulso no es medir mejor un retardo.

- «Con sesenta y cuatro muestras» → `n64`: el pulso con barrido y la etiqueta «64 muestras»
- «el pico ocupa un solo desplazamiento» → `solo`: su autocorrelación, con el pico de un solo tallo
- «los lóbulos laterales quedan» → `lobulos`: los tallos laterales se marcan
- «unos veintiún decibelios más abajo» → `db21`: «−21 dB»
- «tan largo como se quiera» → `largo`: la señal se alarga con «128», «256», …
- «cosa que no pasa con Barker» → `barker`: la secuencia de Barker con «13» y una barrera
- «Pero la ventaja mayor» → `ventaja`: una estrella ámbar
- «de comprimir el pulso» → `comprimir`: «compresión» con un pulso que se encoge
- «no es medir mejor un retardo» → `nomedir`: «D» con una cruz tenue

---

# Escena 15 — DosAvionesConElRectangular

**Capítulo YouTube:** Dos aviones y una meseta
**Objetivo:** ver que el rectángulo funde dos ecos cercanos en una meseta.

## Narración

<!-- b1 -->
Imagina dos aviones cuyos ecos llegan separados tres muestras. Sin ruido. Con el pulso rectangular, cada eco da su triángulo, y los dos se suman. Entre los dos picos, uno suma trece más diez, el siguiente doce más once, y así: veintitrés, veintitrés, veintitrés. La salida es una meseta. No hay forma de saber si hay uno o dos aviones.

- «dos aviones» → `dos`: dos aviones, uno junto al otro
- «ecos llegan separados tres muestras» → `separados`: dos pulsos rectangulares en una línea de tiempo con «3 muestras» entre ellos
- «Sin ruido» → `sinruido`: la etiqueta «sin ruido»
- «Con el pulso rectangular» → `rect`: el rectángulo de trece sobre la línea
- «cada eco da su triángulo» → `triangulos`: dos triángulos, uno por eco, se dibujan
- «los dos se suman» → `suman`: los dos triángulos se suman en una sola curva
- «trece más diez» → `13mas10`: sobre un punto entre los picos aparece «13 + 10»
- «doce más once» → `12mas11`: sobre el siguiente aparece «12 + 11»
- «veintitrés, veintitrés, veintitrés» → `v23`: «23» sobre tres puntos seguidos
- «La salida es una meseta» → `meseta`: la curva suma queda plana en 23 entre los picos
- «No hay forma de saber» → `noforma`: un «?» sobre la meseta
- «si hay uno o dos aviones» → `unoodos`: «¿uno o dos?» con uno y dos aviones

---

# Escena 16 — DosAvionesConBarker

**Capítulo YouTube:** Con Barker se ven dos
**Objetivo:** ver que Barker conserva los dos picos separados.

## Narración

<!-- b1 -->
Con Barker, cada eco da su pico de trece, y los lóbulos laterales son cero o uno. A tres muestras de distancia, el lóbulo del vecino vale cero. Así que los dos picos conservan la altura completa, trece, con un valle claro en medio. Se ven dos aviones.

- «Con Barker» → `barker`: las mismas dos llegadas, ahora con el pulso de Barker
- «cada eco da su pico de trece» → `picos13`: dos picos de altura «13»
- «los lóbulos laterales son cero o uno» → `lobulos`: los laterales de cada pico, muy bajos
- «A tres muestras de distancia» → `tres`: una llave de tres muestras entre los picos
- «el lóbulo del vecino vale cero» → `vecino0`: «0» en el lugar donde cae el lóbulo del otro pico
- «Así que los dos picos» → `asique`: los dos picos se iluminan
- «conservan la altura completa» → `altura`: los dos picos se marcan a la misma altura
- «con un valle claro en medio» → `valle`: el valle entre ambos se resalta
- «Se ven dos aviones» → `dosaviones`: los dos aviones con una tilde verde

---

# Escena 17 — ComprimirEsResolver

**Capítulo YouTube:** Comprimir es resolver
**Objetivo:** fijar que la compresión sirve para separar objetos cercanos y recordar que para solo detectar con ruido blanco da igual la forma.

## Narración

<!-- b1 -->
Ahí está la razón de fondo de la compresión de pulso: no es solo precisión en el retardo, es poder separar objetos cercanos. Y una aclaración: para decidir solo si hay o no hay señal, con ruido blanco, el rectangular y Barker dan el mismo error. Ya lo vimos: solo importa la energía. La forma cuenta cuando además hay que medir cuándo.

- «la razón de fondo» → `razon`: aparece una llave sobre las dos salidas anteriores
- «de la compresión de pulso» → `compresion`: «compresión de pulso» en ámbar
- «no es solo precisión en el retardo» → `precision`: «precisión del retardo» con una raya
- «es poder separar objetos cercanos» → `separar`: «comprimir = resolver» en grande
- «Y una aclaración» → `aclaracion`: se atenúa lo anterior y entra una nota
- «hay o no hay señal» → `hayono`: «¿hay señal?» con el radar
- «con ruido blanco» → `blanco`: la etiqueta «ruido blanco»
- «el rectangular y Barker dan el mismo error» → `mismo`: dos pulsos con el mismo «P_e»
- «Ya lo vimos» → `yavimos`: reaparece la tarjeta «E3 · solo la energía» con las dos campanas
- «solo importa la energía» → `energia`: «E» en ámbar sobre los dos
- «La forma cuenta» → `forma`: las formas de los dos pulsos se resaltan
- «cuando además hay que medir cuándo» → `cuando`: la «D» del retardo vuelve a aparecer

---

# Escena 18 — MilPosiciones

**Capítulo YouTube:** Buscar en mil posiciones
**Objetivo:** plantear que probar muchas posiciones multiplica las ocasiones de falsa alarma.

## Narración

<!-- b1 -->
Volvamos al ruido. Si no conocemos el retardo, hay que probar todas las posiciones posibles, digamos mil, y quedarnos con el máximo de la salida. Y aquí hay un problema. Cada posición es una oportunidad de que el ruido, solo, cruce el umbral y dé una falsa alarma. Cuantas más posiciones, más oportunidades.

- «Volvamos al ruido» → `ruido`: se limpia y vuelve una salida con ruido magenta
- «no conocemos el retardo» → `noconocemos`: «D = ?»
- «probar todas las posiciones posibles» → `probar`: una tira de celdas que se recorren una a una
- «digamos mil» → `mil`: «1.000 celdas»
- «quedarnos con el máximo de la salida» → `maximo`: se marca el máximo de la tira
- «Y aquí hay un problema» → `problema`: un signo de exclamación ámbar
- «Cada posición es una oportunidad» → `oportunidad`: sobre cada celda aparece un dado pequeño
- «el ruido, solo» → `solo`: solo ruido magenta, sin eco
- «cruce el umbral» → `cruce`: un pico de ruido atraviesa la línea de umbral
- «una falsa alarma» → `falsa`: la celda se pone en rojo con «falsa alarma»
- «Cuantas más posiciones» → `mas`: la tira se alarga
- «más oportunidades» → `oportunidades`: más dados, más celdas rojas

---

# Escena 19 — LaCuentaDeLasPosiciones

**Capítulo YouTube:** Ene por pe
**Objetivo:** la cuenta de «al menos una» entre N posiciones y qué falsa alarma por posición hace falta.

## Narración

<!-- b1 -->
Hagamos la cuenta. Si cada posición tiene una probabilidad pequeña, pe, de falsa alarma, la probabilidad de que salte al menos una entre ene posiciones es aproximadamente ene por pe. Queremos una falsa alarma total de una entre mil, buscando en mil posiciones. Así que cada posición tiene que tener una falsa alarma de una entre un millón.

- «Hagamos la cuenta» → `cuenta`: se limpia y aparece una pizarra
- «cada posición tiene una probabilidad pequeña, pe» → `pe`: «p» pequeña sobre una celda
- «de falsa alarma» → `falsa`: «p = P(falsa alarma de una celda)»
- «la probabilidad de que salte al menos una» → `alomenos`: aparece «P(al menos una)»
- «entre ene posiciones» → `ene`: «de N posiciones»
- «aproximadamente ene por pe» → `nporp`: «≈ N · p»
- «Queremos una falsa alarma total de una entre mil» → `total`: «≈ 10⁻³» en rojo
- «buscando en mil posiciones» → `milpos`: «N = 1.000»
- «cada posición tiene que tener» → `cada`: la fórmula se despeja: «p = 10⁻³ / 1.000»
- «una falsa alarma de una entre un millón» → `millon`: «p = 10⁻⁶» y la comprobación «1.000 · 10⁻⁶ = 10⁻³»

---

# Escena 20 — ElUmbralSube

**Capítulo YouTube:** El umbral sube casi dos desvíos
**Objetivo:** traducir la falsa alarma por posición a un umbral con la inversa de Q.

## Narración

<!-- b1 -->
Traducido al umbral. Para una sola posición y una falsa alarma de una entre mil, la inversa de cu da tres coma cero nueve desvíos. Para una entre un millón, cuatro coma siete cinco. El umbral tiene que subir casi dos desvíos completos, solo porque hemos decidido buscar en mil sitios.

- «Traducido al umbral» → `traducido`: se limpia y aparece la campana de H₀
- «una sola posición» → `una`: etiqueta «una posición»
- «una falsa alarma de una entre mil» → `unaentremil`: se sombrea en rojo una cola de área «10⁻³»
- «la inversa de cu» → `inversa`: aparece «Q⁻¹(10⁻³)»
- «tres coma cero nueve desvíos» → `v309`: el umbral se marca en «3,09 σ»
- «Para una entre un millón» → `millon`: la cola se hace diminuta, «10⁻⁶»
- «cuatro coma siete cinco» → `v475`: la marca del umbral salta a «4,75 σ»
- «subir casi dos desvíos completos» → `subir`: una flecha entre las dos marcas, hacia la derecha
- «buscar en mil sitios» → `sitios`: la tira de mil celdas vuelve abajo

---

# Escena 21 — ElPrecioEnEnergia

**Capítulo YouTube:** Cuánto cuesta buscar
**Objetivo:** calcular cuánta energía extra cuesta buscar, y nombrar las comparaciones múltiples.

## Narración

<!-- b1 -->
Y eso cuesta señal. Para detectar el noventa por ciento de los aviones, hay que separar las dos campanas el umbral más uno coma dos ocho desvíos. Con el umbral de una posición, cuatro coma tres siete. Con el de mil, seis coma cero tres. Al cuadrado, diecinueve contra treinta y seis: casi el doble de energía, unos dos coma ocho decibelios.

- «Y eso cuesta señal» → `cuesta`: se limpia y entra el radar con un contador de energía
- «detectar el noventa por ciento» → `noventa`: «P_D = 0,9»
- «separar las dos campanas» → `campanas`: las dos campanas, H₀ y H₁, con el umbral
- «el umbral más uno coma dos ocho desvíos» → `mas128`: «umbral + 1,28 σ» entre el umbral y el centro de H₁
- «Con el umbral de una posición» → `unapos`: el umbral de 3,09 σ vuelve a la campana
- «cuatro coma tres siete» → `v437`: «d = 3,09 + 1,28 = 4,37»
- «seis coma cero tres» → `v603`: «d = 4,75 + 1,28 = 6,03»
- «Al cuadrado» → `cuadrado`: aparecen los dos cuadrados
- «diecinueve contra treinta y seis» → `v1936`: «19» frente a «36»
- «casi el doble de energía» → `doble`: dos barras de energía, la segunda casi el doble
- «unos dos coma ocho decibelios» → `db28`: «+2,8 dB» en ámbar

<!-- b2 -->
Es un fenómeno muy general: si haces muchas pruebas, alguna saldrá positiva por puro azar, y hay que endurecer el criterio. Se llama el problema de las comparaciones múltiples.

- «Es un fenómeno muy general» → `general`: se limpia y entra una fila de mil análisis médicos
- «si haces muchas pruebas» → `pruebas`: la fila se llena de tubos de ensayo
- «alguna saldrá positiva» → `positiva`: algunos se ponen en rojo
- «por puro azar» → `azar`: un dado sobre la fila
- «hay que endurecer el criterio» → `endurecer`: una línea de umbral sube y se pone rígida
- «comparaciones múltiples» → `multiples`: la palabra «comparaciones múltiples» en ámbar

---

# Escena 22 — Cierre

**Capítulo YouTube:** ¿Cuál de ellas mandaron? (próximo episodio)

## Narración

<!-- b1 -->
Hoy hemos visto que, si no sabes cuándo llega el eco, el pico de la salida lo mide; que un pulso largo con la autocorrelación estrecha lo vuelve nítido y separa dos ecos; y que buscar en muchos sitios cuesta señal.

- «si no sabes cuándo llega el eco» → `eco`: el radar con el eco y «D = ?»
- «el pico de la salida lo mide» → `pico`: el pico de la salida y la «D» que sale de él
- «un pulso largo» → `largo`: un pulso largo
- «con la autocorrelación estrecha» → `estrecha`: su autocorrelación, un pico fino
- «separa dos ecos» → `separa`: dos picos de trece separados
- «buscar en muchos sitios» → `buscar`: la tira de mil celdas
- «cuesta señal» → `cuesta`: «+2,8 dB» en ámbar

<!-- b2 -->
Hasta ahora decidíamos solo entre «hay señal» y «no hay». ¿Y si mandaron una entre varias señales posibles, y hay que decir cuál? Ese es el próximo episodio: ¿cuál de ellas mandaron?

- «decidíamos solo entre» → `antes`: dos cajas, H₀ y H₁
- «hay señal» → `hay`: la caja H₁ se resalta
- «no hay» → `nohay`: la caja H₀ se resalta
- «una entre varias señales posibles» → `varias`: entran tres pulsos distintos
- «hay que decir cuál» → `cual`: un «¿cuál?» sobre los tres
- «el próximo episodio» → `proximo`: una flecha hacia la derecha
- «¿cuál de ellas mandaron?» → `titulo`: el título «¿Cuál de ellas mandaron?» en grande
