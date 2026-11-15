# Episodio 3 — ¿Cuánto nos equivocamos?

Capítulo 13 (Detección de señales), episodio 3 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 09 a 13), más un gancho y un cierre nuevos.

**Estado:** escenas `s01`–`s13` animadas; borrador 480p15 de 11:20 (`salida/E3_Cuanto_nos_equivocamos-480p15.mp4`), 0 avisos, hojas de contacto revisadas. Falta: que el usuario revise el texto ⭐ (paso 9) y vea el mp4 (paso 15); después render final `--calidad qh` (paso 16). Si se quiere bajar de ~11 min, recortar el bloque b3 de la escena 12.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «¿Cuántas veces se equivoca un radar? Una de cada quince, y la cuenta cabe en un papel. Pero hay algo raro: la forma del pulso no entra en ella.»
- ⭐ Escena 13 (cierre): resumen corto, el cabo suelto (cómo se calcula ge en un aparato real) y anuncia E4 por su título, «El filtro que es la señal al revés».
- ⭐ Retoque en la escena 12 (bloque b3): «Con priors iguales» pasa a «Con probabilidades iguales» (sin anglicismo; es lo que ya se dice en las escenas 05 y 06).

Notas:
- El cierre del último episodio anterior (E2, «Toda la señal en un solo número») tiene que anunciar este título, **«¿Cuánto nos equivocamos?»**.
- Reparto de las escenas del guion base: 09 → escenas 03 y 04; 10 → 05 y 06; 11 → 07 y 08; 12 → 09 y 10; 13 → 11 y 12.
  Solo se partieron bloques enteros en escenas atómicas: el texto del guion base no cambia (salvo el retoque de arriba).
- Longitud: ~1.490 palabras del guion base + gancho y cierre ≈ 10,5–11 min. Si `ritmo.py` o el borrador pasan de ~11 min, el candidato a recortarse es el bloque b5 de la escena 12 («más rápido que exponencial», la letra chica).
- Números que vuelven con el **mismo dibujo** que en E2: el pulso `s = (2, 2, 1)`, `σ² = 1`, `E = 9`, el umbral 4,5. Colores: `SENAL` (azul) en la señal y en la campana de H₁, `RUIDO` (magenta) en la campana de H₀, `ERROR` (rojo) en las colas, `ESTIMACION` (ámbar) en el umbral y en los resultados, `VERDE` en detección y aciertos.
- El radar de la escena 07 es el mismo del E1.

---

# Escena 01 — Gancho

**Capítulo YouTube:** Un radar que se equivoca una de cada quince

## Narración

<!-- b1 -->
¿Cuántas veces se equivoca un radar? Una de cada quince, y la cuenta cabe en un papel. Pero hay algo raro: la forma del pulso no entra en ella.

- «¿Cuántas veces se equivoca un radar?» → `radar`: el radar del E1 lanza un pulso; vuelve el eco entre ruido, con «¿avión o ruido?» y un «P_e = ?» en rojo
- «Una de cada quince» → `quince`: quince casillas, una en rojo; al lado «0,0668»
- «la cuenta cabe en un papel» → `papel`: una hoja con seis renglones breves, el último «Q(1,5)»
- «algo raro» → `raro`: un signo de interrogación ámbar sobre la hoja
- «la forma del pulso» → `forma`: entran las tres barras azules del pulso (2, 2, 1)
- «no entra en ella» → `noentra`: las barras se apagan y se tachan en rojo, y la hoja queda sin ellas

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** ¿Cuánto nos equivocamos?

## Narración

<!-- b1 -->
¿Cuánto nos equivocamos?

- «¿Cuánto» → `t1`: «¿Cuánto» entra con rebote
- «nos equivocamos?» → `t2`: «nos equivocamos?» entra debajo, con la etiqueta «Capítulo 13 · Detección de señales»

---

# Escena 03 — ReparteDeGe

**Capítulo YouTube:** Cómo se reparte g con solo ruido

## Narración

<!-- b1 -->
Recuerda de dónde viene ge: es la suma de recibido por señal. Queremos saber cómo se reparte. Empecemos por la hipótesis cero, donde solo hay ruido. Ahí, ge vale dos veces el ruido de la primera muestra, más dos veces el de la segunda, más una vez el de la tercera. Una combinación de campanas independientes.

- «de dónde viene ge» → `ge`: entra «g = Σ r[n] s[n]», con r en cian y s en azul
- «la suma de recibido por señal» → `suma`: la sumatoria se resalta en ámbar; r y s se señalan una a una
- «Queremos saber cómo se reparte» → `reparte`: aparece una campana punteada con «¿cómo se reparte g?»
- «hipótesis cero» → `h0`: casilla «H₀ · solo ruido» en magenta
- «solo hay ruido» → `solo`: las tres barras de r se vuelven magenta: r = W
- «ge vale dos veces el ruido de la primera muestra» → `w0`: se construye «g = 2·W₀» (el 2 azul, W₀ magenta)
- «más dos veces el de la segunda» → `w1`: se suma «+ 2·W₁»
- «más una vez el de la tercera» → `w2`: se suma «+ 1·W₂»
- «Una combinación de campanas independientes» → `comb`: bajo cada término aparece una campanita magenta, con «⟂» entre ellas

<!-- b2 -->
Del capítulo siete: una combinación de gaussianas independientes es otra gaussiana. Solo falta su media y su varianza. La media es cero, porque cada ruido tiene media cero. La varianza: multiplicar una variable por dos multiplica su varianza por cuatro, y las varianzas de variables independientes se suman. Cuatro más cuatro más uno: nueve, por sigma cuadrado.

- «Del capítulo siete» → `cap7`: etiqueta «Capítulo 7» junto a una campana
- «es otra gaussiana» → `gauss`: las tres campanitas se funden en una sola campana grande
- «Solo falta su media y su varianza» → `faltan`: junto a la campana, «media = ?  varianza = ?»
- «La media es cero» → `media`: «0 + 0 + 0 = 0»
- «porque cada ruido tiene media cero» → `cadaruido`: un «0» sobre cada campanita
- «La varianza» → `varianza`: junto a la campana, «varianza = ?» en ámbar
- «multiplicar una variable por dos» → `por2`: una campana W₀ y a su lado «2·W₀», más ancha
- «multiplica su varianza por cuatro» → `por4`: «varianza × 2² = × 4»
- «las varianzas de variables independientes se suman» → `suman`: un «+» entre las tres varianzas, con «⟂» debajo
- «Cuatro más cuatro más uno» → `cuenta`: «4σ² + 4σ² + 1σ²»
- «nueve, por sigma cuadrado» → `nueve`: «= 9 σ²», con el 9 en ámbar

<!-- b3 -->
Con sigma cuadrado igual a uno, la varianza es nueve y el desvío, tres. Fíjate en que nueve es la energía: en general, la varianza de ge es sigma cuadrado por la energía. Así que bajo la hipótesis cero, ge es una campana centrada en cero, con desvío sigma por la raíz de la energía.

- «Con sigma cuadrado igual a uno» → `sigma1`: «σ² = 1»
- «la varianza es nueve» → `var9`: «varianza = 9»
- «el desvío, tres» → `des3`: «desvío = √9 = 3»
- «nueve es la energía» → `energia`: «E = 2² + 2² + 1² = 9», con el 9 resaltado
- «sigma cuadrado por la energía» → `general`: «varianza de g = σ² E»
- «bajo la hipótesis cero» → `bajoh0`: sale una campana magenta sobre un eje horizontal
- «centrada en cero» → `cero`: la campana queda centrada en 0
- «con desvío sigma por la raíz de la energía» → `desvio`: marca de desvío sobre la campana: «σ√E = 3»

---

# Escena 04 — DosCampanas

**Capítulo YouTube:** Dos campanas separadas por la energía

## Narración

<!-- b1 -->
Bajo la hipótesis uno, lo recibido es señal más ruido. Al multiplicar por la señal y sumar, ge vale la suma de los cuadrados de la señal, que es la energía, más lo mismo que antes: la parte del ruido. Es la misma campana, corrida en nueve, con el mismo desvío de tres. Dos campanas iguales, una en cero y otra en nueve.

- «Bajo la hipótesis uno» → `h1`: casilla «H₁ · señal + ruido»
- «lo recibido es señal más ruido» → `recibido`: «r = s + W», con s azul y W magenta
- «Al multiplicar por la señal y sumar» → `mult`: se escribe «g = Σ (s + W) s»
- «la suma de los cuadrados de la señal» → `cuadrados`: «Σ s² = 4 + 4 + 1»
- «que es la energía» → `eneg`: llave «= E = 9» en ámbar
- «la parte del ruido» → `parte`: «+ Σ W s» en magenta, la misma de la hipótesis cero
- «la misma campana, corrida en nueve» → `corrida`: la campana magenta se desliza de 0 a 9 y se tiñe de azul
- «el mismo desvío de tres» → `mismo`: dos flechas de «3» a cada lado de la campana
- «Dos campanas iguales» → `dos`: aparecen las dos campanas juntas
- «una en cero y otra en nueve» → `cerono`: etiquetas «0» y «9» bajo los centros

<!-- b2 -->
Y el umbral, cuatro coma cinco, cae justo en medio. Todo el problema de detección se ha reducido a separar dos campanas del mismo ancho, cuyos centros están a una distancia igual a la energía. Es el problema del capítulo nueve con una medición, solo que ahora la medición es ge. Más energía, más separadas. Más ruido, más anchas.

- «el umbral, cuatro coma cinco» → `umbral`: línea vertical ámbar en 4,5, «γ = 4,5»
- «cae justo en medio» → `medio`: llaves iguales a cada lado del umbral, hasta cada centro
- «Todo el problema de detección» → `todo`: las dos campanas con el rótulo «detección» en ámbar
- «separar dos campanas del mismo ancho» → `separar`: una flecha ámbar entre las dos campanas
- «una distancia igual a la energía» → `distancia`: sobre la flecha, «E = 9»
- «el problema del capítulo nueve» → `cap9`: etiqueta «Capítulo 9» con una sola medición
- «la medición es ge» → `esge`: el rótulo «medición = g» bajo las campanas
- «Más energía, más separadas» → `maseng`: las campanas se alejan (un ValueTracker sobre la separación)
- «Más ruido, más anchas» → `masrui`: las campanas se ensanchan sin moverse

---

# Escena 05 — LaFuncionQ

**Capítulo YouTube:** Las colas de la campana: la función Q

## Narración

<!-- b1 -->
¿Cuánto nos equivocamos? Una falsa alarma ocurre cuando estamos en la campana de la hipótesis cero y ge sale por encima del umbral: es el área de la cola derecha. Un fallo ocurre cuando estamos en la campana de la hipótesis uno y ge sale por debajo: el área de la cola izquierda. Las dos probabilidades son áreas.

- «¿Cuánto nos equivocamos?» → `pregunta`: la pregunta en ámbar sobre las dos campanas con el umbral
- «Una falsa alarma» → `fa`: etiqueta roja «falsa alarma»
- «la campana de la hipótesis cero» → `campcero`: se resalta la campana magenta
- «por encima del umbral» → `encima`: un punto g cae a la derecha de 4,5
- «el área de la cola derecha» → `coladcha`: se sombrea de rojo la cola derecha de la magenta, rotulada «P_FA»
- «Un fallo» → `fallo`: etiqueta roja «fallo (miss)»
- «la campana de la hipótesis uno» → `campuno`: se resalta la campana azul
- «sale por debajo» → `debajo`: un punto g cae a la izquierda de 4,5
- «el área de la cola izquierda» → `colaizq`: se sombrea de rojo la cola izquierda de la azul, rotulada «P_M»
- «Las dos probabilidades son áreas» → `areas`: las dos colas pulsan a la vez

<!-- b2 -->
Para calcularlas hay una herramienta. Cualquier campana se convierte en la campana estándar, de media cero y desvío uno, restando la media y dividiendo entre el desvío. El área de la cola de la campana estándar, a partir de un punto equis, se llama función cu de equis. No tiene fórmula sencilla: se mira en una tabla o se calcula.

- «hay una herramienta» → `herr`: corte; entra la palabra «herramienta» con rebote
- «Cualquier campana» → `cualq`: varias campanas de distinto centro y ancho
- «la campana estándar» → `estandar`: una sola campana, centro 0, desvío 1
- «restando la media» → `resta`: «− media» y una campana se desliza hasta el 0
- «dividiendo entre el desvío» → `divide`: «÷ desvío» y la campana se estrecha a ancho 1
- «El área de la cola» → `cola`: sobre la estándar, se sombrea la cola desde un punto x
- «a partir de un punto equis» → `desde`: un punto x se marca sobre el eje y la cola nace de él
- «función cu de equis» → `q`: entra «Q(x)» sobre la cola
- «No tiene fórmula sencilla» → `nofor`: una integral larga aparece y se tacha con un signo de interrogación
- «se mira en una tabla» → `tabla`: aparece una tabla pequeña de dos columnas
- «o se calcula» → `calc`: un ordenador junto a la tabla

<!-- b3 -->
Algunos valores para ubicarnos. Cu de cero vale un medio: la mitad de la campana. Cu de uno, cero coma dieciséis. Cu de uno coma cinco, cero coma cero seis seis ocho. Cu de tres, menos de dos milésimas. Cuanto más lejos, más pequeña la cola, y cae muy deprisa.

- «Algunos valores» → `valores`: la tabla se llena con las columnas «x» y «Q(x)»
- «Cu de cero vale un medio» → `q0`: fila «Q(0) = 0,5», la mitad de la campana sombreada
- «la mitad de la campana» → `mitad`: la mitad derecha de la campana se destaca
- «Cu de uno, cero coma dieciséis» → `q1`: fila «Q(1) = 0,16», cola sombreada desde 1
- «Cu de uno coma cinco» → `q15`: fila «Q(1,5) = 0,0668» resaltada en ámbar (la que se usa a continuación)
- «cero coma cero seis seis ocho» → `v0668`: la cola desde 1,5 se sombrea, pequeña
- «Cu de tres, menos de dos milésimas» → `q3`: fila «Q(3) = 0,00135»; la cola casi no se ve
- «Cuanto más lejos, más pequeña la cola» → `lejos`: el punto x se desliza a la derecha y la cola se encoge
- «cae muy deprisa» → `deprisa`: una flecha descendente recorre la columna de valores

---

# Escena 06 — ElErrorDelPulso

**Capítulo YouTube:** El error del pulso (2, 2, 1): 6,7 %

## Narración

<!-- b1 -->
Ahora la falsa alarma. El umbral es cuatro coma cinco y la campana está centrada en cero con desvío tres. Estandarizamos: cuatro coma cinco menos cero, entre tres, es uno coma cinco. Falsa alarma igual a cu de uno coma cinco: cero coma cero seis seis ocho. Con el fallo hacemos lo mismo: nueve menos cuatro coma cinco, entre tres, otra vez uno coma cinco.

- «Ahora la falsa alarma» → `fa`: las dos campanas de la escena 04; la cola roja derecha pulsa
- «El umbral es cuatro coma cinco» → `umbral`: marca «γ = 4,5»
- «centrada en cero con desvío tres» → `cent`: sobre la campana magenta, «media 0 · desvío 3»
- «Estandarizamos» → `estand`: la campana se transforma en la estándar y el umbral viaja con ella
- «cuatro coma cinco menos cero» → `resta`: se escribe «(4,5 − 0)»
- «entre tres» → `entre`: se completa «/ 3»
- «es uno coma cinco» → `uno5`: «= 1,5»; la marca del umbral cae en 1,5 de la estándar
- «Falsa alarma igual a cu de uno coma cinco» → `qfa`: «P_FA = Q(1,5)»
- «cero coma cero seis seis ocho» → `val`: «= 0,0668»
- «Con el fallo hacemos lo mismo» → `fallo`: la campana azul con la cola izquierda roja pulsando
- «nueve menos cuatro coma cinco» → `nueve`: se escribe «(9 − 4,5)»
- «otra vez uno coma cinco» → `otra`: «/ 3 = 1,5», con un tilde junto al resultado anterior

<!-- b2 -->
Por la simetría de la campana, las dos colas son iguales. Con probabilidades iguales, nos equivocamos un seis coma siete por ciento: unas siete de cada cien veces. En general, la falsa alarma es cu de gamma entre sigma raíz de e, y el fallo, cu de e menos gamma, entre lo mismo: cuentan los desvíos del umbral a cada centro. Un millón de simulaciones da cero coma cero seis seis siete.

- «Por la simetría de la campana» → `simetria`: una campana se refleja sobre el eje vertical: la cola izquierda pasa a derecha
- «las dos colas son iguales» → `iguales`: un «=» entre las dos colas rojas
- «Con probabilidades iguales» → `priors`: «p₀ = p₁ = ½»
- «un seis coma siete por ciento» → `pe`: «P_e = ½·0,0668 + ½·0,0668 = 6,7 %»
- «unas siete de cada cien veces» → `siete`: una grilla de cien puntos, siete en rojo
- «En general» → `general`: corte; las dos campanas con γ, E y σ√E sin números
- «la falsa alarma es cu de gamma entre sigma raíz de e» → `fgen`: se construye «P_FA = Q(γ / σ√E)» pieza a pieza
- «y el fallo, cu de e menos gamma, entre lo mismo» → `mgen`: se construye «P_M = Q((E − γ) / σ√E)»
- «cuentan los desvíos del umbral a cada centro» → `desv`: flechas desde γ hasta cada centro, medidas en desvíos
- «Un millón de simulaciones» → `sim`: un contador sube hasta «1.000.000 de pruebas»
- «da cero coma cero seis seis siete» → `res`: «0,0667» al lado de «0,0668»

---

# Escena 07 — UmbralMasAlto

**Capítulo YouTube:** Aviones raros: el umbral sube

## Narración

<!-- b1 -->
Volvamos al radar donde los aviones son raros: pe uno igual a cero coma dos. Ya vimos que el umbral sube a cinco coma ocho ocho seis. En las dos campanas, la marca se desplaza hacia la derecha. Veamos qué le pasa a cada error.

- «Volvamos al radar» → `radar`: corte; el radar del E1
- «los aviones son raros» → `raros`: un cielo con un solo avión entre muchos huecos vacíos
- «pe uno igual a cero coma dos» → `p1`: «p₁ = 0,2 · p₀ = 0,8»
- «el umbral sube a cinco coma ocho ocho seis» → `sube`: «γ: 4,5 → 5,886» en ámbar
- «En las dos campanas» → `campanas`: vuelven las dos campanas con la marca todavía en 4,5
- «la marca se desplaza hacia la derecha» → `marca`: vuelven las dos campanas; la marca se desliza de 4,5 a 5,886
- «qué le pasa a cada error» → `cada`: las dos colas rojas rotuladas «P_FA» y «P_M»

<!-- b2 -->
La falsa alarma: cinco coma ocho ocho seis entre tres es uno coma nueve seis dos. Cu de eso vale cero coma cero dos cuatro nueve. Bajó de casi siete por ciento a poco más de dos y medio: con el umbral más alto, es más difícil que el ruido solo lo cruce.

- «La falsa alarma» → `fa`: la cola derecha se resalta
- «cinco coma ocho ocho seis entre tres» → `cuenta`: «5,886 / 3»
- «uno coma nueve seis dos» → `z`: «= 1,962»
- «Cu de eso vale cero coma cero dos cuatro nueve» → `q`: «P_FA = Q(1,962) = 0,0249»
- «cero coma cero dos cuatro nueve» → `v`: «0,0249» se resalta al final de la cuenta
- «Bajó de casi siete por ciento» → `bajo`: queda un fantasma de la cola vieja con «6,7 %» tachado
- «a poco más de dos y medio» → `dosmedio`: «2,5 %» en verde
- «es más difícil que el ruido solo lo cruce» → `dificil`: una traza magenta intenta cruzar la marca y no llega

<!-- b3 -->
El fallo: nueve menos cinco coma ocho ocho seis, entre tres, es uno coma cero tres ocho. Cu de eso vale cero coma uno cuatro nueve siete. Subió a un quince por ciento: ahora la señal, que sí estaba, se queda a veces por debajo. Un detector más conservador: da menos falsas alarmas y pierde más aviones.

- «El fallo» → `fallo`: la cola izquierda de la campana azul se resalta
- «nueve menos cinco coma ocho ocho seis» → `cuenta`: «(9 − 5,886) / 3»
- «uno coma cero tres ocho» → `z`: «= 1,038»
- «Cu de eso vale cero coma uno cuatro nueve siete» → `q`: «P_M = Q(1,038) = 0,1497»
- «cero coma uno cuatro nueve siete» → `v`: «0,1497» se resalta al final de la cuenta
- «Subió a un quince por ciento» → `subio`: la cola izquierda crece y se rotula «15 %» en rojo
- «la señal, que sí estaba» → `estaba`: aparecen puntos azules sobre la campana azul
- «se queda a veces por debajo» → `debajo`: algunos puntos azules caen a la izquierda de la marca
- «Un detector más conservador» → `conserv`: etiqueta «más conservador»
- «da menos falsas alarmas y pierde más aviones» → `pierde`: «falsas alarmas ↓ · misses ↑» con flechas

---

# Escena 08 — ElErrorConPrior

**Capítulo YouTube:** Usar lo que sabíamos rebaja el error

## Narración

<!-- b1 -->
La probabilidad de error es la media ponderada: cero coma ocho por cero coma cero dos cuatro nueve, más cero coma dos por cero coma uno cuatro nueve siete. Cero coma cero uno nueve nueve, más cero coma cero dos nueve nueve: casi cinco por ciento.

- «La probabilidad de error es la media ponderada» → `pe`: se construye «P_e = p₀ P_FA + p₁ P_M» (la de la escena 01 del E1)
- «cero coma ocho por cero coma cero dos cuatro nueve» → `t1`: se sustituye «0,8 · 0,0249»
- «más cero coma dos» → `t2`: se sustituye «+ 0,2 ·»
- «cero coma uno cuatro nueve siete» → `t2b`: se completa «0,1497»
- «Cero coma cero uno nueve nueve» → `r1`: debajo, «= 0,0199»
- «más cero coma cero dos nueve nueve» → `r2`: «+ 0,0299»
- «casi cinco por ciento» → `res`: «P_e = 0,0498 ≈ 5 %» enmarcado en verde

<!-- b2 -->
¿Y si hubiéramos dejado el umbral en cuatro coma cinco? Cada probabilidad seguiría valiendo cero coma cero seis seis ocho, y el error sería seis coma siete por ciento. Peor que el cinco por ciento. Es el mismo detector, calcular ge y compararlo; solo hemos movido la marca, usando lo que sabíamos de antemano. Y rebaja el error.

- «¿Y si hubiéramos dejado el umbral» → `vuelta`: las campanas; la marca empieza a volver de 5,886
- «en cuatro coma cinco» → `c45`: la marca llega a 4,5, «γ = 4,5»
- «Cada probabilidad» → `cada`: las dos colas rojas se resaltan
- «cero coma cero seis seis ocho» → `val`: las dos colas se rotulan «0,0668»
- «el error sería seis coma siete por ciento» → `error`: «0,8 · 0,0668 + 0,2 · 0,0668 = 6,7 %»
- «Peor que el cinco por ciento» → `peor`: «6,7 % > 5 %», el 6,7 en rojo y el 5 en verde
- «Es el mismo detector» → `mismo`: la caja «g ≷ γ» queda igual, sin cambios
- «calcular ge y compararlo» → `calc`: dos pasos en la caja, «calcular g» y «comparar con γ»
- «solo hemos movido la marca» → `movida`: la marca oscila entre 4,5 y 5,886
- «usando lo que sabíamos de antemano» → `antemano`: «p₁ = 0,2» sobre la marca de 5,886
- «Y rebaja el error» → `rebaja`: flecha verde hacia abajo, de «6,7 %» a «5 %»

---

# Escena 09 — SinSaberElPrior

**Capítulo YouTube:** Sin saber cuántos aviones hay: Neyman-Pearson

## Narración

<!-- b1 -->
Hay un problema con lo anterior. Para poner el umbral hacía falta saber la probabilidad de que haya un avión. ¿Y si no la sabemos? En un radar, ¿cuántos aviones vendrán hoy? Del capítulo nueve: criterio de Neyman-Pearson. Se fija cuántas falsas alarmas se toleran, por ejemplo un uno por ciento, y se busca el umbral que detecta más aviones con esa condición.

- «Hay un problema» → `problema`: se tacha «p₁ = 0,2» con un signo de interrogación rojo
- «Para poner el umbral» → `poner`: una marca ámbar se coloca sobre las campanas
- «saber la probabilidad de que haya un avión» → `saber`: el radar, con «p₁ = ?» sobre un cielo vacío
- «¿Y si no la sabemos?» → `nosabemos`: «p₁ = ?» parpadea en rojo
- «En un radar» → `enradar`: el radar con el cielo vacío
- «¿cuántos aviones vendrán hoy?» → `hoy`: el cielo con varios «?» entrando y saliendo
- «Del capítulo nueve» → `cap9`: etiqueta «Capítulo 9»
- «Neyman-Pearson» → `np`: etiqueta «Neyman-Pearson · capítulo 9»
- «cuántas falsas alarmas se toleran» → `toleran`: aparece «P_FA ≤ 1 %»
- «un uno por ciento» → `uno`: sobre las campanas, una cola roja diminuta
- «detecta más aviones» → `detecta`: se resalta de verde el área bajo la campana azul a la derecha del umbral

<!-- b2 -->
Buscamos el umbral que deja un uno por ciento de cola en la campana de la hipótesis cero. Necesitamos la operación inversa de cu: dado un área, qué punto la deja. Para un uno por ciento, ese punto es dos coma tres tres desvíos. Así que el umbral vale tres por dos coma tres tres: seis coma nueve ocho.

- «el umbral que deja un uno por ciento de cola» → `busca`: una marca ámbar recorre la campana magenta hasta dejar una cola del 1 %
- «en la campana de la hipótesis cero» → `encero`: se resalta la campana magenta
- «la operación inversa de cu» → `inversa`: entra «Q⁻¹», con una flecha de vuelta sobre «Q»
- «dado un área, qué punto la deja» → `area`: flecha desde «área 0,01» hasta «punto x» sobre la campana estándar
- «Para un uno por ciento» → `para1`: «1 %» marcado en la cola de la campana estándar
- «dos coma tres tres desvíos» → `z233`: «Q⁻¹(0,01) = 2,33», con la cola de 1 % sombreada
- «tres por dos coma tres tres» → `prod`: «γ = 3 · 2,33»
- «seis coma nueve ocho» → `gam`: «= 6,98», y la marca se fija en 6,98 en las dos campanas

<!-- b3 -->
Ahora, ¿cuántos aviones detectamos con ese umbral? Es el área a la derecha de seis coma nueve ocho en la campana centrada en nueve. Estandarizamos: seis coma nueve ocho menos nueve, entre tres, es menos cero coma seis siete. El área a la derecha es cero coma siete cinco. Detectamos tres de cada cuatro aviones, con solo un uno por ciento de falsas alarmas.

- «¿cuántos aviones detectamos con ese umbral?» → `cuantos`: la pregunta «P_D = ?» en verde
- «el área a la derecha de seis coma nueve ocho» → `areader`: se sombrea de verde el área a la derecha de 6,98 bajo la campana azul
- «la campana centrada en nueve» → `en9`: la campana azul se resalta, con «media 9 · desvío 3»
- «seis coma nueve ocho menos nueve, entre tres» → `estand`: «(6,98 − 9) / 3»
- «menos cero coma seis siete» → `z`: «= −0,67»
- «cero coma siete cinco» → `pd`: «P_D = Q(−0,67) = 0,75», en verde
- «tres de cada cuatro aviones» → `tres4`: cuatro avioncitos, tres en verde y uno en rojo
- «un uno por ciento de falsas alarmas» → `uno`: «P_FA = 1 %» junto a «P_D = 75 %»

---

# Escena 10 — CurvaRoc

**Capítulo YouTube:** La curva ROC

## Narración

<!-- b1 -->
Ahora desliza el umbral de derecha a izquierda. Cada posición es un punto: falsa alarma en un eje, detección en el otro. Con el umbral muy a la derecha, no detectamos nada; con el umbral muy a la izquierda, lo detectamos todo, con todas las falsas alarmas. Los puntos dibujan una curva: la curva ROC. Cuanto más cerca de la esquina de arriba a la izquierda, mejor.

- «desliza el umbral de derecha a izquierda» → `desliza`: las campanas con la marca barriendo de derecha a izquierda (un ValueTracker), colas rojas y verdes que cambian
- «Cada posición es un punto» → `punto`: a la derecha aparece un plano cuadrado con un punto que sigue a la marca
- «falsa alarma en un eje» → `ejex`: se rotula el eje horizontal «P_FA»
- «detección en el otro» → `ejey`: se rotula el eje vertical «P_D»
- «muy a la derecha, no detectamos nada» → `nada`: el punto en (0, 0)
- «muy a la izquierda» → `izq`: la marca llega a la izquierda de las dos campanas
- «lo detectamos todo» → `todo`: el punto en (1, 1)
- «con todas las falsas alarmas» → `todas`: el 1 del eje horizontal se marca en rojo
- «Los puntos dibujan una curva» → `curva`: los puntos que quedaron en el plano forman una curva
- «la curva ROC» → `roc`: queda trazada la curva y entra la etiqueta «curva ROC»
- «la esquina de arriba a la izquierda» → `esquina`: la esquina (0, 1) se marca en verde y la diagonal punteada se rotula «azar»
- «mejor» → `mejor`: un tilde verde sobre la esquina

<!-- b2 -->
Y esta curva depende de un solo número: la distancia entre las dos campanas medida en desvíos, la raíz de la energía entre sigma. Aquí, tres. Con un valor mayor, la curva se pega a la esquina. La detección vale cu de la inversa de cu de la falsa alarma, menos ese número. Para detectar más sin más falsas alarmas, hay que subir la energía o bajar el ruido.

- «depende de un solo número» → `solo`: junto a la curva aparece una «d» ámbar grande
- «la distancia entre las dos campanas medida en desvíos» → `dist`: las dos campanas con una flecha entre sus centros medida en desvíos
- «la raíz de la energía entre sigma» → `d`: se construye «d = √E / σ»
- «Aquí, tres» → `tres`: «d = 3» y la curva actual se resalta
- «Con un valor mayor, la curva se pega a la esquina» → `mayor`: aparecen las curvas d = 1 (cerca de la diagonal) y d = 5 (pegada a la esquina)
- «La detección vale cu de la inversa de cu de la falsa alarma» → `form`: se construye «P_D = Q(Q⁻¹(P_FA) − d)» por piezas
- «menos ese número» → `menos`: el «− d» se resalta en ámbar
- «Para detectar más» → `detectar`: «P_D ↑» en verde
- «subir la energía» → `subir`: «E ↑» y la curva se acerca a la esquina
- «bajar el ruido» → `bajar`: «σ² ↓» y la curva se acerca otra vez

---

# Escena 11 — DestelloOPulso

**Capítulo YouTube:** Un pulso largo o un destello: ¿cuál se detecta mejor?

## Narración

<!-- b1 -->
Fíjate en algo curioso: en todas las fórmulas solo aparecen la energía y la varianza del ruido. Ninguna muestra concreta de la señal. Pregunta, y piénsala un momento: tenemos el pulso dos, dos, uno, y otro pulso que es un solo destello de tres en una muestra y ceros en las demás. Los dos tienen energía nueve. ¿Cuál se detecta mejor?

- «en todas las fórmulas» → `formulas`: en fila, «P_FA = Q(γ / σ√E)», «P_M = Q((E − γ) / σ√E)» y «P_D = Q(Q⁻¹(P_FA) − d)»
- «la energía y la varianza del ruido» → `solo`: en las tres fórmulas, E se tiñe de ámbar y σ² de magenta
- «Ninguna muestra concreta de la señal» → `ninguna`: «s[0], s[1], s[2]» se buscan en las fórmulas y no están
- «Pregunta, y piénsala un momento» → `piensa`: un reloj de pausa y las fórmulas se atenúan
- «el pulso dos, dos, uno» → `pulso1`: a la izquierda, las tres barras azules (2, 2, 1)
- «un solo destello de tres en una muestra» → `destello`: a la derecha, una barra azul de altura 3
- «y ceros en las demás» → `ceros`: dos «0» sobre las otras dos muestras
- «energía nueve» → `nueve`: «E = 9» bajo cada uno, con el 9 en ámbar
- «¿Cuál se detecta mejor?» → `cual`: «¿cuál?» en ámbar entre los dos pulsos

<!-- b2 -->
Hagamos la cuenta del destello. Ge es tres por lo recibido en la primera muestra. Bajo la hipótesis cero, media cero y desvío tres. Bajo la hipótesis uno, media nueve y desvío tres. Son las mismas dos campanas, el mismo umbral, el mismo error: cero coma cero seis seis ocho. Da igual. Un pulso extendido y un destello dan el mismo error.

- «la cuenta del destello» → `cuenta`: se escribe «g = 3 r[0] + 0 r[1] + 0 r[2]»
- «Ge es tres por» → `ge`: los términos con cero se apagan y queda «g = 3 · r[0]»
- «lo recibido en la primera muestra» → `primera`: se resalta r[0] en cian
- «Bajo la hipótesis cero» → `bajoh0`: casilla «H₀ · solo ruido»
- «media cero y desvío tres» → `h0`: campana magenta en 0, desvío 3
- «Bajo la hipótesis uno» → `bajoh1`: casilla «H₁ · señal + ruido»
- «media nueve y desvío tres» → `h1`: campana azul en 9, desvío 3
- «las mismas dos campanas» → `mismas`: sobre ellas se superponen, en fantasma, las campanas del pulso (2, 2, 1): coinciden
- «el mismo umbral» → `umbral`: marca ámbar en 4,5
- «el mismo error: cero coma cero seis seis ocho» → `error`: «P_e = 0,0668» bajo el destello y bajo el pulso (2, 2, 1)
- «Da igual» → `daigual`: un «=» ámbar entre los dos pulsos
- «Un pulso extendido y un destello» → `extend`: los dos pulsos otra vez, cada uno con «P_e = 0,0668» en verde
- «dan el mismo error» → `final`: un tilde verde sobre «P_e = 0,0668»

---

# Escena 12 — SoloLaEnergia

**Capítulo YouTube:** Solo cuenta la energía (con ruido blanco)

## Narración

<!-- b1 -->
Es el resultado central. Con ruido blanco, el error depende solo de un cociente: la energía de la señal entre la varianza del ruido, que llamamos relación señal-ruido. Con probabilidades iguales, la probabilidad de error es cu de la raíz de la energía entre dos sigma. La forma de la señal no importa. Guarda esto: es verdad con ruido blanco. Más adelante lo vamos a matizar.

- «Es el resultado central» → `central`: la frase «resultado central» en un marco ámbar
- «Con ruido blanco» → `blanco`: etiqueta «ruido blanco» en magenta
- «depende solo de un cociente» → `cociente`: entra una fracción «E / σ²», aún sin rellenar
- «la energía de la señal» → `e`: el numerador E se tiñe de azul
- «la varianza del ruido» → `s2`: el denominador σ² se tiñe de magenta
- «relación señal-ruido» → `snr`: la fracción se rotula «relación señal-ruido», sobre una barra que se llena
- «Con probabilidades iguales» → `iguales`: «p₀ = p₁»
- «la probabilidad de error es cu de» → `pe`: entra «P_e = Q(»
- «la raíz de la energía entre dos sigma» → `raiz`: se completa «√E / 2σ )» pieza a pieza
- «La forma de la señal no importa» → `forma`: los pulsos (2, 2, 1) y (3, 0, 0) con un «=» en medio
- «Guarda esto» → `guarda`: una chincheta ámbar sobre la fórmula
- «con ruido blanco» → `blanco2`: la etiqueta «ruido blanco» parpadea
- «Más adelante lo vamos a matizar» → `matizar`: aparece un «?» pequeño junto a la chincheta

<!-- b2 -->
¿Cuánto mejora el error con más energía? Duplicamos la energía, de nueve a dieciocho. La raíz de dieciocho entre dos es dos coma doce, y cu de dos coma doce vale cero coma cero uno siete. Con el doble de energía, el error pasa de casi siete de cada cien a menos de dos de cada cien.

- «¿Cuánto mejora el error con más energía?» → `pregunta`: la pregunta en ámbar sobre la fórmula
- «Duplicamos la energía, de nueve a dieciocho» → `dup`: «E: 9 → 18»; la barra de relación señal-ruido se duplica
- «La raíz de dieciocho entre dos» → `raiz`: se escribe «√18 / 2»
- «es dos coma doce» → `z`: «= 2,12»
- «cu de dos coma doce vale cero coma cero uno siete» → `q`: «Q(2,12) = 0,017»
- «cero coma cero uno siete» → `v`: «0,017» se resalta en verde
- «Con el doble de energía» → `doble`: la barra duplicada y «E = 18»
- «casi siete de cada cien» → `siete`: cien puntos con siete en rojo
- «menos de dos de cada cien» → `dos`: los cien puntos pasan a tener solo dos en rojo, con una flecha verde de bajada

<!-- b3 -->
Se suele decir que el error cae más rápido que una exponencial, y tiene letra chica. Como función de la raíz de la energía entre sigma, cu cae como una campana, más deprisa que cualquier exponencial. Como función de la relación señal-ruido, la energía entre la varianza, cae esencialmente como una exponencial. Son dos formas de mirar la misma curva.

- «más rápido que una exponencial» → `rapido`: «¿más rápido que una exponencial?» en ámbar
- «tiene letra chica» → `letra`: una lupa sobre un asterisco de letra pequeña
- «la raíz de la energía entre sigma» → `eje1`: unos ejes con el eje horizontal «√E / σ»
- «cu cae como una campana» → `campana`: la curva Q cae como la cola de una campana
- «más deprisa que cualquier exponencial» → `deprisa`: una exponencial punteada queda por encima de la curva
- «Como función de la relación señal-ruido» → `eje2`: se cambia el eje horizontal
- «la energía entre la varianza» → `ev`: el eje se rotula «E / σ²»
- «cae esencialmente como una exponencial» → `expo`: la curva se pega a la exponencial punteada
- «dos formas de mirar la misma curva» → `misma`: las dos vistas se superponen y se rotula «la misma curva»

---

# Escena 13 — Cierre

**Capítulo YouTube:** Y ahora, ¿cómo se calcula g?

## Narración

<!-- b1 -->
Resumamos. Con ruido blanco, detectar es separar dos campanas, una en cero y otra en la energía, y el error es el área de dos colas. Con un umbral que usa lo que sabemos, o con la curva ROC cuando no lo sabemos. Y solo cuenta la energía entre el ruido, no la forma.

- «separar dos campanas» → `campanas`: las dos campanas vuelven al centro, la magenta en 0 y la azul en 9
- «una en cero y otra en la energía» → `centros`: etiquetas «0» y «E» bajo los centros
- «el área de dos colas» → `colas`: las dos colas rojas se sombrean
- «Con un umbral que usa lo que sabemos» → `umbral`: la marca ámbar se coloca en 5,886
- «la curva ROC» → `roc`: la curva ROC de la escena 10 aparece en una esquina
- «solo cuenta la energía entre el ruido» → `energia`: «E / σ²» en grande, en ámbar
- «no la forma» → `forma`: los pulsos (2, 2, 1) y (3, 0, 0) con un «=»

<!-- b2 -->
Pero queda un cabo suelto: ge se calcula con multiplicaciones y una suma, y un aparato real recibe la señal muestra a muestra. ¿Cómo lo hace? Con un filtro que es la señal puesta al revés. Es el siguiente episodio: «El filtro que es la señal al revés».

- «un cabo suelto» → `cabo`: «g = Σ r[n] s[n]» con un hilo suelto ámbar
- «multiplicaciones y una suma» → `suma`: las tres multiplicaciones y la suma se resaltan una a una
- «y un aparato real» → `aparato`: una caja, el aparato, entra a la derecha
- «muestra a muestra» → `muestra`: la señal r desfila de a una muestra hacia un aparato (una caja)
- «¿Cómo lo hace?» → `como`: un signo de interrogación ámbar sobre la caja
- «un filtro que es la señal puesta al revés» → `filtro`: la caja se rotula «filtro» con las barras (1, 2, 2), la señal (2, 2, 1) invertida
- «Es el siguiente episodio» → `siguiente`: la caja se aparta y asoma «E4»
- «El filtro que es la señal al revés» → `titulo`: el título del episodio siguiente entra con rebote
