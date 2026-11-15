# Episodio 2 — Toda la señal en un solo número

Capítulo 13 (Detección de señales), episodio 2 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 05 a 08), más un gancho y un cierre nuevos.

**Estado:** escenas `s01`–`s11` animadas; borrador 480p15 de 9:15 con 0 avisos (`salida/E2_Toda_la_senal_en_un_solo_numero-480p15.mp4`). Sigue: revisión del texto ⭐ y visto bueno del usuario al mp4 (paso 15); después render final `--calidad qh` (paso 16).

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Un radar oye cientos de muestras y tiene que decir sí o no. Y todo lo que importa de ellas cabe en un solo número: lo parecida que es la señal recibida a la que buscamos.»
- ⭐ Escena 11 (cierre): resumen y anuncia E3 por su título, «¿Cuánto nos equivocamos?».
- ⭐ Retoque en la escena 10 (bloque b2): se quita la última frase del guion base («Solo falta saber cuánto vamos a fallar.»); la pregunta pasa al cierre.

Nota para el episodio anterior: el E1 («Más datos no bastan») termina con la pregunta de si existe un resumen de la señal entera que no tire nada; este episodio la responde. Su cierre tiene que anunciar el título de este: «Toda la señal en un solo número».

Reparto de las escenas del guion base: 05 → escenas 03 y 04; 06 → 05 y 06; 07 → 07 y 08; 08 → 09 y 10.
Solo se partieron bloques enteros en escenas atómicas: el texto del guion base no cambia (salvo el retoque de arriba).

---

# Escena 01 — Gancho

**Capítulo YouTube:** Un solo número

## Narración

<!-- b1 -->
Un radar oye cientos de muestras y tiene que decir sí o no. Y todo lo que importa de ellas cabe en un solo número: lo parecida que es la señal recibida a la que buscamos.

- «Un radar oye» → `radar`: entra la antena de radar a la izquierda
- «cientos de muestras» → `muestras`: una traza cian larga y ruidosa se dibuja a la derecha de la antena
- «decir sí o no» → `sino`: dos casillas, «sí» y «no», en ámbar
- «un solo número» → `numero`: la traza se comprime en una sola barra ámbar con un número encima
- «lo parecida que es la señal recibida» → `parecida`: junto a la traza cian aparece el pulso azul y se alinean
- «a la que buscamos» → `buscamos`: el pulso azul se rotula «la que buscamos»

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Toda la señal en un solo número

## Narración

<!-- b1 -->
Toda la señal en un solo número.

- «Toda la señal» → `t1`: «Toda la señal» entra con rebote
- «en un solo número» → `t2`: «en un solo número» entra debajo, con la etiqueta «Capítulo 13 · Detección de señales»

---

# Escena 03 — ElPulsoYElRuido

**Capítulo YouTube:** La señal conocida y el ruido gaussiano

## Narración

<!-- b1 -->
Vamos al caso concreto. El radar manda un pulso que conocemos de antemano: tres muestras, de valores dos, dos y uno. Lo llamamos la señal objetivo, y se escribe ese de ene. Si hay un avión, lo recibido es ese pulso más ruido, muestra a muestra. Si no, solo ruido. En total, tres números recibidos: erre de cero, erre de uno y erre de dos.

- «un pulso que conocemos de antemano» → `pulso`: la antena lanza un pulso hacia la derecha
- «tres muestras» → `tres`: aparecen tres huecos vacíos sobre un eje n = 0, 1, 2
- «dos, dos y uno» → `valores`: se llenan tres barras azules de alturas 2, 2 y 1, con su número encima
- «la señal objetivo» → `objetivo`: una llave sobre las barras con «la señal objetivo, conocida»
- «ese de ene» → `sn`: entra «s[n]» en azul sobre la llave
- «Si hay un avión» → `avion`: entra el ícono de un avión
- «ese pulso más ruido» → `mas`: sobre cada barra azul se apila una barra magenta pequeña, de signo variable
- «muestra a muestra» → `muestra`: un marco recorre n = 0, 1 y 2, una a una
- «Si no, solo ruido» → `solo`: las barras azules se apagan y quedan solo las magenta
- «tres números recibidos» → `recibidos`: tres barras cian, la suma de cada pareja
- «erre de cero, erre de uno y erre de dos» → `erres`: rótulos «r[0]», «r[1]» y «r[2]» bajo las tres barras cian

<!-- b2 -->
Sobre el ruido suponemos dos cosas. Primera: en cada muestra es una campana de Gauss centrada en cero, con varianza sigma cuadrado, que aquí vale uno. Segunda: cada muestra es independiente de las demás. Por lo que vimos en el capítulo siete, eso significa que la densidad conjunta es el producto de las densidades de cada una.

- «dos cosas» → `dos`: entran los números «1» y «2» en magenta, apilados
- «Primera» → `p1`: se enciende el «1»
- «una campana de Gauss» → `campana`: se dibuja una campana magenta sobre un eje
- «centrada en cero» → `cero`: una línea punteada marca el 0 en el centro
- «sigma cuadrado» → `sigma`: entra «σ²» como ancho de la campana
- «aquí vale uno» → `vale1`: «σ² = 1» en magenta
- «Segunda» → `p2`: se enciende el «2»
- «independiente de las demás» → `indep`: tres campanas pequeñas, una por muestra, sin ninguna flecha entre ellas
- «el capítulo siete» → `cap7`: la etiqueta «Capítulo 7» junto a las campanas
- «el producto de las densidades de cada una» → `producto`: se construye «f(w₀, w₁, w₂) = f(w₀) · f(w₁) · f(w₂)», cada factor sale de su campana

---

# Escena 04 — LasDosDensidades

**Capítulo YouTube:** Las densidades bajo cada hipótesis

## Narración

<!-- b1 -->
Recuerda la campana centrada en cero: una constante por e elevado a menos equis al cuadrado entre dos sigma cuadrado. Si multiplicamos tres, las constantes se multiplican y los exponentes, como siempre con potencias del mismo número, se suman. Bajo la hipótesis cero solo recibimos ruido, así que la densidad de lo recibido es esa constante por e elevado a menos la suma de los cuadrados de lo recibido, entre dos sigma cuadrado.

- «la campana centrada en cero» → `campana`: la campana magenta de la escena anterior vuelve a su sitio
- «una constante por e elevado a menos equis al cuadrado» → `forma`: se construye «c · e^(−x²/2σ²)», pieza a pieza
- «entre dos sigma cuadrado» → `dossigma`: se resalta el «2σ²» del denominador
- «Si multiplicamos tres» → `tres`: la fórmula se copia tres veces y las tres copias se juntan con puntos de producto
- «las constantes se multiplican» → `const`: las tres «c» se juntan en «c³»
- «los exponentes» → `expo`: los tres exponentes se resaltan en ámbar
- «se suman» → `suman`: los tres exponentes se unen en un solo exponente con signos «+»
- «Bajo la hipótesis cero» → `h0`: entra «H₀» a la izquierda
- «solo recibimos ruido» → `solo`: las barras magenta de las tres muestras
- «la densidad de lo recibido» → `dens`: entra «f(r | H₀) =»
- «la suma de los cuadrados de lo recibido» → `suma`: se completa «c · e^(−Σ r²[n] / 2σ²)», con Σ r²[n] en cian
- «entre dos sigma cuadrado» → `finh0`: la fórmula de H₀ queda enmarcada

<!-- b2 -->
Bajo la hipótesis uno, cada muestra es la señal más ruido. Es una campana igual, pero centrada en ese de ene en lugar de en cero. La densidad tiene la misma constante y el mismo exponente, con una diferencia: dentro del cuadrado aparece lo recibido menos la señal. Es lo que queda del ruido una vez quitada la señal.

- «Bajo la hipótesis uno» → `h1`: entra «H₁» bajo «H₀»
- «la señal más ruido» → `smasr`: la barra azul y la magenta se apilan en una cian
- «una campana igual» → `igual`: la campana de H₀ se copia
- «centrada en ese de ene» → `centrada`: la copia se desliza hasta s[n] y la línea punteada va con ella
- «en lugar de en cero» → `encero`: la campana original de H₀ queda como un fantasma tenue en el 0
- «la misma constante y el mismo exponente» → `misma`: se escribe «f(r | H₁) = c · e^(−Σ ( … )² / 2σ²)» con c y el denominador en tinta
- «una diferencia» → `dif`: el hueco «( … )» parpadea en ámbar
- «lo recibido menos la señal» → `resta`: el hueco se llena con «r[n] − s[n]» en cian y azul
- «lo que queda del ruido» → `queda`: una llave bajo «r[n] − s[n]» con «el ruido: w[n]» en magenta
- «una vez quitada la señal» → `quitada`: la barra azul se separa de la cian y queda la magenta

<!-- b3 -->
Esas son las dos densidades. La regla que ya conocemos nos pide compararlas, cada una multiplicada por su probabilidad a priori. Y aquí viene lo bonito: como son exponentes con sumas, casi todo lo que hay dentro va a desaparecer. Hagamos la cuenta entera, paso a paso, a ver qué queda.

- «Esas son las dos densidades» → `dos`: las dos fórmulas apiladas quedan enmarcadas
- «La regla que ya conocemos» → `regla`: entra la etiqueta «error mínimo»
- «compararlas» → `compara`: entra el signo «≷» entre ellas
- «su probabilidad a priori» → `prior`: a cada lado aparecen «p₀» y «p₁» en ámbar como factores
- «Y aquí viene lo bonito» → `bonito`: las dos fórmulas brillan
- «exponentes con sumas» → `sumas`: los dos «Σ» de los exponentes se resaltan en ámbar
- «casi todo lo que hay dentro» → `casi`: se resalta el interior de los dos exponentes
- «va a desaparecer» → `desaparecer`: el interior se difumina
- «paso a paso» → `paso`: aparece una escalera de cuatro peldaños vacíos

---

# Escena 05 — CancelarLosCuadrados

**Capítulo YouTube:** La derivación, paso a paso

## Narración

<!-- b1 -->
Empezamos por la regla: hay señal si la densidad de la hipótesis uno, por su a priori, es mayor que la de la hipótesis cero por la suya. Sustituimos las dos densidades. La constante es la misma a los dos lados, así que se cancela. Nos quedan dos exponenciales comparadas, cada una por su a priori.

- «hay señal si» → `senal`: entra el renglón «p₁ f(r|H₁) ≷ p₀ f(r|H₀)» con «H₁» en azul y «H₀» en magenta
- «la densidad de la hipótesis uno» → `d1`: se resalta f(r|H₁)
- «por su a priori» → `p1`: se resalta p₁
- «es mayor que» → `mayor`: se resalta el signo
- «la de la hipótesis cero por la suya» → `d0`: se resaltan f(r|H₀) y p₀
- «Sustituimos las dos densidades» → `sustituye`: en el renglón 1 las dos densidades se reemplazan por sus fórmulas
- «La constante es la misma a los dos lados» → `misma`: las dos «c» se subrayan en ámbar
- «se cancela» → `cancela`: las dos «c» se tachan con una línea roja
- «dos exponenciales comparadas» → `quedan`: queda el renglón 2: «p₁ e^(…) ≷ p₀ e^(…)»
- «cada una por su a priori» → `priors`: se resaltan p₁ y p₀ en ámbar

<!-- b2 -->
Ahora un truco: tomar logaritmos naturales. El logaritmo es la operación inversa de la exponencial: el logaritmo de e elevado a algo es ese algo. Y si un número es mayor que otro, su logaritmo también lo es, así que la comparación se conserva. Las exponenciales desaparecen y queda una comparación de sumas.

- «un truco» → `truco`: «ln» aparece a los dos lados del renglón 2 (renglón 3)
- «logaritmos naturales» → `ln`: la palabra «logaritmo natural» entra con rebote
- «la operación inversa de la exponencial» → `inversa`: dos flechas curvas, una de ida «e^x» y otra de vuelta «ln»
- «el logaritmo de e elevado a algo es ese algo» → `regla`: se construye «ln(eˣ) = x»
- «Y si un número» → `ysi`: aparecen dos números, 3 y 5
- «mayor que otro» → `mayor`: dos barras de distinta altura, la derecha más alta
- «su logaritmo también lo es» → `tambien`: bajo ellas, dos barras ln de la misma ordenación, con un tilde verde
- «la comparación se conserva» → `conserva`: el signo «≷» se enmarca en verde
- «Las exponenciales desaparecen» → `desaparecen`: en el renglón 3, las «e» y los «ln» se tachan
- «una comparación de sumas» → `sumas`: queda el renglón 4: «ln p₁ − Σ (r − s)² / 2σ² ≷ ln p₀ − Σ r² / 2σ²»

<!-- b3 -->
Desarrollemos el cuadrado de la hipótesis uno. Recibido menos señal, al cuadrado, es recibido al cuadrado, menos dos por recibido por señal, más señal al cuadrado. Y mira: la suma de los cuadrados de lo recibido aparece a los dos lados de la desigualdad. Aparece igual en las dos hipótesis, así que se cancela.

- «Desarrollemos el cuadrado» → `desarrolla`: se resalta el «(r − s)²» del renglón 4
- «Recibido menos señal, al cuadrado» → `rmenos`: se lee «(r − s)²» con r en cian y s en azul
- «es recibido al cuadrado» → `r2`: aparece «r²» en cian
- «menos dos por recibido por señal» → `dosrs`: aparece «− 2rs», con r en cian y s en azul
- «más señal al cuadrado» → `s2`: aparece «+ s²» en azul
- «la suma de los cuadrados de lo recibido» → `sumar2`: se resalta «Σ r²» en el lado izquierdo y también en el derecho
- «a los dos lados de la desigualdad» → `dos`: una flecha une los dos «Σ r²»
- «Aparece igual en las dos hipótesis» → `igual`: los dos «Σ r²» se tiñen del mismo color
- «se cancela» → `cancela`: los dos «Σ r²» se tachan con una línea roja

---

# Escena 06 — ElResultado

**Capítulo YouTube:** Un solo número: ge

## Narración

<!-- b1 -->
Queda: logaritmo de pe uno, más la suma de dos veces recibido por señal menos señal al cuadrado, entre dos sigma cuadrado, mayor que logaritmo de pe cero. Multiplicamos por sigma cuadrado y ordenamos. A la izquierda queda lo único que depende de lo recibido: la suma de recibido por señal, que llamamos ge. A la derecha, un umbral, gamma: sigma cuadrado por el logaritmo de pe cero entre pe uno, más la energía entre dos.

- «Queda» → `queda`: el renglón 5: «ln p₁ + Σ (2rs − s²) / 2σ² ≷ ln p₀»
- «logaritmo de pe uno» → `lnp1`: se resalta «ln p₁»
- «dos veces recibido por señal» → `dosrs`: se resalta «2rs»
- «señal al cuadrado» → `s2`: se resalta «s²»
- «mayor que logaritmo de pe cero» → `lnp0`: se resalta «ln p₀»
- «Multiplicamos por sigma cuadrado» → `mult`: «× σ²» entra con una flecha a los dos lados
- «y ordenamos» → `ordena`: los términos se reacomodan: lo que lleva r a la izquierda, lo demás a la derecha
- «lo único que depende de lo recibido» → `depende`: la parte izquierda se rodea en cian
- «la suma de recibido por señal» → `sumars`: se lee «Σ r[n] s[n]»
- «ge» → `ge`: entra «g» en ámbar, con rebote, como nombre de esa suma
- «un umbral, gamma» → `gamma`: entra «γ» en ámbar a la derecha
- «sigma cuadrado por el logaritmo de pe cero entre pe uno» → `lnpp`: se construye «σ² ln(p₀ / p₁)»
- «más la energía entre dos» → `energia`: se suma «+ E / 2», con E en azul; todo el resultado queda enmarcado en ámbar

<!-- b2 -->
Compruébalo con números. Si recibimos tres, uno y dos, ge vale tres por dos, más uno por dos, más dos por uno: diez. Con priors iguales el umbral es cuatro coma cinco, así que decimos «hay señal». Si recibimos cero coma cinco, menos uno y uno, ge vale cero. Decimos «solo ruido». Ge mide cuánto se parece lo recibido a la señal buscada.

- «Compruébalo con números» → `comprueba`: el resultado se desplaza a la izquierda y entra el pulso s = (2, 2, 1) en azul
- «tres, uno y dos» → `r1`: tres barras cian de alturas 3, 1 y 2 bajo el pulso
- «tres por dos, más uno por dos, más dos por uno» → `cuenta`: se construye «g = 3·2 + 1·2 + 2·1» con cada producto bajo su pareja de barras
- «diez» → `diez`: «= 10» en ámbar, con rebote
- «el umbral es cuatro coma cinco» → `umbral`: «γ = 4,5» en ámbar
- «hay señal» → `hay`: un tilde verde y «10 > 4,5 → hay señal»
- «cero coma cinco, menos uno y uno» → `r2`: las barras cian cambian a 0,5, −1 y 1
- «ge vale cero» → `cero`: «g = 1 − 2 + 1 = 0»
- «solo ruido» → `solo`: «0 < 4,5 → solo ruido», en gris
- «cuánto se parece lo recibido a la señal buscada» → `parece`: «g» se rotula «lo parecida que es r a s», con las dos series de barras alineadas

---

# Escena 07 — ElUmbral

**Capítulo YouTube:** ¿Dónde se pone el umbral?

## Narración

<!-- b1 -->
Miremos el umbral. Sobre una recta, marquemos dos valores de ge. Si no recibiéramos nada, ge valdría cero. Si recibiéramos la señal sin ruido, valdría la suma de los cuadrados de la señal: la energía, que aquí es cuatro más cuatro más uno, nueve. Con probabilidades iguales, el umbral es la energía entre dos: cuatro coma cinco, justo a mitad de camino.

- «Miremos el umbral» → `umbral`: un renglón «γ = σ² ln(p₀/p₁) + E/2» en la parte alta
- «una recta» → `recta`: una recta horizontal rotulada «g»
- «Si no recibiéramos nada» → `nada`: sobre la recta aparece la marca 0
- «ge valdría cero» → `g0`: «g = 0» junto a la marca
- «la señal sin ruido» → `sinruido`: las tres barras azules de la señal limpia entran
- «la suma de los cuadrados de la señal» → `cuadrados`: «Σ s²[n]»
- «la energía» → `energia`: «E» en azul, con rebote
- «cuatro más cuatro más uno» → `cuenta`: se construye «4 + 4 + 1»
- «nueve» → `nueve`: «E = 9» y una marca en 9 sobre la recta
- «Con probabilidades iguales» → `iguales`: «p₀ = p₁» y el logaritmo se tacha: «ln 1 = 0»
- «el umbral es la energía entre dos» → `emedio`: se queda «γ = E/2» en ámbar
- «cuatro coma cinco» → `cuatro`: una marca ámbar en 4,5
- «a mitad de camino» → `mitad`: dos flechas iguales entre 0, 4,5 y 9

<!-- b2 -->
Ahora una pregunta, y piénsala un momento antes de seguir. Si los aviones son raros, si pe uno baja a cero coma dos, ¿el umbral sube o baja? La cuenta: el logaritmo de cero coma ocho entre cero coma dos es el logaritmo de cuatro, uno coma tres ocho seis. El umbral sube a cinco coma ocho ocho seis.

- «una pregunta» → `pregunta`: aparece «¿sube o baja?» en ámbar
- «piénsala un momento» → `piensa`: una cuenta atrás de tres segundos, con un reloj de arena
- «si pe uno baja a cero coma dos» → `p1`: «p₁ = 0,2» en ámbar
- «¿el umbral sube o baja?» → `sube`: dos flechas, izquierda y derecha, con signo de interrogación
- «La cuenta» → `cuenta`: se construye «γ = 1 · ln(0,8 / 0,2) + 4,5»
- «el logaritmo de cero coma ocho» → `ln08`: se resalta «ln(0,8 / 0,2)»
- «es el logaritmo de cuatro» → `ln4b`: «= ln 4»
- «uno coma tres ocho seis» → `ln4`: «ln 4 = 1,386»
- «El umbral sube a cinco coma ocho ocho seis» → `sube2`: la marca ámbar se corre de 4,5 a 5,886, con la flecha a la derecha

<!-- b3 -->
Tiene sentido. Si los aviones son raros, hay que pedirle más evidencia al radar antes de creerle. Y si los aviones fueran muy frecuentes, el logaritmo sería negativo, el umbral bajaría y bastaría con menos evidencia. Con priors iguales, el logaritmo de uno es cero y volvemos al punto medio.

- «Tiene sentido» → `sentido`: un tilde verde sobre la marca en 5,886
- «los aviones son raros» → `raros`: pocos aviones pequeños en el cielo
- «más evidencia» → `evidencia`: la marca ámbar se aleja de la mitad hacia la derecha, y «más evidencia» en ámbar
- «antes de creerle» → `creerle`: un tilde sobre el radar, que espera
- «muy frecuentes» → `frecuentes`: el cielo se llena de aviones
- «el logaritmo sería negativo» → `neg`: aparece «ln(p₀/p₁) < 0»
- «el umbral bajaría» → `baja`: la marca va a la izquierda de 4,5
- «menos evidencia» → `menos`: «menos evidencia» en ámbar
- «el logaritmo de uno es cero» → `ln1`: «ln 1 = 0»
- «volvemos al punto medio» → `medio`: la marca vuelve a 4,5

---

# Escena 08 — ElPesoDelRuido

**Capítulo YouTube:** El ruido y el umbral

## Narración

<!-- b1 -->
La varianza del ruido también pesa. Multiplica al logaritmo. Si el ruido es muy pequeño, el radar se fía de lo que oye y las probabilidades a priori casi no importan. Si el ruido es grande, lo que oye vale poco y pesa más lo que sabía de antemano. El umbral se mueve más.

- «La varianza del ruido» → `varianza`: se resalta «σ²» en magenta en la fórmula del umbral
- «Multiplica al logaritmo» → `mult`: una flecha de σ² a «ln(p₀/p₁)»
- «muy pequeño» → `pequeno`: un deslizador de σ² a la izquierda; la campana de ruido se estrecha
- «se fía de lo que oye» → `fia`: un oído con un tilde
- «casi no importan» → `casino`: la marca del umbral casi no se mueve de 4,5 al variar p₁
- «el ruido es grande» → `grande`: el deslizador va a la derecha; la campana se ensancha
- «vale poco» → `poco`: el oído se atenúa
- «lo que sabía de antemano» → `antemano`: la etiqueta «a priori» en ámbar
- «El umbral se mueve más» → `mueve`: la marca recorre un tramo largo al variar p₁

<!-- b2 -->
Una advertencia importante. Hemos derivado esto con la regla de error mínimo. Pero en el capítulo de pruebas de hipótesis vimos otros criterios: Neyman-Pearson, riesgo mínimo. Con un ruido como este, todos llevan al mismo detector, calcular ge y compararlo. Lo único que cambia es dónde se pone el umbral. Veamos por qué.

- «Una advertencia importante» → `aviso`: un signo de exclamación en ámbar
- «la regla de error mínimo» → `map`: la etiqueta «error mínimo (MAP)» en ámbar
- «pruebas de hipótesis» → `cap9`: la etiqueta «Capítulo 9»
- «Neyman-Pearson» → `np`: la etiqueta «Neyman-Pearson»
- «riesgo mínimo» → `riesgo`: la etiqueta «riesgo mínimo»
- «Con un ruido como este» → `ruido`: aparece una campana magenta
- «mismo detector» → `mismo`: las tres etiquetas apuntan a una misma caja «g ≷ γ»
- «calcular ge y compararlo» → `calcular`: dentro de la caja, «g = Σ r s» y una marca de umbral
- «dónde se pone el umbral» → `donde`: de las tres etiquetas salen tres marcas distintas sobre la recta de g
- «Veamos por qué» → `veamos`: la caja «g ≷ γ» se enmarca en ámbar

---

# Escena 09 — LaSombraYLaPerpendicular

**Capítulo YouTube:** La sombra y la parte que sobra

## Narración

<!-- b1 -->
¿Por qué ge basta? Piensa en lo recibido como una flecha con tres números, y en la señal como otra flecha fija. Del capítulo siete: el producto escalar de las dos, que es justo ge, dice cuánto de una flecha cae en la dirección de la otra. Es la longitud de su sombra sobre la señal, multiplicada por la longitud de la señal.

- «¿Por qué ge basta?» → `basta`: entra la pregunta «¿por qué g basta?» en ámbar
- «lo recibido como una flecha con tres números» → `flecha_r`: una flecha cian en un espacio de tres ejes, con «(3, 1, 2)» en la punta
- «la señal como otra flecha fija» → `flecha_s`: una flecha azul «s = (2, 2, 1)»
- «el capítulo siete» → `cap7`: la etiqueta «Capítulo 7»
- «el producto escalar de las dos» → `escalar`: se construye «r · s»
- «que es justo ge» → `esge`: «= g» en ámbar
- «cuánto de una flecha cae en la dirección de la otra» → `cuanto`: una línea punteada baja desde la punta de r hasta la recta de s
- «la longitud de su sombra» → `sombra`: el tramo de s hasta ese pie se marca en cian
- «multiplicada por la longitud de la señal» → `largo`: se escribe «g = |sombra| · |s|»

<!-- b2 -->
Cualquier flecha se descompone en dos partes: la que va en la dirección de la señal y la que es perpendicular a ella. Ge es la parte paralela. ¿Qué pasa con la perpendicular? Sale solo del ruido. Y el ruido gaussiano no distingue direcciones: es una nube esférica. La señal la desplaza en la dirección de la señal, y en los planos perpendiculares las dos nubes son idénticas.

- «se descompone en dos partes» → `dos`: r se parte en dos flechas, una sobre s y otra a 90°
- «la que va en la dirección de la señal» → `paralela`: la componente paralela en cian
- «perpendicular a ella» → `perp`: la componente perpendicular en magenta, con el cuadradito de ángulo recto
- «Ge es la parte paralela» → `gpar`: «g» en ámbar junto a la componente paralela
- «¿Qué pasa con la perpendicular?» → `quepasa`: la componente perpendicular parpadea
- «Sale solo del ruido» → `solo`: una llave sobre ella: «solo ruido»
- «no distingue direcciones» → `direcciones`: flechas magenta cortas apuntan en todas las direcciones
- «una nube esférica» → `nube`: una nube de puntos magenta en forma de esfera, alrededor del origen
- «La señal la desplaza» → `desplaza`: una segunda nube, alrededor de la punta de s, aparece azulada
- «en la dirección de la señal» → `direccion`: una flecha ámbar de una nube a la otra, paralela a s
- «las dos nubes son idénticas» → `identicas`: un plano perpendicular a s corta las dos nubes: los dos cortes son círculos iguales

<!-- b3 -->
Es decir: la parte perpendicular tiene exactamente la misma distribución si hay avión o no. No aporta nada para decidir. Tirarla no cuesta nada. Todo lo que sirve está en ge. Eso es lo que significa ser un estadístico suficiente: un resumen que contiene toda la información relevante, ni más ni menos. Y ya vimos la señal de esto en la cuenta: la suma de cuadrados se canceló.

- «la misma distribución» → `misma`: los dos círculos se superponen en uno
- «si hay avión o no» → `avion`: junto al círculo, un avión y un avión tachado
- «No aporta nada para decidir» → `nada`: «no informa» en rojo junto a la perpendicular
- «Tirarla no cuesta nada» → `tirar`: la componente perpendicular se desvanece
- «Todo lo que sirve está en ge» → `todo`: «g» en ámbar queda como la única flecha
- «Eso es lo que significa» → `significa`: una lupa sobre «g»
- «un estadístico suficiente» → `suficiente`: «estadístico suficiente» entra con rebote
- «toda la información relevante» → `info`: la palabra «toda la información» en verde
- «ni más ni menos» → `nimas`: una balanza equilibrada
- «Y ya vimos la señal de esto» → `vimos`: una flecha hacia atrás, a la escena de la cuenta
- «la suma de cuadrados se canceló» → `cancelo`: reaparece «Σ r²» tachado, de la escena 05

---

# Escena 10 — UnCocienteCreciente

**Capítulo YouTube:** Por qué vale con cualquier criterio

## Narración

<!-- b1 -->
Segunda pregunta: ¿por qué con otros criterios sigue valiendo? Recuerda la razón de verosimilitud del capítulo nueve: el cociente de las dos densidades. Aquí vale e elevado a dos ge menos la energía, entre dos sigma cuadrado. Es una función siempre creciente de ge. Comparar ese cociente con un umbral es lo mismo que comparar ge con otro umbral.

- «Segunda pregunta» → `segunda`: entra «¿y con otros criterios?» en ámbar
- «¿por qué con otros criterios sigue valiendo?» → `otros`: aparecen tres etiquetas pequeñas, una por criterio
- «la razón de verosimilitud» → `razon`: entra «Λ» en ámbar
- «el cociente de las dos densidades» → `cociente`: se construye «Λ = f(r|H₁) / f(r|H₀)»
- «e elevado a dos ge menos la energía» → `exp`: se completa «= e^((2g − E) / 2σ²)»
- «entre dos sigma cuadrado» → `dossigma`: se resalta el denominador
- «siempre creciente de ge» → `creciente`: una gráfica de Λ contra g que sube siempre
- «Comparar ese cociente con un umbral» → `umbral_l`: una recta horizontal «η» corta la curva
- «lo mismo que comparar ge con otro umbral» → `umbral_g`: desde el punto de corte baja una vertical hasta «γ» en el eje de g

<!-- b2 -->
Así que Neyman-Pearson, riesgo mínimo o error mínimo dan el mismo detector. Solo cambia dónde se pone la marca. Y ahora el bucle del episodio: el promedio de las dos mediciones tiraba información; ge no tira nada. La diferencia es que ge sale de mirar cómo es el ruido, no de un resumen a ojo.

- «Neyman-Pearson, riesgo mínimo o error mínimo» → `tres`: las tres etiquetas de la escena 08 entran en fila
- «el mismo detector» → `mismo`: las tres señalan una caja «g ≷ γ»
- «dónde se pone la marca» → `marca`: tres marcas distintas sobre la recta de g
- «el bucle del episodio» → `bucle`: vuelven las dos mediciones del episodio anterior, con su cuadrado
- «el promedio de las dos mediciones» → `promedio`: «a = (r₁ + r₂) / 2» en ámbar
- «tiraba información» → `tiraba`: la etiqueta «error ¼: como no medir» en rojo
- «ge no tira nada» → `gnada`: «g» en ámbar con la etiqueta «suficiente» en verde
- «mirar cómo es el ruido» → `ruido`: la nube esférica magenta de la escena anterior
- «un resumen a ojo» → `ojo`: un ojo con una cruz roja junto al promedio

---

# Escena 11 — Cierre

**Capítulo YouTube:** Y ahora, ¿cuánto nos equivocamos?

## Narración

<!-- b1 -->
Resumamos. Una señal conocida enterrada en ruido gaussiano se decide con un solo número: ge, lo parecida que es lo recibido a la señal, comparada con un umbral. Ese número no tira nada, y con cualquier criterio sale el mismo detector. Ya sabemos qué calcular y dónde cortar. Falta saber cuánto vamos a equivocarnos, y de qué depende. En el próximo episodio: ¿cuánto nos equivocamos?

- «Resumamos» → `resumamos`: reaparece el pulso azul y la señal cian con ruido
- «Una señal conocida enterrada en ruido gaussiano» → `conocida`: pulso azul bajo una traza magenta que lo tapa
- «un solo número» → `numero`: la traza se comprime en una barra ámbar con «g»
- «lo parecida que es lo recibido a la señal» → `parecida`: las barras cian y azules se alinean
- «comparada con un umbral» → `umbral`: una marca «γ» en la recta de g
- «Ese número no tira nada» → `nada`: «suficiente» en verde
- «el mismo detector» → `mismo`: la caja «g ≷ γ» se enmarca
- «qué calcular» → `calcular`: se resalta «g»
- «dónde cortar» → `cortar`: se resalta «γ»
- «cuánto vamos a equivocarnos» → `equivocar`: aparecen las dos campanas del próximo episodio, en 0 y 9, con colas rojas
- «y de qué depende» → `depende`: las dos colas rojas se resaltan
- «¿cuánto nos equivocamos?» → `titulo`: el título del E3 en ámbar sobre las campanas
