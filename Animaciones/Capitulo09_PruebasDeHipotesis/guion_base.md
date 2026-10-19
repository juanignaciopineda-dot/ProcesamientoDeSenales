# Capítulo 9 — Pruebas de hipótesis

> **Guion base: narración de todo el capítulo. No se renderiza.**
> Es la fuente de texto para los 6 episodios (ver `../README.md` §1 para qué
> escenas van en cada uno). Cada episodio copia de aquí su narración a su
> propio `E<N>_.../guion.md`, que es el que lleva gancho, cierre y momentos, y
> el que se anima. Las secciones "Visual" son ideas iniciales, no
> especificación.
>
> **Estado:** narración completa. **E1 (escenas 01–05) aprobado** por el
> usuario, con dos retoques ya aplicados (01·b5 y 02·b6). **E3 (escenas
> 11–15) aprobado**, con «voltios» agregado en 14·b5. **E4 (escenas 16–19)
> aprobado**, sin cambios. **E5 (escenas 20–23) aprobado**, con el retoque en
> 23·b4 («el cero coma setenta y nueve y el uno»). **E6 (escenas 24–28)
> aprobado**, sin cambios. E2 **esperando la aprobación del usuario**.
> Mientras no esté aprobada, cualquier ajuste de texto que pida el usuario se
> hace aquí primero, y después se copia al `guion.md` del episodio.

Guion para las 28 escenas del capítulo. Fuentes: `Apuntes/PROCESAMIENTO DE
SEÑALES.md` (sección "Pruebas De Hipótesis", líneas 504–596, sin los
Ejercicios Propuestos) y `Apuntes/PROCESAMIENTO DE SEÑALES - Cap 9 en
profundidad.md`: Parte 1 (el MAP minimiza el error total, fronteras y M
hipótesis, lema de Neyman-Pearson, pendiente de la ROC y punto de Bayes,
umbral de riesgo mínimo), Parte 2 (varianzas distintas, diseño con falsa
alarma fija, costes asimétricos y «riesgo no es error»), Parte 3 (ROC con
datos, AUC, cuántas simulaciones, Youden y tasa de error igual, prevalencia y
valor predictivo, calibración) y Parte 4 (detección y estimación, puente al
capítulo 13). Figuras de referencia: `c9-regiones-decision.svg`, `c9-roc.svg`,
`c9p-map-varianzas-distintas.svg`, `c9p-neyman-pearson-lema.svg`,
`c9p-roc-pendiente.svg`, `c9p-riesgo-costos.svg`, `c9p-auc.svg`,
`c9p-ppv-prevalencia.svg`, `c9p-estimacion-continuo.svg`.

**Qué se da por sabido y dónde se recuerda** (README §3, regla 2):
- del capítulo 7: el canal que confunde bits y su tabla (01, 02), Bayes, a
  priori y a posteriori, probabilidad total (01, 06), la densidad como altura y
  la probabilidad como área (03, 07), la campana de Gauss con su centro y su
  desvío (03), el test médico contado sobre mil personas (09), la derivada como
  pendiente (18), los grandes números (27);
- del capítulo 8: «0,79 no es un bit» (01), las tres formas de medir el error
  y la moda (01, 23), la media condicional (23);
- de matemáticas se explica aquí: estandarizar una campana y la función Q (07),
  la fórmula de la campana y el cociente de exponenciales (12), el logaritmo
  natural (12), la ecuación de segundo grado y hacia dónde abre una parábola
  (13), la recta tangente a una curva (19).

Cómo está escrito (README §3, "Explicar de forma explícita"): cada concepto
sigue el camino caso → cuenta a mano → dibujo → fórmula → comprobación. **Casi
todo el capítulo corre sobre un solo par de campanas**: el cero se envía como
0 voltios y el uno como 2 voltios, con ruido gaussiano de desvío 1; las
probabilidades a priori son las del canal del capítulo 7 (0,7 y 0,3) y la
medición que vuelve es 1,3 voltios. Las mismas dos campanas son después el
radar (escenas 14 a 19) y el análisis de sangre (20 a 22). Las deducciones
cortas se hacen enteras (la razón de verosimilitud, el umbral del riesgo, la
pendiente de la ROC); de las largas (el lema de Neyman-Pearson con integrales)
se hace la versión con números (sin nombrar el apunte: quien mira en YouTube
no sabe que existe). Hay
preguntas con pausa y sorpresas en las escenas 02, 04, 09, 10, 13, 20 y 27.

Convención: cada escena tiene Objetivo, qué hace falta saber antes, qué se ve,
y la narración partida en bloques `<!-- bN -->`. Castellano de España. Lo que
se dice: «hache cero», «hache uno», «pe cero», «pe uno», «erre», «falsa
alarma», «fallo» (en pantalla también «Miss»), «detección», «la razón de
verosimilitud» (en pantalla Λ), «eta», «la función cu». Todo texto en
pantalla empieza con mayúscula.

## Reparto en episodios

| Episodio | Escenas | Idea fuerza |
|---|---|---|
| E1 · ¿Un cero o un uno? | 01 ElegirNoEsEstimar, 02 CuatroReglas, 03 ElCanalPorDentro, 04 CurvasEscaladas, 05 PorQueEsLaMejor | Decidir es quedarse con la hipótesis más probable después de mirar, y eso combina lo que ves con lo que sabías antes |
| E2 · Dos maneras de equivocarse | 06 FalsaAlarmaYFallo, 07 ElAreaDeLaCola, 08 MoverElUmbral, 09 ElTestMedicoVuelve, 10 LaPrevalenciaManda | Hay dos errores distintos, mover el umbral cambia uno por otro, y cuánto creerle a un positivo depende de lo raro que sea lo que se busca |
| E3 · Un número y un umbral | 11 RazonDeVerosimilitud, 12 LaCuentaConCampanas, 13 DosUmbrales, 14 SinProbabilidadesAPriori, 15 ElPresupuesto | Toda decisión óptima es comparar la razón de verosimilitud con un umbral; lo único que cambia de un criterio a otro es el umbral |
| E4 · La curva de todos los umbrales | 16 CurvaRoc, 17 LeerLaCurva, 18 LaPendienteEsElUmbral, 19 ElPuntoDeBayes | La curva ROC es el detector entero, su pendiente es el umbral y cada criterio es un punto de ella |
| E5 · ¿Cuánto cuesta equivocarse? | 20 ErroresQueNoCuestanIgual, 21 ElUmbralDelRiesgo, 22 RiesgoNoEsError, 23 DecidirYEstimar | Si un error cuesta más que el otro, lo que se minimiza es el coste, no la probabilidad de error: cambia el umbral, no el detector |
| E6 · Decidir con datos de verdad | 24 RocConDatos, 25 AreaBajoLaCurva, 26 OrdenarNoEsCortar, 27 CuantasPruebas, 28 DeUnNumeroAUnaSenal | Con datos, la curva es una escalera; ordenar bien no es cortar bien, y cero errores vistos no es error cero |

El gancho y el cierre de cada episodio **no** están aquí: se escriben al
armar el `guion.md` del episodio (README §2, paso 8). Cada cierre anuncia el
episodio siguiente por su título. **El cierre del E5 del capítulo 8 tiene que
anunciar «¿Un cero o un uno?»** (su escena 21 ya termina con esa pregunta). El
cierre de E6 anuncia el E1 del capítulo 10, **«Mil grabaciones del mismo
ruido»**: la escena 28 ya lo prepara.

Narración base por episodio (sin gancho ni cierre): E1 ≈ 1.520 palabras, E2 ≈
1.480, E3 ≈ 1.520, E4 ≈ 1.090, E5 ≈ 1.090 y E6 ≈ 1.160. Son unos 7–10 min de
voz; con gancho y cierre, ~8,5–11 min. **E1, E2 y E3 son los más largos** (cinco
escenas cada uno): sus ganchos y cierres tienen que ser cortos, y si al armar
el `guion.md` pasan de ~10,5 min, los primeros candidatos a recortarse son el
bloque b5 de la escena 05 (tres hipótesis), el b6 de la escena 10 (la lección
para el radar) y el b6 de la escena 13 (la nota honesta sobre la cola
izquierda).

## Hilos que cruzan el capítulo

Para quien arme cada episodio: estos bucles ya están sembrados en la
narración y hay que respetarlos (y retomarlos en ganchos y cierres).

- **Los ejemplos que vuelven** (mismo dibujo y mismos números siempre):
  - **el canal que confunde bits** del capítulo 7 (escenas 01, 02, 06): 0,7 y
    0,3, cambia el bit un 10 %; tabla 0,63 · 0,07 · 0,03 · 0,27; a posteriori
    0,79 / 0,21 y 0,955 / 0,045. Las cuatro reglas fallan 0,10 · 0,30 · 0,70 ·
    0,90. Con unos rarísimos (0,05): 0,045 contra 0,095, y «siempre cero» falla
    0,05 contra 0,10;
  - **las dos campanas** (escenas 03 a 08, 11, 12, 14 a 22): centros 0 y 2,
    desvío 1. Sus números:
    - en 1,3 las alturas son 0,17 y 0,31 (razón 1,82); escaladas, 0,12 y 0,094;
      a posteriori del uno, 0,44;
    - a priori iguales: umbral 1, falsa alarma = fallo = Q(1) = 0,159;
    - a priori 0,7 / 0,3: η = 2,33, umbral 1,42, falsa alarma 0,077, fallo
      0,28, detección 0,72, error 0,054 + 0,085 = 0,139 (contra 0,159 con el
      umbral en 1 y 0,30 diciendo siempre cero);
    - la razón de verosimilitud es e^(2r − 2): 0,135 · 0,37 · 1 · 2,72 · 7,39 en
      r = 0 · 0,5 · 1 · 1,5 · 2; umbral = 1 + ln(η)/2;
    - falsa alarma fija en 5 %: umbral 1,645, detección 0,64 (η = 3,6); en 1 %:
      umbral 2,33, detección 0,37;
    - puntos de la ROC: umbral 3 → (0,001; 0,16), 2 → (0,023; 0,5), 1 → (0,16;
      0,84), 0 → (0,5; 0,977); área bajo la curva 0,92;
    - con costes (fallo 5, falsa alarma 1): η = 0,47, umbral 0,62, falsa alarma
      0,27, fallo 0,084, error 0,21, coste 0,31 (el MAP: error 0,139, coste 0,48);
  - **la medición de 1,3 voltios** (03, 04, 11, 20): con a priori iguales se
    decide uno; con 0,7 / 0,3 se decide cero; con costes se vuelve a decidir uno
    (decir «sano» cuesta 2,2 y decir «enfermo» 0,56);
  - **el test médico** del capítulo 7 (09, 10, y se paga en la 20): 1 %, 99 %,
    5 % → 17 %. Valor predictivo 2 % · 17 % · 69 % · 95 % con prevalencia
    0,1 % · 1 % · 10 % · 50 %. Repitiendo el test: 17 % → 80 % → 99 %. Su
    probabilidad de error es 5 % y la de «siempre sano» es 1 %;
  - **el radar** (06, 14, 15, 16): es el del capítulo 13;
  - **los ocho casos** (24, 25): orden + + − + − + − −, área 13/16 = 0,81.
- **«Lo que sabías antes pesa tanto como lo que ves»**: se abre en la escena 02
  (unos rarísimos), sigue en la 04 (el cruce se mueve), en la 10 (la
  prevalencia) y en la 11 (la evidencia tiene que compensar la ventaja).
- **«En cada columna, lo que menos falla»**: el argumento de por qué el MAP es
  óptimo se hace con la tabla en la escena 02 y se repite con infinitas
  columnas en la 05.
- **Mover el umbral cambia un error por otro** (08): es la semilla de la curva
  ROC (16) y de los tres criterios como tres puntos (19, 22).
- **«Lo mejor sería no hacer el test»** (09): bucle abierto a propósito, con
  promesa explícita. Se paga en la escena 20 (los errores no cuestan igual).
- **El presupuesto** (15): «primero lo que más rinde» vuelve en la 18 para
  explicar por qué la curva tiene panza hacia arriba.
- **Un número y un umbral**: MAP (11), Neyman-Pearson (15) y riesgo mínimo (21)
  son el mismo test. Los tres puntos sobre la misma curva se ven en la 22.
- **Puentes a otros capítulos:**
  - capítulo 8: paga «0,79 no es un bit» y «acertar o fallar da la moda» (01),
    y cierra el círculo con el coste cuadrático y la media condicional (23);
  - capítulo 13: lo hereda todo. Su guion base recuerda este capítulo entero
    porque se escribió antes; con este guion, sus escenas 01, 02, 10 y 12 pasan
    a ser repaso y usan las mismas palabras («fallo», «la función cu»,
    «falsa alarma»). La escena 28 de aquí anuncia sus dos primeras ideas («toda
    la señal en un solo número», «más datos no bastan») sin desarrollarlas;
  - capítulo 10: la escena 28 plantea la pregunta que lo abre.
- **Cierre del capítulo** (escena 28; cierre de E6, a escribir): para decidir
  con una señal entera hay que describir el ruido a lo largo del tiempo →
  «Mil grabaciones del mismo ruido».

## Recortes decididos

- El ejemplo de varianzas distintas se rehízo con los centros del capítulo (0 y
  2, desvíos 1 y 2) en vez del N(0, 1) contra N(3, 4) del "en profundidad": da
  umbrales −2,57 y 1,24 y evita que 1,42 aparezca dos veces con significados
  distintos. Los números están comprobados con Python.
- El diseño con falsa alarma fija se hace con las campanas, no con las
  exponenciales de la Parte 2.2 (habría que presentar otra distribución).
- El lema de Neyman-Pearson se demuestra con una tabla de cinco niveles
  (inventada, con números redondos); la versión con integrales y el argumento
  del intercambio no entran, y la escena 15 no remite al apunte. La regla
  aleatorizada en el umbral no entra.
- Las probabilidades a priori son 0,7 y 0,3 (las del canal del capítulo 7) y no
  0,6 y 0,4 como en la Parte 2.3: por eso los números del riesgo son otros
  (umbral 0,62 y no 0,40). La idea y el coste del fallo (5) son los mismos.
- La demostración de que el MAP minimiza el error total se hace sin escribir la
  integral: se dice qué es (un promedio con pesos no negativos) y se dibuja.
- M hipótesis: solo el caso de tres niveles (0, 2 y 4 voltios) en un bloque.
- El estadístico de Mann-Whitney se usa (contar parejas) pero no se nombra. La
  fórmula del área para dos campanas, Φ(d/√2), no se dice: solo el 0,92.
- La receta práctica de la Parte 3.7 no se lee como lista: sus puntos están
  repartidos en las escenas 24 a 27.
- La fórmula Σ r[n]s[n] y el filtro adaptado no se adelantan: son del capítulo 13.
- Los Ejercicios Propuestos no se resuelven.

## Pronunciación

Probar de oído antes de sintetizar (README §9): Neyman-Pearson, Bayes, Youden,
Gauss; «hache cero», «hache uno», «pe cero», «pe uno», «erre», «eta», «lambda
mayúscula», «la función cu», «miss», «curva ROC» (¿«roc» o «erre o ce»?). Las
siglas MAP, AUC, PAM y LRT **no se dicen**: se dice «máximo a posteriori»,
«área bajo la curva», «modulación por amplitud de pulsos» y «test de razón de
verosimilitud», y la sigla aparece solo en pantalla.

## Piezas visuales nuevas

Ya existen en `comun/figuras.py` y se reutilizan: `Curva` y `gaussiana`,
`TablaDecision` (Cap. 13 E1, la tabla 2 × 2 de realidad contra decisión),
`dens3`, `cola3`, `umbral3` y `rejilla3` (Cap. 13 E3: campanas, colas
sombreadas, marca de umbral y cien puntos), `radar13()` (Cap. 13 E6), la tabla
conjunta del canal (Caps. 7 y 8) y la grilla de personas del test médico
(Cap. 7 E2). Nuevas (sección «capítulo 09, episodio N»):
- las dos campanas escalables: cada una con un factor (su a priori) que se
  anima, el punto de cruce marcado y las dos regiones de decisión coloreadas
  sobre el eje;
- una regla vertical en la medición (1,3) con las dos alturas leídas;
- tabla de las cuatro reglas del canal con su error;
- campana estándar con cola sombreada y tabla corta de Q;
- curva del valor predictivo contra la prevalencia;
- la gráfica de la razón de verosimilitud contra r, con el umbral η horizontal;
- campana estrecha y campana ancha con dos umbrales y tres regiones;
- la «mochila»: cinco casillas con coste, rendimiento y cociente;
- plano de la ROC: punto que se mueve al deslizar el umbral, diagonal, familia
  de curvas, recta tangente con su pendiente, rectas paralelas de igual error;
- tabla de costes 2 × 2;
- fila de niveles que se multiplican (2, 3, 9, 100) hasta volverse un eje continuo;
- tira de ocho casos etiquetados y la escalera de la ROC empírica, con sus columnas.

---

# Escena 01 — ElegirNoEsEstimar

**Objetivo:** plantear el problema del capítulo (elegir entre dos explicaciones
a partir de un dato), dar nombre a las hipótesis y a las probabilidades a priori
y a posteriori, y llegar a la regla del máximo a posteriori con el canal de bits.

**Qué hace falta saber antes:** capítulo 7, escena 08 (Bayes con el canal);
capítulo 8, escenas 04 y 06 (la moda; «0,79 no es un bit»). Se recuerdan aquí.

**Visual:**
- «0,79» entre un «0» y un «1», con un «?» ámbar (el dibujo del capítulo 8). El
  0,79 se tacha y queda la pregunta «¿0 o 1?».
- Dos casillas: «H₀ · Se envió 0» y «H₁ · Se envió 1». Debajo, «p₀ = 0,7» y
  «p₁ = 0,3» con el rótulo «A priori».
- El árbol del canal del capítulo 7: «0,3 · 0,9 = 0,27», «0,7 · 0,1 = 0,07»,
  suma «0,34».
- Dos barras «A posteriori»: «0,79» y «0,21» para «Recibido 1»; «0,045» y
  «0,955» para «Recibido 0». La más alta de cada par se ilumina.
- Rótulo: «Máximo a posteriori · MAP».

## Narración

<!-- b1 -->
En el capítulo anterior quedó una pregunta abierta. Por un canal se envían
ceros y unos, recibes un uno, y la mejor estimación de lo enviado era cero coma
setenta y nueve. Pero eso no es un bit. El receptor de tu móvil no puede
entregar cero coma setenta y nueve: tiene que elegir. Cero o uno. Eso es
decidir, y es el tema de este capítulo.

<!-- b2 -->
Pongamos nombres. Cada explicación posible se llama hipótesis. La hipótesis
cero, hache cero, dice: se envió un cero. La hipótesis uno, hache uno, dice: se
envió un uno. Solo una es verdad, y no sabemos cuál. Tenemos dos cosas: un
dato, que es lo recibido, y lo que ya sabíamos antes de mirar.

<!-- b3 -->
Lo que ya sabíamos es que se envía un cero el setenta por ciento de las veces
y un uno el treinta. Son las probabilidades a priori, pe cero y pe uno: valen
antes de recibir nada. Y sabemos cómo es el canal: cambia el bit una de cada
diez veces.

<!-- b4 -->
Recibes un uno. Hay dos caminos para eso. Se envió un uno y llegó bien: cero
coma tres por cero coma nueve, cero coma veintisiete. O se envió un cero y el
canal lo cambió: cero coma siete por cero coma uno, cero coma cero siete. Por
la regla de Bayes, la probabilidad de hache uno es cero coma setenta y nueve, y
la de hache cero, cero coma veintiuno.

<!-- b5 -->
Esas son las probabilidades a posteriori: las de después de mirar. ¿Con cuál
te quedas? Con la mayor: dices uno. Y si recibes un cero, la cuenta da cero
coma noventa y cinco para el cero: dices cero. Esta regla se llama máximo a
posteriori. Es la tercera forma de medir el error del capítulo anterior, la de
acertar o fallar, que lleva a quedarse con lo más probable: la moda.

<!-- b6 -->
Aquí la regla acaba diciendo algo muy simple: cree lo que recibes. Parece
obvio. Pero ¿es de verdad lo mejor que se puede hacer? ¿Y será siempre así?

---

# Escena 02 — CuatroReglas

**Objetivo:** comprobar con números que el máximo a posteriori es la mejor regla
(enumerando las cuatro reglas posibles del canal), entender por qué (en cada
columna se falla la casilla pequeña) y ver, con unos rarísimos, que lo que se
sabía antes puede pesar más que el dato.

**Qué hace falta saber antes:** escena 01; capítulo 7, escena 17 (la tabla
conjunta del canal).

**Visual:**
- Tabla de cuatro reglas, una por renglón: «Creer lo recibido», «Siempre 0»,
  «Siempre 1», «Llevar la contraria». Al lado, su error: «0,10», «0,30»,
  «0,70», «0,90». La primera se enmarca en verde.
- La tabla conjunta del canal (mismo dibujo del capítulo 7): «0,63 · 0,07 / 0,03
  · 0,27». Columna «Recibido 1»: 0,27 en verde (acierto) y 0,07 en rojo (fallo).
  Columna «Recibido 0»: 0,63 en verde y 0,03 en rojo. Suma «0,07 + 0,03 = 0,10».
- Pregunta con pausa: «Unos: 1 de cada 20. Recibes un 1. ¿Qué dices?».
- Cuenta: «0,05 · 0,9 = 0,045» contra «0,95 · 0,1 = 0,095».
- «Siempre 0 → 0,05» contra «Creer → 0,10».

## Narración

<!-- b1 -->
Aquí se puede comprobar, porque solo hay cuatro reglas posibles. Lo recibido
solo puede ser un cero o un uno, y en cada caso hay que decir cero o uno. Dos
por dos, cuatro reglas. Calculemos cuánto falla cada una.

<!-- b2 -->
Primera: creer lo recibido. Falla cuando el canal cambia el bit: un diez por
ciento. Segunda: decir siempre cero. Falla cuando se envió un uno: un treinta
por ciento. Tercera: decir siempre uno. Falla el setenta. Cuarta: llevar la
contraria. Falla el noventa. Gana la primera, que es la del máximo a posteriori.

<!-- b3 -->
¿Por qué gana? Mira la tabla del canal, columna por columna. En la columna de
recibir un uno hay dos casillas: cero coma veintisiete, se envió un uno, y cero
coma cero siete, se envió un cero. Si dices uno, aciertas la grande y fallas la
pequeña. Si dices cero, al revés. Elegir lo más probable es fallar la casilla
pequeña.

<!-- b4 -->
En la otra columna pasa lo mismo: dices cero y fallas solo cero coma cero tres.
Y si en cada columna fallas lo menos posible, el total también es el menor
posible: cero coma cero siete más cero coma cero tres, un diez por ciento.
Ninguna regla puede bajar de ahí.

<!-- b5 -->
Ahora una pregunta, y piénsala antes de seguir. Supón que los unos fueran
rarísimos: uno de cada veinte. Recibes un uno. ¿Qué dices? La cuenta: se envió
un uno y llegó bien, cero coma cero cinco por cero coma nueve, cero coma cero
cuarenta y cinco. Se envió un cero y se cambió, cero coma noventa y cinco por
cero coma uno: cero coma cero noventa y cinco.

<!-- b6 -->
Es más probable que fuera un cero estropeado. La mejor regla es decir siempre
cero, sin mirar lo recibido: falla un cinco por ciento, y creer lo recibido
fallaría un diez. Lo que sabías antes puede pesar más que lo que ves. Decidir
bien es combinar las dos cosas.

---

# Escena 03 — ElCanalPorDentro

**Objetivo:** abrir el canal: la medición es un número continuo, amplitud más
ruido. Ver las dos campanas (una por hipótesis), leer sus alturas en la medición
y llamarlas verosimilitud. Con a priori iguales, gana la más alta y el umbral
queda a mitad de camino.

**Qué hace falta saber antes:** capítulo 7, escenas 11 y 12 (densidad: la altura
no es una probabilidad; la campana de Gauss, su centro y su desvío). Se
recuerdan aquí.

**Visual:**
- La caja del canal se abre: un «0» sale como un nivel de «0 V», un «1» como un
  pulso de «2 V». Por el cable se le suma ruido (magenta) y llega un punto que
  tiembla.
- La fórmula, pieza a pieza: «R = A + V», con «A» en azul (`SENAL`), «V» en
  magenta (`RUIDO`) y «R» en cian (`MEDIDA`). Rótulo: «PAM».
- Una campana centrada en 0 («Si se envió 0») y otra igual centrada en 2 («Si
  se envió 1»); la segunda aparece deslizando la primera.
- Una regla vertical en «r = 1,3»; dos puntos donde corta a las campanas, con
  sus alturas «0,17» y «0,31». Rótulo «Verosimilitud».
- Las dos campanas se cruzan en «1»; el eje se colorea: a la izquierda «Decir
  0», a la derecha «Decir 1».

## Narración

<!-- b1 -->
Hasta ahora el canal era una caja que cambiaba bits. Vamos a abrirla. Un cero
se envía como cero voltios y un uno como dos voltios. Por el cable se le suma
ruido. Lo que llega, erre, es la amplitud enviada más el ruido. Esto se llama
modulación por amplitud de pulsos, y es la forma más simple de enviar bits.

<!-- b2 -->
El ruido es gaussiano: una campana centrada en cero, con un desvío de un
voltio. Si se envió un cero, lo que llega es solo ruido: una campana centrada
en cero. Si se envió un uno, llega dos más ruido: la misma campana, desplazada
hasta el dos. Dos campanas iguales, separadas dos voltios, que se solapan.

<!-- b3 -->
Mides uno coma tres voltios. ¿Cero o uno? Ya no podemos contar casos como en la
tabla, porque la medición puede valer cualquier número. Lo que tenemos es la
altura de cada campana en ese punto: su densidad. La campana del cero vale ahí
cero coma diecisiete. La del uno, cero coma treinta y uno.

<!-- b4 -->
Esa altura se llama verosimilitud: lo compatible que es lo que has medido con
cada hipótesis. Uno coma tres queda lejos del centro de una campana y cerca
del centro de la otra. Por eso es casi el doble de compatible con el uno.

<!-- b5 -->
Si ceros y unos fueran igual de frecuentes, con eso bastaría: gana la campana
más alta. Las dos se cruzan justo en uno, a mitad de camino. Por encima de un
voltio dirías uno, y por debajo, cero. Pero no son igual de frecuentes: hay más
ceros. ¿Cómo se mezcla eso con las campanas?

---

# Escena 04 — CurvasEscaladas

**Objetivo:** llegar a la regla del máximo a posteriori con una medición
continua: Bayes con densidades, cancelar el denominador común y comparar las
campanas escaladas por su a priori. Ver que la misma medición cambia de decisión,
que el cruce se mueve a 1,42 y que el eje queda partido en regiones de decisión.

**Qué hace falta saber antes:** escenas 01 y 03.

**Visual:** (idea de `c9-regiones-decision.svg`)
- Bayes construido pieza a pieza: «P(H₁ | r) = p₁ · f(r | H₁) / f(r)», y debajo
  el de H₀ con el mismo denominador. El denominador de los dos se tacha.
- Las dos campanas de la escena 03 se encogen: la del cero al 70 % de su altura,
  la del uno al 30 %.
- En «r = 1,3»: «0,7 · 0,17 = 0,12» y «0,3 · 0,31 = 0,094». Gana la del cero.
  Contraste con la escena 03: «Antes: 1 · Ahora: 0».
- El cruce se desliza de «1» a «1,42». El eje se colorea en dos regiones: «D₀ ·
  Decir 0» y «D₁ · Decir 1».
- La regla, término a término: «p₁ · f(r | H₁) ≷ p₀ · f(r | H₀)».

## Narración

<!-- b1 -->
Se mezcla con la regla de Bayes, igual que antes, pero con alturas en lugar de
probabilidades. La probabilidad a posteriori de hache uno, habiendo medido
erre, es pe uno por la altura de la campana del uno en erre, dividida entre la
densidad total de erre.

<!-- b2 -->
Para hache cero es igual, con el mismo denominador. Y como solo queremos saber
cuál de las dos es mayor, ese denominador sobra: es positivo y está en los dos
lados. Basta comparar pe uno por su campana con pe cero por la suya.

<!-- b3 -->
En el dibujo, cada campana se multiplica por su probabilidad a priori. La del
cero se queda en el setenta por ciento de su altura. La del uno se encoge al
treinta. Y se decide por la curva que quede más alta en el punto medido.

<!-- b4 -->
Hagamos la cuenta en uno coma tres. Cero coma siete por cero coma diecisiete:
cero coma doce. Cero coma tres por cero coma treinta y uno: cero coma cero
noventa y cuatro. Gana el cero. Con la misma medición que hace un momento nos
hacía decir uno.

<!-- b5 -->
El cruce de las curvas ya no está en uno: se ha ido a uno coma cuarenta y dos.
Como los unos son más raros, pedimos más voltios antes de creernos un uno. El
eje queda partido en dos regiones de decisión: a la derecha de uno coma
cuarenta y dos se dice uno, y a la izquierda, cero.

<!-- b6 -->
Esta es la regla del máximo a posteriori para una medición continua. Pe uno
por la densidad de erre bajo hache uno, comparada con pe cero por la densidad
de erre bajo hache cero. Si gana la primera, se dice uno. Si gana la segunda,
cero.

---

# Escena 05 — PorQueEsLaMejor

**Objetivo:** entender por qué esa regla minimiza la probabilidad de error total
y no solo la de cada medición (pesos que nunca son negativos); qué pasa justo en
la frontera; y cómo se extiende a más de dos hipótesis.

**Qué hace falta saber antes:** escenas 02 y 04; capítulo 7, escena 11 (la
integral como suma de rebanadas finas; la densidad nunca es negativa).

**Visual:**
- La tabla del canal con sus dos columnas se convierte en las curvas escaladas
  cortadas en muchas rebanadas verticales: «Una columna por cada r».
- En una rebanada, dos segmentos: el alto (acierto, verde) y el bajo (fallo,
  rojo). Al recorrer el eje, el rojo va rellenando el área bajo la curva más
  baja: «Error = Área roja».
- Otra regla (umbral en 1): aparece un triángulo rojo de más entre 1 y 1,42.
- Zoom al cruce en 1,42: las dos alturas iguales, «Empate», y una rebanada de
  ancho cero: «Probabilidad 0».
- Tres campanas en «0 V», «2 V» y «4 V»; umbrales en «1» y «3»; tres regiones.

## Narración

<!-- b1 -->
¿Es la mejor regla posible, o solo una regla razonable? El argumento es el de
las columnas de la tabla, solo que ahora hay infinitas columnas: una por cada
valor de erre. En cada una, si dices uno fallas con la probabilidad a
posteriori del cero, y si dices cero, con la del uno. Quedarte con la mayor es
fallar lo menos posible ahí.

<!-- b2 -->
La probabilidad de error total es el promedio de esos fallos sobre todos los
valores de erre, cada uno pesado por lo a menudo que aparece. Ese peso es una
densidad, y una densidad nunca es negativa. El promedio es una integral: la
suma de rebanadas muy finas que vimos en el capítulo siete.

<!-- b3 -->
Cualquier otra regla, en cada rebanada, falla lo mismo o más. Y sumar cosas
iguales o mayores, con pesos que nunca son negativos, da un total igual o
mayor. Ninguna regla puede ganarle. En el dibujo, el error es el área bajo la
curva escalada que pierde. Si mueves el umbral a otro sitio, aparece un trozo
de área de más.

<!-- b4 -->
¿Y justo en el cruce, en uno coma cuarenta y dos? Ahí hay empate: decir cero o
uno falla lo mismo. Además, la probabilidad de medir exactamente ese valor es
cero. Así que en la frontera puedes decidir lo que quieras, y la regla sigue
siendo la mejor.

<!-- b5 -->
Con más de dos hipótesis no cambia nada. Si se pudieran enviar cero, dos o
cuatro voltios, habría tres campanas, cada una escalada por su probabilidad a
priori, y ganaría la más alta. Si las tres son igual de probables, los umbrales
caen en uno y en tres.

<!-- b6 -->
Ya tenemos la regla y sabemos que es la mejor. Lo que todavía no sabemos es
cuánto se equivoca, ni de qué manera. Porque hay más de una forma de fallar.

---

# Escena 06 — FalsaAlarmaYFallo

**Objetivo:** distinguir los dos errores (falsa alarma y fallo), definir sus
probabilidades como condicionales a la hipótesis verdadera, definir la
detección y deducir la probabilidad de error total como media ponderada.
Comprobarlo con el canal.

**Qué hace falta saber antes:** escenas 01 y 02; capítulo 7, escenas 05 y 08
(probabilidad condicional y ley de probabilidad total).

**Visual:**
- Un radar con su pantalla. Dos casillas: «H₀ · Solo ruido» y «H₁ · Hay avión».
- Tabla 2 × 2 (`TablaDecision`): filas «Realidad», columnas «Decisión». Dos
  casillas con tilde verde; dos con cruz roja: «Falsa alarma» y «Fallo · Miss».
- La fila de «Solo ruido» se resalta y se parte en dos trozos: el trozo rojo es
  «P_FA». La fila de «Hay avión» igual: trozo rojo «P_M», trozo verde «P_D».
  «P_D = 1 − P_M».
- La fórmula, término a término: «P_e = p₀ · P_FA + p₁ · P_M», sobre un árbol de
  dos ramas.
- Comprobación con el canal: «0,7 · 0,1 + 0,3 · 0,1 = 0,10» y, para «Siempre
  0», «0,7 · 0 + 0,3 · 1 = 0,30».

## Narración

<!-- b1 -->
Un radar mira al cielo. La hipótesis cero dice: solo hay ruido. La hipótesis
uno dice: hay un avión. El radar mide y decide. Hay cuatro casos posibles. En
dos, acierta. En los otros dos se equivoca, pero no de la misma manera.

<!-- b2 -->
Si dice que hay un avión y no lo había, es una falsa alarma. Si dice que no hay
nada y sí lo había, es un fallo, que en inglés se llama miss. Los nombres
vienen del radar, pero valen para todo. En el canal de bits, una falsa alarma
es decir uno cuando se envió un cero.

<!-- b3 -->
Cada error tiene su probabilidad, y cuidado con cómo se definen. La
probabilidad de falsa alarma es, de todas las veces que no había avión, la
fracción en que el radar dice que sí. Está condicionada a hache cero. La
probabilidad de fallo es, de las veces que sí había avión, la fracción que se
le escapa. Está condicionada a hache uno.

<!-- b4 -->
Hay una tercera, que es la que se suele anunciar: la probabilidad de detección.
De las veces que había avión, la fracción que el radar ve. Es uno menos la
probabilidad de fallo, porque un avión o se ve o se escapa.

<!-- b5 -->
¿Y la probabilidad de equivocarse, en total? Hay dos caminos para fallar. No
había avión, con probabilidad pe cero, y hubo falsa alarma. O había avión, con
probabilidad pe uno, y hubo fallo. La probabilidad de error es pe cero por la
de falsa alarma, más pe uno por la de fallo.

<!-- b6 -->
Comprobémoslo con el canal. Creyendo lo recibido, la falsa alarma vale cero
coma uno y el fallo también. Cero coma siete por cero coma uno, más cero coma
tres por cero coma uno: un diez por ciento. Y diciendo siempre cero no hay
falsas alarmas, pero se fallan todos los unos: un treinta por ciento. Lo mismo
que antes.

---

# Escena 07 — ElAreaDeLaCola

**Objetivo:** calcular las dos probabilidades de error con las campanas: son
áreas de colas. Estandarizar, definir la función Q y obtener 0,159 para el
umbral en 1. Ver que lo que cuenta es la separación medida en desvíos.

**Qué hace falta saber antes:** escenas 03 y 06; capítulo 7, escena 11
(probabilidad = área bajo la densidad).

**Visual:**
- Las dos campanas con el umbral en «1». Se sombrea en rojo la cola derecha de
  la campana del cero («Falsa alarma») y la cola izquierda de la del uno
  («Fallo»).
- Una campana cualquiera se desplaza y se encoge hasta la estándar: «Restar el
  centro, dividir entre el desvío».
- Campana estándar con la cola desde «x» sombreada: «Q(x)». Tabla corta: «Q(0) =
  0,5», «Q(1) = 0,16», «Q(2) = 0,023», «Q(3) = 0,0013».
- Cuentas: «(1 − 0) / 1 = 1 → Q(1) = 0,159» y «(2 − 1) / 1 = 1 → Q(1) = 0,159»;
  la cola izquierda se refleja para verse como cola derecha.
- «P_e = 0,159»: cien bits en fila, dieciséis en rojo.
- Las campanas se separan a 6 desvíos: las colas casi desaparecen, «Q(3) = 0,0013».

## Narración

<!-- b1 -->
Volvamos a las campanas, con el umbral en un voltio. Hay falsa alarma cuando se
envió un cero y el ruido empujó la medición por encima del umbral. Su
probabilidad es el área de la campana del cero a la derecha del umbral. Y el
fallo es el área de la campana del uno a la izquierda. Los dos errores son
áreas de colas.

<!-- b2 -->
Para calcularlas hay una herramienta. Cualquier campana se convierte en la
campana estándar, de centro cero y desvío uno, restando su centro y dividiendo
entre su desvío. Es medir las distancias en desvíos. El área de la cola de la
campana estándar, desde un punto equis en adelante, se llama función cu de
equis.

<!-- b3 -->
No tiene una fórmula sencilla: se mira en una tabla o se le pide al ordenador.
Algunos valores para orientarse. Cu de cero es un medio: media campana. Cu de
uno, cero coma dieciséis. Cu de dos, cero coma cero veintitrés. Cu de tres,
poco más de una milésima. La cola cae muy deprisa.

<!-- b4 -->
La falsa alarma: el umbral está en uno y la campana del cero tiene centro cero
y desvío uno. El umbral queda a un desvío del centro. Cu de uno: cero coma
ciento cincuenta y nueve. El fallo es una cola izquierda, pero la campana es
simétrica: del dos al uno hay también un desvío. Otra vez cero coma ciento
cincuenta y nueve.

<!-- b5 -->
Con ceros y unos igual de frecuentes, la probabilidad de error es esa misma:
dieciséis bits mal de cada cien. Es mucho, porque las campanas están a solo dos
desvíos una de otra. Lo que cuenta es esa separación medida en desvíos. Con
seis desvíos entre ellas, el umbral quedaría a tres, y fallaría poco más de un
bit de cada mil.

---

# Escena 08 — MoverElUmbral

**Objetivo:** hacer la cuenta completa con el umbral del máximo a posteriori
(1,42): la falsa alarma baja, el fallo sube y el error total es 0,139, menor que
con el umbral en 1 y que diciendo siempre cero. Ver que mover el umbral cambia
un error por otro.

**Qué hace falta saber antes:** escenas 04, 06 y 07.

**Visual:**
- Las dos campanas; el umbral se desliza de «1» a «1,42». La cola roja de la
  derecha encoge y la de la izquierda crece, a la vez.
- Dos cuentas: «Q(1,42) = 0,077» y «(2 − 1,42) / 1 = 0,58 → Q(0,58) = 0,28».
- La media ponderada: «0,7 · 0,077 + 0,3 · 0,28 = 0,054 + 0,085 = 0,139».
- Tres barras de error: «Siempre 0 · 0,30», «Umbral en 1 · 0,159», «Umbral en
  1,42 · 0,139». La última, en verde.
- El umbral va y viene: una cola sube cuando la otra baja. Después las campanas
  se separan y las dos colas bajan juntas: «Más señal o menos ruido».

## Narración

<!-- b1 -->
Ahora con los ceros más frecuentes: setenta y treinta. La regla del máximo a
posteriori ponía el umbral en uno coma cuarenta y dos. La falsa alarma es la
cola a partir de ahí: cu de uno coma cuarenta y dos, cero coma cero setenta y
siete. Ha bajado a la mitad.

<!-- b2 -->
El fallo: del centro de la campana del uno, que está en dos, al umbral hay cero
coma cincuenta y ocho desvíos. Cu de cero coma cincuenta y ocho: cero coma
veintiocho. Casi se ha duplicado.

<!-- b3 -->
La probabilidad de error es la media ponderada. Cero coma siete por cero coma
cero setenta y siete, más cero coma tres por cero coma veintiocho. Cero coma
cero cincuenta y cuatro, más cero coma cero ochenta y cinco: cero coma ciento
treinta y nueve.

<!-- b4 -->
Comparemos. Con el umbral en uno, las dos colas valen cero coma ciento
cincuenta y nueve, y el error también. Diciendo siempre cero, el error es cero
coma treinta. Con el umbral en uno coma cuarenta y dos, cero coma ciento
treinta y nueve. Es el menor, como tenía que ser.

<!-- b5 -->
Fíjate en lo que ha pasado al mover el umbral: una cola encoge y la otra crece.
No hay manera de bajar las dos a la vez moviendo el umbral. Para eso hay que
separar las campanas: más amplitud o menos ruido. El umbral solo reparte el
error, y el máximo a posteriori lo carga sobre los unos porque son menos.

<!-- b6 -->
Minimizar el total parece lo sensato. Pero ¿es siempre lo que queremos? Hay un
ejemplo que ya conoces donde el total engaña.

---

# Escena 09 — ElTestMedicoVuelve

**Objetivo:** traducir el vocabulario al test médico del capítulo 7
(sensibilidad, especificidad, prevalencia, valor predictivo positivo),
distinguir la detección del valor predictivo, y descubrir que por probabilidad
de error «lo mejor» sería no hacer el test. Dejar esa pregunta abierta.

**Qué hace falta saber antes:** escena 06; capítulo 7, escena 07 (el test
contado sobre mil personas). Se recuerda aquí con el mismo dibujo.

**Visual:**
- Las tres tarjetas del capítulo 7: «1 de cada 100», «Enfermo → positivo 99 %»,
  «Sano → positivo 5 %». Casillas «H₀ · Sano» y «H₁ · Enfermo».
- Un diccionario de dos columnas que se llena renglón a renglón: «Detección =
  Sensibilidad · 99 %», «Falsa alarma = Falso positivo · 5 %», «1 − Falsa
  alarma = Especificidad · 95 %», «Fallo = Falso negativo · 1 %», «p₁ =
  Prevalencia · 1 %».
- La grilla de mil personas del capítulo 7: 10 rojas, ~50 sanas con «+»; el
  recuadro de los 60 positivos: «10 / 60 ≈ 17 %». Rótulo «Valor predictivo positivo».
- La tabla 2 × 2: una flecha que la recorre por filas («Sensibilidad») y otra
  por columnas («Valor predictivo»).
- «P_e = 0,99 · 0,05 + 0,01 · 0,01 ≈ 5 %» frente a «Siempre sano → 1 %», con un
  «?» grande y la etiqueta «Dentro de tres episodios».

## Narración

<!-- b1 -->
Vuelve el test médico del capítulo siete. Una enfermedad la tiene una persona
de cada cien. Si estás enfermo, el test da positivo el noventa y nueve por
ciento de las veces. Si estás sano, da positivo un cinco por ciento. Es un
problema de hipótesis: hache cero, sano; hache uno, enfermo. Y la decisión es
lo que dice el test.

<!-- b2 -->
Los médicos usan otros nombres para lo mismo. La probabilidad de detección,
noventa y nueve por ciento, es la sensibilidad. La de falsa alarma, cinco por
ciento, es la de falso positivo, y lo que falta hasta cien, noventa y cinco, es
la especificidad. El fallo es el falso negativo. Y la probabilidad a priori de
estar enfermo, uno por ciento, es la prevalencia.

<!-- b3 -->
Pero al paciente no le interesa ninguna de esas. Le interesa esto: he dado
positivo, ¿estoy enfermo? Es el valor predictivo positivo. Ya hicimos la
cuenta. De mil personas, diez enfermas dan positivo, y de las novecientas
noventa sanas, unas cincuenta también. Diez de sesenta: un diecisiete por
ciento.

<!-- b4 -->
Aquí está la trampa. La sensibilidad recorre la tabla por filas: de los
enfermos, cuántos dan positivo. El valor predictivo la recorre por columnas: de
los positivos, cuántos están enfermos. Son preguntas distintas, y para pasar de
una a otra hace falta la prevalencia.

<!-- b5 -->
Y ahora una sorpresa. La probabilidad de error de este test: cero coma noventa
y nueve por cero coma cero cinco, más cero coma cero uno por cero coma cero
uno. Casi un cinco por ciento. Un test que dijera siempre sano, sin mirar a
nadie, solo fallaría con los enfermos: un uno por ciento.

<!-- b6 -->
Según la probabilidad de error, lo mejor sería no hacer el test. Es absurdo, y
la razón es que hemos tratado los dos errores como si costaran lo mismo. Lo
arreglaremos dentro de tres episodios. Guárdate la pregunta.

---

# Escena 10 — LaPrevalenciaManda

**Objetivo:** ver cómo cambia el valor predictivo con la prevalencia (de 2 % a
95 % con el mismo test), entender por qué, y ver que repetir el test encadena
Bayes: la probabilidad a posteriori pasa a ser la nueva a priori.

**Qué hace falta saber antes:** escena 09.

**Visual:** (idea de `c9p-ppv-prevalencia.svg`)
- Cuenta sobre cien mil personas: «100 enfermas → 99 positivos», «99.900 sanas
  → 4.995 positivos», «99 / 5.094 ≈ 2 %».
- Una curva que se dibuja: valor predictivo contra prevalencia, con cuatro
  puntos marcados: «0,1 % → 2 %», «1 % → 17 %», «10 % → 69 %», «50 % → 95 %».
- Dos montones: uno enorme de sanos del que sale una tira fina de positivos, y
  uno minúsculo de enfermos del que salen casi todos. La tira fina es más larga.
- Una cadena: «1 % → Test + → 17 % → Test + → 80 % → Test + → 99 %». Cuenta del
  segundo paso: «167 enfermas → 165 positivos», «833 sanas → 42 positivos»,
  «165 / 207 ≈ 80 %».
- Dos tarjetas: «El detector: Falsa alarma y Detección» y «Cuánto creerle:
  además, lo frecuente que es».

## Narración

<!-- b1 -->
Cambiemos solo la prevalencia, con el mismo test. Si la enfermedad la tiene una
persona de cada mil: de cien mil personas, cien están enfermas y dan noventa y
nueve positivos. Las otras noventa y nueve mil novecientas están sanas y dan
casi cinco mil positivos. Noventa y nueve de unos cinco mil cien: un dos por
ciento.

<!-- b2 -->
Con una de cada cien, un diecisiete por ciento. Con una de cada diez, un
sesenta y nueve. Con la mitad de la población enferma, un noventa y cinco. El
mismo test, con la misma sensibilidad y la misma especificidad, da respuestas
que van del dos al noventa y cinco por ciento.

<!-- b3 -->
La razón es de dónde sale cada positivo. Los falsos salen de un montón enorme
de sanos, y los verdaderos, de un montón minúsculo de enfermos. Un porcentaje
pequeño de muchísimos puede ser más que un porcentaje grande de muy pocos.

<!-- b4 -->
¿Entonces el test no sirve? Sí sirve: has pasado del uno al diecisiete por
ciento. Y ese diecisiete es tu nueva probabilidad a priori. Repite el test, y
supón que sus errores no dependen de la primera vez. De mil personas como tú,
ciento sesenta y siete están enfermas y dan ciento sesenta y cinco positivos.
Las otras ochocientas treinta y tres dan cuarenta y dos.

<!-- b5 -->
Ciento sesenta y cinco de doscientos siete: un ochenta por ciento. Con un
tercer positivo, un noventa y nueve. Por eso un positivo se confirma con otra
prueba, y por eso no se hacen pruebas masivas de enfermedades muy raras.

<!-- b6 -->
La lección vale igual para un radar o un receptor. La falsa alarma y la
detección describen al detector. Pero cuánto creerle cuando dice que sí depende
también de lo frecuente que sea lo que busca.

---

# Escena 11 — RazonDeVerosimilitud

**Objetivo:** reordenar la regla del máximo a posteriori para dejar los datos a
un lado y lo que se sabía antes al otro: la razón de verosimilitud contra un
umbral. Comprobarlo con la medición de 1,3 y leer qué significa.

**Qué hace falta saber antes:** escena 04; que dividir una desigualdad entre un
número positivo no le da la vuelta (se dice aquí).

**Visual:**
- La regla de la escena 04: «p₁ · f(r | H₁) ≷ p₀ · f(r | H₀)». Las piezas se
  mueven: «f(r | H₀)» baja al denominador de la izquierda y «p₁» al de la
  derecha. Recordatorio: «Dividir entre algo positivo: la desigualdad no gira».
- Queda: «Λ(r) = f(r | H₁) / f(r | H₀) ≷ p₀ / p₁ = η». Llave a la izquierda:
  «Lo que has medido». Llave a la derecha: «Lo que sabías antes».
- Las dos campanas con la regla vertical en 1,3: «0,31 / 0,17 = 1,82».
- Dos comparaciones: «1,82 > 1 → Decir 1» (a priori iguales) y «1,82 < 2,33 →
  Decir 0» (0,7 y 0,3).
- Una balanza: en un platillo la evidencia (Λ), en el otro la ventaja de partida (η).
- Rótulo: «Test de razón de verosimilitud».

## Narración

<!-- b1 -->
En la regla del máximo a posteriori, cada lado mezcla dos cosas: lo que has
medido y lo que sabías antes. Vamos a separarlas. Para decir uno, pe uno por la
campana del uno tiene que superar a pe cero por la campana del cero. Dividimos
los dos lados entre la campana del cero y entre pe uno. Son números positivos,
así que la desigualdad no se da la vuelta.

<!-- b2 -->
A la izquierda queda la altura de la campana del uno dividida entre la altura
de la campana del cero, en el punto medido. Es la razón de verosimilitud, y se
escribe lambda mayúscula de erre. Dice cuántas veces más compatible es el dato
con hache uno que con hache cero.

<!-- b3 -->
A la derecha queda un número fijo, que no depende de la medición: pe cero
entre pe uno. Es el umbral, y se llama eta. Todo lo que has medido está a un
lado. Todo lo que sabías antes, al otro.

<!-- b4 -->
Comprobémoslo con uno coma tres voltios. La razón es cero coma treinta y uno
entre cero coma diecisiete: uno coma ochenta y dos. Con ceros y unos igual de
frecuentes, eta vale uno: se dice uno. Con setenta y treinta, eta vale dos coma
treinta y tres: uno coma ochenta y dos no llega, y se dice cero. Lo mismo que
con las curvas escaladas.

<!-- b5 -->
Y ahora se lee muy bien. Si los ceros son dos coma tres veces más frecuentes,
para decir uno el dato tiene que ser al menos dos coma tres veces más
compatible con el uno. La evidencia tiene que compensar la ventaja de partida.
Esto es el test de razón de verosimilitud, y va a aparecer en todo lo que
queda de capítulo.

---

# Escena 12 — LaCuentaConCampanas

**Objetivo:** calcular la razón de verosimilitud de las dos campanas paso a paso
(queda e elevado a 2r − 2), ver que crece con r, tomar logaritmos y obtener el
umbral sobre la medición: 1 + ln(η)/2. Comprobar que da 1 y 1,42.

**Qué hace falta saber antes:** escena 11. De matemáticas se explica aquí: la
fórmula de la campana, dividir potencias del mismo número, desarrollar un
cuadrado y el logaritmo natural.

**Visual:**
- La fórmula de la campana, pieza a pieza: «Constante · e^(−(r − Centro)² / 2σ²)»;
  con «σ = 1» se simplifica.
- El cociente: las constantes se tachan. Recordatorio: «eᵃ / eᵇ = eᵃ⁻ᵇ».
- Renglones: «−(r − 2)²/2 + r²/2», después «(r − 2)² = r² − 4r + 4», los «r²»
  se tachan en rojo, queda «(4r − 4)/2 = 2r − 2».
- Resultado enmarcado: «Λ(r) = e^(2r − 2)». Su gráfica, siempre creciente, con
  tres puntos: «r = 0 → 0,135», «r = 1 → 1», «r = 2 → 7,39».
- Una línea horizontal «η» que corta la curva; la vertical baja al eje:
  «Umbral». Recordatorio: «ln(eˣ) = x».
- «2r − 2 ≷ ln η → r ≷ 1 + ln(η)/2»; «η = 1 → 1» y «η = 2,33 → 1 + 0,85/2 = 1,42».

## Narración

<!-- b1 -->
Calculemos esa razón para nuestras campanas. La campana de Gauss tiene fórmula:
una constante, por e elevado a menos la distancia al centro al cuadrado,
dividida entre dos sigma cuadrado. Aquí sigma vale uno, así que el exponente es
menos la distancia al cuadrado, entre dos.

<!-- b2 -->
Dividimos la campana del uno entre la del cero. Las constantes son iguales y se
cancelan. Y dividir potencias del mismo número es restar los exponentes. Queda
e elevado a: menos erre menos dos al cuadrado entre dos, más erre al cuadrado
entre dos.

<!-- b3 -->
Desarrollamos el cuadrado. Erre menos dos, al cuadrado, es erre al cuadrado,
menos cuatro erre, más cuatro. Los dos erre al cuadrado se cancelan. Queda
cuatro erre menos cuatro, entre dos: dos erre menos dos. La razón de
verosimilitud es e elevado a dos erre menos dos.

<!-- b4 -->
Probemos valores. En cero voltios vale cero coma ciento treinta y cinco: el
dato apoya al cero. En un voltio vale uno: empate. En dos voltios, siete coma
cuatro: apoya al uno. La razón crece siempre con erre. Por eso compararla con
eta es lo mismo que comparar erre con un umbral.

<!-- b5 -->
Para hallarlo se toma el logaritmo natural, que es la operación inversa de la
exponencial y conserva el orden. Queda dos erre menos dos, comparado con el
logaritmo de eta. Despejando: erre comparado con uno más la mitad del logaritmo
de eta.

<!-- b6 -->
Con eta igual a uno, el logaritmo es cero y el umbral es un voltio. Con eta
igual a dos coma treinta y tres, el logaritmo es cero coma ochenta y cinco, y
el umbral, uno coma cuarenta y dos. Los mismos cruces de antes. Una razón que
siempre crece da un solo umbral. Pero no siempre crece.

---

# Escena 13 — DosUmbrales

**Objetivo:** ver que, si las dos campanas tienen anchuras distintas, la región
de decisión tiene dos pedazos: la campana más ancha gana en las dos colas. Hacer
la cuenta (una ecuación de segundo grado) y entender por qué.

**Qué hace falta saber antes:** escena 12. De matemáticas se explica aquí: una
parábola que abre hacia arriba es positiva fuera de sus dos raíces.

**Visual:** (idea de `c9p-map-varianzas-distintas.svg`)
- Una campana estrecha y alta centrada en 0 («Cero · Desvío 1») y otra ancha y
  baja centrada en 2 («Uno · Desvío 2»).
- Pregunta con pausa: una marca en «r = −4» y «¿Cero o uno?». Encuesta: «Cero,
  está más cerca» · «Uno».
- Zoom a la cola izquierda: la estrecha vale «0,0001», la ancha «0,002»: «17
  veces más».
- La cuenta: «ln Λ = ln ½ − (r − 2)²/8 + r²/2»; los «r²» no se tachan: «½ − ⅛».
  Multiplicado por 8: «3r² + 4r − 9,55 ≥ 0».
- Una parábola que abre hacia arriba; sus raíces «−2,57» y «1,24»; positiva fuera.
- El eje con tres regiones: «Uno · Cero · Uno».
- «Dos umbrales: 0,227» y «Solo el derecho: 0,230».

## Narración

<!-- b1 -->
Un cambio pequeño. Supón que el uno llega con más ruido que el cero: pasa en
la fibra óptica, donde la luz encendida es más ruidosa que la apagada. La
campana del cero tiene centro cero y desvío uno. La del uno, centro dos y
desvío dos. Ceros y unos, igual de frecuentes. Mides menos cuatro voltios.
¿Cero o uno? Piénsalo un momento.

<!-- b2 -->
Menos cuatro está más cerca de cero que de dos. Pero la respuesta es uno. A
cuatro desvíos de su centro, la campana estrecha prácticamente ha desaparecido:
vale una diezmilésima. La ancha está a solo tres de sus desvíos, y vale
diecisiete veces más.

<!-- b3 -->
Hagamos la cuenta con el logaritmo de la razón. Ahora las constantes no se
cancelan, porque la campana ancha es la mitad de alta: aparece el logaritmo de
un medio. Y los erre al cuadrado tampoco: uno va dividido entre dos y el otro
entre ocho.

<!-- b4 -->
Multiplicando todo por ocho y ordenando, se dice uno cuando tres erre al
cuadrado, más cuatro erre, menos nueve coma cincuenta y cinco, es positivo. Eso
es una parábola que abre hacia arriba: es positiva fuera de sus dos raíces. La
fórmula de la ecuación de segundo grado las da: menos dos coma cincuenta y
siete, y uno coma veinticuatro.

<!-- b5 -->
La región del uno tiene dos pedazos: las dos colas. La del cero es el intervalo
del medio. La regla general: lejos del centro, por los dos lados, gana siempre
la campana más ancha. Solo cuando las dos anchuras son iguales desaparece el
término al cuadrado y queda un único umbral.

<!-- b6 -->
Siendo honestos: aquí la cola izquierda casi nunca ocurre. El error baja de
cero coma doscientos treinta a cero coma doscientos veintisiete. Pero la
lección importa: el umbral no se pone a ojo. Se calcula la razón de
verosimilitud y se mira dónde supera a eta.

---

# Escena 14 — SinProbabilidadesAPriori

**Objetivo:** plantear el caso en que no se conocen las probabilidades a priori
(radar) y el criterio de Neyman-Pearson: fijar la falsa alarma y maximizar la
detección. Hacer el diseño con las campanas para 5 % (umbral 1,645, detección
0,64) y compararlo con otros umbrales.

**Qué hace falta saber antes:** escenas 06 y 07 (falsa alarma, detección, la
función Q).

**Visual:**
- El radar y la pregunta: «p₁ = ?». La fórmula «η = p₀ / p₁» se queda sin
  numerador ni denominador.
- Un cambio de pregunta, en dos tarjetas: «Fijar: Falsa alarma ≤ 5 %» y
  «Conseguir: La mayor detección».
- La campana del ruido (centro 0) con la cola del 5 % sombreada. La función Q al
  revés: «Q(x) = 0,05 → x = 1,645». Umbral en «1,645».
- La campana del eco (centro 2): el área a la derecha de 1,645 en verde,
  «Detección = 0,64».
- Tabla de tres renglones: «Umbral 1 · 16 % · 84 %», «Umbral 1,645 · 5 % ·
  64 %», «Umbral 2,33 · 1 % · 37 %».
- Una región rara, en varios trozos sueltos sobre el eje, con un «?»: «¿Y con
  otra región?».

## Narración

<!-- b1 -->
Todo lo anterior necesitaba las probabilidades a priori. En el canal las
conocemos. Pero vuelve al radar: ¿qué probabilidad hay de que ahora mismo haya
un avión delante? Nadie lo sabe. Y sin probabilidades a priori, no hay eta.

<!-- b2 -->
Neyman y Pearson propusieron cambiar la pregunta. En vez de minimizar el error
total, se fija cuántas falsas alarmas se toleran, por ejemplo un cinco por
ciento. Y con esa condición, se busca detectar lo máximo posible.

<!-- b3 -->
Hagámoslo con las campanas: el ruido solo, con centro en cero, y el eco, con
centro en dos. Buscamos el umbral que deja un cinco por ciento de cola en la
campana del ruido. Es la función cu al revés: dada un área, qué punto la deja.
Para un cinco por ciento, ese punto es uno coma seiscientos cuarenta y cinco.

<!-- b4 -->
Ahora la detección: el área de la campana del eco a la derecha de ese umbral.
El umbral queda un poco a la izquierda de su centro, así que es algo más de la
mitad: cero coma sesenta y cuatro. Vemos dos de cada tres aviones, con un cinco
por ciento de falsas alarmas.

<!-- b5 -->
Comparemos con otros umbrales. En un voltio: dieciséis por ciento de falsas
alarmas y ochenta y cuatro de detección. Para tolerar solo un uno por ciento,
el umbral sube a dos coma treinta y tres voltios, y la detección cae al treinta y
siete. Ninguno es mejor en abstracto: menos falsas alarmas se pagan con menos
aviones vistos.

<!-- b6 -->
Pero hemos dado algo por supuesto: que la región donde se dice avión es todo lo
que queda a la derecha de un umbral. ¿Y si existiera otra región, más rara, con
el mismo cinco por ciento de falsas alarmas y más detección?

---

# Escena 15 — ElPresupuesto

**Objetivo:** demostrar el lema de Neyman-Pearson con una tabla de cinco niveles:
la falsa alarma es un presupuesto, la detección es lo que se compra, y lo que
más rinde por lo que cuesta es justo la razón de verosimilitud. Concluir que los
dos criterios son el mismo test con distinto umbral.

**Qué hace falta saber antes:** escenas 11 y 14.

**Visual:** (idea de `c9p-neyman-pearson-lema.svg`)
- Cinco casillas, «Nivel 1» a «Nivel 5». Fila «Sin avión»: «0,40 · 0,30 · 0,15
  · 0,10 · 0,05». Fila «Con avión»: «0,05 · 0,10 · 0,15 · 0,30 · 0,40».
- Un monedero: «Presupuesto: Falsa alarma ≤ 0,15». Cada casilla muestra «Cuesta»
  (fila de arriba) y «Rinde» (fila de abajo).
- Tercera fila, «Rinde / Cuesta»: «0,125 · 0,33 · 1 · 3 · 8». Rótulo: «= Λ».
- Una mochila: entran el nivel 5 y el nivel 4. «Coste 0,05 + 0,10 = 0,15»,
  «Detección 0,40 + 0,30 = 0,70». Alternativa: solo el nivel 3, «Coste 0,15 ·
  Detección 0,15», tachada.
- Las dos campanas: la gráfica creciente de Λ y la región «r ≥ 1,645».
- Dos tarjetas que apuntan a la misma caja «Λ(r) ≷ η»: «Máximo a posteriori: η
  = p₀/p₁» y «Neyman-Pearson: η por presupuesto».

## Narración

<!-- b1 -->
Veámoslo con un caso de juguete. Un detector entrega un nivel, de uno a cinco.
Sin avión, los niveles salen con probabilidades cero coma cuarenta, cero coma
treinta, cero coma quince, cero coma diez y cero coma cero cinco. Con avión, al
revés. Hay que elegir en qué niveles se dice avión, con un quince por ciento de
falsas alarmas como mucho.

<!-- b2 -->
Piénsalo como un presupuesto. Cada nivel que metes en la región de decir avión
cuesta su probabilidad sin avión, porque eso es falsa alarma. Y rinde su
probabilidad con avión, porque eso es detección. El nivel cinco cuesta cero
coma cero cinco y rinde cero coma cuarenta. El nivel tres cuesta cero coma
quince y rinde cero coma quince.

<!-- b3 -->
Es como llenar una mochila: primero, lo que más rinde por lo que cuesta. Para
el nivel cinco, ese cociente es ocho. Para el cuatro, tres. Para el tres, uno.
Para los otros dos, menos de uno. Y ese cociente, lo que rinde con avión entre
lo que cuesta sin avión, es exactamente la razón de verosimilitud.

<!-- b4 -->
Compramos el nivel cinco y el nivel cuatro. Cuestan cero coma quince, justo el
presupuesto, y la detección es cero coma setenta. Con el mismo gasto podrías
haber comprado solo el nivel tres, y detectarías cero coma quince. Cualquier
cambio saca algo que rendía mucho para meter algo que rinde menos.

<!-- b5 -->
Este es el lema de Neyman-Pearson. Para un presupuesto de falsas alarmas, la
mejor región es siempre la de razón de verosimilitud mayor que un umbral, con
eta elegido para gastar justo el presupuesto. Con mediciones continuas el
argumento es el mismo, con rebanadas finas en vez de casillas.

<!-- b6 -->
En las campanas la razón crece con erre, así que esa región es todo lo que
queda a la derecha de un umbral. No había una región mejor. Y fíjate: dos
criterios distintos, el mismo test. Un número, la razón de verosimilitud, y un
umbral. Solo cambia de dónde sale el umbral.

---

# Escena 16 — CurvaRoc

**Objetivo:** construir la curva ROC punto a punto con las campanas: cada umbral
es un punto (falsa alarma, detección). Ubicar los dos extremos y ver que la
curva no depende de las probabilidades a priori.

**Qué hace falta saber antes:** escenas 07, 08 y 14.

**Visual:** (idea de `c9-roc.svg`)
- A la izquierda, las dos campanas con un umbral móvil; a la derecha, un plano
  vacío con ejes «Falsa alarma» (horizontal) y «Detección» (vertical), de 0 a 1.
- Cuatro posiciones del umbral, cada una deja un punto: «Umbral 3 → (0,001;
  0,16)», «Umbral 2 → (0,023; 0,5)», «Umbral 1 → (0,16; 0,84)», «Umbral 0 →
  (0,5; 0,977)». Las colas se sombrean en cada paso.
- Los extremos: umbral fuera por la derecha → punto en «(0, 0) · Nunca decir
  1»; fuera por la izquierda → «(1, 1) · Siempre decir 1».
- El umbral barre de derecha a izquierda de forma continua y el punto traza la
  curva entera. Rótulo: «Curva ROC».
- Las etiquetas «p₀» y «p₁» aparecen y se tachan: «No intervienen».

## Narración

<!-- b1 -->
Un detector no es un único par de números. Es una familia entera: un par por
cada umbral. Vamos a dibujarla. En un plano, ponemos en horizontal la
probabilidad de falsa alarma y en vertical la de detección. Cada umbral es un
punto.

<!-- b2 -->
Empezamos con el umbral en tres voltios. La falsa alarma es cu de tres: una
milésima. La detección: del tres al dos hay un desvío, así que cu de uno, cero
coma dieciséis. Un punto pegado al eje vertical, muy abajo. Casi no hay falsas
alarmas, pero se escapan casi todos los aviones.

<!-- b3 -->
Bajamos el umbral a dos. Falsa alarma, cero coma cero veintitrés. Detección,
justo media campana: cero coma cinco. Con el umbral en uno: cero coma dieciséis
y cero coma ochenta y cuatro. Y con el umbral en cero: cero coma cinco y cero
coma noventa y ocho.

<!-- b4 -->
Los extremos son fáciles. Con un umbral altísimo nunca se dice uno: ni falsas
alarmas ni detección. Es la esquina de abajo a la izquierda. Con un umbral
bajísimo siempre se dice uno: todo son detecciones y todo son falsas alarmas.
Es la esquina de arriba a la derecha.

<!-- b5 -->
Al deslizar el umbral, el punto viaja de una esquina a la otra y dibuja una
curva. Se llama curva ROC, característica operativa del receptor: el nombre se
lo pusieron los operadores de radar. Resume todo lo que el detector puede
hacer. Elegir un umbral es elegir un punto de la curva.

<!-- b6 -->
Y fíjate en lo que no aparece: las probabilidades a priori. La curva es del
detector, no de lo frecuente que sea lo que busca. Las probabilidades a priori
servirán para elegir el punto, pero no cambian la curva.

---

# Escena 17 — LeerLaCurva

**Objetivo:** aprender a leer el plano: la esquina ideal, la diagonal como
decidir al azar, la familia de curvas según la separación entre campanas, qué
significa una curva por debajo de la diagonal y cómo se comparan dos detectores.

**Qué hace falta saber antes:** escena 16.

**Visual:**
- El plano con la curva. La esquina superior izquierda se ilumina: «Ideal ·
  Detección 1 · Falsa alarma 0».
- Una moneda cargada que dice «1» con probabilidad «q»; al mover q, un punto
  recorre la diagonal: «Falsa alarma = Detección = q». Rótulo «Decidir al azar».
- Las dos campanas se separan: «1 desvío», «2 desvíos», «3 desvíos»; en el
  plano, tres curvas cada vez más cerca de la esquina. Una vertical en «5 %»
  las corta en «0,26», «0,64» y «0,91».
- Una curva por debajo de la diagonal; se invierten las decisiones y la curva
  se refleja hacia arriba.
- Dos curvas, una siempre por encima de la otra («Mejor siempre»); después dos
  que se cruzan («Depende de la zona»).

## Narración

<!-- b1 -->
¿Cómo se lee esta curva? Primero, la esquina de arriba a la izquierda. Ahí la
detección vale uno y la falsa alarma, cero: el detector perfecto. Cuanto más se
acerque la curva a esa esquina, mejor.

<!-- b2 -->
Segundo, la diagonal. Imagina un detector que no mira nada: tira una moneda
cargada que dice uno con cierta probabilidad. Dirá uno esa fracción de las
veces, haya avión o no. Su falsa alarma y su detección son iguales. Eso es la
diagonal: decidir al azar.

<!-- b3 -->
Todo lo útil queda entre la diagonal y la esquina, y depende de cuánto se
separan las campanas, medido en desvíos. Fijemos un cinco por ciento de falsas
alarmas. Con un desvío de separación, la detección es del veintiséis por
ciento. Con dos, del sesenta y cuatro. Con tres, del noventa y uno.

<!-- b4 -->
¿Y una curva por debajo de la diagonal? Sería un detector peor que el azar. Es
decir, un buen detector puesto al revés: basta con invertir todas sus
decisiones, y su curva se refleja por encima de la diagonal.

<!-- b5 -->
La curva sirve también para comparar. Si la de un detector queda por encima de
la de otro en todos los puntos, es mejor con cualquier criterio. Si se cruzan,
depende de la zona en la que vayas a trabajar.

<!-- b6 -->
Y un detalle de la forma: estas curvas tienen siempre la panza hacia arriba.
Muy empinadas al principio, casi planas al final. No es casualidad, y la razón
esconde el resultado más bonito del capítulo.

---

# Escena 18 — LaPendienteEsElUmbral

**Objetivo:** demostrar que la pendiente de la ROC en cada punto es la razón de
verosimilitud en el umbral, es decir, η. Comprobarlo con números y deducir que
la curva es cóncava.

**Qué hace falta saber antes:** escenas 11, 12 y 16; capítulo 7, escena 11 (la
pendiente de una curva: cuánto sube por cada paso a la derecha). Se recuerda aquí.

**Visual:** (idea de `c9p-roc-pendiente.svg`)
- Sobre la curva, un triángulo pequeño: «Paso a la derecha» y «Lo que sube».
  Rótulo «Pendiente».
- Las dos campanas: el umbral baja de «1» a «0,99» y aparece una rebanada fina.
  Dentro de la rebanada, dos rectángulos: uno bajo la campana del cero («Altura
  f₀ · Ancho») y otro bajo la del uno («Altura f₁ · Ancho»).
- El cociente: «(f₁ · Ancho) / (f₀ · Ancho)»; los anchos se tachan; queda «f₁ /
  f₀ = Λ». Enmarcado: «Pendiente = Λ en el umbral = η».
- Tabla de dos columnas que se llena: «Umbral 1,5 → 2,72», «1 → 1», «0,5 →
  0,37», «0 → 0,135»; en la curva, cuatro rectas tangentes con esas pendientes.
- La tangente recorre la curva de izquierda a derecha y se va tumbando:
  «Pendiente que baja = Panza hacia arriba». La mochila de la escena 15, pequeña.

## Narración

<!-- b1 -->
La pendiente de una curva dice cuánto sube por cada paso que das hacia la
derecha. En esta curva, eso es cuánta detección ganas por cada poco de falsa
alarma que aceptas.

<!-- b2 -->
Baja el umbral un poquito, de uno a cero coma noventa y nueve. La región donde
se dice uno gana una rebanada muy fina. La falsa alarma aumenta en el área de
esa rebanada bajo la campana del cero: su altura por el ancho. Y la detección
aumenta en el área bajo la campana del uno: su altura por el mismo ancho.

<!-- b3 -->
La pendiente es lo que sube entre lo que avanza. Los anchos se cancelan, y
queda la altura de la campana del uno entre la altura de la campana del cero,
en el umbral. La razón de verosimilitud. La pendiente de la curva en cada punto
es el umbral eta que se está usando ahí.

<!-- b4 -->
Comprobémoslo. Con el umbral en uno coma cinco, la razón es e elevado a uno:
dos coma setenta y dos. En uno vale uno. En cero coma cinco, cero coma treinta
y siete. En cero, cero coma ciento treinta y cinco. Si mides las pendientes
sobre la curva dibujada, salen esos mismos números.

<!-- b5 -->
De ahí sale la forma. Al bajar el umbral, eta baja, y la pendiente con él. Una
curva cuya pendiente no para de bajar tiene la panza hacia arriba. Es el
presupuesto otra vez: las primeras falsas alarmas compran mucha detección, y
las últimas, casi nada. Y este resultado sirve para algo más: dice en qué punto de la curva está cada
criterio.

---

# Escena 19 — ElPuntoDeBayes

**Objetivo:** encontrar en la curva el punto de mínimo error: las rectas de
igual error tienen pendiente p₀/p₁, y la última que toca la curva es tangente.
Reencontrar así η = p₀/p₁. Ubicar también el punto de a priori iguales y el de
Neyman-Pearson.

**Qué hace falta saber antes:** escenas 06, 16 y 18. De matemáticas se explica
aquí: una recta tangente toca la curva en un punto y tiene ahí su misma pendiente.

**Visual:**
- «P_e = p₀ · P_FA + p₁ · (1 − P_D)», término a término.
- En el plano, un punto y dos flechas: a la derecha «+0,7 de error por unidad»,
  hacia arriba «−0,3 por unidad». Un triángulo: «1 a la derecha, 2,33 hacia
  arriba: mismo error».
- Una familia de rectas paralelas de pendiente 2,33, más verdes cuanto más
  arriba a la izquierda. Una se desliza hasta tocar la curva en un solo punto:
  «Tangente».
- En el punto: «Pendiente de la curva = η» y «Pendiente de la recta = p₀/p₁» →
  «η = p₀/p₁». El punto: «(0,077; 0,72) · Umbral 1,42 · Error 0,139».
- Rectas de pendiente 1 (paralelas a la diagonal): tangente en «(0,16; 0,84)».
- Una vertical en «5 %»: corta la curva en «(0,05; 0,64)», pendiente «3,6».
- Dos puntos sobre la misma curva con su etiqueta, y un tercero vacío con «?».

## Narración

<!-- b1 -->
¿Qué punto de la curva da el menor error? Recuerda la fórmula: pe cero por la
falsa alarma, más pe uno por el fallo. Y el fallo es uno menos la detección.

<!-- b2 -->
Con setenta y treinta: si te mueves hacia la derecha, el error sube cero coma
siete por cada unidad de falsa alarma. Si te mueves hacia arriba, baja cero
coma tres por cada unidad de detección. Para quedarte con el mismo error, por
cada paso a la derecha tienes que subir dos coma treinta y tres. Los puntos de
igual error forman rectas con esa pendiente: pe cero entre pe uno.

<!-- b3 -->
Son rectas paralelas, y cuanto más arriba y a la izquierda, menos error.
Desliza una hacia la esquina ideal hasta que toque la curva por última vez. En
ese momento la roza en un solo punto: es tangente.

<!-- b4 -->
En el punto de tangencia, la curva y la recta tienen la misma pendiente. La de
la recta es pe cero entre pe uno. La de la curva es eta. Así que eta vale pe
cero entre pe uno. Es la regla del máximo a posteriori, encontrada otra vez,
ahora con un dibujo. El punto: falsa alarma cero coma cero setenta y siete,
detección cero coma setenta y dos.

<!-- b5 -->
Con ceros y unos igual de frecuentes, las rectas tienen pendiente uno, como la
diagonal. El punto de tangencia es el más alejado de la diagonal. Y el criterio
de Neyman-Pearson es una recta vertical en el cinco por ciento: donde corta a
la curva, ese es el punto. Ahí la pendiente vale tres coma seis.

<!-- b6 -->
Dos criterios, un detector, dos puntos de la misma curva. Y falta un tercero:
el que arregla el absurdo del test médico.

---

# Escena 20 — ErroresQueNoCuestanIgual

**Objetivo:** pagar la pregunta de la escena 09: los errores no cuestan lo
mismo. Poner costes, calcular el coste esperado de cada decisión para la
medición de 1,3 y ver que conviene decir «enfermo» aunque «sano» sea más
probable. Enunciar la regla de riesgo mínimo.

**Qué hace falta saber antes:** escenas 04, 09 y 11; capítulo 7, escena 13
(esperanza: valor por probabilidad).

**Visual:**
- La tarjeta de la escena 09: «Siempre sano → 1 %», con su «?». Dos escenas
  enfrentadas: «Enfermo enviado a casa» y «Sano que repite la prueba», con una
  balanza que se inclina hacia la primera.
- Las dos campanas de siempre con rótulos nuevos: «Sano · Centro 0» y «Enfermo
  · Centro 2». «De cada 10 con síntomas, 3 enfermos».
- Tabla de costes 2 × 2: «Acierto · 0», «Falsa alarma · 1», «Fallo · 5».
- La regla vertical en «1,3». Las probabilidades a posteriori: «Enfermo 0,44» y
  «Sano 0,56».
- Dos cuentas: «Decir sano: 5 · 0,44 = 2,2» y «Decir enfermo: 1 · 0,56 = 0,56».
  La segunda en verde.
- Rótulo: «Riesgo mínimo: La decisión de menor coste esperado».

## Narración

<!-- b1 -->
Quedó una pregunta pendiente. En el test médico, si solo contaba la
probabilidad de error, lo mejor era decir siempre sano. Era absurdo porque
mandar a casa a un enfermo no cuesta lo mismo que repetirle la prueba a un
sano. La probabilidad de error cuenta los dos fallos igual.

<!-- b2 -->
Pongámosles precio. Usaremos las mismas campanas, con otro significado: un
análisis de sangre que da un número. En los sanos, centro cero. En los
enfermos, centro dos. De cada diez personas que llegan a la consulta con
síntomas, tres están enfermas.

<!-- b3 -->
Y una tabla de costes. Acertar no cuesta nada. Una falsa alarma, tratar a un
sano, cuesta uno. Un fallo, dejar ir a un enfermo, cuesta cinco. Los números
son inventados, pero la idea no: un error es cinco veces más grave que el otro.

<!-- b4 -->
El análisis sale uno coma tres. La regla del máximo a posteriori decía cero:
sano. Miremos los costes. Con ese resultado, la probabilidad a posteriori de
estar enfermo es cero coma cuarenta y cuatro, y la de estar sano, cero coma
cincuenta y seis.

<!-- b5 -->
Si digo sano, me equivoco con probabilidad cero coma cuarenta y cuatro, y eso
cuesta cinco: en promedio, dos coma dos. Si digo enfermo, me equivoco con
probabilidad cero coma cincuenta y seis, y eso cuesta uno: cero coma cincuenta
y seis. Decir enfermo sale cuatro veces más barato, aunque sano sea más
probable.

<!-- b6 -->
Esta es la regla de riesgo mínimo. Ya no se elige la hipótesis más probable. Se
elige la decisión con menor coste esperado.

---

# Escena 21 — ElUmbralDelRiesgo

**Objetivo:** deducir paso a paso que la regla de riesgo mínimo es otra vez un
test de razón de verosimilitud, con umbral η = p₀ · (coste de falsa alarma) /
(p₁ · coste del fallo). Calcularlo (0,47; umbral 0,62), comprobar que con costes
iguales se recupera el máximo a posteriori y dar la fórmula general.

**Qué hace falta saber antes:** escenas 11, 12 y 20.

**Visual:** (idea de `c9p-riesgo-costos.svg`)
- Renglón 1: «Coste falsa alarma · P(H₀ | r) < Coste fallo · P(H₁ | r)».
- Renglón 2: «P(H₁ | r) / P(H₀ | r) > 1/5». Al lado: «P(Enfermo) > 1/6 ≈ 17 %».
- Renglón 3, Bayes: «P(H₁ | r) / P(H₀ | r) = (p₁ / p₀) · Λ(r)»; el denominador
  común tachado.
- Renglón 4, enmarcado: «Λ(r) ≷ η = p₀ · C_FA / (p₁ · C_M)».
- «η = 0,7 · 1 / (0,3 · 5) = 0,47»; «Umbral = 1 + ln(0,47)/2 = 1 − 0,38 = 0,62».
- Las campanas: el umbral se desliza de «1,42» a «0,62»; la franja intermedia se
  ilumina: «Aquí ahora se dice enfermo».
- Costes iguales: «η = p₀/p₁». La fórmula general, pequeña: «η = p₀ (c₁₀ − c₀₀)
  / p₁ (c₀₁ − c₁₁)», con la llave «Cuánto más cuesta fallar que acertar».

## Narración

<!-- b1 -->
Convirtamos esa cuenta en una regla. Se dice uno cuando decir uno sale más
barato: cuando el coste de la falsa alarma, por la probabilidad a posteriori de
hache cero, es menor que el coste del fallo, por la probabilidad a posteriori
de hache uno.

<!-- b2 -->
Pasamos las probabilidades a un lado y los costes al otro. La probabilidad a
posteriori del uno, entre la del cero, tiene que superar al coste de la falsa
alarma entre el coste del fallo. Aquí, un quinto. Es decir: basta con que la
probabilidad de estar enfermo pase de un sexto, un diecisiete por ciento, para
decir enfermo.

<!-- b3 -->
Ahora, la regla de Bayes a la izquierda. El denominador común se cancela, y ese
cociente es pe uno entre pe cero, por la razón de verosimilitud. Despejamos: la
razón de verosimilitud tiene que superar a pe cero por el coste de la falsa
alarma, entre pe uno por el coste del fallo.

<!-- b4 -->
Otra vez la razón de verosimilitud contra un umbral. Solo ha cambiado eta. Con
nuestros números: cero coma siete por uno, entre cero coma tres por cinco. Cero
coma cuarenta y siete. Y el umbral sobre el análisis: uno más la mitad del
logaritmo de cero coma cuarenta y siete. Cero coma sesenta y dos.

<!-- b5 -->
El umbral ha bajado de uno coma cuarenta y dos a cero coma sesenta y dos. En
toda esa franja, donde antes se decía sano, ahora se dice enfermo. Si dejar ir
a un enfermo sale caro, más vale pasarse de precavido.

<!-- b6 -->
Dos comprobaciones. Si los dos errores cuestan lo mismo, eta vuelve a ser pe
cero entre pe uno: el máximo a posteriori es un caso particular. Y si acertar
también costara algo, en la fórmula entraría la diferencia entre fallar y
acertar. Lo que cuenta es cuánto más cuesta equivocarse.

---

# Escena 22 — RiesgoNoEsError

**Objetivo:** medir las dos reglas con las dos varas: el máximo a posteriori
gana en probabilidad de error y el riesgo mínimo gana en coste. No hay
contradicción: son objetivos distintos. Ver los tres criterios como tres puntos
de la misma curva ROC.

**Qué hace falta saber antes:** escenas 08, 19 y 21.

**Visual:**
- Tabla de dos renglones y cinco columnas que se llena celda a celda:
  «Máximo a posteriori · Umbral 1,42 · Falsa alarma 0,077 · Fallo 0,28 · Error
  0,139 · Coste 0,48» y «Riesgo mínimo · Umbral 0,62 · Falsa alarma 0,27 · Fallo
  0,084 · Error 0,21 · Coste 0,31». Se marcan en verde el menor error y el menor
  coste, que están en renglones distintos.
- Cuentas del coste: «0,7 · 0,077 · 1 + 0,3 · 0,28 · 5 = 0,054 + 0,42» y «0,7 ·
  0,27 · 1 + 0,3 · 0,084 · 5 = 0,19 + 0,125».
- Cien enfermos en fila: «28 se escapan» pasa a «8 se escapan».
- La curva ROC de la escena 19 con tres puntos y sus pendientes:
  «Neyman-Pearson · 3,6», «Máximo a posteriori · 2,33», «Riesgo mínimo · 0,47».
- Frase final en pantalla: «Cambia el umbral, no el detector».

## Narración

<!-- b1 -->
Tenemos dos reglas sobre las mismas campanas: la del máximo a posteriori, con
el umbral en uno coma cuarenta y dos, y la de riesgo mínimo, con el umbral en
cero coma sesenta y dos. Midamos las dos con las dos varas: la probabilidad de
error y el coste medio.

<!-- b2 -->
El máximo a posteriori: falsa alarma cero coma cero setenta y siete, fallo
cero coma veintiocho. Su error ya lo sabemos: cero coma ciento treinta y nueve.
Su coste: cero coma cero cincuenta y cuatro de las falsas alarmas, más cero
coma cero ochenta y cinco de los fallos multiplicado por cinco. En total, cero
coma cuarenta y ocho.

<!-- b3 -->
El riesgo mínimo: la falsa alarma sube a cero coma veintisiete y el fallo baja
a cero coma cero ochenta y cuatro. Su error: cero coma veintiuno. Su coste:
cero coma diecinueve, más cero coma ciento veinticinco. Cero coma treinta y
uno.

<!-- b4 -->
El máximo a posteriori gana en error: catorce por ciento contra veintiuno. El
riesgo mínimo gana en coste: cero coma treinta y uno contra cero coma cuarenta
y ocho. No hay contradicción: persiguen cosas distintas. El segundo acepta más
del triple de falsas alarmas para que se le escapen ocho enfermos de cada cien,
en lugar de veintiocho.

<!-- b5 -->
En la curva es un punto más, donde la pendiente vale cero coma cuarenta y
siete: más arriba y más a la derecha. Tres criterios, tres puntos de la misma
curva. Neyman-Pearson, donde la curva es más empinada. El máximo a posteriori,
en medio. El riesgo mínimo, donde ya se tumba.

<!-- b6 -->
La moraleja: minimizar la probabilidad de error es lo correcto solo si todos
los errores cuestan lo mismo. Cuando no es así, hay que minimizar el coste. Y
lo que cambia es el umbral, no el detector.

---

# Escena 23 — DecidirYEstimar

**Objetivo:** cerrar el círculo con el capítulo 8: decidir y estimar son el
mismo problema con distinto coste. Con acertar o fallar sale la hipótesis más
probable; al juntar las hipótesis hasta un continuo, ese coste deja de servir,
se usa el cuadrado del error y sale la media condicional.

**Qué hace falta saber antes:** escenas 01 y 20; capítulo 8, escenas 04 y 06
(media, mediana y moda según cómo se mide el error; la media condicional).

**Visual:** (idea de `c9p-estimacion-continuo.svg`)
- Las tres casillas del capítulo 8: «Cuadrado → Media», «Tamaño → Mediana»,
  «Acierto → Moda». La tercera se ilumina y se une a «Máximo a posteriori».
- Un eje de voltios con dos niveles (0 y 2) y sus dos campanas; pasan a ser
  tres, nueve, cien, cada vez más juntos, hasta un eje continuo. Rótulo que
  cambia: «¿Cuál de estas?» → «¿Cuánto?».
- Un dardo que nunca cae exactamente en el punto: «Acertar: Probabilidad 0». La
  tabla de costes 0–1 se sustituye por una parábola: «Coste = Error²».
- Una curva a posteriori sobre el eje continuo, con su pico («Más probable») y
  su centro de masa («Media condicional · Capítulo 8»).
- El «0,79» y el «1» del canal, lado a lado: «Estimar» y «Decidir».

## Narración

<!-- b1 -->
Con los costes sobre la mesa, se cierra el círculo con el capítulo anterior.
Allí vimos que la mejor apuesta depende de cómo se mide el error. Con el
cuadrado sale la media. Con acertar o fallar, la moda: lo más probable. La
regla del máximo a posteriori es exactamente eso: coste cero si aciertas, uno
si fallas.

<!-- b2 -->
Ahora junta las hipótesis. Con dos amplitudes posibles, cero y dos voltios,
eliges entre dos. Con tres, entre tres. Con nueve. Con cien niveles, cada vez
más apretados. En el límite, la amplitud puede ser cualquier número, y ya no
eliges entre opciones: das un valor. Eso es estimar.

<!-- b3 -->
En ese límite, acertar o fallar deja de servir: nunca vas a dar con el valor
exacto. Hay que medir cuánto te alejas, y lo habitual es el cuadrado del error.
Con ese coste, la regla de riesgo mínimo da la media condicional: el estimador
del capítulo ocho.

<!-- b4 -->
Es la misma maquinaria: probabilidades a posteriori y el menor coste esperado.
Solo cambia el coste, y con él, el tipo de respuesta. Detectar responde a cuál
de estas pocas. Estimar responde a cuánto. Por eso, en el canal, el cero coma
setenta y nueve y el uno eran las dos respuestas correctas: a dos preguntas
distintas.

<!-- b5 -->
Todo lo que hemos hecho supone algo muy cómodo: que conocemos las dos campanas.
En la práctica nadie te las da. Lo que tienes son datos.

---

# Escena 24 — RocConDatos

**Objetivo:** construir una curva ROC sin conocer las densidades, a partir de
casos etiquetados y una puntuación: ordenar, bajar el umbral caso a caso y
dibujar la escalera. Avisar de sus dos limitaciones.

**Qué hace falta saber antes:** escena 16.

**Visual:**
- Las dos campanas se desvanecen y quedan puntos sueltos. Ocho fichas, cada una
  con una puntuación y una etiqueta: cuatro «+» (azul) y cuatro «−» (magenta).
- Las fichas se ordenan de mayor a menor puntuación: «+ + − + − + − −».
- Un umbral baja ficha a ficha. En el plano, el punto se mueve: cada «+» sube
  «¼», cada «−» avanza «¼» a la derecha: «Arriba, arriba, derecha, arriba,
  derecha, arriba, derecha, derecha».
- La escalera completa de «(0, 0)» a «(1, 1)». Rótulo «ROC empírica».
- La escalera se afina al pasar de 8 a 80 y a 8.000 casos, hasta parecerse a la
  curva suave.
- Dos avisos: «Pocos casos: Dibujo tosco» y «Mismos datos para ajustar y medir:
  Optimista».

## Narración

<!-- b1 -->
En la práctica no conoces las densidades. Lo que tienes son casos ya
resueltos, de los que sabes la verdad, y un detector que le pone a cada uno una
puntuación: cuanto más alta, más parece hache uno. Puede ser un análisis, un
filtro de correo basura o un programa que busca tumores en radiografías.

<!-- b2 -->
Tomemos ocho casos: cuatro positivos y cuatro negativos. Los ordenamos de
mayor a menor puntuación. Queda así: positivo, positivo, negativo, positivo,
negativo, positivo, negativo, negativo. No está perfecto: hay negativos
colados entre los positivos.

<!-- b3 -->
Ahora bajamos el umbral desde arriba, caso a caso. Cada vez que un positivo
queda por encima del umbral, la detección sube un cuarto: un escalón hacia
arriba. Cada vez que queda un negativo, la falsa alarma sube un cuarto: un
escalón hacia la derecha.

<!-- b4 -->
El camino es: arriba, arriba, derecha, arriba, derecha, arriba, derecha,
derecha. Una escalera que va de una esquina a la otra. Es la curva ROC medida
con datos. Con ocho casos los escalones son enormes; con miles, la escalera se
confunde con la curva suave.

<!-- b5 -->
Dos avisos. Con pocos casos de un tipo, la curva es un dibujo tosco, y no hay
que fiarse de sus detalles. Y si la mides con los mismos datos con los que
ajustaste el detector, sale mejor de lo que es. Hay que medirla con datos que
el detector no haya visto.

---

# Escena 25 — AreaBajoLaCurva

**Objetivo:** resumir la curva en un número, el área bajo ella; calcularla en la
escalera (13/16) y descubrir lo que significa: la probabilidad de que un
positivo al azar tenga más puntuación que un negativo al azar. Avisar de lo que
no dice.

**Qué hace falta saber antes:** escena 24.

**Visual:** (idea de `c9p-auc.svg`)
- La escalera con el área de debajo sombreada. Referencias: la diagonal, «0,5»;
  el cuadrado entero, «1».
- Cuatro columnas de ancho «¼» y alturas «2/4», «3/4», «1» y «1»: «(0,5 + 0,75 +
  1 + 1) / 4 = 13/16 = 0,81».
- La tira «+ + − + − + − −»: bajo cada «−», cuántos «+» tiene por encima: «2, 3,
  4, 4». «13 de 16 parejas».
- Un positivo y un negativo sacados al azar, con sus puntuaciones comparadas:
  «Área = P(Positivo > Negativo)».
- Las dos campanas de siempre: «Área = 0,92».
- Dos curvas distintas con la misma área; un recuadro en la zona de «1 %» donde
  una es mucho mejor que la otra.

## Narración

<!-- b1 -->
A veces se quiere resumir toda la curva en un solo número. El más usado es el
área que queda debajo. Para la diagonal, el detector que tira una moneda, el
área es un medio. Para el detector perfecto, uno.

<!-- b2 -->
Calculémosla en nuestra escalera. Son cuatro columnas de un cuarto de ancho.
Sus alturas: dos cuartos, tres cuartos, uno y uno. Sumamos y dividimos entre
cuatro: trece dieciseisavos. Cero coma ochenta y uno.

<!-- b3 -->
Ese número significa algo muy concreto. Toma un positivo al azar y un negativo
al azar: es la probabilidad de que el positivo tenga más puntuación.
Comprobémoslo. Hay dieciséis parejas. El primer negativo tiene dos positivos
por encima. El segundo, tres. Los otros dos, cuatro cada uno. Trece de
dieciséis. El mismo número.

<!-- b4 -->
Así que el área mide lo bien que el detector ordena: que ponga los positivos
por delante de los negativos. Para nuestras dos campanas, separadas dos
desvíos, vale cero coma noventa y dos.

<!-- b5 -->
Pero cuidado con lo que no dice. Es un promedio sobre todos los umbrales,
también los que nunca vas a usar. Dos detectores con la misma área pueden ser
muy distintos en la zona de un uno por ciento de falsas alarmas, que quizá es
la única que te importa. Y el área tampoco te dice dónde poner el umbral.

---

# Escena 26 — OrdenarNoEsCortar

**Objetivo:** separar dos propiedades de una puntuación: ordenar bien (lo que ve
la curva ROC) y significar una probabilidad (calibración). Ver que cortar en 0,5
solo es óptimo si la puntuación está calibrada, y cómo elegir el umbral con un
criterio explícito, incluido el caso de no tener ni costes ni a priori.

**Qué hace falta saber antes:** escenas 19, 22, 24 y 25.

**Visual:**
- Las ocho fichas con sus puntuaciones; se transforman todas (al cuadrado): los
  números cambian, el orden no. La escalera, al lado, no se mueve: «Mismo orden
  = Misma curva».
- Un clasificador que entrega «0,7»; un umbral fijo en «0,5» con el rótulo «Por
  defecto».
- Cien casos con puntuación 0,7: «Calibrado: 70 positivos»; al lado, «Mal
  calibrado: 40 positivos».
- La curva ROC con el punto del «0,5» cayendo en un sitio cualquiera, lejos de
  los tres puntos de la escena 22.
- Tres tarjetas: «Cota de falsas alarmas → Neyman-Pearson», «Costes → Riesgo
  mínimo», «Nada → El punto más lejos de la diagonal». Bajo la tercera, la
  tangente de pendiente 1 y la letra pequeña: «Supone a priori iguales y costes
  iguales».

## Narración

<!-- b1 -->
En una puntuación hay dos cosas distintas, y conviene separarlas. Una es que
ordene bien: los positivos, por encima. La otra es qué significa el número.

<!-- b2 -->
Haz un experimento: eleva todas las puntuaciones al cuadrado. Los números
cambian, pero el orden no. La escalera es idéntica, y el área también. La curva
ROC solo ve el orden.

<!-- b3 -->
Ahora, muchos detectores modernos entregan un número entre cero y uno y lo
llaman probabilidad. Y casi todo el mundo corta en cero coma cinco. Eso solo es
la regla del máximo a posteriori si el número es de verdad la probabilidad a
posteriori: si, de todos los casos que reciben un cero coma siete, el setenta
por ciento son positivos. A eso se le llama estar calibrado.

<!-- b4 -->
Un detector puede ordenar perfectamente y estar mal calibrado. Entonces su
cero coma cinco cae en un punto cualquiera de la curva. Un área alta dice que
ordena bien. No dice que cero coma cinco sea el sitio donde cortar.

<!-- b5 -->
El umbral se elige con un criterio explícito. Si tienes un tope de falsas
alarmas, Neyman-Pearson. Si tienes costes, riesgo mínimo. ¿Y si no tienes nada?
Se suele tomar el punto de la curva más alejado de la diagonal.

<!-- b6 -->
Pero ese punto ya lo conocemos: es donde la pendiente vale uno. Elegirlo es
suponer, sin decirlo, que las dos hipótesis son igual de probables y que los
dos errores cuestan lo mismo. No existe un umbral sin supuestos. Solo hay
supuestos que se dicen y supuestos que no.

---

# Escena 27 — CuantasPruebas

**Objetivo:** ver que una probabilidad de error medida contando tiene su propio
error (raíz de p(1 − p)/N), cuántas pruebas hacen falta, y la trampa de los
sucesos raros: no ver ningún error no quiere decir que no los haya.

**Qué hace falta saber antes:** escenas 07 y 16; capítulo 7, escena 16 (grandes
números: el promedio se acerca al valor real al crecer el número de pruebas).

**Visual:**
- Un contador de pruebas: bits que pasan por el umbral, con los fallos en rojo.
  «Fallos / Pruebas» que oscila y se estabiliza hacia «0,159».
- La fórmula, pieza a pieza: «Error típico = √(p (1 − p) / N)».
- Dos barras de incertidumbre alrededor de 0,159: «N = 100 → ± 0,037» (de 0,12 a
  0,20) y «N = 10.000 → ± 0,004». «Precisión × 10 = Pruebas × 100».
- Pregunta con pausa: umbral en 3, «Falsa alarma = 0,00135». «1.000 pruebas sin
  señal. ¿Cuántas falsas alarmas verás?». Un histograma de resultados posibles:
  la barra del «0» mide «26 %».
- La regla: «Ver al menos 10 sucesos → N ≥ 10 / p». «10 / 0,00135 ≈ 7.400».
  «Uno en un millón → Diez millones».
- Frase final: «Cero errores vistos ≠ Error cero».

## Narración

<!-- b1 -->
Una última cuestión práctica. Las probabilidades de error se miden contando: se
hacen muchas pruebas y se mira cuántas salen mal. Es el promedio del capítulo
siete: al crecer el número de pruebas, la fracción de fallos se acerca a la
probabilidad real. La pregunta es cuántas pruebas hacen falta.

<!-- b2 -->
Esa cuenta tiene su propio error. Su tamaño típico es la raíz cuadrada de pe
por uno menos pe, dividido entre el número de pruebas. Para nuestro cero coma
ciento cincuenta y nueve, con cien pruebas es de cero coma cero treinta y
siete: puede salirte un doce por ciento o un veinte.

<!-- b3 -->
Con diez mil pruebas baja a cero coma cero cero cuatro. Por la raíz cuadrada,
para ganar diez veces más precisión hacen falta cien veces más pruebas.

<!-- b4 -->
Lo delicado son los sucesos raros. Pon el umbral en tres voltios: la falsa
alarma es de poco más de una entre mil. Haces mil pruebas sin señal. ¿Cuántas
falsas alarmas vas a ver? Lo esperado es una y pico. Pero la probabilidad de no
ver ninguna es del veintiséis por ciento.

<!-- b5 -->
Una de cada cuatro veces concluirías que tu detector nunca da falsas alarmas.
La regla práctica: para medir una probabilidad hay que llegar a ver al menos
unos diez sucesos. Aquí, unas siete mil cuatrocientas pruebas. Para un error de
uno entre un millón, diez millones. Cero errores vistos no es error cero. Es que todavía no has probado lo
bastante.

---

# Escena 28 — DeUnNumeroAUnaSenal

**Objetivo:** recapitular el capítulo en tres ideas y abrir el siguiente: todo se
hizo con una sola medición, pero un receptor real recibe una señal entera, y
para decidir con ella hay que saber describir el ruido a lo largo del tiempo.

**Qué hace falta saber antes:** todo el capítulo.

**Visual:**
- Tres tarjetas que aparecen una a una: «Λ(r) ≷ η», «η: A priori · Presupuesto ·
  Costes», «La curva ROC: Pendiente = η» (con la curva y sus tres puntos).
- Un solo punto «r» sobre un eje. El punto se multiplica: una fila larga de
  barras, una señal con ruido muestra a muestra.
- La razón de verosimilitud con muchas «r» dentro: «Λ(r[0], r[1], r[2], …) ≷ η».
  Dos etiquetas pequeñas hacia delante: «Toda la señal en un solo número» y «Más
  datos no bastan», con «Capítulo 13».
- Dos muestras vecinas del ruido unidas por un «?»: «¿Tienen algo que ver?».
- Una grabación de ruido; debajo se apilan muchas más, distintas entre sí.

## Narración

<!-- b1 -->
Recojamos el capítulo en tres ideas. Una: decidir bien es comparar un número,
la razón de verosimilitud, con un umbral. Dos: el umbral sale de lo que sabes o
de lo que quieres: las probabilidades a priori, un presupuesto de falsas
alarmas, o los costes. Tres: la curva ROC enseña todos los umbrales a la vez, y
su pendiente es el propio umbral.

<!-- b2 -->
Pero en todo el capítulo la medición ha sido un solo número. Un voltaje. Un
receptor de verdad no recibe un número: recibe una señal entera, miles de
muestras seguidas, cada una con su ruido.

<!-- b3 -->
La regla no cambia: la razón de verosimilitud de todas las muestras juntas,
contra un umbral. Al final del curso veremos que toda esa señal se puede
resumir en un solo número sin perder nada. Y también que tener más datos no
basta: hay que saber combinarlos.

<!-- b4 -->
Antes hace falta algo que todavía no tenemos. Para escribir esa razón hay que
describir el ruido a lo largo del tiempo. El ruido de este instante, ¿tiene
algo que ver con el de dentro de un milisegundo? ¿Cómo se describe, con
probabilidades, una señal entera que nunca se repite? Para eso no basta con mirar una grabación del ruido. Hay que imaginar muchas a
la vez.
