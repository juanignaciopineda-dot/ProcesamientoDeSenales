# Episodio 3 — Mirar el registro entero

Capítulo 12 (Estimación de señales), episodio 3 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 09 a 13), más un gancho y un cierre nuevos.

**Estado:** `guion.md` escrito (13 escenas atómicas, con momentos), Gancho y cierre ⭐ aprobados por el usuario. `ritmo.py` sin huecos de más de 4 s; escenas `s01`–`s13` animadas; borrador 480p15 de 10:30 con 0 avisos. Falta el visto bueno del usuario al mp4 (paso 15) y el render final.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Un sistema con infinitas ecuaciones y con infinitas incógnitas. Y se resuelve con una sola división. Hoy vemos cómo.»
- ⭐ Escena 13 (cierre): resumen (la división en cada frecuencia, el error de 0,686) y la pregunta que abre E4, con su título, «El futuro no está disponible». Reemplaza las dos últimas frases de la escena 13 del guion base («Hasta aquí… no puede ver el futuro»).

Retoques al texto del guion base (por el formato de episodios):
- Escena 04, b5: «En el episodio cuarto» → «En el próximo episodio».
- Escena 05, b2: «Recuerda la escena de una sola medición» → «Recuerda la medición única del primer episodio» (es la escena 02 de E1, h = 0,8).

Notas para otros episodios:
- El cierre de E2 tiene que anunciar este título, «Mirar el registro entero».
- El cierre de este episodio anuncia E4, «El futuro no está disponible», que cobra la promesa de la escena 04 («la igualdad vale para todo eme»).
- Los coeficientes del filtro no causal (0,686 · 0,108 · 0,017) y el error 0,686 vuelven en E4 y E5 (comparación con el causal, 0,7386).
- El promediador (½, ½) es el del Cap. 10, escena 25; las densidades del sensor son las del eco del 0,6 del Cap. 11, escena 26.

Reparto de las escenas del guion base: 09 → escenas 03 y 04; 10 → 05 y 06; 11 → 07 y 08; 12 → 09 y 10; 13 → 11 y 12 (más el cierre, escena 13).
Solo se partieron bloques enteros en escenas atómicas: el texto del guion base no cambia (salvo los retoques de arriba).
Si la duración pasa de ~10,5 min, la escena de recorte es la 11–12 (deconvolución).

---

# Escena 01 — Gancho

**Capítulo YouTube:** Infinitas incógnitas, una división

## Narración

<!-- b1 -->
Un sistema con infinitas ecuaciones y con infinitas incógnitas. Y se resuelve con una sola división. Hoy vemos cómo.

- «infinitas ecuaciones» → `ecs`: una columna de ecuaciones que se alarga hacia arriba y hacia abajo hasta salirse de la pantalla
- «infinitas incógnitas» → `incog`: a su lado, una columna de «h[j]» que se alarga igual
- «una sola división» → `division`: todo se pliega en una fracción «S_yx / S_xx»
- «Hoy vemos cómo» → `como`: un «¿cómo?» en ámbar sobre la fracción

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Mirar el registro entero

## Narración

<!-- b1 -->
Mirar el registro entero

- «Mirar» → `t1`: «Mirar» entra con rebote
- «el registro entero» → `t2`: «el registro entero» entra debajo, con la etiqueta «Capítulo 12 · Estimación de señales»

---

# Escena 03 — TodoElRegistro

**Capítulo YouTube:** Usar todo el registro: pasado y futuro
**Objetivo:** el filtro con infinitos coeficientes y la condición de ortogonalidad para todo m, que da una convolución en todo el eje.

## Narración

<!-- b1 -->
Si la grabación ya está hecha, podemos usar todo el registro: el pasado, el presente y también lo que vendrá después. La estimación es una suma con infinitos coeficientes, de menos infinito a infinito: hache de jota por equis de ene menos jota. Ya no hay ninguna matriz finita que valga.

- «la grabación ya está hecha» → `grab`: la grabación de la temperatura aparece entera, con un cursor en la muestra n
- «todo el registro» → `todo`: una ventana se abre a los dos lados del cursor hasta cubrir la grabación
- «el pasado» → `pasado`: el lado izquierdo de la ventana se tiñe de cian
- «el presente» → `presente`: la muestra x[n] se marca en ámbar
- «lo que vendrá después» → `futuro`: el lado derecho de la ventana se tiñe de cian
- «una suma con infinitos coeficientes» → `suma`: aparece «ŷ[n] = Σ h[j] x[n−j]»
- «de menos infinito a infinito» → `limites`: bajo la sigma, «j de −∞ a +∞»
- «hache de jota por equis de ene menos jota» → `termino`: h[j] se marca en ámbar y x[n−j] en cian
- «Ya no hay ninguna matriz finita» → `matriz`: una matriz crece en las dos direcciones hasta salirse de la pantalla
- «que valga» → `tacha`: la matriz se tacha y aparece «no hay matriz que invertir»

<!-- b2 -->
La condición es la de siempre: el error, perpendicular a cada muestra que usamos. Y ahora usamos todas, así que la pedimos para todo eme entero, hacia los dos lados. Se repite el mismo desarrollo de antes. Sale: la suma de hache de jota por la autocorrelación en eme menos jota es la correlación cruzada en eme. Y eso es una convolución: hache convolucionado con la autocorrelación de equis es la correlación cruzada.

- «el error, perpendicular» → `perp`: aparece «e ⟂ x[n−m]» con una flecha de error a 90°
- «cada muestra que usamos» → `cada`: la flecha a 90° se repite sobre cada muestra de la ventana
- «Y ahora usamos todas» → `todas`: todas las muestras de la ventana se iluminan a la vez
- «para todo eme entero» → `todom`: «para todo m» en ámbar; hay flechas hacia los dos lados
- «hacia los dos lados» → `lados`: dos flechas de punta, una a cada lado del cursor
- «el mismo desarrollo de antes» → `desarrollo`: los renglones de E1 se repiten atenuados, pequeños
- «la suma de hache de jota» → `sumah`: «Σ h[j]»
- «por la autocorrelación en eme menos jota» → `autoc`: se suma «C_xx[m−j]»
- «es la correlación cruzada en eme» → `cruz`: se suma «= C_yx[m]»
- «una convolución» → `conv`: dos palitos se deslizan uno sobre otro
- «hache convolucionado con la autocorrelación de equis» → `hconv`: «h ∗ C_xx»
- «es la correlación cruzada» → `igual`: «= C_yx», con «para todo m» en ámbar

---

# Escena 04 — DeConvolucionAProducto

**Capítulo YouTube:** Transformar: la convolución se vuelve producto
**Objetivo:** recordar que Fourier convierte la convolución en producto, ubicar el eje Ω y transformar la igualdad porque vale en todo el eje.

## Narración

<!-- b1 -->
Recuerda qué hace Fourier con una convolución, de Señales y Sistemas: la convierte en un producto. En tiempo discreto, la frecuencia, que escribimos omega mayúscula, va de menos pi a pi. Cero es la continua, sin variación, y pi es la más rápida: la señal que alterna más, menos, más, menos, en cada muestra. Ese es el eje sobre el que vamos a trabajar.

- «qué hace Fourier» → `fourier`: aparece la caja «Fourier» con una flecha de entrada y otra de salida
- «una convolución» → `conv`: entra «h ∗ g»
- «la convierte en un producto» → `prod`: sale «H · G»; el rótulo «∗ ↔ ×»
- «En tiempo discreto» → `discreto`: una secuencia de palitos, una muestra por paso
- «omega mayúscula» → `omega`: aparece un eje horizontal rotulado «Ω»
- «va de menos pi a pi» → `rango`: el eje se marca de −π a π
- «Cero es la continua» → `cero`: en Ω = 0 una línea horizontal plana y el rótulo «continua»
- «pi es la más rápida» → `pi`: en Ω = π una señal +, −, +, −
- «más, menos, más, menos» → `alterna`: los signos se encienden uno tras otro en la señal
- «en cada muestra» → `muestra`: los signos se repiten, uno por palito
- «Ese es el eje» → `eje`: el eje queda iluminado en ámbar

<!-- b2 -->
Aquí viene el punto clave. La igualdad, hache convolucionado con la autocorrelación igual a la correlación cruzada, se cumple para todo eme. Si dos secuencias son iguales en todas sus muestras, sus transformadas son iguales en todas las frecuencias. Así que podemos transformar los dos lados: el producto de hache por la densidad espectral de equis, igual a la densidad cruzada de i griega con equis.

- «el punto clave» → `clave`: aparece «h ∗ C_xx = C_yx» con «para todo m» en ámbar
- «hache convolucionado con la autocorrelación» → `izq`: «h ∗ C_xx» a la izquierda
- «la correlación cruzada» → `der`: «= C_yx» a la derecha
- «se cumple para todo eme» → `cumple`: «para todo m» en ámbar
- «Si dos secuencias» → `secs`: dos secuencias de palitos aparecen una sobre otra
- «iguales en todas sus muestras» → `muestras`: dos secuencias de palitos idénticas, con un tilde por muestra
- «iguales en todas las frecuencias» → `frecs`: sus dos curvas transformadas coinciden
- «transformar los dos lados» → `lados`: una flecha de Fourier sobre cada lado de la igualdad
- «el producto de hache por la densidad espectral de equis» → `lado1`: «H(Ω) · S_xx(Ω)»
- «la densidad cruzada de i griega con equis» → `lado2`: «= S_yx(Ω)»

<!-- b3 -->
Ahora cada frecuencia es una ecuación con una sola incógnita, y se despeja dividiendo. Un sistema infinito, resuelto con una división. Pero guarda esto que acabamos de usar: «la igualdad vale para todo eme». En el próximo episodio veremos qué pasa cuando no vale, y por qué entonces todo se complica.

- «una ecuación con una sola incógnita» → `unaincog`: el eje se parte en rebanadas, cada una con «H · S_xx = S_yx»
- «se despeja dividiendo» → `despeja`: aparece «H = S_yx / S_xx»
- «Un sistema infinito» → `infinito`: vuelve la columna de ecuaciones infinitas
- «resuelto con una división» → `unadiv`: la columna se pliega en la fracción
- «guarda esto» → `guarda`: «para todo m» se destaca y se queda en una esquina
- «la igualdad vale para todo eme» → `vale`: la esquina «para todo m» parpadea en ámbar
- «En el próximo episodio» → `proximo`: un cartel «E4» en una esquina
- «cuando no vale» → `novale`: la esquina se tacha y aparece un «¿?» en rojo

---

# Escena 05 — LaFormulaDeWiener

**Capítulo YouTube:** El filtro de Wiener no causal
**Objetivo:** el filtro H = S_yx / S_xx y su paralelo con la medición única del capítulo 8: covarianza cruzada entre varianza.

## Narración

<!-- b1 -->
Ya tenemos el filtro: hache de omega es la densidad cruzada entre i griega y equis, dividida entre la densidad espectral de equis. Se llama filtro de Wiener no causal, porque usa también el futuro. Es una fórmula muy corta para un problema con infinitos coeficientes. Y merece que la miremos despacio, porque no es nueva.

- «Ya tenemos el filtro» → `filtro`: un recuadro ámbar con «H(Ω)»
- «hache de omega es» → `h`: «H(Ω) =»
- «la densidad cruzada entre i griega y equis» → `num`: «S_yx(Ω)» en el numerador
- «dividida entre» → `raya`: se traza la raya de la fracción
- «la densidad espectral de equis» → `den`: «S_xx(Ω)» en el denominador
- «filtro de Wiener no causal» → `sello`: sello «filtro de Wiener no causal»
- «porque usa también el futuro» → `futuro`: una flecha apunta al futuro de la grabación
- «una fórmula muy corta» → `corta`: la fórmula se agranda y queda sola
- «infinitos coeficientes» → `infinitos`: detrás aparece la fila «… h[−2] h[−1] h[0] h[1] h[2] …»
- «la miremos despacio» → `despacio`: una lupa se acerca a la fórmula
- «no es nueva» → `nueva`: sobre la fórmula, un «¿nueva?» que se tacha

<!-- b2 -->
Recuerda la medición única del primer episodio. El coeficiente era la media de i griega por equis, entre la media de equis al cuadrado: cuatro entre cinco, cero coma ocho. Una covarianza cruzada dividida entre una varianza. Pues esta es la misma división, pero hecha en cada frecuencia: la densidad cruzada, que es la covarianza entre los dos procesos en esa frecuencia, entre la densidad de equis, que es su varianza.

- «la medición única» → `unica`: a la izquierda reaparece el dibujo de y proyectada sobre x
- «El coeficiente era» → `coef`: «h =» en el dibujo de la izquierda
- «la media de i griega por equis» → `num1`: «h = E[y x]»
- «entre la media de equis al cuadrado» → `den1`: «/ E[x²]»
- «cuatro entre cinco, cero coma ocho» → `cuenta`: «= 4 / 5 = 0,8»
- «Una covarianza cruzada» → `cov`: una llave bajo el numerador
- «dividida entre una varianza» → `var`: una llave bajo el denominador
- «la misma división» → `misma`: a la derecha, la fórmula en frecuencia y una flecha que la une con la de la izquierda
- «en cada frecuencia» → `cada`: el eje Ω se parte en rebanadas
- «la covarianza entre los dos procesos en esa frecuencia» → `covf`: «S_yx» se marca en una rebanada
- «entre la densidad de equis» → `denf`: «S_xx» se marca en esa misma rebanada
- «su varianza» → `varf`: la rebanada se rotula «varianza»

---

# Escena 06 — EnCadaFrecuenciaDosVariables

**Capítulo YouTube:** En cada frecuencia, dos procesos son dos variables
**Objetivo:** el paralelo con varias variables (C⁻¹c) y la razón profunda: el filtro actúa por separado en cada frecuencia. Cobra la promesa del capítulo 11.

## Narración

<!-- b1 -->
Con varias variables, el coeficiente era la inversa de la matriz de covarianzas por el vector de covarianzas cruzadas. Aquí, la densidad de equis hace de matriz y la cruzada de vector: la misma fórmula. Es lo que anunciaba el capítulo once: en cada frecuencia, dos procesos son dos variables.

- «varias variables» → `varias`: aparece «a = C_xx⁻¹ c»
- «la inversa de la matriz de covarianzas» → `inv`: «C_xx⁻¹» se marca como «matriz de covarianzas»
- «el vector de covarianzas cruzadas» → `vec`: «c» se marca como «vector de covarianzas cruzadas»
- «la densidad de equis hace de matriz» → `hmat`: «S_xx» aparece bajo «C_xx»
- «la cruzada de vector» → `hvec`: «S_yx» aparece bajo «c»
- «la misma fórmula» → `igual`: se completa «H = S_xx⁻¹ S_yx»
- «el capítulo once» → `cap11`: una etiqueta «Cap. 11» en la esquina
- «dos procesos son dos variables» → `dosvar`: dos trazas, cortadas en una rebanada, se vuelven dos flechas

<!-- b2 -->
Hay una razón profunda. Al pasar a frecuencia, el filtro actúa por separado en cada omega: lo que hace en una frecuencia no afecta a las demás. Estimar un proceso a partir de otro se reduce, frecuencia por frecuencia, a estimar una variable a partir de otra.

- «Hay una razón profunda» → `razon`: el eje de frecuencias con todas sus rebanadas
- «el filtro actúa por separado» → `separado`: cada rebanada muestra su propio «H(Ω)»
- «en cada omega» → `omega`: una rebanada se ilumina en ámbar, luego otra
- «no afecta a las demás» → `noafecta`: flechas entre rebanadas, tachadas
- «Estimar un proceso a partir de otro» → `proceso`: dos trazas, una de y y otra de x
- «frecuencia por frecuencia» → `fxf`: la rebanada recorre el eje de izquierda a derecha
- «una variable a partir de otra» → `variable`: las trazas se reducen a dos flechas con la proyección

<!-- b3 -->
Pongámoslo a prueba con el sensor y su cable ruidoso. Piénsalo antes de seguir: si la temperatura cambia despacio y el ruido cambia deprisa, ¿en qué frecuencias te fiarías más de lo medido?

- «el sensor» → `sensor`: el termómetro del Cap. 10 con su cable ruidoso
- «Piénsalo antes de seguir» → `piensa`: pausa; aparece un reloj de pensar
- «la temperatura cambia despacio» → `lenta`: una traza azul lenta
- «el ruido cambia deprisa» → `rapido`: una traza magenta rápida
- «¿en qué frecuencias» → `preg`: el eje Ω con un «¿?» en ámbar
- «te fiarías más» → `fiar`: dos casillas, «bajas» y «altas», esperando respuesta

---

# Escena 07 — DensidadesDelSensor

**Capítulo YouTube:** El filtro de Wiener aplicado al sensor
**Objetivo:** con el sensor, S_yx = S_yy y S_xx = S_yy + S_vv, y las tres densidades en tres frecuencias.

## Narración

<!-- b1 -->
Apliquemos la fórmula al sensor. La temperatura y el ruido no tienen ninguna relación, así que la densidad cruzada entre i griega y equis es solo la de la temperatura: el ruido no aporta. Y la densidad de lo medido es la de la temperatura más la del ruido, porque las potencias de dos señales sin relación se suman. El filtro queda: la densidad de la señal, entre esa densidad más uno.

- «Apliquemos la fórmula» → `aplica`: reaparece «H = S_yx / S_xx»
- «al sensor» → `alsensor`: el termómetro del Cap. 10
- «La temperatura y el ruido» → `tyr`: la traza azul y la magenta, una junto a otra
- «ninguna relación» → `norel`: la traza de temperatura y la del ruido, separadas por un «≠»
- «la densidad cruzada entre i griega y equis» → `cruz`: «S_yx» se marca
- «solo la de la temperatura» → `sola`: se escribe «S_yx = S_yy» en azul
- «el ruido no aporta» → `noaporta`: el ruido se tacha del numerador
- «la densidad de lo medido» → `medido`: «S_xx» se marca en cian
- «la de la temperatura más la del ruido» → `suma`: se escribe «S_xx = S_yy + S_vv», con S_yy en azul y S_vv en magenta
- «las potencias de dos señales sin relación se suman» → `potsuma`: dos barras de potencia se apilan en una sola
- «El filtro queda» → `queda`: se sustituye en la fórmula
- «entre esa densidad más uno» → `final`: «H = S_yy / (S_yy + 1)»

<!-- b2 -->
Es una fracción en cada frecuencia: la parte de lo medido que es señal. La densidad de la temperatura es la del eco del capítulo once: dos coma cinco seis entre el módulo al cuadrado de uno menos cero coma seis e elevado a menos jota omega. En omega cero vale dieciséis. En pi medios, uno coma ocho ocho. En pi, uno. El ruido vale uno en todas.

- «la parte de lo medido que es señal» → `parte`: una barra cian dividida en azul (señal) y magenta (ruido), con la porción azul resaltada
- «La densidad de la temperatura» → `dtemp`: «S_yy» en azul
- «la del eco del capítulo once» → `eco`: aparece la montaña de S_yy, la del eco del 0,6
- «dos coma cinco seis» → `num`: «2,56 /» sobre la fracción
- «el módulo al cuadrado» → `den`: «|1 − 0,6 e^{−jΩ}|²» bajo la raya
- «uno menos cero coma seis» → `unomenos`: «1 − 0,6» bajo la raya
- «e elevado a menos jota omega» → `expo`: se completa «e^{−jΩ}»
- «En omega cero vale dieciséis» → `v16`: un punto sobre la curva en Ω = 0 con «16»
- «En pi medios, uno coma ocho ocho» → `v188`: un punto en Ω = π/2 con «1,88»
- «En pi, uno» → `v1`: un punto en Ω = π con «1»
- «El ruido vale uno en todas» → `ruido`: una recta plana magenta en 1

---

# Escena 08 — RepartirLaGanancia

**Capítulo YouTube:** El filtro reparte la ganancia según la señal
**Objetivo:** las tres cuentas, la curva H(Ω) suave y por qué el estimador tira hacia la media.

## Narración

<!-- b1 -->
Hacemos las cuentas. En frecuencia cero: dieciséis entre diecisiete, cero coma nueve cuatro. En pi medios: uno coma ocho ocho entre dos coma ocho ocho, cero coma seis cinco. En pi: uno entre dos, cero coma cinco. Un filtro suave que deja pasar casi todo en las frecuencias bajas y va cerrándose, sin cortar de golpe. La temperatura cambia despacio; el ruido, deprisa.

- «Hacemos las cuentas» → `cuentas`: tres casillas vacías, una por frecuencia
- «En frecuencia cero» → `f0`: «Ω = 0» en la primera casilla
- «dieciséis entre diecisiete» → `c0`: «16 / 17»
- «cero coma nueve cuatro» → `r94`: «= 0,94»
- «En pi medios» → `pm`: «Ω = π/2» en la segunda casilla
- «uno coma ocho ocho entre dos coma ocho ocho» → `c1`: «1,88 / 2,88»
- «cero coma seis cinco» → `r65`: «= 0,65»
- «En pi:» → `p`: «Ω = π» en la tercera casilla
- «uno entre dos» → `c2`: «1 / 2»
- «cero coma cinco» → `r5`: «= 0,5»
- «Un filtro suave» → `suave`: los tres puntos se unen en la curva H(Ω) ámbar
- «casi todo en las frecuencias bajas» → `bajas`: la parte izquierda de la curva se ilumina
- «sin cortar de golpe» → `golpe`: se dibuja en gris un corte rectangular, que se aparta
- «La temperatura cambia despacio» → `despacio`: la traza azul lenta vuelve a la esquina
- «el ruido, deprisa» → `deprisa`: la traza magenta rápida vuelve a la esquina

<!-- b2 -->
Lo que hace el filtro es repartir la ganancia según cuánta señal hay en cada banda. Donde la señal domina, la ganancia se acerca a uno y deja pasar. Donde manda el ruido, se acerca a cero y corta.

- «repartir la ganancia» → `reparte`: la curva H(Ω) se muestra sobre las dos densidades superpuestas
- «cuánta señal hay en cada banda» → `banda`: el eje se divide en bandas, cada una con su cociente
- «Donde la señal domina» → `domina`: una banda baja se tiñe de azul
- «se acerca a uno y deja pasar» → `uno`: la curva sube hacia 1 y una flecha cruza la banda
- «Donde manda el ruido» → `manda`: una banda alta se tiñe de magenta
- «se acerca a cero y corta» → `cero`: la curva baja y la flecha se frena contra una barrera

<!-- b3 -->
Fíjate en otra cosa: la ganancia nunca llega a uno. La estimación tiene menos amplitud que la señal verdadera. No es un error: el estimador siempre tira hacia la media, como la predicción del capítulo diez, porque cuando duda, prefiere no arriesgar. Cuanta más información tiene, menos tira.

- «la ganancia nunca llega a uno» → `nunca`: la curva H(Ω) se queda por debajo de una línea en 1
- «menos amplitud» → `amplitud`: la traza estimada, ámbar, aparece más pequeña dentro de la azul verdadera
- «No es un error» → `noerror`: un tilde verde sobre las dos trazas
- «tira hacia la media» → `tira`: flechas cortas empujan la estimación hacia la línea del cero
- «la predicción del capítulo diez» → `cap10`: la predicción que tiraba hacia la media, con etiqueta «Cap. 10»
- «cuando duda» → `duda`: un «?» sobre un punto de la traza
- «Cuanta más información tiene» → `info`: la estimación se acerca a la señal
- «menos tira» → `menos`: las flechas se acortan

---

# Escena 09 — DesarrolloDelError

**Capítulo YouTube:** El error del filtro, paso a paso
**Objetivo:** desarrollo entero de S_ee = S_yy − |S_yx|²/S_xx = S_yy (1 − |γ|²), como el σ²(1 − ρ²) del capítulo 8.

## Narración

<!-- b1 -->
Ahora, el error: i griega menos su estimación. Desarrollamos el cuadrado como siempre, con cuatro términos: la densidad de i griega; menos hache por la cruzada de equis con i griega; menos hache conjugada por la de i griega con equis; y más el módulo de hache al cuadrado por la densidad de equis.

- «el error» → `error`: aparece «e = y − ŷ» en rojo
- «Desarrollamos el cuadrado» → `cuadrado`: «S_ee = |y − ŷ|² » se abre en renglón
- «la densidad de i griega» → `t1`: «S_yy» (azul)
- «menos hache por la cruzada de equis con i griega» → `t2`: «− H S_xy»
- «menos hache conjugada por la de i griega con equis» → `t3`: «− H* S_yx», con una nota «H* = conjugada»
- «más el módulo de hache al cuadrado» → `t4`: «+ |H|²»
- «por la densidad de equis» → `dxx`: «S_xx» completa el cuarto término

<!-- b2 -->
Sustituimos hache por su valor: la cruzada entre la densidad de equis. El segundo término da menos el módulo de la cruzada al cuadrado, entre la densidad de equis. El tercero, lo mismo. Y el cuarto da más ese mismo cociente. Dos veces menos y una vez más: queda menos uno. El error es la densidad de i griega, menos ese cociente.

- «Sustituimos hache» → `sustituye`: en el renglón anterior, cada H se cambia por «S_yx / S_xx»
- «la cruzada entre la densidad de equis» → `valor`: «S_yx / S_xx» sobre el renglón
- «El segundo término da» → `d2`: el segundo término se vuelve «− |S_yx|² / S_xx»
- «menos el módulo de la cruzada al cuadrado» → `d2b`: «− |S_yx|²» sobre «S_xx»
- «entre la densidad de equis» → `dd`: se completa la fracción bajo el numerador
- «El tercero, lo mismo» → `d3`: el tercero se vuelve idéntico
- «el cuarto da más ese mismo cociente» → `d4`: el cuarto se vuelve «+ |S_yx|² / S_xx»
- «Dos veces menos y una vez más» → `cuenta`: bajo los tres cocientes, «−1 −1 +1»
- «queda menos uno» → `menos1`: queda un solo cociente, con «−1»
- «El error es la densidad de i griega» → `resultado`: «S_ee = S_yy»
- «menos ese cociente» → `menoscoc`: «− |S_yx|² / S_xx»

<!-- b3 -->
Sacamos factor común la densidad de i griega. Queda uno menos el módulo de la cruzada al cuadrado, entre el producto de las dos densidades. Ese cociente es la coherencia al cuadrado, el rho de cada frecuencia que vimos en el capítulo once. El error es la densidad de i griega por uno menos la coherencia al cuadrado: la varianza por uno menos rho al cuadrado del capítulo ocho, hecho frecuencia a frecuencia.

- «Sacamos factor común» → `factor`: «S_yy» sale como factor común, entre paréntesis
- «uno menos el módulo de la cruzada al cuadrado» → `uno_menos`: «(1 − |S_yx|²»
- «entre el producto de las dos densidades» → `producto`: «/ (S_xx S_yy))»
- «Ese cociente» → `cociente`: el cociente se enmarca
- «la coherencia al cuadrado» → `coher`: el cociente se rotula «|γ|²»
- «el rho de cada frecuencia» → `rho`: un pequeño rho bajo «γ» en varias rebanadas
- «que vimos en el capítulo once» → `vimos`: la etiqueta «Cap. 11» junto a «γ»
- «El error es la densidad de i griega» → `ee`: «S_ee = S_yy» en un recuadro
- «por uno menos la coherencia al cuadrado» → `final`: «S_ee = S_yy (1 − |γ|²)» en un recuadro
- «la varianza por uno menos rho al cuadrado» → `cap8`: a la derecha, «σ² (1 − ρ²)» con etiqueta «Cap. 8»
- «del capítulo ocho» → `delocho`: «Cap. 8» junto a la fórmula
- «frecuencia a frecuencia» → `rebanadas`: la fórmula se repite en rebanadas del eje

---

# Escena 10 — ElErrorDelSensor

**Capítulo YouTube:** El mejor error posible: 0,686
**Objetivo:** el error es no negativo gracias a Cauchy-Schwarz; con el sensor, S_ee = H y media 0,686; interpretación de la coherencia; comparación con el FIR (0,7386).

## Narración

<!-- b1 -->
Y como la coherencia nunca pasa de uno, gracias a la parábola de Cauchy-Schwarz del capítulo once, el error nunca es negativo. Con el sensor, como el ruido vale uno, el error en cada frecuencia coincide con la ganancia: cero coma nueve cuatro, cero coma seis cinco y cero coma cinco. El error total es la media de esa curva sobre todas las frecuencias: cero coma seis ocho seis.

- «la coherencia nunca pasa de uno» → `gamma1`: «|γ| ≤ 1» y una barra que no sobrepasa la línea de 1
- «la parábola de Cauchy-Schwarz» → `parabola`: la parábola del capítulo 11 con su mínimo
- «el error nunca es negativo» → `positivo`: «S_ee ≥ 0» con tilde verde
- «Con el sensor» → `consensor`: reaparece el termómetro del Cap. 10
- «el ruido vale uno» → `ruido1`: una línea plana magenta en 1
- «el error en cada frecuencia coincide con la ganancia» → `coincide`: la curva S_ee se superpone a la H(Ω) de la escena 08
- «cero coma nueve cuatro» → `t94`: un punto sobre la curva, «0,94»
- «cero coma seis cinco» → `t65`: un punto, «0,65»
- «y cero coma cinco» → `t5`: un punto, «0,5»
- «El error total» → `total`: «error total» entre llaves
- «la media de esa curva» → `media`: una línea horizontal ámbar a la altura de la media, hacia el eje
- «cero coma seis ocho seis» → `v686`: «error total = 0,686» en ámbar

<!-- b2 -->
Donde la coherencia es cercana a uno, la estimación es buena en esa banda; donde es cercana a cero, el filtro no puede hacer nada. Y ese cero coma seis ocho seis es lo mejor que puede hacer cualquier filtro lineal con el registro entero. Compáralo con el cero coma siete tres ocho seis del pasado: mirar el futuro ayuda, pero menos de lo que parece.

- «cercana a uno» → `cerca1`: un cartel «γ ≈ 1» sobre una banda
- «la estimación es buena» → `buena`: en esa banda, la estimación se pega a la señal
- «cercana a cero» → `cerca0`: un cartel «γ ≈ 0» sobre otra banda
- «no puede hacer nada» → `nada`: en esa banda, la estimación queda plana
- «ese cero coma seis ocho seis» → `ese686`: el «0,686» se agranda
- «lo mejor que puede hacer cualquier filtro lineal» → `mejor`: «0,686» en un recuadro con un sello «el mínimo»
- «con el registro entero» → `entero`: la ventana infinita de la escena 03 vuelve
- «el cero coma siete tres ocho seis del pasado» → `pasado`: a su lado «0,7386» con la ventana solo hacia atrás
- «mirar el futuro ayuda» → `ayuda`: una flecha corta entre los dos números, 0,7386 → 0,686
- «menos de lo que parece» → `parece`: la diferencia, «0,05», en una escala pequeña

---

# Escena 11 — ElBorron

**Capítulo YouTube:** Deshacer un borrón: el filtro inverso
**Objetivo:** deconvolución. La señal pasa por un sistema G que la emborrona y se le suma ruido. El inverso 1/G amplifica el ruido donde G es pequeño.

## Narración

<!-- b1 -->
Otro caso. Ahora la temperatura llega emborronada por un sistema, que llamamos ge, y encima con ruido. Como una foto movida, o un sensor con inercia. Tomemos el emborronador más sencillo, el promediador de dos muestras del capítulo diez: cada medida es la media de la temperatura de ahora y la anterior.

- «Otro caso» → `otro`: corte a un plano nuevo con la cadena en blanco
- «emborronada por un sistema» → `sistema`: y[n] entra a una caja «G»
- «ruido» → `ruido`: a la salida se suma v[n] en magenta
- «una foto movida» → `foto`: junto a la caja, una foto emborronada
- «un sensor con inercia» → `inercia`: un termómetro cuya aguja llega con retraso
- «el emborronador más sencillo» → `sencillo`: la caja G se vuelve un solo bloque simple
- «el promediador de dos muestras» → `prom`: la caja se rotula «promediador (½, ½)»
- «la media de la temperatura de ahora y la anterior» → `media`: «r[n] = (y[n] + y[n−1]) / 2»

<!-- b2 -->
Su ganancia es uno en las frecuencias lentas, cero coma siete uno en pi medios, cero coma uno seis en cero coma nueve pi y cero en pi: las altas casi desaparecen. La idea ingenua para deshacerlo es el inverso, uno entre ge, que multiplica cada frecuencia por lo contrario.

- «Su ganancia es uno» → `g1`: la curva |G(Ω)| = |cos(Ω/2)| se dibuja desde 1 en Ω = 0
- «cero coma siete uno en pi medios» → `g71`: un punto en π/2 con «0,71»
- «cero coma uno seis en cero coma nueve pi» → `g16`: un punto en 0,9π con «0,16»
- «cero en pi» → `g0`: un punto en π con «0»
- «las altas casi desaparecen» → `altas`: la parte derecha de la curva se apaga
- «La idea ingenua» → `ingenua`: aparece un «¿?» sobre la caja del inverso
- «uno entre ge» → `inverso`: «1 / G» en ámbar
- «lo contrario» → `contrario`: la curva 1/|G| sube de forma simétrica

<!-- b3 -->
Y con ruido, eso es un desastre. En cero coma nueve pi, el inverso multiplica por seis coma tres nueve; la potencia se multiplica por unos cuarenta y uno. Pero ahí la señal casi no llegó, así que lo que estamos multiplicando por seis es el ruido. En pi, donde la ganancia de ge es cero, habría que multiplicar por infinito.

- «con ruido, eso es un desastre» → `desastre`: la curva del inverso se pone en rojo
- «En cero coma nueve pi» → `en09`: una línea vertical en 0,9π sobre la curva
- «seis coma tres nueve» → `x639`: en 0,9π, «× 6,39»
- «la potencia se multiplica por unos cuarenta y uno» → `x41`: «potencia del ruido × 41»
- «Pero ahí» → `ahi`: la línea de 0,9π se mantiene
- «la señal casi no llegó» → `nollego`: la traza azul de la señal, casi plana en esa frecuencia
- «lo que estamos multiplicando por seis» → `por6`: una barra gris crece × 6
- «es el ruido» → `esruido`: la barra se tiñe de magenta
- «donde la ganancia de ge es cero» → `gcero`: la curva |G| toca el cero en π
- «habría que multiplicar por infinito» → `infinito`: en π la curva del inverso se sale de la pantalla

---

# Escena 12 — WienerDeshaceElBorron

**Capítulo YouTube:** Primero limpiar, después deshacer
**Objetivo:** el Wiener de la deconvolución: (1/G) por S_rr/(S_rr + S_vv). En 0,9π baja de 6,39 a 1,26.

## Narración

<!-- b1 -->
El filtro de Wiener sale de la misma fórmula: el inverso, uno entre ge, por un factor, la potencia de la señal emborronada entre esa potencia más la del ruido. Con señal uno y ruido cero coma uno: en cero coma nueve pi el factor es cero coma dos, y la ganancia baja de seis coma tres nueve a uno coma dos seis. En cero coma uno pi vale cero coma nueve: casi el inverso puro.

- «El filtro de Wiener sale de la misma fórmula» → `mismo`: reaparece «H = S_yx / S_xx»
- «el inverso, uno entre ge» → `inv`: «H = 1/G ·» en ámbar
- «por un factor» → `factor`: se suma «·  S_rr / (S_rr + S_vv)»
- «la potencia de la señal emborronada» → `srr`: «S_rr» se marca
- «esa potencia más la del ruido» → `suma`: «S_rr + S_vv» se marca
- «Con señal uno y ruido cero coma uno» → `datos`: «S_rr = 1, S_vv = 0,1»
- «en cero coma nueve pi» → `en09`: una línea vertical en 0,9π
- «cero coma dos» → `f02`: en 0,9π, «factor 0,2»
- «uno coma dos seis» → `g126`: la ganancia de Wiener, ámbar, cruza por 1,26; el inverso rojo sigue en 6,39
- «cero coma uno pi vale cero coma nueve» → `f09`: en 0,1π, «0,91»; las dos curvas casi coinciden
- «casi el inverso puro» → `puro`: las dos curvas se superponen

<!-- b2 -->
Se lee muy bien: primero limpiar el ruido, con ese factor que se apaga donde la señal se perdió, y después deshacer el emborronado. Nadie le ha dicho al filtro dónde parar: cuando la señal desaparece, deja de invertir.

- «primero limpiar el ruido» → `primero`: un cartel «1.º quitar el ruido» y el factor se muestra apagándose en las altas
- «se apaga donde la señal se perdió» → `apaga`: la curva del factor cae a cero hacia la derecha
- «después deshacer el emborronado» → `despues`: un cartel «2.º deshacer el borroneo» y aparece 1/G
- «Nadie le ha dicho al filtro dónde parar» → `parar`: una señal de «stop» en la curva de Wiener
- «cuando la señal desaparece» → `desaparece`: la señal azul se apaga en las altas
- «deja de invertir» → `deja`: la curva de Wiener se aparta de la roja y baja

---

# Escena 13 — Cierre

**Capítulo YouTube:** Lo que viene: el futuro no está disponible

## Narración

<!-- b1 -->
Con el registro entero, un sistema infinito se resuelve con una división en cada frecuencia: la misma cuenta del capítulo ocho, frecuencia a frecuencia. Con el sensor, lo mejor que se puede conseguir es un error de cero coma seis ocho seis. Pero un filtro de verdad no puede ver el futuro. Y entonces la división deja de valer. En el próximo episodio: el futuro no está disponible.

- «un sistema infinito» → `sistema`: la columna infinita de ecuaciones reaparece
- «una división en cada frecuencia» → `division`: se pliega en «H = S_yx / S_xx», con el eje en rebanadas
- «la misma cuenta del capítulo ocho» → `cap8`: a su lado «a = C⁻¹ c» con la etiqueta «Cap. 8»
- «frecuencia a frecuencia» → `fxf`: la rebanada recorre el eje
- «Con el sensor» → `consensor`: reaparece el termómetro
- «lo mejor que se puede conseguir» → `mejor`: un sello «el mínimo»
- «cero coma seis ocho seis» → `v686`: «0,686» en ámbar
- «un filtro de verdad» → `verdad`: un reloj en tiempo real, con la ventana abierta solo hacia el pasado
- «no puede ver el futuro» → `nover`: el lado derecho de la ventana se tacha en rojo
- «la división deja de valer» → `deja`: la fracción «S_yx / S_xx» se parte con una grieta
- «En el próximo episodio» → `proximo`: una puerta «E4» se abre
- «el futuro no está disponible» → `titulo`: el título del episodio 4 entra con rebote
