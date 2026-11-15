# Episodio 7 — De Wiener a Kalman

Capítulo 12 (Estimación de señales), episodio 7 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 26 a 29), más un gancho y un cierre nuevos.

**Estado:** texto ⭐ aprobado por el usuario. Escenas `s01`–`s17` animadas; borrador 480p15 de 9:45 con 0 avisos y hojas de contacto revisadas. Falta: visto bueno del usuario al mp4 (paso 15) y render final.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «El filtro de Wiener y el de Kalman parecen dos inventos distintos. Con un sensor y una sola cuenta, hoy vemos que son el mismo.»
- ⭐ Escena 17 (cierre), bloque 1: «Y con esto se cierra el capítulo: Wiener y Kalman eran el mismo filtro, todo era una proyección, y el LMS llega al mismo sitio sin conocer las correlaciones.» El bloque 2 es el final de la escena 29 del guion base, con un retoque: «y empieza con una idea» pasa a «y el próximo capítulo empieza con una idea», que anuncia el E1 del Cap. 13 por su título, «Más datos no bastan».

Retoques de frases del guion base, porque el episodio se ve suelto (ya no hay «escenas» a las que remitir):
- escena 26, bloque 1: «que anunciamos al principio» → «que anunciamos al empezar el capítulo»;
- escena 26, bloque 3 (ahora escena 05): «el numerador de la escena dieciocho» → «el numerador del episodio quinto»;
- escena 27, bloques 1 y 3 (ahora escenas 07 y 08): «el predictor de la escena veinticuatro» → «el predictor del episodio anterior»; «el primer coeficiente del filtro de la escena diecinueve» → «el primer coeficiente del filtro causal del sensor»;
- escena 28 (ahora escenas 11 y 12): «la tabla de la escena cinco» → «la tabla del segundo episodio»; «la parábola del error de la escena dos» → «la parábola del error del primer episodio»;
- escena 29, bloque 1 (ahora escena 14): «En el siete» y «En el ocho» → «En el capítulo siete» y «En el capítulo ocho»;
- escena 29, bloque 3 (ahora escena 15): «hache es la cruzada entre la densidad» → «hache es la densidad cruzada dividida entre la densidad de lo medido».

Reparto de las escenas del guion base: 26 → escenas 03 a 06; 27 → 07 a 09; 28 → 10 a 13; 29 → 14 a 17.
Solo se partieron bloques enteros en escenas atómicas: el resto del texto del guion base no cambia.

Bucles de este episodio: «Kalman = Wiener» (el 0,443 y el 0,157 del predictor del E6 aparecen en la escena 07, y el 0,7386 del filtro del E5 es la ganancia de la escena 08); la parábola del error del E1 (escena 12: el filtro adaptativo baja rodando por ella); la tabla de errores del E2 (escena 11); la proyección del Cap. 7 y el Cap. 8 (escena 14); blanquear primero (Cap. 11 → escena 16 → Cap. 13); el colador de la voz y el murmullo del Cap. 11 (escena 14).

---

# Escena 01 — Gancho

**Capítulo YouTube:** Dos inventos, un solo filtro

## Narración

<!-- b1 -->
El filtro de Wiener y el de Kalman parecen dos inventos distintos. Con un sensor y una sola cuenta, hoy vemos que son el mismo.

- «El filtro de Wiener» → `wiener`: entra una caja azul «Wiener» con una curva de espectro dentro
- «el de Kalman» → `kalman`: entra a su lado una caja ámbar «Kalman» con un cohete dentro
- «dos inventos distintos» → `distintos`: entre las cajas aparece un «≠» y un «?» grande
- «Con un sensor» → `sensor`: el termómetro del sensor del capítulo 10 entra debajo de las dos cajas
- «una sola cuenta» → `cuenta`: del termómetro salen dos flechas, una a cada caja, y el mismo «0,443» sobre ambas
- «son el mismo» → `mismo`: el «≠» pasa a «=» y las dos cajas se funden en una sola

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** De Wiener a Kalman

## Narración

<!-- b1 -->
De Wiener a Kalman.

- «De Wiener» → `t1`: «De Wiener» entra con rebote
- «a Kalman» → `t2`: «a Kalman» entra debajo, con la etiqueta «Capítulo 12 · Estimación de señales»

---

# Escena 03 — EstadoDeUnSistema

**Capítulo YouTube:** Un modelo de cómo nace la señal
**Objetivo:** que quien mira entienda qué es un estado, antes de usarlo.

## Narración

<!-- b1 -->
Vamos con la sorpresa que anunciamos al empezar el capítulo. El filtro de Wiener parte de espectros. La otra forma de ver el mismo problema parte de un modelo de cómo nace la señal: un sistema en espacio de estados. Un estado es el conjunto de números que resumen lo que el sistema recuerda: en un cohete, la posición y la velocidad. En el sensor, solo un número.

- «la sorpresa» → `sorpresa`: aparece un signo «?» ámbar en el centro
- «El filtro de Wiener» → `wiener`: el «?» sube a un rincón y entra la caja «Wiener»
- «parte de espectros» → `espectros`: dentro de la caja se dibujan dos curvas de espectro
- «La otra forma de ver el mismo problema» → `otra`: a la derecha aparece una segunda caja vacía, con una flecha doble «mismo problema»
- «un modelo de cómo nace la señal» → `modelo`: la caja nueva se llena con «w → sistema → y»
- «espacio de estados» → `estados`: el rótulo «espacio de estados» entra en ámbar sobre la caja
- «el conjunto de números» → `conjunto`: del sistema salen varios números «q₁, q₂, …» agrupados en una llave
- «lo que el sistema recuerda» → `recuerda`: una nube con unos números «q» sale del sistema
- «un cohete» → `cohete`: entra el cohete pequeño
- «la posición y la velocidad» → `posvel`: junto al cohete, dos números «posición» y «velocidad», el estado de dos números
- «solo un número» → `uno`: el termómetro del sensor con un único «q»

---

# Escena 04 — ElSensorEnEstados

**Capítulo YouTube:** El sensor en espacio de estados
**Objetivo:** escribir el sensor de siempre como un sistema de estados con sus dos ruidos.

## Narración

<!-- b1 -->
El sensor es el estado q de ene más uno igual a cero coma seis por q de ene, más la moneda w, de varianza dos coma cinco seis. La temperatura, i griega, es ese estado. Y lo medido es i griega más el ruido, de varianza uno. Es exactamente el sensor de siempre: la varianza de la temperatura sigue siendo cuatro. Lo que cambia es la manera de describirlo.

- «El sensor es el estado» → `estado`: entra «q[n]» en azul dentro de una caja
- «q de ene más uno» → `qsig`: a la izquierda se escribe «q[n+1] =»
- «cero coma seis por q de ene» → `seis`: se completa con «0,6 q[n]»
- «la moneda w» → `moneda`: entra «+ w[n]» en magenta con una moneda encima
- «de varianza dos coma cinco seis» → `var256`: aparece «σ_w² = 2,56» bajo la moneda
- «La temperatura, i griega» → `temp`: debajo, «y[n] = q[n]» en azul
- «lo medido» → `medido`: aparece «x[n] = y[n] + v[n]» en cian
- «el ruido, de varianza uno» → `ruido`: «v[n]» se marca en magenta con «σ_v² = 1»
- «el sensor de siempre» → `siempre`: a un lado aparece el dibujo del sensor con su cable, el del capítulo 10
- «la varianza de la temperatura sigue siendo cuatro» → `cuatro`: sobre la traza azul aparece «σ_y² = 4»
- «Lo que cambia» → `cambia`: los dos modelos del sensor se separan, con el mismo «σ_y² = 4» en ambos
- «la manera de describirlo» → `describir`: dos rótulos, «espectros» y «estados», unidos por una flecha doble

---

# Escena 05 — LaMismaFactorizacion

**Capítulo YouTube:** La misma factorización, ahora con estados
**Objetivo:** ver que el numerador de este lenguaje es el mismo de la factorización del E5.

## Narración

<!-- b1 -->
En este lenguaje, el numerador de la densidad de lo medido es erre, el cociente entre la potencia de la moneda y la del ruido, dos coma cinco seis, más a de zeta por a de zeta a la menos uno, con a de zeta igual a zeta menos cero coma seis. Da tres coma nueve dos menos cero coma seis por zeta más zeta a la menos uno: ¡el numerador del episodio quinto! Y alfa de zeta vale zeta menos cero coma uno cinco siete.

- «En este lenguaje» → `lenguaje`: aparece «numerador de S_xx» como caja vacía
- «es erre» → `erre`: dentro, «r =»
- «el cociente entre la potencia de la moneda y la del ruido» → `cociente`: «r = σ_w² / σ_v²» con la moneda y el ruido señalados
- «dos coma cinco seis» → `v256`: «= 2,56»
- «a de zeta por a de zeta a la menos uno» → `aa`: se suma «+ a(z) a(z⁻¹)»
- «zeta menos cero coma seis» → `az`: aparece «a(z) = z − 0,6» y el producto se desarrolla como «1,36 − 0,6 (z + z⁻¹)»
- «tres coma nueve dos» → `resultado`: «2,56 + 1,36 = 3,92» y queda «3,92 − 0,6 (z + z⁻¹)»
- «menos cero coma seis por zeta» → `menoszeta`: se completa «3,92 − 0,6 (z + z⁻¹)», con la parte «− 0,6 (z + z⁻¹)» resaltada
- «el numerador del episodio quinto» → `igual`: al lado entra la fórmula de aquel episodio, «3,92 − 0,6 (z + 1/z)», y las dos se iluminan: son iguales
- «Y alfa de zeta» → `alfa`: aparece «α(z) = z − 0,157» en ámbar
- «zeta menos cero coma uno cinco siete» → `z157`: la raíz 0,157 se marca en el eje

---

# Escena 06 — ElObservador

**Capítulo YouTube:** El observador y su ganancia
**Objetivo:** el observador como una copia del modelo que predice y se corrige con la sorpresa; qué ganancia elegir.

## Narración

<!-- b1 -->
El observador es una copia del modelo dentro del ordenador. Predice con el modelo: cero coma seis por su estimación de ahora. Y se corrige con la sorpresa: lo que se mide menos lo que esperaba, multiplicado por una ganancia, ge. Si lo medido coincide con lo esperado, no hay corrección. Con ge igual a cero, ignora las medidas; con ge igual a uno, se fía solo del dato.

- «una copia del modelo» → `copia`: bajo la planta aparece una copia con «q̂»
- «dentro del ordenador» → `ord`: un ordenador pequeño encierra la copia
- «Predice con el modelo» → `predice`: «q̂[n+1] = 0,6 q̂[n]»
- «cero coma seis por su estimación de ahora» → `seis`: se resalta «0,6 q̂[n]»
- «se corrige con la sorpresa» → `sorpresa`: entra «x[n] − q̂[n]», resaltada
- «multiplicado por una ganancia» → `gan`: se suma «+ G (x[n] − q̂[n])», con G en ámbar
- «Si lo medido coincide con lo esperado» → `coincide`: dos valores iguales y la sorpresa pasa a «0» en verde
- «no hay corrección» → `nocorr`: el término «G (…)» se apaga a «0»
- «Con ge igual a cero» → `g0`: aparece un dial de G; con G = 0, el rótulo «ignora las medidas»
- «con ge igual a uno» → `g1`: el dial pasa a G = 1 y el rótulo «se fía del dato»

<!-- b2 -->
¿Qué ganancia elegir? La estimación evoluciona con un polo en cero coma seis menos ge. Si queremos que caiga justo en el cero coma uno cinco siete de la factorización, ge tiene que valer cero coma seis menos cero coma uno cinco siete. Haz la cuenta antes de seguir: cero coma cuatro cuatro tres. ¿Te suena ese número?

- «¿Qué ganancia elegir?» → `pregunta`: aparece «G = ?» grande
- «un polo en cero coma seis menos ge» → `polo`: la fórmula pasa a «q̂[n+1] = (0,6 − G) q̂[n] + G x[n]» y en el plano z aparece un polo en «0,6 − G»
- «Si queremos que caiga justo» → `caiga`: el polo se mueve a lo largo del eje, como buscando un sitio
- «el cero coma uno cinco siete de la factorización» → `objetivo`: en el eje se marca el 0,157 con una diana
- «ge tiene que valer» → `valer`: se escribe «G = 0,6 − 0,157»
- «cero coma seis menos cero coma uno cinco siete» → `resta`: se resaltan «0,6» y «0,157» dentro de la resta
- «Haz la cuenta antes de seguir» → `cuenta`: pausa visible: el resultado queda tapado con «?»
- «cero coma cuatro cuatro tres» → `r443`: el «?» se revela como «G = 0,443»
- «¿Te suena ese número?» → `suena`: el 0,443 late en ámbar y una lupa lo recorre

---

# Escena 07 — ElObservadorEsElFiltro

**Capítulo YouTube:** El observador es el filtro de Wiener
**Objetivo:** el observador con G = 0,443 es el predictor del E6; lo mismo vale en general.

## Narración

<!-- b1 -->
Con esa ganancia, la estimación del observador es cero coma uno cinco siete por su valor anterior, más cero coma cuatro cuatro tres por lo que llega. Su transferencia es cero coma cuatro cuatro tres, zeta a la menos uno, entre uno menos cero coma uno cinco siete zeta a la menos uno. ¡Son los números del predictor del episodio anterior! El observador y el filtro de Wiener son el mismo filtro.

- «Con esa ganancia» → `gan`: reaparece «G = 0,443»
- «cero coma uno cinco siete por su valor anterior» → `p157`: se escribe «q̂[n+1] = 0,157 q̂[n]»
- «cero coma cuatro cuatro tres por lo que llega» → `p443`: se suma «+ 0,443 x[n]»
- «Su transferencia» → `transf`: una flecha lleva la recursión a «H(z) = …»
- «cero coma cuatro cuatro tres, zeta a la menos uno» → `num`: aparece el numerador «0,443 z⁻¹»
- «entre uno menos cero coma uno cinco siete» → `den`: se completa con «/ (1 − 0,157 z⁻¹)»
- «a la menos uno» → `retardo`: el «z⁻¹» se resalta como un retardo de una muestra
- «los números del predictor» → `predictor`: al lado entra la fórmula del predictor del E6, «0,443 z⁻¹ / (1 − 0,157 z⁻¹)», y se superponen
- «El observador y el filtro de Wiener» → `obswie`: las etiquetas «observador» y «Wiener causal» se acercan
- «el mismo filtro» → `mismo`: un «=» une «observador» y «Wiener causal»; el 0,443 y el 0,157 se iluminan

<!-- b2 -->
No es una casualidad del sensor. En general, con una ganancia elegida para que el polinomio del observador sea alfa de zeta, la transferencia es alfa menos a, entre alfa. Con nuestros números, zeta menos cero coma uno cinco siete menos zeta más cero coma seis: cero coma cuatro cuatro tres. El filtro de Wiener causal se implementa como un observador. Eso sí: es el predictor, el que no usa la muestra de ahora.

- «No es una casualidad» → `casual`: «¿casualidad?» aparece y queda tachado
- «En general» → `general`: un sistema genérico «A, b, c» reemplaza al sensor
- «el polinomio del observador sea alfa de zeta» → `polialfa`: «polinomio del observador = α(z)»
- «la transferencia es alfa menos a, entre alfa» → `hobs`: «H = (α(z) − a(z)) / α(z)»
- «Con nuestros números» → `nuestros`: se sustituye por «((z − 0,157) − (z − 0,6)) / (z − 0,157)»
- «menos zeta más cero coma seis» → `restaz`: el «z» del numerador se cancela con el «− z» y quedan los números
- «cero coma cuatro cuatro tres» → `r443`: queda «= 0,443 / (z − 0,157)»
- «El filtro de Wiener causal» → `wcausal`: aparece la caja «Wiener causal»
- «se implementa como un observador» → `impl`: una flecha va de «Wiener causal» a «observador»
- «es el predictor» → `esp`: etiqueta ámbar «predictor» sobre la fórmula
- «no usa la muestra de ahora» → `nousa`: la x[n] de la recursión queda tachada y se resalta el retardo «z⁻¹»

---

# Escena 08 — ElPasoDeCorreccion

**Capítulo YouTube:** El paso de corrección
**Objetivo:** el filtro (que sí usa la muestra de ahora) es el predictor más un paso de corrección; la ganancia K = 0,7386.

## Narración

<!-- b1 -->
Para el filtro, el que sí la usa, añadimos un paso. Primero se predice; después, se corrige con lo que llega, con una ganancia, k. Esa ganancia vale cero coma siete tres ocho seis, el primer coeficiente del filtro causal del sensor. Comprobación: cero coma seis por uno menos k da justo el polo cero coma uno cinco siete.

- «el que sí la usa» → `usa`: la x[n] vuelve a aparecer en la recursión, sin tachar
- «añadimos un paso» → `paso`: entra una caja «paso de corrección» detrás del predictor
- «Primero se predice» → `predice`: «q̂[n|n−1]» en la primera caja
- «se corrige con lo que llega» → `corrige`: se escribe «q̂[n|n] = q̂[n|n−1] + K (x[n] − q̂[n|n−1])»
- «una ganancia, k» → `k`: la K se resalta en ámbar
- «cero coma siete tres ocho seis» → `k7386`: aparece «K = 0,7386»
- «el primer coeficiente del filtro» → `h0`: al lado, los tallos del filtro causal del E5, con el primero, 0,7386, resaltado
- «Comprobación» → `comprob`: aparece un sello de comprobación
- «cero coma seis por uno menos k» → `c1`: se escribe «0,6 (1 − K) = 0,6 · 0,2614»
- «el polo cero coma uno cinco siete» → `c2`: queda «= 0,157» con un tilde verde

<!-- b2 -->
Y tiene una lectura sencilla. El error de la predicción es dos coma ocho dos seis y el ruido, uno. De la sorpresa que trae cada medición, la parte que viene de la señal es dos coma ocho dos seis entre tres coma ocho dos seis: cero coma siete tres ocho seis. Justo la ganancia. Corregimos con más fuerza cuando el ruido molesta menos.

- «lectura sencilla» → `lectura`: una lupa recorre la ganancia K
- «El error de la predicción es dos coma ocho dos seis» → `errpred`: barra roja «2,826»
- «el ruido, uno» → `ruido1`: a su lado, barra magenta «1»
- «la sorpresa que trae cada medición» → `sorp`: las dos barras se juntan en una sola, «3,826», rotulada «sorpresa»
- «la parte que viene de la señal» → `parte`: la parte roja se resalta
- «dos coma ocho dos seis entre» → `entre`: se escribe «K = 2,826 / (2,826 + 1)»
- «cero coma siete tres ocho seis» → `r`: queda «= 0,7386»
- «Justo la ganancia» → `justo`: un «=» lo une con la K de antes, con tilde verde
- «cuando el ruido molesta menos» → `menos`: la barra magenta se encoge y K sube hacia 1

---

# Escena 09 — ElFiltroDeKalman

**Capítulo YouTube:** El filtro de Kalman
**Objetivo:** ponerle nombre; Wiener contra Kalman: mismo resultado, distinto camino.

## Narración

<!-- b1 -->
Este filtro se llama de Kalman. Desde Wiener se llega por la factorización; Kalman parte del modelo de estados y le sale la forma de observador. Kalman va más lejos: admite sistemas que cambian con el tiempo, inestables, con varias entradas y salidas, y en vez de factorizar resuelve la ecuación de Riccati. Es el filtro que sigue a un cohete. Y es lo que acabamos de hacer con un sensor.

- «de Kalman» → `kalman`: el nombre «Kalman» entra en ámbar
- «Desde Wiener se llega por la factorización» → `wiener`: columna izquierda: «Wiener: densidad → factorización → α(z)»
- «Kalman parte del modelo de estados» → `kcol`: columna derecha: «Kalman: modelo de estados → observador»
- «la forma de observador» → `obs`: las dos columnas desembocan en el mismo «0,443 z⁻¹ / (1 − 0,157 z⁻¹)»
- «Kalman va más lejos» → `lejos`: aparece la tabla de filas bajo las dos columnas
- «cambian con el tiempo» → `variante`: fila «variante en el tiempo»: ✗ en Wiener, ✓ en Kalman
- «inestables» → `inest`: fila «inestable»: ✗ y ✓
- «varias entradas y salidas» → `mimo`: fila «varias entradas y salidas»: ✗ y ✓
- «la ecuación de Riccati» → `riccati`: fila «cómo se resuelve»: «factorización» contra «Riccati»
- «sigue a un cohete» → `cohete`: el cohete con su estimación de posición y velocidad
- «lo que acabamos de hacer con un sensor» → `sensor`: el termómetro del sensor sobre el cohete, con «K = 0,7386»

---

# Escena 10 — CorrelacionesEstimadas

**Capítulo YouTube:** Y si no conocemos las correlaciones
**Objetivo:** en la práctica solo hay un registro; las correlaciones se estiman y el filtro hereda sus errores.

## Narración

<!-- b1 -->
Todo lo que hemos hecho supone que conocemos las correlaciones. En la práctica solo tenemos un registro. Hay que estimarlas, con los mismos problemas del capítulo once: sesgo y varianza, sobre todo en los desfases grandes. El filtro que sale hereda esos errores. Regla práctica: un registro mucho más largo que la ventana, al menos diez veces.

- «conocemos las correlaciones» → `conocemos`: corte seco; aparece «C_xx[m]» con la etiqueta «conocida»
- «solo tenemos un registro» → `registro`: queda una única traza cian con el rótulo «solo datos» y «C_xx[m] = ?»
- «Hay que estimarlas» → `estimar`: se dibuja la curva estimada, ruidosa
- «sesgo y varianza» → `sesgo`: la curva verdadera punteada y la estimada, con los rótulos «sesgo» y «varianza»
- «sobre todo en los desfases grandes» → `desfases`: la zona de m grande se resalta y se ve más temblorosa
- «El filtro que sale» → `filtro`: aparece el filtro h calculado con esa curva, como una caja con tallos
- «hereda esos errores» → `hereda`: una flecha lleva la curva ruidosa a un filtro h que sale torcido
- «un registro mucho más largo que la ventana» → `largo`: un registro largo con una ventana corta encima, «N ≫ L»
- «al menos diez veces» → `diez`: se completa «N ≥ 10 L»

---

# Escena 11 — ResolverLasEcuaciones

**Capítulo YouTube:** Resolver las ecuaciones: Levinson-Durbin
**Objetivo:** costo de invertir (L³), mal condicionamiento, y Toeplitz con Levinson-Durbin (L²).

## Narración

<!-- b1 -->
Luego hay que resolver las ecuaciones. Invertir una matriz de ele por ele cuesta ele al cubo operaciones: con mil coeficientes, mil millones. Y si el proceso está cerca de ser determinista, la matriz está mal condicionada y se pierde precisión. Pero es de Toeplitz, y para eso existe el algoritmo de Levinson-Durbin: ele al cuadrado, un millón, y de paso da la solución de todos los órdenes, como la tabla del segundo episodio.

- «resolver las ecuaciones» → `resolver`: aparece «R h = r» en ámbar
- «una matriz de ele por ele» → `matriz`: se dibuja la matriz R de L × L
- «ele al cubo» → `cubo`: un contador «L³» crece
- «mil millones» → `mil`: «L = 1.000 → 1.000.000.000»
- «cerca de ser determinista» → `determ`: una traza casi predecible, casi una senoide, con «determinista»
- «mal condicionada» → `mal`: dos filas de la matriz casi iguales se resaltan
- «se pierde precisión» → `precision`: la cifra «0,7386» se vuelve «0,7??»
- «es de Toeplitz» → `toeplitz`: las diagonales de la matriz se pintan, una de cada color
- «Levinson-Durbin» → `levinson`: el nombre entra en ámbar
- «ele al cuadrado» → `cuad`: el contador pasa a «L²»
- «un millón» → `millon`: «1.000.000», mucho menor que el de antes
- «la solución de todos los órdenes» → `ordenes`: una escalera de órdenes 1, 2, 3…
- «la tabla del segundo episodio» → `tabla`: aparece la tabla de errores del E2: 0,8 · 0,7401 · 0,7387 · 0,7386

---

# Escena 12 — BajarPorLaParabola

**Capítulo YouTube:** El filtro adaptativo: LMS
**Objetivo:** bajar por la parábola del error con la pendiente de una sola muestra, y una iteración a mano.

## Narración

<!-- b1 -->
Y hay otra vía que no necesita estimar correlaciones. Recuerda la parábola del error del primer episodio, cuatro menos ocho hache más cinco hache al cuadrado. El filtro adaptativo baja rodando por ella: en cada muestra, mueve hache un poco en contra de la pendiente. La pendiente verdadera es menos dos veces la media del error por el dato. El truco: usar la de esta sola muestra, sin la media. Es el algoritmo LMS.

- «otra vía» → `via`: una segunda flecha se desvía del camino anterior
- «no necesita estimar correlaciones» → `noncorr`: «C_xx = ?» aparece y queda tachado
- «la parábola del error» → `parab`: se dibuja la parábola J(h) del E1, con su vértice en h = 0,8
- «cuatro menos ocho hache más cinco hache al cuadrado» → `jh`: aparece «J(h) = 4 − 8h + 5h²»
- «El filtro adaptativo» → `adapt`: entra la caja «filtro adaptativo» junto a la parábola
- «baja rodando por ella» → `baja`: un punto se desliza por la parábola
- «en cada muestra» → `muestra`: marcas de muestra x[n] pasan por debajo
- «mueve hache un poco en contra de la pendiente» → `contra`: tangente en el punto y una flecha en sentido contrario
- «La pendiente verdadera» → `verdadera`: aparece «pendiente = −2 E[e x]»
- «la media del error por el dato» → `media`: se resalta la «E[ ]»
- «usar la de esta sola muestra» → `sola`: aparece «−2 e[n] x[n]»
- «sin la media» → `sinmedia`: la «E[ ]» queda tachada
- «el algoritmo LMS» → `lms`: entra «h ← h + μ e x» con LMS en ámbar

<!-- b2 -->
Con un paso de cero coma uno, empezando en cero. Llega equis igual a dos, y la temperatura era uno coma cinco: el error es uno coma cinco y hache pasa a cero coma tres. Llega menos uno, la temperatura era menos cero coma ocho: el error es menos cero coma cinco y hache sube a cero coma tres cinco. Se acerca al cero coma ocho que sabemos que es el óptimo.

- «un paso de cero coma uno» → `mu`: aparece «μ = 0,1»
- «empezando en cero» → `cero`: el punto se coloca en h = 0 sobre la parábola
- «Llega equis igual a dos» → `x2`: «x = 2» entra desde la derecha
- «la temperatura era uno coma cinco» → `y15`: «y = 1,5» en azul
- «el error es uno coma cinco» → `e15`: «e = 1,5 − 0 · 2 = 1,5» en rojo
- «hache pasa a cero coma tres» → `h03`: «h = 0 + 0,1 · 1,5 · 2 = 0,3» y el punto baja hasta h = 0,3
- «Llega menos uno» → `xm1`: «x = −1»
- «la temperatura era menos cero coma ocho» → `ym08`: «y = −0,8»
- «el error es menos cero coma cinco» → `em05`: «e = −0,8 − 0,3 · (−1) = −0,5»
- «hache sube a cero coma tres cinco» → `h035`: «h = 0,35» y el punto baja un poco más
- «al cero coma ocho que sabemos» → `optimo`: se marca el vértice de la parábola en 0,8

---

# Escena 13 — ElCompromisoDelPaso

**Capítulo YouTube:** Velocidad contra precisión
**Objetivo:** el paso marca el compromiso velocidad-precisión; para qué sirve; Wiener es el norte.

## Narración

<!-- b1 -->
El paso marca el compromiso de siempre entre velocidad y precisión: grande, converge deprisa pero tiembla lejos del óptimo; chico, converge despacio pero fino. Con esto se cancelan los ecos de una llamada o el ruido en unos auriculares. El filtro de Wiener es el norte; el LMS es cómo llegar hasta él sin mapa.

- «El paso marca el compromiso» → `compromiso`: un balancín con «velocidad» a un lado y «precisión» al otro
- «grande, converge deprisa» → `grande`: sobre la parábola, una trayectoria con pasos grandes que baja rápido
- «tiembla lejos del óptimo» → `tiembla`: la trayectoria queda zigzagueando alrededor del vértice
- «chico, converge despacio» → `chico`: otra trayectoria con pasos pequeños que baja lento
- «pero fino» → `fino`: esa trayectoria se posa exacta en el vértice
- «los ecos de una llamada» → `eco`: un teléfono con ondas de eco que se apagan
- «el ruido en unos auriculares» → `auri`: unos auriculares con el ruido que se atenúa
- «El filtro de Wiener es el norte» → `norte`: una brújula apunta al vértice, rotulado «Wiener»
- «el LMS es cómo llegar» → `llegar`: el punto del LMS empieza a bajar hacia la brújula
- «sin mapa» → `mapa`: el punto baja a ciegas y aparece un mapa tachado

---

# Escena 14 — LaMismaProyeccion

**Capítulo YouTube:** Todo era una proyección
**Objetivo:** el cierre del capítulo: la proyección por tercera vez, con un plano que ha crecido; resumen con el sensor.

## Narración

<!-- b1 -->
Miremos el capítulo desde arriba. En el capítulo siete, las variables eran flechas y la correlación, el coseno de un ángulo. En el capítulo ocho, estimar era proyectar una flecha sobre el plano de las mediciones, con el error en ángulo recto. Aquí, lo mismo, con un plano que ha crecido: el de las muestras de la ventana, finito en el FIR, hacia el pasado en el causal, hacia los dos lados en el no causal.

- «desde arriba» → `arriba`: corte seco; la cámara se aleja y quedan tres cuadros pequeños en fila: capítulo 7, capítulo 8, capítulo 12
- «las variables eran flechas» → `flechas`: el cuadro del capítulo 7 se amplía: dos flechas, y y x
- «el coseno de un ángulo» → `coseno`: un arco entre ellas y «ρ = cos θ»
- «En el capítulo ocho» → `ocho`: el cuadro del capítulo 8 se destaca y el del 7 se atenúa
- «proyectar una flecha» → `proyectar`: el cuadro del capítulo 8: la sombra de y sobre el plano
- «el plano de las mediciones» → `plano`: aparece el plano de X₁ y X₂
- «el error en ángulo recto» → `recto`: el error en rojo, a 90° con el plano
- «un plano que ha crecido» → `crecido`: el cuadro del capítulo 12: el plano se agranda
- «las muestras de la ventana» → `ventana`: una ventana de L muestras se desliza sobre x[n]
- «finito en el FIR» → `fir`: el plano finito, «x[n], …, x[n − L + 1]»
- «hacia el pasado en el causal» → `causal`: el plano pasa a semiinfinito, «x[n − k], k ≥ 0»
- «hacia los dos lados en el no causal» → `nocausal`: el plano se abre a los dos lados

<!-- b2 -->
Recuerda el sensor: sin datos, cuatro. Con una muestra, cero coma ocho. Con el filtro causal, cero coma siete tres ocho seis. Con todo el registro, cero coma seis ocho seis. Y aquel colador que buscábamos en el capítulo once, para separar la voz del murmullo, es esta curva: la ganancia que reparte, en cada frecuencia, cuánto fiarse de lo medido.

- «Recuerda el sensor» → `sensor`: corte seco; el termómetro con su cable
- «sin datos, cuatro» → `s4`: barra roja «sin datos: 4»
- «Con una muestra, cero coma ocho» → `s08`: barra «una muestra: 0,8»
- «Con el filtro causal, cero coma siete tres ocho seis» → `s7386`: barra «causal: 0,7386»
- «Con todo el registro» → `registro`: aparece la etiqueta «todo el registro» para la siguiente barra
- «cero coma seis ocho seis» → `s686`: barra «no causal: 0,686»
- «Y aquel colador» → `colador`: entra el colador del capítulo 11
- «separar la voz del murmullo» → `voz`: la voz azul y el murmullo magenta a ambos lados del colador
- «es esta curva» → `curva`: se dibuja H(Ω) con sus valores 0,94 · 0,65 · 0,5
- «en cada frecuencia» → `cadafrec`: un marcador recorre el eje Ω
- «cuánto fiarse de lo medido» → `fiarse`: la curva se resalta donde se acerca a 1, con la etiqueta «me fío»

---

# Escena 15 — TiempoContinuo

**Capítulo YouTube:** Lo mismo en tiempo continuo
**Objetivo:** las tres fórmulas en tiempo continuo, apareadas con las discretas.

## Narración

<!-- b1 -->
Todo el capítulo se ha hecho en tiempo discreto, pero en tiempo continuo pasa lo mismo, con demostraciones análogas. No causal: hache es la densidad cruzada dividida entre la densidad de lo medido. Causal: uno entre F, por la parte causal de la cruzada entre F de menos jota omega. Y predecir con antelación te segundos: uno entre F, por la parte causal de e elevado a ese te por F. La diferencia: el ruido blanco continuo tiene potencia infinita; es una idealización.

- «tiempo discreto» → `discreto`: tallos que se dibujan uno a uno
- «tiempo continuo» → `continuo`: los tallos se unen en una curva continua
- «con demostraciones análogas» → `analogas`: junto a cada fórmula discreta aparece su par continuo, con un «≈»
- «No causal» → `nc`: aparece «H(jω) = S_yx / S_xx»
- «hache es» → `hache`: se escribe «H(jω) =»
- «la densidad cruzada» → `cruzada`: se completa con «S_yx(jω)» en ámbar
- «entre la densidad de lo medido» → `entre`: se completa con «/ S_xx(jω)»
- «Causal» → `c`: debajo, «H = (1/F) [S_yx / F(−jω)]₊»
- «uno entre F» → `unof`: se resalta el factor «1/F»
- «la parte causal» → `parte`: se resalta el corchete con el «₊»
- «la cruzada entre F de menos jota omega» → `cruzadaf`: se resalta «S_yx / F(−jω)»
- «predecir con antelación te segundos» → `pred`: debajo, «H(s) = (1/F) [e^{sT} F]₊»
- «por la parte causal de» → `parte2`: se resalta el corchete «[ ]₊» de la tercera fórmula
- «e elevado a ese te» → `exp`: se resalta «e^{sT}», el adelanto de T segundos
- «La diferencia» → `diferencia`: las tres fórmulas se apartan a un lado
- «el ruido blanco continuo tiene potencia infinita» → `infinita`: un espectro plano que se extiende al infinito
- «una idealización» → `ideal`: el rótulo «idealización» sobre ese espectro

---

# Escena 16 — LaPiezaSuelta

**Capítulo YouTube:** La pieza que queda suelta
**Objetivo:** la factorización y el blanqueador quedan como estrategia para el capítulo de detección.

## Narración

<!-- b1 -->
Y una pieza se ha quedado suelta a propósito: la factorización, con su filtro de fase mínima y su blanqueador. Volverá. Cuando lo que hay que hacer es detectar una señal conocida en un ruido con memoria, la estrategia empieza igual: blanquear con uno entre F y aplicar después lo que ya sabemos sobre ruido blanco.

- «una pieza se ha quedado suelta» → `suelta`: una pieza de rompecabezas con una «F» flota sola
- «la factorización» → `fact`: aparece «S_xx = F F*»
- «fase mínima» → `fasemin`: un plano z con los ceros dentro del círculo unidad
- «su blanqueador» → `blanq`: aparece «1/F» en ámbar
- «Volverá» → `volvera`: una flecha lleva la pieza a un rótulo «capítulo 13»
- «detectar una señal conocida» → `detectar`: un pulso conocido entra
- «un ruido con memoria» → `memoria`: el pulso queda sobre una traza de ruido con memoria
- «blanquear con uno entre F» → `blanquear`: la cadena «x → 1/F → ruido blanco»
- «lo que ya sabemos sobre ruido blanco» → `blanco`: al final de la cadena entra un filtro adaptado

---

# Escena 17 — Cierre

**Capítulo YouTube:** Lo que viene: más datos no bastan

## Narración

<!-- b1 -->
Y con esto se cierra el capítulo: Wiener y Kalman eran el mismo filtro, todo era una proyección, y el LMS llega al mismo sitio sin conocer las correlaciones.

- «Wiener y Kalman» → `wk`: dos cajas, «Wiener» y «Kalman»
- «el mismo filtro» → `mismo`: un «=» las une y se funden en una sola
- «todo era una proyección» → `proy`: las flechas de la proyección con el error a 90°
- «el LMS llega al mismo sitio» → `lms`: un punto baja por la parábola hasta el vértice
- «sin conocer las correlaciones» → `sin`: «C_xx = ?» tachado

<!-- b2 -->
Hasta aquí hemos estimado: adivinar lo mejor posible un valor que no vemos limpio. Pero a veces la pregunta no es cuánto, sino sí o no. ¿Hay un avión en el radar o solo ruido? Ya no se trata de acertar un valor, sino de decidir, sabiendo que te puedes equivocar de dos maneras distintas. Eso es detectar, y el próximo capítulo empieza con una idea que suena a broma: más datos no bastan.

- «adivinar lo mejor posible» → `adivinar`: una flecha ámbar apunta a un valor
- «un valor que no vemos limpio» → `limpio`: el valor aparece bajo una traza de ruido
- «no es cuánto, sino sí o no» → `sino`: «¿cuánto?» queda tachado y entra «¿sí o no?»
- «un avión en el radar» → `radar`: un radar con un punto
- «solo ruido» → `solo`: el mismo radar, con manchas de ruido
- «acertar un valor» → `acertar`: el valor queda tachado
- «decidir» → `decidir`: aparece «sí / no»
- «dos maneras distintas» → `dos`: dos cruces rojas sobre el «sí / no»
- «Eso es detectar» → `detect`: el título «Detección de señales» entra pequeño
- «una idea que suena a broma» → `broma`: un signo de risa, «¿en serio?», sobre el título anterior
- «más datos no bastan» → `titulo13`: entra el título del capítulo siguiente, «Más datos no bastan»
