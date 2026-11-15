# Episodio 2 — Lo que un espectro no puede hacer

Capítulo 11 (Densidad espectral de potencia), episodio 2 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 06 a 10), más un gancho y un cierre nuevos.

**Estado:** gancho y cierre aprobados por el usuario; escenas `s01`–`s13` escritas; `ritmo.py` sin huecos; borrador 480p15 de 10:24 con 0 avisos y hojas de contacto revisadas. Falta el visto bueno del usuario al mp4 (paso 15) y el render final.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Un rectángulo parece la autocorrelación más razonable del mundo. Pero ningún proceso puede tenerla, y se descubre con una sola cuenta…»
- ⭐ Escena 13 (cierre): resumen y anuncia E3 por su título, «El color del ruido».

Nota para el episodio anterior: el cierre de E1 ya anuncia este título, «Lo que un espectro no puede hacer».

Reparto de las escenas del guion base: 06 → escenas 03 y 04; 07 → 05 y 06; 08 → 07 y 08; 09 → 09 y 10; 10 → 11 y 12.
Solo se partieron bloques enteros en escenas atómicas: el texto del guion base no cambia.

Hilos que este episodio abre o paga (ver `../guion_base.md`):
- El rectángulo que se desliza sobre otro (escena 07): se anuncia que vuelve; se paga en la escena 16 (E4).
- Las tres barras ρ, 1, ρ con ρ = 0,4 (escenas 05 a 12): espectro 1 + 0,8 cos Ω, el mismo dibujo en todo el capítulo.
- El filtro (2, 1)/√5 (escena 12): se anuncia que vuelve; se revela como filtro modelador en la escena 26 (E6).
- «La potencia no puede ser negativa»: se usa en el rectángulo (07) y en el límite de ρ (09).

---

# Escena 01 — Gancho

**Capítulo YouTube:** Una curva que no puede ser

## Narración

<!-- b1 -->
Un rectángulo parece la autocorrelación más razonable del mundo. Pero ningún proceso puede tenerla, y se descubre con una sola cuenta. Hoy vemos qué curvas puede tener un espectro y cuáles no.

- «Un rectángulo» → `rect`: se dibuja un rectángulo de altura 1 entre −1 y 1
- «la autocorrelación más razonable» → `razonable`: entra la etiqueta «R_xx(τ)» y un tilde verde junto al rectángulo
- «ningún proceso puede tenerla» → `nopuede`: el tilde se vuelve una cruz roja
- «una sola cuenta» → `cuenta`: a la derecha se dibuja la transformada del rectángulo, que se hunde bajo cero
- «Hoy vemos» → `hoy`: aparece un eje de frecuencias con la etiqueta «espectro»
- «cuáles no» → `cuales`: dos curvas quedan lado a lado, una con tilde verde y otra con cruz roja

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Lo que un espectro no puede hacer

## Narración

<!-- b1 -->
Lo que un espectro no puede hacer.

- «Lo que un espectro» → `t1`: «Lo que un espectro» entra con rebote
- «no puede hacer» → `t2`: «no puede hacer» entra debajo, con la etiqueta «Capítulo 11 · Densidad espectral de potencia»

---

# Escena 03 — NuncaNegativa

**Capítulo YouTube:** ¿Puede un espectro ser negativo?

## Narración

<!-- b1 -->
Una pregunta antes de seguir. ¿Puede una densidad espectral valer menos cero coma cinco en alguna frecuencia? Piénsalo un momento. Tienes todo lo necesario: sabes qué pasa cuando pones un colador encima de una banda.

- «Una pregunta antes de seguir» → `pregunta`: corte seco; aparece la pregunta «¿S_xx(jω) = −0,5?» sobre un eje vacío
- «¿Puede una densidad espectral» → `puede`: entra la etiqueta «densidad espectral» sobre el eje
- «menos cero coma cinco» → `valor`: una marca en −0,5 sobre el eje vertical
- «Piénsalo un momento» → `pausa`: un reloj de arena se vacía
- «Tienes todo lo necesario» → `necesario`: el colador se resalta junto a un «✓ ya lo sabes»
- «un colador encima de una banda» → `colador`: aparece el ícono del colador con su ventanita sobre un tramo del eje

<!-- b2 -->
Supongamos que sí. Una curva que se hunde hasta menos cero coma cinco entre tres y cuatro radianes por segundo, y lo mismo en su reflejo. Ponemos el colador justo ahí. El área que queda es aproximadamente altura por ancho, dos veces: menos cero coma cinco por uno, por dos. Menos uno. Dividido entre dos pi, una potencia de menos cero coma uno seis.

- «Supongamos que sí» → `supongamos`: la curva imaginaria aparece, positiva, sobre el eje
- «Una curva que se hunde» → `curva`: la curva baja suavemente hacia el eje
- «entre tres y cuatro radianes por segundo» → `hundir`: entre ω = 3 y ω = 4 la curva se hunde hasta −0,5 y se rotula «3 a 4 rad/s»
- «su reflejo» → `reflejo`: la misma hendidura aparece en −4 a −3
- «Ponemos el colador justo ahí» → `poner`: las dos ventanitas del colador se colocan sobre las dos hendiduras y el resto se apaga
- «El área que queda» → `quedaarea`: el área bajo la hendidura se sombrea en rojo
- «altura por ancho, dos veces» → `altancho`: se marcan «altura −0,5» y «ancho 1», y un «× 2»
- «menos cero coma cinco por uno, por dos» → `cuenta`: aparece «−0,5 × 1 × 2»
- «Menos uno» → `menos1`: «= −1» debajo
- «Dividido entre dos pi» → `dospi`: «−1 / 2π» se arma por piezas
- «menos cero coma uno seis» → `p016`: «≈ −0,16» y un sello rojo «potencia negativa»

<!-- b3 -->
Pero la potencia de la salida es la esperanza de un cuadrado, y un cuadrado nunca es negativo. Una potencia negativa es imposible. Así que esa curva no puede ser la densidad espectral de ningún proceso. Y si la parte negativa fuera estrechísima, daría igual: el colador se puede estrechar tanto como quieras, hasta atraparla.

- «la esperanza de un cuadrado» → `espcuad`: aparece «E[y²]»
- «un cuadrado nunca es negativo» → `cuadrado`: junto a «E[y²]» entra «≥ 0» en verde
- «Una potencia negativa es imposible» → `imposible`: el sello «potencia negativa» se tacha con una cruz grande
- «esa curva no puede ser» → `nopuede`: la curva imaginaria se apaga en rojo
- «de ningún proceso» → `ninguno`: la etiqueta «S_xx de ningún proceso» se tacha
- «Y si la parte negativa» → `parteneg`: una hendidura más fina aparece en la curva
- «estrechísima» → `estrecha`: la hendidura se vuelve una rendija muy fina
- «el colador se puede estrechar» → `colestrecha`: el colador se angosta alrededor de la rendija
- «hasta atraparla» → `atrapa`: el colador se estrecha y la atrapa igual

---

# Escena 04 — LaFormula

**Capítulo YouTube:** La densidad espectral nunca baja de cero

## Narración

<!-- b1 -->
La conclusión, como fórmula: la densidad espectral es mayor o igual que cero en todas las frecuencias. Comprobémoslo con la telegráfica: cuatro dividido entre cuatro más omega al cuadrado. El numerador es positivo, y el denominador es cuatro más un cuadrado, también positivo. Nunca baja de cero.

- «La conclusión, como fórmula» → `conclusion`: corte seco; se construye «S_xx(jω)» por piezas
- «mayor o igual que cero» → `mayor`: «≥ 0» entra en ámbar
- «en todas las frecuencias» → `todas`: «para todo ω» se completa y una banda verde cubre todo el eje
- «Comprobémoslo con la telegráfica» → `tele`: la curva 4/(4 + ω²) se dibuja sobre el eje ω
- «cuatro dividido entre cuatro más omega al cuadrado» → `formula`: junto a la curva se escribe «4 / (4 + ω²)»
- «El numerador es positivo» → `numerador`: el «4» de arriba se resalta con un tilde
- «el denominador es cuatro más un cuadrado» → `denominador`: «4 + ω²» se resalta, con ω² marcado como «≥ 0»
- «también positivo» → `tambien`: un tilde verde junto al denominador
- «Nunca baja de cero» → `nunca`: la curva se queda sobre el eje con un tilde verde

<!-- b2 -->
Esta propiedad sale de la potencia. Hay otras dos que salen de la autocorrelación, y con las tres juntas vamos a poder hacer algo muy útil: decidir si una función cualquiera puede ser, o no, la autocorrelación de un proceso.

- «Esta propiedad sale de la potencia» → `primera`: una casilla «≥ 0 · sale de la potencia» queda marcada
- «otras dos» → `otras`: aparecen dos casillas vacías más
- «las tres juntas» → `juntas`: las tres casillas se alinean como un examen de tres preguntas
- «decidir si una función cualquiera» → `decidir`: a la izquierda entra una curva cualquiera con un «?»
- «la autocorrelación de un proceso» → `autocorr`: la curva lleva la etiqueta «¿R_xx(τ)?»

---

# Escena 05 — LaAutocorrelacionEsPar

**Capítulo YouTube:** Por qué el espectro es real

## Narración

<!-- b1 -->
Del capítulo anterior sabemos que la autocorrelación es real y par. Par quiere decir simétrica como en un espejo: vale lo mismo en tau que en menos tau. Tiene sentido: parecerse a uno mismo un segundo después es lo mismo que parecerse a uno mismo un segundo antes.

- «real y par» → `realpar`: aparece «R_xx(τ)» con las etiquetas «real» y «par»
- «simétrica como en un espejo» → `espejo`: la curva e^{−2|τ|} con una línea vertical en el cero como espejo
- «en tau que en menos tau» → `taumenos`: dos puntos a igual altura en τ y −τ, unidos por una línea horizontal
- «parecerse a uno mismo» → `parecerse`: una señal y su copia desplazada, parecidas, unidas por una doble flecha
- «un segundo después» → `despues`: una flecha hacia la derecha, «+1 s»
- «un segundo antes» → `antes`: una flecha hacia la izquierda, «−1 s», con el mismo valor

<!-- b2 -->
Ahora mira la transformada. La exponencial compleja es un coseno menos jota por un seno, así que la transformada tiene dos partes. La que lleva jota es el área de la autocorrelación multiplicada por un seno. Y el seno es impar: en menos tau vale lo contrario que en tau. Par por impar da una función impar.

- «Ahora mira la transformada» → `transf`: corte seco; aparece «S_xx = ∫ R_xx(τ) e^{−jωτ} dτ»
- «La exponencial compleja» → `expcompleja`: «e^{−jωτ}» se resalta dentro de la integral
- «un coseno menos jota por un seno» → `cosseno`: la exponencial se abre en «cos(ωτ) − j sen(ωτ)»
- «dos partes» → `partes`: la integral se parte en dos renglones, uno con coseno y otro con j y seno
- «La que lleva jota» → `lleva`: el renglón con j se resalta
- «multiplicada por un seno» → `porseno`: el renglón con j muestra «R_xx(τ) · sen(ωτ)»
- «Y el seno es impar» → `impar`: el seno se dibuja y su valor en −τ es el opuesto, con la etiqueta «impar»
- «lo contrario que en tau» → `contrario`: dos puntos, uno arriba y otro abajo, en τ y −τ
- «Par por impar da una función impar» → `parimpar`: aparece «par × impar = impar» y se dibuja el producto

---

# Escena 06 — RealYPar

**Capítulo YouTube:** Real y par, demostrado

## Narración

<!-- b1 -->
Y el área de una función impar es cero, porque lo de la izquierda cancela lo de la derecha. Si en tau igual a uno el producto vale cero coma uno, en menos uno vale menos cero coma uno. Así en cada pareja de puntos. La parte con jota desaparece, y queda solo el área de la autocorrelación por un coseno: un número real.

- «el área de una función impar es cero» → `areacero`: la función impar con su área a cada lado del cero, una positiva y otra negativa
- «lo de la izquierda cancela lo de la derecha» → `cancela`: las dos áreas se juntan y se anulan
- «en tau igual a uno» → `tau1`: un punto en τ = 1 con la etiqueta «+0,1»
- «en menos uno vale» → `menos1`: un punto en τ = −1 con la etiqueta «−0,1»
- «cada pareja de puntos» → `parejas`: aparecen más parejas con su suma «0»
- «La parte con jota desaparece» → `jota`: el renglón con j se tacha
- «queda solo el área» → `queda`: el renglón con coseno se resalta
- «un número real» → `real`: queda «S_xx = ∫ R_xx(τ) cos(ωτ) dτ» con la etiqueta «real»

<!-- b2 -->
Además, el coseno no cambia si le das la vuelta a omega. Así que la densidad espectral vale lo mismo en omega que en menos omega: es par. Real y par, demostrado. Esa es la razón de la simetría de las dos ventanitas del colador.

- «el coseno no cambia» → `coseno`: «cos(−ωτ) = cos(ωτ)» se escribe
- «le das la vuelta a omega» → `vuelta`: la curva del coseno se refleja con una flecha curva
- «Así que la densidad espectral» → `asique`: aparece «S_xx(jω) = S_xx(−jω)»
- «en omega que en menos omega» → `omegamenos`: la curva de la telegráfica con dos puntos a igual altura en ω y −ω
- «Real y par, demostrado» → `demostrado`: dos tildes verdes, «real» y «par»
- «la simetría» → `simetria`: una línea de simetría vertical sobre el espectro
- «las dos ventanitas del colador» → `ventanitas`: sobre la curva aparecen las dos ventanitas simétricas

<!-- b3 -->
Veámoslo en un ejemplo de tiempo discreto, donde la frecuencia solo va de menos pi a pi. Una autocorrelación de tres barras: cero coma cuatro, uno, cero coma cuatro. Su transformada tiene dos exponenciales, una con más jota y otra con menos jota. Al sumarlas, los senos se cancelan y queda uno más cero coma ocho por el coseno de omega. Real y par, a la vista.

- «tiempo discreto» → `discreto`: corte seco; aparece la etiqueta «tiempo discreto»
- «de menos pi a pi» → `pipi`: un eje de frecuencia Ω con marcas en −π, 0 y π
- «tres barras» → `barras`: tres barras en −1, 0 y 1
- «cero coma cuatro, uno, cero coma cuatro» → `alturas`: las barras se rotulan «0,4», «1» y «0,4»
- «Su transformada» → `sutransf`: aparece «S(Ω) =» a la derecha de las barras
- «dos exponenciales» → `dosexp`: aparece «0,4 e^{jΩ} + 1 + 0,4 e^{−jΩ}»
- «con más jota» → `masj`: el primer término se resalta
- «con menos jota» → `menosj`: el tercer término se resalta
- «los senos se cancelan» → `cancelan`: las partes con j se tachan
- «uno más cero coma ocho» → `ochos`: queda «1 + 0,8 cos Ω»
- «Real y par, a la vista» → `vista`: se dibuja la curva 1 + 0,8 cos Ω entre −π y π, simétrica

---

# Escena 07 — Rectangulo

**Capítulo YouTube:** El rectángulo no aprueba

## Narración

<!-- b1 -->
Te proponen dos funciones y te preguntan cuál puede ser la autocorrelación de algún proceso. Un rectángulo, que vale uno entre menos uno y uno, y cero fuera. Y un triángulo, que vale dos en el origen y baja en línea recta hasta cero en más y menos dos. ¿Las dos, ninguna, o solo una? Piénsalo antes de seguir.

- «dos funciones» → `dos`: corte seco; dos recuadros vacíos lado a lado
- «la autocorrelación de algún proceso» → `autocorr`: sobre los dos recuadros entra «¿R_xx(τ)?»
- «Un rectángulo» → `rect`: en el primero se dibuja el rectángulo de altura 1 entre −1 y 1
- «entre menos uno y uno» → `entre`: se marcan −1 y 1 en el eje
- «Y un triángulo» → `tri`: en el segundo se dibuja el triángulo
- «vale dos en el origen» → `dos_origen`: la altura 2 en el cero se marca
- «hasta cero en más y menos dos» → `cero2`: se marcan −2 y 2 en el eje del triángulo
- «¿Las dos, ninguna, o solo una?» → `encuesta`: aparecen tres opciones, «las dos», «ninguna», «solo una»
- «Piénsalo antes de seguir» → `pausa`: un reloj de arena se vacía

<!-- b2 -->
El rectángulo es real, es par, y vale lo máximo en el origen. Parece que lo tiene todo. Falta la tercera pregunta, que se contesta en frecuencia. Su transformada es dos por el seno de omega dividido entre omega: una función que se llama sinc. Oscila, y no siempre por encima de cero.

- «es real, es par» → `realpar`: dos casillas «real ✓» y «par ✓» junto al rectángulo
- «lo máximo en el origen» → `maximo`: una marca en el cero sobre el pico
- «Parece que lo tiene todo» → `todo`: un tilde verde junto al rectángulo
- «Falta la tercera pregunta» → `tercera`: aparece una tercera casilla «≥ 0 ?» vacía
- «que se contesta en frecuencia» → `enfrec`: una flecha lleva el rectángulo a un eje de frecuencias
- «dos por el seno de omega» → `dosseno`: se construye «2 sen ω / ω» por piezas
- «se llama sinc» → `sinc`: la palabra «sinc» entra con rebote y se dibuja la curva
- «no siempre por encima de cero» → `negativa`: los lóbulos bajo el eje se tiñen de rojo

<!-- b3 -->
Con un número: en omega igual a cuatro coma siete, el seno vale menos uno, y la transformada da unos menos cero coma cuatro dos. Negativa. En esa frecuencia, la densidad espectral sería negativa, y eso es imposible. Así que el rectángulo, por razonable que parezca, no es la autocorrelación de ningún proceso.

- «cuatro coma siete» → `w47`: un punto sobre la curva en ω ≈ 4,7
- «el seno vale menos uno» → `senomenos`: «sen 4,7 ≈ −1»
- «menos cero coma cuatro dos» → `valor`: la etiqueta «≈ −0,42» junto al punto
- «Negativa» → `negativa`: la casilla «≥ 0 ?» se vuelve «≥ 0 ✗» en rojo
- «En esa frecuencia» → `enesa`: una línea vertical marca ω ≈ 4,7
- «la densidad espectral sería negativa» → `serianeg`: el valor −0,42 se tiñe de rojo bajo el eje
- «eso es imposible» → `imposible`: sello «potencia negativa»
- «por razonable que parezca» → `razonable`: el rectángulo queda con una cruz roja grande
- «ningún proceso» → `ninguno`: la cruz roja queda sobre «R_xx(τ)» del rectángulo

---

# Escena 08 — Triangulo

**Capítulo YouTube:** El triángulo sí aprueba

## Narración

<!-- b1 -->
El triángulo esconde un truco. Recuerda la convolución de Señales y Sistemas: deslizas una función sobre otra y, en cada posición, mides el área común. Desliza el rectángulo sobre sí mismo. Sin desplazamiento, el área común es dos. Desplazado uno, es uno. Desplazado dos, cero. Sube y baja en línea recta: el triángulo.

- «esconde un truco» → `truco`: corte seco; el triángulo aparece con un interrogante
- «la convolución» → `convo`: la palabra «convolución» entra con rebote
- «deslizas una función sobre otra» → `deslizas`: dos rectángulos, uno se desliza sobre el otro
- «mides el área común» → `comun`: dos rectángulos se superponen y su zona común se sombrea
- «Desliza el rectángulo sobre sí mismo» → `desliza`: un rectángulo se desliza sobre el otro
- «Sin desplazamiento» → `d0`: desplazamiento 0, área común «2», un punto en el gráfico de abajo
- «Desplazado uno» → `d1`: desplazamiento 1, área común «1», segundo punto
- «Desplazado dos» → `d2`: desplazamiento 2, área común «0», tercer punto
- «Sube y baja» → `sube`: una línea quebrada une los tres puntos
- «el triángulo» → `triangulo`: los puntos se unen y dibujan el triángulo

<!-- b2 -->
Y la transformada de una convolución es el producto de las transformadas: sinc por sinc, la sinc al cuadrado. Un cuadrado nunca es negativo, así que el triángulo aprueba. Guarda el dibujo del rectángulo deslizándose sobre otro: volverá cuando intentemos medir un espectro con datos, y será la causa de casi todos los problemas.

- «la transformada de una convolución» → `transfconv`: aparece «F{a ∗ b}»
- «el producto de las transformadas» → `producto`: se completa «= F{a} · F{b}»
- «la sinc al cuadrado» → `sinc2`: «sinc · sinc = sinc²» y se dibuja la curva, toda sobre el eje
- «Un cuadrado nunca es negativo» → `cuadrado`: un «≥ 0» verde junto a la curva
- «el triángulo aprueba» → `aprueba`: tilde verde grande junto al triángulo
- «Guarda el dibujo» → `guarda`: los dos rectángulos deslizantes quedan en una esquina con un candado
- «volverá» → `volvera`: el candado con los rectángulos parpadea
- «medir un espectro con datos» → `datos`: una grabación corta con su periodograma al lado
- «la causa de casi todos los problemas» → `causa`: un «?» rojo junto al triángulo

---

# Escena 09 — CorrelacionAUnPaso

**Capítulo YouTube:** Un proceso que solo recuerda a su vecino

## Narración

<!-- b1 -->
Imagina un proceso en tiempo discreto en el que cada muestra se parece a sus vecinas inmediatas, con un coeficiente de correlación rho, y no tiene ninguna relación con las demás. Su autocovarianza son tres barras: rho, uno, rho. En el capítulo siete vimos que rho puede ir de menos uno a uno. ¿Puede valer aquí cero coma seis?

- «cada muestra se parece a sus vecinas» → `vecinas`: una fila de muestras donde cada una se parece a las dos de al lado
- «coeficiente de correlación rho» → `rho`: aparece «ρ» entre vecinas
- «ninguna relación con las demás» → `ninguna`: las muestras lejanas se unen con una línea cortada y un «0»
- «Su autocovarianza» → `autocov`: aparece «C_xx[m]» sobre la fila de muestras
- «tres barras: rho, uno, rho» → `barras`: la autocovarianza como tres barras «ρ · 1 · ρ»
- «En el capítulo siete» → `cap7`: aparece una etiqueta «capítulo 7»
- «de menos uno a uno» → `rango`: un segmento de −1 a 1 con un punto
- «¿Puede valer aquí cero coma seis?» → `pregunta`: el punto se mueve a 0,6 con un signo de pregunta

<!-- b2 -->
Pasemos el examen. Ya sabemos que el espectro de esas tres barras es uno más dos rho por el coseno de omega. Con rho igual a cero coma cuatro, en frecuencia cero vale uno coma ocho; en pi medios, uno; y en pi, cero coma dos. Siempre positivo: el proceso existe. Y tiene más potencia en las frecuencias bajas, porque vecinas parecidas dan una señal que cambia despacio.

- «Pasemos el examen» → `examen`: aparecen las tres casillas del examen
- «el espectro de esas tres barras» → `espectro`: las tres barras se transforman en una curva con flecha
- «uno más dos rho por el coseno de omega» → `formula`: se construye «1 + 2ρ cos Ω» por piezas
- «rho igual a cero coma cuatro» → `rho04`: ρ = 0,4 en la fórmula
- «uno coma ocho» → `t18`: fila «Ω = 0 → 1,8»
- «en pi medios, uno» → `t1`: fila «π/2 → 1»
- «en pi, cero coma dos» → `t02`: fila «π → 0,2»
- «Siempre positivo» → `positivo`: la curva se dibuja sobre el eje con un tilde verde
- «el proceso existe» → `existe`: tilde verde grande junto a «ρ = 0,4»
- «más potencia en las frecuencias bajas» → `bajas`: el bulto en Ω = 0 se resalta
- «vecinas parecidas» → `parecidas`: dos muestras vecinas con valores casi iguales
- «cambia despacio» → `despacio`: arriba, una señal suave que cambia despacio

<!-- b3 -->
Ahora con cero coma seis. En frecuencia pi, el coseno vale menos uno: uno menos uno coma dos, menos cero coma dos. Negativo. Ese proceso no puede existir. En general, el punto más bajo es uno menos dos veces el valor absoluto de rho, y para que no baje de cero, rho tiene que estar entre menos un medio y un medio.

- «Ahora con cero coma seis» → `rho06`: un `ValueTracker` sube ρ de 0,4 a 0,6 y el mínimo baja
- «el coseno vale menos uno» → `cos`: «cos π = −1» en Ω = π
- «uno menos uno coma dos» → `cuenta`: «1 − 1,2»
- «Negativo» → `negativo`: «= −0,2» en rojo y el mínimo se hunde bajo el eje
- «no puede existir» → `noexiste`: sello «no existe»
- «el punto más bajo» → `bajo`: se marca el mínimo de la curva en Ω = π
- «uno menos dos veces el valor absoluto de rho» → `formula`: aparece «1 − 2|ρ|» junto al mínimo
- «para que no baje de cero» → `nobaje`: el mínimo toca el eje
- «entre menos un medio y un medio» → `medio`: se escribe «1 − 2|ρ| ≥ 0 → |ρ| ≤ ½» y el segmento de ρ se acorta a [−½, ½]

---

# Escena 10 — ElLimiteDeUnMedio

**Capítulo YouTube:** Por qué rho no pasa de un medio

## Narración

<!-- b1 -->
Es una sorpresa: el capítulo siete permitía llegar hasta uno, y aquí solo llegamos a la mitad. ¿Por qué? Si cada muestra se pareciera muchísimo a la siguiente, y esa a la siguiente, la primera tendría que parecerse también a la tercera. Pero hemos dicho que a dos pasos no hay ninguna relación. Pedir las dos cosas a la vez es contradictorio.

- «Es una sorpresa» → `sorpresa`: corte seco; «capítulo 7: |ρ| ≤ 1» y debajo «aquí: |ρ| ≤ ½»
- «hasta uno» → `hastauno`: el «1» del capítulo 7 se resalta
- «solo llegamos a la mitad» → `mitad`: el «1» se tacha a medias y queda «½» en ámbar
- «¿Por qué?» → `porque`: un gran «¿por qué?»
- «muchísimo a la siguiente» → `mucho`: tres muestras en fila, primera y segunda unidas por una flecha gruesa
- «y esa a la siguiente» → `esa`: una segunda flecha gruesa entre la segunda y la tercera muestra
- «también a la tercera» → `tercera`: una flecha cortada une la primera con la tercera, «se parecen»
- «a dos pasos no hay ninguna relación» → `dospasos`: la misma flecha con un «0» y una cruz
- «Pedir las dos cosas a la vez» → `pedir`: las dos flechas se acercan
- «contradictorio» → `contradictorio`: las dos flechas chocan con un destello rojo

<!-- b2 -->
El examen dice qué es imposible. Pero ¿y lo que aprueba? Que el espectro salga positivo, ¿garantiza que existe de verdad un proceso con rho igual a cero coma cuatro? ¿Y cómo se fabricaría?

- «qué es imposible» → `imposible`: una cruz roja sobre una curva que se hunde
- «lo que aprueba» → `aprueba`: un tilde verde sobre 1 + 0,8 cos Ω
- «salga positivo» → `positivo`: la curva con un «≥ 0»
- «garantiza que existe de verdad» → `garantiza`: un signo de pregunta sobre un bloque vacío
- «un proceso con rho igual a cero coma cuatro» → `proceso04`: aparece «ρ = 0,4» dentro del bloque
- «¿Y cómo se fabricaría?» → `fabricar`: un signo de pregunta grande en ámbar y una rueda dentada vacía al lado

---

# Escena 11 — Bochner

**Capítulo YouTube:** El teorema de Bochner

## Narración

<!-- b1 -->
La respuesta es sí, y tiene nombre: el teorema de Bochner, o de Herglotz en tiempo discreto. Dice que la vuelta también vale: cualquier función real, par, que nunca baja de cero y con área finita es la densidad espectral de algún proceso. Y lo mejor es que se puede comprobar fabricándolo. Vamos a construir rho igual a cero coma cuatro.

- «La respuesta es sí» → `si`: corte seco; un «sí» grande verde
- «el teorema de Bochner» → `bochner`: «Bochner» entra con rebote
- «Herglotz» → `herglotz`: «Herglotz · tiempo discreto» aparece debajo
- «la vuelta también vale» → `vuelta`: una flecha de ida (autocorrelación → real, par, ≥ 0) y otra de vuelta en ámbar
- «real, par, que nunca baja de cero» → `tres`: las tres casillas junto a la flecha de vuelta
- «es la densidad espectral de algún proceso» → `existe`: la flecha de vuelta termina en «existe un proceso»
- «Y lo mejor» → `mejor`: una estrella ámbar junto al bloque
- «fabricándolo» → `fabricando`: aparece un bloque vacío con entrada y salida
- «construir rho igual a cero coma cuatro» → `rho04`: sobre el bloque entra «ρ = 0,4» y «1 + 0,8 cos Ω»

<!-- b2 -->
El ingrediente es una moneda: en cada instante sale más uno o menos uno, y cada tirada es independiente de las demás. Con ella montamos un filtro de dos coeficientes: la salida es dos veces la moneda de ahora más una vez la moneda anterior, todo dividido entre raíz de cinco.

- «una moneda» → `moneda`: aparece la moneda
- «más uno o menos uno» → `pm1`: sale la tira «+1, −1, −1, +1…»
- «independiente de las demás» → `indep`: las tiradas se separan con un «independientes»
- «un filtro de dos coeficientes» → `filtro`: la tira entra al bloque de filtro con dos casillas
- «dos veces la moneda de ahora» → `dos`: «2 w[n]» entra en la fórmula
- «una vez la moneda anterior» → `uno`: «+ w[n−1]» se suma
- «raíz de cinco» → `raiz5`: todo se divide entre «√5» y la fórmula completa «y[n] = (2 w[n] + w[n−1]) / √5» queda armada

---

# Escena 12 — LasCuentasDeBochner

**Capítulo YouTube:** Fabricar rho y su límite

## Narración

<!-- b1 -->
Hagamos las cuentas. La potencia de la salida: dos al cuadrado más uno al cuadrado, cinco, dividido entre cinco: uno. Los productos cruzados se promedian a cero porque las monedas son independientes. Y dos salidas vecinas comparten una moneda, que aparece con peso uno en una y dos en la otra: dos por uno entre cinco, cero coma cuatro. Fabricado.

- «La potencia de la salida» → `potencia`: aparece «E[y²] =»
- «dos al cuadrado más uno al cuadrado» → `cuadrados`: «(2² + 1²)»
- «dividido entre cinco: uno» → `uno`: «/ 5 = 1» en ámbar
- «Los productos cruzados» → `cruzados`: los productos cruzados de la expansión se resaltan
- «independientes» → `indep`: los cruzados se tachan y quedan en «0»
- «comparten una moneda» → `comparten`: dos salidas vecinas unidas por la moneda común, resaltada
- «peso uno en una y dos en la otra» → `pesos`: sobre la moneda común, «1» hacia una salida y «2» hacia la otra
- «dos por uno entre cinco» → `dospor`: «2 · 1 / 5»
- «Fabricado» → `fabricado`: «= 0,4» con un tilde verde

<!-- b2 -->
¿Y si intentamos cero coma seis? Con coeficientes a y be, necesitamos que a al cuadrado más be al cuadrado valga uno, y a por be, cero coma seis. Entonces a menos be, al cuadrado, vale uno menos dos por cero coma seis: menos cero coma dos. Un cuadrado negativo. No hay números que lo cumplan: el mismo límite que dio el espectro.

- «¿Y si intentamos cero coma seis?» → `seis`: corte seco; «ρ = 0,6» con un signo de pregunta
- «Con coeficientes a y be» → `coefs`: aparece el filtro «a w[n] + b w[n−1]»
- «a al cuadrado más be al cuadrado valga uno» → `suma`: «a² + b² = 1»
- «a por be, cero coma seis» → `prod`: «a b = 0,6»
- «a menos be, al cuadrado» → `resta`: «(a − b)² =» se arma
- «vale uno menos dos por cero coma seis» → `vale`: se escribe «1 − 2 · 0,6»
- «menos cero coma dos» → `menos02`: «= 1 − 1,2 = −0,2» en rojo
- «Un cuadrado negativo» → `cuadneg`: el cuadrado con un signo menos y un sello rojo
- «No hay números que lo cumplan» → `nohay`: una cruz roja sobre las ecuaciones
- «el mismo límite» → `limite`: a su lado el «−0,2» del espectro en π y un signo igual

<!-- b3 -->
No es casualidad: preguntar si el espectro es positivo y preguntar si existe un filtro que fabrique el proceso es la misma pregunta. Eso dice Bochner. Y mira los extremos: con rho igual a un medio, los dos coeficientes son iguales y el filtro promedia vecinas, como el promediador del capítulo anterior; con menos un medio, las resta. Guarda este filtro: volverá.

- «No es casualidad» → `casualidad`: corte seco; aparece un signo igual vacío
- «preguntar si el espectro es positivo» → `preg1`: a la izquierda entra «espectro ≥ 0»
- «preguntar si existe un filtro» → `preg2`: a la derecha entra «existe el filtro»
- «la misma pregunta» → `misma`: «espectro ≥ 0» y «existe el filtro» unidos por un signo de equivalencia
- «Eso dice Bochner» → `dicebochner`: el rótulo «Bochner» sobre la equivalencia
- «los extremos» → `extremos`: dos casillas para ρ = ½ y ρ = −½
- «rho igual a un medio» → `medio`: el primer filtro con coeficientes iguales
- «los dos coeficientes son iguales» → `iguales`: «(1, 1)/√2» aparece
- «promedia vecinas» → `promedia`: la salida se suaviza
- «con menos un medio» → `menosmedio`: el segundo filtro con coeficientes opuestos
- «las resta» → `resta`: «(1, −1)/√2» y la salida alterna de signo
- «Guarda este filtro» → `guarda`: el filtro (2, 1)/√5 queda en una esquina con un candado y la etiqueta «volverá»

---

# Escena 13 — Cierre

**Capítulo YouTube:** Lo que viene: el color del ruido

## Narración

<!-- b1 -->
Repasemos. Un espectro nunca baja de cero, es real y par, y con esas reglas sabemos qué correlaciones existen: cero coma cuatro sí, cero coma seis no. Además, todo espectro que aprueba se puede fabricar con un filtro. Pero ¿cómo es el espectro de un ruido que no recuerda nada, y el de uno que lo recuerda todo? En el próximo episodio: el color del ruido.

- «nunca baja de cero» → `nunca`: una curva sobre el eje con un tilde verde
- «real y par» → `realpar`: la curva se refleja en un espejo vertical
- «con esas reglas» → `reglas`: las tres casillas del examen aparecen en fila
- «cero coma cuatro sí» → `si`: «ρ = 0,4 ✓» en verde
- «cero coma seis no» → `no`: «ρ = 0,6 ✗» en rojo
- «todo espectro que aprueba» → `aprueba`: un tilde verde sobre la curva 1 + 0,8 cos Ω
- «se puede fabricar con un filtro» → `fabricar`: la moneda entra en el bloque de filtro y sale un proceso
- «¿cómo es el espectro» → `comoes`: aparece un eje de frecuencias vacío con un signo de pregunta
- «un ruido que no recuerda nada» → `sinmemoria`: una línea plana de espectro junto a una única barra de autocovarianza
- «lo recuerda todo» → `todo`: dos rayas de espectro junto a un coseno que no decae
- «el color del ruido» → `titulo_e3`: entra el título del siguiente episodio sobre un prisma de colores
