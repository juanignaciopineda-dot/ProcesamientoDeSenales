# Episodio 4 — El filtro que es la señal al revés

Capítulo 13 (Detección de señales), episodio 4 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 14 a 18), más un gancho y un cierre nuevos.

**Estado:** `guion.md` con 19 escenas atómicas y momentos, validado con `ritmo.py`. Escenas `s01`–`s19` animadas; borrador 480p15 de 10:36 con 0 avisos y hojas de contacto revisadas (los palitos de varias escenas quedan chicos: candidatos a agrandar si el usuario lo pide). Pendiente: revisión del texto ⭐ (gancho y cierre, paso 9), visto bueno del usuario al mp4 (paso 15) y render final.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Dale la vuelta a una señal, úsala como filtro, y tendrás el mejor detector que se puede construir. Hoy vemos por qué.»
- ⭐ Escena 19 (cierre): repasa el episodio y anuncia el E5 por su título, «Cuando el ruido tiene memoria».

Retoques de frases del guion base, porque el episodio se ve suelto:
- Escena 14, bloque 1 (ahora escena 03): «Ya sabemos qué calcular» pasa a «En el episodio anterior vimos qué calcular».
- Escena 18, bloque 5 (ahora escena 18, segundo bloque): se quitan las dos últimas frases («Y hay otra suposición… ¿Qué pasa si el ruido tiene memoria?»); las reemplaza el cierre ⭐.
- Todo lo demás es el texto del guion base sin cambios. Los números de los dibujos son los del hilo del capítulo: `s = (2, 2, 1)`, `r = (3, 1, 2)`, `h = (1, 2, 2)`, salida `(3, 7, 10, 6, 4)` y autocorrelación `(2, 6, 9, 6, 2)`.

Reparto de las escenas del guion base: 14 → escenas 03 a 07 (un bloque por escena); 15 → 08 a 10; 16 → 11 a 13; 17 → 14 a 16; 18 → 17 y 18.

Bucles de este episodio: «más datos no bastan» (E1 → escena 18 de aquí: el promediador que no ve nada); la parábola de Cauchy-Schwarz, cuarta aparición (Caps. 7, 10 y 11 → escena 15; se cierra en E7); el pico como autocorrelación (escena 10 → E6, escenas 23 a 25); «¿y si el ruido tiene memoria?» (escena 19 → E5). Pronunciaciones a probar de oído antes de sintetizar: Cauchy-Schwarz, «cu de uno» / «cu de cero» (la función Q), «ge».

---

# Escena 01 — Gancho

**Capítulo YouTube:** El mejor detector

## Narración

<!-- b1 -->
Dale la vuelta a una señal, úsala como filtro, y tendrás el mejor detector que se puede construir. Hoy vemos por qué.

- «Dale la vuelta a una señal» → `vuelta`: las tres barras azules (2, 2, 1) se dan la vuelta y quedan (1, 2, 2)
- «úsala como filtro» → `filtro`: las barras entran en una caja «filtro»
- «el mejor detector» → `mejor`: sobre la caja aparece una corona ámbar
- «que se puede construir» → `construir`: una alarma junto a la caja se enciende
- «Hoy vemos por qué» → `porque`: una lupa se acerca a las barras

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** El filtro que es la señal al revés

## Narración

<!-- b1 -->
El filtro que es la señal al revés.

- «El filtro que es la señal» → `t1`: «El filtro que es la señal» entra con rebote
- «al revés» → `t2`: «al revés» entra debajo, con la etiqueta «Capítulo 13 · Detección de señales»

---

# Escena 03 — ElFiltro

**Capítulo YouTube:** Qué hace un filtro

**Objetivo:** recordar qué es la respuesta al impulso y cómo se calcula la salida de un filtro (dar la vuelta, deslizar, multiplicar, sumar).

## Narración

<!-- b1 -->
En el episodio anterior vimos qué calcular: ge, la suma de recibido por señal. Falta saber cómo se calcula en la práctica, y ahí entra un filtro. Recuerda cómo actúa un filtro: tiene una respuesta al impulso, que es lo que sale si entra un único uno. Y para cualquier entrada, la salida se calcula dando la vuelta a esa respuesta, deslizándola sobre la entrada, multiplicando y sumando.

- «ge, la suma de recibido por señal» → `ge`: aparece «g = Σ r[n] s[n]» con r en cian y s en azul
- «cómo se calcula en la práctica» → `practica`: un interrogante grande junto a la fórmula
- «ahí entra un filtro» → `filtro`: la fórmula se aparta y entra una caja «filtro»
- «Recuerda cómo actúa un filtro» → `recuerda`: la caja late, con un «¿qué hace?»
- «una respuesta al impulso» → `respuesta`: dentro de la caja se ve h como tres barras
- «un único uno» → `ununo`: a la entrada, un solo 1; a la salida, las barras de h
- «Y para cualquier entrada» → `entrada`: a la caja entran las barras de r = (3, 1, 2)
- «dando la vuelta a esa respuesta» → `vuelta`: las barras de h se dan la vuelta
- «deslizándola sobre la entrada» → `desliza`: h invertida se desliza sobre las barras de r
- «multiplicando y sumando» → `suma`: aparecen los productos y su suma bajo cada posición

---

# Escena 04 — AlReves

**Capítulo YouTube:** La respuesta es la señal invertida

**Objetivo:** deducir qué respuesta hace que la salida sea `g`: la señal invertida en el tiempo.

## Narración

<!-- b1 -->
Entonces la pregunta es: ¿qué respuesta hace que, en algún instante, salga justo ge? La convolución da la vuelta a la respuesta. Nosotros queremos que cada muestra recibida se multiplique por su muestra de señal. Para eso, la respuesta, una vez dada la vuelta, tiene que ser la señal. Es decir: la respuesta al impulso es la señal invertida en el tiempo.

- «¿qué respuesta hace que» → `pregunta`: aparece «¿h = ?» en ámbar
- «salga justo ge» → `ge`: se enciende «g = Σ r s» al lado
- «da la vuelta a la respuesta» → `vuelta`: h se da la vuelta (flecha curva)
- «cada muestra recibida se multiplique por su muestra de señal» → `parejas`: cada barra de r se empareja con la de s mediante una línea
- «su muestra de señal» → `suya`: las líneas se tiñen de ámbar
- «Para eso, la respuesta» → `respuesta`: la caja h se resalta
- «una vez dada la vuelta» → `dada`: h se da la vuelta otra vez
- «tiene que ser la señal» → `ser`: h invertida y s se superponen y coinciden
- «Es decir» → `esdecir`: las dos hileras de barras se alinean una bajo otra
- «la señal invertida en el tiempo» → `invertida`: «h[n] = s[L − 1 − n]» en ámbar, con h = (1, 2, 2) bajo s = (2, 2, 1)

---

# Escena 05 — LaCuentaAMano

**Capítulo YouTube:** La cuenta, a mano

**Objetivo:** hacer la convolución completa con `r = (3, 1, 2)` y `h = (1, 2, 2)`: sale `(3, 7, 10, 6, 4)`.

## Narración

<!-- b1 -->
Con números. La señal es dos, dos, uno; su inversa, uno, dos, dos. Lo recibido es tres, uno, dos. Salida en el instante cero: tres por uno, tres. En el uno: tres por dos, más uno por uno, siete. En el dos: tres por dos, más uno por dos, más dos por uno, diez. Luego seis y cuatro.

- «La señal es dos, dos, uno» → `senal`: barras azules (2, 2, 1)
- «su inversa, uno, dos, dos» → `inversa`: barras (1, 2, 2) del filtro
- «Lo recibido es tres, uno, dos» → `recibido`: barras cian (3, 1, 2)
- «Salida en el instante cero» → `i0`: h empieza a deslizar; la tabla de salida muestra y[0]
- «tres por uno, tres» → `c0`: «3·1 = 3»
- «En el uno» → `i1`: h avanza una posición
- «tres por dos, más uno por uno, siete» → `c1`: «3·2 + 1·1 = 7»
- «En el dos» → `i2`: h avanza otra posición
- «tres por dos, más uno por dos, más dos por uno» → `c2`: «3·2 + 1·2 + 2·1»
- «diez» → `diez`: «= 10» con el 10 resaltado
- «Luego seis y cuatro» → `resto`: «6» y «4» completan la tabla (3, 7, 10, 6, 4)

---

# Escena 06 — ElRetardo

**Capítulo YouTube:** El filtro adaptado y su retardo

**Objetivo:** ver que el tercer valor de la salida es `g`, entender el retardo y nombrar el filtro adaptado.

## Narración

<!-- b1 -->
Mira el tercer valor: diez. Es justo el ge que calculamos antes. Ocurre en el instante dos, que es cuando todo el pulso ya ha entrado en el filtro: hay un retardo de dos muestras. El libro lo escribe sin retardo; es el mismo número con el reloj corrido. Este filtro se llama filtro adaptado a la señal.

- «el tercer valor: diez» → `tercero`: el 10 de la tabla se agranda y se resalta
- «el ge que calculamos antes» → `ge`: un «g = 10» sale de la cuenta del episodio anterior y coincide
- «en el instante dos» → `instante`: marca sobre n = 2 en el eje de la salida
- «ya ha entrado en el filtro» → `entrado`: las tres barras de r aparecen todas dentro de la caja
- «un retardo de dos muestras» → `retardo`: una flecha «2 muestras» entre n = 0 y n = 2
- «sin retardo» → `sinret`: una nota «el libro: h[k] = s[−k], muestrear en 0»
- «el reloj corrido» → `reloj`: un reloj gira dos pasos y la nota se desplaza
- «filtro adaptado a la señal» → `adaptado`: «filtro adaptado (matched filter)» entra con rebote en ámbar

---

# Escena 07 — ElDetectorCompleto

**Capítulo YouTube:** El detector completo

**Objetivo:** juntar la cadena entera y plantear por qué funciona tan bien.

## Narración

<!-- b1 -->
Así que el detector completo es una cadena sencilla: la señal recibida entra en el filtro adaptado, se toma la salida en el instante en que ha entrado todo el pulso, y se compara con el umbral. Sí o no. Y queda una pregunta: ¿por qué funciona tan bien? Hay dos formas de verlo: en el tiempo y en la frecuencia.

- «una cadena sencilla» → `cadena`: la cadena en blanco: «r[n] → h → muestrear → γ → H₁ / H₀»
- «la señal recibida entra» → `entra`: «r[n]» se enciende en cian
- «en el filtro adaptado» → `filtro`: la caja «h» se enciende en ámbar
- «se toma la salida» → `muestreo`: un interruptor «n = 2» recoge un valor
- «se compara con el umbral» → `umbral`: aparece «γ = 4,5»
- «Sí o no» → `sino`: salen «H₁» y «H₀»
- «¿por qué funciona tan bien?» → `porque`: un interrogante grande sobre la caja
- «en el tiempo» → `tiempo`: un reloj a la izquierda
- «y en la frecuencia» → `frec`: un espectro a la derecha

---

# Escena 08 — SenalLimpia

**Capítulo YouTube:** Primera lectura: en el tiempo

**Objetivo:** con la señal limpia a la entrada, la salida es `(2, 6, 9, 6, 2)`, con el pico igual a la energía.

## Narración

<!-- b1 -->
Primera lectura, en el tiempo. Imagina que a la entrada del filtro no hay ruido: solo la señal, dos, dos, uno, pasando por el filtro uno, dos, dos. Calculamos la salida igual que antes. Instante cero: dos por uno, dos. Instante uno: dos por dos, más dos por uno, seis. Instante dos: dos por dos, más dos por dos, más uno por uno, nueve.

- «Primera lectura, en el tiempo» → `lectura`: «1.ª lectura: el tiempo» entra con rebote, con un reloj
- «Imagina que» → `imagina`: la caja y r aparecen a la izquierda
- «no hay ruido» → `sinruido`: la franja magenta del ruido desaparece de r
- «dos, dos, uno, pasando» → `pasa`: las barras azules (2, 2, 1) entran a la caja
- «el filtro uno, dos, dos» → `filtro`: la caja muestra h = (1, 2, 2)
- «Calculamos la salida» → `calculamos`: la tabla de salida, vacía, bajo la caja
- «igual que antes» → `antes`: h invertida se coloca al comienzo de la señal
- «Instante cero» → `i0`: se abre la tabla de salida
- «dos por uno, dos» → `c0`: «2·1 = 2»
- «Instante uno» → `i1`: h avanza
- «dos por dos, más dos por uno, seis» → `c1`: «2·2 + 2·1 = 6»
- «Instante dos» → `i2`: h avanza
- «más uno por uno, nueve» → `c2`: «2·2 + 2·2 + 1·1 = 9» con el 9 resaltado

<!-- b2 -->
Y los dos últimos: dos por dos, más uno por dos, seis; uno por dos, dos. La salida es dos, seis, nueve, seis, dos: un pico en el medio, y ese pico vale nueve, que es justo la energía. Cada valor compara la señal con una copia suya desplazada: se multiplican y se suman.

- «Y los dos últimos» → `ultimos`: h sigue avanzando
- «más uno por dos, seis» → `c3`: «2·2 + 1·2 = 6»
- «uno por dos, dos» → `c4`: «1·2 = 2»
- «dos, seis, nueve, seis, dos» → `salida`: la salida (2, 6, 9, 6, 2) como tallos
- «un pico en el medio» → `pico`: el tallo central se alza y se resalta
- «vale nueve» → `nueve`: «9» sobre el pico
- «la energía» → `energia`: «E = 9» junto al pico
- «una copia suya desplazada» → `copia`: la señal y una copia desplazada, una sobre otra
- «se multiplican y se suman» → `suman`: aparecen «×» y «Σ» entre ellas

---

# Escena 09 — LaAutocorrelacion

**Capítulo YouTube:** La salida es la autocorrelación

**Objetivo:** reconocer la autocorrelación determinista y ver por qué el máximo está en desplazamiento cero.

## Narración

<!-- b1 -->
Eso es una autocorrelación, la misma idea del capítulo diez, aunque aquí sin promedios: la señal es una sola y la conocemos. Y el pico ocurre sin desplazar: cada muestra se multiplica por sí misma, y la suma de cuadrados es la energía. Con cualquier desplazamiento, las barras dejan de coincidir y la suma baja.

- «una autocorrelación» → `auto`: «autocorrelación» entra con rebote junto a la salida
- «el capítulo diez» → `cap10`: un recuadro pequeño «capítulo 10» con la autocorrelación de la moneda
- «sin promedios» → `sinprom`: «E[ ]» tachado en rojo
- «la señal es una sola» → `una`: una única hilera de barras azules
- «la conocemos» → `conocemos`: una marca verde «conocida» sobre las barras
- «sin desplazar» → `sindesp`: señal y copia exactamente superpuestas
- «se multiplica por sí misma» → `misma`: cada barra con su cuadrado: 4, 4, 1
- «la suma de cuadrados es la energía» → `cuadrados`: «2² + 2² + 1² = 9 = E»
- «cualquier desplazamiento» → `desp`: la copia se corre una posición
- «dejan de coincidir» → `coinciden`: las barras no se alinean; los productos se achican
- «la suma baja» → `baja`: «6» y después «2» sobre los tallos laterales

---

# Escena 10 — ElPico

**Capítulo YouTube:** Por qué se muestrea en el pico

**Objetivo:** en el pico la señal destaca al máximo sobre el ruido, que pesa igual en cualquier instante. El filtro adaptado es un detector de parecidos.

## Narración

<!-- b1 -->
Aquí está la razón de muestrear en el pico. En ese instante, la contribución de la señal es máxima: nueve, contra seis o dos en los vecinos. La contribución del ruido, en cambio, es del mismo tamaño en cualquier instante. Así que en el pico, la señal destaca lo más posible sobre el ruido.

- «muestrear en el pico» → `pico`: sobre la salida (2, 6, 9, 6, 2) un cursor marca n = 2
- «la contribución de la señal es máxima» → `maxima`: el tallo central en azul brillante
- «nueve, contra seis o dos en los vecinos» → `vecinos`: «9», «6» y «2» sobre los tres tallos
- «La contribución del ruido» → `ruido`: una franja magenta aparece bajo los tres instantes
- «del mismo tamaño» → `igual`: la franja mide lo mismo en los tres
- «Así que en el pico» → `asique`: el cursor vuelve al pico
- «la señal destaca» → `destaca`: en el pico el tallo azul asoma muy por encima de la franja; en los vecinos, menos

<!-- b2 -->
Por eso el filtro adaptado es un detector de parecidos. Se queda tranquilo mientras lo que entra no se parece a la señal buscada, y da un pico cuando aparece algo que sí se le parece, y el pico crece con lo parecido que sea. Ahora, veamos la misma idea en el mundo de las frecuencias.

- «un detector de parecidos» → `detector`: «detector de parecidos» entra con rebote en ámbar
- «Se queda tranquilo» → `tranquilo`: entra ruido y la salida es una línea casi plana
- «no se parece a la señal buscada» → `noparece`: la entrada es una forma distinta de s, sin pico en la salida
- «da un pico» → `pico`: entra la señal y la salida da un pico, con una alarma
- «el pico crece» → `crece`: con una copia más parecida (más grande) el pico sube
- «Ahora, veamos la misma idea» → `ahora`: el reloj se aparta a la izquierda
- «en el mundo de las frecuencias» → `mundo`: un espectro se desliza desde la derecha

---

# Escena 11 — SinusoidesFlechas

**Capítulo YouTube:** Segunda lectura: en la frecuencia

**Objetivo:** recordar la señal como suma de sinusoides con amplitud y fase, dibujadas como flechas, y ver que la suma máxima exige flechas alineadas.

## Narración

<!-- b1 -->
Segunda lectura, en la frecuencia. De Señales y Sistemas: cualquier señal es una suma de sinusoides. Cada una tiene una amplitud y una fase, es decir, un desplazamiento. Como en el capítulo once, podemos dibujar cada sinusoide como una flecha con una longitud, la amplitud, y un ángulo, la fase.

- «Segunda lectura, en la frecuencia» → `lectura`: «2.ª lectura: la frecuencia» entra con rebote
- «De Señales y Sistemas» → `sys`: un recuadro pequeño «Señales y Sistemas»
- «una suma de sinusoides» → `suma`: tres sinusoides de frecuencias y desfases distintos se suman en una forma irregular
- «una amplitud y una fase» → `ampfase`: una sinusoide se resalta con su altura y su desfase marcados
- «un desplazamiento» → `desp`: una flecha horizontal marca cuánto está corrida
- «el capítulo once» → `cap11`: un recuadro pequeño «capítulo 11: números complejos como flechas»
- «una flecha» → `flecha`: la sinusoide se convierte en una flecha que gira
- «una longitud, la amplitud» → `long`: la longitud de la flecha se marca en ámbar
- «un ángulo, la fase» → `ang`: el arco del ángulo se marca en ámbar

<!-- b2 -->
Ahora, ¿qué haría falta para que todas esas sinusoides se sumaran lo más posible en el instante de muestreo? Que sus flechas apuntaran en la misma dirección. Con números: tres flechas de longitud uno, en ángulos cero, ciento veinte y doscientos cuarenta grados, se cancelan: suman cero. Alineadas, suman tres.

- «qué haría falta» → `falta`: las tres flechas aparecen con un interrogante
- «se sumaran lo más posible» → `sumar`: una flecha resultante larga con «¿máximo?»
- «instante de muestreo» → `muestreo`: una línea vertical «n = 2» sobre las sinusoides
- «apuntaran en la misma dirección» → `misma`: las tres flechas se señalan con un «=»
- «tres flechas de longitud uno» → `tres`: tres flechas de longitud 1 salen del origen
- «en ángulos cero» → `a0`: la primera marca «0°»
- «ciento veinte» → `c120`: la segunda marca «120°»
- «doscientos cuarenta grados» → `c240`: la tercera marca «240°»
- «suman cero» → `cero`: puestas punta con cola cierran un triángulo: «Σ = 0»
- «Alineadas, suman tres» → `alin`: las tres giran hasta alinearse: «Σ = 3»

---

# Escena 12 — LaConjugada

**Capítulo YouTube:** La respuesta en frecuencia del filtro adaptado

**Objetivo:** `H = conj(S)`: mismo módulo, ángulo con el signo cambiado; así todas las componentes quedan alineadas.

## Narración

<!-- b1 -->
Eso es lo que hace el filtro adaptado. Su respuesta en frecuencia es la conjugada de la transformada de la señal: mismo módulo, pero el ángulo cambiado de signo. Cada flecha de la señal, al pasar por el filtro, gira justo el ángulo contrario al suyo y queda apuntando a cero. Todas alineadas: se suman al máximo.

- «Su respuesta en frecuencia» → `resp`: aparece «H(Ω)» junto al filtro
- «la conjugada de la transformada» → `conj`: «H = S*» en ámbar
- «mismo módulo» → `modulo`: dos flechas de igual longitud, una de S y otra de H
- «el ángulo cambiado de signo» → `signo`: la flecha de H es el espejo de la de S respecto del eje real
- «Cada flecha de la señal» → `cada`: tres flechas de S con ángulos distintos
- «gira justo el ángulo contrario» → `gira`: cada una gira por el ángulo opuesto al suyo
- «apuntando a cero» → `cero`: las tres quedan apuntando a 0°
- «Todas alineadas» → `alin`: las tres se encuentran en una misma recta
- «se suman al máximo» → `max`: se suman en una flecha larga: «|S|²» sobre ella

---

# Escena 13 — ElRuidoDesordenado

**Capítulo YouTube:** Qué pasa con el ruido

**Objetivo:** el módulo acentúa donde hay señal; el ruido, de fase al azar, no se alinea. Las dos lecturas dicen lo mismo.

## Narración

<!-- b1 -->
Y el módulo hace su parte: el filtro amplifica las frecuencias donde la señal tiene contenido y atenúa donde no lo tiene. El ruido blanco es plano: tiene lo mismo en todas las frecuencias. Así que amplificar donde está la señal gana señal sin ganar tanto ruido.

- «el módulo hace su parte» → `modulo`: |H| se dibuja como una curva sobre el eje de frecuencias
- «amplifica las frecuencias donde la señal tiene contenido» → `ampl`: la curva sube donde el espectro de la señal tiene su bulto
- «atenúa donde no lo tiene» → `atenua`: la curva baja donde la señal no tiene nada
- «El ruido blanco es plano» → `plano`: una línea horizontal magenta
- «lo mismo en todas las frecuencias» → `todas`: la línea magenta recorre todo el eje
- «Así que amplificar» → `asique`: una flecha ámbar sube sobre el bulto
- «gana señal sin ganar tanto ruido» → `gana`: tras el filtro, el bulto azul sube y la línea magenta apenas cambia

<!-- b2 -->
¿Y el ruido? Sus flechas tienen ángulos al azar. Al girarlas, siguen sin apuntar al mismo sitio, así que no se suman: se quedan en una flecha corta. Las dos lecturas dicen lo mismo: en el tiempo, el filtro busca parecidos; en la frecuencia, pone la señal en fase consigo misma y deja al ruido desordenado.

- «¿Y el ruido?» → `ruido`: flechas magentas aparecen
- «ángulos al azar» → `azar`: cada flecha apunta a un lado distinto
- «Al girarlas» → `girar`: giran, pero siguen desordenadas
- «no se suman» → `nosuma`: puestas punta con cola, el recorrido se enreda
- «una flecha corta» → `corta`: la resultante es una flecha pequeña
- «Las dos lecturas» → `dos`: aparecen las dos lecturas lado a lado: reloj y espectro
- «en el tiempo, el filtro busca parecidos» → `tiempo`: bajo el reloj, un pico en la autocorrelación
- «en la frecuencia, pone la señal en fase» → `fase`: bajo el espectro, tres flechas alineadas
- «deja al ruido desordenado» → `desorden`: bajo el espectro, las flechas magentas sin ordenar

---

# Escena 14 — MedirFiltros

**Capítulo YouTube:** Cómo medir lo bueno que es un filtro

**Objetivo:** definir la relación señal-ruido de salida de un filtro cualquiera y calcularla para el promediador y el adaptado.

## Narración

<!-- b1 -->
¿Es este el mejor filtro que existe? Y una segunda pregunta: ¿y si el ruido es blanco, pero no sabemos que sea gaussiano? Entonces no podemos calcular la regla de error mínimo. Pero podemos medir cuánto separa un filtro las dos hipótesis: la relación señal-ruido de su salida, la diferencia de medias al cuadrado dividida entre la varianza.

- «el mejor filtro que existe» → `mejor`: la corona ámbar sobre el filtro adaptado, con un interrogante
- «una segunda pregunta» → `segunda`: aparece una campana magenta con «¿gaussiano?»
- «no sabemos que sea gaussiano» → `nogauss`: la campana se deforma
- «Entonces no podemos calcular» → `entonces`: «MAP» con una cruz roja
- «la regla de error mínimo» → `regla`: «regla de error mínimo» en rojo, tachada
- «cuánto separa un filtro las dos hipótesis» → `separa`: dos campanas de salida, una en cada hipótesis, con una flecha entre sus centros
- «la relación señal-ruido de su salida» → `snr`: «SNR de salida» entra con rebote
- «la diferencia de medias al cuadrado» → `medias`: aparece «(μ₁ − μ₀)²» sobre una raya
- «dividida entre la varianza» → `varianza`: aparece «σ²_salida» bajo la raya

<!-- b2 -->
Para un filtro cualquiera, la media con señal es la suma de señal por filtro, y la varianza del ruido es sigma cuadrado por la suma de los cuadrados del filtro. Prueba con el promediador, uno, uno, uno: media cinco, al cuadrado veinticinco, varianza tres: ocho coma tres tres. El adaptado da ochenta y uno entre nueve: nueve.

- «la media con señal» → `media`: aparece «μ₁ = Σ s h»
- «la suma de señal por filtro» → `sumasf`: s y h se emparejan barra a barra
- «la varianza del ruido» → `varruido`: aparece «Var = σ² Σ h²»
- «sigma cuadrado por la suma de los cuadrados» → `sigma`: se resaltan «σ²» y «Σ h²»
- «Prueba con» → `prueba`: s = (2, 2, 1) en azul
- «el promediador, uno, uno, uno» → `prom`: barras (1, 1, 1) bajo s = (2, 2, 1)
- «media cinco» → `m5`: «2 + 2 + 1 = 5»
- «veinticinco» → `v25`: «5² = 25»
- «varianza tres» → `v3`: «1 + 1 + 1 = 3»
- «ocho coma tres tres» → `r833`: «25 / 3 = 8,33» en ámbar
- «ochenta y uno entre nueve» → `ad81`: junto, «adaptado: 81 / 9 = 9»

---

# Escena 15 — LaParabola

**Capítulo YouTube:** La parábola, por cuarta vez

**Objetivo:** la desigualdad de Cauchy-Schwarz a partir de una suma de cuadrados, con el dibujo de la parábola de los capítulos 7, 10 y 11.

## Narración

<!-- b1 -->
¿Existe algún filtro que supere nueve? Y aquí aparece un viejo conocido, por cuarta vez: la parábola de Cauchy-Schwarz. Toma dos listas de números, equis e i griega, y un número lambda cualquiera. La suma de equis menos lambda por i griega, al cuadrado, es una suma de cuadrados: nunca es negativa.

- «supere nueve» → `supere`: «¿> 9?» junto al 9 del adaptado
- «un viejo conocido» → `conocido`: la parábola del capítulo 7 aparece en pequeño, con «cap. 7 · 10 · 11»
- «por cuarta vez» → `cuarta`: un contador «cuarta vez» en ámbar
- «la parábola de Cauchy-Schwarz» → `parabola`: la parábola en grande, con sus ejes
- «dos listas de números, equis e i griega» → `listas`: dos filas de casillas «x₁ x₂ x₃» e «y₁ y₂ y₃»
- «un número lambda cualquiera» → `lambda`: «λ» con un deslizador
- «equis menos lambda por i griega, al cuadrado» → `suma`: aparece «Σ (x − λy)²»
- «una suma de cuadrados» → `cuadrados`: cada término del sumatorio se marca como un cuadrado
- «nunca es negativa» → `nuncaneg`: «≥ 0» en verde

<!-- b2 -->
La desarrollamos y es una parábola en lambda. Nunca baja de cero, así que no puede cortar el eje dos veces: su discriminante no es positivo. Queda que la suma de equis por i griega, al cuadrado, no supera la suma de los cuadrados de equis por la de i griega. Aplicada al filtro: la relación de salida no supera la energía entre sigma cuadrado.

- «La desarrollamos» → `desarrolla`: «(Σx²)λ² − 2(Σxy)λ + Σy² ≥ 0»
- «una parábola en lambda» → `parab`: la expresión se grafica como parábola abierta hacia arriba
- «Nunca baja de cero» → `nunca`: la parábola se queda por encima del eje
- «cortar el eje dos veces» → `corta`: una segunda parábola que corta dos veces, tachada en rojo
- «su discriminante no es positivo» → `discr`: «Δ ≤ 0»
- «la suma de equis por i griega, al cuadrado» → `cs`: se escribe «(Σxy)²»
- «no supera la suma de los cuadrados de equis» → `nosupera`: «≤ (Σx²)»
- «por la de i griega» → `porlade`: «(Σy²)» completa la desigualdad
- «Aplicada al filtro» → `aplic`: se sustituye x = s, y = h
- «la energía entre sigma cuadrado» → `cota`: «SNR ≤ E / σ²» en ámbar

---

# Escena 16 — NadaSeGana

**Capítulo YouTube:** Ningún filtro supera al adaptado

**Objetivo:** la igualdad se da cuando `h` es múltiplo de `s`; el máximo es la relación de entrada, así que el adaptado no pierde nada. Dos justificaciones independientes.

## Narración

<!-- b1 -->
La igualdad se da si la parábola toca el eje, es decir, cuando el filtro es un múltiplo de la señal: el filtro adaptado. Y ese máximo, la energía entre sigma cuadrado, es la relación señal-ruido que ya había a la entrada: no se pierde nada. Dos justificaciones independientes: con ruido gaussiano, minimiza el error; solo con ruido blanco, maximiza la relación señal-ruido.

- «La igualdad se da» → `igualdad`: se resalta el «=» de «SNR = E / σ²»
- «la parábola toca el eje» → `toca`: la parábola baja hasta tocar el eje en un único punto
- «un múltiplo de la señal» → `multiplo`: h = c·s con las barras de h proporcionales a las de s
- «el filtro adaptado» → `adaptado`: «adaptado» entra con rebote junto a la parábola
- «ese máximo» → `maximo`: la cota se marca con una corona
- «la relación señal-ruido que ya había a la entrada» → `entrada`: «SNR entrada = E / σ²» a la izquierda de la caja, igual que la cota
- «no se pierde nada» → `nada`: un «=» verde entre entrada y salida
- «Dos justificaciones independientes» → `dos`: aparecen dos recuadros lado a lado
- «con ruido gaussiano, minimiza el error» → `gauss`: el recuadro izquierdo: «ruido gaussiano → mínimo error»
- «solo con ruido blanco, maximiza» → `blanco`: el recuadro derecho: «solo blanco → máxima SNR»
- «maximiza la relación señal-ruido» → `maxsnr`: la «SNR» del recuadro sube hasta su cota

---

# Escena 17 — CuantoSePierde

**Capítulo YouTube:** Cuánto se pierde con otros filtros

**Objetivo:** medir con números cuánto se pierde con el promediador y con la muestra suelta; la pérdida es el coseno al cuadrado del ángulo entre filtro y señal.

## Narración

<!-- b1 -->
¿Cuánto se pierde con un filtro que no es el adaptado? Comparemos tres. El adaptado. El promediador, uno, uno, uno, que suma todo lo recibido, como el promediador del capítulo diez. Y quedarse solo con una muestra, la más grande. La pérdida de un filtro es el coseno al cuadrado del ángulo entre él y la señal: la fracción de relación señal-ruido que conserva.

- «¿Cuánto se pierde» → `cuanto`: «¿cuánto se pierde?» en ámbar
- «Comparemos tres. El adaptado» → `tres`: la primera barra de tres filas: el adaptado (2, 2, 1)
- «El promediador, uno, uno, uno» → `prom`: segunda fila: (1, 1, 1)
- «como el promediador del capítulo diez» → `cap10`: un recuadro pequeño «capítulo 10: (½, ½)»
- «solo con una muestra» → `muestra`: tercera fila: (1, 0, 0), con la barra suelta
- «La pérdida de un filtro» → `perdida`: «pérdida» en rojo
- «el coseno al cuadrado del ángulo» → `coseno`: las flechas s y h con el ángulo entre ellas y «cos² θ»
- «la fracción de relación señal-ruido que conserva» → `fraccion`: «cos² θ = SNR del filtro / SNR del adaptado»

<!-- b2 -->
Con el pulso dos, dos, uno. El promediador da veinticinco entre veintisiete: cero coma nueve dos seis. Pierde menos de medio decibelio: casi nada. La muestra suelta da cuatro entre nueve: cero coma cuatro cuatro cuatro. Pierde más de la mitad, tres coma cinco decibelios.

- «Con el pulso dos, dos, uno» → `pulso`: s = (2, 2, 1) en azul sobre las tres filas
- «El promediador da» → `da`: se resalta la fila del promediador
- «veinticinco entre veintisiete» → `v27`: «25 / 27»
- «cero coma nueve dos seis» → `r926`: «= 0,926»
- «menos de medio decibelio» → `db`: «−0,33 dB» en verde
- «casi nada» → `casi`: una barra casi llena
- «La muestra suelta» → `suelta`: la tercera fila se resalta
- «cuatro entre nueve» → `c49`: «4 / 9»
- «cero coma cuatro cuatro cuatro» → `r444`: «= 0,444»
- «Pierde más de la mitad» → `mitad`: la barra de la muestra suelta queda por debajo de la mitad
- «tres coma cinco decibelios» → `db35`: «−3,52 dB» en rojo, con la barra por debajo de la mitad

<!-- b3 -->
Traducido a errores: el adaptado se equivoca cero coma cero seis seis ocho. El promediador, cero coma cero siete cuatro cinco, apenas más. Pero la muestra suelta, cu de uno, cero coma uno cinco nueve: más del doble de errores. Tirar las otras dos muestras, más de la mitad de la energía, sale caro.

- «Traducido a errores» → `trad`: las tres filas pasan a mostrar su error
- «cero coma cero seis seis ocho» → `e0668`: «Q(1,5) = 0,0668» en la primera
- «cero coma cero siete cuatro cinco» → `e0745`: «Q(1,44) = 0,0745» en la segunda
- «apenas más» → `apenas`: una flechita corta entre 0,0668 y 0,0745
- «cu de uno» → `q1`: «Q(1)» en la tercera
- «cero coma uno cinco nueve» → `e159`: «= 0,159» en rojo
- «más del doble de errores» → `doble`: «× 2,4» junto al 0,159
- «Tirar las otras dos muestras» → `tirar`: las dos barras de la muestra suelta que valen 0 se tachan
- «sale caro» → `caro`: el 0,159 se agranda y tiembla

---

# Escena 18 — LaSorpresa

**Capítulo YouTube:** El promediador que no ve nada

**Objetivo:** con `s = (1, −2, 1)` el promediador queda perpendicular a la señal y no ve nada; cualquier desalineación cuesta. Retomar «promediar no siempre es buena idea».

## Narración

<!-- b1 -->
Ahora una sorpresa. Cambia el pulso por uno, menos dos, uno. Tiene energía seis y es tan detectable como cualquier otro. Pero mira al promediador: uno menos dos, más uno, cero. Su filtro es perpendicular a la señal: coseno cero. No ve nada. Su error es cu de cero: un medio, tirar una moneda.

- «una sorpresa» → `sorpresa`: «sorpresa» entra con rebote
- «uno, menos dos, uno» → `pulso`: barras azules (1, −2, 1), la del medio hacia abajo
- «energía seis» → `e6`: «E = 6»
- «tan detectable» → `detectable`: una marca verde «detectable» junto a la energía
- «mira al promediador» → `mira`: las barras (1, 1, 1) en una fila bajo el pulso
- «uno menos dos, más uno, cero» → `suma0`: «1 − 2 + 1 = 0»
- «perpendicular a la señal» → `perp`: las flechas s y h con marca de ángulo recto
- «coseno cero» → `cos0`: «cos² 90° = 0»
- «No ve nada» → `nada`: un ojo se cierra sobre el promediador
- «cu de cero» → `q0`: «Q(0)»
- «tirar una moneda» → `moneda`: «= 0,5» y una moneda al aire

<!-- b2 -->
La muestra suelta, la del menos dos con su signo, aún conserva dos tercios. Moraleja: cualquier desalineación con la señal cuesta, y puede costarlo todo. Promediar no siempre es buena idea, como ya vimos con las dos mediciones.

- «La muestra suelta» → `suelta`: la fila (0, −2, 0)
- «dos tercios» → `tercios`: «4 / 6 = 0,667 (−1,76 dB)»
- «Moraleja» → `moraleja`: «moraleja» entra con rebote
- «cualquier desalineación con la señal cuesta» → `cuesta`: una escala de ángulos de 0° a 90° con la fracción que se conserva cayendo
- «puede costarlo todo» → `todo`: la escala llega a 0 en 90°
- «Promediar no siempre es buena idea» → `promediar`: el promediador (1, 1, 1) tachado en rojo junto a (1, −2, 1)
- «las dos mediciones» → `dos`: un recuadro pequeño del episodio 1: el cuadrado de las dos mediciones uniformes

---

# Escena 19 — Cierre

**Capítulo YouTube:** Lo que viene: cuando el ruido tiene memoria

## Narración

<!-- b1 -->
El filtro adaptado es la señal al revés: en el tiempo busca parecidos, en la frecuencia alinea las fases, y ningún otro filtro saca más relación señal-ruido. Pero todo esto suponía ruido blanco. ¿Y si el ruido tiene memoria? En el próximo episodio: cuando el ruido tiene memoria.

- «es la señal al revés» → `reves`: las barras (2, 2, 1) y (1, 2, 2) con la flecha de dar la vuelta
- «en el tiempo busca parecidos» → `tiempo`: el pico (2, 6, 9, 6, 2) con su alarma
- «en la frecuencia alinea las fases» → `frec`: las tres flechas que se alinean
- «ningún otro filtro» → `ninguno`: la parábola tocando el eje en un punto
- «Pero todo esto suponía» → `pero`: aparece un signo de advertencia
- «ruido blanco» → `blanco`: una línea magenta plana
- «¿Y si el ruido tiene memoria?» → `memoria`: la línea se vuelve una curva con memoria (el eco del 0,6)
- «En el próximo episodio» → `proximo`: el reloj avanza
- «cuando el ruido tiene memoria» → `titulo`: el título «Cuando el ruido tiene memoria» entra con rebote
