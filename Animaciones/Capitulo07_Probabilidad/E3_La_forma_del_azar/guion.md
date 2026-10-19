# Episodio 3 — La forma del azar

Capítulo 7 (Modelos probabilísticos), episodio 3 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 09 a 12), más un gancho y un cierre nuevos.
Idea fuerza: todo lo que se puede saber de una variable aleatoria cabe en una curva.

**Estado:** **Subido a YouTube y publicado** (subido el 17/10/2026, público desde el 19/10): render final 1080p60 de 8:17, con título, descripción con `capitulos.txt`, subtítulos `.srt`, categoría Educación y «no es para niños» (https://youtu.be/TVyUsukj6qU). Residuos limpiados el 17/10/2026; se rehace con `python rehacer.py Capitulo07_Probabilidad`. La caché de voz versionada (`media/voiceovers/`) se volvió a sintetizar después de la subida: un render nuevo es reproducible, pero la voz puede diferir un poco de la del vídeo subido.

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Un dado, un cable y un bit no se parecen en nada…».
- ⭐ Escena 17 (cierre): reescribe el último bloque del guion base (b5 de la escena 12): cambia «en el próximo paso» por el anuncio de E4, «Dos números para resumirlo todo».

Supuesto: el cierre de E2 anuncia este episodio por su título, «La forma del azar».

---

# Escena 01 — Gancho

**Capítulo YouTube:** Una curva lo dice todo

## Narración

<!-- b1 -->
Un dado, un cable y un bit no se parecen en nada. Y sin embargo, todo lo que se puede saber de cualquiera de los tres cabe en una sola curva.

- «Un dado» → `dado`: aparece un dado
- «un cable» → `cable`: junto al dado, un cable con una curva de tensión
- «un bit» → `bit`: junto a ellos, un bit «1» sobre una moneda
- «no se parecen en nada» → `nada`: los tres se separan con un «≠» entre ellos
- «Y sin embargo» → `sinembargo`: los tres se acercan entre sí, como si fueran lo mismo
- «de cualquiera de los tres» → `tres`: se resaltan uno a uno el dado, el cable y el bit
- «cabe en» → `cabe`: los tres se acercan hacia unos ejes vacíos
- «una sola curva» → `curva`: los tres se funden en una única curva ámbar, resaltada con un marco

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** La forma del azar

## Narración

<!-- b1 -->
La forma del azar.

- «La forma» → `t1`: «La forma» entra con rebote
- «del azar» → `t2`: «del azar» entra debajo, con la etiqueta «Capítulo 7 · Modelos probabilísticos»

---

# Escena 03 — VariableAleatoria

**Capítulo YouTube:** Qué es una variable aleatoria

## Narración

<!-- b1 -->
Los resultados de un experimento no siempre son números. Una moneda da cara o cruz. Un paciente está sano o enfermo. Para poder hacer cuentas necesitamos una regla que le ponga un número a cada resultado. Esa regla se llama variable aleatoria. Por ejemplo: cara vale uno y cruz vale cero.

- «no siempre son números» → `numeros`: aparecen palabras sueltas que no son números, con un signo de interrogación
- «Una moneda da cara o cruz» → `moneda`: una moneda con «cara» y «cruz»
- «Un paciente está sano o enfermo» → `paciente`: un paciente con «sano» y «enfermo»
- «hacer cuentas» → `cuentas`: aparece «P = ?» sobre los resultados sin número
- «una regla que le ponga un número» → `regla`: flechas desde cada resultado hacia una recta numérica
- «a cada resultado» → `cada_res`: un número aparece junto a cada flecha
- «variable aleatoria» → `va`: «variable aleatoria» entra con rebote en ámbar
- «cara vale uno y cruz vale cero» → `cara_uno`: la cara va al «1» y la cruz al «0» de la recta

---

# Escena 04 — VariasReglas

**Capítulo YouTube:** Una variable es una forma de leer

## Narración

<!-- b1 -->
Sobre un mismo experimento se pueden definir muchas variables. Con el dado, una variable puede ser el número que sale. Otra, que valga uno si sale par y cero si sale impar. El experimento es el mismo; lo que cambia es la pregunta que le hacemos. Por eso una variable aleatoria no es el dado: es una forma de leerlo.

- «muchas variables» → `muchas`: aparece el dado con dos rótulos de variable «X» e «Y» por encima
- «el número que sale» → `numero`: flechas desde las seis caras a 1, 2, 3, 4, 5 y 6 en una recta
- «valga uno si sale par» → `par`: otra recta debajo; las caras 2, 4 y 6 van al «1»
- «cero si sale impar» → `impar`: las caras 1, 3 y 5 van al «0»
- «El experimento es el mismo» → `mismo`: el dado queda quieto en el centro, las dos reglas a cada lado
- «lo que cambia es la pregunta» → `pregunta`: las dos reglas parpadean, el dado no
- «Por eso» → `por_eso`: el dado se atenúa
- «no es el dado» → `no_dado`: el dado se tacha con una cruz roja
- «una forma de leerlo» → `leerlo`: el dado se tacha como «variable» y aparece una lupa sobre él

---

# Escena 05 — Notacion

**Capítulo YouTube:** Equis mayúscula y equis minúscula

## Narración

<!-- b1 -->
Una cuestión de notación que se usa en todo el curso. La equis mayúscula es la variable aleatoria, o sea, la regla, el experimento que todavía no ha ocurrido. La equis minúscula es un número concreto, es decir, uno de los valores posibles. Cuando escribimos equis mayúscula igual a cuatro, estamos diciendo: el experimento ha salido, y la variable ha valido cuatro.

- «notación» → `notacion`: aparece la palabra «notación» y se aparta a una esquina
- «La equis mayúscula» → `mayus`: una «X» grande ámbar
- «la regla» → `la_regla`: bajo la «X» aparece «la regla»
- «todavía no ha ocurrido» → `no_ocurrio`: un dado en el aire con una interrogación
- «La equis minúscula» → `minus`: una «x» pequeña ámbar sobre una recta numérica
- «un número concreto» → `concreto`: un punto sobre el «4» de la recta
- «uno de los valores posibles» → `posibles`: sobre la recta se marcan los seis valores
- «equis mayúscula igual a cuatro» → `x_cuatro`: aparece «X = 4»
- «el experimento ha salido» → `salido`: el dado cae sobre la mesa
- «ha valido cuatro» → `valio`: el dado cae mostrando 4 y el punto sobre el «4» se enciende

---

# Escena 06 — DiscretasContinuas

**Capítulo YouTube:** Discretas y continuas

## Narración

<!-- b1 -->
Algunas variables toman valores que se pueden contar uno a uno, por ejemplo las caras de un dado o los bits de un mensaje. Estas se llaman variables aleatorias discretas. Otras pueden tomar cualquier valor dentro de un intervalo, por ejemplo la tensión en un cable o la temperatura en un sensor. Estas se llaman continuas. En señales y sistemas aparecen las dos, y necesitamos una forma de describir cualquiera de ellas con la misma herramienta.

- «se pueden contar uno a uno» → `contar`: puntos sueltos sobre una recta que se cuentan 1, 2, 3
- «las caras de un dado» → `caras`: seis puntos sobre una recta con un dado
- «los bits de un mensaje» → `bits`: dos puntos, «0» y «1», con una tira de bits
- «Estas se llaman variables aleatorias discretas» → `discretas`: «discretas» entra con rebote
- «Otras pueden tomar» → `otras`: la primera recta se atenúa y se enciende la segunda
- «cualquier valor dentro de un intervalo» → `intervalo`: un tramo lleno sobre otra recta
- «la tensión en un cable» → `tension`: un cable sobre el tramo
- «la temperatura» → `temperatura`: un termómetro sobre el tramo
- «Estas se llaman continuas» → `continuas`: «continuas» entra con rebote
- «En señales y sistemas aparecen las dos» → `aparecen`: una señal con tramos sueltos y un tramo continuo
- «necesitamos una forma» → `necesitamos`: aparece un interrogante ámbar entre las dos rectas
- «la misma herramienta» → `herramienta`: las dos rectas se unen y una llave inglesa ámbar aparece entre ellas con un interrogante

---

# Escena 07 — LaPregunta

**Capítulo YouTube:** La pregunta de la acumulada

## Narración

<!-- b1 -->
Vamos a construir una curva que describe cualquier variable aleatoria. La idea es hacerse siempre la misma pregunta: ¿qué probabilidad hay de que la variable salga menor o igual que un número dado? Hagámoslo con el dado. ¿Qué probabilidad hay de sacar menos de cero coma cinco? Ninguna, por lo tanto la probabilidad vale cero.

- «una curva» → `curva`: aparecen unos ejes vacíos
- «cualquier variable aleatoria» → `cualquiera`: el dado, el cable y el bit pasan rápido junto a los ejes
- «la misma pregunta» → `misma`: aparece «¿P(X ≤ x)?»
- «menor o igual» → `menor`: se resalta el «≤»
- «un número dado» → `dado_num`: un cursor vertical aparece sobre el eje
- «con el dado» → `con_dado`: el dado a un lado de los ejes
- «cero coma cinco» → `medio`: el cursor se coloca en 0,5
- «por lo tanto la probabilidad vale cero» → `cero`: aparece un punto en altura 0 y «P(X ≤ 0,5) = 0»

<!-- b2 -->
¿Y de sacar uno o menos? Solo vale el uno: un sexto. ¿Dos coma cinco o menos? El uno y el dos: dos sextos. ¿Seis o menos? Todas las caras: uno. ¿Y diez o menos? También uno, porque ya no hay más caras que sumar. Si dibujamos todas estas respuestas, sale una escalera, con un peldaño de un sexto en cada cara.

- «uno o menos» → `uno`: el cursor salta a 1
- «un sexto» → `un_sexto`: punto en altura 1/6 y «P(X ≤ 1) = 1/6»
- «Dos coma cinco o menos» → `dos_medio`: el cursor salta a 2,5
- «dos sextos» → `dos_sextos`: punto en altura 2/6, se iluminan las caras 1 y 2
- «Seis o menos» → `seis`: el cursor salta a 6
- «Todas las caras» → `todas`: se iluminan las seis caras; punto en altura 1
- «diez o menos» → `diez`: el cursor salta a 10
- «ya no hay más caras» → `no_mas`: punto en altura 1, sin caras nuevas
- «Si dibujamos todas estas respuestas» → `dibujamos`: los puntos se encienden uno a uno
- «una escalera» → `escalera`: los puntos se unen en una escalera de seis peldaños
- «un sexto en cada cara» → `peldanos`: cada peldaño se marca con «1/6»

---

# Escena 08 — Acumulada

**Capítulo YouTube:** La función de distribución acumulada

## Narración

<!-- b1 -->
Esa curva se llama función de distribución acumulada. Se escribe efe mayúscula sub equis de equis, y es la probabilidad de que la variable no pase de equis. En una variable continua no hay peldaños: sube suave de cero a uno. Y a veces es una mezcla: una curva suave con un salto, como un sensor que a veces se satura y devuelve siempre el mismo valor.

- «función de distribución acumulada» → `nombre`: sobre la escalera entra el nombre en ámbar
- «efe mayúscula sub equis de equis» → `formula`: aparece «F_X(x) = P(X ≤ x)», pieza a pieza
- «la probabilidad de que la variable» → `prob_que`: en la fórmula se resalta «P»
- «no pase de equis» → `no_pase`: el cursor se mueve y la altura de la escalera acompaña
- «una variable continua» → `continua`: otros ejes con una curva en forma de ese
- «sube suave de cero a uno» → `suave`: la curva se dibuja de 0 a 1
- «una mezcla» → `mezcla`: otra curva con un tramo suave y un salto vertical
- «un sensor que a veces se satura» → `sensor`: un sensor con una luz roja de saturación
- «siempre el mismo valor» → `mismo_valor`: el salto se marca sobre el valor de saturación

<!-- b2 -->
Hay dos cosas que se cumplen siempre. La acumulada nunca baja: si la variable no pasa de tres, tampoco pasa de cuatro, así que la segunda probabilidad es por lo menos la primera. Y empieza en cero y termina en uno: muy a la izquierda no hay nada, y muy a la derecha está todo.

- «dos cosas que se cumplen siempre» → `dos_cosas`: aparecen los números «1» y «2»
- «nunca baja» → `nunca_baja`: una flecha ascendente sobre la escalera
- «no pasa de tres» → `tres`: cursor en 3 y su altura marcada
- «tampoco pasa de cuatro» → `cuatro`: cursor en 4, la altura es mayor o igual; aparece «≥»
- «la segunda probabilidad» → `segunda`: se marca la altura en 4
- «por lo menos la primera» → `primera`: las dos alturas se comparan con «≥»
- «empieza en cero» → `cero_izq`: el extremo izquierdo se pega al eje, «0»
- «termina en uno» → `uno_der`: el extremo derecho se pega a la línea «1»
- «muy a la derecha está todo» → `todo`: aparece «todo» sobre la meseta

---

# Escena 09 — ReglaDelIntervalo

**Capítulo YouTube:** La probabilidad de un intervalo

## Narración

<!-- b1 -->
Y de regalo, una regla práctica. ¿Qué probabilidad hay de que el dado caiga entre dos y cinco, sin incluir el dos? Es lo acumulado hasta cinco, cinco sextos, menos lo acumulado hasta dos, dos sextos: tres sextos. Las caras tres, cuatro y cinco. En general: la probabilidad de caer entre a y b es la acumulada en b menos la acumulada en a.

- «una regla práctica» → `regla`: la escalera en pantalla, con la palabra «regla»
- «que el dado caiga» → `caiga`: el dado junto a la escalera
- «entre dos y cinco» → `entre`: dos cursores, uno en a = 2 y otro en b = 5
- «sin incluir el dos» → `sin_dos`: el extremo en 2 se marca como círculo vacío
- «acumulado hasta cinco» → `hasta_cinco`: altura 5/6 marcada
- «cinco sextos» → `cinco_sextos`: aparece «F(5) = 5/6»
- «acumulado hasta dos» → `hasta_dos`: altura 2/6 marcada
- «dos sextos» → `dos_sextos`: aparece «F(2) = 2/6»
- «tres sextos» → `tres_sextos`: aparece «5/6 − 2/6 = 3/6»; se iluminan las caras 3, 4 y 5
- «Las caras tres, cuatro y cinco» → `caras`: las tres caras se encienden en verde
- «En general» → `general`: la escalera se funde con una curva genérica
- «la probabilidad de caer entre» → `caer`: aparece «P(a < X ≤ b)» vacío a la izquierda
- «a y b» → `a_b`: las dos letras sustituyen a los números en los cursores
- «la acumulada en b menos la acumulada en a» → `resta`: se construye «P(a < X ≤ b) = F(b) − F(a)», pieza a pieza

---

# Escena 10 — Pendiente

**Capítulo YouTube:** De la acumulada a la densidad

## Narración

<!-- b1 -->
Mira la acumulada de una variable continua y fíjate en dónde sube deprisa y dónde apenas se mueve. Donde sube deprisa se acumula mucha probabilidad en poco espacio, esta region es de los valores que más salen. Lo rápido que sube una curva en cada punto es su pendiente, y en matemáticas se llama derivada.

- «la acumulada de una variable continua» → `acumulada`: la curva en forma de ese sobre unos ejes
- «sube deprisa» → `deprisa`: se resalta el tramo central empinado
- «apenas se mueve» → `quieta`: se resaltan los tramos planos de los extremos
- «mucha probabilidad en poco espacio» → `mucha`: un recuadro estrecho sobre el tramo empinado, con una barra alta de «probabilidad»
- «los valores que más salen» → `mas_salen`: el tramo empinado se pinta ámbar
- «Lo rápido que sube una curva» → `rapido`: una flecha sube por la curva, más larga donde es empinada
- «su pendiente» → `pendiente`: una recta tangente aparece sobre la curva
- «derivada» → `derivada`: «derivada = pendiente» entra con rebote

<!-- b2 -->
Si dibujamos la pendiente de la acumulada en cada punto, aparece una curva nueva: la función de densidad de probabilidad, efe minúscula sub equis de equis. Es alta donde la acumulada sube deprisa, y baja donde sube despacio. La densidad nos dice, de un vistazo, dónde se concentran los valores.

- «la pendiente de la acumulada en cada punto» → `en_cada`: la tangente recorre la curva y, debajo, una altura va marcando su pendiente
- «una curva nueva» → `nueva`: debajo se dibuja la campana
- «función de densidad de probabilidad» → `densidad`: el nombre entra con rebote sobre la campana
- «efe minúscula sub equis de equis» → `f_minus`: aparece «f_X(x)» sobre la campana
- «Es alta» → `alta`: se resalta el pico de la campana
- «sube despacio» → `despacio`: se resaltan las colas
- «de un vistazo» → `vistazo`: un ojo aparece junto a la campana
- «dónde se concentran los valores» → `concentran`: las dos curvas, una encima de la otra, con una banda vertical que cruza las dos

---

# Escena 11 — Histograma

**Capítulo YouTube:** La densidad desde las medidas

## Narración

<!-- b1 -->
Hay otra forma de llegar a la misma curva, más física. Mide una tensión con ruido muchas veces y apila cada medida en una columna según su valor. Con cien medidas, sale un dibujo irregular. Con diez mil, las columnas dibujan una forma suave. Esa forma es la densidad: donde es alta, hay muchas medidas, y donde es baja, casi ninguna.

- «otra forma de llegar» → `otra`: la campana se aparta y quedan unos ejes vacíos
- «Mide una tensión con ruido» → `mide`: un voltímetro con una lectura que tiembla
- «apila cada medida en una columna» → `apila`: las medidas caen como cuadritos sobre el eje y se apilan
- «cien medidas» → `cien`: rótulo «100» y un histograma irregular
- «un dibujo irregular» → `irregular`: el histograma se resalta con bordes dentados
- «diez mil» → `diez_mil`: rótulo «10.000» y las columnas se afinan
- «una forma suave» → `suave`: las columnas dibujan la campana
- «Esa forma es la densidad» → `es_densidad`: la campana ámbar se superpone al histograma
- «hay muchas medidas» → `muchas`: se resalta el pico
- «casi ninguna» → `ninguna`: se resaltan las colas

---

# Escena 12 — AreaBajoLaCurva

**Capítulo YouTube:** La probabilidad es un área

## Narración

<!-- b1 -->
¿Y cómo se calcula ahora la probabilidad de caer entre a y entre b? Es el área bajo la densidad entre el valor de a y el valor de b. Imagina el área cortada en rectángulos muy finos y sumados: esa suma, cuando los rectángulos se hacen infinitamente finos, se llama integral. Así que la probabilidad de un intervalo es la integral de la densidad entre el valor de a y el valor de b.

- «entre a y entre b» → `entre`: dos marcas «a» y «b» sobre el eje de la campana
- «el área bajo la densidad» → `area`: el área entre a y b se rellena
- «entre el valor de a y el valor de b» → `valores`: las letras a y b se agrandan un momento
- «Imagina el área cortada» → `imagina`: el área parpadea
- «rectángulos muy finos» → `rectangulos`: el área se corta en rectángulos delgados
- «y sumados» → `sumados`: los rectángulos se suman en una barra de «total»
- «infinitamente finos» → `finos`: los rectángulos se afinan hasta fundirse en un único área
- «integral» → `integral`: «integral = área» entra con rebote
- «la integral de la densidad» → `formula`: se construye «P(a < X ≤ b) = ∫ f_X(x) dx», pieza a pieza, de a a b
- «entre el valor de a y el valor de b» → `limites`: en la fórmula se resaltan a y b

---

# Escena 13 — PropiedadesDeLaDensidad

**Capítulo YouTube:** Dos propiedades de la densidad

## Narración

<!-- b1 -->
Las dos propiedades de la acumulada se traducen solas. Como la acumulada nunca baja, su pendiente nunca es negativa: la densidad siempre está por encima del eje. Y como la acumulada va de cero a uno, el área total bajo la densidad vale exactamente uno. Ojo con un detalle: la densidad no es una probabilidad. Una probabilidad es siempre un área.

- «se traducen solas» → `traducen`: la acumulada arriba y la densidad abajo, con una flecha entre ellas
- «nunca baja» → `nunca_baja`: la acumulada sube sin bajar nunca
- «nunca es negativa» → `no_neg`: la pendiente sobre la acumulada, siempre hacia arriba
- «por encima del eje» → `encima`: la campana se pinta verde por encima del eje, con una línea en cero
- «de cero a uno» → `cero_uno`: la acumulada va de 0 a 1
- «el área total bajo la densidad» → `total`: toda la campana se rellena
- «exactamente uno» → `uno`: aparece «área = 1»
- «Ojo con un detalle» → `ojo`: aparece una señal de aviso
- «la densidad no es una probabilidad» → `no_prob`: «f_X(x) ≠ P» en rojo
- «Una probabilidad es» → `una_prob`: aparece «probabilidad =» junto al área
- «siempre un área» → `siempre_area`: un área sombreada junto a «probabilidad»

---

# Escena 14 — Bernoulli

**Capítulo YouTube:** Bernoulli: el bit

## Narración

<!-- b1 -->
Hay unas pocas distribuciones que vamos a encontrarnos todo el tiempo, así que conviene conocerlas por su nombre. La más sencilla es discreta: la de Bernoulli. La variable solo puede valer cero o uno, como un bit. Vale uno con probabilidad pe, y cero con probabilidad uno menos pe. Su dibujo son dos barras.

- «unas pocas distribuciones» → `pocas`: tres huecos en una fila, vacíos
- «todo el tiempo» → `todo_tiempo`: las tres distribuciones del final parpadean en los huecos
- «por su nombre» → `nombre`: el primer hueco se ilumina
- «la de Bernoulli» → `bernoulli`: «Bernoulli» entra con rebote en el primer hueco
- «cero o uno, como un bit» → `bit`: un bit «0» y uno «1»
- «Vale uno con probabilidad pe» → `p`: aparece una barra sobre el «1» con altura «p»
- «cero con probabilidad uno menos pe» → `uno_menos_p`: una barra sobre el «0» con altura «1 − p»
- «dos barras» → `barras`: las dos barras se encierran en un marco

---

# Escena 15 — Uniforme

**Capítulo YouTube:** La uniforme

## Narración

<!-- b1 -->
La primera continua es la uniforme: todos los valores de un intervalo, entre a, y b, son igual de probables. Su densidad es un rectángulo plano. ¿Qué altura tiene? El área total tiene que ser uno, y el área de un rectángulo es ancho por alto. Así que el alto es uno dividido entre el ancho, es decir, b menos a. Aparece cuando algo puede caer en cualquier sitio, como el error al redondear una señal.

- «la uniforme» → `uniforme`: «uniforme» entra con rebote en el segundo hueco
- «entre a, y b» → `entre`: marcas «a» y «b» sobre un eje
- «igual de probables» → `iguales`: puntos distintos del intervalo se iluminan, todos con la misma altura
- «un rectángulo plano» → `rect`: el rectángulo se dibuja entre a y b
- «¿Qué altura tiene?» → `altura`: aparece una «h = ?» sobre el rectángulo
- «El área total tiene que ser uno» → `area_uno`: aparece «área = 1»
- «ancho por alto» → `ancho_alto`: «(b − a) · h = 1», pieza a pieza
- «uno dividido entre el ancho» → `division`: «h = 1/(b − a)» sustituye a la «h = ?»
- «b menos a» → `b_menos_a`: el ancho se marca con una llave bajo el rectángulo
- «Aparece cuando» → `aparece`: el rectángulo se desplaza a un lado
- «cualquier sitio» → `sitio`: un punto salta a distintos lugares del intervalo
- «redondear una señal» → `redondear`: una señal con su error de redondeo dibujado como una banda

---

# Escena 16 — Gaussiana

**Capítulo YouTube:** La gaussiana

## Narración

<!-- b1 -->
Y la reina de todas: la gaussiana, o campana de Gauss. Tiene dos parámetros. Mu dice dónde está el centro: si cambias mu, la campana se desplaza sin deformarse. Sigma dice lo ancha que es: si aumentas sigma, la campana se ensancha y se aplana, porque el área tiene que seguir valiendo uno.

- «la gaussiana» → `gaussiana`: «gaussiana» entra con rebote en el tercer hueco
- «Tiene dos parámetros» → `dos`: aparecen dos deslizadores, μ y σ
- «Mu dice dónde está el centro» → `mu`: μ se ilumina y el centro de la campana se marca con una línea
- «se desplaza sin deformarse» → `desplaza`: la campana se traslada a ambos lados
- «Sigma dice lo ancha que es» → `sigma`: σ se ilumina y una llave marca el ancho
- «se ensancha y se aplana» → `ensancha`: la campana se ensancha y se baja
- «el área tiene que seguir valiendo uno» → `sigue_uno`: el área sombreada se mantiene y aparece «área = 1»

<!-- b2 -->
¿Por qué es tan importante? Porque cuando se suman muchos efectos pequeños e independientes, el resultado tiende a tener forma de campana, sea cual sea la forma de cada efecto. Y el ruido de un circuito es justamente eso: la suma de millones de electrones moviéndose al azar. Por eso casi todo el ruido de esta materia será gaussiano.

- «tan importante» → `importante`: la campana ámbar se agranda
- «muchos efectos pequeños» → `efectos`: aparecen muchas barritas pequeñas de formas distintas
- «independientes» → `indep`: las barritas se separan, sin tocarse
- «forma de campana» → `forma`: al sumarse, forman una campana
- «sea cual sea la forma de cada efecto» → `cada`: las barritas cambian de forma y la campana se mantiene
- «el ruido de un circuito» → `circuito`: un circuito con una curva de ruido
- «millones de electrones» → `electrones`: una nube de puntos que se agitan dentro del cable
- «casi todo el ruido de esta materia» → `materia`: el ruido se ve con la campana al lado, en magenta
- «gaussiano» → `gauss`: «gaussiano» entra con rebote

---

# Escena 17 — Cierre

**Capítulo YouTube:** Qué viene ahora

## Narración

<!-- b1 -->
Una curva describe una variable por completo. Pero muchas veces no conocemos la curva entera, o es demasiada información para trabajar con ella. ¿Y si pudiéramos resumirla en solo dos números? Y lo sorprendente es que alcanzan para mucho. Lo veremos en el próximo episodio: «Dos números para resumirlo todo».

- «Una curva describe una variable» → `curva`: las tres distribuciones (barras, rectángulo y campana) aparecen una al lado de otra
- «por completo» → `completo`: las tres se resaltan con un marco
- «no conocemos la curva entera» → `no_conocemos`: las curvas se difuminan, con una interrogación
- «demasiada información» → `demasiada`: las curvas se llenan de puntos y números
- «trabajar con ella» → `trabajar`: una mano intenta agarrar la curva y se pasa
- «¿Y si pudiéramos resumirla» → `resumirla`: la curva se encoge hacia un punto
- «solo dos números» → `dos_numeros`: cada curva se reduce a dos números, un punto y una barra de ancho
- «alcanzan para mucho» → `alcanzan`: los dos números se agrandan
- «Lo veremos en el próximo episodio» → `veremos`: aparece una flecha hacia la derecha
- «Dos números para resumirlo todo» → `titulo`: el título del próximo episodio entra con rebote
