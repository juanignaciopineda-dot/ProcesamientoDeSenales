# Episodio 4 — La curva de todos los umbrales

Capítulo 9 (Pruebas de hipótesis), episodio 4 de 6. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 16 a 19), más un gancho y un cierre nuevos.

**Estado:** **Subido a YouTube en privado** el 19/10/2026: render final 1080p60 de 8:18, título buscable, descripción con el capítulo del libro y `capitulos.txt`, subtítulos, categoría Educación (https://youtu.be/jBKt4tRmkts). Residuos limpiados; la caché de voz está en `media/voiceovers/`: se rehace con `python rehacer.py Capitulo09_PruebasDeHipotesis E4`. **Ojo**: el vídeo subido dice «curva ROC» (escena 04, b2) con la pronunciación anterior a /ˈrok/, porque esa escena venía de un render previo a la regla; un render nuevo la dice /ˈrok/ (único bloque que cambia). **Falta**: publicarlo (lo hace el usuario).
16 a 19, gancho, título y cierre). Momentos escritos (paso 10) y `ritmo.py`
sin tramos de más de 4 s (paso 11), con la voz real de Azure. Escenas
`s01`–`s14` animadas (paso 12; piezas en `comun/figuras_c9e4.py`); borrador
480p15 de 8:19 con **0 avisos** y hojas de contacto revisadas (pasos 13 y 14).
El usuario decidió dejarlo en ~8,5 min. Borrador aprobado por el usuario (paso
15) y render final 1080p60 hecho (8:18, 0 avisos). El usuario marcó dos errores en
0:43 (escena 03: las colas roja y verde entraban un instante con la forma del
umbral anterior); corregidos en `s03` y **render final 1080p60 rehecho** (8:18,
0 avisos). Sigue subir a YouTube y limpiar residuos (paso 17).

Texto nuevo (marcado con ⭐, **aprobado**):
- ⭐ Escena 01 (gancho): «Cada umbral es un detector distinto. Si los dibujas
  todos a la vez, sale una curva. Y esa curva guarda un secreto: su pendiente,
  en cada punto, es el umbral que estás usando.»
- ⭐ Escena 02 (título): «La curva de todos los umbrales».
- ⭐ Escena 14 (cierre): resumen corto (un detector es una curva, su pendiente
  es el umbral, cada criterio es un punto) y anuncia E5 por su título,
  «¿Cuánto cuesta equivocarse?».

Notas:
- El cierre del E3 ya anuncia este título («¿Y si pudiéramos verlos todos a la
  vez, en un solo dibujo?»). El gancho retoma esa idea y adelanta el resultado
  de la escena 09 (la pendiente es el umbral) sin dar la cuenta.
- Reparto de las escenas del guion base: 16 → escenas 03 y 04; 17 → 05, 06 y
  07; 18 → 08, 09 y 10; 19 → 11, 12 y 13. Solo se partieron bloques enteros: el
  texto del guion base no cambia.
- La escena 13 (bloque 19·b6) ya deja abierto el tercer criterio («el que
  arregla el absurdo del test médico»): el cierre lo retoma y no lo repite. La
  promesa «lo mejor sería no hacer el test» (E2) se paga en la escena 20 del
  guion base, que abre el E5.
- Largo: ~1.090 palabras del guion base más ~110 de gancho, título y cierre
  ≈ 1.200 palabras, unos 8 min de voz a 150 palabras por minuto. **Es el
  episodio más corto del capítulo.** Con los respiros y las pausas queda en
  ~8,5 min; si el usuario lo quiere más cerca de 10, lo natural es estirar la
  escena 06 (la familia de curvas: decir la cuenta de un desvío, cu de 0,645) o
  la 09 (una segunda comprobación de la pendiente). No se agrega nada sin su
  visto bueno.
- Números con el mismo dibujo de todo el capítulo: las dos campanas (centros 0
  y 2, desvío 1); puntos de la ROC: umbral 3 → (0,001; 0,16), 2 → (0,023; 0,5),
  1 → (0,16; 0,84), 0 → (0,5; 0,977); detección al 5 % con 1, 2 y 3 desvíos de
  separación: 0,26 · 0,64 · 0,91; pendientes e^(2r − 2): 2,72 · 1 · 0,37 ·
  0,135 en r = 1,5 · 1 · 0,5 · 0; punto del máximo a posteriori (0,077; 0,72)
  con umbral 1,42 y error 0,139; a priori iguales (0,16; 0,84);
  Neyman-Pearson (0,05; 0,64) con pendiente 3,6. Recomprobados.
- La mochila de la escena 15 del guion base (escenas 13 y 14 del E3) vuelve en
  pequeño en la escena 10: mismo dibujo que en el E3.
- Disposición fija de casi todo el episodio: **campanas a la izquierda** (`dens3`,
  `cola3`, `umbral3`: cero en `SENAL`… mismo dibujo que en E2 y E3) y **plano de la
  ROC a la derecha** (ejes «Falsa alarma» y «Detección», de 0 a 1). La curva ROC en
  `ESTIMACION` (ámbar); la falsa alarma y el fallo en `ERROR`, la detección en `VERDE`.

---

# Escena 01 — Gancho

**Capítulo YouTube:** Todos los detectores en un dibujo

## Narración

<!-- b1 -->
Cada umbral es un detector distinto. Si los dibujas todos a la vez, sale una
curva. Y esa curva guarda un secreto: su pendiente, en cada punto, es el umbral
que estás usando.

- «Cada umbral» → `umbral`: las dos campanas con un umbral vertical que salta a tres posiciones
- «un detector distinto» → `detector`: cada posición deja un punto ámbar en un plano a la derecha
- «todos a la vez» → `todos`: el umbral barre rápido y los puntos se vuelven una curva continua
- «guarda un secreto» → `secreto`: la curva se ilumina; un «?» ámbar sobre ella
- «su pendiente» → `pendiente`: una recta tangente recorre la curva
- «es el umbral» → `es`: junto a la tangente, «Pendiente = Umbral» con pop

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** La curva de todos los umbrales

## Narración

<!-- b1 -->
La curva de todos los umbrales.

- «La curva de todos los umbrales» → `titulo`: el título del episodio, solo, con la curva ámbar dibujándose detrás

---

# Escena 03 — UnPuntoPorUmbral

**Capítulo YouTube:** Un punto por cada umbral
**Objetivo:** ver que cada umbral da un par (falsa alarma, detección) y llevar
cuatro umbrales al plano, con la cuenta de cada cola.

## Narración

<!-- b1 -->
Un detector no es un único par de números. Es una familia entera: un par por
cada umbral. Vamos a dibujarla. En un plano, ponemos en horizontal la
probabilidad de falsa alarma y en vertical la de detección. Cada umbral es un
punto.

- «Un detector no es» → `par`: las dos campanas con el umbral en 1,42 y una tarjeta «(0,077; 0,72)»
- «una familia entera» → `familia`: la tarjeta se multiplica en una pila de tarjetas con otros pares
- «Vamos a dibujarla» → `dibujar`: la pila se va; las campanas se corren a la izquierda
- «en horizontal» → `horiz`: a la derecha se dibuja el eje horizontal, «Falsa alarma», de 0 a 1
- «en vertical» → `vert`: el eje vertical, «Detección», de 0 a 1
- «Cada umbral es un» → `punto`: un umbral vertical en las campanas y una flecha hacia el plano

<!-- b2 -->
Empezamos con el umbral en tres voltios. La falsa alarma es cu de tres: una
milésima. La detección: del tres al dos hay un desvío, así que cu de uno, cero
coma dieciséis. Un punto pegado al eje vertical, muy abajo. Casi no hay falsas
alarmas, pero se escapan casi todos los aviones.

- «el umbral en tres voltios» → `u3`: el umbral se desliza a 3; rótulo «Umbral 3»
- «La falsa alarma es» → `fa3`: se sombrea en rojo la cola de la campana del cero a la derecha de 3
- «una milésima» → `q3`: «P_FA = Q(3) = 0,001»
- «del tres al dos» → `desvio`: una llave entre 2 y 3 con «1 desvío»
- «cero coma dieciséis» → `pd3`: se sombrea en verde la cola de la campana del uno; «P_D = Q(1) = 0,16»
- «Un punto pegado» → `p3`: el punto (0,001; 0,16) cae en el plano, con «3» al lado
- «Casi no hay falsas» → `pocas`: la cola roja, casi invisible, se resalta con un aro
- «se escapan casi todos» → `escapan`: la parte sin sombrear de la campana del uno parpadea en rojo

<!-- b3 -->
Bajamos el umbral a dos. Falsa alarma, cero coma cero veintitrés. Detección,
justo media campana: cero coma cinco. Con el umbral en uno: cero coma dieciséis
y cero coma ochenta y cuatro. Y con el umbral en cero: cero coma cinco y cero
coma noventa y ocho.

- «Bajamos el umbral a dos» → `u2`: el umbral se desliza a 2; las colas crecen
- «cero coma cero veintitrés» → `fa2`: «0,023» junto a la cola roja
- «justo media campana» → `media`: la mitad derecha de la campana del uno en verde; «0,5»
- «cero coma cinco.» → `p2`: cae el punto (0,023; 0,5) con «2»
- «Con el umbral en uno» → `u1`: el umbral pasa a 1; «0,16» y «0,84»
- «cero coma ochenta y cuatro» → `p1`: cae el punto (0,16; 0,84) con «1»
- «con el umbral en cero» → `u0`: el umbral pasa a 0; «0,5» y «0,98»
- «cero coma noventa y ocho» → `p0`: cae el punto (0,5; 0,98) con «0»

---

# Escena 04 — LaCurvaRoc

**Capítulo YouTube:** La curva ROC
**Objetivo:** ubicar los dos extremos, barrer el umbral para trazar la curva
entera y ver que no depende de las probabilidades a priori.

## Narración

<!-- b1 -->
Los extremos son fáciles. Con un umbral altísimo nunca se dice uno: ni falsas
alarmas ni detección. Es la esquina de abajo a la izquierda. Con un umbral
bajísimo siempre se dice uno: todo son detecciones y todo son falsas alarmas.
Es la esquina de arriba a la derecha.

- «Los extremos son fáciles» → `extremos`: los cuatro puntos de antes quedan en el plano; las dos esquinas parpadean
- «un umbral altísimo» → `alto`: el umbral sale por la derecha de las campanas; las colas desaparecen
- «ni falsas alarmas ni detección» → `cero`: «0» y «0» en las dos lecturas
- «abajo a la izquierda» → `esq0`: punto en (0, 0) con «Nunca decir 1»
- «un umbral bajísimo» → `bajo`: el umbral sale por la izquierda; las dos campanas se sombrean enteras
- «todo son detecciones» → `todo`: «1» y «1» en las dos lecturas
- «todo son falsas alarmas» → `todofa`: la campana del cero entera en rojo
- «arriba a la derecha» → `esq1`: punto en (1, 1) con «Siempre decir 1»

<!-- b2 -->
Al deslizar el umbral, el punto viaja de una esquina a la otra y dibuja una
curva. Se llama curva ROC, característica operativa del receptor: el nombre se
lo pusieron los operadores de radar. Resume todo lo que el detector puede
hacer. Elegir un umbral es elegir un punto de la curva.

- «Al deslizar el umbral» → `barrido`: el umbral barre de derecha a izquierda de forma continua
- «dibuja una curva» → `traza`: el punto ámbar arrastra la curva, que pasa por los cuatro puntos
- «curva ROC» → `roc`: rótulo «Curva ROC» con pop
- «característica operativa del receptor» → `nombre`: debajo, «Receiver Operating Characteristic» en pequeño
- «operadores de radar» → `radar`: un `radar13()` pequeño en la esquina, con sus ondas
- «Resume todo» → `resume`: la curva se resalta; el radar se va
- «Elegir un umbral» → `umbral`: el umbral vuelve a moverse y se frena
- «elegir un punto» → `elegir`: el umbral se fija en 1,42 y un punto se marca sobre la curva

<!-- b3 -->
Y fíjate en lo que no aparece: las probabilidades a priori. La curva es del
detector, no de lo frecuente que sea lo que busca. Las probabilidades a priori
servirán para elegir el punto, pero no cambian la curva.

- «lo que no aparece» → `falta`: a un lado aparecen «p₀ = 0,7» y «p₁ = 0,3»
- «las probabilidades a priori» → `apriori`: las dos etiquetas se resaltan en ámbar
- «La curva es del detector» → `del`: las campanas (sin escalar) y la curva se iluminan juntas
- «lo frecuente» → `tachar`: las etiquetas se tachan; «No intervienen»
- «lo que busca» → `busca`: rótulo «No intervienen» con pop
- «para elegir el punto» → `punto`: una flecha de las etiquetas tachadas al punto marcado
- «no cambian la curva» → `igual`: p₀ cambia a 0,5 y a 0,9; la curva no se mueve

---

# Escena 05 — LaEsquinaYLaDiagonal

**Capítulo YouTube:** La esquina ideal y la diagonal del azar
**Objetivo:** leer las dos referencias del plano: la esquina del detector
perfecto y la diagonal de decidir al azar.

## Narración

<!-- b1 -->
¿Cómo se lee esta curva? Primero, la esquina de arriba a la izquierda. Ahí la
detección vale uno y la falsa alarma, cero: el detector perfecto. Cuanto más se
acerque la curva a esa esquina, mejor.

- «¿Cómo se lee esta curva?» → `leer`: corte; el plano con la curva en grande, centrado
- «arriba a la izquierda» → `esquina`: la esquina (0, 1) se ilumina en verde
- «la detección vale uno» → `uno`: «Detección 1» junto al eje vertical
- «la falsa alarma, cero» → `cero`: «Falsa alarma 0» junto al eje horizontal
- «el detector perfecto» → `ideal`: una estrella verde en la esquina con «Ideal»
- «Cuanto más se acerque» → `acerca`: la curva se estira hacia la esquina y vuelve
- «esa esquina, mejor» → `mejor`: tilde verde junto a la estrella

<!-- b2 -->
Segundo, la diagonal. Imagina un detector que no mira nada: tira una moneda
cargada que dice uno con cierta probabilidad. Dirá uno esa fracción de las
veces, haya avión o no. Su falsa alarma y su detección son iguales. Eso es la
diagonal: decidir al azar.

- «Segundo, la diagonal» → `diagonal`: se dibuja la diagonal de (0, 0) a (1, 1), en gris
- «Imagina un detector» → `imagina`: una caja «Detector» junto al plano
- «no mira nada» → `ciego`: un `ojo` tachado junto al plano
- «una moneda cargada» → `moneda`: una `moneda("1")` con «q» debajo
- «con cierta probabilidad» → `prob`: la moneda gira y cae en «1»
- «Dirá uno esa fracción» → `q`: «q = 0,3» y un punto sobre la diagonal en (0,3; 0,3)
- «haya avión o no» → `avion`: dos casillas, «Con avión» y «Sin avión», ambas con «0,3»
- «son iguales» → `iguales`: «Falsa alarma = Detección = q»; q barre y el punto recorre la diagonal
- «decidir al azar» → `azar`: rótulo «Decidir al azar» sobre la diagonal

---

# Escena 06 — FamiliaDeCurvas

**Capítulo YouTube:** Cuanto más separadas, mejor curva
**Objetivo:** ver la familia de curvas según la separación de las campanas
(26 %, 64 % y 91 % de detección al 5 %) y qué significa quedar por debajo de
la diagonal.

## Narración

<!-- b1 -->
Todo lo útil queda entre la diagonal y la esquina, y depende de cuánto se
separan las campanas, medido en desvíos. Fijemos un cinco por ciento de falsas
alarmas. Con un desvío de separación, la detección es del veintiséis por
ciento. Con dos, del sesenta y cuatro. Con tres, del noventa y uno.

- «Todo lo útil» → `util`: se sombrea suave la zona entre la diagonal y la esquina
- «cuánto se separan las campanas» → `campanas`: a la izquierda, las dos campanas pequeñas
- «medido en desvíos» → `desvios`: una llave entre los centros con «2 desvíos»
- «un cinco por ciento» → `cinco`: una vertical en 0,05 en el plano, rótulo «5 %»
- «Con un desvío» → `d1`: las campanas se acercan a 1 desvío; se dibuja su curva, baja; marca «0,26»
- «del veintiséis por» → `v26`: la marca «0,26» se resalta
- «Con dos» → `d2`: vuelven a 2 desvíos; la curva de siempre; marca «0,64»
- «Con tres» → `d3`: se separan a 3; una curva pegada a la esquina; marca «0,91»

<!-- b2 -->
¿Y una curva por debajo de la diagonal? Sería un detector peor que el azar. Es
decir, un buen detector puesto al revés: basta con invertir todas sus
decisiones, y su curva se refleja por encima de la diagonal.

- «¿Y una curva por debajo» → `debajo`: las tres curvas se atenúan; aparece una curva roja bajo la diagonal
- «de la diagonal?» → `diag`: la diagonal se resalta en gris claro
- «peor que el azar» → `peor`: rótulo «Peor que el azar»
- «puesto al revés» → `reves`: dos casillas «0 ↔ 1» que se intercambian
- «invertir todas sus decisiones» → `invertir`: las casillas giran
- «se refleja» → `refleja`: la curva roja se refleja sobre la diagonal y queda ámbar, por encima

---

# Escena 07 — CompararDetectores

**Capítulo YouTube:** Comparar dos detectores
**Objetivo:** comparar detectores con sus curvas (una encima de otra, o que se
cruzan) y dejar abierta la pregunta de la forma.

## Narración

<!-- b1 -->
La curva sirve también para comparar. Si la de un detector queda por encima de
la de otro en todos los puntos, es mejor con cualquier criterio. Si se cruzan,
depende de la zona en la que vayas a trabajar.

- «sirve también para comparar» → `comparar`: corte; el plano con dos curvas, «A» en ámbar y «B» en cian
- «por encima de la de otro» → `encima`: la zona entre las dos curvas se sombrea en verde
- «con cualquier criterio» → `mejor`: rótulo «A mejor siempre»
- «Si se cruzan» → `cruzan`: la curva B se transforma en una que corta a A en un punto
- «depende de la zona» → `zona`: a la izquierda del cruce gana A, a la derecha gana B, sombreado con sus colores; «Depende de la zona»

<!-- b2 -->
Y un detalle de la forma: estas curvas tienen siempre la panza hacia arriba.
Muy empinadas al principio, casi planas al final. No es casualidad, y la razón
esconde el resultado más bonito del capítulo.

- «un detalle de la forma» → `forma`: queda la curva de siempre sola
- «la panza hacia arriba» → `panza`: una flecha curva bajo la curva señalando su comba
- «Muy empinadas al principio» → `empinada`: un tramo corto de la curva cerca del origen se resalta
- «casi planas al final» → `plana`: se resalta un tramo cerca de (1, 1)
- «No es casualidad» → `casualidad`: un «?» ámbar grande sobre la curva
- «el resultado más bonito» → `bonito`: el «?» late con un brillo

---

# Escena 08 — LaRebanada

**Capítulo YouTube:** Bajar el umbral un poquito
**Objetivo:** recordar qué es la pendiente y ver que bajar el umbral un poco
suma una rebanada fina a cada error: altura por ancho.

## Narración

<!-- b1 -->
La pendiente de una curva dice cuánto sube por cada paso que das hacia la
derecha. En esta curva, eso es cuánta detección ganas por cada poco de falsa
alarma que aceptas.

- «La pendiente de una curva» → `pendiente`: corte; sobre la curva, un punto
- «cuánto sube» → `sube`: un triángulo pequeño; su cateto vertical en verde, «Lo que sube»
- «hacia la derecha» → `paso`: su cateto horizontal, «Paso a la derecha»
- «cuánta detección ganas» → `gana`: el rótulo vertical cambia a «+ Detección»
- «falsa alarma que aceptas» → `acepta`: el horizontal cambia a «+ Falsa alarma»

<!-- b2 -->
Baja el umbral un poquito, de uno a cero coma noventa y nueve. La región donde
se dice uno gana una rebanada muy fina. La falsa alarma aumenta en el área de
esa rebanada bajo la campana del cero: su altura por el ancho. Y la detección
aumenta en el área bajo la campana del uno: su altura por el mismo ancho.

- «Baja el umbral un poquito» → `baja`: corte a las campanas grandes, umbral en 1
- «cero coma noventa y nueve» → `u099`: el umbral se mueve apenas; rótulos «1» y «0,99»
- «La región donde» → `region`: la región a la derecha del umbral se sombrea suave
- «una rebanada muy fina» → `rebanada`: zoom a la franja entre 0,99 y 1, que se ilumina
- «La falsa alarma aumenta» → `fa`: rótulo «+ Falsa alarma» sobre la franja, en rojo
- «bajo la campana del cero» → `r0`: en la franja, un rectángulo rojo bajo la campana del cero
- «su altura por el ancho» → `area0`: «f₀ · Ancho» junto al rectángulo rojo
- «Y la detección aumenta» → `pd`: rótulo «+ Detección», en verde
- «bajo la campana del uno» → `r1`: un rectángulo verde (solo el borde) bajo la campana del uno; en el umbral 1 las campanas se cruzan y queda de la misma altura
- «por el mismo ancho» → `area1`: «f₁ · Ancho» y una llave sobre la rebanada (el ancho común)

---

# Escena 09 — LaPendienteEsEta

**Capítulo YouTube:** La pendiente es el umbral
**Objetivo:** cancelar los anchos y llegar a pendiente = razón de verosimilitud
en el umbral = eta; comprobarlo con cuatro umbrales.

## Narración

<!-- b1 -->
La pendiente es lo que sube entre lo que avanza. Los anchos se cancelan, y
queda la altura de la campana del uno entre la altura de la campana del cero,
en el umbral. La razón de verosimilitud. La pendiente de la curva en cada punto
es el umbral eta que se está usando ahí.

- «lo que sube entre lo que avanza» → `cociente`: «Pendiente = (f₁ · Ancho) / (f₀ · Ancho)», término a término
- «Los anchos se cancelan» → `cancela`: los dos «Ancho» se tachan y se van
- «la altura de la campana del uno» → `f1`: queda «f₁ / f₀»; f₁ en verde
- «la altura de la campana del cero» → `f0`: f₀ en rojo
- «La razón de verosimilitud» → `lambda`: «= Λ(umbral)» con pop
- «en cada punto» → `punto`: un punto sobre la curva ROC con su tangente
- «el umbral eta» → `eta`: recuadro enmarcado «Pendiente = Λ en el umbral = η»

<!-- b2 -->
Comprobémoslo. Con el umbral en uno coma cinco, la razón es e elevado a uno:
dos coma setenta y dos. En uno vale uno. En cero coma cinco, cero coma treinta
y siete. En cero, cero coma ciento treinta y cinco. Si mides las pendientes
sobre la curva dibujada, salen esos mismos números.

- «Comprobémoslo» → `tabla`: a la izquierda, tabla vacía «Umbral · Λ = e^(2r − 2)»
- «uno coma cinco» → `u15`: fila «1,5 → e¹»
- «dos coma setenta y dos» → `l15`: «2,72» y la tangente en ese punto de la ROC
- «En uno vale uno» → `u1`: fila «1 → 1» y su tangente
- «cero coma treinta y siete» → `u05`: fila «0,5 → 0,37» y su tangente
- «cero coma ciento treinta y cinco» → `u0`: fila «0 → 0,135» y su tangente, casi plana
- «Si mides las pendientes» → `mides`: sobre cada tangente se dibuja su triángulo
- «salen esos mismos números» → `mismos`: cada tangente con su triángulo y el número; tilde verde

---

# Escena 10 — LaPanzaHaciaArriba

**Capítulo YouTube:** Por qué la curva tiene panza
**Objetivo:** deducir la forma de la curva (pendiente que baja) y atarla al
presupuesto del episodio anterior.

## Narración

<!-- b1 -->
De ahí sale la forma. Al bajar el umbral, eta baja, y la pendiente con él. Una
curva cuya pendiente no para de bajar tiene la panza hacia arriba. Es el
presupuesto otra vez: las primeras falsas alarmas compran mucha detección, y
las últimas, casi nada. Y este resultado sirve para algo más: dice en qué punto
de la curva está cada criterio.

- «De ahí sale la forma» → `forma`: corte; la curva sola con una tangente en el origen
- «Al bajar el umbral» → `barre`: la tangente recorre la curva de izquierda a derecha
- «y la pendiente con él» → `tumba`: la tangente se va tumbando; un contador de pendiente que baja
- «Una curva cuya pendiente» → `cuya`: una flecha curva bajo la curva marca la comba
- «la panza hacia arriba» → `panza`: «Pendiente que baja = Panza hacia arriba»
- «Es el presupuesto otra vez» → `mochila`: la mochila del E3, pequeña, en una esquina
- «las primeras falsas alarmas» → `primeras`: en la mochila entra el nivel 5 (rinde 8) y la curva se resalta al principio
- «compran mucha detección» → `compran`: la tangente empinada del principio se resalta
- «casi nada» → `ultimas`: entra el nivel 1 (0,125) y se resalta el tramo final, casi plano
- «sirve para algo más» → `mas`: la mochila se va
- «cada criterio» → `criterio`: tres puntos vacíos con «?» sobre la curva

---

# Escena 11 — RectasDeIgualError

**Capítulo YouTube:** Rectas de igual error
**Objetivo:** escribir el error con la falsa alarma y la detección y ver que
los puntos de igual error forman rectas de pendiente pe cero entre pe uno.

## Narración

<!-- b1 -->
¿Qué punto de la curva da el menor error? Recuerda la fórmula: pe cero por la
falsa alarma, más pe uno por el fallo. Y el fallo es uno menos la detección.

- «¿Qué punto de la curva» → `pregunta`: el plano con la curva; un punto que se mueve por ella con un «?»
- «Recuerda la fórmula» → `formula`: arriba, «P_e =» en ámbar
- «pe cero por la falsa alarma» → `t1`: arriba, «P_e = p₀ · P_FA»
- «más pe uno por el fallo» → `t2`: se suma «+ p₁ · P_M»
- «uno menos la detección» → `t3`: P_M se reemplaza por «(1 − P_D)»

<!-- b2 -->
Con setenta y treinta: si te mueves hacia la derecha, el error sube cero coma
siete por cada unidad de falsa alarma. Si te mueves hacia arriba, baja cero
coma tres por cada unidad de detección. Para quedarte con el mismo error, por
cada paso a la derecha tienes que subir dos coma treinta y tres. Los puntos de
igual error forman rectas con esa pendiente: pe cero entre pe uno.

- «Con setenta y treinta» → `pes`: en la fórmula, p₀ → 0,7 y p₁ → 0,3
- «hacia la derecha» → `derecha`: en el plano, un punto con una flecha roja a la derecha
- «cero coma siete por cada unidad» → `mas07`: junto a la flecha, «+0,7 de error por unidad»
- «de falsa alarma» → `ufa`: el punto avanza y un contador de error sube
- «hacia arriba» → `arriba`: una flecha verde hacia arriba
- «coma tres por cada unidad» → `menos03`: «−0,3 por unidad»
- «Para quedarte» → `quedar`: las dos flechas se combinan en una diagonal
- «el mismo error» → `mismo`: un triángulo: «1 a la derecha»
- «dos coma treinta y tres» → `sube233`: el cateto vertical crece: «2,33 hacia arriba»
- «forman rectas» → `recta`: por el punto pasa una recta de pendiente 2,33
- «pe cero entre pe uno» → `pend`: «Pendiente = p₀ / p₁ = 2,33»

---

# Escena 12 — LaTangente

**Capítulo YouTube:** El punto de Bayes
**Objetivo:** deslizar la recta hasta que sea tangente, igualar pendientes y
reencontrar eta = pe cero entre pe uno, con el punto (0,077; 0,72).

## Narración

<!-- b1 -->
Son rectas paralelas, y cuanto más arriba y a la izquierda, menos error.
Desliza una hacia la esquina ideal hasta que toque la curva por última vez. En
ese momento la roza en un solo punto: es tangente.

- «Son rectas paralelas» → `familia`: aparecen cinco rectas paralelas de pendiente 2,33
- «menos error» → `verde`: las rectas se colorean de rojo a verde hacia arriba a la izquierda
- «Desliza una» → `desliza`: queda una recta, que se desplaza hacia la esquina ideal
- «por última vez» → `ultima`: la recta llega a rozar la curva
- «en un solo punto» → `toca`: el punto de contacto se marca
- «es tangente» → `tangente`: rótulo «Tangente» con pop

<!-- b2 -->
En el punto de tangencia, la curva y la recta tienen la misma pendiente. La de
la recta es pe cero entre pe uno. La de la curva es eta. Así que eta vale pe
cero entre pe uno. Es la regla del máximo a posteriori, encontrada otra vez,
ahora con un dibujo. El punto: falsa alarma cero coma cero setenta y siete,
detección cero coma setenta y dos.

- «la misma pendiente» → `misma`: zoom al punto de tangencia, la recta y la curva juntas
- «La de la recta» → `recta`: «Pendiente de la recta = p₀/p₁»
- «La de la curva es eta» → `curva`: «Pendiente de la curva = η»
- «Así que eta vale» → `igual`: las dos se funden en «η = p₀/p₁», enmarcado
- «la regla del máximo a posteriori» → `map`: «MAP» en pantalla junto al recuadro
- «con un dibujo» → `dibujo`: zoom de vuelta; la curva entera con la tangente
- «cero coma cero setenta y siete» → `fa`: «(0,077;» junto al punto
- «cero coma setenta y dos» → `pd`: «0,72)»; debajo, «Umbral 1,42 · Error 0,139»

---

# Escena 13 — CadaCriterioUnPunto

**Capítulo YouTube:** Cada criterio, un punto de la curva
**Objetivo:** ubicar en la misma curva el punto de a priori iguales y el de
Neyman-Pearson, y dejar el hueco del tercer criterio.

## Narración

<!-- b1 -->
Con ceros y unos igual de frecuentes, las rectas tienen pendiente uno, como la
diagonal. El punto de tangencia es el más alejado de la diagonal. Y el criterio
de Neyman-Pearson es una recta vertical en el cinco por ciento: donde corta a
la curva, ese es el punto. Ahí la pendiente vale tres coma seis.

- «igual de frecuentes» → `iguales`: «p₀ = p₁ = 0,5» en la esquina
- «pendiente uno» → `pend1`: rectas paralelas a la diagonal; una se desliza hasta tocar la curva
- «El punto de tangencia» → `tang`: el punto de contacto (0,16; 0,84) se marca
- «el más alejado de la diagonal» → `lejos`: un segmento perpendicular de la diagonal al punto (0,16; 0,84)
- «Neyman-Pearson» → `np`: rótulo «Neyman-Pearson»
- «una recta vertical» → `vertical`: una vertical en 0,05 sube desde el eje
- «donde corta a la curva» → `corta`: el punto (0,05; 0,64) se marca
- «ese es el punto» → `ese`: rótulo «(0,05; 0,64)» junto al punto
- «tres coma seis» → `pend36`: la tangente en ese punto con «Pendiente 3,6»

<!-- b2 -->
Dos criterios, un detector, dos puntos de la misma curva. Y falta un tercero:
el que arregla el absurdo del test médico.

- «Dos criterios» → `dos`: los dos puntos con sus etiquetas, «Máximo a posteriori» y «Neyman-Pearson»
- «un detector» → `uno`: la curva se resalta, una sola
- «falta un tercero» → `tercero`: un tercer punto vacío sobre la curva con «?»
- «el absurdo del test médico» → `test`: junto al «?», la tarjeta «Siempre sano → 1 %» del E2

---

# Escena 14 — Cierre

**Capítulo YouTube:** Lo que viene: cuánto cuesta equivocarse

## Narración

<!-- b1 -->
Hoy hemos visto que un detector es una curva entera, un punto por cada umbral.
Su pendiente, en cada punto, es el umbral que se usa ahí. Y cada criterio no es
otro detector: es otro punto de la misma curva.

- «un detector es una curva entera» → `curva`: corte; las campanas y el plano con la curva ámbar
- «un punto por cada umbral» → `barre`: el umbral barre y el punto recorre la curva
- «Su pendiente» → `pend`: la tangente en el punto con «Pendiente = η»
- «es el umbral que se usa» → `ahi`: «η» late junto a la tangente
- «cada criterio no es» → `criterios`: aparecen los dos puntos con sus etiquetas
- «otro punto de la misma curva» → `misma`: el tercer punto vacío con «?»

<!-- b2 -->
Pero hasta ahora los dos errores pesaban lo mismo. ¿Y si mandar a casa a un
enfermo fuera mucho más grave que repetirle la prueba a un sano? Lo veremos en
el próximo episodio: ¿cuánto cuesta equivocarse?

- «los dos errores pesaban lo mismo» → `balanza`: corte; una balanza equilibrada con «Falsa alarma» y «Fallo»
- «mandar a casa a un enfermo» → `enfermo`: en un platillo, una `casa` y una persona roja
- «mucho más grave» → `inclina`: la balanza se inclina hacia ese lado
- «repetirle la prueba a un sano» → `sano`: en el otro platillo, una persona y una tira de test
- «en el próximo episodio» → `proximo`: tarjeta «Episodio 5 · ¿Cuánto cuesta equivocarse?»
- «¿cuánto cuesta equivocarse?» → `titulo5`: el título del E5 se resalta y la balanza late
