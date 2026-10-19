# Capítulo 8 — Estimación

> **Guion base: narración de todo el capítulo. No se renderiza.**
> Es la fuente de texto para los 5 episodios (ver `../README.md` §1 para qué
> escenas van en cada uno). Cada episodio copia de aquí su narración a su
> propio `E<N>_.../guion.md`, que es el que lleva gancho, cierre y momentos, y
> el que se anima. Las secciones "Visual" son ideas iniciales, no
> especificación.
>
> **Estado:** narración completa, **esperando la aprobación del usuario**.
> Mientras no esté aprobada, cualquier ajuste de texto que pida el usuario se
> hace aquí primero, y después se copia al `guion.md` del episodio.

Guion para las 21 escenas del capítulo. Fuentes: `Apuntes/PROCESAMIENTO DE
SEÑALES.md` (sección "Estimación", líneas 289–403, sin los Ejercicios
Propuestos) y `Apuntes/PROCESAMIENTO DE SEÑALES - Cap 8 en profundidad.md`:
Parte 1 (completar el cuadrado, media condicional y doble promedio, regla de
ortogonalidad, LMMSE por cálculo, por ortogonalidad y por geometría, ecuaciones
normales), Parte 2.1 (la carpa), 2.3 (el caso gaussiano), 2.4 y 2.5 (dos
mediciones y redundancia, rehechas con números redondos), Parte 3.1 y 3.4
(estimador con datos, actualización con un dato nuevo) y Parte 4 (costos,
puentes a los capítulos 9, 10 y 12). Figuras de referencia:
`c8p-completar-cuadrado.svg`, `c8p-costos.svg`, `c8p-proyeccion.svg`,
`c8p-gaussiano-condicional.svg`.

**Qué se da por sabido del capítulo 7** (y se recuerda en una frase donde se
usa): el dado (media 3,5, varianza 2,92), esperanza y su linealidad, varianza,
varianza de una uniforme (ancho² / 12) y de un bit (p(1 − p)), el canal que
confunde bits y su tabla conjunta (0,63 · 0,07 · 0,03 · 0,27), la esperanza
condicional y la torre (0,79 y 0,045), la altura y la ley de la varianza total
(81,76 = 41,2 + 40,56), covarianza, "cero no es nada", las variables como
flechas y rho como coseno. De matemáticas se explica aquí: completar el
cuadrado, derivada como pendiente, la distancia más corta a una recta,
Pitágoras con seno y coseno, sistema de dos ecuaciones, matriz por columna,
inversa y determinante 2 × 2.

Cómo está escrito (README §3, "Explicar de forma explícita"): cada concepto
sigue el camino caso → cuenta a mano → dibujo → fórmula → comprobación. Casi
todo el capítulo corre sobre cuatro ejemplos que vuelven: el dado, la altura,
el canal de bits y **el termómetro** (temperatura de media 20 y varianza 4,
ruido de varianza 1), que es el sensor de los capítulos 10 y 12.

Convención de letras: el libro escribe el estimador lineal como aX + b. Aquí la
pendiente se llama **h** («hache»), como en el capítulo 12, que recuerda este
capítulo con «i griega con sombrero igual a hache por equis» y la parábola
4 − 8h + 5h². Con dos termómetros, los pesos se dicen «el peso de A» y «el
peso de B» (en pantalla h_A, h_B). Castellano de España.

## Reparto en episodios

| Episodio | Escenas | Idea fuerza |
|---|---|---|
| E1 · ¿Cuál es tu mejor apuesta? | 01 AdivinarUnNumero, 02 ProbarApuestas, 03 CompletarElCuadrado, 04 OtrasFormasDeFallar | Sin datos, la mejor apuesta es la media y el error que queda es la varianza; si cambias la forma de medir el error, cambia la respuesta |
| E2 · Lo que el dato te cuenta | 05 LaAlturaOtraVez, 06 MediaCondicional, 07 ElEstimadorEsAleatorio, 08 ElErrorSinPatron | Con un dato, apuesta la media de la rebanada; el error que queda no tiene ningún patrón que el dato pueda explicar |
| E3 · ¿Y si solo vale una recta? | 09 LaCarpa, 10 ElTermometro, 11 LaFormulaDeLaRecta, 12 LeerLaRecta | La mejor recta solo necesita medias, varianzas y covarianzas, y su error es σ²(1 − ρ²) |
| E4 · La sombra de una flecha | 13 LaSombra, 14 DosCondiciones, 15 Pitagoras, 16 CuandoLaRectaBasta | Estimar con una recta es proyectar una flecha sobre otra, y con gaussianas eso ya es lo mejor posible |
| E5 · ¿Dos termómetros mejor que uno? | 17 DosTermometros, 18 EcuacionesNormales, 19 ElSegundoTermometro, 20 LlegaUnDatoNuevo, 21 DeLaTeoriaALosDatos | Con varias mediciones, el error perpendicular a cada una da las ecuaciones normales; cada medición vale por lo que trae de nuevo |

Narración base por episodio (sin gancho ni cierre): ~1.150–1.480 palabras,
unos 7,5–10 min de voz; con gancho y cierre, ~9–11 min. **E5 es el más
largo** (5 escenas, ~1.480 palabras): su cierre tiene que ser corto, y si al
armar su `guion.md` pasa de ~10,5 min, el bloque b1 de la escena 21 (la ironía
de los datos) es el primer candidato a recortarse.

El gancho y el cierre de cada episodio **no** están aquí: se escriben al
armar el `guion.md` del episodio (README §2, paso 8). Cada cierre anuncia el
episodio siguiente por su título. El cierre de E5 anuncia el E1 del capítulo 9
por su título: **«¿Un cero o un uno?»**.

## Hilos que cruzan el capítulo

- **Los ejemplos que vuelven** (mismo dibujo y mismos números siempre):
  - **el dado** (escenas 01–03): apuestas 3 y 4 → 19/6 ≈ 3,17; apuesta 1 →
    55/6 ≈ 9,17; apuesta 3,5 → 2,92 = la varianza del dado. Parábola
    2,92 + (3,5 − ŷ)²;
  - **las llamadas** (escena 04, vuelve en la 21): 0 (40 %), 1 (30 %), 2 (20 %),
    10 (10 %). Media 1,7; mediana 1 (error absoluto 1,5 contra 1,78 apostando
    1,7); moda 0 (acierta el 40 %);
  - **la altura** del capítulo 7 (escena 05): sin datos 167,2 y error 81,76;
    sabiendo el grupo, 175 / 162 con errores 49 / 36 → 41,2; lo explicado, 40,56;
  - **el canal de bits** del capítulo 7 (escenas 06–08, 16 y 21): Ŝ = 0,79 o
    0,045; errores por columna 0,16 y 0,04; Ŝ vale 0,79 con prob. 0,34;
    media de Ŝ = 0,3; error total 0,084 contra 0,21 (−60 %); dentro de la
    columna «recibido 1», 0,27 · 0,21 − 0,07 · 0,79 = 0. Como R solo vale 0 o 1,
    la recta empata con la media condicional (escena 16);
  - **la carpa** (escenas 09 y 12): uniforme en el triángulo de base 0–2 y
    pico 1; media condicional = carpa de altura ½, error 1/24 ≈ 0,042; ρ = 0,
    mejor recta horizontal en ⅓, error 1/18 ≈ 0,056;
  - **el termómetro** (escenas 10–20): temperatura de media 20 y varianza 4,
    ruido de A de varianza 1. Lee 23. h = 0 → error 4; h = 1 → error 1;
    h = 0,8 → error 0,8 y apuesta 22,4. Parábola 4 − 8h + 5h². ρ² = 0,8.
    Flechas de largo 2 y √5 ≈ 2,24, ángulo ≈ 27°, sombra 1,79, error √0,8 ≈ 0,89;
    Pitágoras 4 = 3,2 + 0,8. Al revés (lectura desde la temperatura) el factor
    es 1, no 1,25;
  - **los dos termómetros** (escenas 17–20): B con ruido de varianza 4. Matriz
    (5, 4; 4, 8), columna (4, 4), determinante 24. Pesos ⅔ y ⅙; B lee 22 →
    apuesta 22,33; error ⅔ ≈ 0,67 (solo A 0,8; solo B 2). Los tres segundos
    termómetros: copia exacta (determinante 0), copia empeorada (peso 0, error
    0,8), ruido doble del de A (pesos 2 y −1, error 0; A 23 y B 24 → 22).
    Actualización: sorpresa −0,4, ganancia 0,8/4,8 = ⅙, 22,33, error 0,67.
- **La promesa del capítulo 7** (escena 20 de aquel guion: «el error del mejor
  estimador será exactamente ese primer trozo»): se paga en la escena 05.
- **La regla de ortogonalidad**: se presenta con números en la escena 08 (contra
  toda función del dato), se recorta a «contra 1 y contra el dato» en la 14, y
  se usa para cada medición en la 17. Es la herramienta del filtro de Wiener.
- **Tres caminos, un resultado** (escenas 10, 11, 13 y 14): el fondo de la
  parábola, la pendiente cero y el ángulo recto dan el mismo 0,8.
- **La partición de la varianza** (escenas 05 y 15): la varianza total del
  capítulo 7 y el Pitágoras de la proyección son la misma idea («lo que el dato
  explica y lo que no»).
- **«0,79 no es un bit»** (escena 06 → escena 21 → capítulo 9): la pregunta de
  decidir entre cero y uno queda abierta a propósito. Se suma a la tercera forma
  de medir el error, acertar o fallar (escena 04), que es la del MAP.
- **Puentes a otros capítulos:**
  - capítulo 9: el costo acertar/fallar da la moda (MAP); decidir en vez de
    estimar (escenas 04, 06, 21);
  - capítulo 10: el termómetro es el sensor (media 20, varianza 4); la
    predicción lineal (escena 21 de aquel guion) usa la recta y las flechas de
    este capítulo. Aquel guion pide el **mismo dibujo de flechas**: Y, X, la
    sombra de Y sobre X y el error a 90°. Es el que se usa aquí;
  - capítulo 12: su escena 02 recuerda este capítulo con el termómetro de
    una medición (h = 0,8, error 0,8, parábola 4 − 8h + 5h²) y su escena 27
    muestra la ganancia de Kalman 2,826/3,826, de la misma forma
    error / (error + ruido) que la escena 20 de aquí (0,8/4,8);
  - capítulos 10 y 12: las ecuaciones normales con muestras de una señal
    (escena 21).
- **Cierre del capítulo** (la escena 21 ya lo prepara; cierre de E5, a escribir):
  muchas veces no hay que dar un número sino elegir (¿cero o uno?, ¿avión o
  ruido?) → capítulo 9.
- **Entrada desde el capítulo 7:** el cierre de su E7 tiene que anunciar el E1
  de este capítulo por su título, **«¿Cuál es tu mejor apuesta?»**. La escena 29
  del Cap. 7 termina con la proyección; el puente puede quedarse así («antes de
  proyectar flechas, empecemos por lo más simple: apostar un número»).
- **Parábolas**: la del error de este capítulo (dado, termómetro) **no es** la de
  Cauchy-Schwarz del capítulo 7, así que no cuenta en el «volverá dos veces más»
  de la escena 28 de aquel guion. Sí es la «parábola del error» que retoman los
  capítulos 10 y 12.

## Recortes decididos

- La demostración por cálculo del MMSE sin datos se menciona en una frase; el
  camino principal es completar el cuadrado (escena 03). La derivada se explica
  en la escena 11, donde hace falta.
- El trapecio asimétrico (Parte 2.2) no entra: la carpa ya muestra que la curva
  gana, con números más simples.
- El ejemplo de dos mediciones de la Parte 2.4 (con raíces) y la tabla de mal
  condicionamiento de la 2.5 se sustituyen por los termómetros, con números
  redondos y la misma idea (redundancia, pesos de signo opuesto).
- No entran (se cortaron de la escena 21 para que E5 no pase de ~10,5 min): no
  invertir la matriz, el problema de las mediciones casi repetidas, Cholesky,
  número de condición, regularización, el MMSE negativo como señal de momentos
  imposibles, el n − 1 de los estimadores muestrales, Toeplitz y
  Levinson-Durbin (son del capítulo 12).
- La gaussiana condicional se muestra (rebanadas que son campanas de igual
  ancho), no se demuestra.
- Los Ejercicios Propuestos no se resuelven. Ojo: el contraejemplo Y = X² del
  capítulo 7 es el ejercicio 2b; por eso el ejemplo de «la curva gana» es la carpa.

## Pronunciación

Probar de oído antes de sintetizar (README §9): «hache», «be», «i griega
sombrero», «rho», «sigma», «mu», «Pitágoras», «Kalman», «gaussiano»,
«veinticuatroavo», «dieciochoavo», «centralita». Las siglas MMSE y LMMSE **no se
dicen**: se dice «estimador de mínimo error cuadrático medio» y «estimador
lineal óptimo», y la sigla aparece solo en pantalla.

## Piezas visuales nuevas

Ya existen en `comun/figuras.py` y se reutilizan: `dado_n` (Cap. 10 E1),
`termometro()` (Cap. 10 E2), `ParabolaJ` (Cap. 12 E7: es la parábola
4 − 8h + 5h² de la escena 10), `flechas_xy` (Cap. 12 E1: «el dibujo del
capítulo 8» con x, y, ŷ, e), `MatrizT` (Cap. 12 E1, para la matriz 2 × 2),
`Curva` y `gaussiana`. Nuevas (sección «capítulo 08, episodio N»):
- parábola de apuestas: puntos (apuesta, error) que caen sobre una U, con el
  vértice marcado;
- barras de probabilidad para las llamadas, con marcas de media, mediana y moda;
- tabla conjunta del canal 2 × 2 (si el Cap. 7 todavía no la creó), con
  columnas que se resaltan;
- la carpa: triángulo, puntos uniformes, rebanada vertical y la carpa de los centros;
- nube elíptica gaussiana con rebanadas que se convierten en campanas;
- dos termómetros A y B con su lectura;
- triángulo rectángulo de la proyección con el ángulo recto marcado.

---

# Escena 01 — AdivinarUnNumero

**Objetivo:** plantear qué es estimar en este curso (conocida la distribución,
apostar por el valor que saldrá), distinguirlo de la estimación de
Probabilidad y Estadística, y elegir cómo medir lo mal que lo hacemos: el error
cuadrático medio, explicando por qué el cuadrado.

**Qué hace falta saber antes:** capítulo 7 (el dado, esperanza; escena 03:
estimar y detectar).

**Visual:**
- El dado, quieto, y un «?» grande: «¿qué número dices?».
- Dos tarjetas: «Prob. y Estadística: muestra → parámetros» (tachada para este
  curso) y «aquí: distribución conocida → apostar un valor».
- Errores con signo: apuesta 3, sale 5 → «+2»; sale 1 → «−2»; se cancelan.
- Los mismos errores al cuadrado: «4», «4». Una tabla «error → coste»: 1 → 1,
  2 → 4, 3 → 9.
- La fórmula por piezas: «E[(Y − ŷ)²]», con el rótulo «error cuadrático medio».
- El sombrero: «ŷ = estimación» (el sombrero se ilumina en ámbar).

## Narración

<!-- b1 -->
En el primer capítulo dijimos que esta materia hace dos cosas con el azar, que son estimar y detectar. Empezamos por estimar, y con el caso más sencillo posible.
Voy a tirar un dado, pero antes de que lo tire tienes que decirme un número, y
quiero que te equivoques lo menos posible. ¿Qué número dices?

<!-- b2 -->
Ojo, que estimar aquí no es lo mismo que en Probabilidad y Estadística. Allí
no conocías la distribución y la aproximabas con una muestra, es decir, estimabas la media de una población a partir de unos cuantos datos. Aquí, en cambio, la distribución la conocemos entera. Lo que no sabemos es qué valor saldrá esta vez, así que hay que apostar por uno.

<!-- b3 -->
Para elegir la mejor apuesta hace falta medir cuánto nos equivocamos. El error es lo que sale menos lo que dijimos. Así, si apuestas tres y sale cinco, el error es dos, y si sale uno, el error es menos dos. Podríamos promediar los errores, pero entonces los positivos y los negativos se cancelarían, y un error enorme hacia arriba
taparía otro enorme hacia abajo.

<!-- b4 -->
La solución es elevar el error al cuadrado antes de promediar. Un cuadrado
nunca es negativo, así que ya nada se cancela. Además, castiga más los errores grandes, porque equivocarse por dos cuesta cuatro, y equivocarse por tres cuesta nueve. La media
de ese cuadrado se llama error cuadrático medio, y la mejor apuesta será la
que lo haga lo más pequeño posible.

<!-- b5 -->
La apuesta se escribe con un sombrero. Así, i griega sombrero es lo que adivinamos de i griega, que es lo que sale. El sombrero se queda para todo el curso, así que cada vez que lo veas, significa estimación. Y ahora, a probar apuestas con el dado.

---

# Escena 02 — ProbarApuestas

**Objetivo:** encontrar la mejor apuesta del dado probando a mano, ver que los
puntos dibujan una parábola con el fondo en 3,5 (la media) y que el error que
queda ahí es 2,92 (la varianza). Sorpresa: la mejor apuesta no sale nunca.

**Qué hace falta saber antes:** escena 01; capítulo 7 (media 3,5 y varianza
2,92 del dado).

**Visual:**
- Apuesta «3»: una fila con las seis caras y debajo los cuadrados de los
  errores «4 · 1 · 0 · 1 · 4 · 9»; «19/6 ≈ 3,17».
- Apuesta «4»: la misma fila al revés, «19/6 ≈ 3,17». Apuesta «1»: «0 · 1 · 4 ·
  9 · 16 · 25 → 55/6 ≈ 9,17».
- Pausa con «¿3,5?»; luego «6,25 · 2,25 · 0,25 · 0,25 · 2,25 · 6,25 → 17,5/6 ≈ 2,92».
- Unos ejes (apuesta, error); cada punto cae en su sitio y se traza la U.
  El vértice: «3,5 = media», «2,92 = varianza».
- Un dado que gira y nunca muestra «3,5».

## Narración

<!-- b1 -->
Probemos a apostar tres. Si sale uno, el error es menos dos, y su cuadrado es cuatro. Si sale dos, el cuadrado es uno, y si sale tres, es cero. Con el cuatro vuelve a ser uno, con el cinco es cuatro, y con el seis es nueve. Cada cara tiene probabilidad un sexto, así que el error cuadrático medio es la suma, que da diecinueve, dividida entre seis, o sea, tres coma uno siete.

<!-- b2 -->
Ahora apostemos cuatro. Las cuentas son las mismas, pero al revés, porque el seis queda a dos y el uno queda a tres. Vuelve a dar diecinueve sextos, que son tres coma uno siete, así que hay empate. Y si apostamos uno, el uno sale gratis, pero el seis cuesta veinticinco, y el error medio sube a nueve coma uno siete. Apostar a un extremo
es mala idea.

<!-- b3 -->
Si tres y cuatro empatan, quizá lo mejor esté en medio. Piénsalo un momento
antes de seguir. Apostemos tres coma cinco. Ahora los cuadrados son seis coma veinticinco, dos coma veinticinco y cero coma veinticinco, y cada uno sale dos veces. Suman diecisiete coma cinco, y entre seis son dos coma nueve dos. Es más bajo que todos los anteriores.

<!-- b4 -->
Pongamos los resultados en un dibujo. En el eje horizontal se encuentra la apuesta, y en el eje vertical, el error cuadrático medio. Los puntos forman una parábola, una curva en forma
de U, y su punto más bajo está justo en tres coma cinco. Y tres coma cinco es
la media del dado, que calculamos en el capítulo siete.

<!-- b5 -->
Y aquí está la sorpresa, y es que la mejor apuesta es un número que el dado no saca nunca. No buscamos acertar, sino equivocarnos lo menos posible en promedio. Y
el error que queda en el fondo, dos coma nueve dos, también te sonará, porque es la varianza del dado. ¿Casualidad? Vamos a demostrar que no.

---

# Escena 03 — CompletarElCuadrado

**Objetivo:** demostrar para cualquier variable que la mejor apuesta es la
media y que el error mínimo es la varianza, completando el cuadrado paso a
paso; leer el resultado como «un suelo más una multa»; comprobarlo con el dado.

**Qué hace falta saber antes:** escena 02; capítulo 7 (linealidad de la
esperanza, varianza, desarrollo de (a + b)²).

**Visual:** (como `c8p-completar-cuadrado.svg`)
- «E[(Y − ŷ)²]»; dentro del paréntesis aparece «− μ + μ» en ámbar.
- Renglones, uno por regla:
  «Y − ŷ = (Y − μ) + (μ − ŷ)»;
  «(…)² = (Y − μ)² + 2(Y − μ)(μ − ŷ) + (μ − ŷ)²»;
  «E[(Y − μ)²] = σ²», «E[Y − μ] = 0» (el término cruzado se tacha),
  «(μ − ŷ)²» se queda.
- Resultado en caja: «E[(Y − ŷ)²] = σ² + (μ − ŷ)²». Debajo de σ², una losa
  gris «suelo»; debajo del cuadrado, «multa ≥ 0».
- La parábola de la escena 02 con su suelo en 2,92 dibujado como una línea.
- Comprobación: «2,92 + (3,5 − 3)² = 2,92 + 0,25 = 3,17» ✓.

## Narración

<!-- b1 -->
Hagámoslo en general, para cualquier variable i griega de media mu y varianza
sigma cuadrado. Queremos el número i griega sombrero que haga más pequeña la media de i griega menos i griega sombrero, al cuadrado. El truco consiste en sumar y restar la media dentro del paréntesis. No cambia nada, pero parte el error en dos trozos.

<!-- b2 -->
El primer trozo es i griega menos mu, esto es: cuánto se aparta la variable de su media. El segundo es mu menos i griega sombrero, o sea: cuánto se aparta nuestra apuesta de la media. Elevamos al cuadrado la suma de los dos, resolvemos el cuadrado de un binomio: el primero al cuadrado, más dos veces el producto, más el segundo al cuadrado.

<!-- b3 -->
Ahora tomamos la media de cada término y, por linealidad, sumamos los resultados. La media del primero
es la varianza. En el término cruzado, mu menos i griega sombrero es un número fijo, así que sale fuera, y lo que queda dentro es la media de i griega menos mu, que es
cero. El término cruzado desaparece. Y el último es un número fijo al cuadrado, así que se queda como está.

<!-- b4 -->
Y este es el resultado. El error cuadrático medio es la varianza, más la distancia entre la
apuesta y la media, al cuadrado. El primer término no depende de lo que apuestes, así que es un suelo que no puedes perforar. El segundo es una multa que nunca
es negativa y que vale cero solo si apuestas la media. Así que la mejor apuesta
es la media, y el error que queda es la varianza.

<!-- b5 -->
Comprobémoslo con el dado. Si apostamos tres, tenemos la varianza, dos coma nueve dos, más tres coma cinco menos tres, al cuadrado, que es cero coma veinticinco. Da tres coma uno siete, lo mismo que con la cuenta larga. Y de aquí sale una lectura que usaremos mucho. La varianza es la incertidumbre que queda cuando ya has hecho lo mejor que podías
sin mirar nada más.

---

# Escena 04 — OtrasFormasDeFallar

**Objetivo:** ver que «la mejor apuesta» depende de cómo se mide el error: con
el cuadrado sale la media, con el tamaño del error sale la mediana, y con
acertar o fallar sale la moda. Comprobarlo con un ejemplo asimétrico. Sembrar
el capítulo 9 (acertar o fallar = decidir) y justificar por qué nos quedamos con
el cuadrado.

**Qué hace falta saber antes:** escena 03; capítulo 7 (distribución discreta,
media).

**Visual:** (idea de `c8p-costos.svg`)
- Una centralita con un teléfono; barras de probabilidad sobre 0, 1, 2 y 10:
  «0,4 · 0,3 · 0,2 · 0,1».
- Cuadrado: «0 · 0,4 + 1 · 0,3 + 2 · 0,2 + 10 · 0,1 = 1,7»; un triángulo-fiel
  ámbar en 1,7. La barra del 10 tira de él (flecha).
- Tamaño del error: la masa partida a la mitad; marca verde en «1 = mediana».
  «apostar 1 → 1,5», «apostar 1,7 → 1,78».
- Acertar o fallar: la barra más alta se ilumina; «0 = moda, acierta 40 %»;
  «1,7 → acierta 0 %».
- Tres casillas: «cuadrado → media», «tamaño → mediana», «acierto → moda». La
  tercera con una etiqueta «capítulo 9».

## Narración

<!-- b1 -->
¿Por qué el cuadrado y no otra forma de medir el error? Porque es una
elección, y cada elección da otra respuesta. Veámoslo con un ejemplo. Cuentas
las llamadas que entran en una centralita en un minuto. Entran cero llamadas el cuarenta por ciento de las veces, una llamada el treinta, dos el veinte, y diez de golpe el diez por ciento restante.

<!-- b2 -->
Con el error al cuadrado ya lo sabemos, la mejor apuesta es la media. Para calcularla hacemos cero por cero coma cuatro, más uno por cero coma tres, más dos por cero coma dos, más diez por cero coma uno, y sale uno coma siete llamadas. Ese diez raro tira de la media
hacia arriba, porque el cuadrado castiga mucho fallar por nueve.

<!-- b3 -->
Si en cambio el error se mide por su tamaño, sin cuadrado, la mejor apuesta es la mediana, que es el valor que deja la mitad de la probabilidad a cada lado. Aquí es
una llamada. Si apostamos uno, el error medio es uno coma cinco, pero si apostamos uno coma siete, sube a uno coma siete ocho. Con esta medida, el diez raro pesa
mucho menos.

<!-- b4 -->
Y si lo único que cuenta es acertar o fallar, sin importar por cuánto, la
mejor apuesta es el valor más probable, que es la moda, o sea, cero llamadas, que acierta el
cuarenta por ciento de las veces. Apostar uno coma siete no acertaría nunca.
Son tres formas de medir el error y tres respuestas, que son la media, la mediana y la moda.

<!-- b5 -->
La última, acertar o fallar, es la que se usa para decidir, y la retomaremos en
el capítulo siguiente. En este nos quedamos con el cuadrado, por tres motivos. Castiga los errores grandes, las cuentas salen limpias y, como veremos,
convierte la estimación en geometría. Pero antes viene lo interesante. ¿Qué pasa
cuando, además, puedes mirar algo?

---

# Escena 05 — LaAlturaOtraVez

**Objetivo:** ver con el ejemplo de la altura que mirar un dato (el grupo)
achica el error: apostar la media del grupo, con el error de cada grupo, y en
promedio 41,2 en vez de 81,76. Pagar la promesa de la escena 20 del capítulo 7:
el error del mejor estimador es el primer trozo de la varianza total.

**Qué hace falta saber antes:** escenas 02 y 03 (mejor apuesta = media, error
= varianza); capítulo 7, escenas 19 y 20 (la altura, la ley de la varianza total).

**Visual:**
- Las dos campanas de la altura del capítulo 7, el mismo dibujo: hombres
  «175 cm, σ = 7, 40 %», mujeres «162 cm, σ = 6, 60 %». Una puerta y una silueta.
- Sin datos: una campana ancha de toda la población; «ŷ = 167,2», «error = 81,76
  (σ ≈ 9 cm)».
- Una tarjeta «es mujer»: la campana de los hombres se apaga; «ŷ = 162»,
  «error = 6² = 36». Tarjeta «es hombre»: «ŷ = 175», «error = 7² = 49».
- Promedio: «0,4 · 49 + 0,6 · 36 = 19,6 + 21,6 = 41,2». Una barra de 81,76 que
  se encoge a 41,2.
- Las dos barras apiladas de la escena 20 del capítulo 7: «41,2 + 40,56 = 81,76»;
  el trozo de 41,2 con el rótulo «error del mejor estimador» y un tilde de
  «promesa cumplida».

## Narración

<!-- b1 -->
Recuerda la población del capítulo siete: el cuarenta por ciento son hombres,
con una altura media de ciento setenta y cinco centímetros, y el sesenta por
ciento son mujeres, con ciento sesenta y dos. Entra alguien por la puerta y
tienes que adivinar su altura. Si no sabes nada de esa persona, ya sabes qué
hacer.

<!-- b2 -->
Apuestas la media de toda la población: ciento sesenta y siete coma dos. Y el
error cuadrático medio es la varianza de la altura, que calculamos entonces:
ochenta y uno coma setenta y seis, una desviación típica de unos nueve
centímetros. Ahora cambiemos una cosa: antes de apostar, alguien te dice si es
un hombre o una mujer.

<!-- b3 -->
Si te dicen «es una mujer», el mundo se achica: ya solo cuentan las mujeres.
Dentro de ese grupo repites lo de siempre: apuestas su media, ciento sesenta y
dos, y el error es la varianza de ese grupo, seis al cuadrado, treinta y seis.
Si te dicen «es un hombre», apuestas ciento setenta y cinco, con un error de
siete al cuadrado, cuarenta y nueve.

<!-- b4 -->
¿Y en promedio, sin saber todavía quién entrará? Cuatro de cada diez veces
tendrás un error de cuarenta y nueve, y seis de cada diez, uno de treinta y
seis. Cero coma cuatro por cuarenta y nueve, más cero coma seis por treinta y
seis: cuarenta y uno coma dos. Saber el grupo ha reducido el error a la mitad.

<!-- b5 -->
Y ese cuarenta y uno coma dos no es un número nuevo. Es el primer trozo de la
ley de la varianza total: lo que el grupo no explica. En el capítulo siete
prometimos que el error del mejor estimador sería exactamente ese trozo, y aquí
está. La otra mitad, cuarenta coma cinco seis, es justo lo que nos ha ahorrado
saber el grupo.

---

# Escena 06 — MediaCondicional

**Objetivo:** generalizar: observado X = x, la mejor apuesta es la media
condicional y su error es la varianza condicional. Aplicarlo al canal de bits
con la tabla (0,79 y 0,045, errores 0,16 y 0,04). Sembrar que 0,79 no es un bit.

**Qué hace falta saber antes:** escena 05; capítulo 7, escenas 17 y 19 (tabla
conjunta del canal, esperanza condicional por columnas).

**Visual:**
- Una nube de puntos; una rebanada vertical en «X = x» se ilumina y el resto se
  apaga. Dentro de la rebanada, su centro: «E[Y | X = x]» y su ancho:
  «Var(Y | X = x)».
- La tabla del canal del capítulo 7 (el mismo dibujo): «0,63 · 0,07 / 0,03 ·
  0,27», columnas «recibido 0» y «recibido 1».
- Columna «recibido 1» resaltada: «P(enviado 1) = 0,27/0,34 ≈ 0,79» → «ŝ = 0,79».
- Columna «recibido 0»: «0,03/0,66 ≈ 0,045» → «ŝ = 0,045».
- La varianza de un bit: «p(1 − p)». «0,79 · 0,21 ≈ 0,16», «0,045 · 0,955 ≈ 0,04».
- Una moneda con «0» y «1» y, entre medias, «0,79» con un «?» ámbar.

## Narración

<!-- b1 -->
Lo que acabamos de hacer funciona siempre. Observas una variable, equis, y
quieres adivinar otra, i griega. Cuando ves que equis vale un valor concreto,
el mundo se achica a los casos donde equis vale eso. Dentro de ese mundo
pequeño, el problema es el de siempre: apuesta la media, y el error será la
varianza.

<!-- b2 -->
Solo que ahora son la media y la varianza dentro del mundo achicado: la
esperanza condicional de i griega dado equis, y la varianza condicional. Es la
regla del dado, aplicada rebanada a rebanada. Ningún cálculo nuevo: la misma
idea, repetida para cada valor que pueda tomar lo que observas.

<!-- b3 -->
Volvamos al canal que confunde bits. Se envía un cero con probabilidad cero
coma siete y un uno con cero coma tres, y el canal cambia el bit una de cada
diez veces. Si recibes un uno, la columna de recibir uno dice que se envió un
uno con probabilidad cero coma setenta y nueve. Esa es la media de lo enviado
en esa columna, y esa es la apuesta.

<!-- b4 -->
Si recibes un cero, en la otra columna se envió un uno con probabilidad cero
coma cero cuatro cinco: apuestas eso. Y los errores son las varianzas de cada
columna. Para algo que vale uno con probabilidad pe y cero si no, la varianza
es pe por uno menos pe. Cero coma uno seis en la primera columna, y cero coma
cero cuatro en la segunda.

<!-- b5 -->
Fíjate en algo raro: la mejor apuesta, cero coma setenta y nueve, no es un bit.
Ni cero ni uno. Con el error al cuadrado no se busca acertar, sino quedarse
cerca, y eso a veces cae entre medias. Si lo que necesitas es elegir entre cero
y uno, eso ya es decidir, y es el tema del capítulo siguiente. Guárdate esta
pregunta.

---

# Escena 07 — ElEstimadorEsAleatorio

**Objetivo:** distinguir la estimación ya calculada (un número) del estimador
antes de mirar (una variable aleatoria); calcular su distribución y su media
(la torre: insesgado); calcular el error total (0,084 contra 0,21) y ver por
qué la media condicional también es la mejor en promedio («las columnas no se
estorban»). Nombrar el estimador de mínimo error cuadrático medio.

**Qué hace falta saber antes:** escena 06; capítulo 7, escena 19 (la torre).

**Visual:**
- «f(3)» → «un número»; «f(·)» → «una regla».
- Una regla con dos casillas: «recibo 1 → 0,79», «recibo 0 → 0,045». Encima,
  «Ŝ» con mayúscula; dos barras de probabilidad «0,34» y «0,66».
- Media: «0,34 · 0,79 + 0,66 · 0,045 = 0,27 + 0,03 = 0,30 = E[S]» y una balanza
  en equilibrio.
- Error total: «0,34 · 0,16 + 0,66 · 0,04 ≈ 0,084» frente a «σ_S² = 0,21»; una
  barra que se encoge un 60 %.
- Las dos columnas, cada una con su mínimo marcado, separadas por una pared:
  «mejorar una no empeora la otra».
- Caja final: «Ŷ = E[Y | X]», «error = E[Var(Y | X)]», con la sigla «MMSE» al lado.

## Narración

<!-- b1 -->
Hay una diferencia sutil entre dos cosas que se escriben casi igual. Una
función evaluada en tres, efe de tres, es un número. Una función sin evaluar,
efe de un punto que todavía no conoces, es una regla. Con la estimación pasa lo
mismo. Si ya recibiste un uno, la apuesta es un número: cero coma setenta y
nueve.

<!-- b2 -->
Pero antes de recibir nada, la apuesta es una regla: si llega un uno, cero coma
setenta y nueve; si llega un cero, cero coma cero cuatro cinco. Y como lo que
llega es aleatorio, la apuesta también lo es. Es una variable aleatoria, con su
propia distribución: vale cero coma setenta y nueve con probabilidad cero coma
treinta y cuatro, y cero coma cero cuatro cinco con cero coma sesenta y seis.

<!-- b3 -->
Como toda variable aleatoria, tiene media. Cero coma treinta y cuatro por cero
coma setenta y nueve, más cero coma sesenta y seis por cero coma cero cuatro
cinco: cero coma tres. Es la media de lo enviado. No es casualidad: es la
propiedad de la torre del capítulo siete. Quiere decir que la estimación, en
promedio, no se desvía hacia ningún lado.

<!-- b4 -->
También tiene un error total, promediando sobre lo que llegue. Cero coma
treinta y cuatro por cero coma uno seis, más cero coma sesenta y seis por cero
coma cero cuatro: cero coma cero ocho cuatro. Sin mirar el canal, el error
sería la varianza de lo enviado, cero coma dos uno. Mirar lo recibido lo ha
reducido un sesenta por ciento.

<!-- b5 -->
¿Podría otra regla conseguir un error total más pequeño? No. El error total es
un promedio de los errores de cada columna, y cada uno ya es el más pequeño
posible. Las columnas no se estorban: mejorar una no empeora la otra. Así que
la media condicional es la mejor regla, y su error es la media de las varianzas
condicionales. Se llama estimador de mínimo error cuadrático medio.

---

# Escena 08 — ElErrorSinPatron

**Objetivo:** presentar la regla de ortogonalidad con números: dentro de cada
columna el error tiene media cero, así que su producto con cualquier función de
lo recibido tiene media cero. Leerla como «el error no tiene patrón: ya se usó
toda la información». Anunciar que se convertirá en un dibujo.

**Qué hace falta saber antes:** escenas 06 y 07; capítulo 7, escena 26
(ortogonal = esperanza del producto cero = perpendicular).

**Visual:**
- Columna «recibido 1»: dos casillas, «enviado 1: error +0,21, prob. 0,27» y
  «enviado 0: error −0,79, prob. 0,07».
- La cuenta: «0,27 · 0,21 − 0,07 · 0,79 = 0,056 − 0,056 = 0». Una balanza que
  queda horizontal. Lo mismo, más rápido, en la otra columna.
- «g(R)»: un número cualquiera escrito sobre cada columna (por ejemplo «5» y
  «−2»); «E[e · g(R)] = 0,34 · 5 · 0 + 0,66 · (−2) · 0 = 0».
- Dos flechas perpendiculares con el rótulo «E[e · g(X)] = 0: ortogonales».
- Un error con patrón (todos los errores de una columna por encima de cero) y
  una flecha «corregir» que lo baja: «si hay patrón, se puede mejorar».

## Narración

<!-- b1 -->
El mejor estimador tiene una propiedad que lo explica todo, y se ve en el
canal. Mira la columna de recibir un uno. Cuando se envió un uno, el error es
uno menos cero coma setenta y nueve: cero coma dos uno. Cuando se envió un
cero, es menos cero coma setenta y nueve. Unas veces nos quedamos cortos y
otras nos pasamos.

<!-- b2 -->
¿Cuánto vale el error en promedio dentro de esa columna? Cero coma veintisiete
por cero coma dos uno, menos cero coma cero siete por cero coma setenta y
nueve. Cero coma cero cinco seis menos cero coma cero cinco seis: cero. Y en la
otra columna pasa lo mismo. Dentro de cada columna, el error se compensa
exactamente.

<!-- b3 -->
Eso tiene una consecuencia fuerte. Toma cualquier función de lo recibido: un
número para la columna del uno y otro para la del cero. Multiplícala por el
error y haz la media. Dentro de cada columna, ese número es fijo y sale fuera,
y lo que queda es la media del error en la columna, que es cero. Así que la
media del producto es cero, sea cual sea la función.

<!-- b4 -->
En el capítulo siete, dos variables cuya esperanza del producto vale cero eran
ortogonales: flechas perpendiculares. Así que el error del mejor estimador es
ortogonal a cualquier función de lo observado. Se llama regla de
ortogonalidad, y es la idea más importante del capítulo.

<!-- b5 -->
Léela así: el error no tiene ningún patrón que dependa del dato. Si lo tuviera,
si por ejemplo nos quedáramos cortos siempre que llega un uno, bastaría con
sumar algo en esa columna para mejorar. Que el error sea ortogonal a todo lo
que se puede calcular con el dato significa que ya le hemos sacado toda la
información. Esta perpendicular volverá convertida en un dibujo.

---

# Escena 09 — LaCarpa

**Objetivo:** ver que la media condicional puede ser una curva y que necesita
la distribución entera; con la carpa, comparar la curva (error 1/24) con la
mejor recta, que por simetría es horizontal (ρ = 0, error 1/18). Proponer el
trato: conformarse con la mejor recta, que solo pide medias, varianzas y
covarianzas.

**Qué hace falta saber antes:** escenas 06 y 07; capítulo 7 (uniforme y su
varianza ancho²/12; escena 23, la parábola: covarianza cero por simetría).

**Visual:**
- Un triángulo con forma de carpa (base de 0 a 2, pico en (1, 1)); caen puntos
  uniformes dentro.
- Rebanada en «x = 0,5»: un segmento de 0 a 0,5 con su centro «0,25». Rebanada
  en «x = 1»: de 0 a 1, centro «0,5».
- Los centros de todas las rebanadas dibujan una carpa más baja (altura ½), en
  ámbar: «E[Y | X = x]». «error = 1/24 ≈ 0,042».
- Mitad izquierda con flecha que sube y mitad derecha con flecha que baja; se
  cancelan: «σ_XY = 0». La recta horizontal en «⅓»: «error = 1/18 ≈ 0,056».
- Dos barras: «curva 0,042», «recta 0,056». Un apretón de manos: «el trato:
  solo rectas → solo μ, σ², σ_XY».

## Narración

<!-- b1 -->
La media condicional es la mejor apuesta, pero tiene una pega, y es que para calcularla hay que conocer la distribución conjunta entera. Y a veces la regla
que sale es una curva. Mira este ejemplo. Un punto cae al azar, con la misma
probabilidad en cualquier sitio, dentro de un triángulo con forma de carpa, cuya base va de cero a dos y cuyo pico, en equis igual a uno, tiene altura uno.

<!-- b2 -->
Observamos su posición horizontal, equis, y queremos adivinar la vertical, i
griega. Corta la carpa en equis igual a cero coma cinco y verás que la rebanada va de cero a cero coma cinco. Como el punto cae con la misma probabilidad a cualquier
altura, la mejor apuesta es el centro, cero coma veinticinco. En equis igual a
uno, la rebanada llega hasta uno: apuesta cero coma cinco.

<!-- b3 -->
Uniendo los centros de todas las rebanadas sale otra carpa, de la mitad de
altura. Esa es la media condicional, y no es una recta, porque sube y luego baja. Cada
rebanada es una uniforme, con varianza igual a su ancho al cuadrado entre
doce, y el promedio de esas varianzas, que es una integral, da un veinticuatroavo, que es aproximadamente cero coma cero cuatro dos.

<!-- b4 -->
Ahora, la covarianza. En la mitad izquierda, cuando equis sube, i griega
tiende a subir; en la derecha, tiende a bajar. Como en la parábola del
capítulo siete, las dos mitades se cancelan y la covarianza es cero. Si solo
pudiéramos usar una recta, la mejor sería horizontal, a la altura de la media,
un tercio. Y su error, un dieciochoavo, que son cero coma cero cinco seis, un tercio más.

<!-- b5 -->
La curva gana. Pero para dibujarla hace falta toda la distribución, y en la
práctica casi nunca la tenemos, porque lo que tenemos son medias, varianzas y covarianzas. Así
que hagamos un trato. Nos conformamos con la mejor recta, que solo pide esos
pocos números, a cambio de perder algo cuando la relación es curva. Es el
estimador lineal óptimo.

---

# Escena 10 — ElTermometro

**Objetivo:** buscar la mejor recta con un caso concreto, el termómetro: fijar
b (la recta arranca de la media), probar h = 0 (error 4) y h = 1 (error 1),
deducir la parábola 4 − 8h + 5h² paso a paso y ver que el fondo está en 0,8
con error 0,8: la apuesta es 22,4, no 23.

**Qué hace falta saber antes:** escena 09; escena 03 (desarrollar el cuadrado
y tomar medias); capítulo 7 (covarianza; varianza de una suma de
independientes).

**Visual:**
- Un termómetro (`termometro()`) en una sala; «temperatura: μ = 20, σ² = 4»
  (azul), «ruido: σ² = 1» (magenta), «lectura = temperatura + ruido» (cian).
  La lectura marca «23».
- «ŷ = h · x + b». Debajo: «b = 20 − 20h» → «ŷ = 20 + h (x − 20)».
- Dos tarjetas: «h = 0 → ŷ = 20, error 4» y «h = 1 → ŷ = 23, error 1».
- Renglones: «E[(ỹ − h x̃)²] = E[ỹ²] − 2h E[ỹ x̃] + h² E[x̃²]»; «E[ỹ²] = 4»;
  «E[ỹ x̃] = 4 + 0 = 4»; «E[x̃²] = 4 + 1 = 5».
- La parábola `ParabolaJ`: «J(h) = 4 − 8h + 5h²», con puntos en h = 0 (4) y
  h = 1 (1), y el vértice «h = 0,8, J = 0,8».
- «ŷ = 20 + 0,8 · 3 = 22,4».

## Narración

<!-- b1 -->
Probemos el trato con un ejemplo que nos acompañará mucho tiempo. La
temperatura de una sala tiene una media de veinte grados y una varianza de cuatro, de modo que se aparta unos dos grados, arriba o abajo. La medimos con un
termómetro que suma su propio ruido, de media cero y varianza uno, sin ninguna
relación con la temperatura. El termómetro marca veintitrés. ¿Qué temperatura
hace?

<!-- b2 -->
Buscamos la apuesta entre las rectas de la forma hache por lo que marca el termómetro,
más un número fijo, be. Empecemos por be. Sea cual sea hache, conviene que en
promedio no nos desviemos, y eso fija be en veinte menos veinte hache. Así la
recta queda veinte, más hache por lo que la lectura se aparta de veinte.
Arrancamos de la media y corregimos.

<!-- b3 -->
Queda elegir hache. Dos opciones extremas. Con hache igual a cero, ignoramos
el termómetro y apostamos veinte, así que el error es la varianza de la temperatura,
cuatro. Con hache igual a uno, nos lo creemos a ciegas y apostamos veintitrés, así que el error es el del ruido, uno. Mucho mejor. Pero, ¿y si lo mejor está entre
medias?

<!-- b4 -->
Calculemos el error para cualquier hache. Con todo centrado, es la media de la
temperatura menos hache por la lectura, al cuadrado. Desarrollamos el cuadrado
y tomamos la media de cada término. La de la temperatura al cuadrado es
cuatro. La de la temperatura por la lectura también es cuatro, porque el ruido
no tiene nada que ver con la temperatura. Y la de la lectura al cuadrado es cuatro más uno, es decir, cinco.

<!-- b5 -->
El error queda cuatro, menos ocho hache, más cinco hache al cuadrado, que es otra parábola. Con hache igual a cero da cuatro; con hache igual a uno, uno. Y su
punto más bajo, que enseguida calcularemos, está en hache igual a cero coma
ocho, donde el error baja a cero coma ocho. La mejor apuesta no es veintitrés, sino veinte más cero coma ocho por tres, que da veintidós coma cuatro.

---

# Escena 11 — LaFormulaDeLaRecta

**Objetivo:** explicar la derivada como pendiente y usarla para encontrar el
fondo de la parábola del termómetro; repetir la cuenta con letras para llegar a
h = σ_XY/σ_X², a la recta ŷ = μ_Y + ρ(σ_Y/σ_X)(x − μ_X) y al error
σ_Y²(1 − ρ²), deducido paso a paso; comprobar con el termómetro.

**Qué hace falta saber antes:** escena 10; capítulo 7 (σ_XY = ρ σ_X σ_Y).

**Visual:**
- La parábola con una recta tangente que se desliza: pendiente negativa a la
  izquierda, positiva a la derecha, horizontal en el fondo: «pendiente =
  derivada».
- «d/dh (4 − 8h + 5h²) = −8 + 10h = 0 → h = 0,8»; «J(0,8) = 4 − 6,4 + 3,2 = 0,8».
- Con letras: «J(h) = σ_Y² − 2h σ_XY + h² σ_X²»; «−2σ_XY + 2h σ_X² = 0»;
  «h = σ_XY / σ_X²». Al lado, en pequeño, «4/5 = 0,8».
- La recta por piezas: «ŷ = μ_Y + (σ_XY / σ_X²)(x − μ_X)»; luego
  «σ_XY / σ_X² = ρ σ_Y / σ_X».
- El error: «σ_Y² − 2 σ_XY²/σ_X² + σ_XY²/σ_X² = σ_Y² − σ_XY²/σ_X² = σ_Y²(1 − ρ²)».
- Comprobación: «ρ² = 4² / (4 · 5) = 0,8», «4 · (1 − 0,8) = 0,8» ✓. Rótulo
  «LMMSE» en pantalla.

## Narración

<!-- b1 -->
¿Cómo se encuentra el punto más bajo de una parábola sin probar valores? Con la
pendiente. En cada punto de una curva, la pendiente dice cuánto sube por cada
paso hacia la derecha, y eso es la derivada. Bajando por la izquierda, la
pendiente es negativa; subiendo por la derecha, positiva. Y en el fondo, justo
entre las dos, es cero.

<!-- b2 -->
La derivada de cuatro menos ocho hache más cinco hache al cuadrado es menos
ocho más diez hache. Igualada a cero, hache vale ocho décimos, o sea, cero coma ocho.
Y el error ahí es cuatro, menos seis coma cuatro, más tres coma dos, que da cero coma ocho. Ahora, lo mismo con letras, para cualquier pareja de variables.

<!-- b3 -->
El error, centrado, es la varianza de i griega, menos dos hache por la
covarianza, más hache al cuadrado por la varianza de equis. Su pendiente es
menos dos veces la covarianza, más dos hache por la varianza de equis.
Igualada a cero, hache es la covarianza dividida entre la varianza de equis. En
el termómetro, cuatro entre cinco, es decir, cero coma ocho.

<!-- b4 -->
Así que la mejor recta se lee como la media de i griega, más la covarianza
entre la varianza de equis, por lo que equis se aparta de su media. Y como la
covarianza es rho por las dos desviaciones típicas, el factor también se
escribe rho, por sigma de i griega, entre sigma de equis.

<!-- b5 -->
Falta el error. Metiendo ese hache en la parábola, los dos últimos términos se
juntan en menos la covarianza al cuadrado entre la varianza de equis. Sacando
factor común la varianza de i griega, queda la varianza por uno menos rho al
cuadrado. En el termómetro, rho al cuadrado es dieciséis entre veinte, cero coma
ocho, y cuatro por cero coma dos da cero coma ocho. Coincide.

---

# Escena 12 — LeerLaRecta

**Objetivo:** leer la fórmula de la recta: arranca de la media y corrige según
ρ; casos ρ = 0 (la carpa) y ρ = ±1; ρ² como la parte de la varianza que el dato
explica; por qué la apuesta tira hacia la media (22,4 y no 23). Advertir la
trampa: la recta para adivinar X desde Y no es la inversa (factor 1, no 1,25).

**Qué hace falta saber antes:** escenas 09 a 11.

**Visual:**
- La recta sobre la nube del termómetro, con un deslizador de ρ: en 0 se queda
  horizontal (y aparece un mini dibujo de la carpa), en 1 la nube es una recta y
  el error «0».
- Una barra de 4 partida en «3,2 (80 %) explicado» y «0,8 sin explicar».
- La lectura «23» (3 por encima de la media) y la apuesta «22,4» (2,4 por
  encima): una flecha corta que tira hacia 20. Dos causas posibles de una
  lectura alta: un sol (calor de verdad) y el ruido en magenta.
- La pregunta al revés: «temperatura → lectura». Tachado «1/0,8 = 1,25»;
  «σ_XY / σ_Y² = 4/4 = 1» → «x̂ = y».
- Dos rectas distintas sobre la misma nube; una con los errores dibujados en
  vertical y la otra en horizontal.

## Narración

<!-- b1 -->
Leamos la fórmula con calma, porque dice mucho. Arranca de la media de lo que
quieres adivinar y corrige según cuánto se aparta el dato de la suya. El tamaño
de la corrección depende de rho. Si rho vale cero, no corrige nada y la recta es horizontal, a la altura de la media. Es lo que le pasaba a la carpa.

<!-- b2 -->
Si rho vale uno o menos uno, la nube es una recta exacta, y el error, la
varianza por uno menos uno, es cero, así que el dato lo dice todo. Y entre medias, rho
al cuadrado es la parte de la varianza que el dato consigue explicar. En el
termómetro, un ochenta por ciento. El veinte por ciento restante, cero coma
ocho de cuatro, se queda sin explicar.

<!-- b3 -->
Fíjate en el veintidós coma cuatro. El termómetro marcaba veintitrés, tres por
encima de la media, y la apuesta solo sube dos coma cuatro. ¿Por qué no fiarse
del todo? Porque una lectura alta puede venir de calor de verdad o de ruido
hacia arriba. La fórmula reparte la diferencia, y por eso siempre tira un poco
hacia la media.

<!-- b4 -->
Ahora, una trampa. Cambiemos la pregunta y, sabiendo la temperatura de verdad, adivinemos qué marcará el termómetro. Si fuera la misma recta al revés, el factor
sería uno entre cero coma ocho, es decir, uno coma veinticinco. Pero la fórmula dice
covarianza, cuatro, entre la varianza de lo que observas, ahora la temperatura,
cuatro. Uno. La apuesta es la temperatura misma, y tiene sentido, porque el ruido es igual de probable hacia arriba que hacia abajo.

<!-- b5 -->
Así que sobre la misma nube hay dos rectas distintas, la que adivina i griega a
partir de equis y la que adivina equis a partir de i griega. La primera mide
los errores en vertical y la segunda, en horizontal. Solo coinciden cuando rho
vale uno o menos uno. Y para entender por qué todo esto funciona, toca volver a
las flechas del capítulo siete.

---

# Escena 13 — LaSombra

**Objetivo:** dibujar el termómetro como flechas (largos 2 y √5, producto
escalar 4, ángulo ≈ 27°), ver que estimar con h·x es elegir un punto de la recta
de la lectura, y que el más cercano es el pie de la perpendicular: la
proyección. Calcular su largo y recuperar h = 0,8 sin derivar.

**Qué hace falta saber antes:** escenas 10 y 11; capítulo 7, escenas 25 a 27
(flechas: largo = desviación típica, producto escalar = covarianza, coseno = ρ).

**Visual:** (como `c8p-proyeccion.svg`; el mismo dibujo que usan los capítulos
10 y 12, `flechas_xy`)
- Flecha de la temperatura (azul, largo «2») y flecha de la lectura (cian,
  largo «√5 ≈ 2,24»). «producto escalar = 4», «cos θ = 4 / (2 · √5) ≈ 0,89»,
  arco «≈ 27°».
- La recta que sigue la dirección de la lectura (punteada); un punto ámbar que
  se desliza por ella: «h · x». Desde la punta de la temperatura, un segmento
  rojo hasta el punto: «error»; su largo cambia al deslizar.
- Un punto y una recta del colegio con varios segmentos; el perpendicular es el
  más corto. Un foco de luz arriba: la sombra.
- El punto se detiene en el pie de la perpendicular, con el cuadradito del
  ángulo recto. «sombra = 2 · 0,89 ≈ 1,79»; «h = 1,79 / 2,24 = 0,8».

## Narración

<!-- b1 -->
En el capítulo siete vimos que las variables centradas se comportan como
flechas. El largo de cada flecha es su desviación típica, su producto escalar
es la covarianza, y el coseno del ángulo entre dos flechas es rho. Dibujemos así
el termómetro. La temperatura es una flecha de largo dos. La lectura, una de
largo raíz de cinco, algo más de dos coma dos.

<!-- b2 -->
Su producto escalar es la covarianza, cuatro. Así que el coseno del ángulo es
cuatro entre dos por raíz de cinco: cero coma ocho nueve. Forman unos
veintisiete grados. Y ahora, la estimación: hache por la lectura es la flecha
de la lectura, estirada o encogida. Todas las opciones están sobre una misma
recta, la que sigue la dirección de la lectura.

<!-- b3 -->
Elegir el mejor hache es elegir el punto de esa recta más cercano a la punta de
la flecha de la temperatura. Porque el error es la flecha que va de la
estimación a la temperatura, y su largo al cuadrado es el error cuadrático
medio. Probemos puntos. Uno muy atrás queda lejos. Uno muy adelante, también.
¿Cuál es el más cercano?

<!-- b4 -->
Es una regla del colegio: la distancia más corta de un punto a una recta es la
perpendicular. El mejor punto es el pie de esa perpendicular. Es como la sombra
de la flecha de la temperatura sobre la recta de la lectura, con la luz
cayendo en ángulo recto. Se llama proyección.

<!-- b5 -->
¿Cuánto mide la sombra? El largo de la flecha por el coseno del ángulo: dos por
cero coma ocho nueve, uno coma siete nueve. Y para saber qué múltiplo de la
lectura es, la dividimos entre el largo de la lectura, raíz de cinco. Da cero
coma ocho. El mismo número que salió de la parábola, ahora sin derivar nada:
solo un dibujo.

---

# Escena 14 — DosCondiciones

**Objetivo:** leer el ángulo recto como la regla de ortogonalidad recortada (el
error ortogonal solo a 1 y al dato, porque la recta solo usa eso); sacar b y h
de esas dos condiciones sin derivar; ver que pendiente cero y ángulo recto son
la misma condición; escribir la fórmula de proyección y leer en ella
h = σ_XY / σ_X².

**Qué hace falta saber antes:** escena 13; escena 08 (regla de ortogonalidad);
escena 10 (b fija la recta en la media).

**Visual:**
- El cuadradito del ángulo recto parpadea: «E[e · x̃] = 0».
- Al lado, la escena 08 en pequeño: «E[e · g(X)] = 0 para toda g» → recortado a
  dos casillas: «1» y «x».
- Condición con 1: «E[e] = 0» → «b = 20 − 20h» (ya visto, tilde).
- Condición con x: «E[(ỹ − h x̃) x̃] = 4 − 5h = 0 → h = 0,8».
- Tres caminos con flechas que llegan al mismo «0,8»: «fondo de la parábola»,
  «pendiente = 0», «ángulo recto». «J′(h) = −2 E[e · x̃]».
- Fórmula de proyección: «proy = (⟨y, x⟩ / ⟨x, x⟩) · x» → «(σ_XY / σ_X²) · x».

## Narración

<!-- b1 -->
Mira el ángulo recto. El error es perpendicular a la flecha de la lectura. Y
perpendicular, para variables, significa que la media de su producto es cero.
Es la regla de ortogonalidad de hace dos episodios, pero recortada: allí el
error era ortogonal a cualquier función del dato; aquí, solo a la lectura. ¿Por
qué solo a ella?

<!-- b2 -->
Porque la recta solo sabe usar dos cosas: la lectura, y un número fijo, el uno
que multiplica a be. Si el error tuviera algo en común con cualquiera de las
dos, la recta podría aprovecharlo. Así que pedimos dos condiciones. Que el
error sea ortogonal al uno, es decir, que su media sea cero. Y que sea ortogonal
a la lectura.

<!-- b3 -->
La primera condición ya la usamos: es la que fijaba be, con la recta
arrancando de la media. La segunda es nueva y da hache sin derivadas. La media
de la temperatura centrada menos hache por la lectura centrada, todo por la
lectura centrada, tiene que ser cero. Por linealidad: cuatro menos cinco hache,
igual a cero. Hache vale cero coma ocho.

<!-- b4 -->
Tres caminos y un solo resultado: el fondo de la parábola, la pendiente igual a
cero y el ángulo recto. No es casualidad. La pendiente de la parábola, escrita
con medias, es menos dos por la media del error por la lectura. Que la
pendiente sea cero y que el error sea perpendicular son la misma condición,
dicha de dos formas.

<!-- b5 -->
Y queda una fórmula de geometría que sirve siempre. La proyección de una flecha
sobre otra es el producto escalar de las dos, dividido entre el largo al
cuadrado de la segunda, por esa segunda flecha. El producto escalar es la
covarianza; el largo al cuadrado, la varianza de equis. El factor hache,
covarianza entre varianza, sale solo, leyendo el dibujo.

---

# Escena 15 — Pitagoras

**Objetivo:** sacar el error por Pitágoras (4 = 3,2 + 0,8) y, en general, como
σ_Y² sen²θ = σ_Y²(1 − ρ²); leer los casos ρ = 1 y ρ = 0 en el dibujo; ver que
la partición «explicado + no explicado» es la misma de la altura (escena 05).

**Qué hace falta saber antes:** escenas 13 y 14; escena 05 (la altura);
capítulo 7, escena 25 (Pitágoras, seno y coseno).

**Visual:**
- El triángulo rectángulo: hipotenusa «temperatura, 2», cateto «sombra, 1,79»,
  cateto «error, ?». Cuadrados dibujados sobre cada lado.
- «2² = 1,79² + error²» → «4 = 3,2 + 0,8» → «error = √0,8 ≈ 0,89».
- En general: «error² = σ_Y² sen²θ = σ_Y² (1 − cos²θ) = σ_Y² (1 − ρ²)».
- Deslizador del ángulo: en 0° el cateto del error se encoge a nada; en 90° la
  sombra es un punto.
- Dos barras lado a lado: «altura: 81,76 = 40,56 + 41,2» y «termómetro: 4 = 3,2
  + 0,8», con los mismos colores para «explicado» y «sin explicar».

## Narración

<!-- b1 -->
Ahora el error. La flecha de la temperatura, la sombra y el error forman un
triángulo rectángulo. La temperatura es la hipotenusa; la sombra y el error,
los catetos. Y Pitágoras dice que la hipotenusa al cuadrado es la suma de los
catetos al cuadrado.

<!-- b2 -->
La hipotenusa al cuadrado es la varianza de la temperatura: cuatro. La sombra
mide uno coma siete nueve, y al cuadrado, tres coma dos. Así que el error al
cuadrado es cuatro menos tres coma dos: cero coma ocho. Otra vez el mismo
número. Y el cateto del error mide raíz de cero coma ocho, unos cero coma nueve
grados.

<!-- b3 -->
En general, el cateto opuesto al ángulo es la hipotenusa por el seno. Al
cuadrado: la varianza por el seno al cuadrado. Y el seno al cuadrado es uno
menos el coseno al cuadrado, es decir, uno menos rho al cuadrado. La fórmula
del error, varianza por uno menos rho al cuadrado, no hay que memorizarla: es el
cateto que le falta a la sombra.

<!-- b4 -->
Los casos extremos se ven en el dibujo. Si las flechas apuntan en la misma
dirección, con rho igual a uno, la sombra es la flecha entera y el error
desaparece. Si son perpendiculares, con rho igual a cero, la sombra es un
punto: la estimación es la media, y el error, la varianza entera. Un dato
perpendicular a lo que buscas no ayuda en nada.

<!-- b5 -->
Y fíjate en el reparto: cuatro es tres coma dos más cero coma ocho. La varianza
de la temperatura se parte en lo que la lectura explica, la sombra, y lo que
no, el error. Es la misma partición que la de la altura: lo que el grupo
explica y lo que no. Allí con medias condicionales, aquí con una recta. En los
dos casos es Pitágoras.

---

# Escena 16 — CuandoLaRectaBasta

**Objetivo:** dejar claro que la media condicional nunca pierde contra la recta
y que empatan en dos casos que importan: cuando el dato solo toma dos valores
(el canal de bits: dos puntos siempre caben en una recta, error 0,084 por las
dos fórmulas) y cuando todo es gaussiano (rebanadas de la elipse = campanas
centradas en la recta, de igual ancho 0,8). Por qué esto justifica los filtros
lineales del resto de la materia.

**Qué hace falta saber antes:** escenas 07, 09, 11 y 15; capítulo 7 (la
gaussiana; escena 23, la excepción gaussiana).

**Visual:**
- Un podio: «media condicional ≥ recta», con la carpa como ejemplo de que gana.
- El canal: dos puntos «(0; 0,045)» y «(1; 0,79)» y la recta que pasa por ambos.
  «0,21 · (1 − ρ²) ≈ 0,21 · 0,40 ≈ 0,084» junto a «0,084» de la escena 07: «=».
- La nube del termómetro como elipse inclinada (como
  `c8p-gaussiano-condicional.svg`). Tres rebanadas verticales giran y se
  convierten en campanas; sus centros caen sobre la recta 0,8 y todas tienen el
  mismo ancho: «Var = 0,8».
- «gaussianas: E[Y | X] = recta» → «LMMSE = MMSE».
- Una caja «filtro lineal» con una flecha hacia «capítulos 10 a 13».

## Narración

<!-- b1 -->
La recta es lo mejor entre las rectas. La media condicional es lo mejor sin
restricciones. Así que la media condicional nunca pierde contra la recta, y a
veces gana, como en la carpa. La pregunta es cuándo empatan: cuándo la recta no
pierde nada. Hay dos casos que nos importan mucho.

<!-- b2 -->
El primero es el canal de bits. Lo recibido solo vale cero o uno, así que la
media condicional son dos puntos: cero coma cero cuatro cinco sobre el cero, y
cero coma setenta y nueve sobre el uno. Por dos puntos siempre pasa una recta.
La mejor regla ya es una recta, y la fórmula lo confirma: cero coma dos uno por
uno menos rho al cuadrado da cero coma cero ocho cuatro, el mismo error de antes.

<!-- b3 -->
El segundo caso es el gaussiano. Si la temperatura y el ruido del termómetro
son gaussianos, la nube de puntos tiene forma de elipse inclinada. Corta la
elipse en rebanadas verticales: cada rebanada es una campana. Sus centros caen
exactamente sobre una recta, la del cero coma ocho. Y todas las campanas tienen
el mismo ancho: varianza cero coma ocho, marque lo que marque el termómetro.

<!-- b4 -->
Es decir, con gaussianas la media condicional ya es una recta, la misma que da
la fórmula. La mejor estimación posible y la mejor estimación lineal son la
misma, y no se pierde nada por usar rectas. Y la varianza de cada rebanada,
cero coma ocho, es justo el error de la recta.

<!-- b5 -->
Esto es lo que permite al resto de la materia trabajar solo con filtros
lineales sin disculparse. El ruido suele ser gaussiano, y entonces lo lineal ya
es lo óptimo. Cuando no lo es, lo lineal sigue siendo lo mejor que se puede
hacer con medias, varianzas y covarianzas. Y ahora, el siguiente paso: ¿qué
pasa si en vez de un termómetro tienes dos?

---

# Escena 17 — DosTermometros

**Objetivo:** estimar con dos mediciones a mano: dos condiciones de
ortogonalidad (una por termómetro), dos ecuaciones, resolverlas por
sustitución (⅔ y ⅙), la apuesta 22,33 y el error ⅔, mejor que cada termómetro
por separado (0,8 y 2).

**Qué hace falta saber antes:** escenas 10 y 14 (la recta y sus condiciones de
ortogonalidad); capítulo 7 (covarianza de sumas de independientes).

**Visual:**
- Dos termómetros: «A: ruido σ² = 1» marca «23»; «B: ruido σ² = 4» marca «22».
- «ŷ = 20 + h_A (x_A − 20) + h_B (x_B − 20)».
- Dos flechas de lectura y el error perpendicular a las dos (dos cuadraditos).
- Covarianzas, cada una con su porqué: «cov(temp., A) = 4», «var(A) = 4 + 1 =
  5», «cov(A, B) = 4 (ven la misma temperatura)», «var(B) = 4 + 4 = 8».
- Las dos ecuaciones: «4 − 5h_A − 4h_B = 0», «4 − 4h_A − 8h_B = 0».
  Sustitución renglón a renglón: «h_A = 1 − 2h_B» → «−1 + 6h_B = 0» →
  «h_B = 1/6», «h_A = 2/3».
- «ŷ = 20 + ⅔ · 3 + ⅙ · 2 ≈ 22,33». «error = 4 − ⅔ · 4 − ⅙ · 4 = ⅔ ≈ 0,67».
- Tres barras: «solo A: 0,8», «solo B: 2», «A y B: 0,67».

## Narración

<!-- b1 -->
Pongamos un segundo termómetro en la sala, más barato que el primero. El
primero, el A, tiene un ruido de varianza uno. El segundo, el B, de varianza
cuatro. Los dos ruidos no tienen nada que ver entre sí ni con la temperatura. A
marca veintitrés y B marca veintidós. ¿Qué temperatura hace?

<!-- b2 -->
La apuesta es ahora veinte, más el peso de A por lo que A se aparta de veinte,
más el peso de B por lo que se aparta B. Dos pesos por elegir. Y la regla es la
de siempre: el error tiene que ser ortogonal a todo lo que usa la estimación.
Usa dos lecturas, así que hay dos condiciones: el error, perpendicular a A y
perpendicular a B.

<!-- b3 -->
Primera condición, con A. La covarianza de la temperatura con A: cuatro. Menos
el peso de A por la varianza de A, que es cinco. Menos el peso de B por la
covarianza entre A y B. ¿Cuánto vale esa? Los dos termómetros ven la misma
temperatura y sus ruidos no se relacionan, así que comparten solo la varianza
de la temperatura: cuatro. Igualado a cero.

<!-- b4 -->
Segunda condición, con B: cuatro, menos cuatro por el peso de A, menos ocho por
el peso de B, porque la varianza de B es cuatro más cuatro. Igual a cero. Dos
ecuaciones, dos incógnitas. De la segunda, el peso de A es uno menos dos veces
el de B. Lo metemos en la primera y queda menos uno más seis veces el peso de
B, igual a cero. El peso de B es un sexto, y el de A, dos tercios.

<!-- b5 -->
La apuesta: veinte, más dos tercios por tres, más un sexto por dos. Veintidós
coma tres tres. Y el error: la varianza, cuatro, menos cada peso por su
covarianza con la temperatura. Cuatro, menos dos tercios por cuatro, menos un
sexto por cuatro: dos tercios, cero coma seis siete. Con A solo era cero coma
ocho, y con B solo, dos. Juntos, mejor que el mejor de los dos.

---

# Escena 18 — EcuacionesNormales

**Objetivo:** escribir las ecuaciones de los dos termómetros con una matriz,
explicando desde cero qué es una matriz y cómo se multiplica por una columna;
llegar a C_XX h = c_XY (ecuaciones normales), a la solución con la inversa
(determinante 24) y al error σ² − cᵀh, diciendo por qué vale. Comprobaciones de
sentido común: pesos según el ruido, pesos que suman menos de uno, más
mediciones nunca empeoran.

**Qué hace falta saber antes:** escena 17.

**Visual:**
- La matriz por casillas (`MatrizT`): «5 4 / 4 8». La diagonal en ámbar
  («varianza de cada termómetro»), fuera de la diagonal en cian («covarianza
  entre ellos»).
- Matriz por columna: la fila «5 4» se desliza sobre «h_A, h_B» → «5h_A + 4h_B»;
  la fila «4 8» → «4h_A + 8h_B».
- La columna de la derecha «4, 4»: «covarianza de cada lectura con la temperatura».
- Todo en una línea: «C_XX · h = c_XY». Un rótulo «normal = perpendicular».
- «h = C_XX⁻¹ c_XY»; «det = 5 · 8 − 4 · 4 = 24 ≠ 0».
- «error = σ_Y² − c_XYᵀ h = 4 − (4 · ⅔ + 4 · ⅙) = ⅔».
- Comprobaciones: «⅔ : ⅙ = 4 : 1» junto a «ruido 1 : ruido 4»; «⅔ + ⅙ = ⅚ < 1»;
  «más mediciones → error nunca sube».

## Narración

<!-- b1 -->
Con tres termómetros habría tres ecuaciones; con diez, diez. Para no
escribirlas una a una se usa una matriz: una tabla de números. Aquí, la tabla de
covarianzas entre las lecturas. En la diagonal, la varianza de cada termómetro:
cinco y ocho. Fuera de la diagonal, la covarianza entre los dos: cuatro, y otra
vez cuatro.

<!-- b2 -->
Una matriz por una columna de números se calcula fila por fila: cada fila se
multiplica, término a término, por la columna, y se suma. La primera fila,
cinco y cuatro, por los dos pesos, da cinco veces el peso de A más cuatro veces
el de B. La segunda, cuatro veces el de A más ocho veces el de B. Son justo los
lados izquierdos de nuestras dos ecuaciones.

<!-- b3 -->
Y los lados derechos forman otra columna: la covarianza de cada lectura con la
temperatura, cuatro y cuatro. Así que las dos ecuaciones, y las de cualquier
número de mediciones, caben en una línea: la matriz de covarianzas de las
mediciones, por los pesos, igual a las covarianzas con lo que se estima. Se
llaman ecuaciones normales. Normal, en geometría, significa perpendicular.

<!-- b4 -->
Resolverlas es como dividir entre la matriz, y eso se llama multiplicar por su
inversa. Existe si un número llamado determinante no es cero. En dos por dos,
es el producto de la diagonal menos el de fuera: cinco por ocho menos cuatro
por cuatro, veinticuatro. Y el error es la varianza menos los pesos por las
covarianzas con la temperatura, porque, al ser perpendicular a las lecturas, el
error solo comparte con la temperatura su propio tamaño.

<!-- b5 -->
Dos comprobaciones de sentido común. A pesa dos tercios y B un sexto: cuatro
veces más. Y el ruido de A es cuatro veces más pequeño. Cada termómetro pesa
según lo poco que se equivoca. Además, los pesos suman cinco sextos, menos de
uno: la estimación sigue tirando un poco hacia la media. Y una regla general:
añadir una medición nunca empeora el error.

---

# Escena 19 — ElSegundoTermometro

**Objetivo:** ver con tres segundos termómetros que una medición vale por lo
que trae de nuevo: una copia exacta no aporta y deja la matriz sin inversa;
una copia empeorada recibe peso cero; uno cuyo ruido es el doble del de A
permite restarlo (pesos 2 y −1) y deja el error en cero. Encuesta visual con
pausa antes de cada respuesta.

**Qué hace falta saber antes:** escenas 17 y 18.

**Visual:**
- Tres tarjetas boca abajo: «B₁: un cable que copia A», «B₂: A + ruido propio
  (σ² = 3)», «B₃: su ruido es el doble del de A». Una pregunta: «¿cuál aporta
  más?». Se dan vuelta de a una.
- B₁: la matriz «5 5 / 5 5»; «det = 25 − 25 = 0» en rojo; «infinitos pesos dan lo
  mismo».
- B₂: la matriz «5 5 / 5 8» → «h = (0,8; 0)»; «error = 0,8», el mismo de A solo.
- B₃: la matriz «5 6 / 6 8» → «h = (2; −1)»; «error = 0». El «−1» resaltado.
- Con números: «A = 23», «B₃ = 24» → «B₃ − A = 1 = ruido de A» → «23 − 1 = 22»;
  «20 + 2 · 3 − 1 · 4 = 22» ✓.
- Rótulo final: «vale lo que trae de nuevo».

## Narración

<!-- b1 -->
¿Añadir un termómetro siempre ayuda? Depende de cómo sea su ruido. Veamos tres
segundos termómetros distintos, y piensa cada respuesta antes de oírla. El
primero es un cable que copia la lectura de A: marca exactamente lo mismo.
¿Cuánto aporta?

<!-- b2 -->
Nada, claro. Y las ecuaciones lo notan: la matriz de covarianzas tiene todas
sus casillas iguales, cinco. El determinante, cinco por cinco menos cinco por
cinco, es cero, y la matriz no tiene inversa. Hay infinitos pares de pesos que
dan la misma estimación, porque da igual cómo repartas el peso entre dos
lecturas idénticas. Una medición repetida no es información nueva.

<!-- b3 -->
El segundo es una copia empeorada: marca lo mismo que A, más un ruido propio de
varianza tres. En total, su ruido tiene varianza cuatro, como el B de antes.
Pero al resolver, su peso sale cero. Todo lo que sabe de la temperatura ya lo
sabía A; lo demás es ruido añadido. El error se queda en cero coma ocho, igual
que con A solo.

<!-- b4 -->
El tercero es el más curioso. Su ruido es exactamente el doble que el de A: si
A se pasa medio grado, este se pasa un grado. Al resolver, los pesos salen dos
y menos uno. ¡Un peso negativo! Y el error, cero. ¿Por qué? Porque la lectura
de este termómetro menos la de A es justo el ruido de A. Con esa resta sabes
cuánto se equivocó A, y lo quitas.

<!-- b5 -->
Con números: A marca veintitrés y el tercero, veinticuatro. La diferencia, uno,
es el ruido de A, así que la temperatura es veintitrés menos uno: veintidós, sin
error. Y eso dan los pesos: veinte, más dos por tres, menos uno por cuatro.
Veintidós. Una medición no vale por lo que se parece a la señal, sino por lo
que trae de nuevo. Y las ecuaciones normales lo calculan solas.

---

# Escena 20 — LlegaUnDatoNuevo

**Objetivo:** actualizar una estimación cuando llega una medición nueva sin
rehacer el sistema: predecir la medición, medir la sorpresa (−0,4), calcular
la ganancia con la fórmula de la recta (0,8 / 4,8 = ⅙) y corregir: 22,33 y error
0,67, lo mismo que con el sistema. Sembrar el filtro de Kalman (capítulo 12).

**Qué hace falta saber antes:** escenas 10, 11 y 17.

**Visual:**
- Línea de tiempo: «leo A = 23 → ŷ = 22,4, error 0,8»; luego «llega B = 22».
- «¿qué esperaba de B?» → «22,4». «sorpresa = 22 − 22,4 = −0,4» (en ámbar).
- La sorpresa por piezas: «(error que tenía, σ² = 0,8) + (ruido de B, σ² = 4)» →
  «σ² = 4,8»; «comparte con mi error: 0,8» → «ganancia = 0,8 / 4,8 = ⅙».
- «ŷ_nueva = 22,4 + ⅙ · (−0,4) = 22,4 − 0,067 ≈ 22,33» junto al «22,33» de la
  escena 17: «=». «error = 0,8 · ⅚ ≈ 0,67» ✓.
- Un diagrama en bucle: «estimación → predecir → sorpresa → × ganancia →
  estimación», con la etiqueta «filtro de Kalman (capítulo 12)».

## Narración

<!-- b1 -->
Una situación muy habitual: ya tenías una estimación y llega una medición
nueva. Primero leíste A, que marcaba veintitrés, y apostaste veintidós coma
cuatro, con error cero coma ocho. Ahora llega B, el que tiene ruido de varianza
cuatro, y marca veintidós. ¿Hay que rehacer todas las cuentas desde el
principio?

<!-- b2 -->
No hace falta. Antes de mirar B, ¿qué esperabas que marcara? B es la
temperatura más un ruido de media cero, así que tu mejor apuesta para B era tu
apuesta para la temperatura: veintidós coma cuatro. Marca veintidós. La
sorpresa es la diferencia entre lo que llega y lo que esperabas: menos cero
coma cuatro.

<!-- b3 -->
La sorpresa es un dato nuevo, y se usa con la fórmula de la recta de siempre:
covarianza entre varianza. La sorpresa está hecha del error que todavía
tenías, de varianza cero coma ocho, más el ruido de B, de varianza cuatro. Su
varianza es la suma: cuatro coma ocho. Y lo que comparte con tu error es cero
coma ocho. El factor es cero coma ocho entre cuatro coma ocho: un sexto.

<!-- b4 -->
La estimación nueva es la vieja más un sexto por la sorpresa: veintidós coma
cuatro, menos cero coma cero seis siete. Veintidós coma tres tres, lo mismo que
resolviendo el sistema entero. Y el error baja en la misma proporción: cero
coma ocho por cinco sextos, cero coma seis siete. Tampoco cambia.

<!-- b5 -->
Esa forma de trabajar, la estimación vieja más una ganancia por la sorpresa, es
una de las ideas más útiles de la ingeniería. La ganancia es grande cuando tu
error es grande comparado con el ruido de la medición, y pequeña en el caso
contrario. Repetida en el tiempo, muestra a muestra, se convierte en el filtro
de Kalman, que veremos en el capítulo doce.

---

# Escena 21 — DeLaTeoriaALosDatos

**Objetivo:** contar qué cambia en la práctica (los momentos se calculan con
datos: la ironía con la estimación de Probabilidad y Estadística); adelantar
que con muestras de una señal las ecuaciones normales son las de los capítulos
10 y 12; y abrir el capítulo 9 con «0,79 no es un bit». La recapitulación del
capítulo queda para el cierre del episodio.

**Qué hace falta saber antes:** todo el capítulo; escena 01 (las dos
«estimaciones»); escenas 04 y 06 (acertar o fallar; 0,79).

**Visual:**
- Una tabla de datos que se llena; de ella salen «μ», «σ²» y «σ_XY» con un
  sombrero cada uno, y entran en la fórmula de la recta. La tarjeta tachada de
  la escena 01 («Prob. y Estadística») se destacha.
- Una señal (el sensor) con muestras «x[n−1], x[n−2], x[n−3]» que entran como
  mediciones en «C_XX h = c_XY»; etiquetas «capítulo 10: predecir» y
  «capítulo 12: limpiar».
- «0,79» entre un «0» y un «1»; un radar con un «¿avión o ruido?». Rótulo «decidir».

## Narración

<!-- b1 -->
Todo este capítulo ha supuesto que conocemos medias, varianzas y covarianzas.
En la práctica casi nunca es así: tenemos datos. Entonces se calculan
promediando los datos, y se meten en las fórmulas como si fueran los
verdaderos. Y aquí hay una ironía. Al principio dijimos que esta estimación no
era la de Probabilidad y Estadística. Pues para usarla de verdad, hace falta
aquella.

<!-- b2 -->
Ahora, un adelanto. ¿Y si las mediciones son muestras de una misma señal? Lo
que marcó el sensor hace un segundo, hace dos, hace tres. Las ecuaciones
normales son exactamente las mismas: covarianzas entre las muestras, por los
pesos, igual a covarianzas con lo que se quiere adivinar. Con ellas
predeciremos el futuro de una señal y limpiaremos el ruido de una grabación,
en los capítulos diez y doce.

<!-- b3 -->
Pero queda una pregunta abierta desde el canal de bits. La mejor apuesta era
cero coma setenta y nueve, y eso no es un bit. Muchas veces no hay que dar un
número, sino elegir: ¿se envió un cero o un uno? ¿Hay un avión en la pantalla
del radar, o solo ruido? Eso ya no es estimar: es decidir, con la tercera forma
de medir el error, acertar o fallar. Y es el tema del capítulo siguiente.
