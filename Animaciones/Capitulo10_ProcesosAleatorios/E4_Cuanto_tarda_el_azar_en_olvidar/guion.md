# Episodio 4 — ¿Cuánto tarda el azar en olvidar?

Capítulo 10 (Procesos aleatorios), episodio 4 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 13 a 16), más un gancho y un cierre nuevos.

**Estado:** texto ⭐ aprobado por el usuario; momentos escritos y ritmo validado (3 huecos de 4,4–5,2 s cubiertos por animaciones); escenas `s01`–`s16` hechas; borrador 480p15 renderizado (9:15, 2 avisos menores de los controles). Falta el visto bueno del usuario al borrador (paso 15) y el render final `--calidad qh`.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Un interruptor que salta al azar. Medio segundo después, aún recuerda un treinta y siete por ciento de lo que valía. Dos segundos después, un dos por ciento. Así olvida el azar.»
- ⭐ Escena 16 (cierre): anuncia E5 por su título, «¿Basta con una sola grabación?».

Reparto de las escenas del guion base: 13 → escenas 03 a 05; 14 → 06 a 08; 15 → 09 a 11; 16 → 12 a 15.
Solo se partieron bloques enteros en escenas atómicas: el texto del guion base no cambia.

---

# Escena 01 — Gancho

**Capítulo YouTube:** Un interruptor que olvida

## Narración

<!-- b1 -->
Un interruptor que salta al azar. Medio segundo después, aún recuerda un treinta y siete por ciento de lo que valía. Dos segundos después, un dos por ciento. Así olvida el azar.

- «Un interruptor» → `interruptor`: un interruptor con una mano encima
- «salta al azar» → `salta`: la señal ±1 se dibuja con saltos irregulares
- «Medio segundo después» → `medio`: dos marcas sobre la señal, separadas medio segundo
- «treinta y siete por ciento» → `p37`: aparece «0,37» y una barra al 37 %
- «Dos segundos después» → `dos`: las marcas se separan hasta dos segundos
- «un dos por ciento» → `p2`: aparece «0,02» y la barra casi desaparece
- «olvida el azar» → `olvida`: la curva de memoria cae hasta casi cero

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** ¿Cuánto tarda el azar en olvidar?

## Narración

<!-- b1 -->
¿Cuánto tarda el azar en olvidar?

- «¿Cuánto tarda» → `t1`: las palabras «¿Cuánto tarda» entran con rebote
- «el azar en olvidar?» → `t2`: «el azar en olvidar?» entra debajo, con la etiqueta «Capítulo 10 · Procesos aleatorios»

---

# Escena 03 — Interruptor

**Capítulo YouTube:** La onda telegráfica aleatoria

## Narración

<!-- b1 -->
Imagina un interruptor que alguien acciona en momentos al azar, sin ningún patrón. La señal vale más uno o menos uno, y cada vez que alguien toca el interruptor, cambia de signo. Los cambios llegan, de media, una vez por segundo, y sin ponerse de acuerdo entre ellos. A esta señal se le llama la onda telegráfica aleatoria.

- «un interruptor» → `interruptor`: un interruptor que una mano acciona
- «en momentos al azar» → `azar`: marcas de cambio en instantes irregulares sobre el eje de tiempos
- «sin ningún patrón» → `patron`: las marcas se reparten sin orden, con separaciones distintas
- «más uno o menos uno» → `valores`: la señal se dibuja con dos niveles, +1 y −1
- «cambia de signo» → `cambia`: cada marca voltea la señal
- «una vez por segundo» → `ritmo`: un contador «λ = 1 cambio/s, de media»
- «sin ponerse de acuerdo» → `indep`: las marcas se reparten sin patrón, ninguna arrastra a otra
- «entre ellos» → `entre`: flechas ✕ entre marcas vecinas: ninguna se apoya en otra
- «onda telegráfica aleatoria» → `nombre`: la señal completa con su nombre en palabra clave

---

# Escena 04 — Poisson

**Capítulo YouTube:** La distribución de Poisson

## Narración

<!-- b1 -->
Para trabajar con ella hay que saber cuántos cambios caben en un intervalo. Llamemos lambda al ritmo medio: aquí, un cambio por segundo. En un intervalo de medio segundo esperamos, de media, lambda por te: medio cambio. Pero a veces habrá cero cambios, a veces uno, a veces dos. ¿Con qué probabilidad cada cosa?

- «cuántos cambios caben» → `cuantos`: una ventana sobre la onda que abarca un intervalo
- «lambda al ritmo medio» → `lambda`: aparece «λ = 1»
- «un cambio por segundo» → `uno_s`: el contador «1 cambio/s» parpadea
- «medio segundo» → `medio`: la ventana se acota a medio segundo
- «lambda por te» → `lt`: aparece «λT = 0,5»
- «cero cambios» → `cero`: la ventana se desliza y a veces no contiene ninguna marca
- «¿Con qué probabilidad cada cosa?» → `pregunta`: aparece «P(k) = ?» con tres casillas 0, 1, 2

<!-- b2 -->
La respuesta es la distribución de Poisson, la de los sucesos que llegan al azar a un ritmo fijo. La probabilidad de ver ka cambios es lambda te elevado a ka, por e elevado a menos lambda te, dividido entre ka factorial. La e es el número dos coma siete uno ocho. Y ka factorial es uno por dos por tres, así hasta ka: el factorial de dos es dos, y el de tres, seis.

- «distribución de Poisson» → `poisson`: el nombre en palabra clave
- «sucesos que llegan al azar» → `sucesos`: puntos que caen al azar sobre una línea de tiempo
- «ver ka cambios» → `p_k`: aparece «P(k) =»
- «lambda te elevado a ka» → `num`: entra «(λT)^k»
- «e elevado a menos lambda te» → `exp`: entra «e^(−λT)»
- «dividido entre ka factorial» → `fact`: entra «/ k!»
- «dos coma siete uno ocho» → `e`: al lado, «e ≈ 2,718»
- «uno por dos por tres» → `fact_ej`: aparece «k! = 1 · 2 · 3 · … · k»
- «el factorial de dos» → `f2`: aparece «2! = 1 · 2 = 2»
- «el de tres, seis» → `f3`: «2! = 2» y «3! = 6»

---

# Escena 05 — CuentaPoisson

**Capítulo YouTube:** Poisson con números: medio segundo

## Narración

<!-- b1 -->
Hagamos la cuenta con medio segundo. Cero cambios: e elevado a menos cero coma cinco, que es cero coma seis uno. Un cambio: cero coma cinco por eso, cero coma tres cero. Dos cambios: cero coma cinco al cuadrado, por cero coma seis uno, entre dos: cero coma cero ocho. Tres o más: algo más del uno por ciento. Y todo junto suma uno, como debe ser.

- «Hagamos la cuenta» → `cuenta`: la fórmula con λT = 0,5 sustituido
- «Cero cambios» → `p0`: se levanta la primera barra
- «cero coma seis uno» → `v61`: la barra se rotula «0,61»
- «Un cambio» → `p1`: se levanta la segunda barra
- «cero coma tres cero» → `v30`: rótulo «0,30»
- «Dos cambios» → `p2`: se levanta la tercera barra
- «cero coma cinco al cuadrado» → `cuad`: aparece «0,5² / 2 · 0,61»
- «cero coma cero ocho» → `v08`: rótulo «0,08»
- «Tres o más» → `p3`: una barra diminuta, «≈ 0,01»
- «uno por ciento» → `uno_pc`: la barra de 3 o más se rotula «≈ 1 %»
- «suma uno» → `suma`: aparece «Σ = 1» con tilde verde

<!-- b2 -->
En medio segundo, lo más probable es que no haya ningún cambio, y dos o más son raros. Si el intervalo es más largo, las probabilidades se van hacia muchos cambios. Con esto ya podemos calcular la autocorrelación de la onda: cuánto se parece la señal a sí misma medio segundo después.

- «lo más probable» → `probable`: la barra del cero se resalta
- «dos o más son raros» → `raros`: se resaltan las barras bajas
- «intervalo es más largo» → `largo`: la ventana se ensancha y las barras se desplazan a la derecha
- «muchos cambios» → `muchos`: el máximo de las barras se mueve a k mayores
- «la autocorrelación de la onda» → `autocorr`: aparece «R_xx(τ)»
- «cuánto se parece la señal» → `parece`: la onda y su copia desplazada, superpuestas
- «medio segundo después» → `despues`: dos marcas sobre la onda separadas medio segundo

---

# Escena 06 — MediaYSigno

**Capítulo YouTube:** Media cero y producto ±1

## Narración

<!-- b1 -->
Primero, la media. En cualquier instante, más uno y menos uno son igual de probables, porque los cambios no prefieren ningún signo. La media es cero. Ahora, la autocorrelación entre dos instantes separados tau. Las dos muestras valen más uno o menos uno, así que su producto también: más uno si tienen el mismo signo, y menos uno si tienen signos distintos.

- «la media» → `media`: aparece «μ_x(t)»
- «más uno y menos uno» → `igual`: dos barras iguales, 50 % y 50 %
- «no prefieren ningún signo» → `prefieren`: una balanza de +1 y −1 en equilibrio
- «La media es cero» → `cero`: aparece «μ_x = 0»
- «la autocorrelación» → `autoc`: aparece «R_xx(τ)» entre los dos cortes
- «dos instantes separados tau» → `dos_inst`: dos cortes sobre la onda con una llave rotulada «τ»
- «Las dos muestras valen» → `muestras`: las dos muestras se marcan con puntos sobre los valores +1 y −1
- «su producto» → `producto`: aparece «x(t) · x(t+τ)»
- «el mismo signo» → `mismo`: «+1 · +1 = +1» con tilde verde
- «signos distintos» → `distintos`: «+1 · −1 = −1» con cruz roja

<!-- b2 -->
¿Cuándo tienen el mismo signo? Cada cambio le da la vuelta a la señal. Con un cambio, está al revés. Con dos, vuelve a estar como al principio. Con tres, al revés otra vez. Así que las dos muestras coinciden cuando entre ellas ha habido un número par de cambios, y no coinciden cuando ha habido un número impar.

- «¿Cuándo tienen el mismo signo?» → `cuando`: pregunta sobre los dos cortes
- «le da la vuelta» → `vuelta`: una marca entre los cortes voltea la señal
- «Con un cambio» → `uno`: un cambio entre los cortes, la señal sale al revés (cruz roja)
- «Con dos» → `dos`: dos cambios, la señal vuelve igual (tilde verde)
- «Con tres» → `tres`: tres cambios, al revés otra vez (cruz roja)
- «al revés otra vez» → `otra_vez`: la señal entre cortes queda de nuevo invertida
- «las dos muestras coinciden» → `coin`: se unen los dos puntos de las muestras con una llave «=»
- «un número par» → `par`: los casos 0, 2, 4 se agrupan en verde
- «un número impar» → `impar`: los casos 1, 3 se agrupan en rojo

---

# Escena 07 — ParMenosImpar

**Capítulo YouTube:** La autocorrelación es par menos impar

## Narración

<!-- b1 -->
Entonces, la esperanza del producto es más uno por la probabilidad de un número par de cambios, más menos uno por la probabilidad de un número impar. A medio segundo, sumando con todos sus decimales, los casos pares dan cero coma seis ocho cuatro, y los impares, cero coma tres uno seis. La autocorrelación a medio segundo es la diferencia: cero coma tres seis ocho.

- «la esperanza del producto» → `esperanza`: aparece «R = E[x(t) x(t+τ)] =»
- «probabilidad de un número par» → `p_par`: entra «(+1) · P(par)»
- «probabilidad de un número impar» → `p_impar`: entra «+ (−1) · P(impar)»
- «A medio segundo» → `medio`: aparece «τ = 0,5»
- «los casos pares» → `pares`: las barras 0, 2, 4 se colorean de verde
- «cero coma seis ocho cuatro» → `v684`: las barras de Poisson pares en verde suman «0,684»
- «cero coma tres uno seis» → `v316`: las impares en rojo suman «0,316»
- «La autocorrelación a medio segundo» → `autoc`: aparece «R_xx(0,5) =» con la resta a su lado
- «es la diferencia» → `dif`: aparece «0,684 − 0,316»
- «cero coma tres seis ocho» → `v368`: resultado «0,368»

<!-- b2 -->
Si se hace la misma cuenta con un tau cualquiera, aparece una suma de términos de Poisson con los signos alternados: más, menos, más, menos. Esa suma alternada es una serie conocida, la de la exponencial, y da e elevado a menos lambda tau. Multiplicada por el e elevado a menos lambda tau que ya llevaba cada término, queda e elevado a menos dos lambda por el valor absoluto de tau.

- «un tau cualquiera» → `tau`: la cuenta con «λτ» en vez de 0,5
- «términos de Poisson» → `terminos`: la suma de términos «(λτ)^k e^(−λτ)/k!»
- «signos alternados» → `alternados`: los signos +, −, +, − sobre los términos
- «Esa suma alternada» → `suma_alt`: se encuadra la suma de términos con signos alternados
- «una serie conocida» → `conocida`: aparece el rótulo «serie conocida»
- «la de la exponencial» → `serie`: aparece la serie de e^(−x)
- «da e elevado a menos lambda tau» → `da`: la suma alternada se reduce a «e^(−λτ)»
- «Multiplicada por» → `mult`: aparece el signo «×» con el factor «e^(−λτ)»
- «que ya llevaba cada término» → `llevaba`: se resalta el factor «e^(−λτ)» de cada término
- «menos dos lambda por el valor absoluto de tau» → `resultado`: aparece «R_xx(τ) = e^(−2λ|τ|)»

---

# Escena 08 — ComprobarTelegrafica

**Capítulo YouTube:** Comprobación y estacionariedad

## Narración

<!-- b1 -->
Comprobémoslo con medio segundo y lambda igual a uno: e elevado a menos uno, que es uno entre dos coma siete uno ocho, cero coma tres seis ocho. Lo mismo que la cuenta a mano. Y la fórmula solo depende de la separación, así que, con la media constante, la onda es estacionaria en sentido amplio. La serie completa está en el apunte en profundidad.

- «Comprobémoslo» → `comprobar`: la fórmula final con los valores por sustituir
- «lambda igual a uno» → `lam1`: aparece «λ = 1, τ = 0,5»
- «e elevado a menos uno» → `em1`: aparece «e⁻¹»
- «uno entre dos coma siete uno ocho» → `div`: aparece «1 / 2,718»
- «cero coma tres seis ocho» → `v368`: resultado «≈ 0,368»
- «Lo mismo que la cuenta a mano» → `igual`: tilde verde entre este valor y el de la escena anterior
- «solo depende de la separación» → `separacion`: se resalta «τ» en la fórmula
- «con la media constante» → `mediacte`: aparece «μ_x = 0»
- «estacionaria en sentido amplio» → `wss`: sello «WSS»
- «La serie completa» → `serie_c`: aparece un pequeño libro «en profundidad»
- «apunte en profundidad» → `apunte`: nota pequeña «serie completa: apunte en profundidad, Parte 2.1»

---

# Escena 09 — LeerLaFormula

**Capítulo YouTube:** Leer la exponencial

## Narración

<!-- b1 -->
Leamos la fórmula. El valor absoluto quita el signo: da igual mirar hacia delante o hacia atrás. Y una exponencial negativa es una curva que se divide entre dos coma siete uno ocho cada vez que el exponente avanza una unidad. Con lambda uno vale uno en cero, cero coma tres siete a medio segundo, cero coma uno cuatro a un segundo y cero coma cero dos a dos segundos.

- «Leamos la fórmula» → `leer`: la curva «e^(−2|τ|)» de dos lados
- «El valor absoluto» → `abs`: se resaltan las barras de «|τ|»
- «hacia delante o hacia atrás» → `ambos`: la curva se refleja respecto del eje vertical
- «una exponencial negativa» → `expneg`: se resalta el signo menos del exponente
- «entre dos coma siete uno ocho» → `divide`: una flecha «÷ 2,718» por cada unidad de exponente
- «avanza una unidad» → `unidad`: un cursor avanza una unidad sobre el exponente
- «Con lambda uno» → `lam1`: aparece «λ = 1»
- «vale uno en cero» → `v1`: un cursor en τ = 0 deja la marca «1»
- «cero coma tres siete» → `v037`: el cursor en τ = 0,5 deja «0,37»
- «cero coma uno cuatro» → `v014`: el cursor en τ = 1 deja «0,14»
- «cero coma cero dos» → `v002`: el cursor en τ = 2 deja «0,02»

<!-- b2 -->
La curva cuenta una historia. Con tau muy pequeño, casi seguro que no ha habido ningún cambio: la señal se acuerda perfectamente de sí misma. Cuanto más lejos, más cambios caben entre medias, y el signo de antes dice cada vez menos del de ahora. La exponencial es la memoria del interruptor, borrándose. A dos segundos, prácticamente no queda nada.

- «La curva cuenta una historia» → `historia`: la curva se resalta entera
- «tau muy pequeño» → `pequeno`: dos marcas muy juntas sobre la onda, sin cambios entre ellas
- «ningún cambio» → `ninguno`: entre las dos marcas juntas, ninguna marca de cambio
- «se acuerda perfectamente» → `acuerda`: el cursor pegado al pico, valor casi 1
- «Cuanto más lejos» → `lejos`: las marcas se separan y aparecen cambios entre ellas
- «más cambios caben» → `caben`: aparecen marcas de cambio entre las dos marcas lejanas
- «dice cada vez menos» → `menos`: el valor de la curva baja con la separación
- «la memoria del interruptor» → `memoria`: rótulo «memoria» sobre la curva
- «borrándose» → `borrando`: la curva se atenúa y el rótulo «memoria» se desvanece
- «A dos segundos» → `dos_s`: el cursor llega a τ = 2 sobre la curva
- «no queda nada» → `nada`: la cola de la curva pegada al eje

---

# Escena 10 — NerviosoYTranquilo

**Capítulo YouTube:** Interruptores nerviosos y tranquilos

## Narración

<!-- b1 -->
¿Y si el interruptor es más nervioso? Con cinco cambios por segundo, la curva cae cinco veces más deprisa: a medio segundo ya vale siete milésimas. Con un cambio cada cuatro segundos, a medio segundo todavía vale cero coma siete ocho. Dos lambda es la velocidad a la que el proceso olvida. Un interruptor nervioso olvida deprisa; uno tranquilo, despacio.

- «más nervioso» → `nervioso`: una onda con muchísimos saltos
- «cinco cambios por segundo» → `cinco`: aparece «λ = 5» y la curva se estrecha
- «cae cinco veces más deprisa» → `cae5`: la curva estrecha se dibuja encima de la original
- «siete milésimas» → `v007`: marca «0,007» a medio segundo
- «un cambio cada cuatro segundos» → `tranquilo`: una onda con pocos saltos, «λ = ¼», y la curva se ensancha
- «cero coma siete ocho» → `v078`: marca «0,78» a medio segundo
- «Dos lambda es la velocidad» → `velocidad`: aparece «velocidad de olvido = 2λ»
- «a la que el proceso olvida» → `olvida`: una flecha que baja sobre la curva, rotulada «olvida»
- «olvida deprisa» → `deprisa`: se resalta la curva estrecha
- «uno tranquilo, despacio» → `despacio`: se resalta la curva ancha

---

# Escena 11 — VersionContinuaDelSensor

**Capítulo YouTube:** Del sensor al interruptor, y la pregunta

## Narración

<!-- b1 -->
Es la versión continua del sensor de temperatura. En el sensor, la correlación se multiplicaba por cero coma seis en cada paso. Aquí se multiplica por un mismo factor cada vez que pasa un mismo tiempo. Las dos son memorias que se borran poco a poco, al contrario que la de los osciladores. Y ese dos lambda volverá en el capítulo siguiente, disfrazado de ancho de banda.

- «la versión continua» → `continua`: las barras discretas del sensor se superponen a la exponencial
- «sensor de temperatura» → `sensor`: vuelve el sensor con su dibujo
- «la correlación se multiplicaba» → `correl`: barras del sensor, cada una 0,6 veces la anterior
- «cero coma seis en cada paso» → `x06`: aparece «× 0,6 por paso»
- «un mismo factor» → `factor`: la exponencial se marca a intervalos iguales con el mismo cociente
- «un mismo tiempo» → `tiempo`: las marcas a intervalos iguales del eje de la exponencial
- «Las dos son memorias» → `dos_mem`: las barras y la curva, juntas, se tiñen del mismo color
- «se borran poco a poco» → `borran`: ambas curvas decaen suavemente
- «los osciladores» → `osc`: al lado, la autocorrelación de los osciladores oscila sin apagarse
- «ese dos lambda» → `dos_lambda`: se resalta «2λ»
- «ancho de banda» → `ancho`: rótulo «2λ → capítulo 11: ancho de banda»

<!-- b2 -->
Hasta aquí, todas las cuentas del capítulo han sido promedios sobre el ensemble: en cada corte, a través de todas las realizaciones. Pero en un laboratorio nadie tiene mil interruptores ni mil sensores. Tienes un sensor, una grabación, una tarde de datos. Y la pregunta es inevitable: ¿basta con eso?

- «promedios sobre el ensemble» → `ensemble`: vuelve el ensemble entero de realizaciones
- «en cada corte» → `corte`: un corte vertical con una flecha «promedio del ensemble»
- «a través de todas las realizaciones» → `traves`: una flecha vertical cruza todas las realizaciones
- «en un laboratorio» → `lab`: aparece un matraz y un monitor de laboratorio
- «mil interruptores» → `mil`: una pila de mil interruptores
- «mil sensores» → `sensores`: junto a la pila de interruptores aparece una pila de termómetros
- «una grabación» → `una`: todo se apaga menos una realización
- «una tarde de datos» → `tarde`: un reloj de sol y un solo sensor con una banda de tiempo
- «¿basta con eso?» → `basta`: aparece «¿basta?» sobre la realización que queda

---

# Escena 12 — DosPromedios

**Capítulo YouTube:** Promedio vertical y promedio horizontal

## Narración

<!-- b1 -->
La media de un proceso es un promedio vertical: en un instante fijo, a través de todas las realizaciones. Para calcularla con datos harían falta miles de grabaciones hechas a la vez. Lo que sí puedes hacer con una sola grabación es un promedio horizontal: recorrerla a lo largo del tiempo, sumar sus valores y dividir entre la duración. Es el promedio temporal.

- «un promedio vertical» → `vertical`: corte vertical con flecha «promedio del ensemble»
- «en un instante fijo» → `fijo`: el corte vertical parpadea en un instante
- «a través de todas las realizaciones» → `traves`: la flecha vertical cruza todas las realizaciones
- «miles de grabaciones» → `miles`: las realizaciones se multiplican
- «hechas a la vez» → `vez`: todas las realizaciones suben a la vez
- «una sola grabación» → `sola`: todas se apagan menos una: «lo que tienes»
- «un promedio horizontal» → `horizontal`: una flecha horizontal recorre la realización
- «sumar sus valores» → `suma`: un contador acumula los valores
- «dividir entre la duración» → `divide`: el contador se divide entre el tiempo recorrido
- «el promedio temporal» → `temporal`: rótulo «promedio temporal» sobre la flecha

<!-- b2 -->
La pregunta es si los dos promedios coinciden. Ya nos la planteamos con la ley de los grandes números: el promedio de muchas medidas independientes se pega a la media, y dijimos que la idea volvería al promediar a lo largo de una sola grabación. Aquí está. La diferencia es que las muestras de una grabación no son independientes: tienen memoria.

- «si los dos promedios coinciden» → `coinciden`: aparece «promedio temporal = ¿media del ensemble?»
- «Ya nos la planteamos» → `plante`: aparece un sello «ya lo vimos: capítulo 7»
- «ley de los grandes números» → `grandes`: vuelven las corridas del promedio del capítulo 7
- «muchas medidas independientes» → `indep`: el eje de las corridas dice «n»
- «se pega a la media» → `pega`: la banda se angosta hacia la media
- «dijimos que la idea volvería» → `volveria`: el sello «promesa» sobre las corridas
- «a lo largo de una sola grabación» → `largo`: una flecha horizontal recorre una sola grabación
- «Aquí está» → `aqui`: el eje «n» se cambia por «tiempo»
- «La diferencia» → `difer`: aparece «¡pero!» sobre la grabación
- «no son independientes» → `noindep`: las muestras de la grabación se unen con arcos
- «tienen memoria» → `memoria`: rótulo «memoria» sobre los arcos

---

# Escena 13 — Ergodico

**Capítulo YouTube:** Qué es un proceso ergódico

## Narración

<!-- b1 -->
Cuando la respuesta es sí, el proceso se llama ergódico. Ergódico en media quiere decir que el promedio temporal, calculado sobre una ventana cada vez más larga, se acerca a la media del ensemble. Se escribe como un límite: uno entre dos te, por la integral de la señal entre menos te y te, cuando te crece sin fin.

- «se llama ergódico» → `ergodico`: la palabra «ergódico» en palabra clave
- «Ergódico en media» → `enmedia`: aparece «ergódico en media»
- «el promedio temporal» → `temporal`: el rótulo «promedio temporal» sobre la señal
- «ventana cada vez más larga» → `ventana`: la ventana [−T, T] se ensancha sobre la señal
- «la media del ensemble» → `ensemble`: el promedio temporal se acerca a una línea «μ_x»
- «un límite» → `limite`: aparece «lim_{T→∞}»
- «uno entre dos te» → `uno_dos_t`: entra «1/2T»
- «la integral de la señal» → `integral`: entra «∫ x(t) dt»
- «entre menos te y te» → `limites`: los límites «−T» y «T» sobre la integral
- «crece sin fin» → `fin`: la fórmula completa «= μ_x»

---

# Escena 14 — OsciladoresErgodicos

**Capítulo YouTube:** Los osciladores son ergódicos

## Narración

<!-- b1 -->
Probémoslo con los cuatro osciladores. Coge uno cualquiera y promedia a lo largo del tiempo. En cada período, el coseno pasa el mismo tiempo por encima del cero que por debajo, y las áreas se cancelan: el promedio temporal es cero. La media del ensemble también era cero. Coinciden. Y se habla de ergodicidad en correlación cuando, además, promediar en el tiempo la señal por su copia retrasada da la autocorrelación.

- «los cuatro osciladores» → `cuatro`: vuelven los cuatro osciladores desfasados
- «Coge uno cualquiera» → `uno`: uno se resalta y los demás se atenúan
- «a lo largo del tiempo» → `largo`: una flecha horizontal recorre el oscilador elegido
- «En cada período» → `periodo`: un período se sombrea sobre la señal
- «por encima del cero» → `encima`: el área positiva de un período, en verde
- «por debajo» → `debajo`: el área negativa, en rojo
- «las áreas se cancelan» → `cancelan`: verde y rojo del mismo tamaño
- «el promedio temporal es cero» → `cero`: aparece «promedio temporal = 0»
- «La media del ensemble también era cero» → `media_ens`: aparece «= 0 = media del ensemble»
- «Coinciden» → `coinciden`: tilde verde
- «ergodicidad en correlación» → `en_corr`: aparece «ergódico en correlación»
- «promediar en el tiempo» → `prom_t`: un contador corre a lo largo del producto
- «su copia retrasada» → `copia`: la señal y su copia retrasada τ, multiplicadas
- «da la autocorrelación» → `autocorr`: el promedio del producto da «R_xx(τ)»

---

# Escena 15 — PeroNoEsAutomatico

**Capítulo YouTube:** Pero no es automático

## Narración

<!-- b1 -->
Si un proceso es ergódico, una grabación larga vale tanto como el ensemble entero, y podemos medir su estadística con datos reales. Es tan cómodo que en la práctica se suele dar por supuesto, salvo que haya pruebas en contra. Pero no es automático. Hay procesos perfectamente estacionarios en los que una grabación, por larga que sea, no dice casi nada.

- «una grabación larga» → `larga`: una sola realización muy larga
- «el ensemble entero» → `entero`: el ensemble aparece detrás y coincide con la grabación
- «datos reales» → `reales`: aparece un sensor con su tarde de datos
- «se suele dar por supuesto» → `supuesto`: sello «se suele suponer»
- «pruebas en contra» → `pruebas`: aparece «salvo pruebas en contra»
- «no es automático» → `noauto`: el sello se rompe y aparece «pero…»
- «perfectamente estacionarios» → `estac`: sello «estacionario» sobre el proceso
- «por larga que sea» → `sea`: la grabación se alarga más y más
- «no dice casi nada» → `nada`: la grabación se apaga hasta quedar una línea plana

---

# Escena 16 — Cierre

**Capítulo YouTube:** ¿Basta con una sola grabación?

## Narración

<!-- b1 -->
Hoy hemos visto cómo olvida un proceso: la memoria del interruptor se borra como una exponencial, y con una sola grabación quizá baste, si el proceso es ergódico. Pero ¿y si no lo es? Hay procesos donde una grabación larga engaña. En el próximo episodio: ¿basta con una sola grabación?

- «cómo olvida un proceso» → `olvida`: vuelve la curva de memoria del interruptor
- «una exponencial» → `expo`: aparece «e^(−2λ|τ|)»
- «una sola grabación quizá baste» → `una`: una realización con un signo de interrogación
- «si el proceso es ergódico» → `ergodico`: aparece «ergódico»
- «¿y si no lo es?» → `y_si_no`: la palabra «ergódico» se tacha
- «una grabación larga engaña» → `engana`: la grabación larga queda como una línea constante
- «En el próximo episodio» → `proximo`: aparece «Próximo episodio»
- «¿basta con una sola grabación?» → `titulo_e5`: tarjeta con el título del próximo episodio
