# Episodio 5 — Cuando el ruido tiene memoria

Capítulo 13 (Detección de señales), episodio 5 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 19 a 22), más un gancho y un cierre nuevos.

**Estado:** `ritmo.py` sin huecos de más de 4 s. Escenas `s01`–`s12` animadas; borrador 480p15 de 8:42, **0 avisos**, hojas de contacto revisadas (`salida/E5_Cuando_el_ruido_tiene_memoria-480p15.mp4`). Falta: visto bueno del usuario al texto ⭐ (paso 9) y al mp4 (paso 15); después render final `--calidad qh` (paso 16). El gancho (16 s) se pronuncia «cu de uno» en la escena 03: probar de oído.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Miras una sola muestra y te equivocas casi el dieciséis por ciento de las veces. Miras también la de al lado y bajas a poco más del diez. ¿Por qué? Porque cuando el ruido tiene memoria, el vecino delata al ruido.»
- ⭐ Escena 12 (cierre): resumen y anuncia E6 por su título, «¿Cuándo llegó el eco?».
- ⭐ Retoque en la escena 11 (bloque b5): se quitan las dos últimas frases del guion base («Pero hasta aquí siempre hemos sabido cuándo llegaba el pulso… Ese es el siguiente problema»); pasan al cierre.
- ⭐ Retoque en la escena 09 (bloque b5): «letra chica» → «letra pequeña» (castellano de España).

Notas para otros episodios:
- El cierre del E4 de este capítulo tiene que anunciar este título, «Cuando el ruido tiene memoria».
- Números que tienen que volver con el mismo dibujo: el eco del 0,6 (nube elíptica de dos muestras), el pulso `(2, 0)`, 0,64, 6,25 (Q(1) = 0,1587 frente a Q(1,25) = 0,1056), el pulso blanqueado `(2, −1,5)`, y los pulsos `(1, 1)` y `(1, −1)` con relaciones 1,25 y 5.

Reparto de las escenas del guion base: 19 → escenas 03 y 04; 20 → 05, 06 y 07; 21 → 08 y 09; 22 → 10 y 11.
Solo se partieron bloques enteros en escenas atómicas: el texto del guion base no cambia (salvo los retoques de arriba).

---

# Escena 01 — Gancho

**Capítulo YouTube:** El vecino que delata al ruido

## Narración

<!-- b1 -->
Miras una sola muestra y te equivocas casi el dieciséis por ciento de las veces. Miras también la de al lado y bajas a poco más del diez. ¿Por qué? Porque cuando el ruido tiene memoria, el vecino delata al ruido.

- «una sola muestra» → `una`: aparece una sola barra de muestra con su ruido encima, en cian
- «casi el dieciséis por ciento» → `err16`: junto a la barra, «P_e = 15,9 %» en rojo
- «de las veces» → `veces`: junto a la cifra, una fila de diez intentos con unos pocos en rojo
- «la de al lado» → `lado`: se enciende la muestra vecina, a la derecha de la primera
- «poco más del diez» → `err10`: el rojo baja a «P_e = 10,6 %»
- «¿Por qué?» → `porque`: un «¿por qué?» ámbar entre las dos cifras
- «el ruido tiene memoria» → `memoria`: las dos muestras de ruido se unen con un hilo magenta
- «el vecino delata al ruido» → `delata`: el ruido de la vecina se copia sobre el de la primera, en magenta

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Cuando el ruido tiene memoria

## Narración

<!-- b1 -->
Cuando el ruido tiene memoria.

- «Cuando» → `t1`: «Cuando» entra con rebote
- «el ruido tiene memoria.» → `t2`: «el ruido tiene memoria» entra debajo, con la etiqueta «Capítulo 13 · Detección de señales»

---

# Escena 03 — LaMemoriaDelRuido

**Capítulo YouTube:** Dos muestras con memoria y un pulso

## Narración

<!-- b1 -->
Hasta ahora, el ruido de cada muestra era independiente del de las demás. Pero muchos ruidos tienen memoria. Recuerda el eco del cero coma seis: cada muestra se parece un sesenta por ciento a la anterior. Tomemos dos muestras seguidas de ese ruido, con varianza uno cada una y una correlación de cero coma seis entre ellas.

- «independiente del de las demás» → `indep`: una tira de muestras de ruido sueltas, sin relación entre ellas
- «muchos ruidos tienen memoria» → `memoria`: la tira se vuelve una traza lenta, cada muestra unida a la anterior
- «el eco del cero coma seis» → `eco`: entra el eco del capítulo 10, con «× 0,6» entre dos muestras
- «se parece un sesenta por ciento a la anterior» → `sesenta`: una muestra copiada al 60 % sobre la siguiente
- «dos muestras seguidas» → `dos`: corte; quedan dos muestras, v₀ y v₁, sobre un plano
- «varianza uno cada una» → `var1`: «σ² = 1» sobre cada eje
- «una correlación de cero coma seis» → `corr`: una nube elíptica inclinada rodea los puntos, con «ρ = 0,6»

<!-- b2 -->
La señal ahora es un pulso de una sola muestra: dos, cero. Bajo la hipótesis uno recibimos dos más el ruido de la primera muestra, y el ruido de la segunda. El detector ingenuo mira solo la primera: media dos, varianza uno, relación cuatro. Su probabilidad de error es cu de uno: cero coma uno cinco ocho siete.

- «un pulso de una sola muestra» → `pulso`: entra la tira n = 0, 1 con una sola barra azul
- «dos, cero» → `dos0`: la barra se rotula «s = (2, 0)»
- «Bajo la hipótesis uno» → `h1`: aparece «H₁» en ámbar
- «dos más el ruido de la primera muestra» → `r0`: «r₀ = 2 + v₀», con el 2 en azul y v₀ en magenta
- «y el ruido de la segunda» → `r1`: «r₁ = v₁» debajo, en magenta
- «El detector ingenuo» → `ingenuo`: un ojo mira solo r₀ y tacha r₁
- «media dos» → `media`: una campana centrada en 2
- «varianza uno» → `var`: «σ² = 1» sobre la campana
- «relación cuatro» → `rel4`: «d² = 4 / 1 = 4»
- «cu de uno» → `qu`: «Q(1)» con su cola sombreada en rojo
- «cero coma uno cinco ocho siete» → `pe`: «= 0,1587», en rojo

---

# Escena 04 — LaSegundaMuestraChiva

**Capítulo YouTube:** Restar lo que delata el vecino

## Narración

<!-- b1 -->
Pero la segunda muestra no es basura. Como el ruido de la segunda se parece al de la primera, la segunda nos chiva algo del ruido de la primera. Así que probamos con una combinación: la primera menos cero coma seis veces la segunda. Si el ruido de la primera fue alto, el de la segunda probablemente también, y la resta lo compensa.

- «no es basura» → `basura`: la muestra r₁ vuelve a encenderse, con una cruz roja que se borra
- «se parece al de la primera» → `parece`: un hilo une v₁ con v₀ en la nube
- «nos chiva» → `chiva`: una flecha magenta de v₁ hacia v₀, con «pista»
- «algo del ruido de la primera» → `algo`: la flecha magenta se detiene sobre v₀, con «pista»
- «una combinación» → `comb`: entra «r₀ − ? · r₁», con un signo de interrogación ámbar
- «la primera menos cero coma seis veces la segunda» → `formula`: queda «r₀ − 0,6 r₁»
- «Si el ruido de la primera» → `si`: v₀ se marca en la nube con un punto
- «fue alto» → `alto`: v₀ sube, un punto alto en la nube
- «la resta lo compensa» → `compensa`: v₁ sube con él y la resta lo devuelve al centro

<!-- b2 -->
Calculemos su varianza, con la regla del capítulo siete: varianza de una combinación. Uno, de la primera, más cero coma seis al cuadrado, cero coma tres seis, de la segunda, menos dos por cero coma seis por cero coma seis, de la covarianza: cero coma siete dos. Uno más cero coma tres seis menos cero coma siete dos: cero coma seis cuatro.

- «con la regla del capítulo siete» → `regla`: «Var(a X + b Y) = a² Var X + b² Var Y + 2ab Cov» en el borde
- «varianza de una combinación» → `varcomb`: la regla se completa con «a² Var X + b² Var Y + 2ab Cov»
- «Uno, de la primera» → `t1`: se construye «Var = 1»
- «más cero coma seis al cuadrado» → `t2`: «+ 0,6²»
- «cero coma tres seis» → `t36`: «0,6² = 0,36»
- «menos dos por cero coma seis por cero coma seis» → `t3`: «− 2 · 0,6 · 0,6»
- «de la covarianza» → `cov`: el término se rotula «covarianza», en magenta
- «cero coma siete dos» → `t72`: «= 0,72»
- «Uno más cero coma tres seis menos cero coma siete dos» → `suma`: «1 + 0,36 − 0,72»
- «cero coma seis cuatro» → `v64`: «= 0,64», en ámbar, y la nube encoge en esa dirección

<!-- b3 -->
La media sigue siendo dos: el pulso solo está en la primera muestra. Así que la relación vale cuatro entre cero coma seis cuatro: seis coma dos cinco. Mucho mejor que cuatro. El error baja de cero coma uno cinco ocho siete a cero coma uno cero cinco seis. Y fíjate: los pesos del mejor filtro, uno y menos cero coma seis, no son la señal al revés. La receta cambia.

- «La media sigue siendo dos» → `media`: una campana centrada en 2
- «solo está en la primera muestra» → `sola`: la barra (2, 0) con el cero marcado
- «Así que la relación vale» → `asi`: aparece «d² = » en ámbar
- «cuatro entre cero coma seis cuatro» → `cuenta`: «4 / 0,64»
- «seis coma dos cinco» → `s625`: «= 6,25», en ámbar
- «Mucho mejor que cuatro» → `mejor`: junto al 6,25 el 4 anterior, tachado
- «de cero coma uno cinco ocho siete» → `e1587`: «Q(1) = 0,1587» en rojo
- «a cero coma uno cero cinco seis» → `e1056`: «Q(1,25) = 0,1056» en rojo, más corto
- «los pesos del mejor filtro» → `pesos`: «(1, −0,6)» en ámbar
- «no son la señal al revés» → `noalreves`: al lado, «(0, 2)» (la señal invertida) y un «≠»
- «La receta cambia» → `receta`: «receta distinta» en ámbar

---

# Escena 05 — BlanquearElRuido

**Capítulo YouTube:** Blanquear el ruido con dos muestras

## Narración

<!-- b1 -->
La receta general es la que anunciamos en el capítulo once: blanquear primero, y después aplicar lo que ya sabemos. Recuerda el blanqueador: para el eco del cero coma seis, restar cero coma seis veces la muestra anterior devolvía una moneda: ruido blanco. Hagámoslo con las dos muestras.

- «blanquear primero» → `blanquear`: una caja «blanqueador» entra a la izquierda
- «aplicar lo que ya sabemos» → `aplicar`: a su derecha, una caja «filtro adaptado»
- «Recuerda el blanqueador» → `recuerda`: la cadena «ruido con memoria → blanqueador → ruido blanco»
- «restar cero coma seis veces la muestra anterior» → `restar`: «x[n] − 0,6 x[n−1]» dentro de la caja
- «devolvía una moneda» → `moneda`: sale una tira de monedas ±1
- «ruido blanco» → `blanco`: la tira se rotula «ruido blanco»
- «Hagámoslo con las dos muestras» → `hagamos`: corte; vuelve la nube elíptica de v₀ y v₁

<!-- b2 -->
La primera queda igual: varianza uno. A la segunda le restamos cero coma seis veces la primera. La resta tiene varianza cero coma seis cuatro, y no está correlacionada con la primera. Para que valga uno, dividimos entre cero coma ocho, la raíz de cero coma seis cuatro. Ahora las dos muestras son independientes, de varianza uno: ruido blanco.

- «La primera queda igual» → `igual`: «u₀ = v₀», con «σ² = 1»
- «A la segunda le restamos» → `resta`: «v₁ − 0,6 v₀»
- «cero coma seis veces la primera» → `seis`: «v₁ − 0,6 v₀» con el 0,6 en ámbar
- «varianza cero coma seis cuatro» → `v64`: «σ² = 0,64»
- «no está correlacionada con la primera» → `nocorr`: la nube se endereza hacia los ejes
- «Para que valga uno» → `valga`: «σ² = 1» como objetivo, en ámbar
- «dividimos entre cero coma ocho» → `div`: «÷ 0,8», la resta se rotula «u₁»
- «la raíz de cero coma seis cuatro» → `raiz`: «√0,64 = 0,8»
- «Ahora las dos muestras son independientes» → `indep`: la nube elíptica se vuelve un círculo
- «ruido blanco» → `blanco2`: el círculo se rotula «ruido blanco», con «σ² = 1» en cada eje

---

# Escena 06 — BlanquearLaSenal

**Capítulo YouTube:** El pulso blanqueado y el mismo número

## Narración

<!-- b1 -->
Pasamos la señal por el mismo blanqueador. La primera muestra sigue valiendo dos. La segunda, cero menos cero coma seis por dos, entre cero coma ocho: menos uno coma cinco. El pulso blanqueado es dos, menos uno coma cinco. Y sobre ruido blanco ya sabemos qué hacer: el filtro adaptado a ese pulso.

- «el mismo blanqueador» → `mismo`: la barra (2, 0) entra en la caja «blanqueador»
- «sigue valiendo dos» → `dos`: la primera barra sale igual, en 2
- «cero menos cero coma seis por dos» → `cuenta`: «p₁ = (0 − 0,6 · 2)»
- «entre cero coma ocho» → `entre`: «/ 0,8»
- «menos uno coma cinco» → `m15`: «= −1,5»; una barra hacia abajo
- «El pulso blanqueado» → `pulsob`: las dos barras (2, −1,5) en azul
- «dos, menos uno coma cinco» → `valores`: las barras se rotulan «(2, −1,5)»
- «sobre ruido blanco» → `sobre`: el círculo del ruido blanco, al fondo
- «el filtro adaptado a ese pulso» → `adaptado`: la caja «filtro adaptado» con la barra invertida (−1,5, 2)

<!-- b2 -->
Su energía es cuatro más dos coma veinticinco: seis coma veinticinco. Es exactamente la relación de antes. Por los dos caminos, el mismo número. Y no se pierde información, porque el blanqueador se puede deshacer: a partir de las muestras blanqueadas puedes recuperar las originales. No es como el promedio, que tiraba lo que no se puede recuperar.

- «Su energía» → `energia`: sobre las barras, «E = p₀² + p₁²»
- «cuatro más dos coma veinticinco» → `suma`: «4 + 2,25»
- «seis coma veinticinco» → `s625`: «= 6,25», en ámbar
- «la relación de antes» → `antes`: a la izquierda, el «6,25» de la escena 04
- «Por los dos caminos» → `caminos`: dos flechas, la de la combinación y la del blanqueo, que llegan al mismo punto
- «el mismo número» → `mismo2`: un «=» verde entre los dos 6,25
- «no se pierde información» → `nopierde`: «sin pérdida» en verde
- «se puede deshacer» → `deshacer`: una flecha inversa del ruido blanco al ruido con memoria
- «recuperar las originales» → `orig`: la flecha inversa llega a las dos muestras originales
- «No es como el promedio» → `promedio`: el promedio de la escena 04 aparece con una flecha inversa tachada
- «lo que no se puede recuperar» → `norecup`: el promedio se rotula «irrecuperable», en rojo

---

# Escena 07 — EnFrecuencia

**Capítulo YouTube:** El filtro en frecuencia

## Narración

<!-- b1 -->
En frecuencia, el filtro total tiene una forma muy sensata: la conjugada de la transformada de la señal, dividida entre la densidad espectral del ruido. Tiene mucha ganancia donde la señal es fuerte y el ruido débil. Y la relación señal-ruido es la integral, en todas las frecuencias, del cuadrado de la señal entre la densidad del ruido. La derivación con matrices está en el apunte.

- «En frecuencia» → `frec`: un lienzo de frecuencias, con el espectro de la señal en azul y el del ruido en magenta
- «la conjugada de la transformada de la señal» → `conj`: se construye «H = S*», con S* en azul
- «dividida entre» → `div`: aparece «/ »
- «la densidad espectral del ruido» → `dens`: «D_vv» en magenta
- «mucha ganancia» → `ganancia`: la curva de H en ámbar crece
- «la señal es fuerte» → `fuerte`: se resalta el trozo donde la azul está alta
- «el ruido débil» → `debil`: se resalta el trozo donde la magenta está baja; ahí la ámbar es un pico
- «la relación señal-ruido» → `rel`: «relación = »
- «la integral, en todas las frecuencias» → `integral`: «(1/2π) ∫ dΩ»
- «del cuadrado de la señal» → `cuad`: «|S|²»
- «entre la densidad del ruido» → `entre`: «/ D_vv»; el área |S|²/D se sombrea
- «La derivación con matrices» → `deriv`: una matriz de covarianza esbozada en el borde
- «está en el apunte» → `apunte`: el icono del libro junto a la matriz

---

# Escena 08 — DosPulsos

**Capítulo YouTube:** Dos pulsos con la misma energía

## Narración

<!-- b1 -->
Con ruido blanco, la forma de la señal no importaba: solo la energía. Con ruido con memoria, sí. Comprobémoslo con dos pulsos de dos muestras y la misma energía, dos. Uno, uno: no cambia de signo, es lento. Y uno, menos uno: cambia de signo en cada muestra, es rápido. El ruido, el del eco del cero coma seis, es un ruido lento.

- «la forma de la señal no importaba» → `forma`: el resumen de la escena 13: tres barras distintas con el mismo «E = 9»
- «solo la energía» → `energia`: «E» en ámbar, el resto se apaga
- «Con ruido con memoria, sí» → `si`: «con memoria: sí» en ámbar, con un signo de interrogación que se vuelve tilde
- «dos pulsos de dos muestras» → `dospulsos`: aparecen dos tiras de dos barras
- «la misma energía, dos» → `e2`: «E = 2» sobre las dos
- «Uno, uno» → `uno1`: la primera tira, barras (1, 1), rotulada «(1, 1)»
- «no cambia de signo, es lento» → `lento`: una línea suave y plana
- «Y uno, menos uno» → `uno_m1`: la segunda tira, barras (1, −1), rotulada «(1, −1)»
- «cambia de signo en cada muestra, es rápido» → `rapido`: una línea en zigzag
- «El ruido» → `ruido`: la nube inclinada del ruido entra a la derecha
- «el del eco del cero coma seis» → `eco`: aparece el eco del 0,6 en una esquina
- «es un ruido lento» → `ruidolento`: la nube inclinada con su eje largo (1, 1) en magenta

<!-- b2 -->
¿Cuánto fluctúa el ruido en cada dirección? La suma de las dos muestras tiene varianza uno más uno, más dos veces cero coma seis: tres coma dos. La resta, uno más uno, menos uno coma dos: cero coma ocho. Un ruido lento fluctúa mucho a lo largo de la suma y poco a lo largo de la resta.

- «¿Cuánto fluctúa el ruido en cada dirección?» → `cuanto`: en la nube, dos flechas, una larga (1, 1) y otra corta (1, −1)
- «La suma de las dos muestras» → `suma`: «v₀ + v₁» junto a la dirección larga
- «uno más uno, más dos veces cero coma seis» → `cuenta1`: «1 + 1 + 2 · 0,6»
- «tres coma dos» → `t32`: «= 3,2», en ámbar
- «La resta» → `resta`: «v₀ − v₁» junto a la dirección corta
- «uno más uno, menos uno coma dos» → `cuenta2`: «1 + 1 − 1,2»
- «cero coma ocho» → `t08`: «= 0,8», en ámbar
- «fluctúa mucho a lo largo de la suma» → `mucho`: el eje largo de la nube se resalta
- «poco a lo largo de la resta» → `poco`: el eje corto se resalta

---

# Escena 09 — LaFormaSiImporta

**Capítulo YouTube:** El pulso rápido gana al lento

## Narración

<!-- b1 -->
Para el pulso uno, uno, la media es dos, al cuadrado cuatro, entre tres coma dos: uno coma veinticinco. Para el pulso uno, menos uno, cuatro entre cero coma ocho: cinco. Con ruido blanco, los dos habrían dado dos. Uno coma veinticinco, dos, cinco: los errores son cero coma veintinueve, cero coma veinticuatro y cero coma trece.

- «Para el pulso uno, uno» → `p11`: la tira (1, 1) a la izquierda, con una tabla vacía de tres filas
- «al cuadrado cuatro» → `cuad`: «2² = 4»
- «entre tres coma dos» → `entre32`: «/ 3,2»
- «uno coma veinticinco» → `r125`: «= 1,25» en la primera fila
- «Para el pulso uno, menos uno» → `p1m1`: la tira (1, −1) pasa a la derecha
- «cuatro entre cero coma ocho» → `entre08`: «4 / 0,8»
- «cinco» → `r5`: «= 5» en la segunda fila
- «Con ruido blanco, los dos habrían dado dos» → `blanco`: la tercera fila, «ruido blanco: 2»
- «Uno coma veinticinco, dos, cinco» → `lista`: se resaltan las tres cifras de la columna de relaciones
- «los errores son» → `errores`: aparece una columna «P_e» en rojo
- «cero coma veintinueve» → `q29`: «0,29» en la primera fila
- «cero coma veinticuatro» → `q24`: «0,24» en la fila del ruido blanco
- «cero coma trece» → `q13`: «0,13» en la fila del pulso rápido

<!-- b2 -->
Fíjate en lo que ha pasado: el pulso rápido, con el mismo gasto de energía, consigue una relación cuatro veces mayor que el lento, porque vive donde el ruido es débil. En frecuencia: la relación señal-ruido es la integral del cuadrado de la señal dividido entre la densidad del ruido. Cada frecuencia de la señal cuenta menos donde el ruido es fuerte.

- «el pulso rápido» → `rapido`: la fila del (1, −1) se resalta
- «el mismo gasto de energía» → `gasto`: «E = 2» sobre las dos tiras
- «cuatro veces mayor» → `cuatro`: «5 / 1,25 = 4» con una flecha ámbar
- «que el lento» → `lento`: la fila del (1, 1) se atenúa
- «donde el ruido es débil» → `debil`: lienzo de frecuencias con el bulto del ruido a bajas frecuencias; el pulso rápido cae donde el ruido es bajo
- «En frecuencia» → `frec`: el espectro del pulso lento queda dentro del bulto del ruido
- «la integral del cuadrado de la señal» → `integral`: «∫ |S|²», con el área bajo cada pulso
- «dividido entre la densidad del ruido» → `dens`: «/ D_vv», las áreas se reescalan
- «Cada frecuencia de la señal cuenta menos» → `cuenta`: el área del pulso lento se achica
- «donde el ruido es fuerte» → `fuerte`: el bulto del ruido, en magenta, se resalta

<!-- b3 -->
Y con memoria negativa sería al revés: el ruido alterna, y convendría una señal que no alterne. Es la letra pequeña de «la forma no importa»: era cierto solo con ruido blanco. Cuando puedes diseñar la señal, en un radar o en una comunicación, eliges dónde poner la energía: donde el ruido es más débil.

- «memoria negativa» → `neg`: el eco con un «− 0,6»
- «al revés» → `reves`: el bulto del ruido salta de las bajas a las altas frecuencias
- «el ruido alterna» → `alterna`: una traza magenta en zigzag
- «una señal que no alterne» → `noalterne`: el pulso (1, 1), plano, se enciende en verde
- «la letra pequeña» → `chica`: «la forma no importa» con un asterisco ámbar
- «solo con ruido blanco» → `blanco`: el asterisco se rotula «solo con ruido blanco»
- «Cuando puedes diseñar la señal» → `disenar`: un lápiz sobre el espectro de la señal
- «en un radar o en una comunicación» → `radar`: dos iconos, una antena de radar y un par de antenas de radio
- «dónde poner la energía» → `energia`: el espectro azul se desplaza hacia el valle del ruido
- «donde el ruido es más débil» → `debil`: el valle del ruido se resalta

---

# Escena 10 — RuidoDesconocido

**Capítulo YouTube:** Aprender el ruido de un tramo sin señal

## Narración

<!-- b1 -->
En la práctica no conocemos el ruido. Ni cómo se reparte en frecuencias, ni cuánto vale su varianza. ¿Qué se hace? Se graba un tramo en el que seguro no hay señal, solo ruido, y se aprende de él. Con ese tramo se pueden hacer dos cosas.

- «no conocemos el ruido» → `noconoce`: la nube y el espectro del ruido se vuelven sombras con signos de interrogación
- «cómo se reparte en frecuencias» → `reparte`: un lienzo de frecuencias con una curva punteada de interrogación
- «cuánto vale su varianza» → `varianza`: «σ² = ?»
- «¿Qué se hace?» → `quehace`: «¿qué se hace?» en ámbar
- «Se graba un tramo» → `graba`: un registro largo; se enmarca un tramo gris
- «solo ruido» → `solo`: el tramo gris se rotula «solo ruido», en magenta
- «se aprende de él» → `aprende`: una flecha del tramo a un recuadro «ruido»
- «dos cosas» → `dos`: se abren dos caminos, «1» y «2»

<!-- b2 -->
La primera: estimar la densidad espectral del ruido. Ya sabes cómo, del capítulo once: se parte el registro en trozos, se calcula el periodograma de cada uno y se promedian, el método de Welch. Con eso se construye el filtro. El precio es el de siempre: más trozos, menos varianza, pero menos resolución.

- «La primera» → `primera`: se resalta el camino «1»

- «estimar la densidad espectral del ruido» → `estimar`: «D_vv ?» en magenta
- «Ya sabes cómo» → `sabes`: aparece la etiqueta «capítulo 11» con el lienzo de frecuencias
- «se parte el registro en trozos» → `trozos`: el tramo se parte en marcos solapados, como en el capítulo 11
- «el periodograma de cada uno» → `periodo`: cada marco da una curva fina y ruidosa
- «se promedian» → `promedian`: las curvas se apilan y el promedio queda más suave
- «el método de Welch» → `welch`: la etiqueta «Welch», sobre la curva promedio
- «Con eso se construye el filtro» → `filtro`: la curva promedio entra en «H = S* / D_vv»
- «El precio es el de siempre» → `precio`: una balanza con «varianza» y «resolución»
- «más trozos, menos varianza» → `masmenos`: la curva promedio se suaviza más
- «menos resolución» → `resol`: la curva se ensancha, y se pierde el detalle

<!-- b3 -->
La segunda: ajustar un modelo con pocos coeficientes. Por ejemplo, decir que cada muestra es un cierto número por la anterior, más una moneda, como en el eco del cero coma seis. Solo hay que estimar un coeficiente, y el blanqueador sale directamente: restar ese coeficiente por la muestra anterior. Con registros cortos, un modelo pequeño casi siempre gana.

- «La segunda» → `segunda`: se resalta el camino «2»
- «un modelo con pocos coeficientes» → `modelo`: «x[n] = a x[n−1] + moneda»
- «Por ejemplo» → `ejemplo`: la ecuación empieza a escribirse con «x[n] = …»
- «un cierto número por la anterior» → `a`: el «a» se resalta en ámbar
- «más una moneda» → `moneda`: la moneda ±1 se resalta, en magenta
- «como en el eco del cero coma seis» → `eco`: «a = 0,6» en el eco
- «estimar un coeficiente» → `coef`: «â = ?» con una lupa
- «el blanqueador sale directamente» → `blanq`: la caja «x[n] − â x[n−1]»
- «restar ese coeficiente por la muestra anterior» → `restar`: se resalta el término «â x[n−1]»
- «Con registros cortos» → `cortos`: un registro corto
- «un modelo pequeño casi siempre gana» → `gana`: un tilde verde junto al modelo pequeño

---

# Escena 11 — UmbralQueSeAdapta

**Capítulo YouTube:** Un umbral que se adapta a la lluvia

## Narración

<!-- b1 -->
Y si lo único que no conocemos es la varianza del ruido, hay un problema con el umbral. Imagina un radar donde llueve en una zona: ahí el ruido es mayor, y un umbral fijo daría falsas alarmas sin parar. La solución es recalcular el umbral con la varianza estimada en las celdas vecinas, donde no hay avión. Un umbral que se adapta. Cuesta un par de decibelios.

- «lo único que no conocemos» → `unico`: una pregunta pequeña, «σ² = ?»
- «la varianza del ruido» → `var`: el ruido se dibuja con una banda de ancho variable
- «un problema con el umbral» → `problema`: una línea horizontal de umbral sobre la banda
- «un radar donde llueve» → `radar`: una antena y una nube de lluvia sobre una zona de celdas
- «el ruido es mayor» → `mayor`: en esa zona, la banda de ruido se ensancha
- «un umbral fijo» → `fijo`: el umbral recto cruza el ruido mayor
- «falsas alarmas sin parar» → `falsas`: puntos rojos de falsa alarma en el tramo de lluvia
- «recalcular el umbral» → `recalcular`: una línea nueva sube y baja con el ruido
- «las celdas vecinas» → `celdas`: se marcan las celdas a ambos lados de la celda bajo prueba
- «donde no hay avión» → `noavion`: las celdas vecinas se rotulan «sin avión», en gris
- «Un umbral que se adapta» → `adapta`: la etiqueta «CFAR» sobre la línea que se adapta, y desaparecen las falsas alarmas
- «un par de decibelios» → `decibelios`: «pérdida: un par de dB» en rojo

<!-- b2 -->
Un aviso: el filtro hereda el error de lo que se ha estimado. Un blanqueador estimado nunca es perfecto, y cuanto más corto el registro, peor.

- «Un aviso» → `aviso`: un triángulo de aviso en ámbar
- «hereda el error» → `hereda`: una flecha del estimado al filtro, con «error» en rojo
- «lo que se ha estimado» → `estimado`: el blanqueador estimado se dibuja sobre el ideal, con una pequeña diferencia
- «nunca es perfecto» → `perfecto`: la diferencia se resalta en rojo
- «cuanto más corto el registro» → `corto`: el registro se acorta
- «peor» → `peor`: la diferencia crece

---

# Escena 12 — Cierre

**Capítulo YouTube:** Lo que se viene: ¿cuándo llegó el eco?

## Narración

<!-- b1 -->
Si el ruido tiene memoria, se blanquea primero y se adapta después, y entonces la forma de la señal sí importa. Pero hasta aquí siempre hemos sabido cuándo llegaba el pulso. Un radar de verdad no lo sabe, y es justo lo que quiere medir. En el próximo episodio: ¿cuándo llegó el eco?

- «se blanquea primero» → `blanquea`: la caja «blanqueador» con el círculo de ruido blanco a la salida
- «se adapta después» → `adapta`: a su derecha, la caja «filtro adaptado»
- «la forma de la señal sí importa» → `forma`: los pulsos (1, 1) y (1, −1) con «1,25» y «5»
- «siempre hemos sabido» → `sabido`: una marca verde sobre el tiempo de llegada
- «cuándo llegaba el pulso» → `cuando`: una línea de tiempo con el pulso en un lugar fijo
- «Un radar de verdad» → `radar`: corte; la antena del radar y un avión lejano
- «justo lo que quiere medir» → `medir`: sobre la línea de tiempo, el retardo «D = ?» en ámbar
- «En el próximo episodio» → `proximo`: el título «¿Cuándo llegó el eco?» entra con rebote
- «¿cuándo llegó el eco?» → `eco`: el eco vuelve, un pulso pequeño sobre la línea de tiempo, con un signo de interrogación
