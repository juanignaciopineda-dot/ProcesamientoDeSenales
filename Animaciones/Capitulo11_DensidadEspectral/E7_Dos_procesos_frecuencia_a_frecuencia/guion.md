# Episodio 7 — Dos procesos, frecuencia a frecuencia

Capítulo 11 (Densidad espectral de potencia), episodio 7 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 29 a 32), más un gancho y un cierre nuevos.

**Estado:** `guion.md` con momentos y 18 escenas animadas (`s01`–`s18`). Borrador 480p15 de 8:36 con 0 avisos. Pendiente: revisar el texto ⭐ (paso 9) y el visto bueno del usuario al mp4 (paso 15); después, render final.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Dos grabaciones sin ninguna relación entre sí. Mides cuánto se parecen, y sale uno: parecido perfecto. Es mentira, y hoy vemos por qué.»
- ⭐ Escena 18 (cierre): repasa el capítulo y anuncia el E1 del Cap. 12 por su título, «¿Cuál es el mejor filtro?».

Retoque de una frase del guion base (escena 31, bloque 5, ahora escena 13): «el colador que buscábamos en la primera escena» pasa a «el colador que buscábamos al empezar el capítulo», porque el episodio se ve suelto.

Reparto de las escenas del guion base: 29 → escenas 03 a 06; 30 → 07 a 09; 31 → 10 a 13; 32 → 14 a 17.
Solo se partieron bloques enteros en escenas atómicas: el resto del texto del guion base no cambia.

Bucles de este episodio: la parábola de Cauchy-Schwarz (tercera aparición; la escena 07 la recuerda con el mismo dibujo del Cap. 7 y la 09 anuncia la cuarta en el Cap. 13); la voz y el murmullo de la escena 01 del Cap. 11 (escenas 13 y 17); «mira la nube antes que el número» (Cap. 7 → escena 15).

---

# Escena 01 — Gancho

**Capítulo YouTube:** Dos grabaciones sin relación

## Narración

<!-- b1 -->
Dos grabaciones sin ninguna relación entre sí. Mides cuánto se parecen, y sale uno: parecido perfecto. Es mentira, y hoy vemos por qué.

- «Dos grabaciones» → `dos`: aparecen dos trazas de ruido distintas, una sobre otra
- «ninguna relación» → `sinrel`: entre ellas un signo «≠» y el rótulo «sin relación»
- «Mides cuánto se parecen» → `mides`: una flecha lleva las dos trazas a una caja «coherencia»
- «sale uno» → `uno`: de la caja sale un «1» enorme en rojo
- «parecido perfecto» → `perfecto`: el «1» se rodea de un aura como si fuera un acierto
- «Es mentira» → `mentira`: una cruz roja tacha el «1»
- «hoy vemos por qué» → `porque`: una lupa se acerca al «1» tachado

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Dos procesos, frecuencia a frecuencia

## Narración

<!-- b1 -->
Dos procesos, frecuencia a frecuencia.

- «Dos procesos» → `t1`: «Dos procesos,» entra con rebote
- «frecuencia a frecuencia» → `t2`: «frecuencia a frecuencia» entra debajo, con la etiqueta «Capítulo 11 · Densidad espectral de potencia»

---

# Escena 03 — DosProcesosALaVez

**Capítulo YouTube:** Dos procesos a la vez

## Narración

<!-- b1 -->
Hasta ahora hemos mirado un proceso cada vez. Pero en señales casi siempre hay dos: lo que se envía y lo que se recibe, la voz y lo que capta un micrófono lejano. Del capítulo anterior, la correlación cruzada mide cuánto se parece uno a una copia desplazada del otro. Su transformada se llama densidad espectral cruzada.

- «un proceso cada vez» → `uno`: una traza azul sola en el centro
- «casi siempre hay dos» → `dos`: aparece una segunda traza debajo
- «lo que se envía y lo que se recibe» → `envia`: rótulos «envía» sobre la primera y «recibe» sobre la segunda
- «la voz y lo que capta un micrófono lejano» → `mic`: entran la persona azul a la izquierda y el micrófono a la derecha
- «Del capítulo anterior» → `anterior`: un recuadro pequeño «Cap. 10» en un rincón
- «la correlación cruzada» → `cruzada`: aparece «R_yx(τ)» en ámbar
- «una copia desplazada del otro» → `copia`: la traza de abajo se desliza sobre la de arriba
- «Su transformada» → `transf`: una flecha sale de «R_yx(τ)» hacia la derecha
- «densidad espectral cruzada» → `densidad`: la flecha termina en «S_yx(jω)» y el nombre queda en ámbar

---

# Escena 04 — ElMicrofonoQueLlegaTarde

**Capítulo YouTube:** El micrófono que llega tarde

## Narración

<!-- b1 -->
Un ejemplo: el micrófono capta la voz medio segundo tarde. La correlación cruzada tiene su pico en tau igual a cero coma cinco, no en cero: ya no es par. Y si no es par, la parte con jota de la transformada no se cancela. La densidad cruzada es un número complejo en cada frecuencia.

- «el micrófono capta la voz» → `tarde`: aparecen la voz x y el micrófono, y «y(t) = x(t − …)»
- «medio segundo tarde» → `medio`: el hueco se completa con «0,5» y un reloj que marca 0,5 s
- «tiene su pico en tau igual a cero coma cinco» → `pico`: se dibuja R_yx(τ) con un pico en τ = 0,5
- «no en cero» → `nocero`: una marca en τ = 0 queda tachada
- «ya no es par» → `nopar`: el espejo punteado de la curva no coincide con ella
- «la parte con jota» → `jota`: debajo, la transformada escrita como «cos − j sen» con el término con j resaltado
- «no se cancela» → `nocancela`: las dos áreas del seno quedan a un mismo lado, sin anularse
- «un número complejo en cada frecuencia» → `complejo`: sobre un eje ω aparece «S_yx(jω)» con la etiqueta «complejo»

---

# Escena 05 — NumerosComplejosComoFlechas

**Capítulo YouTube:** Números complejos como flechas

## Narración

<!-- b1 -->
Un número complejo se puede ver como una flecha en el plano: tiene un largo, que se llama módulo, y un ángulo. Y multiplicar por e elevado a menos jota por un ángulo es girar la flecha ese ángulo, sin cambiar su largo. Es la forma más cómoda de pensar en ellos.

- «una flecha en el plano» → `flecha`: corte seco; un plano con ejes y una flecha desde el origen
- «un largo, que se llama módulo» → `modulo`: una llave sobre la flecha con «módulo»
- «y un ángulo» → `angulo`: un arco desde el eje con «ángulo»
- «multiplicar por e elevado a menos jota por un ángulo» → `exp`: aparece «× e^{−jθ}» construida por piezas
- «es girar la flecha ese ángulo» → `gira`: la flecha gira en sentido horario un ángulo θ
- «sin cambiar su largo» → `largo`: una circunferencia punteada muestra que la punta no sale de ella
- «la forma más cómoda de pensar en ellos» → `comoda`: quedan rotulados «módulo = largo» y «ángulo = giro»

---

# Escena 06 — ModuloYAngulo

**Capítulo YouTube:** Módulo y ángulo de la densidad cruzada

## Narración

<!-- b1 -->
En el ejemplo, la densidad cruzada es la densidad de la voz por e elevado a menos jota omega por cero coma cinco. El módulo es la densidad de la voz: cuánta potencia comparten las dos señales en esa frecuencia. El ángulo es menos cero coma cinco por omega: en un hercio, omega es dos pi, y la flecha gira media vuelta.

- «En el ejemplo» → `ejemplo`: vuelve el micrófono retrasado y aparece «S_yx(jω) = ?»
- «la densidad de la voz» → `sxx`: se arma «S_xx(jω)» en azul
- «por e elevado a menos jota omega» → `exp`: se suma «· e^{−jω·…}»
- «por cero coma cinco» → `medio`: el exponente se completa con «0,5»
- «El módulo es la densidad de la voz» → `modulo`: una flecha de largo S_xx con llave de «módulo»
- «cuánta potencia comparten» → `comparten`: el rótulo «módulo = cuánto comparten»
- «en esa frecuencia» → `esafreq`: una marca sobre un eje ω fija la frecuencia de la flecha
- «El ángulo es menos cero coma cinco por omega» → `angulo`: un arco con «−0,5 ω»
- «en un hercio, omega es dos pi» → `hz`: aparece «1 Hz → ω = 2π»
- «gira media vuelta» → `media`: la flecha gira media vuelta, hasta «−π», con el largo intacto

<!-- b2 -->
Así que la densidad cruzada dice dos cosas en cada frecuencia: cuánto se parecen las dos señales, en el módulo, y cuánto están desfasadas, en el ángulo. Y como con las variables del capítulo siete, hay un límite a cuánto pueden parecerse. Recuerda la parábola.

- «dice dos cosas en cada frecuencia» → `dos`: dos rótulos, «módulo» y «ángulo», bajo la flecha
- «cuánto se parecen las dos señales, en el módulo» → `parecen`: el módulo se resalta en ámbar con «parecido»
- «cuánto están desfasadas, en el ángulo» → `desfase`: el ángulo se resalta con «desfase»
- «las variables del capítulo siete» → `var7`: aparece el par de flechas con su ángulo, como en el capítulo 7
- «hay un límite» → `limite`: una barrera horizontal aparece sobre el módulo
- «Recuerda la parábola» → `parabola`: asoma la silueta de la parábola del capítulo 7

---

# Escena 07 — LaParabolaDelCapitulo7

**Capítulo YouTube:** La parábola del capítulo 7

## Narración

<!-- b1 -->
En el capítulo siete demostramos que la covarianza al cuadrado nunca supera el producto de las varianzas. El truco era mezclar las dos variables con un número lambda: la varianza de la mezcla nunca es negativa, y desarrollada es una parábola en lambda. Una parábola que nunca baja de cero tiene el discriminante menor o igual que cero. De ahí salía todo.

- «la covarianza al cuadrado» → `desig`: corte seco; aparece «σ_XY²»
- «nunca supera» → `nosupera`: se suma «≤»
- «el producto de las varianzas» → `prodvar`: se completa «σ_X² σ_Y²»
- «mezclar las dos variables con un número lambda» → `mezcla`: debajo, «X + λY»
- «la varianza de la mezcla nunca es negativa» → `nonegativa`: «Var(X + λY) ≥ 0»
- «desarrollada es una parábola en lambda» → `parabola`: se dibuja la parábola con «λ²σ_Y² + 2λσ_XY + σ_X²»
- «Una parábola que» → `unaparab`: la parábola se ilumina
- «nunca baja de cero» → `nobaja`: la parábola queda por encima del eje, sin cortarlo
- «el discriminante menor o igual que cero» → `discr`: aparece «discriminante ≤ 0» con el punto bajo del eje
- «De ahí salía todo» → `todo`: la desigualdad del principio se resalta

---

# Escena 08 — LaParabolaFrecuenciaAFrecuencia

**Capítulo YouTube:** La misma parábola, frecuencia a frecuencia

## Narración

<!-- b1 -->
Ahora con procesos. Mezclamos equis con una versión de i griega multiplicada por un número alfa, y a veces retrasada. La densidad espectral de la mezcla, en una frecuencia cualquiera, es una parábola en alfa: la densidad de i griega por alfa al cuadrado, más un término con la cruzada por alfa, más la densidad de equis.

- «Mezclamos equis» → `mezcla`: corte seco; aparece «z = x + …» con x en azul
- «multiplicada por un número alfa» → `alfa`: se suma «α · y»
- «y a veces retrasada» → `retraso`: junto a y aparece «(retrasada)» con un reloj pequeño
- «La densidad espectral de la mezcla» → `dzz`: aparece «D_zz(ω)» en ámbar
- «en una frecuencia cualquiera» → `freq`: un eje ω con una marca que se mueve a una frecuencia
- «una parábola en alfa» → `parab`: se dibuja la parábola de D_zz contra α
- «la densidad de i griega por alfa al cuadrado» → `t1`: «D_yy α²»
- «más un término con la cruzada por alfa» → `t2`: «+ 2 Re(D_yx) α»
- «más la densidad de equis» → `t3`: «+ D_xx»

<!-- b2 -->
Y la densidad espectral de la mezcla nunca es negativa. Es la misma parábola que nunca baja de cero, en cada frecuencia por separado. Su discriminante da la desigualdad: el módulo de la densidad cruzada al cuadrado no supera el producto de las dos densidades. El retardo sirve para girar la flecha y quedarse con el módulo entero: el detalle está en el apunte en profundidad.

- «nunca es negativa» → `nonegativa`: «D_zz ≥ 0» y la parábola sobre el eje
- «la misma parábola» → `misma`: la parábola del capítulo 7 se superpone y coincide
- «en cada frecuencia por separado» → `cadafreq`: la parábola se repite en varias frecuencias a lo largo del eje ω
- «Su discriminante» → `discr`: aparece «discriminante ≤ 0»
- «el módulo de la densidad cruzada al cuadrado» → `mod2`: se arma «|D_yx(jω)|²»
- «no supera el producto de las dos densidades» → `prod`: se completa «≤ D_xx(jω) D_yy(jω)»
- «El retardo» → `retardo`: aparece el rótulo «retardo τ» junto a y
- «sirve para girar la flecha» → `gira`: una flecha compleja gira hasta quedar sobre el eje real
- «el detalle está en el apunte en profundidad» → `apunte`: una nota pequeña «apunte en profundidad»

---

# Escena 09 — LaComprobacionConElMicrofono

**Capítulo YouTube:** Comprobación con el micrófono

## Narración

<!-- b1 -->
Es la parábola de Cauchy-Schwarz del capítulo siete, la misma que en el capítulo anterior acotó la autocovarianza. Y aún volverá una vez más, en el capítulo trece. Comprobémoslo con el micrófono. El módulo de la cruzada es la densidad de la voz, y al cuadrado, la densidad de la voz al cuadrado. La densidad del micrófono es la misma que la de la voz, porque retrasar no cambia la potencia.

- «la parábola de Cauchy-Schwarz del capítulo siete» → `cs7`: la parábola del capítulo 7 se superpone a la de esta escena, igual
- «el capítulo anterior» → `anterior`: aparece un recuadro pequeño «Cap. 10»
- «acotó la autocovarianza» → `autocov`: una cita pequeña del capítulo 10, «|R(τ)| ≤ R(0)»
- «una vez más, en el capítulo trece» → `cap13`: una flecha hacia un recuadro «Cap. 13»
- «Comprobémoslo con el micrófono» → `comprobar`: corte seco; vuelven la voz y el micrófono retrasado
- «El módulo de la cruzada» → `modulo`: aparece «|S_yx|² = S_xx²»
- «la densidad de la voz al cuadrado» → `sxx2`: el «S_xx²» se resalta en azul
- «La densidad del micrófono es la misma» → `syy`: aparece «S_yy = S_xx»
- «retrasar no cambia la potencia» → `retrasar`: una onda desplazada con la misma área bajo la curva

<!-- b2 -->
Así que los dos lados son iguales: la parábola toca el eje. En el capítulo siete, tocar el eje era rho igual a uno, una variable exactamente una recta de la otra. Aquí es lo mismo: el micrófono es una copia exacta de la voz, sin nada de azar añadido. Cuanto más ruido añada la sala, más se separarán los dos lados. Y eso tiene una medida.

- «los dos lados son iguales» → `iguales`: «S_xx · S_xx = S_xx · S_xx» con un signo «=» en verde
- «la parábola toca el eje» → `toca`: la parábola baja hasta tocar el eje en un punto
- «En el capítulo siete» → `cap7`: un recuadro pequeño «Cap. 7»
- «rho igual a uno» → `rho1`: aparece «ρ = 1» con la recta del capítulo 7
- «una recta de la otra» → `recta`: puntos alineados sobre una recta
- «Aquí es lo mismo» → `mismo`: una flecha lleva la recta al micrófono y la voz
- «una copia exacta de la voz» → `copia`: la voz y el micrófono se superponen, idénticos
- «sin nada de azar añadido» → `sinazar`: el rótulo «sin azar añadido» bajo el micrófono
- «Cuanto más ruido añada la sala» → `ruido`: sube una traza magenta sobre el micrófono
- «más se separarán los dos lados» → `separan`: la igualdad se abre en «<» y la parábola se despega del eje
- «Y eso tiene una medida» → `medida`: entra un «?» sobre el hueco entre los dos lados

---

# Escena 10 — LaCoherencia

**Capítulo YouTube:** La coherencia

## Narración

<!-- b1 -->
Si dividimos la densidad cruzada entre la raíz del producto de las dos densidades, sale un número que nunca pasa de uno en módulo: la coherencia. Es exactamente lo que era rho en el capítulo siete, la covarianza dividida entre las desviaciones típicas, pero calculado en cada frecuencia. Un rho para cada frecuencia.

- «dividimos la densidad cruzada» → `cruzada`: aparece «γ_yx = D_yx» como numerador
- «la raíz del producto de las dos densidades» → `raiz`: debajo de la barra, «√(D_xx D_yy)»
- «nunca pasa de uno en módulo» → `menor1`: aparece «|γ| ≤ 1»
- «la coherencia» → `coh`: «γ_yx» se resalta en ámbar con el nombre «coherencia»
- «lo que era rho» → `rho`: al lado entra «ρ = σ_XY / (σ_X σ_Y)» del capítulo 7
- «la covarianza dividida» → `cov`: σ_XY sobre la barra se alinea con D_yx
- «las desviaciones típicas» → `desv`: σ_X σ_Y bajo la barra se alinea con √(D_xx D_yy)
- «en cada frecuencia» → `cadafreq`: la fórmula de γ se copia a varias posiciones de un eje ω
- «Un rho para cada frecuencia» → `unrho`: sobre el eje se dibuja una curva «ρ(ω)» entre 0 y 1

---

# Escena 11 — LaCoherenciaConNumeros

**Capítulo YouTube:** La coherencia con números

## Narración

<!-- b1 -->
Un ejemplo con números. Ahora el micrófono capta la voz más el ruido de la sala, que no tiene nada que ver con la voz. En una frecuencia, la voz tiene potencia tres y el ruido, uno. La cruzada solo recoge la voz: módulo tres. El micrófono tiene tres más uno, cuatro. Coherencia al cuadrado: tres al cuadrado entre tres por cuatro. Cero coma siete cinco.

- «el micrófono capta la voz más el ruido de la sala» → `mezcla`: corte seco; «y = voz + ruido» con la voz en azul y el ruido en magenta
- «no tiene nada que ver con la voz» → `indep`: entre voz y ruido, una «≠» y el rótulo «independientes»
- «la voz tiene potencia tres» → `voz3`: una barra azul de altura 3
- «y el ruido, uno» → `ruido1`: una barra magenta de altura 1
- «solo recoge la voz: módulo tres» → `cruz3`: aparece «|D_yx| = 3» y la barra azul se marca
- «El micrófono tiene» → `mictiene`: aparece «D_yy = ?» junto a las barras
- «tres más uno, cuatro» → `mic4`: las dos barras se apilan en una de altura 4 con «D_yy = 4»
- «tres al cuadrado entre tres por cuatro» → `cuenta`: se arma «|γ|² = 3² / (3 · 4)»
- «Cero coma siete cinco» → `res`: aparece «= 0,75»

<!-- b2 -->
En otra frecuencia, al revés: voz uno, ruido tres. Uno al cuadrado entre uno por cuatro: cero coma dos cinco. La coherencia al cuadrado es la fracción de lo que capta el micrófono que viene de la voz. En la primera frecuencia, el micrófono es casi todo voz; en la segunda, casi todo ruido.

- «al revés: voz uno, ruido tres» → `reves`: las barras cambian a azul 1 y magenta 3
- «Uno al cuadrado entre uno por cuatro» → `cuenta`: se arma «|γ|² = 1² / (1 · 4)»
- «cero coma dos cinco» → `res`: aparece «= 0,25»
- «la fracción de lo que capta el micrófono» → `fraccion`: la barra del micrófono se colorea por partes
- «que viene de la voz» → `viene`: el tramo azul se marca como «fracción»
- «En la primera frecuencia» → `primera`: vuelve la barra 3 + 1, casi toda azul, con «0,75»
- «en la segunda, casi todo ruido» → `segunda`: la barra 1 + 3, casi toda magenta, con «0,25»

---

# Escena 12 — DosVariablesPorFrecuencia

**Capítulo YouTube:** En cada frecuencia, dos variables

## Narración

<!-- b1 -->
Esta es la idea que se lleva el capítulo: en frecuencia, dos procesos se analizan, en cada frecuencia por separado, como dos variables aleatorias. Mismo rho, misma desigualdad, las mismas dos flechas con un ángulo. Y ya sabemos qué se hace con dos variables: estimar una a partir de la otra, proyectando una flecha sobre la otra.

- «la idea que se lleva el capítulo» → `idea`: corte seco; un marco ámbar con «la idea del capítulo»
- «dos procesos» → `procesos`: dos trazas, azul y cian
- «en cada frecuencia por separado» → `rebanadas`: el eje ω se parte en rebanadas verticales
- «dos variables aleatorias» → `variables`: en cada rebanada aparecen dos flechas con un ángulo
- «Mismo rho» → `rho`: junto a una rebanada, «ρ = cos θ»
- «misma desigualdad» → `desig`: junto a ella, «|ρ| ≤ 1»
- «las mismas dos flechas con un ángulo» → `flechas`: el ángulo θ entre las flechas se resalta, igual que en el capítulo 7
- «qué se hace con dos variables» → `quehace`: aparece «¿qué se hace?» junto a las flechas
- «estimar una a partir de la otra» → `estimar`: una flecha pasa a ser «dato» y la otra «lo que se quiere»
- «proyectando una flecha sobre la otra» → `proyecta`: se dibuja la proyección con el error perpendicular

---

# Escena 13 — ElColadorDeVuelta

**Capítulo YouTube:** El colador, otra vez

## Narración

<!-- b1 -->
Vuelve a la grabación del principio: la voz y el murmullo. Donde la coherencia es alta, fíate del micrófono y déjalo pasar. Donde es baja, atenúalo. Eso es casi el colador que buscábamos al empezar el capítulo. Pero antes de usar la coherencia, hay que saber estimarla sin engañarse.

- «la voz y el murmullo» → `vozmurmullo`: corte seco; vuelve la persona azul con el murmullo magenta, como en el E1
- «Donde la coherencia es alta» → `alta`: un eje ω con la curva ρ(ω); una zona alta se marca en verde
- «déjalo pasar» → `pasa`: en esa zona el colador se abre y pasa la barra
- «Donde es baja» → `baja`: otra zona baja de la curva se marca en rojo
- «atenúalo» → `atenua`: en esa zona el colador se cierra y la barra se encoge
- «el colador que buscábamos» → `colador`: el colador completo, con una ganancia que cambia de forma frecuencia a frecuencia
- «Pero antes de usar la coherencia» → `antes`: el colador se atenúa y aparece «¿y si la coherencia miente?»
- «estimarla sin engañarse» → `estimar`: entra una lupa con un «?» sobre la curva

---

# Escena 14 — LaTrampaDeUnSoloTrozo

**Capítulo YouTube:** La trampa de un solo trozo

## Narración

<!-- b1 -->
La coherencia se estima igual que la densidad espectral: partiendo en trozos y promediando. Pero tiene una trampa. Toma dos grabaciones que no tienen absolutamente nada que ver. Estima su coherencia con un solo trozo. ¿Qué sale: cero, cero coma cinco, o uno? Piénsalo.

- «partiendo en trozos y promediando» → `trozos`: corte seco; un registro partido en trozos que se promedian
- «una trampa» → `trampa`: un triángulo de aviso sobre el dibujo
- «dos grabaciones» → `dos`: dos ruidos distintos, uno sobre otro
- «nada que ver» → `sinrel`: el rótulo «sin relación» entre ambos
- «con un solo trozo» → `uno`: un único trozo de cada grabación queda enmarcado
- «¿Qué sale» → `encuesta`: tres opciones en pantalla: «0», «0,5» y «1»
- «cero, cero coma cinco, o uno» → `opciones`: las tres opciones se encienden una a una
- «Piénsalo» → `piensa`: un contador de pausa de unos segundos bajo las opciones

---

# Escena 15 — SaleUnoSiempre

**Capítulo YouTube:** Sale uno, siempre

## Narración

<!-- b1 -->
Sale uno. Siempre. Con un solo trozo, en cada frecuencia hay un número complejo para cada señal; pongamos que sus módulos son tres y cuatro. Arriba, el módulo del producto: doce. Abajo, la raíz de nueve por dieciséis: doce. Doce entre doce, uno. Con cualquier otro par de números pasa lo mismo: arriba y abajo es el mismo número.

- «Sale uno» → `uno`: la opción «1» se enciende en rojo, las otras se apagan
- «Siempre» → `siempre`: el «1» rojo tiembla, insistente
- «Con un solo trozo» → `trozo`: un trozo enmarcado de cada señal
- «un número complejo para cada señal» → `complejos`: aparecen dos flechas, «X» para una señal y «Y» para la otra
- «sus módulos son tres y cuatro» → `mod`: «|X| = 3» y «|Y| = 4»
- «Arriba, el módulo del producto: doce» → `arriba`: se arma el numerador «|X · Y*| = 12»
- «Abajo, la raíz de nueve por dieciséis: doce» → `abajo`: se arma el denominador «√(9 · 16) = 12»
- «Doce entre doce, uno» → `uno12`: «12 / 12 = 1» en grande
- «cualquier otro par de números» → `otro`: los números cambian, por ejemplo «2» y «5», y el resultado vuelve a ser 1
- «es el mismo número» → `igual`: numerador y denominador unidos por un signo «=»

<!-- b2 -->
No es un resultado experimental, es una identidad: da uno aunque las señales no tengan ninguna relación. Es la misma trampa que un rho calculado con dos puntos, que siempre vale uno o menos uno, porque por dos puntos siempre pasa una recta. Otra vez: mira la nube antes que el número.

- «una identidad» → `identidad`: el «=» del paso anterior se convierte en «≡»
- «aunque las señales no tengan ninguna relación» → `sinrel`: vuelve el rótulo «sin relación» sobre el «1»
- «Es la misma trampa» → `trampa`: vuelve el triángulo de aviso
- «un rho calculado con dos puntos» → `dospuntos`: corte seco; dos puntos sueltos en un plano
- «siempre vale uno o menos uno» → `pm1`: aparece «ρ = ±1»
- «por dos puntos siempre pasa una recta» → `recta`: se traza la recta por los dos puntos
- «Otra vez» → `otra`: el triángulo de aviso parpadea
- «mira la nube antes que el número» → `nube`: se suma una nube de puntos bajo la recta, con un ojo

---

# Escena 16 — PromediarLoArreglaDespacio

**Capítulo YouTube:** Promediar lo arregla, despacio

## Narración

<!-- b1 -->
Promediar lo arregla, pero despacio. Con dos grabaciones sin relación, la coherencia al cuadrado estimada con eme trozos sale, en promedio, uno sobre eme. Con ocho trozos, cero coma uno dos: parece que hay algo, y no hay nada. La regla: solo creer coherencias bastante mayores que uno sobre eme, y con menos de unos diez trozos, no creer ninguna.

- «Promediar lo arregla» → `promediar`: corte seco; varios trozos que se promedian en una curva
- «pero despacio» → `despacio`: una flecha hacia abajo muy lenta sobre la curva
- «Con dos grabaciones sin relación» → `dos`: dos trazas con el rótulo «sin relación»
- «la coherencia al cuadrado estimada» → `cuadrado`: aparece «|γ|²» con un sombrerito de estimación
- «eme trozos» → `mtrozos`: aparece «M trozos»
- «uno sobre eme» → `unosobre`: se arma «|γ|² ≈ 1/M» y empieza una tabla con «M = 1 → 1» y «M = 2 → 0,5»
- «Con ocho trozos, cero coma uno dos» → `ocho`: la tabla suma «M = 8 → 0,12» y «M = 64 → 0,016», y la fila del 8 se resalta
- «parece que hay algo» → `algo`: una barra pequeña de 0,12 sobre el eje, con un signo «?»
- «y no hay nada» → `nada`: junto a ella, el rótulo «sin relación» tacha el «?»
- «La regla» → `regla`: entra un marco «la regla»
- «bastante mayores que uno sobre eme» → `mayores`: un umbral «1/M» y solo se acepta lo que queda por encima
- «con menos de unos diez trozos» → `diez`: se marca «M < 10»
- «no creer ninguna» → `ninguna`: «M < 10: no reportar» con un sello de prohibido

---

# Escena 17 — LasHerramientasDelCapitulo

**Capítulo YouTube:** Las herramientas del capítulo

## Narración

<!-- b1 -->
Con esto el capítulo tiene todas sus herramientas: un espectro para cada proceso, uno cruzado para cada pareja, y una forma honesta de medirlos. Y en cada frecuencia, dos procesos son dos variables. Separar la voz del murmullo es, entonces, estimar una variable a partir de otra, frecuencia por frecuencia.

- «todas sus herramientas» → `herr`: corte seco; un tablero vacío con el título «el capítulo 11»
- «un espectro para cada proceso» → `espectro`: aparece una curva ámbar «S_xx(jω)»
- «uno cruzado para cada pareja» → `cruzado`: aparece «S_yx(jω)» con su flecha compleja
- «una forma honesta de medirlos» → `honesta`: aparece «trozos + promedio» con un tilde
- «Y en cada frecuencia» → `encada`: la curva y la flecha se cortan en rebanadas verticales
- «dos procesos son dos variables» → `variables`: las dos flechas con ángulo de la escena 12
- «Separar la voz del murmullo» → `separar`: vuelven la voz azul y el murmullo magenta con el colador
- «estimar una variable a partir de otra» → `estimar`: la proyección de una flecha sobre la otra
- «frecuencia por frecuencia» → `fxf`: la ganancia del colador cambia de forma a lo largo del eje ω

---

# Escena 18 — Cierre

**Capítulo YouTube:** Lo que viene: ¿cuál es el mejor filtro?

## Narración

<!-- b1 -->
Repasemos el capítulo: la densidad espectral dice dónde vive la potencia, la cruzada dice cuánto comparten dos señales, y la coherencia es un rho por frecuencia. Queda la pregunta de fondo. En el próximo capítulo: ¿cuál es el mejor filtro?

- «la densidad espectral» → `psd`: aparece la curva ámbar S_xx(jω)
- «dónde vive la potencia» → `donde`: una banda bajo la curva se sombrea
- «la cruzada» → `cruzada`: a su lado aparece la flecha compleja de S_yx(jω)
- «cuánto comparten dos señales» → `comparten`: la flecha se rotula con «módulo = cuánto comparten»
- «la coherencia» → `coh`: aparece «γ_yx» en ámbar
- «un rho por frecuencia» → `rho`: la curva ρ(ω) se dibuja sobre el eje ω
- «la pregunta de fondo» → `pregunta`: entra el colador con un «?» en su ganancia
- «cuál es el mejor filtro» → `titulo_c12`: entra el título del capítulo siguiente, «¿Cuál es el mejor filtro?»
