# Episodio 2 — Lo que el dato te cuenta

Capítulo 8 (Estimación), episodio 2 de 5. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 05 a 08), más un gancho y un cierre nuevos.
Ejemplos que vuelven con el mismo dibujo y los mismos números: la altura del Cap. 7 (40 % hombres de 175 cm, 60 % mujeres de 162 cm; 81,76 → 41,2 + 40,56) y el canal que confunde bits (0,7 / 0,3 y una de cada diez veces; tabla 0,63 · 0,07 · 0,03 · 0,27).

**Estado:** **Subido a YouTube y publicado** (19/10/2026): render final 1080p60 de 9:10, título buscable, descripción con el capítulo del libro y `capitulos.txt`, subtítulos, categoría Educación (https://youtu.be/CCC0y1jMOoM). Lo subió el usuario sin el visto bueno que figuraba pendiente (texto ⭐ / mp4). Residuos limpiados; la caché de voz original está en `media/voiceovers/`: se rehace igual con `python rehacer.py Capitulo08_Estimacion E2`.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Alguien entra por la puerta y tienes que adivinar su altura. Te dicen una sola cosa y tu error se reduce a la mitad…».
- ⭐ Escena 16 (cierre): resume el episodio, plantea el problema de la distribución entera y anuncia E3, «¿Y si solo vale una recta?».
- ⭐ Retoque en la escena 03 (b1): «ya sabes qué hacer» pasa a «como en el episodio anterior, ya sabes qué hacer», porque el episodio se ve suelto.
- ⭐ Retoque en la escena 05 (b1): «prometimos» → «prometimos al final de aquel capítulo», para ubicar la promesa.

---

# Escena 01 — Gancho

**Capítulo YouTube:** Lo que el dato te cuenta

## Narración

<!-- b1 -->
Alguien entra por la puerta y tienes que adivinar su altura. Si te dicen una sola cosa, tu error se reduce a la mitad. Y lo que queda no tiene ningún patrón que puedas aprovechar.

- «Alguien entra por la puerta» → `puerta`: una puerta y una silueta que entra
- «adivinar su altura» → `altura`: una regla de altura con un «?» sobre la silueta
- «una sola cosa» → `dato`: una tarjeta «Es mujer» se coloca junto a la silueta
- «se reduce a la mitad» → `mitad`: una barra «81,76» se encoge hasta «41,2»
- «ningún patrón» → `patron`: una nube de errores sueltos alrededor de cero, sin forma

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Lo que el dato te cuenta

## Narración

<!-- b1 -->
Lo que el dato te cuenta.

- «Lo que el dato» → `t1`: «Lo que el dato» entra con rebote, con la etiqueta «Capítulo 8 · Estimación»
- «te cuenta» → `t2`: «te cuenta» entra debajo

---

# Escena 03 — LaAlturaOtraVez

**Capítulo YouTube:** La altura otra vez
**Objetivo:** recordar la población de la altura y apostar la media de todos, con el error de siempre: la varianza.

## Narración

<!-- b1 -->
Recuerda la población del capítulo siete, en la que el cuarenta por ciento son hombres, con una altura media de ciento setenta y cinco centímetros, y el sesenta por ciento son mujeres, con ciento sesenta y dos. Entra alguien por la puerta y tienes que adivinar su altura. Si no sabes nada de esa persona, como en el episodio anterior, ya sabes qué hacer.

- «el capítulo siete» → `cap7`: las dos campanas de la altura, la azul (hombres) y la magenta (mujeres), del mismo dibujo del Cap. 7
- «el cuarenta por ciento son hombres» → `hombres`: la campana azul se resalta con «Hombres · 40 %»
- «ciento setenta y cinco centímetros» → `h175`: una marca vertical azul en «175»
- «el sesenta por ciento son mujeres» → `mujeres`: la campana magenta se resalta con «Mujeres · 60 %»
- «ciento sesenta y dos» → `m162`: una marca vertical magenta en «162»
- «Entra alguien por la puerta» → `entra`: una silueta aparece a la derecha con un «?»
- «adivinar su altura» → `adivinar`: la silueta con la regla de altura y el «?» crece
- «Si no sabes nada» → `nada`: las dos campanas se funden en una sola, ancha, que son todos
- «ya sabes qué hacer» → `sabes`: se pregunta «¿Qué apuesta?» con un tilde de «la media»

<!-- b2 -->
Apuestas la media de toda la población, que es ciento sesenta y siete coma dos. Y el error cuadrático medio es la varianza de la altura, que calculamos entonces y que vale ochenta y uno coma setenta y seis, una desviación típica de unos nueve centímetros. Ahora cambiemos una cosa, y es que antes de apostar alguien te dice si es un hombre o una mujer.

- «la media de toda la población» → `media`: se dibuja la campana ancha de toda la población con su marca ámbar
- «ciento sesenta y siete coma dos» → `n1672`: «ŷ = 167,2» aparece sobre la marca
- «el error cuadrático medio» → `ecm`: se enciende «Error cuadrático medio»
- «la varianza de la altura» → `varianza`: «= σ²» junto al error
- «ochenta y uno coma setenta y seis» → `n8176`: una barra roja larga con «81,76»
- «unos nueve centímetros» → `nueve`: una llave sobre la campana ancha con «≈ 9 cm»
- «Ahora cambiemos una cosa» → `cambiemos`: la campana ancha se aparta a un lado
- «antes de apostar» → `antes_apostar`: una mano con una tarjeta se acerca a la silueta
- «alguien te dice» → `dice`: aparecen dos tarjetas, «Hombre» y «Mujer»

---

# Escena 04 — SabiendoElGrupo

**Capítulo YouTube:** Saber el grupo achica el error
**Objetivo:** apostar la media de cada grupo, con el error de cada grupo, y en promedio 41,2 en vez de 81,76.

## Narración

<!-- b1 -->
Si te dicen «es una mujer», el mundo se achica, porque ya solo cuentan las mujeres. Dentro de ese grupo repites lo de siempre, que es apostar su media, ciento sesenta y dos, y el error es la varianza de ese grupo, seis al cuadrado, treinta y seis. Si te dicen «es un hombre», apuestas ciento setenta y cinco, con un error de siete al cuadrado, cuarenta y nueve.

- «es una mujer» → `mujer`: la tarjeta «Mujer» se ilumina y la campana azul se apaga
- «el mundo se achica» → `achica`: la campana magenta crece hasta ocupar todo el dibujo
- «ya solo cuentan las mujeres» → `solo_mujeres`: las siluetas de mujer se iluminan, las de hombre se apagan
- «Dentro de ese grupo» → `dentro`: un marco ámbar rodea la campana magenta
- «lo de siempre» → `lo_siempre`: «Media y varianza» se escribe junto a la campana
- «apostar su media» → `su_media`: una marca ámbar en el centro de la campana magenta
- «ciento sesenta y dos» → `n162`: «ŷ = 162» sobre la marca
- «seis al cuadrado» → `seis2`: «error = 6² = 36» con una barra roja corta
- «es un hombre» → `hombre`: la tarjeta «Hombre» se ilumina; la campana azul vuelve y se apaga la magenta
- «ciento setenta y cinco» → `n175`: «ŷ = 175» sobre su marca ámbar
- «siete al cuadrado» → `siete2`: «error = 7² = 49» con una barra roja un poco más larga

<!-- b2 -->
¿Y en promedio, sin saber todavía quién entrará? Cuatro de cada diez veces tendrás un error de cuarenta y nueve, y seis de cada diez, uno de treinta y seis. Cero coma cuatro por cuarenta y nueve, más cero coma seis por treinta y seis, que da cuarenta y uno coma dos. Saber el grupo ha reducido el error a la mitad.

- «sin saber todavía quién entrará» → `sin_saber`: las dos tarjetas de error («49» y «36») quedan una junto a la otra
- «Cuatro de cada diez veces» → `cuatro`: «0,4» sobre el 49
- «seis de cada diez» → `seis`: «0,6» sobre el 36
- «Cero coma cuatro por cuarenta y nueve» → `c1`: «0,4 · 49 = 19,6» se escribe
- «más cero coma seis por treinta y seis» → `c2`: «+ 0,6 · 36 = 21,6» se escribe
- «cuarenta y uno coma dos» → `suma`: «= 41,2» en verde
- «reducido el error a la mitad» → `mitad`: la barra de 81,76 se encoge a la de 41,2

---

# Escena 05 — LaPromesaDelCapitulo7

**Capítulo YouTube:** La promesa del capítulo siete
**Objetivo:** el 41,2 es el primer trozo de la ley de la varianza total: la promesa se cumple.

## Narración

<!-- b1 -->
Y ese cuarenta y uno coma dos no es un número nuevo. Es el primer trozo de la ley de la varianza total, es decir, lo que el grupo no explica. En el capítulo siete prometimos, al final de aquel capítulo, que el error del mejor estimador sería exactamente ese trozo, y aquí está. La otra mitad, cuarenta coma cinco seis, es justo lo que nos ha ahorrado saber el grupo.

- «no es un número nuevo» → `nuevo`: «41,2» en grande, con un signo de interrogación que se desvanece
- «la ley de la varianza total» → `ley`: la barra del Cap. 7: «41,2 + 40,56 = 81,76» partida en rojo y verde
- «lo que el grupo no explica» → `no_explica`: el trozo rojo se resalta con «Lo que el grupo no explica»
- «prometimos» → `prometimos`: sobre el trozo rojo, «Error del mejor estimador» y un «?»
- «al final de aquel capítulo» → `final`: la barra del Cap. 7 aparece con «Capítulo 7» pequeño
- «el error del mejor estimador» → `mejor_est`: el trozo rojo se vuelve a iluminar
- «exactamente ese trozo» → `exacto`: una flecha une «41,2» con «Error»
- «aquí está» → `aqui`: un tilde verde de «Promesa cumplida»
- «cuarenta coma cinco seis» → `n4056`: el trozo verde se resalta con «40,56»
- «nos ha ahorrado» → `ahorrado`: una flecha verde de la barra entera al trozo rojo, «Lo ahorrado»

---

# Escena 06 — RebanadaPorRebanada

**Capítulo YouTube:** Rebanada por rebanada
**Objetivo:** generalizar: observado X = x, la mejor apuesta es la media condicional y el error es la varianza condicional.

## Narración

<!-- b1 -->
Lo que acabamos de hacer funciona siempre. Observas una variable, equis, y quieres adivinar otra, i griega. Cuando ves que equis vale un valor concreto, el mundo se achica a los casos donde equis vale eso. Dentro de ese mundo pequeño, el problema es el de siempre, así que apuestas la media y el error será la varianza.

- «funciona siempre» → `siempre`: una nube de puntos (x, y)
- «equis» → `equis`: «X» azul bajo el eje horizontal
- «i griega» → `griega`: «Y» cian junto al eje vertical
- «equis vale un valor concreto» → `valor`: una rebanada vertical se ilumina en «X = x» y el resto de la nube se apaga
- «el mundo se achica» → `achica`: la rebanada se amplía a un lado, aislada
- «los casos donde equis vale eso» → `casos`: la rebanada se ensancha a un lado, con los puntos de dentro
- «Dentro de ese mundo pequeño» → `pequeno`: un marco ámbar rodea la rebanada aislada
- «el problema es el de siempre» → `siempre2`: el dado «3,5 · 2,92» asoma en una esquina
- «apuestas la media» → `apuesta`: un punto ámbar en el centro de la rebanada
- «la varianza» → `varianza`: una llave roja sobre la rebanada, de su ancho

<!-- b2 -->
Solo que ahora son la media y la varianza dentro del mundo achicado, es decir, la esperanza condicional de i griega dado equis, y la varianza condicional. Es la regla del dado, aplicada rebanada a rebanada. Ningún cálculo nuevo, sino la misma idea repetida para cada valor que pueda tomar lo que observas.

- «la media y la varianza» → `mv`: «media» y «varianza» junto a la rebanada
- «la esperanza condicional» → `esperanza`: se construye «E[Y | X = x]» en ámbar
- «la varianza condicional» → `var_cond`: se construye «Var(Y | X = x)» en rojo
- «la regla del dado» → `dado`: aparece un dado con «3,5» y «2,92»
- «rebanada a rebanada» → `rebanadas`: la nube vuelve y se iluminan varias rebanadas, una tras otra, con su punto ámbar
- «Ningún cálculo nuevo» → `nuevo`: una cruz roja sobre «Cálculo nuevo»
- «la misma idea» → `idea`: la rebanada se repite en tres posiciones
- «para cada valor» → `cada`: los puntos ámbar se unen en una curva

---

# Escena 07 — CanalPorColumnas

**Capítulo YouTube:** El canal, columna por columna
**Objetivo:** con la tabla del canal, apuesta 0,79 si se recibe un uno y 0,045 si se recibe un cero, con errores 0,16 y 0,04.

## Narración

<!-- b1 -->
Volvamos al canal que confunde bits. Se envía un cero con probabilidad cero coma siete y un uno con cero coma tres, y el canal cambia el bit una de cada diez veces. Si recibes un uno, la columna de recibir uno dice que se envió un uno con probabilidad cero coma setenta y nueve. Esa es la media de lo enviado en esa columna, y esa es la apuesta.

- «canal que confunde bits» → `canal`: el canal del Cap. 7 (entrada, caja, salida), mismo dibujo
- «Se envía un cero» → `envia`: un «0» azul recorre la flecha de entrada hasta la caja
- «cero coma siete» → `p0`: «0 · 0,7» sobre la entrada
- «un uno con cero coma tres» → `p1`: «1 · 0,3» sobre la entrada
- «una de cada diez veces» → `error`: «10 %» en rojo sobre la caja
- «Si recibes un uno» → `recibes`: el canal se encoge y aparece la tabla 2 × 2 con 0,63 · 0,07 · 0,03 · 0,27; la columna R = 1 se resalta
- «la columna de recibir uno» → `columna`: la columna R = 1 de la tabla se marca con un marco
- «se envió un uno» → `env1`: la casilla «0,27» se ilumina frente a «0,07»
- «cero coma setenta y nueve» → `n79`: «0,27 / 0,34 ≈ 0,79» sale de la columna
- «la media de lo enviado» → `media_env`: «E[S | R = 1]» en ámbar junto al 0,79
- «esa es la apuesta» → `apuesta`: «ŝ = 0,79» en un cuadro verde

<!-- b2 -->
Si recibes un cero, en la otra columna se envió un uno con probabilidad cero coma cero cuatro cinco, y eso es lo que apuestas. Y los errores son las varianzas de cada columna. Para algo que vale uno con probabilidad pe y cero si no, la varianza es pe por uno menos pe. Cero coma uno seis en la primera columna, y cero coma cero cuatro en la segunda.

- «Si recibes un cero» → `cero`: la columna R = 0 se resalta y la otra se apaga
- «en la otra columna» → `otra`: la columna R = 0 se marca con un marco
- «cero coma cero cuatro cinco» → `n045`: «0,03 / 0,66 ≈ 0,045» sale de la columna
- «lo que apuestas» → `apuesta0`: «ŝ = 0,045» en un cuadro verde
- «los errores son las varianzas» → `errores`: sobre cada columna, «Error = varianza»
- «Para algo que vale uno» → `algo`: un bit «1» con un «0» al lado
- «con probabilidad pe» → `pe`: «P(1) = p» aparece
- «y cero si no» → `cero_si_no`: «P(0) = 1 − p» aparece
- «pe por uno menos pe» → `pq`: se construye «p (1 − p)» pieza a pieza
- «Cero coma uno seis» → `e16`: «0,79 · 0,21 ≈ 0,16» bajo la columna R = 1
- «cero coma cero cuatro» → `e04`: «0,045 · 0,955 ≈ 0,04» bajo la columna R = 0

---

# Escena 08 — NoEsUnBit

**Capítulo YouTube:** Cero coma setenta y nueve no es un bit
**Objetivo:** la mejor apuesta no es ni cero ni uno; decidir es otra cosa y queda para el capítulo siguiente.

## Narración

<!-- b1 -->
Fíjate en algo raro, y es que la mejor apuesta, cero coma setenta y nueve, no es un bit. Ni cero ni uno. Con el error al cuadrado no se busca acertar, sino quedarse cerca, y eso a veces cae entre medias. Si lo que necesitas es elegir entre cero y uno, eso ya es decidir, y es el tema del capítulo siguiente. Guárdate esta pregunta.

- «algo raro» → `raro`: una moneda con «0» y «1» a los lados
- «cero coma setenta y nueve» → `n79`: «0,79» aparece entre medias, cerca del uno, con una interrogación ámbar
- «no es un bit» → `no_bit`: un aspa roja sobre el 0,79 y las dos opciones «0» y «1» se agrandan
- «Ni cero ni uno» → `ni`: el «0» y el «1» se agrandan, el 0,79 queda entre ellos
- «no se busca acertar» → `acertar`: una diana tachada
- «quedarse cerca» → `cerca`: una flecha corta del 0,79 hacia el 1, «Cerca»
- «a veces cae entre medias» → `medias`: el 0,79 se queda entre los dos bits
- «Si lo que necesitas» → `necesitas`: las cajas «0» y «1» se acercan a una mano que elige
- «elegir entre cero y uno» → `elegir`: dos cajas «0» y «1» con una flecha que elige una
- «ya es decidir» → `decidir`: «Decidir ≠ estimar»
- «el capítulo siguiente» → `cap9`: etiqueta «Capítulo 9»
- «Guárdate esta pregunta» → `guarda`: la pregunta «¿Cero o uno?» se guarda en un cofre

---

# Escena 09 — ReglaYNumero

**Capítulo YouTube:** Una regla, no un número
**Objetivo:** distinguir la estimación ya calculada (un número) del estimador antes de mirar (una variable aleatoria) y darle su distribución.

## Narración

<!-- b1 -->
Hay una diferencia sutil entre dos cosas que se escriben casi igual. Una función evaluada en tres, efe de tres, es un número. Una función sin evaluar, efe de un punto que todavía no conoces, es una regla. Con la estimación pasa lo mismo. Si ya recibiste un uno, la apuesta es un número, el cero coma setenta y nueve.

- «dos cosas que se escriben casi igual» → `dos`: «f(3)» y «f(x)» a la vista, una junto a la otra
- «Una función evaluada en tres» → `evaluada`: «f(x) = x² + 16» con la x sustituida por 3
- «efe de tres» → `f3`: «f(3)» se resalta, sale «= 25» como ejemplo de número
- «es un número» → `numero`: una casilla con un número, «Un número»
- «Una función sin evaluar» → `sin_evaluar`: «f(·)» con un hueco
- «es una regla» → `regla`: una caja con entrada y salida, «Una regla»
- «Con la estimación pasa lo mismo» → `igual`: «ŝ» y «Ŝ» a la vez, uno minúscula y otro mayúscula
- «Si ya recibiste un uno» → `recibido`: el canal con el «1» a la salida
- «cero coma setenta y nueve» → `n79`: «0,79» dentro de la casilla del número

<!-- b2 -->
Pero antes de recibir nada, la apuesta es una regla que dice que, si llega un uno, la apuesta es cero coma setenta y nueve y, si llega un cero, es cero coma cero cuatro cinco. Y como lo que llega es aleatorio, la apuesta también lo es. Es una variable aleatoria, con su propia distribución, pues vale cero coma setenta y nueve con probabilidad cero coma treinta y cuatro y cero coma cero cuatro cinco con cero coma sesenta y seis.

- «antes de recibir nada» → `antes`: la caja-regla con dos casillas
- «si llega un uno» → `llega1`: «Recibo 1 → 0,79» en la primera casilla
- «si llega un cero» → `llega0`: «Recibo 0 → 0,045» en la segunda
- «cero coma cero cuatro cinco» → `n045`: «0,045» resaltado en la segunda casilla
- «lo que llega es aleatorio» → `aleatorio`: la entrada de la regla parpadea entre «0» y «1»
- «la apuesta también lo es» → `tambien`: «Ŝ» (con mayúscula) sale de la regla
- «variable aleatoria» → `va`: «Variable aleatoria» entra con rebote
- «con su propia distribución» → `distrib`: dos barras vacías aparecen
- «vale cero coma setenta y nueve» → `vale79`: la barra del 0,79 se levanta
- «cero coma treinta y cuatro» → `p34`: una barra de probabilidad en 0,79 con «0,34»
- «cero coma sesenta y seis» → `p66`: una barra en 0,045 con «0,66»

---

# Escena 10 — MediaDelEstimador

**Capítulo YouTube:** El estimador no se desvía
**Objetivo:** la media del estimador es la media de lo enviado: la torre; el estimador es insesgado.

## Narración

<!-- b1 -->
Como toda variable aleatoria, tiene media. Cero coma treinta y cuatro por cero coma setenta y nueve, más cero coma sesenta y seis por cero coma cero cuatro cinco, que da cero coma tres. Es la media de lo enviado. No es casualidad, sino la propiedad de la torre del capítulo siete. Quiere decir que la estimación, en promedio, no se desvía hacia ningún lado.

- «tiene media» → `media`: las dos barras de la escena anterior, con un fiel bajo ellas
- «Cero coma treinta y cuatro por cero coma setenta y nueve» → `t1`: «0,34 · 0,79 = 0,27» se escribe
- «más cero coma sesenta y seis por cero coma cero cuatro cinco» → `t2`: «+ 0,66 · 0,045 = 0,03» se escribe
- «cero coma tres» → `r03`: «= 0,3» en verde y el fiel se coloca en 0,3
- «la media de lo enviado» → `enviado`: «E[S] = 0,3» junto al resultado, la misma cuenta
- «la propiedad de la torre» → `torre`: se escribe «E[ E[S | R] ] = E[S]» con el cartel «La torre»
- «del capítulo siete» → `cap7`: «Capítulo 7» pequeño junto a la torre
- «Quiere decir» → `quiere`: el fiel vuelve a su sitio y brilla
- «en promedio, no se desvía» → `no_desvia`: una balanza en equilibrio, «Sin sesgo»

---

# Escena 11 — ErrorTotal

**Capítulo YouTube:** El error total
**Objetivo:** promediar el error sobre lo recibido: 0,084 contra 0,21, un 60 % menos.

## Narración

<!-- b1 -->
También tiene un error total, promediando sobre lo que llegue. Cero coma treinta y cuatro por cero coma uno seis, más cero coma sesenta y seis por cero coma cero cuatro, que da cero coma cero ocho cuatro. Sin mirar el canal, el error sería la varianza de lo enviado, cero coma dos uno. Mirar lo recibido lo ha reducido un sesenta por ciento.

- «error total» → `total`: las dos columnas con sus errores «0,16» y «0,04» y sus pesos «0,34» y «0,66»
- «Cero coma treinta y cuatro por cero coma uno seis» → `c1`: «0,34 · 0,16» se escribe
- «más cero coma sesenta y seis por cero coma cero cuatro» → `c2`: «+ 0,66 · 0,04» se escribe
- «cero coma cero ocho cuatro» → `r084`: «≈ 0,084» en verde
- «Sin mirar el canal» → `sin_mirar`: una barra roja larga aparece debajo
- «la varianza de lo enviado» → `var_s`: «σ² = 0,3 · 0,7 = 0,21» se escribe sobre la barra
- «cero coma dos uno» → `n021`: «0,21» resaltado sobre la barra
- «Mirar lo recibido» → `mirar`: una lupa sobre la salida del canal
- «un sesenta por ciento» → `sesenta`: la barra se encoge hasta 0,084 con «−60 %»

---

# Escena 12 — LasColumnasNoSeEstorban

**Capítulo YouTube:** Por qué la media condicional es la mejor
**Objetivo:** cada columna ya está en su mínimo, y las columnas no se estorban; así la media condicional es el mejor estimador posible.

## Narración

<!-- b1 -->
¿Podría otra regla conseguir un error total más pequeño? No. El error total es un promedio de los errores de cada columna, y cada uno ya es el más pequeño posible. Las columnas no se estorban, así que mejorar una no empeora la otra. Así que la media condicional es la mejor regla, y su error es la media de las varianzas condicionales. Se llama estimador de mínimo error cuadrático medio.

- «otra regla» → `otra`: una regla alternativa «0,6 / 0,1» sustituye a la de 0,79 / 0,045, con una interrogación
- «un error total más pequeño» → `menor`: la cuenta de la escena anterior con la regla nueva, más grande
- «No.» → `no`: una cruz roja grande sobre la regla alternativa
- «un promedio de los errores de cada columna» → `promedio`: las dos columnas con una parábola de error cada una
- «el más pequeño posible» → `minimo`: en cada parábola, un punto verde en el fondo, sobre 0,79 y 0,045
- «no se estorban» → `pared`: una pared entre las dos columnas
- «mejorar una no empeora la otra» → `mejorar`: una flecha mueve el punto de una parábola sin tocar la otra
- «la media condicional es la mejor regla» → `mejor`: se construye «Ŷ = E[Y | X]» en ámbar
- «la media de las varianzas condicionales» → `err`: se construye «Error = E[Var(Y | X)]» en rojo
- «Se llama estimador» → `llama`: el cuadro de la fórmula se resalta
- «mínimo error cuadrático medio» → `mmse`: el rótulo «Estimador de mínimo error cuadrático medio» con la sigla «MMSE» al lado

---

# Escena 13 — ErrorCompensado

**Capítulo YouTube:** Dentro de cada columna, el error se compensa
**Objetivo:** con el canal, comprobar que dentro de cada columna el error medio es cero.

## Narración

<!-- b1 -->
El mejor estimador tiene una propiedad que lo explica todo, y se ve en el canal. Mira la columna de recibir un uno. Cuando se envió un uno, el error es uno menos cero coma setenta y nueve, o sea, cero coma dos uno. Cuando se envió un cero, es menos cero coma setenta y nueve. Unas veces nos quedamos cortos y otras nos pasamos.

- «una propiedad que lo explica todo» → `propiedad`: la tabla del canal
- «se ve en el canal» → `canal`: el canal pequeño aparece sobre la tabla
- «la columna de recibir un uno» → `col1`: la columna R = 1 se resalta, con sus dos casillas «0,07» y «0,27»
- «Cuando se envió un uno» → `env1`: la casilla de abajo (0,27) se ilumina
- «uno menos cero coma setenta y nueve» → `cuenta`: «1 − 0,79» se escribe
- «cero coma dos uno» → `e21`: «= +0,21» sobre la casilla
- «Cuando se envió un cero» → `env0`: la casilla de arriba (0,07) se ilumina
- «menos cero coma setenta y nueve» → `e79`: «0 − 0,79 = −0,79» sobre la casilla
- «nos quedamos cortos» → `cortos`: una flecha hacia arriba (error positivo) en la casilla de abajo
- «nos pasamos» → `pasamos`: una flecha hacia abajo (error negativo) en la de arriba

<!-- b2 -->
¿Cuánto vale el error en promedio dentro de esa columna? Cero coma veintisiete por cero coma dos uno, menos cero coma cero siete por cero coma setenta y nueve. Cero coma cero cinco seis menos cero coma cero cinco seis, que da cero. Y en la otra columna pasa lo mismo. Dentro de cada columna, el error se compensa exactamente.

- «en promedio dentro de esa columna» → `promedio`: una balanza con las dos casillas en los platillos
- «Cero coma veintisiete por cero coma dos uno» → `a`: «0,27 · 0,21 = 0,056» se escribe, platillo izquierdo
- «menos cero coma cero siete por cero coma setenta y nueve» → `b`: «− 0,07 · 0,79 = −0,056» se escribe, platillo derecho
- «Cero coma cero cinco seis menos cero coma cero cinco seis» → `resta`: «0,056 − 0,056» se escribe
- «que da cero» → `cero`: «= 0» en verde y la balanza queda horizontal
- «en la otra columna» → `otra`: la columna R = 0 se resalta, con una balanza pequeña también en equilibrio
- «pasa lo mismo» → `mismo`: la balanza pequeña de la otra columna se equilibra
- «se compensa exactamente» → `compensa`: «Se compensa» en verde

---

# Escena 14 — CualquierFuncion

**Capítulo YouTube:** Ortogonal a cualquier función del dato
**Objetivo:** multiplicar el error por cualquier función de lo recibido da media cero; eso es ser ortogonal; es la regla de ortogonalidad.

## Narración

<!-- b1 -->
Eso tiene una consecuencia fuerte. Toma cualquier función de lo recibido, es decir, un número para la columna del uno y otro para la del cero. Multiplícala por el error y haz la media. Dentro de cada columna, ese número es fijo y sale fuera, y lo que queda es la media del error en la columna, que es cero. Así que la media del producto es cero, sea cual sea la función.

- «una consecuencia fuerte» → `fuerte`: las dos columnas del canal, con el error medio «0» en cada una
- «cualquier función de lo recibido» → `funcion`: sobre cada columna un número libre, «5» y «−2»
- «un número para la columna del uno» → `n1`: el «5» sobre la columna R = 1 se resalta
- «otro para la del cero» → `n0`: el «−2» sobre la columna R = 0 se resalta
- «Multiplícala por el error» → `mult`: se construye «E[ e · g(R) ]» por piezas
- «haz la media» → `haz`: «E[ ]» se cierra sobre el producto
- «Dentro de cada columna» → `dentro`: un marco rodea cada columna
- «ese número es fijo y sale fuera» → `fuera`: el «5» sale fuera de la media, «5 · E[e]»
- «la media del error en la columna» → `media_e`: «E[e | R = 1] = 0» dentro del paréntesis
- «cero» → `cero`: «= 0,34 · 5 · 0 + 0,66 · (−2) · 0 = 0»
- «sea cual sea la función» → `sea`: el 5 y el −2 cambian de valor varias veces y el resultado sigue siendo 0

<!-- b2 -->
En el capítulo siete, dos variables cuya esperanza del producto vale cero eran ortogonales, o sea, flechas perpendiculares. Así que el error del mejor estimador es ortogonal a cualquier función de lo observado. Se llama regla de ortogonalidad, y es la idea más importante del capítulo.

- «el capítulo siete» → `cap7`: dos flechas que forman un ángulo recto, con «E[U V] = 0»
- «cuya esperanza del producto vale cero» → `producto`: «E[U · V] = 0» se escribe junto a las flechas
- «ortogonales» → `ortog`: una marca de ángulo recto entre las dos flechas
- «flechas perpendiculares» → `perp`: las flechas se rotulan «Error» (rojo) y «g(R)» (cian)
- «el error del mejor estimador» → `err`: la flecha roja se resalta
- «cualquier función de lo observado» → `cualquier`: aparecen varias flechas cian, todas perpendiculares al error
- «regla de ortogonalidad» → `regla`: el cartel «Regla de ortogonalidad» entra con rebote
- «la idea más importante» → `importante`: un marco ámbar rodea el cartel

---

# Escena 15 — SinPatron

**Capítulo YouTube:** El error no tiene patrón
**Objetivo:** leer la regla: el error no tiene ningún patrón que dependa del dato; si lo tuviera, se podría mejorar.

## Narración

<!-- b1 -->
Léela así. El error no tiene ningún patrón que dependa del dato. Si lo tuviera, si por ejemplo nos quedáramos cortos siempre que llega un uno, bastaría con sumar algo en esa columna para mejorar. Que el error sea ortogonal a todo lo que se puede calcular con el dato significa que ya le hemos sacado toda la información. Esta perpendicular volverá convertida en un dibujo.

- «ningún patrón» → `patron`: errores en puntos sueltos alrededor de cero, para cada columna, sin forma
- «Si lo tuviera» → `tuviera`: la columna R = 1 con todos los errores por encima de cero
- «nos quedáramos cortos siempre que llega un uno» → `cortos`: una flecha roja indica «Siempre cortos»
- «sumar algo en esa columna» → `sumar`: una flecha ámbar baja los puntos hasta centrarlos en cero
- «para mejorar» → `mejorar`: la barra de error se acorta, «Mejor»
- «ortogonal a todo lo que se puede calcular con el dato» → `ortogonal`: vuelven las dos flechas perpendiculares de la escena anterior
- «lo que se puede calcular» → `calcular`: una fila de funciones g₁(R), g₂(R), g₃(R) aparece
- «toda la información» → `toda`: se enciende «Toda la información usada» con un tilde
- «volverá convertida en un dibujo» → `dibujo`: la perpendicular se queda sola, grande, con «¿Y si solo una recta?» sin mostrar todavía

---

# Escena 16 — Cierre

**Capítulo YouTube:** Lo que viene: ¿y si solo vale una recta?

## Narración

<!-- b1 -->
Resumiendo, con un dato, la mejor apuesta es la media de la rebanada, y el error que queda no tiene ningún patrón. Pero hay una pega. Para calcular esa media hace falta conocer la distribución entera, y casi nunca la tenemos, porque lo que tenemos son medias, varianzas y covarianzas. ¿Qué pasa si solo podemos usar una recta? En el próximo episodio responderemos a la pregunta «¿Y si solo vale una recta?»

- «Resumiendo» → `resumen`: una rebanada con su punto ámbar y, debajo, una flecha roja perpendicular
- «la media de la rebanada» → `rebanada`: la rebanada se ilumina con «E[Y | X = x]»
- «ningún patrón» → `patron`: el error se resalta con un tilde
- «una pega» → `pega`: aparece un «!» ámbar
- «la distribución entera» → `entera`: una colina enorme, con «Toda la distribución»
- «casi nunca la tenemos» → `nunca`: la colina se tacha en rojo
- «medias, varianzas y covarianzas» → `numeros`: aparecen tres números, «μ», «σ²» y «σ_XY»
- «solo podemos usar una recta» → `recta`: una recta se dibuja sobre la nube de puntos
- «En el próximo episodio» → `proximo`: etiqueta «Próximo episodio»
- «¿Y si» → `t1`: «¿Y si solo» entra con rebote
- «vale una recta» → `t2`: «vale una recta?» entra debajo
