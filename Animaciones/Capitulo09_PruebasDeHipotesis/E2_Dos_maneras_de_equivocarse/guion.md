# Episodio 2 — Dos maneras de equivocarse

Capítulo 9 (Pruebas de hipótesis), episodio 2 de 6. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 06 a 10), más un gancho y un cierre nuevos.

**Estado:** **Subido a YouTube en privado** el 19/10/2026: render final 1080p60 de 11:01, título buscable, descripción con el capítulo del libro y `capitulos.txt`, subtítulos, categoría Educación (https://youtu.be/165D2jx3yDQ). Residuos limpiados; la caché de voz está en `media/voiceovers/`: se rehace con `python rehacer.py Capitulo09_PruebasDeHipotesis E2`. **Falta**: publicarlo (lo hace el usuario).
`comun/figuras_c9e2.py`), borrador aprobado por el usuario y **render final
1080p60 hecho** (11:00, 0 avisos; «cu» se dice «ku»). Falta subirlo a YouTube y
limpiar residuos (paso 17).

Texto nuevo (marcado con ⭐, **aprobado**):
- ⭐ Escena 01 (gancho): «Un mismo test, sin tocarle nada. Si das positivo, la
  probabilidad de estar enfermo puede ser un dos por ciento. O un noventa y
  cinco. Y no depende del test.»
- ⭐ Escena 02 (título): «Dos maneras de equivocarse».
- ⭐ Escena 13 (cierre): resumen corto (dos errores que son colas, el umbral que
  los reparte, la prevalencia que manda) y anuncia E3 por su título, «Un número
  y un umbral».

Notas:
- Reparto de las escenas del guion base: 06 → escenas 03 y 04; 07 → 05 y 06;
  08 → 07 y 08; 09 → 09 y 10; 10 → 11 y 12. Solo se partieron bloques enteros:
  el texto del guion base no cambia.
- El gancho usa el resultado de la escena 11 (del 2 % al 95 %) y no el de la
  escena 10 («lo mejor sería no hacer el test»), para no gastar esa sorpresa.
- La promesa de la escena 10 («dentro de tres episodios») se paga en el E5,
  escena 20 del guion base. Ahí tiene que volver la tarjeta «Siempre sano → 1 %».
- El cierre del E1 («¿Un cero o un uno?») tiene que anunciar este título,
  **«Dos maneras de equivocarse»**. El E1 todavía no tiene `guion.md`.
- Longitud: ~1.480 palabras del guion base + gancho, título y cierre ≈ 1.590
  palabras; voz de 10:45 (~11 min). El bloque b3 de la escena 12 (la lección
  para el radar, 10·b6 del guion base) se mantiene por decisión del usuario.
- Números con el **mismo dibujo** que en E1: las dos campanas (centros 0 y 2,
  desvío 1), umbrales 1 y 1,42, a priori 0,7 / 0,3; el canal de bits del Cap. 7
  (0,10 y 0,30). Del Cap. 7 vuelven la grilla de mil personas (`GrillaMil07`), la
  tira del test (`tira_test07`) y las tres tarjetas del test médico. El radar es
  el del Cap. 13 (`radar13()`), la tabla 2 × 2 es `TablaDecision`, las campanas y
  colas `dens3` / `cola3` / `umbral3`, los cien bits `rejilla3`.
- Colores: `RUIDO` (magenta) en la campana del cero / «Solo ruido» / sanos,
  `SENAL` (azul) en la del uno / «Hay avión» / enfermos, `ERROR` (rojo) en las
  colas y los fallos, `VERDE` en detección y aciertos, `ESTIMACION` (ámbar) en el
  umbral, `MEDIDA` (cian) en la medición.

---

# Escena 01 — Gancho

**Capítulo YouTube:** El mismo test, dos respuestas

## Narración

<!-- b1 -->
Un mismo test, sin tocarle nada. Si das positivo, la probabilidad de estar
enfermo puede ser un dos por ciento. O un noventa y cinco. Y no depende del
test.

- «Un mismo test» → `test`: la tira del test del Cap. 7 entra al centro
- «sin tocarle nada» → `nada`: debajo, las tarjetas «Enfermo → Positivo 99 %» y «Sano → Positivo 5 %» con un candado pequeño
- «Si das positivo» → `positivo`: la ventana de la tira se enciende en rojo con un «+»
- «la probabilidad de estar enfermo» → `prob`: arriba, «P(Enfermo | +) = ?»
- «un dos por ciento» → `dos`: el «?» se cambia por «2 %»
- «un noventa y cinco» → `noventa`: al lado entra «95 %», con una flecha de doble punta entre los dos
- «no depende del test» → `nodepende`: la tira se atenúa y un «?» ámbar grande late sobre ella

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Dos maneras de equivocarse

## Narración

<!-- b1 -->
Dos maneras de equivocarse.

- «Dos maneras» → `t1`: «Dos maneras» entra con rebote
- «de equivocarse» → `t2`: «de equivocarse» entra debajo, con la etiqueta «Capítulo 9 · Pruebas de hipótesis»

---

# Escena 03 — FalsaAlarmaYFallo

**Capítulo YouTube:** Falsa alarma y fallo

## Narración

<!-- b1 -->
Un radar mira al cielo. La hipótesis cero dice: solo hay ruido. La hipótesis
uno dice: hay un avión. El radar mide y decide. Hay cuatro casos posibles. En
dos, acierta. En los otros dos se equivoca, pero no de la misma manera.

- «Un radar mira al cielo» → `radar`: el radar (`radar13`) entra abajo a la izquierda y lanza ondas hacia arriba
- «La hipótesis cero dice» → `h0`: casilla «H₀ · Solo ruido» en magenta, con un garabato de ruido
- «solo hay ruido» → `garabato`: dentro de la casilla H₀ se dibuja un garabato magenta de ruido
- «hay un avión» → `h1`: casilla «H₁ · Hay avión» en azul, con un avión pequeño
- «mide y decide» → `decide`: vuelve un eco al radar y sale una flecha a «Decisión»
- «cuatro casos posibles» → `tabla`: la `TablaDecision` 2 × 2 vacía; filas «Realidad» (Solo ruido, Hay avión), columnas «Decisión» (Nada, Avión)
- «En dos, acierta» → `aciertos`: tildes verdes en la diagonal
- «se equivoca» → `errores`: cruces rojas en las otras dos casillas
- «no de la misma manera» → `distintos`: entre las dos cruces aparece un «≠» ámbar

<!-- b2 -->
Si dice que hay un avión y no lo había, es una falsa alarma. Si dice que no hay
nada y sí lo había, es un fallo, que en inglés se llama miss. Los nombres
vienen del radar, pero valen para todo. En el canal de bits, una falsa alarma
es decir uno cuando se envió un cero.

- «Si dice que hay un avión» → `dice`: se resalta la casilla Solo ruido × Avión
- «es una falsa alarma» → `fa`: dentro, «Falsa alarma» en rojo
- «Si dice que no hay nada» → `dicenada`: se resalta la casilla Hay avión × Nada
- «es un fallo» → `fallo`: dentro, «Fallo» en rojo
- «se llama miss» → `miss`: debajo de «Fallo», «Miss» más pequeño
- «valen para todo» → `todo`: a la derecha, tres íconos pequeños en columna: radar, tira del test y canal
- «En el canal de bits» → `canal`: el canal (`canal7`) ocupa el sitio del radar; las filas pasan a «Se envió 0» y «Se envió 1»
- «decir uno cuando se envió un cero» → `fa_canal`: en la casilla de falsa alarma aparece «0 → 1»

---

# Escena 04 — ProbabilidadDeError

**Capítulo YouTube:** Detección y probabilidad de error

## Narración

<!-- b1 -->
Cada error tiene su probabilidad, y cuidado con cómo se definen. La
probabilidad de falsa alarma es, de todas las veces que no había avión, la
fracción en que el radar dice que sí. Está condicionada a hache cero. La
probabilidad de fallo es, de las veces que sí había avión, la fracción que se
le escapa. Está condicionada a hache uno.

- «Cada error tiene su probabilidad» → `probs`: la tabla 2 × 2 de la escena anterior se encoge a la izquierda
- «cuidado con cómo se definen» → `cuidado`: un triángulo de aviso ámbar sobre la tabla
- «probabilidad de falsa alarma» → `pfa`: a la derecha entra «P_FA» en rojo
- «de todas las veces que no había avión» → `fila0`: la fila «Solo ruido» se resalta y se estira en una barra magenta
- «la fracción en que el radar dice que sí» → `trozo_fa`: la barra se parte; el trozo de la derecha se vuelve rojo con «P_FA»
- «condicionada a hache cero» → `cond0`: debajo, «P_FA = P(Decir 1 | H₀)», con «H₀» resaltado
- «La probabilidad de fallo» → `pm`: entra «P_M» en rojo
- «de las veces que sí había avión» → `fila1`: la fila «Hay avión» se estira en una barra azul
- «la fracción que se le escapa» → `trozo_m`: el trozo de la izquierda se vuelve rojo con «P_M»
- «condicionada a hache uno» → `cond1`: «P_M = P(Decir 0 | H₁)», con «H₁» resaltado

<!-- b2 -->
Hay una tercera, que es la que se suele anunciar: la probabilidad de detección.
De las veces que había avión, la fracción que el radar ve. Es uno menos la
probabilidad de fallo, porque un avión o se ve o se escapa.

- «Hay una tercera» → `tercera`: un «3» ámbar junto a las dos fórmulas
- «la probabilidad de detección» → `pd`: entra «P_D» en verde
- «De las veces que había avión» → `fila1d`: la barra azul de «Hay avión» se resalta
- «la fracción que el radar ve» → `trozo_d`: el resto de la barra azul se vuelve verde con «P_D»
- «Es uno menos la probabilidad de fallo» → `formula`: «P_D = 1 − P_M», pieza a pieza
- «o se ve o se escapa» → `suma`: los trozos rojo y verde se juntan bajo una llave «= 1»

<!-- b3 -->
¿Y la probabilidad de equivocarse, en total? Hay dos caminos para fallar. No
había avión, con probabilidad pe cero, y hubo falsa alarma. O había avión, con
probabilidad pe uno, y hubo fallo. La probabilidad de error es pe cero por la
de falsa alarma, más pe uno por la de fallo.

- «¿Y la probabilidad de equivocarse» → `pe`: corte; arriba, «P_e = ?» en rojo
- «dos caminos para fallar» → `arbol`: una raíz con dos ramas vacías
- «con probabilidad pe cero» → `rama0`: la rama de arriba se etiqueta «p₀» y lleva a «Solo ruido»
- «y hubo falsa alarma» → `hoja0`: al final, la hoja «Falsa alarma · P_FA» en rojo
- «con probabilidad pe uno» → `rama1`: la rama de abajo, «p₁», lleva a «Hay avión»
- «y hubo fallo» → `hoja1`: la hoja «Fallo · P_M» en rojo
- «La probabilidad de error es pe cero por la de falsa alarma» → `term0`: debajo se construye «P_e = p₀ · P_FA»
- «más pe uno por la de fallo» → `term1`: se suma «+ p₁ · P_M»; la fórmula queda enmarcada

<!-- b4 -->
Comprobémoslo con el canal. Creyendo lo recibido, la falsa alarma vale cero
coma uno y el fallo también. Cero coma siete por cero coma uno, más cero coma
tres por cero coma uno: un diez por ciento. Y diciendo siempre cero no hay
falsas alarmas, pero se fallan todos los unos: un treinta por ciento. Lo mismo
que antes.

- «Comprobémoslo con el canal» → `canal`: el árbol sale; la fórmula sube y entra el canal pequeño en una esquina
- «Creyendo lo recibido» → `creer`: renglón «Creer lo recibido»
- «la falsa alarma vale cero coma uno» → `fa01`: «P_FA = 0,1»
- «el fallo también» → `m01`: «P_M = 0,1»
- «Cero coma siete por cero coma uno» → `c1`: «0,7 · 0,1»
- «más cero coma tres por cero coma uno» → `c2`: «+ 0,3 · 0,1»
- «un diez por ciento» → `diez`: «= 0,10»
- «diciendo siempre cero» → `siempre`: segundo renglón, «Siempre 0»
- «no hay falsas alarmas» → `fa0`: «0,7 · 0»
- «se fallan todos los unos» → `m1`: «+ 0,3 · 1»
- «un treinta por ciento» → `treinta`: «= 0,30»
- «Lo mismo que antes» → `antes`: al lado, la tabla de las cuatro reglas del E1 en pequeño; 0,10 y 0,30 se marcan con tilde verde

---

# Escena 05 — ElAreaDeLaCola

**Capítulo YouTube:** Errores que son colas: la función Q

## Narración

<!-- b1 -->
Volvamos a las campanas, con el umbral en un voltio. Hay falsa alarma cuando se
envió un cero y el ruido empujó la medición por encima del umbral. Su
probabilidad es el área de la campana del cero a la derecha del umbral. Y el
fallo es el área de la campana del uno a la izquierda. Los dos errores son
áreas de colas.

- «Volvamos a las campanas» → `campanas`: las dos campanas del E1 se dibujan: centro 0 (magenta) y centro 2 (azul)
- «con el umbral en un voltio» → `umbral`: marca vertical ámbar en «1»
- «se envió un cero» → `cero`: se resalta la campana del cero
- «el ruido empujó la medición» → `empuja`: un punto cian sale de 0 y avanza a empujones hacia la derecha
- «por encima del umbral» → `encima`: el punto cruza la marca y queda en 1,6
- «el área de la campana del cero a la derecha del umbral» → `cola_fa`: la cola derecha de la campana del cero se rellena en rojo, con «Falsa alarma»
- «Y el fallo» → `fallo`: se resalta la campana del uno
- «a la izquierda» → `cola_m`: su cola izquierda se rellena en rojo, con «Fallo»
- «áreas de colas» → `colas`: las dos colas laten a la vez

<!-- b2 -->
Para calcularlas hay una herramienta. Cualquier campana se convierte en la
campana estándar, de centro cero y desvío uno, restando su centro y dividiendo
entre su desvío. Es medir las distancias en desvíos. El área de la cola de la
campana estándar, desde un punto equis en adelante, se llama función cu de
equis.

- «hay una herramienta» → `herramienta`: corte; una campana cualquiera, ancha, centrada en 3
- «la campana estándar» → `estandar`: aparece en línea punteada la silueta de destino, centrada en 0 y más estrecha
- «restando su centro» → `restar`: la campana se desliza hasta el 0, con «− Centro»
- «dividiendo entre su desvío» → `dividir`: se estrecha hasta coincidir con la silueta, con «÷ Desvío»
- «medir las distancias en desvíos» → `desvios`: en el eje, marcas «1», «2», «3» con la etiqueta «Desvíos»
- «El área de la cola» → `area`: rótulo «Área de la cola» en ámbar sobre el lado derecho de la campana
- «desde un punto equis en adelante» → `x`: una marca «x» en el eje y la cola a su derecha se rellena en rojo
- «se llama función cu de equis» → `q`: sobre la cola, «Q(x)» con rebote

<!-- b3 -->
No tiene una fórmula sencilla: se mira en una tabla o se le pide al ordenador.
Algunos valores para orientarse. Cu de cero es un medio: media campana. Cu de
uno, cero coma dieciséis. Cu de dos, cero coma cero veintitrés. Cu de tres,
poco más de una milésima. La cola cae muy deprisa.

- «No tiene una fórmula sencilla» → `nofor`: un «Q(x) = ?» que se tacha
- «se mira en una tabla» → `tabla`: a la derecha, una tabla vacía de cuatro renglones, «x · Q(x)»
- «se le pide al ordenador» → `ordenador`: el ícono del ordenador junto a la tabla
- «Algunos valores para orientarse» → `valores`: la marca x aparece sobre el eje, lista para moverse
- «Cu de cero es un medio» → `q0`: la marca x va a 0, media campana roja; renglón «Q(0) = 0,5»
- «media campana» → `media`: la mitad derecha de la campana late en rojo
- «uno, cero coma dieciséis» → `q1`: x va a 1; renglón «Q(1) = 0,16»
- «Cu de dos» → `q2`: x va a 2; renglón «Q(2) = 0,023»
- «Cu de tres» → `q3`: x va a 3, la cola casi no se ve; renglón «Q(3) = 0,0013»
- «La cola cae muy deprisa» → `deprisa`: los cuatro valores se convierten en cuatro barras que se desploman

---

# Escena 06 — DieciseisDeCien

**Capítulo YouTube:** Dieciséis bits de cada cien

## Narración

<!-- b1 -->
La falsa alarma: el umbral está en uno y la campana del cero tiene centro cero
y desvío uno. El umbral queda a un desvío del centro. Cu de uno: cero coma
ciento cincuenta y nueve. El fallo es una cola izquierda, pero la campana es
simétrica: del dos al uno hay también un desvío. Otra vez cero coma ciento
cincuenta y nueve.

- «La falsa alarma» → `fa`: vuelven las dos campanas con el umbral en 1 y la cola de falsa alarma en rojo
- «la campana del cero tiene centro cero» → `centro`: un punto en 0 sobre el eje
- «y desvío uno» → `desvio1`: bajo la campana del cero, un segmento de 0 a 1 con «σ = 1»
- «a un desvío del centro» → `undesvio`: una cota de 0 a 1, «1 desvío»
- «Cu de uno» → `cuenta_fa`: arriba a la izquierda, «(1 − 0) / 1 = 1 → Q(1)»
- «cero coma ciento cincuenta y nueve» → `v_fa`: «= 0,159» junto a la cola
- «El fallo es una cola izquierda» → `cola_m`: se rellena la cola izquierda de la campana del uno
- «la campana es simétrica» → `simetrica`: una copia de esa cola se refleja sobre el 2 y queda como cola derecha
- «del dos al uno hay también un desvío» → `cuenta_m`: cota de 1 a 2 y, arriba a la derecha, «(2 − 1) / 1 = 1 → Q(1)»
- «Otra vez cero coma ciento cincuenta y nueve» → `v_m`: «= 0,159» junto a la otra cola

<!-- b2 -->
Con ceros y unos igual de frecuentes, la probabilidad de error es esa misma:
dieciséis bits mal de cada cien. Es mucho, porque las campanas están a solo dos
desvíos una de otra. Lo que cuenta es esa separación medida en desvíos. Con
seis desvíos entre ellas, el umbral quedaría a tres, y fallaría poco más de un
bit de cada mil.

- «igual de frecuentes» → `iguales`: arriba, «p₀ = p₁ = ½»
- «la probabilidad de error es esa misma» → `pe`: «P_e = ½ · 0,159 + ½ · 0,159 = 0,159»
- «dieciséis bits mal de cada cien» → `bits`: corte; cien bits en una rejilla (`rejilla3`), dieciséis se encienden en rojo
- «Es mucho» → `mucho`: «16 %» grande en rojo, con rebote, junto a la rejilla
- «a solo dos desvíos» → `dos`: vuelven las campanas, con una cota entre los centros: «2 desvíos»
- «separación medida en desvíos» → `sep`: rótulo «Separación ÷ Desvío»
- «Con seis desvíos entre ellas» → `seis`: las campanas se separan; la cota cuenta hasta «6 desvíos»
- «el umbral quedaría a tres» → `tres`: el umbral en el medio, con cota «3 desvíos»; las colas casi desaparecen
- «un bit de cada mil» → `mil`: «Q(3) = 0,0013»

---

# Escena 07 — MoverElUmbral

**Capítulo YouTube:** El umbral del máximo a posteriori

## Narración

<!-- b1 -->
Ahora con los ceros más frecuentes: setenta y treinta. La regla del máximo a
posteriori ponía el umbral en uno coma cuarenta y dos. La falsa alarma es la
cola a partir de ahí: cu de uno coma cuarenta y dos, cero coma cero setenta y
siete. Ha bajado a la mitad.

- «los ceros más frecuentes» → `frec`: las dos campanas (separación 2) con el umbral en 1; arriba «p₀ = 0,7 · p₁ = 0,3»
- «setenta y treinta» → `escala`: las campanas se escalan al 70 % y al 30 % y se ve el cruce en 1,42; después vuelven a su altura
- «La regla del máximo a posteriori» → `map`: rótulo «Máximo a posteriori» en ámbar sobre el cruce
- «el umbral en uno coma cuarenta y dos» → `umbral`: el umbral se desliza de «1» a «1,42»
- «La falsa alarma es la cola» → `cola_fa`: la cola roja de la derecha se rellena desde 1,42
- «cu de uno coma cuarenta y dos» → `q142`: «Q(1,42)»
- «cero coma cero setenta y siete» → `v077`: «= 0,077»
- «Ha bajado a la mitad» → `mitad`: «0,159 → 0,077» con una flecha verde hacia abajo

<!-- b2 -->
El fallo: del centro de la campana del uno, que está en dos, al umbral hay cero
coma cincuenta y ocho desvíos. Cu de cero coma cincuenta y ocho: cero coma
veintiocho. Casi se ha duplicado.

- «El fallo» → `fallo`: se rellena la cola izquierda de la campana del uno, hasta 1,42
- «que está en dos» → `dos`: un punto en 2 sobre el eje
- «cero coma cincuenta y ocho desvíos» → `cota`: cota de 1,42 a 2, «0,58 desvíos»
- «Cu de cero coma cincuenta y ocho» → `q058`: «(2 − 1,42) / 1 = 0,58 → Q(0,58)»
- «cero coma veintiocho» → `v028`: «= 0,28»
- «Casi se ha duplicado» → `doble`: «0,159 → 0,28» con una flecha roja hacia arriba

<!-- b3 -->
La probabilidad de error es la media ponderada. Cero coma siete por cero coma
cero setenta y siete, más cero coma tres por cero coma veintiocho. Cero coma
cero cincuenta y cuatro, más cero coma cero ochenta y cinco: cero coma ciento
treinta y nueve.

- «la media ponderada» → `formula`: las campanas suben y se achican; abajo, «P_e = p₀ · P_FA + p₁ · P_M»
- «Cero coma siete por cero coma cero setenta y siete» → `t0`: debajo, «0,7 · 0,077»
- «más cero coma tres por cero coma veintiocho» → `t1`: «+ 0,3 · 0,28»
- «Cero coma cero cincuenta y cuatro» → `r0`: tercer renglón, «0,054»
- «más cero coma cero ochenta y cinco» → `r1`: «+ 0,085»
- «cero coma ciento treinta y nueve» → `total`: «= 0,139», enmarcado en verde

---

# Escena 08 — UnErrorPorOtro

**Capítulo YouTube:** Mover el umbral cambia un error por otro

## Narración

<!-- b1 -->
Comparemos. Con el umbral en uno, las dos colas valen cero coma ciento
cincuenta y nueve, y el error también. Diciendo siempre cero, el error es cero
coma treinta. Con el umbral en uno coma cuarenta y dos, cero coma ciento
treinta y nueve. Es el menor, como tenía que ser.

- «Comparemos» → `ejes`: corte; un eje vertical «Error» con tres huecos de barra
- «Con el umbral en uno» → `u1`: crece la barra «Umbral en 1 · 0,159»
- «las dos colas valen» → `colas`: sobre la barra, dos colas rojas pequeñas con «0,159» cada una
- «y el error también» → `tambien`: las dos colas se funden en el valor «0,159» encima de la barra
- «Diciendo siempre cero» → `s0`: crece la barra «Siempre 0 · 0,30», más alta
- «el error es cero coma treinta» → `v030`: el valor «0,30» encima de su barra
- «Con el umbral en uno coma cuarenta y dos» → `u142`: crece la barra «Umbral en 1,42 · 0,139»
- «cero coma ciento treinta y nueve» → `v139`: el valor «0,139» encima de la barra
- «Es el menor» → `menor`: la última barra se pone verde y se resalta

<!-- b2 -->
Fíjate en lo que ha pasado al mover el umbral: una cola encoge y la otra crece.
No hay manera de bajar las dos a la vez moviendo el umbral. Para eso hay que
separar las campanas: más amplitud o menos ruido. El umbral solo reparte el
error, y el máximo a posteriori lo carga sobre los unos porque son menos.

- «al mover el umbral» → `mover`: corte a las campanas con sus dos colas; el umbral empieza a ir y venir
- «una cola encoge» → `encoge`: la cola de falsa alarma se achica (el umbral va a la derecha)
- «la otra crece» → `crece`: la cola del fallo crece a la vez
- «No hay manera de bajar las dos» → `nohay`: dos flechas hacia abajo sobre las colas, tachadas en rojo
- «moviendo el umbral» → `vaiven`: el umbral sigue yendo y viniendo y las flechas tachadas parpadean
- «separar las campanas» → `separar`: las campanas se separan y las dos colas bajan juntas
- «más amplitud o menos ruido» → `amp`: rótulo «Más señal o menos ruido»
- «solo reparte el error» → `reparte`: las campanas vuelven a la separación 2; el umbral queda en 1,42
- «lo carga sobre los unos» → `carga`: la cola del fallo se resalta, más grande que la otra
- «porque son menos» → `menos`: junto a la campana del uno, «p₁ = 0,3»

<!-- b3 -->
Minimizar el total parece lo sensato. Pero ¿es siempre lo que queremos? Hay un
ejemplo que ya conoces donde el total engaña.

- «Minimizar el total» → `total`: «P_e mínima» con una tilde verde al centro
- «¿es siempre lo que queremos?» → `pregunta`: un «?» ámbar sobre la tilde
- «un ejemplo que ya conoces» → `ejemplo`: la tira del test asoma por un lado
- «el total engaña» → `engana`: la tilde se tacha en rojo

---

# Escena 09 — ElTestMedicoVuelve

**Capítulo YouTube:** El test médico vuelve

## Narración

<!-- b1 -->
Vuelve el test médico del capítulo siete. Una enfermedad la tiene una persona
de cada cien. Si estás enfermo, el test da positivo el noventa y nueve por
ciento de las veces. Si estás sano, da positivo un cinco por ciento. Es un
problema de hipótesis: hache cero, sano; hache uno, enfermo. Y la decisión es
lo que dice el test.

- «Vuelve el test médico» → `test`: la tira del test entra al centro, con la etiqueta «Capítulo 7»
- «Una enfermedad» → `enfermedad`: la cruz de hospital pequeña junto a la tira
- «una persona de cada cien» → `cien`: primera tarjeta, «1 de cada 100»
- «Si estás enfermo» → `enfermo`: segunda tarjeta, con una persona azul
- «noventa y nueve por ciento» → `p99`: la tarjeta se completa: «Enfermo → Positivo 99 %»
- «Si estás sano» → `sano`: tercera tarjeta, con una persona magenta
- «un cinco por ciento» → `p5`: «Sano → Positivo 5 %»
- «hache cero, sano» → `h0`: casilla «H₀ · Sano» en magenta
- «hache uno, enfermo» → `h1`: casilla «H₁ · Enfermo» en azul
- «la decisión es lo que dice el test» → `decision`: flecha de la tira a «Decisión: + / −» en ámbar

<!-- b2 -->
Los médicos usan otros nombres para lo mismo. La probabilidad de detección,
noventa y nueve por ciento, es la sensibilidad. La de falsa alarma, cinco por
ciento, es la de falso positivo, y lo que falta hasta cien, noventa y cinco, es
la especificidad. El fallo es el falso negativo. Y la probabilidad a priori de
estar enfermo, uno por ciento, es la prevalencia.

- «otros nombres» → `dicc`: corte; un diccionario de dos columnas, «Nosotros» y «Médicos»
- «La probabilidad de detección» → `det`: primer renglón, a la izquierda «Detección»
- «es la sensibilidad» → `sens`: a la derecha «Sensibilidad · 99 %»
- «La de falsa alarma» → `fa`: segundo renglón, «Falsa alarma»
- «falso positivo» → `fp`: «Falso positivo · 5 %»
- «es la especificidad» → `esp`: tercer renglón, «1 − Falsa alarma» · «Especificidad · 95 %»
- «el falso negativo» → `fn`: cuarto renglón, «Fallo» · «Falso negativo · 1 %»
- «la probabilidad a priori de estar enfermo» → `apriori`: quinto renglón, a la izquierda «p₁»
- «es la prevalencia» → `prev`: quinto renglón, «p₁» · «Prevalencia · 1 %»

<!-- b3 -->
Pero al paciente no le interesa ninguna de esas. Le interesa esto: he dado
positivo, ¿estoy enfermo? Es el valor predictivo positivo. Ya hicimos la
cuenta. De mil personas, diez enfermas dan positivo, y de las novecientas
noventa sanas, unas cincuenta también. Diez de sesenta: un diecisiete por
ciento.

- «al paciente» → `paciente`: el diccionario se atenúa; entra una persona a la izquierda
- «no le interesa ninguna de esas» → `ninguna`: los renglones del diccionario se tachan uno tras otro
- «Le interesa esto» → `esto`: la persona se ilumina y da un paso al frente
- «he dado positivo, ¿estoy enfermo?» → `pregunta`: burbuja de pensamiento con «+ → ¿Enfermo?»
- «el valor predictivo positivo» → `vpp`: rótulo «Valor predictivo positivo» en ámbar
- «Ya hicimos la cuenta» → `cuenta`: corte; la grilla de mil personas del Cap. 7
- «diez enfermas dan positivo» → `diez`: diez puntos se encienden en azul con «+»
- «unas cincuenta también» → `cincuenta`: unos cincuenta puntos magenta se marcan con «+»
- «Diez de sesenta» → `sesenta`: recuadro alrededor de los sesenta positivos; «10 / 60»
- «un diecisiete por ciento» → `diecisiete`: «≈ 17 %», con rebote

<!-- b4 -->
Aquí está la trampa. La sensibilidad recorre la tabla por filas: de los
enfermos, cuántos dan positivo. El valor predictivo la recorre por columnas: de
los positivos, cuántos están enfermos. Son preguntas distintas, y para pasar de
una a otra hace falta la prevalencia.

- «Aquí está la trampa» → `trampa`: corte; tabla 2 × 2 de mil personas, filas «Sano», «Enfermo», columnas «−», «+»: «940 · 50 / 0 · 10»
- «La sensibilidad recorre la tabla» → `senst`: rótulo «Sensibilidad» a la izquierda de la fila «Enfermo»
- «por filas» → `filas`: una flecha horizontal recorre la fila «Enfermo», con «Sensibilidad»
- «de los enfermos, cuántos dan positivo» → `filacuenta`: al final de la fila, «10 de 10 ≈ 99 %»
- «El valor predictivo» → `vp`: rótulo «Valor predictivo» encima de la columna «+»
- «por columnas» → `columnas`: una flecha vertical recorre la columna «+», con «Valor predictivo»
- «cuántos están enfermos» → `colcuenta`: al pie de la columna, «10 de 60 ≈ 17 %»
- «Son preguntas distintas» → `distintas`: un «≠» grande entre «99 %» y «17 %»
- «hace falta la prevalencia» → `prev`: entre las dos flechas entra la tarjeta «Prevalencia · 1 %»

---

# Escena 10 — NoHacerElTest

**Capítulo YouTube:** ¿Mejor no hacer el test?

## Narración

<!-- b1 -->
Y ahora una sorpresa. La probabilidad de error de este test: cero coma noventa
y nueve por cero coma cero cinco, más cero coma cero uno por cero coma cero
uno. Casi un cinco por ciento. Un test que dijera siempre sano, sin mirar a
nadie, solo fallaría con los enfermos: un uno por ciento.

- «una sorpresa» → `sorpresa`: corte con un «!» ámbar que estalla y desaparece
- «La probabilidad de error de este test» → `formula`: «P_e = p₀ · P_FA + p₁ · P_M»
- «cero coma noventa y nueve por cero coma cero cinco» → `t0`: debajo, «0,99 · 0,05»
- «más cero coma cero uno por cero coma cero uno» → `t1`: «+ 0,01 · 0,01»
- «Casi un cinco por ciento» → `cinco`: «≈ 5 %», y crece una barra roja «Test · 5 %»
- «siempre sano» → `siempre`: a su lado, la tarjeta «Siempre sano»
- «sin mirar a nadie» → `nadie`: una tira del test pequeña, tachada
- «solo fallaría con los enfermos» → `enfermos`: cien puntos (uno azul, el enfermo); el azul se pone rojo y crece
- «un uno por ciento» → `uno`: crece una barra verde «Siempre sano · 1 %», mucho más baja

<!-- b2 -->
Según la probabilidad de error, lo mejor sería no hacer el test. Es absurdo, y
la razón es que hemos tratado los dos errores como si costaran lo mismo. Lo
arreglaremos dentro de tres episodios. Guárdate la pregunta.

- «lo mejor sería no hacer el test» → `nohacer`: sobre las barras, «Mejor: No hacer el test»
- «Es absurdo» → `absurdo`: el rótulo se tacha en rojo
- «los dos errores» → `dos`: corte; dos casillas: «Enfermo enviado a casa» y «Sano que repite la prueba»
- «como si costaran lo mismo» → `igual`: un «=» entre las dos casillas, que tiembla
- «dentro de tres episodios» → `promesa`: un «?» ámbar grande con la etiqueta «Dentro de tres episodios»
- «Guárdate la pregunta» → `guarda`: el «?» se encoge y vuela a una esquina

---

# Escena 11 — LaPrevalenciaManda

**Capítulo YouTube:** La prevalencia manda

## Narración

<!-- b1 -->
Cambiemos solo la prevalencia, con el mismo test. Si la enfermedad la tiene una
persona de cada mil: de cien mil personas, cien están enfermas y dan noventa y
nueve positivos. Las otras noventa y nueve mil novecientas están sanas y dan
casi cinco mil positivos. Noventa y nueve de unos cinco mil cien: un dos por
ciento.

- «Cambiemos solo la prevalencia» → `prev`: la tarjeta «Prevalencia» con una perilla que gira
- «con el mismo test» → `mismo`: las tarjetas «99 %» y «5 %» con un candado
- «una persona de cada mil» → `mil`: la perilla marca «1 de cada 1.000»
- «de cien mil personas» → `cienmil`: arriba, «100.000 personas»
- «cien están enfermas» → `enf`: rama azul, «100 enfermas»
- «noventa y nueve positivos» → `p99`: «→ 99 positivos»
- «noventa y nueve mil novecientas» → `sanas`: rama magenta, «99.900 sanas»
- «casi cinco mil positivos» → `p5000`: «→ 4.995 positivos»
- «Noventa y nueve de unos cinco mil cien» → `div`: abajo, «99 / 5.094»
- «un dos por ciento» → `dos`: «≈ 2 %», con rebote

<!-- b2 -->
Con una de cada cien, un diecisiete por ciento. Con una de cada diez, un
sesenta y nueve. Con la mitad de la población enferma, un noventa y cinco. El
mismo test, con la misma sensibilidad y la misma especificidad, da respuestas
que van del dos al noventa y cinco por ciento.

- «Con una de cada cien» → `cien`: corte; ejes «Prevalencia» (horizontal) y «Valor predictivo» (vertical), con el punto «0,1 % → 2 %» y entra «1 % → 17 %»
- «Con una de cada diez» → `p10`: punto «10 % → 69 %»
- «Con la mitad» → `p50`: punto «50 % → 95 %»
- «un noventa y cinco» → `v95`: el punto del 50 % se enciende en verde con «95 %»
- «mismo test, con la misma sensibilidad» → `curva`: la curva se dibuja pasando por los cuatro puntos
- «la misma especificidad» → `candado`: en una esquina, las tarjetas «99 %» y «5 %» con su candado
- «del dos al noventa y cinco por ciento» → `rango`: una llave vertical junto al eje, «2 % → 95 %»

<!-- b3 -->
La razón es de dónde sale cada positivo. Los falsos salen de un montón enorme
de sanos, y los verdaderos, de un montón minúsculo de enfermos. Un porcentaje
pequeño de muchísimos puede ser más que un porcentaje grande de muy pocos.

- «de dónde sale cada positivo» → `donde`: corte; un «+» ámbar con un «?»
- «un montón enorme de sanos» → `sanos`: un montón magenta enorme del que sale una tira fina de «+»
- «un montón minúsculo de enfermos» → `enfermos`: un montón azul minúsculo del que salen casi todos con «+»
- «Un porcentaje pequeño de muchísimos» → `pequeno`: bajo el montón grande, «5 % de 99.900 = 4.995»
- «un porcentaje grande de muy pocos» → `grande`: bajo el pequeño, «99 % de 100 = 99»; las dos tiras se ponen lado a lado y la fina es mucho más larga

---

# Escena 12 — RepetirElTest

**Capítulo YouTube:** Repetir el test

## Narración

<!-- b1 -->
¿Entonces el test no sirve? Sí sirve: has pasado del uno al diecisiete por
ciento. Y ese diecisiete es tu nueva probabilidad a priori. Repite el test, y
supón que sus errores no dependen de la primera vez. De mil personas como tú,
ciento sesenta y siete están enfermas y dan ciento sesenta y cinco positivos.
Las otras ochocientas treinta y tres dan cuarenta y dos.

- «¿Entonces el test no sirve?» → `nosirve`: la tira del test con un «?» ámbar
- «Sí sirve» → `sisirve`: arriba, una cadena: «1 % → Test + → 17 %»
- «has pasado del uno al diecisiete» → `paso`: una flecha verde crece de «1 %» a «17 %»
- «Y ese diecisiete» → `ese`: el «17 %» late en ámbar
- «tu nueva probabilidad a priori» → `nueva`: la flecha verde se va y debajo del «17 %» aparece «Nueva a priori»
- «Repite el test» → `repite`: la cadena sigue: «→ Test + → ?»
- «no dependen de la primera vez» → `indep`: entre las dos tiras, un «⟂»
- «De mil personas como tú» → `mil`: debajo, «1.000 personas»
- «ciento sesenta y siete están enfermas» → `e167`: rama azul, «167 enfermas»
- «ciento sesenta y cinco positivos» → `p165`: «→ 165 positivos»
- «ochocientas treinta y tres» → `s833`: rama magenta, «833 sanas»
- «dan cuarenta y dos» → `p42`: «→ 42 positivos»

<!-- b2 -->
Ciento sesenta y cinco de doscientos siete: un ochenta por ciento. Con un
tercer positivo, un noventa y nueve. Por eso un positivo se confirma con otra
prueba, y por eso no se hacen pruebas masivas de enfermedades muy raras.

- «Ciento sesenta y cinco de doscientos siete» → `div`: «165 / 207»
- «un ochenta por ciento» → `ochenta`: el «?» de la cadena pasa a «80 %»
- «Con un tercer positivo» → `tercer`: la cadena sigue: «→ Test + → ?»
- «un noventa y nueve» → `v99`: el «?» se cambia por «99 %», enmarcado en verde
- «se confirma con otra prueba» → `confirma`: dos tiras del test con tilde verde
- «pruebas masivas» → `masivas`: una multitud enorme de puntos con el rótulo «Prueba masiva», tachado

<!-- b3 -->
La lección vale igual para un radar o un receptor. La falsa alarma y la
detección describen al detector. Pero cuánto creerle cuando dice que sí depende
también de lo frecuente que sea lo que busca.

- «un radar o un receptor» → `radar`: corte; el radar y el canal, lado a lado
- «La falsa alarma y la detección» → `fad`: entre los dos íconos, «P_FA» y «P_D»
- «describen al detector» → `detector`: tarjeta «El detector: Falsa alarma y Detección»
- «cuánto creerle» → `creer`: segunda tarjeta, «Cuánto creerle»
- «lo frecuente que sea lo que busca» → `frec`: la tarjeta se completa: «Además, lo frecuente que es»

---

# Escena 13 — Cierre

**Capítulo YouTube:** Lo que viene: un número y un umbral

## Narración

<!-- b1 -->
Hoy hemos visto que hay dos maneras de equivocarse, la falsa alarma y el
fallo, y que las dos son colas de campana. Mover el umbral solo cambia una por
otra. Y cuánto creerle a un positivo depende de lo raro que sea lo que buscas.

- «dos maneras de equivocarse» → `dos`: la tabla 2 × 2 con sus dos cruces rojas
- «la falsa alarma» → `fa`: se resalta la cruz de la falsa alarma
- «el fallo» → `fallo`: se resalta la cruz del fallo
- «colas de campana» → `colas`: las cruces vuelan a las dos colas rojas de las campanas
- «Mover el umbral» → `umbral`: el umbral se desliza a la derecha
- «una por otra» → `cambia`: una cola encoge y la otra crece
- «cuánto creerle a un positivo» → `creer`: a la derecha, «+ → ?»
- «lo raro que sea lo que buscas» → `raro`: la curva del valor predictivo, en pequeño

<!-- b2 -->
Pero ese umbral lo hemos sacado mirando dónde se cruzan dos curvas. ¿Y si
cualquier buena decisión se pudiera escribir comparando un solo número con un
umbral? Lo veremos en el próximo episodio: un número y un umbral.

- «dónde se cruzan dos curvas» → `cruce`: corte; las campanas escaladas (70 % y 30 %) y su cruce en 1,42 marcado
- «¿Y si cualquier buena decisión» → `pregunta`: las curvas se atenúan; un «?» ámbar
- «un solo número» → `numero`: una caja «Un número»
- «con un umbral» → `umbral`: «≷ Umbral» a su lado
- «en el próximo episodio» → `proximo`: tarjeta «Episodio 3»
- «un número y un umbral» → `titulo`: el título «Un número y un umbral» con rebote
