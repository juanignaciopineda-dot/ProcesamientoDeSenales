# Episodio 7 — ¿Cuál de ellas mandaron?

Capítulo 13 (Detección de señales), episodio 7 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 27 a 31), más un gancho y un cierre nuevos.

**Estado:** `guion.md` con 19 escenas y momentos; escenas `s01`–`s19` animadas; borrador 480p15 de 11:05 con 0 avisos (hojas de contacto revisadas a ojo salvo el borrador unido). Falta: revisión del texto ⭐ (gancho y cierre de la serie, paso 9), visto bueno del usuario al mp4 (paso 15) y render final. Dura algo más de 10 min: candidato a recorte, el bloque 2 de la escena 11. El guion base del Cap. 13 sigue sin aprobarse.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Mismo pulso, misma energía y cincuenta veces menos errores. Hoy vemos por qué los módems envían cada bit y su contrario.»
- ⭐ Escena 19 (cierre), bloque 2: «Y con esto se cierra la serie. Gracias por acompañarnos hasta el final.» El bloque 1 es el final de la escena 31 del guion base, sin cambios. **Este cierre no anuncia ningún episodio: cierra toda la serie.**

Retoques de frases del guion base, porque el episodio se ve suelto (ya no hay «escenas» a las que remitir):
- escena 27, bloque 2 (ahora escena 03): «la derivación de la escena seis» → «la derivación del segundo episodio»;
- escena 27, bloque 4 (ahora escena 04): «Con números.» → «Con números, y con sigma cuadrado igual a uno.» (el guion base no decía cuánto vale σ² y las cuentas lo suponen);
- escena 29, bloque 2 (ahora escena 10): «el de la escena anterior» → «el del ejemplo anterior»;
- escena 30, bloque 3 (ahora escena 13): «como en la escena de las flechas» → «como cuando leímos el filtro en frecuencia».

Reparto de las escenas del guion base: 27 → escenas 03 a 05; 28 → 06 a 08; 29 → 09 a 11; 30 → 12 a 14; 31 → 15 a 19.
Solo se agruparon bloques enteros en escenas atómicas: el resto del texto del guion base no cambia.

Recorte posible (si `ritmo.py` pasa de ~10,5 min): el bloque 2 de la escena 11, la comparación honesta a igual energía media.

Bucles de este episodio: los priors que cambian al ganador (escenas 04 → 05; vienen del E3, escena 11); el pulso `(2, 2, 1)` con energía 9 (escenas 06 a 10); la parábola de Cauchy-Schwarz, su cuarta aparición (09 → 15); las tres señalizaciones con 0,0668 · 0,0170 · 0,00135 (10); el filtro adaptado y la autocorrelación del E4 (12 a 14); blanquear primero (E5 → 17 y 18); el radar, la búsqueda del pico y la receta (E6 → 18); la flecha y su sombra del Cap. 8 (17 y 19); la voz y el murmullo del Cap. 11 (19).

---

# Escena 01 — Gancho

**Capítulo YouTube:** Cincuenta veces menos errores

## Narración

<!-- b1 -->
Mismo pulso, misma energía y cincuenta veces menos errores. Hoy vemos por qué los módems envían cada bit y su contrario.

- «Mismo pulso» → `pulso`: entran las tres barras azules del pulso (2, 2, 1)
- «misma energía» → `energia`: junto al pulso aparece «E = 9» en ámbar
- «cincuenta veces menos errores» → `cincuenta`: dos barras rojas de error; la primera, alta, «0,0668», y la segunda, diminuta, «0,00135»
- «Hoy vemos por qué» → `hoy`: las barras de error se apartan y entra un módem pequeño
- «los módems envían» → `modem`: del módem salen pulsos hacia la derecha
- «cada bit y su contrario» → `contrario`: aparecen el pulso azul y, debajo, el mismo pulso invertido

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** ¿Cuál de ellas mandaron?

## Narración

<!-- b1 -->
¿Cuál de ellas mandaron?

- «¿Cuál de ellas» → `t1`: «¿Cuál de ellas» entra con rebote, con tres pulsos de colores debajo
- «mandaron?» → `t2`: «mandaron?» entra a continuación, con la etiqueta «Capítulo 13 · Detección de señales»

---

# Escena 03 — TresSenales

**Capítulo YouTube:** Decidir entre varias señales
**Objetivo:** pasar de «hay señal o no» a «cuál de M señales es» y repetir la derivación del segundo episodio con M hipótesis.

## Narración

<!-- b1 -->
Un módem no decide entre «hay señal» y «no hay»: decide entre varias señales posibles, una por cada símbolo que se pueda enviar. Tomemos tres, de cuatro muestras cada una y energía dos: uno, uno, cero, cero; cero, cero, uno, uno; y uno, menos uno, cero, cero. Bajo cada hipótesis, lo recibido es esa señal más ruido.

- «Un módem» → `modem`: entra el módem pequeño con su antena
- «no decide entre» → `nodecide`: dos casillas, «hay señal» y «no hay», aparecen tachadas
- «varias señales posibles» → `varias`: las casillas se funden en un abanico de tres pulsos distintos
- «una por cada símbolo» → `simbolo`: cada pulso recibe su letra: «0», «1», «2»
- «Tomemos tres» → `tres`: queda una fila con tres cuadros vacíos, uno por pulso
- «de cuatro muestras cada una» → `cuatro`: cada cuadro se divide en cuatro casillas
- «energía dos» → `energia`: sobre cada cuadro aparece «E = 2»
- «uno, uno, cero, cero» → `s0`: el primer cuadro se llena: «s₀ = (1, 1, 0, 0)» con barras
- «cero, cero, uno, uno» → `s1`: el segundo: «s₁ = (0, 0, 1, 1)»
- «uno, menos uno, cero, cero» → `s2`: el tercero: «s₂ = (1, −1, 0, 0)», con la segunda barra hacia abajo
- «Bajo cada hipótesis» → `hip`: encima de cada cuadro, «H₀», «H₁», «H₂»
- «esa señal más ruido» → `masruido`: «r = s_i + ruido» con el ruido en magenta bajo la fila

<!-- b2 -->
Repetimos la derivación del segundo episodio. Comparamos las densidades escaladas por sus priors, tomamos logaritmos, desarrollamos el cuadrado. Y ahora la suma de cuadrados de lo recibido es común a todas las hipótesis, no solo a dos: se cancela. Queda: elegir la hipótesis que maximice la suma de recibido por señal, más sigma cuadrado por el logaritmo de su prior, menos su energía entre dos.

- «Repetimos la derivación» → `repetimos`: arriba, una copia en miniatura de la derivación del segundo episodio, con las mismas piezas
- «segundo episodio» → `segundo`: sobre la copia aparece el rótulo «episodio 2»
- «las densidades escaladas por sus priors» → `densidades`: «p_i · f(r | H_i)» para las tres hipótesis, en tres renglones
- «tomamos logaritmos» → `logs`: «ln» delante de cada renglón
- «desarrollamos el cuadrado» → `cuadrado`: «(r − s_i)²» se abre en «r² − 2 r s_i + s_i²»
- «la suma de cuadrados de lo recibido» → `sumacuad`: «Σ r²» se resalta en cada uno de los tres renglones
- «común a todas las hipótesis» → `comun`: una llave recorre los tres renglones sobre la «Σ r²»
- «se cancela» → `cancela`: la «Σ r²» se tacha en los tres a la vez
- «Queda» → `queda`: los tres renglones se encogen y suben, y abajo se despeja el resultado
- «elegir la hipótesis que maximice» → `maximice`: aparece el marco «elegir la i que maximice»
- «la suma de recibido por señal» → `rs`: «Σ r s_i» entra en el marco, en cian y azul
- «más sigma cuadrado por el logaritmo de su prior» → `prior`: «+ σ² ln P(H_i)» entra en ámbar
- «menos su energía entre dos» → `mediaenergia`: «− E_i / 2» entra en azul

---

# Escena 04 — FiltrosEnParalelo

**Capítulo YouTube:** Un filtro adaptado por señal
**Objetivo:** ver que se implementa con M filtros adaptados y un «elegir el mayor», y hacer la cuenta a mano con tres señales.

## Narración

<!-- b1 -->
Se implementa con tantos filtros adaptados como señales, en paralelo, y un bloque que elige la salida mayor. Y si todas las señales tienen la misma energía y la misma probabilidad, los dos últimos términos son iguales para todas: gana el filtro con la salida más grande.

- «Se implementa» → `implementa`: el resultado de la escena anterior sube y se achica a un rincón
- «tantos filtros adaptados como señales» → `filtros`: tres cajas «filtro adaptado a s₀, s₁, s₂» aparecen apiladas
- «en paralelo» → `paralelo`: la entrada «r» entra desde la izquierda y se reparte a las tres cajas
- «un bloque que elige la salida mayor» → `elige`: a la derecha, un bloque ámbar «elegir el mayor» recibe las tres salidas
- «Y si todas las señales» → `ysi`: las tres cajas se vuelven a ver completas, con «E igual, P igual»
- «la misma energía» → `igualenergia`: en el rincón, «− E_i / 2» se marca con «igual en las tres»
- «la misma probabilidad» → `igualprior`: «σ² ln P(H_i)» se marca igual
- «son iguales para todas» → `iguales`: los dos términos se tachan
- «gana el filtro con la salida más grande» → `gana`: la salida mayor se enciende en verde y el bloque señala esa

<!-- b2 -->
Con números, y con sigma cuadrado igual a uno. Recibimos cero coma cuatro, uno, cero coma nueve, cero coma siete. Primera señal: cero coma cuatro más uno, uno coma cuatro. Segunda: cero coma nueve más cero coma siete, uno coma seis. Tercera: cero coma cuatro menos uno, menos cero coma seis. Gana la segunda, por poco.

- «Con números» → `numeros`: la cadena de filtros se aparta y entra una fila de cuatro casillas vacías
- «sigma cuadrado igual a uno» → `sigma`: aparece «σ² = 1» en magenta
- «cero coma cuatro, uno» → `recibido`: las dos primeras casillas se llenan: «r = (0,4; 1; …» en cian
- «cero coma nueve, cero coma siete» → `recibido2`: las otras dos: «…; 0,9; 0,7)»
- «Primera señal» → `primera`: debajo, «s₀ = (1, 1, 0, 0)» alineada con las casillas
- «uno coma cuatro» → `g0`: «0,4 + 1 = 1,4» y aparece «g₀ = 1,4»
- «Segunda» → `segunda`: «s₁ = (0, 0, 1, 1)» alineada
- «uno coma seis» → `g1`: «0,9 + 0,7 = 1,6» y aparece «g₁ = 1,6»
- «Tercera» → `tercera`: «s₂ = (1, −1, 0, 0)» alineada
- «menos cero coma seis» → `g2`: «0,4 − 1 = −0,6» y aparece «g₂ = −0,6»
- «Gana la segunda» → `ganalasegunda`: «g₁ = 1,6» se enciende en verde y las otras se apagan
- «por poco» → `porpoco`: entre «1,4» y «1,6» aparece una pequeña llave con «0,2»

---

# Escena 05 — ElGiroDelPrior

**Capítulo YouTube:** Lo que sabías de antemano
**Objetivo:** que el mismo dato, con otros priors, cambie la decisión: el prior pesa cuando la evidencia está reñida.

## Narración

<!-- b1 -->
Ahora un giro. Supongamos que la primera señal es la más probable, un medio, y las otras, un cuarto. A cada resultado le sumamos el logaritmo de su prior y le restamos la energía entre dos, uno. Sale menos cero coma veintinueve, menos cero coma setenta y nueve, menos dos coma noventa y nueve. ¡Ahora gana la primera! Mismo dato, otra decisión: lo que sabías de antemano pesa cuando la evidencia está reñida.

- «Ahora un giro» → `giro`: vuelven las tres sumas «1,4 · 1,6 · −0,6» y aparece la palabra «giro» en ámbar
- «la primera señal es la más probable» → `probable`: junto a s₀ aparece «P(H₀) = ½»
- «un medio» → `medio`: el «½» se agranda con un pop
- «las otras, un cuarto» → `cuarto`: junto a s₁ y s₂ aparece «¼» en cada una
- «le sumamos el logaritmo de su prior» → `suma`: bajo cada suma entra «+ ln P(H_i)»
- «le restamos la energía entre dos, uno» → `resta`: bajo cada suma entra «− E_i/2 = −1»
- «menos cero coma veintinueve» → `r0`: el primer renglón se completa: «1,4 − 0,69 − 1 = −0,29»
- «menos cero coma setenta y nueve» → `r1`: el segundo: «1,6 − 1,39 − 1 = −0,79»
- «menos dos coma noventa y nueve» → `r2`: el tercero: «−0,6 − 1,39 − 1 = −2,99»
- «¡Ahora gana la primera!» → `ganaprimera`: «−0,29» se enciende en verde y la corona pasa de la segunda señal a la primera
- «Mismo dato, otra decisión» → `mismodato`: a un lado, el resultado anterior «gana 1» y el nuevo «gana 0», unidos por una flecha de cambio
- «pesa cuando la evidencia está reñida» → `renida`: la pequeña llave de «0,2» vuelve a aparecer entre 1,4 y 1,6, ahora superada por el peso del prior

---

# Escena 06 — UnSoloFiltro

**Capítulo YouTube:** Con dos señales, un solo filtro
**Objetivo:** reducir M = 2 a un único filtro adaptado a la diferencia, y calcular esa diferencia con el pulso del capítulo.

## Narración

<!-- b1 -->
Con dos señales, la regla se simplifica mucho: basta un único filtro adaptado a la diferencia entre las dos. Ge es la suma de recibido por la señal uno menos la señal cero. Lo que importa no es cada señal por separado, sino en qué se distinguen: la parte que tienen en común no ayuda a decidir.

- «Con dos señales» → `dos`: de los tres filtros en paralelo quedan solo dos
- «la regla se simplifica mucho» → `simplifica`: los dos filtros se funden en uno solo
- «un único filtro adaptado» → `unico`: una caja «filtro adaptado» con una flecha de entrada «r»
- «a la diferencia entre las dos» → `difs`: dentro de la caja aparece «s₁ − s₀»
- «Ge es la suma de recibido» → `ge`: debajo, «g = Σ r ·» entra con «r» en cian
- «por la señal uno menos la señal cero» → `uno_menos_cero`: se completa «(s₁ − s₀)»
- «no es cada señal por separado» → `separado`: s₁ y s₀ aparecen separadas, con un «✗» pequeño
- «en qué se distinguen» → `distinguen`: entre las dos barras aparece una llave con la parte distinta
- «la parte que tienen en común» → `comun`: la parte coincidente se pinta de gris
- «no ayuda a decidir» → `noayuda`: la parte gris se desvanece y queda solo lo distinto

<!-- b2 -->
Un ejemplo. La señal uno, dos, dos, uno. La señal cero, dos, menos uno, menos dos. Las dos tienen energía nueve. Su diferencia es cero, tres, tres: la primera muestra, que tienen igual, desaparece. La longitud de la diferencia es la raíz de dieciocho, cuatro coma dos cuatro.

- «Un ejemplo» → `ejemplo`: entra el rótulo «ejemplo» y un par de ejes vacíos
- «La señal uno» → `uno`: entra el pulso de siempre en azul, con «s₁ = (2, 2, 1)»
- «La señal cero» → `cero`: debajo, el eje de «s₀» vacío
- «menos uno, menos dos» → `negativas`: «s₀ = (2, −1, −2)» en otro azul, con la segunda y la tercera barra hacia abajo
- «energía nueve» → `nueve`: a la derecha de cada una, «E = 4 + 1 + 4 = 9»
- «Su diferencia» → `diferencia`: debajo, tres casillas vacías para «s₁ − s₀»
- «cero, tres, tres» → `cerotrestres`: las casillas se llenan: «(0, 3, 3)»
- «la primera muestra, que tienen igual» → `primera`: las dos primeras barras, ambas de altura dos, se resaltan
- «desaparece» → `desaparece`: la primera casilla se vuelve gris y la barra se desvanece
- «La longitud de la diferencia» → `longitud`: una flecha con la longitud «‖s₁ − s₀‖»
- «raíz de dieciocho» → `raiz`: «√(0 + 9 + 9) = √18»
- «cuatro coma dos cuatro» → `cuatro24`: «= 4,24» en ámbar

---

# Escena 07 — CuantoNosEquivocamos

**Capítulo YouTube:** El error entre dos señales
**Objetivo:** calcular a mano P_e = Q(2,12) = 0,017 con las dos campanas de g.

## Narración

<!-- b1 -->
¿Cuánto nos equivocamos? Con probabilidades y energías iguales, el umbral es cero. Bajo la hipótesis uno, ge tiene media la señal uno por la diferencia: nueve. Bajo la cero, menos nueve. Y ambos con desvío cuatro coma dos cuatro. Nueve entre cuatro coma dos cuatro es dos coma doce, y cu de dos coma doce vale cero coma cero uno siete.

- «¿Cuánto nos equivocamos?» → `pregunta`: aparece «P_e = ?» en rojo
- «Con probabilidades y energías iguales» → `iguales`: a un lado, «p₀ = p₁» y «E₀ = E₁» en ámbar
- «el umbral es cero» → `umbral`: un eje horizontal con una línea vertical en 0, «umbral = 0»
- «Bajo la hipótesis uno» → `h1`: se dibuja una campana hacia la derecha, en cian
- «ge tiene media» → `media`: sobre la campana, «E[g | H₁]»
- «la señal uno por la diferencia» → `producto`: «s₁ · (s₁ − s₀) = 4 + 2 = ...»; la cuenta con (2, 2, 1) y (0, 3, 3)
- «nueve» → `nueve`: «= 9» y la campana queda centrada en «+9»
- «Bajo la cero» → `h0`: se dibuja la campana de la izquierda
- «menos nueve» → `menosnueve`: centrada en «−9»
- «desvío cuatro coma dos cuatro» → `desvio`: ambas campanas con un pequeño «σ_g = 4,24»
- «Nueve entre cuatro coma dos cuatro» → `division`: «9 / 4,24» aparece junto al umbral
- «dos coma doce» → `dos12`: «= 2,12» y una flecha de 0 a 9 marcada con ese número de desvíos
- «cu de dos coma doce» → `q`: «Q(2,12)» aparece y la cola roja de una campana se rellena
- «cero coma cero uno siete» → `valor`: «= 0,017» en rojo

---

# Escena 08 — DistanciaEnDesvios

**Capítulo YouTube:** La distancia entre señales
**Objetivo:** llegar a P_e = Q(‖s₁ − s₀‖/2σ) y a la geometría: dos puntos, nubes redondas y frontera perpendicular; plantear la pregunta de X.

## Narración

<!-- b1 -->
Es la misma cuenta de siempre, y generaliza. El error es cu de la longitud de la diferencia entre dos sigma: la distancia entre las señales, medida en desvíos del ruido. Geométricamente, dos puntos, cada uno rodeado de una nube redonda de ruido. La regla óptima traza una frontera perpendicular por el punto medio.

- «la misma cuenta de siempre» → `misma`: la campana con «Q(2,12)» baja a un rincón
- «y generaliza» → `generaliza`: «P_e = Q( ... )» aparece con el hueco vacío
- «cu de la longitud de la diferencia» → `longitud`: el hueco se llena con «‖s₁ − s₀‖»
- «entre dos sigma» → `dossigma`: debajo de la longitud aparece «2σ»
- «la distancia entre las señales» → `distancia`: el numerador se resalta en ámbar
- «medida en desvíos del ruido» → `desvios`: una regla con marcas de tamaño σ aparece bajo la fórmula
- «Geométricamente» → `geo`: aparece un plano vacío con ejes
- «dos puntos» → `puntos`: un plano con dos puntos, «s₀» y «s₁»
- «una nube redonda de ruido» → `nubes`: alrededor de cada punto, una nube redonda de radio σ, en magenta
- «La regla óptima» → `optima`: aparece el punto medio entre s₀ y s₁
- «una frontera perpendicular» → `frontera`: una recta vertical, perpendicular al segmento, por el punto medio
- «por el punto medio» → `medio`: marca de ángulo recto y de las dos mitades iguales

<!-- b2 -->
Llamemos equis a la suma de una señal por la otra: cuánto se parecen. La longitud al cuadrado de la diferencia vale dos veces la energía menos dos equis. Cuanto menos se parezcan las dos señales, más lejos están los puntos y menos nos equivocamos. Para minimizar el error, hay que hacer equis lo más negativo posible. ¿Hasta dónde puede bajar?

- «Llamemos equis» → `equis`: «X = s₀ · s₁» aparece en ámbar
- «cuánto se parecen» → `parecen`: dos flechas con un ángulo entre ellas
- «La longitud al cuadrado de la diferencia» → `long2`: «‖s₁ − s₀‖²» a la izquierda
- «dos veces la energía» → `dos_e`: «= 2E» se completa
- «menos dos equis» → `menos_x`: «− 2X» entra en ámbar
- «Cuanto menos se parezcan» → `menos`: las dos flechas se abren más
- «más lejos están los puntos» → `lejos`: los dos puntos del plano se separan
- «menos nos equivocamos» → `menoserror`: las nubes se solapan menos y el área roja de la frontera se achica
- «hay que hacer equis lo más negativo posible» → `negativo`: «X» se desplaza hacia la izquierda sobre una recta numérica
- «¿Hasta dónde puede bajar?» → `hasta`: la recta numérica se queda con un signo «?» a la izquierda

---

# Escena 09 — LaCotaDeCauchySchwarz

**Capítulo YouTube:** Cauchy-Schwarz otra vez
**Objetivo:** ver que X no baja de −E (Cauchy-Schwarz), con igualdad en s₁ = −s₀: señalización antipodal. Es la cuarta aparición de la parábola.

## Narración

<!-- b1 -->
Equis es la suma de una señal por la otra, y las dos tienen la misma energía. ¿Hasta dónde puede bajar? Aquí aparece, por última vez en el capítulo, Cauchy-Schwarz: equis al cuadrado no supera la energía por la energía. Así que equis no baja de menos la energía, y llega justo ahí cuando una señal es la otra con el signo cambiado. Se llama señalización antipodal.

- «Equis es la suma de una señal por la otra» → `equis`: «X = s₀ · s₁» vuelve del escenario anterior
- «las dos tienen la misma energía» → `energia`: «E₀ = E₁ = E» en ámbar
- «¿Hasta dónde puede bajar?» → `bajar`: la recta numérica con «X» y un «?» a la izquierda
- «Aquí aparece» → `aparece`: la recta numérica se corre a un lado
- «por última vez en el capítulo» → `ultima`: aparece el rótulo «4.ª vez» en ámbar
- «Cauchy-Schwarz» → `cs`: aparece la parábola de siempre, el mismo dibujo, con «Cauchy-Schwarz» encima
- «equis al cuadrado no supera» → `cuadrado`: «X² ≤ ...» se escribe junto a la parábola
- «la energía por la energía» → `ee`: se completa «X² ≤ E · E = E²»
- «equis no baja de menos la energía» → `cota`: «X ≥ −E» y en la recta numérica un tope en −E
- «llega justo ahí» → `justo`: el valor «X» baja hasta tocar el tope
- «la otra con el signo cambiado» → `signo`: debajo, «s₁ = −s₀»; el pulso azul y su espejo en el eje
- «señalización antipodal» → `antipodal`: la palabra «antipodal» entra con rebote, en ámbar

---

# Escena 10 — TresManeras

**Capítulo YouTube:** Tres maneras de enviar un bit
**Objetivo:** comparar on-off, ortogonal y antipodal con el pulso (2, 2, 1): 0,0668 · 0,0170 · 0,00135.

## Narración

<!-- b1 -->
Comparemos tres maneras de enviar un bit con el mismo pulso, dos, dos, uno, de energía nueve, y sigma uno. La primera, on-off: enviamos el pulso o no enviamos nada. La distancia es tres, y el error, cu de uno coma cinco: cero coma cero seis seis ocho. La segunda, ortogonal: el pulso contra el del ejemplo anterior. Distancia cuatro coma dos cuatro: cero coma cero uno siete.

- «Comparemos tres maneras» → `tres`: tres columnas vacías, con las etiquetas «on-off», «ortogonal», «antipodal»
- «el mismo pulso» → `pulso`: el pulso (2, 2, 1) aparece sobre las tres columnas
- «de energía nueve» → `nueve`: «E = 9» sobre el pulso
- «sigma uno» → `sigma`: «σ = 1» en magenta
- «La primera, on-off» → `onoff`: la primera columna se enciende
- «enviamos el pulso o no enviamos nada» → `pulsono`: dos puntos en el plano: uno en el origen, otro en (2, 2, 1)
- «La distancia es tres» → `tres3`: segmento entre los dos puntos con «3»
- «cu de uno coma cinco» → `q15`: «Q(3 / 2) = Q(1,5)»
- «cero coma cero seis seis ocho» → `v668`: «0,0668» en rojo con dos campanas de solape
- «La segunda, ortogonal» → `orto`: la segunda columna se enciende
- «el pulso contra el del ejemplo anterior» → `ejant`: dos puntos, s₁ = (2, 2, 1) y s₀ = (2, −1, −2), con ángulo recto marcado
- «Distancia cuatro coma dos cuatro» → `d424`: segmento con «4,24»
- «cero coma cero uno siete» → `v017`: «0,0170» en rojo, con las campanas más separadas

<!-- b2 -->
La tercera, antipodal: el pulso contra el mismo pulso cambiado de signo. La distancia es seis, el doble que en on-off, y el error, cu de tres: cero coma cero cero uno tres cinco. Piénsalo un momento: con el mismo pulso y la misma energía, ¿cuántas veces menos errores? Cerca de cincuenta.

- «La tercera, antipodal» → `anti`: la tercera columna se enciende
- «el mismo pulso cambiado de signo» → `cambiado`: dos puntos, s₁ = (2, 2, 1) y s₀ = (−2, −2, −1), simétricos respecto del origen
- «La distancia es seis» → `seis`: segmento con «6»
- «el doble que en on-off» → `doble`: el segmento de on-off, de 3, reaparece al lado y cabe dos veces
- «cu de tres» → `q3`: «Q(3)»
- «cero coma cero cero uno tres cinco» → `v135`: «0,00135» en rojo, con las campanas casi sin solape
- «Piénsalo un momento» → `piensalo`: aparece un reloj de arena y la pregunta grande
- «¿cuántas veces menos errores?» → `cuantas`: «0,0668 / 0,00135 = ?»
- «Cerca de cincuenta» → `cincuenta`: «≈ 50» en verde con un pop

---

# Escena 11 — LaEscaleraDeEnergia

**Capítulo YouTube:** Antipodal gana por tres decibelios
**Objetivo:** medir la ventaja en energía (73 · 36 · 18) y dar la comparación honesta con la potencia media.

## Narración

<!-- b1 -->
Otra manera de verlo: cuánta energía hace falta para tener un error de uno entre cien mil. Con antipodal, dieciocho. Con ortogonal, treinta y seis, el doble. Con on-off, setenta y tres, el cuádruple. Tres decibelios de diferencia entre cada escalón. Duplicar la distancia es lo mismo que cuadruplicar la relación señal-ruido.

- «Otra manera de verlo» → `otra`: las tres columnas bajan y entra una escalera de tres peldaños, vacía
- «un error de uno entre cien mil» → `error`: sobre la escalera, «P_e = 10⁻⁵» en rojo
- «Con antipodal, dieciocho» → `d18`: el peldaño de más abajo, con «E ≈ 18»
- «Con ortogonal, treinta y seis» → `d36`: el siguiente, con «E ≈ 36»
- «el doble» → `doble`: una llave marca «× 2» entre los dos peldaños
- «Con on-off, setenta y tres» → `d73`: el peldaño de arriba, con «E ≈ 73»
- «el cuádruple» → `cuadruple`: una llave marca «× 4» entre el primer peldaño y el último
- «Tres decibelios» → `tresdb`: junto a cada escalón, «3 dB»
- «entre cada escalón» → `escalon`: las dos llaves «3 dB» y «3 dB» se encienden en ámbar
- «Duplicar la distancia» → `duplicar`: dos segmentos, uno el doble del otro
- «cuadruplicar la relación señal-ruido» → `cuadruplicar`: «distancia × 2 = SNR × 4»

<!-- b2 -->
Una advertencia honesta. On-off no transmite nada la mitad del tiempo, así que gasta la mitad de energía. Si comparas a igual energía media, on-off empata con ortogonal, y antipodal sigue ganando por tres decibelios. Por eso casi todos los sistemas digitales usan antipodal, o alguna variante suya.

- «Una advertencia honesta» → `honesta`: aparece un cartel «ojo»
- «On-off no transmite nada la mitad del tiempo» → `mitad`: una tira de tiempo con la mitad de los bits en blanco
- «gasta la mitad de energía» → `gasta`: «E media = E / 2» bajo la tira
- «a igual energía media» → `igual`: las tres columnas se nivelan en un mismo peldaño de energía
- «on-off empata con ortogonal» → `empata`: on-off y ortogonal quedan a la misma altura, con un «=»
- «antipodal sigue ganando» → `sigue`: antipodal queda más abajo
- «tres decibelios» → `tres`: la llave «3 dB» entre antipodal y los otros dos
- «casi todos los sistemas digitales» → `digitales`: aparecen pequeños íconos de módem, móvil y wifi
- «antipodal, o alguna variante suya» → `variante`: sobre los íconos se enciende «antipodal» en ámbar

---

# Escena 12 — Interferencia

**Capítulo YouTube:** Pulsos que se pisan
**Objetivo:** recordar PAM, la interferencia entre símbolos y la condición de Nyquist, y por qué con ruido el receptor es el adaptado.

## Narración

<!-- b1 -->
Un módem envía un pulso por cada símbolo, uno detrás de otro. Del capítulo tres, PAM: si los pulsos son largos, se solapan, y cada símbolo se mezcla con sus vecinos. Es la interferencia entre símbolos. El criterio de Nyquist pide que el pulso total valga uno en su instante de muestreo y cero en los instantes de todos los demás.

- «Un módem envía un pulso» → `envia`: el módem pequeño lanza un pulso hacia la derecha
- «por cada símbolo» → `simbolo`: una fila de símbolos, «+1, −1, +1», cada uno con su pulso
- «uno detrás de otro» → `detras`: los pulsos se colocan en fila, separados por un intervalo T
- «PAM» → `pam`: la palabra «PAM» entra con rebote
- «si los pulsos son largos» → `largos`: los pulsos se ensanchan
- «se solapan» → `solapan`: las colas de los pulsos vecinos se cruzan y se suman
- «cada símbolo se mezcla con sus vecinos» → `mezcla`: las dos colas vecinas se pintan en rojo bajo el pulso del medio
- «interferencia entre símbolos» → `isi`: el rótulo «interferencia entre símbolos» en rojo
- «El criterio de Nyquist» → `nyquist`: el nombre «Nyquist» entra
- «valga uno en su instante de muestreo» → `uno`: una marca de muestreo en el pico, «1»
- «cero en los instantes de todos los demás» → `cero`: en los instantes de los vecinos, la curva cruza el cero con puntos verdes

<!-- b2 -->
Sin ruido, esto se resolvía diseñando un pulso que cumpliera esa condición. Con ruido, sabemos que el receptor óptimo es el filtro adaptado al pulso que llega. Si el transmisor envía un pulso pe, y el canal tiene una respuesta hache de ce, el pulso que llega es el producto. El receptor tiene su conjugado.

- «Sin ruido» → `sinruido`: una curva limpia, sin ruido, con la condición de Nyquist cumplida
- «diseñando un pulso» → `disenando`: un lápiz dibuja el pulso con los ceros en su sitio
- «Con ruido» → `conruido`: el ruido magenta se suma a la curva
- «el receptor óptimo» → `optimo`: una caja «receptor» aparece al final de una cadena
- «el filtro adaptado» → `adaptado`: la caja se rotula «filtro adaptado» en ámbar
- «al pulso que llega» → `llega`: una flecha apunta desde el pulso recibido a la caja
- «un pulso pe» → `pe`: la cadena «transmisor → canal → receptor»; sobre el transmisor, «P»
- «una respuesta hache de ce» → `hc`: sobre el canal, «H_c»
- «el pulso que llega es el producto» → `producto`: entre el canal y el receptor, «P · H_c»
- «El receptor tiene su conjugado» → `conjugado`: dentro del receptor, «conj(P · H_c)»

---

# Escena 13 — ElPulsoTotal

**Capítulo YouTube:** El pulso total es real y positivo
**Objetivo:** calcular P·H_c·conj(P·H_c) = |P|²|H_c|² y concluir que Nyquist se impone a |P|².

## Narración

<!-- b1 -->
Y el pulso total, tras el canal y el receptor, es el producto de esas cosas: pe por hache de ce, por su conjugado. Es el cuadrado del módulo de pe por el cuadrado del módulo de hache de ce. Es real y positivo: la fase se ha cancelado, como cuando leímos el filtro en frecuencia. Así que la condición de Nyquist ya no se impone al pulso enviado, sino a su módulo al cuadrado.

- «el pulso total» → `total`: toda la cadena se encierra en un marco: «pulso total»
- «tras el canal y el receptor» → `tras`: se resaltan el canal y el receptor
- «pe por hache de ce» → `pehc`: aparece «P · H_c ·»
- «por su conjugado» → `porconj`: se completa «conj(P · H_c)»
- «el cuadrado del módulo de pe» → `modp`: «= |P|²» entra en azul
- «por el cuadrado del módulo de hache de ce» → `modhc`: «· |H_c|²» entra en azul
- «Es real y positivo» → `real`: una flecha compleja de ángulo cualquiera, con el ángulo marcado en la fórmula
- «la fase se ha cancelado» → `fase`: la flecha gira hasta ángulo cero sobre el eje real
- «cuando leímos el filtro en frecuencia» → `recuerdo`: aparece un rincón con el recuerdo: flechas que giran en el plano complejo
- «la condición de Nyquist ya no se impone al pulso enviado» → `noenviado`: «P» con un «✗»
- «sino a su módulo al cuadrado» → `sino`: «|P|²» en ámbar con un «✓» y la frase «Nyquist se impone a |P|², no a P»

---

# Escena 14 — RaizDeCosenoAlzado

**Capítulo YouTube:** La raíz del coseno alzado
**Objetivo:** repartir el conformado entre transmisor y receptor, y cerrar el detector: máxima SNR y cero interferencia a la vez.

## Narración

<!-- b1 -->
Una consecuencia práctica. Si el pulso deseado, el que cumple Nyquist, es un coseno alzado, el transmisor y el receptor se reparten el trabajo: cada uno aplica la raíz de ese pulso. Es el filtro raíz de coseno alzado, que está en casi todos los módems. La mitad del conformado se hace en el transmisor, y la otra mitad, en el receptor.

- «Una consecuencia práctica» → `practica`: queda a la vista el «|P|²» resaltado
- «el pulso deseado, el que cumple Nyquist» → `deseado`: un pulso con ceros en los vecinos, en verde
- «es un coseno alzado» → `coseno`: la curva se rotula «coseno alzado»
- «el transmisor y el receptor» → `reparten`: la cadena con las cajas «transmisor» y «receptor» destacadas
- «se reparten el trabajo» → `trabajo`: del pulso deseado salen dos mitades iguales hacia las dos cajas
- «cada uno aplica la raíz de ese pulso» → `raiz`: dentro de cada caja, «√» del pulso deseado
- «Es el filtro» → `filtro`: las dos cajas se vuelven a mostrar con el signo «√»
- «raíz de coseno alzado» → `rcos`: el nombre completo «raíz de coseno alzado» entra con rebote
- «casi todos los módems» → `todos`: varios módems pequeños alrededor
- «La mitad del conformado» → `mitad`: el pulso se parte en dos mitades
- «en el transmisor» → `tx`: una mitad entra en el transmisor
- «la otra mitad, en el receptor» → `rx`: la otra entra en el receptor

<!-- b2 -->
Así, con un solo reparto, se cumplen dos exigencias a la vez: la máxima relación señal-ruido en el receptor, y ninguna interferencia entre símbolos. No hay que elegir entre las dos. Y con esto tenemos todas las piezas del detector. Vamos a mirar el conjunto.

- «con un solo reparto» → `reparto`: las dos mitades se unen con un único marco
- «dos exigencias a la vez» → `dos`: aparecen dos casillas vacías
- «la máxima relación señal-ruido» → `snr`: la primera casilla, «máxima SNR», con un tilde
- «ninguna interferencia entre símbolos» → `noisi`: la segunda, «cero interferencia», con un tilde
- «No hay que elegir» → `noelegir`: ambos tildes se encienden en verde a la vez
- «todas las piezas del detector» → `piezas`: debajo, el filtro adaptado, el muestreo y el umbral, como piezas de un rompecabezas
- «mirar el conjunto» → `conjunto`: las piezas encajan y la cámara se aleja

---

# Escena 15 — LaCuartaParabola

**Capítulo YouTube:** La parábola de Cauchy-Schwarz
**Objetivo:** recordar las cuatro apariciones de la parábola de Cauchy-Schwarz en el curso.

## Narración

<!-- b1 -->
Un último vistazo. La parábola de Cauchy-Schwarz ha aparecido cuatro veces. En el capítulo siete, para probar que rho no pasa de uno. En el diez, para acotar la covarianza del sensor. En el once, para la coherencia. Y aquí, para el filtro adaptado. Siempre el mismo truco: una suma de cuadrados no puede ser negativa.

- «Un último vistazo» → `vistazo`: aparece el rótulo «Cauchy-Schwarz» en ámbar
- «La parábola de Cauchy-Schwarz» → `parabola`: aparece la parábola de siempre, el mismo dibujo
- «cuatro veces» → `cuatro`: cuatro marcas vacías alrededor de la parábola
- «En el capítulo siete» → `cap7`: la primera marca se enciende: «ρ ≤ 1 (cap. 7)»
- «rho no pasa de uno» → `rho`: «|ρ| ≤ 1» junto a la marca
- «En el diez» → `cap10`: la segunda: «covarianza acotada (cap. 10)»
- «la covarianza del sensor» → `sensor`: aparece el termómetro del sensor
- «En el once» → `cap11`: la tercera: «coherencia ≤ 1 (cap. 11)»
- «la coherencia» → `coh`: «γ ≤ 1» junto a la marca
- «Y aquí» → `aqui`: la cuarta: «filtro adaptado (cap. 13)» en ámbar
- «el filtro adaptado» → `adaptado`: la pequeña ecuación «X ≥ −E» junto a la marca
- «una suma de cuadrados no puede ser negativa» → `suma`: la parábola se pinta en verde por encima del eje, con «Σ (…)² ≥ 0»

---

# Escena 16 — WienerContraAdaptado

**Capítulo YouTube:** Wiener contra adaptado
**Objetivo:** distinguir el filtro de Wiener (estimar la forma) del adaptado (decidir si hay señal), y recordar que ambos blanquean primero.

## Narración

<!-- b1 -->
Este capítulo y el anterior se parecen mucho, y conviene no confundirlos. El filtro de Wiener del capítulo doce estima la forma de una señal aleatoria, muestra a muestra, minimizando el error cuadrático. El filtro adaptado decide si hay una señal conocida, y se queda con un solo número. Los dos, cuando el ruido tiene color, hacen lo mismo primero: blanquear.

- «Este capítulo y el anterior» → `capitulos`: dos columnas, «Wiener (cap. 12)» y «adaptado (cap. 13)»
- «se parecen mucho» → `parecen`: una flecha doble entre ellas
- «no confundirlos» → `confundir`: la flecha doble se tacha con un «≠»
- «El filtro de Wiener» → `wiener`: se enciende la primera columna, en ámbar
- «estima la forma de una señal aleatoria» → `forma`: debajo, una curva que sigue a una señal
- «muestra a muestra» → `muestra`: sobre la curva, puntos en cada muestra
- «minimizando el error cuadrático» → `error`: «mín E[e²]» en rojo
- «El filtro adaptado» → `adapt`: se enciende la segunda columna
- «decide si hay una señal conocida» → `decide`: debajo, un pulso conocido con una pregunta «¿hay?»
- «un solo número» → `unnumero`: de la columna sale un único número, «g»
- «cuando el ruido tiene color» → `color`: un ruido con memoria (curva suave) entra en las dos
- «hacen lo mismo primero» → `primero`: en las dos columnas aparece al inicio un bloque
- «blanquear» → `blanquear`: ese bloque se rotula «blanquear»

---

# Escena 17 — LaGeometria

**Capítulo YouTube:** Una geometría para todo
**Objetivo:** unir todo el capítulo en la misma geometría: flechas, nubes redondas, proyección y distancias en desvíos.

## Narración

<!-- b1 -->
Y detrás de todo está la misma geometría. Las señales son flechas, o puntos. El ruido es una nube redonda. Lo que va en la dirección que importa se queda, y lo perpendicular se tira. Y decidir es medir distancias, en desvíos del ruido. Es la flecha y su sombra del capítulo ocho, la misma idea, una y otra vez.

- «la misma geometría» → `geometria`: un plano vacío con ejes
- «Las señales son flechas, o puntos» → `flechas`: dos flechas que terminan en dos puntos
- «El ruido es una nube redonda» → `nube`: una nube redonda magenta alrededor de cada punto
- «en la dirección que importa» → `direccion`: una dirección marcada, en ámbar
- «se queda» → `queda`: la proyección de una flecha sobre esa dirección, en verde
- «lo perpendicular se tira» → `tira`: el trozo perpendicular se vuelve gris y se desvanece
- «decidir es medir distancias» → `medir`: un segmento entre dos puntos
- «en desvíos del ruido» → `desvios`: sobre el segmento, marcas de tamaño σ
- «la flecha y su sombra» → `sombra`: el dibujo del capítulo 8: una flecha, su sombra y el error perpendicular
- «la misma idea, una y otra vez» → `otravez`: el dibujo vuelve a aparecer en pequeño en las esquinas, una vez por capítulo

---

# Escena 18 — LaReceta

**Capítulo YouTube:** La receta para detectar
**Objetivo:** resumir el procedimiento práctico en pasos, con sus variantes.

## Narración

<!-- b1 -->
Si tuvieras que resolver un problema real, la receta es esta. Identifica qué es señal y qué es ruido. Si el ruido tiene memoria, blanquéalo. Correlaciona con la señal, con un filtro adaptado. Muestrea en el pico. Compara con un umbral, que sale de la probabilidad a priori o de una falsa alarma tolerada. Y si no sabes cuándo llega, usa el máximo y sube el umbral.

- «Si tuvieras que resolver un problema real» → `problema`: aparece un cuaderno vacío
- «la receta es esta» → `receta`: en el cuaderno, la palabra «receta» en ámbar
- «Identifica qué es señal y qué es ruido» → `paso1`: el primer paso: «¿señal? ¿ruido?» con los colores del curso
- «Si el ruido tiene memoria» → `memoria`: junto, una curva suave de ruido con memoria
- «blanquéalo» → `paso2`: el segundo paso: «blanquear»
- «Correlaciona con la señal» → `paso3`: el tercer paso: «correlacionar»
- «con un filtro adaptado» → `adaptado`: se completa «filtro adaptado»
- «Muestrea en el pico» → `paso4`: el cuarto paso: «muestrear en el pico», con el pico de la salida
- «Compara con un umbral» → `paso5`: el quinto paso: «umbral»
- «la probabilidad a priori» → `prior`: junto, «prior» (de E3)
- «una falsa alarma tolerada» → `fa`: junto, «P_FA tolerada» (Neyman-Pearson)
- «Y si no sabes cuándo llega» → `cuando`: se abre una variante a un lado: el radar y su eco
- «usa el máximo» → `maximo`: «máx. de la salida»
- «sube el umbral» → `sube`: la línea del umbral sube un escalón

---

# Escena 19 — Cierre

**Capítulo YouTube:** Una flecha y su sombra

## Narración

<!-- b1 -->
Empezamos este curso con una señal que no podíamos predecir. Aprendimos a describirla con probabilidad, a estimarla con proyecciones, a decidir con hipótesis, a caracterizarla con procesos y espectros, a limpiarla con Wiener y, ahora, a detectarla. Detrás de cada capítulo estaba la misma idea. Una flecha y su sombra.

- «una señal que no podíamos predecir» → `impredecible`: la señal ruidosa del primer episodio de la serie
- «Aprendimos a describirla» → `aprendimos`: el mapa del curso empieza a dibujarse: una línea vacía
- «con probabilidad» → `prob`: la primera estación del mapa: «probabilidad» (cap. 7)
- «con proyecciones» → `proyecciones`: la segunda: «estimación» (cap. 8)
- «con hipótesis» → `hipotesis`: la tercera: «hipótesis» (cap. 9)
- «con procesos y espectros» → `procesos`: las siguientes dos: «procesos» (cap. 10) y «espectros» (cap. 11)
- «con Wiener» → `wiener`: la sexta: «Wiener» (cap. 12)
- «ahora, a detectarla» → `detectar`: la séptima: «detección» (cap. 13), en ámbar
- «Detrás de cada capítulo» → `detras`: debajo de las siete estaciones aparece un rótulo «¿qué hay detrás?»
- «la misma idea» → `idea`: flechas unen las siete estaciones en un mapa
- «Una flecha y su sombra» → `flechasombra`: el mapa se funde en el dibujo de la flecha y su sombra, la voz y el murmullo del capítulo 11 al fondo

<!-- b2 -->
Y con esto se cierra la serie. Gracias por acompañarnos hasta el final.

- «Y con esto se cierra la serie» → `serie`: la flecha y su sombra se achican y quedan en el centro, en ámbar
- «Gracias» → `gracias`: «Gracias» entra con rebote bajo el dibujo
- «hasta el final» → `final`: todo se funde a negro despacio
