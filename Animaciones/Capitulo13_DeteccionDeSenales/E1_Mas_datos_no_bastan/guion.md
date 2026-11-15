# Episodio 1 — Más datos no bastan

Capítulo 13 (Detección de señales), episodio 1 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 01 a 04), más un gancho y un cierre nuevos.

**Estado:** escenas `s01`–`s12` animadas; borrador 480p15 de 8:44, **0 avisos**, hojas de contacto revisadas. Falta: revisión del usuario del texto ⭐ (gancho y cierre, paso 9), el visto bueno al mp4 (paso 15) y el render final. Sin probar de oído: «miss».

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Con una medición te equivocas una de cada cuatro veces. Con dos, menos. Pero si las promedias, vuelves a equivocarte una de cada cuatro. Más datos no bastan.»
- ⭐ Escena 12 (cierre): resumen y anuncia E2 por su título, «Toda la señal en un solo número».

Nota para el episodio anterior: el cierre del último episodio del Cap. 12 (E7, escena 17) ya anuncia este título, «Más datos no bastan».

Reparto de las escenas del guion base: 01 → escenas 03, 04 y 05; 02 → 06 y 07; 03 → 08 y 09; 04 → 10 y 11.
Solo se partieron bloques enteros en escenas atómicas: el texto del guion base no cambia.

Ejemplos que se fijan aquí y vuelven en el resto del capítulo: la tabla de 2 × 2 (falsa alarma y miss, escena 04), las dos curvas escaladas por su a priori (escenas 06 y 07) y el cuadrado grande con el pequeño dentro (escenas 08 y 09). El pulso `s = (2, 2, 1)` asoma al final de la escena 11 y se presenta en el E2.

---

# Escena 01 — Gancho

**Capítulo YouTube:** Dos datos, y promediarlos

## Narración

<!-- b1 -->
Con una medición te equivocas una de cada cuatro veces. Con dos, menos. Pero si las promedias, vuelves a equivocarte una de cada cuatro. Más datos no bastan.

- «Con una medición» → `una`: un eje con un único punto «r»
- «una de cada cuatro veces» → `cuatro`: cuatro casillas, una en rojo, y una barra de error «¼»
- «Con dos» → `dos`: aparece el plano r₁, r₂ con dos puntos
- «menos» → `menos`: la barra de error baja a «3/16», más corta que la anterior
- «si las promedias» → `promedias`: entra «(r₁ + r₂) / 2» y los dos puntos se aplastan sobre la diagonal
- «vuelves a equivocarte» → `vuelves`: la barra de error vuelve a subir a «¼», en rojo
- «Más datos no bastan» → `nobastan`: la frase entra con rebote en ámbar, sobre todo lo demás

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Más datos no bastan

## Narración

<!-- b1 -->
Más datos no bastan.

- «Más datos» → `t1`: «Más datos» entra con rebote
- «no bastan» → `t2`: «no bastan» entra debajo, con la etiqueta «Capítulo 13 · Detección de señales»

---

# Escena 03 — ElRadar

**Capítulo YouTube:** El radar: ¿avión o ruido?
**Objetivo:** plantear el problema del capítulo (¿hay una señal escondida en el ruido o solo hay ruido?) y fijar las dos hipótesis y las probabilidades a priori.

## Narración

<!-- b1 -->
Un radar lanza un pulso y se queda escuchando. Si hay un avión, vuelve un eco muy débil, escondido en el ruido. Si no hay nada, solo se oye el ruido. Con lo que ha oído, el radar tiene que decidir: ¿hay un avión o no? Ese sí o no es el problema de todo este capítulo.

- «lanza un pulso» → `pulso`: una antena de radar a la izquierda lanza un arco azul hacia la derecha
- «se queda escuchando» → `escucha`: el pulso se apaga y la antena queda con ondas de escucha
- «Si hay un avión» → `avion`: aparece un avión a la derecha
- «vuelve un eco muy débil» → `eco`: una onda azul diminuta vuelve a la antena
- «escondido en el ruido» → `escondido`: una traza magenta enorme tapa el eco
- «Si no hay nada» → `nada`: el avión se va y solo queda la traza magenta
- «solo se oye el ruido» → `solo`: el rótulo «solo ruido» en magenta
- «tiene que decidir» → `decidir`: una caja ámbar «decidir» junto a la antena
- «¿hay un avión o no?» → `pregunta`: la pregunta «¿avión o ruido?» en ámbar
- «Ese sí o no» → `sino`: «sí» y «no» grandes a los lados de la pregunta
- «todo este capítulo» → `capitulo`: la etiqueta «Capítulo 13 · Detección de señales»

<!-- b2 -->
Démosle nombres. La hipótesis cero, hache cero, dice: solo hay ruido. La hipótesis uno, hache uno, dice: hay señal más ruido. Y antes de escuchar nada ya sabemos algo: por ejemplo, que aviones hay pocos. Esas dos probabilidades de partida, pe cero y pe uno, se llaman probabilidades a priori, porque valen antes de medir.

- «Démosle nombres» → `nombres`: corte; aparecen dos casillas vacías, lado a lado
- «hache cero» → `h0`: la casilla izquierda se rotula «H₀» en magenta
- «solo hay ruido» → `h0r`: dentro, la traza magenta y el texto «solo ruido»
- «hache uno» → `h1`: la casilla derecha se rotula «H₁»
- «hay señal más ruido» → `h1r`: dentro, la suma cian de la señal azul y el ruido magenta
- «antes de escuchar nada» → `antes`: sobre las casillas, un oído tachado
- «aviones hay pocos» → `pocos`: una fila de diez cuadraditos grises con uno solo en azul
- «Esas dos probabilidades de partida» → `partida`: una llave une las dos casillas
- «pe cero y pe uno» → `ps`: bajo cada casilla aparecen «p₀» y «p₁»
- «probabilidades a priori» → `priori`: «a priori» entra con rebote en ámbar
- «antes de medir» → `medir`: «antes de medir» debajo de «a priori»

---

# Escena 04 — CuatroCasos

**Capítulo YouTube:** Falsa alarma, miss y probabilidad de error
**Objetivo:** los cuatro casos de una decisión (dos aciertos, falsa alarma y miss) y la probabilidad de error como media ponderada, con números redondos.

## Narración

<!-- b1 -->
Al decidir hay cuatro casos posibles. Dos son aciertos. Los otros dos son errores, y tienen nombre propio. Si el radar dice que hay avión y no lo había, es una falsa alarma. Si dice que no hay nada y sí lo había, es un fallo, que en inglés se llama miss. En medicina es igual: el falso positivo y el falso negativo de un test.

- «cuatro casos posibles» → `cuatro`: corte; tabla de 2 × 2, filas «realidad» (H₀, H₁) y columnas «decisión» (H₀, H₁)
- «Dos son aciertos» → `aciertos`: las dos casillas de la diagonal reciben un tilde verde
- «Los otros dos son errores» → `errores`: las otras dos reciben una cruz roja
- «nombre propio» → `nombre`: las dos cruces se resaltan
- «dice que hay avión y no lo había» → `dicehay`: se resalta la casilla (realidad H₀, decisión H₁), con un avión tachado
- «falsa alarma» → `fa`: el rótulo «falsa alarma» en rojo sobre esa casilla
- «dice que no hay nada y sí lo había» → `dicenada`: se resalta la casilla (realidad H₁, decisión H₀), con un avión y un signo «no»
- «un fallo» → `fallo`: el rótulo «fallo» en rojo sobre esa casilla
- «miss» → `miss`: bajo «fallo», la palabra inglesa «miss»
- «En medicina es igual» → `medicina`: una cruz de hospital aparece junto a la tabla
- «falso positivo» → `fpos`: «falso positivo» junto a «falsa alarma»
- «falso negativo» → `fneg`: «falso negativo» junto a «miss»

<!-- b2 -->
Cada error tiene su probabilidad: la de falsa alarma y la de miss. Y la probabilidad total de equivocarnos es la media ponderada de las dos: pe cero por la falsa alarma, más pe uno por el miss. Con números redondos: si el avión aparece una de cada diez veces, con cinco por ciento de falsas alarmas y veinte por ciento de misses, nos equivocamos un seis coma cinco por ciento.

- «Cada error tiene su probabilidad» → `prob`: sobre las casillas rojas, «P_FA» sobre la falsa alarma y «P_M» sobre el miss
- «la de falsa alarma» → `lafa`: se resalta «P_FA» sobre la casilla de la falsa alarma
- «la de miss» → `lam`: se resalta «P_M» sobre la casilla del miss
- «la probabilidad total de equivocarnos» → `total`: una llave rodea las dos casillas rojas, rotulada «probabilidad de error»
- «la media ponderada» → `media`: aparece «P_e =» en rojo, a la derecha de la tabla
- «pe cero por la falsa alarma» → `t1`: se completa «p₀ · P_FA»
- «más pe uno por el miss» → `t2`: se completa «+ p₁ · P_M»
- «Con números redondos» → `redondos`: la fórmula sube y debajo queda sitio para los números
- «una de cada diez veces» → `diez`: la fila de diez cuadraditos con uno en azul y «p₁ = 0,1 · p₀ = 0,9»
- «cinco por ciento de falsas alarmas» → `cinco`: «P_FA = 0,05»
- «veinte por ciento de misses» → `veinte`: «P_M = 0,2»
- «nos equivocamos» → `equivocamos`: se escribe la cuenta «0,9 · 0,05 + 0,1 · 0,2»
- «un seis coma cinco por ciento» → `resultado`: «= 0,065» en rojo, con «6,5 %»

---

# Escena 05 — UnaSenalEntera

**Capítulo YouTube:** De un número a una señal entera
**Objetivo:** pasar de una medición a una señal entera y anunciar la sorpresa: más datos no bastan.

## Narración

<!-- b1 -->
Todo esto es lo que viste en el capítulo de pruebas de hipótesis, con una única medición. Pero un radar no oye un número: oye una señal entera, muchas muestras seguidas. Y ahí nos espera una sorpresa: tener más datos no basta. Para verla, volvamos a la regla de decisión, y hagámoslo con un ejemplo muy pequeño.

- «el capítulo de pruebas de hipótesis» → `cap9`: sobre la tabla, la etiqueta «Capítulo 9 · Pruebas de hipótesis»
- «una única medición» → `una`: corte; un eje con un solo punto «r»
- «un radar no oye un número» → `nonum`: el punto se tacha
- «una señal entera» → `entera`: en su lugar, una fila de barras: la señal medida, muestra a muestra
- «muchas muestras seguidas» → `muchas`: la fila se alarga hacia la derecha con barras nuevas
- «una sorpresa» → `sorpresa`: un signo «!» ámbar sobre la fila
- «tener más datos no basta» → `nobasta`: «más datos» y, tachado, «mejor decisión»
- «la regla de decisión» → `regla`: una caja «regla de decisión» entra con rebote
- «un ejemplo muy pequeño» → `pequeno`: la fila se reduce a un solo número «r» y dos casillas H₀ y H₁

---

# Escena 06 — DosCurvas

**Capítulo YouTube:** Una medición: dos densidades uniformes
**Objetivo:** fijar un ejemplo pequeño: una medición con densidades uniformes bajo cada hipótesis, y calcular sus alturas a partir de que el área vale uno.

## Narración

<!-- b1 -->
Imagina una medición, un solo número. Bajo la hipótesis cero, ese número puede valer cualquier cosa entre menos uno y uno, con la misma probabilidad. Bajo la hipótesis uno, cualquier cosa entre menos un medio y un medio. Y a priori, la hipótesis cero es tres veces más probable que la uno: tres cuartos frente a un cuarto.

- «Imagina una medición» → `medicion`: un eje horizontal con el punto de una medición
- «un solo número» → `numero`: la letra «r» sobre el punto
- «Bajo la hipótesis cero» → `bajoh0`: «H₀» en magenta junto al eje
- «entre menos uno y uno» → `m11`: marcas −1 y 1 en el eje y un tramo magenta entre ellas
- «con la misma probabilidad» → `igual`: sobre el tramo, puntos magenta que caen repartidos por igual
- «Bajo la hipótesis uno» → `bajoh1`: «H₁» en azul
- «entre menos un medio y un medio» → `mm`: marcas −½ y ½ y un tramo azul más corto, dentro del magenta
- «a priori» → `apriori`: las palabras «a priori» en ámbar
- «tres veces más probable» → `tres`: la «H₀» crece frente a la «H₁»
- «tres cuartos frente a un cuarto» → `p34`: «p₀ = ¾ · p₁ = ¼»

<!-- b2 -->
¿Qué altura tienen esas dos curvas? El área de cada una tiene que valer uno. La primera mide dos de ancho, así que su altura es un medio. La segunda mide uno de ancho, así que su altura es uno. Son las densidades de la medición bajo cada hipótesis: nos dicen cuánto cabe esperar cada valor, según quién sea la verdadera.

- «¿Qué altura tienen esas dos curvas?» → `altura`: dos rectángulos planos sobre los tramos, con un «?» sobre su altura
- «El área de cada una tiene que valer uno» → `area`: los dos rectángulos se rellenan y se rotula «área = 1»
- «La primera mide dos de ancho» → `ancho2`: una llave de ancho 2 bajo el rectángulo magenta
- «su altura es un medio» → `alto12`: «2 · alto = 1 → alto = ½»; el rectángulo magenta sube a ½
- «La segunda mide uno de ancho» → `ancho1`: una llave de ancho 1 bajo el rectángulo azul
- «su altura es uno» → `alto1`: «1 · alto = 1 → alto = 1»; el rectángulo azul sube a 1
- «las densidades» → `densidades`: las etiquetas «f(r | H₀)» y «f(r | H₁)» sobre cada rectángulo
- «cuánto cabe esperar cada valor» → `esperar`: puntos que caen sobre cada rectángulo, más seguidos donde el rectángulo es más alto
- «según quién sea la verdadera» → `verdadera`: los dos rectángulos se turnan, uno se enciende y el otro se apaga, con un «?»

---

# Escena 07 — LaReglaDeDecision

**Capítulo YouTube:** La regla: curvas escaladas por su a priori
**Objetivo:** la regla MAP como «dos curvas escaladas por su a priori: gana la más alta», y comprobar que con una medición siempre se decide lo mismo y el error es un cuarto.

## Narración

<!-- b1 -->
Ahora, la regla. Midiendo un valor, la probabilidad de cada hipótesis, ya con el dato en la mano, es proporcional a su curva por su probabilidad a priori. Así que dibujamos cada curva multiplicada por su a priori, y decidimos por la más alta en el valor medido. Es la regla que minimiza la probabilidad de error.

- «Ahora, la regla» → `regla`: corte; los dos rectángulos de la escena 6 y la palabra «regla» en ámbar
- «Midiendo un valor» → `valor`: un punto «r» cae sobre el eje
- «la probabilidad de cada hipótesis» → `probh`: aparecen «P(H₀ | r)» y «P(H₁ | r)»
- «ya con el dato en la mano» → `dato`: el punto «r» se resalta
- «proporcional a su curva» → `prop`: se construye «P(Hᵢ | r) ∝ f(r | Hᵢ)»
- «su probabilidad a priori» → `pi`: se completa «P(Hᵢ | r) ∝ pᵢ · f(r | Hᵢ)»
- «dibujamos cada curva multiplicada» → `escalar`: cada rectángulo se encoge al multiplicarse por su a priori
- «decidimos por la más alta» → `alta`: una flecha ámbar señala la curva más alta sobre el punto «r»
- «en el valor medido» → `medido`: la flecha ámbar baja hasta el punto «r» sobre el eje
- «minimiza la probabilidad de error» → `minimiza`: «error mínimo» con la palabra «error» en rojo

<!-- b2 -->
Hagamos la cuenta. La hipótesis cero escalada vale tres cuartos por un medio: tres octavos. La hipótesis uno escalada vale un cuarto por uno: un cuarto, o dos octavos. En todos los puntos donde las dos existen, gana la cero. Nunca conviene decir hache uno.

- «Hagamos la cuenta» → `cuenta`: los dos rectángulos escalados quedan a la vista
- «La hipótesis cero escalada» → `h0esc`: el rectángulo magenta se resalta
- «tres cuartos por un medio» → `c0`: se escribe «¾ · ½»
- «tres octavos» → `o3`: «= 3/8» y el rectángulo magenta baja a esa altura
- «un cuarto por uno» → `c1`: se escribe «¼ · 1»
- «o dos octavos» → `o2`: «= ¼ = 2/8» y el rectángulo azul baja a esa altura, por debajo del magenta
- «En todos los puntos donde las dos existen» → `puntos`: un punto «r» barre el tramo de −½ a ½
- «gana la cero» → `gana`: ese tramo se sombrea en magenta
- «Nunca conviene decir hache uno» → `nunca`: una cruz roja sobre «H₁»

<!-- b3 -->
La mejor regla posible con esta medición es decir siempre «solo ruido». Y solo nos equivocamos cuando en realidad era hache uno, que pasa una de cada cuatro veces: la probabilidad de error es un cuarto. Parece triste. Veamos qué pasa si en vez de una medición hacemos dos.

- «decir siempre» → `siempre`: un cartel «siempre H₀» en ámbar
- «nos equivocamos» → `equivocamos`: el rectángulo azul de H₁ se tiñe de rojo: esos casos son errores
- «una de cada cuatro veces» → `cuatro`: cuatro casillas con una en rojo
- «la probabilidad de error es un cuarto» → `pe`: «P_e = ¼» en rojo
- «Parece triste» → `triste`: el «¼» tiembla un instante
- «Veamos qué pasa» → `veamos`: junto al «¼», aparece la pregunta «¿y con dos?» en ámbar
- «hacemos dos» → `dos`: aparece un segundo eje, r₂, perpendicular al primero

---

# Escena 08 — DosMediciones

**Capítulo YouTube:** Dos mediciones: de la recta al plano
**Objetivo:** con dos mediciones independientes la densidad conjunta es un cuadrado; aplicar la misma regla de escalar y comparar.

## Narración

<!-- b1 -->
Ahora tenemos dos mediciones independientes, cada una con las mismas reglas de antes. Como son independientes, la densidad conjunta es el producto de las dos. Bajo la hipótesis cero, el par cae en un cuadrado de lado dos, de área cuatro: su altura es un cuarto. Bajo la hipótesis uno, en un cuadrado de lado uno, de área uno: su altura es uno.

- «dos mediciones independientes» → `dos`: los ejes r₁ y r₂; sobre cada uno, su rectángulo de antes
- «las mismas reglas de antes» → `reglas`: los dos rectángulos de la escena anterior se resaltan
- «Como son independientes» → `indep`: entre los dos ejes aparece el signo «⟂»
- «la densidad conjunta es el producto» → `producto`: se construye «f(r₁, r₂) = f(r₁) · f(r₂)»
- «Bajo la hipótesis cero» → `bajoh0`: en el plano aparece un cuadrado magenta de lado 2, centrado en el origen
- «de área cuatro» → `a4`: «lado 2 → área 4»
- «su altura es un cuarto» → `alto14`: «altura = ¼»
- «Bajo la hipótesis uno» → `bajoh1`: un cuadrado azul de lado 1, dentro del grande
- «de área uno» → `a1`: «lado 1 → área 1»
- «su altura es uno» → `alto1`: «altura = 1»

<!-- b2 -->
La regla es exactamente la misma: escalar por el a priori y comparar. La hipótesis cero vale tres cuartos por un cuarto, tres dieciseisavos. La hipótesis uno vale un cuarto por uno, cuatro dieciseisavos. Cuatro es mayor que tres. Así que dentro del cuadrado pequeño, gana la hipótesis uno, y fuera de él, la cero.

- «escalar por el a priori» → `escalar`: «× p₀» sobre el cuadrado grande y «× p₁» sobre el pequeño
- «y comparar» → `comparar`: dos barras de altura, una junto a la otra, listas para compararse
- «tres cuartos por un cuarto» → `c0`: se escribe «¾ · ¼»
- «tres dieciseisavos» → `d3`: «= 3/16» y la barra magenta sube a esa altura
- «un cuarto por uno» → `c1`: se escribe «¼ · 1»
- «cuatro dieciseisavos» → `d4`: «= 4/16» y la barra azul sube a esa altura
- «Cuatro es mayor que tres» → `mayor`: «4 > 3» en ámbar entre las dos barras
- «dentro del cuadrado pequeño» → `dentro`: el cuadrado pequeño se pinta de azul y se rotula «decido H₁»
- «fuera de él» → `fuera`: el resto del cuadrado grande se pinta de gris y se rotula «decido H₀»

---

# Escena 09 — RegionesYError

**Capítulo YouTube:** Las regiones de decisión y el error
**Objetivo:** ver que la regla no cambia, solo dónde vive la medición, y calcular el error con dos mediciones (3/16 en vez de ¼).

## Narración

<!-- b1 -->
Fíjate en lo que ha cambiado: lo que antes eran tramos de una recta ahora son regiones de un plano. Decidimos «hay señal» si el par de mediciones cae en el cuadrado pequeño, y «solo ruido» si cae fuera. Con tres mediciones serían regiones de un espacio de tres dimensiones. La regla no cambia; cambia dónde vive la medición.

- «tramos de una recta» → `recta`: corte; la recta de la escena 7 con sus tramos de decisión
- «regiones de un plano» → `plano`: la recta se funde con el plano y sus dos regiones
- «hay señal» → `haysenal`: el cuadrado pequeño azul con el rótulo «hay señal»
- «solo ruido» → `solo`: el resto gris con el rótulo «solo ruido»
- «tres mediciones» → `tres`: los ejes se inclinan y aparece r₃
- «tres dimensiones» → `tresd`: un cubo pequeño dentro de otro más grande
- «La regla no cambia» → `nocambia`: la desigualdad «p₁ f(**r** | H₁) ≷ p₀ f(**r** | H₀)» se construye pieza a pieza
- «dónde vive la medición» → `vive`: la «r» en negrita se resalta

<!-- b2 -->
¿Cuánto nos equivocamos ahora? Si es hache uno, el par siempre cae en el cuadrado pequeño, así que acertamos: cero errores. Si es hache cero, que pasa tres de cada cuatro veces, nos equivocamos cuando el par cae en el cuadrado pequeño, que es una de cada cuatro. Tres cuartos por un cuarto: tres dieciseisavos.

- «¿Cuánto nos equivocamos ahora?» → `cuanto`: vuelve el cuadrado grande con el pequeño dentro y una pregunta en rojo
- «Si es hache uno» → `esh1`: una nube de puntos azules, todos dentro del cuadrado pequeño
- «así que acertamos» → `acertamos`: un tilde verde sobre la nube azul
- «cero errores» → `cero`: tildes verdes y «0 errores»
- «Si es hache cero» → `esh0`: una nube de puntos magenta repartida por el cuadrado grande
- «tres de cada cuatro veces» → `tres4`: cuatro casillas, tres en magenta
- «nos equivocamos cuando el par cae» → `cae`: los puntos magenta que caen dentro del cuadrado pequeño se marcan en rojo
- «una de cada cuatro» → `uno4`: «¼ de los puntos»
- «Tres cuartos por un cuarto» → `cuentas`: se escribe «¾ · ¼ + ¼ · 0»
- «tres dieciseisavos» → `d3`: «= 3/16» en rojo

<!-- b3 -->
Tres dieciseisavos, cero coma uno ocho siete cinco, es menos que un cuarto. Con una medición nos equivocábamos una de cada cuatro veces; con dos, algo menos de una de cada cinco. Más datos, mejor decisión. Ahora viene la pregunta obvia: si tengo dos mediciones, ¿no bastaría con promediarlas?

- «cero coma uno ocho siete cinco» → `decimal`: «3/16 = 0,1875»
- «menos que un cuarto» → `menos`: «0,1875 < 0,25»
- «Con una medición» → `con1`: una barra de error de 0,25 en rojo
- «con dos» → `con2`: debajo, una barra más corta de 0,1875
- «Más datos, mejor decisión» → `mejor`: un tilde verde junto a las dos barras
- «la pregunta obvia» → `obvia`: un «?» ámbar
- «¿no bastaría con promediarlas?» → `promediarlas`: entra el cartel «(r₁ + r₂) / 2» entre las dos mediciones

---

# Escena 10 — ElPromedio

**Capítulo YouTube:** Promediar las dos mediciones
**Objetivo:** ver que el promedio de las dos mediciones se distribuye como un triángulo y que, escalado por el a priori, la hipótesis uno nunca gana: el error vuelve a ser un cuarto.

## Narración

<!-- b1 -->
Probemos la idea más natural. Tengo dos mediciones y decido promediarlas: el número de resumen es a igual a erre uno más erre dos, entre dos. ¿Cómo se distribuye ese promedio? Hay muchas maneras de obtener un valor cerca del centro, sumando un número alto y otro bajo, y pocas de obtener uno en el borde. Sale un triángulo.

- «Probemos la idea más natural» → `natural`: corte; el plano con los dos cuadrados y la diagonal r₁ = r₂ en trazo fino
- «Tengo dos mediciones» → `tengo`: dos puntos «r₁» y «r₂» se resaltan sobre sus ejes
- «decido promediarlas» → `promediar`: los puntos del plano se proyectan sobre la diagonal
- «a igual a» → `a`: aparece «a =»
- «erre uno» → `r1`: se completa «a = (r₁»
- «más erre dos» → `r2`: se completa «a = (r₁ + r₂»
- «entre dos» → `ent2`: se completa «a = (r₁ + r₂) / 2»
- «¿Cómo se distribuye ese promedio?» → `distrib`: a la derecha, un eje «a» vacío con una pregunta
- «Hay muchas maneras» → `maneras`: varias parejas de puntos distintas, unidas por flechas al mismo valor de «a»
- «cerca del centro» → `centro`: muchas parejas distintas apuntan al mismo valor central
- «un número alto y otro bajo» → `altobajo`: el ejemplo «1 y −1 → 0»
- «en el borde» → `borde`: casi ninguna pareja llega al borde: solo «1 y 1 → 1»
- «Sale un triángulo» → `triangulo`: se dibuja un triángulo sobre el eje «a»

<!-- b2 -->
Bajo la hipótesis cero, un triángulo de base dos y altura uno. Bajo la hipótesis uno, un triángulo de base uno y altura dos. Ya sabes lo que sigue: escalamos por el a priori. La hipótesis cero llega a tres cuartos en el centro. La hipótesis uno, a un medio. Tres cuartos es más que un medio.

- «Bajo la hipótesis cero» → `t0`: el triángulo magenta, de −1 a 1
- «base dos y altura uno» → `b2a1`: «base 2 · altura 1», con el área sombreada
- «Bajo la hipótesis uno» → `t1`: el triángulo azul, de −½ a ½, más alto
- «base uno y altura dos» → `b1a2`: «base 1 · altura 2»
- «Ya sabes lo que sigue» → `sabes`: «× p₀» y «× p₁» asoman junto a cada triángulo
- «escalamos por el a priori» → `escalamos`: los dos triángulos bajan al multiplicarse por p₀ y p₁
- «La hipótesis cero llega» → `llega`: el pico magenta baja, con un contador de altura que va de 1 hacia ¾
- «tres cuartos en el centro» → `tc`: el pico magenta queda en «¾»
- «a un medio» → `medio`: el pico azul queda en «½»
- «Tres cuartos es más que un medio» → `mas`: «¾ > ½» en ámbar

<!-- b3 -->
Y no solo en el centro: a medida que nos alejamos, la curva de la hipótesis uno baja más deprisa que la otra. En ningún punto le gana. Así que la regla óptima sobre el promedio vuelve a ser: decir siempre «solo ruido». Y el error vuelve a ser un cuarto. Exactamente lo mismo que con una sola medición.

- «a medida que nos alejamos» → `alejamos`: un punto «a» se aleja del centro hacia la derecha
- «baja más deprisa» → `deprisa`: el triángulo azul llega a cero en ½ mientras el magenta sigue en pie
- «En ningún punto le gana» → `ninguno`: todo el eje se sombrea de magenta
- «la regla óptima sobre el promedio» → `optima`: «regla óptima» sobre el eje
- «decir siempre» → `siempre`: el cartel «siempre H₀»
- «vuelve a ser un cuarto» → `uncuarto`: «P_e = ¼» en rojo
- «con una sola medición» → `igual`: junto a ese «¼», la barra de una sola medición de la escena 7, con un «=» entre las dos

---

# Escena 11 — QueSePerdio

**Capítulo YouTube:** ¿Qué se perdió al promediar?
**Objetivo:** ver qué información tira el promedio (dos pares distintos dan el mismo promedio), fijar el lema del capítulo y plantear la pregunta del E2: ¿hay un resumen que no tire nada?

## Narración

<!-- b1 -->
¿Qué ha pasado? Dos pares de mediciones muy distintos pueden dar el mismo promedio. Uno y menos uno, y cero y cero, promedian cero los dos. Con el par entero podíamos distinguir cuál hacía más probable la hipótesis uno. Con el promedio, ya no. Al resumir, tiramos justo lo que sabía la forma del par.

- «¿Qué ha pasado?» → `pasado`: corte; el plano con los dos cuadrados
- «Dos pares de mediciones muy distintos» → `pares`: dos puntos en el plano, uno en una esquina del cuadrado grande y otro en el centro
- «el mismo promedio» → `mismo`: los dos puntos se proyectan sobre la diagonal en el mismo sitio, y una perpendicular los une
- «Uno y menos uno» → `um`: el primer punto se rotula «(1, −1)»
- «cero y cero» → `cc`: el segundo se rotula «(0, 0)»
- «promedian cero los dos» → `cero`: sobre la diagonal, «a = 0»
- «el par entero» → `entero`: el punto (0, 0) cae dentro del cuadrado pequeño, el (1, −1) fuera
- «distinguir» → `distinguir`: uno se tiñe de azul y el otro de gris
- «Con el promedio, ya no» → `yano`: los dos puntos coinciden en un solo punto sobre la diagonal
- «tiramos» → `tiramos`: la dirección perpendicular a la diagonal se tacha en rojo

<!-- b2 -->
Esta es la lección del capítulo: más datos no ayudan solos. Hay que procesarlos bien. Pero entonces surge la pregunta importante: en el caso que de verdad nos interesa, una señal conocida enterrada en ruido gaussiano, ¿hay un resumen que lo aproveche todo y no tire nada? Sí. Y es sorprendentemente sencillo: un único número.

- «la lección del capítulo» → `leccion`: corte; la palabra «lección» en ámbar
- «más datos no ayudan solos» → `nosolos`: «más datos» y, tachado, «mejor decisión»
- «Hay que procesarlos bien» → `procesar`: una caja «procesar» entre los datos y la decisión
- «la pregunta importante» → `importante`: la caja «procesar» se aparta y en el centro entra un «?» ámbar
- «en el caso que de verdad nos interesa» → `interesa`: el «?» se encoge y deja sitio a un eje con casillas vacías
- «una señal conocida» → `conocida`: una fila de barras azules fijas: la señal conocida
- «enterrada en ruido gaussiano» → `ruidog`: encima, el ruido magenta y una campana de Gauss
- «¿hay un resumen que lo aproveche todo» → `resumen`: una flecha ámbar de la fila de barras a un recuadro vacío
- «no tire nada» → `nada`: una tilde verde junto al recuadro
- «Y es sorprendentemente sencillo» → `sencillo`: el recuadro se agranda
- «un único número» → `unico`: dentro del recuadro, un «?» ámbar grande

---

# Escena 12 — Cierre

**Capítulo YouTube:** Lo que viene: toda la señal en un solo número

## Narración

<!-- b1 -->
Resumimos. La regla de decisión no cambia, tengas uno, dos o mil datos: escalar por el a priori y quedarse con la más alta. Pero promediar los datos puede tirar justo lo que necesitabas, y entonces más datos no bastan. Hay que saber resumirlos sin perder nada. Lo vemos en el próximo episodio: toda la señal en un solo número.

- «Resumimos» → `resumen`: corte; la palabra «resumen» en ámbar
- «no cambia» → `nocambia`: la desigualdad «p₁ f(r | H₁) ≷ p₀ f(r | H₀)» con un candado
- «uno, dos o mil datos» → `datos`: tres ejes: uno, un plano y una nube de ejes que se multiplican
- «escalar por el a priori» → `escalar`: dos curvas que se encogen con «× p₀» y «× p₁»
- «quedarse con la más alta» → `alta`: una flecha ámbar señala la más alta
- «promediar los datos» → `promediar`: el cartel «(r₁ + r₂) / 2» aplasta los puntos sobre la diagonal
- «puede tirar justo lo que necesitabas» → `tirar`: la dirección perpendicular se tacha en rojo
- «más datos no bastan» → `nobastan`: «más datos» y, tachado, «mejor decisión»
- «sin perder nada» → `sinperder`: un recuadro con un tilde verde
- «el próximo episodio» → `proximo`: aparece la tarjeta «Episodio 2»
- «toda la señal en un solo número» → `titulo`: «Toda la señal en un solo número» entra con rebote
