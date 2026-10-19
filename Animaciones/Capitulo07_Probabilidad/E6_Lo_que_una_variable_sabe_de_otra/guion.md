# Episodio 6 — Lo que una variable sabe de otra

Capítulo 7 (Modelos probabilísticos), episodio 6 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 21 a 24), más un gancho y un cierre nuevos.
Ejemplos que vuelven con el mismo dibujo: el canal que confunde bits (tabla 0,63 · 0,07 · 0,03 · 0,27; E[S] = 0,3, E[R] = 0,34) y el ejemplo 6, 4, 3 (el que se retoma en el E7). Paga la promesa de «las varianzas se suman» de la escena 16 (E4).

**Estado:** **Subido a YouTube y publicado** (subido el 17/10/2026, público desde el 19/10): render final 1080p60 de 8:53, con título, descripción con `capitulos.txt`, subtítulos `.srt`, categoría Educación y «no es para niños» (https://youtu.be/MAd5jyBUiaM). Residuos limpiados el 17/10/2026; se rehace con `python rehacer.py Capitulo07_Probabilidad`. La caché de voz versionada (`media/voiceovers/`) se volvió a sintetizar después de la subida: un render nuevo es reproducible, pero la voz puede diferir un poco de la del vídeo subido.

Texto nuevo (marcado con ⭐, aprobado por el usuario):
- ⭐ Escena 01 (gancho): «Toma dos variables en las que una es exactamente el cuadrado de la otra… ¿Cómo puede ser?» (adelanta el contraejemplo de la escena 11).
- ⭐ Escena 18 (cierre): resume correlación, covarianza y su límite, recuerda la fórmula de dos cuadrados y un término cruzado y anuncia E7, «Variables que son flechas».
- ⭐ Retoque en la escena 17 (bloque b5): se quitó la última frase del guion base («Para verlo hay que dejar de pensar en las variables como números…»), que ahora vive en el cierre.
- Retoque menor en la escena 13 (bloque b4): las comillas de «no correlacionadas» e «independientes» pasan a comillas angulares.

---

# Escena 01 — Gancho

**Capítulo YouTube:** Dependencia total, covarianza cero

## Narración

<!-- b1 -->
Toma dos variables en las que una es exactamente el cuadrado de la otra. Dependencia total. Y aun así, su covarianza vale cero. ¿Cómo puede ser?

- «una es exactamente el cuadrado de la otra» → `cuadrado`: aparece «Y = X²» y una parábola perfecta se dibuja con puntos azules
- «Dependencia total» → `dep`: sello «dependencia total» sobre la parábola
- «su covarianza vale cero» → `cero`: aparece «σ_XY = 0» en ámbar junto al sello
- «¿Cómo puede ser?» → `pregunta`: un interrogante grande crece sobre la parábola

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Lo que una variable sabe de otra

## Narración

<!-- b1 -->
Lo que una variable sabe de otra.

- «Lo que una variable» → `t1`: «Lo que una variable» entra con rebote
- «sabe de otra» → `t2`: «sabe de otra» entra debajo, con la etiqueta «Capítulo 7 · Modelos probabilísticos»

---

# Escena 03 — ProductoDeVariables

**Capítulo YouTube:** La correlación: multiplicar y promediar

## Narración

<!-- b1 -->
¿Cómo medimos si dos variables tienden a moverse juntas? Una idea sencilla: multiplicar equis por i griega en cada caso y promediar. Si cuando una es grande la otra también lo es, los productos serán grandes, y el promedio también. Esa esperanza del producto se llama correlación.

- «¿Cómo medimos» → `pregunta`: la nube inclinada de lo enviado contra lo recibido, con el rótulo «¿se mueven juntas?»
- «tienden a moverse juntas» → `juntas`: una recta de ajuste cruza la nube
- «Una idea sencilla» → `idea`: la pregunta «¿se mueven juntas?» late
- «multiplicar equis por i griega» → `producto`: sobre un punto de la nube aparece «x · y» con sus valores sustituidos
- «en cada caso» → `cada_caso`: otros tres puntos muestran su producto, cada uno con su número
- «y promediar» → `promediar`: los productos se reúnen en una barra que dice «promedio»
- «cuando una es grande» → `grande`: dos puntos arriba a la derecha se iluminan con productos grandes
- «los productos serán grandes» → `prod_grandes`: los números de esos puntos crecen
- «el promedio también» → `prom_grande`: la barra del promedio sube
- «Esa esperanza del producto» → `esperanza`: se construye «E[XY]» pieza a pieza
- «correlación» → `correlacion`: «correlación» entra con rebote y la fórmula queda como «r_XY = E[XY]»

---

# Escena 04 — CorrelacionDelCanal

**Capítulo YouTube:** Correlación del canal

## Narración

<!-- b1 -->
Calculémosla con el canal. Hay que multiplicar lo enviado por lo recibido en cada casilla, y pesarlo con su probabilidad. Pero si alguno de los dos es cero, el producto es cero. Así que solo cuenta la casilla en la que se envió un uno y se recibió un uno: uno por uno por cero coma veintisiete. La correlación es cero coma veintisiete.

- «Calculémosla con el canal» → `tabla`: aparece la tabla del canal con 0,63 · 0,07 · 0,03 · 0,27
- «multiplicar lo enviado por lo recibido» → `mult`: en cada casilla se escribe el producto s · r (0, 0, 0, 1)
- «en cada casilla» → `casillas`: un destello recorre las cuatro casillas
- «pesarlo con su probabilidad» → `pesar`: cada producto se multiplica por la probabilidad de su casilla
- «si alguno de los dos es cero» → `cero`: tres casillas se apagan con un «0» en la fila o columna del cero
- «el producto es cero» → `prod_cero`: en esas casillas queda «× 0 = 0»
- «solo cuenta la casilla» → `cuenta`: la casilla de abajo a la derecha se resalta
- «se envió un uno y se recibió un uno» → `uno_uno`: se marcan «S = 1» y «R = 1» en los bordes de la tabla
- «uno por uno por cero coma veintisiete» → `cuenta_f`: se escribe «1 · 1 · 0,27»
- «La correlación es cero coma veintisiete» → `resultado`: queda «E[SR] = 0,27» en ámbar

---

# Escena 05 — LaTrampaDelProducto

**Capítulo YouTube:** La esperanza del producto no es el producto de las esperanzas

## Narración

<!-- b1 -->
Ahora, atención a una trampa. La esperanza del producto no es el producto de las esperanzas. La media de lo enviado es cero coma tres, y la de lo recibido, cero coma treinta y cuatro. Su producto es cero coma uno cero dos. Y la correlación es cero coma veintisiete: bastante más.

- «atención a una trampa» → `trampa`: cartel de aviso con un triángulo
- «La esperanza del producto» → `e_prod`: a la izquierda aparece «E[SR]»
- «no es el producto de las esperanzas» → `prod_e`: a la derecha aparece «E[S] · E[R]» y entre ambos un «≠» rojo
- «de las esperanzas» → `esper`: se resalta «E[S] · E[R]»
- «La media de lo enviado» → `media_env`: el rótulo «lo enviado» bajo la media de S
- «cero coma tres» → `m_s`: «E[S] = 0,3»
- «la de lo recibido» → `media_rec`: el rótulo «lo recibido» bajo la media de R
- «cero coma treinta y cuatro» → `m_r`: «E[R] = 0,34»
- «cero coma uno cero dos» → `p_med`: «0,3 · 0,34 = 0,102»
- «cero coma veintisiete» → `corr27`: «E[SR] = 0,27» junto al 0,102
- «bastante más» → `mas`: dos barras, la de 0,27 mucho más larga que la de 0,102

<!-- b2 -->
Esa diferencia no es un error: es la información que buscamos. El producto de las medias es lo que saldría si las dos variables fueran por libre. Si la correlación es mayor, es porque cuando se envía un uno suele recibirse un uno: las variables se mueven juntas más de lo que harían por casualidad.

- «Esa diferencia» → `dif`: el hueco entre las dos barras se marca con una llave
- «no es un error» → `no_error`: un tilde verde junto al hueco
- «es la información que buscamos» → `info`: el hueco se pinta de ámbar con el rótulo «información»
- «El producto de las medias» → `medias`: la barra corta se resalta
- «por libre» → `libre`: dos puntos se mueven cada uno por su lado, sin relación
- «Si la correlación es mayor» → `mayor`: se resalta la barra larga
- «cuando se envía un uno» → `envia1`: en la tabla se marca «S = 1»
- «suele recibirse un uno» → `recibe1`: una flecha lleva a «R = 1» y la casilla del 0,27 se agranda
- «más de lo que harían por casualidad» → `casualidad`: las dos barras con la diferencia rotulada

---

# Escena 06 — CorrelacionContinua

**Capítulo YouTube:** Correlación de variables continuas

## Narración

<!-- b1 -->
Para variables continuas la idea es la misma: se multiplica equis por i griega, se pesa con la densidad conjunta y se suma sobre todo el plano, con una integral doble. Y esa diferencia entre la correlación y el producto de las medias es tan importante que tiene nombre propio.

- «variables continuas» → `continuas`: la tabla se funde en una nube continua sombreada, como la de la escena 18
- «se multiplica equis por i griega» → `xy`: aparece «x · y»
- «se pesa con la densidad conjunta» → `peso`: se suma «f_XY(x, y)»
- «se suma sobre todo el plano» → `plano`: un barrido cubre todo el plano
- «con una integral doble» → `integral`: se completa «r_XY = ∬ x y f_XY(x, y) dx dy», pieza a pieza
- «esa diferencia» → `dif2`: debajo aparece «E[XY] − E[X] E[Y]»
- «la correlación» → `la_corr`: se resalta «E[XY]»
- «el producto de las medias» → `las_medias`: se resalta «E[X] E[Y]»
- «nombre propio» → `nombre`: un interrogante sobre la diferencia, «¿cómo se llama?»

---

# Escena 07 — LosCuatroCuadrantes

**Capítulo YouTube:** Cuadrantes y signo del producto

## Narración

<!-- b1 -->
Movamos el origen al centro de la nube, para esto le restamos la media a cada variable. Ahora el plano queda dividido en cuatro cuadrantes. Arriba a la derecha y abajo a la izquierda, el producto es positivo. En los otros dos, negativo. Si la nube sube hacia la derecha, ganan los positivos. Si baja, ganan los negativos. Si es redonda, se compensan.

- «Movamos el origen» → `origen`: los ejes se desplazan hasta el centro de masa de la nube
- «le restamos la media» → `restar`: sobre los ejes aparecen «X − μ_X» y «Y − μ_Y»
- «a cada variable» → `su_media`: un punto ámbar marca el centro de masa
- «Ahora el plano» → `ahora`: los dos ejes nuevos laten
- «cuatro cuadrantes» → `cuadrantes`: el plano queda dividido en cuatro
- «Arriba a la derecha» → `ard`: ese cuadrante se pinta de verde con «+ · + = +»
- «abajo a la izquierda» → `abi`: también verde, con «− · − = +»
- «el producto es positivo» → `positivo`: los dos cuadrantes verdes laten
- «En los otros dos» → `otros_dos`: los dos cuadrantes rojos laten
- «negativo» → `neg`: los otros dos se pintan de rojo con «+ · − = −»
- «Si la nube sube hacia la derecha» → `sube`: la nube se inclina hacia arriba y casi todos los puntos caen en los verdes
- «ganan los positivos» → `gana_pos`: aparece un «+» grande verde
- «Si baja» → `baja`: la nube se inclina hacia abajo, con casi todos los puntos en los rojos
- «ganan los negativos» → `gana_neg`: aparece un «−» grande rojo
- «Si es redonda» → `redonda`: la nube se vuelve redonda, repartida en los cuatro
- «se compensan» → `compensan`: verdes y rojos se equilibran y aparece «0»

---

# Escena 08 — FormulaDeLaCovarianza

**Capítulo YouTube:** La covarianza y su fórmula práctica

## Narración

<!-- b1 -->
La esperanza de ese producto, medido desde el centro, es la covarianza. Y con la misma cuenta que hicimos para la varianza, desarrollando el producto y usando la linealidad, sale la fórmula práctica: la covarianza es la correlación menos el producto de las medias. Justo la diferencia que vimos antes. De hecho, la varianza es la covarianza de una variable consigo misma.

- «La esperanza de ese producto» → `esp`: se construye «E[(X − μ_X)(Y − μ_Y)]» por piezas
- «medido desde el centro» → `centro`: se resaltan los dos restos de media
- «es la covarianza» → `cov`: a la izquierda entra «σ_XY =» con rebote
- «la misma cuenta que hicimos para la varianza» → `misma`: un rótulo «como con la varianza»
- «desarrollando el producto» → `desarrollo`: segundo renglón con los cuatro términos del producto desarrollado
- «usando la linealidad» → `lineal`: la esperanza entra en cada término y se agrupan los semejantes
- «la fórmula práctica» → `practica`: queda «σ_XY = E[XY] − μ_X μ_Y» en un recuadro
- «la correlación menos el producto de las medias» → `lectura`: se colorean «E[XY]» (la correlación) y «μ_X μ_Y» (las medias)
- «la diferencia que vimos antes» → `antes`: reaparece el hueco entre las dos barras de la escena 05
- «la varianza es la covarianza de una variable consigo misma» → `var_cov`: aparece «σ_XX = σ_X²»
- «consigo misma» → `consigo`: se resalta «σ_X²»

---

# Escena 09 — CovarianzaDelCanal

**Capítulo YouTube:** Covarianza del canal

## Narración

<!-- b1 -->
Para el canal: cero coma veintisiete menos cero coma uno cero dos. La covarianza entre lo enviado y lo recibido es cero coma uno seis ocho. Es positiva, como tenía que ser: lo enviado y lo recibido tienden a ir en la misma dirección.

- «Para el canal» → `canal`: vuelve la tabla del canal, pequeña, a un lado
- «cero coma veintisiete» → `c27`: «0,27»
- «menos cero coma uno cero dos» → `c102`: «− 0,102»
- «La covarianza entre lo enviado» → `cov_ent`: se resalta «S = 1»
- «lo recibido» → `lo_rec`: se resalta «R = 1»
- «cero coma uno seis ocho» → `c168`: «σ_SR = 0,168» en ámbar
- «Es positiva» → `positiva`: un «+» verde junto al resultado
- «como tenía que ser» → `como`: la nube inclinada hacia arriba
- «tienden a ir en la misma dirección» → `misma_dir`: dos flechas paralelas, enviado y recibido, hacia arriba

---

# Escena 10 — IndependienteEsCero

**Capítulo YouTube:** Independientes implica covarianza cero

## Narración

<!-- b1 -->
¿Y si las variables son independientes? Entonces la probabilidad de cada pareja es el producto de las probabilidades de cada una. Y al calcular la esperanza del producto, la suma se separa en dos: la esperanza de equis por la de i griega. La correlación es exactamente el producto de las medias, y la covarianza da cero.

- «¿Y si las variables son independientes?» → `indep`: aparece la tabla con el rótulo «independientes»
- «la probabilidad de cada pareja» → `pareja`: «P(x, y)»
- «el producto de las probabilidades de cada una» → `prod_p`: se completa «P(x, y) = P(x) · P(y)»
- «Y al calcular» → `al_calc`: se resalta «P(x, y) = P(x) P(y)»
- «la esperanza del producto» → `e_prod2`: se escribe «E[XY] = Σ Σ x y P(x) P(y)»
- «la suma se separa en dos» → `separa`: la suma doble se parte en dos sumas, una de x y otra de y
- «la esperanza de equis por la de i griega» → `ex_ey`: queda «E[X] · E[Y]»
- «La correlación» → `la_corr`: se resalta «E[XY]»
- «el producto de las medias» → `medias2`: «r_XY = μ_X μ_Y»
- «la covarianza da cero» → `cero_cov`: «σ_XY = 0» en ámbar

<!-- b2 -->
Independientes, entonces, significa covarianza cero. Es tentador leerlo al revés: si la covarianza es cero, serán independientes. Parece lógico, y es uno de los errores más comunes de toda la estadística. Vamos a ver por qué.

- «Independientes, entonces» → `ind_cero`: «independientes ⇒ σ_XY = 0»
- «significa covarianza cero» → `signif`: se resalta «σ_XY = 0»
- «leerlo al revés» → `reves`: la flecha se invierte y aparece «⇐ ?»
- «si la covarianza es cero» → `si_cero`: se resalta «σ_XY = 0» de abajo
- «serán independientes» → `seran`: se resalta «independientes» de abajo
- «Parece lógico» → `logico`: la flecha inversa queda con un tilde dudoso
- «uno de los errores más comunes» → `error`: la flecha inversa se tacha en rojo
- «Vamos a ver por qué» → `por_que`: un interrogante grande

---

# Escena 11 — ParabolaPerfecta

**Capítulo YouTube:** Un contraejemplo: la parábola

## Narración

<!-- b1 -->
Toma una variable equis uniforme entre menos uno y uno, y define i griega como equis al cuadrado. Estas dos variables son todo lo dependientes que pueden ser: si te digo que equis vale cero coma siete, sabes sin ninguna duda que i griega vale cero coma cuarenta y nueve. La nube ni siquiera es una nube: es una parábola perfecta.

- «equis uniforme entre menos uno y uno» → `uniforme`: un rectángulo de densidad uniforme sobre el intervalo de −1 a 1
- «define i griega como equis al cuadrado» → `def_y`: aparece «Y = X²»
- «Estas dos variables» → `estas`: se resalta «Y = X²»
- «todo lo dependientes que pueden ser» → `dep`: sello «totalmente dependientes»
- «equis vale cero coma siete» → `x07`: una línea vertical en x = 0,7
- «sabes sin ninguna duda» → `sin_duda`: un punto sube desde el eje hasta la curva
- «cero coma cuarenta y nueve» → `y049`: el punto queda rotulado «0,49»
- «La nube ni siquiera es una nube» → `no_nube`: aparecen muchos puntos (x, x²)
- «una parábola perfecta» → `parabola`: se traza la curva completa sobre los puntos

---

# Escena 12 — CuentaDeLaParabola

**Capítulo YouTube:** La covarianza de la parábola

## Narración

<!-- b1 -->
Calculemos su covarianza. La media de equis es cero, porque la uniforme es simétrica alrededor de cero. Así que la covarianza es simplemente la esperanza de equis por i griega, que es la esperanza de equis al cubo. Y equis al cubo es negativo a la izquierda y positivo a la derecha, en la misma medida. Su media es cero. La covarianza es cero.

- «Calculemos su covarianza» → `calc`: aparece «σ_XY = E[XY] − μ_X μ_Y»
- «La media de equis es cero» → `mu0`: «μ_X = 0» y la fórmula pierde el último término
- «simétrica alrededor de cero» → `simetria`: línea de espejo vertical en x = 0 sobre el rectángulo uniforme
- «la covarianza es simplemente la esperanza de equis por i griega» → `exy`: la fórmula se reduce a «σ_XY = E[XY]»
- «la esperanza de equis al cubo» → `cubo`: «E[XY] = E[X · X²] = E[X³]»
- «negativo a la izquierda» → `izq`: curva x³ con la parte izquierda en rojo
- «positivo a la derecha» → `der`: la parte derecha en verde
- «en la misma medida» → `medida`: las dos áreas se marcan iguales
- «Su media es cero» → `media0`: «E[X³] = 0»
- «La covarianza es cero» → `cov0`: «σ_XY = 0» en ámbar

---

# Escena 13 — SoloLoLineal

**Capítulo YouTube:** La covarianza solo ve lo lineal

## Narración

<!-- b1 -->
Dependencia total, y covarianza cero. ¿Cómo puede ser? Mira la parábola. En la mitad izquierda, cuando equis sube, i griega baja. En la mitad derecha, cuando equis sube, i griega sube. La covarianza solo pregunta si, en conjunto, suben o bajan juntas. Y las dos mitades se cancelan: no hay una tendencia en línea recta.

- «Dependencia total» → `dep_total`: vuelve el sello «dependencia total»
- «covarianza cero» → `cov_cero`: «σ_XY = 0» al lado
- «¿Cómo puede ser?» → `como`: un interrogante
- «Mira la parábola» → `mira`: la parábola de la escena 11 ocupa la pantalla
- «En la mitad izquierda» → `mitad_izq`: la mitad izquierda se resalta con una flecha descendente
- «i griega baja» → `baja_y`: la flecha es roja
- «En la mitad derecha» → `mitad_der`: se resalta la mitad derecha
- «i griega sube» → `sube_y`: la flecha es verde y ascendente
- «solo pregunta si» → `pregunta`: aparece «¿suben o bajan juntas?»
- «en conjunto» → `conjunto`: las dos flechas laten
- «Y las dos mitades» → `mitades`: los rótulos «y baja» e «y sube» laten
- «se cancelan» → `cancelan`: las dos flechas se anulan con un «0»
- «no hay una tendencia en línea recta» → `plana`: la recta de mejor ajuste queda plana, horizontal

<!-- b2 -->
Esa es la clave: la covarianza solo detecta la parte en línea recta de una relación. Si la relación es una curva, la covarianza puede no verla en absoluto. Por eso, covarianza cero se dice «no correlacionadas», y no «independientes». No es lo mismo.

- «la covarianza solo detecta» → `detecta`: rótulo «covarianza = relación en línea recta»
- «la parte en línea recta» → `recta`: una recta atraviesa una nube inclinada
- «Si la relación es una curva» → `curva`: vuelve la parábola
- «puede no verla en absoluto» → `no_ve`: un ojo tachado junto a la curva
- «Por eso» → `por_eso`: el rótulo de arriba late
- «covarianza cero se dice» → `se_dice`: aparece «σ_XY = 0»
- «no correlacionadas» → `no_corr`: «no correlacionadas» entra con rebote
- «independientes» → `no_indep`: «independientes» aparece tachado con un «≠»
- «No es lo mismo» → `distinto`: el «≠» crece entre las dos etiquetas

---

# Escena 14 — ExcepcionGaussiana

**Capítulo YouTube:** La excepción gaussiana

## Narración

<!-- b1 -->
Hay una excepción, y es muy importante para nosotros. Si las dos variables son gaussianas a la vez, entonces covarianza cero sí quiere decir independencia. Como el ruido suele ser gaussiano, esa excepción la vamos a usar muchísimo. Pero hay que acordarse de que es una excepción.

- «Hay una excepción» → `excepcion`: aparece el cartel «excepción»
- «muy importante para nosotros» → `importante`: la palabra «excepción» late
- «Si las dos variables» → `si_dos`: se dibujan las dos campanas
- «gaussianas a la vez» → `gauss`: una nube gaussiana conjunta, redonda, con una campana en cada eje
- «covarianza cero» → `cov_cero2`: «σ_XY = 0»
- «independencia» → `indep2`: «⇒ independientes» con un tilde verde
- «el ruido suele ser gaussiano» → `ruido`: una señal ruidosa magenta con su campana al lado
- «la vamos a usar muchísimo» → `usar`: una estrella junto al cartel de la excepción
- «es una excepción» → `solo_gauss`: rótulo «solo si ambas son gaussianas»

---

# Escena 15 — MediaDeLaCombinacion

**Capítulo YouTube:** Combinaciones de variables: la media

## Narración

<!-- b1 -->
En señales combinamos variables todo el tiempo: la señal más el ruido, el promedio de dos medidas, la diferencia entre dos sensores. Así que conviene saber qué pasa con la media y la varianza de una combinación: zeta igual a alfa por equis más beta por i griega. La media es fácil: por linealidad, es alfa por la media de equis más beta por la media de i griega.

- «combinamos variables» → `combinar`: dos curvas se suman en una tercera
- «la señal más el ruido» → `sr`: «S + N» en azul y magenta, con la suma en cian
- «el promedio de dos medidas» → `prom`: «(M₁ + M₂) / 2»
- «la diferencia entre dos sensores» → `dif_s`: «S₁ − S₂»
- «Así que conviene saber» → `conviene`: las filas de ejemplos laten
- «la media y la varianza» → `m_v`: aparecen «μ_Z» y «σ_Z²» con interrogantes
- «zeta igual a alfa por equis más beta por i griega» → `zeta`: se construye «Z = αX + βY» pieza a pieza
- «La media es fácil» → `facil`: «μ_Z» se enciende
- «por linealidad» → `lineal2`: rótulo «linealidad»
- «alfa por la media de equis» → `a_mx`: «α μ_X»
- «más beta por la media de i griega» → `b_my`: queda «μ_Z = α μ_X + β μ_Y»

---

# Escena 16 — VarianzaDeLaCombinacion

**Capítulo YouTube:** Combinaciones de variables: la varianza

## Narración

<!-- b1 -->
La varianza hay que deducirla. Restamos la media: zeta menos su media es alfa por equis centrada más beta por i griega centrada. Lo elevamos al cuadrado, y resolvemos el cuadrado de un binomio: el primero al cuadrado, más el segundo al cuadrado, más dos veces el producto. Y tomamos la esperanza de cada término.

- «hay que deducirla» → `deducir`: aparece «σ_Z² = E[(Z − μ_Z)²]»
- «Restamos la media» → `restar2`: se resalta «Z − μ_Z»
- «alfa por equis centrada» → `a_xc`: «α (X − μ_X)»
- «más beta por i griega centrada» → `b_yc`: «+ β (Y − μ_Y)», con el renglón «Z − μ_Z = α (X − μ_X) + β (Y − μ_Y)»
- «Lo elevamos al cuadrado» → `cuadrado`: el segundo miembro se encierra en un paréntesis al cuadrado
- «el cuadrado de un binomio» → `abc`: a un lado aparece «(a + b)² = a² + 2ab + b²»
- «el primero al cuadrado» → `prim`: «α² (X − μ_X)²»
- «el segundo al cuadrado» → `seg`: «β² (Y − μ_Y)²»
- «dos veces el producto» → `doble`: «2 α β (X − μ_X)(Y − μ_Y)»
- «la esperanza de cada término» → `esp_t`: un «E[ ]» entra delante de cada término

<!-- b2 -->
Quedan tres términos. Alfa al cuadrado por la varianza de equis. Beta al cuadrado por la varianza de i griega. Y un término cruzado: dos por alfa por beta por la covarianza. Si las variables no tienen covarianza, el término cruzado desaparece y las varianzas simplemente se suman. Esta es la promesa que dejamos pendiente hace dos episodios, al hablar de promedios.

- «Quedan tres términos» → `tres`: queda el resultado con tres términos
- «Alfa al cuadrado por la varianza de equis» → `t1`: «α² σ_X²»
- «Beta al cuadrado por la varianza de i griega» → `t2`: «β² σ_Y²»
- «un término cruzado» → `cruzado`: «2 α β σ_XY» en ámbar
- «dos por alfa por beta» → `dosab`: el marco del término cruzado late
- «por la covarianza» → `por_cov`: el marco late en rojo
- «no tienen covarianza» → `sin_cov`: «σ_XY = 0»
- «desaparece» → `desaparece`: el término cruzado se desvanece
- «las varianzas simplemente se suman» → `suman`: queda «σ_Z² = α² σ_X² + β² σ_Y²»
- «la promesa que dejamos pendiente» → `promesa`: vuelve el recuadro «las varianzas se suman» de la escena 16 del E4
- «al hablar de promedios» → `pagada`: un tilde verde sobre la promesa

---

# Escena 17 — EjemploSeisCuatroTres

**Capítulo YouTube:** Ejemplo con números: 6, 4 y 3

## Narración

<!-- b1 -->
Un ejemplo con números. La varianza de equis es seis, la de i griega es cuatro, y su covarianza es tres. Calculemos la varianza de dos equis menos tres i griega. Primer término: dos al cuadrado por seis, veinticuatro. Segundo: tres al cuadrado por cuatro, treinta y seis. Término cruzado: dos por dos por menos tres por tres, menos treinta y seis. En total, veinticuatro.

- «Un ejemplo con números» → `ejemplo`: la fórmula de tres términos queda arriba, con huecos
- «La varianza de equis es seis» → `v6`: «σ_X² = 6»
- «la de i griega es cuatro» → `v4`: «σ_Y² = 4»
- «su covarianza es tres» → `c3`: «σ_XY = 3»
- «dos equis menos tres i griega» → `z`: «Z = 2X − 3Y», con α = 2 y β = −3 resaltados
- «Primer término» → `p1`: se enciende «α² σ_X²» con los números «2² · 6»
- «veinticuatro» → `r24a`: «24»
- «Segundo» → `p2`: se enciende «β² σ_Y²» con «(−3)² · 4»
- «treinta y seis» → `r36`: «36»
- «Término cruzado» → `p3`: se enciende «2 α β σ_XY» con «2 · 2 · (−3) · 3»
- «menos treinta y seis» → `rm36`: «−36» en rojo
- «En total, veinticuatro» → `total`: «24 + 36 − 36 = 24» en ámbar

<!-- b2 -->
Fíjate en el signo. La covarianza es positiva: equis e i griega suelen subir juntas. Pero al restarlas, sus movimientos se compensan, y por eso el término cruzado resta. Y otra cosa: una fórmula con dos cuadrados y un término cruzado seguramente te suena de otro sitio. No es casualidad.

- «Fíjate en el signo» → `signo`: el signo menos del término cruzado se resalta
- «La covarianza es positiva» → `pos`: «σ_XY = +3»
- «suelen subir juntas» → `juntas`: dos curvas suben a la vez
- «al restarlas» → `restarlas`: aparece «X − Y»
- «sus movimientos se compensan» → `compensa`: las dos curvas se restan y queda una diferencia casi plana
- «el término cruzado resta» → `resta`: «−36» en rojo se agranda
- «Y otra cosa» → `otra`: se resalta la fórmula de arriba
- «dos cuadrados y un término cruzado» → `tres_t`: «a² + b² + 2ab» junto a la fórmula, con los tres términos emparejados por color
- «te suena de otro sitio» → `suena`: un interrogante
- «No es casualidad» → `casualidad2`: la fórmula queda quieta, enmarcada, como una pregunta pendiente

---

# Escena 18 — Cierre

**Capítulo YouTube:** Resumen y próximo episodio

## Narración

<!-- b1 -->
Hoy hemos visto cómo medir si dos variables se mueven juntas: la correlación y la covarianza, que es la correlación descontando las medias. Y que solo ven lo que va en línea recta, por lo que covarianza cero no es independencia, salvo en las gaussianas.

- «cómo medir si dos variables se mueven juntas» → `medir`: la nube inclinada con «σ_XY»
- «la correlación» → `corr`: «E[XY]»
- «la covarianza» → `cov`: «σ_XY = E[XY] − μ_X μ_Y»
- «descontando las medias» → `descontando`: se resaltan «μ_X μ_Y»
- «solo ven lo que va en línea recta» → `recta`: una recta sobre la nube
- «covarianza cero no es independencia» → `no_indep`: la parábola con «σ_XY = 0» y un «≠» sobre «independientes»
- «salvo en las gaussianas» → `gaussianas`: la nube gaussiana redonda con un tilde verde

<!-- b2 -->
También dedujimos la varianza de una combinación, con dos cuadrados y un término cruzado. Esa fórmula te suena de otro sitio, ¿verdad? Para verlo hay que dejar de pensar en las variables como números, y empezar a pensarlas como flechas. De eso va el próximo episodio: «Variables que son flechas».

- «la varianza de una combinación» → `combi`: «σ_Z² = α² σ_X² + β² σ_Y² + 2 α β σ_XY» por piezas
- «dos cuadrados y un término cruzado» → `tres_t`: los tres términos se colorean
- «te suena de otro sitio» → `suena`: un interrogante
- «dejar de pensar en las variables como números» → `numeros`: los números «6, 4, 3» se desvanecen
- «pensarlas como flechas» → `flechas`: aparecen dos flechas, de largo √6 y 2, con el ángulo entre ellas
- «De eso va» → `deeso`: las dos flechas laten
- «Variables que son flechas» → `titulo`: el título del próximo episodio entra con rebote
