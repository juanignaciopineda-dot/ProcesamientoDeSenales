# Episodio 5 — Cortar sin romper

Capítulo 11 (Densidad espectral de potencia), episodio 5 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 20 a 24), más un gancho y un cierre nuevos.

**Estado:** gancho y cierre aprobados por el usuario. Escenas `s01`–`s14` escritas; borrador 480p15 renderizado (9:37, 0 avisos, `ritmo.py` sin huecos de más de 4 s). Sigue: el usuario mira `salida/E5_Cortar_sin_romper-480p15.mp4` (paso 15); después render final `--calidad qh` (paso 16).

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Un tono puro debería ser una raya fina. Pero si lo cortas mal, sus faldas pueden tapar a otro tono un millón de veces más débil. ¿Cómo se corta sin romper?»
- ⭐ Escena 14 (cierre): resume el episodio y anuncia E6 por su título, «Fabricar el color y quitarlo».

Reparto de las escenas del guion base: 20 → escenas 03 y 04; 21 → 05 y 06; 22 → 07 y 08; 23 → 09 y 10; 24 → 11 a 13.
Solo se partieron bloques enteros en escenas atómicas: el texto del guion base no cambia.
Cosas que el E5 da por vistas en el E4: el periodograma y la resolución como 1 sobre la duración (escena 17), el promedio de trozos (19) y los tonos de 50 y 50,5 hercios.

---

# Escena 01 — Gancho

**Capítulo YouTube:** Un tono que tapa a otro

## Narración

<!-- b1 -->
Un tono puro debería ser una raya fina. Pero si lo cortas mal, sus faldas pueden tapar a otro tono un millón de veces más débil. ¿Cómo se corta sin romper?

- «Un tono puro» → `tono`: aparece una senoide azul que se dibuja sobre un eje
- «una raya fina» → `raya`: debajo, en el eje de frecuencias, su espectro: una raya delgada
- «si lo cortas mal» → `cortas`: unas tijeras cortan la senoide y en el corte queda un salto rojo
- «sus faldas» → `faldas`: la raya se abre en faldas a los lados
- «pueden tapar a otro tono» → `tapa`: un segundo tono pequeño junto a la raya queda cubierto por las faldas
- «un millón de veces más débil» → `millon`: junto al tono pequeño aparece «1/1.000.000»
- «¿Cómo se corta sin romper?» → `pregunta`: las tijeras vuelven con un signo de interrogación

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Cortar sin romper

## Narración

<!-- b1 -->
Cortar sin romper

- «Cortar» → `t1`: la palabra «Cortar» entra con rebote
- «sin romper» → `t2`: «sin romper» entra debajo, con la etiqueta «Capítulo 11 · Densidad espectral de potencia»

---

# Escena 03 — FugaAparece

**Capítulo YouTube:** Un tono de 10 Hz y otro de 10,5 Hz

## Narración

<!-- b1 -->
Graba un tono puro de diez hercios durante un segundo y calcula su espectro con la FFT, el algoritmo que usa cualquier ordenador para hacer Fourier con datos. Sale una raya limpia en diez hercios. Ahora repite con un tono de diez hercios y medio. La raya ya no es limpia: tiene unas faldas que se extienden a los lados.

- «un tono puro de diez hercios» → `tono10`: una senoide azul de 10 Hz se dibuja sobre un eje de 1 s, con la etiqueta «10 Hz»
- «durante un segundo» → `un_s`: una llave marca el segundo de grabación y se cuentan diez ciclos
- «con la FFT» → `fft`: una caja «FFT» recibe el trozo
- «el algoritmo que usa cualquier ordenador» → `algoritmo`: junto a la caja aparece un ordenador
- «hacer Fourier con datos» → `fourier`: de la caja sale un eje de frecuencias, todavía vacío
- «Sale una raya limpia» → `raya`: sobre el eje aparece una raya delgada
- «en diez hercios» → `raya10`: la raya se rotula «10 Hz»
- «un tono de diez hercios y medio» → `tono105`: junto al primero, otra senoide con la etiqueta «10,5 Hz»
- «La raya ya no es limpia» → `sucia`: la raya se ensancha y aparece una cruz roja
- «unas faldas» → `faldas`: aparecen las faldas, en magenta, a ambos lados de la raya
- «a los lados» → `lados`: dos flechas cortas señalan hacia afuera

<!-- b2 -->
La explicación está en cómo trabaja la FFT: trata el trozo como si se repitiera para siempre, pegado a sí mismo. Con diez hercios, en un segundo caben diez ciclos exactos, y la unión es perfecta. Con diez y medio, caben diez ciclos y medio: al pegar el final con el principio, queda un salto.

- «cómo trabaja la FFT» → `trabaja`: vuelve la caja «FFT» con el trozo de 10 Hz dentro
- «trata el trozo» → `trozo`: el trozo de un segundo se resalta con un marco
- «se repitiera para siempre» → `repite`: a izquierda y derecha aparecen copias del trozo hasta los bordes de la pantalla
- «pegado a sí mismo» → `pegado`: las copias se pegan, con pequeñas marcas en cada unión
- «Con diez hercios» → `c10`: quedan solo las copias del tono de 10 Hz
- «caben diez ciclos exactos» → `diez_ciclos`: un contador recorre los ciclos de 1 a 10
- «la unión es perfecta» → `perfecta`: la unión se resalta en verde, con la curva continua
- «Con diez y medio» → `c105`: cambio al tono de 10,5 Hz repetido
- «caben diez ciclos y medio» → `ciclos_y_medio`: el contador llega a 10 y un medio ciclo queda suelto
- «al pegar el final con el principio» → `pegar`: el final de una copia y el principio de la siguiente se acercan y se tocan
- «queda un salto» → `salto`: en la unión aparece un escalón en rojo

---

# Escena 04 — UnSaltoTodasLasFrecuencias

**Capítulo YouTube:** La fuga (leakage)

## Narración

<!-- b1 -->
Y un salto, como un escalón, necesita todas las frecuencias para dibujarse. Así que en el espectro aparece potencia donde no debería haber: la raya se convierte en una sinc, con un lóbulo principal y lóbulos laterales que bajan muy despacio. Esa potencia que se escapa a los lados se llama fuga.

- «un salto, como un escalón» → `escalon`: un escalón se dibuja sobre un eje de tiempo
- «necesita todas las frecuencias» → `todas`: debajo, el espectro del escalón: barras que se suceden sin acabarse hacia la derecha
- «para dibujarse» → `dibuja`: la suma de senoides va aproximando el escalón, de a una
- «en el espectro aparece potencia» → `potencia`: el espectro de la raya de 10,5 Hz, con potencia en rojo a los lados
- «donde no debería haber» → `nohaber`: signos de interrogación sobre las faldas
- «la raya se convierte en una sinc» → `sinc`: la raya se transforma en la curva sinc
- «un lóbulo principal» → `principal`: el lóbulo central se resalta en ámbar
- «lóbulos laterales» → `laterales`: los lóbulos laterales se resaltan
- «bajan muy despacio» → `despacio`: una flecha descendente suave recorre la cola de los laterales
- «Esa potencia que se escapa a los lados» → `escapa`: flechas salen de la raya hacia las faldas
- «se llama fuga» → `fuga`: la palabra «fuga (leakage)» entra con rebote

<!-- b2 -->
Una trampa: en el caso de diez hercios, la fuga también está. La sinc es la misma. Lo que pasa es que la FFT solo mira el espectro en algunos puntos, y esos puntos caen justo en los ceros de la sinc. No es que no haya fuga: es que no la estás mirando. En datos reales, esa coincidencia no ocurre nunca.

- «Una trampa» → `trampa`: la palabra «trampa» con un triángulo de aviso
- «en el caso de diez hercios» → `caso10`: vuelve la raya limpia de 10 Hz
- «la fuga también está» → `tambien`: detrás de la raya aparece la sinc en tenue
- «La sinc es la misma» → `misma`: las dos sincs, la de 10 y la de 10,5 Hz, se superponen y coinciden
- «solo mira el espectro en algunos puntos» → `puntos`: sobre el eje aparecen los puntos de la FFT, separados
- «esos puntos caen justo» → `justo`: los puntos se colocan sobre la curva
- «en los ceros de la sinc» → `ceros`: un círculo marca cada cruce por cero, y ahí cae un punto
- «No es que no haya fuga» → `nohay`: la sinc se resalta entera
- «no la estás mirando» → `nomiras`: un ojo tachado junto a la sinc
- «En datos reales» → `reales`: aparece un registro real, con ruido
- «esa coincidencia no ocurre nunca» → `nunca`: los puntos de la FFT se corren y dejan de caer en los ceros

<!-- b3 -->
La fuga es peligrosa cuando hay un tono fuerte y otro débil cerca: las faldas del fuerte pueden tapar al débil. ¿Cuánto más débil? Para hablar de potencias tan distintas necesitamos una escala adecuada.

- «La fuga es peligrosa» → `peligrosa`: la palabra «fuga» con un triángulo de aviso
- «un tono fuerte y otro débil cerca» → `dos_tonos`: dos rayas, una alta y otra pequeña a su lado
- «las faldas del fuerte» → `faldas_f`: del tono fuerte bajan las faldas
- «pueden tapar al débil» → `tapan`: las faldas cubren al tono débil
- «¿Cuánto más débil?» → `cuanto`: un signo de interrogación sobre el débil
- «potencias tan distintas» → `distintas`: aparecen los números «1» y «0,000001» a cada lado
- «una escala adecuada» → `escala`: entra una regla vertical, vacía

---

# Escena 05 — DecibeliosDesdeCero

**Capítulo YouTube:** Decibelios desde cero

## Narración

<!-- b1 -->
Si un tono tiene potencia uno y otro una millonésima, en una gráfica normal el pequeño es invisible: una millonésima de la altura. Para ver a la vez cosas tan distintas se cuentan ceros, es decir, se usa el logaritmo. Los decibelios son exactamente eso: diez veces el logaritmo en base diez del cociente entre dos potencias.

- «un tono tiene potencia uno» → `p1`: una barra azul alta con la etiqueta «1»
- «otro una millonésima» → `p2`: junto a ella, un punto apenas visible con la etiqueta «0,000001»
- «en una gráfica normal» → `normal`: los ejes se rotulan «escala lineal»
- «el pequeño es invisible» → `invisible`: el punto parpadea y se tacha
- «una millonésima de la altura» → `altura`: una llave a lo alto de la barra con «1/1.000.000»
- «Para ver a la vez» → `ver`: aparece un ojo junto a las dos barras
- «cosas tan distintas» → `distintas`: una flecha doble une la barra alta con el punto diminuto
- «se cuentan ceros» → `ceros`: los ceros de 0,000001 se resaltan de uno en uno
- «se usa el logaritmo» → `log`: aparece «log₁₀» junto a los ceros
- «Los decibelios» → `db`: la palabra «decibelios (dB)» entra con rebote
- «diez veces el logaritmo en base diez» → `formula1`: se construye «10 · log₁₀»
- «del cociente entre dos potencias» → `cociente`: se completa con «(P₁ / P₂)»

<!-- b2 -->
Con números. Diez veces más potencia son diez decibelios, porque el logaritmo de diez es uno. Cien veces, veinte. Mil veces, treinta. Un millón, sesenta. Cada diez decibelios, un cero más. Y la mitad de la potencia son unos menos tres decibelios: el punto de media altura de la telegráfica, en omega igual a alfa, estaba a menos tres decibelios.

- «Con números» → `numeros`: una regla vertical vacía entra a escena
- «Diez veces más potencia» → `x10`: primera marca de la regla: «×10»
- «son diez decibelios» → `d10`: junto a ella, «10 dB»
- «el logaritmo de diez es uno» → `log10`: debajo, «10 · log₁₀ 10 = 10 · 1»
- «Cien veces, veinte» → `x100`: segunda marca: «×100 → 20 dB»
- «Mil veces, treinta» → `x1000`: tercera marca: «×1.000 → 30 dB»
- «Un millón, sesenta» → `x1m`: cuarta marca: «×1.000.000 → 60 dB»
- «Cada diez decibelios, un cero más» → `cero_mas`: en cada escalón de 10 dB aparece un cero más
- «la mitad de la potencia» → `mitad`: en la regla aparece la marca «½»
- «unos menos tres decibelios» → `m3`: «10 · log₁₀ 0,5 ≈ −3 dB»
- «el punto de media altura de la telegráfica» → `telegrafica`: aparece la curva 4/(4 + ω²) con su altura media señalada
- «en omega igual a alfa» → `w_alfa`: una línea vertical en ω = 2 baja hasta la altura 0,5
- «estaba a menos tres decibelios» → `m3b`: sobre ese punto, la etiqueta «−3 dB»

---

# Escena 06 — LaFugaEnDecibelios

**Capítulo YouTube:** Las faldas de la ventana rectangular

## Narración

<!-- b1 -->
Ahora miremos la fuga con esta regla. Con la ventana rectangular, el primer lóbulo lateral está a menos trece decibelios del pico: más o menos una vigésima parte. Y los siguientes bajan, pero despacio: bastante lejos del pico, las faldas siguen a treinta o cuarenta decibelios por debajo.

- «miremos la fuga con esta regla» → `regla`: la sinc se dibuja en decibelios junto a la regla, con el pico a 0 dB
- «la ventana rectangular» → `rect`: aparece el recorte rectangular de un trozo, con su rótulo
- «el primer lóbulo lateral» → `primero`: el primer lóbulo lateral se resalta
- «a menos trece decibelios del pico» → `m13`: una llave desde el pico hasta ese lóbulo con «−13 dB»
- «una vigésima parte» → `veinte`: junto a ella, «≈ 1/20»
- «los siguientes bajan» → `bajan`: los demás laterales se resaltan uno a uno, cada vez más bajos
- «pero despacio» → `lento`: una línea marca la pendiente suave de las cimas
- «bastante lejos del pico» → `lejos`: una flecha recorre el eje hacia la cola
- «treinta o cuarenta decibelios por debajo» → `tres_cuatro`: las bandas «−30 dB» y «−40 dB» se marcan y las faldas pasan por ellas

<!-- b2 -->
Pongamos un tono débil, sesenta decibelios por debajo del fuerte, una millonésima de su potencia, al lado. Allí las faldas del fuerte están a menos treinta: mil veces por encima del débil. El tono débil queda enterrado. Si buscas un armónico pequeño en una señal, cortar con una ventana rectangular te lo esconde.

- «un tono débil» → `debil`: junto al pico fuerte aparece una raya pequeña
- «sesenta decibelios por debajo del fuerte» → `m60`: la raya cae hasta la marca «−60 dB»
- «una millonésima de su potencia» → `millon`: a su lado, «1/1.000.000»
- «las faldas del fuerte están a menos treinta» → `faldas30`: las faldas pasan por la marca «−30 dB», justo encima del débil
- «mil veces por encima del débil» → `mil`: una flecha de 30 dB entre las faldas y el débil, con «×1.000»
- «El tono débil queda enterrado» → `enterrado`: las faldas cubren la raya débil
- «un armónico pequeño» → `armonico`: la raya se rotula «armónico»
- «cortar con una ventana rectangular te lo esconde» → `esconde`: un ojo tachado sobre la zona de las faldas

<!-- b3 -->
Hace falta, entonces, una forma de cortar que derrame menos. Y la idea es sencilla: el problema era el salto en los bordes. Si no cortamos de golpe, no hay salto.

- «una forma de cortar que derrame menos» → `derrame`: unas tijeras con una gota que cae
- «Y la idea es sencilla» → `idea`: aparece una bombilla junto a las tijeras
- «el problema era el salto en los bordes» → `salto_bordes`: un trozo con saltos rojos en los dos extremos
- «Si no cortamos de golpe» → `nogolpe`: los bordes del trozo bajan suavemente hasta cero
- «no hay salto» → `sinsalto`: una tilde verde en cada borde

---

# Escena 07 — CampanaEnLosBordes

**Capítulo YouTube:** La ventana de Hann

## Narración

<!-- b1 -->
En lugar de cortar de golpe, multiplicamos el trozo por una campana que empieza en cero, sube suave y vuelve a cero en los bordes. Así el final y el principio del trozo valen los dos cero, y al pegarlos no hay salto. A esa campana se la llama ventana. La más usada es la de Hann, que tiene forma de coseno levantado.

- «En lugar de cortar de golpe» → `lugar`: el trozo de 10,5 Hz con sus bordes cortados en seco
- «multiplicamos el trozo por una campana» → `mult`: debajo entra una campana y entre ambos un signo «×»
- «empieza en cero» → `cero_ini`: un punto marca el comienzo de la campana en cero
- «sube suave» → `sube`: la campana sube
- «vuelve a cero en los bordes» → `cero_fin`: un punto marca el final de la campana en cero
- «el final y el principio del trozo valen los dos cero» → `ambos`: aparece el producto, y sus dos extremos caen a cero
- «al pegarlos no hay salto» → `pegar`: se pegan dos copias del producto, sin salto, con una tilde verde
- «se la llama ventana» → `ventana`: la palabra «ventana» entra con rebote junto a la campana
- «la de Hann» → `hann`: la campana se rotula «Hann»
- «coseno levantado» → `coseno`: un coseno se levanta hasta que su mínimo toca el cero, y queda la campana

<!-- b2 -->
El efecto en la fuga es enorme. Con la ventana rectangular, el primer lóbulo lateral estaba a menos trece decibelios. Con la de Hann, a menos treinta y uno. Con otra todavía más suave, la de Blackman, a menos cincuenta y ocho. Con Blackman, el tono débil de antes, sesenta decibelios por debajo, por fin tiene una oportunidad de asomar.

- «El efecto en la fuga es enorme» → `enorme`: el espectro en decibelios con la ventana de Hann: las faldas caen
- «la ventana rectangular» → `rect`: el núcleo de la rectangular, con su primer lateral
- «a menos trece decibelios» → `m13`: la etiqueta «−13 dB» en ese lóbulo
- «Con la de Hann» → `hann`: el núcleo de Hann aparece al lado
- «a menos treinta y uno» → `m31`: la etiqueta «−31 dB» en su primer lateral
- «la de Blackman» → `blackman`: aparece el núcleo de Blackman
- «a menos cincuenta y ocho» → `m58`: la etiqueta «−58 dB»
- «el tono débil de antes» → `debil`: vuelve la raya débil de la escena anterior
- «sesenta decibelios por debajo» → `m60`: una línea marca «−60 dB»
- «por fin tiene una oportunidad de asomar» → `asoma`: con Blackman la raya débil sobresale apenas de las faldas

---

# Escena 08 — AnchoContraFuga

**Capítulo YouTube:** Menos fuga, peor resolución

## Narración

<!-- b1 -->
Pero no hay nada gratis. Cuanto más suave es la ventana, más ancho es su lóbulo principal: el de Hann mide el doble que el de la rectangular, y el de Blackman, el triple. Y un lóbulo principal más ancho es más desenfoque. Menos fuga a cambio de peor resolución.

- «no hay nada gratis» → `gratis`: las palabras «nada gratis» entran con rebote
- «Cuanto más suave es la ventana» → `suave`: las tres ventanas se alinean, de la más brusca a la más suave
- «más ancho es su lóbulo principal» → `ancho`: los lóbulos principales de los tres núcleos se ensanchan
- «el de Hann mide el doble» → `doble`: el principal de Hann con la etiqueta «ancho 2»
- «que el de la rectangular» → `rectangular`: el de la rectangular con «ancho 1»
- «el de Blackman» → `blackman`: el de Blackman aparece
- «el triple» → `triple`: su etiqueta: «ancho 3»
- «más desenfoque» → `desenfoque`: los tres lóbulos ensanchados emborronan dos rayas cercanas
- «Menos fuga a cambio de peor resolución» → `compromiso`: un balancín con «fuga» bajando y «resolución» subiendo

<!-- b2 -->
Con los tonos de cincuenta y cincuenta y medio y dos segundos de grabación, la rectangular los separa justo. Con la de Hann, el doble de ancha, se funden, y hacen falta cuatro segundos. Así que cada ventana tiene su uso. La de Hann, por defecto. La de Blackman, cuando hay algo pequeño junto a algo enorme. La rectangular, cuando manda la resolución y las amplitudes se parecen.

- «los tonos de cincuenta y cincuenta y medio» → `tonos`: dos rayas con las etiquetas «50 Hz» y «50,5 Hz»
- «dos segundos de grabación» → `dos_s`: una barra de tiempo con la etiqueta «2 s»
- «la rectangular los separa justo» → `rectsep`: con la rectangular, dos picos que apenas se separan, y una tilde
- «Con la de Hann» → `hannf`: los dos picos se convierten en un bulto
- «el doble de ancha» → `dobleancha`: el lóbulo de Hann el doble de ancho que el rectangular
- «se funden» → `funden`: un solo bulto, con una cruz
- «hacen falta cuatro segundos» → `cuatro_s`: la barra de tiempo crece a «4 s» y los dos picos vuelven a aparecer
- «cada ventana tiene su uso» → `uso`: tres fichas vacías entran
- «La de Hann, por defecto» → `ficha_hann`: se llena la primera ficha: «Hann: por defecto»
- «cuando hay algo pequeño junto a algo enorme» → `ficha_bl`: segunda ficha: «Blackman: algo pequeño junto a algo enorme»
- «La rectangular, cuando manda la resolución» → `ficha_rect`: tercera ficha: «rectangular: máxima resolución»
- «las amplitudes se parecen» → `parecen`: dos picos de igual altura junto a la ficha

<!-- b3 -->
La ventana decide cómo se deforma el espectro, y la resolución la sigue dando el tiempo grabado. Pero hay un atajo muy tentador, y muy extendido, para mejorar la resolución sin grabar más. Veamos si funciona.

- «cómo se deforma el espectro» → `deforma`: una ventana y el espectro que se deforma con ella
- «la resolución la sigue dando» → `sigue`: aparece el cartel «resolución» con una flecha que llega desde la izquierda
- «el tiempo grabado» → `tiempo`: un reloj ocupa el origen de la flecha
- «un atajo muy tentador» → `atajo`: una flecha punteada en forma de atajo
- «muy extendido» → `extendido`: junto al atajo, una fila de personas que lo siguen
- «sin grabar más» → `sin_grabar`: el reloj se tacha
- «Veamos si funciona» → `funciona`: un signo de interrogación grande

---

# Escena 09 — EncuestaDeLosCeros

**Capítulo YouTube:** ¿Rellenar con ceros separa dos tonos?

## Narración

<!-- b1 -->
Tienes sesenta y cuatro muestras de dos tonos muy cercanos, y la FFT te da unos pocos puntos con un solo bulto. Alguien te sugiere añadir dos mil ceros al final de los datos y volver a calcular la FFT, que así tendrá muchos más puntos. ¿Aparecerán los dos picos? Piénsalo.

- «sesenta y cuatro muestras» → `m64`: una fila de 64 puntos sobre un eje de tiempo
- «dos tonos muy cercanos» → `cercanos`: etiqueta «dos tonos muy cercanos»
- «unos pocos puntos con un solo bulto» → `bulto`: su FFT: pocos puntos formando un solo bulto
- «Alguien te sugiere» → `alguien`: una persona con una burbuja de diálogo
- «añadir dos mil ceros» → `ceros`: a la derecha de los datos se alarga una fila plana con «+ 2.000 ceros»
- «al final de los datos» → `final`: una llave señala dónde termina el registro real
- «volver a calcular la FFT» → `recalcula`: entra la caja «FFT»
- «muchos más puntos» → `mas_puntos`: los puntos del espectro se multiplican
- «¿Aparecerán los dos picos?» → `encuesta`: encuesta con dos opciones: «sí» y «no»
- «Piénsalo» → `piensa`: una cuenta atrás de tres segundos

<!-- b2 -->
No. La curva sale mucho más suave, bonita y completa. Y sigue siendo un solo bulto. En cambio, si en lugar de ceros tienes doscientas cincuenta y seis muestras de verdad, aparecen dos picos, justo en las dos frecuencias.

- «No» → `no`: la opción «no» se marca en verde y «sí» se tacha
- «La curva sale mucho más suave» → `suave`: la FFT con relleno: una curva continua
- «bonita y completa» → `bonita`: la curva queda entera sobre el eje
- «sigue siendo un solo bulto» → `unbulto`: un círculo señala que sigue habiendo un solo bulto
- «en lugar de ceros» → `enlugar`: los ceros grises de la fila se reemplazan por puntos reales
- «doscientas cincuenta y seis muestras de verdad» → `m256`: abajo, 256 muestras reales de los dos tonos
- «aparecen dos picos» → `dos_picos`: su FFT muestra dos picos
- «justo en las dos frecuencias» → `frecs`: líneas punteadas bajan desde los picos a las dos frecuencias

---

# Escena 10 — InterpolacionNoInformacion

**Capítulo YouTube:** Interpolación, no información

## Narración

<!-- b1 -->
La razón es la de la fuga: la FFT mira el espectro en algunos puntos. Con sesenta y cuatro muestras, el espectro que hay debajo ya está decidido, desenfocado por una ventana de sesenta y cuatro. Los ceros no son datos: no cambian esa curva, solo hacen que la FFT la mire en más puntos. Es interpolación, no información.

- «la FFT mira el espectro en algunos puntos» → `mira`: sobre el eje, los pocos puntos de la FFT de 64 muestras
- «Con sesenta y cuatro muestras» → `c64`: vuelve la fila de 64 muestras sobre el eje de tiempo
- «el espectro que hay debajo» → `debajo`: aparece, en gris, la curva de fondo
- «ya está decidido» → `decidido`: un candado sobre la curva gris
- «una ventana de sesenta y cuatro» → `v64`: una ventana de 64 muestras y el desenfoque que produce
- «Los ceros no son datos» → `nodatos`: los ceros del relleno se ven en gris
- «no cambian esa curva» → `nocambia`: la curva gris sigue idéntica
- «la mire en más puntos» → `masp`: aparecen muchos más puntos, todos sobre la misma curva
- «interpolación, no información» → `interp`: la frase «interpolación, no información» entra con rebote

<!-- b2 -->
¿Entonces rellenar con ceros no sirve? Sí sirve, para dos cosas: ubicar con más precisión un pico que ya sabes que es único, y no subestimar su altura cuando cae entre dos puntos de la FFT. Lo que no hace nunca es separar dos cosas que la ventana ya fundió.

- «¿Entonces rellenar con ceros no sirve?» → `pregunta`: un signo de interrogación sobre «ceros»
- «Sí sirve» → `sirve`: el signo se convierte en una tilde
- «ubicar con más precisión un pico» → `ubicar`: un pico único con una línea que marca su posición exacta
- «que ya sabes que es único» → `unico`: aparece una tilde con «ubicar un pico único»
- «no subestimar su altura» → `altura`: un pico entre dos puntos de la FFT: sin relleno, su altura queda baja; con relleno, sube
- «entre dos puntos de la FFT» → `entre`: los dos puntos vecinos se marcan
- «Lo que no hace nunca» → `nunca`: una cruz roja
- «separar dos cosas» → `separar`: dos picos, con la etiqueta «separar dos picos» junto a la cruz
- «que la ventana ya fundió» → `fundio`: siguen fundidos en un solo bulto, aunque haya más puntos

<!-- b3 -->
La regla, otra vez: la resolución solo se compra con tiempo grabado. Y con esto ya tenemos todas las piezas. Falta juntarlas en el método que se usa de verdad.

- «la resolución solo se compra con tiempo grabado» → `compra`: una moneda con un reloj paga un cartel «resolución»
- «Y con esto ya tenemos» → `tenemos`: la moneda y el reloj se apartan hacia un lado
- «todas las piezas» → `piezas`: fichas de las escenas anteriores: «trozos», «ventana», «promedio», «media»
- «el método que se usa de verdad» → `metodo`: las fichas señalan un hueco con un signo de interrogación

---

# Escena 11 — MetodoDeWelch

**Capítulo YouTube:** El método de Welch

## Narración

<!-- b1 -->
El método que se usa en la práctica junta todo lo que hemos visto, y se llama método de Welch. Primero, se resta la media. Segundo, se parte la grabación en trozos que se solapan por la mitad. Tercero, a cada trozo se le aplica una ventana de Hann. Y cuarto, se promedian todos los periodogramas.

- «todo lo que hemos visto» → `junta`: las fichas de las escenas anteriores convergen en el centro
- «método de Welch» → `welch`: el rótulo «método de Welch» entra con rebote
- «Primero, se resta la media» → `media`: se enciende la ficha «restar la media» y un registro baja hasta quedar centrado en cero
- «se parte la grabación en trozos» → `trozos`: se enciende la ficha «trozos solapados a la mitad» y el registro se parte
- «se solapan por la mitad» → `solapan`: los trozos se superponen, cada uno por la mitad del anterior
- «Tercero, a cada trozo» → `tercero`: se enciende la ficha «ventana de Hann» y los trozos se resaltan
- «una ventana de Hann» → `hann`: cada trozo recibe su campana
- «se promedian todos los periodogramas» → `promedia`: se enciende la ficha «promediar» y los periodogramas se apilan y se funden en uno

<!-- b2 -->
¿Por qué solapar? La ventana de Hann aplasta los bordes de cada trozo, así que sin solapamiento esas muestras casi no cuentan. Solapando, lo que en un trozo cae en el borde, en el siguiente cae en el centro. Y de paso salen casi el doble de trozos: de ocho a quince, y la desviación se divide entre uno coma cuatro. Una mejora modesta, pero gratis.

- «¿Por qué solapar?» → `porque`: un signo de interrogación sobre los trozos solapados
- «aplasta los bordes de cada trozo» → `aplasta`: las campanas bajan a cero en los bordes de cada trozo
- «esas muestras casi no cuentan» → `nocuentan`: las muestras de los bordes se apagan
- «lo que en un trozo cae en el borde» → `borde`: una muestra marcada en el borde del primer trozo
- «en el siguiente cae en el centro» → `centro`: esa misma muestra, en el centro del segundo trozo
- «casi el doble de trozos» → `doble`: dos filas: «sin solapar: 8 trozos» y «con solapamiento: 15»
- «de ocho a quince» → `ocho_quince`: los números 8 y 15 se resaltan
- «se divide entre uno coma cuatro» → `raiz`: aparece «√(15/8) ≈ 1,4»
- «Una mejora modesta» → `modesta`: la cifra 1,4 se queda pequeña
- «pero gratis» → `gratis`: una tilde verde

---

# Escena 12 — ElPermisoDeLaErgodicidad

**Capítulo YouTube:** ¿Con qué permiso se promedia en el tiempo?

## Narración

<!-- b1 -->
Detrás del método hay un salto que conviene mirar de frente. La densidad espectral es un promedio sobre el ensemble, sobre todas las grabaciones posibles. Y nosotros estamos promediando trozos de una sola grabación, a lo largo del tiempo. ¿Con qué permiso?

- «un salto que conviene mirar de frente» → `salto`: un abismo entre dos orillas, «ensemble» y «tiempo»
- «La densidad espectral» → `densidad`: en la orilla izquierda aparece el rótulo «densidad espectral» con una curva pequeña
- «un promedio sobre el ensemble» → `ensemble`: en la orilla izquierda, una pila de grabaciones con un corte vertical
- «todas las grabaciones posibles» → `todas`: la pila se llena de curvas
- «Y nosotros estamos promediando» → `nosotros`: una lupa pasa a la orilla derecha, vacía
- «trozos de una sola grabación» → `una`: en la orilla derecha, una sola grabación partida en trozos
- «a lo largo del tiempo» → `tiempo`: una flecha horizontal sobre esa grabación
- «¿Con qué permiso?» → `permiso`: un sello de permiso con un signo de interrogación cruza el abismo

<!-- b2 -->
Con el de la ergodicidad, del capítulo anterior. Recuerda las pilas: cada realización es una tensión constante, y promediar en el tiempo da el voltaje de esa pila, no el de todas. Si el proceso no es ergódico, promediar más tiempo no te acerca a la densidad espectral del ensemble, sino a la del trozo de ensemble que te ha tocado.

- «la ergodicidad» → `ergo`: el sello queda con el texto «ergodicidad = permiso»
- «del capítulo anterior» → `cap10`: aparece la etiqueta «capítulo 10»
- «Recuerda las pilas» → `pilas`: el cajón de pilas del capítulo 10
- «una tensión constante» → `constante`: cada pila se dibuja como una línea horizontal a su propio voltaje
- «promediar en el tiempo» → `prom_t`: una flecha recorre una de las líneas
- «el voltaje de esa pila» → `esa_pila`: su valor se señala, distinto del de las otras
- «no el de todas» → `todas`: aparece el valor medio del ensemble, en otra altura
- «no es ergódico» → `noerg`: una cruz roja junto al ensemble
- «promediar más tiempo» → `mas_t`: la flecha temporal se alarga
- «no te acerca a la densidad espectral del ensemble» → `noacerca`: una flecha que no llega a la del ensemble
- «el trozo de ensemble que te ha tocado» → `tocado`: la pila concreta se resalta en ámbar

---

# Escena 13 — RepiteConOtroTramo

**Capítulo YouTube:** Un pico real vuelve a aparecer

## Narración

<!-- b1 -->
Y una regla práctica, de la misma familia que "mira la nube antes que el número". Si en una estimación aparece un pico llamativo, repítela con otro tramo de datos. Lo que es real vuelve a aparecer; el temblor del estimador, no. Con esto ya sabemos medir un espectro. Lo siguiente es usarlo.

- «una regla práctica» → `regla`: las palabras «regla práctica» entran con rebote
- «mira la nube antes que el número» → `nube`: vuelve la nube de puntos del capítulo 7 junto a un número
- «Si en una estimación» → `estimacion`: aparece el eje de una estimación de espectro, todavía sin pico
- «un pico llamativo» → `llamativo`: una estimación con un pico alto resaltado
- «repítela con otro tramo de datos» → `repite`: una segunda estimación de otro tramo de la grabación
- «vuelve a aparecer» → `vuelve`: el pico está también en la segunda, con una tilde
- «el temblor del estimador, no» → `temblor`: otro pico que solo aparece en una, con una cruz
- «ya sabemos medir un espectro» → `medir`: un espectro limpio y completo
- «Lo siguiente es usarlo» → `usarlo`: una flecha sale del espectro hacia la derecha

---

# Escena 14 — Cierre

**Capítulo YouTube:** Próximo episodio: Fabricar el color y quitarlo

## Narración

<!-- b1 -->
Hoy hemos aprendido a cortar sin romper: una ventana suave frena la fuga, el tiempo grabado compra la resolución, y Welch junta todo en un método. En el próximo episodio, Fabricar el color y quitarlo: un filtro que pinta el ruido blanco del color que quieras, y otro que lo deja blanco otra vez.

- «cortar sin romper» → `cortar`: vuelve el trozo con las tijeras, ahora sin salto
- «una ventana suave frena la fuga» → `ventana`: una campana sobre el trozo y las faldas que bajan
- «el tiempo grabado compra la resolución» → `tiempo`: un reloj que paga un cartel «resolución»
- «Welch junta todo en un método» → `welch`: las cuatro fichas del método se encienden juntas
- «En el próximo episodio» → `proximo`: las fichas se apartan y entra una tarjeta de episodio
- «Fabricar el color y quitarlo» → `titulo`: el título del episodio 6 entra con rebote
- «un filtro que pinta el ruido blanco del color que quieras» → `pinta`: un espectro plano entra a un bloque y sale coloreado
- «otro que lo deja blanco otra vez» → `blanquea`: un segundo bloque devuelve el espectro coloreado a plano
