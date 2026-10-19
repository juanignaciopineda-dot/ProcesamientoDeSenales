# Episodio 3 — ¿Y si solo vale una recta?

Capítulo 8 (Estimación), episodio 3 de 5. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 09 a 12), más un gancho y un cierre nuevos.

**Estado:** **Subido a YouTube y publicado** (19/10/2026): render final 1080p60 de 9:38, título buscable, descripción con el capítulo del libro y `capitulos.txt`, subtítulos, categoría Educación (https://youtu.be/ufFp3Hqbl-4). Residuos limpiados; la caché de voz original está en `media/voiceovers/`: se rehace igual con `python rehacer.py Capitulo08_Estimacion E3`.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Un termómetro marca veintitrés grados y, aun así, la mejor apuesta para la temperatura real no es veintitrés, sino veintidós coma cuatro. ¿Por qué? Con una recta y unos pocos números te lo explico.»
- ⭐ Escena 14 (cierre): resumen y anuncia E4 por su título, «La sombra de una flecha».
- ⭐ Retoque en la escena 13 (bloque b5): se quita la última frase del guion base («Y para entender por qué todo esto funciona, toca volver a las flechas del capítulo siete.»); esa pregunta pasa al cierre.

Nota para el episodio anterior: el cierre del E2 («Lo que el dato te cuenta») tiene que anunciar este título, «¿Y si solo vale una recta?».

Reparto de las escenas del guion base: 09 → escenas 03 y 04; 10 → escenas 05, 06 y 07; 11 → escenas 08, 09 y 10; 12 → escenas 11, 12 y 13.
Solo se partieron bloques enteros en escenas atómicas: el texto del guion base no cambia (salvo el retoque de arriba).

Ejemplos que vuelven con el **mismo dibujo y los mismos números**: la carpa (E3 escenas 03 y 04, y de nuevo mini en la 11), el termómetro (media 20, varianza 4, ruido 1, lee 23; h = 0,8, error 0,8, apuesta 22,4; parábola 4 − 8h + 5h²). Letras: `x` la lectura (cian), `y` la temperatura (azul), `v` el ruido (magenta), `ŷ` la apuesta (ámbar), `J` el error (rojo).

---

# Escena 01 — Gancho

**Capítulo YouTube:** Veintitrés grados, pero apuesta 22,4

## Narración

<!-- b1 -->
Un termómetro marca veintitrés grados y, aun así, la mejor apuesta para la temperatura real no es veintitrés, sino veintidós coma cuatro. ¿Por qué? Con una recta y unos pocos números te lo explico.

- «Un termómetro marca veintitrés grados» → `marca`: entra el termómetro y, a su lado, «23» en cian
- «la mejor apuesta» → `apuesta`: aparece «Mejor apuesta» en ámbar
- «no es veintitrés» → `no23`: el «23» se tacha en rojo
- «sino veintidós coma cuatro» → `s224`: «22,4» grande, en ámbar
- «¿Por qué?» → `porque`: «¿Por qué?» entra con rebote
- «una recta» → `recta`: corte; una nube de puntos con una recta ámbar que la atraviesa
- «unos pocos números» → `numeros`: tres fichas: «Medias», «Varianzas», «Covarianza»

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** ¿Y si solo vale una recta?

## Narración

<!-- b1 -->
¿Y si solo vale una recta?

- «¿Y si solo» → `t1`: «¿Y si solo» entra con rebote
- «vale una recta?» → `t2`: «vale una recta?» entra debajo, con la etiqueta «Capítulo 8 · Estimación»

---

# Escena 03 — LaCarpa

**Capítulo YouTube:** La media condicional es una curva

## Narración

<!-- b1 -->
La media condicional es la mejor apuesta, pero tiene un problema, y es que para calcularla hay que conocer la distribución conjunta entera. Y a veces la regla que sale es una curva. Mira este ejemplo. Un punto cae al azar, con la misma probabilidad en cualquier sitio, dentro de un triángulo con forma de carpa, cuya base va de cero a dos y cuyo pico, en equis igual a uno, tiene altura uno.

- «La media condicional» → `mc`: «E[y | x]» en ámbar a la izquierda, con «Media condicional» debajo
- «un problema» → `pega`: «Un problema» en rojo, bajo la fórmula
- «la distribución conjunta entera» → `conjunta`: a la derecha, una nube de puntos con «Distribución conjunta entera»
- «Y a veces la regla» → `regla`: sobre la nube aparece «La regla» en ámbar
- «una curva» → `curva`: una curva ámbar atraviesa la nube
- «Mira este ejemplo» → `ejemplo`: corte; los ejes de la carpa (x, y)
- «Un punto cae al azar» → `punto`: caen cuatro o cinco puntos en sitios cualquiera, uno tras otro
- «con la misma probabilidad en cualquier sitio» → `mismo`: siguen cayendo puntos, repartidos parejos por el cuadro
- «un triángulo con forma de carpa» → `triangulo`: se dibuja el triángulo y los puntos caen dentro
- «cuya base va de cero a dos» → `base`: se resaltan el 0 y el 2 del eje horizontal
- «cuyo pico, en equis igual a uno» → `pico`: un punto marca el pico sobre el 1 del eje horizontal
- «tiene altura uno» → `alto`: aparece el «1» del eje vertical y una línea guía hasta el pico

<!-- b2 -->
Observamos su posición horizontal, equis, y queremos adivinar la vertical, i griega. Corta la carpa en equis igual a cero coma cinco y verás que la rebanada va de cero a cero coma cinco. Como el punto cae con la misma probabilidad a cualquier altura, la mejor apuesta es el centro, cero coma veinticinco. En equis igual a uno, la rebanada llega hasta uno, por lo que la mejor apuesta es cero coma cinco.

- «Observamos su posición horizontal» → `obs`: se resalta el eje x, con «Lo que observamos»
- «queremos adivinar la vertical» → `adivinar`: se resalta el eje y, con «Lo que adivinamos»
- «Corta la carpa en equis igual a cero coma cinco» → `corte`: una línea cian vertical en x = 0,5, con «0,5» en el eje
- «la rebanada va de cero a cero coma cinco» → `rebanada`: el trozo de la línea dentro del triángulo se pone azul y grueso
- «Como el punto cae» → `como`: un punto cae sobre la rebanada
- «a cualquier altura» → `altura`: puntos caen a lo largo de la rebanada, a cualquier altura
- «la mejor apuesta es el centro» → `centro`: un punto ámbar en el medio de la rebanada
- «cero coma veinticinco» → `c025`: el rótulo «0,25» junto al punto
- «En equis igual a uno» → `x1`: la primera línea se apaga y entra otra en x = 1
- «la rebanada llega hasta uno» → `reb1`: la rebanada azul de 0 a 1
- «apuesta es cero coma cinco» → `a05`: punto ámbar en 0,5 con su rótulo

---

# Escena 04 — LaCurvaGanaLaRectaSeConforma

**Capítulo YouTube:** La curva gana, la recta se conforma

## Narración

<!-- b1 -->
Uniendo los centros de todas las rebanadas sale otra carpa, de la mitad de altura. Esa es la media condicional, y no es una recta, porque sube y luego baja. Cada rebanada es una uniforme, con varianza igual a su ancho al cuadrado entre doce, y el promedio de esas varianzas, que es una integral, da uno sobre veinticuatro, que es aproximadamente cero coma cero cuatro dos.

- «Uniendo los centros» → `unir`: la rebanada barre la carpa de izquierda a derecha y deja una estela de centros ámbar
- «otra carpa, de la mitad de altura» → `carpa2`: queda dibujada la carpa ámbar, con el pico en 0,5
- «Esa es la media condicional» → `esa`: sobre la carpa ámbar, «E[y | x]»
- «y no es una recta» → `norecta`: «No es una recta» junto a la carpa
- «sube y luego baja» → `sube`: una flecha corta sube en la izquierda y otra baja en la derecha
- «Cada rebanada es una uniforme» → `unif`: una rebanada azul con «Uniforme» al lado
- «su ancho al cuadrado entre doce» → `var`: «σ² = a² / 12», con una llave que marca el ancho «a» de la rebanada
- «el promedio de esas varianzas» → `prom`: se barre de nuevo la carpa; «Promedio de σ²»
- «una integral» → `integral`: el signo «∫» sobre el promedio
- «uno sobre veinticuatro» → `v24`: «= 1/24» en rojo
- «cero coma cero cuatro dos» → `v042`: «≈ 0,042» en rojo, con «Error» delante

<!-- b2 -->
Ahora, la covarianza. En la mitad izquierda, cuando equis sube, i griega tiende a subir; en la derecha, tiende a bajar. Como en la parábola del capítulo siete, las dos mitades se cancelan y la covarianza es cero. Si solo pudiéramos usar una recta, la mejor sería horizontal, a la altura de la media, es decir, un tercio. Y su error, un dieciochoavo, que son cero coma cero cinco seis, un tercio más.

- «Ahora, la covarianza» → `cov`: la carpa ámbar se atenúa; entra «σ_xy» arriba
- «En la mitad izquierda» → `izq`: la mitad izquierda del triángulo se sombrea
- «tiende a subir» → `sube2`: una flecha ámbar sube sobre esa mitad
- «en la derecha» → `der`: la mitad derecha se sombrea
- «tiende a bajar» → `baja`: una flecha ámbar baja sobre esa mitad
- «Como en la parábola del capítulo siete» → `parab7`: en una esquina, una parábola pequeña con «Capítulo 7»
- «se cancelan» → `cancel`: las dos flechas se juntan en el centro y aparece «σ_xy = 0»
- «Si solo pudiéramos usar una recta» → `recta`: la palabra «Recta» aparece junto a un ícono de regla
- «horizontal, a la altura de la media» → `horiz`: se dibuja una recta ámbar horizontal
- «un tercio» → `tercio`: la recta se sitúa en 1/3 y aparece «1/3»
- «un dieciochoavo» → `e18`: «Error = 1/18» en rojo
- «cero coma cero cinco seis» → `e056`: «≈ 0,056»

<!-- b3 -->
La curva gana. Pero para dibujarla hace falta toda la distribución, y en la práctica casi nunca la tenemos, porque lo que tenemos son medias, varianzas y covarianzas. Así que hagamos un trato. Nos conformamos con la mejor recta, que solo pide esos pocos números, a cambio de perder algo cuando la relación es curva. Es el estimador lineal óptimo.

- «La curva gana» → `gana`: corte; dos barras rojas, «Curva 0,042» y «Recta 0,056», con un tilde verde sobre la curva
- «toda la distribución» → `toda`: «Toda la distribución» con una cruz roja
- «casi nunca la tenemos» → `nunca`: la caja tachada «Toda la distribución» destella en rojo
- «medias, varianzas y covarianzas» → `pocos`: tres fichas «Medias», «Varianzas», «Covarianzas», con un tilde verde
- «hagamos un trato» → `trato`: «Un trato» entra con rebote
- «Nos conformamos con la mejor recta» → `conformamos`: «Solo rectas» junto a un trazo recto
- «que solo pide esos pocos números» → `solopide`: las tres fichas de antes se resaltan, una tras otra
- «a cambio de perder algo» → `perder`: entre las dos barras aparece la diferencia, «+0,014», en rojo
- «el estimador lineal óptimo» → `lineal`: un sello «Estimador lineal óptimo» y, en pequeño, «LMMSE»

---

# Escena 05 — ElTermometro

**Capítulo YouTube:** El termómetro de la sala

## Narración

<!-- b1 -->
Probemos el trato con un ejemplo que nos acompañará mucho tiempo. La temperatura de una sala tiene una media de veinte grados y una varianza de cuatro, de modo que se aparta unos dos grados, arriba o abajo. La medimos con un termómetro que suma su propio ruido, de media cero y varianza uno, sin ninguna relación con la temperatura. El termómetro marca veintitrés y queremos responder a una pregunta. ¿Qué temperatura hace?

- «un ejemplo que nos acompañará mucho tiempo» → `ejemplo`: entra el termómetro, grande, a la izquierda
- «La temperatura de una sala» → `sala`: «Temperatura  y» en azul a la derecha
- «una media de veinte grados» → `media`: «μ = 20» junto a «y»
- «una varianza de cuatro» → `var`: «σ² = 4» junto a «y»
- «se aparta unos dos grados» → `dos`: una recta numérica de 16 a 24 con una banda azul de 18 a 22
- «arriba o abajo» → `arriba`: dos flechas cortas, una a cada lado del 20
- «un termómetro que suma su propio ruido» → `ruido`: «Ruido  v» en magenta
- «de media cero y varianza uno» → `r01`: «μ = 0 · σ² = 1» junto a «v»
- «sin ninguna relación con la temperatura» → `norel`: «Sin relación con y» y una barra que separa «v» de «y»
- «El termómetro marca veintitrés» → `m23`: «Lectura  x = y + v» en cian y «23» sobre el termómetro
- «y queremos» → `busca`: el «23» del termómetro se resalta
- «¿Qué temperatura hace?» → `que`: un «¿y = ?» grande en ámbar

<!-- b2 -->
Buscamos la apuesta entre las rectas de la forma hache por lo que marca el termómetro, más un número fijo, be. Empecemos por be. Sea cual sea hache, conviene que en promedio no nos desviemos, y eso fija be en veinte menos veinte hache. Así la recta queda veinte, más hache por lo que la lectura se aparta de veinte. Arrancamos de la media y corregimos.

- «hache por lo que marca el termómetro» → `hx`: «ŷ = h · x» se construye pieza a pieza
- «más un número fijo, be» → `b`: se añade «+ b»
- «Empecemos por be» → `emp`: «b» se resalta
- «Sea cual sea hache» → `sea`: «Para cualquier h» en ámbar
- «en promedio no nos desviemos» → `prom`: «E[ŷ] = E[y]», es decir «20h + b = 20»
- «veinte menos veinte hache» → `b20`: «b = 20 − 20h»
- «la recta queda veinte» → `queda`: «ŷ = 20 + h (x − 20)» sustituye a la anterior
- «más hache por lo que la lectura se aparta de veinte» → `aparta`: se enmarca «h (x − 20)», con «Lo que se aparta»
- «Arrancamos de la media» → `arranca`: «Media» bajo el «20»
- «y corregimos» → `corregimos`: «Corrección» bajo «h (x − 20)»

---

# Escena 06 — DosOpciones

**Capítulo YouTube:** Dos opciones extremas

## Narración

<!-- b1 -->
Queda elegir hache. Dos opciones extremas. Con hache igual a cero, ignoramos el termómetro y apostamos veinte, así que el error es la varianza de la temperatura, cuatro. Con hache igual a uno, nos lo creemos a ciegas y apostamos veintitrés, así que el error es el del ruido, uno. Mucho mejor. Pero, ¿y si lo mejor está entre medias?

- «Queda elegir hache» → `elegir`: «ŷ = 20 + h (x − 20)» con la h resaltada y un «?»
- «Dos opciones extremas» → `dos`: aparecen dos tarjetas vacías, una a cada lado
- «hache igual a cero» → `h0`: entra la tarjeta izquierda «h = 0»
- «ignoramos el termómetro» → `ign`: el termómetro de la tarjeta se tacha
- «apostamos veinte» → `a20`: «ŷ = 20»
- «la varianza de la temperatura, cuatro» → `e4`: una barra roja alta, «Error 4»
- «hache igual a uno» → `h1`: entra la tarjeta derecha «h = 1»
- «nos lo creemos a ciegas» → `ciegas`: el termómetro de la tarjeta se ilumina
- «apostamos veintitrés» → `a23`: «ŷ = 23»
- «el del ruido, uno» → `e1`: una barra roja baja, «Error 1»
- «Mucho mejor» → `mejor`: una flecha va de la barra de 4 a la de 1
- «¿y si lo mejor está entre medias?» → `entre`: entre las dos tarjetas aparece un «h = ?» y una barra que oscila

<!-- b2 -->
Calculemos el error para cualquier hache. Con todo centrado, es la media de la temperatura menos hache por la lectura, al cuadrado. Desarrollamos el cuadrado y tomamos la media de cada término. La de la temperatura al cuadrado es cuatro. La de la temperatura por la lectura también es cuatro, porque el ruido no tiene nada que ver con la temperatura. Y la de la lectura al cuadrado es cuatro más uno, es decir, cinco.

- «Con todo centrado» → `centrado`: corte; «Restamos 20 a todo»
- «es la media» → `jmedia`: «J(h) = E[ ]» entra
- «de la temperatura menos hache por la lectura» → `jdif`: «( y − h x )» dentro de la media
- «al cuadrado» → `jcuad`: el «²» entra en rojo
- «Desarrollamos el cuadrado» → `des`: «y² − 2h y x + h² x²»
- «tomamos la media de cada término» → `medias`: «E[y²] − 2h E[y x] + h² E[x²]»
- «La de la temperatura al cuadrado» → `yy`: se enmarca «E[y²]» y se escribe «E[y²] = 4»
- «La de la temperatura por la lectura» → `yx`: se enmarca «E[y x]»
- «también es cuatro» → `c4`: «E[y x] = 4»
- «porque el ruido no tiene nada que ver» → `norel`: «x = y + v» y «E[y v] = 0»
- «la de la lectura al cuadrado» → `xx`: se enmarca «E[x²]»
- «cuatro más uno, es decir, cinco» → `c5`: «E[x²] = 4 + 1 = 5»

---

# Escena 07 — LaParabolaDelError

**Capítulo YouTube:** La parábola del error

## Narración

<!-- b1 -->
El error queda cuatro, menos ocho hache, más cinco hache al cuadrado, que es otra parábola. Con hache igual a cero da cuatro; con hache igual a uno, uno. Y su punto más bajo, que enseguida calcularemos, está en hache igual a cero coma ocho, donde el error baja a cero coma ocho. La mejor apuesta no es veintitrés, sino veinte más cero coma ocho por tres, que da veintidós coma cuatro.

- «El error queda cuatro» → `j1`: «J(h) = 4»
- «menos ocho hache» → `j2`: «− 8h»
- «más cinco hache al cuadrado» → `j3`: «+ 5h²»
- «otra parábola» → `parabola`: los ejes y la parábola roja se dibujan
- «Con hache igual a cero da cuatro» → `p0`: un punto en h = 0, J = 4
- «con hache igual a uno, uno» → `p1`: un punto en h = 1, J = 1
- «su punto más bajo» → `bajo`: un punto recorre la parábola hasta el fondo
- «hache igual a cero coma ocho» → `h08`: guía vertical y «h = 0,8» bajo el eje
- «el error baja a cero coma ocho» → `j08`: guía horizontal y «J = 0,8»
- «no es veintitrés» → `no23`: «23» tachado
- «veinte más cero coma ocho por tres» → `cuenta`: «ŷ = 20 + 0,8 · 3»
- «veintidós coma cuatro» → `r224`: «22,4» en ámbar

---

# Escena 08 — LaPendiente

**Capítulo YouTube:** El fondo de una parábola

## Narración

<!-- b1 -->
¿Cómo se encuentra el punto más bajo de una parábola sin probar valores? Con la pendiente. En cada punto de una curva, la pendiente dice cuánto sube por cada paso hacia la derecha, y eso es la derivada. Bajando por la izquierda, la pendiente es negativa; subiendo por la derecha, positiva. Y en el fondo, justo entre las dos, es cero.

- «el punto más bajo de una parábola» → `bajo`: la parábola del error con su fondo marcado
- «sin probar valores» → `probar`: un punto salta de un valor a otro, y se tacha
- «Con la pendiente» → `pend`: una recta tangente aparece sobre la curva
- «En cada punto de una curva» → `cadapunto`: la tangente se desliza por la curva
- «cuánto sube por cada paso hacia la derecha» → `paso`: un escalón: un paso a la derecha y lo que sube
- «la derivada» → `deriv`: «Pendiente = derivada»
- «la pendiente es negativa» → `neg`: la tangente a la izquierda, inclinada hacia abajo, con «−» en rojo
- «positiva» → `pos`: la tangente a la derecha, inclinada hacia arriba, con «+» en verde
- «en el fondo» → `fondo`: la tangente se desliza hasta el fondo
- «es cero» → `cero`: la tangente queda horizontal, con «0»

<!-- b2 -->
La derivada de cuatro menos ocho hache más cinco hache al cuadrado es menos ocho más diez hache. Igualada a cero, hache vale ocho décimos, o sea, cero coma ocho. Y el error ahí es cuatro, menos seis coma cuatro, más tres coma dos, que da cero coma ocho. Ahora, lo mismo con letras, para cualquier pareja de variables.

- «La derivada de» → `dd`: «J(h) = 4 − 8h + 5h²» arriba
- «menos ocho más diez hache» → `d`: «J′(h) = −8 + 10h»
- «Igualada a cero» → `igual0`: «= 0»
- «ocho décimos» → `h810`: «h = 8/10»
- «Y el error ahí» → `eahi`: «J(0,8) = 4»
- «menos seis coma cuatro» → `c64`: «− 6,4»
- «más tres coma dos» → `c32`: «+ 3,2»
- «cero coma ocho. Ahora» → `r08`: «= 0,8» en rojo
- «lo mismo con letras» → `letras`: «Con letras» en ámbar

---

# Escena 09 — ConLetras

**Capítulo YouTube:** La mejor recta, con letras

## Narración

<!-- b1 -->
El error, centrado, es la varianza de i griega, menos dos hache por la covarianza, más hache al cuadrado por la varianza de equis. Su pendiente es menos dos veces la covarianza, más dos hache por la varianza de equis. Igualada a cero, hache es la covarianza dividida entre la varianza de equis. En el termómetro, cuatro entre cinco, es decir, cero coma ocho.

- «El error, centrado» → `j0`: «J(h) =» entra arriba
- «la varianza de i griega» → `sy`: «σ_y²» en azul
- «menos dos hache por la covarianza» → `cov`: «− 2h σ_xy»
- «más hache al cuadrado por la varianza de equis» → `sx`: «+ h² σ_x²» en cian
- «Su pendiente es» → `pend`: «J′(h) =» en la segunda fila
- «menos dos veces la covarianza» → `p1`: «− 2σ_xy»
- «más dos hache por la varianza de equis» → `p2`: «+ 2h σ_x²»
- «Igualada a cero» → `cero`: «= 0»
- «hache es la covarianza dividida entre la varianza de equis» → `h`: «h = σ_xy / σ_x²» en una caja
- «En el termómetro, cuatro entre cinco» → `term`: a la derecha «4 / 5» con los datos del termómetro
- «cero coma ocho» → `r08`: «= 0,8»

<!-- b2 -->
Así que la mejor recta se lee como la media de i griega, más la covarianza entre la varianza de equis, por lo que equis se aparta de su media. Y como la covarianza es rho por las dos desviaciones estándar, el factor también se escribe rho, por sigma de i griega, entre sigma de equis.

- «la media de i griega» → `mu`: «ŷ = μ_y»
- «más la covarianza entre la varianza de equis» → `fac`: «+ σ_xy / σ_x²»
- «por lo que equis se aparta de su media» → `xmu`: «(x − μ_x)»
- «la covarianza es rho por las dos desviaciones estándar» → `rho`: «σ_xy = ρ σ_x σ_y»
- «el factor también se escribe» → `fac2`: el factor se transforma en «ρ σ_y / σ_x»
- «sigma de i griega, entre sigma de equis» → `sigs`: se resaltan «σ_y» y «σ_x»

---

# Escena 10 — ElErrorDeLaRecta

**Capítulo YouTube:** El error: varianza por uno menos rho cuadrado

## Narración

<!-- b1 -->
Falta el error. Metiendo ese hache en la parábola, los dos últimos términos se juntan en menos la covarianza al cuadrado entre la varianza de equis. Sacando factor común la varianza de i griega, queda la varianza por uno menos rho al cuadrado. En el termómetro, rho al cuadrado es dieciséis entre veinte, cero coma ocho, y cuatro por cero coma dos da cero coma ocho. Coincide.

- «Falta el error» → `falta`: «J = σ_y² − 2h σ_xy + h² σ_x²»
- «Metiendo ese hache» → `meter`: debajo, la misma con h = σ_xy / σ_x²
- «los dos últimos términos» → `ultimos`: se enmarcan los dos últimos términos
- «menos la covarianza al cuadrado entre la varianza de equis» → `res`: «J = σ_y² − σ_xy² / σ_x²»
- «entre la varianza de equis» → `entre`: se resalta el denominador «σ_x²»
- «Sacando factor común la varianza de i griega» → `factor`: se enmarca «σ_y²»
- «uno menos rho al cuadrado» → `final`: «J = σ_y² (1 − ρ²)» en una caja roja
- «En el termómetro» → `term`: aparece la columna del termómetro
- «dieciséis entre veinte» → `d16`: «ρ² = 16/20 = 0,8»
- «cuatro por cero coma dos» → `cuenta`: «4 · 0,2 = 0,8»
- «Coincide» → `ok`: un tilde verde junto al 0,8 de la parábola

---

# Escena 11 — LeerLaRecta

**Capítulo YouTube:** Leer la recta: la media y rho

## Narración

<!-- b1 -->
Leamos la fórmula con calma, porque dice mucho. Arranca de la media de lo que quieres adivinar y corrige según cuánto se aparta el dato de la suya. El tamaño de la corrección depende de rho. Si rho vale cero, no corrige nada y la recta es horizontal, a la altura de la media. Es lo que le pasaba a la carpa.

- «Leamos la fórmula» → `formula`: «ŷ = μ_y + ρ (σ_y / σ_x) (x − μ_x)» arriba
- «Arranca de la media de lo que quieres adivinar» → `arranca`: se enmarca «μ_y»
- «cuánto se aparta el dato de la suya» → `aparta`: se enmarca «(x − μ_x)»
- «El tamaño de la corrección» → `tamano`: una llave bajo «ρ (σ_y / σ_x)», con «Tamaño de la corrección»
- «depende de rho» → `rho`: se enmarca «ρ»
- «Si rho vale cero» → `r0`: una nube de puntos sin relación, con «ρ = 0»
- «la recta es horizontal» → `horiz`: la recta ámbar queda plana, a la altura de la media
- «Es lo que le pasaba a la carpa» → `carpa`: una carpa en miniatura, con su recta plana

<!-- b2 -->
Si rho vale uno o menos uno, la nube es una recta exacta, y el error, la varianza por uno menos uno, es cero, así que el dato lo dice todo. Y entre medias, rho al cuadrado es la parte de la varianza que el dato consigue explicar. En el termómetro, un ochenta por ciento. El veinte por ciento restante, cero coma ocho de cuatro, se queda sin explicar.

- «Si rho vale uno» → `r1`: la nube se estira hasta ser una recta, «ρ = 1»
- «o menos uno» → `rm1`: la recta se invierte, «ρ = −1»
- «la varianza por uno menos uno» → `e0`: «σ_y² (1 − 1) = 0»
- «el dato lo dice todo» → `todo`: un tilde verde
- «rho al cuadrado es la parte de la varianza» → `r2`: corte; una barra de largo 4, «Varianza de y»
- «que el dato consigue explicar» → `explica`: la barra se divide en dos tramos
- «un ochenta por ciento» → `p80`: el tramo verde de 3,2, «Explicado 80 %»
- «El veinte por ciento restante» → `p20`: el tramo rojo de 0,8
- «cero coma ocho de cuatro» → `c08`: «0,8 de 4»
- «se queda sin explicar» → `sin`: «Sin explicar»

---

# Escena 12 — TiraHaciaLaMedia

**Capítulo YouTube:** Por qué la apuesta tira hacia la media

## Narración

<!-- b1 -->
Fíjate en el veintidós coma cuatro. El termómetro marcaba veintitrés, tres por encima de la media, y la apuesta solo sube dos coma cuatro. ¿Por qué no fiarse del todo? Porque una lectura alta puede venir de calor de verdad o de ruido hacia arriba. La fórmula reparte la diferencia, y por eso siempre tira un poco hacia la media.

- «Fíjate en el veintidós coma cuatro» → `a224`: una recta numérica de 18 a 24 con «20» (media), «22,4» (apuesta, ámbar) y «23» (lectura, cian)
- «El termómetro marcaba veintitrés» → `m23`: entra el «23» en cian sobre la recta numérica
- «tres por encima de la media» → `tres`: una llave del 20 al 23, «+3»
- «la apuesta solo sube dos coma cuatro» → `sube`: una llave del 20 al 22,4, «+2,4»
- «¿Por qué no fiarse del todo?» → `fiar`: un «¿Fiarse del todo?» en ámbar
- «Porque una lectura alta» → `alta`: se resalta el «23»
- «calor de verdad» → `calor`: un sol azul empuja hacia arriba
- «ruido hacia arriba» → `ruidoar`: una flecha magenta empuja hacia arriba
- «reparte la diferencia» → `reparte`: el hueco entre 22,4 y 23 se marca, «0,6»
- «tira un poco hacia la media» → `tira`: una flecha ámbar va de 23 hacia el 20

---

# Escena 13 — LaTrampa

**Capítulo YouTube:** La trampa: la recta al revés

## Narración

<!-- b1 -->
Ahora, una trampa. Cambiemos la pregunta y, sabiendo la temperatura de verdad, adivinemos qué marcará el termómetro. Si fuera la misma recta al revés, el factor sería uno entre cero coma ocho, es decir, uno coma veinticinco. Pero la fórmula dice covarianza, cuatro, entre la varianza de lo que observas, ahora la temperatura, cuatro. Uno. La apuesta es la temperatura misma, y tiene sentido, porque el ruido es igual de probable hacia arriba que hacia abajo.

- «una trampa» → `trampa`: «Trampa» en rojo
- «Cambiemos la pregunta» → `cambio`: «Antes: x → y» y «Ahora: y → x»
- «adivinemos qué marcará el termómetro» → `marca`: el termómetro con un «?» sobre la lectura
- «Si fuera la misma recta al revés» → `reves`: «x̂ = μ_x + ρ (σ_x / σ_y)(y − μ_y)» y flechas que intercambian x e y
- «el factor sería» → `sera`: se resalta «ρ σ_x / σ_y»
- «uno entre cero coma ocho» → `inv`: «1 / 0,8»
- «uno coma veinticinco» → `v125`: «= 1,25»
- «Pero la fórmula dice covarianza» → `forml`: «σ_xy / σ_y²» (ahora la varianza es la de y)
- «covarianza, cuatro,» → `cov4`: «4 / ...» el 4 de arriba en verde
- «la varianza de lo que observas» → `ent`: se señala el denominador
- «ahora la temperatura, cuatro» → `var4`: «4 / 4»
- «Uno.» → `uno`: «= 1» y el «1,25» se tacha
- «La apuesta es la temperatura misma» → `misma`: «x̂ = y»
- «el ruido es igual de probable» → `ruido`: dos flechas magenta, hacia arriba y hacia abajo, de igual largo

<!-- b2 -->
Así que sobre la misma nube hay dos rectas distintas, la que adivina i griega a partir de equis y la que adivina equis a partir de i griega. La primera mide los errores en vertical y la segunda, en horizontal. Solo coinciden cuando rho vale uno o menos uno.

- «sobre la misma nube» → `nube`: corte; una nube de puntos con ρ = 0,9
- «la que adivina i griega a partir de equis» → `r1`: la recta ámbar de y sobre x
- «y la que adivina equis a partir de i griega» → `r2`: la segunda recta, más inclinada
- «mide los errores en vertical» → `vert`: segmentos rojos verticales de la nube a la primera recta
- «la segunda, en horizontal» → `hori`: segmentos rojos horizontales hasta la segunda recta
- «Solo coinciden cuando rho vale uno o menos uno» → `coin`: la nube se aprieta (ρ → 1) y las dos rectas se juntan en una

---

# Escena 14 — Cierre

**Capítulo YouTube:** Lo que viene: la sombra de una flecha

## Narración

<!-- b1 -->
Resumimos. Con una recta basta conocer medias, varianzas y la covarianza, y con eso la mejor apuesta arranca en la media y corrige con rho, y el error que deja es la varianza por uno menos rho al cuadrado. Pero queda una pregunta. ¿Por qué esa fórmula, y por qué no hay una recta mejor? La respuesta es un dibujo con flechas. Lo vemos en el próximo episodio, la sombra de una flecha.

- «Resumimos» → `resumen`: corte; la palabra «Resumen» en ámbar
- «medias, varianzas y la covarianza» → `datos`: tres fichas «Medias», «Varianzas», «Covarianza»
- «arranca en la media y corrige con rho» → `recta`: «ŷ = μ_y + ρ (σ_y/σ_x)(x − μ_x)»
- «el error que deja» → `error`: la palabra «Error» en rojo
- «la varianza por uno menos rho al cuadrado» → `var1r`: «J = σ_y² (1 − ρ²)» en rojo
- «Pero queda una pregunta» → `pregunta`: «Una pregunta» en ámbar
- «¿Por qué esa fórmula» → `porque`: un «¿Por qué?» en ámbar sobre la fórmula
- «por qué no hay una recta mejor» → `mejor`: una segunda recta con una cruz roja
- «un dibujo con flechas» → `flechas`: corte; las flechas y, x, la sombra ŷ y el error e a 90°
- «el próximo episodio» → `proximo`: aparece la tarjeta «Episodio 4»
- «la sombra de una flecha» → `titulo`: «La sombra de una flecha» entra con rebote
