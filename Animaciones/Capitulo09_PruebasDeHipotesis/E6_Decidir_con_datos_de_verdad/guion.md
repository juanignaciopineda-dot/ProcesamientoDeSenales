# Episodio 6 — Decidir con datos de verdad

Capítulo 9 (Pruebas de hipótesis), episodio 6 de 6. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 24 a 28), más un gancho y un cierre nuevos.

**Estado:** Render final 1080p60 hecho (9:08, 0 avisos). **No se pudo subir el 19/10/2026: YouTube dio «límite diario de subida alcanzado».** El mp4, el `.srt` y `capitulos.txt` siguen en `salida/` para subirlo otro día (título: «Curva ROC con datos y área bajo la curva (AUC) - Ep 6 Decidir con datos de verdad»). Después, limpiar `salida/`.
animadas (piezas en `comun/figuras_c9e6.py`). Borrador 480p15 de **9:09 con 0
avisos**, hojas de contacto revisadas y correcciones re-renderizadas (tamaños y
solapes; en las escenas 03 y 04, una ficha y un tramo por palabra). «Curva ROC»
se dice /ˈrok/ (variante 4 de `voces_prueba/probar_roc.py`, en
`comun/pronunciacion.py`). Borrador aprobado por el usuario y **render final 1080p60 hecho** (9:08, 0
avisos). Falta subirlo a YouTube y limpiar residuos (paso 17).

Texto nuevo (marcado con ⭐, **aprobado**):
- ⭐ Escena 01 (gancho): «Pruebas un detector mil veces y no da ni una sola
  falsa alarma. ¿Puedes decir que nunca se equivoca? Uno que se equivoca poco
  más de una vez de cada mil te daría ese mismo resultado una de cada cuatro
  veces.»
- ⭐ Escena 02 (título): «Decidir con datos de verdad».
- ⭐ Escena 13 (cierre): resumen corto (la escalera, el área que mide el orden,
  ordenar no es cortar, cero errores vistos no es error cero), cierra el
  capítulo y anuncia el E1 del capítulo 10 por su título, «Mil grabaciones del
  mismo ruido».

Notas:
- El cierre del E5 ya anuncia este título («Lo veremos en el próximo episodio:
  decidir con datos de verdad») y termina con las campanas desvaneciéndose y
  una lista de casos «+» y «−». La escena 03 arranca desde ahí.
- El gancho adelanta la sorpresa de la escena 11 (26 % de no ver ninguna falsa
  alarma con el umbral en 3 voltios); la escena 11 la paga con la cuenta.
- Reparto de las escenas del guion base: 24 → escenas 03 y 04; 25 → 05 y 06;
  26 → 07, 08 y 09; 27 → 10 y 11; 28 → 12. Solo se partieron bloques enteros:
  el texto del guion base no cambia.
- Largo: ~1.160 palabras del guion base más ~120 de gancho, título y cierre
  ≈ 1.280 palabras; voz medida de 8:51 (~9:10 con los respiros). No hace falta
  recortar nada.
- Números (recomprobados con Python): los ocho casos «+ + − + − + − −», área
  13/16 = 0,81 (alturas de las columnas 2/4, 3/4, 1, 1; positivos por encima
  de cada negativo 2, 3, 4, 4); área de las dos campanas 0,92; error típico
  √(p(1 − p)/N) con p = 0,159: 0,037 con N = 100 y 0,004 con N = 10.000;
  umbral en 3: falsa alarma 0,00135, en mil pruebas ninguna con probabilidad
  0,26 (Poisson de media 1,35: 0 → 26 %, 1 → 35 %, 2 → 24 %, 3 → 11 %, 4+ → 5 %);
  diez sucesos → 10 / 0,00135 ≈ 7.400 pruebas.
- Puntuaciones de los ocho casos (inventadas, todas distintas, de mayor a
  menor): 0,95 (+), 0,85 (+), 0,75 (−), 0,65 (+), 0,55 (−), 0,40 (+),
  0,30 (−), 0,15 (−). Al cuadrado: 0,90 · 0,72 · 0,56 · 0,42 · 0,30 · 0,16 ·
  0,09 · 0,02 (mismo orden).
- Referencias a episodios anteriores dentro de la narración: el punto de
  pendiente uno (E4, escena 19 del guion base), Neyman-Pearson y riesgo mínimo
  (E3 y E5), el cero coma ciento cincuenta y nueve (E2), los grandes números
  («el promedio del capítulo siete»). Se dicen sin número de episodio.
- Disposición y colores, como en E4: **plano de la ROC a la derecha** (ejes
  «Falsa alarma» y «Detección», de 0 a 1, con la diagonal punteada en `INK`), la
  curva o la escalera en `ESTIMACION` (ámbar). Fichas: positivos «+» en `SENAL`
  (azul), negativos «−» en `RUIDO` (magenta). El umbral es una línea horizontal
  ámbar. Las campanas de siempre (`dens3`, centros 0 y 2, desvío 1), los fallos y
  falsas alarmas en `ERROR`, aciertos en `VERDE`.
- Piezas nuevas (módulo aparte `comun/figuras_c9e6.py`, como los otros episodios del capítulo): la ficha
  (rectángulo redondeado con signo y puntuación), la tira de ocho fichas, la
  escalera de la ROC empírica (camino de pasos de ¼ que se va dibujando, con
  sus columnas sombreables), el contador «Fallos / Pruebas» y el histograma de
  falsas alarmas en mil pruebas.

---

# Escena 01 — Gancho

**Capítulo YouTube:** Mil pruebas sin una falsa alarma

## Narración

<!-- b1 -->
Pruebas un detector mil veces y no da ni una sola falsa alarma. ¿Puedes decir
que nunca se equivoca? Uno que se equivoca poco más de una vez de cada mil te
daría ese mismo resultado una de cada cuatro veces.

- «Pruebas un detector» → `detector`: una caja «Detector» al centro, con una luz apagada
- «mil veces» → `mil`: una rejilla de mil puntos grises se llena deprisa detrás de la caja; contador «1.000 pruebas»
- «ni una sola falsa alarma» → `cero`: rótulo «Falsas alarmas: 0» en verde, con un tic
- «¿Puedes decir» → `pregunta`: el rótulo verde se ilumina con un «?» ámbar al lado
- «que nunca se equivoca?» → `nunca`: debajo entra «Error = 0» con un «?»
- «Uno que se equivoca» → `otro`: corte; la caja se vuelve «Detector» con «1 de cada 740» en rojo pequeño
- «una vez de cada mil» → `fa`: rótulo «Falsa alarma ≈ 0,00135»
- «ese mismo resultado» → `mismo`: vuelve «Falsas alarmas: 0» junto a la caja
- «una de cada cuatro veces» → `cuatro`: cuatro copias pequeñas de la rejilla; una se enciende en ámbar con «26 %»

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Decidir con datos de verdad

## Narración

<!-- b1 -->
Decidir con datos de verdad.

- «Decidir» → `t1`: «Decidir» entra con rebote
- «con datos de verdad» → `t2`: «con datos de verdad» entra debajo, con la etiqueta «Capítulo 9 · Pruebas de hipótesis»

---

# Escena 03 — OchoCasos

**Capítulo YouTube:** Casos resueltos y una puntuación
**Objetivo:** pasar de las densidades conocidas a casos etiquetados con una
puntuación, y ordenarlos de mayor a menor.

## Narración

<!-- b1 -->
En la práctica no conoces las densidades. Lo que tienes son casos ya
resueltos, de los que sabes la verdad, y un detector que le pone a cada uno una
puntuación: cuanto más alta, más parece hache uno. Puede ser un análisis, un
filtro de correo basura o un programa que busca tumores en radiografías.

- «no conoces las densidades» → `densidades`: las dos campanas de siempre (`dens3`) entran y se vuelven punteadas con un «?» encima
- «Lo que tienes» → `tienes`: las campanas se apartan a la izquierda y se atenúan
- «casos ya resueltos» → `casos`: las campanas se deshacen en puntos sueltos que caen a una fila de fichas grises
- «sabes la verdad» → `verdad`: cada ficha se marca: «+» azul o «−» magenta
- «un detector» → `detector`: la caja «Detector» encima de la fila
- «una puntuación» → `punt`: cada ficha recibe su número (0,95 · 0,30 · 0,65…), en orden revuelto
- «más parece hache uno» → `h1`: una flecha vertical a la derecha, «Más alta → Más parece H₁»
- «un análisis» → `analisis`: a la izquierda, un tubo de ensayo pequeño
- «correo basura» → `correo`: un sobre pequeño con una cruz
- «tumores en radiografías» → `radio`: un rectángulo de radiografía con una mancha clara

<!-- b2 -->
Tomemos ocho casos: cuatro positivos y cuatro negativos. Los ordenamos de
mayor a menor puntuación. Queda así: positivo, positivo, negativo, positivo,
negativo, positivo, negativo, negativo. No está perfecto: hay negativos
colados entre los positivos.

- «ocho casos» → `ocho`: los íconos salen; quedan ocho fichas en fila
- «cuatro positivos» → `pos`: los cuatro «+» laten en azul; rótulo «4 +»
- «cuatro negativos» → `neg`: los cuatro «−» laten en magenta; rótulo «4 −»
- «Los ordenamos» → `ordenar`: las fichas se reordenan en una columna vertical, de 0,95 arriba a 0,15 abajo
- «Queda así» → `queda`: un cursor ámbar se pone junto a la ficha de arriba
- «positivo, positivo, negativo, positivo» → `f1`: el cursor junto a la ficha 1 (+, 0,95), que se enciende
- «positivo, negativo, positivo, negativo, positivo» → `f2`: el cursor baja a la ficha 2 (+)
- «negativo, positivo, negativo, positivo» → `f3`: ficha 3 (−)
- «positivo, negativo, positivo, negativo, negativo» → `f4`: ficha 4 (+)
- «negativo, positivo, negativo, negativo» → `f5`: ficha 5 (−)
- «positivo, negativo, negativo» → `f6`: ficha 6 (+)
- «negativo, negativo.» → `f7`: ficha 7 (−)
- «negativo.» → `f8`: ficha 8 (−); a la derecha, la tira «+ + − + − + − −»
- «No está perfecto» → `imperfecto`: la tira ideal «+ + + + − − − −» aparece pequeña al lado, atenuada
- «negativos colados» → `colados`: los «−» de las posiciones 3 y 5 se rodean en rojo
- «entre los positivos» → `entre`: los «+» de las posiciones 4 y 6, debajo de ellos, laten

---

# Escena 04 — LaEscalera

**Capítulo YouTube:** La curva ROC con datos
**Objetivo:** bajar el umbral caso a caso y dibujar la escalera; ver que se
afina con más casos y avisar de sus dos limitaciones.

## Narración

<!-- b1 -->
Ahora bajamos el umbral desde arriba, caso a caso. Cada vez que un positivo
queda por encima del umbral, la detección sube un cuarto: un escalón hacia
arriba. Cada vez que queda un negativo, la falsa alarma sube un cuarto: un
escalón hacia la derecha.

- «bajamos el umbral» → `umbral`: la columna de fichas a la izquierda; una línea ámbar horizontal por encima de la primera
- «caso a caso» → `plano`: a la derecha, el plano de la ROC vacío con la diagonal punteada y un punto en (0, 0)
- «un positivo» → `pos1`: el umbral baja bajo la ficha 1 (+), que queda por encima y se enciende
- «la detección sube un cuarto» → `sube`: el punto sube a (0, ¼); en el eje vertical, «¼»
- «un escalón hacia arriba» → `arriba`: el tramo vertical queda dibujado en ámbar con una flecha «↑»
- «queda un negativo» → `neg1`: muestra fija: una ficha «−» suelta, al lado del umbral, se enciende en magenta
- «la falsa alarma sube un cuarto» → `derecha`: en el plano, una flecha corta «→ ¼» punteada, todavía sin recorrer
- «hacia la derecha» → `regla`: debajo del plano, la regla «+ → ↑ ¼ · − → → ¼»

<!-- b2 -->
El camino es: arriba, arriba, derecha, arriba, derecha, arriba, derecha,
derecha. Una escalera que va de una esquina a la otra. Es la curva ROC medida
con datos. Con ocho casos los escalones son enormes; con miles, la escalera se
confunde con la curva suave.

- «El camino es» → `p0`: la flecha punteada se borra; el primer escalón sigue en el plano
- «arriba, arriba,» → `p1`: el primer tramo (ya dibujado) late
- «arriba, derecha, arriba, derecha, arriba» → `p2`: el umbral baja bajo la ficha 2; tramo hacia arriba
- «derecha, arriba, derecha, arriba» → `p3`: ficha 3; tramo a la derecha
- «arriba, derecha, arriba, derecha, derecha» → `p4`: ficha 4; arriba
- «derecha, arriba, derecha, derecha» → `p5`: ficha 5; derecha
- «arriba, derecha, derecha» → `p6`: ficha 6; arriba
- «derecha, derecha.» → `p7`: ficha 7; derecha
- «derecha.» → `p8`: ficha 8; derecha: el camino llega a (1, 1)
- «de una esquina a la otra» → `esquinas`: las esquinas (0, 0) y (1, 1) laten
- «la curva ROC medida» → `roc`: rótulo «ROC empírica» en ámbar
- «Con ocho casos» → `ocho`: «8 casos» junto a la escalera
- «los escalones son enormes» → `enormes`: los escalones laten, uno tras otro
- «con miles» → `miles`: la escalera se rehace con 80 casos y después con 8.000; el rótulo cambia a «80» y «8.000»
- «la curva suave» → `suave`: encima, punteada, la curva suave de las dos campanas; casi coinciden

<!-- b3 -->
Dos avisos. Con pocos casos de un tipo, la curva es un dibujo tosco, y no hay
que fiarse de sus detalles. Y si la mides con los mismos datos con los que
ajustaste el detector, sale mejor de lo que es. Hay que medirla con datos que
el detector no haya visto.

- «Dos avisos» → `avisos`: vuelve la escalera de 8 casos; un triángulo de aviso ámbar arriba a la izquierda
- «pocos casos de un tipo» → `pocos`: tarjeta «Pocos casos: Dibujo tosco»
- «no hay que fiarse de sus detalles» → `detalles`: una lupa sobre un escalón, con un «?»
- «Y si la mides» → `mides`: una regla pequeña se apoya en la escalera
- «los mismos datos» → `mismos`: dos montones de fichas, «Ajustar» y «Medir», con las mismas fichas
- «ajustaste el detector» → `ajustar`: una flecha del montón «Ajustar» a la caja «Detector»
- «sale mejor de lo que es» → `optimista`: la escalera se infla hacia la esquina de arriba; tarjeta «Optimista»
- «datos que el detector no haya visto» → `nuevos`: el montón «Medir» se cambia por fichas nuevas; la escalera vuelve a su sitio, con un tic verde

---

# Escena 05 — ElAreaDeLaEscalera

**Capítulo YouTube:** El área bajo la curva
**Objetivo:** resumir la curva en su área, con las dos referencias (un medio y
uno), y calcularla en la escalera: 13/16.

## Narración

<!-- b1 -->
A veces se quiere resumir toda la curva en un solo número. El más usado es el
área que queda debajo. Para la diagonal, el detector que tira una moneda, el
área es un medio. Para el detector perfecto, uno.

- «resumir toda la curva» → `curva`: el plano al centro, con la curva suave de las campanas en ámbar
- «en un solo número» → `numero`: al lado, una casilla vacía «= ?»
- «el área que queda debajo» → `area`: el área bajo la curva se rellena de ámbar translúcido; rótulo «AUC»
- «Para la diagonal» → `diagonal`: la curva se atenúa; la diagonal se ilumina y se rellena el triángulo de debajo
- «tira una moneda» → `moneda`: una moneda pequeña gira junto a la diagonal
- «el área es un medio» → `medio`: «Área = 0,5»
- «el detector perfecto» → `perfecto`: el camino (0, 0) → (0, 1) → (1, 1) en verde y el cuadrado entero relleno
- «uno.» → `uno`: «Área = 1»; las dos referencias quedan como marcas en una regla de 0,5 a 1

<!-- b2 -->
Calculémosla en nuestra escalera. Son cuatro columnas de un cuarto de ancho.
Sus alturas: dos cuartos, tres cuartos, uno y uno. Sumamos y dividimos entre
cuatro: trece dieciseisavos. Cero coma ochenta y uno.

- «nuestra escalera» → `escalera`: corte; la escalera de los ocho casos en el plano
- «cuatro columnas» → `columnas`: debajo de la escalera aparecen cuatro columnas separadas por líneas finas
- «un cuarto de ancho» → `ancho`: una llave bajo la primera, «¼»
- «dos cuartos» → `c1`: la columna 1 se rellena; «2/4» encima
- «tres cuartos» → `c2`: la columna 2; «3/4»
- «uno y uno» → `c34`: las columnas 3 y 4; «1» y «1»
- «Sumamos y dividimos» → `suma`: debajo, «(2/4 + 3/4 + 1 + 1) / 4», pieza a pieza
- «trece dieciseisavos» → `trece`: «= 13/16»
- «Cero coma ochenta y uno» → `ochentayuno`: «= 0,81»; la marca 0,81 cae en la regla, entre 0,5 y 1

---

# Escena 06 — ContarParejas

**Capítulo YouTube:** Qué significa el área
**Objetivo:** descubrir que el área es la probabilidad de que un positivo al
azar puntúe más que un negativo al azar (13 de 16 parejas), y avisar de lo que
no dice.

## Narración

<!-- b1 -->
Ese número significa algo muy concreto. Toma un positivo al azar y un negativo
al azar: es la probabilidad de que el positivo tenga más puntuación.
Comprobémoslo. Hay dieciséis parejas. El primer negativo tiene dos positivos
por encima. El segundo, tres. Los otros dos, cuatro cada uno. Trece de
dieciséis. El mismo número.

- «Ese número» → `numero`: «0,81» se encoge arriba a la derecha
- «algo muy concreto» → `concreto`: el «0,81» late; debajo, dos montones: uno de «+» y uno de «−»
- «un positivo al azar» → `pos`: del montón de «+» sale una ficha
- «un negativo al azar» → `neg`: sale una ficha «−»; las dos quedan lado a lado
- «el positivo tenga más puntuación» → `compara`: entre ellas «>»; rótulo «P(Positivo > Negativo)»
- «Comprobémoslo» → `tira`: la columna de los ocho casos al centro
- «dieciséis parejas» → `parejas`: una cuadrícula 4 × 4 al lado: filas los «+», columnas los «−»
- «El primer negativo» → `n1`: el «−» de la posición 3 se resalta; dos líneas lo unen con los «+» de arriba
- «dos positivos» → `dos`: bajo esa columna de la cuadrícula, dos casillas verdes; número «2»
- «El segundo, tres» → `n2`: el «−» de la posición 5; tres líneas; «3»
- «Los otros dos» → `otros`: los dos últimos «−» se resaltan
- «cuatro cada uno» → `n34`: cuatro líneas a cada uno; «4» y «4»
- «Trece de» → `trece`: «2 + 3 + 4 + 4 = 13»; la cuadrícula queda con 13 casillas verdes y 3 rojas
- «El mismo número» → `mismo`: «13/16» junto al «0,81» de arriba, unidos por un «=» verde

<!-- b2 -->
Así que el área mide lo bien que el detector ordena: que ponga los positivos
por delante de los negativos. Para nuestras dos campanas, separadas dos
desvíos, vale cero coma noventa y dos.

- «el área mide» → `mide`: tarjeta «Área = Lo bien que ordena»
- «los positivos por delante» → `delante`: la tira ideal «+ + + + − − − −» entra debajo
- «de los negativos» → `detras`: los «−» de la tira ideal se agrupan al final, atenuados
- «nuestras dos campanas» → `campanas`: corte; las dos campanas de siempre a la izquierda y su curva ROC suave a la derecha
- «separadas dos desvíos» → `desvios`: una llave entre los centros 0 y 2: «2 desvíos»
- «cero coma noventa y dos» → `noventaydos`: el área bajo la curva se rellena; «Área = 0,92»

<!-- b3 -->
Pero cuidado con lo que no dice. Es un promedio sobre todos los umbrales,
también los que nunca vas a usar. Dos detectores con la misma área pueden ser
muy distintos en la zona de un uno por ciento de falsas alarmas, que quizá es
la única que te importa. Y el área tampoco te dice dónde poner el umbral.

- «cuidado con lo que no dice» → `cuidado`: triángulo de aviso ámbar
- «Es un promedio» → `promedio`: vuelve la curva de las campanas con su área; rótulo «Promedio»
- «todos los umbrales» → `todos`: un punto recorre la curva entera de una esquina a la otra
- «los que nunca vas a usar» → `nunca`: el tramo de la derecha (falsa alarma > 0,5) se atenúa
- «Dos detectores» → `dos`: corte; dos curvas en el mismo plano, una azul y una cian, que se cruzan
- «la misma área» → `misma`: «Área = 0,85» bajo cada una
- «muy distintos» → `distintos`: las dos curvas laten, una tras otra
- «un uno por ciento» → `uno`: un recuadro ampliado en la zona de falsa alarma 0 a 0,01; dentro, la curva azul muy arriba y la cian muy abajo, con una flecha de doble punta
- «la única que te importa» → `importa`: el recuadro se ilumina en ámbar
- «Y el área tampoco» → `tampoco`: el recuadro se apaga; vuelve el área rellena
- «dónde poner el umbral» → `donde`: un «?» ámbar sobre la curva; tarjeta «Área ≠ Umbral»

---

# Escena 07 — SoloElOrden

**Capítulo YouTube:** La curva solo ve el orden
**Objetivo:** separar ordenar bien de lo que significa el número: al elevar las
puntuaciones al cuadrado, la curva y el área no cambian.

## Narración

<!-- b1 -->
En una puntuación hay dos cosas distintas, y conviene separarlas. Una es que
ordene bien: los positivos, por encima. La otra es qué significa el número.

- «En una puntuación» → `ficha`: una ficha grande «0,65» al centro
- «dos cosas distintas» → `dos`: la ficha se parte en dos tarjetas
- «conviene separarlas» → `separar`: las dos tarjetas se apartan, una a cada lado
- «ordene bien» → `orden`: tarjeta izquierda «Orden», con la columna de los ocho casos en pequeño
- «los positivos, por encima» → `encima`: en la columna pequeña, los «+» laten hacia arriba
- «La otra» → `otra`: la tarjeta derecha se ilumina
- «qué significa el número» → `significa`: en ella, «Significado», con «0,65 = ?»

<!-- b2 -->
Haz un experimento: eleva todas las puntuaciones al cuadrado. Los números
cambian, pero el orden no. La escalera es idéntica, y el área también. La curva
ROC solo ve el orden.

- «Haz un experimento» → `exp`: corte; la columna de ocho fichas a la izquierda y su escalera a la derecha
- «al cuadrado» → `cuadrado`: «x²» ámbar sobre la columna
- «Los números cambian» → `cambian`: cada puntuación se transforma: 0,95 → 0,90, 0,85 → 0,72… hasta 0,15 → 0,02
- «el orden no» → `orden`: los signos «+ + − + − + − −» laten sin moverse
- «La escalera es idéntica» → `identica`: una copia de la escalera se superpone exacta a la anterior
- «y el área también» → `area`: «13/16» y «13/16», con un «=» verde
- «solo ve el orden» → `solo`: tarjeta «Mismo orden = Misma curva»

---

# Escena 08 — EstarCalibrado

**Capítulo YouTube:** Cortar en cero coma cinco
**Objetivo:** ver que cortar en 0,5 solo es el máximo a posteriori si la
puntuación está calibrada, y que un área alta no lo garantiza.

## Narración

<!-- b1 -->
Ahora, muchos detectores modernos entregan un número entre cero y uno y lo
llaman probabilidad. Y casi todo el mundo corta en cero coma cinco. Eso solo es
la regla del máximo a posteriori si el número es de verdad la probabilidad a
posteriori: si, de todos los casos que reciben un cero coma siete, el setenta
por ciento son positivos. A eso se le llama estar calibrado.

- «muchos detectores modernos» → `detector`: la caja «Detector» con una salida
- «entre cero y uno» → `regla`: sale una regla horizontal de 0 a 1 con una marca en «0,7»
- «lo llaman probabilidad» → `prob`: sobre la marca, «Probabilidad» entre comillas
- «corta en cero coma cinco» → `corte`: una línea ámbar en 0,5 con la etiqueta «Por defecto»
- «la regla del máximo a posteriori» → `map`: debajo, «MAP: P(H₁ | r) > 0,5»
- «de verdad la probabilidad a posteriori» → `deverdad`: la palabra «Probabilidad» pierde las comillas y se subraya
- «de todos los casos» → `todos`: una rejilla de cien casos grises
- «reciben un cero coma siete» → `cien`: sobre la rejilla, «Puntuación 0,7»
- «el setenta por ciento son positivos» → `setenta`: setenta casillas se vuelven «+» azules y treinta «−» magenta; «70 de 100»
- «A eso se le llama» → `llama`: una llave abraza la rejilla y la regla
- «estar calibrado» → `calibrado`: tarjeta verde «Calibrado» sobre la rejilla

<!-- b2 -->
Un detector puede ordenar perfectamente y estar mal calibrado. Entonces su
cero coma cinco cae en un punto cualquiera de la curva. Un área alta dice que
ordena bien. No dice que cero coma cinco sea el sitio donde cortar.

- «ordenar perfectamente» → `ordena`: al lado, otra rejilla de cien con «0,7»; tic verde «Ordena bien»
- «mal calibrado» → `mal`: solo cuarenta casillas son «+»; tarjeta roja «Mal calibrado: 40 de 100»
- «su cero coma cinco» → `punto`: corte; la curva ROC suave y un punto ámbar «0,5»
- «un punto cualquiera» → `cualquiera`: el punto resbala por la curva y se para lejos de donde estaba
- «Un área alta» → `area`: el área se rellena; «Área alta» con un tic
- «ordena bien» → `bien`: el tic se vuelve verde
- «No dice que» → `nodice`: el punto «0,5» vuelve a latir
- «el sitio donde cortar» → `cortar`: sobre el punto «0,5», un «?» rojo; tarjeta «Área alta ≠ Buen corte»

---

# Escena 09 — UmbralSinSupuestos

**Capítulo YouTube:** No hay umbral sin supuestos
**Objetivo:** elegir el umbral con un criterio explícito, y ver que el punto más
lejos de la diagonal supone a priori y costes iguales.

## Narración

<!-- b1 -->
El umbral se elige con un criterio explícito. Si tienes un tope de falsas
alarmas, Neyman-Pearson. Si tienes costes, riesgo mínimo. ¿Y si no tienes nada?
Se suele tomar el punto de la curva más alejado de la diagonal.

- «con un criterio explícito» → `criterio`: «Criterio» en ámbar arriba; la curva ROC a la derecha
- «un tope de falsas alarmas» → `tope`: tarjeta «Cota de falsas alarmas → Neyman-Pearson»; en la curva, una línea vertical en 0,05
- «Neyman-Pearson» → `np`: el nombre de la tarjeta se ilumina; su punto se marca en la curva
- «tienes costes» → `costes`: tarjeta «Costes → Riesgo mínimo»; su punto en la curva
- «¿Y si no tienes nada?» → `nada`: tarjeta «Nada → ?» con el «?» latiendo
- «Se suele tomar» → `suele`: un punto ámbar recorre la curva despacio
- «más alejado de la diagonal» → `lejos`: una línea punteada mide la distancia de la curva a la diagonal y crece hasta su máximo; el «?» se cambia por «El punto más lejos de la diagonal»

<!-- b2 -->
Pero ese punto ya lo conocemos: es donde la pendiente vale uno. Elegirlo es
suponer, sin decirlo, que las dos hipótesis son igual de probables y que los
dos errores cuestan lo mismo. No existe un umbral sin supuestos. Solo hay
supuestos que se dicen y supuestos que no.

- «ese punto ya lo conocemos» → `conocemos`: el punto más lejano se ilumina
- «la pendiente vale uno» → `pendiente`: la recta tangente en ese punto, paralela a la diagonal; «Pendiente = 1»
- «Elegirlo es suponer» → `suponer`: la tercera tarjeta se agranda
- «sin decirlo» → `letra`: bajo la tercera tarjeta, en letra pequeña, «Supone:»
- «igual de probables» → `priori`: «p₀ = p₁»
- «cuestan lo mismo» → `costes_iguales`: «Coste FA = Coste fallo»; η = 1 en ámbar
- «sin supuestos» → `sin`: tarjeta «Umbral sin supuestos» que se tacha en rojo
- «supuestos que se dicen» → `dicen`: dos tarjetas: «Supuestos dichos» con tic verde
- «supuestos que no» → `no`: «Supuestos callados», atenuada y con un «?»

---

# Escena 10 — MedirContando

**Capítulo YouTube:** ¿Cuántas pruebas hacen falta?
**Objetivo:** ver que una probabilidad de error medida contando tiene su propio
error, raíz de p(1 − p)/N, y que diez veces más precisión cuesta cien veces más
pruebas.

## Narración

<!-- b1 -->
Una última cuestión práctica. Las probabilidades de error se miden contando: se
hacen muchas pruebas y se mira cuántas salen mal. Es el promedio del capítulo
siete: al crecer el número de pruebas, la fracción de fallos se acerca a la
probabilidad real. La pregunta es cuántas pruebas hacen falta.

- «Una última cuestión práctica» → `practica`: corte; las campanas con el umbral en 1 a la izquierda
- «Las probabilidades de error» → `perror`: «P(error) = ?» arriba
- «se miden contando» → `contando`: bits que caen uno a uno por el umbral; los fallos en rojo, los aciertos en verde
- «cuántas salen mal» → `contador`: contador «Fallos / Pruebas = 3 / 20»
- «el promedio del capítulo siete» → `cap7`: etiqueta pequeña «Grandes números · Capítulo 7»
- «al crecer el número de pruebas» → `crece`: los bits caen más deprisa; a la derecha, la gráfica de la fracción contra el número de pruebas oscila
- «se acerca a la probabilidad real» → `real`: la gráfica se aplana junto a una línea horizontal «0,159»
- «La pregunta es» → `pregunta`: la gráfica se encoge a un lado
- «cuántas pruebas hacen falta» → `cuantas`: «N = ?» en ámbar

<!-- b2 -->
Esa cuenta tiene su propio error. Su tamaño típico es la raíz cuadrada de pe
por uno menos pe, dividido entre el número de pruebas. Para nuestro cero coma
ciento cincuenta y nueve, con cien pruebas es de cero coma cero treinta y
siete: puede salirte un doce por ciento o un veinte.

- «su propio error» → `error`: la gráfica se encoge arriba; «Error típico =» en rojo
- «la raíz cuadrada» → `raiz`: «√(   )» vacía
- «de pe» → `p`: dentro, «p»
- «uno menos pe» → `unomenos`: «p (1 − p)»
- «el número de pruebas» → `n`: «/ N» bajo la raíz: «√(p (1 − p) / N)»
- «nuestro cero coma ciento cincuenta y nueve» → `p159`: «p = 0,159»
- «con cien pruebas» → `cien`: «N = 100»
- «cero coma cero treinta y siete» → `e037`: «± 0,037»; debajo, un eje con una barra de incertidumbre alrededor de 0,159
- «un doce por ciento» → `doce`: el extremo izquierdo de la barra, «0,12»
- «o un veinte» → `veinte`: el extremo derecho, «0,20»

<!-- b3 -->
Con diez mil pruebas baja a cero coma cero cero cuatro. Por la raíz cuadrada,
para ganar diez veces más precisión hacen falta cien veces más pruebas.

- «Con diez mil pruebas» → `diezmil`: segunda barra, «N = 10.000»
- «cero coma cero cero cuatro» → `e004`: la barra se encoge a «± 0,004», casi un punto
- «Por la raíz cuadrada» → `porraiz`: la raíz de la fórmula se ilumina
- «diez veces más precisión» → `precision`: «Precisión × 10»
- «cien veces más pruebas» → `pruebas`: «= Pruebas × 100»

---

# Escena 11 — SucesosRaros

**Capítulo YouTube:** Cero errores vistos no es error cero
**Objetivo:** la trampa de los sucesos raros: con falsa alarma 0,00135, mil
pruebas no dan ninguna un 26 % de las veces; hay que ver al menos diez sucesos.

## Narración

<!-- b1 -->
Lo delicado son los sucesos raros. Pon el umbral en tres voltios: la falsa
alarma es de poco más de una entre mil. Haces mil pruebas sin señal. ¿Cuántas
falsas alarmas vas a ver? Lo esperado es una y pico. Pero la probabilidad de no
ver ninguna es del veintiséis por ciento.

- «los sucesos raros» → `raros`: corte; la campana del cero sola
- «el umbral en tres voltios» → `tres`: el umbral ámbar en 3 V
- «la falsa alarma» → `cola`: la cola a la derecha de 3 se sombrea en rojo, diminuta; una lupa la amplía
- «una entre mil» → `fa`: «Falsa alarma = 0,00135»
- «mil pruebas sin señal» → `mil`: la rejilla de mil puntos grises del gancho
- «¿Cuántas» → `pregunta`: «¿Cuántas falsas alarmas?» en ámbar; pausa
- «vas a ver?» → `ver`: tres opciones pequeñas, «0», «1» y «2», con un «?» cada una
- «una y pico» → `esperado`: «Esperado: 1,35»
- «no ver ninguna» → `hist`: a la derecha, un histograma de barras 0, 1, 2, 3, 4+; la barra del «0» se dibuja la primera
- «veintiséis por ciento» → `veintiseis`: la barra del «0» se ilumina en ámbar con «26 %»; las demás entran atenuadas (35 %, 24 %, 11 %, 5 %)

<!-- b2 -->
Una de cada cuatro veces concluirías que tu detector nunca da falsas alarmas.
La regla práctica: para medir una probabilidad hay que llegar a ver al menos
unos diez sucesos. Aquí, unas siete mil cuatrocientas pruebas. Para un error de
uno entre un millón, diez millones. Cero errores vistos no es error cero. Es
que todavía no has probado lo bastante.

- «Una de cada cuatro veces» → `cuatro`: cuatro rejillas pequeñas; una se enciende en ámbar
- «nunca da falsas alarmas» → `nunca`: en ella, el rótulo verde «Falsas alarmas: 0» del gancho
- «La regla práctica» → `regla`: corte; tarjeta «Regla práctica»
- «para medir una probabilidad» → `medir`: el contador «Fallos / Pruebas» pequeño junto a la tarjeta
- «al menos unos diez sucesos» → `diez`: «Ver ≥ 10 sucesos → N ≥ 10 / p»
- «Aquí, unas» → `aqui`: «p = 0,00135» entra bajo la regla
- «siete mil cuatrocientas pruebas» → `n7400`: «10 / 0,00135 ≈ 7.400»
- «Para un error de» → `error`: una segunda fila debajo, vacía
- «uno entre un millón» → `millon`: «p = 1 / 1.000.000»
- «diez millones» → `diezmillones`: «→ N ≈ 10.000.000»
- «Cero errores vistos» → `vistos`: frase grande «Cero errores vistos»
- «no es error cero» → `noes`: «≠ Error cero», con el «≠» en rojo
- «no has probado lo bastante» → `bastante`: el contador de pruebas vuelve a correr debajo

---

# Escena 12 — DeUnNumeroAUnaSenal

**Capítulo YouTube:** De un número a una señal entera
**Objetivo:** recapitular el capítulo en tres ideas y abrir el siguiente: un
receptor real recibe una señal entera, y para decidir con ella hay que
describir el ruido a lo largo del tiempo.

## Narración

<!-- b1 -->
Recojamos el capítulo en tres ideas. Una: decidir bien es comparar un número,
la razón de verosimilitud, con un umbral. Dos: el umbral sale de lo que sabes o
de lo que quieres: las probabilidades a priori, un presupuesto de falsas
alarmas, o los costes. Tres: la curva ROC enseña todos los umbrales a la vez, y
su pendiente es el propio umbral.

- «tres ideas» → `tres`: tres tarjetas vacías en fila, numeradas 1, 2 y 3
- «comparar un número» → `uno`: la tarjeta 1 se llena: «Λ(r)»
- «con un umbral» → `umbral`: «Λ(r) ≷ η»
- «Dos: el umbral sale» → `dos`: la tarjeta 2 se llena con «η:»
- «las probabilidades a priori» → `priori`: «A priori»
- «un presupuesto de falsas» → `presupuesto`: «· Presupuesto»
- «o los costes» → `costes`: «· Costes»
- «Tres: la curva ROC» → `roc`: la tarjeta 3 con la curva ROC pequeña y sus tres puntos
- «todos los umbrales a la vez» → `todos`: un punto recorre la curva pequeña
- «su pendiente es el propio umbral» → `pendiente`: la tangente en un punto; «Pendiente = η»

<!-- b2 -->
Pero en todo el capítulo la medición ha sido un solo número. Un voltaje. Un
receptor de verdad no recibe un número: recibe una señal entera, miles de
muestras seguidas, cada una con su ruido.

- «un solo número» → `r`: corte; un solo punto cian «r» sobre un eje
- «Un voltaje» → `voltaje`: «1,3 V» junto al punto
- «Un receptor de verdad» → `receptor`: el radar (`radar13`) entra a la izquierda
- «una señal entera» → `senal`: el punto se multiplica en una fila larga de barras cian
- «miles de muestras» → `miles`: la fila se alarga hasta salir de pantalla
- «cada una con su ruido» → `ruido`: cada barra tiembla con un trocito magenta

<!-- b3 -->
La regla no cambia: la razón de verosimilitud de todas las muestras juntas,
contra un umbral. Al final del curso veremos que toda esa señal se puede
resumir en un solo número sin perder nada. Y también que tener más datos no
basta: hay que saber combinarlos.

- «La regla no cambia» → `regla`: vuelve «Λ(r) ≷ η»
- «todas las muestras juntas» → `muchas`: la «r» se estira: «Λ(r[0], r[1], r[2], …) ≷ η»
- «contra un umbral. Al» → `contra`: el «η» late
- «Al final del curso» → `cap13`: etiqueta «Capítulo 13» abajo a la derecha
- «toda esa señal» → `toda`: la fila de barras se ilumina entera
- «en un solo número» → `numero`: la fila de barras se comprime en un solo punto; tarjeta «Toda la señal en un solo número»
- «sin perder nada» → `nada`: un tic verde junto a la tarjeta
- «más datos no basta» → `masdatos`: segunda tarjeta «Más datos no bastan»
- «saber combinarlos» → `combinar`: varias flechas desde las barras convergen en una caja «Σ»

<!-- b4 -->
Antes hace falta algo que todavía no tenemos. Para escribir esa razón hay que
describir el ruido a lo largo del tiempo. El ruido de este instante, ¿tiene
algo que ver con el de dentro de un milisegundo? ¿Cómo se describe, con
probabilidades, una señal entera que nunca se repite? Para eso no basta con
mirar una grabación del ruido. Hay que imaginar muchas a la vez.

- «algo que todavía no tenemos» → `falta`: las tarjetas se apartan; un hueco con un «?» ámbar
- «Para escribir esa razón» → `escribir`: vuelve «Λ(r[0], r[1], …)» con un «?» dentro
- «describir el ruido a lo largo del tiempo» → `ruido`: una grabación de ruido magenta se dibuja de izquierda a derecha
- «a lo largo del tiempo» → `tiempo`: bajo la grabación, un eje «Tiempo» con una flecha
- «de este instante» → `ahora`: una muestra se resalta con un punto
- «dentro de un milisegundo» → `despues`: la muestra vecina se resalta; las dos se unen con un arco y un «?»: «¿Tienen algo que ver?»
- «¿Cómo se describe» → `como`: «¿Cómo se describe?» arriba en ámbar
- «una señal entera que» → `entera`: la grabación entera se ilumina
- «nunca se repite» → `repite`: la grabación se borra y se dibuja otra distinta en el mismo sitio
- «una grabación del ruido» → `una`: queda una sola grabación, con la etiqueta «1»
- «imaginar muchas a la vez» → `muchas`: debajo se apilan muchas más, todas distintas

---

# Escena 13 — Cierre

**Capítulo YouTube:** Lo que viene: mil grabaciones del mismo ruido

## Narración

<!-- b1 -->
Hoy hemos dejado las campanas y hemos decidido con datos. La curva se vuelve
una escalera, y su área mide lo bien que el detector ordena. Pero ordenar no es
cortar, y cero errores vistos no es error cero.

- «dejado las campanas» → `campanas`: corte; las dos campanas se desvanecen
- «decidido con datos» → `datos`: la tira «+ + − + − + − −»
- «una escalera» → `escalera`: la escalera de la ROC empírica se dibuja de una vez
- «su área» → `area`: el área se rellena; «0,81»
- «lo bien que el detector ordena» → `ordena`: «Área = Lo bien que ordena»
- «ordenar no es cortar» → `cortar`: tarjeta «Ordenar ≠ Cortar»
- «cero errores vistos no es error cero» → `vistos`: tarjeta «Cero errores vistos ≠ Error cero»

<!-- b2 -->
Con esto cerramos las pruebas de hipótesis. En el próximo episodio empieza el
capítulo diez, y empezamos justo por ahí: muchas grabaciones de un mismo ruido,
una encima de otra. Mil grabaciones del mismo ruido.

- «cerramos las pruebas de hipótesis» → `cierre`: las tarjetas se juntan bajo «Capítulo 9 · Pruebas de hipótesis», con un tic
- «el próximo episodio» → `proximo`: corte; etiqueta «Capítulo 10 · Procesos aleatorios»
- «empezamos justo por ahí» → `ahi`: vuelve la grabación de ruido de la escena anterior
- «muchas grabaciones» → `grabaciones`: debajo de la grabación empiezan a apilarse otras
- «una encima de otra» → `apila`: la pila crece hasta llenar la pantalla
- «Mil grabaciones del mismo ruido» → `titulo`: tarjeta «Episodio 1 · Mil grabaciones del mismo ruido»
