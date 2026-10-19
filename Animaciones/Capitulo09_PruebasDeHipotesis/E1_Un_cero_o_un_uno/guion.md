# Episodio 1 — ¿Un cero o un uno?

Capítulo 9 (Pruebas de hipótesis), episodio 1 de 6. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 01 a 05), más un gancho y un cierre nuevos.

**Estado:** **Subido a YouTube en privado** el 19/10/2026: render final 1080p60 de 10:51, título buscable, descripción con el capítulo del libro y `capitulos.txt`, subtítulos, categoría Educación (https://youtu.be/RRY9hYkdNrY). Residuos limpiados; la caché de voz está en `media/voiceovers/`: se rehace con `python rehacer.py Capitulo09_PruebasDeHipotesis E1`. **Falta**: publicarlo (lo hace el usuario).

Texto nuevo (marcado con ⭐, **aprobado**):
- ⭐ Escena 01 (gancho): «Mides uno coma tres voltios. Si ceros y unos se envían igual de a menudo, dices uno. Si hay más ceros, con la misma medición, dices cero. Hoy veremos por qué, y por qué ninguna regla lo hace mejor.»
- ⭐ Escena 14 (cierre): toma el bloque b6 de la escena 05 del guion base (la pregunta de cuánto y cómo se equivoca), le suma un resumen de una frase y anuncia E2 por su título, «Dos maneras de equivocarse».

Nota para el episodio anterior: el cierre del E5 del capítulo 8 («¿Dos termómetros mejor que uno?») tiene que anunciar este título, «¿Un cero o un uno?».
El cierre de este episodio anuncia el E2, «Dos maneras de equivocarse».

Reparto de las escenas del guion base: 01 → escenas 03 y 04; 02 → 05, 06 y 07; 03 → 08 y 09; 04 → 10 y 11; 05 → 12 y 13 (su b6 pasa al cierre, escena 14).
Solo se partieron bloques enteros en escenas atómicas: el texto del guion base no cambia.

Duración estimada: ~1.600 palabras, unos 10,5–11 min de voz. Si `ritmo.py` da más de ~10,5 min, el primer recorte candidato es la escena 13, bloque b2 (tres hipótesis).

Notas para animar:
- Colores, iguales que en E2: `RUIDO` (magenta) para la campana del cero, H₀ y «Se envió 0»; `SENAL` (azul) para la campana del uno, H₁ y «Se envió 1»; `MEDIDA` (cian) para lo recibido y la regla en 1,3; `ESTIMACION` (ámbar) para la decisión, el cruce y el umbral; `ERROR` (rojo) para los fallos; `VERDE` para los aciertos.
- Piezas que ya existen en `comun/figuras.py`: `canal7` y `TablaCanal` (el canal del Cap. 7 y su tabla conjunta), `Arbol07` (el árbol de Bayes), `dens3`, `cola3` y `umbral3` (campanas, colas y umbral), `Curva` y `gaussiana`. Las campanas escalables con su factor y las regiones coloreadas sobre el eje son nuevas (sección «capítulo 09, episodio 1»).
- Números: alturas en 1,3 = 0,171 y 0,312; escaladas 0,120 y 0,094; cruce en 1 + ln(7/3)/2 = 1,42.

---

# Escena 01 — Gancho

**Capítulo YouTube:** La misma medición, dos decisiones

## Narración

<!-- b1 -->
Mides uno coma tres voltios. Si ceros y unos se envían igual de a menudo, dices uno. Si hay más ceros, con la misma medición, dices cero. Hoy veremos por qué, y por qué ninguna regla lo hace mejor.

- «Mides uno coma tres voltios» → `medida`: las dos campanas (la del cero en magenta, la del uno en azul) entran ya dibujadas y una regla vertical cian cae en «r = 1,3»
- «Si ceros y unos» → `apriori`: arriba, «Ceros» y «Unos» con dos casillas vacías
- «igual de a menudo» → `iguales`: arriba, «p₀ = 0,5 · p₁ = 0,5»; las dos campanas a la misma altura
- «dices uno» → `uno`: el corte con la campana azul, más alto, se ilumina; junto a la regla, «Decir 1» en ámbar
- «Si hay más ceros» → `masceros`: los a priori pasan a «0,7 · 0,3» y las campanas se reescalan en vivo
- «con la misma medición» → `misma`: la regla cian late, sin moverse
- «dices cero» → `cero`: «Decir 1» se tacha y se cambia por «Decir 0»
- «Hoy veremos por qué» → `porque`: todo se atenúa; un «?» ámbar grande
- «ninguna regla lo hace mejor» → `mejor`: aparece «Ninguna regla falla menos» con un tilde verde

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** ¿Un cero o un uno?

## Narración

<!-- b1 -->
¿Un cero o un uno?

- «¿Un cero» → `t1`: «¿Un cero» entra con rebote
- «o un uno?» → `t2`: «o un uno?» entra debajo, con la etiqueta «Capítulo 9 · Pruebas de hipótesis»

---

# Escena 03 — NoEsUnBit

**Capítulo YouTube:** Decidir no es estimar
**Objetivo:** plantear el problema del capítulo (elegir entre dos explicaciones a partir de un dato) y dar nombre a las hipótesis y a las probabilidades a priori.

## Narración

<!-- b1 -->
En el capítulo anterior quedó una pregunta abierta. Por un canal se envían
ceros y unos, recibes un uno, y la mejor estimación de lo enviado era cero coma
setenta y nueve. Pero eso no es un bit. El receptor de tu móvil no puede
entregar cero coma setenta y nueve: tiene que elegir. Cero o uno. Eso es
decidir, y es el tema de este capítulo.

- «En el capítulo anterior» → `anterior`: etiqueta pequeña «Capítulo 8» arriba a la izquierda
- «Por un canal se envían» → `canal`: el canal del Cap. 7 (`canal7`) entra al centro, con bits que lo cruzan
- «recibes un uno» → `recibe`: a la salida del canal aparece un «1» cian
- «cero coma setenta y nueve» → `est`: debajo, «0,79» en ámbar entre un «0» y un «1», con un «?» (el dibujo del Cap. 8)
- «no es un bit» → `nobit`: el 0,79 se tacha en rojo
- «El receptor de tu móvil» → `movil`: un ícono de móvil al final del canal
- «tiene que elegir» → `elegir`: del móvil salen dos casillas, «0» y «1»
- «Eso es decidir» → `decidir`: «Decidir» entra con `pop` en ámbar
- «el tema de este capítulo» → `tema`: debajo, «Pruebas de hipótesis»

<!-- b2 -->
Pongamos nombres. Cada explicación posible se llama hipótesis. La hipótesis
cero, hache cero, dice: se envió un cero. La hipótesis uno, hache uno, dice: se
envió un uno. Solo una es verdad, y no sabemos cuál. Tenemos dos cosas: un
dato, que es lo recibido, y lo que ya sabíamos antes de mirar.

- «Pongamos nombres» → `limpia`: corte; queda solo el «1» recibido arriba
- «se llama hipótesis» → `hip`: «Hipótesis» en ámbar
- «hache cero» → `h0`: casilla magenta «H₀ · Se envió 0»
- «se envió un cero» → `env0`: de la casilla H₀ sale un «0» pequeño hacia la derecha
- «hache uno» → `h1`: casilla azul «H₁ · Se envió 1»
- «Solo una es verdad» → `una`: sobre las dos casillas, un tilde tapado por un «?»
- «Tenemos dos cosas» → `dos`: debajo, dos huecos vacíos
- «un dato» → `dato`: en el primer hueco, «Dato: recibido 1» en cian
- «antes de mirar» → `antes`: en el segundo, «Lo que sabíamos antes» en ámbar

<!-- b3 -->
Lo que ya sabíamos es que se envía un cero el setenta por ciento de las veces
y un uno el treinta. Son las probabilidades a priori, pe cero y pe uno: valen
antes de recibir nada. Y sabemos cómo es el canal: cambia el bit una de cada
diez veces.

- «el setenta por ciento» → `p0`: bajo H₀, «70 %»
- «un uno el treinta» → `p1`: bajo H₁, «30 %»
- «probabilidades a priori» → `apriori`: rótulo «A priori»; los porcentajes pasan a «p₀ = 0,7» y «p₁ = 0,3»
- «antes de recibir nada» → `nada`: el «1» recibido se atenúa
- «cómo es el canal» → `canal`: el canal vuelve, pequeño, abajo
- «una de cada diez veces» → `diez`: un bit cruza y se voltea; «10 %» en rojo sobre el canal

---

# Escena 04 — MaximoAPosteriori

**Capítulo YouTube:** La regla del máximo a posteriori
**Objetivo:** calcular las probabilidades a posteriori con el árbol del canal y quedarse con la mayor.

## Narración

<!-- b1 -->
Recibes un uno. Hay dos caminos para eso. Se envió un uno y llegó bien: cero
coma tres por cero coma nueve, cero coma veintisiete. O se envió un cero y el
canal lo cambió: cero coma siete por cero coma uno, cero coma cero siete. Por
la regla de Bayes, la probabilidad de hache uno es cero coma setenta y nueve, y
la de hache cero, cero coma veintiuno.

- «Recibes un uno» → `recibe`: «Recibido 1» en cian a la derecha
- «dos caminos» → `arbol`: el árbol del Cap. 7 (`Arbol07`), con dos ramas que acaban en «Recibido 1»
- «Se envió un uno y llegó bien» → `rama1`: se ilumina la rama de arriba (azul)
- «cero coma tres por» → `m1`: al final de la rama, «0,3 · 0,9»
- «cero coma veintisiete» → `c027`: se completa «= 0,27»
- «el canal lo cambió» → `rama0`: se ilumina la rama de abajo (magenta), con el bit volteado
- «cero coma siete por» → `m0`: al final de la rama, «0,7 · 0,1»
- «cero coma cero siete» → `c007`: se completa «= 0,07»
- «la regla de Bayes» → `bayes`: suma «0,27 + 0,07 = 0,34» y la división «0,27 / 0,34»
- «cero coma setenta y nueve» → `p79`: barra azul «P(H₁ | 1) = 0,79»
- «cero coma veintiuno» → `p21`: barra magenta «P(H₀ | 1) = 0,21»

<!-- b2 -->
Esas son las probabilidades a posteriori: las de después de mirar. ¿Con cuál
te quedas? Con la mayor: dices uno. Y si recibes un cero, la cuenta da cero
coma noventa y cinco para el cero: dices cero. Esta regla se llama máximo a
posteriori. Es la tercera forma de medir el error del capítulo anterior, la de
acertar o fallar, que lleva a quedarse con lo más probable: la moda.

- «probabilidades a posteriori» → `apost`: sobre las barras, «A posteriori»
- «¿Con cuál» → `cual`: un «?» ámbar entre las dos barras
- «Con la mayor» → `mayor`: la barra de 0,79 se enmarca en ámbar
- «dices uno» → `di1`: debajo, «Decir 1»
- «si recibes un cero» → `rec0`: al lado, otro par de barras para «Recibido 0»
- «cero coma noventa y cinco» → `p95`: «0,955» en magenta y «0,045» en azul
- «dices cero» → `di0`: la barra de 0,955 se enmarca; «Decir 0»
- «máximo a posteriori» → `map`: título «Máximo a posteriori · MAP» con `pop`
- «la tercera forma» → `tres`: las tres casillas del Cap. 8: «Cuadrado → media», «Tamaño → mediana», «Acierto → moda»
- «la de acertar o fallar» → `acierto`: la tercera casilla, «Acierto → moda», se resalta
- «lo más probable» → `probable`: junto a ella, «Lo más probable»
- «la moda» → `moda`: la tercera casilla se enmarca en ámbar y una flecha la une con «MAP»

<!-- b3 -->
Aquí la regla acaba diciendo algo muy simple: cree lo que recibes. Parece
obvio. Pero ¿es de verdad lo mejor que se puede hacer? ¿Y será siempre así?

- «algo muy simple» → `simple`: corte; «Recibido 1 → Decir 1» y «Recibido 0 → Decir 0»
- «cree lo que recibes» → `cree`: una llave las agrupa: «Cree lo que recibes»
- «Parece» → `obvio`: un tilde gris al lado
- «lo mejor que se puede hacer» → `lamejor`: el tilde se cambia por «¿La mejor?»
- «¿Y será siempre así?» → `siempre`: debajo, «¿Siempre?» en ámbar, latiendo

---

# Escena 05 — CuatroReglas

**Capítulo YouTube:** Las cuatro reglas posibles
**Objetivo:** enumerar las cuatro reglas del canal y calcular cuánto falla cada una.

## Narración

<!-- b1 -->
Aquí se puede comprobar, porque solo hay cuatro reglas posibles. Lo recibido
solo puede ser un cero o un uno, y en cada caso hay que decir cero o uno. Dos
por dos, cuatro reglas. Calculemos cuánto falla cada una.

- «se puede comprobar» → `titulo`: título «Cuatro reglas» arriba
- «solo hay cuatro reglas» → `cuatro`: un «4» grande en ámbar junto al título
- «Lo recibido» → `rec`: columna «Recibido» con «0» y «1»
- «hay que decir cero o uno» → `decir`: al lado, columna «Decir» con dos huecos
- «Dos» → `dosxdos`: «2 × 2 = 4»
- «cuatro reglas.» → `tabla`: tabla vacía de cuatro renglones
- «cuánto falla cada una» → `error`: columna «Error» con cuatro «?»

<!-- b2 -->
Primera: creer lo recibido. Falla cuando el canal cambia el bit: un diez por
ciento. Segunda: decir siempre cero. Falla cuando se envió un uno: un treinta
por ciento. Tercera: decir siempre uno. Falla el setenta. Cuarta: llevar la
contraria. Falla el noventa. Gana la primera, que es la del máximo a posteriori.

- «Primera: creer lo recibido» → `r1`: renglón «Creer lo recibido (0 → 0, 1 → 1)»
- «el canal cambia el bit» → `cambia`: junto al renglón, un bit pequeño se voltea
- «un diez por ciento» → `e1`: «0,10»
- «decir siempre cero» → `r2`: renglón «Siempre 0»
- «Falla cuando se envió un uno» → `falla2`: junto al renglón, un «1» azul tachado
- «un treinta por ciento» → `e2`: «0,30»
- «decir siempre uno» → `r3`: renglón «Siempre 1»
- «Falla el setenta» → `e3`: «0,70»
- «llevar la contraria» → `r4`: renglón «Llevar la contraria (0 → 1, 1 → 0)»
- «Falla el noventa» → `e4`: «0,90»
- «Gana la primera» → `gana`: el primer renglón se enmarca en verde
- «máximo a posteriori» → `map`: etiqueta «MAP» junto al marco

---

# Escena 06 — LaCasillaPequena

**Capítulo YouTube:** En cada columna, lo que menos falla
**Objetivo:** ver con la tabla del canal por qué gana el máximo a posteriori: en cada columna se falla la casilla pequeña.

## Narración

<!-- b1 -->
¿Por qué gana? Mira la tabla del canal, columna por columna. En la columna de
recibir un uno hay dos casillas: cero coma veintisiete, se envió un uno, y cero
coma cero siete, se envió un cero. Si dices uno, aciertas la grande y fallas la
pequeña. Si dices cero, al revés. Elegir lo más probable es fallar la casilla
pequeña.

- «¿Por qué gana?» → `porque`: «¿Por qué?» en ámbar
- «la tabla del canal» → `tabla`: la tabla conjunta del Cap. 7 (`TablaCanal`): «0,63 · 0,07 / 0,03 · 0,27»
- «columna por columna» → `columnas`: las dos columnas se separan un poco
- «la columna de» → `col1`: se resalta la columna «Recibido 1»
- «cero coma veintisiete» → `c27`: la casilla 0,27 late (azul, «Se envió 1»)
- «cero coma cero siete» → `c07`: la casilla 0,07 late (magenta, «Se envió 0»)
- «Si dices uno» → `di1`: una flecha «Decir 1» apunta a la columna
- «aciertas la grande» → `grande`: 0,27 en verde, con un tilde
- «fallas la pequeña» → `falla`: 0,07 en rojo, con una cruz
- «Si dices cero, al revés» → `di0`: los colores se invierten un momento y vuelven
- «Elegir lo más probable» → `elegir`: rótulo «Elegir lo más probable» bajo la columna
- «fallar la casilla» → `pequena`: debajo, «= Fallar la pequeña»

<!-- b2 -->
En la otra columna pasa lo mismo: dices cero y fallas solo cero coma cero tres.
Y si en cada columna fallas lo menos posible, el total también es el menor
posible: cero coma cero siete más cero coma cero tres, un diez por ciento.
Ninguna regla puede bajar de ahí.

- «En la otra columna» → `col0`: se resalta la columna «Recibido 0»
- «dices cero» → `verde`: 0,63 en verde
- «cero coma cero tres» → `c03`: 0,03 en rojo
- «en cada columna» → `cada`: las dos casillas rojas laten a la vez
- «el menor» → `menor`: las dos casillas rojas vuelan hacia abajo
- «cero coma cero siete más» → `mas`: abajo, «0,07 +»
- «un diez por ciento» → `suma`: se completa «0,07 + 0,03 = 0,10»
- «Ninguna regla puede bajar de ahí» → `suelo`: una línea horizontal «Mínimo» bajo el 0,10

---

# Escena 07 — UnosRarisimos

**Capítulo YouTube:** Cuando lo de antes pesa más que el dato
**Objetivo:** ver, con unos rarísimos, que lo que se sabía antes puede pesar más que lo recibido.

## Narración

<!-- b1 -->
Ahora una pregunta, y piénsala antes de seguir. Supón que los unos fueran
rarísimos: uno de cada veinte. Recibes un uno. ¿Qué dices? La cuenta: se envió
un uno y llegó bien, cero coma cero cinco por cero coma nueve, cero coma cero
cuarenta y cinco. Se envió un cero y se cambió, cero coma noventa y cinco por
cero coma uno: cero coma cero noventa y cinco.

- «Ahora una pregunta» → `pregunta`: corte; un «?» ámbar grande
- «piénsala antes de seguir» → `pausa`: un reloj pequeño gira junto al «?»
- «los unos fueran» → `raros`: la casilla «Unos» en azul se encoge
- «uno de cada veinte» → `veinte`: fila de veinte bits, uno azul y diecinueve magenta; «p₁ = 0,05»
- «Recibes un uno» → `recibe`: «Recibido 1» en cian
- «¿Qué dices?» → `que`: dos botones, «Decir 0» y «Decir 1», con un «?»
- «se envió un uno y llegó bien» → `rama1`: el árbol; se ilumina la rama de arriba
- «cero coma cero cinco por» → `m1`: «0,05 · 0,9»
- «cero coma cero cuarenta y cinco» → `c045`: se completa «= 0,045»
- «Se envió un cero y se cambió» → `rama0`: se ilumina la rama de abajo
- «cero coma noventa y cinco por» → `m0`: «0,95 · 0,1»
- «cero coma cero noventa y cinco» → `c095`: se completa «= 0,095»

<!-- b2 -->
Es más probable que fuera un cero estropeado. La mejor regla es decir siempre
cero, sin mirar lo recibido: falla un cinco por ciento, y creer lo recibido
fallaría un diez. Lo que sabías antes puede pesar más que lo que ves. Decidir
bien es combinar las dos cosas.

- «un cero estropeado» → `gana0`: «0,095 > 0,045»; el botón «Decir 0» se ilumina
- «decir siempre» → `siempre0`: tarjeta «Siempre 0»
- «sin mirar lo recibido» → `sinmirar`: el «Recibido 1» se tacha
- «un cinco por ciento» → `e5`: «Siempre 0 → 0,05» en verde
- «fallaría un diez» → `e10`: «Creer → 0,10» en rojo
- «puede pesar más» → `balanza`: una balanza: «Lo que sabías» baja y «Lo que ves» sube
- «combinar las dos cosas» → `combinar`: la balanza se equilibra; «Decidir = combinar»

---

# Escena 08 — AbrirElCanal

**Capítulo YouTube:** El canal por dentro
**Objetivo:** ver que la medición es un número continuo, amplitud más ruido, y que cada hipótesis da una campana.

## Narración

<!-- b1 -->
Hasta ahora el canal era una caja que cambiaba bits. Vamos a abrirla. Un cero
se envía como cero voltios y un uno como dos voltios. Por el cable se le suma
ruido. Lo que llega, erre, es la amplitud enviada más el ruido. Esto se llama
modulación por amplitud de pulsos, y es la forma más simple de enviar bits.

- «una caja que cambiaba bits» → `caja`: la caja del canal al centro; un bit entra y sale volteado
- «Vamos a abrirla» → `abrir`: la tapa se levanta y la caja se vuelve un cable
- «cero voltios» → `v0`: un «0» entra como un nivel plano en «0 V»
- «dos voltios» → `v2`: un «1» entra como un pulso azul de «2 V»
- «se le suma» → `ruido`: un garabato magenta se suma al cable
- «Lo que llega, erre» → `r`: al final llega un punto cian que tiembla, «r»
- «la amplitud enviada» → `a`: fórmula: «R = A», con «A» en azul
- «más el ruido» → `v`: «+ V» en magenta
- «modulación por amplitud de pulsos» → `pam`: rótulo «PAM»
- «la forma más simple» → `tren`: un tren de pulsos de 0 V y 2 V pasa por el cable

<!-- b2 -->
El ruido es gaussiano: una campana centrada en cero, con un desvío de un
voltio. Si se envió un cero, lo que llega es solo ruido: una campana centrada
en cero. Si se envió un uno, llega dos más ruido: la misma campana, desplazada
hasta el dos. Dos campanas iguales, separadas dos voltios, que se solapan.

- «El ruido es gaussiano» → `ejes`: corte; un eje horizontal «r (V)» con marcas 0, 1 y 2
- «una campana centrada en cero» → `campana`: se dibuja la campana (`dens3`)
- «un desvío de un» → `desvio`: flecha de doble punta de 0 a 1 con «σ = 1»
- «Si se envió un cero» → `h0`: la campana se tiñe de magenta: «Si se envió 0»
- «solo ruido» → `solo`: un punto cian cae varias veces cerca de 0
- «Si se envió un uno» → `h1`: una copia se desliza hasta 2 y se tiñe de azul: «Si se envió 1»
- «desplazada hasta el dos» → `dos`: flecha de 0 a 2 sobre el eje
- «Dos campanas iguales» → `iguales`: las dos laten a la vez
- «que se solapan» → `solapan`: la zona común se rellena en gris tenue

---

# Escena 09 — Verosimilitud

**Capítulo YouTube:** La altura de cada campana
**Objetivo:** leer las alturas de las dos campanas en 1,3, llamarlas verosimilitud y ver que, con a priori iguales, el umbral queda a mitad de camino.

## Narración

<!-- b1 -->
Mides uno coma tres voltios. ¿Cero o uno? Ya no podemos contar casos como en la
tabla, porque la medición puede valer cualquier número. Lo que tenemos es la
altura de cada campana en ese punto: su densidad. La campana del cero vale ahí
cero coma diecisiete. La del uno, cero coma treinta y uno.

- «uno coma tres voltios» → `medida`: regla vertical cian en «r = 1,3»
- «¿Cero o uno?» → `pregunta`: «¿0 o 1?» arriba
- «contar casos como en la» → `tabla`: la tabla del canal aparece pequeña en una esquina y se tacha
- «cualquier número» → `eje`: un punto recorre el eje de punta a punta
- «altura de cada campana» → `alturas`: dos puntos donde la regla corta a las campanas
- «su densidad» → `dens`: rótulo «Densidad = altura»
- «cero coma diecisiete» → `a17`: segmento magenta hasta la campana del cero, «0,17»
- «cero coma treinta y uno» → `a31`: segmento azul hasta la del uno, «0,31»

<!-- b2 -->
Esa altura se llama verosimilitud: lo compatible que es lo que has medido con
cada hipótesis. Uno coma tres queda lejos del centro de una campana y cerca
del centro de la otra. Por eso es casi el doble de compatible con el uno.

- «se llama verosimilitud» → `vero`: «Verosimilitud» con `pop` en ámbar
- «lo compatible» → `fx`: «f(r | H₀) = 0,17» y «f(r | H₁) = 0,31»
- «con cada hipótesis» → `cada`: una línea une «f(r | H₀)» con la campana magenta y «f(r | H₁)» con la azul
- «lejos del centro» → `lejos`: flecha de 0 a 1,3 con «1,3»
- «cerca del centro de la otra» → `cerca`: flecha de 2 a 1,3 con «0,7»
- «casi el doble» → `doble`: «0,31 / 0,17 ≈ 1,8»

<!-- b3 -->
Si ceros y unos fueran igual de frecuentes, con eso bastaría: gana la campana
más alta. Las dos se cruzan justo en uno, a mitad de camino. Por encima de un
voltio dirías uno, y por debajo, cero. Pero no son igual de frecuentes: hay más
ceros. ¿Cómo se mezcla eso con las campanas?

- «igual de frecuentes» → `iguales`: «p₀ = p₁» arriba
- «gana la campana más alta» → `gana`: el punto azul se ilumina; «Decir 1»
- «se cruzan justo en uno» → `cruce`: un punto ámbar en el cruce, «1»
- «a mitad de camino» → `mitad`: llaves de 0 a 1 y de 1 a 2
- «dirías uno» → `der`: a la derecha de 1, el eje se colorea de azul: «Decir 1»
- «por debajo, cero» → `izq`: a la izquierda, de magenta: «Decir 0»
- «no son igual de frecuentes» → `noiguales`: «p₀ = p₁» se tacha
- «hay más» → `mas`: «p₀ = p₁» se cambia por «p₀ = 0,7 · p₁ = 0,3»
- «¿Cómo se mezcla eso» → `mezcla`: un «?» ámbar entre los a priori y las campanas

---

# Escena 10 — CampanasEscaladas

**Capítulo YouTube:** Bayes con campanas
**Objetivo:** escribir Bayes con densidades, tachar el denominador común y escalar cada campana por su a priori.

## Narración

<!-- b1 -->
Se mezcla con la regla de Bayes, igual que antes, pero con alturas en lugar de
probabilidades. La probabilidad a posteriori de hache uno, habiendo medido
erre, es pe uno por la altura de la campana del uno en erre, dividida entre la
densidad total de erre.

- «la regla de Bayes» → `bayes`: rótulo «Bayes» y, pequeño, el árbol de la escena 04
- «con alturas» → `alturas`: el árbol se cambia por las dos campanas pequeñas
- «La probabilidad a posteriori de hache uno» → `post`: «P(H₁ | r) =»
- «habiendo medido erre» → `r`: la «r» de la fórmula late en cian
- «pe uno» → `p1`: «p₁ ·»
- «la altura de la campana del uno» → `f1`: «f(r | H₁)» en azul
- «la densidad total de erre» → `den`: raya de fracción y «f(r)» debajo

<!-- b2 -->
Para hache cero es igual, con el mismo denominador. Y como solo queremos saber
cuál de las dos es mayor, ese denominador sobra: es positivo y está en los dos
lados. Basta comparar pe uno por su campana con pe cero por la suya.

- «Para hache cero es igual» → `h0`: debajo, «P(H₀ | r) = p₀ · f(r | H₀) / f(r)» con lo de H₀ en magenta
- «el mismo denominador» → `mismo`: los dos «f(r)» se marcan
- «cuál de las dos es mayor» → `comparar`: entre las dos fórmulas, «≷»
- «ese denominador sobra» → `tacha`: los dos «f(r)» se tachan y se van
- «es positivo» → `positivo`: «f(r) > 0» pequeño, al lado
- «Basta comparar» → `regla`: queda «p₁ · f(r | H₁) ≷», con lo de H₁ en azul
- «con pe cero por la suya» → `suya`: a la derecha del «≷», «p₀ · f(r | H₀)» en magenta

<!-- b3 -->
En el dibujo, cada campana se multiplica por su probabilidad a priori. La del
cero se queda en el setenta por ciento de su altura. La del uno se encoge al
treinta. Y se decide por la curva que quede más alta en el punto medido.

- «En el dibujo» → `dibujo`: corte; las dos campanas grandes de la escena 09
- «se multiplica por su probabilidad a priori» → `factores`: sobre cada una, «× 0,7» y «× 0,3»
- «La del cero» → `del0`: la campana magenta se resalta
- «el setenta por ciento» → `esc0`: la campana magenta se encoge al 70 %
- «se encoge al» → `esc1`: la azul se encoge al 30 %
- «la curva que quede más alta» → `alta`: un cursor recorre el eje y, en cada punto, se resalta la curva más alta

---

# Escena 11 — ElCruceSeMueve

**Capítulo YouTube:** Regiones de decisión
**Objetivo:** ver que 1,3 cambia de decisión, que el cruce se mueve a 1,42 y que el eje queda partido en dos regiones; leer la regla término a término.

## Narración

<!-- b1 -->
Hagamos la cuenta en uno coma tres. Cero coma siete por cero coma diecisiete:
cero coma doce. Cero coma tres por cero coma treinta y uno: cero coma cero
noventa y cuatro. Gana el cero. Con la misma medición que hace un momento nos
hacía decir uno.

- «en uno coma tres» → `medida`: la regla cian en 1,3, sobre las campanas escaladas
- «Cero coma siete por» → `m0`: el punto magenta: «0,7 · 0,17»
- «cero coma doce» → `c12`: «= 0,12»
- «Cero coma tres por» → `m1`: el punto azul: «0,3 · 0,31»
- «cero coma cero» → `c094`: «= 0,094»
- «Gana el cero» → `gana0`: el punto magenta se ilumina; «Decir 0»
- «Con la misma medición» → `misma`: la regla cian late
- «nos» → `antes`: tarjeta «Antes: 1 · Ahora: 0», con «Antes» atenuado

<!-- b2 -->
El cruce de las curvas ya no está en uno: se ha ido a uno coma cuarenta y dos.
Como los unos son más raros, pedimos más voltios antes de creernos un uno. El
eje queda partido en dos regiones de decisión: a la derecha de uno coma
cuarenta y dos se dice uno, y a la izquierda, cero.

- «El cruce de las curvas» → `cruce`: el punto ámbar del cruce aparece en 1, atenuado
- «uno coma cuarenta y dos» → `mueve`: el cruce se desliza hasta «1,42»
- «más raros» → `raros`: los factores «× 0,3» y «× 0,7» laten
- «más voltios» → `voltios`: flecha ámbar de 1 a 1,42
- «antes de creernos un uno» → `creer`: el rótulo «Decir 1» se aleja hasta 1,42
- «dos regiones de decisión» → `regiones`: el eje se parte en dos tramos
- «se dice uno» → `d1`: tramo derecho azul: «D₁ · Decir 1»
- «a la izquierda, cero» → `d0`: tramo izquierdo magenta: «D₀ · Decir 0»

<!-- b3 -->
Esta es la regla del máximo a posteriori para una medición continua. Pe uno
por la densidad de erre bajo hache uno, comparada con pe cero por la densidad
de erre bajo hache cero. Si gana la primera, se dice uno. Si gana la segunda,
cero.

- «la regla del máximo a posteriori» → `titulo`: el dibujo sube y se achica; «MAP» al centro
- «para una medición continua» → `continua`: debajo de «MAP», «r continua» en cian
- «Pe uno» → `p1`: «p₁»
- «la densidad de erre bajo hache uno» → `f1`: «· f(r | H₁)» en azul
- «comparada con» → `comp`: «≷»
- «pe cero» → `p0`: «p₀»
- «bajo hache cero» → `f0`: «· f(r | H₀)» en magenta
- «Si gana la primera» → `gana1`: el «>» se ilumina y sale una flecha a «Decir 1»
- «Si gana la segunda» → `gana0`: el «<» se ilumina y sale una flecha a «Decir 0»

---

# Escena 12 — InfinitasColumnas

**Capítulo YouTube:** Por qué ninguna regla le gana
**Objetivo:** entender por qué la regla minimiza el error total: una columna por cada valor de erre, pesos que nunca son negativos, y el error como área.

## Narración

<!-- b1 -->
¿Es la mejor regla posible, o solo una regla razonable? El argumento es el de
las columnas de la tabla, solo que ahora hay infinitas columnas: una por cada
valor de erre. En cada una, si dices uno fallas con la probabilidad a
posteriori del cero, y si dices cero, con la del uno. Quedarte con la mayor es
fallar lo menos posible ahí.

- «¿Es la mejor regla posible» → `pregunta`: «¿La mejor?»
- «o solo una regla razonable» → `razonable`: debajo, «¿O solo razonable?»
- «las columnas de la tabla» → `tabla`: la tabla del canal de la escena 06, con sus casillas rojas pequeñas
- «infinitas columnas» → `rebanadas`: la tabla se transforma en las campanas escaladas, cortadas en rebanadas verticales
- «una por cada» → `cada`: rótulo «Una columna por cada r»
- «si dices uno» → `di1`: en una rebanada, el tramo de la curva del cero se marca en rojo
- «si dices cero» → `di0`: en otra rebanada, el tramo de la curva del uno se marca en rojo
- «Quedarte con la mayor» → `mayor`: en cada rebanada, el tramo alto en verde y el bajo en rojo
- «fallar lo menos posible ahí» → `menos`: el tramo rojo de cada rebanada late

<!-- b2 -->
La probabilidad de error total es el promedio de esos fallos sobre todos los
valores de erre, cada uno pesado por lo a menudo que aparece. Ese peso es una
densidad, y una densidad nunca es negativa. El promedio es una integral: la
suma de rebanadas muy finas que vimos en el capítulo siete.

- «La probabilidad de error total» → `pe`: arriba, «P(error)» en rojo
- «el promedio de esos fallos» → `promedio`: los tramos rojos de varias rebanadas vuelan hacia «P(error)»
- «sobre todos los valores de erre» → `todos`: un cursor barre el eje de punta a punta
- «lo a menudo que aparece» → `peso`: bajo el eje, una curva gris «f(r)» con el rótulo «Peso»
- «Ese peso es una densidad» → `densidad`: el rótulo «Peso» se cambia por «Densidad»
- «nunca es negativa» → `positiva`: «f(r) ≥ 0»
- «El promedio es una integral» → `integral`: «P(error) = ∫ …»
- «rebanadas muy finas» → `finas`: las rebanadas se afinan hasta volverse un área continua

<!-- b3 -->
Cualquier otra regla, en cada rebanada, falla lo mismo o más. Y sumar cosas
iguales o mayores, con pesos que nunca son negativos, da un total igual o
mayor. Ninguna regla puede ganarle. En el dibujo, el error es el área bajo la
curva escalada que pierde. Si mueves el umbral a otro sitio, aparece un trozo
de área de más.

- «Cualquier otra regla» → `otra`: en una rebanada, una regla gris se queda con el tramo bajo: falla el alto
- «lo mismo o más» → `mayor`: «≥»
- «Y sumar cosas» → `sumar`: varias rebanadas, cada una con su «≥», se apilan
- «con pesos que nunca son negativos» → `pesos`: vuelve «f(r) ≥ 0»
- «da un total igual o» → `total`: «P(error, otra) ≥ P(error, MAP)»
- «Ninguna regla puede ganarle» → `gana`: tilde verde junto a «MAP»
- «En el dibujo» → `dibujo`: las rebanadas se van; quedan las campanas escaladas
- «el área bajo la» → `area`: se rellena el área roja bajo la curva más baja, a cada lado de 1,42: «Error = área roja»
- «Si mueves el umbral» → `mueve`: el umbral ámbar se desliza de 1,42 a 1
- «un trozo» → `trozo`: entre 1 y 1,42 se rellena un trozo rojo más intenso: «De más»

---

# Escena 13 — LaFrontera

**Capítulo YouTube:** El empate y las tres hipótesis
**Objetivo:** qué pasa justo en la frontera y cómo se extiende la regla a tres hipótesis.

## Narración

<!-- b1 -->
¿Y justo en el cruce, en uno coma cuarenta y dos? Ahí hay empate: decir cero o
uno falla lo mismo. Además, la probabilidad de medir exactamente ese valor es
cero. Así que en la frontera puedes decidir lo que quieras, y la regla sigue
siendo la mejor.

- «justo en el cruce» → `zoom`: zoom al cruce en 1,42
- «Ahí hay empate» → `empate`: dos segmentos de la misma altura; «Empate»
- «falla lo mismo» → `igual`: «=» entre los dos
- «exactamente ese valor» → `linea`: una rebanada de ancho cero, una línea finísima
- «es» → `cero`: «Probabilidad 0»
- «en la frontera» → `frontera`: la línea del cruce se marca en ámbar
- «lo que quieras» → `moneda`: una moneda gira sobre la frontera
- «sigue» → `mejor`: el zoom vuelve atrás; tilde verde en «MAP»

<!-- b2 -->
Con más de dos hipótesis no cambia nada. Si se pudieran enviar cero, dos o
cuatro voltios, habría tres campanas, cada una escalada por su probabilidad a
priori, y ganaría la más alta. Si las tres son igual de probables, los umbrales
caen en uno y en tres.

- «más de dos hipótesis» → `mas`: corte; un eje de 0 a 4
- «no cambia nada» → `nada`: «Misma regla» en ámbar
- «cero, dos o» → `niveles`: marcas «0 V», «2 V» y «4 V»
- «tres campanas» → `tres`: tres campanas, en magenta, azul y verde
- «escalada por su probabilidad a» → `escala`: las tres se encogen y crecen un poco, con «× p₀», «× p₁» y «× p₂»
- «ganaría la más alta» → `alta`: un cursor recorre el eje y resalta la más alta
- «igual de probables» → `iguales`: las tres a la misma altura
- «en uno y en tres» → `umbrales`: umbrales ámbar en 1 y 3; tres regiones coloreadas

---

# Escena 14 — Cierre

**Capítulo YouTube:** Dos maneras de equivocarse

## Narración

<!-- b1 -->
Decidir es quedarse con la hipótesis más probable después de mirar: la altura
de cada campana, pesada por lo que sabías antes. Ya tenemos la regla y sabemos
que es la mejor. Lo que todavía no sabemos es cuánto se equivoca, ni de qué
manera. Porque hay más de una forma de fallar. En el próximo episodio veremos
«Dos maneras de equivocarse».

- «Decidir es quedarse» → `decidir`: las dos campanas escaladas con las regiones D₀ y D₁
- «la altura» → `altura`: las campanas laten
- «lo que sabías antes» → `antes`: «× 0,7» y «× 0,3» laten
- «Ya tenemos la regla» → `regla`: arriba, «p₁ · f(r | H₁) ≷ p₀ · f(r | H₀)»
- «es la mejor» → `mejor`: «MAP» con un tilde verde
- «cuánto se equivoca» → `cuanto`: las colas a cada lado de 1,42 se rellenan de rojo, con un «?»
- «ni de qué» → `manera`: las dos colas se separan en dos tonos de rojo
- «más de una forma de fallar» → `formas`: «≠» entre las dos colas
- «En el próximo episodio» → `proximo`: las campanas se atenúan
- «Dos maneras de equivocarse» → `siguiente`: todo se apaga y entra el título «Dos maneras de equivocarse»
