# Episodio 6 — Adivinar el futuro, limpiar el presente

Capítulo 10 (Procesos aleatorios), episodio 6 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 21 a 24), más un gancho y un cierre nuevos.

**Estado:** escenas `s01`–`s12` escritas; borrador 480p15 renderizado (9:00, 0 avisos, hojas de contacto revisadas). Falta el visto bueno del usuario (paso 15) y la revisión del texto ⭐ (gancho y cierre). Después: render final `--calidad qh` (paso 16).

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «El sensor marca veintitrés grados. Un paso después, la mejor apuesta es veintiuno coma ocho. Diez pasos después, veinte: el presente ya no sabe nada del futuro. Así de corto es el alcance de un proceso que olvida.»
- ⭐ Escena 12 (cierre): «Ya sabemos diseñar un filtro con solo las autocorrelaciones. Pero, una vez que existe, ¿qué le hace a un proceso aleatorio que pasa por él? ¿Qué pasa con su media, con su memoria, con su varianza? Lo veremos en el último episodio del capítulo: ¿Qué le hace un filtro al ruido?» Anuncia E7 por su título.
- Retoque: en la escena 11, el último bloque termina en «capítulo doce»; se quitó la pregunta final del guion base («¿qué le hace un filtro…?») porque ahora la hace el cierre.

Reparto de las escenas del guion base: 21 → escenas 03 a 05; 22 → 06 y 07; 23 → 08 y 09; 24 → 10 y 11.
Solo se partieron bloques enteros en escenas atómicas: el texto del guion base no cambia (salvo el retoque de arriba).

Empalme: el cierre de E5 (escena 23) ya anuncia este episodio como «Adivinar el futuro, limpiar el presente» y abre la «tercera cara» de la memoria; la escena 03 la retoma.

---

# Escena 01 — Gancho

**Capítulo YouTube:** El sensor que predice

## Narración

<!-- b1 -->
El sensor marca veintitrés grados. Un paso después, la mejor apuesta es veintiuno coma ocho. Diez pasos después, veinte: el presente ya no sabe nada del futuro. Así de corto es el alcance de un proceso que olvida.

- «veintitrés grados» → `v23`: la grabación del sensor en azul termina en un punto «23 °C», con la media en 20
- «Un paso después» → `uno`: un punto gris a un paso del último, con un «?»
- «veintiuno coma ocho» → `p218`: el «?» se vuelve ámbar «21,8»
- «Diez pasos después» → `diez`: el punto gris salta diez pasos a la derecha
- «veinte» → `v20`: el punto cae sobre la media: «20»
- «ya no sabe nada» → `nada`: la flecha de «+3» se encoge hasta desaparecer
- «Así de corto» → `corto`: una banda de error ensanchándose y una línea vertical «horizonte»

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Adivinar el futuro, limpiar el presente

## Narración

<!-- b1 -->
Adivinar el futuro, limpiar el presente.

- «Adivinar el futuro» → `t1`: las palabras «Adivinar el futuro» entran con rebote
- «limpiar el presente» → `t2`: «limpiar el presente» entra debajo, con la etiqueta «Capítulo 10 · Procesos aleatorios»

---

# Escena 03 — PresenteYFuturo

**Capítulo YouTube:** Predecir una muestra

## Narración

<!-- b1 -->
La tercera cara: si un proceso recuerda, se puede predecir. El sensor marca ahora veintitrés grados, tres por encima de su media. ¿Cuánto marcará en el paso siguiente? No podemos saberlo seguro, pero podemos dar la mejor apuesta. La buscaremos entre las más sencillas, una recta: la predicción es a por el dato de ahora, más be.

- «La tercera cara» → `cara`: rótulo «3.ª cara de la memoria: predecir»
- «si un proceso recuerda» → `recuerda`: dos puntos de la grabación unidos por una curva: se parecen, «recuerda»
- «El sensor marca ahora» → `sensor`: la grabación del sensor se dibuja en azul hasta el instante n₀
- «veintitrés grados» → `v23`: el último punto se resalta con «23 °C»
- «tres por encima de su media» → `media`: línea de la media en 20 y una llave «+3»
- «¿Cuánto marcará en el paso siguiente?» → `pregunta`: a la derecha, el futuro en gris con un «?»
- «No podemos saberlo seguro» → `seguro`: el «?» se rodea de una nube de valores posibles
- «la mejor apuesta» → `apuesta`: el «?» parpadea entre varios valores posibles
- «las más sencillas» → `sencillas`: una recta, una parábola y una curva rara: la recta se ilumina
- «una recta» → `recta`: se construye «x̂ = a · x[n₀] + b» pieza a pieza
- «más be» → `masb`: se completa «+ b» en la fórmula, con «a» y «b» en ámbar

---

# Escena 04 — ProyeccionDeFlechas

**Capítulo YouTube:** La proyección, otra vez

## Narración

<!-- b1 -->
Este problema ya lo resolvimos en el capítulo de estimación: la mejor estimación lineal de una variable a partir de otra. Recuerda la idea con flechas. Las variables centradas son flechas. Estimar el futuro a partir del presente es buscar el múltiplo de la flecha del presente que queda más cerca de la flecha del futuro. Y el más cercano es la proyección: el error queda perpendicular al dato.

- «capítulo de estimación» → `cap8`: un sello «Cap. 8 · estimación lineal»
- «la mejor estimación lineal» → `lineal`: «ŷ = a x + b» junto al sello
- «a partir de otra» → `otra`: una flecha de la variable «X» a la variable «Y»
- «con flechas» → `flechas`: aparecen los ejes de flechas del capítulo 8 (el mismo dibujo)
- «variables centradas» → `centradas`: las flechas salen del origen, sin la media
- «Estimar el futuro» → `estimar`: la flecha del futuro, gris, con un «?»
- «el múltiplo» → `multiplo`: copias de la flecha del presente, más largas y más cortas, sobre su recta
- «flecha del presente» → `presente`: una flecha azul «x[n₀]»
- «flecha del futuro» → `futuro`: una flecha gris «x[n₀ + m]» con otro ángulo
- «la proyección» → `proyeccion`: la sombra de la flecha del futuro sobre la del presente, en ámbar
- «perpendicular al dato» → `perp`: el error, rojo, con el cuadradito de ángulo recto

<!-- b2 -->
De esa proyección salía la fórmula. La estimación es la media de lo que se quiere adivinar, más la covarianza entre las dos variables dividida entre la varianza del dato, multiplicada por lo que el dato se aparta de su media. Y el error cuadrático medio que queda es la varianza por uno menos rho al cuadrado.

- «De esa proyección» → `fml`: aparece «ŷ =» junto al dibujo
- «La estimación es» → `estima`: el signo «=» espera sus piezas
- «la media de lo que se quiere adivinar» → `mu`: entra «μ_Y»
- «la covarianza entre las dos variables» → `cov`: entra «σ_XY»
- «la varianza del dato» → `var`: entra «/ σ_X²»
- «se aparta de su media» → `aparta`: entra «(x − μ_X)»
- «el error cuadrático medio» → `mmse`: aparece «MMSE =» en rojo
- «uno menos rho al cuadrado» → `rho2`: se completa «σ_Y² (1 − ρ²)»

---

# Escena 05 — PredictorDeProcesos

**Capítulo YouTube:** El predictor lineal de un proceso

## Narración

<!-- b1 -->
Traducido a procesos: lo que se quiere adivinar es la muestra que llegará eme pasos más adelante, y el dato es la de ahora. Como el proceso es estacionario, las dos tienen la misma media y la misma varianza, y su covarianza es la autocovarianza en eme. La predicción queda así: la media, más la autocovarianza en eme dividida entre la autocovarianza en cero, por lo que el dato se aparta de la media.

- «Traducido a procesos» → `traduce`: la fórmula del capítulo 8 sube y queda al lado
- «eme pasos más adelante» → `m`: sobre la grabación, una flecha de longitud «m» del presente al futuro
- «la de ahora» → `ahora`: se marca el punto n₀
- «es estacionario» → `estac`: sello «estacionario»
- «la misma media y la misma varianza» → `igual`: «μ_Y → μ_x» y «σ_X² → σ_x²» se sustituyen
- «su covarianza es la autocovarianza en eme» → `cm`: «σ_XY → C_xx[m]»
- «La predicción queda así» → `queda`: se arma «x̂[n₀ + m] = μ_x +»
- «más la autocovarianza en eme» → `num`: entra «C_xx[m]»
- «dividida entre la autocovarianza en cero» → `c0`: entra «/ C_xx[0]» y «(x[n₀] − μ_x)»
- «se aparta de la media» → `aparta`: el paréntesis «(x[n₀] − μ_x)» se resalta

<!-- b2 -->
Ese cociente es el coeficiente de correlación entre el presente y el futuro. Y la fórmula dice algo muy razonable. Si el presente y el futuro están muy correlacionados, le hacemos caso al dato. Si casi no lo están, nos quedamos con la media. Veamos cuánto caso le hacemos en el sensor.

- «Ese cociente» → `cociente`: el cociente se ilumina en ámbar
- «coeficiente de correlación» → `rho`: aparece «= ρ»
- «entre el presente y el futuro» → `entre`: dos puntos de la grabación unidos por una llave «m pasos»
- «algo muy razonable» → `razonable`: aparece el dial de ρ
- «muy correlacionados» → `alto`: un dial de ρ en 1 y la predicción que sigue al dato
- «le hacemos caso al dato» → `sigue`: la recta de predicción coincide con el dato
- «Si casi no lo están» → `bajo`: el dial baja a 0
- «nos quedamos con la media» → `media0`: la predicción se aplana sobre la media
- «Veamos cuánto caso» → `veamos`: el dial se apaga y vuelve el sensor
- «en el sensor» → `sensor`: vuelve la grabación del sensor con el «23»

---

# Escena 06 — UnPasoAdelante

**Capítulo YouTube:** Predecir un paso adelante

## Narración

<!-- b1 -->
Un paso adelante. La correlación es cero coma seis, y la predicción, veinte más cero coma seis por tres: veintiuno coma ocho grados. El error cuadrático medio es cuatro por uno menos cero coma tres seis: dos coma cinco seis. Sin mirar el dato, apostando a la media, el error sería la varianza entera, cuatro. Mirar el presente ha reducido el error en más de un tercio.

- «Un paso adelante» → `paso1`: la grabación con el «23» y la media en 20, y un rótulo «m = 1»
- «La correlación es cero coma seis» → `r06`: aparece «ρ = 0,6»
- «veinte más cero coma seis por tres» → `cuenta`: «20 + 0,6 · 3»; la flecha de +3 se proyecta y se encoge
- «veintiuno coma ocho grados» → `p218`: «x̂ = 21,8» en ámbar, con una banda de error alrededor
- «El error cuadrático medio» → `mmse`: aparece «MMSE =» en rojo
- «cuatro por uno menos cero coma tres seis» → `ecm`: «MMSE = 4 (1 − 0,36)»
- «dos coma cinco seis» → `e256`: «= 2,56» en rojo
- «apostando a la media» → `sindato`: la predicción baja a la línea de 20, con banda ancha
- «la varianza entera, cuatro» → `v4`: «sin dato: 4» junto al «2,56»
- «Mirar el presente» → `mirar`: la banda de error se estrecha
- «en más de un tercio» → `tercio`: dos barras de error, 4 y 2,56, la segunda más baja

<!-- b2 -->
Fíjate en que el predictor no se atreve a proyectar los tres grados enteros: solo uno coma ocho. Tira hacia la media. ¿Y ese dos coma cinco seis? Ya lo habíamos visto: era el punto más bajo de la parábola del sensor, y se alcanzaba justo en lambda igual a cero coma seis. Aquella parábola era, sin decirlo, el error de predecir una muestra a partir de otra.

- «los tres grados enteros» → `tres`: la flecha de «+3» completa, fantasma
- «solo uno coma ocho» → `uno8`: la flecha encogida «+1,8» en ámbar
- «Tira hacia la media» → `tira`: una flecha curva desde el 21,8 hacia la línea de 20
- «¿Y ese dos coma cinco seis?» → `pregunta`: el «2,56» se marca con un «?»
- «Ya lo habíamos visto» → `visto`: un fogonazo de la parábola de E3
- «el punto más bajo de la parábola» → `parabola`: reaparece la parábola del sensor (la misma de E3) con el mínimo resaltado
- «lambda igual a cero coma seis» → `lam`: «λ = 0,6» sobre el mínimo, que baja a 2,56
- «Aquella parábola» → `aquella`: la parábola se ilumina entera
- «el error de predecir una muestra» → `error`: la parábola se rotula «error de predicción»

---

# Escena 07 — TresYDiezPasos

**Capítulo YouTube:** El horizonte de la predicción

## Narración

<!-- b1 -->
Tres pasos adelante. La correlación es cero coma seis al cubo, cero coma dos uno seis. La predicción, veinte más cero coma dos uno seis por tres, da unos veinte coma seis cinco grados. El error: cuatro por uno menos cero coma dos uno seis al cuadrado, tres coma ocho uno. El dato ya casi no ayuda.

- «Tres pasos adelante» → `paso3`: el rótulo pasa a «m = 3» y el punto gris salta tres pasos
- «cero coma seis al cubo» → `cubo`: «ρ = 0,6³ = 0,216»
- «cero coma dos uno seis» → `r216`: «0,216» en ámbar
- «veinte más cero coma dos uno seis por tres» → `cuenta`: «20 + 0,216 · 3»
- «unos veinte coma seis cinco grados» → `p2065`: «x̂ ≈ 20,65», casi pegado a la media
- «cuatro por uno menos» → `ecm`: «MMSE = 4 (1 − 0,216²)»
- «tres coma ocho uno» → `e381`: «MMSE ≈ 3,81» en rojo
- «ya casi no ayuda» → `poco`: la banda de error casi tan ancha como sin dato

<!-- b2 -->
Diez pasos adelante. Cero coma seis elevado a diez son unas seis milésimas. La predicción es prácticamente la media, veinte coma cero dos, y el error es prácticamente cuatro, la varianza entera. Da igual lo que marque ahora el sensor: dentro de diez pasos, la mejor apuesta es veinte grados.

- «Diez pasos adelante» → `paso10`: el rótulo pasa a «m = 10»
- «Cero coma seis elevado a diez» → `elev`: «0,6¹⁰» se escribe
- «unas seis milésimas» → `mil`: «0,6¹⁰ ≈ 0,006»
- «prácticamente la media» → `media`: la predicción queda pegada a la línea de 20
- «veinte coma cero dos» → `p2002`: «x̂ ≈ 20,02»
- «prácticamente cuatro» → `e4`: «MMSE ≈ 4»
- «Da igual lo que marque ahora» → `igual`: el dato «23» se difumina: da lo mismo
- «la mejor apuesta es veinte grados» → `veinte`: la predicción descansa sobre la media, «20 °C»

<!-- b3 -->
La predicción lineal tiene un horizonte, y lo marca la memoria del proceso. Con la moneda, el horizonte es cero: ni un paso adelante. Con la pila es infinito: el valor de ahora es el de siempre. Y la misma idea, proyectar y dejar el error perpendicular, sirve para algo todavía más útil que predecir: limpiar una señal.

- «tiene un horizonte» → `horizonte`: la curva de predicción que baja del 23 al 20, con una línea vertical «horizonte»
- «la memoria del proceso» → `memoria`: el horizonte se ajusta con la curva de memoria de 0,6ⁿ
- «la moneda» → `moneda`: miniatura de la moneda: «horizonte 0»
- «ni un paso adelante» → `ni`: la flecha del presente al futuro de la moneda, tachada
- «Con la pila» → `pila`: miniatura de la pila: «horizonte ∞»
- «el valor de ahora es el de siempre» → `siempre`: la recta plana de la pila, a la altura del dato
- «proyectar y dejar el error perpendicular» → `proy`: vuelven las flechas con el error a 90°
- «más útil que predecir» → `util`: la flecha de proyección se une a un «¿filtrar?»
- «limpiar una señal» → `limpiar`: sobre la flecha de la proyección aparece «¿limpiar?» y una señal con ruido

---

# Escena 08 — ElProblemaDelFiltro

**Capítulo YouTube:** Limpiar una señal con ruido

## Narración

<!-- b1 -->
Ahora, el problema que da sentido a toda la asignatura. El sensor mide la temperatura, pero el cable le suma un ruido. Lo que recibimos, erre de ene, es la señal, ese de ene, más el ruido, de de ene. El ruido es como la moneda: sin memoria, de media cero, con varianza uno y sin relación con la temperatura. Queremos recuperar la señal a partir de lo recibido.

- «el problema que da sentido» → `problema`: rótulo «el problema del curso»
- «El sensor mide la temperatura» → `mide`: el sensor con su termómetro
- «el cable le suma un ruido» → `cable`: un sensor con un cable, y el ruido que se suma por el camino
- «Lo que recibimos, erre de ene» → `recibido`: sale «r[n]» en cian
- «la señal, ese de ene» → `senal`: entra «s[n]» en azul al sumador
- «el ruido, de de ene» → `ruido`: entra «d[n]» en magenta al sumador
- «es como la moneda» → `moneda`: la moneda ±1 del capítulo, en magenta
- «varianza uno» → `var1`: «media 0 · varianza 1» junto al ruido
- «sin relación con la temperatura» → `indep`: una barra entre «s» y «d» con «no correlacionados»
- «recuperar la señal» → `recuperar`: una caja «h» a la salida de r[n], con «ŝ[n]» en ámbar

<!-- b2 -->
Para simplificar, trabajemos con la temperatura centrada, restándole sus veinte grados: la señal tiene media cero y varianza cuatro. La herramienta es un filtro FIR: la estimación es una suma de las últimas ele muestras recibidas, cada una multiplicada por un coeficiente, hache de ka. Empecemos por el filtro más pequeño posible, con una sola muestra.

- «la temperatura centrada» → `centrada`: la curva del sensor baja 20 unidades y oscila alrededor de 0
- «restándole sus veinte grados» → `resta`: una flecha «−20» baja la curva
- «media cero y varianza cuatro» → `m0v4`: «media 0 · varianza 4» junto a la señal
- «un filtro FIR» → `fir`: sello «filtro FIR»
- «las últimas ele muestras» → `ventana`: una ventana de L muestras que se desliza sobre r[n]
- «multiplicada por un coeficiente» → `mult`: cada muestra de la ventana con su coeficiente encima
- «hache de ka» → `hk`: se construye «ŝ[n] = Σ h[k] r[n − k]»
- «Empecemos por el filtro más pequeño» → `empecemos`: la ventana empieza a encogerse
- «una sola muestra» → `una`: la ventana se reduce a una muestra: «ŝ = h · r»

---

# Escena 09 — FiltroDeUnaMuestra

**Capítulo YouTube:** El filtro de una sola muestra

## Narración

<!-- b1 -->
La estimación es hache por lo recibido ahora. ¿Qué hache? El que haga mínimo el error cuadrático medio. La regla es la de la proyección: el error, la señal menos hache por lo recibido, tiene que ser perpendicular al dato. Es decir, la esperanza del error por lo recibido tiene que ser cero. Despejando, hache es la esperanza de la señal por lo recibido, entre la esperanza de lo recibido al cuadrado.

- «hache por lo recibido ahora» → `hr`: queda «ŝ = h · r» en grande
- «¿Qué hache?» → `que`: el «h» parpadea con un «?»
- «mínimo el error cuadrático medio» → `minimo`: aparece «E[(s − h r)²] → mínimo»
- «es la de la proyección» → `regla`: vuelven las flechas: r, s y la sombra de s sobre r
- «la señal menos hache por lo recibido» → `resto`: «s − h r» se resalta dentro del error
- «perpendicular al dato» → `perp`: el error, rojo, a 90° de la flecha de r
- «la esperanza del error por lo recibido» → `ortog`: «E[(s − h r) r] = 0»
- «tiene que ser cero» → `cero`: «= 0» en verde
- «Despejando» → `despeja`: la ecuación se ordena paso a paso
- «entre la esperanza de lo recibido al cuadrado» → `den`: queda «h = E[s r] / E[r²]»

<!-- b2 -->
Hagamos las cuentas. La señal por lo recibido es la señal al cuadrado más la señal por el ruido. La primera esperanza es la varianza, cuatro; la segunda es cero, porque no están relacionados. Lo recibido al cuadrado da la varianza de la señal más la del ruido: cuatro más uno, cinco. Hache vale cuatro quintos: cero coma ocho.

- «Hagamos las cuentas» → `cuentas`: el cuaderno de cuentas, dos renglones vacíos
- «la señal al cuadrado más la señal por el ruido» → `suma`: «E[s r] = E[s²] + E[s d]»
- «La primera esperanza» → `primera`: «E[s²]» se ilumina
- «la varianza, cuatro» → `c4`: «= 4»
- «es cero, porque no están relacionados» → `c0`: «+ 0» y «no correlacionados»
- «Lo recibido al cuadrado» → `r2`: aparece «E[r²]»
- «la varianza de la señal más la del ruido» → `sumvar`: «4 + 1» bajo «E[r²]»
- «cuatro más uno, cinco» → `c5`: «E[r²] = 4 + 1 = 5»
- «cuatro quintos» → `q45`: «h = 4/5»
- «cero coma ocho» → `h08`: «h = 0,8» en ámbar

<!-- b3 -->
El filtro se fía de lo recibido, pero no del todo: lo encoge un veinte por ciento, porque sabe que una parte es ruido. El error que queda es cero coma ocho. Si nos quedáramos con lo recibido tal cual, el error sería todo el ruido: uno. Con una sola muestra ya mejoramos. ¿Y si usamos también la muestra anterior?

- «lo encoge un veinte por ciento» → `encoge`: la flecha de r se encoge al 80 % hasta la proyección
- «una parte es ruido» → `parte`: la parte de ruido de r, en magenta
- «El error que queda es cero coma ocho» → `e08`: barra roja «h = 0,8: 0,8»
- «Si nos quedáramos» → `quedar`: la flecha de r entera, sin encoger
- «tal cual» → `tal`: la misma flecha de r sin encoger, entera
- «todo el ruido: uno» → `e1`: barra roja más alta «sin filtrar: 1»
- «ya mejoramos» → `mejora`: flecha entre las dos barras, de 1 a 0,8
- «también la muestra anterior» → `anterior`: aparece una segunda muestra «r[n − 1]» a la izquierda

---

# Escena 10 — EcuacionesNormales

**Capítulo YouTube:** Las ecuaciones normales

## Narración

<!-- b1 -->
Con ele muestras, el error tiene que ser perpendicular a cada una de ellas: son ele condiciones, una por muestra. Si se desarrolla cada condición como antes, aparecen autocorrelaciones. La suma de cada coeficiente, hache de ka, por la autocorrelación de lo recibido en eme menos ka, tiene que ser igual a la correlación cruzada entre la señal y lo recibido en eme.

- «perpendicular a cada una de ellas» → `cada`: el error a 90° de r[n], r[n − 1], … r[n − L + 1]
- «ele condiciones» → `ele`: «L muestras → L condiciones»
- «cada condición» → `condicion`: «E[(s − ŝ) r[n − m]] = 0» se desarrolla
- «aparecen autocorrelaciones» → `auto`: «E[(s − ŝ) r[n − m]] = 0» se desarrolla y salen términos de autocorrelación
- «La suma de cada coeficiente» → `suma`: entra «Σ h[k]»
- «la autocorrelación de lo recibido en eme menos ka» → `rrr`: entra «R_rr[m − k]» en cian
- «tiene que ser igual» → `igual`: el signo «=» en ámbar
- «la correlación cruzada entre la señal y lo recibido» → `sr`: entra «= R_sr[m]»

<!-- b2 -->
Son las ecuaciones normales del capítulo de estimación, ahora con procesos: ele ecuaciones con ele incógnitas. Y como la señal y el ruido no están relacionados, se simplifican. La correlación cruzada entre la señal y lo recibido es la autocorrelación de la señal. Y la autocorrelación de lo recibido es la de la señal más la del ruido.

- «ecuaciones normales» → `normales`: sello «ecuaciones normales»
- «ele ecuaciones con ele incógnitas» → `sistema`: «m = 0 … L − 1» y «h[0] … h[L − 1]»
- «Y como la señal y el ruido» → `ycomo`: «s» en azul y «d» en magenta
- «no están relacionados» → `indep`: «s ⟂ d» con los colores de señal y ruido
- «se simplifican» → `simplifican`: los términos que sobran se tachan
- «La correlación cruzada entre la señal y lo recibido» → `ccruz`: «R_sr» en ámbar
- «es la autocorrelación de la señal» → `rss`: «R_sr = R_ss» en azul
- «Y la autocorrelación de lo recibido» → `rrecib`: «R_rr» en cian
- «es la de la señal más la del ruido» → `rrr2`: «R_rr = R_ss + R_dd» en azul y magenta

---

# Escena 11 — DosMuestras

**Capítulo YouTube:** El filtro de dos muestras

## Narración

<!-- b1 -->
Con dos muestras. La autocorrelación de la señal vale cuatro en cero y dos coma cuatro a un paso; la del ruido, uno en cero y nada más. La de lo recibido, cinco y dos coma cuatro. Primera ecuación: cinco por hache cero más dos coma cuatro por hache uno igual a cuatro. Segunda: dos coma cuatro por hache cero más cinco por hache uno igual a dos coma cuatro.

- «Con dos muestras» → `dos`: el rótulo «L = 2»
- «la señal vale cuatro en cero» → `s4`: barra azul «R_ss[0] = 4»
- «dos coma cuatro a un paso» → `s24`: barra azul «R_ss[1] = 2,4»
- «uno en cero y nada más» → `d1`: barra magenta «R_dd[0] = 1», el resto en cero
- «cinco y dos coma cuatro» → `r5`: barras cian «5» y «2,4», suma de las dos
- «Primera ecuación» → `e1`: «5 h₀ + 2,4 h₁ = 4»
- «igual a cuatro» → `igual4`: «= 4»
- «Segunda» → `e2`: «2,4 h₀ + 5 h₁ = 2,4»
- «cinco por hache uno» → `c5h1`: «+ 5 h₁» y «= 2,4»

<!-- b2 -->
Resolviendo el sistema, hache cero vale cero coma siete cuatro, y hache uno, cero coma uno dos. El filtro usa sobre todo la muestra de ahora, y un poco la anterior, porque la temperatura recuerda y el ruido no. El error baja de cero coma ocho a cero coma siete cuatro. Con más muestras seguiría bajando, cada vez menos.

- «Resolviendo el sistema» → `resuelve`: las dos ecuaciones se combinan en una flecha hacia la solución
- «hache cero vale cero coma siete cuatro» → `h0`: «h₀ ≈ 0,74» y una barra alta sobre r[n]
- «hache uno, cero coma uno dos» → `h1`: «h₁ ≈ 0,12» y una barra baja sobre r[n − 1]
- «sobre todo la muestra de ahora» → `ahora`: se resalta la barra de r[n]
- «la temperatura recuerda y el ruido no» → `recuerda`: junto a la barra baja, la curva 0,6ⁿ de memoria y la moneda sin memoria
- «de cero coma ocho a cero coma siete cuatro» → `baja`: «0,8 → 0,74» en rojo
- «Con más muestras» → `mas`: aparecen más barras a la izquierda
- «cada vez menos» → `menos`: una curva de error que baja cada vez más despacio al añadir muestras

<!-- b3 -->
Fíjate en lo que ha hecho falta para diseñar el filtro: solo la memoria de la señal y la del ruido, sus autocorrelaciones. Ninguna densidad. Esto es el germen del filtro de Wiener, que veremos en el capítulo doce.

- «solo la memoria de la señal y la del ruido» → `memorias`: las barras de R_ss y R_dd otra vez, sin más
- «sus autocorrelaciones» → `autos`: las dos barras, rotuladas «R_ss» y «R_dd»
- «Ninguna densidad» → `nada`: una densidad de probabilidad tachada
- «el filtro de Wiener» → `wiener`: sello «Wiener»
- «capítulo doce» → `cap12`: «→ capítulo 12»

---

# Escena 12 — Cierre

**Capítulo YouTube:** Lo que viene: un filtro y el ruido

## Narración

<!-- b1 -->
Ya sabemos diseñar un filtro con solo las autocorrelaciones. Pero, una vez que existe, ¿qué le hace a un proceso aleatorio que pasa por él? ¿Qué pasa con su media, con su memoria, con su varianza? Lo veremos en el último episodio del capítulo: ¿Qué le hace un filtro al ruido?

- «solo las autocorrelaciones» → `auto`: las barras de autocorrelación del filtro, pequeñas
- «una vez que existe» → `existe`: la caja «h» ya dibujada
- «un proceso aleatorio que pasa por él» → `pasa`: la caja «h» con una grabación ruidosa que entra y otra que sale
- «su media, con su memoria, con su varianza» → `tres`: tres rótulos «media · memoria · varianza» sobre la señal de salida
- «el último episodio» → `ultimo`: indicador «7 / 7»
- «¿Qué le hace un filtro al ruido?» → `titulo`: el título del E7 entra con rebote, como cierre
