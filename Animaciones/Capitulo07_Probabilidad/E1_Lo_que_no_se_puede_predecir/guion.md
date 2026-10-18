# Episodio 1 — Lo que no se puede predecir

Capítulo 7 (Modelos probabilísticos), episodio 1 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 01 a 04), más un gancho y un cierre nuevos.
Es el primer vídeo de la serie: abre con el repaso de ~3 min de Señales y Sistemas y de Probabilidad y Estadística.

**Estado:** **Subido a YouTube en privado** el 17/10/2026: render final 1080p60 de 7:22, con título, descripción con `capitulos.txt`, subtítulos `.srt`, categoría Educación y «no es para niños» (https://youtu.be/6sebWkz3paI). Residuos limpiados el 17/10/2026; se rehace con `python rehacer.py Capitulo07_Probabilidad`. La caché de voz versionada (`media/voiceovers/`) se volvió a sintetizar después de la subida: un render nuevo es reproducible, pero la voz puede diferir un poco de la del vídeo subido. **Falta**: publicarlo (lo hace el usuario).

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Esta señal puedes calcularla dentro de un año. Esta otra, ni dentro de un segundo…».
- ⭐ Escena 11 (cierre): resume el lenguaje del episodio, plantea la pregunta de la información nueva y anuncia E2, «Cuando sabes algo más».
- ⭐ Retoque en la escena 10 (bloque b2): se quitó la última frase del guion base («Con estas piezas ya podemos hacernos la primera pregunta interesante…»), que ahora vive en el cierre.

---

# Escena 01 — Gancho

**Capítulo YouTube:** Señales que no se pueden predecir

## Narración

<!-- b1 -->
Esta señal puedes calcularla dentro de un año. Esta otra, ni dentro de un segundo. Y toda una materia trata de lo segundo: señales que no se pueden predecir, pero sí describir.

- «Esta señal puedes calcularla» → `seno`: aparecen ejes y se dibuja un seno perfecto, azul
- «dentro de un año» → `anio`: el seno sigue hacia la derecha hasta una marca «+1 año»
- «Esta otra» → `ruido`: debajo se dibuja una curva ruidosa, magenta
- «ni dentro de un segundo» → `segundo`: una interrogación crece justo después de la marca «+1 s»
- «toda una materia» → `materia`: aparece el cartel «Procesamiento de Señales»
- «señales que no se pueden predecir» → `impredecible`: se resalta la curva ruidosa y entra «impredecible»
- «pero sí describir» → `describir`: la curva se convierte en una pila de curvas con una campana al lado

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Lo que no se puede predecir

## Narración

<!-- b1 -->
Lo que no se puede predecir.

- «Lo que no» → `t1`: «Lo que no» entra con rebote
- «se puede predecir» → `t2`: «se puede predecir» entra debajo, con la etiqueta «Capítulo 7 · Modelos probabilísticos»

---

# Escena 03 — RepasoSenales

**Capítulo YouTube:** Repaso: qué es una señal

## Narración

<!-- b1 -->
Antes de empezar, un repaso muy por encima de lo que se vio en Señales y Sistemas. Una señal es algo que cambia con el tiempo y lleva información, por ejemplo: la voz que capta un micrófono, la tensión en un cable o la temperatura de una habitación. Matemáticamente, es una función: a cada instante le toca un valor.

- «un repaso» → `repaso`: entra un reloj de repaso
- «muy por encima» → `encima`: entra «muy por encima», en gris
- «Señales y Sistemas» → `sys`: junto al reloj entra el cartel «Señales y Sistemas»
- «Una señal es algo que cambia con el tiempo» → `senal`: ejes y una curva que se dibuja de izquierda a derecha
- «y lleva información» → `info`: bajo la curva entra «lleva información»
- «la voz que capta un micrófono» → `microfono`: un micrófono y la onda de voz que sale de él
- «la tensión en un cable» → `cable`: un cable con una curva de tensión
- «la temperatura de una habitación» → `habitacion`: un termómetro con una curva lenta
- «es una función» → `funcion`: aparece «x(t)» sobre la curva
- «a cada instante le toca un valor» → `valor`: un cursor vertical barre la curva y un punto marca el valor

<!-- b2 -->
Si la señal tiene un valor en cada instante, sin huecos, es de tiempo continuo. Si solo la miramos cada cierto tiempo, por ejemplo mil veces por segundo, se convierte en una lista de números: es de tiempo discreto, y es la que manejan los ordenadores. Pasar de una a otra se llama muestrear.

- «un valor en cada instante» → `cont`: la curva completa con el rótulo «continuo»
- «sin huecos» → `sin_huecos`: la curva se resalta de punta a punta
- «cada cierto tiempo» → `cada`: aparecen marcas verticales equiespaciadas
- «mil veces por segundo» → `mil`: rótulo «1.000 por segundo»
- «una lista de números» → `lista`: los puntos de la curva bajan a una lista de números
- «tiempo discreto» → `discreto`: «discreto» entra con rebote
- «la que manejan los ordenadores» → `ordenador`: aparece un ordenador con la lista
- «Pasar de una a otra» → `pasar`: se dibuja la flecha de «continuo» a «discreto»
- «muestrear» → `muestrear`: una flecha de «continuo» a «discreto» con la palabra «muestrear»

---

# Escena 04 — RepasoSistemas

**Capítulo YouTube:** Repaso: sistemas y Fourier

## Narración

<!-- b1 -->
Un sistema es cualquier cosa que recibe una señal y entrega otra, por ejemplo: un amplificador, un altavoz o un programa que limpia una grabación. Los más útiles son los lineales e invariantes en el tiempo. Lineales son aquellos donde si sumas dos entradas, se suman sus salidas. Por otra parte, los invariantes son aquellos en los que si metes la misma entrada más tarde, sale lo mismo, pero más tarde.

- «Un sistema es cualquier cosa» → `caja`: una caja con una flecha de entrada y otra de salida
- «recibe una señal» → `entra`: una curva entra por la izquierda
- «entrega otra» → `sale`: sale una curva distinta por la derecha
- «un amplificador» → `amp`: la caja se etiqueta «amplificador»
- «un altavoz» → `altavoz`: la etiqueta cambia a «altavoz»
- «un programa que limpia una grabación» → `programa`: la etiqueta cambia a «programa» y la curva sale más limpia
- «los lineales e invariantes» → `li`: aparecen dos etiquetas, «lineal» e «invariante»
- «Lineales son aquellos» → `lineales`: late la etiqueta «lineal»
- «si sumas dos entradas» → `suma_in`: dos entradas se suman antes de entrar
- «se suman sus salidas» → `suma_out`: las dos salidas, sumadas, coinciden con la salida de la suma
- «los invariantes» → `invariantes`: late la etiqueta «invariante»
- «la misma entrada más tarde» → `tarde`: la entrada se dibuja corrida a la derecha
- «sale lo mismo, pero más tarde» → `mismo`: la salida sale idéntica, corrida lo mismo

<!-- b2 -->
Y la gran idea de esa materia es que cualquier señal se puede ver como una suma de senos de distintas frecuencias. Eso es la transformada de Fourier, y el dibujo de cuánto hay de cada frecuencia es el espectro. Un filtro es un sistema que deja pasar unas frecuencias y frena otras. Todo esto volverá, explicado con calma, cuando lo necesitemos.

- «la gran idea de esa materia» → `idea`: cartel con una bombilla
- «cualquier señal» → `cualquier`: se dibuja la señal compuesta
- «una suma de senos de distintas frecuencias» → `suma_senos`: una señal se descompone en tres senos de colores
- «la transformada de Fourier» → `fourier`: aparece «Fourier» con una flecha del tiempo a la frecuencia
- «cuánto hay de cada frecuencia» → `barras`: suben tres barras de un espectro
- «es el espectro» → `espectro`: la palabra «espectro» entra con rebote
- «Un filtro es un sistema» → `filtro`: una caja «filtro» sobre el espectro
- «deja pasar unas frecuencias» → `pasa`: dos barras pasan en verde
- «frena otras» → `frena`: una barra se apaga contra la caja
- «explicado con calma» → `calma`: un sello «con calma» sobre el cartel

---

# Escena 05 — RepasoExperimento

**Capítulo YouTube:** Repaso: experimento y probabilidad

## Narración

<!-- b1 -->
Ahora, repasemos Probabilidad y Estadística, también muy por encima. Un experimento aleatorio es un experimento cuyo resultado no se puede saber de antemano, aunque se repita simultaneamente en las mismas condiciones, por ejemplo: lanzar una moneda, tirar un dado o medir el ruido de un aparato.

- «repasemos Probabilidad y Estadística» → `repaso2`: cartel «Probabilidad y Estadística»
- «Un experimento aleatorio» → `experimento`: una caja «experimento» con la palabra «aleatorio»
- «no se puede saber de antemano» → `no_saber`: una interrogación sobre la caja
- «en las mismas condiciones» → `mismas`: la caja se repite tres veces y cada una da un resultado distinto
- «lanzar una moneda» → `moneda`: entra una moneda
- «tirar un dado» → `dado`: entra un dado
- «medir el ruido de un aparato» → `ruido`: entra una curva ruidosa con un medidor

<!-- b2 -->
La probabilidad de un resultado es la fracción de veces que ocurriría si repitieras el experimento muchísimas veces. Si lanzamos una moneda diez veces, quizás salgan siete caras, pero, si lanzamos la moneda diez mil veces la fracción de caras se pega al cincuenta por ciento. Ese número al que se acerca es la probabilidad.

- «La probabilidad de un resultado» → `prob`: aparece «probabilidad» sobre una moneda
- «la fracción de veces» → `fraccion`: una fracción «veces que sale / veces que repito»
- «muchísimas veces» → `muchas`: un contador de lanzamientos empieza a subir
- «diez veces» → `diez`: diez monedas en fila
- «siete caras» → `siete`: siete caras marcadas y la fracción «7/10 = 0,7»
- «diez mil veces» → `diez_mil`: el contador sube hasta 10.000 y aparece una curva de la fracción
- «se pega al cincuenta por ciento» → `cincuenta`: la curva se aplana sobre la línea de 0,5
- «Ese número» → `ese_numero`: la línea de 0,5 se resalta
- «es la probabilidad» → `es_prob`: se marca «probabilidad = 0,5»

---

# Escena 06 — RepasoVariable

**Capítulo YouTube:** Repaso: variable aleatoria y media

## Narración

<!-- b1 -->
Una variable aleatoria es un número que depende del resultado del experimento, es decir, lo que marca el dado o la tensión que se mide. Su distribución dice qué valores puede tomar y con qué probabilidad, y se suele dibujar como una curva. La más famosa es la campana de Gauss. Y la media es el valor alrededor del cual se reparten los resultados.

- «Una variable aleatoria» → `va`: una recta numérica y la etiqueta «variable aleatoria»
- «un número que depende del resultado» → `numero`: un dado con una flecha hacia un punto de la recta
- «lo que marca el dado» → `marca`: el dado muestra un cuatro y el punto va al 4
- «la tensión que se mide» → `tension`: un voltímetro marca un valor que cae en la recta
- «Su distribución» → `distribucion`: aparecen barras sobre la recta
- «con qué probabilidad» → `con_prob`: las barras muestran su altura como fracción
- «como una curva» → `curva`: las barras se suavizan hasta una curva
- «la campana de Gauss» → `campana`: la curva se convierte en la campana
- «la media es el valor» → `media`: un triángulo de equilibrio bajo el centro de la campana
- «se reparten los resultados» → `reparten`: puntos se reparten alrededor del centro

<!-- b2 -->
Si todo esto te suena, perfecto. Si no, no pasa nada: en este capítulo vamos a construir cada una de estas ideas desde cero, con ejemplos y con números, porque todo el resto de la materia se apoya en ellas. Y la primera pregunta es la más importante: ¿por qué una materia de señales necesita tanta probabilidad?

- «Si todo esto te suena» → `suena`: una tilde verde sobre las ideas del repaso
- «no pasa nada» → `nada`: la tilde se transforma en un gesto tranquilo, «no pasa nada»
- «en este capítulo» → `capitulo`: entra «capítulo 7» en ámbar
- «cada una de estas ideas» → `ideas`: las tres tarjetas se resaltan una a una
- «desde cero» → `cero`: un «0» y los cimientos de un edificio
- «con ejemplos y con números» → `ejemplos`: aparecen un dado, una moneda y una cuenta
- «todo el resto de la materia» → `apoya`: sobre los cimientos suben los capítulos 8 a 13
- «se apoya en ellas» → `ellas`: los cimientos laten bajo los capítulos
- «la primera pregunta» → `primera`: todo se va y entra una interrogación grande
- «es la más importante» → `importante`: la interrogación se resalta
- «¿por qué una materia de señales necesita tanta probabilidad?» → `porque`: la pregunta ocupa la pantalla

---

# Escena 07 — SenalesImpredecibles

**Capítulo YouTube:** Por qué una materia de señales necesita probabilidad

## Narración

<!-- b1 -->
En Señales y Sistemas las señales se conocían de antemano. Un seno vale lo mismo hoy que mañana: puedes calcular cuánto valdrá dentro de un año. Pero las señales que de verdad importan no son así. Nadie sabe qué palabras dirás en tu próxima llamada, ni qué forma exacta tendrá el ruido que se cuele en ella. Si lo supiéramos, no haría falta enviar nada.

- «se conocían de antemano» → `conocidas`: un seno perfecto se dibuja
- «lo mismo hoy que mañana» → `hoy_manana`: el seno se repite igual con las marcas «hoy» y «mañana»
- «dentro de un año» → `anio`: la curva se prolonga lejos con la marca «+1 año»
- «de verdad importan» → `importan`: entra «las que importan», en ámbar
- «no son así» → `no_asi`: una cruz sobre el seno
- «qué palabras dirás» → `palabras`: una onda de voz con interrogaciones
- «tu próxima llamada» → `llamada`: un móvil con la onda
- «el ruido que se cuele» → `ruido`: una curva ruidosa magenta se mete en la onda
- «no haría falta enviar nada» → `nada`: un mensaje tachado

<!-- b2 -->
Piensa en un mensaje que viaja por el aire. Lo que sale de la antena es una señal limpia. Por el camino se le suma ruido, por ejemplo: interferencias, calor en los circuitos u otras señales. Y lo que llega al otro lado es la suma de las dos cosas. El ruido es distinto cada vez, así que no se puede restar sin más, como si fuera un número conocido.

- «un mensaje que viaja por el aire» → `mensaje`: una antena emisora y una onda que avanza
- «sale de la antena» → `limpia`: la señal limpia, en azul
- «se le suma ruido» → `suma`: el ruido, en magenta, se suma a la señal
- «interferencias» → `interf`: aparece el rótulo «interferencias»
- «calor en los circuitos» → `calor`: aparece el rótulo «calor»
- «otras señales» → `otras`: aparece el rótulo «otras señales»
- «lo que llega al otro lado» → `llega`: una antena receptora
- «la suma de las dos cosas» → `recibida`: la señal recibida, en cian, igual a azul más magenta
- «distinto cada vez» → `distinto`: tres versiones distintas del ruido
- «no se puede restar sin más» → `restar`: una resta que se tacha
- «un número conocido» → `conocido`: aparece «ruido = ?» en magenta

---

# Escena 08 — EstimarYDetectar

**Capítulo YouTube:** Las dos tareas: estimar y detectar

## Narración

<!-- b1 -->
Lo que sí se puede es conocer sus reglas, como: qué valores suele tomar, cuáles son raros o cómo se relaciona con lo que se envió. Con esas reglas hacemos dos cosas, que son las dos grandes tareas de esta materia. La primera, estimar, es adivinar lo mejor posible cuánto valía la señal. Y detectar, que es decidir si en lo que llegó hay señal o solo ruido, o si se envió un uno o un cero.

- «conocer sus reglas» → `reglas`: junto al ruido aparece una campana
- «qué valores suele tomar» → `suele`: el centro de la campana se ilumina
- «cuáles son raros» → `raros`: la cola de la campana se sombrea
- «cómo se relaciona con lo que se envió» → `relaciona`: una flecha entre el ruido y la señal enviada
- «Con esas reglas» → `con_reglas`: la campana y la señal enviada se resaltan
- «hacemos dos cosas» → `dos_cosas`: aparecen dos fichas, «1» y «2»
- «las dos grandes tareas» → `tareas`: aparecen dos tarjetas vacías
- «La primera, estimar» → `estimar`: la primera tarjeta lleva «estimar» y una curva que intenta seguir a la señal
- «cuánto valía la señal» → `valia`: un número «?» sobre la señal limpia
- «Y detectar» → `detectar`: la segunda tarjeta lleva «detectar»
- «hay señal o solo ruido» → `senal_o_ruido`: una pregunta con un «sí» y un «no»
- «un uno o un cero» → `bit`: un «1» y un «0» sobre la tarjeta

<!-- b2 -->
Las dos cosas se hacen con probabilidad. Por eso la materia empieza aquí, ya que en este capítulo construimos el lenguaje, en los siguientes aprendemos a estimar y a decidir, y al final lo aplicamos a señales enteras que cambian en el tiempo. Empecemos por lo más básico: ¿como hacemos para describir, con matemáticas, algo que no se puede predecir?

- «Las dos cosas se hacen con probabilidad» → `con_prob`: sobre las dos tarjetas aparece una «P»
- «la materia empieza aquí» → `empieza`: un mapa de línea con capítulos 7 a 13 y la estación 7 encendida
- «construimos el lenguaje» → `lenguaje`: la estación 7 recibe «lenguaje»
- «aprendemos a estimar y a decidir» → `estimar_decidir`: se encienden las estaciones 8 y 9
- «y al final» → `final`: se resalta la última estación
- «señales enteras que cambian en el tiempo» → `enteras`: se encienden las estaciones 10 a 13
- «Empecemos por lo más básico» → `basico`: el mapa se aleja y queda solo la estación 7
- «algo que no se puede predecir» → `impredecible`: una curva ruidosa con una interrogación

---

# Escena 09 — ModeloTresPiezas

**Capítulo YouTube:** Espacio muestral, eventos y probabilidad

## Narración

<!-- b1 -->
Para describir algo que no se puede predecir hacen falta tres piezas. La primera es el espacio muestral, este es la lista de todo lo que puede pasar. Si tiras un dado, son las seis caras. Lo dibujamos como un rectángulo con los seis resultados dentro. Pase lo que pase, el resultado estará ahí.

- «hacen falta tres piezas» → `tres`: tres huecos numerados 1, 2 y 3
- «el espacio muestral» → `espacio`: se enciende el hueco 1 y entra «espacio muestral»
- «la lista de todo lo que puede pasar» → `lista`: una lista vertical vacía
- «Si tiras un dado» → `dado`: entra un dado
- «son las seis caras» → `caras`: aparecen las seis caras en fila
- «un rectángulo» → `rect`: las seis caras quedan dentro de un rectángulo
- «Pase lo que pase» → `pase`: un dado cae dentro del rectángulo
- «el resultado estará ahí» → `ahi`: la cara que salió se ilumina dentro del rectángulo

<!-- b2 -->
La segunda pieza son los eventos, son el grupos de resultados que nos interesan. Que salga un número par es un evento, y está formado por el dos, el cuatro y el seis. Que salga más de cuatro es otro, formado por el cinco y el seis. Un evento ocurre si el resultado cae dentro de su grupo.

- «La segunda pieza son los eventos» → `eventos`: se enciende el hueco 2 y entra «eventos»
- «grupos de resultados» → `grupos`: óvalos vacíos sobre el rectángulo
- «Que salga un número par» → `par`: un óvalo rodea tres caras con «sale par»
- «es un evento» → `evento`: el marco de los pares late
- «el dos, el cuatro y el seis» → `246`: se iluminan el 2, el 4 y el 6
- «Que salga más de cuatro» → `mas4`: otro óvalo, de otro color, con «más de 4»
- «el cinco y el seis» → `56`: se iluminan el 5 y el 6, y el 6 pertenece a los dos
- «Un evento ocurre» → `ocurre`: los óvalos parpadean
- «cae dentro de su grupo» → `cae`: el dado cae en el 6 y brillan los dos óvalos

<!-- b3 -->
La tercera pieza es la probabilidad, esta es un número que le asignamos a cada evento. Con un dado bien hecho, cada cara vale un sexto. Y la probabilidad de un evento es la suma de las de sus caras, la probabilidad de que  salga un valor par tiene tres caras, así que vale tres sextos, es decir, un medio.

- «La tercera pieza es la probabilidad» → `tercera`: se enciende el hueco 3 y entra «probabilidad»
- «un número que le asignamos a cada evento» → `numero`: cada óvalo recibe un «P = ?»
- «un dado bien hecho» → `bien`: el dado gira con brillo y queda quieto
- «cada cara vale un sexto» → `sexto`: «1/6» bajo cada cara
- «la probabilidad de un evento» → `prob_evento`: late la fórmula «P(A) = ?»
- «la suma de las de sus caras» → `suma`: las tres caras pares se suman con signos «+»
- «un valor par tiene tres caras» → `par3`: «1/6 + 1/6 + 1/6»
- «tres sextos» → `tres_sextos`: el resultado «3/6»
- «un medio» → `medio`: «3/6» se simplifica a «1/2»

---

# Escena 10 — TresReglas

**Capítulo YouTube:** Las tres reglas de la probabilidad

## Narración

<!-- b1 -->
No vale cualquier número. Toda probabilidad cumple tres reglas. Primera: está entre cero y uno. Cero es imposible, uno es seguro. Segunda: el espacio muestral entero vale uno, porque algo tiene que pasar. Tercera: si dos eventos no pueden ocurrir a la vez, la probabilidad de que ocurra uno u otro es la suma de sus probabilidades.

- «No vale cualquier número» → `cualquiera`: un «−3» y un «7» aparecen y se tachan
- «tres reglas» → `reglas`: tres casillas numeradas
- «Primera: está entre cero y uno» → `r1`: una barra de 0 a 1 con una marca en medio
- «Cero es imposible» → `cero`: el extremo 0 se rotula «imposible»
- «uno es seguro» → `uno`: el extremo 1 se rotula «seguro»
- «Segunda: el espacio muestral entero vale uno» → `r2`: el rectángulo del dado entero con «P = 1»
- «algo tiene que pasar» → `algo`: un dado cae dentro del rectángulo
- «Tercera: si dos eventos» → `r3`: entra el óvalo A
- «no pueden ocurrir a la vez» → `no_vez`: entra el óvalo B, separado, sin tocarse
- «ocurra uno u otro» → `uno_u_otro`: los dos óvalos laten y entra «si no se solapan, se suman»
- «la suma de sus probabilidades» → `suma`: «P(A o B) = P(A) + P(B)»

<!-- b2 -->
De esas tres reglas sale una muy útil. La probabilidad de que algo no pase es uno menos la probabilidad de que pase. ¿Qué probabilidad hay de no sacar un seis? Uno menos un sexto: cinco sextos.

- «una muy útil» → `util`: aparece la palabra «complementario»
- «algo no pase» → `no_pase`: el óvalo del 6 y, en otro color, todo lo que queda fuera
- «uno menos la probabilidad de que pase» → `formula`: «P(no A) = 1 − P(A)» se construye pieza a pieza
- «¿Qué probabilidad hay» → `que_prob`: se resalta el seis
- «no sacar un seis» → `no_seis`: se tacha el 6 y las caras 1 a 5 se iluminan
- «Uno menos un sexto» → `cuenta`: «1 − 1/6»
- «cinco sextos» → `cinco_sextos`: el resultado «5/6» sobre las cinco caras

---

# Escena 11 — Cierre

**Capítulo YouTube:** Cuando sabes algo más

## Narración

<!-- b1 -->
Ya tenemos el lenguaje: un espacio de resultados, eventos y probabilidades que cumplen tres reglas. Con él se puede hablar de señales que no se pueden predecir, pero sí describir. Pero falta hacernos una pregunta: ¿qué le pasa a una probabilidad cuando recibes información nueva? Te dicen que el dado salió par, y de pronto el seis ya no vale un sexto. En el próximo episodio: «Cuando sabes algo más».

- «un espacio de resultados» → `espacio`: reaparece el rectángulo con las seis caras
- «eventos» → `eventos`: reaparecen los óvalos
- «probabilidades que cumplen tres reglas» → `reglas`: aparecen las tres reglas como tres fichas
- «Con él se puede hablar» → `con_el`: el espacio del dado late
- «señales que no se pueden predecir» → `senales`: una curva ruidosa a un lado
- «pero sí describir» → `describir`: la curva se vuelve una pila con su campana
- «falta hacernos una pregunta» → `falta`: aparece una interrogación grande
- «qué le pasa a una probabilidad» → `pasa`: junto a la interrogación entra «P = ?»
- «información nueva» → `nueva`: aparece un sobre con un «¡nuevo!»
- «el dado salió par» → `par`: el óvalo de los pares se ilumina y el resto del rectángulo se apaga
- «ya no vale un sexto» → `tercio`: «1/6» sobre el seis se tacha y aparece «?»
- «Cuando sabes algo más» → `titulo`: entra el título del siguiente episodio con rebote
