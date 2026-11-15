# Capítulo 13 — Detección de señales

> **Guion base: narración de todo el capítulo. No se renderiza.**
> Es la fuente de texto para los 7 episodios (ver `../README.md` §1 para qué
> escenas van en cada uno). Cada episodio copia de aquí su narración a su
> propio `E<N>_.../guion.md`, que es el que lleva gancho, cierre y momentos, y
> el que se anima. Las secciones "Visual" son ideas iniciales, no
> especificación.
>
> **Estado:** narración completa, **esperando la aprobación del usuario**.
> Mientras no esté aprobada, cualquier ajuste de texto que pida el usuario se
> hace aquí primero, y después se copia al `guion.md` del episodio.

Guion para las 31 escenas del capítulo. Fuentes: `Apuntes/PROCESAMIENTO DE
SEÑALES.md` (sección "Detección De Señales", líneas 1880–2122, sin los
Ejercicios Propuestos ni las actividades 13.3 y 13.4) y `Apuntes/PROCESAMIENTO
DE SEÑALES - Cap 13 en profundidad.md`: Parte 1 (suficiencia de g, fórmulas de
desempeño y ROC, letra chica de «más rápido que exponencial», ganancia del
filtro adaptado, ruido coloreado, la distancia entre señales y las tres
señalizaciones), Parte 2 (dos mediciones, un detector armado con números,
filtros desadaptados, ruido coloreado resuelto, tabla de señalización,
Barker contra rectangular), Parte 3 (implementación causal, σ² desconocida,
retardo desconocido y su coste, ruido coloreado en la práctica) y Parte 4
(geometría, Wiener contra adaptado, puentes). Figuras de referencia:
`c13-dos-gaussianas.svg`, `c13-matched-autocorr.svg`,
`c13-onoff-vs-antipodal.svg`, `c13p-dos-mediciones.svg`,
`c13p-suficiencia.svg`, `c13p-roc-detector.svg`, `c13p-cotas-q.svg`,
`c13p-desadaptado.svg`, `c13p-ruido-coloreado.svg`, `c13p-constelaciones.svg`,
`c13p-compresion-retardo.svg`.

**Qué se recuerda y dónde** (README §3, regla 2: nada se da por sabido, se
recuerda donde se usa, con su dibujo):
- del capítulo 9 (que aún no tiene guion base, así que se recuerda entero): las
  dos hipótesis y las probabilidades a priori (01), falsa alarma, miss y
  probabilidad de error (01), la regla MAP como «curvas escaladas por su
  probabilidad a priori» (02), la razón de verosimilitud y los otros criterios
  (08), la curva ROC y Neyman-Pearson (12);
- del capítulo 7: la campana de Gauss (05), independencia y densidad conjunta
  como producto (05), combinación lineal de gaussianas, varianza de una
  combinación (09, 19), producto escalar y proyección (08), la parábola de
  Cauchy-Schwarz (17, 29);
- del capítulo 10: la convolución como «deslizar, multiplicar y sumar» (14), la
  autocorrelación (15), el sensor del 0,6 (19);
- del capítulo 11: los números complejos como flechas con módulo y ángulo (16),
  el blanqueador (20), Parseval (21), la estimación del espectro con Welch (22),
  los decibelios (24);
- de matemáticas: logaritmo natural (06), la cola de la campana y su simetría
  (10), la función inversa (12), el discriminante (17);
- de Señales y Sistemas: respuesta al impulso y filtro LTI (14), la transformada
  como suma de sinusoides con fase (16), PAM y la interferencia entre símbolos,
  con su condición de no-ISI (30).

Cómo está escrito (README §3, "Explicar de forma explícita"): cada concepto
sigue el camino caso → cuenta a mano con números pequeños → dibujo → fórmula
como resumen → comprobación. **Un solo pulso, `s = (2, 2, 1)`, con `σ² = 1` y
energía 9, atraviesa el capítulo entero**, para que cada idea nueva se aplique a
algo que ya se entiende. Las deducciones cortas se hacen enteras, diciendo qué
regla se usa en cada paso (la derivación de la escena 06, la desigualdad de
Cauchy-Schwarz de la 17, la distancia de la 28). Las largas (la derivación
vectorial con matriz de covarianza, la cota de Chernoff, el lema de
Neyman-Pearson) se dicen en su paso clave y se remite al apunte "en
profundidad". Hay preguntas con pausa y sorpresas en las escenas 01, 04, 07,
10, 13, 15, 18, 19, 27 y 29. Castellano de España.

Convención: cada escena tiene Objetivo, qué hace falta saber antes, qué se ve,
y la narración partida en bloques `<!-- bN -->` que se sincronizan uno a uno
con un tramo de animación.

## Reparto en episodios

| Episodio | Escenas | Idea fuerza |
|---|---|---|
| E1 · Más datos no bastan | 01 ElRadar, 02 UnaMedicion, 03 DosMediciones, 04 PromediarDestruye | Decidir con una señal entera es la misma regla que con un número, pero con muchos datos hay que usarlos bien: promediarlos tira información |
| E2 · Toda la señal en un solo número | 05 SenalConocida, 06 LaCuenta, 07 ElUmbral, 08 UnNumeroQueBasta | Con ruido gaussiano, la señal entera se resume en un número, lo parecida que es a la señal buscada, y no se pierde nada |
| E3 · ¿Cuánto nos equivocamos? | 09 DosCampanas, 10 FuncionQ, 11 ElPrior, 12 CurvaRoc, 13 SoloLaEnergia | Detectar es separar dos campanas; el error depende solo de la energía de la señal entre la varianza del ruido, no de su forma |
| E4 · El filtro que es la señal al revés | 14 ElFiltroAlReves, 15 ElPicoEsLaAutocorrelacion, 16 LaLecturaEnFrecuencia, 17 NadieLaSupera, 18 CuantoSePierde | El número se calcula con un filtro cuya respuesta es la señal invertida, y ningún otro filtro saca más relación señal-ruido |
| E5 · Cuando el ruido tiene memoria | 19 LaMemoriaDelRuido, 20 BlanquearYAdaptar, 21 DondeVivaLaSenal, 22 RuidoEnLaPractica | Si el ruido tiene memoria, se blanquea primero y se adapta después; y entonces la forma de la señal sí importa |
| E6 · ¿Cuándo llegó el eco? | 23 ElEcoQueLlega, 24 PulsoQueSeComprime, 25 ChirpYResolucion, 26 BuscarTienePrecio | Si no sabes cuándo llega el pulso, el pico de la salida lo mide; y para que sea nítido hace falta un pulso largo cuya autocorrelación sea estrecha |
| E7 · ¿Cuál de ellas mandaron? | 27 VariasSenales, 28 LaDiferencia, 29 AntipodalGana, 30 ReceptorDeModem, 31 ElMapaDelCurso | Con varias señales posibles, cuenta la distancia entre ellas: la antipodal la hace máxima, y por eso la usan casi todos los sistemas digitales |

Narración base por episodio (sin gancho ni cierre): E1 ≈ 1.140 palabras, E2 ≈
1.210, E3 ≈ 1.490, E4 ≈ 1.420, E5 ≈ 1.170, E6 ≈ 1.100, E7 ≈ 1.450: entre 7,3 y
9,9 min de voz; con gancho y cierre, ~8–10,5 min. E3, E4 y E7 son los más
largos (E3 y E7 pasan de las ~1.300 palabras del README) y admiten recortes al armar
el `guion.md` (README §2, paso 8): por ejemplo, en E3 la nota de «más rápido que
exponencial» (escena 13) y en E7 la comparación honesta de la escena 29.

El gancho y el cierre de cada episodio **no** están aquí: se escriben al
armar el `guion.md` del episodio (README §2, paso 8). Cada cierre anuncia el
episodio siguiente por su título. El E1 lo anuncia el cierre del último
episodio del capítulo 12 (Estimación de señales), que todavía no tiene guion
base: **al escribirlo, su cierre tiene que anunciar «Más datos no bastan»**
(estimar una señal es una cosa; decidir si hay señal, otra). El cierre de E7 es
el **cierre de toda la serie**: no anuncia ningún episodio, y se escribe con la
escena 31 como base.

## Hilos que cruzan el capítulo

Para quien arme cada episodio: estos bucles ya están sembrados en la
narración y hay que respetarlos (y retomarlos en ganchos y cierres).

- **Los ejemplos que vuelven** (mismo dibujo y mismos números siempre):
  - **el pulso `s = (2, 2, 1)`** con `σ² = 1` y energía `E = 9` (escenas 05, 06,
    07, 09 a 18, 23, 28, 29): tres barras en azul (`SENAL`). Sus números:
    - `r = (3, 1, 2)` da `g = 10` y se decide «hay señal»; `r = (0,5; −1; 1)`
      da `g = 0` y se decide «solo ruido» (06);
    - umbral 4,5 con priors iguales, 5,886 con `p₁ = 0,2` (07, 11);
    - dos campanas en 0 y 9, desvío 3 (09); `P_FA = P_M = Q(1,5) = 0,0668` (10);
      con `p₁ = 0,2`: 0,0249, 0,1497 y `P_e = 0,0498` (11); Neyman-Pearson con
      `P_FA = 0,01`: umbral 6,979 y `P_D = 0,75` (12);
    - el filtro `h = (1, 2, 2)`; con `r = (3, 1, 2)` sale `(3, 7, 10, 6, 4)` y
      el tercer valor es 10 (14); con la señal limpia sale `(2, 6, 9, 6, 2)`,
      pico 9 = E (15);
    - el promediador `(1, 1, 1)` conserva 0,926 de la relación señal-ruido
      (−0,33 dB) y la muestra suelta 0,444 (−3,52 dB) (17, 18);
  - **el promedio que destruye información** (04) y **el promediador que no ve
    nada** (18): «promediar no siempre es buena idea»; en 04 con dos mediciones
    uniformes, en 18 con el pulso `(1, −2, 1)` cuya suma es cero;
  - **el eco del 0,6** (19, 20, 21): el sensor del capítulo 10 y el ejemplo del
    capítulo 11 (vecinas correlacionadas 0,6; blanqueador `x[n] − 0,6 x[n−1]`).
    Aquí, dos muestras con covarianza 0,6: el pulso `(2, 0)` da `d² = 6,25`
    frente a 4, y `P_e` 0,1056 frente a 0,1587;
  - **las tres señalizaciones**: el mismo pulso `(2, 2, 1)` con energía 9 es
    también el punto de partida de la escena 28 y la 29: on-off `(2, 2, 1)` y 0,
    ortogonal `(2, 2, 1)` y `(2, −1, −2)`, antipodal `(2, 2, 1)` y `(−2, −2, −1)`,
    con `P_e` 0,0668 · 0,0170 · 0,00135;
  - **el radar** (01, 23, 26): el avión y su eco;
  - **Barker de trece** y el **pulso rectangular de trece** (24, 25).
- **«Más datos no bastan»** (01 a 04): la promesa del capítulo se abre en el
  E1 con las dos mediciones, se cierra en la escena 08 (el número que sí lo
  aprovecha todo) y vuelve en la 18 (el promediador que no ve nada).
- **La forma no importa, solo la energía**: se afirma en la 13 (con ruido
  blanco) y se **matiza a propósito en la 21** (con ruido que tiene memoria, la
  forma sí importa). Es un bucle que se anuncia («con ruido blanco») y se paga.
- **La parábola de Cauchy-Schwarz**: viene del capítulo 7 (escena 28), volvió
  en el capítulo 10 (12) y en el 11 (30). **Esta es su cuarta aparición** (escena
  17, mismo dibujo) y se cierra en la 29 (la correlación entre dos señales no
  baja de menos la energía) y en la 31. (Ojo: la escena 28 del capítulo 7 dice
  que «volverá dos veces más», y con el capítulo 10 son tres; con este, cuatro.)
- **Blanquear primero y aplicar lo que ya sabemos después**: se planta en el
  capítulo 11 (escena 27), se usa en la 20 y se cierra en la 31 (Wiener y
  adaptado hacen lo mismo con objetivos distintos).
- **Proyectar sobre lo que importa y tirar lo perpendicular**: la geometría
  del capítulo 8 (la flecha y su sombra) vuelve en la escena 08 (la parte de
  ruido perpendicular a `s` no informa) y en la 28 (la distancia entre
  señales, la frontera perpendicular).
- **Dónde se pone el máximo**: la escena 15 (el pico de la salida es la
  autocorrelación) se paga en las 23, 24 y 25 (medir el retardo, hacerlo
  nítido, resolver dos ecos).
- **Buscar en muchos sitios cuesta**: se anuncia en la 23 («no sabemos en qué
  celda está») y se calcula en la 26.
- **Puentes a otros capítulos** (Parte 4.3 del "en profundidad"):
  - capítulo 9: todo el aparato de MAP, Neyman-Pearson y ROC se hereda entero,
    solo cambia qué es «la medición» (escenas 02, 08, 12);
  - capítulo 12: Wiener estima la forma de un proceso, el adaptado decide sobre
    una forma conocida; los dos blanquean primero (31).
- **Cierre del capítulo y de la serie** (escena 31): el mapa del curso, la
  cuarta parábola y la receta práctica. El cierre de E7 (a escribir) cierra la
  serie.

## Recortes decididos

- La derivación vectorial con matriz de covarianza (`g = rᵀC⁻¹s`, Parte 1.5): se
  hace con **dos muestras** a mano (escenas 19 y 20), sin la matriz general. La
  escena 20 dice dónde está.
- La cota de Chernoff y la asintótica de `Q` (Parte 1.3): solo se nombra la
  idea de «más rápido que exponencial» y en qué eje lo es (escena 13).
- El teorema de factorización de Fisher-Neyman (Parte 1.1): la idea geométrica
  (la parte perpendicular no informa) sí; el teorema, no (escena 08).
- El lema de Neyman-Pearson: se usa (escena 12), no se demuestra; está en el
  capítulo 9.
- La pendiente de la ROC igual al umbral y el riesgo mínimo con costos (capítulo
  9): no se retoman.
- La implementación causal completa (Parte 3.1): se hace con el retardo de
  `L − 1` muestras en la escena 14 (es la forma más concreta), sin la versión
  no causal del apunte más que como nota.
- La amplitud, el signo y la fase desconocidos, y el detector de envolvente
  (Parte 3.3): quedan para el apunte; en la escena 23 solo se nombra la amplitud
  como una razón más para no fijar el umbral a ojo.
- La regularización de la matriz de covarianza y el filtro de Wiener cuando el
  ruido se estima con pocos datos: se dice en una frase (escena 22).
- Cuántas simulaciones hacen falta (Parte 3.6): no se cuenta; las
  simulaciones se citan como comprobación.
- La ROC como familia de curvas con `d`: solo se dibuja (escena 12).
- La ortogonalidad entre `s₀` y `s₁` con energías distintas y el caso de energías
  desiguales en la señalización (Parte 2.5, párrafo final): se hace la
  comparación honesta a igual energía media en una frase (escena 29).
- Los Ejercicios Propuestos y las actividades 13.3 y 13.4 no se resuelven; los
  números de los ejemplos son del "en profundidad" (`s = (2, 2, 1)`, las dos
  mediciones uniformes, el filtro desadaptado con `(1, −2, 1)`, Barker-13, las
  tres señalizaciones) o inventados con números redondos (el eco del 0,6 con
  `(2, 0)`, las tres señales de la escena 27).
- El ejemplo de las dos mediciones uniformes (escenas 02 a 04) **es una
  reconstrucción** que da los mismos números que cita el apunte (1/4, 3/16, 1/4):
  el libro no lo da con esas densidades. Conviene decirlo si alguien lo compara.
- **Una inconsistencia en el apunte**, no en el guion: la tabla de la Parte 2.3
  dice «una muestra» con cos² = 0,889 (−0,51 dB) para el pulso `(2, 2, 1)`, pero
  la muestra suelta más grande da 4/9 = 0,444 (−3,52 dB), que es lo que dice la
  Parte 1.4 (ganancia 9/4). El guion usa 0,444. (0,889 = 8/9 es el resultado de
  mirar **dos** muestras.)

## Pronunciación

Probar de oído antes de sintetizar (README §9): Neyman-Pearson, Cauchy-Schwarz,
Barker, Nyquist, Wiener, Bayes, «chirp» (en la narración se dice «señal con
barrido de frecuencia», y «chirp» solo en pantalla; probar cómo suena si se
quiere decir), «coseno alzado». Siglas y anglicismos: «curva ROC» (probar «erre
o ce» contra «roc»), «miss» (se dice «un fallo, que en inglés se llama miss»;
probar), «matched filter» (solo en pantalla; se narra «filtro adaptado»), y se
evitan «SNR», «CFAR», «FIR» y «ISI» en la narración («relación señal-ruido»,
«umbral que se adapta», «interferencia entre símbolos»). «La función Q» se dice
«la función cu»: probar, y «la inversa de la función cu». Letras y símbolos que
se leen en voz alta: «ge» para `g`, «gamma», «sigma cuadrado», «pe cero» y «pe
uno» para las a priori, «hache cero» y «hache uno», «erre de ene», «ese de ene»,
«lambda», «omega», «ele» para el largo de la señal (o «el número de muestras»).
Unidades: «decibelios», «hercios». Números: `0,0668` se dice «cero coma cero
seis seis ocho»; los enteros simples van en cifra.

## Piezas visuales nuevas

Van a `comun/figuras.py` (sección «capítulo 13, episodio N»):
- una señal de muestras como **barras** azules (`s`) y la recibida (`r`) en
  cian con ruido magenta encima, más una tira que muestra `n = 0, 1, 2` (E1, E2);
- densidades uniformes con altura visible: rectángulos 1/2 y 1 sobre el eje, y el
  cuadrado grande con el cuadrado pequeño dentro; el triángulo del promedio (E1);
- regla de decisión como **dos curvas escaladas por su prior**, una encima de la
  otra, con la región donde cada una gana (E1); ampliable a las regiones en el
  plano (E1);
- `Espectro`/`Curva` con **dos campanas** de igual ancho separadas por `E`, con
  umbral móvil y las colas `P_FA` y `P_M` sombreadas (E3); pieza `DosCampanas`
  con `ValueTracker` sobre el umbral y sobre la separación (E3);
- la **curva ROC** que se traza al mover el umbral, con `d` como parámetro (E3);
- **flecha de `r` descompuesta** en componente paralela y perpendicular a `s`,
  y la nube esférica de ruido (E2);
- `BloqueLTI` (prevista en el README) con la respuesta `h` a la vista, la
  entrada `r` desfilando y la salida que se llena de a una muestra (E4);
- tres **flechas complejas** (módulo y ángulo) que se alinean con `H = conj(S)`
  y se suman en una larga (E4);
- **parábola de Cauchy-Schwarz** del capítulo 7 (misma pieza) (E4, E7);
- plano con la **nube elíptica de dos muestras correlacionadas** (covarianza
  0,6) y el eje `(1, 1)` frente al `(1, −1)`; espectro del ruido con memoria
  contra el de la señal, con el área ponderada (E5);
- **radar**: antena, avión y eco; **línea de tiempo** con el retardo `D` y la
  salida del filtro con su pico (E6);
- **autocorrelación** del rectángulo de 13 (triángulo) contra la de Barker
  (pico y sidelobes de 0 o 1), y la de la señal con barrido de frecuencia (E6);
- **dos ecos** con retardo relativo de 3 muestras, salida del rectángulo (meseta
  de 23) y de Barker (dos picos de 13) (E6);
- **constelación**: los puntos `s₀` y `s₁` en el plano, on-off, ortogonal y
  antipodal, con la frontera perpendicular y la distancia marcada (E7);
- tres flechas de `M` señales con `M` filtros adaptados en paralelo y un bloque
  «elegir el mayor» (E7);
- cadena **transmisor → canal → receptor** con `|P|²` repartido y el pulso
  coseno alzado (E7);
- el **mapa del curso** (cadena de siete capítulos con los puentes) (E7).

---

# Escena 01 — ElRadar

**Objetivo:** plantear el problema del capítulo (¿hay una señal escondida en el
ruido o solo hay ruido?), recordar las dos hipótesis, las probabilidades a
priori, la falsa alarma, el miss y la probabilidad de error como media
ponderada, y traducirlo al test médico. Terminar con la pregunta: ¿cómo se
decide con una señal entera?

**Qué hace falta saber antes:** nada del capítulo; del capítulo 9, hipótesis y
tipos de error (se recuerdan aquí).

**Visual:**
- Una antena de radar que lanza un pulso; vuelve un eco diminuto tapado por un
  ruido que lo desborda. «¿avión o ruido?».
- Dos casillas: «H₀ · solo ruido» (magenta) y «H₁ · señal + ruido» (azul y
  magenta). Probabilidades «p₀ = 0,9 · p₁ = 0,1».
- Tabla de 2 × 2: filas «realidad» y columnas «decisión»; dos casillas con tilde
  (aciertos) y dos con cruz roja: «falsa alarma» y «miss».
- La fórmula de `P_e` construida término a término: «p₀ · P_FA + p₁ · P_M», con el
  ejemplo «0,9 · 0,05 + 0,1 · 0,2 = 0,065».
- Una fila de barras, la señal medida muestra a muestra, y la pregunta: «¿y si es
  una señal entera?».

## Narración

<!-- b1 -->
Un radar lanza un pulso y se queda escuchando. Si hay un avión, vuelve un eco
muy débil, escondido en el ruido. Si no hay nada, solo se oye el ruido. Con lo
que ha oído, el radar tiene que decidir: ¿hay un avión o no? Ese sí o no es el
problema de todo este capítulo.

<!-- b2 -->
Démosle nombres. La hipótesis cero, hache cero, dice: solo hay ruido. La
hipótesis uno, hache uno, dice: hay señal más ruido. Y antes de escuchar nada
ya sabemos algo: por ejemplo, que aviones hay pocos. Esas dos probabilidades de
partida, pe cero y pe uno, se llaman probabilidades a priori, porque valen antes
de medir.

<!-- b3 -->
Al decidir hay cuatro casos posibles. Dos son aciertos. Los otros dos son
errores, y tienen nombre propio. Si el radar dice que hay avión y no lo había,
es una falsa alarma. Si dice que no hay nada y sí lo había, es un fallo, que en
inglés se llama miss. En medicina es igual: el falso positivo y el falso
negativo de un test.

<!-- b4 -->
Cada error tiene su probabilidad: la de falsa alarma y la de miss. Y la
probabilidad total de equivocarnos es la media ponderada de las dos: pe cero
por la falsa alarma, más pe uno por el miss. Con números redondos: si el avión
aparece una de cada diez veces, con cinco por ciento de falsas alarmas y veinte
por ciento de misses, nos equivocamos un seis coma cinco por ciento.

<!-- b5 -->
Todo esto es lo que viste en el capítulo de pruebas de hipótesis, con una única
medición. Pero un radar no oye un número: oye una señal entera, muchas muestras
seguidas. Y ahí nos espera una sorpresa: tener más datos no basta. Para verla,
volvamos a la regla de decisión, y hagámoslo con un ejemplo muy pequeño.

---

# Escena 02 — UnaMedicion

**Objetivo:** recordar la regla MAP como «dos curvas escaladas por sus
probabilidades a priori: gana la más alta», con un ejemplo de densidades
uniformes donde la cuenta es trivial. Ver que con una sola medición la regla
óptima decide siempre lo mismo y comete un error de un cuarto.

**Qué hace falta saber antes:** escena 01; del capítulo 7, la densidad y que el
área vale uno (se recuerda aquí).

**Visual:**
- Bajo `H₀` (75 %): la medición vale cualquier número entre −1 y 1, con la misma
  probabilidad (rectángulo). Su altura se calcula en pantalla: «ancho 2 · alto =
  1 → alto ½».
- Bajo `H₁` (25 %): entre −½ y ½ (rectángulo más estrecho y más alto): «ancho 1 ·
  alto = 1 → alto 1».
- Las dos curvas se **escalan** por su prior: `p₀ · f₀ = ¾ · ½ = 3/8` y `p₁ · f₁ =
  ¼ · 1 = ¼`. Se dibujan superpuestas: la de `H₀` siempre por encima donde
  ambas existen.
- La regla: «p₁ f(r|H₁) ≷ p₀ f(r|H₀)», con las piezas apareciendo mientras se
  nombran.
- Un contador de `P_e = p₁ × 1 = ¼`.

## Narración

<!-- b1 -->
Imagina una medición, un solo número. Bajo la hipótesis cero, ese número puede
valer cualquier cosa entre menos uno y uno, con la misma probabilidad. Bajo la
hipótesis uno, cualquier cosa entre menos un medio y un medio. Y a priori, la
hipótesis cero es tres veces más probable que la uno: tres cuartos frente a un
cuarto.

<!-- b2 -->
¿Qué altura tienen esas dos curvas? El área de cada una tiene que valer uno.
La primera mide dos de ancho, así que su altura es un medio. La segunda mide
uno de ancho, así que su altura es uno. Son las densidades de la medición bajo
cada hipótesis: nos dicen cuánto cabe esperar cada valor, según quién sea la
verdadera.

<!-- b3 -->
Ahora, la regla. Midiendo un valor, la probabilidad de cada hipótesis, ya con
el dato en la mano, es proporcional a su curva por su probabilidad a priori.
Así que dibujamos cada curva multiplicada por su a priori, y decidimos por la
más alta en el valor medido. Es la regla que minimiza la probabilidad de error.

<!-- b4 -->
Hagamos la cuenta. La hipótesis cero escalada vale tres cuartos por un medio:
tres octavos. La hipótesis uno escalada vale un cuarto por uno: un cuarto, o
dos octavos. En todos los puntos donde las dos existen, gana la cero. Nunca
conviene decir hache uno.

<!-- b5 -->
La mejor regla posible con esta medición es decir siempre «solo ruido». Y solo
nos equivocamos cuando en realidad era hache uno, que pasa una de cada cuatro
veces: la probabilidad de error es un cuarto. Parece triste. Veamos qué pasa si
en vez de una medición hacemos dos.

---

# Escena 03 — DosMediciones

**Objetivo:** con dos mediciones independientes, la densidad conjunta es un
cuadrado; aplicar la misma regla en el plano y ver que ahora sí hay una región
donde conviene decidir «hay señal» y que el error baja de 1/4 a 3/16. Recordar
la densidad conjunta como producto.

**Qué hace falta saber antes:** escena 02; del capítulo 7, variables
independientes: la densidad conjunta es el producto.

**Visual:**
- Los ejes `r₁`, `r₂`. Bajo `H₀`: cuadrado de lado 2 (área 4, altura ¼); bajo `H₁`:
  cuadrado de lado 1, centrado (área 1, altura 1), dentro del grande.
- Las alturas escaladas: `p₀ f₀ = ¾ · ¼ = 3/16` y `p₁ f₁ = ¼ · 1 = ¼ = 4/16`.
- Se pinta el cuadrado pequeño de azul («decido H₁») y el resto de gris («decido
  H₀»): las dos regiones de decisión.
- Errores: una nube de puntos bajo `H₀`; el cuarto de puntos que cae en el
  cuadrado pequeño se marca en rojo. Bajo `H₁` no hay ninguno fuera.
- Cuenta: «¾ · ¼ + ¼ · 0 = 3/16».
- La fórmula del vector: «p₁ f(r|H₁) ≷ p₀ f(r|H₀)» con `r` en negrita.

## Narración

<!-- b1 -->
Ahora tenemos dos mediciones independientes, cada una con las mismas reglas de
antes. Como son independientes, la densidad conjunta es el producto de las
dos. Bajo la hipótesis cero, el par cae en un cuadrado de lado dos, de área
cuatro: su altura es un cuarto. Bajo la hipótesis uno, en un cuadrado de lado uno,
de área uno: su altura es uno.

<!-- b2 -->
La regla es exactamente la misma: escalar por el a priori y comparar. La
hipótesis cero vale tres cuartos por un cuarto, tres dieciseisavos. La
hipótesis uno vale un cuarto por uno, cuatro dieciseisavos. Cuatro es mayor
que tres. Así que dentro del cuadrado pequeño, gana la hipótesis uno, y fuera de
él, la cero.

<!-- b3 -->
Fíjate en lo que ha cambiado: lo que antes eran tramos de una recta ahora son
regiones de un plano. Decidimos «hay señal» si el par de mediciones cae en el
cuadrado pequeño, y «solo ruido» si cae fuera. Con tres mediciones serían
regiones de un espacio de tres dimensiones. La regla no cambia; cambia dónde vive
la medición.

<!-- b4 -->
¿Cuánto nos equivocamos ahora? Si es hache uno, el par siempre cae en el
cuadrado pequeño, así que acertamos: cero errores. Si es hache cero, que pasa
tres de cada cuatro veces, nos equivocamos cuando el par cae en el cuadrado
pequeño, que es una de cada cuatro. Tres cuartos por un cuarto: tres
dieciseisavos.

<!-- b5 -->
Tres dieciseisavos, cero coma uno ocho siete cinco, es menos que un cuarto.
Con una medición nos equivocábamos una de cada cuatro veces; con dos, algo menos de
una de cada cinco. Más datos, mejor decisión. Ahora viene la pregunta obvia:
si tengo dos mediciones, ¿no bastaría con promediarlas?

---

# Escena 04 — PromediarDestruye

**Objetivo:** ver que promediar las dos mediciones deja el error en 1/4, o sea,
tira exactamente la información que las dos juntas tenían. Fijar el lema del
capítulo («más datos no ayudan solos: hay que procesarlos bien») y plantear la
pregunta que abre el E2: ¿existe un resumen de la señal entera que no tire nada?

**Qué hace falta saber antes:** escenas 02 y 03; del capítulo 7, el promedio y
que una suma de dos uniformes no es uniforme.

**Visual:**
- Un promedio `a = (r₁ + r₂) / 2`. Un gráfico de puntos: las dos mediciones
  proyectadas sobre la diagonal, apretadas hacia el centro.
- La densidad de `a`: un triángulo bajo `H₀` (base de −1 a 1, altura 1) y otro
  bajo `H₁` (base de −½ a ½, altura 2). Se dice «triángulo» porque hay muchas
  maneras de llegar a un valor en el medio y pocas en las puntas.
- Las dos curvas escaladas por su prior: la de `H₁` (pico 1/2) siempre por debajo
  de la de `H₀` (pico 3/4).
- Una pregunta en pantalla: «¿qué se perdió?». Un cuadrado con sus dos
  esquinas opuestas alineadas en la diagonal, y dos puntos distintos que dan el
  mismo promedio.
- La frase final: «más datos no bastan».

## Narración

<!-- b1 -->
Probemos la idea más natural. Tengo dos mediciones y decido promediarlas: el
número de resumen es a igual a erre uno más erre dos, entre dos. ¿Cómo se
distribuye ese promedio? Hay muchas maneras de obtener un valor cerca del
centro, sumando un número alto y otro bajo, y pocas de obtener uno en el
borde. Sale un triángulo.

<!-- b2 -->
Bajo la hipótesis cero, un triángulo de base dos y altura uno. Bajo la hipótesis
uno, un triángulo de base uno y altura dos. Ya sabes lo que sigue: escalamos por
el a priori. La hipótesis cero llega a tres cuartos en el centro. La hipótesis
uno, a un medio. Tres cuartos es más que un medio.

<!-- b3 -->
Y no solo en el centro: a medida que nos alejamos, la curva de la hipótesis
uno baja más deprisa que la otra. En ningún punto le gana. Así que la regla
óptima sobre el promedio vuelve a ser: decir siempre «solo ruido». Y el error
vuelve a ser un cuarto. Exactamente lo mismo que con una sola medición.

<!-- b4 -->
¿Qué ha pasado? Dos pares de mediciones muy distintos pueden dar el mismo
promedio. Uno y menos uno, y cero y cero, promedian cero los dos. Con el par
entero podíamos distinguir cuál hacía más probable la hipótesis uno. Con el
promedio, ya no. Al resumir, tiramos justo lo que sabía la forma del par.

<!-- b5 -->
Esta es la lección del capítulo: más datos no ayudan solos. Hay que
procesarlos bien. Pero entonces surge la pregunta importante: en el caso que de
verdad nos interesa, una señal conocida enterrada en ruido gaussiano, ¿hay un
resumen que lo aproveche todo y no tire nada? Sí. Y es sorprendentemente
sencillo: un único número.

---

# Escena 05 — SenalConocida

**Objetivo:** fijar el modelo del capítulo (señal conocida más ruido gaussiano
independiente, `σ² = 1`) con el pulso `(2, 2, 1)`, y escribir, con
la campana y el producto de densidades, las densidades de lo recibido bajo las
dos hipótesis.

**Qué hace falta saber antes:** escenas 01 a 04; del capítulo 7, la campana de
Gauss, la independencia y que las exponenciales se multiplican sumando los
exponentes (se recuerdan aquí).

**Visual:**
- Tres barras azules: `s[0] = 2`, `s[1] = 2`, `s[2] = 1`, con el rótulo «la señal
  objetivo, conocida».
- Debajo, tres campanas de ruido (magenta) centradas en cero y una fórmula
  `H₀: R[n] = W[n]`, `H₁: R[n] = s[n] + W[n]` construida pieza a pieza.
- La densidad de una campana centrada en cero: «constante · e^{−x²/2σ²}»; el
  producto de tres: se multiplican las constantes y se suman los exponentes.
- Dos fórmulas apiladas: «f(r|H₀) = c · e^{−Σ r²[n] / 2σ²}» y «f(r|H₁) = c · e^{−Σ
  (r[n] − s[n])² / 2σ²}», con la diferencia `r − s` resaltada.
- Un recordatorio: «σ² = 1».

## Narración

<!-- b1 -->
Vamos al caso concreto. El radar manda un pulso que conocemos de antemano:
tres muestras, de valores dos, dos y uno. Lo llamamos la señal objetivo, y se
escribe ese de ene. Si hay un avión, lo recibido es ese pulso más ruido, muestra
a muestra. Si no, solo ruido. En total, tres números recibidos: erre de cero,
erre de uno y erre de dos.

<!-- b2 -->
Sobre el ruido suponemos dos cosas. Primera: en cada muestra es una campana de
Gauss centrada en cero, con varianza sigma cuadrado, que aquí vale uno.
Segunda: cada muestra es independiente de las demás. Por lo que vimos en el
capítulo siete, eso significa que la densidad conjunta es el producto de las
densidades de cada una.

<!-- b3 -->
Recuerda la campana centrada en cero: una constante por e elevado a menos equis
al cuadrado entre dos sigma cuadrado. Si multiplicamos tres, las constantes se
multiplican y los exponentes, como siempre con potencias del mismo número, se
suman. Bajo la hipótesis cero solo recibimos ruido, así que la densidad de lo
recibido es esa constante por e elevado a menos la suma de los cuadrados de lo
recibido, entre dos sigma cuadrado.

<!-- b4 -->
Bajo la hipótesis uno, cada muestra es la señal más ruido. Es una campana igual,
pero centrada en ese de ene en lugar de en cero. La densidad tiene la misma
constante y el mismo exponente, con una diferencia: dentro del cuadrado aparece lo
recibido menos la señal. Es lo que queda del ruido una vez quitada la señal.

<!-- b5 -->
Esas son las dos densidades. La regla que ya conocemos nos pide compararlas,
cada una multiplicada por su probabilidad a priori. Y aquí viene lo bonito:
como son exponentes con sumas, casi todo lo que hay dentro va a desaparecer.
Hagamos la cuenta entera, paso a paso, a ver qué queda.

---

# Escena 06 — LaCuenta

**Objetivo:** hacer la derivación completa, un paso por renglón: comparar,
tomar logaritmo, desarrollar el cuadrado, cancelar `Σ r²`, y llegar a `g = Σ r s`
contra un umbral. Comprobarlo con dos casos numéricos y leer `g` como «cuánto se
parece lo recibido a la señal».

**Qué hace falta saber antes:** escena 05; de matemáticas, el logaritmo
natural (se recuerda aquí); del capítulo 7, el producto escalar.

**Visual:**
- La desigualdad `p₁ f(r|H₁) ≷ p₀ f(r|H₀)` con las dos densidades sustituidas.
- Renglón 1: las constantes iguales se tachan.
- Renglón 2: «ln» aparece a ambos lados. Recordatorio: «ln(eˣ) = x» y «si a > b,
  ln a > ln b».
- Renglón 3: `(r − s)² = r² − 2rs + s²`, los tres términos con colores; `Σ r²`
  aparece a los dos lados y se tacha con una línea roja.
- Renglón 4: queda `ln p₁ + Σ(2rs − s²)/2σ² ≷ ln p₀`; se multiplica por `σ²` y se
  ordena.
- El resultado enmarcado: «g = Σ r[n] s[n] ≷ γ = σ² ln(p₀/p₁) + E/2».
- Dos comprobaciones: con `r = (3, 1, 2)`, «g = 3·2 + 1·2 + 2·1 = 10 > 4,5 →
  hay señal»; con `r = (0,5; −1; 1)`, «g = 1 − 2 + 1 = 0 < 4,5 → solo ruido».

## Narración

<!-- b1 -->
Empezamos por la regla: hay señal si la densidad de la hipótesis uno, por su a
priori, es mayor que la de la hipótesis cero por la suya. Sustituimos las
dos densidades. La constante es la misma a los dos lados, así que se
cancela. Nos quedan dos exponenciales comparadas, cada una por su a priori.

<!-- b2 -->
Ahora un truco: tomar logaritmos naturales. El logaritmo es la operación
inversa de la exponencial: el logaritmo de e elevado a algo es ese algo. Y si un
número es mayor que otro, su logaritmo también lo es, así que la comparación se
conserva. Las exponenciales desaparecen y queda una comparación de sumas.

<!-- b3 -->
Desarrollemos el cuadrado de la hipótesis uno. Recibido menos señal, al
cuadrado, es recibido al cuadrado, menos dos por recibido por señal, más señal
al cuadrado. Y mira: la suma de los cuadrados de lo recibido aparece a los dos
lados de la desigualdad. Aparece igual en las dos hipótesis, así que se
cancela.

<!-- b4 -->
Queda: logaritmo de pe uno, más la suma de dos veces recibido por señal menos
señal al cuadrado, entre dos sigma cuadrado, mayor que logaritmo de pe cero.
Multiplicamos por sigma cuadrado y ordenamos. A la izquierda queda lo único que
depende de lo recibido: la suma de recibido por señal, que llamamos ge. A la
derecha, un umbral, gamma: sigma cuadrado por el logaritmo de pe cero entre pe
uno, más la energía entre dos.

<!-- b5 -->
Compruébalo con números. Si recibimos tres, uno y dos, ge vale tres por dos, más
uno por dos, más dos por uno: diez. Con priors iguales el umbral es cuatro coma
cinco, así que decimos «hay señal». Si recibimos cero coma cinco, menos uno y
uno, ge vale cero. Decimos «solo ruido». Ge mide cuánto se parece lo recibido a
la señal buscada.

---

# Escena 07 — ElUmbral

**Objetivo:** interpretar el umbral `γ = σ² ln(p₀/p₁) + E/2`: la mitad de la energía
cuando los priors son iguales (a mitad de camino entre «no hay señal» y «señal
sin ruido»), y cómo lo desplazan las probabilidades a priori y la varianza del
ruido. Una pregunta con pausa: ¿hacia dónde se mueve el umbral si los aviones
son raros?

**Qué hace falta saber antes:** escena 06.

**Visual:**
- Una recta con `g` y dos marcas: `0` (nada recibido) y `9` (la señal sin ruido:
  `g = E`); el umbral en `4,5`, justo en el medio.
- La fórmula del umbral construida término a término: «σ² ln(p₀/p₁)» en ámbar y
  «E/2» en azul.
- Pregunta con pausa: «¿hacia dónde se mueve si `p₁` baja a 0,2?». Cuenta: «ln(0,8 /
  0,2) = ln 4 = 1,386; 1,386 + 4,5 = 5,886». La marca se corre a la derecha.
- Un deslizador de `p₁` de 0,1 a 0,9: el umbral se mueve; en `p₁ = 0,5` vuelve a 4,5.
- Un deslizador de `σ²`: con ruido pequeño el umbral casi no se mueve; con ruido
  grande sí.
- Tres etiquetas: «Neyman-Pearson», «riesgo mínimo», «MAP» apuntando al mismo
  detector, y una flecha «solo cambia gamma».

## Narración

<!-- b1 -->
Miremos el umbral. Sobre una recta, marquemos dos valores de ge. Si no
recibiéramos nada, ge valdría cero. Si recibiéramos la señal sin ruido, valdría la
suma de los cuadrados de la señal: la energía, que aquí es cuatro más cuatro más
uno, nueve. Con probabilidades iguales, el umbral es la energía entre dos:
cuatro coma cinco, justo a mitad de camino.

<!-- b2 -->
Ahora una pregunta, y piénsala un momento antes de seguir. Si los aviones son
raros, si pe uno baja a cero coma dos, ¿el umbral sube o baja? La cuenta: el
logaritmo de cero coma ocho entre cero coma dos es el logaritmo de cuatro,
uno coma tres ocho seis. El umbral sube a cinco coma ocho ocho seis.

<!-- b3 -->
Tiene sentido. Si los aviones son raros, hay que pedirle más evidencia al radar
antes de creerle. Y si los aviones fueran muy frecuentes, el logaritmo sería
negativo, el umbral bajaría y bastaría con menos evidencia. Con priors iguales,
el logaritmo de uno es cero y volvemos al punto medio.

<!-- b4 -->
La varianza del ruido también pesa. Multiplica al logaritmo. Si el ruido es
muy pequeño, el radar se fía de lo que oye y las probabilidades a priori casi
no importan. Si el ruido es grande, lo que oye vale poco y pesa más lo que sabía
de antemano. El umbral se mueve más.

<!-- b5 -->
Una advertencia importante. Hemos derivado esto con la regla de error mínimo.
Pero en el capítulo de pruebas de hipótesis vimos otros criterios: Neyman-Pearson,
riesgo mínimo. Con un ruido como este, todos llevan al mismo detector, calcular
ge y compararlo. Lo único que cambia es dónde se pone el umbral. Veamos por qué.

---

# Escena 08 — UnNumeroQueBasta

**Objetivo:** ver geométricamente que `g` no tira información: la parte del ruido
perpendicular a `s` es igual bajo las dos hipótesis, así que no informa. Ver
también que la razón de verosimilitud es creciente en `g`, y por eso cualquier
criterio lleva a `g ≷ γ`. Cerrar la promesa «más datos no bastan» (escena 04).

**Qué hace falta saber antes:** escenas 04 y 06; del capítulo 7 (escenas 25 a 27),
el producto escalar como longitud por longitud por coseno y la proyección
(«sombra») de una flecha sobre otra.

**Visual:**
- Las tres muestras de `r` como una flecha en un espacio de tres dimensiones, y
  `s` como otra flecha fija. La sombra de `r` sobre `s`, y lo que queda: la parte
  perpendicular.
- Una esfera de ruido alrededor de la punta de `s` (bajo `H₁`) y otra alrededor
  del origen (bajo `H₀`). Se corta con un plano perpendicular a `s`: en el plano,
  las dos nubes son idénticas.
- La fórmula «r = (g / ‖s‖²) s + r_⊥» con `g = r·s`.
- El cociente «Λ = f₁ / f₀ = e^{(2g − E) / 2σ²}»; una gráfica de `Λ` contra `g`
  siempre creciente, con un umbral `η` que corta en `γ`.
- Una etiqueta «estadístico suficiente».
- Regreso a las dos mediciones de la escena 04: «el promedio no era suficiente;
  ge sí».

## Narración

<!-- b1 -->
¿Por qué ge basta? Piensa en lo recibido como una flecha con tres números, y en
la señal como otra flecha fija. Del capítulo siete: el producto escalar de las
dos, que es justo ge, dice cuánto de una flecha cae en la dirección de la otra.
Es la longitud de su sombra sobre la señal, multiplicada por la longitud de la
señal.

<!-- b2 -->
Cualquier flecha se descompone en dos partes: la que va en la dirección de la
señal y la que es perpendicular a ella. Ge es la parte paralela. ¿Qué pasa con
la perpendicular? Sale solo del ruido. Y el ruido gaussiano no distingue
direcciones: es una nube esférica. La señal la desplaza en la dirección de
la señal, y en los planos perpendiculares las dos nubes son idénticas.

<!-- b3 -->
Es decir: la parte perpendicular tiene exactamente la misma distribución si hay
avión o no. No aporta nada para decidir. Tirarla no cuesta nada. Todo lo que
sirve está en ge. Eso es lo que significa ser un estadístico suficiente: un
resumen que contiene toda la información relevante, ni más ni menos. Y ya vimos
la señal de esto en la cuenta: la suma de cuadrados se canceló.

<!-- b4 -->
Segunda pregunta: ¿por qué con otros criterios sigue valiendo? Recuerda la
razón de verosimilitud del capítulo nueve: el cociente de las dos densidades.
Aquí vale e elevado a dos ge menos la energía, entre dos sigma cuadrado. Es una
función siempre creciente de ge. Comparar ese cociente con un umbral es lo mismo
que comparar ge con otro umbral.

<!-- b5 -->
Así que Neyman-Pearson, riesgo mínimo o error mínimo dan el mismo detector.
Solo cambia dónde se pone la marca. Y ahora el bucle del episodio: el promedio
de las dos mediciones tiraba información; ge no tira nada. La diferencia es que
ge sale de mirar cómo es el ruido, no de un resumen a ojo. Solo falta saber
cuánto vamos a fallar.

---

# Escena 09 — DosCampanas

**Objetivo:** calcular a mano la distribución de `g` bajo cada hipótesis: una
campana centrada en 0 y otra en `E`, ambas con desvío `σ√E`. Con `s = (2, 2, 1)`:
0 y 9, desvío 3. Reducir el problema a «separar dos campanas».

**Qué hace falta saber antes:** escena 06 (`g`); del capítulo 7, la combinación
lineal de gaussianas independientes es gaussiana y cómo se calculan su media y
su varianza (se recuerda aquí).

**Visual:**
- `g = 2 W₀ + 2 W₁ + 1 W₂` bajo `H₀`, con cada `W` como una campana pequeña.
- Cuenta de la media («0 + 0 + 0») y de la varianza: «2² + 2² + 1² = 9», con la
  regla «multiplicar por 2 multiplica la varianza por 4» y «las varianzas de
  independientes se suman».
- Una campana centrada en 0 con desvío 3 (`H₀`, magenta).
- Bajo `H₁`: «g = Σ (s + W) s = E + Σ W s»; la campana se desplaza a 9 (azul), mismo
  ancho.
- Las dos campanas juntas, la marca del umbral en 4,5, y la flecha «distancia
  E = 9».
- Fórmulas generales: «desvío σ√E» y «medias 0 y E».

## Narración

<!-- b1 -->
Recuerda de dónde viene ge: es la suma de recibido por señal. Queremos saber
cómo se reparte. Empecemos por la hipótesis cero, donde solo hay ruido. Ahí,
ge vale dos veces el ruido de la primera muestra, más dos veces el de la
segunda, más una vez el de la tercera. Una combinación de campanas
independientes.

<!-- b2 -->
Del capítulo siete: una combinación de gaussianas independientes es otra
gaussiana. Solo falta su media y su varianza. La media es cero, porque cada
ruido tiene media cero. La varianza: multiplicar una variable por dos multiplica
su varianza por cuatro, y las varianzas de variables independientes se suman.
Cuatro más cuatro más uno: nueve, por sigma cuadrado.

<!-- b3 -->
Con sigma cuadrado igual a uno, la varianza es nueve y el desvío, tres. Fíjate
en que nueve es la energía: en general, la varianza de ge es sigma cuadrado por
la energía. Así que bajo la hipótesis cero, ge es una campana centrada en cero,
con desvío sigma por la raíz de la energía.

<!-- b4 -->
Bajo la hipótesis uno, lo recibido es señal más ruido. Al multiplicar por la
señal y sumar, ge vale la suma de los cuadrados de la señal, que es la energía,
más lo mismo que antes: la parte del ruido. Es la misma campana, corrida en
nueve, con el mismo desvío de tres. Dos campanas iguales, una en cero y otra en
nueve.

<!-- b5 -->
Y el umbral, cuatro coma cinco, cae justo en medio. Todo el problema de
detección se ha reducido a separar dos campanas del mismo ancho, cuyos centros
están a una distancia igual a la energía. Es el problema del capítulo nueve con
una medición, solo que ahora la medición es ge. Más energía, más separadas. Más
ruido, más anchas.

---

# Escena 10 — FuncionQ

**Objetivo:** definir la función Q como el área de la cola de la campana
estándar, estandarizar con la resta de la media y la división por el desvío, y
calcular a mano `P_FA` y `P_M` del pulso `(2, 2, 1)` con umbral 4,5 (las dos valen
0,0668). Dar las fórmulas generales.

**Qué hace falta saber antes:** escena 09; del capítulo 7, la campana estándar
(media 0, desvío 1) y que el área bajo la campana vale uno.

**Visual:**
- Las dos campanas de la escena 09. Se sombrea la cola derecha de la de `H₀` más
  allá de 4,5 (falsa alarma, roja) y la cola izquierda de la de `H₁` a la izquierda
  de 4,5 (miss, roja).
- Una campana estándar con la cola desde `x` sombreada: «Q(x)». Una tabla corta: «Q(0)
  = 0,5», «Q(1) = 0,16», «Q(1,5) = 0,0668», «Q(2) = 0,023», «Q(3) = 0,00135».
- Estandarizar: «(4,5 − 0) / 3 = 1,5»: la campana de `H₀` se encoge y se centra; la
  marca del umbral cae en 1,5.
- Segunda cuenta: «(9 − 4,5) / 3 = 1,5»; se refleja la campana de `H₁` para que la
  cola izquierda pase a derecha.
- Las fórmulas construidas pieza a pieza: «P_FA = Q(γ / σ√E)» y «P_M = Q((E − γ) / σ√E)».
- Un contador de simulación: «1.000.000 de pruebas → 0,0667».

## Narración

<!-- b1 -->
¿Cuánto nos equivocamos? Una falsa alarma ocurre cuando estamos en la campana de
la hipótesis cero y ge sale por encima del umbral: es el área de la cola
derecha. Un fallo ocurre cuando estamos en la campana de la hipótesis uno y ge
sale por debajo: el área de la cola izquierda. Las dos probabilidades son áreas.

<!-- b2 -->
Para calcularlas hay una herramienta. Cualquier campana se convierte en la
campana estándar, de media cero y desvío uno, restando la media y dividiendo
entre el desvío. El área de la cola de la campana estándar, a partir de un punto
equis, se llama función cu de equis. No tiene fórmula sencilla: se mira en una
tabla o se calcula.

<!-- b3 -->
Algunos valores para ubicarnos. Cu de cero vale un medio: la mitad de la campana.
Cu de uno, cero coma dieciséis. Cu de uno coma cinco, cero coma cero seis seis
ocho. Cu de tres, menos de dos milésimas. Cuanto más lejos, más pequeña la cola,
y cae muy deprisa.

<!-- b4 -->
Ahora la falsa alarma. El umbral es cuatro coma cinco y la campana está
centrada en cero con desvío tres. Estandarizamos: cuatro coma cinco menos cero,
entre tres, es uno coma cinco. Falsa alarma igual a cu de uno coma cinco: cero
coma cero seis seis ocho. Con el fallo hacemos lo mismo: nueve menos cuatro coma
cinco, entre tres, otra vez uno coma cinco.

<!-- b5 -->
Por la simetría de la campana, las dos colas son iguales. Con probabilidades
iguales, nos equivocamos un seis coma siete por ciento: unas siete de cada cien
veces. En general, la falsa alarma es cu de gamma entre sigma raíz de e, y el
fallo, cu de e menos gamma, entre lo mismo: cuentan los desvíos del umbral a
cada centro. Un millón de simulaciones da cero coma cero seis seis siete.

---

# Escena 11 — ElPrior

**Objetivo:** hacer la cuenta completa con `p₁ = 0,2` (umbral 5,886): la falsa
alarma baja, el miss sube y la probabilidad de error es 0,0498; comparar con el
umbral de priors iguales (0,0668) para ver que usar el prior importa.

**Qué hace falta saber antes:** escenas 07 y 10.

**Visual:**
- Las dos campanas con la marca del umbral moviéndose de 4,5 a 5,886; las colas se
  redimensionan: la roja izquierda (miss) crece, la de falsa alarma (derecha)
  encoge.
- Dos cuentas paralelas: «5,886 / 3 = 1,962 → Q = 0,0249» y «(9 − 5,886) / 3 = 1,038
  → Q = 0,1497».
- La media ponderada: «0,8 · 0,0249 + 0,2 · 0,1497 = 0,0199 + 0,0299 = 0,0498».
- Comparación con el umbral 4,5: «0,8 · 0,0668 + 0,2 · 0,0668 = 0,0668».
- La frase «mismo detector, otra marca».

## Narración

<!-- b1 -->
Volvamos al radar donde los aviones son raros: pe uno igual a cero coma dos. Ya
vimos que el umbral sube a cinco coma ocho ocho seis. En las dos campanas, la
marca se desplaza hacia la derecha. Veamos qué le pasa a cada error.

<!-- b2 -->
La falsa alarma: cinco coma ocho ocho seis entre tres es uno coma nueve seis
dos. Cu de eso vale cero coma cero dos cuatro nueve. Bajó de casi siete por
ciento a poco más de dos y medio: con el umbral más alto, es más difícil que el
ruido solo lo cruce.

<!-- b3 -->
El fallo: nueve menos cinco coma ocho ocho seis, entre tres, es uno coma cero
tres ocho. Cu de eso vale cero coma uno cuatro nueve siete. Subió a un quince por
ciento: ahora la señal, que sí estaba, se queda a veces por debajo. Un detector
más conservador: da menos falsas alarmas y pierde más aviones.

<!-- b4 -->
La probabilidad de error es la media ponderada: cero coma ocho por cero coma
cero dos cuatro nueve, más cero coma dos por cero coma uno cuatro nueve siete.
Cero coma cero uno nueve nueve, más cero coma cero dos nueve nueve: casi cinco
por ciento.

<!-- b5 -->
¿Y si hubiéramos dejado el umbral en cuatro coma cinco? Cada probabilidad
seguiría valiendo cero coma cero seis seis ocho, y el error sería seis coma siete
por ciento. Peor que el cinco por ciento. Es el mismo detector, calcular ge y
compararlo; solo hemos movido la marca, usando lo que sabíamos de antemano. Y
rebaja el error.

---

# Escena 12 — CurvaRoc

**Objetivo:** el caso en que no se conocen las probabilidades a priori (radar):
Neyman-Pearson. Fijar `P_FA = 0,01`, obtener el umbral con la inversa de Q
(6,979) y la probabilidad de detección (0,75); mover el umbral para trazar la
curva ROC y ver que depende de `d = √E/σ`.

**Qué hace falta saber antes:** escenas 09 a 11; del capítulo 9, la probabilidad
de detección y la ROC (se recuerdan aquí).

**Visual:**
- Un radar y una pregunta: «¿cuántos aviones hay? no lo sé». Se sustituye el a
  priori por una cota: «P_FA ≤ 1 %».
- La inversa de `Q`: «Q(x) = 0,01 → x = 2,33»; una campana estándar con la cola de
  1 % sombreada. Umbral: «γ = σ√E · 2,33 = 3 · 2,33 = 6,98».
- Detección: la campana de `H₁` con el área a la derecha del umbral sombreada en
  verde, «(6,98 − 9) / 3 = −0,67 → P_D = 0,75».
- El umbral se desliza de derecha a izquierda; en el plano `P_FA`-`P_D` un punto
  traza la curva ROC. La diagonal (azar) y la esquina superior izquierda (ideal).
- «P_D = Q(Q⁻¹(P_FA) − d)», con `d = √E / σ = 3`; para `d = 1` y `d = 5` otras curvas.

## Narración

<!-- b1 -->
Hay un problema con lo anterior. Para poner el umbral hacía falta saber la
probabilidad de que haya un avión. ¿Y si no la sabemos? En un radar, ¿cuántos
aviones vendrán hoy? Del capítulo nueve: criterio de Neyman-Pearson. Se fija
cuántas falsas alarmas se toleran, por ejemplo un uno por ciento, y se busca el
umbral que detecta más aviones con esa condición.

<!-- b2 -->
Buscamos el umbral que deja un uno por ciento de cola en la campana de la
hipótesis cero. Necesitamos la operación inversa de cu: dado un área, qué
punto la deja. Para un uno por ciento, ese punto es dos coma tres tres desvíos.
Así que el umbral vale tres por dos coma tres tres: seis coma nueve ocho.

<!-- b3 -->
Ahora, ¿cuántos aviones detectamos con ese umbral? Es el área a la derecha de
seis coma nueve ocho en la campana centrada en nueve. Estandarizamos: seis coma
nueve ocho menos nueve, entre tres, es menos cero coma seis siete. El área a
la derecha es cero coma siete cinco. Detectamos tres de cada cuatro aviones,
con solo un uno por ciento de falsas alarmas.

<!-- b4 -->
Ahora desliza el umbral de derecha a izquierda. Cada posición es un punto:
falsa alarma en un eje, detección en el otro. Con el umbral muy a la derecha,
no detectamos nada; con el umbral muy a la izquierda, lo detectamos todo, con
todas las falsas alarmas. Los puntos dibujan una curva: la curva ROC. Cuanto más
cerca de la esquina de arriba a la izquierda, mejor.

<!-- b5 -->
Y esta curva depende de un solo número: la distancia entre las dos campanas
medida en desvíos, la raíz de la energía entre sigma. Aquí, tres. Con un valor
mayor, la curva se pega a la esquina. La detección vale cu de la inversa de
cu de la falsa alarma, menos ese número. Para detectar más sin más falsas alarmas,
hay que subir la energía o bajar el ruido.

---

# Escena 13 — SoloLaEnergia

**Objetivo:** el resultado central de la primera mitad: con ruido blanco el
error solo depende de `E/σ²`, no de la forma de la señal. Comparar `(2, 2, 1)` con
`(3, 0, 0)` (misma energía, mismo error). Ver el efecto de duplicar la energía y
la letra chica de «más rápido que exponencial». Anunciar que con ruido con
memoria esto cambiará.

**Qué hace falta saber antes:** escenas 09 a 12.

**Visual:**
- Dos pulsos, `(2, 2, 1)` y `(3, 0, 0)`, con la energía «9» debajo de cada uno.
- Pregunta con pausa: «¿cuál se detecta mejor?». Debajo de cada uno, las dos
  campanas (idénticas: 0 y 9, desvío 3) y `P_e = 0,0668` en ambas.
- Definición: «relación señal-ruido = E / σ²» sobre una barra que se llena.
- La fórmula de la probabilidad de error de priors iguales: «P_e = Q(√E / 2σ)».
- Duplicar `E`: «E = 18 → √18 / 2 = 2,12 → Q = 0,017». Barra a la mitad de tamaño.
- Una advertencia: «con ruido blanco».
- Dos ejes: `Q` contra `√E/σ` (cae como una campana) y contra `E/σ²` (cae como
  una exponencial).

## Narración

<!-- b1 -->
Fíjate en algo curioso: en todas las fórmulas solo aparecen la energía y la
varianza del ruido. Ninguna muestra concreta de la señal. Pregunta, y piénsala
un momento: tenemos el pulso dos, dos, uno, y otro pulso que es un solo destello
de tres en una muestra y ceros en las demás. Los dos tienen energía nueve. ¿Cuál
se detecta mejor?

<!-- b2 -->
Hagamos la cuenta del destello. Ge es tres por lo recibido en la primera
muestra. Bajo la hipótesis cero, media cero y desvío tres. Bajo la hipótesis
uno, media nueve y desvío tres. Son las mismas dos campanas, el mismo umbral, el
mismo error: cero coma cero seis seis ocho. Da igual. Un pulso extendido y un
destello dan el mismo error.

<!-- b3 -->
Es el resultado central. Con ruido blanco, el error depende solo de un cociente:
la energía de la señal entre la varianza del ruido, que llamamos relación
señal-ruido. Con priors iguales, la probabilidad de error es cu de la raíz de la
energía entre dos sigma. La forma de la señal no importa. Guarda esto: es
verdad con ruido blanco. Más adelante lo vamos a matizar.

<!-- b4 -->
¿Cuánto mejora el error con más energía? Duplicamos la energía, de nueve a
dieciocho. La raíz de dieciocho entre dos es dos coma doce, y cu de dos coma doce
vale cero coma cero uno siete. Con el doble de energía, el error pasa de casi
siete de cada cien a menos de dos de cada cien.

<!-- b5 -->
Se suele decir que el error cae más rápido que una exponencial, y tiene letra
chica. Como función de la raíz de la energía entre sigma, cu cae como una
campana, más deprisa que cualquier exponencial. Como función de la relación
señal-ruido, la energía entre la varianza, cae esencialmente como una
exponencial. Son dos formas de mirar la misma curva.

---

# Escena 14 — ElFiltroAlReves

**Objetivo:** ver que `g` se puede calcular con un filtro LTI cuya respuesta al
impulso es la señal invertida en el tiempo. Recordar la convolución (dar la vuelta,
deslizar, multiplicar, sumar) y hacerla a mano con `r = (3, 1, 2)` y `h = (1, 2, 2)`:
sale `(3, 7, 10, 6, 4)`, y el tercer valor es `g`. Nombrar el filtro adaptado y
explicar el retardo.

**Qué hace falta saber antes:** escena 06 (`g`); del capítulo 10 (escena 25), la
convolución; de Señales y Sistemas, la respuesta al impulso (se recuerda aquí).

**Visual:**
- Un bloque «filtro» con la entrada `r` desfilando y la respuesta al impulso `h`
  «lo que sale si entra un solo 1»: se ven las barras de `h`.
- La convolución como «dar la vuelta a h, deslizarla, multiplicar y sumar»: se
  anima `h` invertida deslizando sobre `r`, con los productos apareciendo.
- Pregunta: «¿qué `h` hace que salga `Σ r s`?». Respuesta: `h` invertida coincide
  con `s`, es decir `h = (1, 2, 2)`.
- La tabla de la salida `y[0..4]` con cada cuenta escrita: «3·1 = 3», «3·2 + 1·1 =
  7», «3·2 + 1·2 + 2·1 = 10» (resaltada), «1·2 + 2·2 = 6», «2·2 = 4».
- El diagrama: «r[n] → h → muestrear en n = 2 → comparar con γ → H₁ / H₀» y la etiqueta
  «filtro adaptado (matched filter)».
- Nota: «el libro lo escribe sin retardo: h[k] = s[−k], muestrear en 0».

## Narración

<!-- b1 -->
Ya sabemos qué calcular: ge, la suma de recibido por señal. Falta saber cómo se
calcula en la práctica, y ahí entra un filtro. Recuerda cómo actúa un filtro:
tiene una respuesta al impulso, que es lo que sale si entra un único uno. Y para
cualquier entrada, la salida se calcula dando la vuelta a esa respuesta,
deslizándola sobre la entrada, multiplicando y sumando.

<!-- b2 -->
Entonces la pregunta es: ¿qué respuesta hace que, en algún instante, salga
justo ge? La convolución da la vuelta a la respuesta. Nosotros queremos que
cada muestra recibida se multiplique por su muestra de señal. Para eso, la
respuesta, una vez dada la vuelta, tiene que ser la señal. Es decir: la
respuesta al impulso es la señal invertida en el tiempo.

<!-- b3 -->
Con números. La señal es dos, dos, uno; su inversa, uno, dos, dos. Lo recibido
es tres, uno, dos. Salida en el instante cero: tres por uno, tres. En el uno:
tres por dos, más uno por uno, siete. En el dos: tres por dos, más uno por dos,
más dos por uno, diez. Luego seis y cuatro.

<!-- b4 -->
Mira el tercer valor: diez. Es justo el ge que calculamos antes. Ocurre en el
instante dos, que es cuando todo el pulso ya ha entrado en el filtro: hay un
retardo de dos muestras. El libro lo escribe sin retardo; es el mismo número
con el reloj corrido. Este filtro se llama filtro adaptado a la señal.

<!-- b5 -->
Así que el detector completo es una cadena sencilla: la señal recibida entra
en el filtro adaptado, se toma la salida en el instante en que ha entrado todo
el pulso, y se compara con el umbral. Sí o no. Y queda una pregunta: ¿por qué
funciona tan bien? Hay dos formas de verlo: en el tiempo y en la frecuencia.

---

# Escena 15 — ElPicoEsLaAutocorrelacion

**Objetivo:** primera lectura del filtro adaptado, en el tiempo: si a la entrada
solo está la señal limpia, la salida es su autocorrelación (determinista); con
`(2, 2, 1)` sale `(2, 6, 9, 6, 2)`, con el pico igual a la energía. Ver por qué
se muestrea en el pico: la señal contribuye al máximo y el ruido igual en
cualquier instante.

**Qué hace falta saber antes:** escena 14; del capítulo 10, la autocorrelación
(se recuerda aquí).

**Visual:**
- La misma cadena de la escena 14 con la señal limpia `(2, 2, 1)` a la entrada.
- La tabla de la salida: «2·1 = 2», «2·2 + 2·1 = 6», «2·2 + 2·2 + 1·1 = 9», «2·2 +
  1·2 = 6», «1·2 = 2». Aparece un pico en el medio.
- Una imagen de la señal y de una copia desplazada; en el desplazamiento cero,
  cada barra se multiplica por sí misma: «2² + 2² + 1² = 9 = E».
- Las tres marcas del pico: «9», «6», «2», con el ruido como una franja
  del mismo ancho en los tres instantes.
- Una lupa sobre el nombre: «autocorrelación determinista (sin promedios)».
- Una alarma que suena solo en el pico: «un detector de parecidos».

## Narración

<!-- b1 -->
Primera lectura, en el tiempo. Imagina que a la entrada del filtro no hay ruido:
solo la señal, dos, dos, uno, pasando por el filtro uno, dos, dos. Calculamos la
salida igual que antes. Instante cero: dos por uno, dos. Instante uno: dos por
dos, más dos por uno, seis. Instante dos: dos por dos, más dos por dos, más uno
por uno, nueve.

<!-- b2 -->
Y los dos últimos: dos por dos, más uno por dos, seis; uno por dos, dos. La
salida es dos, seis, nueve, seis, dos: un pico en el medio, y ese pico vale nueve,
que es justo la energía. Cada valor compara la señal con una copia suya
desplazada: se multiplican y se suman.

<!-- b3 -->
Eso es una autocorrelación, la misma idea del capítulo diez, aunque aquí sin
promedios: la señal es una sola y la conocemos. Y el pico ocurre sin desplazar:
cada muestra se multiplica por sí misma, y la suma de cuadrados es la energía.
Con cualquier desplazamiento, las barras dejan de coincidir y la suma baja.

<!-- b4 -->
Aquí está la razón de muestrear en el pico. En ese instante, la contribución de
la señal es máxima: nueve, contra seis o dos en los vecinos. La contribución del
ruido, en cambio, es del mismo tamaño en cualquier instante. Así que en el
pico, la señal destaca lo más posible sobre el ruido.

<!-- b5 -->
Por eso el filtro adaptado es un detector de parecidos. Se queda tranquilo
mientras lo que entra no se parece a la señal buscada, y da un pico cuando aparece
algo que sí se le parece, y el pico crece con lo parecido que sea. Ahora, veamos
la misma idea en el mundo de las frecuencias.

---

# Escena 16 — LaLecturaEnFrecuencia

**Objetivo:** segunda lectura, en la frecuencia: el filtro adaptado tiene la
respuesta en frecuencia conjugada de la señal; el módulo acentúa las frecuencias
donde la señal tiene contenido y la fase (opuesta) alinea todas las componentes
en el instante de muestreo, mientras el ruido, de fase aleatoria, no se suma.

**Qué hace falta saber antes:** escena 14; de Señales y Sistemas, que una señal
es suma de sinusoides con amplitud y fase; del capítulo 11 (escena 29), los
números complejos como flechas con módulo y ángulo.

**Visual:**
- Tres sinusoides de frecuencias distintas y desfases distintos, sumadas: una forma
  irregular; luego, cada una como una flecha que gira con longitud y ángulo.
- Tres flechas de longitud 1 con ángulos 0°, 120° y 240°: se suman y dan 0. Luego
  las tres giran hasta alinearse: suman 3.
- La respuesta en frecuencia: «H = S conjugada»: módulo igual, ángulo cambiado de
  signo. Cada flecha de la señal pasa por el filtro y gira el ángulo contrario al
  suyo.
- El espectro de la señal (un bulto) y la ganancia del filtro con el mismo bulto:
  acentúa donde hay señal.
- Flechas de ruido con ángulos al azar: tras el filtro siguen desordenadas y se
  suman en una flecha corta.
- Un lema: «mismo filtro, dos lecturas».

## Narración

<!-- b1 -->
Segunda lectura, en la frecuencia. De Señales y Sistemas: cualquier señal es una
suma de sinusoides. Cada una tiene una amplitud y una fase, es decir, un
desplazamiento. Como en el capítulo once, podemos dibujar cada sinusoide como una
flecha con una longitud, la amplitud, y un ángulo, la fase.

<!-- b2 -->
Ahora, ¿qué haría falta para que todas esas sinusoides se sumaran lo más posible
en el instante de muestreo? Que sus flechas apuntaran en la misma dirección.
Con números: tres flechas de longitud uno, en ángulos cero, ciento veinte y
doscientos cuarenta grados, se cancelan: suman cero. Alineadas, suman tres.

<!-- b3 -->
Eso es lo que hace el filtro adaptado. Su respuesta en frecuencia es la
conjugada de la transformada de la señal: mismo módulo, pero el ángulo
cambiado de signo. Cada flecha de la señal, al pasar por el filtro, gira justo
el ángulo contrario al suyo y queda apuntando a cero. Todas alineadas: se
suman al máximo.

<!-- b4 -->
Y el módulo hace su parte: el filtro amplifica las frecuencias donde la señal
tiene contenido y atenúa donde no lo tiene. El ruido blanco es plano: tiene lo
mismo en todas las frecuencias. Así que amplificar donde está la señal gana señal
sin ganar tanto ruido.

<!-- b5 -->
¿Y el ruido? Sus flechas tienen ángulos al azar. Al girarlas, siguen sin
apuntar al mismo sitio, así que no se suman: se quedan en una flecha corta.
Las dos lecturas dicen lo mismo: en el tiempo, el filtro busca parecidos; en la
frecuencia, pone la señal en fase consigo misma y deja al ruido desordenado.

---

# Escena 17 — NadieLaSupera

**Objetivo:** demostrar que el filtro adaptado maximiza la relación señal-ruido
de salida entre todos los filtros, sin suponer que el ruido sea gaussiano, con la
parábola de Cauchy-Schwarz (cuarta aparición), y ver que el máximo `E/σ²` es el de
entrada: el adaptado no pierde nada. Comprobarlo con el promediador.

**Qué hace falta saber antes:** escenas 14 a 16; la parábola de la escena 28
del capítulo 7, la 12 del capítulo 10 y la 30 del capítulo 11 (mismo dibujo);
del capítulo 7, la varianza de una combinación lineal.

**Visual:**
- Definición: «relación señal-ruido de salida = (separación de medias)² / varianza»,
  con `media = Σ s h` y `varianza = σ² Σ h²`.
- Ejemplo: `h = (1, 1, 1)`: «media = 5 → 25; varianza = 3 → 25/3 = 8,33»; el
  adaptado: «81 / 9 = 9».
- «¿se puede superar 9?» y la parábola de Cauchy-Schwarz del capítulo 7 (mismo
  dibujo): «Σ (x − λy)² ≥ 0 → (Σx²)λ² − 2(Σxy)λ + Σy² ≥ 0», con las tres parábolas
  (dos cortes, uno, ninguno) y el discriminante.
- «(Σxy)² ≤ (Σx²)(Σy²)» y la sustitución `x = s`, `y = h`: «≤ E/σ²».
- Igualdad: la parábola toca el eje, `h` es un múltiplo de `s`.
- Dos etiquetas: «ruido gaussiano → mínimo error» y «solo blanco → máxima relación
  señal-ruido».
- Un contador: «cuarta vez».

## Narración

<!-- b1 -->
¿Es este el mejor filtro que existe? Y una segunda pregunta: ¿y si el ruido es
blanco, pero no sabemos que sea gaussiano? Entonces no podemos calcular la regla
de error mínimo. Pero podemos medir cuánto separa un filtro las dos hipótesis:
la relación señal-ruido de su salida, la diferencia de medias al cuadrado
dividida entre la varianza.

<!-- b2 -->
Para un filtro cualquiera, la media con señal es la suma de señal por filtro, y
la varianza del ruido es sigma cuadrado por la suma de los cuadrados del
filtro. Prueba con el promediador, uno, uno, uno: media cinco, al cuadrado
veinticinco, varianza tres: ocho coma tres tres. El adaptado da ochenta y uno
entre nueve: nueve.

<!-- b3 -->
¿Existe algún filtro que supere nueve? Y aquí aparece un viejo conocido, por
cuarta vez: la parábola de Cauchy-Schwarz. Toma dos listas de números, equis e
i griega, y un número lambda cualquiera. La suma de equis menos lambda por i
griega, al cuadrado, es una suma de cuadrados: nunca es negativa.

<!-- b4 -->
La desarrollamos y es una parábola en lambda. Nunca baja de cero, así que no
puede cortar el eje dos veces: su discriminante no es positivo. Queda que la
suma de equis por i griega, al cuadrado, no supera la suma de los cuadrados de
equis por la de i griega. Aplicada al filtro: la relación de salida no supera la
energía entre sigma cuadrado.

<!-- b5 -->
La igualdad se da si la parábola toca el eje, es decir, cuando el filtro es un
múltiplo de la señal: el filtro adaptado. Y ese máximo, la energía entre sigma
cuadrado, es la relación señal-ruido que ya había a la entrada: no se pierde
nada. Dos justificaciones independientes: con ruido gaussiano, minimiza el
error; solo con ruido blanco, maximiza la relación señal-ruido.

---

# Escena 18 — CuantoSePierde

**Objetivo:** medir con números cuánto se pierde con filtros que no son el
adaptado: el promediador `(1, 1, 1)` y la muestra suelta. La pérdida es el
coseno al cuadrado del ángulo entre el filtro y la señal. Con `(2, 2, 1)` y con
`(1, −2, 1)`, donde el promediador queda perpendicular y no ve nada. Retomar el
lema «promediar no siempre es buena idea».

**Qué hace falta saber antes:** escenas 04, 08 y 17; del capítulo 7, el
coseno como ángulo entre flechas; del capítulo 11 (escena 21), los decibelios.

**Visual:**
- Tres filtros como barras: el adaptado `(2, 2, 1)`, el promediador `(1, 1, 1)` y
  la muestra suelta `(1, 0, 0)`.
- Para `s = (2, 2, 1)`: «promediador: 25 / 27 = 0,926 (−0,33 dB)», «una muestra:
  4 / 9 = 0,444 (−3,52 dB)». Las flechas `s` y `h` con el ángulo entre ellas y
  «cos² θ» como la fracción que se conserva.
- El error de cada uno: «Q(1,5) = 0,0668», «Q(1,44) = 0,0745», «Q(1) = 0,159».
- Segundo pulso: `s = (1, −2, 1)`, energía 6. El promediador: «1 − 2 + 1 = 0»; las
  flechas forman 90°. Un contador de relación: «0».
- «Una muestra (la del −2): 4/6 = 0,667 (−1,76 dB)».
- El error del promediador con este pulso: `Q(0) = 0,5`, y una moneda.
- Un lema en pantalla: «cualquier desalineación cuesta».

## Narración

<!-- b1 -->
¿Cuánto se pierde con un filtro que no es el adaptado? Comparemos tres. El
adaptado. El promediador, uno, uno, uno, que suma todo lo recibido, como el
promediador del capítulo diez. Y quedarse solo con una muestra, la más grande.
La pérdida de un filtro es el coseno al cuadrado del ángulo entre él y la señal:
la fracción de relación señal-ruido que conserva.

<!-- b2 -->
Con el pulso dos, dos, uno. El promediador da veinticinco entre veintisiete:
cero coma nueve dos seis. Pierde menos de medio decibelio: casi nada. La muestra
suelta da cuatro entre nueve: cero coma cuatro cuatro cuatro. Pierde más de la
mitad, tres coma cinco decibelios.

<!-- b3 -->
Traducido a errores: el adaptado se equivoca cero coma cero seis seis ocho. El
promediador, cero coma cero siete cuatro cinco, apenas más. Pero la muestra
suelta, cu de uno, cero coma uno cinco nueve: más del doble de errores. Tirar
las otras dos muestras, más de la mitad de la energía, sale caro.

<!-- b4 -->
Ahora una sorpresa. Cambia el pulso por uno, menos dos, uno. Tiene energía seis
y es tan detectable como cualquier otro. Pero mira al promediador: uno menos
dos, más uno, cero. Su filtro es perpendicular a la señal: coseno cero. No ve
nada. Su error es cu de cero: un medio, tirar una moneda.

<!-- b5 -->
La muestra suelta, la del menos dos con su signo, aún conserva dos tercios.
Moraleja: cualquier desalineación con la señal cuesta, y puede costarlo todo.
Promediar no siempre es buena idea, como ya vimos con las dos mediciones. Y hay
otra suposición que hemos hecho todo el rato: que el ruido es blanco. ¿Qué pasa si
el ruido tiene memoria?

---

# Escena 19 — LaMemoriaDelRuido

**Objetivo:** ver con dos muestras que, si el ruido tiene memoria, la muestra
vecina delata parte del ruido y el mejor detector ya no es «correlacionar con la
señal». Con el eco del 0,6 y el pulso `(2, 0)`: restar 0,6 veces la segunda
muestra deja varianza 0,64 y mejora el error de 0,1587 a 0,1056.

**Qué hace falta saber antes:** escenas 13 y 18 (ruido blanco); del capítulo 10 y
del 11 (escenas 26 y 27), el ruido que se parece a su muestra anterior (el eco
del 0,6); del capítulo 7, la varianza de una combinación lineal (se recuerda
aquí).

**Visual:**
- Dos muestras de ruido vecinas, `v₀` y `v₁`, como una nube de puntos elíptica
  (inclinada: correlación 0,6), y el eco del 0,6 en una esquina.
- El pulso `s = (2, 0)`: una sola barra en la primera muestra. Recibido: `r₀ = 2 +
  v₀` (bajo `H₁`) y `r₁ = v₁`.
- Detector ingenuo: mirar solo `r₀`: «media 2, varianza 1 → 4 → P_e = Q(1) =
  0,1587».
- La idea: `r₁` nos chiva algo del ruido de `r₀`. Se dibuja `r₀ − 0,6 r₁`.
- La cuenta de la varianza: «1 + 0,36 − 2·0,6·0,6 = 0,64», con cada término
  apareciendo con su regla.
- Resultado: «media 2 → 4 / 0,64 = 6,25 → P_e = Q(1,25) = 0,1056».
- Los pesos `(1, −0,6)` frente a la señal invertida `(2, 0)`: no coinciden.

## Narración

<!-- b1 -->
Hasta ahora, el ruido de cada muestra era independiente del de las demás. Pero
muchos ruidos tienen memoria. Recuerda el eco del cero coma seis: cada muestra se
parece un sesenta por ciento a la anterior. Tomemos dos muestras seguidas de ese
ruido, con varianza uno cada una y una correlación de cero coma seis entre ellas.

<!-- b2 -->
La señal ahora es un pulso de una sola muestra: dos, cero. Bajo la hipótesis uno
recibimos dos más el ruido de la primera muestra, y el ruido de la segunda. El
detector ingenuo mira solo la primera: media dos, varianza uno, relación cuatro.
Su probabilidad de error es cu de uno: cero coma uno cinco ocho siete.

<!-- b3 -->
Pero la segunda muestra no es basura. Como el ruido de la segunda se parece al de
la primera, la segunda nos chiva algo del ruido de la primera. Así que probamos
con una combinación: la primera menos cero coma seis veces la segunda. Si el
ruido de la primera fue alto, el de la segunda probablemente también, y la resta lo
compensa.

<!-- b4 -->
Calculemos su varianza, con la regla del capítulo siete: varianza de una
combinación. Uno, de la primera, más cero coma seis al cuadrado, cero coma tres
seis, de la segunda, menos dos por cero coma seis por cero coma seis, de la
covarianza: cero coma siete dos. Uno más cero coma tres seis menos cero coma siete
dos: cero coma seis cuatro.

<!-- b5 -->
La media sigue siendo dos: el pulso solo está en la primera muestra. Así que la
relación vale cuatro entre cero coma seis cuatro: seis coma dos cinco. Mucho
mejor que cuatro. El error baja de cero coma uno cinco ocho siete a cero coma
uno cero cinco seis. Y fíjate: los pesos del mejor filtro, uno y menos cero coma
seis, no son la señal al revés. La receta cambia.

---

# Escena 20 — BlanquearYAdaptar

**Objetivo:** la receta general: blanquear el ruido primero y aplicar después el
filtro adaptado al pulso blanqueado. Hacerlo entero con las dos muestras y ver
que da el mismo número (6,25). Explicar por qué no se pierde información (el
blanqueador se puede deshacer) y dar la fórmula en frecuencia dicha en palabras.

**Qué hace falta saber antes:** escenas 17 y 19; del capítulo 11 (escena 27), el
blanqueador `x[n] − 0,6 x[n−1]`; escena 04 (el promedio sí tiraba
información porque no se podía deshacer); del capítulo 11 (escena 16), Parseval.

**Visual:**
- La cadena: «ruido con memoria → blanqueador → ruido blanco» con el eco del 0,6
  y «x[n] − 0,6 x[n−1]» del capítulo 11.
- Las dos muestras blanqueadas: «u₀ = v₀ (varianza 1)» y «u₁ = (v₁ − 0,6 v₀) / 0,8
  (varianza 0,64 / 0,64 = 1)». La nube elíptica se convierte en un círculo.
- El mismo blanqueador aplicado a la señal: «p₀ = 2; p₁ = (0 − 0,6·2) / 0,8 = −1,5»;
  barras `(2, −1,5)`.
- Energía del pulso blanqueado: «4 + 2,25 = 6,25»; «→ Q(1,25) = 0,1056»: el mismo
  resultado que con el otro camino.
- Un rótulo en el blanqueador: «se puede deshacer: no tira nada»; comparado con la
  escena 04 (el promedio no se puede deshacer).
- La fórmula por piezas: «H = S* / (D_vv / σ²)», y una gráfica: señal fuerte y
  ruido débil, ganancia alta.
- «la relación = (1/2π) ∫ |S|² / D_vv dΩ», con una nota «Parseval».

## Narración

<!-- b1 -->
La receta general es la que anunciamos en el capítulo once: blanquear primero, y
después aplicar lo que ya sabemos. Recuerda el blanqueador: para el eco del cero
coma seis, restar cero coma seis veces la muestra anterior devolvía una moneda:
ruido blanco. Hagámoslo con las dos muestras.

<!-- b2 -->
La primera queda igual: varianza uno. A la segunda le restamos cero coma seis
veces la primera. La resta tiene varianza cero coma seis cuatro, y no está
correlacionada con la primera. Para que valga uno, dividimos entre cero coma
ocho, la raíz de cero coma seis cuatro. Ahora las dos muestras son independientes,
de varianza uno: ruido blanco.

<!-- b3 -->
Pasamos la señal por el mismo blanqueador. La primera muestra sigue valiendo
dos. La segunda, cero menos cero coma seis por dos, entre cero coma ocho: menos
uno coma cinco. El pulso blanqueado es dos, menos uno coma cinco. Y sobre ruido
blanco ya sabemos qué hacer: el filtro adaptado a ese pulso.

<!-- b4 -->
Su energía es cuatro más dos coma veinticinco: seis coma veinticinco. Es
exactamente la relación de antes. Por los dos caminos, el mismo número. Y no se
pierde información, porque el blanqueador se puede deshacer: a partir de las
muestras blanqueadas puedes recuperar las originales. No es como el promedio, que
tiraba lo que no se puede recuperar.

<!-- b5 -->
En frecuencia, el filtro total tiene una forma muy sensata: la conjugada de la
transformada de la señal, dividida entre la densidad espectral del ruido. Tiene
mucha ganancia donde la señal es fuerte y el ruido débil. Y la relación señal-ruido
es la integral, en todas las frecuencias, del cuadrado de la señal entre la
densidad del ruido. La derivación con matrices está en el apunte.

---

# Escena 21 — DondeVivaLaSenal

**Objetivo:** pagar el bucle de la escena 13: con ruido con memoria la forma de la
señal sí importa. Con dos pulsos de energía 2, `(1, 1)` y `(1, −1)`, y el eco del
0,6: relaciones 1,25 y 5, contra 2 con ruido blanco. Leerlo en frecuencia:
poner la energía donde el ruido es débil.

**Qué hace falta saber antes:** escenas 13, 19 y 20; del capítulo 11, el espectro
de un ruido «lento» (concentrado en bajas frecuencias).

**Visual:**
- Dos pulsos de dos muestras: `(1, 1)` (plano y lento) y `(1, −1)` (alternado y
  rápido), ambos con energía 2.
- La nube elíptica inclinada del ruido, con los ejes: la dirección `(1, 1)` (larga)
  y `(1, −1)` (corta). Sumas y restas: «v₀ + v₁: 1 + 1 + 1,2 = 3,2» y «v₀ − v₁: 1 + 1 −
  1,2 = 0,8».
- Tabla de relaciones: «(1, 1): 4 / 3,2 = 1,25», «(1, −1): 4 / 0,8 = 5», «ruido blanco:
  2». Y los errores: «Q(0,56) = 0,288», «Q(0,71) = 0,240», «Q(1,12) = 0,132».
- El espectro del ruido (un bulto a bajas frecuencias) y los espectros de los dos
  pulsos encima; el área sombreada `|S|²/D`.
- Una advertencia: «con ruido blanco: solo la energía».
- Un cambio de signo: memoria negativa; el bulto pasa a altas frecuencias y el
  pulso `(1, 1)` mejora.

## Narración

<!-- b1 -->
Con ruido blanco, la forma de la señal no importaba: solo la energía. Con ruido
con memoria, sí. Comprobémoslo con dos pulsos de dos muestras y la misma energía,
dos. Uno, uno: no cambia de signo, es lento. Y uno, menos uno: cambia de signo en
cada muestra, es rápido. El ruido, el del eco del cero coma seis, es un ruido
lento.

<!-- b2 -->
¿Cuánto fluctúa el ruido en cada dirección? La suma de las dos muestras tiene
varianza uno más uno, más dos veces cero coma seis: tres coma dos. La resta, uno
más uno, menos uno coma dos: cero coma ocho. Un ruido lento fluctúa mucho a lo
largo de la suma y poco a lo largo de la resta.

<!-- b3 -->
Para el pulso uno, uno, la media es dos, al cuadrado cuatro, entre tres coma
dos: uno coma dos cinco. Para el pulso uno, menos uno, cuatro entre cero coma
ocho: cinco. Con ruido blanco, los dos habrían dado dos. Uno coma veinticinco,
dos, cinco: los errores son cero coma veintinueve, cero coma veinticuatro y cero
coma trece.

<!-- b4 -->
Fíjate en lo que ha pasado: el pulso rápido, con el mismo gasto de energía,
consigue una relación cuatro veces mayor que el lento, porque vive donde el
ruido es débil. En
frecuencia: la relación señal-ruido es la integral del cuadrado de la señal
dividido entre la densidad del ruido. Cada frecuencia de la señal cuenta
menos donde el ruido es fuerte.

<!-- b5 -->
Y con memoria negativa sería al revés: el ruido alterna, y convendría una señal
que no alterne. Es la letra chica de «la forma no importa»: era cierto solo con
ruido blanco. Cuando puedes diseñar la señal, en un radar o en una comunicación,
eliges dónde poner la energía: donde el ruido es más débil.

---

# Escena 22 — RuidoEnLaPractica

**Objetivo:** qué se hace cuando no se conoce la densidad espectral del ruido
ni su varianza: estimarlas de un tramo solo de ruido (Welch o un modelo con
pocos coeficientes), y un umbral que se adapta al nivel de ruido local. Avisar del
precio y anunciar la otra incógnita: el retardo.

**Qué hace falta saber antes:** escenas 19 a 21; del capítulo 11, Welch (episodios
4 y 5) y el filtro modelador del eco del 0,6.

**Visual:**
- Un registro con un tramo «solo ruido» marcado en gris y otro con la señal
  posible.
- Opción 1: el periodograma de trozos promediado (Welch), con la ventana
  deslizante del capítulo 11, y la frase «varianza contra resolución».
- Opción 2: la ecuación «x[n] = a x[n−1] + moneda»; un solo coeficiente `a`
  estimado y el blanqueador «x[n] − a x[n−1]» saliendo directamente.
- Un radar con lluvia: el nivel de ruido sube y baja según la zona; un umbral fijo
  (recta) dispara falsas alarmas donde llueve.
- El umbral recalculado con la varianza de las celdas vecinas: una línea que se
  adapta. La etiqueta «CFAR» solo en pantalla.
- «pérdida: un par de dB».

## Narración

<!-- b1 -->
En la práctica no conocemos el ruido. Ni cómo se reparte en frecuencias, ni cuánto
vale su varianza. ¿Qué se hace? Se graba un tramo en el que seguro no hay señal,
solo ruido, y se aprende de él. Con ese tramo se pueden hacer dos cosas.

<!-- b2 -->
La primera: estimar la densidad espectral del ruido. Ya sabes cómo, del capítulo
once: se parte el registro en trozos, se calcula el periodograma de cada uno y se
promedian, el método de Welch. Con eso se construye el filtro. El precio es el
de siempre: más trozos, menos varianza, pero menos resolución.

<!-- b3 -->
La segunda: ajustar un modelo con pocos coeficientes. Por ejemplo, decir que
cada muestra es un cierto número por la anterior, más una moneda, como en el
eco del cero coma seis. Solo hay que estimar un coeficiente, y el blanqueador sale
directamente: restar ese coeficiente por la muestra anterior. Con registros
cortos, un modelo pequeño casi siempre gana.

<!-- b4 -->
Y si lo único que no conocemos es la varianza del ruido, hay un problema con
el umbral. Imagina un radar donde llueve en una zona: ahí el ruido es mayor, y un
umbral fijo daría falsas alarmas sin parar. La solución es recalcular el umbral
con la varianza estimada en las celdas vecinas, donde no hay avión. Un umbral que
se adapta. Cuesta un par de decibelios.

<!-- b5 -->
Un aviso: el filtro hereda el error de lo que se ha estimado. Un blanqueador
estimado nunca es perfecto, y cuanto más corto el registro, peor. Pero hasta aquí
siempre hemos sabido cuándo llegaba el pulso. Un radar de verdad no lo sabe, y
es justo lo que quiere medir. Ese es el siguiente problema.

---

# Escena 23 — ElEcoQueLlega

**Objetivo:** el retardo desconocido: la salida del filtro adaptado es la
autocorrelación corrida en `D`, y buscar su máximo da el retardo. Hacerlo a mano
con `(2, 2, 1)` con retardo 3: sale `(0, 0, 0, 2, 6, 9, 6, 2, 0, 0)`, pico en 5 =
3 + 2. Ver que el ruido puede correr el máximo y que la amplitud también es
desconocida.

**Qué hace falta saber antes:** escenas 14 y 15; de física, que el radar mide la
distancia con el tiempo de ida y vuelta (se dice aquí).

**Visual:**
- Un radar, un avión lejano y las ondas de ida y vuelta; «1 ms de ida y vuelta =
  150 km» con la cuenta «300.000 km/s · 0,001 s / 2».
- Una línea de tiempo con `D` como incógnita: «¿cuándo llega?».
- El registro sin ruido `(0, 0, 0, 2, 2, 1, 0, 0)`, con el pulso desplazado 3.
- La salida del filtro adaptado `(1, 2, 2)` sobre ese registro, se va llenando:
  `0, 0, 0, 2, 6, 9, 6, 2, 0, 0`; el pico en 5 se resalta.
- Restar el retardo del filtro: «5 − 2 = 3».
- El mismo registro con ruido encima: la salida tiene un pico y otros picos
  parecidos; el máximo cae en un vecino.
- Una etiqueta: «amplitud desconocida (eco lejano, más débil)».

## Narración

<!-- b1 -->
Un radar mide distancias con el tiempo. El pulso sale, choca con el avión y
vuelve; cuanto más tarde en volver, más lejos está. Con la velocidad de la luz,
un milisegundo de ida y vuelta son ciento cincuenta kilómetros. Así que el
retardo del eco no es un dato, es lo que queremos medir.

<!-- b2 -->
Veámoslo con números, sin ruido. Nuestro pulso, dos, dos, uno, llega con un
retardo de tres muestras: el registro es cero, cero, cero, dos, dos, uno, cero, cero.
Lo pasamos por el filtro adaptado, uno, dos, dos. La salida es cero, cero, cero,
dos, seis, nueve, seis, dos, cero, cero. Es la misma autocorrelación de antes,
solo que desplazada.

<!-- b3 -->
El pico está en el instante cinco. Restamos el retardo del propio filtro, dos
muestras, y sale tres: justo el retardo con el que llegó el pulso. En general,
si el eco llega con cierto retardo, la salida es la autocorrelación corrida esas
mismas muestras. Buscamos el máximo de la salida, y su posición nos dice el
retardo.

<!-- b4 -->
Con ruido, la historia se complica. A la salida se le suma ruido, y el máximo
puede caer en una posición vecina: medimos mal el retardo. Y hay un segundo
problema: la amplitud del eco también es desconocida, porque un avión lejano da un
eco más débil. Por eso el umbral no se puede fijar a ojo.

<!-- b5 -->
Todo depende de lo nítido que sea el pico. Si el pico es ancho, con un poco de
ruido el máximo resbala a un vecino y la distancia sale mal. Si es estrecho, no.
Pregunta: ¿qué pulso da el pico más estrecho posible? La respuesta se llama
compresión de pulso.

---

# Escena 24 — PulsoQueSeComprime

**Objetivo:** ver por qué el pulso rectangular da un pico ancho (triángulo) y
plantear el problema de diseño: pulso largo (para tener energía con amplitud
limitada) con autocorrelación estrecha. Presentar la secuencia de Barker de 13 y
sus lóbulos laterales (0 o 1), medir con simulaciones cuánto mejora la
estimación del retardo y explicar el matiz de errores raros pero grandes.

**Qué hace falta saber antes:** escena 23; del capítulo 11 (escena 21), los
decibelios.

**Visual:**
- Un rectángulo de 13 unos. Su autocorrelación como triángulo: «13, 12, 11, 10, …»;
  el pico y su vecino casi iguales: «13 y 12».
- La simulación: dos barras «error: 56 %» (rectangular) y «12 %» (Barker), y «40.000
  simulaciones · energía/varianza 13 · registro de 64».
- La idea: «energía = largo × amplitud; amplitud limitada → pulso largo».
- La secuencia de Barker de 13: `+ + + + + − − + + − + − +`, como barras arriba y abajo.
- Su autocorrelación: pico 13 en el medio y `0, 1, 0, 1, …` a los lados. Un caso a
  mano: «desplazamiento 1: 12 productos, 6 valen +1 y 6 valen −1 → suma 0».
- Decibelios: «20 · log(1/13) = −22 dB» contra «20 · log(12/13) = −0,7 dB».
- Un cuadro: errores del rectangular «frecuentes y pequeños» (raíz del error
  cuadrático 3,5) y de Barker «raros y grandes» (4,9).

## Narración

<!-- b1 -->
Tomemos un pulso rectangular de trece muestras, trece unos. Su autocorrelación
sale sola: al desplazarlo una muestra, coinciden doce; dos, once; y así. Un
triángulo ancho. El pico vale trece, pero el vecino vale doce: casi igual. Con
un poco de ruido, no hay manera de saber cuál es el bueno.

<!-- b2 -->
Las simulaciones lo confirman. Con cuarenta mil pruebas, una relación señal-ruido
de trece y un registro de sesenta y cuatro muestras, el rectangular falla el
retardo exacto cincuenta y seis veces de cada cien. Casi siempre falla por poco,
pero falla.

<!-- b3 -->
Queremos un pulso largo, porque la energía es el largo por la amplitud, y la
amplitud del transmisor está limitada. Pero también queremos una autocorrelación
estrecha: grande en el origen y pequeña en todos los demás desplazamientos. Un
pulso largo que a la salida del filtro se comprime en un pico estrecho. Eso se
llama compresión de pulso.

<!-- b4 -->
Una solución clásica es la secuencia de Barker de trece: más, más, más, más, más,
menos, menos, más, más, menos, más, menos, más. Su autocorrelación vale trece en
el origen y, en cualquier otro desplazamiento, cero o uno. Por ejemplo, con un
desplazamiento: doce productos, seis valen uno y seis valen menos uno. Suma cero.

<!-- b5 -->
El lóbulo lateral más alto es uno, contra un pico de trece: unos veintidós
decibelios por debajo. El rectangular, menos de uno. Con las mismas simulaciones,
Barker falla el retardo exacto doce veces de cada cien. Aunque hay un matiz:
cuando el ruido le gana, salta a un lóbulo lateral lejano, y el error es
grande. Errores raros pero grandes, contra errores frecuentes pero pequeños.

---

# Escena 25 — ChirpYResolucion

**Objetivo:** la segunda forma de comprimir: la señal con barrido de frecuencia
(chirp), que escala a pulsos largos donde no hay Barker. Y lo más importante de
la compresión: la **resolución**. Con dos ecos separados 3 muestras, el
rectangular funde los dos en una meseta de 23 y Barker separa dos picos de 13.

**Qué hace falta saber antes:** escena 24; del capítulo 11, el espectro y la
ventana; de la escena 16, la respuesta en frecuencia.

**Visual:**
- Una sinusoide cuya frecuencia sube poco a poco (un «chirrido»); un espectrograma
  sencillo: una recta que sube. La palabra «chirp» solo en pantalla.
- Su autocorrelación: un pico de un solo desplazamiento de ancho. «64 muestras:
  lóbulos laterales a −21 dB».
- La línea «las secuencias Barker no pasan de 13».
- Dos aviones (dos ecos), separados 3 muestras. Sin ruido. El rectangular: cada
  eco da un triángulo; los dos triángulos se suman y, entre los picos, la salida
  es plana en 23: «13 + 10 = 23», «12 + 11 = 23». Un cartel: «¿uno o dos?».
- Con Barker: dos picos de 13 con un valle entre ellos, cada uno de altura completa.
- La frase: «comprimir = resolver».
- La aclaración: «para decidir si hay o no, con ruido blanco, da lo mismo».

## Narración

<!-- b1 -->
Las secuencias de Barker no pasan de trece. Para pulsos más largos, hay otra
idea: una sinusoide cuya frecuencia va subiendo poco a poco. Un barrido de
frecuencia, un chirrido, lo que se llama un chirp. Como cada tramo tiene una
frecuencia distinta, ningún tramo se parece a otro desplazado, y la
autocorrelación se estrecha.

<!-- b2 -->
Con sesenta y cuatro muestras, el pico ocupa un solo desplazamiento y los lóbulos
laterales quedan unos veintiún decibelios más abajo. Y se puede hacer tan largo
como se quiera, cosa que no pasa con Barker. Pero la ventaja mayor de comprimir
el pulso no es medir mejor un retardo.

<!-- b3 -->
Imagina dos aviones cuyos ecos llegan separados tres muestras. Sin ruido. Con el
pulso rectangular, cada eco da su triángulo, y los dos se suman. Entre los dos
picos, uno suma trece más diez, el siguiente doce más once, y así: veintitrés,
veintitrés, veintitrés. La salida es una meseta. No hay forma de saber si hay
uno o dos aviones.

<!-- b4 -->
Con Barker, cada eco da su pico de trece, y los lóbulos laterales son cero o
uno. A tres muestras de distancia, el lóbulo del vecino vale cero. Así que los
dos picos conservan la altura completa, trece, con un valle claro en medio. Se
ven dos aviones.

<!-- b5 -->
Ahí está la razón de fondo de la compresión de pulso: no es solo precisión en
el retardo, es poder separar objetos cercanos. Y una aclaración: para decidir
solo si hay o no hay señal, con ruido blanco, el rectangular y Barker dan el
mismo error. Ya lo vimos: solo importa la energía. La forma cuenta cuando además
hay que medir cuándo.

---

# Escena 26 — BuscarTienePrecio

**Objetivo:** el coste de buscar el retardo: al probar `N` posiciones, la
probabilidad de que alguna dé falsa alarma es unas `N` veces mayor; con
`N = 1000` y una falsa alarma total de una entre mil, cada posición pide una entre un
millón, el umbral sube de 3,09 a 4,75 desvíos y hacen falta unos 2,8 dB más de
energía para el mismo `P_D`. Nombrar las comparaciones múltiples.

**Qué hace falta saber antes:** escenas 12 y 23; del capítulo 7, la probabilidad
de un suceso pequeño repetido `N` veces (aproximación: `N · p`).

**Visual:**
- 1.000 celdas de distancia en una tira; en cada una, un pequeño dado que
  puede dar falsa alarma. El máximo de las mil salidas se compara con el umbral.
- La cuenta: «probabilidad de al menos una ≈ N · p» con `N = 1000`, `p = 10⁻⁶` →
  «10⁻³».
- La campana de `H₀` con el umbral de una sola posición (3,09 desvíos) y el de mil
  posiciones (4,75): la marca salta a la derecha.
- Las dos campanas de `H₀` y `H₁` con la separación necesaria para `P_D = 0,9`: «d =
  3,09 + 1,28 = 4,37» y «d = 4,75 + 1,28 = 6,03»; los cuadrados «19 y 36».
- «casi el doble de energía: 2,8 dB».
- Una fila de análisis médicos con mil pruebas y una etiqueta «comparaciones
  múltiples».

## Narración

<!-- b1 -->
Volvamos al ruido. Si no conocemos el retardo, hay que probar todas las posiciones
posibles, digamos mil, y quedarnos con el máximo de la salida. Y aquí hay un
problema. Cada posición es una oportunidad de que el ruido, solo, cruce el
umbral y dé una falsa alarma. Cuantas más posiciones, más oportunidades.

<!-- b2 -->
Hagamos la cuenta. Si cada posición tiene una probabilidad pequeña, pe, de falsa
alarma, la probabilidad de que salte al menos una entre ene posiciones es
aproximadamente ene por pe. Queremos una falsa alarma total de una entre mil,
buscando en mil posiciones. Así que cada posición tiene que tener una falsa
alarma de una entre un millón.

<!-- b3 -->
Traducido al umbral. Para una sola posición y una falsa alarma de una entre mil,
la inversa de cu da tres coma cero nueve desvíos. Para una entre un millón, cuatro
coma siete cinco. El umbral tiene que subir casi dos desvíos completos, solo
porque hemos decidido buscar en mil sitios.

<!-- b4 -->
Y eso cuesta señal. Para detectar el noventa por ciento de los aviones, hay que
separar las dos campanas el umbral más uno coma dos ocho desvíos. Con el umbral
de una posición, cuatro coma tres siete. Con el de mil, seis coma cero tres. Al
cuadrado, diecinueve contra treinta y seis: casi el doble de energía, unos dos coma
ocho decibelios.

<!-- b5 -->
Es un fenómeno muy general: si haces muchas pruebas, alguna saldrá positiva por
puro azar, y hay que endurecer el criterio. Se llama el problema de las
comparaciones múltiples. Hasta ahora decidíamos entre «hay señal» y «no hay». ¿Y si
hay varias señales posibles, y hay que decir cuál? Ese es el último episodio.

---

# Escena 27 — VariasSenales

**Objetivo:** discriminar entre `M` señales: repetir la derivación de la escena 06
con `M` hipótesis (la suma de cuadrados es común a **todas** y se cancela), llegar a
`Σ r s_i + σ² ln P(H_i) − E_i/2` y ver que se implementa con `M` filtros adaptados
en paralelo. Comprobarlo con tres señales a mano y un giro: los priors cambian el
ganador.

**Qué hace falta saber antes:** escenas 06 y 14; del capítulo 9, decidir entre más
de dos hipótesis (se recuerda aquí).

**Visual:**
- Tres señales de cuatro muestras: `s₀ = (1, 1, 0, 0)`, `s₁ = (0, 0, 1, 1)`, `s₂ = (1,
  −1, 0, 0)`, cada una con energía 2, como tres pares de barras de colores.
- La derivación de la escena 06 en miniatura, con las mismas piezas: «ln», «(r −
  s_i)²», y «Σ r²» tachada en las `M` hipótesis a la vez.
- El resultado: «elegir la i que maximice Σ r s_i + σ² ln P(H_i) − E_i/2».
- Un diagrama: `r` entrando a tres filtros adaptados en paralelo y un bloque «elegir
  el mayor».
- La cuenta con `r = (0,4; 1; 0,9; 0,7)`: «g₀ = 1,4; g₁ = 1,6; g₂ = −0,6 → gana 1».
- El giro: con priors `(½, ¼, ¼)`: «1,4 − 0,69 − 1 = −0,29; 1,6 − 1,39 − 1 = −0,79; −0,6 −
  1,39 − 1 = −2,99 → gana 0».

## Narración

<!-- b1 -->
Un módem no decide entre «hay señal» y «no hay»: decide entre varias señales
posibles, una por cada símbolo que se pueda enviar. Tomemos tres, de cuatro
muestras cada una y energía dos: uno, uno, cero, cero; cero, cero, uno, uno; y uno,
menos uno, cero, cero. Bajo cada hipótesis, lo recibido es esa señal más ruido.

<!-- b2 -->
Repetimos la derivación de la escena seis. Comparamos las densidades escaladas
por sus priors, tomamos logaritmos, desarrollamos el cuadrado. Y ahora la suma
de cuadrados de lo recibido es común a todas las hipótesis, no solo a dos: se
cancela. Queda: elegir la hipótesis que maximice la suma de recibido por señal, más
sigma cuadrado por el logaritmo de su prior, menos su energía entre dos.

<!-- b3 -->
Se implementa con tantos filtros adaptados como señales, en paralelo, y un bloque
que elige la salida mayor. Y si todas las señales tienen la misma energía y la
misma probabilidad, los dos últimos términos son iguales para todas: gana el
filtro con la salida más grande.

<!-- b4 -->
Con números. Recibimos cero coma cuatro, uno, cero coma nueve, cero coma siete.
Primera señal: cero coma cuatro más uno, uno coma cuatro. Segunda: cero coma nueve
más cero coma siete, uno coma seis. Tercera: cero coma cuatro menos uno, menos
cero coma seis. Gana la segunda, por poco.

<!-- b5 -->
Ahora un giro. Supongamos que la primera señal es la más probable, un medio,
y las otras, un cuarto. A cada resultado le sumamos el logaritmo de su prior y
le restamos la energía entre dos, uno. Sale menos cero coma veintinueve, menos cero
coma setenta y nueve, menos dos coma noventa y nueve. ¡Ahora gana la primera!
Mismo dato, otra decisión: lo que sabías de antemano pesa cuando la evidencia
está reñida.

---

# Escena 28 — LaDiferencia

**Objetivo:** con dos señales la regla se reduce a un único filtro adaptado a la
diferencia `s₁ − s₀`. Calcular a mano el error con `s₁ = (2, 2, 1)` y `s₀ = (2, −1,
−2)`: medias ±9, desvío 4,24 y `P_e = Q(2,12) = 0,017`. Llegar a `P_e = Q(‖s₁ − s₀‖ /
2σ)` como una distancia y a la geometría (dos puntos, frontera perpendicular).

**Qué hace falta saber antes:** escenas 09, 10 y 27; del capítulo 7, la norma
(longitud) de una flecha y el producto escalar.

**Visual:**
- El resultado de `M = 2`: «g = Σ r (s₁ − s₀) ≷ σ² ln(p₀/p₁) + (E₁ − E₀)/2».
- `s₁ = (2, 2, 1)` y `s₀ = (2, −1, −2)`, ambas de energía 9; su diferencia `(0, 3, 3)`.
  La primera muestra desaparece: «lo común no ayuda».
- Producto `s₁ · s₀ = 4 − 2 − 2 = 0`; longitud de la diferencia: «√18 = 4,24».
- Las dos campanas de `g`: medias «+9» y «−9», desvío «4,24», el umbral en 0 y las
  colas: «9 / 4,24 = 2,12 → Q(2,12) = 0,017».
- Dos puntos `s₀` y `s₁` en el plano, cada uno con su nube redonda de radio `σ`; la
  frontera perpendicular por el punto medio; la distancia marcada.
- La fórmula por piezas: «P_e = Q(‖s₁ − s₀‖ / 2σ)».
- «X = s₀ · s₁» y «‖s₁ − s₀‖² = 2E − 2X»: la correlación entre las dos señales.

## Narración

<!-- b1 -->
Con dos señales, la regla se simplifica mucho: basta un único filtro adaptado a
la diferencia entre las dos. Ge es la suma de recibido por la señal uno menos la
señal cero. Lo que importa no es cada señal por separado, sino en qué se
distinguen: la parte que tienen en común no ayuda a decidir.

<!-- b2 -->
Un ejemplo. La señal uno, dos, dos, uno. La señal cero, dos, menos uno, menos dos.
Las dos tienen energía nueve. Su diferencia es cero, tres, tres: la primera
muestra, que tienen igual, desaparece. La longitud de la diferencia es la raíz de
dieciocho, cuatro coma dos cuatro.

<!-- b3 -->
¿Cuánto nos equivocamos? Con probabilidades y energías iguales, el umbral es cero.
Bajo la hipótesis uno, ge tiene media la señal uno por la diferencia: nueve. Bajo
la cero, menos nueve. Y ambos con desvío cuatro coma dos cuatro. Nueve entre
cuatro coma dos cuatro es dos coma doce, y cu de dos coma doce vale cero coma
cero uno siete.

<!-- b4 -->
Es la misma cuenta de siempre, y generaliza. El error es cu de la longitud de la
diferencia entre dos sigma: la distancia entre las señales, medida en desvíos del
ruido. Geométricamente, dos puntos, cada uno rodeado de una nube redonda de
ruido. La regla óptima traza una frontera perpendicular por el punto medio.

<!-- b5 -->
Llamemos equis a la suma de una señal por la otra: cuánto se parecen. La longitud
al cuadrado de la diferencia vale dos veces la energía menos dos equis. Cuanto
menos se parezcan las dos señales, más lejos están los puntos y menos nos
equivocamos. Para minimizar el error, hay que hacer equis lo más negativo posible.
¿Hasta dónde puede bajar?

---

# Escena 29 — AntipodalGana

**Objetivo:** ver que la correlación `X` entre dos señales de la misma energía no
puede bajar de `−E` (Cauchy-Schwarz), que se alcanza con `s₁ = −s₀` (señalización
antipodal), y comparar las tres señalizaciones con el pulso `(2, 2, 1)`: on-off
0,0668, ortogonal 0,0170 y antipodal 0,00135. Dar la comparación honesta con la
potencia media.

**Qué hace falta saber antes:** escena 28; escena 17 (Cauchy-Schwarz); del
capítulo 11, los decibelios.

**Visual:**
- La parábola de Cauchy-Schwarz (mismo dibujo) aplicada a `s₀` y `s₁`: «X² ≤ E · E
  → X ≥ −E», con la igualdad en «s₁ = −s₀».
- Tres columnas con la misma energía 9 y `σ = 1`:
  - on-off: `s₁ = (2, 2, 1)`, `s₀ = 0`: distancia 3 → `Q(1,5) = 0,0668`;
  - ortogonal: `s₁ = (2, 2, 1)`, `s₀ = (2, −1, −2)`: distancia 4,24 → `Q(2,12) =
    0,0170`;
  - antipodal: `s₁ = (2, 2, 1)`, `s₀ = (−2, −2, −1)`: distancia 6 → `Q(3) = 0,00135`.
- Los puntos en el plano con las distancias 3, 4,24 y 6, y las campanas cada vez más
  separadas.
- Pregunta con pausa: «¿cuántas veces menos errores?». Cuenta: «0,0668 / 0,00135 ≈ 50».
- La escalera de energía para `P_e = 10⁻⁵`: «73 · 36 · 18» con «3 dB entre cada
  escalón».
- Una nota: on-off no transmite la mitad del tiempo; a igual energía media, on-off
  empata con ortogonal.

## Narración

<!-- b1 -->
Equis es la suma de una señal por la otra, y las dos tienen la misma energía. ¿Hasta
dónde puede bajar? Aquí aparece, por última vez en el capítulo, Cauchy-Schwarz:
equis al cuadrado no supera la energía por la energía. Así que equis no baja de
menos la energía, y llega justo ahí cuando una señal es la otra con el signo
cambiado. Se llama señalización antipodal.

<!-- b2 -->
Comparemos tres maneras de enviar un bit con el mismo pulso, dos, dos, uno, de energía
nueve, y sigma uno. La primera, on-off: enviamos el pulso o no enviamos nada. La
distancia es tres, y el error, cu de uno coma cinco: cero coma cero seis seis ocho. La
segunda, ortogonal: el pulso contra el de la escena anterior. Distancia cuatro coma
dos cuatro: cero coma cero uno siete.

<!-- b3 -->
La tercera, antipodal: el pulso contra el mismo pulso cambiado de signo. La
distancia es seis, el doble que en on-off, y el error, cu de tres: cero coma cero cero
uno tres cinco. Piénsalo un momento: con el mismo pulso y la misma energía, ¿cuántas
veces menos errores? Cerca de cincuenta.

<!-- b4 -->
Otra manera de verlo: cuánta energía hace falta para tener un error de uno entre
cien mil. Con antipodal, dieciocho. Con ortogonal, treinta y seis, el doble. Con
on-off, setenta y tres, el cuádruple. Tres decibelios de diferencia entre cada
escalón. Duplicar la distancia es lo mismo que cuadruplicar la relación
señal-ruido.

<!-- b5 -->
Una advertencia honesta. On-off no transmite nada la mitad del tiempo, así que
gasta la mitad de energía. Si comparas a igual energía media, on-off empata con
ortogonal, y antipodal sigue ganando por tres decibelios. Por eso casi todos los
sistemas digitales usan antipodal, o alguna variante suya.

---

# Escena 30 — ReceptorDeModem

**Objetivo:** unir el filtro adaptado con el diseño de pulsos de Nyquist: el
receptor óptimo es el adaptado al pulso recibido, y el pulso total es `|P|² |H_c|²`,
real y positivo, así que la condición de no interferencia entre símbolos se impone
a `|P|²` y el conformado se reparte a partes iguales entre emisor y receptor
(raíz de coseno alzado).

**Qué hace falta saber antes:** escenas 14 a 16; del capítulo 3, PAM y la
interferencia entre símbolos con la condición de Nyquist (se recuerda aquí).

**Visual:**
- Una secuencia de pulsos, uno por símbolo, que se solapan; en los instantes de
  muestreo, los vecinos deben valer cero: «cero en los demás, uno en el propio».
- La cadena: «transmisor P → canal H_c → receptor → muestrear». En el receptor: «el
  adaptado, conjugado del pulso recibido».
- La cuenta: «P · H_c · conj(P · H_c) = |P|² |H_c|²». El resultado es real y
  positivo: se dibuja una flecha compleja que gira a ángulo cero (recuerdo de la
  escena 16).
- «la condición de Nyquist se impone a |P|², no a P».
- Un reparto: «√ del pulso deseado» en el transmisor y «√ del pulso deseado» en el
  receptor, y el nombre «raíz de coseno alzado».

## Narración

<!-- b1 -->
Un módem envía un pulso por cada símbolo, uno detrás de otro. Del capítulo tres,
PAM: si los pulsos son largos, se solapan, y cada símbolo se mezcla con sus vecinos.
Es la interferencia entre símbolos. El criterio de Nyquist pide que el pulso total
valga uno en su instante de muestreo y cero en los instantes de todos los demás.

<!-- b2 -->
Sin ruido, esto se resolvía diseñando un pulso que cumpliera esa condición. Con
ruido, sabemos que el receptor óptimo es el filtro adaptado al pulso que llega. Si
el transmisor envía un pulso pe, y el canal tiene una respuesta hache de ce, el
pulso que llega es el producto. El receptor tiene su conjugado.

<!-- b3 -->
Y el pulso total, tras el canal y el receptor, es el producto de esas cosas: pe
por hache de ce, por su conjugado. Es el cuadrado del módulo de pe por el cuadrado
del módulo de hache de ce. Es real y positivo: la fase se ha cancelado, como en la
escena de las flechas. Así que la condición de Nyquist ya no se impone al pulso
enviado, sino a su módulo al cuadrado.

<!-- b4 -->
Una consecuencia práctica. Si el pulso deseado, el que cumple Nyquist, es un
coseno alzado, el transmisor y el receptor se reparten el trabajo: cada uno aplica
la raíz de ese pulso. Es el filtro raíz de coseno alzado, que está en casi todos
los módems. La mitad del conformado se hace en el transmisor, y la otra mitad, en
el receptor.

<!-- b5 -->
Así, con un solo reparto, se cumplen dos exigencias a la vez: la máxima relación
señal-ruido en el receptor, y ninguna interferencia entre símbolos. No hay que
elegir entre las dos. Y con esto tenemos todas las piezas del detector. Vamos a
mirar el conjunto.

---

# Escena 31 — ElMapaDelCurso

**Objetivo:** cerrar el capítulo y la serie: la cuarta parábola, detección contra
estimación (Wiener frente a adaptado), la geometría que lo une todo (flechas,
sombras, distancias en desvíos), la receta práctica y una mirada al curso entero.

**Qué hace falta saber antes:** todo el capítulo; del capítulo 12, el filtro de
Wiener (se recuerda aquí); del capítulo 7 (escena 28), del 10 (escena 12) y del 11
(escena 30), la parábola.

**Visual:**
- La parábola de Cauchy-Schwarz del capítulo 7, con cuatro etiquetas que se van
  encendiendo: «ρ ≤ 1 (cap. 7)», «covarianza acotada (cap. 10)», «coherencia ≤ 1
  (cap. 11)», «filtro adaptado (cap. 13)».
- Tabla de dos columnas: «Wiener (cap. 12)» y «adaptado (cap. 13)»: pregunta,
  criterio, qué conserva, la señal.
- Un dibujo geométrico: una flecha y su sombra sobre otra; dos puntos con nubes
  redondas y una frontera perpendicular.
- La receta en pasos: «¿qué es señal y qué es ruido? → blanquear → adaptado →
  muestrear en el pico → umbral (prior o Neyman-Pearson)», con las variantes: «no
  sé cuándo: máximo y umbral más alto», «puedo elegir la señal: donde el ruido es
  débil», «pulso comprimido», «antipodal».
- El mapa del curso: los siete capítulos como estaciones (probabilidad, estimación,
  hipótesis, procesos, espectro, Wiener, detección) unidos por flechas, con la
  imagen de la voz y el murmullo del capítulo 11 al final.

## Narración

<!-- b1 -->
Un último vistazo. La parábola de Cauchy-Schwarz ha aparecido cuatro veces. En el
capítulo siete, para probar que rho no pasa de uno. En el diez, para acotar la
covarianza del sensor. En el once, para la coherencia. Y aquí, para el filtro
adaptado. Siempre el mismo truco: una suma de cuadrados no puede ser negativa.

<!-- b2 -->
Este capítulo y el anterior se parecen mucho, y conviene no confundirlos. El filtro
de Wiener del capítulo doce estima la forma de una señal aleatoria, muestra a
muestra, minimizando el error cuadrático. El filtro adaptado decide si hay una
señal conocida, y se queda con un solo número. Los dos, cuando el ruido tiene
color, hacen lo mismo primero: blanquear.

<!-- b3 -->
Y detrás de todo está la misma geometría. Las señales son flechas, o puntos. El
ruido es una nube redonda. Lo que va en la dirección que importa se queda, y lo
perpendicular se tira. Y decidir es medir distancias, en desvíos del ruido. Es la
flecha y su sombra del capítulo ocho, la misma idea, una y otra vez.

<!-- b4 -->
Si tuvieras que resolver un problema real, la receta es esta. Identifica qué es
señal y qué es ruido. Si el ruido tiene memoria, blanquéalo. Correlaciona con la
señal, con un filtro adaptado. Muestrea en el pico. Compara con un umbral, que sale
de la probabilidad a priori o de una falsa alarma tolerada. Y si no sabes cuándo
llega, usa el máximo y sube el umbral.

<!-- b5 -->
Empezamos este curso con una señal que no podíamos predecir. Aprendimos a
describirla con probabilidad, a estimarla con proyecciones, a decidir con
hipótesis, a caracterizarla con procesos y espectros, a limpiarla con Wiener y,
ahora, a detectarla. Detrás de cada capítulo estaba la misma idea. Una flecha y
su sombra.

