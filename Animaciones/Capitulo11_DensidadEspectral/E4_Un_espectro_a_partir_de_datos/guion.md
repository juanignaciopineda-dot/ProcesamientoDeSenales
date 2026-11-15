# Episodio 4 — Un espectro a partir de datos

Capítulo 11 (Densidad espectral de potencia), episodio 4 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 16 a 19), más un gancho y un cierre nuevos.

**Estado:** `guion.md` escrito (11 escenas atómicas, con momentos), `ritmo.py` corrido (paso 11): 0 huecos de más de 4 s. Texto ⭐ aprobado por el usuario. 11 escenas animadas (`s01`–`s11`); borrador 480p15 de 8:08 con 0 avisos y hojas de contacto revisadas. Falta: visto bueno del usuario al mp4 (paso 15) y render final.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Grabas diez veces más para afinar tu espectro, y el temblor no baja ni un poco. No es un fallo de tu aparato: es una trampa del método. Y tiene arreglo.»
- ⭐ Escena 11 (cierre): resumen y anuncia E5 por su título, «Cortar sin romper».

Nota para el episodio anterior: el cierre de E3 (escena 15 del guion base, bloque final) ya deja dicho que «en la vida real nadie te da la autocorrelación, te dan un archivo con datos». Este episodio arranca de ahí.

Reparto de las escenas del guion base: 03 → escena 16 (bloques 1 y 2); 04 → escena 16 (3 a 5); 05 → escena 17 (1 a 3); 06 → escena 17 (4 y 5); 07 → escena 18 (1 y 2); 08 → escena 18 (3 a 5); 09 → escena 19 (1 y 2); 10 → escena 19 (3 a 5).
Solo se partieron bloques enteros en escenas atómicas: el texto del guion base no cambia.

Bucle que se paga aquí: el rectángulo que se desliza sobre otro (escena 08 del E2) es el triángulo de la ventana (escena 04).

---

# Escena 01 — Gancho

**Capítulo YouTube:** Grabar más no basta

## Narración

<!-- b1 -->
Grabas diez veces más para afinar tu espectro, y el temblor no baja ni un poco. No es un fallo de tu aparato: es una trampa del método. Y tiene arreglo.

- «Grabas diez veces más» → `mas`: la traza de ruido se alarga diez veces hacia la derecha
- «afinar tu espectro» → `espectro`: debajo aparece un periodograma: un bosque de picos magentas sobre la línea plana verdadera
- «el temblor no baja ni un poco» → `temblor`: el bosque se vuelve más denso pero igual de alto; una flecha roja marca la altura que no baja
- «No es un fallo de tu aparato» → `aparato`: una cruz roja sobre un ícono de aparato de medida y, al lado, el rótulo «método»
- «una trampa del método» → `trampa`: una cruz roja tacha el periodograma
- «tiene arreglo» → `arreglo`: el bosque se aplana hasta una curva suave en ámbar

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Un espectro a partir de datos

## Narración

<!-- b1 -->
Un espectro a partir de datos.

- «Un espectro» → `t1`: «Un espectro» entra con rebote
- «a partir de datos» → `t2`: «a partir de datos» entra debajo, con la etiqueta «Capítulo 11 · Densidad espectral de potencia»

---

# Escena 03 — RecortarYMedir

**Capítulo YouTube:** El periodograma

**Objetivo:** el camino del laboratorio: recortar la realización a una ventana, recordar Parseval y definir el periodograma.

## Narración

<!-- b1 -->
Tienes una grabación de ruido de diez segundos y quieres su espectro. La idea del laboratorio es la del principio, con una corrección: si la realización entera no tiene transformada, recortemos un trozo. Una ventana de menos te a te. Lo que queda dentro empieza y termina, tiene energía finita, y su transformada existe.

- «una grabación de ruido de diez segundos» → `grabacion`: una grabación larga de la telegráfica avanza, con la marca «10 s»
- «quieres su espectro» → `espectro`: un eje de frecuencias vacío con un signo de pregunta
- «La idea del laboratorio» → `idea`: aparece un ícono de laboratorio con una flecha hacia la caja «Fourier»
- «con una corrección» → `correccion`: sobre la flecha se dibuja un signo «+» ámbar
- «si la realización entera no tiene transformada» → `entera`: una flecha lleva la grabación a una caja «Fourier» y una cruz roja la tacha
- «recortemos un trozo» → `recorte`: una tijera o un marco recorta un tramo y el resto se apaga
- «Una ventana de menos te a te» → `ventana`: el marco se rotula «−T» y «T» en sus bordes
- «empieza y termina» → `termina`: el trozo queda solo, con el principio y el final marcados
- «tiene energía finita» → `energia`: el área cuadrada bajo el trozo se sombrea y entra la etiqueta «energía finita»
- «su transformada existe» → `existe`: la cruz roja se cambia por una marca verde sobre la caja «Fourier»

<!-- b2 -->
De Señales y Sistemas, el teorema de Parseval: la energía de una señal es el área bajo el módulo al cuadrado de su transformada, dividida entre dos pi. Así que ese módulo al cuadrado reparte la energía del trozo por frecuencias. Si lo dividimos entre la duración, dos te, reparte la potencia. Eso se llama periodograma.

- «el teorema de Parseval» → `parseval`: entra el nombre «Parseval» y el signo igual de la fórmula «energía = …»
- «la energía de una señal» → `e_tiempo`: aparece la pieza «energía»
- «el área bajo el módulo al cuadrado de su transformada» → `area`: entra la pieza «∫ |X_T(jω)|² dω» y se sombrea el área bajo la curva
- «dividida entre dos pi» → `dospi`: entra el «1/2π» delante
- «Así que ese módulo al cuadrado» → `modulo`: se resalta la curva |X_T|² dentro de la fórmula
- «reparte la energía del trozo por frecuencias» → `reparte`: la curva |X_T|² se divide en franjas de colores por frecuencia
- «dividimos entre la duración» → `divide`: entra «/ 2T» bajo la curva
- «reparte la potencia» → `potencia`: la etiqueta pasa de «energía» a «potencia»
- «periodograma» → `periodograma`: la palabra «periodograma = |X_T(jω)|² / 2T» entra con rebote en ámbar

---

# Escena 04 — ElTrianguloVuelve

**Capítulo YouTube:** Einstein, Wiener y Khinchin

**Objetivo:** comprobar el área con la telegráfica, tomar esperanza y alargar la ventana (Einstein-Wiener-Khinchin), y pagar el bucle del rectángulo deslizante: el solapamiento de la ventana con su copia es el triángulo del E2.

## Narración

<!-- b1 -->
Comprobémoslo con la telegráfica: en diez segundos, energía diez; entre diez segundos, potencia uno. El área del periodograma dividida entre dos pi da uno. Ahora tomamos esperanza, para no depender de la grabación concreta, y alargamos la ventana hasta el infinito. Sale la densidad espectral de siempre. Es el teorema de Einstein, Wiener y Khinchin.

- «en diez segundos, energía diez» → `e10`: sobre la telegráfica entra «energía 10 s → 10»
- «entre diez segundos, potencia uno» → `p1`: a su lado entra «10 / 10 s = 1», con una marca verde
- «El área del periodograma» → `area1`: el periodograma de la telegráfica se dibuja y su área se sombrea
- «dividida entre dos pi da uno» → `da_uno`: la etiqueta «1/2π · área = 1» con una marca verde
- «tomamos esperanza» → `esperanza`: aparece «E[ ]» rodeando el periodograma y mil curvas tenues se funden en una
- «alargamos la ventana hasta el infinito» → `limite`: la ventana «−T a T» se ensancha hasta salirse de la pantalla y entra «lím T→∞»
- «Sale la densidad espectral de siempre» → `densidad`: la curva 4/(4 + ω²) en ámbar, la del primer episodio, queda en el centro
- «el teorema de Einstein, Wiener y Khinchin» → `ewk`: la fórmula «S_xx(jω) = lím (1/2T) E[|X_T|²]» se arma por piezas

<!-- b2 -->
El camino del laboratorio y el de la autocorrelación llegan al mismo sitio. Pero en el laboratorio la ventana nunca es infinita, así que lo que importa es qué medimos antes del límite. Y aquí vuelve el dibujo que prometimos. La autocorrelación compara la señal con su copia desplazada tau. Dentro de la ventana, eso solo se puede hacer donde la ventana y su copia se solapan.

- «El camino del laboratorio» → `lab`: dos flechas de colores: «laboratorio» desde la grabación y «autocorrelación» desde R_xx
- «llegan al mismo sitio» → `mismo`: las dos flechas terminan en la misma curva ámbar
- «la ventana nunca es infinita» → `finita`: la ventana «−T a T» vuelve a su tamaño finito y se marca en rojo el «límite» como inalcanzable
- «qué medimos antes del límite» → `antes`: un signo de pregunta rojo sobre la curva
- «vuelve el dibujo que prometimos» → `vuelve`: destello del rectángulo deslizante del E2
- «compara la señal con su copia desplazada tau» → `copia`: debajo de la ventana aparece otra copia idéntica, desplazada tau, con la etiqueta «x(σ − τ)»
- «Dentro de la ventana» → `dentro`: se resalta el marco de la ventana «−T a T»
- «donde la ventana y su copia se solapan» → `solapan`: la zona común de las dos ventanas se sombrea en ámbar

<!-- b3 -->
Y el solapamiento de dos rectángulos que se deslizan es un triángulo: el de hace dos episodios. Así que con una ventana finita no medimos la autocorrelación, sino la autocorrelación multiplicada por un triángulo. El paso completo está en el apunte en profundidad. Lo importante es qué le hace ese triángulo al espectro.

- «dos rectángulos que se deslizan» → `rects`: los dos rectángulos, idénticos a los de la escena 08 del E2, se deslizan uno sobre otro
- «es un triángulo» → `triangulo`: el área común se dibuja punto a punto y sale el triángulo
- «el de hace dos episodios» → `dos_eps`: etiqueta «E2 · escena 08», con una marca verde: bucle pagado
- «con una ventana finita» → `finita2`: la ventana «−T a T» se marca como finita
- «no medimos la autocorrelación» → `nor`: «R_xx(τ)» con un tachón suave
- «multiplicada por un triángulo» → `portri`: entra «R_xx(τ) · triángulo(τ)»
- «El paso completo está en el apunte en profundidad» → `apunte`: aparece el icono del documento con «apunte en profundidad»
- «Lo importante es» → `importante`: el signo de pregunta del espectro se resalta
- «qué le hace ese triángulo al espectro» → `alespectro`: una flecha hacia un eje de frecuencias con un signo de pregunta

---

# Escena 05 — ElDesenfoque

**Capítulo YouTube:** El triángulo desenfoca el espectro

**Objetivo:** cuentas del triángulo con una ventana de 10 s; multiplicar en el tiempo es convolucionar con una sinc al cuadrado en frecuencia, explicado como desenfoque.

## Narración

<!-- b1 -->
Pongamos números. Con una ventana de diez segundos, el triángulo vale uno en tau igual a cero, un medio en cinco segundos y cero en diez. La autocorrelación de la telegráfica ya se ha apagado a los dos segundos, y ahí el triángulo casi no ha bajado. Con una ventana larga, el triángulo apenas estropea nada.

- «Con una ventana de diez segundos» → `diez`: el triángulo de una ventana de 10 s sobre un eje de τ
- «vale uno en tau igual a cero» → `tau0`: un punto en la cima con «τ = 0 → 1»
- «un medio en cinco segundos» → `tau5`: un punto a media bajada con «τ = 5 s → ½»
- «cero en diez» → `tau10`: un punto en el eje con «τ = 10 s → 0»
- «La autocorrelación de la telegráfica» → `autocorr`: se dibuja encima e^(−2|τ|), la curva que decae
- «se ha apagado a los dos segundos» → `apaga`: una marca vertical en 2 s; la curva ya está pegada al eje
- «el triángulo casi no ha bajado» → `casi`: en esa marca el triángulo vale 0,8, con una marca verde
- «Con una ventana larga» → `larga1`: la ventana de 10 s se alarga y el triángulo se ensancha
- «apenas estropea nada» → `nada`: sello «ventana larga: casi no estropea»

<!-- b2 -->
Pero ¿qué hace en frecuencia? Multiplicar en el tiempo es convolucionar en frecuencia. Y convolucionar con una campana estrecha es desenfocar: cada punto del espectro se reemplaza por un promedio ponderado de sus vecinos, como una foto movida. Aquí la campana es la transformada del triángulo, una sinc al cuadrado.

- «qué hace en frecuencia» → `freq`: el eje de frecuencias con la curva verdadera vuelve a la pantalla
- «Multiplicar en el tiempo» → `mult`: entra «producto en el tiempo»
- «convolucionar en frecuencia» → `conv`: entra «⟷ convolución en frecuencia»
- «con una campana estrecha» → `campana`: aparece una campana estrecha
- «desenfocar» → `desenfocar`: la palabra «desenfocar» entra con rebote
- «un promedio ponderado de sus vecinos» → `vecinos`: la sinc al cuadrado se desliza y cada punto de la curva se reemplaza por el promedio de su entorno
- «como una foto movida» → `foto`: icono de foto que pasa de nítida a movida a la vez que la curva se suaviza
- «Aquí la campana» → `aqui`: la campana estrecha se convierte en la sinc al cuadrado
- «la transformada del triángulo» → `trans`: una flecha desde el triángulo hasta la sinc al cuadrado
- «una sinc al cuadrado» → `sinc2`: se dibuja la sinc al cuadrado con la etiqueta «transformada del triángulo»

<!-- b3 -->
Lo que medimos, en promedio, es el espectro verdadero desenfocado. Y el desenfoque depende de la ventana: cuanto más larga, más estrecha es la sinc al cuadrado y más nítido el resultado. Cuando la ventana crece sin límite, el desenfoque desaparece, y eso es exactamente lo que dice el teorema.

- «el espectro verdadero desenfocado» → `medimos`: «medido = verdadero ∗ sinc²», con la curva desenfocada junto a la verdadera
- «depende de la ventana» → `depende`: la ventana del tiempo se resalta
- «cuanto más larga» → `larga`: la ventana en el tiempo se alarga
- «más estrecha es la sinc al cuadrado» → `estrecha`: la sinc al cuadrado se afina a la vez
- «más nítido el resultado» → `nitido`: la curva medida se acerca a la verdadera
- «crece sin límite» → `sinlimite`: la sinc al cuadrado se vuelve una raya
- «el desenfoque desaparece» → `desaparece`: medida y verdadera coinciden, con marca verde
- «lo que dice el teorema» → `teorema`: vuelve «lím T→∞» de la escena anterior

---

# Escena 06 — ResolucionDeLosTonos

**Capítulo YouTube:** Cuánto hay que grabar para separar dos tonos

**Objetivo:** la resolución: con una ventana de L segundos no se separan tonos más cercanos que 1/L hercios; los tonos de 50 y 50,5 Hz con 1 s y con 4 s.

## Narración

<!-- b1 -->
El desenfoque tiene una consecuencia muy concreta. Dos tonos, uno de cincuenta hercios y otro de cincuenta y medio. Con un segundo de grabación, cada tono se convierte en una campana de un hercio de ancho, y las dos se funden en un solo bulto. Con cuatro segundos, las campanas miden un cuarto de hercio, y se ven dos picos.

- «una consecuencia muy concreta» → `conse`: entra el rótulo «consecuencia» sobre el eje de frecuencias
- «Dos tonos» → `tonos`: dos rayas finas sobre un eje de frecuencias
- «cincuenta hercios» → `r50`: la primera raya con la etiqueta «50 Hz»
- «cincuenta y medio» → `r505`: la segunda raya con la etiqueta «50,5 Hz»
- «Con un segundo de grabación» → `un_s`: entra la marca «1 s» y una ventana corta en el tiempo
- «una campana de un hercio de ancho» → `campanas`: cada raya se ensancha a una campana con una llave «1 Hz»
- «se funden en un solo bulto» → `bulto`: las dos campanas se suman en un solo bulto
- «Con cuatro segundos» → `cuatro_s`: la marca pasa a «4 s» y la ventana se alarga
- «un cuarto de hercio» → `cuarto`: las campanas se afinan con la llave «0,25 Hz»
- «se ven dos picos» → `dos_picos`: el bulto se abre en dos picos, con marca verde

<!-- b2 -->
La regla: con una ventana de ele segundos, no se distinguen tonos más cercanos que uno sobre ele hercios. Para separar cincuenta y cincuenta y medio, hacen falta al menos dos segundos. La resolución la da el tiempo de grabación. Pero hay un problema peor, que alargar la ventana no arregla.

- «con una ventana de ele segundos» → `ele`: entra «ventana de L segundos»
- «no se distinguen tonos más cercanos» → `nodist`: dos rayas pegadas se funden en un bulto
- «uno sobre ele hercios» → `unosobre`: entra «resolución ≈ 1 / L»
- «cincuenta y cincuenta y medio» → `separar`: los dos tonos vuelven con su separación de 0,5 Hz marcada
- «al menos dos segundos» → `dos_s`: «1 / 0,5 = 2 s» en ámbar
- «La resolución la da el tiempo de grabación» → `tiempo`: «resolución = tiempo de grabación», con un reloj
- «un problema peor» → `peor`: aparece una sombra roja desde la derecha
- «que alargar la ventana no arregla» → `noarregla`: la ventana larga con una cruz roja encima

---

# Escena 07 — BosqueDePicos

**Capítulo YouTube:** Un periodograma tiembla tanto como vale

**Objetivo:** mostrar que un periodograma crudo tiembla tanto como vale (encuesta con tres opciones) y que grabar más no lo arregla: afina los picos pero no los baja.

## Narración

<!-- b1 -->
Calcula el periodograma de un segundo de la moneda. El espectro verdadero es plano, a altura uno. Lo que sale es un bosque de picos y valles: algunos llegan a tres o cuatro, otros casi a cero, y ninguno significa nada. Ahora la pregunta: si grabas diez veces más, ¿se aplana, los picos se hacen más finos pero igual de altos, o no cambia nada?

- «el periodograma de un segundo de la moneda» → `moneda`: la moneda ±1 y su tira de más uno y menos uno, sobre un eje con «1 s»
- «El espectro verdadero es plano» → `plano`: una línea plana a altura uno, en ámbar
- «a altura uno» → `uno`: una marca «1» sobre la línea plana
- «un bosque de picos y valles» → `bosque`: el periodograma en magenta, muy irregular, se dibuja alrededor de la línea
- «tres o cuatro» → `alto`: se marcan los picos que llegan a 3 y 4
- «casi a cero» → `cero`: se marcan los valles junto al eje
- «ninguno significa nada» → `nada`: sello «ni un pico significa algo»
- «si grabas diez veces más» → `diez`: la marca pasa de «1 s» a «10 s»
- «se aplana» → `opa`: opción «A) se aplana»
- «los picos se hacen más finos pero igual de altos» → `opb`: opción «B) más finos, igual de altos»
- «no cambia nada» → `opc`: opción «C) no cambia nada»

<!-- b2 -->
Los picos se hacen más finos, pero igual de altos. El bosque se vuelve más denso, pero no más bajo. En cada frecuencia, el periodograma sale en promedio uno, que es lo correcto, pero tiembla alrededor de ese uno con una desviación típica de uno: tanto como vale.

- «Los picos se hacen más finos» → `finos`: se tachan las opciones A y C y el periodograma de 10 s aparece, con picos más finos y numerosos
- «igual de altos» → `altos`: una línea horizontal a altura 3 cruza los dos bosques
- «más denso, pero no más bajo» → `denso`: dos llaves: «más denso» en verde, «no más bajo» en rojo
- «En cada frecuencia» → `cadafrec`: una raya vertical se fija en una frecuencia
- «sale en promedio uno» → `media1`: «media 1», con una marca verde
- «pero tiembla alrededor de ese uno» → `alrededor`: flechas rojas suben y bajan alrededor del 1
- «una desviación típica de uno» → `desv1`: la banda alrededor del 1 con «desviación 1»
- «tanto como vale» → `tanto`: «tiembla tanto como vale» en rojo

---

# Escena 08 — UnaSolaMuestra

**Capítulo YouTube:** Una sola muestra del ensemble

**Objetivo:** por qué grabar más no ayuda (cada frecuencia sigue siendo una sola medida), la conexión con el capítulo 7 y con el ensemble, y la pregunta que lleva a promediar trozos.

## Narración

<!-- b1 -->
¿Por qué no ayuda grabar más? Porque una grabación más larga permite ver más frecuencias, más juntas, pero cada una sigue siendo una sola medida. Es lo del capítulo siete: una única medida con ruido no se acerca a la media por mucho que la mires. Hacen falta muchas medidas, y promediarlas.

- «¿Por qué no ayuda grabar más?» → `porque`: el bosque de 10 s con un signo de pregunta
- «Porque una grabación más larga» → `larga`: la traza se alarga
- «ver más frecuencias, más juntas» → `mas_frec`: aparecen más tallos pegados en el eje de frecuencias
- «cada una sigue siendo una sola medida» → `una_medida`: un punto aislado con la etiqueta «1 medida»
- «lo del capítulo siete» → `cap7`: la etiqueta «Capítulo 7» y el histograma de una sola medida suelta
- «una única medida con ruido» → `unica`: un punto que cae lejos de la media
- «no se acerca a la media» → `lejos`: una flecha roja entre el punto y la línea de la media
- «Hacen falta muchas medidas, y promediarlas» → `promediar`: muchos puntos que se agrupan y su promedio se fija sobre la media

<!-- b2 -->
Hay otra forma de verlo. La densidad espectral es un promedio sobre el ensemble, sobre mil grabaciones posibles. Un periodograma usa una sola. Es estimar un promedio con una única muestra. Lo raro sería que saliera bien.

- «Hay otra forma de verlo» → `otra`: limpia la pantalla
- «un promedio sobre el ensemble» → `ensemble`: entra «S_xx = promedio sobre el ensemble»
- «sobre mil grabaciones posibles» → `mil`: mil trazas tenues apiladas, como en el Cap. 10
- «Un periodograma usa una sola» → `una`: una sola traza se ilumina y las otras se apagan
- «estimar un promedio con una única muestra» → `estimar`: «promedio ← 1 muestra» con un signo de pregunta
- «Lo raro sería que saliera bien» → `raro`: sello «lo raro sería que saliera bien»

<!-- b3 -->
La solución también la conocemos del capítulo siete: promediar muchas medidas. Pero aquí tenemos una sola grabación, y un periodograma por grabación. ¿Qué podemos promediar, entonces?

- «promediar muchas medidas» → `muchas`: muchos periodogramas se apilan y se promedian
- «una sola grabación» → `una_grab`: los periodogramas desaparecen y queda una sola traza larga
- «un periodograma por grabación» → `uno_por`: a la traza le sale un solo periodograma
- «¿Qué podemos promediar, entonces?» → `pregunta`: un signo de pregunta grande sobre la traza

---

# Escena 09 — PromediarTrozos

**Capítulo YouTube:** Promediar trozos

**Objetivo:** partir la grabación en M trozos, promediar sus periodogramas y ver que la varianza cae como 1/M. Con 16 s de grabación: 16 trozos de 1 s (suave, 1 Hz de resolución).

## Narración

<!-- b1 -->
Partimos la grabación en trozos, calculamos el periodograma de cada uno y los promediamos. Del capítulo siete: la varianza del promedio de ene medidas independientes es la varianza de una dividida entre ene, y la desviación típica se divide entre la raíz de ene. Aquí igual: con eme trozos, la varianza se divide entre eme.

- «Partimos la grabación en trozos» → `partir`: la traza se corta en M trozos con tijeras o marcos
- «calculamos el periodograma de cada uno» → `cadauno`: debajo de cada trozo sale su periodograma
- «los promediamos» → `promedio`: los periodogramas se apilan y se funden en una curva que se pega a la densidad verdadera
- «Del capítulo siete» → `cap7`: entra «Capítulo 7»
- «la varianza del promedio de ene medidas independientes» → `varprom`: entra «σ²/n»
- «es la varianza de una» → `de_una`: la pieza σ² de la fórmula se resalta
- «dividida entre ene» → `entre_n`: se señala la n de la fórmula
- «la desviación típica se divide entre la raíz de ene» → `raiz`: entra «σ/√n» y la banda de Chebyshev que se angosta
- «Aquí igual» → `aqui`: la fórmula se traslada a los periodogramas
- «con eme trozos» → `emetrozos`: «M trozos» sustituye a la n
- «la varianza se divide entre eme» → `entre_m`: «varianza / M», en ámbar

<!-- b2 -->
Con números. Tienes dieciséis segundos de grabación. Si haces dieciséis trozos de un segundo, la desviación se divide entre raíz de dieciséis, cuatro: el espectro tiembla un cuarto de lo que temblaba. Una curva suave. Pero cada trozo dura un segundo, y la resolución es de un hercio: los tonos de cincuenta y cincuenta y medio salen fundidos.

- «Tienes dieciséis segundos de grabación» → `grab16`: una traza larga con la marca «16 s»
- «dieciséis trozos de un segundo» → `t16`: se divide en 16 trozos iguales con la marca «1 s»
- «la desviación se divide entre raíz de dieciséis» → `raiz16`: «1 / √16»
- «cuatro» → `cuatro`: «= ¼»
- «el espectro tiembla un cuarto» → `cuarto`: el bosque se aplana hasta una banda estrecha con «desviación ¼»
- «Una curva suave» → `suave`: la curva suave en ámbar
- «Pero cada trozo dura un segundo» → `cada_trozo`: se marca un trozo con «1 s»
- «la resolución es de un hercio» → `un_hz`: una llave «resolución 1 Hz»
- «los tonos de cincuenta y cincuenta y medio» → `tonos`: las dos rayas de 50 y 50,5 Hz
- «salen fundidos» → `fundidos`: los dos tonos de 50 y 50,5 Hz salen como un solo bulto

---

# Escena 10 — DosPerillas

**Capítulo YouTube:** Dos perillas y un compromiso

**Objetivo:** 4 trozos de 4 s (ruidoso, separa los tonos) y 1 trozo de 16 s; las dos perillas y el compromiso: solo más datos mejoran las dos cosas.

## Narración

<!-- b1 -->
Si haces cuatro trozos de cuatro segundos, la resolución es de un cuarto de hercio, y los dos tonos se separan. Pero solo promedias cuatro: la desviación se divide entre dos, y la curva tiembla bastante. Y con un solo trozo de dieciséis segundos, la resolución es excelente, pero vuelves al bosque de picos.

- «cuatro trozos de cuatro segundos» → `t4`: la grabación de 16 s se reparte en 4 trozos con la marca «4 s»
- «un cuarto de hercio» → `cuarto_hz`: una llave «resolución 0,25 Hz»
- «los dos tonos se separan» → `separan`: los tonos de 50 y 50,5 Hz salen como dos picos, con marca verde
- «solo promedias cuatro» → `solo4`: se cuentan cuatro periodogramas
- «la desviación se divide entre dos» → `entre2`: «1 / √4 = ½»
- «la curva tiembla bastante» → `tiembla`: la curva con una banda más ancha
- «un solo trozo de dieciséis segundos» → `un_trozo`: la grabación entera como un solo trozo con «16 s»
- «la resolución es excelente» → `excelente`: los dos picos salen muy finos y separados
- «vuelves al bosque de picos» → `bosque`: alrededor de los picos vuelve el bosque magenta

<!-- b2 -->
Hay dos perillas, y conviene no confundirlas. El número de trozos controla cuánto tiembla la estimación. La duración de cada trozo controla la resolución y el desenfoque. Y el número de trozos por la duración de cada uno es la grabación entera: con una grabación fija, subir una perilla baja la otra.

- «dos perillas» → `perillas`: dos perillas en pantalla
- «El número de trozos» → `n_trozos`: la primera perilla se rotula «M»
- «cuánto tiembla la estimación» → `tiembla2`: «M → temblor», con un bosque que se aplana al girar
- «La duración de cada trozo» → `dur_trozo`: la segunda perilla se rotula «duración»
- «la resolución y el desenfoque» → `resol`: «duración → resolución», con picos que se afinan al girar
- «Y el número de trozos por la duración de cada uno» → `producto`: «M × duración» se arma por piezas
- «la grabación entera» → `entera`: entra «M × duración = grabación total»
- «subir una perilla baja la otra» → `balancin`: un balancín: al subir una, baja la otra

<!-- b3 -->
O una curva suave con los picos borrosos, o picos nítidos ahogados en temblor. Ninguna elección gana en todo, y la única forma de mejorar las dos cosas es grabar durante más tiempo. Y todavía queda un tercer problema, que aparece en el momento mismo de cortar la señal con tijeras.

- «una curva suave con los picos borrosos» → `suave`: a la izquierda, curva suave con dos picos fundidos
- «picos nítidos ahogados en temblor» → `nitidos`: a la derecha, picos finos entre un bosque magenta
- «Ninguna elección gana en todo» → `ninguna`: una cruz roja sobre las dos
- «la única forma de mejorar las dos cosas» → `unica`: una flecha ámbar señala la grabación
- «grabar durante más tiempo» → `mas_tiempo`: la grabación se alarga y las dos perillas pueden subir juntas, con marca verde
- «un tercer problema» → `tercero`: «problema 3» en rojo
- «cortar la señal con tijeras» → `tijeras`: el icono de la tijera corta la traza

---

# Escena 11 — Cierre

**Capítulo YouTube:** Lo que viene: cortar sin romper

## Narración

<!-- b1 -->
Nos llevamos una cosa. Con datos finitos, el espectro sale desenfocado por la ventana y tembloroso por ser una sola muestra, y con una grabación fija no puedes arreglar las dos cosas a la vez. Pero queda una pregunta: ¿qué pasa exactamente cuando cortas? En el próximo episodio, «Cortar sin romper».

- «Con datos finitos» → `finitos`: una traza corta y acotada
- «desenfocado por la ventana» → `desenfocado`: el espectro desenfocado con la etiqueta «ventana»
- «tembloroso por ser una sola muestra» → `tembloroso`: el bosque de picos con la etiqueta «una sola muestra»
- «no puedes arreglar las dos cosas a la vez» → `dos_cosas`: las dos perillas con el balancín, y una cruz roja
- «Pero queda una pregunta» → `queda`: un signo de pregunta ámbar
- «¿qué pasa exactamente cuando cortas?» → `cortas`: la tijera corta la traza y aparece un signo de pregunta
- «En el próximo episodio» → `prox_ep`: la tijera se aleja hacia la derecha
- «Cortar sin romper» → `proximo`: el título «Cortar sin romper» entra con rebote
