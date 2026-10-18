# Episodio 5 — Dos variables a la vez

Capítulo 7 (Modelos probabilísticos), episodio 5 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 17 a 20), más un gancho y un cierre nuevos.
Ejemplos que vuelven con el mismo dibujo: el canal que confunde bits (0,7 / 0,3 y 10 % de error, como en la escena 08 del E2) y la altura (40 % hombres de 175 cm, 60 % mujeres de 162 cm).

**Estado:** **Subido a YouTube en privado** el 17/10/2026: render final 1080p60 de 9:01, con título, descripción con `capitulos.txt`, subtítulos `.srt`, categoría Educación y «no es para niños» (https://youtu.be/yOGhkgYWskI). Lo subió el usuario sin el visto bueno que figuraba pendiente en este estado (texto ⭐ / mp4 / pronunciaciones): la aprobación queda en su revisión antes de publicarlo. Residuos limpiados el 17/10/2026; se rehace con `python rehacer.py Capitulo07_Probabilidad`. La caché de voz versionada (`media/voiceovers/`) se volvió a sintetizar después de la subida: un render nuevo es reproducible, pero la voz puede diferir un poco de la del vídeo subido. **Falta**: publicarlo (lo hace el usuario).

Texto nuevo (marcado con ⭐; aprobado por el usuario):
- ⭐ Escena 01 (gancho): «Se recibe un uno. ¿Qué se envió? Una tabla de cuatro números lo responde…».
- ⭐ Escena 14 (cierre): resume el episodio, plantea la pregunta de «un solo número» y anuncia E6, «Lo que una variable sabe de otra».
- ⭐ Retoque en la escena 03 (bloque b1): se suma una frase que recuerda el canal (0,7 / 0,3 y una de cada diez veces), porque la escena 08 queda tres episodios atrás.

---

# Escena 01 — Gancho

**Capítulo YouTube:** Dos variables a la vez

## Narración

<!-- b1 -->
Se recibe un uno. ¿Qué se envió? Una tabla de cuatro números lo responde. Y la misma idea parte la varianza de las alturas en dos mitades casi iguales.

- «Se recibe un uno» → `recibe`: un canal con el bit «1» cian saliendo por la derecha
- «¿Qué se envió?» → `pregunta`: aparece una interrogación azul a la entrada
- «Una tabla de cuatro números» → `tabla`: se dibuja una tabla 2 × 2 con cuatro casillas
- «lo responde» → `responde`: una casilla se ilumina y sale «0,79»
- «la varianza de las alturas» → `alturas`: dos campanas de altura, hombres y mujeres
- «dos mitades casi iguales» → `mitades`: una barra se parte en «41,2» y «40,56»

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Dos variables a la vez

## Narración

<!-- b1 -->
Dos variables a la vez.

- «Dos variables» → `t1`: «Dos variables» entra con rebote
- «a la vez» → `t2`: «a la vez» entra debajo, con la etiqueta «Capítulo 7 · Modelos probabilísticos»

---

# Escena 03 — TablaConjunta

**Capítulo YouTube:** La tabla conjunta

## Narración

<!-- b1 -->
Volvamos al canal que confunde bits: se envía un cero con probabilidad cero coma siete, un uno con cero coma tres, y el canal cambia el bit una de cada diez veces. Llamemos ese a lo que se envió, y erre a lo que se recibió. Ahora nos interesan las dos variables a la vez: qué pareja sale cada vez. Hay cuatro parejas posibles, y podemos poner sus probabilidades en una tabla: filas para lo enviado, columnas para lo recibido.

- «Volvamos al canal» → `canal`: el canal de la escena 08 (entrada, caja, salida), mismo dibujo
- «que confunde bits» → `confunde`: la caja del canal se resalta en rojo
- «se envía un cero» → `envia`: un «0» azul recorre la flecha de entrada hasta la caja
- «cero coma siete» → `p0`: sobre la entrada, «0 · 0,7»
- «un uno con cero coma tres» → `p1`: sobre la entrada, «1 · 0,3»
- «una de cada diez veces» → `error`: la caja del canal con «10 %» en rojo y una flecha cruzada
- «ese a lo que se envió» → `s`: «S» azul sobre la entrada
- «erre a lo que se recibió» → `r`: «R» cian sobre la salida
- «las dos variables a la vez» → `dos`: S y R se juntan en un par «(S, R)»
- «qué pareja sale cada vez» → `cada`: el par «(S, R)» se agranda
- «cuatro parejas posibles» → `parejas`: las parejas (0, 0), (0, 1), (1, 0), (1, 1) en fila
- «sus probabilidades» → `probs`: las cuatro parejas crecen un instante, en ámbar
- «una tabla» → `tabla`: el canal se encoge a un lado y aparece una rejilla 2 × 2 vacía
- «filas para lo enviado» → `filas`: rótulos «S = 0» y «S = 1» a la izquierda
- «columnas para lo recibido» → `columnas`: rótulos «R = 0» y «R = 1» arriba

<!-- b2 -->
Cada casilla se calcula con la regla del producto. Enviar un cero y recibir un cero: cero coma siete por cero coma nueve, cero coma sesenta y tres. Enviar un cero y recibir un uno: cero coma siete por cero coma uno, cero coma cero siete. Enviar un uno y recibir un cero: cero coma cero tres. Y enviar un uno y recibir un uno: cero coma veintisiete. Las cuatro juntas suman uno.

- «la regla del producto» → `regla`: «P(A y B) = P(A) · P(B | A)» se escribe por piezas junto a la tabla
- «Enviar un cero y recibir un cero» → `c00`: se ilumina la casilla (0, 0)
- «cero coma siete por cero coma nueve» → `cuenta00`: «0,7 · 0,9» sale de la casilla
- «cero coma sesenta y tres» → `r00`: la casilla queda con «0,63»
- «Enviar un cero y recibir un uno» → `c01`: se ilumina la casilla (0, 1)
- «cero coma siete por cero coma uno» → `cuenta01`: «0,7 · 0,1» sale de la casilla
- «cero coma cero siete» → `r01`: la casilla queda con «0,07»
- «Enviar un uno y recibir un cero» → `c10`: se ilumina la casilla (1, 0)
- «cero coma cero tres» → `r10`: «0,3 · 0,1 = 0,03» y la casilla queda con «0,03»
- «Y enviar un uno y recibir un uno» → `c11`: se ilumina la casilla (1, 1)
- «cero coma veintisiete» → `r11`: «0,3 · 0,9 = 0,27» y la casilla queda con «0,27»
- «suman uno» → `suman`: las cuatro casillas se suman: «0,63 + 0,07 + 0,03 + 0,27 = 1»

---

# Escena 04 — Marginales

**Capítulo YouTube:** Marginales: sumar filas y columnas

## Narración

<!-- b1 -->
Esta tabla se llama distribución conjunta, y contiene todo. Por ejemplo, si solo te importa lo que se envió, suma cada fila: cero coma siete y cero coma tres, las probabilidades de partida. Si solo te importa lo recibido, suma cada columna: cero coma sesenta y seis y cero coma treinta y cuatro. A estas sumas, que se escriben en los márgenes de la tabla, se les llama marginales.

- «distribución conjunta» → `conjunta`: «distribución conjunta» entra con rebote sobre la tabla
- «contiene todo» → `todo`: un marco ámbar rodea las cuatro casillas
- «lo que se envió» → `envio`: «S = 0» y «S = 1» se agrandan
- «suma cada fila» → `filas`: una llave a la derecha de cada fila
- «cero coma siete y cero coma tres» → `m_s`: a la derecha, «0,63 + 0,07 = 0,7» y «0,03 + 0,27 = 0,3»
- «probabilidades de partida» → `partida`: «0,7» y «0,3» se unen con los de la entrada del canal
- «lo recibido» → `recibido`: «R = 0» y «R = 1» se agrandan
- «suma cada columna» → `columnas`: una llave debajo de cada columna
- «cero coma sesenta y seis y cero coma treinta y cuatro» → `m_r`: abajo, «0,63 + 0,03 = 0,66» y «0,07 + 0,27 = 0,34»
- «A estas sumas» → `sumas`: las cuatro sumas de los márgenes se agrandan a la vez
- «los márgenes de la tabla» → `margenes`: los dos grupos de sumas se marcan en los bordes de la tabla
- «marginales» → `marginales`: «marginales» entra con rebote

---

# Escena 05 — LeerCondicional

**Capítulo YouTube:** Leer una condicional en la tabla

## Narración

<!-- b1 -->
Y también salen las condicionales. Si sabes que se recibió un uno, te quedas solo con esa columna: el mundo se achica, como con el dado. Dentro de la columna, el uno enviado pesa cero coma veintisiete de un total de cero coma treinta y cuatro: cero coma setenta y nueve. Es el mismo número que nos dio Bayes, ahora leído directamente de la tabla.

- «las condicionales» → `condicionales`: «condicionales» entra con rebote
- «se recibió un uno» → `uno`: se ilumina la columna «R = 1»
- «solo con esa columna» → `columna`: las demás columnas se atenúan
- «el mundo se achica» → `achica`: el rectángulo del dado de la escena 05 se encoge a la columna, como entonces
- «como con el dado» → `dado`: entra una cara de dado a la derecha
- «el uno enviado pesa» → `pesa`: se marca la casilla de abajo, «0,27»
- «cero coma veintisiete de un total de» → `total`: «0,27» sobre «0,34»
- «cero coma treinta y cuatro» → `t34`: el denominador de la fracción se agranda
- «cero coma setenta y nueve» → `r79`: «0,27 / 0,34 ≈ 0,79» en verde
- «el mismo número que nos dio Bayes» → `bayes`: el resultado se une con el «0,79» de la escena 08
- «leído directamente de la tabla» → `leido`: el marco verde de la casilla crece y vuelve

<!-- b2 -->
Un detalle importante: de la tabla conjunta siempre puedes sacar las marginales, sumando. Pero al revés, no: sabiendo solo cuánto se envía y cuánto se recibe, no sabes cómo se relacionan. Esa relación es justamente lo que nos interesa. Y cuando las variables son continuas, la tabla se convierte en otra cosa.

- «siempre puedes sacar las marginales» → `sacar`: una flecha de la tabla a las dos marginales
- «Pero al revés, no» → `alreves`: la flecha vuelve tachada con una cruz roja
- «cuánto se envía y cuánto se recibe» → `solo_m`: se dibujan solo los márgenes, con la tabla vacía y una interrogación
- «cómo se relacionan» → `relacionan`: las casillas vacías pasan a «?»
- «lo que nos interesa» → `interesa`: se resalta la tabla completa en ámbar
- «las variables son continuas» → `continuas`: la tabla se difumina y aparecen puntos sueltos
- «se convierte en otra cosa» → `otra`: los puntos se encienden en ámbar uno tras otro

---

# Escena 06 — NubeDePuntos

**Capítulo YouTube:** De la tabla a la nube

## Narración

<!-- b1 -->
Ahora lo que se envía no es un bit, sino una tensión cualquiera, equis. Y lo que se recibe, i griega, es esa tensión más un ruido. Cada envío da una pareja de números, que es un punto en el plano. Repitiendo muchas veces, aparece una nube alargada, la cual indica que cuando se envía más, suele recibirse más, pero con dispersión.

- «una tensión cualquiera» → `x`: «X» azul sobre una recta con una tensión que se envía
- «Y lo que se recibe» → `recibe`: la recta de Y se agranda
- «i griega» → `y`: «Y» cian sobre la salida del canal
- «más un ruido» → `ruido`: «Y = X + ruido», con el ruido en magenta
- «una pareja de números» → `pareja`: aparecen los dos números en pantalla, «(x, y)»
- «un punto en el plano» → `punto`: el par se convierte en un punto en un plano con ejes
- «Repitiendo muchas veces» → `repite`: caen puntos uno tras otro, con semilla fija
- «una nube alargada» → `nube`: la nube se alarga en diagonal
- «suele recibirse más» → `mas`: una flecha diagonal sube con la nube
- «con dispersión» → `dispersion`: se marcan puntos que se separan de la diagonal

<!-- b2 -->
Ya no hay cuatro casillas: hay infinitas parejas posibles. Imagina la tabla cada vez más fina, con casillas más y más pequeñas. En el límite, en lugar de números en casillas, tenemos una superficie sobre el plano, como una colina. Es alta donde caen muchos puntos y baja donde caen pocos. Se llama densidad conjunta, efe sub equis i griega.

- «infinitas parejas posibles» → `infinitas`: la tabla de cuatro casillas se superpone a la nube
- «cada vez más fina» → `fina`: la cuadrícula se refina varias veces
- «casillas más y más pequeñas» → `pequenas`: las casillas se vuelven columnas de altura variable
- «En el límite» → `limite`: entra «en el límite» arriba a la izquierda
- «una superficie sobre el plano» → `superficie`: las columnas se funden en una superficie
- «como una colina» → `colina`: la colina se gira y se ve en perspectiva
- «alta donde caen muchos puntos» → `alta`: se resalta la cima, sobre el centro de la nube
- «baja donde caen pocos» → `baja`: se resaltan los bordes, bajos
- «densidad conjunta» → `densidad`: «densidad conjunta» entra con rebote
- «efe sub equis i griega» → `f_xy`: aparece «f_{XY}(x, y)» por piezas

---

# Escena 07 — ColinaYVolumen

**Capítulo YouTube:** Probabilidad como volumen

## Narración

<!-- b1 -->
Con una variable, la probabilidad era un área bajo una curva. Ahora es un volumen bajo la colina: la probabilidad de que la pareja caiga en una región del plano es el volumen de colina que hay encima de esa región. Se calcula con una integral doble, que es sumar a lo largo de los dos ejes. Y el volumen total vuelve a valer uno.

- «un área bajo una curva» → `area`: el dibujo de la escena 11: curva con el área sombreada
- «un volumen bajo la colina» → `volumen`: la curva se transforma en la colina; aparece su volumen
- «la probabilidad de que la pareja caiga» → `cae`: una gota ámbar cae sobre el plano y se apaga
- «una región del plano» → `region`: un rectángulo sombreado en el plano, bajo la colina
- «el volumen de colina» → `bloque`: sobre la región, una columna de colina se rellena de ámbar
- «una integral doble» → `integral`: «P((X, Y) ∈ R) = ∬ f_{XY}(x, y) dx dy» se escribe por piezas
- «sumar a lo largo de los dos ejes» → `ejes`: dos flechas, una por cada eje, recorren la región
- «el volumen total» → `total`: toda la colina se rellena
- «vuelve a valer uno» → `uno`: «= 1» sobre la fórmula

---

# Escena 08 — AplastarLaColina

**Capítulo YouTube:** Marginales de la colina y centro de masa

## Narración

<!-- b1 -->
Las marginales se sacan igual que en la tabla. Allí sumábamos cada fila; aquí, para cada valor de equis, sumamos toda la colina a lo largo de i griega, es decir, integramos. Es como aplastar la colina contra el eje de las equis: lo que queda es la densidad de equis sola. Y aplastando contra el otro eje, la de i griega.

- «Las marginales» → `marginales`: «marginales» entra con rebote
- «sumábamos cada fila» → `filas`: un destello de la tabla de la escena 04, con sus llaves
- «para cada valor de equis» → `cada_x`: una rebanada vertical de la colina, en un valor de «x»
- «a lo largo de i griega» → `a_lo_largo`: la rebanada se recorre con una flecha vertical
- «integramos» → `integramos`: «f_X(x) = ∫ f_{XY}(x, y) dy» por piezas
- «aplastar la colina» → `aplastar`: la colina se aplasta contra el eje horizontal
- «la densidad de equis sola» → `fx`: aparece la curva de «f_X» sobre el eje, en azul
- «contra el otro eje» → `fy`: la colina se aplasta contra el eje vertical y sale «f_Y», en cian

<!-- b2 -->
La nube también tiene su punto de equilibrio: el centro de masa, con la media de equis en un eje y la media de i griega en el otro. Pero lo más interesante no es el centro: es qué pasa dentro de la nube cuando ya sabes cuánto vale una de las dos variables.

- «punto de equilibrio» → `equilibrio`: la nube sobre un filo, como la placa de la escena 13
- «el centro de masa» → `centro`: un punto ámbar en el centro de la nube
- «la media de equis en un eje» → `mx`: una línea vertical al eje horizontal con «E[X]»
- «la media de i griega en el otro» → `my`: una línea horizontal al eje vertical con «E[Y]»
- «lo más interesante» → `interesante`: el centro se atenúa y aparece un signo de interrogación sobre la nube
- «cuando ya sabes cuánto vale» → `sabes`: una línea vertical fija un valor de «x» sobre la nube

---

# Escena 09 — EsperanzaCondicional

**Capítulo YouTube:** Esperanza condicional

## Narración

<!-- b1 -->
En la tabla del canal, fíjate solo en la columna de recibir un uno. Dentro de esa columna, lo enviado vale uno con probabilidad cero coma setenta y nueve. Así que, sabiendo que se recibió un uno, la media de lo enviado es cero coma setenta y nueve. Es la esperanza condicional: la media de una variable dentro del mundo achicado por lo que sabemos.

- «En la tabla del canal» → `tabla`: vuelve la tabla 2 × 2 con las cuatro casillas
- «la columna de recibir un uno» → `columna`: se ilumina la columna «R = 1» y las demás se atenúan
- «Dentro de esa columna» → `dentro`: el marco ámbar de la columna crece y vuelve
- «vale uno con probabilidad» → `vale`: dentro de la columna, el uno enviado con «0,79» y el cero con «0,21»
- «cero coma setenta y nueve» → `p79`: entra «S = 0: 0,21» debajo del 0,79
- «sabiendo que se recibió un uno» → `sabiendo`: «R = 1» y el 0,79 se agrandan
- «la media de lo enviado» → `cuenta`: «0 · 0,21 + 1 · 0,79 = 0,79»
- «es cero coma setenta y nueve» → `igual`: la cuenta se agranda
- «esperanza condicional» → `esperanza`: «E[S | R = 1] = 0,79» se escribe por piezas
- «mundo achicado» → `achicado`: la columna crece hasta ocupar el centro, como el rectángulo del dado

<!-- b2 -->
Si se recibió un cero, la columna es otra, y la media de lo enviado es mucho más pequeña: cero coma cero cuatro cinco. Dos respuestas distintas, según lo que se reciba. Y como lo que se recibe es aleatorio, la esperanza condicional es, a su vez, una variable aleatoria: un número que depende de lo que salga.

- «Si se recibió un cero» → `cero`: se ilumina la columna «R = 0»
- «la columna es otra» → `otra`: se cambia a la columna R = 0 (marco ámbar)
- «mucho más pequeña» → `pequena`: «0,03 / 0,66» se escribe sobre la columna
- «cero coma cero cuatro cinco» → `r045`: «E[S | R = 0] ≈ 0,045»
- «Dos respuestas distintas» → `dos`: las dos esperanzas, 0,79 y 0,045, una al lado de otra
- «según lo que se reciba» → `segun`: entra la moneda de R
- «es aleatorio» → `aleatorio`: una moneda sobre «R» gira entre 0 y 1
- «una variable aleatoria» → `variable`: «E[S | R]» entra con rebote, con una flecha «depende de R»
- «depende de lo que salga» → `depende`: entra «depende de R» y la moneda gira otra vez

---

# Escena 10 — LaTorre

**Capítulo YouTube:** La propiedad de la torre

## Narración

<!-- b1 -->
Ahora hagamos el promedio de esos promedios, cada uno pesado por lo probable que es su columna. Cero coma treinta y cuatro por cero coma setenta y nueve, más cero coma sesenta y seis por cero coma cero cuatro cinco. Da cero coma tres. ¡Es exactamente la media de lo enviado! Promediar por grupos y después promediar los grupos da lo mismo que promediar todo de golpe. Se llama propiedad de la torre.

- «el promedio de esos promedios» → `promedio`: los dos números «0,79» y «0,045» se juntan en una balanza
- «lo probable que es su columna» → `pesos`: las dos marginales «0,34» y «0,66» aparecen como pesas
- «Cero coma treinta y cuatro por cero coma setenta y nueve» → `cuenta1`: «0,34 · 0,79 ≈ 0,27»
- «más cero coma sesenta y seis» → `cuenta2`: «+ 0,66 · 0,045 ≈ 0,03»
- «cero coma cero cuatro cinco» → `c045`: la media «R = 0: 0,045» se agranda
- «Da cero coma tres» → `da`: «= 0,3» en ámbar
- «la media de lo enviado» → `media`: «E[S] = 0 · 0,7 + 1 · 0,3 = 0,3» y los dos resultados se unen con un «=»
- «Promediar por grupos» → `grupos`: dos cajas de grupos se promedian por separado
- «y después promediar los grupos» → `despues`: las dos sumas se agrandan
- «da lo mismo» → `lo_mismo`: los dos «0,3» se agrandan a la vez
- «propiedad de la torre» → `torre`: «E[S] = E[ E[S | R] ]» se escribe por piezas

<!-- b2 -->
Con la nube pasa lo mismo, en continuo. Corta la nube en rebanadas finas, una para cada valor de equis, y marca el centro de cada rebanada. Esos centros forman una curva: la esperanza de i griega dado equis. Es, rebanada a rebanada, lo que cabe esperar de lo recibido sabiendo lo que se envió.

- «en continuo» → `continuo`: vuelve la nube de puntos de la escena 06
- «rebanadas finas» → `rebanadas`: la nube se corta en rebanadas verticales finas
- «una para cada valor de equis» → `cada_x`: una rebanada se resalta con su valor «x»
- «el centro de cada rebanada» → `centros`: un punto ámbar en el centro de cada rebanada
- «forman una curva» → `curva`: los puntos se unen en una curva
- «la esperanza de i griega dado equis» → `g_x`: «g(x) = E[Y | X = x]» se escribe por piezas
- «rebanada a rebanada» → `reb`: los puntos ámbar se agrandan de izquierda a derecha
- «lo que cabe esperar» → `cabe`: un cursor recorre la curva con la lectura «Y esperada»

<!-- b3 -->
Un ejemplo cotidiano de la torre. En una población, el cuarenta por ciento son hombres, con una altura media de ciento setenta y cinco centímetros, y el sesenta por ciento son mujeres, con ciento sesenta y dos. La altura media de todos es cero coma cuatro por ciento setenta y cinco más cero coma seis por ciento sesenta y dos: ciento sesenta y siete coma dos. Y con la varianza pasa algo todavía más bonito.

- «Un ejemplo cotidiano» → `ejemplo`: corte; entra «la torre» en ámbar
- «el cuarenta por ciento son hombres» → `hombres`: una campana azul de hombres, con «40 %»
- «ciento setenta y cinco centímetros» → `h175`: la media de la campana marcada en «175 cm»
- «el sesenta por ciento son mujeres» → `mujeres`: una campana magenta de mujeres, con «60 %»
- «ciento sesenta y dos» → `m162`: la media de la campana marcada en «162 cm»
- «La altura media de todos» → `todos`: una línea ámbar entre las dos medias
- «cero coma cuatro por ciento setenta y cinco» → `cuenta1`: «0,4 · 175 = 70»
- «cero coma seis por ciento sesenta y dos» → `cuenta2`: «+ 0,6 · 162 = 97,2»
- «ciento sesenta y siete coma dos» → `r1672`: «= 167,2» sobre la línea ámbar
- «con la varianza» → `varianza`: aparece el rótulo «varianza» con una interrogación

---

# Escena 11 — VarianzaDentro

**Capítulo YouTube:** Varianza dentro de cada grupo

## Narración

<!-- b1 -->
Las alturas varían por dos motivos distintos. Uno: dentro de cada grupo hay gente más alta y más baja. Digamos que la desviación típica es de siete centímetros en los hombres y de seis en las mujeres. Dos: los grupos tienen medias distintas, ciento setenta y cinco y ciento sesenta y dos. ¿Cuánto aporta cada motivo a la varianza total?

- «dos motivos distintos» → `motivos`: aparecen dos casillas vacías, «motivo 1» y «motivo 2»
- «dentro de cada grupo» → `dentro`: sobre las campanas, una flecha doble dentro de cada una
- «gente más alta y más baja» → `alta_baja`: una persona alta y otra baja dentro del grupo de hombres
- «Digamos que la desviación típica» → `desv`: las dos flechas dobles se agrandan
- «siete centímetros en los hombres» → `s7`: «σ_H = 7 cm» sobre la campana azul
- «seis en las mujeres» → `s6`: «σ_M = 6 cm» sobre la campana magenta
- «los grupos tienen medias distintas» → `medias`: dos puntos en las medias, 175 y 162, con una flecha entre ellos
- «ciento setenta y cinco» → `h175`: el punto de los hombres se agranda
- «ciento sesenta y dos» → `m162`: el punto de las mujeres se agranda
- «¿Cuánto aporta cada motivo» → `aporta`: las dos casillas de motivos se agrandan
- «la varianza total» → `total`: una barra vacía, «varianza total»

<!-- b2 -->
El primer trozo es la varianza dentro de cada grupo, promediada con los pesos de los grupos. Cero coma cuatro por siete al cuadrado, diecinueve coma seis. Más cero coma seis por seis al cuadrado, veintiuno coma seis. En total, cuarenta y uno coma dos.

- «El primer trozo» → `trozo1`: la primera casilla se llena, con el rótulo «dentro de cada grupo»
- «dentro de cada grupo» → `dcg`: la barra roja se agranda
- «los pesos de los grupos» → `pesos`: «0,4» y «0,6» sobre las dos campanas
- «Cero coma cuatro por siete al cuadrado» → `cuenta1`: «0,4 · 7²»
- «diecinueve coma seis» → `r196`: «= 19,6»
- «Más cero coma seis por seis al cuadrado» → `cuenta2`: «+ 0,6 · 6²»
- «veintiuno coma seis» → `r216`: «= 21,6»
- «cuarenta y uno coma dos» → `suma1`: «= 41,2» en ámbar y una barra de ese tamaño

---

# Escena 12 — VarianzaEntre

**Capítulo YouTube:** Varianza entre los grupos

## Narración

<!-- b1 -->
El segundo trozo es cuánto se dispersan las medias de los grupos alrededor de la media total. La media de los hombres está a siete coma ocho centímetros de ciento sesenta y siete coma dos, y la de las mujeres, a cinco coma dos. Al cuadrado y con sus pesos: veinticuatro coma treinta y cuatro más dieciséis coma veintidós. Cuarenta coma cinco seis.

- «El segundo trozo» → `trozo2`: la segunda casilla se llena, con el rótulo «entre los grupos»
- «las medias de los grupos» → `medias`: dos puntos, 175 y 162, sobre un eje de alturas
- «alrededor de la media total» → `total`: una línea ámbar en 167,2 entre los dos
- «La media de los hombres» → `hombres`: el punto de 175 se resalta
- «siete coma ocho centímetros» → `d78`: una flecha de 167,2 a 175 con «7,8»
- «de ciento sesenta y siete coma dos» → `de1672`: la marca «167,2» se agranda
- «la de las mujeres» → `mujeres`: el punto de 162 se resalta
- «cinco coma dos» → `d52`: una flecha de 167,2 a 162 con «5,2»
- «Al cuadrado y con sus pesos» → `cuadrado`: «0,4 · 7,8² + 0,6 · 5,2²» se escribe por piezas
- «veinticuatro coma treinta y cuatro» → `r2434`: «= 24,34» bajo el primer sumando
- «dieciséis coma veintidós» → `r1622`: «+ 16,22» bajo el segundo
- «Cuarenta coma cinco seis» → `suma2`: «= 40,56» en ámbar y una segunda barra de ese tamaño

---

# Escena 13 — LeyVarianzaTotal

**Capítulo YouTube:** La ley de la varianza total

## Narración

<!-- b1 -->
La varianza total de la altura es la suma de los dos trozos: ochenta y uno coma setenta y seis, una desviación típica de unos nueve centímetros. Casi mitad y mitad. Esto es la ley de la varianza total: la varianza de una variable es la media de las varianzas dentro de los grupos, más la varianza de las medias de los grupos.

- «la suma de los dos trozos» → `suma`: las dos barras (41,2 y 40,56) se apilan
- «ochenta y uno coma setenta y seis» → `r8176`: «41,2 + 40,56 = 81,76» sobre la barra apilada
- «unos nueve centímetros» → `sigma9`: «σ ≈ 9 cm»
- «Casi mitad y mitad» → `mitad`: una línea parte la barra por la mitad
- «la ley de la varianza total» → `ley`: «ley de la varianza total» entra con rebote
- «la media de las varianzas dentro de los grupos» → `f_dentro`: aparece «E[Var(X | Y)]», con la barra de 41,2 resaltada
- «la varianza de las medias de los grupos» → `f_entre`: aparece «+ Var(E[X | Y])», con la barra de 40,56 resaltada

<!-- b2 -->
Léelo de otra forma. El segundo trozo es lo que saber el grupo explica de la altura. El primero es lo que sigue sin saberse aunque conozcas el grupo. Guarda esta idea, porque volverá: cuando intentemos adivinar una variable a partir de otra, el error que cometeremos, incluso haciéndolo lo mejor posible, será exactamente ese primer trozo.

- «lo que saber el grupo explica» → `explica`: la barra de 40,56 se tiñe de verde, «lo que explica el grupo»
- «El primero» → `primero`: la barra de 41,2 se resalta
- «sigue sin saberse» → `sin_saber`: la barra de 41,2 se tiñe de rojo, «lo que no explica el grupo»
- «Guarda esta idea» → `guarda`: la barra roja se encierra en un marco ámbar
- «adivinar una variable a partir de otra» → `adivinar`: dos flechas, de Y hacia X, con una interrogación
- «el error que cometeremos» → `error`: entra «error» en rojo bajo la flecha
- «lo mejor posible» → `mejor`: un sello «lo mejor posible» sobre el marco
- «ese primer trozo» → `trozo`: el marco se une con la barra roja y queda parpadeando una vez

---

# Escena 14 — Cierre

**Capítulo YouTube:** Lo que viene: lo que una variable sabe de otra

## Narración

<!-- b1 -->
Resumiendo: con una tabla, o con una colina, dos variables a la vez lo contienen todo. De ahí salen las marginales, las condicionales y la media de una sabiendo la otra. Y la varianza se parte en lo que el grupo explica y lo que no. Pero falta algo: un solo número que diga cuánto sabe una variable de otra. De eso va el próximo episodio: «Lo que una variable sabe de otra».

- «con una tabla, o con una colina» → `tabla_colina`: la tabla 2 × 2 y la colina, una al lado de otra
- «dos variables a la vez» → `dos`: S y R juntos en el par «(S, R)»
- «las marginales» → `marginales`: las dos sumas en los márgenes de la tabla
- «las condicionales» → `condicionales`: la columna iluminada con «0,79»
- «la media de una sabiendo la otra» → `esperanza`: la curva «E[Y | X = x]» sobre la nube
- «la varianza se parte» → `parte`: la barra apilada se parte en verde y rojo
- «lo que el grupo explica» → `explica`: la barra verde se agranda
- «Pero falta algo» → `falta`: aparece un «?» grande
- «un solo número» → `numero`: aparece un casillero con un solo «?»
- «cuánto sabe una variable de otra» → `sabe`: dos flechas entre X e Y, con la interrogación sobre el casillero
- «el próximo episodio» → `proximo`: aparece «próximo episodio», en gris
- «Lo que una variable» → `t1`: entra «Lo que una variable»
- «sabe de otra» → `t2`: entra «sabe de otra», en ámbar
