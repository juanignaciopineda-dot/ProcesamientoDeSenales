# Episodio 1 — ¿Cuál es tu mejor apuesta?

Capítulo 8 (Estimación), episodio 1 de 5. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 01 a 04), más un gancho y un cierre nuevos.

**Estado:** **Subido a YouTube y publicado** (19/10/2026): render final 1080p60 de 9:07, título buscable, descripción con el capítulo del libro y `capitulos.txt`, subtítulos, categoría Educación (https://youtu.be/uIbSQQLmxYQ). Residuos limpiados; la caché de voz original está en `media/voiceovers/`: se rehace igual con `python rehacer.py Capitulo08_Estimacion E1`.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Voy a tirar un dado y tú tienes que adivinar qué número sale. Y la mejor apuesta es tres coma cinco, pero un dado no puede sacar este número nunca.»
- ⭐ Escena 15 (cierre): resumen y anuncia E2 por su título, «Lo que el dato te cuenta».

Nota para el episodio anterior: el cierre del E7 del Cap. 7 tiene que anunciar el título de este, «¿Cuál es tu mejor apuesta?».

Reparto de las escenas del guion base: 01 → escenas 03, 04 y 05; 02 → 06, 07 y 08; 03 → 09, 10 y 11; 04 → 12, 13 y 14.
Solo se partieron bloques enteros en escenas atómicas: el texto del guion base no cambia (salvo el gancho y el cierre).

Ejemplos que se fijan aquí y vuelven en el resto del capítulo: el dado (apuestas 3 y 4 → 19/6 ≈ 3,17; 1 → 9,17; 3,5 → 2,92), la parábola de las apuestas (escenas 08 y 11) y las llamadas de la centralita (0 · 1 · 2 · 10 con 0,4 · 0,3 · 0,2 · 0,1; media 1,7, mediana 1, moda 0), que vuelven en el E5.

---

# Escena 01 — Gancho

**Capítulo YouTube:** Un número que el dado no saca

## Narración

<!-- b1 -->
Voy a tirar un dado y tú tienes que adivinar qué número sale. Y la mejor apuesta es tres coma cinco, pero un dado no puede sacar este número nunca.

- «tirar un dado» → `dado`: un dado grande en el centro
- «adivinar qué número sale» → `adivinar`: un «?» ámbar sobre el dado
- «la mejor apuesta» → `mejor`: el dado sube y aparece la regla del uno al seis
- «tres coma cinco» → `tres5`: «3,5» entra con rebote en ámbar, entre el tres y el cuatro
- «sacar este número nunca» → `nunca`: una cruz roja sobre el «3,5»

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** ¿Cuál es tu mejor apuesta?

## Narración

<!-- b1 -->
¿Cuál es tu mejor apuesta?

- «¿Cuál es» → `t1`: «¿Cuál es tu» entra con rebote
- «mejor apuesta?» → `t2`: «mejor apuesta?» entra debajo, con la etiqueta «Capítulo 8 · Estimación»

---

# Escena 03 — AdivinarUnNumero

**Capítulo YouTube:** Estimar: apostar un número
**Objetivo:** plantear el problema: antes de tirar el dado, hay que decir un número y equivocarse lo menos posible.

## Narración

<!-- b1 -->
En el primer capítulo dijimos que esta materia hace dos cosas con el azar, que son estimar y detectar. Empezamos por estimar, y con el caso más sencillo posible. Voy a tirar un dado, pero antes de que lo tire tienes que decirme un número, y quiero que te equivoques lo menos posible. ¿Qué número dices?

- «primer capítulo» → `primero`: arriba, la etiqueta «Capítulo 7 · Modelos probabilísticos»
- «estimar y detectar» → `dos`: dos casillas lado a lado: «Estimar» en ámbar y «Detectar» en azul
- «Empezamos por estimar» → `estimar`: «Detectar» se apaga y «Estimar» queda grande
- «el caso más sencillo posible» → `sencillo`: corte; «Estimar» queda como etiqueta pequeña arriba
- «Voy a tirar un dado» → `tirar`: un dado en el centro que cambia de cara
- «antes de que lo tire» → `antes`: el dado se queda quieto con un «?» sobre él
- «tienes que decirme un número» → `numero`: una burbuja de pensamiento con un «?» a la izquierda
- «te equivoques lo menos posible» → `menos`: una diana pequeña con el centro marcado
- «¿Qué número dices?» → `pregunta`: «¿Qué número dices?» en ámbar

---

# Escena 04 — EstimarEsApostar

**Capítulo YouTube:** Estimar aquí no es lo de Estadística
**Objetivo:** distinguir esta estimación de la de Probabilidad y Estadística: aquí la distribución es conocida y lo que falta es el valor que saldrá.

## Narración

<!-- b1 -->
Ojo, que estimar aquí no es lo mismo que en Probabilidad y Estadística. Allí no conocías la distribución y la aproximabas con una muestra, es decir, estimabas la media de una población a partir de unos cuantos datos. Aquí, en cambio, la distribución la conocemos entera. Lo que no sabemos es qué valor saldrá esta vez, así que hay que apostar por uno.

- «Probabilidad y Estadística» → `pye`: una tarjeta gris «Probabilidad y Estadística»
- «no conocías la distribución» → `nodist`: dentro, una campana punteada con interrogantes
- «con una muestra» → `muestra`: caen unos puntos de muestra sobre la campana
- «la media de una población» → `media`: una flecha de los puntos a «μ = ?»
- «a partir de unos cuantos datos» → `pocos`: la tarjeta se tacha en rojo
- «Aquí, en cambio» → `aqui`: tarjeta nueva en ámbar con las seis barras del dado, todas iguales
- «conocemos entera» → `entera`: sobre cada barra aparece «1/6»
- «qué valor saldrá esta vez» → `valor`: sobre las barras, un «?»
- «hay que apostar por uno» → `apostar`: una flecha ámbar baja a una barra, «Apuesta»

---

# Escena 05 — MedirElError

**Capítulo YouTube:** Medir el error: el cuadrado
**Objetivo:** elegir cómo medir lo mal que lo hacemos: error con signo, por qué se cancelan, y el error cuadrático medio.

## Narración

<!-- b1 -->
Para elegir la mejor apuesta hace falta medir cuánto nos equivocamos. El error es lo que sale menos lo que dijimos. Así, si apuestas tres y sale cinco, el error es dos, y si sale uno, el error es menos dos. Podríamos promediar los errores, pero entonces los positivos y los negativos se cancelarían, y un error enorme hacia arriba taparía otro enorme hacia abajo.

- «medir cuánto nos equivocamos» → `medir`: «¿Cuánto nos equivocamos?» arriba
- «lo que sale menos lo que dijimos» → `formula`: «Error = Sale − Dijimos» con «Sale» en azul y «Dijimos» en ámbar
- «si apuestas tres» → `apuestas3`: una recta del uno al seis con una marca ámbar en el tres
- «sale cinco» → `sale5`: un punto azul en el cinco y una flecha del tres al cinco
- «el error es dos» → `mas2`: «+2» sobre la flecha
- «si sale uno» → `sale1`: un punto azul en el uno y una flecha del tres al uno
- «menos dos» → `menos2`: «−2» sobre la flecha
- «Podríamos promediar los errores» → `promediar`: «(+2) + (−2)» aparece abajo
- «los positivos y los negativos» → `positivos`: los dos errores, «+2» y «−2», se resaltan
- «se cancelarían» → `cancelan`: «= 0» en rojo
- «un error enorme hacia arriba» → `enorme`: aparecen «+100» a la derecha y «−100» a la izquierda
- «taparía otro enorme hacia abajo» → `tapa`: un «0» rojo encima de los dos

<!-- b2 -->
La solución es elevar el error al cuadrado antes de promediar. Un cuadrado nunca es negativo, así que ya nada se cancela. Además, castiga más los errores grandes, porque equivocarse por dos cuesta cuatro, y equivocarse por tres cuesta nueve. La media de ese cuadrado se llama error cuadrático medio, y la mejor apuesta será la que lo haga lo más pequeño posible.

- «elevar el error al cuadrado» → `cuadrado`: «(+2)²» y «(−2)²» aparecen
- «Un cuadrado» → `uncuad`: los dos cuadrados se resaltan
- «nunca es negativo» → `positivo`: ambos pasan a «4» y «4» en verde
- «nada se cancela» → `sumacuatro`: «4 + 4 = 8» con un tilde verde
- «castiga más los errores grandes» → `castiga`: una tabla «Error → Coste»
- «equivocarse por dos cuesta cuatro» → `dos4`: fila «2 → 4»
- «equivocarse por tres cuesta nueve» → `tres9`: fila «3 → 9», y «1 → 1» encima
- «La media de ese cuadrado» → `lamedia`: la tabla se aparta y entra «Media del cuadrado»
- «error cuadrático medio» → `ecm`: «E[(Y − ŷ)²]» se construye pieza a pieza, con «Error cuadrático medio» debajo
- «lo más pequeño posible» → `pequeno`: una flecha hacia abajo en verde junto a la fórmula

<!-- b3 -->
La apuesta se escribe con un sombrero. Así, i griega sombrero es lo que adivinamos de i griega, que es lo que sale. El sombrero se queda para todo el curso, así que cada vez que lo veas, significa estimación. Y ahora, a probar apuestas con el dado.

- «se escribe con un sombrero» → `sombrero`: «ŷ» grande en ámbar
- «lo que adivinamos» → `adivinamos`: «ŷ = lo que adivinamos» en ámbar
- «de i griega» → `sobrey`: «Y» en azul junto a «ŷ», con «Lo que sale»
- «todo el curso» → `curso`: «Todo el curso» arriba a la derecha
- «cada vez que lo veas» → `veas`: el sombrero se ilumina
- «significa estimación» → `estimacion`: «Sombrero = estimación» en ámbar
- «a probar apuestas con el dado» → `probar`: aparece el dado

---

# Escena 06 — ApostarTres

**Capítulo YouTube:** Probar apuestas: el tres y el cuatro
**Objetivo:** calcular a mano el error cuadrático medio de apostar tres, cuatro y uno.

## Narración

<!-- b1 -->
Probemos a apostar tres. Si sale uno, el error es menos dos, y su cuadrado es cuatro. Si sale dos, el cuadrado es uno, y si sale tres, es cero. Con el cuatro vuelve a ser uno, con el cinco es cuatro, y con el seis es nueve. Cada cara tiene probabilidad un sexto, así que el error cuadrático medio es la suma, que da diecinueve, dividida entre seis, o sea, tres coma uno siete.

- «Probemos a apostar tres» → `apuesta3`: las seis caras sobre la regla y una marca ámbar «Apuesta 3»
- «Si sale uno» → `sale1`: la cara del uno se ilumina
- «su cuadrado es cuatro» → `c4`: «4» bajo el uno
- «Si sale dos» → `sale2`: la cara del dos se ilumina
- «el cuadrado es uno» → `c1`: «1» bajo el dos
- «si sale tres, es cero» → `c0`: «0» bajo el tres, en verde
- «Con el cuatro vuelve a ser uno» → `c1b`: «1» bajo el cuatro
- «con el cinco es cuatro» → `c4b`: «4» bajo el cinco
- «con el seis es nueve» → `c9`: «9» bajo el seis
- «probabilidad un sexto» → `sexto`: «1/6» sobre cada cara
- «la suma, que da diecinueve» → `suma`: «4 + 1 + 0 + 1 + 4 + 9 = 19»
- «dividida entre seis» → `div`: «19 / 6»
- «tres coma uno siete» → `res`: «≈ 3,17» en ámbar

<!-- b2 -->
Ahora apostemos cuatro. Las cuentas son las mismas, pero al revés, porque el seis queda a dos y el uno queda a tres. Vuelve a dar diecinueve sextos, que son tres coma uno siete, así que hay empate. Y si apostamos uno, el uno sale gratis, pero el seis cuesta veinticinco, y el error medio sube a nueve coma uno siete. Apostar a un extremo es mala idea.

- «Ahora apostemos cuatro» → `apuesta4`: la marca pasa al cuatro y los cuadrados cambian a «9 · 4 · 1 · 0 · 1 · 4»
- «Las cuentas son las mismas» → `mismas`: los seis cuadrados nuevos se resaltan
- «el seis queda a dos» → `seis`: una flecha del cuatro al seis con «2»
- «el uno queda a tres» → `uno`: una flecha del cuatro al uno con «3»
- «diecinueve sextos» → `d196`: «19/6»
- «tres coma uno siete» → `res4`: «≈ 3,17»
- «empate» → `empate`: «3,17 = 3,17» y «Empate» entra con rebote
- «si apostamos uno» → `apuesta1`: la marca pasa al uno y los cuadrados cambian a «0 · 1 · 4 · 9 · 16 · 25»
- «el uno sale gratis» → `gratis`: el «0» en verde
- «el seis cuesta veinticinco» → `cuesta`: el «25» en rojo
- «nueve coma uno siete» → `res1`: «≈ 9,17» en rojo
- «mala idea» → `mala`: una cruz roja sobre la marca del uno

---

# Escena 07 — ApostarEnMedio

**Capítulo YouTube:** La apuesta del medio: tres coma cinco
**Objetivo:** probar la apuesta 3,5 y ver que gana a todas las anteriores.

## Narración

<!-- b1 -->
Si tres y cuatro empatan, quizá lo mejor esté en medio. Piénsalo un momento antes de seguir. Apostemos tres coma cinco. Ahora los cuadrados son seis coma veinticinco, dos coma veinticinco y cero coma veinticinco, y cada uno sale dos veces. Suman diecisiete coma cinco, y entre seis son dos coma nueve dos. Es más bajo que todos los anteriores.

- «tres y cuatro empatan» → `empatan`: las caras sobre la regla, con «3» y «4» enmarcados y «=» entre ellos
- «quizá lo mejor esté en medio» → `medio`: un «?» ámbar entre el tres y el cuatro
- «Piénsalo un momento» → `piensa`: un reloj de arena y «Piénsalo»
- «Apostemos tres coma cinco» → `apuesta35`: la marca ámbar se coloca en el 3,5
- «seis coma veinticinco» → `c625`: «6,25» bajo el uno y el seis
- «dos coma veinticinco» → `c225`: «2,25» bajo el dos y el cinco
- «cero coma veinticinco» → `c025`: «0,25» bajo el tres y el cuatro
- «cada uno sale dos veces» → `dosveces`: los seis cuadrados se resaltan, de dos en dos
- «Suman diecisiete coma cinco» → `suman`: «= 17,5»
- «entre seis» → `entre6`: «17,5 / 6»
- «dos coma nueve dos» → `res`: «≈ 2,92» en verde
- «más bajo que todos los anteriores» → `bajo`: una tabla «Apuesta 1 → 9,17 · 3 y 4 → 3,17 · 3,5 → 2,92», con el 2,92 en verde

---

# Escena 08 — LaParabola

**Capítulo YouTube:** La parábola de las apuestas
**Objetivo:** dibujar apuesta contra error y ver la parábola con el fondo en la media y el suelo en la varianza.

## Narración

<!-- b1 -->
Pongamos los resultados en un dibujo. En el eje horizontal se encuentra la apuesta, y en el eje vertical, el error cuadrático medio. Los puntos forman una parábola, una curva en forma de U, y su punto más bajo está justo en tres coma cinco. Y tres coma cinco es la media del dado, que calculamos en el capítulo siete.

- «en un dibujo» → `dibujo`: aparecen los ejes
- «el eje horizontal» → `horiz`: «Apuesta» bajo el eje horizontal
- «el eje vertical» → `vert`: «Error cuadrático medio» junto al eje vertical
- «Los puntos» → `puntos`: caen los puntos de apuesta 1, 3, 4 y 3,5
- «una curva en forma de U» → `u`: se traza la parábola
- «su punto más bajo» → `bajo`: el vértice se marca en verde
- «justo en tres coma cinco» → `tres5`: una línea punteada hasta el eje con «3,5»
- «es la media del dado» → `media`: «Media = 3,5» en ámbar
- «capítulo siete» → `capsiete`: «Capítulo 7» en pequeño bajo la media

<!-- b2 -->
Y aquí está la sorpresa, y es que la mejor apuesta es un número que el dado no saca nunca. No buscamos acertar, sino equivocarnos lo menos posible en promedio. Y el error que queda en el fondo, dos coma nueve dos, también te sonará, porque es la varianza del dado. ¿Casualidad? Vamos a demostrar que no.

- «la sorpresa» → `sorpresa`: las seis caras del dado aparecen abajo y el 3,5 queda en medio, sin cara
- «no saca nunca» → `nunca`: una cruz roja sobre el «3,5» entre las caras
- «No buscamos acertar» → `acertar`: «Acertar» en gris, tachado
- «equivocarnos lo menos posible en promedio» → `promedio`: «Equivocarse poco, en promedio» en verde
- «el error que queda en el fondo» → `fondo`: una línea horizontal desde el vértice hasta el eje vertical con «2,92»
- «también te sonará» → `sonara`: «¿Te suena?» a la derecha
- «es la varianza del dado» → `varianza`: «Varianza del dado = 2,92» en ámbar
- «¿Casualidad?» → `casualidad`: «¿Casualidad?» entra con rebote
- «demostrar que no» → `demostrar`: «¿Casualidad?» se tacha y queda «Lo demostramos»

---

# Escena 09 — SumarYRestar

**Capítulo YouTube:** Demostración: sumar y restar la media
**Objetivo:** abrir la demostración para cualquier variable: sumar y restar la media parte el error en dos trozos.

## Narración

<!-- b1 -->
Hagámoslo en general, para cualquier variable i griega de media mu y varianza sigma cuadrado. Queremos el número i griega sombrero que haga más pequeña la media de i griega menos i griega sombrero, al cuadrado. El truco consiste en sumar y restar la media dentro del paréntesis. No cambia nada, pero parte el error en dos trozos.

- «en general» → `general`: una caja azul «Y» en el centro
- «de media mu» → `mu`: «μ» junto a la caja, en ámbar
- «varianza sigma cuadrado» → `sigma`: «σ²» bajo la caja
- «Queremos el número» → `quiero`: «ŷ» grande en ámbar bajo la caja
- «haga más pequeña la media de» → `media`: arriba aparecen los corchetes «E[ ]»
- «i griega menos i griega sombrero» → `resta`: dentro, «Y − ŷ»
- «al cuadrado» → `cuad`: el «²» del paréntesis
- «sumar y restar la media» → `sumar`: «− μ + μ» en ámbar sobre el paréntesis
- «No cambia nada» → `nada`: «− μ + μ = 0» a un lado
- «en dos trozos» → `trozos`: debajo, «Y − ŷ = (Y − μ) + (μ − ŷ)» con cada trozo de su color

<!-- b2 -->
El primer trozo es i griega menos mu, esto es: cuánto se aparta la variable de su media. El segundo es mu menos i griega sombrero, o sea: cuánto se aparta nuestra apuesta de la media. Elevamos al cuadrado la suma de los dos, resolvemos el cuadrado de un binomio: el primero al cuadrado, más dos veces el producto, más el segundo al cuadrado.

- «El primer trozo» → `primero`: el primer trozo se enmarca en azul
- «cuánto se aparta la variable» → `apartay`: una recta con «Y» y «μ» y una flecha entre ellos
- «El segundo es» → `segundo`: el segundo trozo se enmarca en ámbar
- «cuánto se aparta nuestra apuesta» → `apartaapuesta`: en la recta, «ŷ» y una flecha hasta «μ»
- «Elevamos al cuadrado la suma» → `elevamos`: sube el paréntesis «(A + B)²»
- «cuadrado de un binomio» → `abc`: «(a + b)² = a² + 2ab + b²» en pequeño
- «el primero al cuadrado» → `p1`: debajo, «(Y − μ)²» en azul
- «dos veces el producto» → `p2`: «+ 2(Y − μ)(μ − ŷ)» en rojo
- «el segundo al cuadrado» → `p3`: «+ (μ − ŷ)²» en ámbar

---

# Escena 10 — TomarMedias

**Capítulo YouTube:** Demostración: tomar medias
**Objetivo:** tomar la media de cada término: la varianza, el término cruzado que desaparece y el cuadrado fijo.

## Narración

<!-- b1 -->
Ahora tomamos la media de cada término y, por linealidad, sumamos los resultados. La media del primero es la varianza. En el término cruzado, mu menos i griega sombrero es un número fijo, así que sale fuera, y lo que queda dentro es la media de i griega menos mu, que es cero. El término cruzado desaparece. Y el último es un número fijo al cuadrado, así que se queda como está.

- «tomamos la media de cada término» → `media`: la fila de tres términos con «E[ ]» alrededor de cada uno
- «por linealidad» → `lineal`: «Linealidad» en pequeño con un tilde
- «La media del primero es la varianza» → `varianza`: el primer término se convierte en «σ²», en azul
- «En el término cruzado» → `cruzado`: el término cruzado se enmarca en rojo
- «es un número fijo, así que sale fuera» → `fijo`: del término cruzado sale «(μ − ŷ)» hacia el exterior de «E[ ]»
- «la media de i griega menos mu» → `quedadentro`: queda «E[Y − μ]» dentro
- «que es cero» → `cero`: «= 0» en verde
- «El término cruzado desaparece» → `desaparece`: el término cruzado se tacha y se desvanece
- «el último es un número fijo» → `ultimo`: el tercer término se enmarca
- «se queda como está» → `queda`: un tilde verde junto a él

<!-- b2 -->
Y este es el resultado. El error cuadrático medio es la varianza, más la distancia entre la apuesta y la media, al cuadrado.

- «el resultado» → `resultado`: corte; entra una caja con «E[(Y − ŷ)²]»
- «la varianza» → `sigma2`: «= σ²» entra en azul
- «la distancia entre la apuesta y la media» → `distancia`: «+ (μ − ŷ)²» entra en ámbar
- «al cuadrado» → `alcuadrado`: la caja se enmarca en verde

---

# Escena 11 — SueloYMulta

**Capítulo YouTube:** Un suelo y una multa
**Objetivo:** leer el resultado como un suelo más una multa; concluir que la mejor apuesta es la media y el error que queda es la varianza; comprobarlo con el dado.

## Narración

<!-- b1 -->
El primer término no depende de lo que apuestes, así que es un suelo que no puedes perforar. El segundo es una multa que nunca es negativa y que vale cero solo si apuestas la media. Así que la mejor apuesta es la media, y el error que queda es la varianza.

- «El primer término» → `primer`: el «σ²» del resultado se ilumina en azul
- «no depende de lo que apuestes» → `nodepende`: bajo él, «ŷ» tachado en gris
- «un suelo que no puedes perforar» → `suelo`: en la parábola, una línea gris horizontal en 2,92 con «Suelo»
- «El segundo es una multa» → `multa`: el «(μ − ŷ)²» se ilumina en ámbar y un segmento rojo vertical une el suelo con la curva
- «nunca es negativa» → `positiva`: «≥ 0» junto al segmento
- «vale cero solo si apuestas la media» → `cero`: el segmento se encoge a cero cuando el punto llega al fondo
- «la mejor apuesta es la media» → `mejor`: «ŷ = μ» en ámbar
- «el error que queda es la varianza» → `error`: «Error = σ²» en ámbar

<!-- b2 -->
Comprobémoslo con el dado. Si apostamos tres, tenemos la varianza, dos coma nueve dos, más tres coma cinco menos tres, al cuadrado, que es cero coma veinticinco. Da tres coma uno siete, lo mismo que con la cuenta larga. Y de aquí sale una lectura que usaremos mucho. La varianza es la incertidumbre que queda cuando ya has hecho lo mejor que podías sin mirar nada más.

- «Comprobémoslo con el dado» → `dado`: corte; un dado pequeño y «Apuesta 3»
- «Si apostamos tres» → `apostamos3`: «Apuesta 3» se resalta
- «la varianza, dos coma nueve dos» → `v`: «2,92 +» en azul
- «tres coma cinco menos tres» → `m`: «(3,5 − 3)²» en ámbar
- «cero coma veinticinco» → `c`: «= 2,92 + 0,25»
- «Da tres coma uno siete» → `r`: «= 3,17»
- «lo mismo que con la cuenta larga» → `larga`: un tilde verde y «Igual que la cuenta larga»
- «una lectura que usaremos mucho» → `lectura`: la fila se aparta y entra «Varianza = lo que queda»
- «la incertidumbre que queda» → `incert`: «Lo que queda» se resalta
- «cuando ya has hecho lo mejor que podías» → `mejorque`: un tilde verde junto a «Mejor apuesta»
- «sin mirar nada más» → `nada`: un ojo tachado y «Incertidumbre»

---

# Escena 12 — LasLlamadas

**Capítulo YouTube:** Otra forma de medir: las llamadas
**Objetivo:** presentar el ejemplo asimétrico (llamadas a una centralita) y calcular la media con el error cuadrático.

## Narración

<!-- b1 -->
¿Por qué el cuadrado y no otra forma de medir el error? Porque es una elección, y cada elección da otra respuesta. Veámoslo con un ejemplo. Cuentas las llamadas que entran en una centralita en un minuto. Entran cero llamadas el cuarenta por ciento de las veces, una llamada el treinta, dos el veinte, y diez de golpe el diez por ciento restante.

- «¿Por qué el cuadrado» → `porque`: «¿Por qué el cuadrado?» arriba
- «otra forma de medir el error» → `otra`: aparecen tres casillas vacías en fila
- «es una elección» → `eleccion`: tres casillas vacías en fila
- «cada elección da otra respuesta» → `respuesta`: las casillas se rellenan con interrogantes distintos
- «Veámoslo con un ejemplo» → `ejemplo`: corte; una centralita con teléfonos
- «Cuentas las llamadas» → `cuentas`: «Llamadas por minuto» y el eje del cero al diez
- «en un minuto» → `minuto`: un reloj junto a «Llamadas por minuto»
- «cero llamadas el cuarenta por ciento» → `ninguna`: barra alta en el cero con «40 %»
- «una llamada el treinta» → `una`: barra en el uno con «30 %»
- «dos el veinte» → `dos`: barra en el dos con «20 %»
- «diez de golpe» → `diez`: barra pequeña en el diez
- «el diez por ciento restante» → `restante`: «10 %» sobre ella

<!-- b2 -->
Con el error al cuadrado ya lo sabemos, la mejor apuesta es la media. Para calcularla hacemos cero por cero coma cuatro, más uno por cero coma tres, más dos por cero coma dos, más diez por cero coma uno, y sale uno coma siete llamadas. Ese diez raro tira de la media hacia arriba, porque el cuadrado castiga mucho fallar por nueve.

- «Con el error al cuadrado» → `cuadrado`: la etiqueta «Error al cuadrado»
- «la mejor apuesta es la media» → `media`: «Media» en ámbar
- «cero por cero coma cuatro» → `c0`: «0 · 0,4»
- «más uno por cero coma tres» → `c1`: «+ 1 · 0,3»
- «más dos por cero coma dos» → `c2`: «+ 2 · 0,2»
- «más diez por cero coma uno» → `c10`: «+ 10 · 0,1»
- «uno coma siete llamadas» → `res`: «= 1,7» y un triángulo ámbar en el 1,7 del eje
- «Ese diez raro tira de la media» → `tira`: una flecha roja desde la barra del diez que tira del triángulo
- «castiga mucho fallar por nueve» → `castiga`: una llave entre el 1 y el 10 con «9»

---

# Escena 13 — MedianaYModa

**Capítulo YouTube:** La mediana y la moda
**Objetivo:** medir el error por su tamaño (mediana, 1,5 contra 1,78) y por acertar o fallar (moda, 40 %).

## Narración

<!-- b1 -->
Si en cambio el error se mide por su tamaño, sin cuadrado, la mejor apuesta es la mediana, que es el valor que deja la mitad de la probabilidad a cada lado. Aquí es una llamada. Si apostamos uno, el error medio es uno coma cinco, pero si apostamos uno coma siete, sube a uno coma siete ocho. Con esta medida, el diez raro pesa mucho menos.

- «se mide por su tamaño» → `tamano`: «|Error|» en grande
- «sin cuadrado» → `sin`: el «²» de la etiqueta anterior tachado
- «la mejor apuesta es la mediana» → `mediana`: «Mediana» en verde
- «deja la mitad de la probabilidad a cada lado» → `mitad`: llaves a los lados del uno con «0,4» y «0,3», cada una por debajo de la mitad
- «Aquí es una llamada» → `llamada`: un triángulo verde en el uno con «Mediana = 1»
- «Si apostamos uno» → `apostando1`: el triángulo ámbar en el uno
- «uno coma cinco» → `e15`: «Error medio = 1,5» en verde
- «si apostamos uno coma siete» → `a17`: el triángulo ámbar pasa al 1,7
- «uno coma siete ocho» → `e178`: «Error medio = 1,78» en rojo
- «el diez raro pesa mucho menos» → `pesa`: la barra del diez se atenúa

<!-- b2 -->
Y si lo único que cuenta es acertar o fallar, sin importar por cuánto, la mejor apuesta es el valor más probable, que es la moda, o sea, cero llamadas, que acierta el cuarenta por ciento de las veces. Apostar uno coma siete no acertaría nunca. Son tres formas de medir el error y tres respuestas, que son la media, la mediana y la moda.

- «acertar o fallar» → `acertar`: «¿Acierto o fallo?» en ámbar
- «sin importar por cuánto» → `importar`: una flecha corta y una larga, las dos con «Fallo»
- «el valor más probable» → `probable`: la barra más alta se ilumina
- «cero llamadas» → `cero`: el triángulo pasa al cero
- «el cuarenta por ciento de las veces» → `cuarenta`: «Acierta el 40 %» en verde
- «Apostar uno coma siete» → `apostar17`: el triángulo ámbar pasa al 1,7
- «no acertaría nunca» → `nunca`: el triángulo en el 1,7 con «0 %» en rojo
- «tres formas de medir el error» → `tres`: tres casillas en fila
- «la media» → `t_media`: «Cuadrado → media»
- «la mediana» → `t_mediana`: «Tamaño → mediana»
- «la moda» → `t_moda`: «Acierto → moda»

---

# Escena 14 — TresRespuestas

**Capítulo YouTube:** Por qué nos quedamos con el cuadrado
**Objetivo:** justificar el cuadrado, sembrar el capítulo 9 (acertar o fallar es decidir) y abrir la pregunta del próximo episodio.

## Narración

<!-- b1 -->
La última, acertar o fallar, es la que se usa para decidir, y la retomaremos en el capítulo siguiente. En este nos quedamos con el cuadrado, por tres motivos. Castiga los errores grandes, las cuentas salen limpias y, como veremos, convierte la estimación en geometría. Pero antes viene lo interesante. ¿Qué pasa cuando, además, puedes mirar algo?

- «La última, acertar o fallar» → `ultima`: tres casillas; la tercera, «Acierto → moda», se resalta
- «para decidir» → `decidir`: «Decidir» en cian junto a la tercera
- «el capítulo siguiente» → `siguiente`: «Capítulo 9» sobre la tercera casilla
- «nos quedamos con el cuadrado» → `cuadrado`: la primera casilla se agranda y se enmarca en verde
- «tres motivos» → `motivos`: la casilla pasa a un lado y aparece una lista vacía de tres números
- «Castiga los errores grandes» → `castiga`: «1 · Castiga lo grande»
- «las cuentas salen limpias» → `limpias`: «2 · Cuentas limpias»
- «convierte la estimación en geometría» → `geometria`: «3 · Geometría» con un triángulo rectángulo
- «Pero antes» → `antes`: la lista se aparta
- «puedes mirar algo» → `mirar`: un ojo grande y un «?» ámbar

---

# Escena 15 — Cierre

**Capítulo YouTube:** Lo que viene: mirar el dato

## Narración

<!-- b1 -->
Resumamos. Sin mirar nada, la mejor apuesta es la media, y el error que queda es la varianza. Y si cambias la forma de medir el error, cambia la respuesta, y sale la mediana, o la moda. Pero ¿y si, antes de apostar, pudieras ver algo? Eso lo veremos en el próximo episodio, que se titula Lo que el dato te cuenta.

- «Resumamos» → `resumen`: corte; «Resumen» en ámbar
- «la mejor apuesta es la media» → `media`: la parábola del dado con el fondo en «3,5»
- «el error que queda es la varianza» → `varianza`: la línea del suelo en «2,92 = varianza»
- «cambias la forma de medir el error» → `cambias`: aparecen las tres casillas «Cuadrado · Tamaño · Acierto»
- «la mediana, o la moda» → `otras`: las flechas a «Mediana» y «Moda»
- «antes de apostar» → `antes`: corte; el dado con «?»
- «pudieras ver algo» → `ver`: un ojo junto al dado
- «el próximo episodio» → `proximo`: una tarjeta «Episodio 2»
- «Lo que el dato te cuenta» → `titulo`: el título entra con rebote en ámbar
