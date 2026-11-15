# Episodio 5 — ¿Basta con una sola grabación?

Capítulo 10 (Procesos aleatorios), episodio 5 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 17 a 20), más un gancho y un cierre nuevos.

**Estado:** 23 escenas animadas (`s01`–`s23`) y borrador 480p15 renderizado (9:30, 0 avisos de controles, hojas de contacto revisadas). Se trabajó sin esperar la aprobación del texto ⭐ (autorizado por el usuario): falta que lo revise y que vea el borrador (paso 15). Después, render final `--calidad qh`.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Mil medidas seguidas del sensor valen solo como doscientas cincuenta. Y mil medidas de una pila valen como una sola. ¿Por qué?»
- ⭐ Escena 23 (cierre): resume la memoria que se borra y la que dura, y anuncia E6 por su título, «Adivinar el futuro, limpiar el presente».
- Retoque en la escena 08 (b1 de la escena 18 del guion base): «En el capítulo anterior vimos la varianza de una suma» pasa a «En el capítulo siete vimos…», porque entre el 7 y el 10 hay otros dos capítulos.

Reparto de las escenas del guion base: 17 → escenas 03 a 07; 18 → 08 a 12; 19 → 13 a 17; 20 → 18 a 22.
Solo se partieron bloques enteros en escenas atómicas (un bloque por escena): el texto del guion base no cambia, salvo el retoque de arriba.

---

# Escena 01 — Gancho

**Capítulo YouTube:** Mil medidas que valen una

## Narración

<!-- b1 -->
Mil medidas seguidas del sensor valen solo como doscientas cincuenta. Y mil medidas de una pila valen como una sola. ¿Por qué?

- «Mil medidas seguidas» → `mil`: una fila de mil puntos se dibuja de golpe
- «del sensor» → `sensor`: la fila se rotula «sensor» en azul
- «doscientas cincuenta» → `n250`: los puntos se agrupan de cuatro en cuatro y aparece «250»
- «mil medidas de una pila» → `pila`: una pila con una fila de mil puntos idénticos, todos a la misma altura
- «como una sola» → `una`: toda la fila se funde en un único punto, «1»
- «¿Por qué?» → `porque`: aparece un «¿?» grande

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** ¿Basta con una sola grabación?

## Narración

<!-- b1 -->
¿Basta con una sola grabación?

- «¿Basta con» → `t1`: las palabras «¿Basta con» entran con rebote
- «una sola grabación?» → `t2`: «una sola grabación?» entra debajo, con la etiqueta «Capítulo 10 · Procesos aleatorios»

---

# Escena 03 — CajonDePilas

**Capítulo YouTube:** El cajón de pilas

## Narración

<!-- b1 -->
Un cajón lleno de pilas, cada una con un voltaje un poco distinto. El experimento: sacas una al azar y mides su voltaje durante una hora. La grabación es una línea recta, porque el voltaje de esa pila no cambia. Cada realización es una constante, y cada pila da una constante diferente. Supón que los voltajes, medidos respecto del nominal, tienen media cero y varianza cuatro.

- «Un cajón lleno de pilas» → `cajon`: un cajón con pilas, cada una con su voltaje escrito: «+1», «−2», «+2», «0»
- «un poco distinto» → `distinto`: las etiquetas de voltaje se resaltan: ninguna pila es igual a otra
- «El experimento» → `exp`: aparece el rótulo «experimento»
- «sacas una al azar» → `saca`: una pila sale del cajón y se conecta a un voltímetro
- «durante una hora» → `hora`: un reloj corre y el voltímetro empieza a dibujar
- «una línea recta» → `recta`: el voltímetro dibuja una recta horizontal
- «no cambia» → `nocambia`: el voltaje se rotula «constante» sobre la recta
- «Cada realización es una constante» → `cte`: la recta se rotula «realización»
- «cada pila da una constante diferente» → `varias`: aparecen otras rectas a alturas distintas, una por pila
- «medidos respecto del nominal» → `nominal`: una línea punteada «nominal» a la altura cero
- «media cero» → `media`: se rotula «μ = 0» a la altura central
- «varianza cuatro» → `var`: se rotula «σ² = 4» con una llave que abarca la dispersión de las rectas

---

# Escena 04 — EstacionarioSi

**Capítulo YouTube:** ¿Es estacionario? ¿Es ergódico?

## Narración

<!-- b1 -->
Antes de seguir, dos preguntas: ¿este proceso es estacionario? ¿Y es ergódico? Piénsalo un momento. Estacionario lo es, y en el sentido más fuerte: la estadística no cambia nunca, porque nada cambia nunca. Da igual cuándo hagas el corte: la densidad de los voltajes es siempre la misma.

- «dos preguntas» → `preguntas`: dos casillas vacías: «¿estacionario?» y «¿ergódico?»
- «¿este proceso es estacionario?» → `q1`: la primera casilla se resalta
- «¿Y es ergódico?» → `q2`: la segunda casilla se resalta
- «Piénsalo un momento» → `pausa`: un reloj de arena marca la pausa, las casillas siguen vacías
- «Estacionario lo es» → `si`: la casilla «¿estacionario?» se marca «sí» con tilde verde
- «en el sentido más fuerte» → `fuerte`: aparece «estricto» junto al «sí»
- «la estadística no cambia nunca» → `nocambia`: un cursor recorre el tiempo sobre las rectas, que permanecen quietas
- «porque nada cambia nunca» → `nada`: las rectas se resaltan: nada se mueve
- «cuándo hagas el corte» → `corte`: un corte vertical en un instante, que luego salta a otro
- «la densidad de los voltajes» → `densidad`: en cada corte aparece la misma campana
- «siempre la misma» → `misma`: «μ = 0, σ² = 4» sobre ambas campanas

---

# Escena 05 — PromedioQueNoCambia

**Capítulo YouTube:** La pila no es ergódica

## Narración

<!-- b1 -->
Ahora promedia tu grabación a lo largo del tiempo. Da el voltaje de tu pila, sea el que sea. Si te tocó una de dos voltios por encima, el promedio temporal es dos, por mucho que alargues la medida. Nunca se acerca a cero, la media del cajón. No es ergódico: una sola pila no te enseña nada de las demás.

- «promedia tu grabación» → `promedia`: un contador de promedio temporal arranca sobre la pila «+2»
- «a lo largo del tiempo» → `tiempo`: una flecha horizontal recorre la recta
- «el voltaje de tu pila» → `suvoltaje`: el contador marca «2» y se queda clavado
- «de dos voltios» → `dos`: aparece «+2» resaltado en ámbar
- «el promedio temporal es dos» → `prom2`: «promedio temporal = 2»
- «alargues la medida» → `alarga`: la ventana se ensancha y el contador no se mueve
- «se acerca a cero» → `cero`: una flecha hacia la altura cero que no llega nunca
- «la media del cajón» → `mediacajon`: «μ = 0» en otra altura, rotulada «media del cajón»
- «No es ergódico» → `no`: la casilla «¿ergódico?» se marca «no» con cruz roja
- «una sola pila» → `una`: la pila «+2» queda resaltada
- «de las demás» → `demas`: las otras rectas se atenúan: la pila «+2» no dice nada de ellas

---

# Escena 06 — AutocovarianzaCuatro

**Capítulo YouTube:** Autocovarianza: cuatro para siempre

## Narración

<!-- b1 -->
La autocovarianza lo explica. La muestra de ahora y la de dentro de una hora son el mismo número, así que su covarianza es la varianza: cuatro. Y eso vale para cualquier separación: cuatro a un segundo, cuatro a un año. Los osciladores tampoco olvidaban, pero al menos cada uno recorría todos sus valores en cada período. Cada pila se queda quieta en el suyo.

- «La autocovarianza» → `autocov`: aparece «C(τ)» con sus ejes
- «La muestra de ahora» → `ahora`: una marca sobre la recta de la pila, en un instante
- «de dentro de una hora» → `hora`: una segunda marca, una hora después: mismo valor
- «son el mismo número» → `mismo`: «=» entre las dos marcas
- «es la varianza» → `esvar`: aparece «C(τ) = σ²»
- «cuatro» → `cuatro`: «= 4» en ámbar
- «cualquier separación» → `sep`: una recta horizontal a altura 4 en toda la gráfica, donde antes caía la exponencial
- «cuatro a un segundo» → `seg`: un punto en «1 s» sobre la recta, en 4
- «cuatro a un año» → `ano`: un punto en «1 año», también en 4
- «Los osciladores tampoco olvidaban» → `osc`: el oscilador aparece con su coseno
- «recorría todos sus valores» → `recorre`: el coseno recorre todos sus valores, con un punto que sube y baja
- «Cada pila se queda quieta» → `quieta`: la recta de la pila se dibuja encerrada en su franja

---

# Escena 07 — DosPropiedades

**Capítulo YouTube:** Estacionario no es ergódico

## Narración

<!-- b1 -->
Así que estacionario y ergódico son cosas distintas. Estacionario dice que la estadística no cambia con el tiempo. Ergódico dice que una sola realización recorre todo lo que el ensemble puede hacer. La pila es estacionaria, pero cada realización se queda encerrada en su valor. ¿Qué tiene que pasar para que el promedio temporal sí funcione?

- «estacionario y ergódico» → `dos`: dos palabras clave, «estacionario» y «ergódico», separadas por «≠»
- «cosas distintas» → `distintas`: el «≠» se resalta
- «Estacionario dice» → `estacp`: la palabra «estacionario» se resalta
- «no cambia con el tiempo» → `estac`: bajo «estacionario» un reloj cuyo corte vertical da siempre la misma campana
- «Ergódico dice» → `ergop`: la palabra «ergódico» se resalta
- «una sola realización» → `una`: bajo «ergódico» una sola curva
- «recorre todo lo que el ensemble puede hacer» → `ergo`: la curva visita todas las alturas del ensemble
- «La pila es estacionaria» → `pila`: aparece la pila con su recta y una tilde en «estacionario»
- «encerrada en su valor» → `encerrada`: el ensemble de la pila como franjas, cada realización dentro de la suya
- «¿Qué tiene que pasar» → `pregunta`: un «¿?» parpadea sobre la pila
- «el promedio temporal sí funcione» → `funcione`: el promedio temporal se dibuja como una línea que sube hacia la media

---

# Escena 08 — PromedioDeDos

**Capítulo YouTube:** La varianza del promedio de dos muestras

## Narración

<!-- b1 -->
Para responder, midamos cuánto se dispersa el promedio temporal, empezando por lo más pequeño: el promedio de dos muestras seguidas. En el capítulo siete vimos la varianza de una suma: la varianza de la primera, más la de la segunda, más dos veces su covarianza. Y al dividir entre dos, la varianza se divide entre cuatro.

- «Para responder» → `resp`: la pregunta «¿qué decide?» se aparta a una esquina
- «cuánto se dispersa» → `dispersa`: una campana ancha sobre el promedio, con una llave de dispersión
- «empezando por lo más pequeño» → `pequeno`: la campana se encoge a una mini campana
- «el promedio de dos muestras» → `dos`: dos muestras seguidas resaltadas sobre una grabación, con «(x₁ + x₂)/2»
- «En el capítulo siete» → `cap7`: un sello «capítulo 7»
- «la varianza de una suma» → `suma`: entra «Var(x₁ + x₂) =»
- «la varianza de la primera» → `v1`: entra «σ²» en ámbar
- «más la de la segunda» → `v2`: entra «+ σ²» en ámbar
- «dos veces su covarianza» → `cov`: entra «+ 2C[1]» en cian
- «al dividir entre dos» → `entre2`: aparece «/ 2» sobre el promedio
- «entre cuatro» → `entre4`: el denominador de la fórmula pasa a «4», con la nota «(÷2)² = ÷4»

---

# Escena 09 — CuentaDeDos

**Capítulo YouTube:** Sensor, independientes y pila

## Narración

<!-- b1 -->
Con el sensor: cuatro más cuatro más dos por dos coma cuatro da doce coma ocho; entre cuatro, tres coma dos. Si las muestras fueran independientes, la covarianza sería cero y quedaría dos. Y con la pila, la covarianza es cuatro: cuatro más cuatro más ocho, dieciséis; entre cuatro, cuatro. Promediar dos muestras de una pila no sirve de nada.

- «Con el sensor» → `sensor`: columna «sensor» con la fórmula y «C[1] = 2,4»
- «cuatro más cuatro más dos por dos coma cuatro» → `formula`: «(4 + 4 + 2 · 2,4)/4» se construye por piezas
- «doce coma ocho» → `v128`: «12,8» debajo
- «tres coma dos» → `v32`: resultado «3,2» en ámbar
- «independientes» → `indep`: segunda columna, «independientes», con «C[1] = 0»
- «quedaría dos» → `v2`: «(4 + 4 + 0)/4 = 2»
- «con la pila» → `pila`: tercera columna, «pila»
- «la covarianza es cuatro» → `c4`: «C[1] = 4»
- «dieciséis» → `v16`: «(4 + 4 + 8)/4» con «16» debajo
- «entre cuatro, cuatro» → `v4`: resultado «4» en rojo
- «no sirve de nada» → `nada`: «4 = 4» con una cruz roja: promediar no reduce nada

---

# Escena 10 — TablaDeTres

**Capítulo YouTube:** Tres muestras: la tabla de covarianzas

## Narración

<!-- b1 -->
Con tres muestras se ve el patrón. Hay que sumar las covarianzas de todas las parejas, que caben en una tabla de tres por tres. En la diagonal hay tres varianzas: tres por cuatro. Junto a la diagonal, cuatro parejas a un paso: cuatro por dos coma cuatro. En las esquinas, dos parejas a dos pasos: dos por uno coma cuatro cuatro. En total, veinticuatro coma cuatro ocho; entre nueve, dos coma siete dos.

- «Con tres muestras» → `tres`: tres muestras seguidas sobre la grabación
- «Hay que sumar las covarianzas» → `sumar`: aparece «Σ C = ?»
- «todas las parejas» → `parejas`: las parejas se unen con arcos entre las tres muestras
- «una tabla de tres por tres» → `tabla`: se dibuja una tabla de 3 × 3 vacía
- «En la diagonal» → `diag`: la diagonal se llena con «4, 4, 4» en ámbar
- «tres por cuatro» → `d12`: a la derecha, «3 × 4 = 12»
- «Junto a la diagonal» → `junto`: las casillas vecinas se resaltan
- «a un paso» → `vecinas`: las cuatro casillas vecinas se llenan con «2,4» en cian
- «cuatro por dos coma cuatro» → `v96`: «4 × 2,4 = 9,6»
- «En las esquinas» → `esquinas`: las dos esquinas se resaltan
- «a dos pasos» → `esq`: las esquinas se llenan con «1,44» en magenta
- «dos por uno coma cuatro cuatro» → `v288`: «2 × 1,44 = 2,88»
- «veinticuatro coma cuatro ocho» → `total`: «12 + 9,6 + 2,88 = 24,48»
- «dos coma siete dos» → `res`: «24,48 / 9 = 2,72» en ámbar

---

# Escena 11 — ElTriangulo

**Capítulo YouTube:** El triángulo de pesos

## Narración

<!-- b1 -->
Fíjate en cuántas parejas hay de cada separación. Tres a separación cero. Dos a un paso, a cada lado. Una a dos pasos, a cada lado. Uno, dos, tres, dos, uno: un triángulo. Con ene muestras pasa lo mismo. La varianza del promedio es la suma de la autocovarianza en cada separación, pesada por ese triángulo, y dividida entre ene al cuadrado.

- «cuántas parejas» → `cuantas`: sobre la tabla se cuentan las parejas por diagonal
- «Tres a separación cero» → `cero`: la diagonal principal se desliza abajo y forma una barra de altura 3
- «Dos a un paso» → `uno`: las diagonales vecinas se deslizan y forman barras de altura 2 a cada lado
- «Una a dos pasos» → `dos`: las esquinas forman barras de altura 1 a cada lado
- «Uno, dos, tres, dos, uno» → `cuenta`: se rotulan las alturas «1, 2, 3, 2, 1»
- «un triángulo» → `tri`: las cinco barras se perfilan como un triángulo
- «Con ene muestras» → `ene`: el triángulo se estira a N muestras
- «La varianza del promedio» → `var`: aparece «Var =»
- «la suma de la autocovarianza» → `suma`: entra «Σ C[k]»
- «pesada por ese triángulo» → `pesada`: entra «(N − |k|)» en ámbar, unido al triángulo
- «entre ene al cuadrado» → `n2`: entra «1/N²» delante

---

# Escena 12 — TiempoContinuo

**Capítulo YouTube:** Qué decide si promediar funciona

## Narración

<!-- b1 -->
Para el tiempo continuo es lo mismo, con una integral en lugar de la suma. Y ahora se ve qué lo decide todo. Si la autocovarianza se queda grande en todas las separaciones, como en la pila, el triángulo entero pesa y la varianza no baja. Pero si la autocovarianza se va apagando con la separación, la cosa cambia.

- «tiempo continuo» → `continuo`: el triángulo de barras se suaviza en un triángulo continuo
- «una integral» → `integral`: la versión continua, con una integral, aparece más pequeña bajo la fórmula de la suma
- «en lugar de la suma» → `suma`: el símbolo Σ se tacha y se sustituye por ∫
- «qué lo decide todo» → `decide`: se resalta la autocovarianza C como factor que multiplica al triángulo
- «Si la autocovarianza se queda grande» → `grande`: C(τ) se dibuja alta y plana
- «en todas las separaciones» → `todas`: la recta se extiende a todo el eje
- «como en la pila» → `pila`: rótulo «pila» junto a la recta
- «el triángulo entero pesa» → `entero`: todo el triángulo se sombrea
- «la varianza no baja» → `nobaja`: aparece «Var = 4» en rojo con una recta plana
- «Pero si la autocovarianza» → `pero`: la recta se sustituye por una curva
- «se va apagando» → `apaga`: C cae como la exponencial y solo la zona cercana al cero queda sombreada
- «la cosa cambia» → `cambia`: la zona sombreada se encoge y aparece un «¿?»

---

# Escena 13 — Criterio

**Capítulo YouTube:** El criterio ergódico

## Narración

<!-- b1 -->
El criterio es este: un proceso estacionario en sentido amplio, con varianza finita, cuya autocovarianza tiende a cero cuando la separación crece, es ergódico en media. La idea: al alargar la ventana, el triángulo se estira, pero la autocovarianza solo es grande cerca del cero. Esa zona pesa cada vez menos frente al total, y la varianza del promedio se va a cero.

- «El criterio» → `criterio`: aparece el marco del teorema
- «estacionario en sentido amplio» → `wss`: entra «WSS»
- «varianza finita» → `finita`: entra «+ σ² < ∞»
- «tiende a cero» → `tiende`: entra «+ C(τ) → 0»
- «es ergódico en media» → `ergo`: entra «⇒ ergódico en media» con tilde verde
- «La idea» → `idea`: el marco se aparta y entra el triángulo de pesos con C(τ)
- «el triángulo se estira» → `estira`: el triángulo de pesos se ensancha al crecer N
- «solo es grande cerca del cero» → `cerca`: C(τ) sombreada solo en la zona central
- «Esa zona» → `zona`: la zona sombreada se resalta
- «pesa cada vez menos» → `menos`: la zona sombreada se vuelve una fracción cada vez más pequeña del triángulo
- «frente al total» → `total`: se compara con el triángulo entero
- «se va a cero» → `cero`: aparece «Var → 0» con una flecha hacia abajo

---

# Escena 14 — NumerosDelSensor

**Capítulo YouTube:** El sensor contra la pila, con números

## Narración

<!-- b1 -->
Con el sensor. Con veinte muestras, la varianza del promedio es cero coma siete dos. Con cien, cero coma uno seis. Con quinientas, cero coma cero tres. Con dos mil, menos de una centésima. Y la pila, en todos los casos, cuatro. Una baja sin parar; la otra no se mueve.

- «Con el sensor» → `sensor`: una tabla vacía con dos columnas, «sensor» y «pila»
- «veinte muestras» → `n20`: primera fila «N = 20»
- «es cero coma siete dos» → `v725`: «0,725» en la columna del sensor
- «Con cien» → `n100`: fila «N = 100»
- «cero coma uno seis» → `v157`: «0,157»
- «Con quinientas» → `n500`: fila «N = 500»
- «cero coma cero tres» → `v032`: «0,032»
- «Con dos mil» → `n2000`: fila «N = 2.000»
- «menos de una centésima» → `v008`: «0,008»
- «la pila» → `pila`: la columna de la pila se rotula
- «en todos los casos» → `todos`: se llena con «4, 4, 4, 4»
- «Una baja sin parar» → `baja`: la columna del sensor se resalta con una flecha hacia abajo
- «la otra no se mueve» → `quieta`: la columna de la pila se resalta con una línea plana

---

# Escena 15 — MonteCarlo

**Capítulo YouTube:** Simulación: los puntos caen encima

## Narración

<!-- b1 -->
No son solo cuentas. Si se simulan miles de sensores y se mide de verdad cuánto se dispersan sus promedios, los puntos caen exactamente sobre la fórmula. El promedio temporal de una grabación larga del sensor se pega a la media del ensemble. El sensor es ergódico; la pila, no. Y la diferencia está en la memoria: una se borra y la otra no.

- «No son solo cuentas» → `cuentas`: la tabla se encoge a un lado
- «miles de sensores» → `miles`: muchas grabaciones del sensor se apilan
- «cuánto se dispersan sus promedios» → `dispersan`: se calcula el promedio de cada grabación y se marca sobre un eje
- «los puntos caen exactamente» → `puntos`: una gráfica log-log: los puntos de simulación aparecen
- «sobre la fórmula» → `formula`: la curva de la fórmula se dibuja debajo de los puntos: coinciden
- «una grabación larga» → `larga`: una grabación larga del sensor con su promedio acumulado
- «se pega a la media» → `pega`: el promedio converge hacia la línea «μ = 20»
- «El sensor es ergódico» → `ergo`: «sensor» con tilde verde
- «la pila, no» → `no`: la recta plana de la pila en 4, con cruz roja
- «la memoria» → `memoria`: aparece la palabra «memoria»
- «se borra» → `borra`: la autocovarianza del sensor cae a cero
- «la otra no» → `dura`: la de la pila sigue plana en 4

---

# Escena 16 — TrozosIndependientes

**Capítulo YouTube:** Muchas realizaciones disfrazadas de una

## Narración

<!-- b1 -->
La cuenta completa, con el límite hecho con cuidado, está en el apunte en profundidad. Pero la intuición es sencilla. Si las muestras muy separadas se olvidan unas de otras, una grabación larga contiene muchos trozos que se comportan casi como realizaciones independientes. Promediar en el tiempo es, en el fondo, promediar muchas realizaciones disfrazadas de una sola.

- «La cuenta completa» → `cuenta`: aparece una hoja del apunte con el límite
- «en el apunte en profundidad» → `apunte`: la hoja se rotula «apunte en profundidad»
- «la intuición es sencilla» → `intuicion`: la hoja se aparta y entra una grabación larga del sensor
- «muy separadas» → `separadas`: dos muestras lejanas resaltadas, con «C ≈ 0»
- «se olvidan unas de otras» → `olvidan`: un hilo entre ambas se corta
- «trozos» → `trozos`: la grabación se parte en trozos de colores
- «casi como realizaciones independientes» → `indep`: los trozos se apilan en vertical como un ensemble
- «Promediar en el tiempo» → `promediar`: una flecha horizontal recorre los trozos
- «en el fondo» → `fondo`: los trozos se resaltan
- «muchas realizaciones disfrazadas de una sola» → `disfraz`: los trozos vuelven a ponerse en fila y forman de nuevo una sola grabación

---

# Escena 17 — LaSorpresa

**Capítulo YouTube:** Con memoria, promediar cuesta más

## Narración

<!-- b1 -->
Y aquí hay una sorpresa. Con veinte muestras independientes de varianza cuatro, la varianza del promedio sería cuatro entre veinte: cero coma dos. Con el sensor es cero coma siete dos, más de tres veces más. Promediar funciona, pero más despacio. Veinte muestras con memoria no valen lo que veinte independientes. ¿Cuánto valen, entonces?

- «una sorpresa» → `sorpresa`: aparece un «!» grande
- «veinte muestras independientes» → `indep20`: veinte puntos independientes en fila
- «de varianza cuatro» → `v4`: cada punto se rotula «σ² = 4»
- «cuatro entre veinte» → `cuenta`: «4/20» en pantalla
- «cero coma dos» → `v02`: resultado «0,2» en verde
- «cero coma siete dos» → `v725`: al lado, «sensor: 0,725» en ámbar
- «más de tres veces más» → `tres`: una flecha entre ambos con «× 3,6»
- «Promediar funciona» → `funciona`: tilde verde sobre «promediar»
- «más despacio» → `despacio`: dos curvas de varianza contra N, la del sensor por encima de la independiente
- «Veinte muestras con memoria» → `memoria`: veinte puntos unidos con hilos
- «no valen lo que veinte independientes» → `novalen`: «≠» entre ambas filas
- «¿Cuánto valen, entonces?» → `cuanto`: «20 del sensor = ¿? independientes»

---

# Escena 18 — CuantasValen

**Capítulo YouTube:** ¿A cuántas muestras independientes equivale?

## Narración

<!-- b1 -->
Tienes mil muestras del sensor. Si fueran independientes, la varianza de su promedio sería cuatro entre mil. Pero tienen memoria. ¿A cuántas muestras independientes equivalen? ¿Mil? ¿Quinientas? ¿Doscientas cincuenta? Piénsalo un momento antes de seguir.

- «mil muestras del sensor» → `mil`: «1.000 muestras del sensor ≈ ¿? independientes»
- «Si fueran independientes» → `indep`: una fila de puntos sin hilos
- «cuatro entre mil» → `cuatro`: aparece «Var = 4/1.000» como referencia
- «tienen memoria» → `memoria`: los puntos se unen con hilos, como muestras que se recuerdan
- «¿A cuántas muestras independientes equivalen?» → `equivalen`: la pregunta «¿?» parpadea sobre la fila
- «¿Mil?» → `o1`: primera opción, «1.000»
- «¿Quinientas?» → `o2`: segunda opción, «500»
- «¿Doscientas cincuenta?» → `o3`: tercera opción, «250»
- «Piénsalo un momento» → `pausa`: un reloj de arena marca la pausa

---

# Escena 19 — SumaDeCorrelaciones

**Capítulo YouTube:** La suma de los coeficientes de correlación

## Narración

<!-- b1 -->
Para un registro largo, el triángulo es casi plano en la zona donde la autocovarianza importa. Así que la varianza del promedio queda como la varianza entre ene, multiplicada por la suma de los coeficientes de correlación en todas las separaciones: la de cero, las de un lado y las del otro. Esa suma dice cuántas veces se repite, en la práctica, cada dato.

- «Para un registro largo» → `registro`: una grabación larga del sensor
- «casi plano» → `plano`: el triángulo de pesos, muy ancho, se ve casi plano en el centro
- «donde la autocovarianza importa» → `zona`: se sombrea la zona central, donde C es grande
- «la varianza entre ene» → `sigman`: entra «σ²/N»
- «multiplicada por la suma» → `suma`: entra «· Σ ρ[k]»
- «coeficientes de correlación» → `rho`: se resalta «ρ[k]»
- «en todas las separaciones» → `todas`: una llave abarca todo el eje de k
- «la de cero, las de un lado y las del otro» → `lados`: la llave se parte en «k = 0», «k > 0» y «k < 0»
- «Esa suma dice» → `dice`: la suma se resalta
- «cuántas veces se repite» → `repite`: cada dato aparece duplicado y triplicado en una fila de puntos
- «cada dato» → `dato`: un dato se resalta entre sus copias

---

# Escena 20 — SumarElSensor

**Capítulo YouTube:** Sumando las correlaciones del sensor

## Narración

<!-- b1 -->
Sumémosla para el sensor. En separación cero, uno. A un paso, cero coma seis a cada lado. A dos pasos, cero coma tres seis. A tres, cero coma dos uno seis. El lado derecho va sumando cero coma nueve seis, uno coma uno ocho, uno coma tres, y se va acercando a uno coma cinco. Los dos lados dan tres, y con el uno del centro, cuatro.

- «Sumémosla para el sensor» → `sumemos`: ejes con barras de ρ[k] vacías
- «En separación cero, uno» → `cero`: barra central de altura «1»
- «cero coma seis a cada lado» → `b06`: barras «0,6» a ambos lados del cero
- «cero coma tres seis» → `b036`: barras «0,36»
- «cero coma dos uno seis» → `b0216`: barras «0,216», y siguen decayendo
- «El lado derecho va sumando» → `lado`: aparece un contador bajo el lado derecho
- «cero coma nueve seis» → `s096`: el contador marca «0,96»
- «uno coma uno ocho» → `s118`: el contador marca «1,18»
- «uno coma tres» → `s13`: el contador marca «1,3»
- «uno coma cinco» → `s15`: el contador se estabiliza en «1,5»
- «Los dos lados dan tres» → `tres`: «2 × 1,5 = 3»
- «el uno del centro, cuatro» → `cuatro`: «1 + 3 = 4» en ámbar

---

# Escena 21 — NEfectiva

**Capítulo YouTube:** Tamaño de muestra efectivo

## Narración

<!-- b1 -->
Así que la varianza del promedio es cuatro veces la que tendrías con datos independientes. Dicho de otra manera, mil muestras del sensor valen como mil entre cuatro: doscientas cincuenta independientes. A eso se le llama tamaño de muestra efectivo: el número de muestras dividido entre la suma de los coeficientes de correlación. Con una memoria más larga, de cero coma nueve por paso, la suma da diecinueve.

- «cuatro veces» → `cuatro`: «Var = 4 × (σ²/N)»
- «con datos independientes» → `indep`: «σ²/N» se rotula «independientes»
- «mil muestras del sensor» → `mil`: una fila de mil puntos
- «mil entre cuatro» → `entre4`: «1.000 / 4»
- «doscientas cincuenta independientes» → `n250`: los puntos se agrupan de cuatro en cuatro y aparece «250»
- «A eso se le llama» → `llama`: una llave sobre «250»
- «tamaño de muestra efectivo» → `neff`: aparece «N_eff =» en palabra clave
- «el número de muestras» → `numero`: entra «N»
- «dividido entre la suma» → `dividido`: entra «/ Σ»
- «de los coeficientes de correlación» → `rho`: entra «ρ[k]»
- «Con una memoria más larga» → `larga`: entran barras de ρ = 0,9 decayendo despacio
- «cero coma nueve por paso» → `r09`: rótulo «ρ = 0,9 por paso»
- «diecinueve» → `v19`: «Σ = 19» y «1.000 / 19 ≈ 53»

---

# Escena 22 — ErrorComun

**Capítulo YouTube:** El error más común con datos con memoria

## Narración

<!-- b1 -->
Es un error muy común calcular el error de una media como si los datos fueran independientes cuando tienen memoria: el resultado parece mucho más preciso de lo que es. Así que la memoria tiene dos caras. Gracias a que se borra, promediar en el tiempo funciona. Pero mientras dura, cada muestra cuenta menos. Y todavía le queda una tercera cara.

- «error de una media» → `error`: aparece la etiqueta «error ± σ/√N»
- «como si los datos fueran independientes» → `tachada`: la etiqueta se tacha y aparece al lado «σ/√N_eff»
- «cuando tienen memoria» → `memoria`: una fila de puntos unidos con hilos
- «mucho más preciso» → `preciso`: dos barras de error: una estrecha (la falsa) y una ancha (la real)
- «de lo que es» → `real`: la barra ancha se resalta
- «dos caras» → `caras`: dos tarjetas en fila
- «se borra» → `borra`: primera tarjeta, «se borra»
- «promediar en el tiempo funciona» → `funciona`: la primera tarjeta completa «→ promediar funciona»
- «Pero mientras dura» → `dura`: segunda tarjeta, «dura»
- «cada muestra cuenta menos» → `menos`: la segunda tarjeta completa «→ cada muestra cuenta menos»
- «una tercera cara» → `tercera`: una tercera tarjeta boca abajo, con un «¿?»

---

# Escena 23 — Cierre

**Capítulo YouTube:** Lo que viene: adivinar el futuro

## Narración

<!-- b1 -->
Si la memoria se borra, una sola grabación basta para medir la media, aunque cada dato cuente menos. Si no se borra, no basta. Pero esa memoria que estorba al promediar tiene una tercera cara: si una muestra recuerda a la anterior, puede servir para adivinar la siguiente. Eso, en el próximo episodio: «Adivinar el futuro, limpiar el presente».

- «se borra» → `borra`: la tarjeta «se borra» con tilde verde y el sensor
- «una sola grabación basta» → `basta`: una sola grabación larga con un contador que se acerca a la media
- «aunque cada dato cuente menos» → `menos`: los datos de la grabación se atenúan
- «Si no se borra» → `noborra`: la pila con su recta plana y una cruz roja
- «Pero esa memoria que estorba» → `estorba`: los hilos de memoria entre muestras se resaltan
- «tercera cara» → `tercera`: la tarjeta boca abajo se da la vuelta: «predecir»
- «si una muestra recuerda a la anterior» → `recuerda`: dos muestras seguidas unidas por un hilo
- «adivinar la siguiente» → `adivinar`: la grabación se corta y una muestra con «?» aparece a la derecha
- «en el próximo episodio» → `proximo`: un sello «próximo episodio»
- «Adivinar el futuro, limpiar el presente» → `titulo`: aparece el título del episodio 6 con rebote
