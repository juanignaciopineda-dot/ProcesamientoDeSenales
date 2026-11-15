# Episodio 5 — El sensor, de punta a punta

Capítulo 12 (Estimación de señales), episodio 5 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 18 a 21), más un gancho, un repaso de los tres pasos y un cierre nuevos.

**Estado:** texto ⭐ aprobado por el usuario. Escenas `s01`–`s12` animadas; borrador 480p15 de 9:48 con 0 avisos, hojas de contacto revisadas. Falta: visto bueno del usuario al mp4 (paso 15) y render final.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Un filtro con infinitos coeficientes que se calcula con dos multiplicaciones. Y un error que baja y baja, y se clava en cero coma siete tres ocho seis. Hoy sabemos por qué.»
- ⭐ Escena 05 (repaso, primer bloque): recuerda los tres pasos de la fórmula causal del episodio anterior, porque el episodio se ve suelto.
- ⭐ Escena 12 (cierre): repasa el episodio y anuncia el E6 por su título, «Lo nuevo y lo que ya sabías».

Retoque de una frase del guion base (escena 19, bloque 5, ahora escena 07): «¡Son los coeficientes de la escena cinco!» pasa a «¡Son los coeficientes del filtro finito del segundo episodio!», porque no hay escenas numeradas para quien ve el vídeo.

Reparto de las escenas del guion base: 18 → escenas 03 y 04; 19 → 05 a 07; 20 → 08 y 09; 21 → 10 y 11.
Solo se partieron bloques enteros en escenas atómicas: el resto del texto del guion base no cambia.

Bucles de este episodio: «¿a qué se acerca el error y por qué 0,157?» (sembrado en el segundo episodio; se paga en la escena 07); el sensor del Cap. 10 (0,8 y 0,74) que termina en 0,7386 (escena 08); «la muestra de ahora vale más que todo el futuro» (se siembra al final de la escena 11 y se paga en el E6).

---

# Escena 01 — Gancho

**Capítulo YouTube:** Infinitos coeficientes, dos cuentas

## Narración

<!-- b1 -->
Un filtro con infinitos coeficientes que se calcula con dos multiplicaciones. Y un error que baja y baja, y se clava en cero coma siete tres ocho seis. Hoy sabemos por qué.

- «infinitos coeficientes» → `infinitos`: una fila de barras que decae y se pierde hacia la derecha, con puntos suspensivos
- «dos multiplicaciones» → `dos`: bajo la fila entran dos cajitas «× 0,157» y «× 0,7386»
- «Y un error que baja» → `baja`: barras de error que bajan escalón a escalón
- «se clava en cero coma siete tres ocho seis» → `clava`: la última barra queda fija con «0,7386» en rojo
- «Hoy sabemos por qué» → `porque`: un signo de pregunta sobre la barra y una lupa que se acerca

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** El sensor, de punta a punta

## Narración

<!-- b1 -->
El sensor, de punta a punta.

- «El sensor» → `t1`: «El sensor,» entra con rebote junto al termómetro con su cable
- «de punta a punta» → `t2`: «de punta a punta» entra debajo, con la etiqueta «Capítulo 12 · Estimación de señales»

---

# Escena 03 — FactorizarLoMedido

**Capítulo YouTube:** Factorizar lo medido

**Objetivo:** escribir la densidad de lo medido como una sola fracción, con un numerador que se pueda factorizar.

## Narración

<!-- b1 -->
Factoricemos, a mano, la densidad de lo medido en el sensor: la de la temperatura, dos coma cinco seis entre el módulo al cuadrado de uno menos cero coma seis e elevado a menos jota omega, más el uno del ruido. Ese denominador vale uno coma tres seis menos cero coma seis por zeta más zeta a la menos uno. Al sumar las fracciones, el numerador queda tres coma nueve dos menos cero coma seis por esa misma suma.

- «Factoricemos, a mano» → `factor`: el termómetro con su cable pasa a un rincón y arriba entra «S_xx = ?» en cian
- «la densidad de lo medido» → `medido`: «S_xx = S_yy + 1» se construye por piezas, S_yy en azul y el 1 en magenta
- «dos coma cinco seis» → `numer`: sobre una raya de fracción entra «2,56»
- «entre el módulo al cuadrado de uno menos cero coma seis» → `modulo`: debajo de la raya entra «|1 − 0,6 e^{−jΩ}|²»
- «e elevado a menos jota omega» → `exp`: la exponencial «e^{−jΩ}» se resalta en ámbar
- «más el uno del ruido» → `ruido`: a la derecha entra «+ 1» en magenta
- «Ese denominador vale» → `deno`: una llave resalta el denominador y debajo empieza su desarrollo «1 + 0,36 − 0,6 (e^{jΩ} + e^{−jΩ})»
- «uno coma tres seis» → `desarrollo`: queda «1,36» y a su lado empieza «− 0,6 (z + z⁻¹)»
- «cero coma seis por zeta más zeta a la menos uno» → `zeta`: se completa «− 0,6 (z + z⁻¹)» y se nota que z = e^{jΩ}
- «Al sumar las fracciones» → `suma`: las dos fracciones se funden en una sola
- «el numerador queda tres coma nueve dos» → `tres92`: sobre la raya aparece «3,92»
- «por esa misma suma» → `misma`: sigue «− 0,6 (z + z⁻¹)», con un trazo que une las dos sumas iguales

<!-- b2 -->
Queremos escribir ese numerador como una constante, kappa, por uno menos ro zeta a la menos uno, por uno menos ro zeta. Al multiplicar, aparece kappa por uno más ro al cuadrado, menos kappa ro por la suma. Igualamos: kappa por ro vale cero coma seis, y kappa por uno más ro al cuadrado, tres coma nueve dos.

- «Queremos escribir ese numerador» → `queremos`: el numerador «3,92 − 0,6 (z + z⁻¹)» se destaca en ámbar
- «una constante, kappa» → `kappa`: debajo entra «κ» en ámbar
- «por uno menos ro zeta a la menos uno» → `ro1`: sigue «(1 − ρ z⁻¹)»
- «por uno menos ro zeta.» → `ro2`: sigue «(1 − ρ z)»
- «Al multiplicar» → `multiplica`: los dos paréntesis se multiplican con un destello
- «aparece kappa por uno más ro al cuadrado» → `masro2`: aparece «κ (1 + ρ²)»
- «menos kappa ro por la suma» → `menoskro`: sigue «− κ ρ (z + z⁻¹)»
- «Igualamos» → `igualamos`: las dos expresiones quedan una sobre otra, con un signo «=» entre ellas
- «kappa por ro vale cero coma seis» → `kro`: se ilumina «κρ = 0,6»
- «tres coma nueve dos» → `k392`: se ilumina «κ (1 + ρ²) = 3,92»

---

# Escena 04 — ElModeladorDelSensor

**Capítulo YouTube:** El modelador del sensor

**Objetivo:** resolver la ecuación de segundo grado, elegir la raíz de dentro y comprobar con la potencia.

## Narración

<!-- b1 -->
Dividimos una entre la otra y desaparece kappa: uno más ro al cuadrado, entre ro, es seis coma cinco tres. Una ecuación de segundo grado. Tiene dos soluciones: seis coma tres siete siete y cero coma uno cinco siete. Su producto es uno: vienen siempre en parejas, una dentro y otra fuera del círculo. Nos quedamos con la de dentro, la de fase mínima. Kappa vale tres coma ocho dos seis.

- «Dividimos una entre la otra» → `divide`: las dos igualdades se ponen una sobre otra con una raya de división
- «desaparece kappa» → `desaparece`: las dos κ se tachan
- «uno más ro al cuadrado, entre ro» → `razon`: queda «(1 + ρ²)/ρ»
- «seis coma cinco tres» → `seis53`: se completa «= 6,53»
- «Una ecuación de segundo grado» → `segundo`: se reordena como «ρ² − 6,53 ρ + 1 = 0» con el rótulo «segundo grado»
- «Tiene dos soluciones» → `dossol`: bajo la ecuación aparece un eje real vacío con «dos soluciones»
- «seis coma tres siete siete» → `r6377`: sobre un eje real aparece una marca en 6,377
- «cero coma uno cinco siete» → `r0157`: aparece otra marca en 0,157
- «Su producto es uno» → `producto`: «0,157 · 6,377 = 1» une las dos marcas con un arco
- «una dentro y otra fuera del círculo» → `circulo`: se dibuja el círculo unidad; 0,157 queda dentro y 6,377 fuera
- «Nos quedamos con la de dentro» → `dentro`: la marca de 6,377 se atenúa y la de 0,157 se ilumina en verde
- «la de fase mínima» → `faseminima`: se rotula «fase mínima»
- «Kappa vale tres coma ocho dos seis» → `k3826`: entra «κ = 3,826» en ámbar

<!-- b2 -->
El filtro de fase mínima es F de zeta igual a uno menos cero coma uno cinco siete zeta a la menos uno, entre uno menos cero coma seis zeta a la menos uno. Tiene un polo en cero coma seis, la memoria de la temperatura, y un cero en cero coma uno cinco siete, que pone el ruido. Los dos, dentro. Y sigma cuadrado vale tres coma ocho dos seis.

- «El filtro de fase mínima» → `filtro`: entra «F(z) =» en ámbar y debajo el plano z con el círculo unidad
- «uno menos cero coma uno cinco siete zeta a la menos uno» → `numf`: sobre la raya entra «1 − 0,157 z⁻¹»
- «entre uno menos cero coma seis zeta a la menos uno» → `denf`: bajo la raya entra «1 − 0,6 z⁻¹»
- «Tiene un polo en cero coma seis» → `polo`: en el plano z aparece una × en 0,6
- «la memoria de la temperatura» → `memoria`: la × se rotula «memoria»
- «un cero en cero coma uno cinco siete» → `cero`: aparece una ○ en 0,157
- «que pone el ruido» → `poneruido`: la ○ se rotula «ruido» en magenta
- «Los dos, dentro» → `dentro2`: el círculo se ilumina con las dos marcas dentro
- «Y sigma cuadrado vale tres coma ocho dos seis» → `sigma`: entra «σ² = 3,826»

<!-- b3 -->
Comprobémoslo con la potencia. La respuesta de F al impulso es uno, cero coma cuatro cuatro tres, cero coma dos seis seis, y así; la suma de sus cuadrados vale uno coma tres cero siete. Multiplicada por tres coma ocho dos seis da cinco: justo la potencia de lo medido, cuatro más uno. Lo medido se comporta como una moneda pasada por este filtro. Ahora falta la parte causal.

- «Comprobémoslo con la potencia» → `compro`: el plano z sale y entra una tira de barras vacía
- «La respuesta de F al impulso» → `respf`: un impulso entra en la caja F y sale una secuencia
- «uno, cero coma cuatro cuatro tres, cero coma dos seis seis, y así» → `impulso`: aparecen las barras 1, 0,443 y 0,266, y luego otras más bajas
- «y así» → `yasi`: las barras se prolongan, cada vez más bajas
- «la suma de sus cuadrados» → `cuadrados`: cada barra se eleva al cuadrado y se suman
- «uno coma tres cero siete» → `s1307`: entra «Σ = 1,307»
- «Multiplicada por tres coma ocho dos seis» → `multiplica2`: «3,826 · 1,307» se construye en la misma línea
- «da cinco» → `cinco`: aparece «= 5» en verde
- «cuatro más uno» → `cuatromasuno`: debajo, «4 + 1» en azul y magenta, con una tilde verde
- «una moneda pasada por este filtro» → `moneda`: la cadena «ε blanca → F → x» con una moneda a la izquierda
- «Ahora falta la parte causal» → `falta`: aparece una tijera pequeña

---

# Escena 05 — PrimerPaso

**Capítulo YouTube:** Primer paso: blanquear

**Objetivo:** recordar los tres pasos de la fórmula causal y hacer el primero con el sensor.

## Narración

<!-- b1 -->
Recordemos los tres pasos de la fórmula causal. Primero, blanquear lo medido dividiendo entre el factor de fase mínima. Segundo, quedarnos con la parte causal, la de las posiciones cero y positivas. Tercero, deshacer el blanqueo. Hagámoslos con el sensor.

- «los tres pasos» → `tres`: entra un recuadro con tres casillas vacías, una por color
- «Primero, blanquear» → `uno`: la casilla uno se llena con «blanquear» y un dibujo «x → 1/F → ε»
- «dividiendo entre el factor de fase mínima» → `divide`: junto a la casilla, «÷ F»
- «Segundo, quedarnos con la parte causal» → `dos`: la casilla dos se llena con una tijera y «parte causal»
- «las posiciones cero y positivas» → `cero`: una secuencia de dos colas con la mitad m ≥ 0 resaltada
- «Tercero, deshacer el blanqueo» → `tres3`: la casilla tres se llena con «deshacer» y «× 1/F»
- «Hagámoslos con el sensor» → `sensor`: el recuadro se encoge a un rincón y aparece el termómetro con su cable

<!-- b2 -->
Primer paso: la cruzada entre i griega y lo medido es la densidad de la temperatura, porque el ruido no aporta. Dividida entre F de zeta a la menos uno, sale dos coma cinco seis entre uno menos cero coma seis zeta a la menos uno, por uno menos cero coma uno cinco siete zeta. Es un producto de dos fracciones, y en el tiempo eso es una secuencia con dos colas.

- «Primer paso» → `paso1`: la casilla uno del rincón se ilumina
- «la cruzada entre i griega y lo medido» → `cruzada`: entra «S_yx» en ámbar
- «es la densidad de la temperatura» → `igual`: «= S_yy = 2,56 / [(1 − 0,6 z⁻¹)(1 − 0,6 z)]» se construye por piezas
- «porque el ruido no aporta» → `noaporta`: el ruido magenta aparece y se desvanece, sin tocar la fórmula
- «Dividida entre F de zeta a la menos uno» → `divide2`: debajo entra «÷ F(z⁻¹) = (1 − 0,157 z) / (1 − 0,6 z)»
- «sale dos coma cinco seis» → `sale256`: aparece el resultado y sobre su raya «2,56»
- «entre uno menos cero coma seis zeta a la menos uno» → `fr1`: bajo la raya, «(1 − 0,6 z⁻¹)»
- «por uno menos cero coma uno cinco siete zeta» → `fr2`: sigue «(1 − 0,157 z)», el factor «(1 − 0,6 z)» se tacha arriba y abajo
- «un producto de dos fracciones» → `producto`: las dos fracciones quedan marcadas con llaves
- «una secuencia con dos colas» → `colas`: la fórmula se desplaza y debajo se esboza una secuencia con una cola a cada lado

---

# Escena 06 — DosColasYUnaTijera

**Capítulo YouTube:** Dos colas y una tijera

**Objetivo:** ver la secuencia de dos colas, calcular su valor central y cortar la cola de la izquierda.

## Narración

<!-- b1 -->
A la derecha, para eme mayor o igual que cero, cae como cero coma seis elevado a eme. A la izquierda, cae como cero coma uno cinco siete elevado al valor absoluto de eme. Y en el centro, el valor común: dos coma cinco seis por la suma de una progresión geométrica de razón cero coma cero nueve cuatro, es decir, dos coma cinco seis entre cero coma nueve cero seis: dos coma ocho dos seis.

- «A la derecha» → `derecha`: se dibujan las barras de la derecha en azul
- «para eme mayor o igual que cero» → `mpos`: bajo ellas, «m ≥ 0»
- «cae como cero coma seis elevado a eme» → `cae06`: sobre las barras, «K · 0,6^m»
- «A la izquierda» → `izquierda`: se dibujan las barras de la izquierda en magenta, más pegadas al eje
- «cae como cero coma uno cinco siete» → `cae157`: sobre ellas, «K · 0,157»
- «al valor absoluto de eme» → `abs`: se completa «K · 0,157^|m|»
- «Y en el centro, el valor común» → `centro`: la barra central en m = 0 se ilumina en ámbar
- «dos coma cinco seis por la suma de una progresión geométrica» → `suma`: entra «2,56 · (1 + 0,094 + 0,094² + …)»
- «de razón cero coma cero nueve cuatro» → `razon`: una llave bajo la suma con «0,6 · 0,157 = 0,094»
- «dos coma cinco seis entre cero coma nueve cero seis» → `cociente`: la suma se transforma en «2,56 / 0,906»
- «dos coma ocho dos seis» → `k2826`: entra «K = 2,826» sobre la barra central

<!-- b2 -->
Segundo paso: quedarnos con la parte causal. La cola de la izquierda, la de eme negativo, se corta. Queda la de la derecha, dos coma ocho dos seis por cero coma seis elevado a eme, que en zeta es dos coma ocho dos seis entre uno menos cero coma seis zeta a la menos uno.

- «Segundo paso» → `paso2`: la casilla dos del rincón se ilumina
- «La cola de la izquierda, la de eme negativo» → `colaizq`: la cola magenta parpadea
- «se corta» → `corta`: una tijera atraviesa el eje y la cola magenta cae y se desvanece
- «Queda la de la derecha» → `queda`: la cola azul y la barra central quedan solas
- «dos coma ocho dos seis por cero coma seis elevado a eme» → `kpor06`: bajo ellas, «2,826 · 0,6^m»
- «que en zeta es» → `enz`: aparece una flecha hacia la derecha
- «dos coma ocho dos seis entre uno menos cero coma seis» → `fraccion`: la flecha termina en «2,826 / (1 − 0,6 …»
- «zeta a la menos uno.» → `finalz`: se completa «z⁻¹)» y la fracción queda enmarcada

---

# Escena 07 — DeshacerElBlanqueo

**Capítulo YouTube:** Deshacer el blanqueo

**Objetivo:** terminar la fórmula causal y ver que sus coeficientes son los del filtro finito: se paga el bucle del 0,157.

## Narración

<!-- b1 -->
Tercer paso: deshacer el blanqueo, multiplicando por uno entre tres coma ocho dos seis F. Uno menos cero coma seis zeta a la menos uno, arriba, se cancela con el mismo factor del segundo paso. Queda cero coma siete tres ocho seis entre uno menos cero coma uno cinco siete zeta a la menos uno. Un filtro de un solo polo.

- «Tercer paso» → `paso3`: la casilla tres del rincón se ilumina
- «multiplicando por uno entre tres coma ocho dos seis F» → `multiplica`: entra «H = 1 / (3,826 F) · 2,826 / (1 − 0,6 z⁻¹)» por piezas
- «Uno menos cero coma seis zeta a la menos uno, arriba» → `arriba`: se resalta «(1 − 0,6 z⁻¹)» en el numerador de 1/F
- «se cancela con el mismo factor del segundo paso» → `cancela`: se resalta el mismo factor abajo y los dos se tachan
- «Queda cero coma siete tres ocho seis» → `q07386`: sobre la raya entra «0,7386»
- «entre uno menos cero coma uno cinco siete» → `deno157`: bajo la raya, «1 − 0,157 …»
- «zeta a la menos uno.» → `zinv`: se completa «z⁻¹» y la fracción queda enmarcada
- «Un filtro de un solo polo» → `unpolo`: «H(z)» aparece como sello y una × en 0,157 dentro del círculo

<!-- b2 -->
Su respuesta al impulso: cero coma siete tres ocho seis; cero coma uno uno cinco ocho; cero coma cero uno ocho dos; cero coma cero cero dos ocho. ¡Son los coeficientes del filtro finito del segundo episodio! Cada uno es cero coma uno cinco siete veces el anterior, y ahora sabemos por qué: es el cero de la factorización. El filtro de Wiener causal es exactamente el límite del filtro finito.

- «Su respuesta al impulso» → `impulso`: aparece un eje con barras vacías
- «cero coma siete tres ocho seis» → `b1`: sube la primera barra con «0,7386»
- «cero coma uno uno cinco ocho» → `b2`: sube la segunda con «0,1158»
- «cero coma cero uno ocho dos» → `b3`: sube la tercera con «0,0182»
- «cero coma cero cero dos ocho» → `b4`: sube la cuarta con «0,0028»
- «¡Son los coeficientes» → `coinciden`: encima aparecen las barras del filtro finito de E2
- «del filtro finito del segundo episodio» → `finito`: las barras de E2 y las nuevas se superponen, idénticas
- «cero coma uno cinco siete veces el anterior» → `veces`: flechas curvas «× 0,157» unen cada barra con la siguiente
- «ahora sabemos por qué» → `sabemos`: sobre las flechas, un signo «¿por qué?» que se aclara
- «es el cero de la factorización» → `cerofact`: el cero ○ en 0,157 del plano z se ilumina junto al «0,157»
- «El filtro de Wiener causal» → `wiener`: entra el sello «filtro de Wiener causal»
- «exactamente el límite del filtro finito» → `limite`: las barras de L = 1, 2, 3 se alinean con las del infinito y entra el sello «Wiener causal = límite del FIR»

---

# Escena 08 — DosMultiplicaciones

**Capítulo YouTube:** Un filtro con dos multiplicaciones

**Objetivo:** pasar del cociente en z a la recursión, hacer una iteración a mano y recordar que su error es el límite del filtro finito.

## Narración

<!-- b1 -->
Un filtro con un polo se implementa con muy pocas cuentas. La ecuación que lo describe es esta: la estimación de ahora es cero coma uno cinco siete por la estimación anterior, más cero coma siete tres ocho seis por lo que acaba de llegar. Dos multiplicaciones y una suma, para un filtro con infinitos coeficientes.

- «Un filtro con un polo» → `unfiltro`: aparece «H(z) = 0,7386 / (1 − 0,157 z⁻¹)»
- «se implementa con muy pocas cuentas» → `pocas`: la fórmula se mueve arriba y debajo se despeja «ŷ[n] − 0,157 ŷ[n − 1] = 0,7386 x[n]»
- «La ecuación que lo describe es esta» → `ecuacion`: el cociente se enmarca y una flecha lo lleva a la recursión
- «la estimación de ahora» → `ahora`: entra «ŷ[n] =» en ámbar
- «cero coma uno cinco siete por la estimación anterior» → `anterior`: sigue «0,157 ŷ[n − 1]», con la parte ŷ en ámbar
- «más cero coma siete tres ocho seis por lo que acaba de llegar» → `llegar`: sigue «+ 0,7386 x[n]», con x en cian
- «Dos multiplicaciones y una suma» → `dos`: un diagrama de bloques con dos amplificadores, un sumador y un retardo z⁻¹ en retroalimentación
- «infinitos coeficientes» → `infinitos`: junto al diagrama, la fila de barras que decae sin fin

<!-- b2 -->
Probémoslo. Supongamos que la estimación anterior era uno y llega una medición de dos. La nueva estimación es cero coma uno cinco siete por uno, más cero coma siete tres ocho seis por dos: uno coma seis tres cuatro. La estimación anterior aporta una memoria pequeña, y casi todo el peso lo lleva la medición nueva.

- «la estimación anterior era uno» → `anterior1`: en el diagrama, el retardo se carga con «1»
- «llega una medición de dos» → `llega2`: entra una flecha cian desde la izquierda con «2»
- «cero coma uno cinco siete por uno» → `por1`: «0,157 · 1» sube por el primer amplificador y da «0,157»
- «más cero coma siete tres ocho seis por dos» → `por2`: «0,7386 · 2» baja por el segundo y da «1,477»
- «uno coma seis tres cuatro» → `suma`: el sumador da «1,634» y el número se ilumina en ámbar
- «una memoria pequeña» → `pequena`: una llave fina sobre el 0,157 con «memoria»
- «casi todo el peso lo lleva la medición nueva» → `peso`: una llave gruesa sobre el 1,477 con «medición»

<!-- b3 -->
Y el error de este filtro es cero coma siete tres ocho seis: el número al que convergía el filtro finito. Con tres coeficientes ya estábamos en cero coma siete tres ocho siete. Es decir, el filtro de Wiener causal no es un filtro distinto al que resolvíamos con matrices; es aquel, con la ventana llevada hasta el infinito, y calculado de un golpe.

- «el error de este filtro» → `error`: el diagrama sale y entra una tabla de barras de error
- «cero coma siete tres ocho seis» → `e07386`: aparece la barra final con «0,7386» en rojo
- «el número al que convergía el filtro finito» → `converge`: aparecen las barras anteriores de 4, 0,8 y 0,740, que bajan hacia ella
- «Con tres coeficientes» → `tres`: la barra «L = 3» se ilumina
- «cero coma siete tres ocho siete» → `e07387`: se rotula «0,7387», casi al nivel de la final
- «Es decir» → `esdecir`: las dos barras finales, 0,7387 y 0,7386, se alinean con un «=»
- «no es un filtro distinto» → `distinto`: un signo «≠» tachado entre «Wiener causal» y «FIR»
- «al que resolvíamos con matrices» → `matrices`: aparece la matriz de Toeplitz del primer episodio
- «es aquel» → `aquel`: una flecha las une
- «con la ventana llevada hasta el infinito» → `ventana`: una ventana de muestras sobre x[n] que se ensancha sin fin
- «calculado de un golpe» → `golpe`: la ventana se reemplaza por la caja «H(z)» de un solo trazo

---

# Escena 09 — ElPoloDelFiltro

**Capítulo YouTube:** Por qué el polo no es 0,6

**Objetivo:** entender por qué el polo del filtro (0,157) no es el de la señal (0,6) mirando los dos extremos de ruido, y ver el coste de no mirar el futuro en la ganancia en continua.

## Narración

<!-- b1 -->
Queda una pregunta: ¿por qué el polo del filtro, cero coma uno cinco siete, no es el de la señal, cero coma seis? Mira los extremos. Con muy poco ruido, el filtro se fía del dato de ahora y casi no usa el pasado: el polo se acerca a cero. Con muchísimo ruido, se fía de la memoria de la señal y el polo se acerca a cero coma seis.

- «Queda una pregunta» → `pregunta`: sobre un eje de 0 a 1 aparecen dos marcas, 0,157 y 0,6
- «el polo del filtro, cero coma uno cinco siete» → `polo157`: la marca 0,157 en ámbar, rotulada «filtro»
- «el de la señal, cero coma seis» → `polo6`: la marca 0,6 en azul, rotulada «señal»
- «Mira los extremos» → `extremos`: se añade un deslizador de ruido, de «poco» a «mucho»
- «Con muy poco ruido» → `poco`: el deslizador va a «poco» y el polo del filtro baja hacia 0
- «el filtro se fía del dato de ahora» → `fia`: aparece una flecha cian gruesa de x[n] a ŷ[n] y una fina del pasado
- «casi no usa el pasado» → `nopasado`: la flecha del pasado se vuelve casi invisible
- «el polo se acerca a cero» → `acerca0`: la marca del polo se pega al 0
- «Con muchísimo ruido» → `mucho`: el deslizador va a «mucho» y el polo sube
- «se fía de la memoria de la señal» → `memoria`: la flecha del pasado se vuelve gruesa y la del dato, fina
- «el polo se acerca a cero coma seis» → `acerca06`: la marca del polo se acerca a la de la señal

<!-- b2 -->
Una última comprobación: la ganancia en continua del filtro es cero coma ocho ocho. Menor que la del filtro no causal, cero coma nueve cuatro: sin poder mirar el futuro, duda más y tira más hacia la media. Ese cero coma siete tres ocho seis frente a cero coma seis ocho seis del no causal es lo que cuesta no ver el futuro. Vamos a ponerle precio exacto.

- «la ganancia en continua» → `continua`: sale el eje y entra la curva de ganancia del filtro con un punto en Ω = 0
- «cero coma ocho ocho» → `g088`: el punto se rotula «0,88» en ámbar
- «Menor que la del filtro no causal» → `menor`: aparece la curva no causal por encima
- «cero coma nueve cuatro» → `g094`: su punto en Ω = 0 se rotula «0,94»
- «sin poder mirar el futuro, duda más» → `duda`: una flecha corta entre los dos puntos con «duda más»
- «tira más hacia la media» → `media`: la curva ámbar se aplana un poco hacia el cero
- «cero coma siete tres ocho seis frente a» → `frente`: aparece la barra de error 0,7386
- «del no causal» → `delno`: a su lado la barra 0,686
- «lo que cuesta no ver el futuro» → `cuesta`: una llave entre las dos alturas con «precio»
- «Vamos a ponerle precio exacto» → `exacto`: un signo «€» o una etiqueta «¿cuánto?» sobre la llave

---

# Escena 10 — ElErrorEnLaSenalBlanca

**Capítulo YouTube:** El precio de la causalidad

**Objetivo:** ver que, con la señal blanqueada, el error se separa en un término por coeficiente.

## Narración

<!-- b1 -->
Pongamos precio a la causalidad. Trabajamos con la señal blanqueada, donde todo es más limpio. El error de un estimador que suma coeficientes por la innovación es la varianza de la señal, menos dos veces la suma de cada coeficiente por su correlación, más sigma cuadrado por la suma de los coeficientes al cuadrado. Como la innovación es blanca, cada posición aporta su propio término, sin mezclarse con las demás.

- «Pongamos precio a la causalidad» → `precio`: entra «precio de la causalidad» con una etiqueta de precio
- «la señal blanqueada» → `blanqueada`: la cadena «x → 1/F → ε blanca»
- «El error de un estimador» → `error`: entra «error =» en rojo
- «la varianza de la señal» → `varianza`: sigue «σ_y²» en azul
- «menos dos veces la suma de cada coeficiente por su correlación» → `menos`: sigue «− 2 Σ g[m] R[m]»
- «más sigma cuadrado por la suma de los coeficientes al cuadrado» → `mas`: sigue «+ σ² Σ g[m]²»
- «Como la innovación es blanca» → `blanca`: la ε blanca de la cadena se resalta
- «cada posición aporta su propio término» → `propio`: la suma se despliega en columnas, una por m, cada una con su pequeño término
- «sin mezclarse con las demás» → `mezclarse`: líneas verticales separan las columnas

<!-- b2 -->
Cada término es una parábola en su coeficiente, y su punto más bajo está en la correlación dividida entre sigma cuadrado. Ahí aporta menos la correlación al cuadrado, entre sigma cuadrado. El filtro no causal puede colocar todos los coeficientes en su punto óptimo. El causal solo puede hacerlo con los de eme mayor o igual que cero: los de eme negativo tienen que valer cero, y ese término se pierde.

- «Cada término es una parábola» → `parabola`: una de las columnas se amplía y muestra su parábola
- «su punto más bajo» → `bajo`: el vértice se marca con un punto
- «la correlación dividida entre sigma cuadrado» → `vertice`: bajo el vértice, «g = R / σ²»
- «aporta menos la correlación al cuadrado, entre sigma cuadrado» → `aporta`: la altura del vértice queda como «− R² / σ²»
- «El filtro no causal puede colocar todos los coeficientes» → `nocausal`: todas las columnas muestran su vértice con un punto verde
- «en su punto óptimo» → `optimo`: los puntos verdes brillan sobre cada vértice
- «El causal solo puede hacerlo con los de eme mayor o igual que cero» → `causal`: las columnas de m ≥ 0 conservan el punto verde
- «los de eme negativo tienen que valer cero» → `negativo`: en las columnas de m < 0 el punto queda anclado en g = 0, lejos del vértice
- «ese término se pierde» → `pierde`: la distancia entre el punto anclado y el vértice se rellena de rojo

---

# Escena 11 — LoQueSePierde

**Capítulo YouTube:** Lo que cuesta no ver el futuro

**Objetivo:** ver que la pérdida es la energía de la cola cortada, calcularla con el sensor y comprobar que encaja con los dos errores.

## Narración

<!-- b1 -->
La diferencia entre los dos errores es, entonces, exactamente la suma de la correlación al cuadrado, para eme negativo, entre sigma cuadrado. Es la energía de la cola que hemos cortado. Y por Parseval, esa energía también es el área de su espectro. Lo que pierdes por ser causal es justo lo que habrías aprovechado del futuro.

- «La diferencia entre los dos errores» → `diferencia`: dos fórmulas de error, no causal y causal, una sobre otra
- «la suma de la correlación al cuadrado» → `suma`: aparece «Σ R[m]²» en rojo
- «para eme negativo» → `neg`: se completa «Σ_{m<0}» y «(1/σ²)» delante
- «la energía de la cola que hemos cortado» → `cola`: la secuencia de dos colas, con la de la izquierda en rojo y una balanza «energía»
- «por Parseval» → `parseval`: aparece el rótulo «Parseval: energía en el tiempo = área en frecuencia»
- «el área de su espectro» → `area`: junto a la cola, el área de su espectro se rellena de rojo
- «lo que habrías aprovechado del futuro» → `futuro`: la cola roja se rotula «futuro» y una flecha apunta al hueco entre errores

<!-- b2 -->
Con el sensor, la cola de la izquierda cae como cero coma uno cinco siete elevado a eme. Su energía es dos coma ocho dos seis al cuadrado entre tres coma ocho dos seis, que es dos coma cero ocho siete, por la suma de los cuadrados de la cola: una progresión de razón cero coma cero dos cinco que da cero coma cero dos cinco dos. Resultado: cero coma cero cinco dos seis.

- «la cola de la izquierda cae» → `colaizq`: la cola roja del sensor, con «K · 0,157^|m|»
- «elevado a eme» → `elevado`: se completa «K · 0,157^|m|»
- «Su energía» → `energia`: junto a la cola entra «energía =»
- «dos coma ocho dos seis al cuadrado entre tres coma ocho dos seis» → `cuenta1`: entra «2,826² / 3,826»
- «que es dos coma cero ocho siete» → `v2087`: sigue «= 2,087»
- «por la suma de los cuadrados de la cola» → `cuadrados`: las barras rojas se elevan al cuadrado y se suman
- «una progresión de razón cero coma cero dos cinco» → `razon`: llave con «0,157² = 0,025»
- «que da cero coma cero dos cinco dos» → `v0252`: entra «0,0252»
- «Resultado: cero coma cero cinco dos seis» → `resultado`: «2,087 · 0,0252 = 0,0526» en rojo

<!-- b3 -->
Cero coma siete tres ocho seis menos cero coma cero cinco dos seis es cero coma seis ocho seis: justo el error del filtro no causal. Todo encaja. Y la sorpresa: mirar todo el futuro solo mejora un siete por ciento. ¿Dónde está, entonces, la diferencia grande? En una decisión mucho más pequeña: usar o no la muestra de ahora.

- «Cero coma siete tres ocho seis menos cero coma cero cinco dos seis» → `resta`: «0,7386 − 0,0526» se construye por piezas
- «cero coma seis ocho seis» → `v0686`: sigue «= 0,686» en verde
- «justo el error del filtro no causal» → `nocausal`: una tilde y la barra del filtro no causal con 0,686
- «Todo encaja» → `encaja`: un destello recorre los tres números
- «mirar todo el futuro solo mejora un siete por ciento» → `siete`: una barra con una porción roja pequeña y «7 %»
- «¿Dónde está, entonces, la diferencia grande?» → `dondeesta`: la barra se difumina y aparece «¿?» sobre ella
- «En una decisión mucho más pequeña» → `decision`: la barra se encoge a una casilla pequeña
- «usar o no la muestra de ahora» → `ahora`: dos casillas «con x[n]» y «sin x[n]» con la pregunta flotando entre ellas

---

# Escena 12 — Cierre

**Capítulo YouTube:** Lo que viene

## Narración

<!-- b1 -->
Hoy hemos recorrido el sensor de punta a punta. Factorizamos, cortamos y deshicimos, y salió un filtro con un solo polo, que se calcula con dos multiplicaciones, y es el límite de todos los filtros finitos. Ser causal cuesta un siete por ciento. Pero la muestra de ahora parece valer mucho más que todo el futuro. ¿Cuánta información nueva trae cada muestra? Lo vemos en el próximo episodio: «Lo nuevo y lo que ya sabías».

- «Hoy hemos recorrido el sensor de punta a punta» → `recorrido`: pasan, a modo de tren, las piezas del episodio: densidad, factor F, cola cortada y filtro
- «Factorizamos, cortamos y deshicimos» → `tres`: tres iconos seguidos: ecuación de segundo grado, tijera y «× 1/F»
- «un solo polo» → `unpolo`: aparece el plano z con una × en 0,157
- «dos multiplicaciones» → `dos`: el diagrama de bloques con las dos cajitas
- «el límite de todos los filtros finitos» → `limite`: las barras de error de L = 1, 2, 3 y la final
- «cuesta un siete por ciento» → `siete`: la barra con la porción roja y «7 %»
- «la muestra de ahora parece valer mucho más» → `ahora`: una muestra cian brilla en una línea del tiempo, con el futuro difuminado
- «¿Cuánta información nueva trae cada muestra?» → `nueva`: sobre la muestra, un signo «?» en ámbar
- «Lo vemos en el próximo episodio» → `proximo`: una puerta se abre a la derecha
- «Lo nuevo y lo que ya sabías» → `titulo`: el título del E6 entra con rebote en ámbar
