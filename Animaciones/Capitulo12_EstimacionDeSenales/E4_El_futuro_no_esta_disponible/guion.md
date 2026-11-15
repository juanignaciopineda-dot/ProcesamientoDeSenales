# Episodio 4 — El futuro no está disponible

Capítulo 12 (Estimación de señales), episodio 4 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 14 a 17), más un gancho y un cierre nuevos.

**Estado:** `guion.md` escrito (20 escenas atómicas, con momentos), validado con `ritmo.py` (~9,2 min de voz, sin huecos de más de 4 s). Texto ⭐ (gancho y cierre) aprobado por el usuario. Escenas `s01`–`s20` animadas; borrador 480p15 de 9:10 con 0 avisos y hojas de contacto revisadas. Pendiente: visto bueno del usuario al mp4 (paso 15) y render final.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Tienes el mejor filtro posible. Le cortas la parte que mira al futuro, y deja de ser el mejor. Hoy vemos por qué, y cómo se arregla.»
- ⭐ Escena 20 (cierre): repasa el episodio y anuncia el E5 por su título, «El sensor, de punta a punta».

Retoques de frases del guion base, porque el episodio se ve suelto:
- Escena 14, bloque 2 (ahora escena 04): «Recuerda la escena anterior» pasa a «Recuerda el episodio anterior».
- Escena 14, bloque 4 (ahora escena 06): «el filtro no causal del sensor» queda igual; ahí se recuerdan sus coeficientes (h[0] = 0,686; h[±1] = 0,108).
- Escena 17, bloques 2 y 4 (ahora escenas 17 y 19): «la escena quince» pasa a «las mediciones blancas».
- Escena 17, bloque 5 (ahora escena 19, segundo bloque): se quita la última frase («Es lo que hacemos en el próximo episodio»); la reemplaza el cierre ⭐.

Reparto de las escenas del guion base: 14 → escenas 03 a 07 (el bloque 5 de la 14 abre la escena 07); 15 → 07 a 10; 16 → 11 a 15; 17 → 16 a 19.
Solo se partieron bloques enteros en escenas atómicas: el resto del texto del guion base no cambia.

Bucles de este episodio: «se resuelve con una división porque la igualdad vale en todo el eje» (E3 escena 09 → escena 04 de aquí); blanquear primero (Cap. 11 escena 27 → escena 11); fase mínima con (2, 1) y (1, 2) (Cap. 11 escena 28 → escena 13); «¿cuánto se pierde por ser causal?» (escenas 06 y 19 → E5 escena 21); el corchete ₊ (escena 17 → E5 escena 19).

---

# Escena 01 — Gancho

**Capítulo YouTube:** El mejor filtro, cortado

## Narración

<!-- b1 -->
Tienes el mejor filtro posible. Le cortas la parte que mira al futuro, y deja de ser el mejor. Hoy vemos por qué, y cómo se arregla.

- «el mejor filtro posible» → `mejor`: barras simétricas de un filtro (0,017 · 0,108 · 0,686 · 0,108 · 0,017) con una corona ámbar encima
- «Le cortas la parte» → `cortas`: una tijera se acerca a las barras de la izquierda
- «mira al futuro» → `futuro`: las barras de m < 0 se cortan y caen, con un reloj y «futuro» sobre ellas
- «deja de ser el mejor» → `deja`: la corona se tacha en rojo
- «Hoy vemos por qué» → `porque`: una lupa se acerca a las barras cortadas
- «cómo se arregla» → `arregla`: sobre las barras sale «blanquear primero» en ámbar

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** El futuro no está disponible

## Narración

<!-- b1 -->
El futuro no está disponible.

- «El futuro» → `t1`: «El futuro» entra con rebote
- «no está disponible» → `t2`: «no está disponible» entra debajo, con la etiqueta «Capítulo 12 · Estimación de señales»

---

# Escena 03 — SinFuturo

**Capítulo YouTube:** Un filtro que no puede ver el futuro

**Objetivo:** el filtro causal solo tiene presente y pasado, así que el error solo puede ser perpendicular a las muestras con m ≥ 0.

## Narración

<!-- b1 -->
Ahora, lo difícil. Un aparato que filtra en tiempo real no puede usar el futuro: solo tiene el presente y el pasado. El filtro tiene que ser causal: hache de jota vale cero para jota negativa. Y entonces la condición cambia: solo podemos exigir que el error sea perpendicular a las muestras que tenemos, las de eme mayor o igual que cero.

- «lo difícil» → `dificil`: «lo difícil» entra con rebote en ámbar
- «tiempo real» → `real`: un aparato con un reloj; entra una señal por la izquierda y sale filtrada por la derecha
- «no puede usar el futuro» → `nofuturo`: una flecha «el futuro no ha llegado» hacia la derecha del reloj, tachada
- «solo tiene el presente y el pasado» → `presente`: eje de tiempo: las muestras ya llegadas encendidas, las futuras apagadas
- «El filtro tiene que ser» → `filtro`: el aparato se dibuja como una caja «filtro»
- «causal» → `causal`: la palabra «causal» entra con rebote
- «hache de jota vale cero» → `hj`: aparece «h[j] = 0»
- «para jota negativa» → `jneg`: se completa «para j < 0» y las posiciones negativas se resaltan en rojo
- «la condición cambia» → `cambia`: aparece «e ⟂ x[n − m]»
- «perpendicular a las muestras que tenemos» → `perp`: flechas de las muestras pasadas con marca de ángulo recto; las del futuro, tachadas
- «eme mayor o igual que cero» → `mpos`: «m ≥ 0» en ámbar junto a la ecuación

---

# Escena 04 — ElSoloLoEstropea

**Capítulo YouTube:** La ecuación vale solo para m ≥ 0

**Objetivo:** la ecuación es la misma pero vale en media recta; por eso ya no se puede transformar.

## Narración

<!-- b1 -->
La ecuación es la misma, hache convolucionado con la autocorrelación igual a la correlación cruzada, pero ahora vale solo para eme mayor o igual que cero. Y ese solo lo estropea todo. Recuerda el episodio anterior: transformamos porque la igualdad valía en todo el eje. Ahora no. Veamos con dos secuencias muy pequeñas qué se rompe.

- «hache convolucionado con la autocorrelación» → `conv`: aparece «h ∗ C_xx»
- «igual a la correlación cruzada» → `igual`: se completa «= C_yx»
- «solo para eme mayor o igual que cero» → `solom`: se añade «m ≥ 0» con el «solo» en rojo
- «ese solo lo estropea todo» → `estropea`: el «solo» se agranda y tiembla
- «Recuerda el episodio anterior» → `recuerda`: un recuadro pequeño «episodio anterior» con «× transformada»
- «la igualdad valía en todo el eje» → `eje`: un eje m completo, iluminado de punta a punta
- «Ahora no» → `ahorano`: la mitad izquierda del eje se apaga
- «dos secuencias muy pequeñas» → `dos`: aparecen dos filas de casillas vacías, «p» y «q»

---

# Escena 05 — DosSecuenciasPequenas

**Capítulo YouTube:** Iguales en media recta no son iguales

**Objetivo:** ver con dos secuencias que dos secuencias iguales en media recta tienen transformadas distintas.

## Narración

<!-- b1 -->
La primera vale uno en cero y nada más. La segunda vale uno en cero y tres en la posición menos uno. Coinciden para todo eme mayor o igual que cero, pero sus transformadas son distintas: la primera es uno; la segunda, uno más tres e elevado a jota omega. Dos secuencias iguales solo en la mitad del eje no tienen, en general, la misma transformada.

- «La primera vale uno en cero» → `p`: en la fila «p», un tallo de altura 1 en m = 0
- «y nada más» → `nada`: el resto de las posiciones de p muestran 0
- «La segunda vale uno en cero» → `q`: en la fila «q», un tallo de altura 1 en m = 0
- «tres en la posición menos uno» → `tres`: un tallo de altura 3 en m = −1, en rojo
- «Coinciden para todo eme mayor o igual que cero» → `coinciden`: un marco verde sobre m ≥ 0, donde p y q valen lo mismo
- «sus transformadas son distintas» → `distintas`: dos cajas «P» y «Q» con un «≠» en rojo entre ellas
- «la primera es uno» → `pp`: en la caja de P aparece «P = 1»
- «uno más tres e elevado a jota omega» → `qq`: en la caja de Q aparece «Q = 1 + 3 e^{jΩ}» construida por piezas
- «Dos secuencias» → `dossec`: las dos filas p y q vuelven a primer plano
- «iguales solo en la mitad del eje» → `mitad`: un rótulo «iguales en media recta»
- «en general» → `engeneral`: «en general» en ámbar junto al rótulo
- «la misma transformada» → `misma`: el rótulo se completa «≠ misma transformada»

---

# Escena 06 — CortarNoSirve

**Capítulo YouTube:** Cortar el filtro no causal no sirve

**Objetivo:** no se puede despejar con la transformada, y cortar los coeficientes del no causal del sensor da otro filtro (0,686 frente a 0,7386).

## Narración

<!-- b1 -->
Además, para eme negativo los dos lados no coinciden, y el izquierdo depende de un hache que aún no conocemos: no podemos transformar y dividir. ¿Y si tomamos el filtro no causal del sensor y le cortamos los coeficientes de eme negativo? Vale cero coma seis ocho seis en el cero y cero coma uno cero ocho a cada lado. Pero el óptimo causal empieza en cero coma siete tres ocho seis: distinto.

- «para eme negativo» → `neg`: «m < 0» con un signo de interrogación en cada lado de una igualdad
- «los dos lados no coinciden» → `nocoin`: «(h ∗ C_xx)[m] ≠ C_yx[m]» con el «≠» en rojo
- «un hache que aún no conocemos» → `noconocemos`: la «h» del lado izquierdo se vuelve «h = ?»
- «no podemos transformar y dividir» → `nodividir`: una división «S_yx / S_xx» tachada
- «el filtro no causal del sensor» → `sensor`: entran las barras simétricas 0,017 · 0,108 · 0,686 · 0,108 · 0,017
- «le cortamos los coeficientes» → `corta`: una tijera se acerca a las barras
- «de eme negativo» → `negc`: la tijera corta las barras de m < 0, que quedan atenuadas
- «cero coma seis ocho seis en el cero» → `c0`: se resalta la barra central, 0,686
- «cero coma uno cero ocho a cada lado» → `lados`: se resaltan las dos barras de 0,108
- «el óptimo causal empieza en cero coma siete tres ocho seis» → `optimo`: debajo, otra fila de barras 0,7386 · 0,1158 · 0,0182 en ámbar
- «distinto» → `distinto`: «0,686 ≠ 0,7386» con el «≠» en rojo

---

# Escena 07 — MedicionesSinMemoria

**Capítulo YouTube:** El caso fácil: mediciones blancas

**Objetivo:** el coeficiente de ahora trabaja más sin futuro; cortar sin más no sirve salvo con mediciones sin memoria, donde la ecuación se desacopla.

## Narración

<!-- b1 -->
Tiene sentido: sin poder ver el futuro, el coeficiente de la muestra de ahora tiene que trabajar más. Cortar sin más no sirve. Pero hay un caso en el que cortar sí funciona, y es la clave de todo el episodio. Ese caso ocurre cuando las mediciones no tienen memoria.

- «sin poder ver el futuro» → `sinfuturo`: el reloj del aparato con el futuro tachado
- «la muestra de ahora tiene que trabajar más» → `trabaja`: la barra central pasa de 0,686 a 0,7386, más alta
- «Cortar sin más no sirve» → `nosirve`: una tijera con una cruz roja
- «un caso en el que cortar sí funciona» → `funciona`: un tilde verde sobre la tijera
- «la clave de todo el episodio» → `clave`: una llave ámbar entra y se queda
- «Ese caso ocurre» → `ocurre`: la llave ámbar señala hacia la derecha, donde está la moneda sin dibujar
- «las mediciones no tienen memoria» → `sinmemoria`: la moneda ±1 del Cap. 10 sustituye a la tijera

<!-- b2 -->
Si las mediciones son blancas, como la moneda, sin ninguna memoria, no hay drama. La autocorrelación vale sigma cuadrado en cero y nada en el resto, así que en la suma de la ecuación solo sobrevive un término: sigma cuadrado por hache de eme igual a la correlación cruzada en eme. Cada coeficiente se despeja por separado.

- «mediciones son blancas» → `blancas`: la tira de la moneda ±1 con el rótulo «blanca»
- «como la moneda» → `moneda`: el ícono de la moneda al lado de la tira
- «sin ninguna memoria» → `sinmem`: cada muestra con una flecha a las demás, tachada: «no depende de las otras»
- «La autocorrelación vale sigma cuadrado en cero» → `sigma`: palitos de la autocorrelación: un solo tallo en 0, «σ²»
- «nada en el resto» → `resto`: el resto de las posiciones, en cero
- «en la suma de la ecuación» → `suma`: aparece «Σ h[k] C_xx[m − k] = C_yx[m]»
- «solo sobrevive un término» → `sobrevive`: todos los términos de la suma se apagan menos uno
- «sigma cuadrado por hache de eme» → `sh`: queda «σ² h[m]»
- «igual a la correlación cruzada en eme» → `ig`: se completa «= C_yx[m]»
- «Cada coeficiente» → `cadacoef`: cada h[m] se resalta una vez, con su color
- «se despeja por separado» → `separado`: una matriz diagonal; cada h[m] se despeja de su propia fila

---

# Escena 08 — ConNumerosInventados

**Capítulo YouTube:** El filtro blanco, con números

**Objetivo:** la cuenta hecha a mano para mediciones blancas: σ² = 2, C_yx = (1, 2, 1, 0,5) en m = −1, 0, 1, 2, y h = (0,5; 1; 0,5; 0,25).

## Narración

<!-- b1 -->
Con números inventados. Sigma cuadrado vale dos, y la correlación cruzada vale uno en menos uno, dos en cero, uno en uno y cero coma cinco en dos. Dividimos entre dos: los coeficientes valen cero coma cinco, uno, cero coma cinco y cero coma dos cinco. Ese es el filtro no causal, que usa una muestra del futuro, la de posición menos uno.

- «Con números inventados» → `inv`: una tabla con tres filas: m, C_yx y h
- «Sigma cuadrado vale dos» → `s2`: «σ² = 2» en ámbar
- «uno en menos uno» → `c1`: en la columna m = −1, C_yx = 1
- «dos en cero» → `c2`: en m = 0, C_yx = 2
- «uno en uno» → `c3`: en m = 1, C_yx = 1
- «cero coma cinco en dos» → `c4`: en m = 2, C_yx = 0,5
- «Dividimos entre dos» → `div`: una flecha «÷ 2» baja sobre la fila de C_yx
- «cero coma cinco, uno, cero coma cinco» → `h`: la fila de h se llena: 0,5 · 1 · 0,5, con barras
- «y cero coma dos cinco» → `h4`: se añade el último, 0,25
- «filtro no causal» → `noc`: el rótulo «no causal» sobre la tabla
- «una muestra del futuro» → `fut`: la columna m = −1 se resalta en rojo

---

# Escena 09 — ElCausalEsElCortado

**Capítulo YouTube:** El filtro causal se calcula cortando

**Objetivo:** con mediciones blancas las ecuaciones de m < 0 no molestan: el causal es el no causal cortado.

## Narración

<!-- b1 -->
Y el causal: las ecuaciones de eme negativo son otras ecuaciones, para coeficientes que ahora valen cero, y no molestan a las demás. Los coeficientes de eme mayor o igual que cero salen igual: uno, cero coma cinco y cero coma dos cinco. Basta calcular la solución no causal y cortarle la parte no causal.

- «Y el causal» → `causal`: el rótulo «causal» sobre la tabla anterior
- «las ecuaciones de eme negativo» → `neg`: la columna m = −1 se separa a un lado
- «otras ecuaciones» → `otras`: la columna separada queda en un recuadro aparte
- «coeficientes que ahora valen cero» → `cero`: en el recuadro, «h[j] = 0 para j < 0»
- «no molestan a las demás» → `nomolestan`: las otras columnas no cambian; un tilde verde
- «Los coeficientes de eme mayor o igual que cero» → `mpos`: un marco sobre las columnas m ≥ 0
- «salen igual» → `igual`: las columnas m = 0, 1, 2 se resaltan en verde
- «uno, cero coma cinco y cero coma dos cinco» → `vals`: abajo, los valores 1 · 0,5 · 0,25 en ámbar, con barras
- «Basta» → `basta`: «basta» entra con rebote
- «calcular la solución no causal» → `calc`: una flecha parte del rótulo «no causal»
- «cortarle la parte no causal» → `corta`: la tijera corta m < 0; queda el causal

---

# Escena 10 — PorQueSePuedeCortar

**Capítulo YouTube:** Por qué se puede cortar

**Objetivo:** cada muestra blanca es una flecha perpendicular a las demás; si lo medido no es blanco, hay que blanquearlo antes.

## Narración

<!-- b1 -->
¿Por qué se puede cortar? Porque cada muestra blanca trae información propia, que no repite la de las otras. Cada coeficiente solo escucha a su muestra, y quitar unas no cambia lo que dicen las demás. Es la suma de varias proyecciones sobre flechas perpendiculares entre sí: no se estorban.

- «¿Por qué se puede cortar?» → `pregunta`: «¿por qué se puede cortar?» en ámbar
- «información propia» → `propia`: cada muestra como una flecha de un color distinto
- «no repite la de las otras» → `norepite`: las flechas forman ángulos rectos entre sí
- «solo escucha a su muestra» → `escucha`: cada coeficiente h[m] queda unido por un hilo a su flecha
- «quitar unas no cambia lo que dicen las demás» → `quitar`: se borran dos flechas y los otros hilos siguen igual
- «suma de varias proyecciones» → `suma`: la flecha de y se proyecta sobre cada una y las proyecciones se suman
- «perpendiculares entre sí» → `perpend`: marcas de ángulo recto entre las flechas
- «no se estorban» → `estorban`: un tilde verde

<!-- b2 -->
El problema es que casi nada es blanco: el sensor tiene memoria, y sus muestras se parecen unas a otras. Pero la idea da una salida: si lo que medimos no es blanco, ¿y si lo convertimos en blanco antes de empezar? Eso ya lo sabemos hacer: es el blanqueador del capítulo once.

- «casi nada es blanco» → `noblanco`: la tira de la moneda se atenúa; aparece una traza con memoria
- «el sensor tiene memoria» → `sensor`: el termómetro y la traza del sensor del 0,6
- «se parecen unas a otras» → `parecen`: las flechas del sensor forman ángulos agudos entre sí
- «una salida» → `salida`: aparece una flecha «salida» hacia la derecha
- «lo convertimos en blanco» → `convertir`: la traza del sensor entra en una caja y sale como tira blanca
- «Eso ya lo sabemos hacer» → `sabemos`: un tilde verde sobre la caja
- «el blanqueador del capítulo once» → `blanq`: la caja se rotula «blanqueador · Cap. 11»

---

# Escena 11 — BlanquearPrimero

**Capítulo YouTube:** La estrategia: blanquear primero

**Objetivo:** blanquear, resolver el caso fácil y deshacer el blanqueo; el blanqueador y su inverso tienen que ser causales.

## Narración

<!-- b1 -->
La estrategia: blanquear primero. Convertimos lo medido en ruido blanco, con un filtro. Resolvemos el problema fácil con esa señal blanca. Y deshacemos el blanqueo. Pero hay una condición, y es lo que hace difícil el asunto: el blanqueador tiene que ser causal, y su inverso, el que deshace el blanqueo, también. Si no, mezclaríamos pasado y futuro.

- «blanquear primero» → `bp`: «blanquear primero» entra con rebote
- «Convertimos lo medido en ruido blanco» → `conv`: la cadena «x → [blanquear] → ε»
- «con un filtro» → `filtro`: la primera caja se rotula «filtro»
- «Resolvemos el problema fácil» → `facil`: segunda caja, «resolver el fácil»
- «con esa señal blanca» → `conesa`: la tira blanca ε entra en la segunda caja
- «Y deshacemos el blanqueo» → `deshace`: tercera caja, «deshacer», y sale «ŷ»
- «una condición» → `cond`: un cartel «condición» en ámbar
- «el blanqueador tiene que ser causal» → `bcausal`: sello «causal» en la primera caja
- «su inverso» → `inverso`: sello «causal» también en la tercera caja
- «el que deshace el blanqueo» → `quedesh`: una flecha señala hacia atrás la tercera caja
- «mezclaríamos pasado y futuro» → `mezcla`: dos flechas, «pasado» y «futuro», chocan; cruz roja

---

# Escena 12 — ElRetardoYElPolo

**Capítulo YouTube:** El retardo y el polo

**Objetivo:** z⁻¹ como retardo, el filtro como suma de retardos y el eco del 0,6 como cociente con un polo en 0,6.

## Narración

<!-- b1 -->
Un poco de notación. Zeta a la menos uno es un retardo de una muestra, y un filtro se escribe como suma de retardos con sus coeficientes: hache cero, más hache uno zeta a la menos uno, y así. El eco del cero coma seis es uno entre uno menos cero coma seis zeta a la menos uno: uno, más cero coma seis retardado, más cero coma treinta y seis retardado dos veces, y así. Tiene un polo en cero coma seis.

- «Un poco de notación» → `nota`: título «notación»
- «Zeta a la menos uno» → `z`: aparece «z⁻¹» en ámbar
- «un retardo de una muestra» → `retardo`: una caja «z⁻¹» desplaza una serie una muestra a la derecha
- «suma de retardos» → `suma`: aparece «F(z) =» con varias cajas «z⁻¹» encadenadas
- «con sus coeficientes» → `coefs`: cada retardo recibe un coeficiente encima
- «hache cero» → `h0`: aparece «h₀»
- «más hache uno zeta a la menos uno» → `h1`: se añade «+ h₁ z⁻¹ + h₂ z⁻² + …»
- «El eco del cero coma seis» → `eco`: la serie con memoria 0,6 del Cap. 10
- «uno entre uno menos cero coma seis zeta a la menos uno» → `cociente`: «F(z) = 1 / (1 − 0,6 z⁻¹)»
- «uno, más cero coma seis retardado» → `s1`: «= 1 + 0,6 z⁻¹»
- «más cero coma treinta y seis retardado dos veces» → `s2`: «+ 0,36 z⁻² + …»
- «y así» → `yasi`: la suma sigue con «…»
- «Tiene un polo en cero coma seis» → `polo`: un recuadro «polo = 0,6»

---

# Escena 13 — PolosDentroYFuera

**Capítulo YouTube:** Polos dentro y fuera del círculo

**Objetivo:** un polo dentro del círculo unidad decae, fuera explota; con (2, 1) y (1, 2) del Cap. 11 se ve qué inverso se apaga y cuál explota.

## Narración

<!-- b1 -->
El polo es la base de la caída. Si su módulo es menor que uno, dentro del círculo unidad, los coeficientes se apagan; si fuera dos, valdrían uno, dos, cuatro, ocho: explotan. Así se entiende el capítulo once. Dos más zeta a la menos uno tiene su cero en menos un medio, dentro: su inverso se apaga. Uno más dos zeta a la menos uno lo tiene fuera: su inverso explota.

- «El polo es la base de la caída» → `base`: el × del polo 0,6 con barras que bajan
- «menor que uno» → `menor`: el polo 0,6 marcado dentro del círculo
- «dentro del círculo unidad» → `circulo`: el plano z con el círculo unidad resaltado
- «los coeficientes se apagan» → `apagan`: barras 1 · 0,6 · 0,36 · 0,22 que decaen
- «si fuera dos» → `dos`: el polo en 2, fuera del círculo
- «uno, dos, cuatro, ocho» → `explotan`: barras 1 · 2 · 4 · 8 que crecen hasta salirse del cuadro
- «Así se entiende el capítulo once» → `cap11`: un recuadro «Cap. 11» en un rincón
- «Dos más zeta a la menos uno» → `f1`: aparece «(2 + z⁻¹)/√5»
- «su cero en menos un medio» → `cero1`: un ○ en −0,5, dentro del círculo
- «su inverso se apaga» → `inv1`: barras de la inversa ½ · −¼ · ⅛ que decaen
- «Uno más dos zeta a la menos uno» → `f2`: aparece «(1 + 2 z⁻¹)/√5», con un ○ en −2, fuera
- «su inverso explota» → `inv2`: barras de la inversa 1 · −2 · 4 · −8 que explotan

---

# Escena 14 — FaseMinima

**Capítulo YouTube:** Fase mínima y factorización

**Objetivo:** fase mínima es causal y estable con inverso causal y estable; la densidad de lo medido es σ² F(z) F(z⁻¹).

## Narración

<!-- b1 -->
Fase mínima es el filtro con todos sus polos y ceros dentro del círculo: es causal y estable, y su inverso también. Y aquí aparece la factorización: la densidad de lo medido es una constante por F de zeta, el filtro de fase mínima, por F de zeta a la menos uno, el mismo filtro dado la vuelta en el tiempo. En el círculo es su ganancia al cuadrado: el modelador del capítulo once.

- «Fase mínima» → `fm`: «fase mínima» entra con rebote
- «todos sus polos y ceros dentro del círculo» → `dentro`: el plano z con × y ○ todos dentro del círculo
- «causal y estable» → `estable`: dos tildes verdes, «causal» y «estable»
- «su inverso también» → `inversotb`: un tercer tilde sobre «su inverso»
- «la factorización» → `fact`: título «factorización»
- «la densidad de lo medido es una constante» → `dens`: aparece «S_xx(z) = σ²»
- «por F de zeta» → `fz`: se añade «F(z)»
- «el filtro de fase mínima» → `fmin`: una etiqueta «fase mínima» bajo F(z)
- «por F de zeta a la menos uno» → `fzi`: se añade «F(z⁻¹)»
- «dado la vuelta en el tiempo» → `vuelta`: la secuencia de F se refleja a la izquierda
- «En el círculo es su ganancia al cuadrado» → `gan`: debajo, «S_xx(Ω) = σ² |F(e^{jΩ})|²»
- «el modelador del capítulo once» → `mod`: un rótulo «modelador · Cap. 11»

---

# Escena 15 — LaInnovacion

**Capítulo YouTube:** La innovación

**Objetivo:** la factorización existe si la densidad no se anula en una banda; la señal blanqueada se llama innovación; falta relacionarla con lo que se busca.

## Narración

<!-- b1 -->
Existe siempre que la densidad no se anule en toda una banda: no se puede blanquear lo que no existe. La señal blanqueada, la que sale de aplicar uno entre F a lo medido, se llama innovación, épsilon, y es blanca. Nos falta un último ingrediente: relacionar la señal que buscamos con esa innovación. Y eso lo hace la fórmula del filtro causal.

- «la densidad no se anule en toda una banda» → `banda`: un espectro con un tramo en cero y el cartel «espectro nulo en una banda»
- «no se puede blanquear lo que no existe» → `noexiste`: el blanqueador con una cruz roja
- «La señal blanqueada» → `blanqueada`: la cadena «x → [1/F] → ε»
- «uno entre F» → `unof`: la caja se rotula «1/F»
- «innovación» → `innov`: la palabra «innovación» entra con rebote
- «épsilon» → `eps`: «ε» junto a la palabra
- «es blanca» → `blanca`: la tira de la moneda sobre ε
- «último ingrediente» → `ingred`: un hueco «?» a la derecha de la cadena
- «relacionar la señal que buscamos» → `relacionar`: aparece «y» en azul con un «?» a la derecha
- «con esa innovación» → `conesa`: el «?» se convierte en una flecha doble hacia «ε»
- «la fórmula del filtro causal» → `formula`: sello «fórmula del filtro causal»

---

# Escena 16 — PrimerPasoBlanquear

**Capítulo YouTube:** Primer paso: blanquear

**Objetivo:** la densidad cruzada con una señal filtrada se multiplica por el conjugado de la respuesta; S_yε = S_yx / F(z⁻¹).

## Narración

<!-- b1 -->
Vamos a construir la fórmula en tres pasos, con la ayuda de la innovación. Primer paso: blanquear lo medido con uno entre F. Necesitamos saber cómo se relaciona ahora la señal que buscamos, i griega, con la señal blanqueada. La regla: la densidad cruzada con una señal filtrada se multiplica por el conjugado de la respuesta del filtro. Y el conjugado de uno entre F es uno entre F de zeta a la menos uno.

- «tres pasos» → `tres`: tres casillas numeradas 1, 2 y 3, vacías
- «Primer paso» → `p1`: la casilla 1 se ilumina, «blanquear»
- «blanquear lo medido con uno entre F» → `bl`: la cadena «x → [1/F] → ε»
- «Necesitamos saber» → `necesitamos`: un signo «?» aparece entre «y» y «ε»
- «la señal que buscamos, i griega» → `y`: «y» en azul, fuera de la cadena
- «la señal blanqueada» → `bla`: «ε» resaltada
- «La regla» → `regla`: un recuadro «regla»
- «la densidad cruzada con una señal filtrada» → `cruz`: «S_y(·)» junto a una caja de filtro
- «se multiplica por el conjugado» → `mult`: «× conjugado»
- «de la respuesta del filtro» → `resp`: «de la respuesta H»
- «el conjugado de uno entre F» → `conj`: «(1/F)*»
- «uno entre F de zeta a la menos uno» → `res`: «= 1 / F(z⁻¹)»

---

# Escena 17 — SegundoPasoParteCausal

**Capítulo YouTube:** Segundo paso: la parte causal

**Objetivo:** con la señal blanca, calcular la solución sin restricción y cortar m < 0; el corchete ₊.

## Narración

<!-- b1 -->
La cruzada entre i griega y la innovación vale, entonces, la cruzada entre i griega y equis, dividida entre F de zeta a la menos uno. Segundo paso: con la señal blanca aplicamos lo de las mediciones blancas, calcular la solución sin restricción y cortar la parte de eme negativo. Lo escribimos con un corchete más: la parte causal, la de las posiciones cero y positivas.

- «La cruzada entre i griega y la innovación» → `cr1`: aparece «S_yε»
- «la cruzada entre i griega y equis» → `cr2`: se completa «= S_yx»
- «dividida entre F de zeta a la menos uno» → `div`: se añade «/ F(z⁻¹)»
- «Segundo paso» → `p2`: la casilla 2 se ilumina, «parte causal»
- «con la señal blanca» → `blanca`: la tira de la moneda sobre ε
- «calcular la solución sin restricción» → `sinres`: una secuencia con dos colas, a izquierda y derecha de m = 0
- «cortar la parte de eme negativo» → `corta`: una tijera corta la cola de m < 0
- «un corchete más» → `corch`: aparece «[ · ]₊» alrededor de la fórmula
- «la parte causal» → `pcausal`: el rótulo «parte causal» bajo el corchete
- «las posiciones cero y positivas» → `pos`: un marco verde sobre m ≥ 0

---

# Escena 18 — TercerPasoDeshacer

**Capítulo YouTube:** Tercer paso: deshacer y la fórmula completa

**Objetivo:** la fórmula del filtro de Wiener causal, H(z) = 1/(σ² F(z)) [S_yx(z)/F(z⁻¹)]₊, leída de derecha a izquierda.

## Narración

<!-- b1 -->
Tercer paso: deshacer el blanqueo, multiplicando por uno entre F. El filtro completo es uno entre sigma cuadrado por F de zeta, por la parte causal de la cruzada dividida entre F de zeta a la menos uno. Se lee de derecha a izquierda: blanquear, quedarse con lo causal y deshacer. Justo lo que anunciamos.

- «Tercer paso» → `p3`: la casilla 3 se ilumina, «deshacer»
- «deshacer el blanqueo» → `deshacer`: la cadena «ε → [F] → ŷ»
- «multiplicando por uno entre F» → `mult`: «× 1/F»
- «El filtro completo» → `completo`: aparece «H(z) =»
- «uno entre sigma cuadrado por F de zeta» → `pizq`: se añade «1 / (σ² F(z))», en el color del paso 3
- «la parte causal de la cruzada» → `pc`: se añade «[ S_yx(z) … ]₊», en el color del paso 2
- «dividida entre F de zeta a la menos uno» → `div`: dentro del corchete, «/ F(z⁻¹)», en el color del paso 1
- «de derecha a izquierda» → `der`: una flecha de derecha a izquierda bajo la fórmula
- «blanquear, quedarse con lo causal y deshacer» → `tresp`: los tres colores se encienden en orden: 1, 2 y 3
- «Justo lo que anunciamos» → `anunc`: sello «filtro de Wiener causal»

---

# Escena 19 — DosComprobaciones

**Capítulo YouTube:** Dos comprobaciones de la fórmula

**Objetivo:** con mediciones blancas sale el corte; sin cortar sale el no causal. Lo que se pierde por ser causal está en el corchete.

## Narración

<!-- b1 -->
Dos comprobaciones. Si lo medido ya fuera blanco, F sería uno, y la fórmula dice que hache es la cruzada dividida entre sigma cuadrado, cortada: es el caso de las mediciones blancas. Y si no cortásemos nada, el corchete desaparecería y quedaría la cruzada entre sigma cuadrado por F por F al revés, que es la densidad de lo medido: el filtro no causal de siempre.

- «Dos comprobaciones» → `dos`: dos casillas, «1» y «2», junto a la fórmula
- «Si lo medido ya fuera blanco» → `blanco`: la tira de la moneda
- «F sería uno» → `f1`: en la fórmula, «F = 1» sustituye a F(z)
- «la cruzada dividida entre sigma cuadrado, cortada» → `h`: queda «h = C_yx / σ² para m ≥ 0»
- «es el caso de las mediciones blancas» → `caso`: un tilde verde y la tabla 1 · 0,5 · 0,25 de la escena 09
- «si no cortásemos nada» → `nocort`: la tijera se aparta de la fórmula
- «el corchete desaparecería» → `desap`: el «[ ]₊» se tacha y se borra
- «la cruzada entre sigma cuadrado por F por F al revés» → `res`: queda «S_yx / (σ² F(z) F(z⁻¹))»
- «la densidad de lo medido» → `dens`: debajo, «= S_yx / S_xx»
- «el filtro no causal de siempre» → `noc`: un tilde verde y el rótulo «el no causal»

<!-- b2 -->
La fórmula es el filtro no causal con una diferencia: el corchete. Lo que se pierde por ser causal está escondido ahí. La parte causal parece un truco, pero solo se ve al hacer las cuentas.

- «el filtro no causal con una diferencia» → `dif`: la fórmula causal y la del no causal, una junto a otra
- «el corchete» → `corchete`: el «[ ]₊» se resalta en ámbar
- «Lo que se pierde por ser causal» → `pierde`: sobre las barras 0,686 y 0,7386 aparece «¿cuánto se pierde?»
- «está escondido ahí» → `escondido`: una lupa sobre el corchete
- «parece un truco» → `truco`: un «¿truco?» en rojo
- «solo se ve al hacer las cuentas» → `cuentas`: debajo, «con el sensor»

---

# Escena 20 — Cierre

**Capítulo YouTube:** Lo que viene: el sensor, de punta a punta

## Narración

<!-- b1 -->
Sin el futuro, la igualdad solo vale en media recta, y ya no se puede transformar y dividir. Con mediciones blancas basta cortar; si no lo son, se blanquean primero, y la fórmula guarda en un corchete lo que se pierde. La fórmula ya está. Falta usarla, con el sensor, de principio a fin. En el próximo episodio: el sensor, de punta a punta.

- «Sin el futuro» → `sinfut`: el reloj del aparato con el futuro tachado
- «solo vale en media recta» → `media`: un eje m con solo la mitad derecha iluminada
- «ya no se puede transformar y dividir» → `nodiv`: una división «S_yx / S_xx» tachada
- «Con mediciones blancas basta cortar» → `cortar`: la tijera sobre la tabla 1 · 0,5 · 0,25
- «se blanquean primero» → `blanq`: la cadena «x → [1/F] → ε»
- «un corchete» → `corch`: aparece «[ · ]₊» en ámbar
- «La fórmula ya está» → `ya`: la fórmula completa del filtro causal
- «Falta usarla» → `usar`: el termómetro del sensor al lado de la fórmula
- «de principio a fin» → `fin`: una flecha recorre el sensor de la entrada a la salida
- «En el próximo episodio» → `proximo`: el reloj del aparato avanza
- «el sensor, de punta a punta» → `titulo`: el título «El sensor, de punta a punta» entra con rebote
