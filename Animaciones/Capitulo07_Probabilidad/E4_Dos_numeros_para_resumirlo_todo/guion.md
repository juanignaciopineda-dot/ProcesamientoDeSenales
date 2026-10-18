# Episodio 4 — Dos números para resumirlo todo

Capítulo 7 (Modelos probabilísticos), episodio 4 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 13 a 16), más un gancho y un cierre nuevos.

**Estado:** **Subido a YouTube en privado** el 17/10/2026: render final 1080p60 de 9:04, con título, descripción con `capitulos.txt`, subtítulos `.srt`, categoría Educación y «no es para niños» (https://youtu.be/tkpbJTO0JOo). Lo subió el usuario sin el visto bueno que figuraba pendiente en este estado (texto ⭐ / mp4 / pronunciaciones): la aprobación queda en su revisión antes de publicarlo. Residuos limpiados el 17/10/2026: se regenera con `python render.py <carpeta> --calidad qh`. **Falta**: publicarlo (lo hace el usuario).

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Un dado nunca saca tres coma cinco…».
- ⭐ Escena 18 (cierre): resume media, varianza, Chebyshev y grandes números, plantea la pregunta de las dos variables y anuncia E5, «Dos variables a la vez».
- ⭐ Retoque en la escena 17 (bloque b2): se quitó la última frase del guion base de la escena 16 («Y ahora pasamos a lo más interesante…»), que ahora vive en el cierre.

---

# Escena 01 — Gancho

**Capítulo YouTube:** El dado que nunca saca 3,5

## Narración

<!-- b1 -->
Un dado nunca saca tres coma cinco. Y aun así, si lo tiras mil veces, el promedio acaba clavado en tres coma cinco. Con dos números, la media y la varianza, vamos a ver por qué.

- «Un dado nunca saca» → `dado`: un dado rueda y se queda en un cinco
- «tres coma cinco» → `valor`: las seis caras con una cruz sobre «3,5»
- «lo tiras mil veces» → `mil`: una curva de promedio se dibuja y salta al principio
- «clavado en tres coma cinco» → `clavado`: la curva se aplana sobre la línea «3,5»
- «dos números» → `dos`: aparecen «μ» y «σ²» en grande
- «la media y la varianza» → `nombres`: «media» bajo μ y «varianza» bajo σ²

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Dos números para resumirlo todo

## Narración

<!-- b1 -->
Dos números para resumirlo todo.

- «Dos números» → `t1`: «Dos números» entra con rebote
- «para resumirlo todo» → `t2`: «para resumirlo todo» entra debajo, con la etiqueta «Capítulo 7 · Modelos probabilísticos»

---

# Escena 03 — Esperanza

**Capítulo YouTube:** La media o esperanza

## Narración

<!-- b1 -->
Tira un dado muchas veces y ve haciendo el promedio de lo que sale. Al principio salta, pero enseguida se estabiliza alrededor de un número: tres coma cinco. Fíjate en que el dado nunca saca tres coma cinco. Es el valor alrededor del cual se reparten los resultados. Se llama media, o esperanza.

- «Tira un dado muchas veces» → `dado`: un dado rueda y deja una columna de resultados: 4, 2, 6, 1, 5
- «haciendo el promedio» → `promedio`: debajo, un contador «promedio» que se actualiza con cada tirada
- «Al principio salta» → `salta`: la curva del promedio da saltos grandes
- «se estabiliza alrededor de un número» → `estabiliza`: la curva se aplana hacia una línea punteada
- «tres coma cinco» → `tres_cinco`: la línea se rotula «3,5»
- «el dado nunca saca» → `nunca`: las seis caras, con una cruz sobre el hueco de «3,5»
- «alrededor del cual se reparten» → `reparten`: los resultados se agrupan en torno a la línea
- «Se llama media» → `media`: «media» entra con rebote
- «o esperanza» → `esperanza`: «esperanza» entra al lado

---

# Escena 04 — CuentaDeLaEsperanza

**Capítulo YouTube:** Calcular la esperanza del dado

## Narración

<!-- b1 -->
Se puede calcular sin tirar el dado. Cada valor se multiplica por su probabilidad, y se suma todo. Uno por un sexto, más dos por un sexto, y así hasta seis por un sexto. Uno más dos más tres más cuatro más cinco más seis son veintiuno, y veintiuno entre seis da tres coma cinco. En general, la esperanza es la suma de cada valor por su probabilidad.

- «sin tirar el dado» → `sin_tirar`: el dado se aparta con un tachón
- «Cada valor» → `valor`: seis casillas con los valores 1 a 6
- «por su probabilidad» → `prob`: bajo cada casilla aparece «1/6»
- «y se suma todo» → `suma`: aparecen los signos «+» entre los términos
- «Uno por un sexto» → `t1`: se forma el primer término «1 · 1/6»
- «más dos por un sexto» → `t2`: «+ 2 · 1/6»
- «hasta seis por un sexto» → `t6`: «+ … + 6 · 1/6»
- «Uno más dos más tres» → `enteros`: los numeradores se juntan en «1 + 2 + 3 + 4 + 5 + 6»
- «son veintiuno» → `veintiuno`: «21/6»
- «da tres coma cinco» → `resultado`: «= 3,5» en verde
- «En general» → `general`: aparece «E[X] =» como cabecera
- «la suma de cada valor» → `sumatoria`: aparece «Σ x»
- «por su probabilidad» → `prob2`: se completa «E[X] = Σ x · P(X = x)»

---

# Escena 05 — PuntoDeEquilibrio

**Capítulo YouTube:** La esperanza es un punto de equilibrio

## Narración

<!-- b1 -->
Tiene una imagen física muy clara. Pon seis pesas iguales sobre una regla, en las posiciones del uno al seis. ¿Dónde tienes que apoyarla para que no caiga? En tres coma cinco. La esperanza es el punto de equilibrio de la distribución. Si la variable es continua, se recorta la densidad como una placa, y el punto de equilibrio se calcula con una integral: equis por la densidad, sumado a lo largo de todo el eje.

- «una imagen física» → `imagen`: aparece una regla horizontal sobre un filo
- «seis pesas iguales» → `pesas`: seis pesas caen sobre las posiciones 1 a 6
- «en las posiciones del uno al seis» → `posiciones`: bajo la regla se marcan las posiciones 1, 2, 3, 4, 5, 6
- «¿Dónde tienes que apoyarla» → `donde`: el filo se desliza y la regla se inclina a un lado y al otro
- «En tres coma cinco» → `equilibrio`: el filo se detiene en 3,5 y la regla queda horizontal, en verde
- «el punto de equilibrio de la distribución» → `punto`: «μ» sobre el filo
- «Si la variable es continua» → `continua`: sobre la regla aparece una densidad
- «se recorta la densidad como una placa» → `placa`: la curva se vuelve una placa sólida sobre el filo
- «con una integral» → `integral`: aparece «∫» con una flecha a «suma de rectángulos finos»
- «equis por la densidad» → `xf`: «x · f_X(x)» entra a la derecha del signo
- «a lo largo de todo el eje» → `eje`: se completan «dx» y los límites, «E[X] = ∫ x f_X(x) dx»

---

# Escena 06 — Linealidad

**Capítulo YouTube:** La esperanza es lineal

## Narración

<!-- b1 -->
Se escribe E de equis, o mu. Y tiene una propiedad que usaremos sin parar, la media  es lineal. Si multiplicas la variable por un número, la esperanza se multiplica por ese número. Si le sumas algo, la esperanza sube lo mismo. La esperanza de dos veces el dado más uno es dos por tres coma cinco más uno: ocho. Y la esperanza de una suma es la suma de las esperanzas, siempre.

- «Se escribe E de equis» → `escribe`: aparece «E[X]»
- «o mu» → `mu`: «= μ»
- «es lineal» → `lineal`: «lineal» entra con rebote
- «multiplicas la variable por un número» → `mult`: «E[aX] = a E[X]»
- «se multiplica por ese número» → `se_mult`: el factor «a» se resalta en los dos lados de la fórmula
- «Si le sumas algo» → `sumas`: «E[X + b] = E[X] + b»
- «dos veces el dado más uno» → `dado21`: «E[2X + 1]»
- «dos por tres coma cinco más uno» → `cuenta`: «= 2 · 3,5 + 1»
- «ocho» → `ocho`: «= 8» en verde
- «la esperanza de una suma» → `esp_suma`: «E[X + Y]»
- «es la suma de las esperanzas» → `suma_esp`: «= E[X] + E[Y]»
- «siempre» → `siempre`: sello «siempre» junto a la fórmula

---

# Escena 07 — LaMediaNoBasta

**Capítulo YouTube:** La media no lo cuenta todo

## Narración

<!-- b1 -->
Pero la media no lo cuenta todo. Un dado y una variable que siempre vale tres coma cinco tienen la misma media, y no se parecen en nada: una salta de uno a seis y la otra no se mueve. Nos falta un segundo número que diga cuánto se aleja la variable de su media.

- «la media no lo cuenta todo» → `no_todo`: «μ = 3,5» en grande, con un «¿todo?» tachado
- «Un dado» → `dado`: a la izquierda, seis barras iguales para las caras
- «una variable que siempre vale» → `cte`: a la derecha, una sola barra alta
- «tres coma cinco» → `siempre`: la barra única se coloca en 3,5
- «la misma media» → `misma`: una línea en 3,5 cruza ambos dibujos, con un «=» entre ellos
- «no se parecen en nada» → `distintas`: el «=» se vuelve «≠»
- «salta de uno a seis» → `salta`: un punto salta entre 1 y 6 en el dibujo de la izquierda
- «la otra no se mueve» → `quieta`: el punto de la derecha queda quieto en 3,5
- «un segundo número» → `segundo`: aparece una casilla «?» al lado de «μ»
- «se aleja la variable de su media» → `aleja`: flechas dobles desde la media hacia los lados

---

# Escena 08 — Distancias

**Capítulo YouTube:** Por qué la varianza va al cuadrado

## Narración

<!-- b1 -->
Queremos medir cuánto se aleja una variable de su media. La primera idea es promediar las distancias a la media. Con el dado, las distancias a tres coma cinco son menos dos coma cinco, menos uno coma cinco, menos cero coma cinco, y las mismas en positivo. Súmalas: dan cero. Las de un lado cancelan a las del otro. Así no sirve.

- «Queremos medir cuánto se aleja» → `medir`: dos campanas con la misma media, una estrecha y otra ancha
- «una variable de su media» → `variable`: sobre las campanas aparece «μ» en el centro común
- «promediar las distancias a la media» → `distancias`: sobre las seis caras, flechas desde 3,5 hasta cada una
- «Con el dado» → `con_dado`: las campanas se apartan y entran las seis caras del dado con el filo en 3,5
- «tres coma cinco son» → `a_35`: una flecha de 3,5 a cada cara, empezando por la 1
- «menos dos coma cinco» → `d1`: etiqueta «−2,5» en la cara 1
- «menos uno coma cinco» → `d2`: «−1,5»
- «menos cero coma cinco» → `d3`: «−0,5»
- «las mismas en positivo» → `positivo`: «0,5 · 1,5 · 2,5» a la derecha
- «Súmalas» → `sumalas`: las seis distancias se juntan en una suma
- «dan cero» → `cero`: «= 0»
- «cancelan a las del otro» → `cancelan`: las flechas de la izquierda y las de la derecha se anulan
- «Así no sirve» → `no_sirve`: tachón rojo sobre la suma

<!-- b2 -->
La solución es elevar cada distancia al cuadrado, para que todas sean positivas. Seis coma veinticinco, dos coma veinticinco, cero coma veinticinco, y lo mismo por el otro lado. Su promedio es dos coma noventa y dos. Eso es la varianza: la esperanza de la distancia a la media, al cuadrado. Se escribe sigma cuadrado.

- «elevar cada distancia al cuadrado» → `cuadrado`: cada distancia se vuelve un cuadrado de ese lado
- «todas sean positivas» → `positivas`: todas pasan a verde
- «Seis coma veinticinco» → `c1`: «6,25»
- «dos coma veinticinco» → `c2`: «2,25»
- «cero coma veinticinco» → `c3`: «0,25»
- «el otro lado» → `otro`: los mismos tres valores aparecen espejados
- «Su promedio» → `prom`: una barra que promedia los seis
- «dos coma noventa y dos» → `p292`: «≈ 2,92»
- «Eso es la varianza» → `varianza`: «varianza» entra con rebote
- «la esperanza de la distancia a la media» → `formula`: «E[(X − μ)²]» se construye por piezas
- «sigma cuadrado» → `sigma2`: «= σ²»

---

# Escena 09 — DesviacionEstandar

**Capítulo YouTube:** La desviación estándar

## Narración

<!-- b1 -->
El problema de la varianza es que está en unidades al cuadrado, por ejemplo: si la variable son voltios, la varianza son voltios al cuadrado. Por eso se usa también su raíz, sigma, que se llama desviación estándar y vuelve a estar en las unidades de la variable. Para el dado, uno coma siete uno: los resultados se alejan de tres coma cinco, típicamente, algo menos de dos puntos.

- «unidades al cuadrado» → `unidades`: «σ²» con la etiqueta «unidades²»
- «la variable son voltios» → `voltios`: «X» con la unidad «V»
- «voltios al cuadrado» → `v2`: la varianza aparece con «V²» en ámbar
- «su raíz» → `raiz`: «√σ² = σ»
- «desviación estándar» → `desv`: «desviación estándar» entra con rebote
- «unidades de la variable» → `vuelve`: «V» vuelve en verde junto a σ
- «uno coma siete uno» → `d171`: «σ ≈ 1,71»
- «se alejan de tres coma cinco» → `alejan`: flechas de ±σ alrededor de 3,5 sobre las caras
- «algo menos de dos puntos» → `menos2`: banda sombreada de 1,79 a 5,21

---

# Escena 10 — FormulaPractica

**Capítulo YouTube:** La fórmula cómoda de la varianza

## Narración

<!-- b1 -->
Hay una forma más cómoda de calcularla, y vale la pena ver de dónde sale. Primero desarrollamos el cuadrado: equis al cuadrado, menos dos mu equis, más mu al cuadrado. Después usamos la linealidad para repartir la esperanza en cada término. Como la esperanza de equis es mu, el término del medio queda menos dos mu al cuadrado. Y al juntar todo: la varianza es la esperanza de equis al cuadrado menos mu al cuadrado.

- «una forma más cómoda» → `comoda`: renglón 1, «σ² = E[(X − μ)²]»
- «de dónde sale» → `donde_sale`: una lupa se posa sobre el renglón 1
- «desarrollamos el cuadrado» → `desarrollo`: renglón 2, «E[X² − 2μX + μ²]», con la regla «desarrollar» al margen
- «equis al cuadrado» → `x2`: se resalta «X²»
- «menos dos mu equis» → `dos_mu`: se resalta «−2μX»
- «más mu al cuadrado» → `mu2`: se resalta «μ²»
- «la linealidad» → `linealidad`: renglón 3, «E[X²] − 2μ E[X] + μ²», con la regla «linealidad» al margen
- «la esperanza de equis es mu» → `ex_mu`: se resalta «E[X] = μ»
- «menos dos mu al cuadrado» → `menos2mu2`: renglón 4, «E[X²] − 2μ² + μ²»
- «al juntar todo» → `juntar`: «−2μ² + μ² = −μ²»
- «la varianza es la esperanza de equis al cuadrado» → `result`: aparece «σ² = E[X²]»
- «menos mu al cuadrado» → `menos_mu2`: se completa «− μ²», en ámbar

---

# Escena 11 — ComprobacionConElDado

**Capítulo YouTube:** Comprobación con el dado

## Narración

<!-- b1 -->
Comprobémoslo con el dado. La esperanza del cuadrado es uno más cuatro más nueve más dieciséis más veinticinco más treinta y seis, entre seis: quince coma diecisiete. Menos tres coma cinco al cuadrado, doce coma veinticinco. Da dos coma noventa y dos, lo mismo que antes. Y un resultado que usaremos: para una uniforme entre a y entre b, la varianza es el ancho al cuadrado dividido entre doce.

- «Comprobémoslo con el dado» → `dado`: el dado y la fórmula «σ² = E[X²] − μ²»
- «uno más cuatro más nueve» → `cuad`: «1 + 4 + 9 + 16 + 25 + 36» se escribe término a término
- «treinta y seis» → `t36`: la suma se cierra con «= 91»
- «entre seis» → `entre6`: «/ 6»
- «quince coma diecisiete» → `q1517`: «= 15,17»
- «tres coma cinco al cuadrado» → `mu2`: «3,5²»
- «doce coma veinticinco» → `doce25`: «= 12,25»
- «dos coma noventa y dos» → `r292`: «15,17 − 12,25 = 2,92», en verde
- «lo mismo que antes» → `igual`: «2,92» de la escena de las distancias, con un «=» entre ambos
- «una uniforme entre a y entre b» → `unif`: un rectángulo de densidad entre a y b
- «el ancho al cuadrado» → `ancho`: flecha «b − a» y su cuadrado
- «entre doce» → `doce`: «σ² = (b − a)²/12»

---

# Escena 12 — Markov

**Capítulo YouTube:** La desigualdad de Markov

## Narración

<!-- b1 -->
Empecemos con una pregunta de sueldos. En una empresa el sueldo medio es de mil euros, y nadie cobra un sueldo negativo. ¿Qué fracción de la plantilla puede cobrar diez mil euros o más? Piénsalo así: si el veinte por ciento cobrara diez mil, solo ellos ya harían que la media fuera de dos mil. Como mucho, puede ser un diez por ciento.

- «pregunta de sueldos» → `sueldos`: una fila de diez personas
- «el sueldo medio es de mil euros» → `media`: «media: 1.000 €»
- «nadie cobra un sueldo negativo» → `negativo`: «sueldo ≥ 0»
- «¿Qué fracción de la plantilla» → `fraccion`: «¿qué fracción?»
- «diez mil euros o más» → `diezmil`: «≥ 10.000 €»
- «si el veinte por ciento» → `veinte`: dos de las diez personas se ponen en rojo
- «cobrara diez mil» → `cobrara`: sobre cada una, «10.000 €»
- «la media fuera de dos mil» → `dosmil`: «media ≥ 2.000 €» choca con «1.000 €» y se tacha
- «Como mucho» → `mucho`: queda una sola persona en rojo
- «un diez por ciento» → `diez`: «≤ 10 %»

<!-- b2 -->
Eso es la desigualdad de Markov. Si una variable nunca es negativa, la probabilidad de que supere un valor a es, como mucho, su media dividida entre a. Una variable que no puede ser negativa y que tiene una media pequeña no puede tomar valores grandes muy a menudo.

- «la desigualdad de Markov» → `markov`: «Markov» entra con rebote
- «nunca es negativa» → `nunca_neg`: «Y ≥ 0»
- «la probabilidad de que supere un valor a» → `supere`: «P(Y ≥ a)»
- «como mucho» → `como_mucho`: «≤»
- «su media dividida entre a» → `cociente`: «E[Y] / a»
- «no puede ser negativa» → `no_puede`: la barra de «Y» muestra el cero y nada a su izquierda
- «una media pequeña» → `pequena`: el valor de «E[Y]» se encoge
- «valores grandes muy a menudo» → `a_menudo`: la barra de probabilidad se achica

---

# Escena 13 — Chebyshev

**Capítulo YouTube:** La desigualdad de Chebyshev

## Narración

<!-- b1 -->
Chebyshev tuvo una idea muy simple: aplicar Markov a la distancia a la media, elevada al cuadrado. Esa cantidad nunca es negativa, y su media es, por definición, la varianza. Con eso, la cuenta sale en dos líneas: la probabilidad de alejarse de la media más de alfa desviaciones estándar es, como mucho, uno dividido entre alfa al cuadrado.

- «Chebyshev tuvo una idea» → `chebyshev`: «Chebyshev» entra con rebote
- «aplicar Markov» → `aplicar`: «Markov» con una flecha hacia una nueva variable
- «la distancia a la media, elevada al cuadrado» → `y_def`: «Y = (X − μ)²»
- «nunca es negativa» → `y_pos`: «Y ≥ 0» en verde
- «su media es, por definición, la varianza» → `y_media`: «E[Y] = σ²»
- «la cuenta sale en dos líneas» → `dos_lineas`: dos renglones: «P(Y ≥ α²σ²) ≤ σ² / α²σ²»
- «alejarse de la media más de alfa desviaciones estándar» → `alejarse`: «P(|X − μ| ≥ ασ)»
- «uno dividido entre alfa al cuadrado» → `uno_alfa2`: «≤ 1/α²» en ámbar

<!-- b2 -->
Con alfa igual a dos: como mucho el veinticinco por ciento de las veces la variable cae a más de dos sigmas de su media. Con alfa igual a tres, como mucho un once por ciento. Y esto vale para cualquier distribución, tenga la forma que tenga. Solo hacen falta la media y la varianza.

- «Con alfa igual a dos» → `a2`: fila «α = 2» de una tabla
- «el veinticinco por ciento» → `p25`: «≤ 25 %» y una curva con las colas a ±2σ sombreadas
- «a más de dos sigmas de su media» → `dos_sigmas`: las flechas de ±2σ desde μ y las colas sombreadas
- «Con alfa igual a tres» → `a3`: fila «α = 3»
- «un once por ciento» → `p11`: «≤ 11 %» con las colas a ±3σ
- «cualquier distribución» → `cualquiera`: tres formas distintas (campana, uniforme, dos picos) con las mismas bandas
- «Solo hacen falta» → `solo`: las formas se apagan y quedan «μ» y «σ²»

---

# Escena 14 — ChebyshevEsFloja

**Capítulo YouTube:** Chebyshev vale para todo, y por eso es flojo

## Narración

<!-- b1 -->
El precio de valer para todo es que suele quedarse corta. Para una uniforme entre cero y uno, con alfa igual a uno coma cinco, Chebyshev asegura que la probabilidad no pasa de cero coma cuatro cuatro. La real es cero coma uno tres: más de tres veces menos. Pero justamente porque no necesita conocer la curva, sirve para demostrar algo que usamos todos los días sin pensarlo: que promediar funciona.

- «El precio de valer para todo» → `precio`: una balanza con «vale para todo» de un lado
- «quedarse corta» → `corta`: del otro lado, «ajustada» sube: la cota queda holgada
- «una uniforme entre cero y uno» → `unif`: un rectángulo de 0 a 1, con su media en 0,5
- «alfa igual a uno coma cinco» → `a15`: bandas a 1,5 σ de la media
- «cero coma cuatro cuatro» → `c044`: «cota: 0,44» como una barra ámbar
- «cero coma uno tres» → `r013`: las colas reales sombreadas, «real: 0,13» como una barra más corta
- «más de tres veces menos» → `tres_veces`: la barra real cabe más de tres veces en la cota
- «no necesita conocer la curva» → `sin_curva`: la curva se desvanece; la cota sigue en pie
- «sirve para demostrar algo» → `sirve`: la cota se queda sola y aparece un signo de interrogación
- «todos los días» → `dias`: un reloj de promediar: un termómetro, una balanza, un voltímetro
- «que promediar funciona» → `promediar`: «promediar funciona» entra con rebote

---

# Escena 15 — ElPromedioSeAsienta

**Capítulo YouTube:** Por qué promediar funciona

## Narración

<!-- b1 -->
Mide la misma tensión con ruido muchas veces y haz el promedio. Con dos medidas, el promedio todavía salta bastante. Con cien, se mueve poco. Con diez mil, apenas tiembla alrededor del valor verdadero. Todos lo hemos visto. Vamos a demostrarlo, con lo que ya tenemos.

- «la misma tensión con ruido» → `tension`: una línea con el valor verdadero y medidas ruidosas a su alrededor
- «muchas veces» → `veces`: caen más puntos de medida
- «haz el promedio» → `promedio`: se dibuja la curva del promedio
- «Con dos medidas» → `dos`: tres corridas con n = 2, muy separadas
- «Con cien» → `cien`: las corridas se acercan
- «Con diez mil» → `diezmil`: las corridas casi no se distinguen de la línea
- «alrededor del valor verdadero» → `verdadero`: la línea «valor verdadero» se resalta
- «Todos lo hemos visto» → `visto`: un guiño visual: las tres corridas pegadas
- «Vamos a demostrarlo» → `demostrar`: «demostrarlo» entra con rebote

---

# Escena 16 — VarianzaDelPromedio

**Capítulo YouTube:** La varianza del promedio

## Narración

<!-- b1 -->
Primero, cuánto se dispersa el promedio. Si las medidas son independientes, la varianza de su suma es la suma de sus varianzas. Esto lo demostraremos dentro de dos episodios; de momento, créetelo. Con n medidas de varianza sigma cuadrado, la suma tiene varianza n por sigma cuadrado.

- «cuánto se dispersa el promedio» → `dispersa`: «Var(X̄ₙ) = ?»
- «independientes» → `indep`: casillas X₁, X₂, …, Xₙ sin conexiones entre ellas
- «la varianza de su suma» → `var_suma`: «Var(X₁ + … + Xₙ)»
- «la suma de sus varianzas» → `suma_var`: «= σ² + … + σ²»
- «dentro de dos episodios» → `dos_ep`: etiqueta «(lo demostramos en el episodio 6)»
- «créetelo» → `creetelo`: sello «de momento»
- «n medidas de varianza sigma cuadrado» → `n_medidas`: n casillas, cada una con «σ²»
- «n por sigma cuadrado» → `n_sigma2`: «= n σ²»

<!-- b2 -->
El promedio es la suma dividida entre n. Y cuando divides una variable entre un número, la varianza se divide entre ese número al cuadrado, porque la varianza mide distancias al cuadrado. Así que la varianza del promedio es n por sigma cuadrado dividido entre n al cuadrado: sigma cuadrado dividido entre n. Cuantas más medidas, menos se dispersa el promedio.

- «la suma dividida entre n» → `prom`: «X̄ₙ = (X₁ + … + Xₙ) / n»
- «divides una variable entre un número» → `divides`: «Var(X / c)»
- «se divide entre ese número al cuadrado» → `c2`: «= Var(X) / c²»
- «mide distancias al cuadrado» → `dist2`: una distancia y su cuadrado dibujados
- «n por sigma cuadrado dividido entre n al cuadrado» → `cociente`: «n σ² / n²»
- «sigma cuadrado dividido entre n» → `sn`: «= σ² / n» en ámbar
- «Cuantas más medidas» → `mas`: un contador n sube
- «menos se dispersa el promedio» → `menos`: la campana del promedio se angosta

---

# Escena 17 — GrandesNumeros

**Capítulo YouTube:** La ley de los grandes números

## Narración

<!-- b1 -->
Ahora le aplicamos Chebyshev al promedio. La probabilidad de que se aleje de la media verdadera más de una distancia épsilon, tan pequeña como quieras, es como mucho sigma cuadrado dividido entre n por épsilon al cuadrado. Y cuando n crece, eso se va a cero. Es la ley de los grandes números: el promedio acaba pegándose a la media.

- «le aplicamos Chebyshev al promedio» → `aplica`: «Chebyshev» se posa sobre «X̄ₙ»
- «se aleje de la media verdadera» → `aleje`: «P(|X̄ₙ − μ| ≥ ε)»
- «tan pequeña como quieras» → `epsilon`: una banda ε estrecha alrededor de μ
- «sigma cuadrado dividido entre n por épsilon al cuadrado» → `cota`: «≤ σ² / (n ε²)»
- «cuando n crece» → `crece`: el contador n sube
- «se va a cero» → `cero`: una flecha «→ 0» sobre la cota
- «la ley de los grandes números» → `ley`: título «ley de los grandes números»
- «pegándose a la media» → `pegado`: las corridas entran en la banda y se quedan

<!-- b2 -->
No hemos necesitado saber nada de la forma del ruido: solo su varianza. Esta idea volverá con fuerza cuando estudiemos señales que cambian en el tiempo, donde promediaremos a lo largo de una sola grabación.

- «la forma del ruido» → `forma`: tres curvas de ruido de formas distintas
- «solo su varianza» → `solo_var`: las formas se apagan y queda «σ²»
- «volverá con fuerza» → `volvera`: una flecha hacia «Capítulo 10»
- «señales que cambian en el tiempo» → `cambian`: una curva ruidosa en el tiempo
- «una sola grabación» → `grabacion`: sobre esa curva, una ventana que promedia a lo largo del tiempo

---

# Escena 18 — Cierre

**Capítulo YouTube:** Dos variables a la vez

## Narración

<!-- b1 -->
Dos números lo resumen casi todo: la media dice dónde está una variable, y la varianza, cuánto se aleja. Con ellas acotamos lo imposible con Chebyshev y entendimos por qué promediar funciona. Pero en señales nunca hay una sola variable. Está lo que se envió y lo que se recibió. ¿Qué podemos saber de una si conocemos la otra? En el próximo episodio: «Dos variables a la vez».

- «la media dice dónde está» → `media`: una campana con «μ» en su centro
- «la varianza, cuánto se aleja» → `varianza`: la campana se ensancha con «σ²»
- «acotamos lo imposible con Chebyshev» → `cheb`: «≤ 1/α²» reaparece
- «por qué promediar funciona» → `prom`: «σ²/n» reaparece
- «nunca hay una sola variable» → `una`: la variable se duplica en dos
- «lo que se envió» → `envio`: «X» con un sobre que sale
- «lo que se recibió» → `recibio`: «Y» con un sobre que llega
- «¿Qué podemos saber de una» → `saber`: flecha doble entre X e Y con una interrogación
- «En el próximo episodio» → `proximo`: un reloj de pausa y la flecha doble X–Y se queda en primer plano
- «Dos variables a la vez» → `titulo`: entra el título del siguiente episodio con rebote
