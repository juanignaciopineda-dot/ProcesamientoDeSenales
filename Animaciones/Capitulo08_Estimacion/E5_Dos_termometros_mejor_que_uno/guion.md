# Episodio 5 — ¿Dos termómetros mejor que uno?

Capítulo 8 (Estimación), episodio 5 de 5. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 17 a 21), más un gancho y un cierre nuevos.

**Estado:** **Subido a YouTube en privado** el 19/10/2026: render final 1080p60 de 10:43, título buscable, descripción con el capítulo del libro y `capitulos.txt`, subtítulos, categoría Educación (https://youtu.be/YzbX-ba7RIg). Residuos limpiados; la caché de voz original está en `media/voiceovers/`: se rehace igual con `python rehacer.py Capitulo08_Estimacion E5`. **Falta**: publicarlo (lo hace el usuario).

Texto nuevo, para revisar (marcado con ⭐):
- ⭐ Escena 01 (gancho): «Pones un segundo termómetro, peor que el primero. Puede no servir de nada, o puede dejar el error en cero. ¿De qué depende?»
- ⭐ Escena 18 (cierre): resumen corto y anuncia el E1 del capítulo 9 por su título, «¿Un cero o un uno?».
- ⭐ Retoque en todo el episodio: la narración va **sin dos puntos**, como en los E2 y E4 (cada «:» del guion base se pasó a coma, punto o «que es»). Ej.: «Y la regla es la de siempre: el error…» → «Y la regla es la de siempre, el error…».
- ⭐ Retoque en la escena 03 (bloque b2): «Usa dos lecturas, así que hay dos condiciones: el error, perpendicular a A y perpendicular a B» → «Como usa dos lecturas, hay dos condiciones. El error tiene que ser perpendicular a A y también a B».
- ⭐ Retoque en la escena 07 (bloque b3): «Se llaman ecuaciones normales. Normal, en geometría…» → «Se llaman ecuaciones normales, porque normal, en geometría…».
- ⭐ Retoque en la escena 13 (bloque b4): el guion base cerraba con «Tampoco cambia», que se entiende mal (el error sí baja, de 0,8 a 0,67); queda «También coincide con el sistema».
- ⭐ Retoque en la escena 12 (bloque b2): «Marca veintidós» → «Pero marca veintidós».

Nota para el episodio anterior: el cierre del E4 ya anuncia este título, «¿Dos termómetros mejor que uno?».
El cierre de este episodio anuncia el E1 del capítulo 9, «¿Un cero o un uno?».

Reparto de las escenas del guion base: 17 → escenas 03, 04 y 05; 18 → 06, 07 y 08; 19 → 09, 10 y 11; 20 → 12, 13 y 14; 21 → 15 y 16 (sin su b1, ver el recorte); 17 es el cierre.
Solo se partieron bloques enteros en escenas atómicas: el texto del guion base no cambia (salvo los retoques de arriba).
⭐ **Recorte:** con todo el texto, la voz sumaba 10,8 min (~11,2 con las pausas). Como prevé el guion base, se quitó el bloque b1 de la escena 21 (la ironía de los datos: «Todo este capítulo ha supuesto que conocemos medias… hace falta aquella»). Si se quiere recuperar, vuelve como escena propia entre la 14 y la 15.

Notación en pantalla: la temperatura es `y` (azul), las lecturas `x_A` y `x_B` (cian), los pesos `h_A` y `h_B` (ámbar), como en el E3.

---

# Escena 01 — Gancho

**Capítulo YouTube:** Un termómetro peor, ¿sirve?

## Narración

<!-- b1 -->
Pones un segundo termómetro, peor que el primero. Puede no servir de nada, o puede dejar el error en cero. ¿De qué depende?

- «Pones un segundo termómetro» → `segundo`: el termómetro A a la izquierda; a su lado entra el B
- «peor que el primero» → `peor`: bajo cada uno, su ruido en magenta; el de B tiembla mucho más
- «no servir de nada» → `nada`: a la derecha, una barra roja de error «0,8» que no se mueve
- «dejar el error en cero» → `cero`: la barra roja se encoge hasta desaparecer y queda «0» en verde
- «¿De qué depende?» → `depende`: un «?» ámbar grande entre los dos termómetros

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** ¿Dos termómetros mejor que uno?

## Narración

<!-- b1 -->
¿Dos termómetros mejor que uno?

- «¿Dos termómetros» → `t1`: «¿Dos termómetros» entra con rebote
- «mejor que uno?» → `t2`: «mejor que uno?» entra debajo, con la etiqueta «Capítulo 8 · Estimación»

---

# Escena 03 — DosTermometros

**Capítulo YouTube:** Un segundo termómetro
**Objetivo:** plantear los dos termómetros (ruidos 1 y 4, lecturas 23 y 22), la apuesta con dos pesos y las dos condiciones de ortogonalidad.

## Narración

<!-- b1 -->
Pongamos un segundo termómetro en la sala, más barato que el primero. El primero, el A, tiene un ruido de varianza uno. El segundo, el B, de varianza cuatro. Los dos ruidos no tienen nada que ver entre sí ni con la temperatura. A marca veintitrés y B marca veintidós. ¿Qué temperatura hace?

- «Pongamos» → `a`: el termómetro A entra a la izquierda, con su letra
- «un segundo termómetro» → `b`: el termómetro B entra a su lado
- «más barato que el primero» → `barato`: B se sacude un poco, como un aparato flojo
- «El primero, el A» → `ra`: se resalta A
- «de varianza uno» → `r1`: bajo A, una traza de ruido fina y «σ² = 1» en magenta
- «El segundo, el B» → `rb`: se resalta B
- «de varianza cuatro» → `r4`: bajo B, una traza de ruido más ancha y «σ² = 4»
- «no tienen nada que ver» → `indep`: entre los dos ruidos, «Sin relación»
- «ni con la temperatura» → `temp`: arriba a la derecha, la temperatura «y» con «μ = 20» y «σ² = 4» en azul
- «A marca veintitrés» → `m23`: el líquido de A sube y aparece «23» en cian
- «B marca veintidós» → `m22`: el líquido de B sube y aparece «22»
- «¿Qué temperatura hace?» → `que`: a la derecha, «y = ?» en ámbar

<!-- b2 -->
La apuesta es ahora veinte, más el peso de A por lo que A se aparta de veinte, más el peso de B por lo que se aparta B. Dos pesos por elegir. Y la regla es la de siempre, el error tiene que ser ortogonal a todo lo que usa la estimación. Como usa dos lecturas, hay dos condiciones. El error tiene que ser perpendicular a A y también a B.

- «La apuesta es ahora veinte» → `veinte`: corte; arriba, «ŷ = 20»
- «el peso de A» → `ha`: «+ h_A»
- «por lo que A se aparta de veinte» → `xa`: «(x_A − 20)»
- «el peso de B» → `hb`: «+ h_B»
- «por lo que se aparta B» → `xb`: «(x_B − 20)»
- «Dos pesos por elegir» → `dos`: h_A y h_B se enmarcan en ámbar
- «la regla es la de siempre» → `regla`: debajo, un plano en perspectiva con las flechas cian de las dos lecturas
- «el error tiene que ser ortogonal» → `orto`: la flecha azul de la temperatura sale del plano; su sombra ámbar en el plano y el error rojo, vertical
- «todo lo que usa la estimación» → `todo`: el plano se ilumina
- «Como usa dos lecturas» → `dosl`: se resaltan las dos flechas cian
- «hay dos condiciones» → `doscond`: a la derecha, «2 condiciones»
- «perpendicular a A» → `pa`: el cuadradito del ángulo recto entre el error y x_A, y «e ⊥ x_A»
- «y también a B» → `pb`: el cuadradito entre el error y x_B, y «e ⊥ x_B»

---

# Escena 04 — DosCondiciones

**Capítulo YouTube:** Dos ecuaciones, dos incógnitas
**Objetivo:** escribir cada condición con sus covarianzas, cada una con su porqué, y resolver el sistema por sustitución: h_B = 1/6, h_A = 2/3.

## Narración

<!-- b1 -->
Primera condición, con A. La covarianza de la temperatura con A es cuatro. Menos el peso de A por la varianza de A, que es cinco. Menos el peso de B por la covarianza entre A y B. ¿Cuánto vale esa? Los dos termómetros ven la misma temperatura y sus ruidos no se relacionan, así que comparten solo la varianza de la temperatura, que es cuatro. Y todo eso, igualado a cero.

- «Primera condición, con A» → `con_a`: arriba a la izquierda, «Con A» en cian
- «La covarianza de la temperatura con A» → `cov`: debajo del hueco del primer término, «cov(y, x_A)»
- «es cuatro» → `c4`: encima, «4»
- «Menos el peso de A» → `mha`: «− h_A ·»
- «la varianza de A, que es cinco» → `v5`: «5», con «var(x_A) = 4 + 1» debajo
- «Menos el peso de B» → `mhb`: «− h_B ·»
- «la covarianza entre A y B» → `cab`: debajo, «cov(x_A, x_B)»
- «¿Cuánto vale esa?» → `cuanto`: en el hueco, un «?» ámbar
- «ven la misma temperatura» → `misma`: abajo a la derecha, la temperatura y con dos flechas azules hacia A y B
- «sus ruidos no se relacionan» → `ruidos`: bajo A y B, sus ruidos magenta, cada uno por su lado
- «comparten solo la varianza de la temperatura» → `comparten`: se resaltan las dos flechas azules que salen de y
- «que es cuatro» → `c4b`: el «?» se convierte en «4»
- «igualado a cero» → `cero`: «= 0»

<!-- b2 -->
Segunda condición, con B. Cuatro, menos cuatro por el peso de A, menos ocho por el peso de B, porque la varianza de B es cuatro más cuatro. Igual a cero. Dos ecuaciones, dos incógnitas. De la segunda, el peso de A es uno menos dos veces el de B. Lo metemos en la primera y queda menos uno más seis veces el peso de B, igual a cero. El peso de B es un sexto, y el de A, dos tercios.

- «Segunda condición, con B» → `con_b`: se van las notas; la primera ecuación sube y debajo aparece «Con B»
- «Cuatro, menos» → `b4`: «4»
- «cuatro por el peso de A» → `b4ha`: «− 4h_A»
- «menos ocho por el peso de B» → `b8hb`: «− 8h_B»
- «cuatro más cuatro» → `b44`: bajo el 8, «4 + 4»
- «Igual a cero» → `bcero`: «= 0»
- «Dos ecuaciones, dos incógnitas» → `sis`: una llave agrupa las dos ecuaciones; h_A y h_B se resaltan
- «De la segunda» → `despeje`: se resalta la segunda ecuación
- «el peso de A es uno menos dos veces el de B» → `despeja2`: debajo, «h_A = 1 − 2h_B», con una flecha desde la segunda
- «Lo metemos en la primera» → `mete`: «4 − 5(1 − 2h_B) − 4h_B = 0»
- «menos uno más seis veces el peso de B» → `m1`: «−1 + 6h_B»
- «igual a cero» → `igual0`: «= 0»
- «El peso de B es un sexto» → `hb`: «h_B = 1/6» en ámbar
- «y el de A, dos tercios» → `ha`: «h_A = 2/3» en ámbar

---

# Escena 05 — JuntosMejor

**Capítulo YouTube:** Juntos, mejor que el mejor
**Objetivo:** usar los pesos: apuesta 22,33 y error 2/3, mejor que cada termómetro por separado (0,8 y 2).

## Narración

<!-- b1 -->
La apuesta queda en veinte, más dos tercios por tres, más un sexto por dos. Veintidós coma tres tres. ¿Y el error? Es la varianza, cuatro, menos cada peso por su covarianza con la temperatura. Cuatro, menos dos tercios por cuatro, menos un sexto por cuatro, da dos tercios, cero coma seis siete. Con A solo era cero coma ocho, y con B solo, dos. Juntos, mejor que el mejor de los dos.

- «La apuesta queda en veinte» → `ap`: arriba, «ŷ = 20»
- «más dos tercios por tres» → `t1`: «+ 2/3 · 3», con «23 − 20» debajo del 3
- «más un sexto por dos» → `t2`: «+ 1/6 · 2», con «22 − 20» debajo del 2
- «Veintidós coma tres tres» → `res`: «≈ 22,33» en ámbar
- «¿Y el error?» → `err`: debajo, «Error =» en rojo
- «Es la varianza, cuatro» → `e4`: «4»
- «menos cada peso por su covarianza» → `ec`: «− h_A · 4 − h_B · 4», en gris
- «Cuatro, menos dos tercios por cuatro» → `en1`: debajo, «4 − 2/3 · 4»
- «menos un sexto por cuatro» → `en2`: «− 1/6 · 4»
- «da dos tercios» → `e23`: «= 2/3»
- «cero coma seis siete» → `e067`: «≈ 0,67»
- «Con A solo era cero coma ocho» → `ba`: a la derecha, una barra roja «Solo A» de 0,8
- «con B solo, dos» → `bb`: una barra «Solo B» de 2
- «Juntos» → `bab`: una barra «A y B» de 0,67
- «mejor que el mejor de los dos» → `mejor`: la barra de A y B se resalta en verde, con un tilde

---

# Escena 06 — UnaTablaDeNumeros

**Capítulo YouTube:** Una tabla de números
**Objetivo:** presentar la matriz de covarianzas (diagonal y fuera de la diagonal) y cómo se multiplica una matriz por una columna, fila por fila.

## Narración

<!-- b1 -->
Con tres termómetros habría tres ecuaciones, y con diez, diez. Para no escribirlas una a una se usa una matriz, que es una tabla de números. Aquí, la tabla de covarianzas entre las lecturas. En la diagonal va la varianza de cada termómetro, cinco y ocho. Fuera de la diagonal, la covarianza entre los dos, cuatro, y otra vez cuatro.

- «Con tres termómetros» → `tres`: arriba, las dos ecuaciones como «5h_A + 4h_B = 4» y «4h_A + 8h_B = 4»; debajo, una tercera tenue
- «con diez, diez» → `diez`: la columna de ecuaciones tenues crece hasta diez
- «se usa una matriz» → `matriz`: las tenues se van; en el centro, los corchetes de una matriz de dos por dos
- «una tabla de números» → `tabla`: una rejilla fina de cuatro casillas dentro de los corchetes
- «la tabla de covarianzas entre las lecturas» → `cov`: rótulos «x_A», «x_B» encima de las columnas y a la izquierda de las filas
- «En la diagonal» → `diag`: una banda ámbar tenue recorre la diagonal
- «cinco y ocho» → `c58`: «5» y «8» en ámbar
- «Fuera de la diagonal» → `fuera`: las otras dos casillas se marcan en cian
- «cuatro, y otra vez cuatro» → `c44`: «4» y «4» en cian

<!-- b2 -->
Una matriz por una columna de números se calcula fila por fila. Cada fila se multiplica, término a término, por la columna, y se suma. La primera fila, cinco y cuatro, por los dos pesos, da cinco veces el peso de A más cuatro veces el de B. La segunda, cuatro veces el de A más ocho veces el de B. Son justo los lados izquierdos de nuestras dos ecuaciones.

- «por una columna de números» → `col`: a la derecha de la matriz, la columna «h_A, h_B» con sus corchetes
- «fila por fila» → `filas`: un marco ámbar rodea la primera fila
- «término a término» → `tat`: arcos finos unen el 5 con h_A y el 4 con h_B
- «y se suma» → `suma`: «=» a la derecha de la columna
- «La primera fila» → `f1`: se resalta el marco de la primera fila
- «por los dos pesos» → `pesos`: se resalta la columna de los pesos
- «da cinco veces el peso de A» → `r1a`: «5h_A»
- «más cuatro veces el de B» → `r1b`: «+ 4h_B»
- «La segunda» → `f2`: el marco baja a la segunda fila
- «cuatro veces el de A más ocho veces el de B» → `r2`: «4h_A + 8h_B»
- «Son justo» → `justo`: los dos resultados se enmarcan
- «los lados izquierdos» → `izq`: se resaltan los lados izquierdos de las ecuaciones de arriba y los dos resultados

---

# Escena 07 — EcuacionesNormales

**Capítulo YouTube:** Las ecuaciones normales
**Objetivo:** escribir C_xx h = c_xy, decir por qué se llaman normales, resolver con la inversa (determinante 24) y escribir el error σ² − cᵀh con su porqué.

## Narración

<!-- b1 -->
Y los lados derechos forman otra columna, la covarianza de cada lectura con la temperatura, cuatro y cuatro. Así que las dos ecuaciones, y las de cualquier número de mediciones, caben en una línea. La matriz de covarianzas de las mediciones, por los pesos, igual a las covarianzas con lo que se estima. Se llaman ecuaciones normales, porque normal, en geometría, significa perpendicular.

- «los lados derechos» → `der`: vuelve la matriz por la columna; arriba, se resaltan los «4» de la derecha de las ecuaciones
- «forman otra columna» → `col2`: a la derecha, «=» y la columna «4, 4»
- «con la temperatura» → `cy`: debajo de la columna, «cov(x, y)»
- «Así que las dos ecuaciones» → `dos`: un marco rodea toda la cuenta de la matriz
- «cualquier número de mediciones» → `cualquier`: detrás, la matriz crece en fantasma con puntos suspensivos
- «caben en una línea» → `linea`: abajo, una caja vacía
- «La matriz de covarianzas de las mediciones» → `cxx`: en la caja, «C_xx», con una flecha desde la matriz
- «por los pesos» → `h`: «h», con una flecha desde la columna de los pesos
- «igual a las covarianzas con lo que se estima» → `cxy`: «= c_xy», con una flecha desde la columna 4, 4
- «Se llaman ecuaciones normales» → `normales`: «Ecuaciones normales» entra con rebote
- «normal, en geometría» → `geo`: a la derecha, una recta con un segmento que la corta en ángulo recto
- «significa perpendicular» → `perp`: «Normal = perpendicular»

<!-- b2 -->
Resolverlas es como dividir entre la matriz, y eso se llama multiplicar por su inversa. Existe si un número llamado determinante no es cero. En dos por dos, es el producto de la diagonal menos el de fuera. Cinco por ocho menos cuatro por cuatro, veinticuatro. Y el error es la varianza menos los pesos por las covarianzas con la temperatura, porque, al ser perpendicular a las lecturas, el error solo comparte con la temperatura su propio tamaño.

- «Resolverlas» → `res`: corte; arriba, «C_xx h = c_xy»
- «dividir entre la matriz» → `div`: debajo, «h = c_xy ÷ C_xx» en gris
- «multiplicar por su inversa» → `inv`: se transforma en «h = C_xx⁻¹ c_xy»
- «un número llamado determinante» → `det`: abajo a la izquierda, la matriz 5 4 / 4 8 y «det»
- «no es cero» → `ne0`: «≠ 0»
- «el producto de la diagonal» → `pd`: la diagonal 5, 8 se marca en ámbar
- «menos el de fuera» → `pf`: los 4 se marcan en cian
- «Cinco por ocho» → `n58`: «5 · 8»
- «menos cuatro por cuatro» → `n44`: «− 4 · 4»
- «veinticuatro» → `d24`: «= 24» en verde
- «Y el error es la varianza» → `err`: a la derecha, «Error = σ_y²»
- «menos los pesos por las covarianzas» → `menos`: «− (4h_A + 4h_B)»
- «al ser perpendicular a las lecturas» → `perp2`: debajo, el plano pequeño con las lecturas, la sombra y el error en ángulo recto
- «el error solo comparte con la temperatura» → `comparte`: se resalta la flecha azul de la temperatura
- «su propio tamaño» → `tam`: se resalta el error rojo

---

# Escena 08 — SentidoComun

**Capítulo YouTube:** Comprobaciones de sentido común
**Objetivo:** leer los pesos (cada termómetro pesa según su ruido, la suma es menor que uno) y ver que más mediciones nunca empeoran.

## Narración

<!-- b1 -->
Dos comprobaciones de sentido común. A pesa dos tercios y B un sexto, cuatro veces más. Y el ruido de A es cuatro veces más pequeño. Cada termómetro pesa según lo poco que se equivoca. Además, los pesos suman cinco sextos, menos de uno, así que la estimación sigue tirando un poco hacia la media. Y una regla general, añadir una medición nunca empeora el error.

- «Dos comprobaciones» → `dos`: arriba, dos casillas «1» y «2»
- «A pesa dos tercios» → `pa`: a la izquierda, una barra ámbar alta «h_A = 2/3»
- «y B un sexto» → `pb`: a su lado, una barra ámbar baja «h_B = 1/6»
- «cuatro veces más» → `x4`: entre las barras, «× 4»
- «Y el ruido de A» → `ra`: a la derecha, una barra magenta baja «σ² = 1» para A
- «cuatro veces más pequeño» → `r4`: una barra magenta alta «σ² = 4» para B y «÷ 4»
- «Cada termómetro pesa según lo poco que se equivoca» → `regla`: «2/3 : 1/6 = 4 : 1» en verde
- «Además» → `ademas`: corte; se enciende la casilla 2
- «los pesos suman cinco sextos» → `suma`: «2/3 + 1/6 = 5/6»
- «menos de uno» → `menos1`: «< 1»
- «tirando un poco hacia la media» → `media`: una recta de 20 a 24 con el 22,33 y una flecha corta hacia el 20
- «una regla general» → `general`: corte; tres barras rojas vacías «Sin dato», «A», «A y B»
- «nunca empeora el error» → `nunca`: las barras crecen, 4, 0,8 y 0,67, en escalera hacia abajo

---

# Escena 09 — LaCopiaExacta

**Capítulo YouTube:** Tres segundos termómetros
**Objetivo:** abrir la encuesta de los tres segundos termómetros y ver el primero: una copia exacta no aporta y deja la matriz sin inversa.

## Narración

<!-- b1 -->
¿Añadir un termómetro siempre ayuda? Depende de cómo sea su ruido. Veamos tres segundos termómetros distintos, y piensa cada respuesta antes de oírla. El primero es un cable que copia la lectura de A, así que marca exactamente lo mismo. ¿Cuánto aporta?

- «¿Añadir un termómetro siempre ayuda?» → `ayuda`: el termómetro A y, a su lado, un «+ ?»
- «Depende de cómo sea su ruido» → `ruido`: bajo el «?», una traza de ruido magenta
- «tres segundos termómetros distintos» → `tres`: tres tarjetas boca abajo, «B₁», «B₂» y «B₃»
- «piensa cada respuesta» → `piensa`: un reloj de arena sobre las tarjetas
- «El primero es un cable» → `b1`: la tarjeta B₁ se da la vuelta: un termómetro unido a A por un cable
- «marca exactamente lo mismo» → `igual`: los dos marcan «23»
- «¿Cuánto aporta?» → `cuanto`: un «?» ámbar sobre B₁

<!-- b2 -->
Nada, claro. Y las ecuaciones lo notan. La matriz de covarianzas tiene todas sus casillas iguales, cinco. El determinante, cinco por cinco menos cinco por cinco, es cero, y la matriz no tiene inversa. Hay infinitos pares de pesos que dan la misma estimación, porque da igual cómo repartas el peso entre dos lecturas idénticas. Una medición repetida no es información nueva.

- «Nada, claro» → `nada`: el «?» se convierte en «0»
- «Y las ecuaciones lo notan» → `notan`: corte; a la izquierda, «C_xx h = c_xy»
- «La matriz de covarianzas» → `mat`: la matriz 5 5 / 5 5
- «todas sus casillas iguales» → `iguales`: las cuatro casillas se resaltan
- «El determinante» → `det`: «det = 5 · 5 − 5 · 5»
- «es cero» → `cero`: «= 0» en rojo
- «no tiene inversa» → `noinv`: «C⁻¹» tachado en rojo
- «infinitos pares de pesos» → `pares`: a la derecha, «(0,8 ; 0)», «(0,4 ; 0,4)», «(0 ; 0,8)» uno tras otro
- «dan la misma estimación» → `misma`: cada par apunta a «ŷ = 22,4»
- «da igual cómo repartas» → `reparte`: los pares se resaltan
- «dos lecturas idénticas» → `identicas`: debajo, A y B₁ pequeños, los dos con «23»
- «Una medición repetida no es información nueva» → `nueva`: «Repetida = nada nuevo» entra con rebote

---

# Escena 10 — LaCopiaEmpeorada

**Capítulo YouTube:** La copia empeorada
**Objetivo:** ver que un termómetro que solo añade ruido a la lectura de A recibe peso cero y no mejora el error.

## Narración

<!-- b1 -->
El segundo es una copia empeorada. Marca lo mismo que A, más un ruido propio de varianza tres. En total, su ruido tiene varianza cuatro, como el B de antes. Pero al resolver, su peso sale cero. Todo lo que sabe de la temperatura ya lo sabía A; lo demás es ruido añadido. El error se queda en cero coma ocho, igual que con A solo.

- «una copia empeorada» → `b2`: la tarjeta B₂ se da la vuelta; arriba, la cadena A → ⊕ → B₂
- «Marca lo mismo que A» → `igual`: una ficha «x_A» viaja de A a la suma
- «un ruido propio de varianza tres» → `r3`: entra en la suma una traza magenta con «σ² = 3»
- «su ruido tiene varianza cuatro» → `r4`: bajo B₂, «1 + 3 = 4»
- «como el B de antes» → `antes`: a su lado, el B de antes, tenue, con «σ² = 4»
- «al resolver» → `res`: abajo, la matriz 5 5 / 5 8 por los pesos igual a 4, 4
- «su peso sale cero» → `cero`: «h = (0,8 ; 0)», con el 0 en rojo
- «ya lo sabía A» → `sabia`: se resalta A en la cadena
- «ruido añadido» → `anadido`: se resalta la traza magenta de la suma
- «se queda en cero coma ocho» → `e08`: «Error = 0,8»
- «igual que con A solo» → `igual_a`: «= solo A»

---

# Escena 11 — ElRuidoDoble

**Capítulo YouTube:** Un peso negativo
**Objetivo:** ver que un termómetro con el doble del ruido de A permite restarlo: pesos 2 y −1, error cero, comprobado con números.

## Narración

<!-- b1 -->
El tercero es el más curioso. Su ruido es exactamente el doble que el de A. Si A se pasa medio grado, este se pasa un grado. Al resolver, los pesos salen dos y menos uno. ¡Un peso negativo! Y el error, cero. ¿Por qué? Porque la lectura de este termómetro menos la de A es justo el ruido de A. Con esa resta sabes cuánto se equivocó A, y lo quitas.

- «El tercero» → `b3`: la tarjeta B₃ se da la vuelta: dos termómetros, A y B₃
- «el más curioso» → `curioso`: un «!» ámbar sobre B₃
- «el doble que el de A» → `doble`: bajo cada uno, su ruido; el de B₃ es la misma traza estirada al doble
- «Si A se pasa medio grado» → `medio`: sobre A, «+0,5» en magenta
- «este se pasa un grado» → `uno`: sobre B₃, «+1»
- «Al resolver» → `res`: a la derecha, la matriz 5 6 / 6 8 por los pesos igual a 4, 4
- «dos y menos uno» → `pesos`: «h = (2 ; −1)»
- «¡Un peso negativo!» → `neg`: el «−1» se resalta en ámbar
- «Y el error, cero» → `e0`: «Error = 0» en verde
- «¿Por qué?» → `porque`: corte; un «?» ámbar
- «menos la de A» → `resta`: «x_B₃ − x_A»
- «justo el ruido de A» → `va`: «= v_A», en magenta
- «sabes cuánto se equivocó A» → `sabes`: se resalta «v_A»
- «y lo quitas» → `quita`: «y = x_A − v_A»

<!-- b2 -->
Con números. A marca veintitrés y el tercero, veinticuatro. La diferencia, uno, es el ruido de A, así que la temperatura es veintitrés menos uno, veintidós, sin error. Y eso dan los pesos. Veinte, más dos por tres, menos uno por cuatro. Veintidós. Una medición no vale por lo que se parece a la señal, sino por lo que trae de nuevo. Y las ecuaciones normales lo calculan solas.

- «A marca veintitrés» → `a23`: abajo, «x_A = 23»
- «el tercero, veinticuatro» → `b24`: «x_B₃ = 24»
- «La diferencia, uno» → `dif`: «24 − 23 = 1»
- «es el ruido de A» → `esva`: «= v_A»
- «veintitrés menos uno, veintidós» → `t22`: «y = 23 − 1 = 22» en verde
- «Y eso dan los pesos» → `pesos2`: a la derecha, «ŷ = 20»
- «más dos por tres» → `p2`: «+ 2 · 3»
- «menos uno por cuatro» → `p1`: «− 1 · 4»
- «cuatro. Veintidós» → `ok22`: «= 22» y un tilde verde
- «no vale por lo que se parece a la señal» → `parece`: corte; «Parecerse a la señal» aparece y se tacha
- «lo que trae de nuevo» → `nuevo`: «Vale lo que trae de nuevo» entra con rebote
- «lo calculan solas» → `solas`: debajo, «C_xx h = c_xy»

---

# Escena 12 — LlegaUnDatoNuevo

**Capítulo YouTube:** Llega un dato nuevo
**Objetivo:** plantear la actualización: ya hay una estimación con A, llega B; predecir B y medir la sorpresa (−0,4).

## Narración

<!-- b1 -->
Una situación muy habitual. Ya tenías una estimación y llega una medición nueva. Primero leíste A, que marcaba veintitrés, y apostaste veintidós coma cuatro, con error cero coma ocho. Ahora llega B, el que tiene ruido de varianza cuatro, y marca veintidós. ¿Hay que rehacer todas las cuentas desde el principio?

- «Una situación muy habitual» → `hab`: una línea de tiempo horizontal
- «Ya tenías una estimación» → `tenias`: un punto ámbar en la línea
- «llega una medición nueva» → `nueva`: una flecha cian baja hacia la línea, más a la derecha
- «Primero leíste A» → `a`: el termómetro A sobre el primer punto, con «x_A = 23»
- «apostaste veintidós coma cuatro» → `ap`: «ŷ = 22,4» en ámbar
- «con error cero coma ocho» → `e08`: «Error 0,8» en rojo
- «Ahora llega B» → `b`: el termómetro B sobre el segundo punto
- «y marca veintidós» → `b22`: «x_B = 22»
- «¿Hay que rehacer todas las cuentas» → `rehacer`: abajo, el sistema de dos por dos tenue, con un «?»

<!-- b2 -->
No hace falta. Antes de mirar B, ¿qué esperabas que marcara? B es la temperatura más un ruido de media cero, así que tu mejor apuesta para B era tu apuesta para la temperatura, veintidós coma cuatro. Pero marca veintidós. La sorpresa es la diferencia entre lo que llega y lo que esperabas, menos cero coma cuatro.

- «No hace falta» → `no`: el sistema se tacha y se va
- «¿qué esperabas que marcara?» → `esperabas`: sobre B, una burbuja «x_B = ?»
- «B es la temperatura» → `bym`: abajo, «x_B = y + v_B»
- «un ruido de media cero» → `media0`: debajo, «E[v_B] = 0»
- «tu mejor apuesta para B» → `apy`: «x̂_B = ŷ»
- «veintidós coma cuatro» → `e224`: «= 22,4» y la burbuja pasa a «22,4»
- «Pero marca veintidós» → `m22`: se resalta «x_B = 22»
- «La sorpresa» → `sorpresa`: «Sorpresa» entra con rebote
- «menos cero coma cuatro» → `s04`: «= 22 − 22,4 = −0,4» en ámbar

---

# Escena 13 — LaGanancia

**Capítulo YouTube:** La sorpresa y la ganancia
**Objetivo:** usar la sorpresa como un dato nuevo con la fórmula de la recta: ganancia 0,8/4,8 = 1/6; la estimación corregida 22,33 y el error 0,67 coinciden con el sistema.

## Narración

<!-- b1 -->
La sorpresa es un dato nuevo, y se usa con la fórmula de la recta de siempre, covarianza entre varianza. La sorpresa está hecha del error que todavía tenías, de varianza cero coma ocho, más el ruido de B, de varianza cuatro. Su varianza es la suma, cuatro coma ocho. Y lo que comparte con tu error es cero coma ocho. El factor es cero coma ocho entre cuatro coma ocho, un sexto.

- «La sorpresa es un dato nuevo» → `dato`: arriba a la izquierda, «Sorpresa = −0,4» en una caja cian
- «la fórmula de la recta de siempre» → `recta`: arriba a la derecha, la fórmula de la recta del E3, en gris
- «covarianza entre varianza» → `cv`: arriba a la derecha, «Factor = cov / var»
- «del error que todavía tenías» → `err`: en el centro, «Sorpresa = (y − ŷ)», en rojo
- «de varianza cero coma ocho» → `v08`: debajo, «σ² = 0,8»
- «más el ruido de B» → `vb`: «+ v_B» en magenta
- «de varianza cuatro» → `v4`: debajo, «σ² = 4»
- «la suma, cuatro coma ocho» → `v48`: «var = 0,8 + 4 = 4,8»
- «lo que comparte con tu error» → `comp`: «cov = 0,8»
- «El factor es» → `factor`: abajo, «Factor =»
- «cero coma ocho entre cuatro coma ocho» → `div`: «0,8 / 4,8»
- «un sexto» → `sexto`: «= 1/6» en verde

<!-- b2 -->
La estimación nueva es la vieja más un sexto por la sorpresa. Veintidós coma cuatro, menos cero coma cero seis siete, da veintidós coma tres tres, lo mismo que resolviendo el sistema entero. Y el error baja en la misma proporción, cero coma ocho por cinco sextos, que da cero coma seis siete. También coincide con el sistema.

- «La estimación nueva» → `nueva`: corte; «ŷ nueva =»
- «es la vieja» → `vieja`: «22,4»
- «más un sexto por la sorpresa» → `mas`: «+ 1/6 · (−0,4)»
- «Veintidós coma cuatro, menos» → `v224`: debajo, «= 22,4»
- «menos cero coma cero seis siete» → `m067`: «− 0,067»
- «veintidós coma tres tres» → `r2233`: «≈ 22,33» en ámbar
- «resolviendo el sistema entero» → `sis`: a la derecha, una tarjeta «Sistema: 22,33» y un «=» verde
- «el error baja» → `eb`: «Error =»
- «cero coma ocho por cinco sextos» → `p56`: «0,8 · 5/6»
- «que da cero coma seis siete» → `e067`: «≈ 0,67»
- «También coincide» → `coinc`: la tarjeta del sistema suma «0,67» y un tilde verde

---

# Escena 14 — HaciaKalman

**Capítulo YouTube:** La idea del filtro de Kalman
**Objetivo:** quedarse con la forma «vieja + ganancia · sorpresa», leer cuándo la ganancia es grande o pequeña y sembrar el filtro de Kalman (capítulo 12).

## Narración

<!-- b1 -->
Esa forma de trabajar, la estimación vieja más una ganancia por la sorpresa, es una de las ideas más útiles de la ingeniería. La ganancia es grande cuando tu error es grande comparado con el ruido de la medición, y pequeña en el caso contrario. Repetida en el tiempo, muestra a muestra, se convierte en el filtro de Kalman, que veremos en el capítulo doce.

- «la estimación vieja» → `vieja`: arriba, «ŷ nueva = ŷ vieja»
- «más una ganancia» → `gan`: «+ K ·»
- «por la sorpresa» → `sorp`: «sorpresa»
- «una de las ideas más útiles» → `util`: debajo, un bucle de cuatro cajas: Estimación → Predecir → Sorpresa → × Ganancia
- «La ganancia es grande» → `grande`: corte del bucle a la derecha; «K = error / (error + ruido)»
- «comparado con el ruido de la medición» → `comp`: «error ≫ ruido → K ≈ 1»
- «pequeña en el caso contrario» → `peq`: «error ≪ ruido → K ≈ 0»
- «Repetida en el tiempo» → `tiempo`: una ficha ámbar recorre el bucle
- «muestra a muestra» → `muestras`: abajo, una fila de muestras que se encienden una tras otra
- «el filtro de Kalman» → `kalman`: «Filtro de Kalman» entra con rebote
- «en el capítulo doce» → `c12`: «Capítulo 12» debajo

---

# Escena 15 — MuestrasDeUnaSenal

**Capítulo YouTube:** Cuando las mediciones son muestras
**Objetivo:** adelantar que con muestras de una señal las ecuaciones normales son las mismas (capítulos 10 y 12).

## Narración

<!-- b1 -->
Ahora, un adelanto. ¿Y si las mediciones son muestras de una misma señal? Lo que marcó el sensor hace un segundo, hace dos, hace tres. Las ecuaciones normales son exactamente las mismas. Covarianzas entre las muestras, por los pesos, igual a covarianzas con lo que se quiere adivinar. Con ellas predeciremos el futuro de una señal y limpiaremos el ruido de una grabación, en los capítulos diez y doce.

- «un adelanto» → `adelanto`: una señal del sensor se dibuja de izquierda a derecha
- «muestras de una misma señal» → `muestras`: sobre la señal, palitos en los instantes enteros
- «hace un segundo» → `m1`: el palito de n − 1 se enciende con «x[n−1]»
- «hace dos» → `m2`: «x[n−2]»
- «hace tres» → `m3`: «x[n−3]»
- «exactamente las mismas» → `mismas`: abajo, «C_xx h = c_xy»
- «Covarianzas entre las muestras» → `cxx`: se resalta «C_xx» y arcos unen las tres muestras entre sí
- «por los pesos» → `h`: se resalta «h»
- «lo que se quiere adivinar» → `cxy`: se resalta «c_xy» y un «?» en el futuro de la señal
- «predeciremos el futuro de una señal» → `pred`: a la derecha del «?», un punto ámbar; etiqueta «Capítulo 10 · Predecir»
- «limpiaremos el ruido de una grabación» → `limpia`: una traza ruidosa y su versión limpia; etiqueta «Capítulo 12 · Limpiar»
- «en los capítulos diez y doce» → `caps`: se resaltan las dos etiquetas

---

# Escena 16 — DecidirEnVezDeEstimar

**Capítulo YouTube:** ¿Y si hay que elegir?
**Objetivo:** abrir el capítulo 9: 0,79 no es un bit; a veces hay que decidir, con el costo de acertar o fallar.

## Narración

<!-- b1 -->
Pero queda una pregunta abierta desde el canal de bits. La mejor apuesta era cero coma setenta y nueve, y eso no es un bit. Muchas veces no hay que dar un número, sino elegir. ¿Se envió un cero o un uno? ¿Hay un avión en la pantalla del radar, o solo ruido? Eso ya no es estimar, es decidir, con la tercera forma de medir el error, acertar o fallar. Y es el tema del capítulo siguiente.

- «desde el canal de bits» → `canal`: el canal que confunde bits, con un 1 que entra
- «cero coma setenta y nueve» → `c79`: a la salida, «0,79» en ámbar
- «no es un bit» → `nobit`: una recta de 0 a 1 con el 0,79 entre los dos
- «sino elegir» → `elegir`: corte; dos casillas «0» y «1»
- «¿Se envió un cero o un uno?» → `cero_uno`: una flecha ámbar duda entre las dos casillas
- «¿Hay un avión» → `avion`: a la derecha, un radar con un avión pequeño
- «o solo ruido?» → `ruido`: el avión se apaga y queda una traza de ruido
- «Eso ya no es estimar» → `noest`: «Estimar» tachado
- «es decidir» → `decidir`: «Decidir» entra con rebote
- «acertar o fallar» → `acierto`: un tilde verde y una cruz roja
- «el tema del capítulo siguiente» → `cap9`: «Capítulo 9» debajo

---

# Escena 17 — Cierre

**Capítulo YouTube:** Resumen y siguiente capítulo

## Narración

<!-- b1 -->
En resumen, con varias mediciones el error tiene que ser perpendicular a cada una, y de ahí salen las ecuaciones normales. Cada medición vale por lo que trae de nuevo. Y cuando llega una más, basta con corregir por la sorpresa. En el próximo episodio, que abre el capítulo nueve, veremos «¿Un cero o un uno?».

- «con varias mediciones» → `varias`: el plano con las dos lecturas y la temperatura
- «perpendicular a cada una» → `perp`: la sombra, el error y los dos ángulos rectos
- «las ecuaciones normales» → `normales`: debajo, «C_xx h = c_xy»
- «lo que trae de nuevo» → `nuevo`: la figura se apaga; las tres tarjetas B₁, B₂ y B₃ con su error 0,8, 0,8 y 0
- «cuando llega una más» → `llega`: una flecha cian nueva baja hacia las tarjetas
- «corregir por la sorpresa» → `sorpresa`: «ŷ nueva = ŷ vieja + K · sorpresa»
- «En el próximo episodio» → `proximo`: todo se va hacia arriba
- «abre el capítulo nueve» → `cap9`: todo se va; «Capítulo 9» en gris
- «¿Un cero o un uno?» → `titulo`: el título «¿Un cero o un uno?» entra con rebote
