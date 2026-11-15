# Episodio 1 — ¿En qué frecuencias vive el azar?

Capítulo 11 (Densidad espectral de potencia), episodio 1 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 01 a 05), más un gancho y un cierre nuevos.

**Estado:** escenas `s01`–`s14` escritas y `ritmo.py` corrido (huecos cubiertos con momentos extra). Borrador 480p15 de 10:17, **0 avisos**, hojas de contacto revisadas. Sigue: el usuario mira `salida/E1_En_que_frecuencias_vive_el_azar-480p15.mp4` y revisa el texto ⭐ (pasos 9 y 15); después render final `--calidad qh` (paso 16).

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Grabas un ruido y le aplicas Fourier… No funciona. Y sin embargo, el ruido sí tiene una curva que dice en qué frecuencias vive su potencia.»
- ⭐ Escena 14 (cierre): resumen y anuncia E2 por su título, «Lo que un espectro no puede hacer».

Nota para el episodio anterior: el cierre del último episodio del Cap. 10 tiene que anunciar este título, «¿En qué frecuencias vive el azar?».

Reparto de las escenas del guion base: 01 → escenas 03 y 04; 02 → 05 y 06; 03 → 07 a 09; 04 → 10 y 11; 05 → 12 y 13.
Solo se partieron bloques enteros en escenas atómicas: el texto del guion base no cambia.

---

# Escena 01 — Gancho

**Capítulo YouTube:** Un ruido sin espectro

## Narración

<!-- b1 -->
Grabas un ruido y le aplicas Fourier, como a cualquier señal. No funciona. Y sin embargo, el ruido sí tiene una curva que dice en qué frecuencias vive su potencia. Hoy vemos cómo se consigue.

- «Grabas un ruido» → `ruido`: aparece una traza de ruido magenta que avanza
- «le aplicas Fourier» → `fourier`: una flecha lleva la traza a una caja «Fourier»
- «No funciona» → `nofunciona`: la salida se llena de picos caóticos y una cruz roja los tacha
- «una curva» → `curva`: sobre un eje de frecuencias se dibuja la curva suave 4/(4 + ω²) en ámbar
- «en qué frecuencias vive su potencia» → `potencia`: el área bajo la curva se sombrea y entra la etiqueta «potencia»
- «Hoy vemos» → `hoy`: una flecha punteada va del ruido a la curva ámbar, con un «¿cómo?»

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** ¿En qué frecuencias vive el azar?

## Narración

<!-- b1 -->
¿En qué frecuencias vive el azar?

- «¿En qué frecuencias» → `t1`: «¿En qué frecuencias» entra con rebote
- «vive el azar?» → `t2`: «vive el azar?» entra debajo, con la etiqueta «Capítulo 11 · Densidad espectral de potencia»

---

# Escena 03 — LaPregunta

**Capítulo YouTube:** Voz, murmullo y Fourier

## Narración

<!-- b1 -->
Imagina una grabación en la que alguien habla y, de fondo, hay un murmullo constante. Queremos limpiarla. Para eso existe una herramienta de Señales y Sistemas: el filtro, un colador que deja pasar unas frecuencias y retiene otras. Pero para diseñar el colador hay que saber algo antes: en qué frecuencias vive la voz, y en cuáles vive el ruido.

- «alguien habla» → `voz`: entra una persona y su onda de voz azul
- «un murmullo constante» → `murmullo`: se suma una traza magenta debajo de la voz
- «Queremos limpiarla» → `limpiar`: la mezcla cian queda en el centro con un «?» hacia la salida
- «una herramienta de Señales y Sistemas» → `herramienta`: la etiqueta «Señales y Sistemas» entra sobre el hueco del colador
- «el filtro» → `filtro`: aparece el ícono del colador entre la mezcla y la salida
- «un colador que deja pasar unas frecuencias» → `colador`: unas barras atraviesan el colador y otras rebotan
- «y retiene otras» → `retiene`: las barras que rebotan se marcan en rojo
- «hay que saber algo antes» → `saber`: el colador queda con un signo de pregunta encima
- «en qué frecuencias vive la voz» → `vive_voz`: un eje de frecuencias vacío con la etiqueta «voz» azul y un signo de pregunta
- «y en cuáles vive el ruido» → `vive_ruido`: en el mismo eje, la etiqueta «ruido» magenta y su signo de pregunta

<!-- b2 -->
Recordemos qué quiere decir eso. Toma un seno lento, que se repite dos veces por segundo, y súmale uno rápido, que se repite cinco veces por segundo. La suma tiene una forma rara, difícil de leer. Pero la transformada de Fourier la desarma: dice que hay un seno de dos hercios y otro de cinco. Un hercio es una vez por segundo.

- «un seno lento» → `lento`: se dibuja un seno azul lento
- «dos veces por segundo» → `dos`: una llave de 1 s marca dos ciclos dentro
- «súmale uno rápido» → `rapido`: se dibuja un seno rápido debajo
- «cinco veces por segundo» → `cinco`: la misma llave de 1 s marca cinco ciclos
- «La suma tiene una forma rara» → `suma`: los dos se suman en una curva irregular arriba
- «difícil de leer» → `dificil`: un signo de pregunta junto a la suma
- «la transformada de Fourier» → `fourier`: una flecha lleva la suma a una caja «Fourier»
- «la desarma» → `desarma`: la suma se separa otra vez en los dos senos
- «un seno de dos hercios» → `b2hz`: sale una barra en «2 Hz»
- «y otro de cinco» → `b5hz`: sale una barra en «5 Hz»
- «Un hercio es una vez por segundo» → `hercio`: aparece «1 Hz = 1 vez por segundo» con un ciclo marcado

---

# Escena 04 — ElEspectroYElColador

**Capítulo YouTube:** El espectro y el colador

## Narración

<!-- b1 -->
El dibujo de cuánto hay de cada frecuencia es el espectro: aquí, dos barras. Y un filtro actúa sobre ese dibujo: multiplica cada barra por un número, su ganancia. Si la ganancia en cinco hercios es cero, esa barra desaparece, y en el tiempo queda solo el seno lento. Eso es el colador.

- «cuánto hay de cada frecuencia» → `cuanto`: las dos barras (2 Hz y 5 Hz) quedan solas sobre un eje
- «el espectro» → `espectro`: la palabra «espectro» entra con rebote sobre las barras
- «dos barras» → `dosbarras`: las dos barras se resaltan
- «Y un filtro actúa» → `filtro`: encima aparece una curva de ganancia que pasa por ambas barras
- «multiplica cada barra por un número» → `multiplica`: un «×» y un número flotan sobre cada barra
- «su ganancia» → `ganancia`: los números se rotulan «ganancia»
- «cinco hercios es cero» → `cero`: la ganancia en 5 Hz baja a cero
- «esa barra desaparece» → `desaparece`: la barra de 5 Hz se apaga
- «queda solo el seno lento» → `solo_lento`: abajo, en el tiempo, queda únicamente el seno lento
- «Eso es el colador» → `colador`: aparece el ícono del colador junto a la curva de ganancia

<!-- b2 -->
Con la voz pasa lo mismo, solo que su espectro no son dos barras sino un bulto, entre unos cientos y unos miles de hercios. Si el murmullo vive en otras frecuencias, el colador los separa sin problema. Si viven en las mismas, no hay colador que valga. Todo depende de conocer el espectro del ruido.

- «Con la voz» → `voz`: corte a un eje de frecuencias nuevo
- «un bulto» → `bulto`: un bulto azul se dibuja en el eje
- «entre unos cientos y unos miles de hercios» → `rango`: el eje se rotula con 300 Hz y 3.000 Hz
- «Si el murmullo vive» → `murmullo`: la etiqueta «murmullo» entra sobre el eje
- «otras frecuencias» → `otras`: un bulto magenta aparece lejos, en otro tramo del eje
- «el colador los separa» → `separa`: el colador deja pasar el azul y corta el magenta
- «en las mismas» → `mismas`: el bulto magenta se corre y se encima con el azul
- «no hay colador que valga» → `novale`: el colador se tacha con una cruz roja
- «Todo depende» → `depende`: el bulto magenta queda resaltado con un «?»

<!-- b3 -->
Así que la pregunta es: ¿cómo calcularías el espectro de un ruido? Piénsalo un momento antes de seguir. La respuesta obvia es grabarlo y aplicarle Fourier, como a los dos senos. Parece fácil. No funciona. Y entender por qué es la mitad de este capítulo.

- «¿cómo calcularías el espectro de un ruido?» → `pregunta`: aparece la pregunta grande en pantalla
- «Piénsalo un momento» → `pausa`: un reloj de arena se vacía
- «La respuesta obvia» → `obvia`: aparece «respuesta obvia» en ámbar
- «grabarlo» → `grabar`: una traza de ruido magenta se graba
- «aplicarle Fourier» → `aplicar`: la traza pasa a la caja «Fourier»
- «Parece fácil» → `facil`: un tilde verde junto a la caja
- «No funciona» → `nofunciona`: el tilde se vuelve una cruz roja
- «la mitad de este capítulo» → `mitad`: queda solo un «¿por qué?» en ámbar

---

# Escena 05 — LaEnergia

**Capítulo YouTube:** Energía finita, energía infinita

## Narración

<!-- b1 -->
Empecemos por la energía. En Señales y Sistemas, la energía de una señal es el área bajo su cuadrado. Un pulso que vale uno durante tres segundos tiene energía tres. Las señales que empiezan y terminan tienen energía finita, y para ellas la transformada de Fourier existe y se puede dibujar.

- «la energía» → `energia`: la palabra «energía» entra con rebote
- «En Señales y Sistemas» → `ss`: la etiqueta «Señales y Sistemas» en tinta
- «el área bajo su cuadrado» → `area`: aparece x²(t) y el área bajo la curva se sombrea
- «Un pulso que vale uno» → `pulso`: un pulso de altura 1 se dibuja
- «durante tres segundos» → `tres`: una llave marca «3 s» en su base
- «energía tres» → `e3`: aparece «E = 3» junto al área
- «empiezan y terminan» → `terminan`: dos marcas, inicio y fin, sobre el pulso
- «energía finita» → `finita`: «E finita» en verde
- «la transformada de Fourier existe» → `existe`: una flecha lleva el pulso a una caja «Fourier»
- «se puede dibujar» → `dibujar`: al lado aparece el espectro del pulso

<!-- b2 -->
Ahora toma un ruido estacionario, que es como llamamos en el capítulo anterior a un proceso cuyas reglas no cambian con el tiempo. Por ejemplo, la onda telegráfica: una señal que salta entre más uno y menos uno en instantes al azar. No empieza ni termina. Y su cuadrado vale uno en todo momento.

- «un ruido estacionario» → `estac`: corte seco a un plano nuevo con la etiqueta «estacionario»
- «en el capítulo anterior» → `anterior`: la etiqueta «capítulo 10» entra junto a la palabra
- «reglas no cambian con el tiempo» → `reglas`: dos tramos distintos de eje de tiempo con el mismo aspecto estadístico
- «la onda telegráfica» → `telegrafica`: se dibuja la onda telegráfica
- «entre más uno y menos uno» → `saltos`: los niveles +1 y −1 se rotulan
- «al azar» → `azar`: los instantes de salto se marcan irregulares
- «No empieza ni termina» → `infinita`: dos flechas en los extremos la alargan hacia los lados
- «su cuadrado vale uno» → `cuadrado`: debajo, el cuadrado es una línea plana en 1

<!-- b3 -->
Hagamos la cuenta. Al cabo de diez segundos, el área bajo el cuadrado vale diez. Al cabo de mil segundos, mil. Y la señal sigue para siempre, así que la energía total es infinita. Una señal de energía infinita no tiene una transformada que se pueda dibujar: como mucho, algo lleno de impulsos. Primer camino cerrado.

- «Hagamos la cuenta» → `cuenta`: aparece un contador de energía en cero
- «diez segundos» → `diez`: el área bajo la línea en 1 se sombrea hasta 10 s
- «vale diez» → `vale10`: el contador marca «10»
- «Al cabo de mil segundos, mil» → `mil`: el área llega a 1.000 s y el contador marca «1.000»
- «sigue para siempre» → `siempre`: el área sigue creciendo fuera del cuadro
- «energía total es infinita» → `inf`: el contador pasa a «∞»
- «Una señal de energía infinita» → `sinf`: la señal con el «∞» queda arriba, a la izquierda
- «no tiene una transformada» → `notiene`: una flecha hacia una caja «Fourier» con una cruz roja
- «algo lleno de impulsos» → `impulsos`: un espectro de picos verticales
- «Primer camino cerrado» → `cerrado`: una cruz roja numerada «1»

---

# Escena 06 — TresProblemas

**Capítulo YouTube:** Tres problemas y dos cambios

## Narración

<!-- b1 -->
Y hay un problema peor. Aunque pudiéramos transformarla, sería el espectro de esa grabación. Recuerda el ensemble: mil grabaciones del mismo fenómeno, una encima de otra. Cada una tiene su propio espectro, distinto en todos los detalles. Lo que buscamos es una propiedad del fenómeno, no de una de sus grabaciones.

- «un problema peor» → `peor`: corte seco, una traza de ruido sola
- «Aunque pudiéramos transformarla» → `transformarla`: una flecha lleva la traza a una caja «Fourier»
- «el espectro de esa grabación» → `espectro`: su espectro aparece al lado
- «el ensemble» → `ensemble`: la palabra «ensemble» entra con rebote
- «mil grabaciones del mismo fenómeno» → `mil`: la traza se multiplica en una pila de curvas
- «una encima de otra» → `encima`: las trazas se apilan unas sobre otras
- «su propio espectro» → `propio`: cada traza de la pila lleva su espectro al lado
- «distinto en todos los detalles» → `distinto`: los espectros se encimen y se ve que no coinciden
- «una propiedad del fenómeno» → `fenomeno`: un recuadro «fenómeno» envuelve toda la pila
- «no de una de sus grabaciones» → `grab`: una de las trazas se tacha

<!-- b2 -->
Tres problemas: dura para siempre, tiene energía infinita y es distinta cada vez. Y los tres se resuelven cambiando dos palabras. En lugar de energía, vamos a mirar potencia. Y en lugar de una grabación, vamos a promediar sobre todo el ensemble.

- «dura para siempre» → `p1`: primer renglón «no empieza ni termina» con una cruz roja
- «tiene energía infinita» → `p2`: segundo renglón «energía infinita» con cruz roja
- «distinta cada vez» → `p3`: tercer renglón «distinta cada vez» con cruz roja
- «cambiando dos palabras» → `dos`: aparecen dos casillas vacías de cambio
- «En lugar de energía» → `energia`: «energía» se tacha en la primera casilla
- «vamos a mirar potencia» → `potencia`: «potencia» entra en ámbar
- «en lugar de una grabación» → `grabacion`: «una grabación» se tacha en la segunda casilla
- «promediar sobre todo el ensemble» → `ensemble`: «ensemble» entra en ámbar, con la pila de curvas

---

# Escena 07 — PotenciaEsperada

**Capítulo YouTube:** De la energía a la potencia

## Narración

<!-- b1 -->
La potencia es energía por unidad de tiempo. Con la onda telegráfica: diez de energía en diez segundos da potencia uno. Mil en mil segundos, potencia uno otra vez. La energía crece sin parar, pero la potencia se queda quieta. Es finita, aunque la señal dure para siempre. Primer problema resuelto.

- «energía por unidad de tiempo» → `def`: aparece «potencia = energía / tiempo»
- «Con la onda telegráfica» → `tele`: una miniatura de la onda telegráfica entra a la izquierda
- «diez de energía en diez segundos» → `diez`: «10 / 10»
- «da potencia uno» → `p1`: «= 1» en ámbar
- «Mil en mil segundos» → `mil`: «1.000 / 1.000 = 1»
- «La energía crece sin parar» → `crece`: una gráfica de energía contra tiempo sube en línea recta
- «la potencia se queda quieta» → `quieta`: a su lado una línea horizontal en 1
- «Es finita» → `finita`: la línea se marca con un tilde verde
- «Primer problema resuelto» → `resuelto`: la cruz número 1 de antes se vuelve un tilde verde

<!-- b2 -->
Si la señal fuera la tensión sobre una resistencia de un ohmio, su cuadrado sería la potencia que se disipa en cada instante: la potencia instantánea. Ahora el segundo cambio: en un instante cualquiera, promediamos esa potencia sobre todas las grabaciones del ensemble. Es la esperanza de equis al cuadrado.

- «una resistencia de un ohmio» → `resist`: una resistencia de 1 Ω con la señal como tensión
- «su cuadrado» → `cuad`: aparece x²(t)
- «la potencia instantánea» → `inst`: x²(t) se rotula «potencia instantánea»
- «el segundo cambio» → `segundo`: la segunda casilla de cambio se resalta
- «en un instante cualquiera» → `corte`: la pila de realizaciones con un corte vertical en t
- «todas las grabaciones del ensemble» → `todas`: los cuadrados de todas las trazas en el corte se juntan en una fila
- «la esperanza de equis al cuadrado» → `esperanza`: se construye «E[x²(t)]» por piezas

---

# Escena 08 — AutocorrelacionEnCero

**Capítulo YouTube:** La potencia es la autocorrelación en cero

## Narración

<!-- b1 -->
Y esa esperanza ya tiene nombre. En el capítulo anterior definimos la autocorrelación: tomas la señal y una copia desplazada un tiempo tau, las multiplicas y promedias. Mide cuánto se parece la señal a sí misma tau segundos después. Con tau igual a cero, la copia coincide con la señal, y queda justo la esperanza de equis al cuadrado.

- «ya tiene nombre» → `nombre`: E[x²(t)] queda arriba con un signo de pregunta
- «la autocorrelación» → `auto`: aparece «R_xx(τ)»
- «una copia desplazada un tiempo tau» → `copia`: una copia de la señal se desplaza τ
- «las multiplicas y promedias» → `mult`: se construye «E[x(t) x(t − τ)]» por piezas
- «cuánto se parece la señal a sí misma» → `parece`: una doble flecha entre señal y copia
- «tau segundos después» → `despues`: una flecha rotulada «τ» une los dos primeros saltos
- «Con tau igual a cero» → `tau0`: la copia se desliza hasta τ = 0
- «la copia coincide con la señal» → `coincide`: las dos trazas se superponen
- «la esperanza de equis al cuadrado» → `igual`: aparece «R_xx(0) = E[x²(t)]»

---

# Escena 09 — LaAutocorrelacionSeApaga

**Capítulo YouTube:** Una curva que sí se apaga

## Narración

<!-- b1 -->
Así que la potencia esperada es la autocorrelación en cero. Y como el proceso es estacionario, da igual en qué instante la midas. Para la onda telegráfica, si salta en promedio una vez por segundo, la autocorrelación es e elevado a menos dos por el valor absoluto de tau. En cero vale uno: la potencia que contamos a mano.

- «la potencia esperada» → `esperada`: aparece «P» con la etiqueta «potencia esperada»
- «la autocorrelación en cero» → `encero`: «P = R_xx(0)»
- «es estacionario» → `estac`: la etiqueta «estacionario» en la pila de realizaciones
- «da igual en qué instante» → `igual`: el corte recorre la pila y el valor no cambia
- «Para la onda telegráfica» → `paratele`: una miniatura de la telegráfica entra a la derecha
- «si salta en promedio una vez por segundo» → `salta`: la telegráfica con sus saltos marcados
- «e elevado a menos dos» → `exp`: se construye «e^{−2|τ|}» por piezas
- «el valor absoluto de tau» → `abs`: se resalta «|τ|»
- «En cero vale uno» → `uno`: se dibuja la curva y un punto en 1 en τ = 0
- «la potencia que contamos a mano» → `mano`: el «1» se une con el «1» de la cuenta a mano

<!-- b2 -->
Fíjate en la forma de esa curva. A medio segundo vale cero coma tres siete; a un segundo, cero coma uno cuatro; y sigue bajando hacia cero. La señal no se apaga nunca, pero su autocorrelación sí. Es una función con área finita, y una función así sí tiene transformada de Fourier. Ahí está la salida.

- «la forma de esa curva» → `forma`: la curva e^{−2|τ|} queda sola en grande
- «A medio segundo» → `medio`: un punto sobre la curva en τ = 0,5
- «cero coma tres siete» → `t37`: etiqueta «0,37»
- «a un segundo» → `uno_s`: un punto en τ = 1
- «cero coma uno cuatro» → `t14`: etiqueta «0,14»
- «sigue bajando hacia cero» → `baja`: la cola se apoya en el eje
- «La señal no se apaga nunca» → `nunca`: arriba la telegráfica sigue oscilando
- «su autocorrelación sí» → `si`: abajo la curva se apaga
- «área finita» → `area`: el área bajo la curva se sombrea
- «transformada de Fourier» → `fourier`: una flecha lleva la curva a la caja «Fourier»
- «Ahí está la salida» → `salida`: la flecha se vuelve verde y aparece «salida»

---

# Escena 10 — LaTransformada

**Capítulo YouTube:** La densidad espectral de potencia

## Narración

<!-- b1 -->
Recordemos qué hace la transformada de Fourier. Para cada frecuencia omega, multiplica la función por una oscilación de esa frecuencia y calcula el área del producto. Si la función tiene mucho de esa frecuencia, el área es grande; si no tiene nada, el área es cero. Es una forma de preguntar, frecuencia por frecuencia, cuánto hay.

- «Para cada frecuencia omega» → `omega`: aparece la autocorrelación y un marcador «ω» con su valor
- «por una oscilación de esa frecuencia» → `oscila`: un coseno de frecuencia ω aparece sobre ella
- «el área del producto» → `producto`: el producto de ambas se dibuja abajo con su área sombreada
- «mucho de esa frecuencia» → `mucho`: con ω bajo el área es grande
- «si no tiene nada» → `nada`: con ω alto las partes positivas y negativas se compensan
- «el área es cero» → `cero`: aparece «área = 0»
- «frecuencia por frecuencia» → `freq`: ω barre y el área cambia
- «cuánto hay» → `cuanto`: una gran pregunta «¿cuánto hay?»

<!-- b2 -->
La oscilación se escribe con una exponencial compleja: e elevado a jota por un ángulo. La jota es la unidad imaginaria, la raíz de menos uno, y esa exponencial es una forma compacta de escribir un coseno y un seno a la vez. Así la transformada mide de una vez las dos oscilaciones de cada frecuencia.

- «una exponencial compleja» → `expo`: corte seco; aparece la palabra «exponencial compleja»
- «e elevado a jota por un ángulo» → `ejt`: se construye «e^{jθ}»
- «la unidad imaginaria» → `imag`: aparece «j»
- «la raíz de menos uno» → `raiz`: «j = √−1»
- «una forma compacta» → `compacta`: una llave junto al lado derecho
- «un coseno y un seno a la vez» → `cosen`: «= cos θ + j sen θ» se completa por piezas
- «Así la transformada mide» → `mide`: aparece una caja «Fourier» con una flecha hacia el coseno y el seno
- «las dos oscilaciones» → `dos`: a la derecha, el coseno y el seno dibujados

<!-- b3 -->
Al final del capítulo anterior le pusimos nombre a la transformada de la autocorrelación: densidad espectral de potencia. Se escribe ese sub equis equis de jota omega, y es la integral de la autocorrelación por e elevado a menos jota omega tau. Una curva sobre el eje de frecuencias. Ahora vamos a ver por qué se merece ese nombre.

- «le pusimos nombre» → `nombre`: corte seco; aparece R_xx(τ) con una flecha hacia un recuadro vacío
- «densidad espectral de potencia» → `dep`: el nombre completo entra en el recuadro
- «ese sub equis equis de jota omega» → `s`: aparece «S_xx(jω) =»
- «la integral de la autocorrelación» → `integral`: «∫ R_xx(τ)»
- «e elevado a menos jota omega tau» → `exp`: «e^{−jωτ} dτ»
- «Una curva sobre el eje de frecuencias» → `curva`: la curva 4/(4 + ω²) se dibuja sobre el eje ω
- «Ahora vamos a ver» → `ahora`: una flecha apunta a la curva
- «por qué se merece ese nombre» → `merece`: sobre la curva aparece un «¿densidad?» en ámbar

---

# Escena 11 — LaInversa

**Capítulo YouTube:** El área es la potencia total

## Narración

<!-- b1 -->
La transformada tiene inversa: la autocorrelación es uno sobre dos pi por la integral de la densidad por e elevado a jota omega tau. Pongamos tau igual a cero. La exponencial de cero vale uno, y desaparece. Queda que la potencia, la autocorrelación en cero, es el área bajo la densidad espectral dividida entre dos pi.

- «tiene inversa» → `inversa`: aparece «R_xx(τ) =»
- «uno sobre dos pi» → `dospi`: «1/2π»
- «la integral de la densidad» → `integral`: «∫ S_xx(jω)»
- «e elevado a jota omega tau» → `exp`: «e^{jωτ} dω»
- «Pongamos tau igual a cero» → `tau0`: τ se reemplaza por 0 en la fórmula
- «La exponencial de cero» → `expcero`: «e⁰» se resalta en la fórmula nueva
- «vale uno, y desaparece» → `desap`: la exponencial se vuelve «1» y se tacha
- «la potencia, la autocorrelación en cero» → `pot`: a la izquierda queda «R_xx(0)»
- «el área bajo la densidad espectral» → `area`: «∫ S_xx(jω) dω» se rodea como un área
- «dividida entre dos pi» → `div`: «1/2π» se resalta

<!-- b2 -->
Comprobémoslo con la telegráfica. Su densidad espectral es cuatro dividido entre cuatro más omega al cuadrado: haremos la cuenta en dos episodios. El área bajo esa curva vale dos pi. Dividida entre dos pi, da uno: la potencia que contamos a mano. El área total es la potencia total.

- «Comprobémoslo con la telegráfica» → `comprueba`: corte seco; la curva de la telegráfica aparece en el eje ω
- «Su densidad espectral» → `su`: el título «S_xx» aparece sobre la curva
- «cuatro dividido entre cuatro más omega al cuadrado» → `formula`: se construye «4 / (4 + ω²)» por piezas
- «haremos la cuenta en dos episodios» → `promesa`: una etiqueta «cuenta: episodio 3» con un candado
- «El área bajo esa curva vale dos pi» → `area`: el área se sombrea y aparece «2π»
- «Dividida entre dos pi, da uno» → `uno`: «2π / 2π = 1»
- «la potencia que contamos a mano» → `mano`: el «1» se une al «1» de la cuenta a mano
- «El área total es la potencia total» → `total`: «área total = potencia total» en ámbar

---

# Escena 12 — ElColadorIdeal

**Capítulo YouTube:** Un colador ideal de frecuencias

## Narración

<!-- b1 -->
Que el área total sea la potencia total no basta para llamar densidad a esta curva. Queremos más: que cada trozo de área sea la potencia de ese trozo de frecuencias. Para comprobarlo usamos un colador ideal: deja pasar tal cual una franja estrecha alrededor de una frecuencia, omega cero, y borra todo lo demás.

- «no basta para llamar densidad» → `nobasta`: la curva de la telegráfica con el «¿densidad?»
- «Queremos más» → `mas`: el «¿densidad?» pulsa en ámbar
- «cada trozo de área» → `trozo`: un trozo de área se sombrea
- «la potencia de ese trozo de frecuencias» → `potrozo`: el trozo se rotula «potencia de esta banda»
- «Para comprobarlo» → `comprobar`: una lupa pasa sobre el trozo de área
- «un colador ideal» → `ideal`: sobre la curva aparece una ventanita de ganancia 1
- «una franja estrecha» → `franja`: la ventanita se angosta
- «omega cero» → `w0`: un marcador «ω₀» en el centro de la franja
- «borra todo lo demás» → `borra`: la curva fuera de la franja se apaga

<!-- b2 -->
Un detalle: el espectro de una señal real es simétrico. Un seno de cinco hercios aparece como dos barras, en más cinco y en menos cinco. Así que el colador también tiene que ser simétrico: una ventanita en más omega cero y su reflejo en menos omega cero.

- «el espectro de una señal real es simétrico» → `simetrico`: un eje con el cero al centro y una línea de simetría
- «Un seno de cinco hercios» → `seno5`: se dibuja el seno de 5 Hz
- «dos barras» → `barras`: salen dos barras
- «en más cinco y en menos cinco» → `pm5`: las barras se rotulan «+5» y «−5»
- «el colador también tiene que ser simétrico» → `colsim`: vuelve la curva con el colador encima
- «una ventanita en más omega cero» → `vpos`: queda una ventanita en «+ω₀»
- «su reflejo en menos omega cero» → `vneg`: aparece su reflejo en «−ω₀»

---

# Escena 13 — PotenciaEnUnaBanda

**Capítulo YouTube:** El área sobre una banda es su potencia

## Narración

<!-- b1 -->
¿Qué hace un filtro con la potencia? Multiplica la amplitud de cada frecuencia por su ganancia. Y la potencia va con el cuadrado de la amplitud: si la ganancia es tres, la potencia se multiplica por nueve. Por eso, como vimos al final del capítulo anterior, a la salida la densidad espectral es la de la entrada por el módulo de la ganancia al cuadrado.

- «¿Qué hace un filtro con la potencia?» → `pregunta`: aparece la pregunta sobre un bloque de filtro
- «Multiplica la amplitud» → `amp`: un seno entra al filtro
- «por su ganancia» → `suganancia`: un «×» y la etiqueta «ganancia» sobre el bloque
- «el cuadrado de la amplitud» → `cuadamp`: aparece «amplitud²»
- «si la ganancia es tres» → `g3`: el seno sale con amplitud triplicada
- «la potencia se multiplica por nueve» → `p9`: aparece «× 9» sobre la potencia
- «Por eso» → `poreso`: una flecha baja del bloque al renglón de la fórmula
- «como vimos al final del capítulo anterior» → `vimos`: la etiqueta «capítulo 10» entra junto a la flecha
- «a la salida» → `salida`: aparece «S_yy»
- «la de la entrada» → `entrada`: aparece «S_xx»
- «el módulo de la ganancia al cuadrado» → `mod`: aparece «|H|²» y la fórmula completa «S_yy = |H|² S_xx» queda armada

<!-- b2 -->
Dentro de las ventanitas, la ganancia es uno, y uno al cuadrado es uno: la curva queda intacta. Fuera, es cero, y la curva desaparece. La potencia de la salida es el área de lo que queda, dividida entre dos pi. Y eso vale para cualquier banda: el área sobre una banda es la potencia que el proceso tiene en ella.

- «Dentro de las ventanitas» → `dentro`: corte seco; la curva con las dos ventanitas encima
- «la ganancia es uno» → `g1`: aparece «ganancia 1» en verde
- «la curva queda intacta» → `intacta`: dentro de las ventanitas la curva se mantiene
- «Fuera, es cero» → `fuera`: fuera la ganancia vale cero
- «la curva desaparece» → `desap`: la curva fuera de las ventanitas se apaga
- «el área de lo que queda» → `area`: las dos áreas restantes se sombrean en ámbar
- «dividida entre dos pi» → `dospi`: aparece «1/2π» delante del área
- «cualquier banda» → `banda`: las ventanitas se desplazan a otra banda
- «la potencia que el proceso tiene en ella» → `potbanda`: el área de la nueva banda se rotula «potencia en la banda»

<!-- b3 -->
Con la telegráfica: si el colador deja pasar de menos dos a dos radianes por segundo, el área que queda da justo la mitad de la potencia. La otra mitad está repartida por todas las demás frecuencias, hasta el infinito. Esa es la herramienta del capítulo: una curva que dice cuánta potencia hay en cada banda.

- «Con la telegráfica» → `tele`: vuelve la curva 4/(4 + ω²)
- «de menos dos a dos radianes por segundo» → `rango`: el colador se ensancha a «−2 < ω < 2 rad/s»
- «la mitad de la potencia» → `mitad`: el área interior queda en ámbar con «½»
- «La otra mitad» → `otra`: las dos colas exteriores se sombrean en gris con «½»
- «hasta el infinito» → `inf`: flechas hacia los dos lados
- «la herramienta del capítulo» → `herr`: la curva entera se rotula «S_xx(jω)»
- «cuánta potencia hay en cada banda» → `cada`: varias bandas sucesivas se sombrean de colores

---

# Escena 14 — Cierre

**Capítulo YouTube:** Lo que viene: lo que un espectro no puede hacer

## Narración

<!-- b1 -->
Repasemos. El ruido no tiene espectro, pero su potencia esperada sí: es la transformada de la autocorrelación, y su área sobre una banda es la potencia que hay en ella. Pero no vale cualquier curva: la potencia no puede ser negativa. Y eso prohíbe cosas. En el próximo episodio: lo que un espectro no puede hacer.

- «El ruido no tiene espectro» → `sin`: una traza de ruido con su espectro tachado
- «su potencia esperada sí» → `potesp`: aparece la curva ámbar de la densidad
- «la transformada de la autocorrelación» → `transf`: flecha de R_xx(τ) a S_xx(jω)
- «y su área sobre una banda» → `area`: una banda se sombrea bajo la curva ámbar
- «la potencia que hay en ella» → `banda`: una banda sombreada bajo la curva
- «Pero no vale cualquier curva» → `cualquiera`: una curva con un hundimiento aparece en gris
- «la potencia no puede ser negativa» → `negativa`: la curva se hunde bajo cero en rojo
- «Y eso prohíbe cosas» → `prohibe`: un sello de prohibido sobre la parte negativa
- «En el próximo episodio» → `proximo`: el sello de prohibido se aparta y entra una flecha
- «lo que un espectro no puede hacer» → `titulo_e2`: entra el título del siguiente episodio
