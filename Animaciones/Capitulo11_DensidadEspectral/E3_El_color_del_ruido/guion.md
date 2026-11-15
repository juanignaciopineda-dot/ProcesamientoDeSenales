# Episodio 3 — El color del ruido

Capítulo 11 (Densidad espectral de potencia), episodio 3 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 11 a 15), más un gancho y un cierre nuevos.

**Estado:** texto ⭐ aprobado por el usuario; escenas `s01`–`s15` animadas; borrador 480p15 de 10:10 con 0 avisos, hojas de contacto revisadas. Falta el visto bueno del usuario al mp4 (paso 15) y el render final.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Hay ruidos con color, igual que la luz. Y el color de un ruido depende de una sola cosa: cuánto recuerda. Hoy vemos por qué.»
- ⭐ Escena 15 (cierre): el final de la escena 15 del guion base (la moneda, el resumen y el archivo con datos) más una frase nueva que anuncia E4 por su título, «Un espectro a partir de datos».

Notas para otros episodios:
- El cierre de E2 tiene que anunciar este título, «El color del ruido».
- Este episodio paga la promesa de la escena 04 (E1): la cuenta de la densidad de la telegráfica (escenas 05 a 07 de aquí). El dibujo de la curva 4/(4 + ω²) es el mismo.
- La escena 14 del guion base dice «el proceso del episodio anterior»: es el de las tres barras con ρ = 0,4 (escenas 09 y 10 de E2).

Reparto de las escenas del guion base: 11 → escenas 03 y 04; 12 → 05 a 07; 13 → 08 a 10; 14 → 11 y 12; 15 → 13 y 14 (y la última parte, el cierre, en la 15).
Solo se partieron bloques enteros en escenas atómicas: el texto del guion base no cambia (salvo un salto de línea suelto en la escena 12, b1).

---

# Escena 01 — Gancho

**Capítulo YouTube:** El color de un ruido

## Narración

<!-- b1 -->
Hay ruidos con color, igual que la luz. Y el color de un ruido depende de una sola cosa: cuánto recuerda. Hoy vemos por qué.

- «Hay ruidos con color» → `color`: una traza de ruido magenta y, a su lado, su espectro pintado con degradado de colores
- «igual que la luz» → `luz`: un prisma abre un rayo blanco en un arcoíris
- «el color de un ruido» → `forma`: tres espectros de formas distintas (plano, joroba, pico) aparecen en fila
- «cuánto recuerda» → `recuerda`: bajo cada espectro, su autocorrelación (barra, decaimiento, coseno)
- «Hoy vemos por qué» → `porque`: un «¿por qué?» en ámbar sobre los tres pares

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** El color del ruido

## Narración

<!-- b1 -->
El color del ruido

- «El color» → `t1`: «El color» entra con rebote
- «del ruido» → `t2`: «del ruido» entra debajo, con la etiqueta «Capítulo 11 · Densidad espectral de potencia»

---

# Escena 03 — TensionDeCincoVoltios

**Capítulo YouTube:** Media y fluctuaciones: cuánta potencia tiene

## Narración

<!-- b1 -->
Muchas señales no oscilan alrededor de cero. Piensa en una tensión que fluctúa alrededor de cinco voltios, con una desviación típica de un voltio. Hay dos cosas mezcladas: un valor medio que no cambia nunca, y unas fluctuaciones que van y vienen alrededor de él. ¿Cuánta potencia tiene?

- «no oscilan alrededor de cero» → `nocero`: una traza oscila alrededor de una línea en cero y, de golpe, toda la traza sube lejos del cero
- «una tensión» → `tension`: la traza queda en azul sobre un eje vertical rotulado «V»
- «cinco voltios» → `cinco`: la línea central se rotula «5 V»
- «una desviación típica de un voltio» → `desv`: una banda de ±1 V se abre alrededor de la línea
- «Hay dos cosas mezcladas» → `dos`: aparecen dos casillas vacías a la derecha, «media» y «fluctuaciones»
- «un valor medio que no cambia nunca» → `media`: la línea de 5 V se separa hacia arriba, plana, con el rótulo «media»
- «unas fluctuaciones» → `fluct`: las oscilaciones quedan abajo, centradas en cero, con el rótulo «fluctuaciones»
- «¿Cuánta potencia tiene?» → `pregunta`: aparece «¿potencia?» en ámbar

<!-- b2 -->
Del capítulo siete: la varianza es la esperanza del cuadrado menos la media al cuadrado. Despejando, la potencia es la media al cuadrado más la varianza: veinticinco más uno, veintiséis. Veinticinco son de la parte constante, lo que en electrónica se llama la continua. Solo uno es de las fluctuaciones.

- «la varianza» → `var`: aparece «σ² =»
- «la esperanza del cuadrado» → `esp`: se suma «E[x²]»
- «menos la media al cuadrado» → `menos`: se suma «− μ²»
- «Despejando» → `despeja`: la fórmula se reordena en «E[x²] = μ² + σ²»
- «la media al cuadrado más la varianza» → `sumaps`: en la fórmula, μ² se marca en ámbar y σ² en magenta
- «veinticinco más uno» → `suma`: debajo, «= 25 + 1» con el 25 en ámbar y el 1 en magenta
- «veintiséis» → `v26`: «= 26» en ámbar
- «la parte constante» → `const`: el 25 se marca con una barra alta azul, la media
- «la continua» → `continua`: aparece el rótulo «la continua (DC)»
- «Solo uno» → `uno`: el 1 se marca con una barra pequeña magenta y el rótulo «fluctuaciones»

---

# Escena 04 — LaMediaEsUnImpulso

**Capítulo YouTube:** La media es un impulso en el origen

## Narración

<!-- b1 -->
Con las autocorrelaciones pasa lo mismo: la autocorrelación es la autocovarianza más la media al cuadrado. La autocovarianza mide solo las fluctuaciones, así que su transformada es la densidad espectral de las fluctuaciones. Se escribe de sub equis equis. ¿Y la media al cuadrado? Es una constante, y la transformada de una constante es un impulso.

- «la autocorrelación es» → `auto`: aparece «R_xx(τ) =»
- «la autocovarianza» → `cov`: se suma «C_xx(τ)» y la curva de autocovarianza se dibuja abajo
- «más la media al cuadrado» → `mu2`: se suma «+ μ²» y un escalón constante de altura 25 sube bajo la curva
- «mide solo las fluctuaciones» → `solofl`: la curva C_xx se separa del escalón y queda sola, en magenta
- «su transformada» → `transf`: una flecha lleva C_xx(τ) a un eje de frecuencias
- «la densidad espectral de las fluctuaciones» → `dens`: sobre el eje sale la curva y el rótulo «densidad de las fluctuaciones»
- «Se escribe» → `escribe`: debajo de la curva aparece un recuadro vacío para el nombre
- «de sub equis equis» → `dxx`: la curva se nombra «D_xx(jω)»
- «¿Y la media al cuadrado?» → `preg`: el escalón de 25 se resalta con un «?»
- «una constante» → `constante`: el escalón se marca con el rótulo «constante»
- «un impulso» → `impulso`: sobre el eje de frecuencias nace una flecha vertical en cero

<!-- b2 -->
Un impulso es un pico infinitamente estrecho con un área fija: toda la potencia concentrada en un solo punto, la frecuencia cero. Así que la densidad espectral es la de las fluctuaciones más un impulso en el origen de área dos pi por la media al cuadrado. Comprobación: la curva aporta uno, el impulso aporta veinticinco. Veintiséis.

- «un pico infinitamente estrecho» → `pico`: un pico se estrecha y crece
- «con un área fija» → `area`: el área bajo el pico se sombrea y se mantiene constante mientras él cambia
- «toda la potencia concentrada» → `toda`: todo el sombreado del área se acumula en la flecha
- «la frecuencia cero» → `cero`: el pico se vuelve la flecha vertical en ω = 0
- «la densidad espectral es la de las fluctuaciones» → `sumaesp`: aparece «S_xx = D_xx»
- «más un impulso en el origen» → `impo`: se suma «+ 2π μ² δ(ω)»
- «dos pi por la media al cuadrado» → `areaimp`: «2π μ²» se marca como el área de la flecha
- «Comprobación» → `compro`: aparece una casilla «comprobación» con dos sumandos vacíos
- «la curva aporta uno» → `aporta1`: sobre la curva, «área 2π → 1»
- «el impulso aporta veinticinco» → `aporta25`: sobre la flecha, «2π · 25 → 25»
- «Veintiséis» → `total`: «total 26» con un tilde verde

<!-- b3 -->
Esto tiene una consecuencia práctica. Si la media es grande, ese impulso se lleva casi toda la potencia, y cuando se estima el espectro con datos, derrama sobre las frecuencias vecinas y tapa lo que queríamos ver. Por eso, antes de estimar un espectro, lo primero es restar la media.

- «una consecuencia práctica» → `practica`: la flecha y la curva quedan en pantalla con un «!» ámbar
- «la media es grande» → `grande`: la flecha crece muchísimo
- «se lleva casi toda la potencia» → `lleva`: la flecha tapa la curva de las fluctuaciones
- «se estima el espectro con datos» → `datos`: un archivo de datos entra en una caja «estimador» y la flecha sale con la curva debajo
- «derrama sobre las frecuencias vecinas» → `derrama`: la flecha se ensancha con faldas a los lados
- «tapa lo que queríamos ver» → `tapa`: la curva desaparece bajo las faldas
- «Por eso» → `poreso`: un «!» ámbar junto a la curva tapada
- «antes de estimar un espectro» → `antes`: la caja «estimador» se resalta con el archivo de datos delante
- «restar la media» → `resta`: aparece «x − μ», la flecha se apaga y la curva reaparece

---

# Escena 05 — LaTelegraficaPartida

**Capítulo YouTube:** La cuenta prometida: partir la integral

## Narración

<!-- b1 -->
Hace dos episodios prometimos una cuenta: la densidad espectral de la onda telegráfica. Su autocorrelación es e elevado a menos alfa por el valor absoluto de tau, donde alfa es dos lambda, el doble del ritmo de saltos. El valor absoluto obliga a partir la integral en dos mitades: a la derecha del cero, donde tau es positivo, y a la izquierda, donde es negativo.

- «Hace dos episodios prometimos una cuenta» → `promesa`: vuelve la curva 4/(4 + ω²) del primer episodio con un «¿cómo se calcula?»
- «la onda telegráfica» → `tele`: la onda de ±1 se dibuja
- «e elevado a menos alfa» → `ealfa`: aparece «R_xx(τ) = e^{−α …»
- «el valor absoluto de tau» → `abs`: la fórmula se completa con «|τ|»
- «alfa es dos lambda» → `dosl`: aparece «α = 2λ»
- «el doble del ritmo de saltos» → `doble`: «λ = ritmo de saltos» con unos saltos marcados en la onda
- «El valor absoluto obliga» → `obliga`: el «|τ|» de la fórmula se resalta en ámbar
- «partir la integral en dos mitades» → `partir`: la curva e^{−α|τ|} queda dividida por una línea vertical en cero
- «a la derecha del cero» → `der`: la mitad derecha se resalta con «τ > 0»
- «a la izquierda» → `izq`: la mitad izquierda se resalta con «τ < 0»

<!-- b2 -->
Una herramienta primero: el área bajo una exponencial que decae, e elevado a menos a por tau, desde cero hasta infinito, vale uno sobre a. Con a igual a dos, un medio. En la mitad derecha, la autocorrelación por la exponencial compleja da e elevado a menos alfa más jota omega, por tau. Es lo mismo con a igual a alfa más jota omega: uno sobre alfa más jota omega.

- «Una herramienta primero» → `herr`: la pantalla se limpia a un plano nuevo con «una herramienta»
- «el área bajo una exponencial que decae» → `areaexp`: se dibuja la curva e^{−aτ} con el área sombreada
- «e elevado a menos a por tau» → `eatau`: aparece «e^{−aτ}» sobre la curva
- «desde cero hasta infinito» → `limites`: aparece «∫₀^∞ … dτ» alrededor de la curva
- «vale uno sobre a» → `unosoba`: «= 1/a»
- «Con a igual a dos» → `a2`: la curva se ajusta a a = 2
- «un medio» → `medio`: «= ½» con el área marcada
- «En la mitad derecha» → `mitadder`: vuelve la mitad derecha de la curva de la escena anterior
- «la exponencial compleja» → `compleja`: aparece «e^{−jωτ}»
- «da e elevado a menos alfa más jota omega» → `producto`: el producto se construye en «e^{−(α + jω)τ}»
- «por tau» → `portau`: «τ» se marca al final del exponente
- «Es lo mismo con a igual a alfa más jota omega» → `igual`: en la fórmula de la herramienta, a se reemplaza por «α + jω»
- «uno sobre alfa más jota omega» → `resultado1`: aparece «= 1/(α + jω)» en ámbar

---

# Escena 06 — SumarLasMitades

**Capítulo YouTube:** Sumar las dos mitades

## Narración

<!-- b1 -->
La mitad izquierda es su espejo, y da uno sobre alfa menos jota omega. Ahora sumamos las dos fracciones con denominador común. Arriba: alfa menos jota omega más alfa más jota omega. Las jotas se cancelan y queda dos alfa. Abajo: alfa al cuadrado menos jota omega al cuadrado.

- «La mitad izquierda es su espejo» → `espejo`: la mitad izquierda se refleja sobre la derecha con una flecha curva
- «uno sobre alfa menos jota omega» → `izq`: aparece «1/(α − jω)»
- «sumamos las dos fracciones» → `suma`: las dos fracciones quedan sumadas en una línea
- «denominador común» → `comun`: las barras de fracción se alinean y se ensanchan
- «Arriba» → `arriba`: el numerador «(α − jω) + (α + jω)»
- «más alfa más jota omega» → `masalfa`: entra el segundo paréntesis «+ (α + jω)» del numerador
- «Las jotas se cancelan» → `cancelan`: las dos jω se tachan
- «dos alfa» → `dosalfa`: queda «= 2α» en ámbar
- «Abajo» → `abajo`: el denominador «(α + jω)(α − jω)»
- «alfa al cuadrado menos jota omega al cuadrado» → `difcuad`: se convierte en «α² − (jω)²»

<!-- b2 -->
Y jota al cuadrado es menos uno, porque jota es la raíz de menos uno. Menos por menos: alfa al cuadrado más omega al cuadrado. Resultado: dos alfa dividido entre alfa al cuadrado más omega al cuadrado. Con alfa igual a dos, cuatro dividido entre cuatro más omega al cuadrado. La que usamos. Promesa cumplida.

- «jota al cuadrado es menos uno» → `j2`: aparece «j² = −1» resaltado
- «la raíz de menos uno» → `raiz`: «j = √−1»
- «Menos por menos» → `menosmenos`: «−(−ω²) = +ω²»
- «alfa al cuadrado más omega al cuadrado» → `den`: el denominador queda «α² + ω²»
- «Resultado» → `res`: aparece «S_xx(jω) =» con el numerador «2α»
- «dos alfa dividido entre» → `frac`: la fracción se completa «2α / (α² + ω²)»
- «alfa al cuadrado más omega al cuadrado» → `denfin`: el denominador de la fracción se completa «α² + ω²»
- «Con alfa igual a dos» → `alfa2`: «α = 2» y se sustituye en la fracción
- «cuatro dividido entre cuatro más omega al cuadrado» → `cuatro`: queda «4 / (4 + ω²)» en ámbar
- «La que usamos» → `usamos`: a su lado se dibuja la curva del primer episodio, que coincide
- «Promesa cumplida» → `cumplida`: un tilde verde sobre «prometimos»

---

# Escena 07 — ElExamenYLaMediaAltura

**Capítulo YouTube:** El examen y la media altura

## Narración

<!-- b1 -->
Pasa el examen: es real, es par porque solo aparece omega al cuadrado, y nunca es negativa. Y miremos dos puntos. En frecuencia cero vale uno. En omega igual a dos, cuatro entre ocho: un medio. La curva cae a la mitad justo en omega igual a alfa. Y eso le da a alfa un segundo significado.

- «Pasa el examen» → `examen`: aparecen las tres casillas del examen del episodio anterior (real, par, nunca negativa)
- «es real» → `real`: tilde verde en la primera
- «es par» → `par`: tilde verde y la curva se refleja sobre el eje vertical
- «solo aparece omega al cuadrado» → `omega2`: se resalta «ω²» en la fórmula
- «nunca es negativa» → `nuncaneg`: tilde verde en la tercera
- «dos puntos» → `puntos`: aparecen dos marcadores vacíos sobre la curva
- «En frecuencia cero vale uno» → `cero`: el primero se fija en (0, 1)
- «En omega igual a dos» → `en2`: el eje marca «ω = 2»
- «cuatro entre ocho» → `ocho`: aparece «4/8» en ω = 2
- «un medio» → `medio`: el segundo punto se fija en (2, ½)
- «cae a la mitad» → `mitad`: una línea horizontal a media altura
- «omega igual a alfa» → `enalfa`: marca «α» sobre el eje, justo bajo el punto
- «un segundo significado» → `segundo`: «α = ¿?» en ámbar

---

# Escena 08 — MemoriaYAncho

**Capítulo YouTube:** Olvidar rápido, espectro ancho

## Narración

<!-- b1 -->
En el capítulo anterior, dos lambda era la velocidad a la que el interruptor olvida, y prometimos que reaparecería disfrazada de ancho de banda. Aquí está: alfa, que es dos lambda, también es la frecuencia donde el espectro cae a la mitad. Movamos alfa y veamos las dos curvas a la vez.

- «dos lambda» → `dosl`: vuelve el interruptor del capítulo 10 con «2λ» encima
- «la velocidad a la que el interruptor olvida» → `olvida`: su autocorrelación decae junto al interruptor
- «prometimos» → `prometimos`: aparece la etiqueta «promesa del capítulo 10»
- «disfrazada de ancho de banda» → `disfraz`: el «2λ» se pone un disfraz con «¿ancho de banda?»
- «Aquí está» → `aqui`: aparece «α = 2λ»
- «la frecuencia donde el espectro cae a la mitad» → `mitad`: el espectro con su punto a media altura marcado
- «Movamos alfa» → `mover`: aparece el deslizador de α
- «las dos curvas a la vez» → `dos`: par autocorrelación ↔ espectro, lado a lado

<!-- b2 -->
Con alfa igual a ocho, la señal salta muy a menudo. A medio segundo, la autocorrelación ya vale cero coma cero dos: casi lo ha olvidado todo. Y el espectro vale cero coma dos cinco en el origen y cae a la mitad en ocho: bajo y ancho. Con alfa igual a cero coma cinco, al revés: la señal recuerda mucho, y el espectro es alto y estrecho.

- «Con alfa igual a ocho» → `a8`: el deslizador sube a α = 8 y la señal salta más
- «salta muy a menudo» → `salta`: marcas de saltos se acumulan sobre la onda
- «A medio segundo» → `medio`: una línea vertical en τ = 0,5 sobre la autocorrelación
- «cero coma cero dos» → `r002`: «R(0,5) = e⁻⁴ ≈ 0,02»
- «casi lo ha olvidado todo» → `olvido`: la curva queda pegada al cero
- «cero coma dos cinco» → `s025`: «S(0) = 2/8 = 0,25»
- «cae a la mitad en ocho» → `mitad8`: el punto de media altura se marca en ω = 8
- «bajo y ancho» → `bajoancho`: el rótulo «bajo y ancho» junto al espectro
- «Con alfa igual a cero coma cinco» → `a05`: el deslizador baja a α = 0,5
- «recuerda mucho» → `recuerda`: la autocorrelación se estira, lenta
- «alto y estrecho» → `altoestrecho`: el espectro se eleva y se estrecha, con «S(0) = 4»

---

# Escena 09 — LaDualidad

**Capítulo YouTube:** Memoria corta, espectro ancho

## Narración

<!-- b1 -->
Fíjate en que el área no cambia: la potencia sigue siendo uno. Lo que el espectro pierde en altura lo gana en anchura. La regla es esta: memoria corta, espectro ancho; memoria larga, espectro estrecho. Es la dualidad de Fourier de Señales y Sistemas, la del pulso estrecho con espectro ancho, aplicada a la memoria de un proceso.

- «el área no cambia» → `area`: el área bajo el espectro se sombrea y el deslizador se mueve sin que cambie, con «potencia = 1»
- «la potencia sigue siendo uno» → `potuno`: el rótulo «potencia = 1» se fija sobre el área
- «pierde en altura» → `altura`: una flecha baja sobre la punta del espectro
- «lo gana en anchura» → `anchura`: flechas se abren hacia los lados
- «memoria corta, espectro ancho» → `corta`: rótulo «memoria corta ↔ espectro ancho»
- «memoria larga, espectro estrecho» → `larga`: rótulo «memoria larga ↔ espectro estrecho»
- «la dualidad de Fourier» → `dual`: aparece «dualidad» con una flecha doble entre tiempo y frecuencia
- «el pulso estrecho con espectro ancho» → `pulso`: un pulso estrecho y, a su lado, su espectro ancho
- «la memoria de un proceso» → `memproc`: el pulso se sustituye por la autocorrelación del proceso

<!-- b2 -->
Llevémoslo al extremo. Una sinusoide con fase al azar, del capítulo anterior, tiene como autocorrelación un coseno que no decae nunca: recuerda para siempre. Y su espectro son solo dos rayas, dos impulsos en más y menos su frecuencia. Toda la potencia en dos puntos. Se llama espectro de líneas.

- «Llevémoslo al extremo» → `extremo`: el deslizador de α baja hasta casi cero
- «Una sinusoide con fase al azar» → `sinus`: varias sinusoides con fases distintas, apiladas
- «del capítulo anterior» → `cap10`: la etiqueta «capítulo 10» junto a las sinusoides
- «un coseno que no decae nunca» → `coseno`: la autocorrelación se dibuja como un coseno que no se apaga
- «recuerda para siempre» → `siempre`: una flecha larga hacia la derecha «para siempre»
- «dos rayas» → `rayas`: dos flechas verticales sobre el eje de frecuencias
- «dos impulsos en más y menos su frecuencia» → `impulsos`: las flechas se rotulan «+ω₀» y «−ω₀»
- «Toda la potencia en dos puntos» → `dospuntos`: a cada flecha, «½» y «½»
- «espectro de líneas» → `lineas`: rótulo «espectro de líneas»

---

# Escena 10 — LaEncuestaDeLaMemoriaCero

**Capítulo YouTube:** ¿Qué espectro tiene la memoria cero?

## Narración

<!-- b1 -->
Memoria infinita, dos rayas. ¿Y un proceso que no recuerda absolutamente nada, en el que cada instante no tiene relación con ningún otro? ¿Su espectro sería una raya en cero, no tendría nada, o sería plano? Piénsalo.

- «Memoria infinita, dos rayas» → `resumen`: las dos rayas quedan a un lado, con «memoria infinita»
- «un proceso que no recuerda absolutamente nada» → `nada`: una traza de valores sueltos, sin relación entre sí
- «cada instante» → `instante`: cada valor de la traza se enmarca en su propia casilla
- «ningún otro» → `ninguno`: unas líneas que conectan instantes aparecen y se tachan
- «una raya en cero» → `opa`: primera casilla: una flecha en el origen
- «no tendría nada» → `opb`: segunda casilla: un eje vacío
- «sería plano» → `opc`: tercera casilla: una línea horizontal
- «Piénsalo» → `piensa`: las tres casillas quedan quietas, con un «?» que parpadea

---

# Escena 11 — LaMonedaSinMemoria

**Capítulo YouTube:** La moneda: potencia y vecinas

## Narración

<!-- b1 -->
Vuelve a la moneda: en cada instante, más uno o menos uno, cada tirada independiente. Su potencia es fácil: más uno o menos uno, al cuadrado, dan siempre uno. ¿Y cuánto se parecen dos tiradas vecinas? Hay cuatro combinaciones igual de probables. Si coinciden, el producto es más uno; si no, menos uno. Dos y dos: el promedio es cero.

- «Vuelve a la moneda» → `moneda`: vuelve el ícono de la moneda
- «más uno o menos uno» → `pm`: la tira «+1, −1, −1, +1, −1…» se dibuja
- «cada tirada independiente» → `indep`: cada tirada en su casilla, sin conexiones
- «Su potencia es fácil» → `pot`: aparece «potencia»
- «al cuadrado, dan siempre uno» → `cuad`: «x² = 1 → E[x²] = 1»
- «dos tiradas vecinas» → `vecinas`: dos casillas adyacentes se resaltan
- «cuatro combinaciones» → `cuatro`: aparece la tabla (+,+), (+,−), (−,+), (−,−)
- «Si coinciden» → `coinciden`: (+,+) y (−,−) se marcan con «→ +1»
- «si no, menos uno» → `difieren`: (+,−) y (−,+) se marcan con «→ −1»
- «el promedio es cero» → `cero`: «promedio = 0» en ámbar

<!-- b2 -->
Y lo mismo a cualquier distancia. Así que la autocovarianza es una única barra de altura uno en el origen, y cero en todo lo demás. Eso se escribe delta de eme: vale uno cuando eme es cero y cero en otro caso. Su transformada tiene un solo término, uno por e elevado a cero: uno, para todas las frecuencias.

- «a cualquier distancia» → `dist`: se resaltan pares de tiradas a separaciones 2, 3 y 4
- «la autocovarianza» → `cov`: aparece «C_xx[m]»
- «una única barra de altura uno en el origen» → `barra`: un gráfico de palitos con una sola barra de altura 1 en m = 0
- «cero en todo lo demás» → `resto`: los demás palitos quedan en cero
- «delta de eme» → `delta`: aparece «δ[m]»
- «vale uno cuando eme es cero» → `vale1`: «1 en m = 0»
- «cero en otro caso» → `vale0`: «0 fuera»
- «Su transformada» → `transf`: una flecha lleva la barra a un eje de frecuencias
- «un solo término» → `solo`: aparece la suma con un único término
- «uno por e elevado a cero» → `unoxe`: «1 · e⁰ = 1»
- «para todas las frecuencias» → `todas`: una línea horizontal de −π a π a altura 1

---

# Escena 12 — ElEspectroPlano

**Capítulo YouTube:** Ruido blanco y ruido coloreado

## Narración

<!-- b1 -->
El espectro es completamente plano: la misma potencia en todas las frecuencias. Esa era la respuesta: memoria cero, espectro plano. Y si cada muestra tuviera varianza ka en lugar de uno, el espectro sería plano a altura ka. Una barra de altura ka en el tiempo, una línea de altura ka en frecuencia.

- «completamente plano» → `plano`: la línea horizontal se resalta en ámbar
- «la misma potencia en todas las frecuencias» → `misma`: barritas iguales de potencia a lo largo del eje
- «Esa era la respuesta» → `respuesta`: vuelven las tres casillas de la encuesta y se marca la tercera con un tilde verde
- «memoria cero, espectro plano» → `regla`: el rótulo «memoria cero ↔ espectro plano»
- «cada muestra» → `muestra`: se marca una muestra de la moneda con su varianza
- «varianza ka» → `ka`: aparece «varianza K»
- «plano a altura ka» → `alturaka`: la línea sube a «K»
- «Una barra de altura ka en el tiempo» → `barrak`: la barra de la autocovarianza crece a «K»
- «una línea de altura ka en frecuencia» → `lineak`: aparece «C_xx[m] = K δ[m] ⟷ D_xx = K»

<!-- b2 -->
A este proceso se lo llama ruido blanco, por analogía con la luz: la luz blanca es una mezcla de todos los colores con la misma intensidad. Un proceso cuyo espectro tiene forma, con más potencia en unas frecuencias que en otras, se llama coloreado. La onda telegráfica y el proceso de rho igual a cero coma cuatro son ruidos coloreados.

- «ruido blanco» → `blanco`: el rótulo «ruido blanco» sobre la línea plana
- «la luz blanca» → `luz`: un prisma abre un rayo blanco
- «todos los colores con la misma intensidad» → `colores`: sale un arcoíris con barras de altura igual
- «Un proceso cuyo espectro» → `procesoesp`: aparece un espectro genérico con un signo de pregunta
- «tiene forma» → `forma`: una curva con joroba se dibuja al lado
- «más potencia en unas frecuencias que en otras» → `unasyotras`: una zona alta y una baja se marcan sobre la curva
- «coloreado» → `coloreado`: el rótulo «coloreado» sobre la joroba
- «La onda telegráfica» → `tele`: aparece su espectro 4/(4 + ω²)
- «rho igual a cero coma cuatro» → `rho04`: aparece el espectro 1 + 0,8 cos Ω de las tres barras
- «ruidos coloreados» → `rotulo`: los dos espectros quedan bajo el rótulo «coloreados»

<!-- b3 -->
El blanco es el ingrediente básico de todo el curso: con él fabricamos el proceso del episodio anterior, y con él fabricaremos cualquier otro color. Pero tiene dos sorpresas guardadas, y una de ellas es que, en cierto sentido, no existe.

- «el ingrediente básico» → `ingred`: la línea plana se convierte en un bote de pintura blanca
- «el proceso del episodio anterior» → `anterior`: las tres barras de ρ = 0,4 con su filtro
- «cualquier otro color» → `otro`: el bote pinta distintas curvas de colores
- «dos sorpresas» → `sorpresas`: aparecen dos cajas con «?»
- «una de ellas» → `unadeellas`: la segunda caja pulsa
- «no existe» → `noexiste`: la segunda caja se vuelve tenue y una diagonal la tacha

---

# Escena 13 — LaPrimeraSorpresa

**Capítulo YouTube:** Primera sorpresa: el blanco tiene media cero

## Narración

<!-- b1 -->
Primera sorpresa. ¿Puede un ruido de espectro plano tener media cinco? Sí, no, ¿depende? Piénsalo con lo que sabemos de la media: aparece en el espectro como un impulso en el origen.

- «Primera sorpresa» → `primera`: la primera caja «?» se abre con el título «primera sorpresa»
- «un ruido de espectro plano» → `plano`: la línea plana de altura K
- «media cinco» → `cinco`: aparece «μ = 5»
- «Sí, no, ¿depende?» → `opciones`: tres casillas, «sí», «no» y «depende»
- «lo que sabemos de la media» → `media`: aparece «media = impulso»
- «un impulso en el origen» → `impulso`: una flecha vertical en ω = 0

<!-- b2 -->
La respuesta es no. Si el espectro es plano a altura ka y la media fuera cinco, la densidad de las fluctuaciones sería el espectro menos el impulso de la media: ka menos dos pi por veinticinco en el origen. Un impulso que apunta hacia abajo: una densidad negativa en frecuencia cero. Imposible. Así que un espectro plano obliga a que la media sea cero.

- «La respuesta es no» → `no`: se marca la casilla «no» con un tilde verde
- «plano a altura ka» → `ka`: la línea plana se rotula «K»
- «la densidad de las fluctuaciones sería» → `dens`: aparece «D_xx =»
- «el espectro menos el impulso de la media» → `menos`: se construye «S_xx − 2π μ² δ(ω)»
- «ka menos dos pi por veinticinco» → `kmenos`: queda «K − 2π · 25 · δ(ω)»
- «en el origen» → `origen`: la flecha roja se ubica en ω = 0
- «apunta hacia abajo» → `abajo`: una flecha roja hacia abajo en ω = 0, bajo la línea
- «una densidad negativa» → `neg`: el sello «densidad negativa: imposible»
- «Imposible» → `imposible`: una cruz roja sobre la flecha
- «la media sea cero» → `mu0`: aparece «μ = 0» en verde

---

# Escena 14 — LaSegundaSorpresa

**Capítulo YouTube:** Segunda sorpresa: potencia infinita

## Narración

<!-- b1 -->
Segunda sorpresa, en tiempo continuo. Allí la frecuencia no se acaba en pi: llega hasta el infinito. Un espectro plano de altura uno hasta mil radianes por segundo, contando las negativas, tiene área dos mil. Hasta un millón, dos millones. Hasta el infinito, área infinita. Es decir, potencia infinita. El ruido blanco continuo no puede existir.

- «Segunda sorpresa» → `segunda`: la segunda caja «?» se abre con el título «segunda sorpresa»
- «en tiempo continuo» → `continuo`: el rótulo «tiempo continuo»
- «no se acaba en pi» → `pi`: el eje discreto termina en ±π y el continuo sigue más allá
- «hasta el infinito» → `inf`: flechas a los dos lados del eje
- «altura uno» → `alt1`: una línea plana de altura 1
- «hasta mil radianes por segundo» → `mil`: un rectángulo entre −1.000 y 1.000
- «área dos mil» → `a2000`: «→ 2.000»
- «Hasta un millón» → `millon`: el rectángulo se ensancha y aparece «→ 2.000.000»
- «dos millones» → `dosmill`: la cuenta «2.000.000» se marca en ámbar
- «área infinita» → `areainf`: «→ ∞»
- «potencia infinita» → `potinf`: «potencia = ∞» en rojo
- «no puede existir» → `noexiste`: el sello «no existe» sobre la línea plana

<!-- b2 -->
Y aun así lo usamos, igual que usamos el impulso de Dirac, que tampoco existe: es una idealización cómoda que da buenos resultados si se interpreta bien. El ruido térmico de una resistencia es plano hasta frecuencias de billones de hercios. Cualquier aparato real corta mucho antes, y en lo que deja pasar, es indistinguible del blanco.

- «aun así lo usamos» → `usamos`: el sello se desvanece y la línea plana sigue en pantalla
- «el impulso de Dirac» → `dirac`: al lado, un pico infinitamente fino
- «una idealización cómoda» → `ideal`: el rótulo «idealización» sobre la línea y el pico
- «buenos resultados» → `buenos`: un tilde verde junto a «idealización»
- «El ruido térmico de una resistencia» → `termico`: entra el ícono de una resistencia
- «billones de hercios» → `billones`: el espectro plano se extiende muy lejos, con «billones de Hz»
- «Cualquier aparato real» → `aparato`: entra una caja de aparato
- «corta mucho antes» → `corta`: una ventana rectangular recorta el espectro antes de llegar al borde
- «indistinguible del blanco» → `indist`: dentro de la ventana, el espectro real coincide con la línea plana; aparece un tilde verde

---

# Escena 15 — Cierre

**Capítulo YouTube:** Lo que viene: un espectro a partir de datos

## Narración

<!-- b1 -->
En tiempo discreto, en cambio, el blanco existe de verdad: la moneda. Resumen del episodio: sin memoria, espectro plano, media cero. Hasta aquí hemos trabajado con autocorrelaciones conocidas. Pero en la vida real nadie te da la autocorrelación. Te dan un archivo con datos. En el próximo episodio: un espectro a partir de datos.

- «el blanco existe de verdad» → `existe`: la moneda vuelve con un tilde verde
- «Resumen del episodio» → `resumen`: entra el rótulo «resumen»
- «sin memoria» → `sinmem`: aparece «sin memoria» con la barra única de autocovarianza
- «espectro plano» → `plano`: junto a ella, la línea plana
- «media cero» → `mu0`: «μ = 0»
- «autocorrelaciones conocidas» → `conocidas`: una fórmula «R_xx(τ) = …» dada, como en todas las cuentas del capítulo
- «nadie te da la autocorrelación» → `nadie`: «R_xx = ?» con una cruz
- «un archivo con datos» → `archivo`: entra un ícono de documento lleno de números
- «un espectro a partir de datos» → `titulo_e4`: entra el título del siguiente episodio
