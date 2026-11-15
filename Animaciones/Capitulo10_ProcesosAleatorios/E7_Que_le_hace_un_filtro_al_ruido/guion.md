# Episodio 7 — ¿Qué le hace un filtro al ruido?

Capítulo 10 (Procesos aleatorios), episodio 7 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 25 a 29), más un gancho y un cierre nuevos.

**Estado:** ritmo validado (0 huecos > 4 s), 17 escenas animadas (`s01`–`s17`) y borrador 480p15 renderizado con 0 avisos (10:21); falta el visto bueno del usuario (paso 15) y la revisión del texto ⭐ (paso 9). Después, render final `--calidad qh`.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Metes ruido puro en una caja que no conoces. Mides una sola correlación entre lo que entra y lo que sale. Y aparece, entera, la respuesta al impulso de la caja.»
- ⭐ Escena 17 (cierre): anuncia el E1 del Cap. 11 por su título, «¿En qué frecuencias vive el azar?».

Reparto de las escenas del guion base: 25 → escenas 03 a 05; 26 → 06 y 07; 27 → 08 a 10; 28 → 11 y 12; 29 → 13 a 16.
Solo se partieron bloques enteros en escenas atómicas: el texto del guion base no cambia.

Bucle que se paga aquí: «lo demostraremos en el último episodio» (escena 08 del guion base, resultado central del capítulo). Se paga en las escenas 06 a 10.

---

# Escena 01 — Gancho

**Capítulo YouTube:** Ruido que revela una caja

## Narración

<!-- b1 -->
Metes ruido puro en una caja que no conoces. Mides una sola correlación entre lo que entra y lo que sale. Y aparece, entera, la respuesta al impulso de la caja.

- «Metes ruido puro» → `ruido`: una tira de ruido blanco (la moneda ±1) entra por la izquierda
- «una caja que no conoces» → `caja`: una caja negra con «h = ?»
- «que no conoces» → `desconocida`: el «?» de la caja parpadea
- «una sola correlación» → `correl`: un correlador une la entrada y la salida
- «entre lo que entra y lo que sale» → `entra_sale`: dos flechas, una a cada lado de la caja
- «aparece, entera» → `aparece`: tres palitos surgen sobre un eje: «½», «½», «0»
- «la respuesta al impulso de la caja» → `impulso`: la caja se abre y muestra la «h» con los mismos tres palitos

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** ¿Qué le hace un filtro al ruido?

## Narración

<!-- b1 -->
¿Qué le hace un filtro al ruido?

- «¿Qué le hace» → `t1`: las palabras «¿Qué le hace» entran con rebote
- «un filtro al ruido?» → `t2`: «un filtro al ruido?» entra debajo, con la etiqueta «Capítulo 10 · Procesos aleatorios»

---

# Escena 03 — RepasoLTI

**Capítulo YouTube:** Repaso: respuesta al impulso

## Narración

<!-- b1 -->
Recordemos cómo funciona un sistema lineal e invariante en el tiempo. Queda descrito entero por su respuesta al impulso, hache: lo que sale cuando entra un golpe instantáneo. Tomemos uno sencillo, en tiempo discreto: el que promedia las dos últimas muestras. Su respuesta al impulso vale un medio en cero, un medio en uno, y nada más.

- «sistema lineal e invariante» → `lti`: una caja «LTI» con entrada y salida
- «en el tiempo» → `tiempo`: un eje t bajo la caja
- «Queda descrito entero» → `entero`: la caja se ilumina entera
- «respuesta al impulso» → `resp`: entra un golpe y sale la forma «h»
- «hache» → `hache`: aparece «h» junto a la forma de salida
- «un golpe instantáneo» → `golpe`: un palito único «δ» entra en la caja
- «Tomemos uno sencillo» → `sencillo`: la caja se vacía y entra un sistema más simple
- «en tiempo discreto» → `discreto`: el eje se convierte en palitos separados
- «el que promedia» → `promedia`: la caja se rotula «promediador»
- «las dos últimas muestras» → `dos`: dos muestras consecutivas se marcan en una tira
- «Su respuesta al impulso» → `su_resp`: vuelve «h» con el eje de palitos
- «un medio en cero» → `h0`: aparece un palito de altura ½ en «h[0]»
- «un medio en uno» → `h1`: aparece un segundo palito de altura ½ en «h[1]»
- «y nada más» → `nada`: el resto del eje queda vacío

---

# Escena 04 — Convolucion

**Capítulo YouTube:** La convolución con números

## Narración

<!-- b1 -->
Entra la secuencia dos, cuatro, seis. La primera salida es un medio por dos: uno, porque antes no había nada. La segunda, un medio por cuatro más un medio por dos: tres. La tercera, un medio por seis más un medio por cuatro: cinco. Cada salida es una suma de entradas recientes, cada una pesada por un valor de hache. Eso es la convolución.

- «Entra la secuencia» → `entrada`: aparece la entrada «2, 4, 6» como palitos
- «dos, cuatro, seis» → `dos_cuatro`: cada palito se rotula: 2, 4, 6
- «La primera salida» → `primera`: aparece la primera posición de la salida
- «un medio por dos» → `c1`: h dada la vuelta bajo el primer valor: «½·2»
- «uno, porque antes no había nada» → `r1`: sale «1» y un hueco a la izquierda
- «La segunda» → `segunda`: h se desplaza a la segunda posición
- «un medio por cuatro» → `c2a`: h se desliza un paso: «½·4»
- «un medio por dos» → `c2b`: se suma «+ ½·2»
- «tres» → `r2`: sale «3»
- «un medio por seis» → `c3a`: h se desliza otro paso: «½·6»
- «un medio por cuatro» → `c3b`: se suma «+ ½·4»
- «cinco» → `r3`: sale «5»
- «Cada salida» → `cada`: las tres salidas 1, 3, 5 se enmarcan juntas
- «entradas recientes» → `recientes`: las entradas usadas en cada suma se resaltan
- «pesada por un valor de hache» → `pesada`: los pesos «h» se marcan sobre cada entrada
- «un valor de hache» → `valor_h`: el «½» de cada entrada se remarca
- «la convolución» → `conv`: la palabra clave «convolución»

<!-- b2 -->
Escrita en general: la salida en ene es la suma, para cada ka, de hache de ka por la entrada en ene menos ka. La entrada de hace ka pasos pesa hache de ka. En tiempo continuo, la suma se convierte en una integral: i griega de te es la integral de hache de uve por equis de te menos uve.

- «la salida en ene» → `y_n`: aparece «y[n] =»
- «la suma, para cada ka» → `suma`: entra «Σ_k»
- «hache de ka» → `h_k`: entra «h[k]»
- «la entrada en ene menos ka» → `x_nk`: entra «x[n − k]»
- «La entrada de hace» → `entrada_hace`: un palito retrasado k pasos bajo la fórmula
- «hace ka pasos» → `pasos`: la cuenta del renglón anterior se marca con «k = 1»
- «En tiempo continuo» → `cont`: los palitos se estrechan hasta ser una curva
- «una integral» → `integral`: la suma se transforma en «∫»
- «i griega de te» → `y_t0`: aparece «y(t) =»
- «hache de uve» → `y_t1`: entra «∫ h(v)»
- «equis de te menos uve» → `x_tv`: entra «x(t − v) dv»

---

# Escena 05 — FourierYGanancia

**Capítulo YouTube:** Fourier y la ganancia en continua

## Narración

<!-- b1 -->
La otra forma de verlo es en frecuencia. La transformada de Fourier descompone una señal en senos de todas las frecuencias. La de la respuesta al impulso, hache de jota omega, dice cuánto amplifica el sistema cada frecuencia. Y la gran ventaja: una convolución en el tiempo se convierte en una multiplicación en frecuencia.

- «en frecuencia» → `frec`: el eje cambia a «ω»
- «La transformada de Fourier» → `fourier`: una flecha «F» lleva de tiempo a frecuencia
- «descompone una señal» → `descompone`: una señal se separa en tres senos
- «senos de todas las frecuencias» → `senos`: los senos se apilan, cada uno de otra frecuencia
- «La de la respuesta al impulso» → `la_de`: la «h» pasa por «F»
- «hache de jota omega» → `h_jw`: aparece «H(jω)» sobre una curva de ganancia
- «cuánto amplifica» → `amplifica`: la curva muestra la ganancia en cada frecuencia
- «la gran ventaja» → `ventaja`: un destello sobre la palabra «ventaja»
- «una convolución en el tiempo» → `conv_t`: «y = h * x»
- «una multiplicación en frecuencia» → `mult`: «Y = H · X», con la estrella transformada en punto

<!-- b2 -->
Un valor nos va a interesar: hache en cero, la ganancia en continua. Es la suma de todos los valores de hache, o su integral, y una entrada constante sale multiplicada por ella. En el promediador, un medio más un medio: uno. Entra un dos constante y sale un dos.

- «hache en cero» → `h0`: se marca «H(0)» sobre el origen de la curva
- «la ganancia en continua» → `continua`: la etiqueta «ganancia en continua»
- «la suma de todos los valores de hache» → `suma_h`: «H(0) = Σ h[k]»
- «o su integral» → `integral_h`: aparece «= ∫ h»
- «una entrada constante» → `const`: una recta constante aparece
- «sale multiplicada por ella» → `mult`: la recta sale escalada por «H(0)»
- «En el promediador» → `en_prom`: vuelve el promediador «½, ½»
- «un medio más un medio» → `medios`: «½ + ½» con los dos palitos
- «uno» → `uno`: «H(0) = 1» con tilde
- «Entra un dos constante» → `entra2`: una recta constante «2, 2, 2» entra en la caja
- «sale un dos» → `sale2`: sale la misma recta «2, 2, 2»

---

# Escena 06 — EsperanzaEntra

**Capítulo YouTube:** La media de la salida

## Narración

<!-- b1 -->
Si a la entrada llega una realización de un proceso, a la salida sale otra señal aleatoria: un proceso nuevo. Empecemos por su media. La media de la salida es la esperanza de una suma de entradas pesadas por hache. Y la esperanza es lineal: la esperanza de una suma es la suma de las esperanzas, y los números que multiplican salen fuera.

- «una realización» → `realiz`: una curva entra en la caja
- «otra señal aleatoria» → `sale`: sale otra curva distinta
- «un proceso nuevo» → `nuevo`: el ensemble de entrada entra y sale otro ensemble
- «su media» → `media`: aparece «E[y[n]] =»
- «La media de la salida» → `media_y`: se marca «E[y[n]]» en la fórmula
- «una suma de entradas pesadas» → `suma`: «E[Σ h[k] x[n − k]]»
- «pesadas por hache» → `pesadas`: los pesos «h[k]» se resaltan
- «la esperanza es lineal» → `lineal`: la palabra «linealidad» en ámbar
- «la esperanza de una suma» → `esp_suma`: «E[a + b]» a la izquierda
- «la suma de las esperanzas» → `sumas`: «E[a + b] = E[a] + E[b]»
- «los números que multiplican» → `numeros`: las constantes se marcan en «E[c a]»
- «salen fuera» → `fuera`: «E[c a] = c E[a]», el número c sale de la esperanza

<!-- b2 -->
Así que la esperanza entra en la suma y se queda con cada entrada. Si la entrada es estacionaria, la esperanza de cada una es la misma media, que sale fuera también. Dentro queda la suma de todos los hache: la ganancia en continua. La media de la salida es hache en cero por la media de la entrada.

- «entra en la suma» → `entra`: segundo renglón «= Σ h[k] E[x[n − k]]»
- «se queda con cada entrada» → `se_queda`: la «E» rodea cada término de la suma
- «estacionaria» → `estac`: sello «estacionaria»
- «la misma media» → `misma`: tercer renglón «= Σ h[k] μ_x»
- «sale fuera» → `sale_fuera`: cuarto renglón «= μ_x Σ h[k]»
- «Dentro queda» → `dentro`: un recuadro sobre lo que queda dentro
- «la suma de todos los hache» → `suma_h`: «Σ h[k]» resaltado
- «la ganancia en continua» → `gan`: la suma se rotula «H(0)»
- «La media de la salida» → `media_sale`: «μ_y» aparece a la izquierda
- «hache en cero por la media» → `resultado`: recuadro «μ_y = H(0) μ_x»

---

# Escena 07 — ComprobarMedia

**Capítulo YouTube:** Comprobar la media

## Narración

<!-- b1 -->
Compruébalo con el sensor y el promediador. La temperatura tiene media veinte, y el promediador, ganancia uno en continua: la salida tiene media veinte. Promediar dos temperaturas no cambia la temperatura media. Y con el filtro que resta la muestra anterior, cuya respuesta es uno y menos uno, la ganancia en continua es cero: la salida tiene media cero, sea cual sea la entrada.

- «el sensor» → `sensor`: el sensor de temperatura con su curva de realización
- «La temperatura» → `temp`: la curva del sensor, con su línea en 20
- «media veinte» → `m20`: aparece «μ_x = 20»
- «ganancia uno» → `g1`: «H(0) = 1»
- «la salida tiene media veinte» → `sale20`: «μ_y = 20» en el recuadro
- «Promediar dos temperaturas» → `promedio`: dos valores se funden en uno
- «no cambia la temperatura media» → `igual`: tilde verde
- «Y con el filtro» → `filtro`: la caja se abre para el nuevo filtro
- «resta la muestra anterior» → `resta`: nueva caja con «h = (1, −1)»
- «uno y menos uno» → `uno_menos`: dos palitos, uno arriba y uno abajo
- «la ganancia en continua es cero» → `h_cero`: «H(0) = 1 − 1 = 0»
- «media cero» → `m0`: «μ_y = 0», la curva de salida oscila alrededor del cero
- «sea cual sea la entrada» → `cual_sea`: varias curvas de entrada distintas, todas con salida centrada en 0

<!-- b2 -->
La media atraviesa el sistema como si fuera una señal constante, que es lo que es: la parte que no cambia. En tiempo continuo, la deducción es idéntica, con una integral, y la letra pequeña es que el sistema sea estable y la entrada tenga varianza finita. Y hay algo más: la correlación cruzada entre entrada y salida solo depende de la separación. Lo veremos en la cuenta siguiente, que es la importante.

- «atraviesa el sistema» → `atraviesa`: una recta constante cruza la caja
- «como si fuera» → `como`: la recta atraviesa la caja sin cambiar
- «la parte que no cambia» → `constante`: la media se subraya sobre la curva
- «En tiempo continuo» → `continuo`: la suma se vuelve integral
- «la deducción es idéntica» → `identica`: los mismos cuatro renglones, con «∫»
- «con una integral» → `integral`: «Σ» se cambia por «∫»
- «la letra pequeña» → `pequena`: aparece el rótulo «apunte en profundidad»
- «sea estable» → `estable`: casilla «sistema estable»
- «varianza finita» → `finita`: casilla «varianza finita»
- «Y hay algo más» → `algo_mas`: un signo de exclamación junto a la caja
- «la correlación cruzada» → `cruzada`: entrada y salida unidas por un correlador
- «solo depende de la separación» → `separacion`: aparece «¿conjuntamente WSS? → ahora»
- «Lo veremos» → `veremos`: la flecha hacia el renglón siguiente
- «la cuenta siguiente» → `siguiente`: un destello apunta al renglón que viene
- «que es la importante» → `importante`: la flecha se ilumina

---

# Escena 08 — CorrelacionCruzada

**Capítulo YouTube:** La correlación cruzada

## Narración

<!-- b1 -->
Calculemos la correlación cruzada entre la salida en te más tau y la entrada en te. La salida es una integral de la entrada, así que el producto también es una integral. La esperanza vuelve a entrar en ella, y dentro queda la esperanza del producto de dos entradas separadas tau menos uve: la autocorrelación de la entrada en tau menos uve.

- «la correlación cruzada» → `cruzada`: aparece «E[y(t + τ) x(t)]»
- «la salida en te más tau» → `y_tau`: la salida se marca en la fórmula
- «la entrada en te» → `x_t`: la entrada se marca en la fórmula
- «una integral» → `integral`: segundo renglón «= E[∫ h(v) x(t + τ − v) dv · x(t)]»
- «el producto también» → `producto`: «· x(t)» se suma a la integral
- «La esperanza vuelve a entrar» → `entra`: tercer renglón «= ∫ h(v) E[x(t + τ − v) x(t)] dv»
- «dentro queda» → `dentro`: un recuadro sobre «E[x(t + τ − v) x(t)]»
- «dos entradas separadas» → `separadas`: las dos entradas se marcan sobre una curva, separadas «τ − v»
- «la autocorrelación de la entrada» → `autocorr`: cuarto renglón «= ∫ h(v) R_xx(τ − v) dv»
- «en tau menos uve» → `tau_v`: «τ − v» en ámbar sobre R_xx

<!-- b2 -->
El resultado es la integral de hache de uve por erre sub equis equis de tau menos uve. Eso es una convolución: la correlación cruzada es hache convolucionada con la autocorrelación de la entrada. Y en el resultado no aparece te por ningún lado, solo tau: entrada y salida son conjuntamente estacionarias, como habíamos anunciado.

- «hache de uve» → `h_v`: se marca «h(v)» en el renglón
- «erre sub equis equis de tau menos uve» → `r_xx`: se marca «R_xx(τ − v)»
- «una convolución» → `conv`: recuadro «R_yx(τ) = h(τ) * R_xx(τ)»
- «hache convolucionada» → `h_conv`: por la caja pasa la curva R_xx en lugar de una señal
- «la autocorrelación de la entrada» → `de_entrada`: la curva R_xx entra por la caja
- «Y en el resultado» → `resultado`: se marca el resultado «h(τ) * R_xx(τ)»
- «no aparece te» → `sin_t`: se tacha cualquier «t» que sobre: «no aparece t»
- «solo tau» → `solo_tau`: «solo τ» en ámbar
- «conjuntamente estacionarias» → `conj`: sello «conjuntamente WSS» en la salida
- «como habíamos anunciado» → `anunciado`: tilde junto al rótulo «¿conjuntamente WSS?»

---

# Escena 09 — Determinista

**Capítulo YouTube:** Azar entra, cuenta determinista

## Narración

<!-- b1 -->
Fíjate en lo que acaba de pasar. Las señales son aleatorias, pero la relación entre sus correlaciones es determinista: la convolución de siempre, con la autocorrelación haciendo de señal de entrada. Repitiendo el mismo paso con la segunda hache sale la autocorrelación de la salida: la de la entrada, convolucionada con erre sub hache hache, la autocorrelación determinista de la respuesta al impulso.

- «Las señales son aleatorias» → `aleat`: el ensemble de entrada y de salida, con curvas desordenadas
- «pero la relación» → `relacion`: una flecha limpia sale del ensemble
- «entre sus correlaciones» → `correls`: dos curvas de correlación sobre la flecha
- «determinista» → `determ`: la relación entre ellas se dibuja como una flecha limpia
- «la convolución de siempre» → `siempre`: la convolución del repaso reaparece, «h * x»
- «haciendo de señal de entrada» → `hace_de`: la curva R_xx toma el lugar de «x»
- «Repitiendo» → `repite`: el bloque se repite una vez más
- «el mismo paso» → `mismo`: el paso de la escena anterior se repite
- «la segunda hache» → `segunda`: dos bloques en cadena, «h(−τ)» y «h(τ)»
- «la autocorrelación de la salida» → `r_yy`: «R_yy»
- «convolucionada con» → `conv_con`: «* R_hh» se une a «R_xx»
- «erre sub hache hache» → `r_hh`: los dos bloques se funden en «R_hh(τ)»
- «determinista de la respuesta» → `det_h`: recuadro «R_yy = R_hh * R_xx»

---

# Escena 10 — SolapeYMoneda

**Capítulo YouTube:** Deslizar h sobre sí misma

## Narración

<!-- b1 -->
Erre sub hache hache se obtiene deslizando hache sobre sí misma y sumando los productos donde se solapa. En el promediador, sin desplazar: un medio al cuadrado más un medio al cuadrado, un medio. Desplazado un paso, solo se solapa un término: un cuarto. Y con la moneda a la entrada, cuya autocorrelación es un impulso, la salida tiene justo esa autocorrelación.

- «deslizando hache sobre sí misma» → `desliza`: h se desliza sobre una copia de sí misma
- «sumando los productos» → `productos`: los productos de las zonas solapadas se suman
- «donde se solapa» → `solapa`: la zona solapada se sombrea
- «En el promediador» → `en_prom`: el promediador «½, ½» sobre su copia
- «sin desplazar» → `cero`: las dos h coinciden exactamente
- «un medio al cuadrado más un medio al cuadrado» → `cuadrados`: «¼ + ¼»
- «un medio» → `medio`: «R_hh[0] = ½»
- «Desplazado un paso» → `paso`: la copia se corre un paso
- «solo se solapa un término» → `un_termino`: queda una sola pareja marcada
- «un cuarto» → `cuarto`: «R_hh[1] = ¼»
- «la moneda» → `moneda`: entra la tira de la moneda ±1
- «un impulso» → `impulso`: «R_xx = impulso»
- «justo esa autocorrelación» → `justo`: la salida muestra «R_yy = R_hh»

<!-- b2 -->
Comprobémoslo a mano. La salida es la media de dos tiradas: vale uno, cero o menos uno, con probabilidades un cuarto, un medio y un cuarto. La esperanza del cuadrado es un cuarto más un cuarto: un medio. Coincide.

- «a mano» → `a_mano`: una tabla de cuatro parejas de tiradas
- «la media de dos tiradas» → `media2`: cada pareja se promedia: «1», «0», «0», «−1»
- «uno, cero o menos uno» → `valores`: los tres valores distintos se separan
- «un cuarto, un medio y un cuarto» → `probs`: «¼, ½, ¼» sobre cada valor
- «La esperanza del cuadrado» → `cuadrado`: «Var = E[y²]»
- «un cuarto más un cuarto» → `cuartos`: «¼ + ¼»
- «un medio» → `var`: «Var = ½»
- «Coincide» → `coincide`: tilde junto a «R_hh[0] = ½»

---

# Escena 11 — TelegraficaYFiltro

**Capítulo YouTube:** Un ejemplo continuo

## Narración

<!-- b1 -->
Ahora, un ejemplo continuo. A la entrada ponemos la onda telegráfica con lambda igual a uno: su autocorrelación es e elevado a menos dos por el valor absoluto de tau, y su varianza, uno. El filtro es un pasabajos sencillo: hache de te es tres por e elevado a menos tres te, a partir de te igual a cero. Su área vale uno: ganancia uno en continua.

- «un ejemplo continuo» → `continuo`: aparece «continuo» y un eje t
- «la onda telegráfica» → `onda`: la onda ±1 entra a la caja
- «lambda igual a uno» → `lambda`: «λ = 1»
- «e elevado a menos dos» → `r_xx`: aparece «R_xx(τ) = e^(−2|τ|)»
- «valor absoluto de tau» → `abs`: la curva en forma de pico simétrico
- «su varianza, uno» → `var1`: la curva vale 1 en el origen
- «un pasabajos sencillo» → `pasabajos`: la caja muestra la curva «3e^(−3t)» dentro
- «tres por e elevado a menos tres te» → `h_t`: «h(t) = 3e^(−3t)»
- «a partir de te igual a cero» → `u_t`: «u(t)», la curva arranca en cero
- «Su área vale uno» → `area`: el área bajo h se sombrea: «área de h = 1»
- «ganancia uno en continua» → `g1`: «H(0) = 1»

<!-- b2 -->
Primero, la autocorrelación determinista del filtro. Deslizamos hache sobre sí misma una distancia tau, multiplicamos y medimos el área donde se solapan. Queda nueve por e elevado a menos tres tau, por el área de e elevado a menos seis te, que es un sexto. Resultado: tres medios por e elevado a menos tres por el valor absoluto de tau.

- «la autocorrelación determinista» → `r_hh`: aparece «R_hh(τ) = ?»
- «Deslizamos hache sobre sí misma» → `desliza`: h se desliza sobre una copia a distancia τ
- «multiplicamos» → `multiplica`: el producto de las dos curvas se dibuja
- «el área donde se solapan» → `solape`: el solapamiento se sombrea
- «nueve por e elevado a menos tres tau» → `nueve`: «9 e^(−3τ)»
- «e elevado a menos seis te» → `seis`: «∫ e^(−6t) dt»
- «un sexto» → `sexto`: «= ⅙»
- «tres medios» → `tres_medios`: «(3/2) e^(−3τ)»
- «valor absoluto de tau» → `r_abs`: recuadro «R_hh(τ) = (3/2) e^(−3|τ|)»

---

# Escena 12 — VarianzaDeSalida

**Capítulo YouTube:** La potencia que quita el filtro

## Narración

<!-- b1 -->
La varianza de la salida es su autocorrelación en cero: la convolución de las dos autocorrelaciones evaluada en cero, que resulta ser el área del producto de las dos curvas. Al multiplicar las exponenciales, los exponentes se suman: tres medios por e elevado a menos cinco por el valor absoluto de tau. Su área es un quinto a cada lado; por tres medios, tres quintos: cero coma seis.

- «La varianza de la salida» → `varianza`: aparece «Var(y) = R_yy(0)»
- «su autocorrelación en cero» → `r_cero`: se marca «τ = 0»
- «la convolución de las dos autocorrelaciones» → `dos_autocorr`: las dos curvas «R_hh» y «R_xx» con la estrella
- «evaluada en cero» → `en_cero`: la convolución se evalúa en τ = 0
- «el área del producto» → `area_prod`: las dos curvas «e^(−2|s|)» y «(3/2) e^(−3|s|)» se dibujan una sobre otra
- «las dos curvas» → `dos_curvas`: las dos curvas se superponen
- «Al multiplicar las exponenciales» → `multiplicar`: las dos curvas se multiplican punto a punto
- «los exponentes se suman» → `suman`: el producto «(3/2) e^(−5|s|)» aparece sombreado
- «cinco por el valor absoluto» → `cinco`: «−5|s|» en ámbar
- «un quinto a cada lado» → `quinto`: «⅕ + ⅕ = ⅖»
- «tres medios» → `tm`: «(3/2)(2/5)»
- «tres quintos» → `tq`: «= 3/5»
- «cero coma seis» → `c06`: «= 0,6»

<!-- b2 -->
Una simulación, filtrando la onda de verdad, da cero coma seis uno: la cuenta funciona. El filtro le ha quitado potencia al proceso, porque un pasabajos recorta las variaciones rápidas. Cuánto quita depende de una carrera entre dos memorias, la del filtro y la del proceso: tres entre tres más dos. Un filtro mucho más rápido lo deja casi intacto; uno mucho más lento se lo come casi entero.

- «Una simulación» → `simula`: la onda filtrada de verdad, en una curva suavizada
- «cero coma seis uno» → `c061`: tilde «simulación: 0,61»
- «la cuenta funciona» → `funciona`: tilde verde
- «le ha quitado potencia» → `quita`: dos barras de potencia: entrada «1», salida «0,6»
- «recorta las variaciones rápidas» → `rapidas`: la salida se ve más suave que la entrada
- «Cuánto quita depende» → `cuanto`: la barra de salida se marca con «¿cuánto?»
- «una carrera entre dos memorias» → `carrera`: dos flechas de memoria compiten, «β» y «α»
- «la del filtro y la del proceso» → `ambas`: dos cajas, «filtro: β = 3» y «proceso: α = 2»
- «tres entre tres más dos» → `formula`: «β/(α + β) = 3/(2 + 3)»
- «mucho más rápido» → `rapido`: un deslizador de β sube y la barra de salida se acerca a 1
- «mucho más lento» → `lento`: el deslizador baja y la barra se acerca a 0

---

# Escena 13 — EnFrecuencia

**Capítulo YouTube:** Pasar a frecuencia

## Narración

<!-- b1 -->
Las convoluciones son incómodas, así que pasemos a frecuencia. Llamemos ese sub equis equis de jota omega a la transformada de Fourier de la autocorrelación. Cada convolución se vuelve un producto: la correlación cruzada se transforma en hache de jota omega por ese sub equis equis, y la autocorrelación de la salida, en el módulo de hache al cuadrado por ese sub equis equis.

- «Las convoluciones son incómodas» → `incomodas`: las fórmulas de las escenas 08 y 09 con sus estrellas
- «pasemos a frecuencia» → `pasar`: el eje cambia a «ω»
- «ese sub equis equis de jota omega» → `s_xx`: aparece «S_xx(jω) = F{R_xx(τ)}»
- «la transformada de Fourier de la autocorrelación» → `fourier`: una flecha «F» une R_xx con S_xx
- «Cada convolución se vuelve un producto» → `producto`: las estrellas «*» se transforman en puntos «·»
- «la correlación cruzada» → `cruzada`: entra «S_yx = H S_xx»
- «hache de jota omega por ese sub equis equis» → `h_s`: se marcan «H» y «S_xx»
- «la autocorrelación de la salida» → `salida`: entra «S_yy = |H|² S_xx», con recuadro
- «el módulo de hache al cuadrado» → `modulo`: se marca «|H|²»
- «por ese sub equis equis» → `de_nuevo`: «S_xx» se resalta en la fórmula

<!-- b2 -->
¿Por qué al cuadrado? Porque hache aparece dos veces, una tal cual y otra dada la vuelta, y en frecuencia sus desfases se cancelan. En cada frecuencia, el filtro multiplica por el cuadrado de su ganancia, y la fase no importa. En tiempo discreto, exactamente igual.

- «¿Por qué al cuadrado?» → `porque`: el cuadrado de «|H|²» parpadea
- «aparece dos veces» → `dos_veces`: dos flechas, «h» y «h dada la vuelta»
- «dada la vuelta» → `vuelta`: la segunda flecha se voltea
- «sus desfases se cancelan» → `cancelan`: «+φ» y «−φ» se anulan y queda «|H|²»
- «En cada frecuencia» → `cada_frec`: una frecuencia se marca sobre la curva
- «el filtro multiplica» → `multiplica`: la curva de ganancia multiplica el espectro
- «el cuadrado de su ganancia» → `cuadrado`: la curva de ganancia se eleva al cuadrado
- «la fase no importa» → `fase`: la fase se tacha
- «En tiempo discreto» → `discreto`: el eje se convierte en palitos, «Ω»

---

# Escena 14 — MonedaEnFrecuencia

**Capítulo YouTube:** Darle forma al ruido

## Narración

<!-- b1 -->
Con la moneda y el promediador. La moneda no tiene memoria: su autocorrelación es un impulso, cuya transformada es plana, igual en todas las frecuencias. El promediador deja pasar la continua y anula la frecuencia más rápida, la que alterna más uno y menos uno. A la salida, la curva plana cae hacia las frecuencias altas: el filtro le ha dado forma al ruido.

- «la moneda» → `moneda`: la tira de la moneda ±1
- «no tiene memoria» → `sin_mem`: su autocorrelación es un impulso
- «un impulso» → `impulso`: el impulso «R_xx» aparece
- «cuya transformada» → `transf`: una flecha «F» lo lleva a frecuencia
- «plana» → `plana`: el espectro de la moneda, una recta horizontal
- «igual en todas las frecuencias» → `todas`: la recta marca todas las frecuencias por igual
- «El promediador» → `prom`: encima, |H|² del promediador
- «deja pasar la continua» → `continua`: la curva vale 1 en frecuencia cero
- «anula la frecuencia más rápida» → `rapida`: la curva vale 0 en la frecuencia más alta
- «alterna más uno y menos uno» → `alterna`: la tira «+1, −1, +1…» entra y sale plana
- «la curva plana cae» → `cae`: el producto, una curva que baja
- «hacia las frecuencias altas» → `altas`: la curva baja hacia la derecha
- «dado forma al ruido» → `forma`: rótulo «el filtro le da forma al ruido»

---

# Escena 15 — IdentificarConRuido

**Capítulo YouTube:** Identificar un sistema con ruido

## Narración

<!-- b1 -->
Y una aplicación preciosa. La correlación cruzada era hache convolucionada con la autocorrelación de la entrada. Si la entrada es la moneda, esa autocorrelación es un impulso, y la correlación cruzada es directamente hache: un medio, un medio y cero, justo el promediador. Metes ruido en un sistema desconocido, mides la correlación entre lo que entra y lo que sale, y tienes su respuesta al impulso.

- «una aplicación» → `aplicacion`: una caja negra «h = ?»
- «La correlación cruzada» → `cruzada`: aparece «R_yx»
- «hache convolucionada» → `conv`: aparece «R_yx = h * R_xx»
- «la autocorrelación de la entrada» → `de_entrada`: «R_xx» se marca en la fórmula
- «Si la entrada» → `si_entrada`: la moneda entra en la caja
- «la moneda» → `moneda`: entra la tira de la moneda en la caja
- «un impulso» → `impulso`: «R_xx = impulso»
- «directamente hache» → `directo`: «R_yx = h»
- «un medio, un medio y cero» → `tres`: un correlador dibuja «½», «½», «0»
- «justo el promediador» → `justo`: tilde junto a la h del promediador
- «un sistema desconocido» → `desconocido`: la caja negra otra vez, con «?»
- «mides la correlación» → `mides`: el correlador une entrada y salida
- «su respuesta al impulso» → `respuesta`: la caja se abre y aparece «h»

---

# Escena 16 — DensidadEspectral

**Capítulo YouTube:** Un nombre para S_xx

## Narración

<!-- b1 -->
Por último, mira otra vez el módulo de hache al cuadrado por ese sub equis equis. En Señales y Sistemas, así se transformaba la densidad espectral de energía de una señal al pasar por un filtro. No es casualidad. Ese sub equis equis dice cómo se reparte la potencia del proceso entre las frecuencias, y su nombre es densidad espectral de potencia.

- «el módulo de hache al cuadrado» → `modulo`: «|H|² S_xx»
- «por ese sub equis equis» → `por_s`: «S_xx» en la fórmula
- «Señales y Sistemas» → `sys`: a su lado, la fórmula de la densidad espectral de energía
- «densidad espectral de energía» → `energia`: «|H|² · densidad de energía» con el mismo dibujo
- «de una señal» → `de_senal`: una señal entra en el filtro
- «al pasar por un filtro» → `pasa_filtro`: la señal sale transformada
- «No es casualidad» → `casualidad`: las dos fórmulas se alinean y se marca su parecido
- «Ese sub equis equis» → `s_xx`: «S_xx» se colorea en ámbar
- «cómo se reparte la potencia» → `reparte`: una curva cuya área se reparte entre las frecuencias
- «entre las frecuencias» → `entre`: el eje «ω» con franjas
- «densidad espectral de potencia» → `nombre`: aparece el nombre en palabra clave

---

# Escena 17 — Cierre

**Capítulo YouTube:** ¿En qué frecuencias vive el azar?

## Narración

<!-- b1 -->
Hoy hemos visto qué le hace un filtro al azar: la media sale multiplicada por la ganancia en continua, y la autocorrelación, por una cuenta determinista. Y en frecuencia, por el módulo al cuadrado. Pero ¿qué dice, de verdad, esa densidad espectral de potencia? En el próximo capítulo: ¿en qué frecuencias vive el azar?

- «la media sale multiplicada» → `media`: vuelve «μ_y = H(0) μ_x»
- «la autocorrelación» → `autocorr`: vuelve «R_yy = R_hh * R_xx»
- «una cuenta determinista» → `determ`: «determinista» en palabra clave
- «en frecuencia» → `frec`: vuelve «S_yy = |H|² S_xx»
- «por el módulo al cuadrado» → `modulo`: el módulo de H al cuadrado se marca
- «Pero ¿qué dice» → `que_dice`: aparece un «?» sobre «S_xx»
- «esa densidad espectral de potencia» → `psd`: «S_xx» en ámbar, con un signo de pregunta
- «En el próximo capítulo» → `proximo`: una puerta con el número 11
- «¿en qué frecuencias vive el azar?» → `titulo_c11`: tarjeta con el título del próximo episodio
