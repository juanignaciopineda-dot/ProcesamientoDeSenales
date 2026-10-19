# Episodio 4 — La sombra de una flecha

Capítulo 8 (Estimación), episodio 4 de 5. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 13 a 16), más un gancho y un cierre nuevos.

**Estado:** **Subido a YouTube y publicado** (19/10/2026): render final 1080p60 de 8:50, título buscable, descripción con el capítulo del libro y `capitulos.txt`, subtítulos, categoría Educación (https://youtu.be/R4nK_JbnUbU). Lo subió el usuario sin el visto bueno que figuraba pendiente (texto ⭐ / mp4). Residuos limpiados; la caché de voz original está en `media/voiceovers/`: se rehace igual con `python rehacer.py Capitulo08_Estimacion E4`.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Para hallar la mejor recta necesitamos una parábola y una derivada. Hoy basta una sombra.»
- ⭐ Escena 11 (cierre): resumen y anuncia E5 por su título, «¿Dos termómetros mejor que uno?».
- ⭐ Retoque en la escena 07 (bloque b2): el guion base decía «unos cero coma nueve grados»; el error es un largo, no un ángulo, así que se quita «grados».
- ⭐ Retoque en la escena 10 (bloque b5): se quita la última frase del guion base («Y ahora, el siguiente paso: ¿qué pasa si en vez de un termómetro tienes dos?»); la pregunta pasa al cierre.

Nota para el episodio anterior: el cierre del E3 («¿Y si solo vale una recta?») tiene que anunciar este título, «La sombra de una flecha».
El cierre de este episodio anuncia el E5, «¿Dos termómetros mejor que uno?».

Reparto de las escenas del guion base: 13 → escenas 03 y 04; 14 → 05 y 06; 15 → 07 y 08; 16 → 09 y 10.
Solo se partieron bloques enteros en escenas atómicas: el texto del guion base no cambia (salvo los retoques de arriba).

---

# Escena 01 — Gancho

**Capítulo YouTube:** Una sombra en vez de una derivada

## Narración

<!-- b1 -->
Para hallar la mejor recta necesitamos una parábola y una derivada. Hoy basta una sombra.

- «una parábola» → `parabola`: se dibuja la parábola del error del termómetro, con su mínimo marcado
- «y una derivada» → `derivada`: una tangente se desliza por la parábola hasta el fondo, donde queda horizontal
- «Hoy» → `hoy`: la parábola y la tangente se apagan
- «basta una sombra» → `sombra`: aparecen la flecha de la lectura, la de la temperatura y la sombra ámbar de una sobre la otra, con el ángulo recto

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** La sombra de una flecha

## Narración

<!-- b1 -->
La sombra de una flecha.

- «La sombra» → `t1`: «La sombra» entra con rebote
- «de una flecha.» → `t2`: «de una flecha» entra debajo, con la etiqueta «Capítulo 8 · Estimación»

---

# Escena 03 — DosFlechas

**Capítulo YouTube:** El termómetro como flechas
**Objetivo:** dibujar la temperatura y la lectura como flechas de largos 2 y √5, con su producto escalar, su ángulo, y ver que todas las estimaciones h · x caen sobre una recta.

## Narración

<!-- b1 -->
En el capítulo siete vimos que las variables centradas se comportan como flechas. El largo de cada flecha es su desviación estándar, su producto escalar es la covarianza, y el coseno del ángulo entre dos flechas es rho. Dibujemos así el termómetro. La temperatura es una flecha de largo dos. La lectura, una de largo raíz de cinco, algo más de dos coma dos.

- «se comportan como flechas» → `flechas`: dos flechas grises genéricas entran a la izquierda
- «El largo de cada flecha» → `largo`: a la derecha, «Largo = desviación estándar»
- «su producto escalar» → `escalar`: debajo, «Producto escalar = covarianza»
- «el coseno del ángulo» → `coseno`: debajo, «cos θ = ρ»
- «Dibujemos así el termómetro» → `termo`: las flechas genéricas se sustituyen por las del termómetro, sin rótulos, y el panel se apaga
- «La temperatura» → `temp`: la flecha azul se rotula «Y»
- «de largo dos» → `dos`: sobre la flecha azul, «2»
- «La lectura» → `lectura`: la flecha cian se rotula «X»
- «raíz de cinco» → `r5`: sobre la flecha cian, «√5»
- «algo más de dos coma dos» → `dosdos`: «√5 ≈ 2,24»

<!-- b2 -->
Su producto escalar es la covarianza, cuatro. Así que el coseno del ángulo es cuatro entre dos por raíz de cinco, que es cero coma ocho nueve. Forman unos veintisiete grados. Y ahora vamos con la estimación, en la que hache por la lectura es la flecha de la lectura, estirada o encogida. Todas las opciones están sobre una misma recta, la que sigue la dirección de la lectura.

- «Su producto escalar» → `pe`: a la derecha, «⟨Y, X⟩ =
- «la covarianza, cuatro» → `cuatro`: «σ_YX = 4»
- «el coseno del ángulo es» → `cos`: debajo, «cos θ = 4 / (2 · √5)»
- «cero coma ocho nueve» → `cos89`: «≈ 0,89»
- «Forman unos veintisiete grados» → `ang`: se dibuja el arco entre las flechas con «≈ 27°»
- «la estimación» → `estim`: arriba a la derecha, «Estimación: ŷ = h · x»
- «hache por la lectura» → `hx`: el rótulo ámbar «h · X» y una flecha ámbar corta sobre la lectura
- «estirada o encogida» → `estira`: la flecha ámbar se estira y se encoge a lo largo de la lectura
- «Todas las opciones» → `todas`: varios puntos ámbar tenues aparecen alineados con la lectura
- «una misma recta» → `recta`: una recta punteada prolonga la flecha de la lectura en los dos sentidos
- «la dirección de la lectura» → `direccion`: se resalta la flecha cian de la lectura

---

# Escena 04 — ElPuntoMasCercano

**Capítulo YouTube:** La sombra es la proyección
**Objetivo:** ver que el mejor h es el punto de la recta más cercano a la punta de Y, que ese punto es el pie de la perpendicular (la sombra), y calcular su largo para recuperar h = 0,8 sin derivar.

## Narración

<!-- b1 -->
Elegir el mejor hache es elegir el punto de esa recta más cercano a la punta de la flecha de la temperatura. Porque el error es la flecha que va de la estimación a la temperatura, y su largo al cuadrado es el error cuadrático medio. Probemos puntos. Uno muy atrás queda lejos. Uno muy adelante, también. ¿Cuál es el más cercano?

- «el punto de esa recta» → `punto`: un punto ámbar sobre la recta, con «ŷ = h · x»
- «la punta de la flecha de la temperatura» → `punta`: un segmento rojo une el punto con la punta de Y
- «el error es la flecha» → `error`: el segmento rojo se rotula «e»
- «su largo al cuadrado» → `largo2`: a la derecha, «Largo² del error = error cuadrático medio»
- «error cuadrático medio» → `ecm`: se resalta «error cuadrático medio»
- «Probemos puntos» → `probemos`: el punto se mueve por la recta, con el segmento rojo siguiéndolo
- «Uno muy atrás» → `atras`: el punto retrocede y el segmento rojo se alarga
- «Uno muy adelante» → `adelante`: el punto avanza muy adelante y el segmento se alarga otra vez
- «¿Cuál es el más cercano?» → `cual`: aparece un «?» ámbar y el punto oscila despacio

<!-- b2 -->
Es una regla del colegio, según la cual la distancia más corta de un punto a una recta es la perpendicular. El mejor punto es el pie de esa perpendicular. Es como la sombra de la flecha de la temperatura sobre la recta de la lectura, con la luz cayendo en ángulo recto. Se llama proyección.

- «una regla del colegio» → `colegio`: desde la punta de Y salen cuatro segmentos grises hacia puntos de la recta
- «la distancia más corta» → `corta`: los cuatro segmentos se iluminan uno tras otro
- «la perpendicular» → `perp`: el segmento vertical se pone grueso y rojo y los demás se apagan
- «el pie de esa perpendicular» → `pie`: el punto ámbar se coloca en el pie y aparece el cuadradito del ángulo recto
- «la sombra» → `sombra`: entra un sol arriba
- «sobre la recta de la lectura» → `sobre`: el trozo de recta hasta el pie se marca grueso, ámbar
- «la luz cayendo» → `luz`: rayos verticales finos bajan desde Y hasta la recta
- «Se llama proyección» → `proy`: «Proyección» entra con rebote

<!-- b3 -->
¿Cuánto mide la sombra? El largo de la flecha por el coseno del ángulo, es decir, dos por cero coma ocho nueve, que da uno coma siete nueve. Y para saber qué múltiplo de la lectura es, la dividimos entre el largo de la lectura, raíz de cinco. Da cero coma ocho. El mismo número que salió de la parábola, ahora sin derivar nada, solo con un dibujo.

- «¿Cuánto mide la sombra?» → `cuanto`: sobre la sombra una llave con «?»
- «El largo de la flecha por el coseno» → `lc`: a la derecha, «sombra = 2 · cos θ»
- «dos por cero coma ocho nueve» → `dosx`: «= 2 · 0,89»
- «uno coma siete nueve» → `s179`: «≈ 1,79» y la llave toma ese valor
- «qué múltiplo de la lectura es» → `mult`: se resalta la flecha cian de la lectura
- «la dividimos» → `divide`: «h = 1,79 /»
- «raíz de cinco» → `r5`: «√5»
- «Da cero coma ocho» → `h08`: «= 0,8» en verde
- «El mismo número que salió de la parábola» → `parab`: abajo a la derecha, la parábola del error con su mínimo en 0,8
- «solo con un dibujo» → `dib`: se resalta la figura de las flechas

---

# Escena 05 — ElErrorEsPerpendicular

**Capítulo YouTube:** La regla de ortogonalidad, recortada
**Objetivo:** leer el ángulo recto como E[e · x̃] = 0, ver por qué el error es ortogonal solo al dato y al uno, y fijar las dos condiciones.

## Narración

<!-- b1 -->
Mira el ángulo recto. El error es perpendicular a la flecha de la lectura. Y perpendicular, para variables, significa que la media de su producto es cero. Es la regla de ortogonalidad de hace dos episodios, pero recortada, porque allí el error era ortogonal a cualquier función del dato y aquí solo a la lectura. ¿Por qué solo a ella?

- «Mira el ángulo recto» → `recto`: vuelve la figura de las flechas y el cuadradito del ángulo recto parpadea
- «El error es perpendicular» → `perp`: se resalta el error rojo
- «a la flecha de la lectura» → `lect`: se resalta la flecha cian
- «para variables» → `variables`: junto al cuadradito aparece «e ⟂ X»
- «la media de su producto es cero» → `prod`: a la derecha, «E[e · x̃] = 0»
- «la regla de ortogonalidad» → `regla`: debajo, una tarjeta con «E[e · g(X)] = 0 para toda g»
- «pero recortada» → `recorta`: unas tijeras cruzan la tarjeta
- «cualquier función del dato» → `cualq`: se resalta «toda g» en la tarjeta
- «solo a la lectura» → `sola`: la tarjeta pasa a «E[e · x̃] = 0»
- «¿Por qué solo a ella?» → `porque`: aparece un «?» ámbar

<!-- b2 -->
Porque la recta solo sabe usar dos cosas, que son la lectura y un número fijo, el uno que multiplica a be. Si el error tuviera algo en común con cualquiera de las dos, la recta podría aprovecharlo. Así que pedimos dos condiciones. Que el error sea ortogonal al uno, es decir, que su media sea cero. Y que sea ortogonal a la lectura.

- «solo sabe usar dos cosas» → `dos`: corte; aparece «ŷ = h · X + b · 1» partida en piezas
- «la lectura» → `lec`: se resalta «X» en cian
- «el uno que multiplica a be» → `uno`: se resalta «1» en gris
- «algo en común» → `comun`: dos círculos que se solapan junto a «e»
- «la recta podría aprovecharlo» → `aprov`: una flecha ámbar va de los círculos solapados a «ŷ»
- «Así que pedimos dos condiciones» → `cond`: entran dos renglones vacíos numerados
- «ortogonal al uno» → `ort1`: primer renglón, «e ⟂ 1»
- «su media sea cero» → `media0`: «E[e] = 0»
- «ortogonal a la lectura» → `ortx`: segundo renglón, «e ⟂ X → E[e · x̃] = 0»

---

# Escena 06 — SinDerivadas

**Capítulo YouTube:** Tres caminos al mismo 0,8
**Objetivo:** sacar h de la segunda condición sin derivar, ver que pendiente cero y ángulo recto son la misma condición y escribir la fórmula de proyección.

## Narración

<!-- b1 -->
La primera condición ya la usamos, porque es la que fijaba be, con la recta arrancando de la media. La segunda es nueva y da hache sin derivadas. La media de la temperatura centrada menos hache por la lectura centrada, todo por la lectura centrada, tiene que ser cero. Por linealidad, queda cuatro menos cinco hache, igual a cero. Hache vale cero coma ocho.

- «La primera condición» → `c1`: a la izquierda, «E[e] = 0»
- «fijaba be» → `fijaba`: una marca verde y «b = 20 − 20h»
- «La segunda es nueva» → `c2`: a la derecha, «E[e · x̃] = 0»
- «La media de la temperatura centrada» → `m1`: se construye «E[(ỹ»
- «menos hache por la lectura centrada» → `m2`: «− h x̃)»
- «todo por la lectura centrada» → `m3`: «x̃]»
- «tiene que ser cero» → `m4`: «= 0»
- «Por linealidad» → `lineal`: debajo, «E[ỹ x̃] − h E[x̃²] = 0»
- «cuatro menos cinco hache» → `cuatro`: «4 − 5h = 0»
- «Hache vale cero coma ocho» → `h08`: «h = 0,8» en verde, con un recuadro

<!-- b2 -->
Tres caminos y un solo resultado, que son el fondo de la parábola, la pendiente igual a cero y el ángulo recto. No es casualidad. La pendiente de la parábola, escrita con medias, es menos dos por la media del error por la lectura. Que la pendiente sea cero y que el error sea perpendicular son la misma condición, dicha de dos formas.

- «Tres caminos» → `tres`: tres tarjetas vacías en fila
- «el fondo de la parábola» → `fondo`: primera tarjeta, la parábola con su mínimo y «0,8»
- «la pendiente igual a cero» → `pend`: segunda tarjeta, la parábola con la tangente horizontal y «0,8»
- «el ángulo recto» → `angr`: tercera tarjeta, el ángulo recto y «0,8»
- «No es casualidad» → `casual`: las tres tarjetas se resaltan
- «La pendiente de la parábola» → `jp`: debajo, «J′(h)»
- «es menos dos por la media» → `medias`: «= −2 E[»
- «del error por la lectura» → `elerror`: «e · x̃]»
- «sea cero» → `cero`: «= 0»
- «la misma condición» → `misma`: «J′(h) = 0 ⟺ e ⟂ X»

<!-- b3 -->
Y queda una fórmula de geometría que sirve siempre. La proyección de una flecha sobre otra es el producto escalar de las dos, dividido entre el largo al cuadrado de la segunda, por esa segunda flecha. El producto escalar es la covarianza; el largo al cuadrado, la varianza de equis. El factor hache, covarianza entre varianza, sale solo, leyendo el dibujo.

- «La proyección de una flecha sobre otra» → `proy`: aparece «proy_X Y =»
- «el producto escalar de las dos» → `num`: el numerador, «⟨Y, X⟩»
- «dividido entre el largo al cuadrado de la segunda» → `den`: el denominador, «⟨X, X⟩»
- «por esa segunda flecha» → `porx`: «· X»
- «El producto escalar es la covarianza» → `cov`: debajo, el numerador se repite como «σ_YX»
- «la varianza de equis» → `var`: el denominador, «σ_X²»
- «El factor hache» → `fh`: se recuadra el factor y aparece «h»
- «covarianza entre varianza» → `cv`: «h = σ_YX / σ_X² = 4 / 5 = 0,8»
- «leyendo el dibujo» → `dibujo`: la fórmula se resalta con un recuadro ámbar

---

# Escena 07 — ElTrianguloRectangulo

**Capítulo YouTube:** Pitágoras y el error
**Objetivo:** sacar el error del termómetro por Pitágoras: 4 = 3,2 + 0,8.

## Narración

<!-- b1 -->
Ahora el error. La flecha de la temperatura, la sombra y el error forman un triángulo rectángulo. La temperatura es la hipotenusa; la sombra y el error, los catetos. Y Pitágoras dice que la hipotenusa al cuadrado es la suma de los catetos al cuadrado.

- «Ahora el error» → `ahora`: vuelve la figura de las flechas y el error rojo se resalta
- «la sombra y el error forman» → `som1`: se resaltan la sombra y el error
- «un triángulo rectángulo» → `triang`: el triángulo se rellena con un tono suave
- «es la hipotenusa» → `hipo`: la flecha azul se resalta con el rótulo «Hipotenusa»
- «la sombra y el error» → `cat`: la sombra y el error se resaltan con «Catetos»
- «Pitágoras dice» → `pit`: a la derecha, «hipotenusa²»
- «al cuadrado es la suma» → `igual`: «=»
- «de los catetos al cuadrado» → `suma`: «cateto² + cateto²»

<!-- b2 -->
La hipotenusa al cuadrado es la varianza de la temperatura, que vale cuatro. La sombra mide uno coma siete nueve, y al cuadrado, tres coma dos. Así que el error al cuadrado es cuatro menos tres coma dos, es decir, cero coma ocho. Otra vez el mismo número. Y el cateto del error mide raíz de cero coma ocho, unos cero coma nueve.

- «la varianza de la temperatura» → `var`: «σ_Y² = 4» en azul
- «La sombra mide» → `sombra`: «sombra = 1,79» en ámbar
- «tres coma dos» → `s32`: «sombra² = 3,2»
- «cuatro menos tres coma dos» → `resta`: «error² = 4 − 3,2»
- «cero coma ocho» → `e08`: «= 0,8» en rojo
- «Otra vez el mismo número» → `mismo`: el 0,8 se resalta junto a la parábola pequeña
- «raíz de cero coma ocho» → `raiz`: «error = √0,8»
- «unos cero coma nueve» → `e089`: «≈ 0,89»

---

# Escena 08 — ElErrorEnGeneral

**Capítulo YouTube:** El error es σ²(1 − ρ²)
**Objetivo:** deducir el error σ_Y²(1 − ρ²) con el seno, leer los casos ρ = 1 y ρ = 0 en el dibujo y ver la partición «explicado + no explicado».

## Narración

<!-- b1 -->
En general, el cateto opuesto al ángulo es la hipotenusa por el seno. Elevado al cuadrado, eso es la varianza por el seno al cuadrado. Y el seno al cuadrado es uno menos el coseno al cuadrado, es decir, uno menos rho al cuadrado. La fórmula del error, varianza por uno menos rho al cuadrado, no hay que memorizarla, porque es el cateto que le falta a la sombra.

- «el cateto opuesto al ángulo» → `opuesto`: el arco del ángulo y el error rojo se resaltan
- «es la hipotenusa por el seno» → `seno`: a la derecha, «error = σ_Y · sen θ»
- «Elevado al cuadrado» → `cuad`: «error² = σ_Y² · sen² θ»
- «la varianza por el seno al cuadrado» → `varsen`: se resalta «σ_Y² · sen² θ»
- «el seno al cuadrado es uno menos el coseno al cuadrado» → `sen2`: «= σ_Y² (1 − cos² θ)»
- «uno menos rho al cuadrado» → `rho2`: «= σ_Y² (1 − ρ²)»
- «La fórmula del error» → `form`: una flecha señala la fórmula final
- «no hay que memorizarla» → `memo`: la fórmula final se recuadra en ámbar
- «el cateto que le falta a la sombra» → `falta`: el error rojo parpadea en la figura

<!-- b2 -->
Los casos extremos se ven en el dibujo. Si las flechas apuntan en la misma dirección, con rho igual a uno, la sombra es la flecha entera y el error desaparece. Si son perpendiculares, con rho igual a cero, la sombra es un punto, así que la estimación es la media y el error es la varianza entera. Un dato perpendicular a lo que buscas no ayuda en nada.

- «Los casos extremos» → `extremos`: la flecha de la temperatura empieza a girar
- «apuntan en la misma dirección» → `misma`: la flecha azul se pone sobre la cian
- «rho igual a uno» → `rho1`: «ρ = 1»
- «el error desaparece» → `desap`: el error rojo se reduce a nada y aparece «error = 0»
- «son perpendiculares» → `perp`: la flecha azul gira hasta quedar vertical
- «rho igual a cero» → `rho0`: «ρ = 0»
- «la sombra es un punto» → `punto`: la sombra ámbar se reduce a un punto
- «la estimación es la media» → `media`: «ŷ = media»
- «el error es la varianza entera» → `varent`: «error = σ_Y²» con el error del largo de la flecha
- «Un dato perpendicular» → `datoperp`: se resalta la flecha cian
- «no ayuda en nada» → `nada`: una cruz roja junto a la flecha cian

<!-- b3 -->
Y fíjate en el reparto, porque cuatro es tres coma dos más cero coma ocho. La varianza de la temperatura se parte en lo que la lectura explica, la sombra, y lo que no, el error. Es la misma partición que la de la altura, donde el grupo explica una parte y la otra queda sin explicar. Allí con medias condicionales, aquí con una recta. En los dos casos es Pitágoras.

- «cuatro es tres coma dos más cero coma ocho» → `cuatro`: corte; una barra de largo fijo, «4», partida en «3,2» (ámbar) y «0,8» (rojo)
- «tres coma dos» → `t32`: se resalta el trozo ámbar de la barra
- «cero coma ocho. La varianza» → `t08`: se resalta el trozo rojo
- «lo que la lectura explica» → `explica`: se resalta el trozo ámbar con «Explicado»
- «lo que no, el error» → `noexp`: se resalta el trozo rojo con «Sin explicar»
- «la misma partición que la de la altura» → `altura`: debajo, otra barra «81,76» partida en «40,56» y «41,2»
- «el grupo explica una parte» → `grupo`: se resalta el trozo ámbar de la altura
- «Allí con medias condicionales» → `condic`: rótulo «Medias condicionales» bajo la barra de la altura
- «aquí con una recta» → `conrecta`: rótulo «Una recta» bajo la barra del termómetro
- «es Pitágoras» → `pitag`: un triángulo rectángulo pequeño entre las dos barras

---

# Escena 09 — ElCanalEsUnaRecta

**Capítulo YouTube:** Cuándo la recta no pierde nada
**Objetivo:** ver que la media condicional nunca pierde contra la recta, plantear cuándo empatan y mostrar el primer caso: el canal de bits.

## Narración

<!-- b1 -->
La recta es lo mejor entre las rectas. La media condicional es lo mejor sin restricciones. Así que la media condicional nunca pierde contra la recta, y a veces gana, como en la carpa. La pregunta es cuándo empatan, es decir, cuándo la recta no pierde nada. Hay dos casos que nos importan mucho.

- «La recta es lo mejor» → `recta`: una caja ámbar «Mejor recta»
- «entre las rectas» → `entre`: bajo la caja, «Entre todas las rectas»
- «La media condicional» → `cond`: encima, una caja verde «Media condicional»
- «sin restricciones» → `sin`: bajo la caja verde, «Sin restricciones»
- «nunca pierde» → `nunca`: entre las dos cajas, «Error ≤ Error»
- «como en la carpa» → `carpa`: a la derecha, «Carpa: 1/24 < 1/18»
- «cuándo empatan» → `empatan`: el «≤» se convierte en «= ?»
- «Hay dos casos» → `dos`: abajo dos fichas, «1 · Dos valores» y «2 · Gaussianas»

<!-- b2 -->
El primero es el canal de bits. Lo recibido solo vale cero o uno, así que la media condicional son dos puntos, uno en cero coma cero cuatro cinco sobre el cero, y otro en cero coma setenta y nueve sobre el uno. Por dos puntos siempre pasa una recta. La mejor regla ya es una recta, y la fórmula lo confirma, ya que cero coma dos uno por uno menos rho al cuadrado da cero coma cero ocho cuatro, el mismo error de antes.

- «el canal de bits» → `canal`: corte; ejes con «Recibido» y «Estimación de lo enviado»
- «solo vale cero o uno» → `cerouno`: dos guías verticales, en 0 y en 1
- «dos puntos» → `puntos`: dos puntos ámbar sobre las guías
- «cero coma cero cuatro cinco» → `p045`: el rótulo «0,045» junto al punto del cero
- «cero coma setenta y nueve» → `p79`: el rótulo «0,79» junto al punto del uno
- «Por dos puntos siempre pasa una recta» → `pasa`: la recta ámbar que pasa por los dos puntos
- «La mejor regla ya es una recta» → `regla`: la recta se resalta
- «la fórmula lo confirma» → `formula`: a la derecha, «Error = σ² · (1 − ρ²)»
- «cero coma dos uno» → `c021`: «σ² = 0,21»
- «uno menos rho al cuadrado da» → `unomenos`: «0,21 · (1 − ρ²)»
- «cero coma cero ocho cuatro» → `e084`: «≈ 0,084»
- «el mismo error de antes» → `antes`: un tilde verde y «Como en el episodio 2»

---

# Escena 10 — LasGaussianas

**Capítulo YouTube:** Gaussianas: lo lineal es lo óptimo
**Objetivo:** mostrar con la elipse y sus rebanadas que, con gaussianas, la media condicional es la recta y la varianza de cada rebanada es el error; y por qué todo el resto de la materia usa filtros lineales.

## Narración

<!-- b1 -->
El segundo caso es el gaussiano. Si la temperatura y el ruido del termómetro son gaussianos, la nube de puntos tiene forma de elipse inclinada. Corta la elipse en rebanadas verticales y verás que cada rebanada es una campana. Sus centros caen exactamente sobre una recta, la del cero coma ocho. Y todas las campanas tienen el mismo ancho, con varianza cero coma ocho, marque lo que marque el termómetro.

- «El segundo caso es el gaussiano» → `gauss`: corte; ejes con «Lectura» y «Temperatura»
- «Si la temperatura y el ruido» → `dosg`: dos campanas pequeñas, una azul y otra magenta
- «son gaussianos» → `songauss`: las campanas se unen en un tilde verde
- «la nube de puntos» → `nube`: aparece una nube de puntos azules
- «elipse inclinada» → `elipse`: se dibuja el contorno de la elipse
- «rebanadas verticales» → `rebanadas`: tres franjas verticales translúcidas
- «cada rebanada es una campana» → `campanas`: en cada franja se dibuja una campana de lado
- «Sus centros caen» → `centros`: un punto ámbar en el centro de cada campana
- «sobre una recta» → `recta`: la recta ámbar pasa por los tres puntos
- «la del cero coma ocho» → `r08`: la recta se rotula «Pendiente 0,8»
- «Y todas las campanas» → `todas`: las tres campanas se resaltan
- «el mismo ancho» → `ancho`: una doble flecha del mismo largo sobre cada campana
- «varianza cero coma ocho» → `v08`: «Varianza 0,8»
- «marque lo que marque el termómetro» → `marque`: una franja se desliza por la nube; su campana la acompaña sin cambiar de ancho

<!-- b2 -->
Es decir, con gaussianas la media condicional ya es una recta, la misma que da la fórmula. La mejor estimación posible y la mejor estimación lineal son la misma, y no se pierde nada por usar rectas. Y la varianza de cada rebanada, cero coma ocho, es justo el error de la recta.

- «la media condicional ya es una recta» → `condrec`: arriba a la derecha, «E[Y | X] = recta»
- «la misma que da la fórmula» → `misma`: debajo, un tilde verde y «La del episodio 3»
- «La mejor estimación posible» → `posible`: una caja verde «Mejor posible»
- «la mejor estimación lineal» → `lineal`: una caja ámbar «Mejor lineal»
- «son la misma» → `igual`: entre las dos cajas aparece «=»
- «no se pierde nada» → `nada`: «No se pierde nada»
- «la varianza de cada rebanada» → `varreb`: se resaltan las tres campanas
- «cero coma ocho» → `v08`: «0,8» sobre las campanas
- «el error de la recta» → `errrecta`: «Error de la recta = 0,8» en rojo

<!-- b3 -->
Esto es lo que permite al resto de la materia trabajar solo con filtros lineales sin disculparse. El ruido suele ser gaussiano, y entonces lo lineal ya es lo óptimo. Cuando no lo es, lo lineal sigue siendo lo mejor que se puede hacer con medias, varianzas y covarianzas.

- «resto de la materia» → `resto`: corte; una caja «Filtro lineal» y una flecha hacia «Capítulos 10 a 13»
- «filtros lineales» → `filtros`: la caja «Filtro lineal» se resalta
- «El ruido suele ser gaussiano» → `ruido`: una campana magenta con «Ruido gaussiano»
- «lo lineal ya es lo óptimo» → `optimo`: un tilde verde y «Lineal = óptimo»
- «Cuando no lo es» → `noes`: la campana se deforma en una forma torcida
- «lo mejor que se puede hacer» → `mejor`: «Lo mejor entre las rectas»
- «medias, varianzas y covarianzas» → `tres`: tres fichas, «Medias», «Varianzas» y «Covarianzas»

---

# Escena 11 — Cierre

**Capítulo YouTube:** Y si fueran dos termómetros

## Narración

<!-- b1 -->
Así que estimar con una recta es proyectar, de modo que la mejor apuesta es la sombra de la temperatura sobre la lectura y el error es el cateto que queda en ángulo recto. Con gaussianas, ninguna otra regla la supera. Pero un termómetro tiene un límite, que es el ruido. ¿Y si pusiéramos dos? En el próximo episodio veremos «¿Dos termómetros mejor que uno?».

- «estimar con una recta es proyectar» → `proyectar`: la figura de las flechas con la sombra ámbar y el error rojo en ángulo recto
- «la sombra de la temperatura» → `sombra`: se resalta la sombra ámbar
- «el error es el cateto» → `cateto`: se resalta el error rojo con el cuadradito
- «Con gaussianas» → `congauss`: la figura se reduce a la izquierda y entra una campana gaussiana
- «ninguna otra regla la supera» → `supera`: un tilde verde junto a la campana
- «un termómetro tiene un límite» → `limite`: la figura se apaga y queda un termómetro
- «el ruido» → `ruido`: una traza magenta lo rodea
- «¿Y si pusiéramos dos?» → `dos`: el termómetro se duplica
- «¿Dos termómetros mejor que uno?» → `titulo`: el título «¿Dos termómetros mejor que uno?» entra con rebote
