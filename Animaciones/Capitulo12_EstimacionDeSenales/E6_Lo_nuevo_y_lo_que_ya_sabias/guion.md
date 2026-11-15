# Episodio 6 — Lo nuevo y lo que ya sabías

Capítulo 12 (Estimación de señales), episodio 6 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 22 a 25), más un gancho y un cierre nuevos.

**Estado:** `guion.md` con 17 escenas y momentos; escenas `s01`–`s17` animadas; borrador 480p15 de 8:36 con 0 avisos y hojas de contacto revisadas. Falta: revisar el texto ⭐ (paso 9), el visto bueno del usuario al mp4 (paso 15) y el render final. El guion base del capítulo sigue esperando la aprobación del usuario.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Cada muestra que llega casi no trae nada nuevo. Hoy aprendemos a separar lo nuevo de lo que ya sabías, y vemos por qué la muestra de ahora vale más que todo el futuro.»
- ⭐ Escena 17 (cierre): repasa el episodio y anuncia el E7, «De Wiener a Kalman».

Retoques de frases del guion base:
- Escena 08, bloque 1 (escena 23 del guion base): «con la fórmula de antes» pasa a «con la fórmula causal de los episodios anteriores», porque el episodio se ve suelto.
- Escena 06, bloque 2 (escena 22, bloque 5): «lo que vimos con las ecuaciones de Yule-Walker» pasa a «lo que vimos en el segundo episodio con las ecuaciones de Yule-Walker».

Reparto de las escenas del guion base: 22 → escenas 03 a 06; 23 → 07 a 09 (el bloque 5 abre la 09); 24 → 09 a 12 (el bloque 1 en la 09); 25 → 13 a 17 (el bloque 5 se reescribe como cierre).
Solo se partieron bloques enteros en escenas atómicas: el resto del texto del guion base no cambia.

Bucles de este episodio: la parábola del error (Cap. 10 y E1: su mínimo es el error de la innovación, escena 07); las ecuaciones de Yule-Walker (E2, escenas 06 y 08); «guarda 0,443 y 0,157» (escena 12 → E7); la muestra de ahora vale más que todo el futuro (E5, escena 21 → escenas 15 y 17); el cierre abre el E7 (observador = filtro).

---

# Escena 01 — Gancho

**Capítulo YouTube:** Cada muestra trae algo nuevo

## Narración

<!-- b1 -->
Cada muestra que llega casi no trae nada nuevo. Hoy aprendemos a separar lo nuevo de lo que ya sabías, y vemos por qué la muestra de ahora vale más que todo el futuro.

- «Cada muestra que llega» → `llega`: una tira de muestras avanza y entra una nueva, x[n], resaltada en cian
- «casi no trae nada nuevo» → `nada`: la muestra se llena de verde y solo una astilla roja queda al borde
- «separar» → `separar`: una tijera corta la muestra por la línea entre verde y rojo
- «lo nuevo» → `nuevo`: la astilla roja sale hacia arriba con la palabra «nuevo»
- «lo que ya sabías» → `sabias`: el trozo verde sale hacia abajo con «ya sabías»
- «la muestra de ahora» → `ahora`: una balanza aparece y en un platillo la muestra x[n] con «ahora»
- «vale más que todo el futuro» → `futuro`: en el otro platillo una fila larga de muestras con «futuro»; el de «ahora» baja

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Lo nuevo y lo que ya sabías

## Narración

<!-- b1 -->
Lo nuevo y lo que ya sabías.

- «Lo nuevo» → `t1`: «Lo nuevo» entra con rebote, en rojo
- «y lo que ya sabías» → `t2`: «y lo que ya sabías» entra debajo, en verde, con la etiqueta «Capítulo 12 · Estimación de señales»

---

# Escena 03 — DosPartes

**Capítulo YouTube:** Las dos partes de cada muestra

## Narración

<!-- b1 -->
Hay otra forma de entender el filtro causal, con la innovación. Volvamos al eco del cero coma seis, sin ruido. Cada muestra es cero coma seis por la anterior, más una moneda nueva, w. Así que la muestra siguiente, equis de ene más uno, tiene dos partes: cero coma seis por equis de ene, que ya conocemos, y w de ene más uno, que todavía no ha llegado.

- «otra forma» → `otra`: la fórmula del filtro causal del episodio anterior, atenuada, y el rótulo «innovación» en ámbar
- «con la innovación» → `innovacion`: la palabra «innovación» entra con rebote en ámbar
- «Volvamos al eco» → `eco`: el bloque del eco del capítulo 11, con una moneda w[n] que entra y x[n] que sale
- «sin ruido» → `sinruido`: el cable ruidoso v, en magenta, queda tachado
- «cero coma seis por la anterior» → `por06`: se escribe «x[n] = 0,6 x[n−1]»
- «más una moneda nueva» → `moneda`: se suma «+ w[n]» con una moneda que cae y «σ² = 2,56»
- «la muestra siguiente» → `siguiente`: aparece «x[n+1] =» a la izquierda de una línea nueva
- «dos partes» → `dospartes`: una llave parte la derecha en dos mitades
- «que ya conocemos» → `conocemos`: «0,6 x[n]» en verde, con un tilde
- «que todavía no ha llegado» → `nollego`: «w[n+1]» en rojo, con un «?» y una moneda en el aire

---

# Escena 04 — MonedasYMuestras

**Capítulo YouTube:** De las monedas a las muestras y vuelta

## Narración

<!-- b1 -->
Veámoslo con números. Si las monedas fueron uno y dos, las muestras son uno, y cero coma seis por uno más dos: dos coma seis. Al revés: dos coma seis menos cero coma seis por uno vale dos, la moneda. Es el blanqueador del capítulo once. De las muestras se recuperan las monedas, y de las monedas, las muestras.

- «Veámoslo con números» → `numeros`: corte seco; dos filas con los rótulos «w:» y «x:», vacías
- «las monedas fueron uno y dos» → `monedas`: en la fila w aparecen «1» y «2»
- «las muestras son uno» → `x1`: en la fila x aparece «1» bajo el primer 1
- «cero coma seis por uno más dos» → `cuenta`: bajo la segunda columna, «0,6 · 1 + 2»
- «dos coma seis» → `x2`: la cuenta pasa a «2,6» y queda en la fila x
- «Al revés» → `reves`: una flecha de vuelta, de la fila x a la fila w
- «dos coma seis menos cero coma seis por uno» → `resta`: se escribe «2,6 − 0,6 · 1» sobre la flecha
- «vale dos» → `vale2`: «= 2»
- «la moneda» → `lamoneda`: ese 2 se enlaza con el 2 de la fila w, en verde
- «el blanqueador del capítulo once» → `blanq`: un bloque «1 − 0,6 z⁻¹» con el rótulo «blanqueador · Cap. 11» a la altura de la flecha
- «se recuperan las monedas» → `recup`: flecha gruesa de la fila x a la fila w
- «de las monedas» → `ida`: flecha gruesa de la fila w a la fila x; las dos flechas forman un ciclo

---

# Escena 05 — LaMismaInformacion

**Capítulo YouTube:** Muestras y monedas son la misma información

## Narración

<!-- b1 -->
Es un hecho general, y depende de la fase mínima. Si F es de fase mínima, su inverso es causal, y conocer las muestras hasta ahora equivale a conocer las monedas hasta ahora: son la misma información. Con un filtro que no fuese de fase mínima, el inverso miraría al futuro y esto se rompería.

- «un hecho general» → `general`: dos bloques encadenados, «F» de w a x y «1/F» de x a w
- «fase mínima» → `fm`: un plano z con el círculo unidad y el cero de F dentro, rótulo «fase mínima» en ámbar
- «su inverso es causal» → `inverso`: el bloque «1/F» se rotula «causal» en verde
- «las muestras hasta ahora» → `muestras`: a la izquierda, el conjunto «x[k], k ≤ n» en cian
- «las monedas hasta ahora» → `monedas`: a la derecha, el conjunto «w[k], k ≤ n» en azul
- «la misma información» → `igual`: un «=» grande entre los dos conjuntos
- «no fuese de fase mínima» → `nofm`: en el plano z el cero salta fuera del círculo
- «miraría al futuro» → `futuro`: el bloque «1/F» se rotula con una flecha hacia las muestras futuras, en rojo
- «se rompería» → `rompe`: el «=» se transforma en «≠» y el conjunto se agrieta

---

# Escena 06 — LoNuevo

**Capítulo YouTube:** La innovación

## Narración

<!-- b1 -->
Entonces la muestra siguiente es lo que ya sé más lo genuinamente nuevo, w de ene más uno. Y lo nuevo, por ser blanco, no está correlacionado con nada de lo que conozco. No hay forma lineal de adivinarlo: por eso se llama innovación. Es lo que la muestra nueva trae que las anteriores no decían.

- «la muestra siguiente» → `sig`: aparece «x[n+1] =»
- «lo que ya sé» → `yase`: «0,6 x[n]» en verde con el rótulo «lo que ya sé»
- «lo genuinamente nuevo» → `nuevo`: «+ w[n+1]» en rojo con el rótulo «lo nuevo»
- «w de ene más uno» → `wn1`: «w[n+1]» se agranda y se separa de «0,6 x[n]»
- «por ser blanco» → `blanco`: bajo w[n+1], una traza de ruido blanco y un espectro plano
- «no está correlacionado» → `nocorr`: una flecha roja w[n+1] y otra verde con el conjunto de lo conocido, a 90°
- «nada de lo que conozco» → `conozco`: el conjunto «x[k], k ≤ n» aparece junto a la flecha verde
- «No hay forma lineal de adivinarlo» → `noadivina`: sobre w[n+1] un «?» y una cruz roja
- «innovación» → `innov`: la palabra «innovación» entra con rebote en ámbar
- «lo que la muestra nueva trae» → `trae`: una flecha lleva «w[n+1]» desde la muestra hasta la palabra «innovación»

<!-- b2 -->
Pausa para pensar: si lo nuevo no se puede adivinar, ¿cuál es la mejor predicción posible? ¿Y cuánto error queda? La respuesta cabe en una línea, y además explica de golpe lo que vimos en el segundo episodio con las ecuaciones de Yule-Walker.

- «Pausa para pensar» → `pausa`: un reloj de arena y una cuenta atrás
- «la mejor predicción posible» → `mejor`: aparece «x̂[n+1] = ?» en ámbar
- «cuánto error queda» → `error`: aparece «error = ?» en rojo
- «cabe en una línea» → `linea`: una sola línea subrayada, vacía
- «de golpe» → `golpe`: un destello sobre la línea vacía
- «en el segundo episodio» → `ep2`: una etiqueta «E2» en un rincón
- «las ecuaciones de Yule-Walker» → `yw`: el sistema de dos ecuaciones del episodio 2, pequeño, en gris

---

# Escena 07 — TirarLoNuevo

**Capítulo YouTube:** Predecir es tirar lo impredecible

## Narración

<!-- b1 -->
La mejor predicción es tirar lo que no se puede predecir y quedarnos con lo demás: la parte que ya sabemos. Y el error es la varianza de lo tirado. Si la innovación entra multiplicada por efe cero, el error es efe cero al cuadrado por la varianza de la moneda. Con el eco, efe cero es uno y la moneda tiene varianza dos coma cinco seis: el error es dos coma cinco seis.

- «tirar lo que no se puede predecir» → `tirar`: «x[n+1] = f₀ w[n+1] + (lo que ya sé)» y una tijera corta el primer término
- «la parte que ya sabemos» → `sabemos`: queda «x̂[n+1] = lo que ya sé» en ámbar
- «el error es la varianza de lo tirado» → `errvar`: aparece «error = varianza de lo tirado» en rojo
- «Si la innovación entra» → `entra`: la palabra «innovación» en rojo entra por la izquierda hacia «x[n+1]»
- «multiplicada por efe cero» → `f0`: se resalta «f₀» en «f₀ w[n+1]»
- «efe cero al cuadrado por la varianza de la moneda» → `formula`: se construye «error = f₀² σ²» por piezas
- «Con el eco, efe cero es uno» → `f01`: «f₀ = 1»
- «tiene varianza dos coma cinco seis» → `s256`: «σ² = 2,56»
- «el error es dos coma cinco seis» → `e256`: «error = 2,56» en rojo y grande

<!-- b2 -->
Es el mismo número que salió de la parábola del capítulo diez, en su punto más bajo, y el de las ecuaciones de Yule-Walker. No es casualidad: aquellas cuentas buscaban, con matrices, exactamente lo que aquí se ve de un vistazo. La mejor predicción de un paso tiene un error igual a la varianza de la innovación, y ninguna otra puede mejorarlo.

- «la parábola del capítulo diez» → `parab`: la parábola del error del capítulo 10, la misma curva
- «en su punto más bajo» → `minimo`: un punto en el vértice con «2,56»
- «las ecuaciones de Yule-Walker» → `yw`: el sistema de dos ecuaciones, con resultado «2,56»
- «No es casualidad» → `nocasual`: un «=» une la parábola y las ecuaciones
- «con matrices» → `matrices`: la matriz de Toeplitz del episodio 1, en gris, junto a las ecuaciones
- «de un vistazo» → `vistazo`: una lupa sobre «f₀² σ²»
- «un error igual a la varianza de la innovación» → `igual`: «error = σ²» enmarcado en rojo
- «ninguna otra puede mejorarlo» → `ninguna`: otras predicciones, como puntos, chocan con el vértice y rebotan hacia arriba

---

# Escena 08 — ElFiltroPredictor

**Capítulo YouTube:** El predictor como filtro

## Narración

<!-- b1 -->
Escribámoslo como filtro con la fórmula causal de los episodios anteriores. Blanquear con uno entre F. Adelantar F una muestra: la respuesta de F al impulso es uno, cero coma seis, cero coma treinta y seis; adelantada, el uno sale por la izquierda, a la posición menos uno, y queda cero coma seis, cero coma treinta y seis, y así. Es la parte que ya se sabe, la causal.

- «Escribámoslo como filtro» → `filtro`: aparece «H = » y un hueco para armar la fórmula causal
- «la fórmula causal de los episodios anteriores» → `formulaant`: la fórmula causal «H = (1/F) [ · ]₊» aparece atenuada, con la etiqueta «E4»
- «Blanquear con uno entre F» → `blanq`: se escribe «1/F» en ámbar
- «Adelantar F una muestra» → `adel`: se escribe «[ z F ]₊»
- «es uno, cero coma seis» → `tallos`: palitos de F: 1, 0,6, 0,36, 0,216…
- «adelantada» → `adelantada`: todos los palitos se desplazan una posición a la izquierda
- «el uno sale por la izquierda» → `sale`: el primer palito, el 1, queda a la izquierda del cero
- «a la posición menos uno» → `menos1`: etiqueta «m = −1» y una tijera sobre el 1
- «y queda cero coma seis» → `queda`: quedan los palitos 0,6, 0,36, 0,216… desde m = 0
- «y así» → `yasi`: tres puntos suspensivos tras los palitos
- «la parte que ya se sabe» → `yasabe`: los palitos se rotulan «la parte causal» en verde

<!-- b2 -->
Esa secuencia es cero coma seis entre uno menos cero coma seis zeta a la menos uno. Y el filtro es el blanqueador, uno menos cero coma seis zeta a la menos uno, multiplicado por ella: se cancela todo y queda cero coma seis. Predecir es multiplicar la última muestra por cero coma seis. Es justo lo que dieron las ecuaciones de Yule-Walker, en una línea.

- «Esa secuencia» → `sec`: los palitos 0,6, 0,36… se enmarcan
- «cero coma seis entre uno menos» → `frac`: se escribe «0,6 / (1 − 0,6 z⁻¹)» junto a los palitos
- «cero coma seis zeta a la menos uno» → `den`: el denominador «1 − 0,6 z⁻¹» de la fracción se resalta
- «Y el filtro» → `elfiltro`: a la izquierda aparece «H =» en ámbar
- «el blanqueador» → `bl`: a la izquierda, «(1 − 0,6 z⁻¹)» con el rótulo «blanqueador»
- «multiplicado por ella» → `mult`: un «·» une el blanqueador y la fracción
- «se cancela todo» → `cancela`: el binomio y el denominador se tachan
- «queda cero coma seis» → `quedaseis`: «H = 0,6» grande, en ámbar
- «multiplicar la última muestra» → `ultima`: x[n] con una flecha, «× 0,6», que lleva a x̂[n+1]
- «por cero coma seis» → `por06`: sobre la flecha, «× 0,6» en ámbar
- «las ecuaciones de Yule-Walker» → `yw`: un tilde verde y el rótulo «= Yule-Walker»
- «en una línea» → `linea`: la línea única de la pausa, ahora llena con «H = 0,6»

---

# Escena 09 — ElReparto

**Capítulo YouTube:** Predecir con ruido

## Narración

<!-- b1 -->
Lo importante no es el caso del eco, sino el reparto: el filtro modelador de fase mínima separa cada muestra en lo que ya sabía y lo genuinamente nuevo. Pero el sensor real no es el eco: su medida lleva ruido. Y ahí predecir y filtrar dejan de ser lo mismo.

- «el reparto» → `reparto`: corte seco; el bloque «F» con la etiqueta «modelador» y una muestra que entra
- «el filtro modelador de fase mínima» → `modelador`: el bloque F se rodea del plano z con el cero dentro del círculo
- «lo que ya sabía» → `yasabia`: de F sale una parte verde con «ya sabía»
- «lo genuinamente nuevo» → `nuevo`: de F sale una astilla roja con «nuevo»
- «el sensor real» → `sensor`: aparece el sensor con su cable
- «lleva ruido» → `ruido`: sobre el cable se suma v en magenta
- «predecir y filtrar» → `pf`: las dos palabras, una junto a otra
- «dejan de ser lo mismo» → `distinto`: entre las dos palabras aparece un «≠» grande

<!-- b2 -->
Ahora predecir en el sensor con ruido: estimar la temperatura de ahora usando solo las mediciones hasta el instante anterior. No es lo mismo que filtrar, que usa también la de ahora. La cuenta es igual, pero con un retardo de más: el coeficiente de la muestra de ahora vale cero, hache de cero igual a cero, y todo empieza una posición después.

- «Ahora predecir» → `ahora`: corte; el sensor con su cable y la palabra «predecir» en ámbar
- «estimar la temperatura de ahora» → `est`: «y[n]» en azul con un «?»
- «hasta el instante anterior» → `hasta`: una ventana sobre las muestras de x: «x[k], k ≤ n − 1»
- «No es lo mismo que filtrar» → `nolo`: debajo, la ventana de filtrar, «x[k], k ≤ n»
- «también la de ahora» → `tambien`: en la ventana de filtrar se resalta la muestra x[n]
- «un retardo de más» → `retardo`: un bloque «z⁻¹» se suma a la cadena
- «vale cero» → `cero`: la muestra x[n] aparece tachada en la ventana de predecir
- «hache de cero igual a cero» → `h0`: «h[0] = 0» en ámbar
- «una posición después» → `despues`: los palitos del filtro se corren una posición a la derecha, el primero vale 0

---

# Escena 10 — UnaSolaMuestra

**Capítulo YouTube:** Predecir con una sola muestra

## Narración

<!-- b1 -->
Con una sola muestra, la anterior. El coeficiente es la correlación cruzada a un paso, dos coma cuatro, entre la autocorrelación de lo medido, cinco: cero coma cuatro ocho. Y el error, cuatro menos dos coma cuatro por cero coma cuatro ocho: dos coma ocho cuatro ocho. Comparado con el cero coma ocho de filtrar con una muestra, es mucho más.

- «Con una sola muestra» → `una`: una ventana que contiene solo «x[n − 1]»
- «la anterior» → `anterior`: la muestra x[n − 1] se enciende en la ventana
- «la correlación cruzada a un paso» → `cruz`: aparece «h = C_yx[1] / C_xx[0]» con la parte de arriba resaltada
- «dos coma cuatro, entre» → `n24`: arriba, «2,4»
- «de lo medido» → `medido`: abajo, «C_xx[0]» con x en cian
- «cinco» → `n5`: abajo, «5»; queda «h = 2,4 / 5»
- «cero coma cuatro ocho. Y el error» → `h048`: «= 0,48» en ámbar
- «el error» → `err`: aparece «error = 4 − 2,4 · 0,48»
- «cuatro menos dos coma cuatro por cero coma cuatro ocho» → `cuenta`: los números de la cuenta se resaltan uno a uno
- «dos coma ocho cuatro ocho» → `e2848`: «= 2,848» en rojo
- «el cero coma ocho de filtrar con una muestra» → `cmp`: a la derecha, «filtrar con una muestra: 0,8», en ámbar
- «es mucho más» → `mucho`: una barra roja de 2,848 junto a una barra corta de 0,8

---

# Escena 11 — TodoElPasado

**Capítulo YouTube:** Predecir con todo el pasado

## Narración

<!-- b1 -->
Con todo el pasado, el resultado es cero coma cuatro cuatro tres, zeta a la menos uno, entre uno menos cero coma uno cinco siete zeta a la menos uno. Se parece al filtro, con el mismo polo, pero con ese retardo de más: el primer coeficiente es cero. Y el error queda en dos coma ocho dos seis. Mirar todo el pasado mejora muy poco lo que daba una sola muestra: dos coma ocho cuatro ocho.

- «Con todo el pasado» → `pasado`: una ventana larga, «x[k], k ≤ n − 1»
- «cero coma cuatro cuatro tres» → `num`: se escribe «H = 0,443 z⁻¹»
- «entre uno menos cero coma uno cinco siete zeta a la menos uno» → `den`: se completa «/ (1 − 0,157 z⁻¹)»
- «cero coma uno cinco siete» → `n157`: el «0,157» del denominador se resalta
- «Se parece al filtro» → `parece`: encima, el filtro causal del episodio 5: «0,7386 / (1 − 0,157 z⁻¹)», atenuado
- «el mismo polo» → `polo`: en las dos fórmulas se resalta el denominador igual
- «ese retardo de más» → `ret`: se resalta el «z⁻¹» del numerador
- «el primer coeficiente es cero» → `primero`: palitos «0 · 0,443 · 0,0695 · 0,0109…» y el primero, el 0, resaltado
- «dos coma ocho dos seis» → `e2826`: «error = 2,826» en rojo
- «mejora muy poco» → `poco`: dos barras, 2,848 y 2,826, casi iguales, con una flecha minúscula entre ellas
- «dos coma ocho cuatro ocho» → `b2848`: la primera barra se rotula «una sola muestra»

---

# Escena 12 — CuatroVecesMas

**Capítulo YouTube:** Por qué predecir cuesta tanto

## Narración

<!-- b1 -->
Filtrar daba cero coma siete tres ocho seis; predecir, dos coma ocho dos seis: casi cuatro veces más error. La razón es sencilla. Con la muestra de ahora tienes una mirada directa, aunque ruidosa, de la temperatura de ahora. Sin ella, tienes que extrapolar desde el pasado, y la temperatura solo se acuerda un cero coma seis de lo anterior. Un paso de extrapolación ya cuesta mucho.

- «Filtrar daba» → `filtrar`: corte; una barra corta, «0,7386», en ámbar
- «predecir, dos coma ocho dos seis» → `predecir`: una barra larga, «2,826», en rojo
- «casi cuatro veces más error» → `veces`: un «×3,8» entre las barras
- «La razón es sencilla» → `razon`: «¿por qué?» sobre las barras
- «una mirada directa» → `mirada`: un ojo sobre x[n] que mira a y[n]
- «aunque ruidosa» → `ruidosa`: sobre el cable, v en magenta se suma a y
- «Sin ella» → `sin`: la muestra x[n] se tacha
- «extrapolar desde el pasado» → `extra`: una flecha va de x[n − 1] a y[n] con un «?»
- «se acuerda un cero coma seis» → `acuerda`: sobre la flecha, «× 0,6»
- «de lo anterior» → `anterior`: la flecha se adelgaza, como si perdiera fuerza
- «Un paso de extrapolación» → `paso`: un solo paso se marca sobre la flecha
- «ya cuesta mucho» → `cuesta`: la flecha se rodea de un halo rojo

<!-- b2 -->
Guarda dos números: cero coma cuatro cuatro tres y cero coma uno cinco siete, los del predictor. Volverán en el último episodio, en un sitio en el que no los esperas. Ahora tenemos casi todo para comparar de una vez las tres cosas que hemos aprendido: predecir, filtrar y suavizar.

- «Guarda dos números» → `guarda`: dos recuadros vacíos, en ámbar
- «cero coma cuatro cuatro tres» → `n443`: el primer recuadro se llena con «0,443»
- «cero coma uno cinco siete» → `n157`: el segundo recuadro se llena con «0,157»
- «los del predictor» → `predictor`: ambos se enlazan a «0,443 z⁻¹ / (1 − 0,157 z⁻¹)»
- «Volverán en el último episodio» → `vuelven`: una etiqueta «E7» y un candado cerrado sobre los recuadros
- «en un sitio en el que no los esperas» → `sitio`: un «?» grande junto a la etiqueta
- «Ahora tenemos casi todo» → `casi`: los recuadros 0,443 y 0,157 se guardan en una esquina
- «comparar de una vez» → `comparar`: tres cajas vacías, en fila
- «predecir, filtrar» → `pf`: las dos primeras cajas se rotulan «predecir» y «filtrar»
- «suavizar» → `suav`: la tercera se rotula «suavizar»

---

# Escena 13 — Encuesta

**Capítulo YouTube:** ¿Qué salto es mayor?

## Narración

<!-- b1 -->
Una encuesta rápida. Para bajar el error del sensor, ¿qué salto es mayor? La opción A: poder usar la muestra de ahora, pasar de predecir a filtrar. La opción B: poder usar además el futuro, pasar de filtrar a suavizar. Piénsalo antes de mirar los números.

- «Una encuesta» → `enc`: corte seco; el rótulo «Encuesta» y dos casillas vacías, A y B
- «bajar el error» → `bajar`: una barra roja que baja
- «¿qué salto es mayor?» → `salto`: «¿qué salto es mayor?» entra con rebote
- «La opción A» → `a`: la casilla A se enciende
- «la muestra de ahora» → `ahora`: en la casilla A, una ventana con x[n] resaltada
- «pasar de predecir a filtrar» → `paf`: «predecir → filtrar» bajo la casilla A
- «La opción B» → `b`: la casilla B se enciende
- «además el futuro» → `futuro`: en la casilla B, la ventana se extiende a muestras futuras
- «pasar de filtrar a suavizar» → `afs`: «filtrar → suavizar» bajo la casilla B
- «Piénsalo» → `piensa`: una cuenta atrás de tres segundos

---

# Escena 14 — LaTabla

**Capítulo YouTube:** La tabla de errores

## Narración

<!-- b1 -->
La tabla. Sin usar ningún dato, el error es la varianza, cuatro. Prediciendo con todo el pasado, sin la muestra de ahora, dos coma ocho dos seis. Filtrando, cero coma siete tres ocho seis. Suavizando, con todo el registro, cero coma seis ocho seis. De cuatro a dos coma ocho: se ha eliminado el veintinueve por ciento del error. Filtrando, el ochenta y dos. Suavizando, el ochenta y tres.

- «La tabla» → `tabla`: corte; una tabla vacía de cuatro filas
- «Sin usar ningún dato» → `sindatos`: la primera fila se rotula «sin datos» y no tiene ventana
- «la varianza, cuatro» → `var4`: una barra larga, «4»
- «Prediciendo con todo el pasado» → `fila2`: segunda fila, «predicción», con la ventana «x[k], k ≤ n − 1»
- «sin la muestra de ahora» → `sinahora`: la muestra x[n] queda tachada en la ventana
- «dos coma ocho dos seis» → `p2826`: la barra baja a «2,826»
- «Filtrando» → `filt`: tercera fila, «filtrado», con la ventana «x[k], k ≤ n»
- «cero coma siete tres ocho seis» → `f07386`: la barra se acorta a «0,7386»
- «Suavizando, con todo el registro» → `suav`: cuarta fila, «suavizado», con la ventana «x[k], todo k»
- «cero coma seis ocho seis» → `s0686`: la barra se acorta a «0,686»
- «De cuatro a dos coma ocho» → `de4`: una flecha entre la primera y la segunda barra
- «el veintinueve por ciento» → `p29`: a la derecha de la segunda fila, «29 %»
- «el ochenta y dos» → `p82`: a la derecha de la tercera fila, «82 %»
- «el ochenta y tres» → `p83`: a la derecha de la cuarta fila, «83 %»

---

# Escena 15 — LaRespuesta

**Capítulo YouTube:** La muestra de ahora vale más que el futuro

## Narración

<!-- b1 -->
Respuesta: la A, y de lejos. Pasar de predecir a filtrar baja el error más de dos unidades; pasar de filtrar a suavizar, solo cinco centésimas. La muestra de ahora vale más que todo el futuro junto. Y el orden se cumple siempre: el suavizado es menor o igual que el filtrado, este que la predicción, y esta que la varianza. Más datos, menos error.

- «la A, y de lejos» → `resp`: la casilla A se llena de verde con un tilde; la B se apaga
- «Pasar de predecir a filtrar» → `paf`: se señala el tramo entre las barras de predecir y filtrar
- «más de dos unidades» → `dos`: entre las barras de predecir y filtrar, una flecha larga «−2,09»
- «solo cinco centésimas» → `cinco`: entre las barras de filtrar y suavizar, una flecha diminuta «−0,05»
- «vale más que todo el futuro junto» → `vale`: la balanza; el platillo de «ahora» baja contra el del futuro
- «el orden se cumple siempre» → `orden`: la tabla se reordena en una cadena
- «el suavizado es menor o igual que el filtrado» → `suavfilt`: «suavizado ≤ filtrado»
- «este que la predicción» → `filtpred`: «≤ predicción»
- «esta que la varianza» → `predvar`: «≤ varianza»
- «Más datos, menos error» → `masdatos`: la cadena entera queda enmarcada en ámbar con una flecha «más datos»

---

# Escena 16 — CuandoUsarCada

**Capítulo YouTube:** Cuándo usar cada versión

## Narración

<!-- b1 -->
Cuál usar depende de cuándo necesitas la respuesta. Si limpias una señal a medida que llega, en tiempo real, filtras. Si tienes que adelantarte, como un control que actúa antes de que pase algo, predices. Y si ya tienes la grabación entera y puedes esperar, suavizas: es lo mejor que se puede hacer.

- «cuándo necesitas la respuesta» → `cuando`: corte; un reloj con tres marcas
- «Si limpias una señal» → `limpias`: el colador limpia una traza ruidosa
- «a medida que llega» → `llega`: una señal avanza por la pantalla con su ventana
- «en tiempo real, filtras» → `filtras`: la palabra «filtrar» con el reloj en verde
- «adelantarte» → `adelantar`: una flecha salta hacia el futuro
- «un control que actúa» → `control`: un bloque de control que envía una orden
- «predices» → `predices`: la palabra «predecir» en ámbar
- «la grabación entera» → `grab`: una cinta con todo el registro
- «puedes esperar» → `espera`: un reloj de arena
- «suavizas» → `suavizas`: la palabra «suavizar» en ámbar
- «lo mejor que se puede hacer» → `mejor`: el error mínimo, «0,686», se enmarca

---

# Escena 17 — Cierre

**Capítulo YouTube:** Qué viene: de Wiener a Kalman

## Narración

<!-- b1 -->
Hoy hemos visto que cada muestra trae algo nuevo, la innovación, y que predecir es tirarlo y quedarse con lo que ya sabías. Y que la muestra de ahora vale más que todo el futuro junto. Pero la fórmula del filtro causal, con sus polos y sus ceros, se parece demasiado a un sistema de control con un observador. Y esa casualidad no lo es. En el siguiente episodio: De Wiener a Kalman.

- «cada muestra trae algo nuevo» → `nuevo`: una muestra con una astilla roja
- «la innovación» → `innov`: la palabra «innovación» en ámbar sobre la astilla
- «predecir es tirarlo» → `tirar`: una tijera corta la astilla
- «lo que ya sabías» → `sabias`: queda el trozo verde, «ya sabías»
- «la muestra de ahora vale más» → `ahora`: la balanza, el platillo de «ahora» baja
- «que todo el futuro junto» → `futuro`: el platillo del futuro sube
- «Pero la fórmula del filtro causal» → `formula`: aparece «0,7386 / (1 − 0,157 z⁻¹)»
- «con sus polos y sus ceros» → `polos`: el plano z con una × y un ○
- «un sistema de control con un observador» → `obs`: cajitas de estado con un observador, dibujadas junto al filtro causal
- «esa casualidad no lo es» → `nolo`: un signo «=» une el filtro y el observador
- «En el siguiente episodio» → `sig`: la etiqueta «Episodio 7» entra desde la derecha
- «De Wiener a Kalman» → `titulo`: el título «De Wiener a Kalman» entra con rebote, con la etiqueta «Episodio 7»
