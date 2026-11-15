# Episodio 6 — Fabricar el color y quitarlo

Capítulo 11 (Densidad espectral de potencia), episodio 6 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 25 a 28), más un gancho y un cierre nuevos.

**Estado:** 13 escenas animadas (`s01`–`s13`); borrador 480p15 de 8:35 con 0 avisos y hojas de contacto revisadas. Falta el visto bueno del usuario al mp4 (paso 15) y el render final.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Hay dos filtros distintos que fabrican exactamente el mismo ruido… uno se apaga y el otro explota.»
- ⭐ Escena 13 (cierre): resumen y anuncia E7 por su título, «Dos procesos, frecuencia a frecuencia».

Notas para los episodios vecinos:
- El cierre de E5 tiene que anunciar este título, «Fabricar el color y quitarlo».
- Las escenas 05 a 09 usan el filtro (2, 1)/√5 de la escena 10 del guion base (E2) y el eco del 0,6 del Cap. 10: tienen que ser el mismo dibujo.

Reparto de las escenas del guion base: 03 → escena 25 (bloques 1–2); 04 → escena 25 (bloques 3–5); 05 → escena 26 (bloques 1–2); 06 → escena 26 (bloque 3); 07 → escena 26 (bloques 4–5); 08 → escena 27 (bloques 1–2); 09 → escena 27 (bloques 3–5); 10 → escena 28 (bloque 1); 11 → escena 28 (bloques 2–3); 12 → escena 28 (bloques 4–5).
El texto del guion base no cambia: solo se reparten bloques enteros en escenas atómicas.

---

# Escena 01 — Gancho

**Capítulo YouTube:** Un ruido, dos filtros

## Narración

<!-- b1 -->
Hay dos filtros distintos que fabrican exactamente el mismo ruido. Pero si intentas deshacerlo, uno de los dos se apaga, y el otro explota. Hoy fabricamos ruido a medida, y aprendemos a quitarlo.

- «dos filtros distintos» → `dos`: aparecen dos cajas de filtro, «H₁» y «H₂», lado a lado
- «exactamente el mismo ruido» → `mismo`: de las dos cajas sale la misma traza magenta
- «intentas deshacerlo» → `deshacer`: flechas de vuelta hacia la moneda blanca desde cada filtro
- «se apaga» → `apaga`: barras que decaen a la izquierda
- «explota» → `explota`: barras que se salen de la pantalla a la derecha, con un destello rojo
- «fabricamos ruido a medida» → `medida`: la traza magenta se ensancha hasta una curva de espectro ámbar
- «quitarlo» → `quitarlo`: la curva se aplana a una línea horizontal

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Fabricar el color y quitarlo

## Narración

<!-- b1 -->
Fabricar el color y quitarlo.

- «Fabricar el color» → `t1`: «Fabricar el color» entra con rebote
- «y quitarlo» → `t2`: «y quitarlo» entra debajo, con la etiqueta «Capítulo 11 · Densidad espectral de potencia»

---

# Escena 03 — ElPicoDeLaRespiracion

**Capítulo YouTube:** Un pico que delata la respiración

## Narración

<!-- b1 -->
Un electrocardiograma registra los latidos del corazón. A partir de él se calcula la frecuencia cardíaca instante a instante: setenta, sesenta y ocho, setenta y dos. Vista en el tiempo, parece una línea que sube y baja sin ningún orden. Pero si le estimamos la densidad espectral, aparece algo que a simple vista no se ve.

- «Un electrocardiograma» → `ecg`: aparece un electrocardiograma
- «los latidos del corazón» → `latidos`: la traza late, un latido por pico, con el sonido de latido
- «frecuencia cardíaca instante a instante» → `fc`: debajo, una segunda traza con los intervalos convertidos en pulsaciones por minuto
- «setenta, sesenta y ocho, setenta y dos» → `valores`: sobre la traza van cayendo los números «70», «68», «72»
- «Vista en el tiempo» → `tiempo`: la traza de pulsaciones se queda sola en pantalla, con la etiqueta «en el tiempo»
- «sube y baja sin ningún orden» → `desorden`: la traza se resalta en ámbar, irregular
- «le estimamos la densidad espectral» → `estimamos`: una flecha lleva la traza a una caja «Welch»
- «a simple vista no se ve» → `novese`: a la derecha se abre un eje de frecuencias vacío, con un «?»

<!-- b2 -->
Un pico nítido en cero coma uno seis seis hercios. Una oscilación que se repite cada uno entre cero coma uno seis seis segundos: unos seis segundos. Diez veces por minuto. Y diez veces por minuto es justo el ritmo al que respiraba la persona. El espectro revela que al respirar el corazón acelera y frena.

- «Un pico nítido» → `pico`: en el eje se alza un pico ámbar, fino
- «cero coma uno seis seis hercios» → `hz`: sobre el pico, la etiqueta «0,166 Hz»
- «Una oscilación que se repite» → `osc`: un seno lento en ámbar se dibuja bajo el pico
- «cada uno entre cero coma uno seis seis segundos» → `cuenta`: aparece «1 / 0,166 ≈ 6 s»
- «unos seis segundos» → `seis`: una llave de 6 s marca un ciclo de la oscilación lenta
- «Diez veces por minuto» → `diez`: aparece «60 / 6 = 10 por minuto»
- «justo el ritmo al que respiraba la persona» → `pecho`: un pecho que sube y baja al ritmo del pico, diez veces
- «El espectro revela» → `revela`: una flecha del pico al pecho con el rótulo «el espectro revela»
- «al respirar el corazón acelera y frena» → `acelera`: la traza de pulsaciones se sincroniza con el pecho, sube al inspirar y baja al espirar

---

# Escena 04 — MuestreoYFabricar

**Capítulo YouTube:** Muestrear y fabricar

## Narración

<!-- b1 -->
Un pico marcado en un espectro delata algo que se repite, como las rayas de la sinusoide de hace unos episodios. Otra herramienta de Señales y Sistemas que sobrevive al azar es el teorema del muestreo: si una señal no tiene frecuencias por encima de be, basta con tomar más de dos be muestras por segundo para reconstruirla.

- «Un pico marcado en un espectro» → `pico`: corte; un espectro con un pico fino
- «algo que se repite» → `repite`: bajo él, una sinusoide que se repite, con flechas de ciclo a ciclo
- «las rayas de la sinusoide» → `rayas`: el pico se convierte en una raya vertical, como en el espectro de líneas
- «de hace unos episodios» → `hace`: las rayas quedan rotuladas «hace unos episodios»
- «Otra herramienta de Señales y Sistemas» → `otra`: se aparta lo anterior y entra la etiqueta «Señales y Sistemas»
- «sobrevive al azar» → `sobrevive`: una traza de ruido magenta aparece junto a la etiqueta con un tilde verde
- «teorema del muestreo» → `muestreo`: la palabra «muestreo» entra con rebote
- «no tiene frecuencias por encima de be» → `banda`: un espectro que vale cero más allá de «B»
- «más de dos be muestras por segundo» → `dosb`: aparece «> 2B muestras por segundo» y unos puntos caen sobre una señal
- «reconstruirla» → `reconstruir`: los puntos se unen y dibujan la curva original

<!-- b2 -->
Con procesos pasa lo mismo: si la densidad espectral vale cero por encima de be, las muestras bastan. No se reconstruye cada realización punto a punto, pero el error tiene potencia cero, y en la práctica eso es lo mismo.

- «Con procesos pasa lo mismo» → `procesos`: la señal se cambia por una traza de ruido magenta
- «la densidad espectral vale cero por encima de be» → `cero`: su densidad espectral ámbar, nula más allá de «B»
- «las muestras bastan» → `bastan`: los puntos de muestra aparecen sobre la traza
- «No se reconstruye cada realización» → `norecon`: una cruz fina sobre «cada realización»
- «punto a punto» → `punto`: la reconstrucción se dibuja casi encima, con una pequeña desviación
- «el error tiene potencia cero» → `error`: aparece «E[(x − x̂)²] = 0» con el error en rojo
- «en la práctica eso es lo mismo» → `igual`: un tilde verde junto a la ecuación

<!-- b3 -->
Hasta aquí hemos usado el espectro para mirar. También sirve para fabricar. Si quieres probar un altavoz con un ruido de una forma concreta, o simular el ruido de un canal de comunicaciones, necesitas generar un proceso con la densidad espectral que tú elijas. ¿Cómo se consigue?

- «usado el espectro para mirar» → `mirar`: aparece una lupa sobre un espectro
- «También sirve para fabricar» → `fabricar`: la lupa se aparta y entra la palabra «fabricar» en ámbar
- «probar un altavoz» → `altavoz`: aparece un altavoz con ondas
- «un ruido de una forma concreta» → `forma`: junto al altavoz, un espectro con una forma elegida
- «el ruido de un canal de comunicaciones» → `canal`: el altavoz se cambia por un canal con una antena y ruido sobre la señal
- «necesitas generar un proceso» → `generar`: aparece una caja «proceso» con una flecha de salida
- «la densidad espectral que tú elijas» → `elijas`: una mano dibuja a voluntad una curva de espectro
- «¿Cómo se consigue?» → `como`: entra la pregunta «¿cómo fabrico un ruido con este espectro?»

---

# Escena 05 — LuzBlancaPorUnVidrio

**Capítulo YouTube:** Luz blanca por un vidrio de color

## Narración

<!-- b1 -->
Empezamos por lo fácil: el ruido blanco, la moneda, con su espectro plano de altura uno. Lo pasamos por un filtro. La densidad espectral de la salida es la ganancia al cuadrado por la de la entrada, que es uno. Así que si quiero una densidad concreta, necesito un filtro cuya ganancia al cuadrado sea esa densidad. Como pasar luz blanca por un vidrio de color.

- «el ruido blanco, la moneda» → `moneda`: la moneda ±1 con su traza de muestras
- «espectro plano de altura uno» → `plano`: su espectro, una línea horizontal a altura 1
- «Lo pasamos por un filtro» → `filtro`: el bloque «H» recibe la moneda y el espectro plano
- «La densidad espectral de la salida» → `salida`: a la salida del bloque se rotula «densidad de salida»
- «la ganancia al cuadrado por la de la entrada» → `formula`: aparece «D_xx = |H|² · 1» pieza a pieza
- «que es uno» → `uno`: el «1» final se resalta
- «una densidad concreta» → `concreta`: a la salida, una curva con forma
- «ganancia al cuadrado sea esa densidad» → `despeja`: la fórmula pasa a «|H| = √D_xx»
- «luz blanca por un vidrio de color» → `vidrio`: un haz de luz blanca atraviesa un vidrio y sale de color

<!-- b2 -->
Ya lo hemos hecho sin decirlo. El filtro que fabricó rho igual a cero coma cuatro, dos veces la moneda más la anterior entre raíz de cinco, tiene una ganancia al cuadrado que, desarrollada, es cuatro más uno más cuatro por el coseno de omega, entre cinco. Es decir, uno más cero coma ocho por el coseno de omega. El espectro de aquel proceso.

- «Ya lo hemos hecho sin decirlo» → `hecho`: vuelve el filtro del episodio de los límites del espectro en su bloque
- «rho igual a cero coma cuatro» → `rho`: aparece «ρ = 0,4»
- «dos veces la moneda más la anterior entre raíz de cinco» → `filtro`: aparece «(2 w[n] + w[n−1]) / √5»
- «una ganancia al cuadrado» → `gan`: aparece «|2 + e^{−jΩ}|² / 5»
- «cuatro más uno más cuatro por el coseno de omega, entre cinco» → `cuenta`: se desarrolla en «(4 + 1 + 4 cos Ω) / 5»
- «por el coseno de omega» → `coseno`: el término «4 cos Ω» se resalta
- «Es decir» → `esdecir`: un signo igual grande entre la cuenta y el resultado
- «uno más cero coma ocho por el coseno de omega» → `resultado`: queda «1 + 0,8 cos Ω»
- «El espectro de aquel proceso» → `espectro`: a su lado, la curva de aquel episodio con una marca de coincidencia y un tilde verde

---

# Escena 06 — ElEcoDelSensor

**Capítulo YouTube:** El eco del sensor

## Narración

<!-- b1 -->
Otro ejemplo, con eco: las fluctuaciones del sensor de temperatura del capítulo anterior. La salida es cero coma seis veces la salida anterior más una moneda nueva: cada muestra arrastra el sesenta por ciento de la anterior. Las vecinas se parecen cero coma seis; a dos pasos, cero coma seis al cuadrado, cero coma tres seis; a tres, cero coma dos dos. Memoria que se borra poco a poco, y un espectro concentrado en las frecuencias bajas.

- «sensor de temperatura» → `sensor`: vuelve el termómetro del capítulo 10
- «La salida es» → `salida`: un recuadro «salida» con la muestra actual resaltada
- «cero coma seis veces la salida anterior más una moneda nueva» → `ecuacion`: aparece «x[n] = 0,6 x[n−1] + w[n]» pieza a pieza
- «una moneda nueva» → `nueva`: la moneda w[n] se resalta en magenta dentro de la fórmula
- «arrastra el sesenta por ciento de la anterior» → `arrastra`: una cadena de muestras, cada una con una flecha que lleva el 60 % de la anterior
- «Las vecinas se parecen cero coma seis» → `vecinas`: el primer tallo de correlación sube a «0,6»
- «cero coma seis al cuadrado, cero coma tres seis» → `dos`: aparece «0,6 · 0,6 = 0,36» y el segundo tallo
- «a tres, cero coma dos dos» → `tres`: el tercer tallo, «0,22»
- «Memoria que se borra poco a poco» → `memoria`: los tallos siguen bajando hasta apagarse
- «concentrado en las frecuencias bajas» → `bajas`: su espectro, un bulto ámbar pegado a la frecuencia cero

---

# Escena 07 — ElFactorEspectral

**Capítulo YouTube:** El filtro modelador y Bochner

## Narración

<!-- b1 -->
Un filtro así se llama modelador, porque le da forma al espectro plano del blanco, y su ganancia es una especie de raíz cuadrada de la densidad: se la llama factor espectral. Siempre existe, porque la densidad nunca es negativa y se le puede sacar la raíz.

- «modelador» → `modelador`: la palabra «modelador» entra con rebote sobre el bloque H
- «le da forma al espectro plano del blanco» → `forma`: el espectro plano entra y sale con forma
- «una especie de raíz cuadrada de la densidad» → `raiz`: aparece «|H| = √D_xx»
- «factor espectral» → `factor`: el rótulo «factor espectral» se pega a la fórmula
- «Siempre existe» → `existe`: un tilde verde
- «la densidad nunca es negativa» → `nunca`: la curva de la densidad sobre el eje, toda por encima del cero
- «se le puede sacar la raíz» → `sacar`: sobre la curva se dibuja su raíz

<!-- b2 -->
Y ahora vuelve al teorema de Bochner: toda función real, par y no negativa es la densidad de algún proceso. La demostración es exactamente esto. Le sacas la raíz, construyes el filtro, le metes ruido blanco, y lo que sale es ese proceso. Cada vez que se colorea un ruido con un filtro, se está ejecutando la demostración.

- «teorema de Bochner» → `bochner`: vuelve el rótulo «Bochner» del episodio anterior
- «real, par y no negativa» → `tres`: tres marcas ✓ junto a la curva: «real», «par», «no negativa»
- «la densidad de algún proceso» → `proceso`: la curva se une con un proceso por una flecha
- «La demostración es exactamente esto» → `demo`: el rótulo «la demostración» aparece
- «Le sacas la raíz» → `raiz`: la curva se transforma en su raíz
- «construyes el filtro» → `filtro`: la raíz pasa a ser el bloque H
- «le metes ruido blanco» → `blanco`: entra la moneda por la izquierda del bloque
- «lo que sale es ese proceso» → `sale`: sale la traza coloreada, con un tilde verde
- «Cada vez que se colorea un ruido» → `colorea`: un ciclo de flechas moneda → filtro → coloreado se repite
- «ejecutando la demostración» → `ejecuta`: el bloque se pega al rótulo «Bochner» y brilla

---

# Escena 08 — PorQueBlanquear

**Capítulo YouTube:** Blanquear un ruido

## Narración

<!-- b1 -->
Ahora el camino contrario, que es el que más vamos a usar en los dos capítulos siguientes. Tengo un ruido coloreado y quiero convertirlo en blanco. ¿Para qué? Porque muchos problemas de estimación y de detección tienen solución conocida cuando el ruido es blanco. La estrategia es blanquear primero y aplicar después lo que ya sabemos.

- «el camino contrario» → `contrario`: la cadena «blanco → H → coloreado» se invierte con una flecha de vuelta
- «los dos capítulos siguientes» → `siguientes`: aparecen los rótulos «Cap. 12» y «Cap. 13»
- «un ruido coloreado» → `coloreado`: a la izquierda, una traza magenta con su espectro con forma
- «convertirlo en blanco» → `blanco`: a la derecha, una traza blanca con su espectro plano
- «¿Para qué?» → `paraque`: aparece un signo de pregunta grande
- «estimación y de detección» → `est`: aparecen las dos etiquetas «estimar» y «detectar»
- «solución conocida cuando el ruido es blanco» → `conocida`: junto a cada etiqueta, un tilde verde con «ruido blanco»
- «La estrategia» → `estrategia`: una flecha en dos pasos: «blanquear» y «aplicar»
- «blanquear primero» → `primero`: la palabra «blanquear» entra con rebote en ámbar
- «lo que ya sabemos» → `sabemos`: sigue «→ aplicar lo que ya sabemos»

<!-- b2 -->
El filtro que lo hace se llama blanqueador, y su ganancia al cuadrado es una constante dividida entre la densidad espectral. Amplifica donde el ruido tiene poca potencia y atenúa donde tiene mucha, hasta dejarlo plano. Si el modelador convertía blanco en coloreado, el blanqueador es su inverso.

- «se llama blanqueador» → `nombre`: la palabra «blanqueador» entra con rebote sobre un bloque nuevo «1/H»
- «una constante dividida entre la densidad espectral» → `formula`: aparece «|H_w|² = σ_w² / S_xx» pieza a pieza
- «Amplifica donde el ruido tiene poca potencia» → `amplifica`: la ganancia del blanqueador sube donde el espectro coloreado baja
- «atenúa donde tiene mucha» → `atenua`: la ganancia baja donde el espectro sube
- «hasta dejarlo plano» → `plano`: el producto de ambas curvas queda como una línea horizontal
- «convertía blanco en coloreado» → `convertia`: la cadena «blanco → H → coloreado» aparece
- «el blanqueador es su inverso» → `inverso`: las dos cadenas, «blanco → H → coloreado» y «coloreado → 1/H → blanco», una encima de la otra

---

# Escena 09 — BlanquearElEco

**Capítulo YouTube:** Blanquear el eco

## Narración

<!-- b1 -->
Con el eco se ve a mano. El modelador hacía: equis de ene es cero coma seis por la equis anterior, más la moneda. Pues el blanqueador hace: equis de ene menos cero coma seis por la equis anterior. Sustituye la primera ecuación en la segunda: el cero coma seis se cancela, y lo que queda es la moneda. Exacta.

- «Con el eco se ve a mano» → `eco`: vuelve el eco del 0,6
- «modelador hacía» → `modelador`: aparece «x[n] = 0,6 x[n−1] + w[n]»
- «por la equis anterior» → `por`: la muestra anterior x[n−1] se resalta con una flecha al 0,6
- «más la moneda» → `masmoneda`: la moneda w[n] de la ecuación se resalta
- «el blanqueador hace» → `blanqueador`: debajo, «u[n] = x[n] − 0,6 x[n−1]»
- «menos cero coma seis» → `menos`: el término «− 0,6 x[n−1]» de la ecuación nueva se resalta
- «Sustituye la primera ecuación en la segunda» → `sustituye`: la primera ecuación entra dentro de la segunda, con una flecha
- «se cancela» → `cancela`: los términos «0,6 x[n−1]» se tachan uno contra otro
- «lo que queda es la moneda» → `queda`: queda «u[n] = w[n]»
- «Exacta» → `exacta`: un tilde verde junto al resultado

<!-- b2 -->
Comprobémoslo con datos: cuatrocientas mil muestras simuladas. Antes del blanqueador, las correlaciones con las vecinas son cero coma seis, cero coma tres seis, cero coma dos dos, cero coma uno tres. Después: cero, cero coma cero cero tres, menos cero coma cero cero uno, cero. Toda la memoria, borrada.

- «cuatrocientas mil muestras simuladas» → `simuladas`: aparece «400.000 muestras»
- «Antes del blanqueador» → `antes`: se arma una tabla con la fila «x»
- «cero coma seis, cero coma tres seis» → `primeras`: se llenan «0,60» y «0,36»
- «cero coma dos dos, cero coma uno tres» → `siguientes`: se llenan «0,22» y «0,13»
- «Después» → `despues`: aparece la fila «u»
- «cero, cero coma cero cero tres» → `ceros1`: se llenan «0,00» y «0,003»
- «menos cero coma cero cero uno, cero» → `ceros2`: se llenan «−0,001» y «0,00»
- «Toda la memoria, borrada» → `borrada`: los tallos de correlación de «u» quedan en cero y brilla un tilde verde

<!-- b3 -->
Modelador y blanqueador son uno el inverso del otro. Pero hay un detalle que hemos pasado por alto. El factor espectral, la raíz cuadrada del espectro, no es único. Hay más de un filtro que fabrica el mismo proceso. Y a la hora de deshacerlo, no todos sirven.

- «uno el inverso del otro» → `inverso`: las dos cadenas de bloques, enfrentadas
- «un detalle que hemos pasado por alto» → `detalle`: entra un signo de pregunta ámbar sobre el bloque H
- «El factor espectral» → `factor`: el rótulo «factor espectral» entra con rebote
- «la raíz cuadrada del espectro» → `raizesp`: aparece «√S_xx» junto al rótulo
- «no es único» → `unico`: junto a «factor espectral», aparece «¿único?» y se tacha
- «más de un filtro» → `mas`: el bloque H se duplica en dos bloques distintos, «H₁» y «H₂»
- «el mismo proceso» → `mismo`: los dos dan la misma traza magenta
- «no todos sirven» → `sirven`: sobre los dos bloques invertidos, un tilde en uno y un interrogante en el otro

---

# Escena 10 — DosModeladores

**Capítulo YouTube:** Dos filtros, el mismo proceso

## Narración

<!-- b1 -->
Volvamos al filtro que fabricó rho igual a cero coma cuatro: dos veces la moneda de ahora más la anterior, entre raíz de cinco. Ahora dale la vuelta a los coeficientes: una vez la de ahora más dos veces la anterior. Potencia: uno más cuatro, entre cinco, uno. Vecinas: uno por dos, entre cinco, cero coma cuatro. El mismo proceso, con otro filtro.

- «rho igual a cero coma cuatro» → `rho`: vuelve «ρ = 0,4»
- «dos veces la moneda de ahora más la anterior» → `primero`: aparece el bloque «(2 w[n] + w[n−1]) / √5»
- «entre raíz de cinco» → `raiz5`: el «/ √5» del bloque se resalta
- «dale la vuelta a los coeficientes» → `vuelta`: los coeficientes «2» y «1» se cruzan con una flecha
- «una vez la de ahora más dos veces la anterior» → `segundo`: aparece, debajo, el bloque «(w[n] + 2 w[n−1]) / √5»
- «Potencia» → `potencia`: sobre los dos bloques, el rótulo «potencia»
- «uno más cuatro, entre cinco, uno» → `cuenta1`: aparece «(4 + 1)/5 = 1» en los dos
- «Vecinas» → `vecinas`: sobre los dos bloques, el rótulo «vecinas»
- «uno por dos, entre cinco, cero coma cuatro» → `cuenta2`: aparece «2 · 1 / 5 = 0,4» en los dos
- «El mismo proceso, con otro filtro» → `mismo`: debajo de los dos, el mismo espectro «1 + 0,8 cos Ω»

---

# Escena 11 — QueSeApagaYQueExplota

**Capítulo YouTube:** Uno se apaga, el otro explota

## Narración

<!-- b1 -->
Los dos sirven como modelador. Veamos si sirven como blanqueador: intentemos recuperar la moneda a partir de la salida. Con el primero, despejando, cada moneda es la salida menos la moneda anterior, dividido entre dos. Si le metemos un único impulso, la respuesta es un medio, menos un cuarto, un octavo: cada vez la mitad. Se apaga. Funciona.

- «sirven como modelador» → `modelador`: dos tildes verdes sobre los dos bloques
- «Veamos si sirven como blanqueador» → `veamos`: un signo de pregunta sobre cada bloque
- «recuperar la moneda a partir de la salida» → `recuperar`: flechas de vuelta desde la salida hacia la moneda
- «Con el primero, despejando» → `primero`: el primer bloque pasa a «w[n] = (√5 y[n] − w[n−1]) / 2»
- «cada moneda es la salida» → `cadamoneda`: aparece el lado derecho de la fórmula, «(√5 y[n] − w[n−1]) / 2»
- «dividido entre dos» → `entredos`: el «/ 2» de la fórmula se resalta
- «único impulso» → `impulso`: entra una sola barra de altura 1
- «un medio, menos un cuarto, un octavo» → `barras`: salen barras «½», «−¼», «⅛» que se alternan
- «cada vez la mitad» → `mitad`: una flecha «× −½» entre barras sucesivas
- «Se apaga» → `apaga`: las barras se hacen cada vez más pequeñas hasta desaparecer
- «Funciona» → `funciona`: un tilde verde

<!-- b2 -->
Con el segundo, cada moneda es la salida menos dos veces la moneda anterior. Ahora el impulso da uno, menos dos, cuatro, menos ocho, dieciséis: cada vez el doble. Explota. Ese blanqueador es inestable: cualquier pequeño error se multiplica hasta el infinito. El filtro modela bien, pero no se puede deshacer.

- «Con el segundo» → `segundo`: corte al segundo bloque invertido
- «la salida menos dos veces la moneda anterior» → `formula`: aparece «w[n] = √5 y[n] − 2 w[n−1]»
- «Ahora el impulso da» → `ahora`: entra un único impulso de altura 1 a la izquierda
- «uno, menos dos, cuatro, menos ocho, dieciséis» → `barras`: salen barras «1», «−2», «4», «−8», «16» que crecen
- «cada vez el doble» → `doble`: una flecha «× −2» entre barras sucesivas
- «Explota» → `explota`: las barras se salen de la pantalla y un destello rojo las cubre
- «inestable» → `inestable`: la palabra «inestable» entra con rebote en rojo
- «cualquier pequeño error» → `error`: una pequeña perturbación sobre la primera barra
- «se multiplica hasta el infinito» → `infinito`: la perturbación crece con las barras
- «El filtro modela bien» → `modela`: tilde verde junto al bloque de modelar
- «no se puede deshacer» → `nodeshacer`: una cruz roja sobre el bloque invertido

---

# Escena 12 — FaseMinimaYElLimite

**Capítulo YouTube:** Fase mínima y el límite del blanqueo

## Narración

<!-- b1 -->
De todos los filtros que fabrican el mismo proceso, hay uno cuya inversa no explota: aquí, el que pone el coeficiente grande primero. Se llama factor de fase mínima, y es el único que permite blanquear en tiempo real, con un filtro causal y estable. En el próximo capítulo será una pieza central.

- «hay uno cuya inversa no explota» → `uno`: los dos filtros, con el primero resaltado y su tilde verde
- «el coeficiente grande primero» → `grande`: en «(2, 1)» el «2» se resalta por delante del «1»
- «factor de fase mínima» → `fase`: el rótulo «fase mínima» entra con rebote
- «el único que permite blanquear en tiempo real» → `tiempo`: un reloj corre junto al blanqueador del primer filtro
- «causal y estable» → `causal`: dos tildes «causal» y «estable»
- «En el próximo capítulo» → `proximo`: aparece una flecha con «Cap. 12»
- «una pieza central» → `central`: «fase mínima» queda en el centro y brilla

<!-- b2 -->
Y un límite que ningún blanqueador puede saltarse. Si el proceso no tiene nada de potencia en toda una banda, para dejarlo plano habría que multiplicar esa banda por infinito. No se puede blanquear lo que no existe. En el capítulo que viene esta idea tendrá nombre propio.

- «un límite que ningún blanqueador puede saltarse» → `limite`: entra un muro sobre la cadena del blanqueador
- «Si el proceso no tiene» → `si`: un espectro con un tramo vacío empieza a dibujarse
- «nada de potencia en toda una banda» → `nada`: un espectro que vale cero en una banda entera
- «dejarlo plano» → `plano`: una línea horizontal punteada a altura uno
- «multiplicar esa banda por infinito» → `infinito`: la ganancia del blanqueador se dispara en esa banda, fuera de pantalla
- «No se puede blanquear lo que no existe» → `noexiste`: una cruz roja sobre el blanqueador y la frase en pantalla
- «En el capítulo que viene» → `cap`: flecha con el rótulo «Cap. 12»
- «tendrá nombre propio» → `nombre`: un rótulo con un nombre tapado por un signo de pregunta

---

# Escena 13 — Cierre

**Capítulo YouTube:** Lo que viene: dos procesos, frecuencia a frecuencia

## Narración

<!-- b1 -->
Repasemos. Con el espectro puedes mirar un ruido, fabricarlo con un filtro modelador y quitarle el color con un blanqueador, y el único que se puede deshacer es el de fase mínima. Pero hasta ahora hemos tratado con un solo proceso. ¿Y si hay dos, como la voz y el murmullo, y queremos saber cuánto se parecen, frecuencia a frecuencia? En el próximo episodio: dos procesos, frecuencia a frecuencia.

- «mirar un ruido» → `mirar`: una traza con su espectro
- «fabricarlo con un filtro modelador» → `fabricar`: la moneda entra en H y sale coloreada
- «quitarle el color con un blanqueador» → `quitar`: la coloreada entra en 1/H y sale plana
- «y el único que se puede deshacer» → `unico`: el bloque de fase mínima se separa del otro, que se tacha
- «fase mínima» → `fasemin`: el rótulo «fase mínima» con un tilde verde
- «un solo proceso» → `uno`: queda una sola traza
- «la voz y el murmullo» → `dos`: aparecen dos trazas, azul y magenta
- «cuánto se parecen» → `parecen`: entre ellas, un «¿cuánto se parecen?»
- «frecuencia a frecuencia» → `frec`: sobre un eje de frecuencias, pequeñas ventanas recorren de banda en banda
- «En el próximo episodio» → `prox`: la flecha hacia el episodio siguiente
- «dos procesos, frecuencia a frecuencia» → `titulo_e7`: entra el título del siguiente episodio
