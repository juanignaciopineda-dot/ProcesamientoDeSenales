# Episodio 2 — Cuando sabes algo más

Capítulo 7 (Modelos probabilísticos), episodio 2 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 05 a 08), más un gancho y un cierre nuevos.
Retoma el dado y el rectángulo del espacio muestral del E1; el test médico y el canal de bits son los ejemplos que vuelven en los Caps. 8, 9 y 13.

**Estado:** **Subido a YouTube y publicado** (subido el 17/10/2026, público desde el 19/10): render final 1080p60 de 8:54, con título, descripción con `capitulos.txt`, subtítulos `.srt`, categoría Educación y «no es para niños» (https://youtu.be/43BeCcP9gUQ). Lo subió el usuario sin el visto bueno que figuraba pendiente en este estado (texto ⭐ / mp4 / pronunciaciones): la aprobación queda en su revisión antes de publicarlo. Residuos limpiados el 17/10/2026; se rehace con `python rehacer.py Capitulo07_Probabilidad`. La caché de voz versionada (`media/voiceovers/`) se volvió a sintetizar después de la subida: un render nuevo es reproducible, pero la voz puede diferir un poco de la del vídeo subido.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Un test médico acierta el noventa y nueve por ciento de las veces. Das positivo. Y aun así, lo más probable es que estés sano…».
- ⭐ Escena 14 (cierre): resume el episodio, plantea la pregunta de cómo se describe un número que no sabemos cuánto va a valer y anuncia E3, «La forma del azar».
- Sin otros retoques: las escenas 03 a 13 son el texto del guion base tal cual, partido en escenas atómicas (las frases «en un minuto» y «dentro de unos capítulos» siguen valiendo).

---

# Escena 01 — Gancho

**Capítulo YouTube:** Un test que acierta el 99 % y casi siempre se equivoca

## Narración

<!-- b1 -->
Un test médico acierta el noventa y nueve por ciento de las veces. Das positivo. Y aun así, lo más probable es que estés sano. ¿Cómo puede ser?

- «Un test médico» → `test`: entra un test con una tira de papel y el rótulo «test»
- «noventa y nueve por ciento» → `99`: aparece «99 %» grande, en verde
- «Das positivo» → `positivo`: la tira se marca con un «+» en rojo
- «lo más probable es que estés sano» → `sano`: una persona sana con un «+» encima, a un lado «?»
- «¿Cómo puede ser?» → `pregunta`: el «?» crece y todo se aleja en un fundido

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Cuando sabes algo más

## Narración

<!-- b1 -->
Cuando sabes algo más.

- «Cuando sabes» → `t1`: «Cuando sabes» entra con rebote
- «algo más» → `t2`: «algo más» entra debajo, con la etiqueta «Capítulo 7 · Modelos probabilísticos»

---

# Escena 03 — DadoPar

**Capítulo YouTube:** Saber algo achica el mundo

## Narración

<!-- b1 -->
Tiras un dado. ¿Qué probabilidad hay de que salga un seis? Un sexto: seis caras y todas pesan lo mismo. Ahora alguien mira el dado antes que tú y te dice que ha salido un número par. Te hago la misma pregunta. ¿Qué probabilidad hay de que sea un seis? Piénsalo un momento antes de seguir.

- «Tiras un dado» → `dado`: el rectángulo del E1 con las seis caras y un dado cayendo
- «un seis» → `seis`: la cara del seis se resalta
- «Un sexto» → `sexto`: aparece «P(6) = 1/6» sobre el seis
- «todas pesan lo mismo» → `pesan`: las seis caras se igualan, cada una con «1/6»
- «alguien mira el dado antes que tú» → `mira`: entra un ojo grande delante del dado
- «ha salido un número par» → `par`: aparece una nota «¡par!» y el dos, el cuatro y el seis brillan
- «Te hago la misma pregunta» → `misma`: «P(6) = ?» con el «1/6» tachado
- «¿Qué probabilidad hay de que sea un seis?» → `otra_vez`: la pregunta «P(6) = ?» vuelve a latir sobre el seis, con un globo de duda
- «Piénsalo un momento» → `piensalo`: un reloj de arena y tres globos de duda sobre el dado

<!-- b2 -->
La respuesta es un tercio. Lo que ha pasado es que el mundo se ha hecho más pequeño. El uno, el tres y el cinco ya no son posibles: quedan el dos, el cuatro y el seis. El seis sigue siendo una cara, pero ahora es una entre tres. El dado no ha cambiado. Ha cambiado el universo dentro del cual medimos.

- «La respuesta es un tercio» → `tercio`: el «?» se convierte en «1/3» con rebote
- «el mundo se ha hecho más pequeño» → `pequeno`: el rectángulo empieza a encogerse
- «El uno, el tres y el cinco» → `impares`: las caras 1, 3 y 5 se señalan
- «ya no son posibles» → `fuera`: esas tres caras se apagan y salen del rectángulo
- «quedan el dos, el cuatro y el seis» → `quedan`: el rectángulo queda ajustado alrededor del 2, el 4 y el 6
- «El seis sigue siendo una cara» → `sigue`: el seis se resalta y su recuadro brilla, con «1 cara»
- «una entre tres» → `entre3`: «1 de 3» junto al seis
- «El dado no ha cambiado» → `igual`: el dado gira intacto, con brillo
- «Ha cambiado el universo» → `universo`: un marco grande, el rectángulo viejo, se desvanece y queda el pequeño

---

# Escena 04 — FormulaCondicional

**Capítulo YouTube:** La probabilidad condicional

## Narración

<!-- b1 -->
Hagamos la misma cuenta con probabilidades, para poder repetirla en cualquier situación. La probabilidad de que salga un seis y además sea par es un sexto. La probabilidad de que salga par es un medio. Si dividimos un sexto entre un medio, sale un tercio. Lo mismo que al contar.

- «con probabilidades» → `probs`: el recuento «1 de 3» se queda a un lado y aparece una columna vacía de cuenta
- «para poder repetirla» → `repetir`: una flecha circular «repetir» junto a la columna de cuenta
- «cualquier situación» → `cualquiera`: varias situaciones pequeñas (dado, moneda, test) pasan por la columna de cuenta
- «salga un seis y además sea par» → `seis_par`: el óvalo de los pares y el seis dentro; «P(6 y par)»
- «es un sexto» → `sexto`: «= 1/6»
- «salga par es un medio» → `medio`: «P(par) = 1/2», con las tres caras pares iluminadas
- «Si dividimos» → `divide`: una fracción «(1/6) / (1/2)» se arma pieza a pieza
- «sale un tercio» → `tercio`: «= 1/3»
- «Lo mismo que al contar» → `igual`: se enlaza con una flecha al «1 de 3» de antes, con una tilde verde

<!-- b2 -->
Eso es la probabilidad condicional. Se escribe P de A, barra vertical, B, y se lee: la probabilidad de A, dado B. Se calcula dividiendo la probabilidad de que ocurran A y B a la vez entre la probabilidad de B. El numerador es lo que queda de A dentro del mundo nuevo. El denominador mide el mundo nuevo, para que vuelva a valer uno entero.

- «Eso es la probabilidad condicional» → `titulo`: entra «probabilidad condicional» con rebote
- «P de A, barra vertical, B» → `escritura`: se construye «P(A | B)» pieza a pieza
- «dado B» → `dado`: la barra se ilumina con la palabra «dado»
- «que ocurran A y B a la vez» → `num`: aparece «=», y encima la pieza «P(A y B)»
- «entre la probabilidad de B» → `den`: debajo, la raya de fracción y «P(B)»
- «El numerador» → `numerador`: el numerador se resalta
- «dentro del mundo nuevo» → `dentro`: el óvalo A recortado dentro del óvalo B
- «El denominador mide el mundo nuevo» → `denominador`: el denominador se resalta y B se rodea con un marco
- «vuelva a valer uno entero» → `uno`: el marco de B se llena y marca «= 1»

<!-- b3 -->
Una condición es que B tiene que ser posible, porque no se puede dividir entre cero. Y fíjate en que, dándole la vuelta a la fórmula, obtenemos otra muy útil: la probabilidad de que ocurran A y B es la probabilidad de B por la de A dado B. Primero pasa B, y después, sabiendo eso, pasa A. La usaremos en un minuto.

- «B tiene que ser posible» → `posible`: «P(B) > 0» junto a la fórmula
- «no se puede dividir entre cero» → `cero`: una fracción con denominador «0» y una cruz roja
- «dándole la vuelta a la fórmula» → `vuelta`: la fórmula gira y se despeja: «P(A y B) =»
- «otra muy útil» → `util`: una estrella junto a la fórmula despejada
- «la probabilidad de B por la de A dado B» → `producto`: se completa «P(B) · P(A | B)» y se enmarca como «regla del producto»
- «Primero pasa B» → `primero`: «B» se enciende en primer lugar, con un «1»
- «sabiendo eso, pasa A» → `despues`: «A» se enciende en segundo lugar, con un «2»
- «La usaremos en un minuto» → `usaremos`: la regla queda guardada en un estante de «herramientas»

---

# Escena 05 — SinCambio

**Capítulo YouTube:** Eventos independientes

## Narración

<!-- b1 -->
A veces la información nueva no cambia nada. Tiras un dado y lanzas una moneda. Alguien te dice que la moneda ha salido cara. ¿Cambia en algo la probabilidad de sacar un seis? No: el dado no sabe qué hizo la moneda. Sigue siendo un sexto.

- «no cambia nada» → `nada`: aparece «información nueva» con un signo igual a «sin efecto»
- «Tiras un dado y lanzas una moneda» → `dado_moneda`: un dado y una moneda lado a lado
- «Alguien te dice» → `alguien`: un globo de diálogo sale de una persona hacia el dado y la moneda
- «la moneda ha salido cara» → `cara`: la moneda cae y muestra cara; una nota «¡cara!»
- «¿Cambia en algo la probabilidad» → `pregunta`: «P(6) = ?» sobre el dado
- «No:» → `no`: un «no» grande en rojo sobre el «P(6) = ?»
- «el dado no sabe qué hizo la moneda» → `no_sabe`: un hilo entre dado y moneda que se corta con unas tijeras
- «Sigue siendo un sexto» → `sexto`: «P(6 | cara) = 1/6», igual que antes, con una tilde

<!-- b2 -->
Cuando saber B no cambia la probabilidad de A, decimos que A y B son independientes. Y entonces pasa algo cómodo. La regla que acabamos de ver decía que la probabilidad de A y B es la de B por la de A dado B. Si son independientes, la de A dado B es simplemente la de A. Así que la probabilidad de que ocurran las dos cosas es el producto de sus probabilidades.

- «saber B no cambia la probabilidad de A» → `no_cambia`: «P(A | B) = P(A)» se construye pieza a pieza
- «independientes» → `indep`: entra «independientes» con rebote
- «algo cómodo» → `comodo`: aparece una pequeña señal de «cuentas más fáciles»
- «La regla que acabamos de ver» → `regla`: vuelve la regla del producto «P(A y B) = P(B) · P(A | B)»
- «la de B por la de A dado B» → `rb`: se resaltan las dos piezas de la derecha
- «Si son independientes» → `si_indep`: la pieza «P(A | B)» se pone en ámbar
- «es simplemente la de A» → `solo_a`: «P(A | B)» se transforma en «P(A)»
- «ocurran las dos cosas» → `dos_cosas`: «P(A y B)» aparece a la izquierda de un «=»
- «el producto de sus probabilidades» → `producto`: queda «P(A y B) = P(A) · P(B)» con marco

<!-- b3 -->
Comprobémoslo contando. Un dado y una moneda dan doce combinaciones, todas igual de probables. Seis con cara es solo una de ellas: un doceavo. Y un sexto por un medio da un doceavo. Encaja.

- «Comprobémoslo contando» → `contar`: una cuadrícula vacía de 6 columnas y 2 filas
- «doce combinaciones» → `doce`: se llenan las 12 casillas con las parejas dado-moneda
- «todas igual de probables» → `igual`: cada casilla con «1/12»
- «Seis con cara» → `seis_cara`: se ilumina la casilla del 6 con cara
- «un doceavo» → `doceavo`: «1/12» sobre la casilla iluminada
- «un sexto por un medio» → `cuenta`: «1/6 · 1/2 = 1/12»
- «Encaja» → `encaja`: tilde verde entre las dos cuentas

---

# Escena 06 — NoIndependientes

**Capítulo YouTube:** Cuando no son independientes

## Narración

<!-- b1 -->
Pero cuidado, porque no todo es independiente. Con un solo dado, piensa en dos eventos: sale par, y sale más de tres. Cada uno tiene probabilidad un medio. Si fueran independientes, que ocurran los dos valdría un cuarto. Pero los números pares mayores que tres son el cuatro y el seis: dos de seis caras, un tercio. No es un cuarto. Saber que salió par hace más probable que sea grande.

- «no todo es independiente» → `cuidado`: un triángulo de aviso con «¡cuidado!»
- «Con un solo dado» → `solo_dado`: el rectángulo con las seis caras
- «sale par, y sale más de tres» → `dos_eventos`: dos óvalos de colores, «par» y «más de 3»
- «Cada uno tiene probabilidad» → `cada`: los dos óvalos con una «P» sobre cada uno
- «un medio» → `medio`: «P(par) = 1/2» y «P(más de 3) = 1/2» bajo cada óvalo
- «Si fueran independientes» → `fueran`: aparece «1/2 · 1/2»
- «valdría un cuarto» → `cuarto`: «= 1/4» con un signo de pregunta
- «los números pares mayores que tres» → `pares_mayores`: la intersección de «par» y «más de 3» se rodea
- «el cuatro y el seis» → `cuatro_seis`: el 4 y el 6, en la intersección de los óvalos, brillan
- «dos de seis caras» → `dos_de_seis`: «2 / 6» sobre la intersección
- «un tercio» → `tercio`: «= 1/3»
- «No es un cuarto» → `no_cuarto`: «1/3 ≠ 1/4» con una cruz roja sobre el «1/4»
- «hace más probable que sea grande» → `grande`: al decir «par», el óvalo de «más de 3» se agranda: de 1/2 a 2/3

<!-- b2 -->
La independencia no se supone porque sí: se comprueba o se justifica. Cuando la tengamos, las cuentas se simplificarán muchísimo. Y cuando no la tengamos, la probabilidad condicional nos puede dar sorpresas enormes. Vamos a ver una que engaña a casi todo el mundo, incluidos muchos médicos.

- «no se supone porque sí» → `supone`: «independencia» con un interrogante, se aparta
- «se comprueba o se justifica» → `comprueba`: dos fichas, «se comprueba» y «se justifica»
- «Cuando la tengamos» → `cuando`: una tilde verde junto a «independencia»
- «las cuentas se simplificarán» → `simplifica`: «P(A y B) = P(A) · P(B)» brilla en verde
- «muchísimo» → `muchisimo`: la fórmula del producto se agranda un instante
- «cuando no la tengamos» → `sin`: la tilde se vuelve una cruz roja
- «sorpresas enormes» → `sorpresas`: «P(A | B)» con un signo de exclamación grande
- «engaña a casi todo el mundo» → `engana`: una multitud de personas con globos de «99 %»
- «muchos médicos» → `medicos`: una cruz de hospital y un médico entre la multitud

---

# Escena 07 — TestPregunta

**Capítulo YouTube:** El test que acierta el 99 %

## Narración

<!-- b1 -->
Una enfermedad la tiene una persona de cada cien. Existe un test muy bueno: si estás enfermo, da positivo el noventa y nueve por ciento de las veces. Si estás sano, se equivoca y da positivo solo un cinco por ciento de las veces. Te haces el test y da positivo. ¿Qué probabilidad hay de que estés enfermo? Elige una respuesta antes de seguir.

- «una persona de cada cien» → `uno_cien`: tarjeta «1 de cada 100 enfermo», con una persona en rojo entre cien
- «Existe un test muy bueno» → `test`: aparece el test, con una tira de papel
- «si estás enfermo» → `enfermo`: tarjeta «si estás enfermo» con una persona en rojo
- «el noventa y nueve por ciento» → `99`: «positivo el 99 %» en la tarjeta, con barra casi llena
- «Si estás sano» → `sano`: tarjeta «si estás sano» con una persona en verde
- «solo un cinco por ciento» → `5`: «positivo el 5 %», con barra casi vacía
- «Te haces el test y da positivo» → `positivo`: la tira se marca con «+» en rojo
- «¿Qué probabilidad hay de que estés enfermo?» → `pregunta`: «P(enfermo | positivo) = ?»
- «Elige una respuesta» → `elige`: cuatro opciones: «99 %», «95 %», «50 %», «17 %»

<!-- b2 -->
La mayoría dice noventa y nueve, o noventa y cinco. Hagamos la cuenta con mil personas, que es más fácil que con porcentajes. Una de cada cien está enferma: son diez. Las otras novecientas noventa están sanas.

- «noventa y nueve, o noventa y cinco» → `encuesta`: las barras de «99 %» y «95 %» crecen, con «la mayoría»
- «con mil personas» → `mil`: se arma una grilla de mil personas
- «más fácil que con porcentajes» → `facil`: «%» se tacha y queda «personas»
- «Una de cada cien está enferma» → `una_cien`: en cada tira de cien, una persona se pone en rojo
- «son diez» → `diez`: diez en rojo, «10»
- «novecientas noventa están sanas» → `sanas`: las otras en verde, «990»

---

# Escena 08 — TestCuenta

**Capítulo YouTube:** La cuenta de las mil personas

## Narración

<!-- b1 -->
De las diez enfermas, el test detecta prácticamente a todas: diez positivos. Ahora las sanas. El cinco por ciento de novecientas noventa es casi cincuenta. Cincuenta personas sanas que reciben un positivo. En total, unos sesenta positivos.

- «De las diez enfermas» → `diez`: las diez personas en rojo se separan arriba
- «detecta prácticamente a todas» → `detecta`: el test pasa por las diez y les pone un «+»
- «diez positivos» → `diez_pos`: «10 positivos»
- «Ahora las sanas» → `sanas`: el foco pasa a las 990 verdes
- «El cinco por ciento de novecientas noventa» → `cuenta`: «5 % de 990»
- «casi cincuenta» → `cincuenta`: «≈ 50»
- «sanas que reciben un positivo» → `falsos`: cincuenta personas verdes reciben un «+»
- «unos sesenta positivos» → `sesenta`: un recuadro rodea todos los «+»: «≈ 60»

<!-- b2 -->
Y de esos sesenta, solo diez están enfermos. Diez entre sesenta es un sexto: más o menos un diecisiete por ciento. Con un test que acierta el noventa y nueve por ciento de las veces, un positivo significa que lo más probable es que estés sano. La razón es que hay tantísimos más sanos que sus pocos errores superan a todos los enfermos juntos.

- «de esos sesenta» → `esos`: foco en el recuadro de los sesenta
- «solo diez están enfermos» → `solo_diez`: dentro del recuadro, diez rojos entre cincuenta verdes
- «Diez entre sesenta» → `diez_sesenta`: «10 / 60»
- «un sexto» → `sexto`: «= 1/6»
- «un diecisiete por ciento» → `17`: «≈ 17 %» grande, en rojo, y una tilde sobre la opción «17 %» de la encuesta
- «acierta el noventa y nueve por ciento» → `acierta`: vuelve «99 %»
- «un positivo significa» → `significa`: el «+» sobre la tira, con una flecha hacia «¿sano?»
- «lo más probable es que estés sano» → `sano`: un «+» con una persona verde, y «83 % sano» como etiqueta
- «tantísimos más sanos» → `tantos`: las 990 verdes crecen frente a las diez rojas
- «superan a todos los enfermos juntos» → `superan`: una balanza: 50 falsos positivos pesan más que 10 enfermos

---

# Escena 09 — LaVuelta

**Capítulo YouTube:** Dos preguntas que no son la misma

## Narración

<!-- b1 -->
El noventa y nueve por ciento era la probabilidad de dar positivo dado que estás enfermo. Lo que tú querías saber era la probabilidad de estar enfermo dado que has dado positivo. Son preguntas distintas, con respuestas muy distintas. Contar personas funciona, pero no siempre tendremos mil personas que contar. Necesitamos una fórmula que le dé la vuelta a la pregunta.

- «El noventa y nueve por ciento» → `99`: «99 %» en grande
- «dar positivo dado que estás enfermo» → `pos_dado_enf`: «P(+ | enfermo) = 99 %»
- «Lo que tú querías saber» → `querias`: una lupa recorre el rótulo y se detiene
- «estar enfermo dado que has dado positivo» → `enf_dado_pos`: debajo, «P(enfermo | +) ≈ 17 %»
- «Son preguntas distintas» → `distintas`: un «≠» entre las dos
- «respuestas muy distintas» → `resp`: «99 %» y «17 %» se separan con una flecha doble
- «Contar personas funciona» → `contar`: la grilla de mil personas aparece de nuevo, con una tilde
- «no siempre tendremos mil personas» → `no_siempre`: la grilla se desvanece, con un «?»
- «Necesitamos una fórmula» → `necesitamos`: una fórmula vacía «P(A | B) = ?» aparece en un recuadro
- «le dé la vuelta a la pregunta» → `vuelta`: las dos condicionales se intercambian con una flecha circular

---

# Escena 10 — BayesDeduccion

**Capítulo YouTube:** La regla de Bayes

## Narración

<!-- b1 -->
La fórmula sale de algo que ya tenemos. La probabilidad de que ocurran A y B se puede escribir de dos maneras: primero B y después A dado B, o primero A y después B dado A. Las dos dan lo mismo, porque es el mismo suceso. Así que igualamos las dos expresiones y despejamos la probabilidad de A dado B.

- «sale de algo que ya tenemos» → `ya_tenemos`: la regla del producto del estante, a la vista
- «ocurran A y B» → `ayb`: «P(A y B)» en el centro
- «de dos maneras» → `dos`: aparecen dos renglones de igualdad, vacíos
- «primero B y después A dado B» → `primera`: primer renglón: «P(A y B) = P(A | B) · P(B)»
- «primero A y después B dado A» → `segunda`: segundo renglón: «P(A y B) = P(B | A) · P(A)»
- «Las dos dan lo mismo» → `lo_mismo`: un signo «=» entre los dos renglones
- «el mismo suceso» → `mismo`: una llave une las dos «P(A y B)» como una sola
- «igualamos las dos expresiones» → `igualar`: «P(A | B) · P(B) = P(B | A) · P(A)»
- «despejamos la probabilidad de A dado B» → `despejar`: «P(B)» pasa a dividir al otro lado

<!-- b2 -->
Queda así: la probabilidad de A dado B es la probabilidad de B dado A, por la probabilidad de A, dividida entre la probabilidad de B. Esta es la regla de Bayes. Cada pieza tiene nombre. La probabilidad de A sola se llama a priori: lo que creías antes de mirar. La de B dado A es la verosimilitud: lo compatible que es lo que viste con A. Y el resultado, la probabilidad a posteriori: lo que crees después de mirar.

- «Queda así» → `queda`: «P(A | B) =» queda a la izquierda
- «la probabilidad de B dado A, por la probabilidad de A» → `numerador`: el numerador «P(B | A) · P(A)»
- «dividida entre la probabilidad de B» → `denominador`: el denominador «P(B)»
- «la regla de Bayes» → `bayes`: marco y la palabra «Bayes» con rebote
- «Cada pieza tiene nombre» → `nombres`: tres huecos de rótulo bajo las piezas
- «La probabilidad de A sola» → `a_sola`: «P(A)» se rodea con un recuadro
- «a priori» → `priori`: «a priori» bajo «P(A)»
- «lo que creías antes de mirar» → `antes`: un ojo cerrado junto a «P(A)»
- «la verosimilitud» → `verosimilitud`: «verosimilitud» bajo «P(B | A)»
- «lo compatible que es lo que viste» → `compatible`: un ojo abierto y un imán entre «lo visto» y «A»
- «Y el resultado» → `resultado`: «P(A | B)» a la izquierda se rodea con un recuadro
- «a posteriori» → `posteriori`: «a posteriori» bajo «P(A | B)»
- «lo que crees después de mirar» → `despues`: el ojo abierto junto a «P(A | B)»

---

# Escena 11 — ProbabilidadTotal

**Capítulo YouTube:** Ley de probabilidad total

## Narración

<!-- b1 -->
Falta el denominador, la probabilidad de B. En el test, ¿de cuántas formas se puede dar positivo? Estando enfermo o estando sano. Cada camino vale su probabilidad por la probabilidad de dar positivo por ese camino, y se suman. Eso se llama ley de probabilidad total: partes el mundo en casos que no se solapan, calculas cada caso, y sumas.

- «Falta el denominador» → `falta`: el denominador «P(B)» parpadea
- «En el test» → `en_test`: vuelve el test con la tira y el «+»
- «¿de cuántas formas se puede dar positivo?» → `formas`: un árbol: raíz con «positivo» al final de varias ramas
- «Estando enfermo» → `enfermo`: la rama «enfermo» → «+» se ilumina
- «estando sano» → `sano`: la rama «sano» → «+» se ilumina
- «Cada camino vale» → `camino`: cada rama lleva su producto: «P(enfermo) · P(+ | enfermo)»
- «de dar positivo por ese camino» → `por_camino`: cada rama recibe su «P(+ | …)»
- «y se suman» → `suman`: un «+» une las dos ramas
- «ley de probabilidad total» → `total`: entra «ley de probabilidad total» con rebote
- «casos que no se solapan» → `casos`: el rectángulo del mundo partido en dos trozos que no se tocan
- «calculas cada caso, y sumas» → `sumas`: «P(B) = P(B | A) P(A) + P(B | no A) P(no A)» se construye pieza a pieza

---

# Escena 12 — CanalPlanteo

**Capítulo YouTube:** Un canal que confunde bits

## Narración

<!-- b1 -->
Ahora un ejemplo de señales. Un emisor envía ceros y unos: un cero el setenta por ciento de las veces, un uno el treinta. El cable tiene ruido y cambia el bit un diez por ciento de las veces. Llega un uno. ¿Qué probabilidad hay de que se enviara un uno?

- «un ejemplo de señales» → `ejemplo`: aparece la línea del canal: emisor, cable y receptor
- «Un emisor envía ceros y unos» → `emisor`: el emisor lanza un «0» y un «1»
- «un cero el setenta por ciento» → `cero70`: «0: 70 %»
- «un uno el treinta» → `uno30`: «1: 30 %»
- «El cable tiene ruido» → `ruido`: un rayo sobre el cable
- «cambia el bit un diez por ciento» → `diez`: «10 %» sobre el rayo, y un «1» que se vuelve «0»
- «Llega un uno» → `llega`: el receptor muestra un «1»
- «¿Qué probabilidad hay de que se enviara un uno?» → `pregunta`: «P(enviado 1 | recibido 1) = ?»

---

# Escena 13 — CanalCuenta

**Capítulo YouTube:** Bayes en un canal ruidoso

## Narración

<!-- b1 -->
Hay dos caminos para recibir un uno. Por el primero: se envió un uno y llegó bien, cero coma tres por cero coma nueve, cero coma veintisiete. Por el otro: se envió un cero y el ruido lo cambió, cero coma siete por cero coma uno, cero coma cero siete.

- «Hay dos caminos» → `dos`: árbol de dos niveles con las ramas 0 y 1 y sus salidas
- «recibir un uno» → `recibir`: el receptor muestra un «1» y dos flechas llegan hasta él
- «se envió un uno y llegó bien» → `bien`: se ilumina la rama 1 → 1
- «cero coma tres por cero coma nueve» → `c1`: «0,3 · 0,9»
- «cero coma veintisiete» → `r1`: «= 0,27»
- «se envió un cero y el ruido lo cambió» → `cambio`: se ilumina la rama 0 → 1
- «cero coma siete por cero coma uno» → `c2`: «0,7 · 0,1»
- «cero coma cero siete» → `r2`: «= 0,07»

<!-- b2 -->
La probabilidad de recibir un uno es la suma: cero coma treinta y cuatro. Y Bayes dice que la probabilidad de que se enviara un uno es cero coma veintisiete entre cero coma treinta y cuatro: casi un ochenta por ciento. Así que, si tuvieras que apostar, dirías que se envió un uno. Elegir la explicación más probable después de mirar es, exactamente, lo que haremos para detectar señales dentro de unos capítulos.

- «de recibir un uno es la suma» → `suma`: «0,27 + 0,07» con un signo más entre las dos ramas
- «cero coma treinta y cuatro» → `c34`: «= 0,34»
- «Y Bayes dice» → `bayes`: la fórmula de Bayes se encaja con el numerador y el denominador
- «cero coma veintisiete entre cero coma treinta y cuatro» → `cociente`: «0,27 / 0,34»
- «casi un ochenta por ciento» → `ochenta`: «≈ 0,79» grande, en ámbar
- «si tuvieras que apostar» → `apostar`: una ficha de apuesta sobre el «1»
- «Elegir la explicación más probable» → `elegir`: el «1» se marca como «decisión»
- «después de mirar» → `mirar`: un ojo abierto sobre el «1» recibido
- «lo que haremos» → `haremos`: el «1» elegido se resalta con una flecha hacia delante
- «para detectar señales» → `detectar`: un cartel «Capítulo 9 · detectar», que se enciende en el mapa

---

# Escena 14 — Cierre

**Capítulo YouTube:** Lo que viene: la forma del azar

## Narración

<!-- b1 -->
Ya sabes qué le pasa a una probabilidad cuando llega información nueva, y cómo darle la vuelta con Bayes. Pero hasta ahora hablábamos de caras de un dado, es decir, de sucesos sueltos. Una señal es un número en cada instante. ¿Cómo se describe un número del que no sabemos cuánto va a valer? En el próximo episodio: «La forma del azar».

- «información nueva» → `nueva`: el sobre «¡nuevo!» y el rectángulo del dado que se encoge
- «darle la vuelta con Bayes» → `bayes`: la fórmula de Bayes con su flecha circular
- «caras de un dado» → `dado`: el dado con sus seis caras
- «Una señal es un número en cada instante» → `senal`: una curva ruidosa con un punto en cada instante
- «¿Cómo se describe un número» → `pregunta`: un «?» sobre un punto que no se sabe dónde caerá
- «cuánto va a valer» → `valer`: el «?» crece y el punto salta a varios sitios
- «En el próximo episodio» → `proximo`: un reloj de arena que gira hacia el siguiente episodio
- «La forma del azar» → `titulo`: entra el título del siguiente episodio con rebote
