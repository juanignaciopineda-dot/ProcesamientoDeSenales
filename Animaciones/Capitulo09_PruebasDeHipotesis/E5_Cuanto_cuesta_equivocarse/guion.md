# Episodio 5 — ¿Cuánto cuesta equivocarse?

Capítulo 9 (Pruebas de hipótesis), episodio 5 de 6. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 20 a 23), más un gancho y un cierre nuevos.

**Estado:** **Subido a YouTube en privado** el 19/10/2026: render final 1080p60 de 8:41, título buscable, descripción con el capítulo del libro y `capitulos.txt`, subtítulos, categoría Educación (https://youtu.be/nz83prMrdOs). Residuos limpiados; la caché de voz está en `media/voiceovers/`: se rehace con `python rehacer.py Capitulo09_PruebasDeHipotesis E5`. **Falta**: publicarlo (lo hace el usuario).
**Render final 1080p60 hecho** (8:40, 0 avisos): mp4, `.srt` y `capitulos.txt`
en `salida/`. Falta subirlo a YouTube y limpiar residuos (paso 17).

Texto nuevo (marcado con ⭐, ya aprobado):
- ⭐ Escena 01 (gancho): «Un análisis de sangre da uno coma tres. Lo más
  probable es que estés sano: un cincuenta y seis por ciento. Y aun así, la
  decisión correcta es tratarte como enfermo. ¿Cómo puede ser?»
- ⭐ Escena 02 (título): «¿Cuánto cuesta equivocarse?».
- ⭐ Retoque en la escena 03 (bloque b1): el guion base decía «Quedó una
  pregunta pendiente»; pasa a «Hace tres episodios quedó una pregunta
  pendiente», para pagar en voz alta la promesa del E2 («dentro de tres
  episodios»).
- ⭐ Escena 11 (cierre): resumen corto (con costes distintos se minimiza el
  coste esperado; sale la misma razón de verosimilitud con un umbral más bajo,
  0,62 en vez de 1,42; con el cuadrado del error, la misma maquinaria estima) y
  anuncia E6 por su título, «Decidir con datos de verdad».

Notas:
- El cierre del E4 (su escena 14) pregunta «¿Y si mandar a casa a un enfermo
  fuera mucho más grave que repetirle la prueba a un sano?» y anuncia este
  título. El gancho responde con un caso concreto (1,3 → «enfermo» aunque
  «sano» sea más probable). La escena 03·b1 repite esa imagen a propósito: es
  el pago de la promesa del E2, y el E4 solo la anunció. Si al usuario le suena
  redundante, el b1 puede empezar directamente por «En el test médico…».
- Reparto de las escenas del guion base: 20 → escenas 03 y 04; 21 → 05 y 06;
  22 → 07 y 08; 23 → 09 y 10. Solo se partieron bloques enteros: el texto del
  guion base no cambia (salvo el retoque de arriba). El bloque 23·b5 («Lo que
  tienes son datos») queda al final de la escena 10 y el cierre arranca desde ahí.
- Largo: ~1.090 palabras del guion base más ~140 de gancho, título y cierre
  ≈ 1.230 palabras, unos 8:10 de voz a 150 palabras por minuto. Es el episodio
  más corto del capítulo; está dentro del margen (~8,5–11 min con pausas y
  animación), así que no se estira.
- Números (recomprobados con Python): a priori 0,7 / 0,3, costes falsa alarma
  1 y fallo 5. En 1,3: a posteriori enfermo 0,44, sano 0,56; decir sano cuesta
  2,2 y decir enfermo 0,56. η = 0,47, umbral 0,62. Máximo a posteriori: umbral
  1,42, falsa alarma 0,077, fallo 0,28, error 0,139, coste 0,48. Riesgo mínimo:
  falsa alarma 0,27, fallo 0,084, error 0,21, coste 0,31. Pendientes de los
  tres puntos de la curva: 3,6 · 2,33 · 0,47.
- Ojo: «0,56» aparece dos veces con el mismo valor y dos sentidos (la
  probabilidad de estar sano y el coste de decir enfermo, que es 1 · 0,56). En
  pantalla, el coste siempre como «1 · 0,56 = 0,56».

---

# Escena 01 — Gancho

**Capítulo YouTube:** Lo más probable no es lo correcto

## Narración

<!-- b1 -->
Un análisis de sangre da uno coma tres. Lo más probable es que estés sano: un
cincuenta y seis por ciento. Y aun así, la decisión correcta es tratarte como
enfermo. ¿Cómo puede ser?

- «Un análisis de sangre» → `tubo`: entra un tubo de ensayo con sangre
- «uno coma tres» → `valor`: «1,3» grande con pop junto al tubo
- «Lo más probable» → `barras`: dos barras vacías, «Sano» y «Enfermo»
- «cincuenta y seis por ciento» → `sano56`: «Sano» crece a 56 % y «Enfermo» a 44 %
- «la decisión correcta» → `decision`: un sello baja desde arriba
- «tratarte como enfermo» → `enfermo`: el sello «Enfermo» cae sobre la barra más baja
- «¿Cómo puede ser?» → `pregunta`: «?» grande en ámbar

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** ¿Cuánto cuesta equivocarse?

## Narración

<!-- b1 -->
¿Cuánto cuesta equivocarse?

- «¿Cuánto cuesta equivocarse?» → `titulo`: el título del episodio con pop

---

# Escena 03 — PonerlesPrecio

**Capítulo YouTube:** Los errores no cuestan igual
**Objetivo:** pagar la pregunta del test médico (E2) y plantear el análisis de
sangre con las campanas de siempre y una tabla de costes.

## Narración

<!-- b1 -->
Hace tres episodios quedó una pregunta pendiente. En el test médico, si solo
contaba la probabilidad de error, lo mejor era decir siempre sano. Era absurdo
porque mandar a casa a un enfermo no cuesta lo mismo que repetirle la prueba a
un sano. La probabilidad de error cuenta los dos fallos igual.

- «Hace tres episodios» → `tarjeta`: la tarjeta del E2 «Siempre sano → 1 %» con su «?»
- «En el test médico» → `test`: detrás, la grilla de personas del test médico
- «lo mejor era decir siempre sano» → `siempre`: «Siempre sano» se ilumina
- «Era absurdo» → `absurdo`: la tarjeta se tacha en rojo
- «mandar a casa a un enfermo» → `casa`: a la izquierda, una persona roja camino de una casa
- «repetirle la prueba a un sano» → `repetir`: a la derecha, una persona con un tubo de ensayo
- «cuenta los dos fallos igual» → `balanza`: los dos dibujos sobre los platillos de una balanza equilibrada

<!-- b2 -->
Pongámosles precio. Usaremos las mismas campanas, con otro significado: un
análisis de sangre que da un número. En los sanos, centro cero. En los
enfermos, centro dos. De cada diez personas que llegan a la consulta con
síntomas, tres están enfermas.

- «Pongámosles precio» → `precio`: dos etiquetas de precio vacías cuelgan de los platillos
- «las mismas campanas» → `campanas`: corte; se dibujan las dos campanas de siempre (centros 0 y 2, desvío 1)
- «un análisis de sangre» → `analisis`: el eje se rotula «Resultado del análisis»
- «En los sanos, centro cero» → `sanos`: rótulo «Sano · Centro 0» sobre la campana izquierda
- «En los enfermos, centro dos» → `enfermos`: rótulo «Enfermo · Centro 2» sobre la derecha
- «De cada diez personas» → `diez`: diez personas en fila arriba
- «tres están enfermas» → `tres`: tres se pintan de rojo; «p₁ = 0,3» y «p₀ = 0,7»

<!-- b3 -->
Y una tabla de costes. Acertar no cuesta nada. Una falsa alarma, tratar a un
sano, cuesta uno. Un fallo, dejar ir a un enfermo, cuesta cinco. Los números
son inventados, pero la idea no: un error es cinco veces más grave que el otro.

- «una tabla de costes» → `tabla`: corte; tabla 2 × 2 vacía, «Realidad» contra «Decisión»
- «Acertar no cuesta nada» → `aciertos`: «0» en las dos casillas de la diagonal
- «Una falsa alarma» → `fa`: la casilla «Falsa alarma» se resalta
- «tratar a un sano» → `fa_ico`: dentro, una persona sana con una pastilla
- «cuesta uno» → `fa1`: «1» con pop
- «Un fallo» → `fallo`: la casilla «Fallo» se resalta
- «dejar ir a un enfermo» → `fallo_ico`: dentro, la persona roja camino de casa
- «cuesta cinco» → `fallo5`: «5» grande en rojo
- «Los números son inventados» → `inventados`: el 1 y el 5 parpadean
- «cinco veces más grave» → `cinco`: la balanza vuelve, pequeña, y se inclina hacia el fallo con «× 5»

---

# Escena 04 — ElCosteDeCadaDecision

**Capítulo YouTube:** La regla de riesgo mínimo
**Objetivo:** calcular el coste esperado de cada decisión para la medición de
1,3 y ver que conviene decir «enfermo» aunque «sano» sea más probable.

## Narración

<!-- b1 -->
El análisis sale uno coma tres. La regla del máximo a posteriori decía cero:
sano. Miremos los costes. Con ese resultado, la probabilidad a posteriori de
estar enfermo es cero coma cuarenta y cuatro, y la de estar sano, cero coma
cincuenta y seis.

- «El análisis sale uno coma tres» → `regla`: las campanas; una regla vertical cae en 1,3
- «La regla del máximo a posteriori» → `rotulo`: entra arriba el rótulo «Máximo a posteriori»
- «decía cero» → `map`: aparece el umbral en 1,42; el 1,3 queda a su izquierda: «Máximo a posteriori: Sano»
- «Miremos los costes» → `tabla`: la tabla de costes entra pequeña en una esquina
- «la probabilidad a posteriori» → `post`: las dos alturas escaladas se leen sobre la regla
- «cero coma cuarenta y cuatro» → `p44`: «P(Enfermo | 1,3) = 0,44»
- «cero coma cincuenta y seis» → `p56`: «P(Sano | 1,3) = 0,56»

<!-- b2 -->
Si digo sano, me equivoco con probabilidad cero coma cuarenta y cuatro, y eso
cuesta cinco: en promedio, dos coma dos. Si digo enfermo, me equivoco con
probabilidad cero coma cincuenta y seis, y eso cuesta uno: cero coma cincuenta
y seis. Decir enfermo sale cuatro veces más barato, aunque sano sea más
probable.

- «Si digo sano» → `digosano`: corte; renglón «Decir sano:»
- «cero coma cuarenta y cuatro» → `x44`: el «0,44» vuela desde arriba al renglón
- «eso cuesta cinco» → `x5`: el «5» de la tabla vuela delante: «5 · 0,44»
- «dos coma dos» → `r22`: «= 2,2» en rojo
- «Si digo enfermo» → `digoenf`: segundo renglón «Decir enfermo:»
- «probabilidad cero coma cincuenta y seis» → `x56`: el «0,56» vuela al segundo renglón
- «eso cuesta uno» → `x1`: el «1» de la tabla vuela delante: «1 · 0,56»
- «cero coma cincuenta y seis» → `r056`: «= 0,56» en verde
- «cuatro veces más barato» → `cuatro`: «2,2 ÷ 0,56 ≈ 4»; el renglón verde se resalta
- «sano sea más probable» → `aunque`: al lado, la barra «Sano 0,56» parpadea

<!-- b3 -->
Esta es la regla de riesgo mínimo. Ya no se elige la hipótesis más probable. Se
elige la decisión con menor coste esperado.

- «la regla de riesgo mínimo» → `riesgo`: «Riesgo mínimo» con pop
- «la hipótesis más probable» → `tacha`: «La hipótesis más probable» aparece y se tacha
- «menor coste esperado» → `coste`: «La decisión de menor coste esperado» en verde

---

# Escena 05 — DeLaCuentaALaRegla

**Capítulo YouTube:** Otra vez la razón de verosimilitud
**Objetivo:** deducir paso a paso que la regla de riesgo mínimo es un test de
razón de verosimilitud con umbral η = p₀ · C_FA / (p₁ · C_M).

## Narración

<!-- b1 -->
Convirtamos esa cuenta en una regla. Se dice uno cuando decir uno sale más
barato: cuando el coste de la falsa alarma, por la probabilidad a posteriori de
hache cero, es menor que el coste del fallo, por la probabilidad a posteriori
de hache uno.

- «Convirtamos esa cuenta en una regla» → `cuenta`: las dos cuentas de antes, pequeñas, arriba
- «Se dice uno» → `uno`: renglón 1, «Decir H₁ si:»
- «el coste de la falsa alarma» → `cfa`: «C_FA»
- «hache cero» → `ph0`: «· P(H₀ | r)»
- «es menor» → `menor`: «<»
- «el coste del fallo» → `cm`: «C_M»
- «hache uno» → `ph1`: «· P(H₁ | r)»

<!-- b2 -->
Pasamos las probabilidades a un lado y los costes al otro. La probabilidad a
posteriori del uno, entre la del cero, tiene que superar al coste de la falsa
alarma entre el coste del fallo. Aquí, un quinto. Es decir: basta con que la
probabilidad de estar enfermo pase de un sexto, un diecisiete por ciento, para
decir enfermo.

- «Pasamos las probabilidades a un lado» → `pasa`: las dos probabilidades se deslizan a la izquierda
- «los costes al otro» → `costes`: los costes, a la derecha; renglón 2
- «La probabilidad a posteriori del uno» → `cociente`: a la izquierda se forma «P(H₁ | r) / P(H₀ | r)»
- «tiene que superar» → `supera`: «>» en medio
- «al coste de la falsa alarma entre el coste del fallo» → `ccoc`: a la derecha, «C_FA / C_M»
- «Aquí, un quinto» → `quinto`: «= 1/5»
- «la probabilidad de estar enfermo» → `penf`: al lado, una barra vertical «P(Enfermo | r)» de 0 a 1
- «pase de un sexto» → `sexto`: al lado, «P(Enfermo | r) > 1/6»
- «un diecisiete por ciento» → `diecisiete`: «≈ 17 %»; una barra con la marca del 17 %
- «para decir enfermo» → `enfermo`: «→ Enfermo» en ámbar

<!-- b3 -->
Ahora, la regla de Bayes a la izquierda. El denominador común se cancela, y ese
cociente es pe uno entre pe cero, por la razón de verosimilitud. Despejamos: la
razón de verosimilitud tiene que superar a pe cero por el coste de la falsa
alarma, entre pe uno por el coste del fallo.

- «la regla de Bayes a la izquierda» → `bayes`: renglón 3; cada probabilidad a posteriori se escribe con Bayes, «p₁ f₁(r) / f(r)» y «p₀ f₀(r) / f(r)»
- «El denominador común se cancela» → `cancela`: los dos «f(r)» se tachan
- «pe uno entre pe cero» → `p1p0`: queda «(p₁ / p₀)»
- «por la razón de verosimilitud» → `lambda`: «· Λ(r)»
- «Despejamos» → `despeja`: «p₁ / p₀» cruza al otro lado de la desigualdad
- «pe cero por el coste de la falsa alarma» → `num`: numerador «p₀ · C_FA»
- «pe uno por el coste del fallo» → `den`: denominador «p₁ · C_M»: queda «Λ(r) > p₀ C_FA / (p₁ C_M)»

---

# Escena 06 — ElUmbralBaja

**Capítulo YouTube:** El umbral del riesgo
**Objetivo:** calcular η = 0,47 y el umbral 0,62, ver la franja que cambia de
decisión y comprobar que con costes iguales se recupera el máximo a posteriori.

## Narración

<!-- b1 -->
Otra vez la razón de verosimilitud contra un umbral. Solo ha cambiado eta. Con
nuestros números: cero coma siete por uno, entre cero coma tres por cinco. Cero
coma cuarenta y siete. Y el umbral sobre el análisis: uno más la mitad del
logaritmo de cero coma cuarenta y siete. Cero coma sesenta y dos.

- «Otra vez la razón de verosimilitud» → `marco`: la desigualdad se enmarca: «Λ(r) ≷ η»
- «Solo ha cambiado eta» → `eta`: «η = p₀ C_FA / (p₁ C_M)» en ámbar
- «cero coma siete por uno» → `num`: «0,7 · 1»
- «cero coma tres por cinco» → `den`: «0,3 · 5»
- «Cero coma cuarenta y siete» → `r047`: «= 0,47»
- «el umbral sobre el análisis» → `umbral`: «Umbral = 1 + ln(η) / 2»
- «la mitad del logaritmo» → `log`: «= 1 + ln(0,47) / 2 = 1 − 0,38»
- «Cero coma sesenta y dos» → `r062`: «= 0,62», enmarcado

<!-- b2 -->
El umbral ha bajado de uno coma cuarenta y dos a cero coma sesenta y dos. En
toda esa franja, donde antes se decía sano, ahora se dice enfermo. Si dejar ir
a un enfermo sale caro, más vale pasarse de precavido.

- «El umbral ha bajado» → `campanas`: corte; las campanas con el umbral en 1,42
- «a cero coma sesenta y dos» → `desliza`: el umbral se desliza de 1,42 a 0,62
- «En toda esa franja» → `franja`: la franja entre 0,62 y 1,42 se ilumina
- «ahora se dice enfermo» → `ahora`: rótulo «Aquí ahora: Enfermo»; la regla en 1,3 queda dentro
- «sale caro» → `caro`: el «5» de la tabla destella
- «pasarse de precavido» → `precavido`: la región «Enfermo» late una vez

<!-- b3 -->
Dos comprobaciones. Si los dos errores cuestan lo mismo, eta vuelve a ser pe
cero entre pe uno: el máximo a posteriori es un caso particular. Y si acertar
también costara algo, en la fórmula entraría la diferencia entre fallar y
acertar. Lo que cuenta es cuánto más cuesta equivocarse.

- «Dos comprobaciones» → `dos`: corte; «1» y «2» a la izquierda
- «cuestan lo mismo» → `iguales`: junto al 1, «C_FA = C_M»
- «eta vuelve a ser pe cero entre pe uno» → `etamap`: los costes se tachan: «η = p₀ / p₁»
- «el máximo a posteriori» → `mapeti`: rótulo «Máximo a posteriori» junto a «η = p₀ / p₁»
- «un caso particular» → `caso`: un círculo «Máximo a posteriori» dentro de otro «Riesgo mínimo»
- «si acertar también costara algo» → `acertar`: junto al 2, «η = p₀ (c₁₀ − c₀₀) / p₁ (c₀₁ − c₁₁)»
- «la diferencia entre fallar y acertar» → `llave`: llaves bajo los dos paréntesis
- «cuánto más cuesta equivocarse» → `lema`: rótulo «Cuánto más cuesta fallar que acertar»

---

# Escena 07 — DosVaras

**Capítulo YouTube:** Error contra coste
**Objetivo:** medir las dos reglas con la probabilidad de error y con el coste
medio, llenando la tabla celda a celda.

## Narración

<!-- b1 -->
Tenemos dos reglas sobre las mismas campanas: la del máximo a posteriori, con
el umbral en uno coma cuarenta y dos, y la de riesgo mínimo, con el umbral en
cero coma sesenta y dos. Midamos las dos con las dos varas: la probabilidad de
error y el coste medio.

- «Tenemos dos reglas» → `campanas`: corte; las campanas con dos umbrales
- «la del máximo a posteriori» → `map`: el umbral de 1,42 se rotula «Máximo a posteriori»
- «uno coma cuarenta y dos» → `u142`: «1,42» bajo ese umbral
- «la de riesgo mínimo» → `riesgo`: el de 0,62, «Riesgo mínimo»
- «cero coma sesenta y dos» → `u062`: «0,62» bajo el otro
- «Midamos las dos» → `tabla`: las campanas suben; abajo, tabla de dos renglones
- «la probabilidad de error» → `colerr`: cabecera «Error»
- «el coste medio» → `colcoste`: cabecera «Coste»

<!-- b2 -->
El máximo a posteriori: falsa alarma cero coma cero setenta y siete, fallo
cero coma veintiocho. Su error ya lo sabemos: cero coma ciento treinta y nueve.
Su coste: cero coma cero cincuenta y cuatro de las falsas alarmas, más cero
coma cero ochenta y cinco de los fallos multiplicado por cinco. En total, cero
coma cuarenta y ocho.

- «falsa alarma cero coma cero setenta y siete» → `fa`: cola de la campana del 0 a la derecha de 1,42; celda «0,077»
- «fallo cero coma veintiocho» → `fallo`: cola de la campana del 2 a la izquierda; celda «0,28»
- «Su error ya lo sabemos» → `errya`: debajo, «0,7 · 0,077 + 0,3 · 0,28»
- «cero coma ciento treinta y nueve» → `err`: celda «0,139»
- «Su coste» → `coste`: debajo, «0,7 · 0,077 · 1 + 0,3 · 0,28 · 5»
- «cero coma cero cincuenta y cuatro» → `c1`: «= 0,054 +»
- «de las falsas alarmas» → `cfa_lbl`: llave «Falsas alarmas» bajo el 0,054
- «cero coma cero ochenta y cinco» → `c085`: «0,085» con la llave «Fallos»
- «multiplicado por cinco» → `c2`: «0,085 · 5 = 0,42»
- «cero coma cuarenta y ocho» → `c048`: celda «0,48»

<!-- b3 -->
El riesgo mínimo: la falsa alarma sube a cero coma veintisiete y el fallo baja
a cero coma cero ochenta y cuatro. Su error: cero coma veintiuno. Su coste:
cero coma diecinueve, más cero coma ciento veinticinco. Cero coma treinta y
uno.

- «la falsa alarma sube» → `fa`: con el umbral en 0,62 la cola del 0 se ensancha; celda «0,27»
- «el fallo baja» → `fallo`: la cola del 2 adelgaza; celda «0,084»
- «Su error» → `errlbl`: debajo, «0,7 · 0,27 + 0,3 · 0,084»
- «cero coma veintiuno» → `err`: celda «0,21»
- «cero coma diecinueve» → `c1`: debajo, «0,19 +»
- «cero coma ciento veinticinco» → `c2`: «0,125»
- «Cero coma treinta y uno» → `c031`: celda «0,31»

---

# Escena 08 — TresPuntosDeLaCurva

**Capítulo YouTube:** Riesgo no es error
**Objetivo:** ver que cada regla gana con su vara, sin contradicción, y ubicar
los tres criterios como tres puntos de la misma curva ROC.

## Narración

<!-- b1 -->
El máximo a posteriori gana en error: catorce por ciento contra veintiuno. El
riesgo mínimo gana en coste: cero coma treinta y uno contra cero coma cuarenta
y ocho. No hay contradicción: persiguen cosas distintas. El segundo acepta más
del triple de falsas alarmas para que se le escapen ocho enfermos de cada cien,
en lugar de veintiocho.

- «gana en error» → `verr`: la celda «0,139» se pinta de verde
- «catorce por ciento contra veintiuno» → `cmp1`: «14 % < 21 %»
- «El riesgo mínimo» → `rmfila`: se resalta el renglón «Riesgo mínimo»
- «gana en coste» → `vcoste`: la celda «0,31», en el otro renglón, en verde
- «treinta y uno contra» → `cmp2`: «0,31 < 0,48»
- «No hay contradicción» → `nocontra`: los dos verdes quedan en diagonal
- «persiguen cosas distintas» → `distintas`: rótulo «Objetivos distintos»
- «El segundo acepta» → `segundo`: se resaltan las dos celdas de falsa alarma
- «más del triple de falsas alarmas» → `triple`: «0,077 → 0,27 · × 3,5»
- «ocho enfermos de cada cien» → `ocho`: corte; cien enfermos en filas, ocho en rojo: «8 se escapan»
- «en lugar de veintiocho» → `veintiocho`: al lado, la misma fila con veintiocho en rojo: «28 se escapan»

<!-- b2 -->
En la curva es un punto más, donde la pendiente vale cero coma cuarenta y
siete: más arriba y más a la derecha. Tres criterios, tres puntos de la misma
curva. Neyman-Pearson, donde la curva es más empinada. El máximo a posteriori,
en medio. El riesgo mínimo, donde ya se tumba.

- «En la curva es un punto más» → `curva`: corte; la curva del E4 con sus dos puntos y el «?»
- «cero coma cuarenta y siete» → `pend`: una tangente de pendiente 0,47 toca la curva
- «más arriba y más a la derecha» → `punto`: el «?» se llena: «(0,27; 0,92)»
- «Tres criterios» → `tres`: los tres puntos se iluminan
- «Neyman-Pearson» → `np`: «Neyman-Pearson · 3,6» con su tangente empinada
- «El máximo a posteriori» → `map`: «Máximo a posteriori · 2,33»
- «El riesgo mínimo» → `rm`: «Riesgo mínimo · 0,47»
- «se tumba» → `tumba`: las tres tangentes juntas; la última, casi plana, se resalta

<!-- b3 -->
La moraleja: minimizar la probabilidad de error es lo correcto solo si todos
los errores cuestan lo mismo. Cuando no es así, hay que minimizar el coste. Y
lo que cambia es el umbral, no el detector.

- «La moraleja» → `moraleja`: corte; pantalla limpia
- «solo si todos los errores cuestan lo mismo» → `si`: «Mínimo error ⇔ Costes iguales»
- «Cuando no es así» → `noasi`: debajo, los costes 1 y 5 se separan
- «hay que minimizar el coste» → `coste`: «Si no: Mínimo coste»
- «cambia es el umbral» → `umbral`: «Cambia el umbral,» con pop
- «no el detector» → `detector`: «no el detector», con la curva pequeña debajo

---

# Escena 09 — DeElegirADarUnValor

**Capítulo YouTube:** Decidir y estimar
**Objetivo:** unir con el capítulo 8: acertar o fallar da la moda (el máximo a
posteriori); al juntar las hipótesis hasta un continuo, el coste cuadrático da
la media condicional.

## Narración

<!-- b1 -->
Con los costes sobre la mesa, se cierra el círculo con el capítulo anterior.
Allí vimos que la mejor apuesta depende de cómo se mide el error. Con el
cuadrado sale la media. Con acertar o fallar, la moda: lo más probable. La
regla del máximo a posteriori es exactamente eso: coste cero si aciertas, uno
si fallas.

- «se cierra el círculo» → `circulo`: un arco une «Capítulo 8» con «Capítulo 9» y se cierra
- «Allí vimos» → `alli`: se van «Capítulo 9» y los arcos; la casilla «Capítulo 8» sube arriba
- «la mejor apuesta depende» → `casillas`: las tres casillas del Cap. 8: «Cuadrado → Media», «Tamaño → Mediana», «Acierto → Moda»
- «Con el cuadrado sale la media» → `media`: «Cuadrado → Media» se ilumina
- «Con acertar o fallar» → `acierto`: la casilla «Acierto» se resalta
- «la moda» → `moda`: «Acierto → Moda» se ilumina
- «La regla del máximo a posteriori» → `map`: una flecha une «Moda» con «Máximo a posteriori»
- «coste cero si aciertas» → `cero`: tabla 0–1, «0» en la diagonal
- «uno si fallas» → `uno`: «1» fuera de la diagonal

<!-- b2 -->
Ahora junta las hipótesis. Con dos amplitudes posibles, cero y dos voltios,
eliges entre dos. Con tres, entre tres. Con nueve. Con cien niveles, cada vez
más apretados. En el límite, la amplitud puede ser cualquier número, y ya no
eliges entre opciones: das un valor. Eso es estimar.

- «Ahora junta las hipótesis» → `eje`: corte; eje de voltios con las dos campanas en 0 y 2
- «Con dos amplitudes posibles» → `amp`: «0 V» y «2 V» bajo los centros
- «eliges entre dos» → `dos`: rótulo «¿Cuál de estas?»; las dos campanas parpadean
- «Con tres, entre tres» → `tres`: pasan a ser tres campanas más estrechas
- «Con nueve» → `nueve`: nueve
- «Con cien niveles» → `cien`: cien campanas finas, casi una franja
- «En el límite» → `limite`: las campanas se aprietan hasta tocarse
- «cualquier número» → `continuo`: se funden en un eje continuo
- «das un valor» → `valor`: un marcador en un punto del eje; «¿Cuánto?» sustituye a «¿Cuál de estas?»
- «Eso es estimar» → `estimar`: «Estimar» con pop

<!-- b3 -->
En ese límite, acertar o fallar deja de servir: nunca vas a dar con el valor
exacto. Hay que medir cuánto te alejas, y lo habitual es el cuadrado del error.
Con ese coste, la regla de riesgo mínimo da la media condicional: el estimador
del capítulo ocho.

- «acertar o fallar deja de servir» → `dardo`: un dardo cae junto al valor, nunca justo encima
- «nunca vas a dar con el valor exacto» → `prob0`: «Acertar: Probabilidad 0»
- «cuánto te alejas» → `distancia`: una flecha mide la distancia del dardo al valor
- «el cuadrado del error» → `parabola`: la tabla 0–1 se sustituye por una parábola: «Coste = Error²»
- «la regla de riesgo mínimo» → `rm`: rótulo «Riesgo mínimo» con la parábola dentro
- «la media condicional» → `media`: una curva a posteriori sobre el eje; se marca su centro de masa
- «el estimador del capítulo ocho» → `cap8`: etiqueta «Media condicional · Capítulo 8»

---

# Escena 10 — LaMismaMaquinaria

**Capítulo YouTube:** Cuál de estas, o cuánto
**Objetivo:** detectar y estimar son la misma maquinaria con distinto coste; el
0,79 y el 1 del canal responden a preguntas distintas.

## Narración

<!-- b1 -->
Es la misma maquinaria: probabilidades a posteriori y el menor coste esperado.
Solo cambia el coste, y con él, el tipo de respuesta. Detectar responde a cuál
de estas pocas. Estimar responde a cuánto. Por eso, en el canal, el cero coma
setenta y nueve y el uno eran las dos respuestas correctas: a dos preguntas
distintas.

- «Es la misma maquinaria» → `maquina`: corte; un bloque con dos partes, «A posteriori» y «Menor coste esperado», apagadas
- «probabilidades a posteriori» → `post`: se ilumina la parte «A posteriori» del bloque
- «el menor coste esperado» → `menor`: se ilumina «Menor coste esperado»
- «Solo cambia el coste» → `coste`: entra «Coste» al bloque; alterna entre «0–1» y «Error²»
- «el tipo de respuesta» → `salida`: la salida alterna entre «H₀ / H₁» y «Un número»
- «Detectar responde» → `detectar`: «Detectar: ¿Cuál de estas?»
- «Estimar responde a cuánto» → `estimar`: «Estimar: ¿Cuánto?»
- «en el canal» → `canal`: corte; el canal de bits del Cap. 7
- «setenta y nueve» → `v079`: «0,79» bajo «Estimar»
- «y el uno» → `v1`: «1» bajo «Decidir»
- «a dos preguntas» → `preguntas`: sobre cada respuesta, su pregunta: «¿Cuánto?» y «¿Cuál?»

<!-- b2 -->
Todo lo que hemos hecho supone algo muy cómodo: que conocemos las dos campanas.
En la práctica nadie te las da. Lo que tienes son datos.

- «algo muy cómodo» → `comodo`: corte; las dos campanas, nítidas
- «conocemos las dos campanas» → `conocidas`: rótulo «Conocidas» sobre ellas
- «nadie te las da» → `borra`: las campanas se borran
- «Lo que tienes son datos» → `datos`: en su lugar, marcas sueltas sobre el eje, una por caso

---

# Escena 11 — Cierre

**Capítulo YouTube:** Lo que viene: decidir con datos de verdad

## Narración

<!-- b1 -->
Hoy hemos visto que, cuando un error cuesta más que el otro, no se minimiza la
probabilidad de error, sino el coste esperado. Y sale otra vez la razón de
verosimilitud contra un umbral, solo que más bajo: cero coma sesenta y dos en
vez de uno coma cuarenta y dos. Con el cuadrado del error, la misma maquinaria
sirve para estimar.

- «cuando un error cuesta más que el otro» → `balanza`: corte; la balanza inclinada con «× 5»
- «no se minimiza la probabilidad de error» → `tacha`: «Mínimo error» aparece y se tacha
- «el coste esperado» → `coste`: «Mínimo coste esperado» en verde
- «la razón de verosimilitud» → `lambda`: «Λ(r) ≷ η»
- «solo que más bajo» → `bajo`: las campanas; el umbral baja
- «cero coma sesenta y dos» → `u062`: «0,62»
- «uno coma cuarenta y dos» → `u142`: al lado, «1,42» tachado
- «Con el cuadrado del error» → `cuadrado`: «Error²» con una parábola pequeña
- «sirve para estimar» → `estimar`: «→ Media condicional»

<!-- b2 -->
Pero sin campanas no hay razón de verosimilitud, ni curva, ni umbral. ¿Cómo se
decide con una lista de casos y nada más? Lo veremos en el próximo episodio:
decidir con datos de verdad.

- «sin campanas» → `sin`: las campanas se desvanecen
- «ni curva, ni umbral» → `ni`: «Λ», «Curva» y «Umbral» se tachan uno tras otro
- «una lista de casos» → `lista`: una lista de casos marcados con «+» y «−»
- «en el próximo episodio» → `proximo`: tarjeta «Episodio 6 · Decidir con datos de verdad»
