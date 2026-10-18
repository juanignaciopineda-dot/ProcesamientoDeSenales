# Episodio 7 — Variables que son flechas

Capítulo 7 (Modelos probabilísticos), episodio 7 de 7. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 25 a 29), más un gancho y un cierre nuevos.
Es el último episodio del capítulo: su cierre anuncia el E1 del capítulo 8.

**Estado:** **Subido a YouTube en privado** el 17/10/2026: render final 1080p60 de 10:25, con título, descripción con `capitulos.txt`, subtítulos `.srt`, categoría Educación y «no es para niños» (https://youtu.be/-_chXp6KYSo). Lo subió el usuario sin el visto bueno que figuraba pendiente en este estado (texto ⭐ / mp4 / pronunciaciones): la aprobación queda en su revisión antes de publicarlo. Residuos limpiados el 17/10/2026; se rehace con `python rehacer.py Capitulo07_Probabilidad`. La caché de voz versionada (`media/voiceovers/`) se volvió a sintetizar después de la subida: un render nuevo es reproducible, pero la voz puede diferir un poco de la del vídeo subido. **Falta**: publicarlo (lo hace el usuario).

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «¿Y si te digo que cuánto se parecen dos variables aleatorias se mide, literalmente, con el coseno de un ángulo?…» (ya no da por sabido el «coeficiente de correlación»: ningún episodio anterior lo presenta).
- ⭐ Escena 16 (cierre): resume el episodio, cierra el capítulo y anuncia el E1 del capítulo 8, «¿Cuál es tu mejor apuesta?».
- ⭐ Retoque en la escena 08 (bloque b2): «Ese cociente ya tenía nombre» pasa a «Ese cociente es un número nuevo… y tiene nombre»: el coeficiente de correlación rho se presenta aquí por primera vez (el E6 llega solo hasta la covarianza). (Ya corregido también en `../guion_base.md`.)
- ⭐ Retoque en la escena 13 (bloque b1): la última frase del guion base decía que la parábola «volverá dos veces más»; con los capítulos 10, 11 y 13 son más, y ahora dice «volverá varias veces más». (Ya corregido también en `../guion_base.md`.)

---

# Escena 01 — Gancho

**Capítulo YouTube:** La correlación es un coseno

## Narración

<!-- b1 -->
¿Y si te digo que cuánto se parecen dos variables aleatorias se mide, literalmente, con el coseno de un ángulo? Las variables aleatorias son flechas, y hoy lo vamos a demostrar.

- «cuánto se parecen dos variables aleatorias» → `rho`: aparece «ρ» grande en ámbar
- «el coseno de un ángulo» → `coseno`: «ρ = cos θ» se completa y aparece un arco de ángulo entre dos flechas
- «Las variables aleatorias son flechas» → `flechas`: las dos flechas se rotulan «X» e «Y»
- «hoy lo vamos a demostrar» → `demostrar`: las flechas se agrandan y el arco brilla

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Variables que son flechas

## Narración

<!-- b1 -->
Variables que son flechas.

- «Variables» → `t1`: «Variables» entra con rebote
- «que son flechas» → `t2`: «que son flechas» entra debajo, con la etiqueta «Capítulo 7 · Modelos probabilísticos»

---

# Escena 03 — RepasoVectores

**Capítulo YouTube:** Repaso: vectores y largo

## Narración

<!-- b1 -->
Un repaso rápido de vectores, porque lo vamos a necesitar. Un vector es una flecha que sale del origen. En el plano se describe con dos números, sus componentes: cuánto avanza en horizontal y cuánto en vertical. La flecha tres, cuatro avanza tres a la derecha y cuatro hacia arriba.

- «Un repaso rápido de vectores» → `repaso`: cartel «Vectores» sobre una cuadrícula vacía
- «porque lo vamos a necesitar» → `necesitar`: sobre la cuadrícula aparece un punto de origen (0, 0)
- «Un vector es una flecha» → `flecha`: una flecha sale del origen hasta el punto (3, 4)
- «que sale del origen» → `origen`: el origen (0, 0) se resalta con un anillo
- «dos números» → `dos`: aparecen dos casillas vacías «( _ , _ )»
- «sus componentes» → `componentes`: «componentes» entra con rebote
- «cuánto avanza en horizontal» → `horiz`: una línea ámbar horizontal de 0 a 3
- «cuánto en vertical» → `vert`: una línea ámbar vertical de 0 a 4 en el extremo
- «La flecha tres, cuatro» → `par`: las casillas se llenan: «( 3 , 4 )»
- «tres a la derecha» → `tres`: se resalta la línea horizontal con el rótulo «3»
- «cuatro hacia arriba» → `cuatro`: se resalta la línea vertical con el rótulo «4»

<!-- b2 -->
¿Cuánto mide? La flecha es la hipotenusa de un triángulo rectángulo con catetos tres y cuatro. Por Pitágoras, su largo al cuadrado es tres al cuadrado más cuatro al cuadrado: veinticinco. El largo es cinco.

- «¿Cuánto mide?» → `mide`: junto a la flecha aparece «¿largo?»
- «hipotenusa de un triángulo rectángulo» → `triangulo`: se sombrea el triángulo y la flecha se marca como hipotenusa
- «catetos tres y cuatro» → `catetos`: los rótulos 3 y 4 pasan a los catetos
- «Por Pitágoras» → `pitagoras`: aparece «largo² = 3² + 4²» construyéndose pieza a pieza
- «tres al cuadrado más cuatro al cuadrado» → `cuentas`: debajo se escribe «= 9 + 16»
- «veinticinco» → `v25`: «= 25» entra con rebote
- «El largo es cinco» → `cinco`: «largo = 5» sobre la flecha, en ámbar

---

# Escena 04 — ProductoEscalar

**Capítulo YouTube:** El producto escalar

## Narración

<!-- b1 -->
Ahora, dos flechas. Su producto escalar se calcula multiplicando componente a componente y sumando. Para u igual a tres, cuatro y para ve igual a cuatro, cero, resulta: tres por cuatro más cuatro por cero, doce. Y ese mismo número se puede calcular de otra forma: el largo de una por el largo de la otra por el coseno del ángulo que forman. Cinco por cuatro por el coseno da doce, así que el coseno vale cero coma seis.

- «dos flechas» → `dos_flechas`: aparece una segunda flecha v = (4, 0), en cian, junto a u = (3, 4)
- «Su producto escalar» → `pe`: «u · v» entra con rebote
- «multiplicando componente a componente» → `mult`: se unen con líneas las primeras componentes (3 y 4) y las segundas (4 y 0)
- «y sumando» → `suma`: aparece un «+» entre los dos productos
- «Para u igual a tres, cuatro y para ve igual a cuatro, cero» → `pares`: se escribe «u = (3, 4), v = (4, 0)»
- «tres por cuatro más cuatro por cero» → `cuenta`: se construye «3·4 + 4·0»
- «doce» → `doce`: «= 12» en ámbar
- «de otra forma» → `otra`: la cuenta se corre a un lado y aparece el dibujo de las dos flechas con el ángulo entre ellas
- «el largo de una por el largo de la otra» → `largos`: se escribe «|u| · |v|» y las dos flechas se resaltan por turnos
- «por el coseno del ángulo» → `coseno`: «· cos θ» se suma y el arco del ángulo brilla
- «Cinco por cuatro por el coseno da doce» → `cuenta2`: «5 · 4 · cos θ = 12»
- «cero coma seis» → `seis`: «cos θ = 0,6» y el arco muestra «≈ 53°»

---

# Escena 05 — DosLecturas

**Capítulo YouTube:** Largo y perpendicular, con un solo número

## Narración

<!-- b1 -->
El producto escalar tiene dos lecturas que vamos a usar. La primera: el producto escalar de una flecha consigo misma es su largo al cuadrado. Tres por tres más cuatro por cuatro, veinticinco. La segunda: si dos flechas son perpendiculares, el coseno de noventa grados es cero, y su producto escalar también. Producto cero significa perpendiculares.

- «dos lecturas» → `dos`: aparecen dos casillas, «1» y «2»
- «La primera» → `primera`: se enciende la casilla 1 y la flecha u se dibuja sola
- «consigo misma» → `consigo`: se escribe «u · u»
- «su largo al cuadrado» → `largo2`: «u · u = |u|²»
- «Tres por tres más cuatro por cuatro» → `cuenta`: debajo, «3·3 + 4·4»
- «veinticinco» → `v25`: «= 25 = 5²» en ámbar
- «La segunda» → `segunda`: se enciende la casilla 2; aparecen dos flechas en ángulo recto
- «si dos flechas son perpendiculares» → `perp`: el ángulo recto se marca con un cuadradito
- «noventa grados» → `noventa`: rótulo «90°» y «cos 90° = 0»
- «y su producto escalar también» → `cero`: «u · v = 0» en verde
- «Producto cero significa perpendiculares» → `regla`: la regla «producto 0 ⇔ perpendiculares» entra con rebote

<!-- b2 -->
Largos, ángulos, perpendiculares. Todo sale del producto escalar. Y aquí viene la idea atrevida: ¿y si pudiéramos definir un producto escalar entre variables aleatorias? Entonces tendrían largo, formarían ángulos y podrían ser perpendiculares. Resulta que se puede.

- «Largos, ángulos, perpendiculares» → `tres`: aparecen tres rótulos en fila: «largo», «ángulo», «perpendicular»
- «Todo sale del producto escalar» → `todo`: de «u · v» salen tres flechas hacia los tres rótulos
- «la idea atrevida» → `atrevida`: «idea atrevida» entra con rebote
- «¿y si pudiéramos definir un producto escalar» → `pregunta`: se escribe «u · v» con un signo de pregunta
- «entre variables aleatorias» → `varaleat`: u y v se reemplazan por «X · Y = ?»
- «tendrían largo» → `largo`: las flechas X e Y se dibujan con su largo marcado
- «formarían ángulos» → `angulos`: aparece el arco entre ellas
- «podrían ser perpendiculares» → `perpend`: las flechas giran hasta quedar en ángulo recto
- «Resulta que se puede» → `puede`: una tilde verde

---

# Escena 06 — ProductoDeVariables

**Capítulo YouTube:** El producto escalar entre variables aleatorias

## Narración

<!-- b1 -->
Definamos el producto escalar de dos variables aleatorias como la esperanza de su producto: la correlación. Para que merezca ese nombre, y no sea solo un parecido, tiene que cumplir las mismas reglas que el producto escalar de flechas. Son tres.

- «el producto escalar de dos variables aleatorias» → `def`: dos columnas, «flechas» y «variables aleatorias»; en la segunda, «X · Y»
- «la esperanza de su producto» → `esperanza`: «X · Y := E[XY]» se construye; en la columna de flechas, «u · v»
- «la correlación» → `correlacion`: «E[XY]» se rotula «correlación»
- «y no sea solo un parecido» → `parecido`: un signo «≈» tachado entre las dos columnas
- «las mismas reglas» → `reglas`: una llave une las dos columnas
- «Son tres» → `tres`: aparecen tres casillas vacías

<!-- b2 -->
Primera: no importa el orden. La esperanza de equis por i griega es la de i griega por equis. Segunda: es lineal. Si una de las variables es una combinación de otras, el producto se reparte, gracias a la linealidad de la esperanza. Tercera: el producto de una variable consigo misma es positivo, porque es la esperanza de un cuadrado. Las tres se cumplen.

- «Primera: no importa el orden» → `orden`: la casilla 1 se llena con «no importa el orden»
- «La esperanza de equis por i griega» → `exy`: «E[XY]»
- «es la de i griega por equis» → `eyx`: «= E[YX]» y una tilde
- «Segunda: es lineal» → `lineal`: la casilla 2 se llena con «es lineal»
- «combinación de otras» → `combina`: «Z = aX + bY» aparece junto a las flechas
- «el producto se reparte» → `reparte`: «E[(aX + bY)Z] = a E[XZ] + b E[YZ]» se construye por piezas
- «la linealidad de la esperanza» → `linealidad`: se subraya «linealidad»
- «Tercera: el producto de una variable» → `tercera`: la casilla 3 se enciende y aparece «X · X»
- «consigo misma es positivo» → `positivo`: se completa «X · X > 0»
- «la esperanza de un cuadrado» → `cuadrado`: «E[X²]» con una parábola pequeña sobre cero que no baja del eje
- «Las tres se cumplen» → `cumplen`: tres tildes verdes

---

# Escena 07 — LargoYCentradas

**Capítulo YouTube:** Largo, ortogonales y variables centradas

## Narración

<!-- b1 -->
Así que las variables aleatorias, si solo miramos sus medias, varianzas y covarianzas, se comportan como flechas. El largo al cuadrado de una variable es la esperanza de su cuadrado. Y dos variables cuya esperanza del producto es cero son perpendiculares y se dice que son ortogonales. No es una forma de hablar. Es la misma condición que en el plano.

- «si solo miramos sus medias, varianzas y covarianzas» → `solo`: tres rótulos en fila: «medias», «varianzas», «covarianzas»
- «se comportan como flechas» → `flechas`: la columna de variables se transforma en dos flechas X e Y
- «El largo al cuadrado de una variable» → `largo`: «|X|²» aparece junto a la flecha X
- «la esperanza de su cuadrado» → `ex2`: «|X|² = E[X²]»
- «dos variables cuya esperanza del producto es cero» → `cero`: «E[XY] = 0»
- «son perpendiculares» → `perp`: las flechas giran hasta el ángulo recto
- «ortogonales» → `ortog`: «ortogonales» entra con rebote
- «No es una forma de hablar» → `nohabla`: un cartel «≠ metáfora» brilla un instante
- «la misma condición que en el plano» → `plano`: al lado, el «u · v = 0» de la escena anterior, con el mismo dibujo

<!-- b2 -->
Ahora centremos las variables, restando a cada una su media. Con eso, el producto escalar se convierte en la covarianza, y el largo al cuadrado, en la varianza. Es decir: el largo de cada flecha es su desviación estándar, y el producto escalar entre dos flechas es su covarianza.

- «centremos las variables» → `centrar`: «X − μ_X» y «Y − μ_Y» reemplazan a X e Y
- «restando a cada una su media» → `restar`: las flechas se desplazan hasta el origen
- «el producto escalar se convierte en la covarianza» → `cov`: «E[(X − μ_X)(Y − μ_Y)] = σ_XY»
- «el largo al cuadrado, en la varianza» → `var`: «|X − μ_X|² = σ_X²»
- «el largo de cada flecha es su desviación estándar» → `desv`: sobre cada flecha, «σ_X» y «σ_Y»
- «el producto escalar entre dos flechas es su covarianza» → `prod`: en el centro, «u · v = σ_XY»

<!-- b3 -->
Volvamos al ejemplo de antes. Una variable con varianza seis es una flecha de largo raíz de seis, algo menos de dos coma cinco. Otra con varianza cuatro es una flecha de largo dos. Y su covarianza, tres, es su producto escalar. Dos flechas con un largo cada una y un producto escalar. Entre ellas tiene que haber un ángulo.

- «Volvamos al ejemplo de antes» → `ejemplo`: la tabla del ejemplo: «σ_X² = 6», «σ_Y² = 4», «σ_XY = 3»
- «varianza seis» → `v6`: se resalta «σ_X² = 6»
- «raíz de seis» → `r6`: la flecha X se dibuja con el rótulo «√6 ≈ 2,45»
- «Otra con varianza cuatro» → `v4`: se resalta «σ_Y² = 4»
- «largo dos» → `l2`: la flecha Y se dibuja con el rótulo «2»
- «su covarianza, tres» → `cov3`: se resalta «σ_XY = 3»
- «su producto escalar» → `pe`: «X · Y = 3» entre las dos flechas
- «Dos flechas con un largo cada una» → `dos`: las dos flechas se resaltan con sus largos «√6» y «2»
- «tiene que haber un ángulo» → `angulo`: un arco con «θ = ?» entre las flechas

---

# Escena 08 — CosenoDelAngulo

**Capítulo YouTube:** Rho es el coseno del ángulo

## Narración

<!-- b1 -->
En el plano, el producto escalar es el largo de una flecha por el largo de la otra por el coseno del ángulo. Traducido a variables: la covarianza es sigma de equis por sigma de i griega por el coseno del ángulo. Despejando, el coseno del ángulo es la covarianza dividida entre las dos desviaciones estándar.

- «el producto escalar es el largo de una flecha» → `plano`: «u · v = |u| |v| cos θ» se construye pieza a pieza
- «por el coseno del ángulo» → `cos`: se resalta «cos θ» y el arco
- «Traducido a variables» → `traduce`: cada pieza se transforma: «σ_XY = σ_X σ_Y cos θ»
- «sigma de equis por sigma de i griega» → `sigmas`: se resaltan «σ_X σ_Y»
- «Despejando» → `despeja`: «cos θ» pasa al otro lado y la fórmula se reordena
- «el coseno del ángulo es la covarianza dividida entre las dos desviaciones estándar» → `cociente`: «cos θ = σ_XY / (σ_X σ_Y)»

<!-- b2 -->
Ese cociente es un número nuevo, que mide cuánto se parecen las dos variables, y tiene nombre: el coeficiente de correlación, rho. Así que rho es, literalmente, el coseno del ángulo entre las dos variables centradas. En el ejemplo, tres dividido entre raíz de seis por dos da cero coma seis uno dos. Las dos flechas forman unos cincuenta y dos grados.

- «es un número nuevo» → `nombre`: el cociente se enmarca con una etiqueta «Número nuevo»
- «el coeficiente de correlación, rho» → `rho`: «= ρ» se completa en ámbar
- «literalmente, el coseno del ángulo» → `literal`: «ρ = cos θ» con el arco de ángulo brillando
- «entre las dos variables centradas» → `centradas`: las flechas se rotulan «X − μ_X» e «Y − μ_Y»
- «En el ejemplo» → `ejemplo`: aparecen «σ_XY = 3, σ_X = √6, σ_Y = 2»
- «tres dividido entre raíz de seis por dos» → `cuenta`: «3 / (√6 · 2)»
- «cero coma seis uno dos» → `v612`: «≈ 0,612»
- «unos cincuenta y dos grados» → `grados`: en el arco aparece «θ ≈ 52°»

---

# Escena 09 — LeerRho

**Capítulo YouTube:** Leer rho de un vistazo

## Narración

<!-- b1 -->
Ahora rho se lee de un vistazo. Si vale uno, las flechas apuntan hacia el mismo lado: la nube es una recta que sube. Si vale cero, son perpendiculares: no hay ninguna relación en línea recta. Si vale menos uno, apuntan en sentidos opuestos: la nube es una recta que baja. Para el canal de bits, por cierto, sale cero coma setenta y siete.

- «se lee de un vistazo» → `vistazo`: un deslizador de ρ, de −1 a 1, con las dos flechas arriba y una nube de puntos abajo
- «Si vale uno» → `uno`: el deslizador va a 1 y las flechas quedan alineadas
- «las flechas apuntan hacia el mismo lado» → `mismo`: se resalta el ángulo cero entre las flechas
- «una recta que sube» → `sube`: la nube se estira en una recta ascendente
- «Si vale cero» → `cero`: el deslizador va a 0 y las flechas giran a 90°
- «no hay ninguna relación en línea recta» → `redonda`: la nube se vuelve redonda
- «Si vale menos uno» → `menos`: el deslizador va a −1 y las flechas quedan opuestas
- «una recta que baja» → `baja`: la nube se vuelve una recta descendente
- «el canal de bits» → `canal`: aparece el dibujo del canal de bits (el de la escena 17)
- «cero coma setenta y siete» → `v077`: «ρ ≈ 0,77» y la flecha del canal a unos 40°

---

# Escena 10 — TeoremaDelCoseno

**Capítulo YouTube:** La cuenta de la combinación era geometría

## Narración

<!-- b1 -->
Y ahora el pago prometido. La varianza de dos equis menos tres i griega era el largo al cuadrado de la flecha dos equis menos tres i griega. Esa flecha es el tercer lado de un triángulo. Y el teorema del coseno dice que el cuadrado de ese lado es la suma de los cuadrados de los otros dos, más un término cruzado con el coseno del ángulo.

- «el pago prometido» → `pago`: «pago prometido» entra con rebote y aparece el recordatorio de la escena 24: «Var(2X − 3Y) = …»
- «La varianza de dos equis menos tres i griega» → `varianza`: se resalta «Var(2X − 3Y)»
- «el largo al cuadrado de la flecha» → `largo`: «= |2X − 3Y|²»
- «Esa flecha» → `esa`: la flecha 2X − 3Y se resalta en ámbar
- «el tercer lado de un triángulo» → `tercer`: se dibuja el triángulo con los lados 2X, −3Y y 2X − 3Y; el tercero en ámbar
- «el teorema del coseno» → `teorema`: «teorema del coseno» entra con rebote
- «la suma de los cuadrados de los otros dos» → `otros`: «c² = a² + b²»
- «un término cruzado con el coseno del ángulo» → `cruzado`: «− 2ab cos γ» se suma y el ángulo del triángulo brilla

<!-- b2 -->
Es exactamente la fórmula de la varianza de una combinación: los dos cuadrados son las varianzas, y el término cruzado es la covarianza. Aquella cuenta era geometría todo el tiempo. Queda una pregunta pendiente: ¿quién garantiza que rho no pueda valer, por ejemplo, uno coma cinco?

- «la fórmula de la varianza de una combinación» → `formula`: junto al teorema, «Var(2X − 3Y) = 4σ_X² + 9σ_Y² − 12σ_XY»
- «los dos cuadrados son las varianzas» → `cuadrados`: se emparejan «a², b²» con «4σ_X², 9σ_Y²» con líneas de colores
- «el término cruzado es la covarianza» → `cruce`: se empareja «2ab cos γ» con «12σ_XY»
- «geometría todo el tiempo» → `geometria`: una tilde verde entre las dos fórmulas
- «una pregunta pendiente» → `pendiente`: aparece «¿ρ = 1,5?» con una interrogación
- «¿quién garantiza» → `quien`: el «¿ρ = 1,5?» se agranda
- «uno coma cinco» → `v15`: «ρ = 1,5» tachado en rojo

---

# Escena 11 — ParabolaNoNegativa

**Capítulo YouTube:** Cauchy-Schwarz: una parábola que no baja

## Narración

<!-- b1 -->
Un coseno siempre está entre menos uno y uno. Pero aquí rho está definido con esperanzas, así que hay que demostrar que también lo cumple. La demostración es preciosa. Toma dos variables, la u y la ve, y un número cualquiera, lambda. Mira la esperanza de u menos lambda por v, todo al cuadrado. Es la esperanza de algo al cuadrado, así que nunca puede ser negativa.

- «Un coseno siempre está entre menos uno y uno» → `coseno`: una recta con «−1» y «1» marcados y el rótulo «cos θ»
- «rho está definido con esperanzas» → `esperanzas`: «ρ = σ_XY / (σ_X σ_Y)» con las esperanzas resaltadas
- «hay que demostrar» → `demostrar`: «¿|ρ| ≤ 1?» entra con rebote
- «La demostración es preciosa» → `preciosa`: «demostración» entra con rebote
- «dos variables, la u y la ve» → `uv`: aparecen «U» y «V»
- «un número cualquiera, lambda» → `lambda`: aparece «λ» con un deslizador
- «la esperanza de u menos lambda por v» → `g`: «g(λ) = E[U − λV…» se construye pieza a pieza
- «todo al cuadrado» → `todo`: se cierra «…(U − λV)²]»
- «algo al cuadrado» → `cuadrado`: se resalta el exponente 2
- «nunca puede ser negativa» → `nunca`: «g(λ) ≥ 0» en verde

<!-- b2 -->
Desarrollemos el cuadrado: la esperanza de u al cuadrado, menos dos lambda por la esperanza de u por v, más lambda al cuadrado por la esperanza de v al cuadrado. Si lo miras como una función de lambda, es una parábola: un número por lambda al cuadrado, más otro por lambda, más otro. Y sabemos que esta parábola nunca baja de cero.

- «Desarrollemos el cuadrado» → `desarrolla`: «(U − λV)²» se abre en tres términos
- «la esperanza de u al cuadrado» → `t1`: «E[U²]»
- «menos dos lambda por la esperanza de u por v» → `t2`: «− 2λ E[UV]»
- «más lambda al cuadrado por la esperanza de v al cuadrado» → `t3`: «+ λ² E[V²]»
- «Si lo miras» → `miras`: los tres términos se ordenan en una fila
- «una función de lambda» → `funcion`: se resalta «λ» en los tres términos
- «es una parábola» → `parabola`: se dibuja una parábola con «g(λ)»
- «un número por lambda al cuadrado, más otro por lambda, más otro» → `abc`: debajo, «a λ² + b λ + c»
- «Y sabemos que esta parábola» → `sabemos`: se vuelve a señalar la parábola
- «nunca baja de cero» → `nunca`: la parábola se dibuja sobre el eje, sin cortarlo, con una banda verde por encima

---

# Escena 12 — Discriminante

**Capítulo YouTube:** El discriminante

## Narración

<!-- b1 -->
Recuerda la ecuación de segundo grado del colegio. Las soluciones tienen una raíz cuadrada de be al cuadrado menos cuatro a ce, que se llama discriminante. Si es positivo, la parábola corta el eje dos veces. Si es cero, lo toca en un punto. Y si es negativo, no lo toca. Nuestra parábola nunca baja de cero, así que no puede cortarlo dos veces: su discriminante no puede ser positivo.

- «la ecuación de segundo grado» → `ecuacion`: «a λ² + b λ + c = 0 → λ = (−b ± √(b² − 4ac)) / 2a»
- «del colegio» → `colegio`: un cuaderno con la fórmula
- «una raíz cuadrada de be al cuadrado menos cuatro a ce» → `raiz`: se resalta «√(b² − 4ac)»
- «discriminante» → `discri`: «discriminante» entra con rebote bajo la raíz
- «Si es positivo» → `positivo`: una parábola que corta el eje en dos puntos, «b² − 4ac > 0»
- «corta el eje dos veces» → `dos`: dos puntos rojos en los cortes
- «Si es cero» → `cero`: una parábola que toca el eje, «= 0»
- «lo toca en un punto» → `un`: un punto ámbar en el contacto
- «si es negativo» → `negativo`: una parábola flotando sobre el eje, «< 0»
- «no lo toca» → `notoca`: la parábola sube un poco y se queda sin puntos
- «no puede cortarlo dos veces» → `nocorta`: la primera parábola se tacha en rojo
- «su discriminante no puede ser positivo» → `nopos`: «b² − 4ac ≤ 0» en verde

<!-- b2 -->
Escribimos esa condición, simplificamos, y queda la desigualdad de Cauchy-Schwarz: la esperanza de u por v, al cuadrado, nunca supera la esperanza de u al cuadrado por la de v al cuadrado. Con variables centradas: la covarianza nunca supera el producto de las desviaciones estándar. Es decir, rho está entre menos uno y uno. Con los números del ejemplo, el discriminante vale menos sesenta: la parábola ni se acerca al eje.

- «Escribimos esa condición» → `condicion`: se sustituyen a, b y c: «(−2E[UV])² − 4 E[V²] E[U²] ≤ 0»
- «simplificamos» → `simplifica`: se cancela el 4 y queda «E[UV]² ≤ E[U²] E[V²]»
- «la desigualdad de Cauchy-Schwarz» → `cs`: la desigualdad se enmarca con el nombre «Cauchy-Schwarz»
- «la esperanza de u por v, al cuadrado» → `euv`: se resalta «E[UV]²»
- «la esperanza de u al cuadrado por la de v al cuadrado» → `eu2v2`: se resalta «E[U²] E[V²]»
- «Con variables centradas» → `centradas`: «σ_XY² ≤ σ_X² σ_Y²»
- «la covarianza nunca supera el producto de las desviaciones estándar» → `nunca`: «|σ_XY| ≤ σ_X σ_Y»
- «Es decir» → `esdecir`: una flecha de la desigualdad hacia «ρ»
- «rho está entre menos uno y uno» → `rho`: «−1 ≤ ρ ≤ 1» en ámbar
- «los números del ejemplo» → `numeros`: «g(λ) = 6 − 6λ + 4λ²»
- «menos sesenta» → `v60`: «36 − 96 = −60 < 0»
- «ni se acerca al eje» → `lejos`: la parábola del ejemplo, claramente sobre el eje

---

# Escena 13 — CuandoEsUno

**Capítulo YouTube:** Cuando rho vale uno

## Narración

<!-- b1 -->
¿Y si el discriminante es justo cero? Entonces la parábola toca el eje: hay un lambda para el que u menos lambda por v vale cero siempre. Es decir, una variable es exactamente una recta de la otra, sin nada de azar. Eso es rho igual a uno o a menos uno. Y guarda este truco de la parábola: volverá varias veces más en el curso, cuando menos lo esperes.

- «¿Y si el discriminante es justo cero?» → `justo`: «b² − 4ac = 0» entra con rebote
- «la parábola toca el eje» → `toca`: la parábola baja hasta tocar el eje en un punto ámbar
- «un lambda» → `lambda`: «λ₀» marcado en el punto de contacto
- «vale cero siempre» → `cero`: «U − λ₀V = 0» y la banda verde desaparece en ese punto
- «una variable es exactamente una recta de la otra» → `recta`: «U = λ₀ V» y la nube de puntos se vuelve una recta exacta
- «sin nada de azar» → `sinazar`: los puntos quedan alineados, sin dispersión
- «rho igual a uno o a menos uno» → `rho`: «|ρ| = 1» en ámbar
- «este truco de la parábola» → `truco`: la parábola se reduce a un icono en una esquina
- «volverá varias veces más» → `volvera`: junto al icono, «Cap. 10 · 11 · 13»

---

# Escena 14 — CuatroNubes

**Capítulo YouTube:** Cuatro nubes, un mismo rho

## Narración

<!-- b1 -->
Rho es un número muy cómodo: una nube entera resumida en un coseno. Pero resumir tanto tiene un precio. Mira estas cuatro nubes. Las cuatro tienen casi el mismo rho, alrededor de cero coma ocho cinco. Y no se parecen en nada.

- «una nube entera resumida en un coseno» → `resumen`: una nube de puntos se comprime en un «ρ = 0,85»
- «tiene un precio» → `precio`: el «0,85» se queda solo, sin la nube
- «cuatro nubes» → `cuatro`: una cuadrícula de 2 × 2 con cuatro nubes distintas
- «el mismo rho» → `mismo`: sobre cada nube, «ρ ≈ 0,85»
- «Y no se parecen en nada» → `nada`: las cuatro nubes se resaltan una a una

<!-- b2 -->
La primera es lo que esperas: una relación en línea recta con algo de ruido. La segunda es una curva perfecta, sin ruido ninguno: rho no avisa de que una recta es el modelo equivocado. La tercera es una recta perfecta con un solo punto escapado, que baja el rho sin que nada lo indique. Y en la cuarta no hay relación ninguna: todos los puntos están en una columna, y un único punto, muy lejos, se inventa toda la correlación.

- «La primera» → `primera`: se resalta la nube 1, una recta con ruido
- «algo de ruido» → `ruido`: la nube tiembla un poco y se dibuja la recta de ajuste
- «La segunda» → `segunda`: se resalta la nube 2, una curva perfecta
- «una recta es el modelo equivocado» → `equivocado`: la recta de ajuste se dibuja en rojo, lejos de la curva
- «La tercera» → `tercera`: se resalta la nube 3, una recta con un punto escapado
- «un solo punto escapado» → `escapado`: el punto se aparta y el «0,85» cae; luego vuelve y sube
- «sin que nada lo indique» → `indique`: el «0,85» baja con un parpadeo
- «en la cuarta» → `cuarta`: se resalta la nube 4, una columna vertical
- «todos los puntos están en una columna» → `columna`: se marca la columna de puntos
- «un único punto, muy lejos» → `lejos`: aparece un punto lejanísimo, en rojo
- «se inventa toda la correlación» → `inventa`: la recta de ajuste se inclina hacia ese punto

---

# Escena 15 — MirarLaNube

**Capítulo YouTube:** Mirar la nube antes que el número

## Narración

<!-- b1 -->
La covarianza es un promedio de productos, así que un solo punto muy lejano puede dominarla. Y ya sabemos que solo ve la parte en línea recta. La regla práctica es sencilla: antes de creerte un rho, mira la nube. El número viene después.

- «un promedio de productos» → `promedio`: «σ_XY = promedio de (X − μ)(Y − μ)» con la cuenta
- «un solo punto muy lejano» → `lejano`: la nube con el punto lejano; su producto se dibuja como un rectángulo enorme
- «puede dominarla» → `domina`: el rectángulo enorme tapa a los pequeños
- «solo ve la parte en línea recta» → `recta`: una curva perfecta con «ρ ≈ 0» como en la escena 23
- «La regla práctica es sencilla» → `regla`: «regla práctica» entra con rebote
- «antes de creerte un rho, mira la nube» → `mira`: una lupa pasa sobre la nube
- «El número viene después» → `despues`: el lema «mirar la nube antes que el número» entra con rebote

<!-- b2 -->
Esta forma de mirar las variables como flechas es la que ordena media asignatura. Si queremos adivinar una variable a partir de otra, la pregunta se convierte en geométrica: cuál es el punto de una flecha que queda más cerca de otra. Y a esa pregunta la geometría le tiene una respuesta desde hace siglos: la proyección.

- «mirar las variables como flechas» → `flechas`: las flechas X e Y con su ángulo, otra vez
- «ordena media asignatura» → `asignatura`: aparecen en fila los números de los capítulos «8 · 10 · 11 · 12 · 13»
- «adivinar una variable a partir de otra» → `adivinar`: junto a la flecha X, un «?» sobre la flecha Y
- «se convierte en geométrica» → `geometrica`: «¿qué punto de X queda más cerca de Y?»
- «cuál es el punto de una flecha que queda más cerca de otra» → `cerca`: se baja una perpendicular desde la punta de Y hasta la recta de X
- «Y a esa pregunta» → `esa`: la pregunta «¿qué punto?» se agranda
- «la geometría le tiene una respuesta desde hace siglos» → `siglos`: el pie de la perpendicular se marca en ámbar
- «la proyección» → `proyeccion`: «proyección» entra con rebote y la sombra de Y sobre X se resalta

---

# Escena 16 — Cierre

**Capítulo YouTube:** Cierre y próximo episodio

## Narración

<!-- b1 -->
Resumiendo: una variable aleatoria es una flecha, su largo es la desviación estándar, y el coseno del ángulo entre dos de ellas es rho. Con esto, el capítulo siete está completo. Ahora toca usarlo: si tienes que adivinar el valor de una variable, ¿cuál es tu mejor apuesta? El próximo episodio se llama ¿Cuál es tu mejor apuesta?

- «una variable aleatoria es una flecha» → `flecha`: la flecha X con el rótulo «variable aleatoria»
- «su largo es la desviación estándar» → `largo`: sobre la flecha, «largo = σ_X»
- «el coseno del ángulo entre dos de ellas es rho» → `rho`: aparece la segunda flecha, el arco y «ρ = cos θ»
- «Con esto» → `conesto`: las tres ideas se apilan en una columna
- «el capítulo siete está completo» → `completo`: una barra de capítulo «7» se llena y se marca con una tilde
- «Ahora toca usarlo» → `usarlo`: las flechas se apartan y deja paso a un dado
- «adivinar el valor de una variable» → `adivinar`: el dado rueda y aparece un «?»
- «¿cuál es tu mejor apuesta?» → `apuesta`: aparece una pregunta grande, «¿Cuál es tu mejor apuesta?»
- «El próximo episodio se llama» → `proximo`: la pregunta pasa a un cartel de episodio, «Capítulo 8 · Estimación»
