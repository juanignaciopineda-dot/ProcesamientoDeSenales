# Episodio 2 — Lo que sabe el pasado

Capítulo 12 (Estimación de señales), episodio 2 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 05 a 08), más un gancho y un cierre nuevos.

**Estado:** escenas `s01`–`s11` escritas; borrador 480p15 de 8:50 con 0 avisos y hojas de contacto revisadas. Falta el visto bueno del usuario al mp4 (paso 15), la revisión del texto ⭐ (gancho y cierre) y el render final.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Hay una muestra que no tiene ninguna relación con lo que quieres adivinar, y aun así las cuentas le dan un coeficiente distinto de cero…»
- ⭐ Escena 11 (cierre): resumen y anuncia E3 por su título, «Mirar el registro entero».

Nota para el episodio anterior: el cierre de E1 tiene que anunciar este título, «Lo que sabe el pasado».

Reparto de las escenas del guion base: 05 → escenas 03 y 04; 06 → 05 y 06; 07 → 07, 08 y el inicio de 09; 08 → 09 (b1, b2) y 10 (b3 a b5).
Solo se agruparon bloques enteros en escenas atómicas: el texto del guion base no cambia (salvo el gancho y el cierre).

Hilos que este episodio abre o paga (ver `../guion_base.md`):
- «¿A qué se acerca el error y por qué 0,157?» (escena 04): se abre aquí; se paga en la escena 19 (E5).
- El eco del 0,6 (escenas 05 y 06): «solo importa la última muestra»; vuelve en la 22 y la 23 (E6).
- Las tres barras ρ, 1, ρ con ρ = 0,4 (escenas 07 a 10): el mismo dibujo del Cap. 11 (filtro (2, 1)/√5).
- «No correlacionado no es inútil» (escena 10): ejemplo de regresión del Cap. 8.
- «Se resuelve con una división» (escena 10): se anuncia aquí; se paga en E3 (escena 10 del capítulo) y la causal en E4.

---

# Escena 01 — Gancho

**Capítulo YouTube:** Una muestra que no se parece en nada

## Narración

<!-- b1 -->
Hay una muestra que no tiene ninguna relación con lo que quieres adivinar, y aun así las cuentas le dan un coeficiente distinto de cero. Hoy vemos por qué, y cuánto pasado hace falta de verdad.

- «Hay una muestra» → `muestra`: una tira de muestras x[n−1], x[n], con x[n−1] resaltada
- «ninguna relación con lo que quieres adivinar» → `sinrel`: una flecha desde x[n−1] hasta x[n+1] con «?» y un «correlación = 0» en rojo
- «las cuentas le dan un coeficiente» → `coef`: sobre x[n−1] aparece «h₁ = »
- «distinto de cero» → `distinto`: «−0,19» en ámbar, con una cruz sobre el cero esperado
- «Hoy vemos por qué» → `hoy`: la tira se aleja y entra una lupa sobre ella
- «cuánto pasado hace falta» → `pasado`: aparecen casillas hacia atrás x[n−2], x[n−3]… que se desvanecen

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Lo que sabe el pasado

## Narración

<!-- b1 -->
Lo que sabe el pasado.

- «Lo que sabe» → `t1`: «Lo que sabe» entra con rebote
- «el pasado» → `t2`: «el pasado» entra debajo, con la etiqueta «Capítulo 12 · Estimación de señales»

---

# Escena 03 — CuantoPasadoHaceFalta

**Capítulo YouTube:** ¿Cuántas muestras hacen falta?

## Narración

<!-- b1 -->
¿Cuántas muestras hacen falta? Sin mirar ninguna, el error es cuatro. Con una muestra, cero coma ocho. Con dos, cero coma siete cuatro cero. Con tres, cero coma siete tres ocho siete. Y con cuatro, cinco, diez, cero coma siete tres ocho seis: deja de bajar. Añadir muestras sirve cada vez menos.

- «¿Cuántas muestras hacen falta?» → `pregunta`: corte seco; aparece la pregunta sobre unos ejes vacíos («error» contra «L, muestras usadas»)
- «Sin mirar ninguna» → `cero`: aparece la primera barra, «0 muestras»
- «el error es cuatro» → `e4`: la barra sube hasta 4 con su rótulo «4»
- «Con una muestra» → `una`: aparece la barra «L = 1»
- «cero coma ocho» → `e08`: la barra baja hasta 0,8 con su rótulo
- «Con dos» → `dos`: aparece la barra «L = 2»
- «cero coma siete cuatro cero» → `e074`: la barra baja hasta 0,740
- «Con tres» → `tres`: aparece la barra «L = 3»
- «cero coma siete tres ocho siete» → `e0738`: la barra queda en 0,7387
- «Y con cuatro, cinco, diez» → `mas`: aparecen de golpe las barras L = 4, 5, 10, casi iguales
- «cero coma siete tres ocho seis» → `limite`: una línea punteada ámbar en 0,7386 recorre las barras
- «deja de bajar» → `plana`: las barras quedan alineadas con la línea, con una flecha plana encima
- «Añadir muestras sirve cada vez menos» → `menos`: las caídas entre barras se marcan con flechas cada vez más cortas

<!-- b2 -->
Dos razones. La primera: añadir una muestra nunca empeora nada, porque el filtro nuevo puede imitar al anterior poniendo a cero el coeficiente extra. La segunda: la temperatura recuerda cero coma seis por paso, así que lo que pasó hace cinco pasos, cero coma seis a la quinta, unos ocho por ciento, casi no dice nada de hoy.

- «Dos razones» → `razones`: se limpian las barras a un lado; aparecen un «1» y un «2» en ámbar
- «La primera» → `primera`: el «1» queda y el «2» se atenúa
- «añadir una muestra nunca empeora nada» → `nuncaempeora`: «error(L + 1) ≤ error(L)» se escribe por piezas, con tilde verde
- «el filtro nuevo puede imitar al anterior» → `imitar`: una fila de casillas h₀ h₁ y una casilla nueva se suma a la derecha
- «poniendo a cero el coeficiente extra» → `cerocoef`: la casilla nueva muestra «0» y las otras no cambian
- «La segunda» → `segunda`: el «2» se enciende y el «1» se atenúa
- «la temperatura recuerda cero coma seis por paso» → `recuerda`: una fila de casillas de tiempo con flechas «× 0,6» entre cada par
- «lo que pasó hace cinco pasos» → `cinco`: se resalta la casilla cinco pasos atrás
- «cero coma seis a la quinta» → `quinta`: se escribe «0,6⁵»
- «unos ocho por ciento» → `ocho`: «≈ 8 %» al lado
- «casi no dice nada de hoy» → `nada`: la casilla lejana se vuelve casi transparente

---

# Escena 04 — LaProgresion

**Capítulo YouTube:** ¿Por qué cero coma uno cinco siete?

## Narración

<!-- b1 -->
Mira ahora los coeficientes: cero coma siete tres ocho seis, cero coma uno uno cinco ocho, cero coma cero uno ocho dos, cero coma cero cero dos ocho. Divide cada uno entre el anterior: cero coma uno cinco siete, cero coma uno cinco siete, cero coma uno cinco siete. Una progresión geométrica perfecta. Y aquí va la sorpresa: ¿por qué cero coma uno cinco siete y no cero coma seis? Piénsalo.

- «Mira ahora los coeficientes» → `coefs`: corte seco; eje con cuatro posiciones h₀ a h₃ vacías
- «cero coma siete tres ocho seis,» → `h0`: sale la barra de h₀ con su rótulo
- «cero coma uno uno cinco ocho» → `h1`: sale la barra de h₁
- «cero coma cero uno ocho dos» → `h2`: sale la barra de h₂, pequeña
- «cero coma cero cero dos ocho» → `h3`: sale la barra de h₃, casi invisible
- «Divide cada uno entre el anterior» → `divide`: tres flechas curvas unen las barras de dos en dos
- «anterior: cero coma uno cinco siete,» → `r1`: sobre la primera flecha, «× 0,157»
- «cero coma uno cinco siete, cero coma uno cinco siete.» → `r2`: sobre la segunda flecha, «× 0,157»
- «siete, cero coma uno cinco siete.» → `r3`: sobre la tercera flecha, «× 0,157»
- «Una progresión geométrica perfecta» → `prog`: una curva exponencial une las puntas de las barras, con la etiqueta «progresión geométrica»
- «la sorpresa» → `sorpresa`: la curva se resalta con un destello
- «¿por qué cero coma uno cinco siete» → `porque`: «0,157» en ámbar a la izquierda con una interrogación
- «y no cero coma seis?» → `noseis`: «0,6» tachado en rojo a la derecha
- «Piénsalo.» → `pausa`: un reloj de arena se vacía

<!-- b2 -->
No lo vamos a contar todavía: lo descubriremos en el episodio cinco, y saldrá de una ecuación de segundo grado. Y el número al que se acerca el error, cero coma siete tres ocho seis, tampoco es casual: es el error del mejor filtro que puede usar todo el pasado. Ese filtro tiene nombre: es el filtro de Wiener causal.

- «No lo vamos a contar todavía» → `candado`: un candado cerrado cubre el «0,157»
- «el episodio cinco» → `ep5`: una etiqueta «episodio 5» sobre el candado
- «una ecuación de segundo grado» → `seg`: aparece la parábola de una ecuación de segundo grado con sus dos raíces marcadas
- «el número al que se acerca el error» → `acerca`: vuelven las barras del error y se resalta la línea en 0,7386
- «tampoco es casual» → `casual`: la línea 0,7386 palpita una vez y aparece un «¡no es casual!»
- «el error del mejor filtro» → `mejor`: junto a la línea, un sello «el mejor filtro»
- «que puede usar todo el pasado» → `pasado`: una flecha larga hacia atrás recorre casillas que se pierden en el infinito
- «Ese filtro tiene nombre» → `nombre`: un cartel vacío se abre junto a la flecha
- «filtro de Wiener causal» → `wiener`: el cartel dice «Wiener causal», con el candado de «episodio 5» al lado

<!-- b3 -->
Regla práctica: aumentar ele hasta que el error deje de bajar o el último coeficiente sea despreciable. Pero hemos estado estimando la temperatura de ahora. Estas mismas ecuaciones sirven para algo todavía más tentador: adivinar lo que todavía no ha ocurrido.

- «Regla práctica» → `regla`: corte seco; sello «regla práctica»
- «aumentar ele» → `aumentar`: «L ↑» con una ventana de casillas que se ensancha
- «el error deje de bajar» → `baja`: una curva de error que se aplana
- «el último coeficiente sea despreciable» → `ultimo`: la última casilla de la ventana se pone casi transparente con un «≈ 0»
- «Pero hemos estado estimando» → `estimando`: aparece una flecha desde la ventana hacia x[n]
- «la temperatura de ahora» → `ahora`: un termómetro y el instante «n» marcado
- «Estas mismas ecuaciones sirven» → `sirven`: la matriz de ecuaciones normales aparece bajo el termómetro
- «más tentador» → `tentador`: el termómetro se acerca a una casilla vacía a la derecha
- «adivinar lo que todavía no ha ocurrido» → `futuro`: una flecha va de la ventana a x[n+1] con una interrogación

---

# Escena 05 — LasEcuacionesDeYuleWalker

**Capítulo YouTube:** Predecir con las ecuaciones de Yule-Walker

## Narración

<!-- b1 -->
Ahora sin ruido. Tenemos el proceso equis y queremos adivinar la muestra que viene, equis de ene más uno, con las ele últimas. Hacemos la misma cuenta: el error tiene que ser perpendicular a cada muestra usada. La única diferencia es lo que estimamos: la correlación de la derecha ya no es la cruzada, sino la autocorrelación de equis a distancia uno, dos, hasta ele.

- «Ahora sin ruido» → `sinruido`: corte seco; el cable ruidoso del sensor pierde su «v» y queda solo la curva
- «el proceso equis» → `proceso`: la curva se rotula «x[n]» en cian
- «la muestra que viene» → `viene`: a la derecha una casilla vacía con una interrogación
- «equis de ene más uno» → `formula`: «x[n+1]» se escribe sobre la casilla vacía
- «con las ele últimas» → `ventana`: una ventana de L casillas se enciende detrás de la casilla vacía
- «la misma cuenta» → `cuenta`: aparece la matriz de las ecuaciones normales del episodio anterior
- «perpendicular a cada muestra usada» → `perp`: flechas con ángulo recto entre el error y cada muestra
- «La única diferencia» → `dif`: el vector de la derecha se resalta
- «la correlación de la derecha» → `derecha`: «c» entra como columna a la derecha de la matriz
- «ya no es la cruzada» → `cruzada`: «C_yx» aparece y se tacha
- «a distancia uno, dos,» → `auto`: la columna se rellena con «C[1], C[2]»
- «hasta ele» → `hastaele`: la columna termina en «…, C[L]»

<!-- b2 -->
Con una muestra, el coeficiente es la autocorrelación en uno entre la autocorrelación en cero, es decir, el coeficiente de correlación: es el predictor del capítulo diez. Con dos muestras, la misma matriz de antes, y a la derecha, la correlación en uno y la correlación en dos. Estas ecuaciones se llaman de Yule-Walker.

- «Con una muestra» → `unamuestra`: la matriz se reduce a una sola casilla, «C[0]»
- «la autocorrelación en uno entre» → `cociente`: se construye «h = C[1] /» por piezas
- «la autocorrelación en cero, es decir» → `cero`: se completa con «C[0]»
- «el coeficiente de correlación» → `rho`: «= ρ» entra en ámbar
- «el predictor del capítulo diez» → `cap10`: un sello «Cap. 10» junto a la fórmula
- «Con dos muestras» → `dos`: la matriz vuelve a crecer a 2 × 2
- «la misma matriz de antes» → `matriz`: la diagonal y las diagonales paralelas se pintan, como en el episodio uno
- «la correlación en uno y la correlación en dos» → `vector`: a la derecha, «C[1]» y «C[2]»
- «Estas ecuaciones se llaman» → `estas`: las dos ecuaciones se enmarcan
- «Yule-Walker» → `yw`: el sello «Yule-Walker» se estampa sobre las ecuaciones

<!-- b3 -->
Aparecen en muchos sitios: para modelar una señal como el resultado de filtrar ruido, lo que se llama un modelo autorregresivo, y en la codificación de la voz, donde cada muestra se predice con las anteriores y solo se guarda lo que falta. Probémoslas con el eco del cero coma seis, sin ruido: autocorrelación cuatro, dos coma cuatro y uno coma cuatro cuatro.

- «Aparecen en muchos sitios» → `sitios`: dos recuadros vacíos se abren a los lados
- «modelar una señal» → `modelar`: en el primero, una caja «filtro» con una moneda a la entrada y una curva a la salida
- «filtrar ruido» → `filtrar`: la moneda entra en la caja y sale la curva
- «un modelo autorregresivo» → `ar`: la etiqueta «modelo autorregresivo» en ámbar
- «la codificación de la voz» → `voz`: en el segundo, un ícono de voz con ondas
- «cada muestra se predice con las anteriores» → `predice`: flechas de las casillas pasadas a la siguiente
- «solo se guarda lo que falta» → `guarda`: queda una barra pequeña, «lo que falta»
- «Probémoslas con el eco del cero coma seis» → `eco`: corte seco; la curva del eco con «× 0,6» entre muestras
- «autocorrelación cuatro» → `c4`: aparece «C[0] = 4»
- «dos coma cuatro» → `c24`: aparece «C[1] = 2,4»
- «uno coma cuatro cuatro» → `c144`: aparece «C[2] = 1,44»

---

# Escena 06 — ElEcoSinRuido

**Capítulo YouTube:** El eco: solo importa la última muestra

## Narración

<!-- b1 -->
Las dos ecuaciones: cuatro hache cero más dos coma cuatro hache uno igual a dos coma cuatro, y dos coma cuatro hache cero más cuatro hache uno igual a uno coma cuatro cuatro. Probamos hache cero igual a cero coma seis y hache uno igual a cero. Primera: dos coma cuatro. Segunda: uno coma cuatro cuatro. Las dos salen. Solo importa la última muestra.

- «Las dos ecuaciones» → `eqs`: corte seco; marco vacío con «las dos ecuaciones»
- «cuatro hache cero más dos coma cuatro hache uno» → `e1a`: se escribe «4 h₀ + 2,4 h₁»
- «igual a dos coma cuatro, y» → `e1b`: «= 2,4»
- «dos coma cuatro hache cero más cuatro hache uno» → `e2a`: debajo, «2,4 h₀ + 4 h₁»
- «igual a uno coma cuatro cuatro» → `e2b`: «= 1,44»
- «Probamos hache cero igual a cero coma seis» → `p0`: «h₀ = 0,6» en ámbar
- «y hache uno igual a cero» → `p1`: «h₁ = 0» en ámbar
- «Primera: dos coma cuatro» → `ok1`: la primera ecuación se rellena con números, «4 · 0,6 + 2,4 · 0 = 2,4», y un tilde verde
- «Segunda: uno coma cuatro cuatro» → `ok2`: «2,4 · 0,6 + 4 · 0 = 1,44» y un tilde verde
- «Las dos salen» → `salen`: los dos tildes se agrandan
- «Solo importa la última muestra» → `ultima`: una barra alta sobre x[n] y otra vacía sobre x[n−1]

<!-- b2 -->
Tiene sentido: el eco es cero coma seis por la salida anterior más una moneda nueva, así que la última muestra ya lo contiene todo. El error es dos coma cinco seis, el mínimo de la parábola del capítulo diez. Pero cuidado con generalizar. Existe un proceso en el que una muestra sin ninguna relación con el futuro tiene un coeficiente distinto de cero. ¿Te atreves a imaginar cuál?

- «el eco es cero coma seis por la salida anterior» → `eco`: «x[n+1] = 0,6 x[n]» se escribe por piezas
- «más una moneda nueva» → `moneda`: «+ w[n+1]» con una moneda ±1
- «la última muestra ya lo contiene todo» → `todo`: x[n] se resalta con un recuadro verde y las anteriores se apagan
- «El error es dos coma cinco seis» → `error`: una barra roja con «error = 2,56»
- «el mínimo de la parábola del capítulo diez» → `parabola`: aparece la parábola del Cap. 10 con su vértice en 2,56
- «Pero cuidado con generalizar» → `cuidado`: un triángulo de advertencia
- «Existe un proceso» → `existe`: se apaga todo y queda una silueta de curva distinta
- «una muestra sin ninguna relación con el futuro» → `sinrel`: «x[n−1]» con «correlación = 0» en rojo
- «un coeficiente distinto de cero» → `distinto`: «h₁ ≠ 0» en ámbar
- «¿Te atreves a imaginar cuál?» → `pregunta`: una interrogación grande y un reloj de arena

---

# Escena 07 — LasTresBarras

**Capítulo YouTube:** Predecir con el proceso de las tres barras

## Narración

<!-- b1 -->
Recordemos el proceso de las tres barras, el de ro igual a cero coma cuatro, que fabricamos en el capítulo once con el filtro de dos coeficientes. Cada muestra se parece solo a sus vecinas inmediatas: correlación uno consigo misma, cero coma cuatro con la de al lado y cero con cualquiera a dos pasos o más.

- «Recordemos el proceso de las tres barras» → `barras`: corte seco; aparecen las tres barras ρ, 1, ρ del Cap. 11 sobre un eje de separación
- «ro igual a cero coma cuatro» → `ro`: «ρ = 0,4» en ámbar
- «el capítulo once» → `cap11`: un sello «Cap. 11» en la esquina
- «el filtro de dos coeficientes» → `filtro`: un bloque pequeño «(2, 1)/√5» con una moneda a la entrada
- «Cada muestra se parece solo a sus vecinas» → `vecinas`: flechas de x[n] a x[n−1] y x[n+1]
- «correlación uno consigo misma» → `uno`: la barra central se resalta, «1»
- «cero coma cuatro con la de al lado» → `cuatro`: las barras laterales se resaltan, «0,4»
- «cero con cualquiera a dos pasos o más» → `cero`: los palitos de más allá quedan en cero, con «0» sobre ellos

<!-- b2 -->
Predecimos equis de ene más uno. Con una sola muestra, equis de ene: el coeficiente es la correlación, cero coma cuatro, y el error, uno menos cero coma cuatro al cuadrado: cero coma ocho cuatro. Y ahora añadimos la anterior, equis de ene menos uno. Pero ojo: entre equis de ene menos uno y equis de ene más uno hay dos pasos, así que su correlación es cero.

- «Predecimos equis de ene más uno» → `pred`: se dibujan tres casillas x[n−1], x[n], x[n+1] con x[n+1] marcada con «?»
- «Con una sola muestra» → `una`: solo x[n] se enciende
- «el coeficiente es la correlación» → `coef`: «h = ρ = 0,4» en ámbar
- «el error, uno menos cero coma cuatro al cuadrado» → `err`: «1 − 0,4²» se construye por piezas
- «cero coma ocho cuatro» → `e084`: «= 0,84» y una barra roja
- «Y ahora añadimos la anterior» → `anade`: x[n−1] se enciende y entra «h₁» sobre ella
- «la anterior, equis de ene menos uno» → `xnm1`: x[n−1] se resalta
- «Pero ojo» → `ojo`: un signo de exclamación ámbar
- «hay dos pasos» → `dospasos`: una llave marca los dos pasos entre x[n−1] y x[n+1]
- «su correlación es cero» → `cero`: un «0» rojo sobre la llave

---

# Escena 08 — LaCuentaDeLaMuestraVieja

**Capítulo YouTube:** La cuenta: un coeficiente que no es cero

## Narración

<!-- b1 -->
Las ecuaciones: hache cero más cero coma cuatro hache uno igual a cero coma cuatro, y cero coma cuatro hache cero más hache uno igual a cero. La segunda dice que hache uno es menos cero coma cuatro hache cero. Lo llevamos a la primera: hache cero por uno menos cero coma dieciséis, igual a cero coma cuatro. Hache cero: cero coma cuatro siete seis.

- «Las ecuaciones» → `eqs`: corte seco; marco con «las ecuaciones»
- «hache cero más cero coma cuatro hache uno» → `ea`: «h₀ + 0,4 h₁»
- «igual a cero coma cuatro, y» → `eb`: «= 0,4»
- «cero coma cuatro hache cero más hache uno» → `ec`: debajo, «0,4 h₀ + h₁»
- «igual a cero. La segunda» → `ed`: «= 0»
- «La segunda dice» → `seg`: la segunda ecuación se resalta
- «hache uno es menos cero coma cuatro hache cero» → `desp`: «h₁ = −0,4 h₀» aparece aparte
- «Lo llevamos a la primera» → `sust`: una flecha lleva «−0,4 h₀» a donde estaba h₁ en la primera ecuación
- «hache cero por uno menos cero coma dieciséis» → `fact`: «h₀ (1 − 0,16)» se agrupa
- «igual a cero coma cuatro. Hache cero» → `igual`: «= 0,4»
- «cero coma cuatro siete seis» → `h0`: «h₀ = 0,476» en ámbar

<!-- b2 -->
Y hache uno, menos cero coma cuatro por cero coma cuatro siete seis: menos cero coma uno nueve. ¡No es cero! La muestra de hace dos pasos, que no tiene ninguna correlación con la que queremos adivinar, recibe un coeficiente, y negativo. Y se nota en el error: uno menos cero coma cuatro siete seis por cero coma cuatro, cero coma ocho uno. Baja.

- «Y hache uno, menos cero coma cuatro por» → `h1c`: «h₁ = −0,4 · 0,476»
- «cero coma cuatro siete seis:» → `x476`: «· 0,476» se suma a la cuenta
- «menos cero coma uno nueve» → `h1`: «= −0,19» en ámbar
- «¡No es cero!» → `nocero`: el «−0,19» destella y una cruz roja tacha un «0» fantasma
- «La muestra de hace dos pasos» → `vieja`: aparecen x[n−1] y x[n+1] con la llave de dos pasos
- «ninguna correlación con la que queremos adivinar» → `sincorr`: «correlación = 0» en rojo junto a la llave
- «recibe un coeficiente, y negativo» → `neg`: una barra negativa en rojo bajo x[n−1] y una positiva sobre x[n]
- «Y se nota en el error» → `nota`: se arma «error =»
- «uno menos cero coma cuatro siete seis por cero coma cuatro» → `cuenta`: «1 − 0,476 · 0,4»
- «cero coma ocho uno. Baja» → `e081`: «= 0,810»
- «Baja.» → `baja`: una flecha hacia abajo desde 0,84 hasta 0,810

---

# Escena 09 — AbrirLasMuestras

**Capítulo YouTube:** Qué monedas contiene cada muestra

## Narración

<!-- b1 -->
Piénsalo un momento: ¿cómo puede servir un dato que no se parece en nada a lo que buscas? No es un truco de las cuentas ni un error. Hay una explicación sencilla, y para verla hay que abrir las muestras y mirar qué monedas contiene cada una.

- «Piénsalo un momento» → `pausa`: corte seco; un reloj de arena se vacía
- «¿cómo puede servir un dato» → `servir`: la casilla x[n−1] con «¿sirve?»
- «que no se parece en nada» → `nada`: «correlación = 0» a su lado
- «No es un truco de las cuentas ni un error» → `truco`: la ecuación «h₁ = −0,19» con un tilde verde
- «Hay una explicación sencilla» → `explic`: una bombilla sobre la casilla
- «abrir las muestras» → `abrir`: la casilla x[n−1] se abre en dos mitades
- «qué monedas contiene cada una» → `monedas`: dentro aparecen monedas ±1 pequeñas

<!-- b2 -->
Abramos las muestras. El proceso sale de una moneda, w, pasada por el filtro de dos coeficientes: equis de ene es dos veces la moneda de ahora más la anterior, entre raíz de cinco. Entonces, equis de ene más uno contiene la moneda nueva, w de ene más uno, imposible de saber, y también la moneda w de ene, que sí ocurrió ya.

- «Abramos las muestras» → `abramos`: una fila de monedas w[n−2], w[n−1], w[n], w[n+1]
- «El proceso sale de una moneda, w» → `sale`: las monedas se rotulan «w» en magenta
- «pasada por el filtro de dos coeficientes» → `filtro`: el bloque «(2, 1)/√5» aparece debajo de la fila
- «equis de ene es dos veces la moneda de ahora» → `xn`: «x[n] = (2 w[n]» se escribe
- «más la anterior,» → `anterior`: «+ w[n−1])» se suma
- «entre raíz de cinco» → `raiz`: «/ √5» cierra la expresión
- «equis de ene más uno contiene» → `futuro`: se escribe «x[n+1] = (2 w[n+1] + w[n]) / √5» debajo
- «la moneda nueva, w de ene más uno» → `nueva`: w[n+1] se pinta en rojo
- «imposible de saber» → `imposible`: sobre w[n+1], el rótulo «imposible de saber»
- «y también la moneda w de ene» → `wn`: w[n] se pinta en verde
- «que sí ocurrió ya» → `ya`: junto a w[n] el rótulo «ya ocurrió»

<!-- b3 -->
Y equis de ene, la muestra de ahora, contiene esa misma moneda, w de ene, con más fuerza. Pero no la trae limpia: viene mezclada con la moneda anterior, w de ene menos uno. Para predecir equis de ene más uno, esa moneda anterior es basura: ensucia la única pista que tenemos.

- «Y equis de ene, la muestra de ahora» → `ahora`: debajo se escribe «x[n] = (2 w[n] + w[n−1]) / √5»
- «esa misma moneda, w de ene,» → `fuerza`: w[n] en verde
- «con más fuerza» → `masfuerza`: el coeficiente 2 se destaca
- «Pero no la trae limpia» → `limpia`: un velo gris cubre parte de la expresión
- «viene mezclada con la moneda anterior» → `mezclada`: w[n−1] se pinta en magenta
- «w de ene menos uno» → `wnm1`: w[n−1] resaltada en la fila de monedas
- «Para predecir equis de ene más uno» → `predecir`: se señala x[n+1] con «?»
- «esa moneda anterior es basura» → `basura`: una papelera junto a w[n−1] en x[n]
- «ensucia la única pista que tenemos» → `ensucia`: la pista x[n] con una mancha magenta

---

# Escena 10 — LaPistaLimpia

**Capítulo YouTube:** No correlacionado no significa inútil

## Narración

<!-- b1 -->
Ahora mira la muestra de hace dos pasos, equis de ene menos uno. Contiene justo esa moneda anterior, w de ene menos uno, y otra más antigua. No tiene ninguna moneda en común con equis de ene más uno, y por eso la correlación es cero. Pero nos dice cuánta basura lleva equis de ene. Restándola, limpiamos la pista. De ahí el coeficiente negativo.

- «Ahora mira la muestra de hace dos pasos» → `mira`: x[n−1] se enciende con su expresión «(2 w[n−1] + w[n−2]) / √5»
- «equis de ene menos uno. Contiene» → `xnm1`: x[n−1] se resalta
- «Contiene justo esa moneda anterior» → `contiene`: w[n−1] se enlaza con la misma moneda de x[n]
- «y otra más antigua» → `antigua`: w[n−2] aparece en gris
- «No tiene ninguna moneda en común» → `comun`: no hay líneas entre x[n−1] y x[n+1]; las dos expresiones no comparten color
- «por eso la correlación es cero» → `cero`: «correlación = 0» en rojo
- «cuánta basura lleva equis de ene» → `cuanta`: una línea desde x[n−1] a la mancha magenta de x[n]
- «Restándola, limpiamos la pista» → `resta`: «x[n] − 0,4 x[n−1]» se escribe y la mancha desaparece
- «De ahí el coeficiente negativo» → `neg`: el «−» del coeficiente se resalta en rojo

<!-- b2 -->
Es lo que pasa en la regresión: una variable de control no se parece al objetivo, pero ayuda a quitar lo que ensucia a otra variable. Lo que decide un coeficiente no es la correlación de esa muestra con el objetivo, sino el resultado de resolver todo el sistema: la inversa de la matriz mezcla los datos entre sí. No correlacionado no significa inútil.

- «la regresión» → `regresion`: corte seco; el sello «Cap. 8 · regresión»
- «una variable de control» → `control`: una flecha «control» apunta a una nube de puntos
- «ayuda a quitar lo que ensucia a otra variable» → `quitar`: la nube se alinea al restar el control
- «Lo que decide un coeficiente» → `decide`: se escribe «h = »
- «no es la correlación de esa muestra con el objetivo» → `nocorr`: «c = (0,4 ; 0)» con el «0» tachado y «no manda solo»
- «el resultado de resolver todo el sistema» → `sistema`: la matriz aparece junto a «c»
- «la inversa de la matriz» → `inversa`: «C⁻¹ c» completa «h = C⁻¹ c»
- «No correlacionado no significa inútil» → `inutil`: sello en ámbar con la frase y un tilde verde

<!-- b3 -->
Resumamos. Hasta aquí, una ventana finita hacia atrás, y sabemos calcular sus coeficientes y su error. Pero si la grabación ya está hecha, no hay razón para mirar solo el pasado: podemos usar todo el registro. Entonces el sistema de ecuaciones se hace infinito, y ocurre algo que parece magia: se resuelve con una división.

- «Resumamos» → `resumen`: corte seco; el mapa del episodio con las casillas de ventana
- «una ventana finita hacia atrás» → `ventana`: una ventana de L casillas, solo hacia la izquierda
- «sabemos calcular sus coeficientes y su error» → `sabemos`: «h» y «error» con tilde verde
- «si la grabación ya está hecha» → `grabacion`: una tira de grabación completa a ambos lados
- «no hay razón para mirar solo el pasado» → `pasado`: la mitad derecha de la grabación se enciende
- «todo el registro» → `registro`: la ventana se ensancha hasta cubrir toda la tira
- «Entonces el sistema de ecuaciones» → `entonces`: la matriz de ecuaciones normales
- «se hace infinito» → `infinito`: la matriz crece con puntos suspensivos y «∞»
- «parece magia» → `magia`: destellos sobre la matriz
- «se resuelve con una división» → `division`: la matriz se reemplaza por «H = S_yx / S_xx»

---

# Escena 11 — Cierre

**Capítulo YouTube:** Próximo episodio: mirar el registro entero

## Narración

<!-- b1 -->
Nos llevamos dos ideas. Más pasado baja el error cada vez menos, hasta quedarse en cero coma siete tres ocho seis. Y una muestra que no se parece en nada a lo que buscas puede servir, si ayuda a limpiar otra. En el próximo episodio: Mirar el registro entero. Allí veremos esa división.

- «Nos llevamos dos ideas» → `dos`: corte seco; aparecen un «1» y un «2» en ámbar
- «Más pasado baja el error cada vez menos» → `menos`: junto al «1», las barras del error que se aplanan
- «cero coma siete tres ocho seis» → `limite`: la línea punteada en 0,7386
- «una muestra que no se parece en nada» → `nada`: junto al «2», la casilla x[n−1] con «correlación = 0»
- «si ayuda a limpiar otra» → `limpiar`: una flecha desde x[n−1] a x[n], con la mancha desapareciendo
- «En el próximo episodio» → `proximo`: todo se apaga; aparece «Episodio 3»
- «Mirar el registro entero» → `titulo`: el título entra con rebote, con la tira de grabación completa debajo
- «esa división» → `division`: «H = S_yx / S_xx» entra bajo el título
