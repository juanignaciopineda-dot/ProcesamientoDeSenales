Solucionario de los Ejercicios Propuestos del capítulo 10 de [[PROCESAMIENTO DE SEÑALES]]. La teoría con demostraciones está en [[PROCESAMIENTO DE SEÑALES - Cap 10 en profundidad]].

# Procesos Aleatorios — Solucionario

Estos ejercicios se resuelven con las herramientas del capítulo: momentos de primer y segundo orden ($\mu_x(t)$, $R_{xx}(t_1,t_2)$, $C_{xx}(t_1,t_2)$), los criterios de estacionariedad (SSS y WSS) y de ergodicidad, la relación entre ensemble y realización única y, en la segunda mitad, el filtrado LTI de procesos WSS ($R_{yy}$, $R_{yx}$ y sus PSD). Cada ejercicio sigue la estructura Enunciado / Idea / Resolución / Verificación; los resultados numéricos están chequeados con simulación o integración numérica antes de escribirse.

###### **Índice**
| Ej. | Qué se practica | Problema del libro |
|---|---|---|
| 1 | Onda telegráfica: probabilidad condicional de persistencia del signo | P10.4 |
| 2 | PMF y autocorrelación a partir de un ensemble de tres funciones muestra | P10.1 |
| 3 | Estimador MMSE a partir de un ensemble de cuatro funciones muestra | P10.2 |
| 4 | Incorrelación no alcanza para factorizar un momento de cuarto orden | P10.16 |
| 5 | SSS no implica ergódico en media (contraejemplo) | P10.15 |
| 6 | Proceso construido con fases i.i.d.: WSS pero no i.i.d. | P10.18 |
| 7 | Fórmula de incrementos cuadráticos, y una constante aleatoria que rompe la ergodicidad | P10.13 |
| 8 | Momentos de un coseno con amplitud aleatoria, y de la suma de dos tonos con fase aleatoria | P10.3 |
| 9 | Coseno con frecuencia y fase aleatorias: WSS y ergódico en media, pero no en correlación | P10.6 |
| 10 | Sinusoide de frecuencia y fase aleatorias, WSS | P10.7 |
| 11 | Criterio de ergodicidad en media y contraejemplo (variable aleatoria de fondo) | P10.5 |
| 12 | Modulación por $(-1)^n$: de PSD pasabajos a pasaaltos | P10.8 |
| 13 | Filtrado FIR de blanco: autocorrelación y correlación cruzada salida-entrada | P10.9 |
| 14 | Filtrado + borrado Bernoulli: seis correlaciones cruzadas y propias | P10.10 |
| 15 | Señal filtrada más ruido no correlacionado: todas las correlaciones cruzadas | P10.12 |
| 16 | Verdadero/falso: retardo, factorización espectral, derivada de un proceso | P10.14 |
| 17 | Producto de rama filtrada y rama retardada con entrada blanca | P10.11 |
| 18 | $R_{yy}=R_{xx}$ no implica retardo puro: ambigüedad pasatodo | P10.17 |

---

## Ejercicio 1 — Onda telegráfica: probabilidad condicional de persistencia del signo

> [!quote] Enunciado
> 1. Para la onda telegráfica aleatoria, evalúe (como función de $T$ para $T>0$) la probabilidad condicional de que $X(t_0+T)=+1$, dado que $X(t_0)=+1$. ¿Para qué rango de $T>0$ esta probabilidad condicional es mayor que la probabilidad condicional de que $X(t_0+T)=-1$? Si, para un $T>0$ dado, usted predijera que $X(t_0+T)=+1$ dado que $X(t_0)=+1$, ¿cuál sería la probabilidad de que su predicción sea incorrecta? ¿Cómo varía esta probabilidad con $T$, y le parece razonable?

###### **Idea**
$X(t_0+T)$ coincide con $X(t_0)$ si y solo si ocurrió un número PAR de saltos en el intervalo $(t_0,t_0+T]$. Como los saltos son un proceso de Poisson de tasa $\lambda$, alcanza con sumar la probabilidad de los términos pares de la Poisson.

###### **Resolución**
Sea $N(T)\sim\text{Poisson}(\lambda T)$ el número de conmutaciones en un intervalo de largo $T$. Como cada conmutación invierte el signo, $X(t_0+T)=X(t_0)$ exactamente cuando $N(T)$ es par:
$$P\{N(T)\text{ par}\}=\sum_{k\ \text{par}}e^{-\lambda T}\frac{(\lambda T)^k}{k!}=e^{-\lambda T}\left(\sum_{j=0}^{\infty}\frac{(\lambda T)^{2j}}{(2j)!}\right)=e^{-\lambda T}\cosh(\lambda T)$$
usando la serie del coseno hiperbólico. Como $\cosh(x)=\tfrac12(e^x+e^{-x})$:
$$P\{N(T)\text{ par}\}=e^{-\lambda T}\cdot\frac{e^{\lambda T}+e^{-\lambda T}}{2}=\frac{1+e^{-2\lambda T}}{2}$$
Entonces:
$$\boxed{\ P\{X(t_0+T)=+1\mid X(t_0)=+1\}=\frac{1+e^{-2\lambda T}}{2}\ }$$
y por complemento, $P\{X(t_0+T)=-1\mid X(t_0)=+1\}=\dfrac{1-e^{-2\lambda T}}{2}$.

**Comparación.** $\dfrac{1+e^{-2\lambda T}}{2}>\dfrac{1-e^{-2\lambda T}}{2}\iff e^{-2\lambda T}>0$, que vale para **todo** $T>0$ (finito). O sea: no importa cuánto haya pasado, siempre es más probable que el signo se haya mantenido que que se haya invertido — aunque la ventaja se achica a medida que $T$ crece.

**Probabilidad de error.** Si predecís "$+1$", la probabilidad de estar equivocado es
$$\boxed{\ P(\text{error})=\frac{1-e^{-2\lambda T}}{2}\ }$$
que crece monótonamente con $T$: vale $0$ en $T=0^+$ (todavía no tuvo tiempo de conmutar) y tiende a $\tfrac12$ cuando $T\to\infty$ (para intervalos larguísimos, el proceso "se olvida" de dónde arrancó y predecir es como tirar una moneda). Es razonable: el proceso de Poisson no tiene memoria más allá de su tasa, así que la correlación entre $X(t_0)$ y $X(t_0+T)$ tiene que decaer exponencialmente con $T$, y eso es justo lo que hace $P(\text{error})$ en espejo.

###### **Verificación**
$P(\text{error})\in[0,\tfrac12]$ para todo $T\ge0$ ✓ (una probabilidad de error nunca puede superar la de "tirar una moneda"). Conexión con la autocorrelación: como $X\in\{-1,+1\}$ con marginal simétrica, $R_{xx}(T)=E[X(t_0)X(t_0+T)]=P(\text{acierto})-P(\text{error})=2P(\text{acierto})-1$, y despejando da $P(\text{acierto})=\tfrac{1+R_{xx}(T)}{2}=\tfrac{1+e^{-2\lambda T}}{2}$ usando $R_{xx}(\tau)=e^{-2\lambda|\tau|}$ del apunte — coincide exactamente. *(verificado numéricamente: con $\lambda=1{,}3$ y $4\cdot10^6$ trayectorias de Poisson simuladas, para $T=1$ la fracción de trayectorias con número par de saltos da $0{,}53716$ contra la fórmula $\tfrac{1+e^{-2,6}}{2}=0{,}53714$; para $T=5$ da $0{,}49978$ contra $0{,}50000$.)*

> [!info] Conexión
> Es la misma $R_{xx}(\tau)=e^{-2\lambda|\tau|}$ del Ejemplo (onda telegráfica aleatoria) de [[PROCESAMIENTO DE SEÑALES]] (capítulo 10), cuya derivación completa está en [[PROCESAMIENTO DE SEÑALES - Cap 10 en profundidad]] (Parte 2.1).

---

## Ejercicio 2 — PMF y autocorrelación a partir de un ensemble de tres funciones muestra

> [!quote] Enunciado
> 2. Como se muestra en la figura, un proceso aleatorio particular $X(t)$ está representado por un espacio muestral con tres funciones del tiempo posibles como resultados. Las probabilidades de los tres resultados $x_1(t)$, $x_2(t)$ y $x_3(t)$ son
> $$P\{x_1(t)\}=\tfrac13, \quad P\{x_2(t)\}=\tfrac14, \quad P\{x_3(t)\}=\tfrac{5}{12}$$
>
> ![[ej-p10-2.png]]
>
> a) Determine la PMF de la variable aleatoria $X(t_1)$.
> b) Determine la PMF conjunta $p_{X(t_1),X(t_2)}(x_1,x_2)$ de las dos variables aleatorias $X(t_1)$ y $X(t_2)$.
> c) Determine la autocorrelación $R_{XX}(t_1,t_2)=E[x(t_1)x(t_2)]$.

###### **Idea**
Con un ensemble de solo tres funciones, "el proceso" se reduce a sortear cuál de las tres funciones te tocó. Una vez elegida, $X(t_1)$ y $X(t_2)$ quedan totalmente determinados: no hay que integrar densidades, alcanza con leer la figura en $t_1$ y $t_2$ y trasladar las probabilidades del ensemble.

###### **Resolución**
**Leer la figura con cuidado.** Entre $t_1$ y $t_2$ las curvas **se cruzan dos veces**, así que no alcanza con mirar a qué altura está cada una en $t_1$: hay que seguir cada curva de punta a punta (conviene hacerlo desde las etiquetas de la derecha, donde no hay cruces después de $t_2$).
- $x_1(t)$ (la que termina en $5$): en $t_2$ vale $4$; yendo hacia la izquierda pasa por el pico de $\approx4{,}25$, cruza la curva plana y en $t_1$ vale $3$.
- $x_2(t)$ (la que termina en $3{,}5$): en $t_2$ vale $3$; hacia la izquierda baja, cruza a la curva que cae, y en $t_1$ vale $1$.
- $x_3(t)$ (la que termina en $0{,}5$): en $t_2$ vale $1$ (el quiebre justo sobre $t_2$); hacia la izquierda es la curva que cae en picada, y antes de caer iba plana en $4$, así que en $t_1$ vale $4$.

| Resultado | $P$ | $x_i(t_1)$ | $x_i(t_2)$ |
|---|---|---|---|
| $x_1$ | $1/3$ | $3$ | $4$ |
| $x_2$ | $1/4$ | $1$ | $3$ |
| $x_3$ | $5/12$ | $4$ | $1$ |

**a)** $X(t_1)$ queda fijado por cuál resultado salió, así que hereda directamente las probabilidades del ensemble:
$$\boxed{\ p_{X(t_1)}(1)=\tfrac14,\quad p_{X(t_1)}(3)=\tfrac13,\quad p_{X(t_1)}(4)=\tfrac{5}{12}\ }$$

**b)** $X(t_1)$ y $X(t_2)$ están determinados por el **mismo** resultado del experimento (no son dos sorteos independientes). Cada resultado aporta un único par $(x_i(t_1),x_i(t_2))$ con su probabilidad:
$$\boxed{\ p_{X(t_1),X(t_2)}(3,4)=\tfrac13,\ \ p_{X(t_1),X(t_2)}(1,3)=\tfrac14,\ \ p_{X(t_1),X(t_2)}(4,1)=\tfrac{5}{12}\ }$$
y $p_{X(t_1),X(t_2)}(x_1,x_2)=0$ para cualquier otro par. Notá que **no** es el producto de las marginales: por ejemplo $p(3,4)=\tfrac13$, pero $p_{X(t_1)}(3)\,p_{X(t_2)}(4)=\tfrac13\cdot\tfrac13=\tfrac19$.

**c)** Esperanza del producto sobre los tres resultados:
$$R_{XX}(t_1,t_2)=3\cdot4\cdot\tfrac13+1\cdot3\cdot\tfrac14+4\cdot1\cdot\tfrac{5}{12}=4+\tfrac34+\tfrac53=\tfrac{48+9+20}{12}$$
$$\boxed{\ R_{XX}(t_1,t_2)=\tfrac{77}{12}\approx6{,}42\ }$$

###### **Verificación**
Las probabilidades de a) y de b) suman $1$ ✓. Por Cauchy-Schwarz, $|R_{XX}(t_1,t_2)|\le\sqrt{E[X(t_1)^2]\,E[X(t_2)^2]}$: con $E[X(t_1)^2]=\tfrac{9}{3}+\tfrac14+\tfrac{80}{12}=\tfrac{119}{12}$ y $E[X(t_2)^2]=\tfrac{16}{3}+\tfrac94+\tfrac{5}{12}=8$, la cota es $\sqrt{(119/12)\cdot8}\approx8{,}91\ge6{,}42$ ✓. *(verificado con aritmética exacta de fracciones: $R_{XX}=77/12$.)*

> [!warning] Ojo
> El error típico es leer las tres curvas "de izquierda a derecha por altura" y suponer que la que está arriba en $t_1$ sigue arriba en $t_2$. Eso da $(4,4)$, $(3,3)$, $(1,1)$ y $R_{XX}=8$, que es incorrecto: las curvas se cruzan entre $t_1$ y $t_2$. Justamente por eso el ejercicio pide la PMF **conjunta** — el par $(X(t_1),X(t_2))$ no se deduce de las dos marginales.

---

## Ejercicio 3 — Estimador MMSE a partir de un ensemble de cuatro funciones muestra

> [!quote] Enunciado
> 3. Un proceso aleatorio $W(t)$ puede tomar cuatro funciones del tiempo distintas como resultados, mostradas en la figura. Las probabilidades de los cuatro resultados $w_1(t)$, $w_2(t)$, $w_3(t)$ y $w_4(t)$ son
> $$P\{w_1(t)\}=\tfrac13,\quad P\{w_2(t)\}=\tfrac14,\quad P\{w_3(t)\}=\tfrac14,\quad P\{w_4(t)\}=\tfrac16$$
>
> ![[ej-p10-3.png]]
>
> Dado que $W(t_1)=6$ y $W(t_2)=4$, encuentre la estimación de mínimo error cuadrático medio (MMSE) para $W(t_3)$.

###### **Idea**
Otra vez cada resultado del experimento es una función determinística completa: "dado $W(t_1)=6,\ W(t_2)=4$" simplemente descarta las realizaciones incompatibles con esas dos lecturas y renormaliza las probabilidades de las que quedan. El estimador MMSE es la esperanza condicional (capítulo 8), que ahí adentro es un promedio pesado.

###### **Resolución**
Leyendo la figura en $t_1$, $t_2$ y $t_3$ para cada una de las cuatro realizaciones. Igual que en el Ejercicio 2, hay cruces (tres curvas pasan por $6$ en $t_1$ y tres por $4$ en $t_2$), así que cada curva se sigue por continuidad de la pendiente, empezando desde su etiqueta a la derecha:

| Realización | $P$ | $w(t_1)$ | $w(t_2)$ | $w(t_3)$ |
|---|---|---|---|---|
| $w_1$ | $1/3$ | $6$ | $8$ | $9$ |
| $w_2$ | $1/4$ | $6$ | $4$ | $6$ |
| $w_3$ | $1/4$ | $2$ | $4$ | $4$ |
| $w_4$ | $1/6$ | $6$ | $4$ | $2$ |

($w_3$ es la curva que sube empinada desde abajo, pasa por $4$ en $t_2$, hace el pico de $\approx7{,}5$ y baja a $4$ en $t_3$: en $t_1$ estaba en $2$. $w_4$ es la recta que baja $6\to4\to2$.)

La condición $W(t_1)=6$ descarta a $w_3$. La condición $W(t_2)=4$ descarta a $w_1$. Sobreviven $w_2$ y $w_4$. Renormalizando sus probabilidades (que **no** son iguales):
$$P(w_2\mid W(t_1)=6,W(t_2)=4)=\frac{1/4}{1/4+1/6}=\frac35,\qquad P(w_4\mid\cdots)=\frac{1/6}{1/4+1/6}=\frac25$$

El estimador MMSE es la esperanza condicional:
$$\hat W(t_3)=E[W(t_3)\mid W(t_1)=6,W(t_2)=4]=\tfrac35\cdot6+\tfrac25\cdot2=\tfrac{18}{5}+\tfrac45$$
$$\boxed{\ \hat W(t_3)=\tfrac{22}{5}=4{,}4\ }$$

###### **Verificación**
El resultado cae entre los dos valores posibles, $2$ y $6$, y más cerca de $6$ porque $w_2$ es más probable que $w_4$ ✓. El MMSE asociado es $\tfrac35(6-4{,}4)^2+\tfrac25(2-4{,}4)^2=3{,}84$. *(verificado con aritmética exacta de fracciones: realizaciones compatibles $\{w_2,w_4\}$, posteriores $3/5$ y $2/5$, estimación $22/5$.)*

> [!warning] Ojo
> Si se lee mal el cruce en $t_1$ y se toma a $w_3$ como compatible (en lugar de $w_4$), sale $\tfrac12\cdot6+\tfrac12\cdot4=5$. La clave es que la curva que en $t_2$ sube empinada hacia el pico viene de **abajo** ($w_3(t_1)=2$), no del cruce en $6$.

> [!info] Conexión
> Es el mismo procedimiento que la Actividad — Ejercicio 10.3 de [[PROCESAMIENTO DE SEÑALES]] (capítulo 10, sección "Qué es un proceso aleatorio"), con una lectura más (tres condiciones en vez de dos, pero el mismo mecanismo de descartar y renormalizar).

---

## Ejercicio 4 — Incorrelación no alcanza para factorizar un momento de cuarto orden

> [!quote] Enunciado
> 4. Si $x(t)$ e $y(t)$ son dos procesos aleatorios WSS de media nula con $R_{xy}(\tau)=0$ para todo $\tau$, ¿es siempre cierto que
> $$E\{x^2(t+\tau)\ y^2(t)\}=R_{xx}(0)\ R_{yy}(0)\ ?$$
> Explique.

###### **Idea**
$R_{xy}(\tau)=0$ es una condición de SEGUNDO orden (incorrelación). La igualdad que se pregunta es de CUARTO orden, y esa factorización solo está garantizada bajo INDEPENDENCIA de $x(t+\tau)$ e $y(t)$ — algo estrictamente más fuerte que incorrelación. Conviene buscar un contraejemplo con dependencia no lineal pero covarianza nula, como en el capítulo 7.

###### **Resolución**
**No, no es siempre cierto.** $R_{xy}(\tau)=0$ dice que $x(t+\tau)$ e $y(t)$ no están correlacionados linealmente, pero no dice nada sobre momentos de orden superior. La igualdad pedida es exactamente el tipo de factorización que solo vale si $x(t+\tau)$ e $y(t)$ son independientes.

**Contraejemplo** (la misma idea del "ensemble de baterías", aplicada a dos variables): tomemos dos procesos constantes en el tiempo, $x(t)=X$ e $y(t)=Y=X^2-1$ para todo $t$, con $X\sim\mathcal N(0,1)$. Son WSS de manera trivial (no dependen de $t$) y de media nula: $E[Y]=E[X^2]-1=1-1=0$. La correlación cruzada:
$$R_{xy}(\tau)=E[XY]=E[X^3-X]=E[X^3]-E[X]=0-0=0\quad\text{para todo }\tau$$
(los momentos impares de una gaussiana centrada son nulos). Sin embargo $Y$ es una función DETERMINÍSTICA de $X$: están lejos de ser independientes. Usando los momentos de la normal estándar ($E[X^2]=1$, $E[X^4]=3$, $E[X^6]=15$):
$$R_{xx}(0)=E[X^2]=1,\qquad R_{yy}(0)=E[(X^2-1)^2]=E[X^4]-2E[X^2]+1=3-2+1=2$$
$$R_{xx}(0)\,R_{yy}(0)=2$$
mientras que
$$E[x^2(t+\tau)y^2(t)]=E[X^2Y^2]=E\big[X^2(X^2-1)^2\big]=E[X^6-2X^4+X^2]=15-6+1=10$$
$$\boxed{\ 10\neq2\ \implies\ \text{la igualdad NO es siempre cierta}\ }$$

###### **Verificación**
$R_{xy}(\tau)=0$ es consistente con $|\rho_{xy}|=0\le1$ ✓ (lo que falla es la factorización de cuarto orden, no ninguna cota de segundo orden). *(verificado numéricamente: Monte Carlo con $6\cdot10^6$ muestras de $X\sim\mathcal N(0,1)$ da $\hat R_{xy}\approx0{,}0004\approx0$, $\hat R_{xx}(0)\approx1{,}000$, $\hat R_{yy}(0)\approx2{,}002$, y $E[X^2Y^2]\approx10{,}02$ contra $R_{xx}(0)R_{yy}(0)\approx2{,}003$ — confirma la discrepancia.)*

> [!warning] Ojo
> "No correlacionados" (covarianza nula) es mucho más débil que "independientes". La igualdad $E[x^2y^2]=E[x^2]E[y^2]$ está garantizada bajo independencia; alcanza con una dependencia de orden superior (acá, $Y$ depende de $X$ solo a través de $X^2$) para que la covarianza se anule sin que la independencia se sostenga — el mismo fenómeno que en el Ejercicio 6 de esta guía.

---

## Ejercicio 5 — SSS no implica ergódico en media

> [!quote] Enunciado
> 5. ¿Un proceso aleatorio SSS $x(t)$ es necesariamente ergódico en media? Explique.

###### **Idea**
Alcanza un contraejemplo. El más económico es reciclar el "ensemble de baterías" del apunte principal: ahí el proceso es SSS de la forma más extrema posible (cada realización es constante en el tiempo) y sin embargo no es ergódico.

###### **Resolución**
**No, no es necesariamente cierto.** SSS garantiza que TODAS las densidades conjuntas del proceso son invariantes ante corrimientos temporales — es una afirmación sobre la estadística del proceso. Pero eso no dice nada sobre si una ÚNICA realización, promediada en el tiempo, es representativa de todo el ensemble; eso es lo que hace falta para la ergodicidad, y es una propiedad distinta.

**Contraejemplo (ensemble de baterías).** Tomemos $N$ baterías con distinto voltaje, elegimos una al azar según algún criterio de probabilidad, y definimos $x(t)=V$ (el voltaje de la batería elegida) para todo $t$. Cada realización es una función CONSTANTE en el tiempo, así que trivialmente
$$f_{x(t_1),\dots,x(t_\ell)}(x_1,\dots,x_\ell)=f_{x(t_1+\alpha),\dots,x(t_\ell+\alpha)}(x_1,\dots,x_\ell)\quad\text{para todo }\alpha$$
(la densidad conjunta ni siquiera depende de qué instantes se elijan: todas las "coordenadas" son la misma variable aleatoria $V$ repetida). El proceso es SSS de la manera más fuerte posible.

Pero el promedio temporal de una realización:
$$\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}x(t)\ dt=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}V\ dt=V$$
es el voltaje de ESA batería en particular, no $E[V]$ (el promedio sobre todo el ensemble). Salvo que todas las baterías tengan el mismo voltaje (caso degenerado), $V\neq E[V]$ con probabilidad 1.
$$\boxed{\ \text{No: SSS no implica ergódico en media (contraejemplo: el ensemble de baterías)}\ }$$

###### **Verificación**
El criterio suficiente de la sección ERGODICIDAD del apunte pide $C_{xx}(\tau)\to0$ cuando $\tau\to\infty$. Acá $C_{xx}(\tau)=\text{Var}(V)$ para todo $\tau$ — no decae nunca — así que el criterio falla explícitamente, consistente con la no ergodicidad.

> [!info] Conexión
> Es literalmente el contraejemplo de la sección **ERGODICIDAD** de [[PROCESAMIENTO DE SEÑALES]] (capítulo 10) y del Ejercicio 6c de [[PROCESAMIENTO DE SEÑALES - Cap 10 en profundidad]] (Parte 5). La moraleja: estacionariedad (la estadística no cambia con el tiempo) y ergodicidad (una realización alcanza para representar a todo el ensemble) son propiedades independientes.

---

## Ejercicio 6 — Proceso construido con fases i.i.d.: WSS pero no i.i.d.

> [!quote] Enunciado
> 6. Sea $\{\Theta_k\}$ un conjunto de variables aleatorias i.i.d., distribuidas uniformemente en el intervalo $[0,2\pi]$. Sea el proceso $x[n]$ formado por
> $$x[2n]=\cos\Theta_n, \qquad x[2n+1]=\sin\Theta_n$$
> de modo que, por ejemplo, $x[-2]=\cos\Theta_{-1}$, $x[-1]=\sin\Theta_{-1}$, $x[0]=\cos\Theta_0$, $x[1]=\sin\Theta_0$, $x[2]=\cos\Theta_1$, $x[3]=\sin\Theta_1$, y así siguiendo.
>
> a) ¿Es el proceso $x[n]$ WSS? Explique.
> b) ¿Es el proceso $x[n]$ i.i.d.? Explique.

###### **Idea**
Conviene separar la autocorrelación en dos casos: muestras que dependen del MISMO $\Theta_k$ (mismo "bloque", índices $2k$ y $2k+1$) y muestras que dependen de $\Theta$'s DISTINTOS (independientes entre sí, por hipótesis). La independencia (para la parte b) hay que chequearla aparte — incorrelación no alcanza.

###### **Resolución**
**a) ¿Es WSS?**
Media: $E[x[2n]]=E[\cos\Theta_n]=\dfrac{1}{2\pi}\displaystyle\int_0^{2\pi}\cos\theta\,d\theta=0$, y $E[x[2n+1]]=E[\sin\Theta_n]=0$ de la misma forma (un seno o coseno integrado sobre un período completo da cero). La media es $0$ para todo $n$: constante ✓.

Autocorrelación $R[n_1,n_2]=E[x[n_1]x[n_2]]$. Si $n_1$ y $n_2$ dependen de $\Theta$'s DISTINTOS (dos bloques distintos), son independientes y de media nula, así que su producto tiene esperanza nula. Solo puede sobrevivir el caso en que ambos dependen del MISMO $\Theta_k$, o sea $n_1,n_2\in\{2k,2k+1\}$:
- $n_1=n_2=2k$: $E[\cos^2\Theta_k]=\tfrac12$
- $n_1=n_2=2k+1$: $E[\sin^2\Theta_k]=\tfrac12$
- $n_1=2k,\ n_2=2k+1$ (índices adyacentes del mismo bloque): $E[\cos\Theta_k\sin\Theta_k]=E\big[\tfrac12\sin(2\Theta_k)\big]=\dfrac{1}{2}\cdot\dfrac{1}{2\pi}\displaystyle\int_0^{2\pi}\sin(2\theta)\,d\theta=0$

Juntando los tres casos con todos los demás (que dan $0$ por independencia de bloques):
$$R_{xx}[n_1,n_2]=\tfrac12\,\delta[n_1-n_2]$$
que depende solo del lag $m=n_1-n_2$. Media constante + autocorrelación función del lag:
$$\boxed{\ x[n]\text{ es WSS, con } R_{xx}[m]=\tfrac12\,\delta[m]\ \text{(blanco)}\ }$$

**b) ¿Es i.i.d.?**
**No**, a pesar de que las muestras son incorrelacionadas dos a dos. El contraejemplo está DENTRO del mismo bloque: $x[2n]=\cos\Theta_n$ y $x[2n+1]=\sin\Theta_n$ comparten el mismo $\Theta_n$, así que satisfacen, con probabilidad 1,
$$x[2n]^2+x[2n+1]^2=\cos^2\Theta_n+\sin^2\Theta_n=1$$
una relación DETERMINÍSTICA. Conociendo $x[2n]$ ya sabés (salvo el signo) el valor de $x[2n+1]$ — están lejos de ser independientes, aunque su covarianza sea cero.
$$\boxed{\ x[n]\text{ no es i.i.d.: }x[2n]\text{ y }x[2n+1]\text{ son incorrelacionadas pero dependientes}\ }$$

###### **Verificación**
$R_{xx}[0]=\tfrac12>0$ ✓ (varianza positiva, como corresponde). *(verificado numéricamente con $2\cdot10^6$ muestras: $\widehat{\text{Var}}(x[2n])\approx0{,}500$, $\widehat{\text{Var}}(x[2n+1])\approx0{,}500$, $\widehat{\text{Cov}}(x[2n],x[2n+1])\approx-0{,}0004\approx0$, $\widehat{\text{Cov}}(x[2n],x[2n+2])\approx0{,}0002\approx0$ — consistente con $R_{xx}[m]=\tfrac12\delta[m]$ — y $\text{Var}\big(x[2n]^2+x[2n+1]^2\big)\approx10^{-33}$, es decir esa suma da exactamente $1$ en cada muestra: la dependencia determinística está ahí, aunque la covarianza sea nula.)*

> [!warning] Ojo
> Otra vez la trampa de "incorrelacionado $\neq$ independiente" (Ejercicio 4), pero acá construida a propósito: un proceso legítimamente WSS —de hecho blanco— que sin embargo no es i.i.d.

---

## Ejercicio 7 — Fórmula de incrementos cuadráticos, y una constante aleatoria que rompe la ergodicidad

> [!quote] Enunciado
> 7. a) Si $x[n]$ es un proceso aleatorio WSS de tiempo discreto con autocorrelación $R_{xx}[m]$, entonces vale una de estas dos igualdades:
> $$E\{(x[n]-x[k])^2\}=2(R_{xx}[n]-R_{xx}[k])$$
> o bien
> $$E\{(x[n]-x[k])^2\}=2(R_{xx}[0]-R_{xx}[n-k])$$
> Elija la igualdad correcta y explique.
>
> b) Verdadero o falso: si $x(t)$ es un proceso WSS de media nula con autocovarianza $C_{xx}(\tau)=e^{-|\tau|}$, e $y(t)=V+x(t)$, donde $V$ es una variable aleatoria de media nula no correlacionada con el proceso $x(\cdot)$, entonces para casi toda realización $y(t)$
> $$\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}y(t)\ dt = 0$$

###### **Idea**
a) Es álgebra directa: expandir el cuadrado y usar que, por WSS, $R_{xx}[n,k]=R_{xx}[n-k]$ depende solo de la diferencia de índices. b) Es otra instancia del "ensemble de baterías": sumarle a un proceso ergódico una variable aleatoria constante en el tiempo (no ergódica) rompe la ergodicidad de la suma.

###### **Resolución**
**a)** Expandiendo el cuadrado y usando linealidad de la esperanza:
$$E\{(x[n]-x[k])^2\}=E\{x[n]^2\}-2E\{x[n]x[k]\}+E\{x[k]^2\}=R_{xx}[0]-2R_{xx}[n,k]+R_{xx}[0]$$
Como el proceso es WSS, $R_{xx}[n,k]=R_{xx}[n-k]$ (la autocorrelación depende solo de la diferencia de índices, no de $n$ y $k$ por separado). Reemplazando:
$$\boxed{\ E\{(x[n]-x[k])^2\}=2\big(R_{xx}[0]-R_{xx}[n-k]\big)\ }$$
es la igualdad correcta. La otra opción, $2(R_{xx}[n]-R_{xx}[k])$, no tiene sentido para un proceso WSS: evaluaría la autocorrelación en los índices absolutos $n$ y $k$ como si $R_{xx}$ tomara un solo argumento igual a la posición temporal, mezclando la notación de un lag con la de dos instantes — no es lo que sale de la cuenta.

**b) Falso.** Escribamos el promedio temporal de $y(t)=V+x(t)$ para una realización fija (con $V$ tomando un valor particular $v$, y $x(t)$ la trayectoria particular del proceso en esa realización):
$$\frac{1}{2T}\int_{-T}^{T}y(t)\,dt=v+\frac{1}{2T}\int_{-T}^{T}x(t)\,dt$$
El proceso $x(t)$ es WSS de media nula con $C_{xx}(\tau)=e^{-|\tau|}\to0$ cuando $\tau\to\infty$: por el criterio de ergodicidad en media del apunte (WSS + varianza finita + autocovarianza que tiende a cero), $x(t)$ SÍ es ergódico en media, así que el segundo término tiende a $\mu_x=0$ para casi toda realización. Pero el primer término es $v$, el valor que le tocó a $V$ en esa realización — y $V$ **no depende de $t$**, así que ningún promediado en $t$ lo puede "promediar hacia $0$". El límite completo es
$$\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}y(t)\,dt = V$$
que es una variable aleatoria de media nula, pero (salvo que $V\equiv0$) no es idénticamente $0$.
$$\boxed{\ \text{Falso: el promedio temporal converge a }V\text{, no a }0\ }$$

###### **Verificación**
$C_{xx}(0)=1<\infty$ (varianza finita, como pide el criterio de ergodicidad) ✓. *(verificado numéricamente: simulando $x(t)$ como un proceso AR(1) que aproxima $C_{xx}(\tau)=e^{-|\tau|}$, con 200 realizaciones de largo $T=4000$ y $V\sim\mathcal N(0,1)$ independiente en cada una: el promedio temporal de $x(t)$ da, en valor absoluto medio, $\approx0{,}019$ (consistente con $0$), mientras que el promedio temporal de $y(t)$ queda pegado a $V$ —correlación $\approx0{,}9997$ entre ambos, diferencia absoluta media $\approx0{,}019$— y su valor absoluto medio es $\approx0{,}84$, claramente no nulo.)*

> [!info] Conexión
> Es la misma idea del Ejercicio 5: sumarle a un proceso ergódico una variable aleatoria constante en el tiempo (tipo "batería") arruina la ergodicidad de la suma. El Ejercicio 11 del capítulo (parte B, no incluida en esta mitad de la guía) pide justamente calcular $C_{yy}(\tau)$ para este mismo $y(t)=x(t)+Z$; ver también el Ejercicio 6c de [[PROCESAMIENTO DE SEÑALES - Cap 10 en profundidad]] (Parte 5).

---

## Ejercicio 8 — Momentos de un coseno con amplitud aleatoria, y de la suma de dos tonos con fase aleatoria

> [!quote] Enunciado
> 8. a) Considere un proceso aleatorio $X(t)$ definido por $X(t)=A\cos(\omega_0 t)$, donde $\omega_0$ es una constante.
> i) Suponga que $A$ es una variable aleatoria distribuida uniformemente en $[0,1]$. Determine la autocorrelación $R_{XX}(t_1,t_2)$ y la autocovarianza $C_{XX}(t_1,t_2)$ de $X(t)$.
> ii) Repita el punto i) para el caso en que $A$ es una variable aleatoria Gaussiana con media $\mu_A=0.5$ y varianza $\sigma_A^2=\frac{1}{12}$.
> iii) ¿Es $X(t)$ WSS?
>
> b) Ahora sea $X(t)=A\cos(\omega_0 t+\Theta_0)+B\cos(\omega_1 t+\Theta_1)$, donde $\omega_0\neq\omega_1$ son constantes, y $A$, $B$, $\Theta_0$ y $\Theta_1$ son variables aleatorias mutuamente independientes, con $\Theta_0$ y $\Theta_1$ uniformes en el intervalo $0\leq\theta<2\pi$. ¿Cuáles son los momentos de primer y segundo orden del proceso $X(t)$? Es decir, halle $E[X(t)]$ y $E[X(t_1)X(t_2)]$. ¿Es el proceso WSS?

###### **Idea**
a) Es una cuenta directa de momentos de $A$: para $R_{XX}$ y $C_{XX}$ solo hacen falta $E[A]$ y $E[A^2]$, no la distribución completa. b) Es el mismo truco del ejemplo "el oscilador, ahora en serio" del apunte (fase uniforme $\Rightarrow$ media nula, y el producto de cosenos se reduce a un coseno de la diferencia), aplicado a una SUMA de dos tonos con fases independientes.

###### **Resolución**
**a) i)** $A\sim\mathcal U[0,1]$: $E[A]=\tfrac12$, $\text{Var}(A)=\tfrac1{12}$, $E[A^2]=\tfrac1{12}+\tfrac14=\tfrac13$.
$$R_{XX}(t_1,t_2)=E[A^2\cos(\omega_0t_1)\cos(\omega_0t_2)]=E[A^2]\cos(\omega_0t_1)\cos(\omega_0t_2)$$
$$\boxed{\ R_{XX}(t_1,t_2)=\tfrac13\cos(\omega_0t_1)\cos(\omega_0t_2)\ }$$
Con $\mu_X(t)=E[A]\cos(\omega_0t)=\tfrac12\cos(\omega_0t)$:
$$C_{XX}(t_1,t_2)=R_{XX}(t_1,t_2)-\mu_X(t_1)\mu_X(t_2)=\big(E[A^2]-E[A]^2\big)\cos(\omega_0t_1)\cos(\omega_0t_2)$$
$$\boxed{\ C_{XX}(t_1,t_2)=\tfrac1{12}\cos(\omega_0t_1)\cos(\omega_0t_2)\ }$$

**ii)** $A\sim\mathcal N(0{,}5,\ \tfrac1{12})$: acá $E[A]=0{,}5$ y $E[A^2]=\text{Var}(A)+E[A]^2=\tfrac1{12}+\tfrac14=\tfrac13$ — **exactamente los mismos** dos momentos que en (i). Como $R_{XX}$ y $C_{XX}$ solo dependen de $E[A]$ y $E[A^2]$ (no de la forma completa de la distribución de $A$), las fórmulas son **idénticas** a las de (i):
$$R_{XX}(t_1,t_2)=\tfrac13\cos(\omega_0t_1)\cos(\omega_0t_2),\qquad C_{XX}(t_1,t_2)=\tfrac1{12}\cos(\omega_0t_1)\cos(\omega_0t_2)$$
Dos distribuciones bien distintas para $A$ (uniforme vs. gaussiana) dan el mismo proceso hasta segundo orden.

**iii)** En ambos casos, $\mu_X(t)=\tfrac12\cos(\omega_0t)$ **depende de $t$**: ya falla la primera condición de WSS.
$$\boxed{\ X(t)\text{ no es WSS, ni en (i) ni en (ii)}\ }$$
Es el caso "fase fija" del Ejemplo del oscilador en el apunte (Caso 1): sin una fase aleatoria que "borre" el origen de tiempos, el proceso recuerda en qué instante está.

**b)** Con $A,B,\Theta_0,\Theta_1$ mutuamente independientes y $\Theta_0,\Theta_1\sim\mathcal U[0,2\pi)$, cada término se comporta como en el ejemplo del apunte: $E[A\cos(\omega_0t+\Theta_0)]=E[A]\cdot E[\cos(\omega_0t+\Theta_0)]=E[A]\cdot0=0$ (fase uniforme integra a cero para cualquier $t$ fijo), y lo mismo con $B,\Theta_1$. Entonces:
$$\boxed{\ E[X(t)]=0\ \ \text{para todo }t\ }$$
Para $R_{XX}(t_1,t_2)=E[X(t_1)X(t_2)]$, al distribuir el producto aparecen dos términos "cuadrados" ($A^2\cos\cos$, $B^2\cos\cos$) y dos "cruzados" ($AB$, mezclando $\omega_0$ y $\omega_1$). Los cruzados se anulan porque $\Theta_0$ y $\Theta_1$ son independientes entre sí, así que cada factor promedia a cero por separado:
$$E[AB\cos(\omega_0t_1+\Theta_0)\cos(\omega_1t_2+\Theta_1)]=E[A]E[B]\underbrace{E[\cos(\omega_0t_1+\Theta_0)]}_{0}\underbrace{E[\cos(\omega_1t_2+\Theta_1)]}_{0}=0$$
Los términos cuadrados son cada uno una copia del ejemplo del apunte (identidad $\cos\alpha\cos\beta=\tfrac12[\cos(\alpha-\beta)+\cos(\alpha+\beta)]$, y el término en $\alpha+\beta$ se anula al integrar la fase sobre un período completo):
$$E\big[A^2\cos(\omega_0t_1+\Theta_0)\cos(\omega_0t_2+\Theta_0)\big]=\frac{E[A^2]}{2}\cos\big(\omega_0(t_1-t_2)\big)$$
y análogamente con $B,\omega_1$. Sumando:
$$\boxed{\ E[X(t_1)X(t_2)]=\frac{E[A^2]}{2}\cos\big(\omega_0(t_1-t_2)\big)+\frac{E[B^2]}{2}\cos\big(\omega_1(t_1-t_2)\big)\ }$$
que depende solo de $\tau=t_1-t_2$. Media constante (cero) + autocorrelación función del lag:
$$\boxed{\ X(t)\text{ SÍ es WSS}\ }$$

###### **Verificación**
Caso (a): $\text{Var}(A)=1/12$ tanto en la uniforme como en la gaussiana ✓ (dato del enunciado). *(verificado numéricamente con $3\cdot10^6$ muestras, $\omega_0=2$, $t_1=0{,}3$, $t_2=1{,}1$: $R_{XX}$ teórico $=-0{,}16190$ contra Monte Carlo $=-0{,}16186$ con $A$ uniforme y $=-0{,}16197$ con $A$ gaussiana — las tres coinciden dentro del ruido de simulación, confirmando que la distribución de $A$ no importa más allá de sus dos primeros momentos.)* Caso (b): *(con $A\sim\mathcal U[0{,}5;1{,}5]$, $B\sim\mathcal U[0{,}2;0{,}9]$, $\omega_0=2$, $\omega_1=3{,}5$ y $3\cdot10^6$ muestras: medias $\approx0$ ✓, $R_{XX}$ teórico $=-0{,}17767$ contra Monte Carlo $=-0{,}17817$.)*

> [!info] Conexión
> El punto de (a.ii) es la misma idea que organiza buena parte del capítulo: dos distribuciones bien distintas para $A$ pueden dar exactamente el mismo comportamiento de segundo orden, que es todo lo que $R_{XX}$ y $C_{XX}$ pueden "ver".

---

## Ejercicio 9 — Coseno con frecuencia y fase aleatorias: WSS y ergódico en media, pero no en correlación

> [!quote] Enunciado
> 9. Considere un proceso aleatorio de tiempo continuo $x(t)$ definido de la siguiente manera:
> $$x(t)=\cos(\Omega t+\Theta), \qquad -\infty<t<\infty$$
> donde $\Omega$ y $\Theta$ son variables aleatorias estadísticamente independientes, con $\Omega$ tomando valores uniformemente distribuidos en el intervalo $[-\omega_o,\omega_o]$ y $\Theta$ tomando valores uniformemente distribuidos en el intervalo $[0,2\pi]$.
>
> Puede resultar útil la identidad trigonométrica:
> $$\cos(A)\cos(B)=\frac{\cos(A+B)+\cos(A-B)}{2}$$
>
> a) Determine los siguientes estadísticos de ensemble del proceso aleatorio $x(t)$:
> i) la función media $\mu_x(t)\triangleq E[x(t)]$, y
> ii) la función de correlación $R_{xx}(t_1,t_2)\triangleq E[x(t_1)x(t_2)]$.
> b) ¿Es el proceso WSS? ¿Es ergódico en media?
> c) Determine, en términos de $\Omega$ y $\Theta$, los siguientes promedios temporales de una única realización del proceso (por simplicidad notacional usamos $x(t)$ para denotar esa realización particular):
> $$\overline{x(t)}\triangleq\lim_{T\to\infty}\frac{1}{T}\int_{-T/2}^{T/2}x(t)\ dt$$
> $$\overline{x(t+\tau_o)x(t)}\triangleq\lim_{T\to\infty}\frac{1}{T}\int_{-T/2}^{T/2}x(t+\tau_o)x(t)\ dt$$
> donde $\tau_o$ es una constante positiva.
> d) ¿Se puede usar un registro muy largo de una única realización, con el promediado temporal adecuado, para calcular al menos aproximadamente $R_{xx}(t_1,t_2)$?

###### **Idea**
Para los estadísticos de ENSEMBLE (a) hay que promediar dos veces: primero en $\Theta$ (usando la identidad trigonométrica dada), después en $\Omega$. Para los promedios TEMPORALES (c), en cambio, $\Omega$ y $\Theta$ ya están fijos en el valor que les tocó a esa realización particular — son números, no variables aleatorias, dentro de esa cuenta — y aparece un caso límite ($\Omega=0$) que hay que tratar aparte.

###### **Resolución**
**a) i)** Condicionando en $\Omega=\omega$ y promediando primero en $\Theta$ (independiente de $\Omega$, uniforme en $[0,2\pi]$):
$$E[x(t)\mid\Omega=\omega]=E_\Theta[\cos(\omega t+\Theta)]=\frac{1}{2\pi}\int_0^{2\pi}\cos(\omega t+\theta)\,d\theta=0$$
para cualquier $\omega$ y $t$ (un coseno integrado sobre un período completo da cero). Como vale para todo $\omega$, promediar después en $\Omega$ no cambia nada:
$$\boxed{\ \mu_x(t)=0\ \ \text{para todo }t\ }$$

**ii)** Con la identidad dada, tomando $A=\Omega t_1+\Theta$, $B=\Omega t_2+\Theta$ (así $A-B=\Omega(t_1-t_2)$, $A+B=\Omega(t_1+t_2)+2\Theta$):
$$R_{xx}(t_1,t_2)=E\big[\cos(\Omega t_1+\Theta)\cos(\Omega t_2+\Theta)\big]=\frac12E\big[\cos(\Omega(t_1-t_2))\big]+\frac12E\big[\cos(\Omega(t_1+t_2)+2\Theta)\big]$$
El segundo término se anula: condicionando en $\Omega=\omega$, cuando $\Theta$ recorre $[0,2\pi)$ el argumento $2\Theta$ recorre $[0,4\pi)$ — dos períodos completos de coseno — así que $E_\Theta[\cos(\omega(t_1+t_2)+2\Theta)]=0$ para cualquier $\omega$, y por lo tanto también después de promediar en $\Omega$.

El primer término solo depende de $\tau=t_1-t_2$, y falta promediarlo sobre $\Omega\sim\mathcal U[-\omega_o,\omega_o]$:
$$E[\cos(\Omega\tau)]=\frac{1}{2\omega_o}\int_{-\omega_o}^{\omega_o}\cos(\Omega\tau)\,d\Omega=\frac{1}{2\omega_o}\cdot\frac{2\sin(\omega_o\tau)}{\tau}=\frac{\sin(\omega_o\tau)}{\omega_o\tau}\quad(\tau\neq0)$$
Entonces:
$$\boxed{\ R_{xx}(t_1,t_2)=\frac12\cdot\frac{\sin(\omega_o\tau)}{\omega_o\tau}\ ,\quad \tau=t_1-t_2\ \ \ \Big(\text{con }R_{xx}(0)=\tfrac12\text{ por continuidad}\Big)\ }$$

**b)** $\mu_x(t)=0$ es constante, y $R_{xx}(t_1,t_2)$ depende solo de $\tau=t_1-t_2$ (recién visto): **SÍ es WSS.** ¿Ergódico en media? Como $C_{xx}=R_{xx}$ (media nula) y
$$C_{xx}(\tau)=\frac{\sin(\omega_o\tau)}{2\omega_o\tau}\xrightarrow[\tau\to\infty]{}0$$
(decae como $1/|\tau|$, oscilando), con varianza finita $C_{xx}(0)=\tfrac12$, se cumple el criterio suficiente de la sección ERGODICIDAD del apunte:
$$\boxed{\ X(t)\text{ es WSS y ergódico en media}\ }$$

**c)** Acá $\Omega=\omega$ y $\Theta=\theta$ ya están fijos —son los valores de ESA realización—, y lo que se integra es en $t$:
$$\overline{x(t)}=\lim_{T\to\infty}\frac{1}{T}\int_{-T/2}^{T/2}\cos(\omega t+\theta)\,dt$$
Si $\omega\neq0$: la primitiva es $\sin(\omega t+\theta)/\omega$, acotada entre $-1/|\omega|$ y $1/|\omega|$; dividida por $T\to\infty$, el límite es $0$.
$$\boxed{\ \overline{x(t)}=0\ \ \text{si }\Omega\neq0\ }$$
Para el segundo promedio, con la misma identidad trigonométrica:
$$x(t+\tau_o)x(t)=\cos\big(\omega(t+\tau_o)+\theta\big)\cos(\omega t+\theta)=\frac{\cos(\omega\tau_o)+\cos(2\omega t+\omega\tau_o+2\theta)}{2}$$
El primer sumando es constante en $t$ y sobrevive el promedio tal cual; el segundo oscila a frecuencia $2\omega\neq0$ y su promedio temporal es $0$ por el mismo argumento de primitiva acotada sobre $T\to\infty$:
$$\boxed{\ \overline{x(t+\tau_o)x(t)}=\frac12\cos(\Omega\tau_o)\ \ \text{si }\Omega\neq0\ }$$
(dejamos $\Omega$ mayúscula para remarcar que es una cantidad ALEATORIA — depende de qué realización te tocó — y no un número fijo).

> [!warning] Ojo — el caso $\Omega=0$
> Si $\Omega=0$ (probabilidad cero, porque $\Omega$ es continua, pero vale la pena entender por qué hay que excluirlo), la realización es $x(t)=\cos\Theta$: una CONSTANTE en el tiempo. Ahí $\overline{x(t)}=\cos\Theta\neq0$ en general, y $\overline{x(t+\tau_o)x(t)}=\cos^2\Theta\neq\tfrac12\cos(0\cdot\tau_o)=\tfrac12$ en general: los dos resultados de arriba se caen. Es el mismo fenómeno del "ensemble de baterías" (Ejercicios 5 y 7): una realización degenerada (constante) no es representativa del ensemble. Como $P(\Omega=0)=0$ esto no afecta la conclusión "para casi toda realización", pero es el motivo técnico de pedir $\Omega\neq0$.

**d)** Para $\overline{x(t)}$: sí. Vale $0$ para casi toda realización ($\Omega\neq0$ c.s.), que coincide con $\mu_x(t)=0$ — consistente con la ergodicidad en media de (b). Pero para $R_{xx}(t_1,t_2)$ la respuesta es **no, en general**: el promedio temporal de segundo orden de una realización da $\tfrac12\cos(\Omega\tau_o)$, una cantidad que sigue siendo ALEATORIA (distinta realización a realización, según qué $\Omega$ le tocó). No converge al número determinístico $R_{xx}(\tau_o)=\sin(\omega_o\tau_o)/(2\omega_o\tau_o)$, que es un promedio ADICIONAL sobre $\Omega$. Un registro larguísimo de una sola realización da $\tfrac12\cos(\Omega\tau_o)$ para ESA $\Omega$ particular, no la autocorrelación del proceso.
$$\boxed{\ \text{El proceso es ergódico en media, pero NO en correlación}\ }$$

###### **Verificación**
$|\rho|$ implícito en $R_{xx}(\tau)/R_{xx}(0)=\text{sinc}$-like $\in[-1,1]$ ✓ (razonable, con $R_{xx}(0)=\tfrac12$ como máximo). *(verificado numéricamente: la fórmula $R_{xx}(\tau)=\sin(\omega_o\tau)/(2\omega_o\tau)$ coincide con la integración numérica en $\Omega$ hasta $10^{-6}$ para varios $\tau$, y Monte Carlo con $3\cdot10^6$ pares $(\Omega,\Theta)$ da, para $\omega_o=5$, $t_1=0{,}4$, $t_2=1{,}7$: $\hat R_{xx}=0{,}01663$ contra fórmula $=0{,}01655$. Simulando 4 realizaciones individuales con $T=2000$: en las cuatro $\overline{x(t)}\approx0$ (como predice (b)), pero $\overline{x(t+\tau_o)x(t)}$ da valores bien distintos entre sí —$-0{,}18$, $0{,}17$, $-0{,}49$ y $0{,}03$ para $\tau_o=0{,}7$— cada uno coincidiendo con $\tfrac12\cos(\Omega\tau_o)$ de SU $\Omega$ particular, no con un único valor común: la falta de ergodicidad en correlación, en los números.)*

> [!info] Conexión
> Este es el ejemplo más nítido del capítulo para la distinción "ergódico en media $\neq$ ergódico en correlación": la media SÍ se recupera de una sola realización, pero la correlación NO, porque $\Omega$ actúa como una "batería escondida" dentro de cada realización — se sortea una sola vez y después queda fija para siempre en esa trayectoria.

---

## Ejercicio 10 — Sinusoide de frecuencia y fase aleatorias, ¿es WSS?

> [!quote] Enunciado
> 10. Considere el proceso aleatorio
> $$X(t)=\cos(\Omega t+\Theta)$$
> donde $\Omega$ y $\Theta$ son variables aleatorias independientes, con $\Omega$ uniforme en $[-B_0,B_0]$ y $\Theta$ uniforme en $[-\pi,\pi]$.
>
> a) Determine $E[X(t)]$, el valor esperado de $X(t)$.
> b) Determine la autocorrelación $R_{XX}(t_1,t_2)=E[X(t_1)X(t_2)]$.
> c) ¿Es el proceso $X(t)$ WSS? Explique claramente por qué sí o por qué no.

###### **Idea**
Es la misma sinusoide de fase aleatoria del apunte principal, pero ahora la frecuencia $\Omega$ también es aleatoria. Como $\Theta$ es uniforme en un período completo, **para cualquier valor fijo de $\Omega$** el promedio sobre $\Theta$ de un coseno desplazado da cero. Eso mata todos los términos "malos" antes de promediar sobre $\Omega$.

###### **Resolución**
**a)** Condicionando en $\Omega=\omega$:
$$E[X(t)\mid\Omega=\omega]=E_\Theta[\cos(\omega t+\Theta)]=\frac{1}{2\pi}\int_{-\pi}^{\pi}\cos(\omega t+\theta)\ d\theta=0$$
(la integral de un coseno sobre un período completo es cero, para cualquier corrimiento de fase $\omega t$). Como esto vale para todo $\omega$, promediando sobre $\Omega$ también da cero:
$$\boxed{\ E[X(t)]=0\ \ \text{para todo }t\ }$$

**b)** Usamos la identidad producto-suma:
$$X(t_1)X(t_2)=\cos(\Omega t_1+\Theta)\cos(\Omega t_2+\Theta)=\frac12\Big[\cos\big(\Omega(t_1-t_2)\big)+\cos\big(\Omega(t_1+t_2)+2\Theta\big)\Big]$$
Tomamos esperanza condicionando primero en $\Omega=\omega$: el primer término no depende de $\Theta$, y el segundo se anula igual que en (a) (integrar $\cos(2\theta+c)$ sobre $\theta\in[-\pi,\pi]$ da cero para cualquier constante $c$, porque $2\theta$ recorre $[-2\pi,2\pi]$, un número entero de períodos). Entonces
$$R_{XX}(t_1,t_2)=E_\Omega\Big[\tfrac12\cos(\Omega\tau)\Big],\qquad \tau\triangleq t_1-t_2$$
y con $\Omega$ uniforme en $[-B_0,B_0]$:
$$E_\Omega[\cos(\Omega\tau)]=\frac{1}{2B_0}\int_{-B_0}^{B_0}\cos(\omega\tau)\ d\omega=\frac{1}{2B_0}\cdot\frac{2\sin(B_0\tau)}{\tau}=\frac{\sin(B_0\tau)}{B_0\tau}$$
Así que
$$\boxed{\ R_{XX}(t_1,t_2)=\frac12\,\frac{\sin(B_0\tau)}{B_0\tau},\qquad \tau=t_1-t_2\ }$$
con la convención habitual $R_{XX}(0)=\tfrac12$ (el límite de $\sin(x)/x$ en $x=0$).

**c)** La media es constante ($=0$) y $R_{XX}(t_1,t_2)$ depende de $t_1,t_2$ **solo a través de** $\tau=t_1-t_2$ (es la función sinc de arriba). Las dos condiciones de WSS se cumplen:
$$\boxed{\ X(t)\text{ es WSS}\ }$$

###### **Verificación**
$R_{XX}(0)=\tfrac12=\tfrac12 E[A^2]$ con $A=1$ tiene sentido dimensional (potencia de un coseno de amplitud unitaria). *(Verificado numéricamente: Monte Carlo con $B_0=3{,}7$ y $4\cdot10^6$ muestras da $E[X(t)]\approx 0{,}00009$, y $R_{XX}(t_1,t_2)$ evaluado en tres pares distintos con el mismo $\tau=1$ (por ejemplo $(t_1,t_2)=(1{,}0\ ;\ 0{,}0)$, $(5{,}0\ ;\ 4{,}0)$, $(10{,}2\ ;\ 9{,}2)$) da siempre $\approx-0{,}0714$, coincidiendo con la fórmula $\tfrac12\sin(B_0)/B_0\approx-0{,}0716$ — confirmando que depende solo de $\tau$.)*

> [!info] Conexión
> Es el mismo mecanismo del Ejercicio 9 (parte A): la fase uniforme "borra" el origen de tiempos. Acá encima promediamos sobre $\Omega$, así que el resultado es directamente la versión WSS — a diferencia del Ejercicio 9, donde $\Omega$ y $\Theta$ jugaban roles distintos (ahí se pedía además comparar con promedios temporales).

---

## Ejercicio 11 — Ergodicidad en media y el efecto de sumar una variable aleatoria constante

> [!quote] Enunciado
> 11. a) Suponga que $x(t)$ es un proceso aleatorio WSS con media $\mu_x$ y autocovarianza $C_{xx}(\tau)=\sigma^2 e^{-|\tau|}$. ¿Qué característica de esta caracterización garantiza que el proceso $x(t)$ es ergódico en media, es decir, que el promedio temporal iguala a la media del ensemble para casi toda realización?
> $$\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}x(t)\ dt=\mu_x$$
>
> b) Si ahora $y(t)=x(t)+Z$, donde $Z$ es una variable aleatoria de media nula con varianza $\sigma_Z^2$, no correlacionada con el proceso $x(t)$, determine la media $\mu_y$ y la autocovarianza $C_{yy}(\tau)$ del proceso $y(t)$. Determine además cuánto valdría el promedio temporal
> $$\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}y(t)\ dt$$
> para una realización genérica del proceso $y(t)$. Usando este resultado o de otra manera, determine si el proceso $y(t)$ es ergódico en media.

###### **Idea**
El criterio de ergodicidad en media (visto en el complemento, Parte 1.4) pide que la autocovarianza se "olvide" del pasado lo bastante rápido — concretamente, que sea absolutamente integrable, para que la varianza del promedio temporal se vaya a cero. En (b) el punto fino es que $Z$ es **una sola variable aleatoria**, la misma para todo $t$ dentro de una realización: no se "promedia" con el tiempo, así que sobrevive intacta en el límite.

###### **Resolución**
**a)** $C_{xx}(\tau)=\sigma^2e^{-|\tau|}$ es **absolutamente integrable**:
$$\int_{-\infty}^{\infty}|C_{xx}(\tau)|\ d\tau=\sigma^2\int_{-\infty}^{\infty}e^{-|\tau|}\ d\tau=2\sigma^2<\infty$$
Por el criterio suficiente de ergodicidad en media (Parte 1.4 del complemento): si $x(t)$ es WSS y $C_{xx}(\tau)\to0$ con suficiente rapidez como para ser integrable, entonces
$$\mathrm{Var}\Big[\frac{1}{2T}\int_{-T}^{T}x(t)\,dt\Big]=\frac{1}{2T}\int_{-2T}^{2T}\Big(1-\frac{|\tau|}{2T}\Big)C_{xx}(\tau)\ d\tau\ \xrightarrow[T\to\infty]{}\ 0$$
porque la integral está acotada por $\int|C_{xx}(\tau)|d\tau<\infty$ mientras el factor $1/(2T)$ que la multiplica se va a cero. Como el promedio temporal tiene esperanza $\mu_x$ (por Fubini, intercambiando integral y esperanza) y varianza que tiende a $0$, converge en media cuadrática (y, con el argumento completo del complemento, c.s.) a $\mu_x$.
$$\boxed{\ \text{La característica clave es que }C_{xx}(\tau)\to0\text{ lo bastante rápido para ser integrable (acá, decaimiento exponencial)}\ }$$

**b)** $Z$ es una variable aleatoria fija (no depende de $t$), de media $0$, no correlacionada con $x(\cdot)$.

*Media:*
$$\mu_y=E[y(t)]=E[x(t)]+E[Z]=\mu_x+0=\boxed{\ \mu_y=\mu_x\ }$$

*Autocovarianza:*
$$C_{yy}(\tau)=E\big[(x(t+\tau)-\mu_x+Z)(x(t)-\mu_x+Z)\big]$$
Expandiendo y usando que $Z$ no está correlacionada con $x(\cdot)$ (así que los términos cruzados $E[Z(x(t)-\mu_x)]$ se anulan):
$$C_{yy}(\tau)=C_{xx}(\tau)+E[Z^2]=\boxed{\ C_{yy}(\tau)=\sigma^2e^{-|\tau|}+\sigma_Z^2\ }$$

*Promedio temporal de una realización:* como $Z$ es la **misma** variable aleatoria para todo $t$ en esa realización, no se promedia — sale afuera de la integral tal cual:
$$\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}y(t)\,dt=\underbrace{\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}x(t)\,dt}_{=\ \mu_x\text{ (por la parte a)}}+\ \underbrace{\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}Z\,dt}_{=\ Z}=\boxed{\ \mu_x+Z\ }$$

*¿Ergódico en media?* El promedio temporal converge a $\mu_x+Z$, una **variable aleatoria** con varianza $\sigma_Z^2$ (no un número determinístico), mientras que $\mu_y=\mu_x$ es una constante. Para que $y(t)$ sea ergódico en media hace falta que el promedio temporal **iguale a $\mu_y$ para casi toda realización** — y eso solo pasa si $\sigma_Z^2=0$. En general:
$$\boxed{\ y(t)\text{ NO es ergódico en media (salvo el caso degenerado }\sigma_Z^2=0)\ }$$

###### **Verificación**
El promedio temporal de $x(t)$ debe tener varianza chica y decreciente con $T$; el de $y(t)$ debe estabilizarse en $\sigma_Z^2$ y no seguir bajando. *(Verificado numéricamente: simulando $x(t)$ como proceso AR(1) discretizado con paso $0{,}01$ y $T=200$ ($\mu_x=3$, $\sigma^2=4$), la varianza empírica del promedio temporal sobre 60 realizaciones da $0{,}018$ — chica, consistente con $\to0$. Agregando $Z\sim\mathcal N(0,9)$ fijo por realización, la varianza empírica del promedio temporal de $y$ da $7{,}34\approx\sigma_Z^2=9$ (la diferencia es la varianza residual de $x$, que en $T=200$ finito todavía no bajó del todo) — muy por arriba de cero, y del orden de $\sigma_Z^2$, no de la varianza de $x$.)*

> [!warning] Ojo
> No confundir "$Z$ no correlacionada con $x(\cdot)$" con "$Z=0$": el proceso $y(t)$ sigue siendo WSS (su media y autocovarianza no dependen de $t$), pero WSS **no implica** ergódico. Es el contraejemplo canónico: agregarle a un proceso ergódico una variable aleatoria "de fondo" (la misma en toda la realización) rompe la ergodicidad sin romper la estacionariedad en sentido amplio.

---

## Ejercicio 12 — Modulación por $(-1)^n$: de pasabajos a pasaaltos

> [!quote] Enunciado
> 12. Un proceso WSS de tiempo discreto y media nula $e[n]$ tiene autocorrelación
> $$R_{ee}[m]=\frac{\sin(\pi m/3)}{m}$$
> para $m\neq0$, y $R_{ee}[0]=\pi/3$. El proceso $x[n]$ se define por la relación
> $$x[n]=(-1)^n\ e[n]$$
> para todo $n$. Muestre que $x[n]$ es WSS y grafique su PSD $S_{xx}(e^{j\Omega})$ en la región $|\Omega|\leq\pi$. ¿Es $x[\cdot]$ además conjuntamente WSS con $e[\cdot]$?

###### **Idea**
$(-1)^n=e^{j\pi n}$ es una modulación a la frecuencia de Nyquist. Multiplicar por $e^{j\pi n}$ en el tiempo corre el espectro en $\pi$ (propiedad de modulación de la DTFT), así que basta reconocer que $R_{ee}[m]$ es la autocorrelación de un pasabajos ideal, y aplicar el corrimiento.

###### **Resolución**
**$x[n]$ es de media nula:** $E[x[n]]=(-1)^nE[e[n]]=(-1)^n\cdot0=0$ para todo $n$ (constante).

**Autocorrelación de $x[n]$:**
$$R_{xx}[n+m,n]=E[x[n+m]x[n]]=E\big[(-1)^{n+m}e[n+m]\,(-1)^{n}e[n]\big]=(-1)^{2n+m}\,E[e[n+m]e[n]]=(-1)^m R_{ee}[m]$$
(porque $(-1)^{2n}=1$). Esto depende **solo de $m$**, no de $n$: junto con la media nula constante, $x[n]$ es WSS, con
$$\boxed{\ R_{xx}[m]=(-1)^m\,R_{ee}[m]\ }$$

**Identificando $R_{ee}[m]$ como un pasabajos ideal.** Reescribimos $R_{ee}[m]=\dfrac{\sin(\pi m/3)}{m}=\pi\cdot\dfrac{\sin\big((\pi/3)m\big)}{\pi m}$. La pareja DTFT estándar es
$$h[n]=\frac{\sin(\Omega_c n)}{\pi n}\ \ \longleftrightarrow\ \ H(e^{j\Omega})=\begin{cases}1,&|\Omega|<\Omega_c\\0,&\Omega_c<|\Omega|\leq\pi\end{cases}$$
Con $\Omega_c=\pi/3$, $R_{ee}[m]=\pi\, h[m]$, así que su PSD es un **pasabajos ideal** de altura $\pi$ y corte en $\pi/3$:
$$S_{ee}(e^{j\Omega})=\begin{cases}\pi,&|\Omega|<\pi/3\\0,&\pi/3<|\Omega|\leq\pi\end{cases}$$
(chequeo rápido: la transformada inversa de este rectángulo en $\Omega=0$ da $R_{ee}[0]=\frac{1}{2\pi}\cdot\pi\cdot\frac{2\pi}{3}=\frac{\pi}{3}$ ✓, y para $m\neq0$ da $\frac{1}{2\pi}\int_{-\pi/3}^{\pi/3}\pi e^{j\Omega m}d\Omega=\frac{\sin(\pi m/3)}{m}$ ✓).

**Aplicando la modulación.** Como $(-1)^m=e^{j\pi m}$, multiplicar la secuencia por $(-1)^n$ corre el espectro en $\Omega=\pi$ (propiedad de modulación: $x[n]=e^{j\pi n}e[n]\ \Leftrightarrow\ S_{xx}(e^{j\Omega})=S_{ee}(e^{j(\Omega-\pi)})$). El pasabajos centrado en $0$ se convierte en una banda centrada en $\Omega=\pi$ (el Nyquist), que dentro de $|\Omega|\leq\pi$ es un **pasaaltos ideal**:
$$\boxed{\ S_{xx}(e^{j\Omega})=\begin{cases}\pi,&\dfrac{2\pi}{3}<|\Omega|\leq\pi\\[4pt]0,&|\Omega|<\dfrac{2\pi}{3}\end{cases}\ }$$

![[sol10-ej12-psd-xn.svg]]
*Se ve la banda que "sobrevivía" de $e[n]$ (las bajas frecuencias, $|\Omega|<\pi/3$) reflejada al extremo opuesto del eje: ahora son las altas frecuencias cercanas a $\pi$ las que tienen potencia.*

**¿Conjuntamente WSS con $e[\cdot]$?** Calculamos la correlación cruzada:
$$R_{xe}[n+m,n]=E[x[n+m]e[n]]=E\big[(-1)^{n+m}e[n+m]e[n]\big]=(-1)^{n+m}R_{ee}[m]$$
Esta expresión **depende de $n$** (a través de la paridad de $(-1)^{n+m}$), no solo del lag $m$. Por lo tanto:
$$\boxed{\ x[\cdot]\text{ y }e[\cdot]\text{ NO son conjuntamente WSS}\ }$$

###### **Verificación**
$S_{xx}(e^{j\Omega})\geq0$ ✓ y es real y par ✓ (propiedades obligatorias de toda PSD). Además $\int_{-\pi}^{\pi}S_{xx}\,d\Omega=\int_{-\pi}^{\pi}S_{ee}\,d\Omega=2\pi R_{ee}[0]=2\pi\cdot\pi/3$ (la potencia total se conserva, como debe ser: modular no crea ni destruye potencia, solo la mueve en frecuencia). *(Verificado numéricamente: calculando la DTFT truncada (suma con $|m|\leq4000$) de $R_{ee}[m]$ y de $R_{xx}[m]=(-1)^mR_{ee}[m]$, se obtiene $S_{ee}(\Omega{=}0{,}2)\approx3{,}142\approx\pi$ y $S_{ee}(\Omega{=}1{,}5)\approx0$ (fuera de banda); y $S_{xx}(\Omega{=}\pi{-}0{,}2)\approx3{,}142\approx\pi$ mientras $S_{xx}(\Omega{=}0{,}5)\approx0$ — exactamente el corrimiento predicho.)*

> [!info] Conexión
> Este es el mecanismo de "modelador/blanqueador" del apunte principal aplicado al revés: acá no partimos de blanco, pero el truco de leer $R_{ee}[m]$ como (una escala de) la respuesta al impulso de un pasabajos ideal es el mismo que se usa para leer PSDs racionales de $S_{xx}(z)$ en la sección de factorización espectral.

---

## Ejercicio 13 — Filtrado FIR de ruido blanco: autocorrelación y correlación cruzada

> [!quote] Enunciado
> 13. Suponga que $x[n]$ es una secuencia aleatoria WSS de media nula con autocorrelación $R_{xx}[m]=\delta[m]$, y que es la entrada de un sistema LTI con respuesta al impulso
> $$h[n]=\begin{cases}1 & n=0,1,2\\ 0 & \text{en otro caso}\end{cases}$$
> La salida del sistema es $y[n]$. Determine $R_{yy}[m]$ y $R_{xy}[m]$, definidas como:
> $$R_{yy}[m]\triangleq E(y[n+m]y[n]) \qquad R_{xy}[m]\triangleq E(x[n+m]y[n])$$

###### **Idea**
Con entrada blanca, ambas fórmulas colapsan a expresiones puramente **determinísticas** en $h[n]$: $R_{yy}[m]$ es la autocorrelación determinística de $h$, y $R_{xy}[m]$ es (una versión reflejada de) $h$ mismo. Vale la pena derivarlas una vez en general porque se reusan todo el capítulo.

###### **Resolución**
$y[n]=\sum_k h[k]\,x[n-k]$.

**$R_{yy}[m]$.**
$$R_{yy}[m]=E[y[n+m]y[n]]=\sum_k\sum_l h[k]h[l]\,E[x[n+m-k]x[n-l]]=\sum_k\sum_l h[k]h[l]\,R_{xx}[m-k+l]$$
Con $R_{xx}[m-k+l]=\delta[m-k+l]$, la doble suma colapsa poniendo $l=k-m$:
$$R_{yy}[m]=\sum_k h[k]\,h[k-m]$$
que es la **autocorrelación determinística** de $h[n]$. Con $h=[1,1,1]$ en $n=0,1,2$ (energía total $3$), calculamos para cada corrimiento (solo sobreviven $|m|\leq2$, porque $h$ tiene soporte de largo 3):
$$R_{yy}[0]=1^2+1^2+1^2=3,\qquad R_{yy}[\pm1]=1\cdot1+1\cdot1=2,\qquad R_{yy}[\pm2]=1\cdot1=1$$
$$\boxed{\ R_{yy}[m]=3\,\delta[m]+2\big(\delta[m-1]+\delta[m+1]\big)+\delta[m-2]+\delta[m+2]\ }$$
(un "triángulo" $\{1,2,3,2,1\}$ para $m=-2,\dots,2$, y $0$ fuera de ese rango).

**$R_{xy}[m]$.**
$$R_{xy}[m]=E[x[n+m]y[n]]=\sum_k h[k]\,E[x[n+m]x[n-k]]=\sum_k h[k]\,R_{xx}[m+k]=\sum_k h[k]\,\delta[m+k]=h[-m]$$
Con $h[n]$ soportado en $n=0,1,2$: $h[-m]\neq0$ solo si $-m\in\{0,1,2\}$, es decir $m\in\{0,-1,-2\}$, y ahí vale $1$:
$$\boxed{\ R_{xy}[m]=\delta[m]+\delta[m+1]+\delta[m+2]\ }$$
(vale $1$ en $m=0,-1,-2$ y $0$ en cualquier otro lado — noten que es **causal hacia atrás**: $y[n]$ depende de $x[n],x[n-1],x[n-2]$, así que solo se correlaciona con "adelantos" de $x$, $m\leq0$).

###### **Verificación**
$R_{yy}[0]=3>0$ (varianza de $y$, tiene que ser positiva) y $R_{yy}$ es simétrica, $R_{yy}[m]=R_{yy}[-m]$ ✓ (toda autocorrelación real lo es). *(Verificado numéricamente: simulando $x[n]$ blanco gaussiano de varianza 1 con $4\cdot10^6$ muestras y filtrando con $h=[1,1,1]$, la autocorrelación muestral de $y$ da $\{1{,}00;\,2{,}00;\,3{,}00;\,2{,}00;\,1{,}00\}$ para $m=-2,\dots,2$, y la correlación cruzada muestral $R_{xy}[m]$ da $\{1{,}00;\,1{,}00;\,1{,}00\}$ en $m=-2,-1,0$ y $\approx0$ en el resto — coincide con lo calculado.)*

> [!info] Conexión
> Esta es exactamente la identificación de sistemas por correlación cruzada del Ejercicio 7 de la Parte 5 del complemento: con entrada blanca, $R_{xy}[m]=h[-m]$ (o $R_{yx}[m]=h[m]$, según cómo se defina el orden) te da la respuesta al impulso directamente, sin necesidad de excitar el sistema con un impulso real.

---

## Ejercicio 14 — Filtrado y "borrado" aleatorio (Bernoulli) de un proceso blanco

> [!quote] Enunciado
> 14. Suponga que el proceso aleatorio de tiempo discreto $w[n]$ es WSS con media $\mu$, y con autocovarianza $C_{ww}[m]=\sigma^2\delta[m]$. Sea $w[n]$ aplicado a la entrada de un sistema LTI estable con respuesta al impulso $h[n]=\alpha^n u[n]$, donde $u[n]$ es el escalón unitario. Denote por $y[n]$ el proceso aleatorio a la salida de este sistema.
>
> Ahora suponga que generamos otro proceso aleatorio $x[n]$ a partir de $w[n]$ según la ecuación $x[n]=b[n]w[n]$, donde $b[n]$ es un proceso de Bernoulli cuyo valor en cualquier instante es $1$ con probabilidad $p$, y $0$ en caso contrario. Se puede pensar a $x[n]$ como una versión corrompida de $w[n]$, en la que muestras aleatorias de $w[n]$ se ponen en cero. Asuma que el proceso $b[\cdot]$ es independiente de $w[\cdot]$. Escriba expresiones para:
>
> a) la autocorrelación $R_{ww}[m]$ del proceso $w[n]$;
> b) la media $\mu_y$ y la autocovarianza $C_{yy}[m]$ del proceso $y[n]$;
> c) la covarianza cruzada $C_{yw}[m]$ de los procesos $y[\cdot]$ y $w[\cdot]$;
> d) la media $\mu_x$ y la autocovarianza $C_{xx}[m]$ del proceso $x[n]$;
> e) la covarianza cruzada $C_{xw}[m]$ de los procesos $x[\cdot]$ y $w[\cdot]$; y
> f) la covarianza cruzada $C_{yx}[m]$ de los procesos $y[\cdot]$ y $x[\cdot]$.

###### **Idea**
Es un ejercicio largo pero mecánico: (a)-(c) son filtrado LTI estándar del capítulo (como el Ejercicio 13). Lo nuevo es el "thinning" Bernoulli de (d)-(f): como $b[n]$ es i.i.d. e independiente de $w[\cdot]$, cada vez que aparece un producto $b[n_1]b[n_2]$ con $n_1\neq n_2$ se factoriza en $p^2$, y solo en $n_1=n_2$ aporta $p$ (porque $b^2=b$ para una Bernoulli). Ese es el único mecanismo que hay que aplicar con cuidado en cada ítem.

###### **Resolución**

**a) $R_{ww}[m]$.** Por definición, autocorrelación = autocovarianza + producto de medias:
$$\boxed{\ R_{ww}[m]=C_{ww}[m]+\mu^2=\sigma^2\delta[m]+\mu^2\ }$$

**b) $\mu_y$ y $C_{yy}[m]$.** Con $y[n]=\sum_k h[k]w[n-k]=\sum_{k=0}^{\infty}\alpha^k w[n-k]$ (converge porque $|\alpha|<1$, estabilidad):
$$\mu_y=\sum_{k=0}^{\infty}\alpha^k\mu=\frac{\mu}{1-\alpha}$$
Para la autocovarianza, usamos que $y[n]-\mu_y=\sum_k h[k]\,(w[n-k]-\mu)$ (el filtro es lineal, así que centra igual que $w$):
$$C_{yy}[m]=\sum_k\sum_l h[k]h[l]\,C_{ww}[m-k+l]=\sigma^2\sum_k h[k]h[k-m]$$
(mismo colapso que en el Ejercicio 13, con $R_{xx}\to C_{ww}=\sigma^2\delta[\cdot]$). Con $h[k]=\alpha^ku[k]$, para $m\geq0$:
$$\sum_k h[k]h[k-m]=\sum_{k=m}^{\infty}\alpha^k\alpha^{k-m}=\alpha^{-m}\sum_{k=m}^{\infty}\alpha^{2k}=\alpha^{-m}\cdot\frac{\alpha^{2m}}{1-\alpha^2}=\frac{\alpha^{m}}{1-\alpha^2}$$
y por simetría (la suma es par en $m$):
$$\boxed{\ \mu_y=\frac{\mu}{1-\alpha}\ ,\qquad C_{yy}[m]=\frac{\sigma^2\,\alpha^{|m|}}{1-\alpha^2}\ }$$

**c) $C_{yw}[m]$.**
$$C_{yw}[m]\triangleq E[(y[n+m]-\mu_y)(w[n]-\mu)]=\sum_k h[k]\,E[(w[n+m-k]-\mu)(w[n]-\mu)]=\sum_k h[k]\,C_{ww}[m-k]=\sigma^2h[m]$$
$$\boxed{\ C_{yw}[m]=\sigma^2\,\alpha^m\,u[m]\ }$$
(cero para $m<0$: tiene sentido, $y[n]$ es causal en $w$, así que no puede estar correlacionado con muestras futuras de $w$).

**d) $\mu_x$ y $C_{xx}[m]$.** Como $b[\cdot]\perp w[\cdot]$:
$$\mu_x=E[b[n]w[n]]=E[b[n]]\,E[w[n]]=p\mu$$
Para la covarianza necesitamos $E[x[n+m]x[n]]=E[b[n+m]b[n]]\,E[w[n+m]w[n]]$ (factoriza porque el par $\{b[n+m],b[n]\}$ es independiente del par $\{w[n+m],w[n]\}$). El primer factor, usando que $b^2=b$ para Bernoulli e independencia entre instantes distintos:
$$E[b[n+m]b[n]]=\begin{cases}E[b[n]^2]=p,& m=0\\ E[b[n+m]]E[b[n]]=p^2,& m\neq0\end{cases}=p^2+p(1-p)\delta[m]$$
y el segundo es $R_{ww}[m]=\sigma^2\delta[m]+\mu^2$ (parte a). Multiplicando y usando $\delta[m]^2=\delta[m]$:
$$E[x[n+m]x[n]]=\big(p^2+p(1-p)\delta[m]\big)\big(\sigma^2\delta[m]+\mu^2\big)=p^2\mu^2+\delta[m]\Big[p\sigma^2+p(1-p)\mu^2\Big]$$
Restando $\mu_x^2=p^2\mu^2$:
$$\boxed{\ \mu_x=p\mu\ ,\qquad C_{xx}[m]=p\big[\sigma^2+(1-p)\mu^2\big]\,\delta[m]\ }$$
($x[n]$ resulta **blanco**: aunque $w$ ya era blanco en covarianza, uno podría temer que el "recorte" Bernoulli introdujera memoria, pero como $b[\cdot]$ es i.i.d. no la introduce.)

**e) $C_{xw}[m]$.**
$$C_{xw}[m]\triangleq E[(x[n+m]-\mu_x)(w[n]-\mu)]=E[x[n+m]w[n]]-\mu_x\mu$$
$$E[x[n+m]w[n]]=E[b[n+m]w[n+m]w[n]]=E[b[n+m]]\,E[w[n+m]w[n]]=p\,R_{ww}[m]=p\big(\sigma^2\delta[m]+\mu^2\big)$$
$$C_{xw}[m]=p\sigma^2\delta[m]+p\mu^2-p\mu^2=\boxed{\ C_{xw}[m]=p\,\sigma^2\,\delta[m]\ }$$

**f) $C_{yx}[m]$.** Escribimos $x[n]-\mu_x=b[n](w[n]-\mu)+\mu(b[n]-p)$ (se verifica expandiendo: $b[n]w[n]-b[n]\mu+b[n]\mu-p\mu=b[n]w[n]-p\mu$ ✓). Entonces
$$C_{yx}[m]=E\Big[\sum_k h[k](w[n+m-k]-\mu)\cdot\big(b[n](w[n]-\mu)+\mu(b[n]-p)\big)\Big]$$
El término con $(b[n]-p)$ se anula: $b[n]-p$ es independiente de todo el proceso $w$ y tiene media cero, así que $E[(w[n+m-k]-\mu)(b[n]-p)]=0$. Queda solo
$$C_{yx}[m]=\sum_k h[k]\,E[b[n]]\,E[(w[n+m-k]-\mu)(w[n]-\mu)]=p\sum_k h[k]\,C_{ww}[m-k]=p\,\sigma^2\,h[m]$$
$$\boxed{\ C_{yx}[m]=p\,\sigma^2\,\alpha^m\,u[m]=p\,C_{yw}[m]\ }$$
(tiene sentido: en covarianza, $x$ es $w$ "atenuado" por el factor $p$, y esa atenuación se traslada tal cual a la covarianza cruzada con $y$).

###### **Verificación**
Todas las autocovarianzas dan $\geq0$ en $m=0$ ($C_{yy}[0]=\sigma^2/(1-\alpha^2)>0$, $C_{xx}[0]=p[\sigma^2+(1-p)\mu^2]>0$) ✓. *(Verificado numéricamente con $\alpha=0{,}6$, $p=0{,}7$, $\mu=2$, $\sigma^2=3$ y $3\cdot10^6$ muestras: $R_{ww}[0]$ emp. $7{,}00$ vs teórico $7{,}00$; $\mu_y$ emp. $5{,}00$ vs $5{,}00$; $C_{yy}[0]$ emp. $4{,}69$ vs $4{,}69$; $C_{yy}[1]$ emp. $2{,}82$ vs $2{,}81$; $C_{yw}[0]$ emp. $3{,}00$ vs $3{,}00$; $\mu_x$ emp. $1{,}40$ vs $1{,}40$; $C_{xx}[0]$ emp. $2{,}94$ vs $2{,}94$, $C_{xx}[1]$ emp. $\approx0$ vs $0$; $C_{xw}[0]$ emp. $2{,}10$ vs $2{,}10$; $C_{yx}[0]$ emp. $2{,}10$ vs $2{,}10$, $C_{yx}[3]$ emp. $0{,}456$ vs $0{,}454$. Todos coinciden dentro del error de muestreo.)*

> [!warning] Ojo
> El paso que más se presta a error es (d): hay que resistir la tentación de escribir $E[b[n+m]b[n]]=p^2$ para todo $m$. Solo vale para $m\neq0$; en $m=0$, $b[n]^2=b[n]$ (no $b[n]^2=p^2$), así que $E[b[n]^2]=p$, no $p^2$. Ese es el único lugar donde entra el $\delta[m]$ extra que después sobrevive en $C_{xx}[m]$.

---

## Ejercicio 15 — Señal más ruido a la salida de un filtro: todas las correlaciones cruzadas

> [!quote] Enunciado
> 15. Como se muestra en la figura, $p(t)$ es la salida de un sistema LTI estable con respuesta al impulso $h(\cdot)$ y entrada WSS $x(\cdot)$, de modo que
> $$p(t)=\int_{-\infty}^{\infty}h(\alpha)\ x(t-\alpha)\ d\alpha$$
> Suponga que $y(t)=p(t)+e(t)$ para algún proceso WSS de media nula $e(\cdot)$ no correlacionado con $x(\cdot)$. Sean $R_{ee}(\tau)$ y $R_{xx}(\tau)$ las autocorrelaciones de $e(\cdot)$ y $x(\cdot)$ respectivamente.
>
> ![[ej-p10-15.png]]
>
> a) Exprese $R_{px}(\tau)$ en términos de una combinación apropiada de $h(\cdot)$ y $R_{xx}(\cdot)$.
> b) Determine $R_{xe}(\tau)$ y explique por qué $R_{pe}(\tau)=0$.
> c) Escriba $R_{ye}(\tau)$, $R_{yp}(\tau)$, $R_{yx}(\tau)$ y $R_{yy}(\tau)$ en términos de combinaciones apropiadas de $h(\cdot)$, $R_{ee}(\cdot)$ y $R_{xx}(\cdot)$.

###### **Idea**
Es el modelo "señal filtrada más ruido independiente" que va a reaparecer en todo el capítulo 12 (Wiener). La cuenta se reduce a dos hechos: (1) $p(t)$ es una combinación lineal de $x(\cdot)$, así que hereda cualquier "no correlación" que tenga $x$ con otro proceso; y (2) $R_{hh}(\tau)\triangleq h(\tau)*h(-\tau)$ (la autocorrelación determinística de $h$, ya usada en la Parte 5 del complemento) aparece cada vez que se autocorrelaciona una señal filtrada.

###### **Resolución**
**a)** Por definición de correlación cruzada entre la salida $p$ y la entrada $x$ de un filtro LTI:
$$R_{px}(\tau)\triangleq E[p(t+\tau)x(t)]=\int h(\alpha)\,E[x(t+\tau-\alpha)x(t)]\,d\alpha=\int h(\alpha)\,R_{xx}(\tau-\alpha)\,d\alpha$$
$$\boxed{\ R_{px}(\tau)=h(\tau)*R_{xx}(\tau)\ }$$

**b) $R_{xe}(\tau)$ y por qué $R_{pe}(\tau)=0$.** "$e(\cdot)$ no correlacionado con $x(\cdot)$" (con $e$ de media nula) significa que la covarianza cruzada es idénticamente nula, es decir $R_{xe}(\tau)-\mu_x\cdot0=0$ para todo $\tau$:
$$\boxed{\ R_{xe}(\tau)=0\ \ \text{para todo }\tau\ }$$
Como $p$ es una combinación lineal (integral) de valores de $x$, y **cada uno** de esos valores tiene correlación cruzada nula con $e$ en cualquier lag, la combinación también:
$$R_{pe}(\tau)=E[p(t+\tau)e(t)]=\int h(\alpha)\,\underbrace{E[x(t+\tau-\alpha)e(t)]}_{=\,R_{xe}(\tau-\alpha)\,=\,0}\,d\alpha=0$$
$$\boxed{\ R_{pe}(\tau)=0\ \ \text{para todo }\tau\ }$$

**c)** Con $y=p+e$, cada correlación se expande linealmente y los términos cruzados con $e$ y $p$ se anulan por (b):

$$R_{ye}(\tau)=E[(p(t+\tau)+e(t+\tau))e(t)]=\underbrace{R_{pe}(\tau)}_{=0}+R_{ee}(\tau)\ \ \Rightarrow\ \ \boxed{\ R_{ye}(\tau)=R_{ee}(\tau)\ }$$

Para $R_{yp}$ y $R_{yy}$ hace falta primero $R_{pp}(\tau)$, la autocorrelación de la señal filtrada:
$$R_{pp}(\tau)=E[p(t+\tau)p(t)]=\iint h(\alpha)h(\beta)\,R_{xx}(\tau-\alpha+\beta)\,d\alpha\,d\beta=\big[h(\tau)*h(-\tau)\big]*R_{xx}(\tau)\triangleq R_{hh}(\tau)*R_{xx}(\tau)$$

$$R_{yp}(\tau)=E[(p(t+\tau)+e(t+\tau))p(t)]=R_{pp}(\tau)+\underbrace{R_{ep}(\tau)}_{=\,R_{pe}(-\tau)\,=\,0}\ \ \Rightarrow\ \ \boxed{\ R_{yp}(\tau)=R_{hh}(\tau)*R_{xx}(\tau)\ }$$

$$R_{yx}(\tau)=E[(p(t+\tau)+e(t+\tau))x(t)]=R_{px}(\tau)+\underbrace{R_{ex}(\tau)}_{=\,R_{xe}(-\tau)\,=\,0}\ \ \Rightarrow\ \ \boxed{\ R_{yx}(\tau)=h(\tau)*R_{xx}(\tau)\ }$$

$$R_{yy}(\tau)=E[(p(t+\tau)+e(t+\tau))(p(t)+e(t))]=R_{pp}(\tau)+\underbrace{R_{pe}(\tau)}_{=0}+\underbrace{R_{ep}(\tau)}_{=0}+R_{ee}(\tau)$$
$$\boxed{\ R_{yy}(\tau)=R_{hh}(\tau)*R_{xx}(\tau)+R_{ee}(\tau)\ }$$

###### **Verificación**
Todos los términos cruzados con $e$ (que no es la señal filtrada) se cancelan: $R_{yy}$ termina siendo simplemente "potencia de la señal filtrada más potencia del ruido", sin términos de interferencia — exactamente lo que se espera de ruido *aditivo independiente*. *(Verificado numéricamente: con $h(t)=e^{-2t}u(t)$, $R_{xx}(\tau)=3e^{-1{,}5|\tau|}$ y $R_{ee}(\tau)=0{,}7e^{-4|\tau|}$, la convolución numérica de $R_{px}(\tau)=h(\tau)*R_{xx}(\tau)$ evaluada en $\tau=1$, $-1$ y $0{,}5$ da $0{,}646$, $0{,}195$ y $0{,}949$, contra $0{,}643$, $0{,}191$ y $0{,}942$ calculados con sympy integrando la expresión cerrada — coinciden dentro del error de discretización.)*

> [!info] Conexión
> Esta es la estructura "señal + ruido no correlacionado" que organiza el capítulo 12 (Estimación de señales / Wiener): $x$ es la señal, $h$ el sistema que la deforma, $e$ el ruido de observación. La fórmula $R_{yy}=R_{hh}*R_{xx}+R_{ee}$ es la que después, en el dominio de la frecuencia, se convierte en $S_{yy}=|H|^2S_{xx}+S_{ee}$.

---

## Ejercicio 16 — Verdadero o falso sobre filtrado LTI de procesos WSS

> [!quote] Enunciado
> 16. Para cada uno de los siguientes puntos, indique si la afirmación dada es verdadera o falsa. Para una afirmación verdadera, dé una explicación breve pero convincente; para una falsa, dé un contraejemplo o una explicación convincente.
>
> a) Considere un sistema LTI de tiempo continuo cuya respuesta al impulso es $\delta(t-17)$. Si la entrada a este sistema es un proceso WSS $x(t)$ con autocorrelación $R_{xx}(\tau)$, entonces el correspondiente proceso de salida WSS $y(t)$ tiene autocorrelación $R_{yy}(\tau)=R_{xx}(\tau)$.
> b) Suponga que la entrada WSS $x(t)$ a un sistema LTI estable de tiempo continuo tiene autocorrelación $R_{xx}(\tau)=e^{-|\tau|}$. Es posible que el correspondiente proceso de salida WSS $y(t)$ tenga autocorrelación $R_{yy}(\tau)=e^{-3|\tau|}$.
> c) Suponga que $x(t)$ es un proceso aleatorio WSS de tiempo continuo con autocorrelación $R_{xx}(\tau)$, y sea $y(t)$ definido como
> $$y(t)=\frac{dx(t)}{dt}$$
> Entonces
> $$R_{yx}(\tau)=\frac{dR_{xx}(\tau)}{d\tau}$$

###### **Idea**
(a) es un caso particular de (c) del Ejercicio 15 con $h(t)=\delta(t-17)$ (retardo puro). (b) hay que resolverlo "al revés": preguntarse si existe algún $H(j\omega)$ físicamente realizable (estable, causal) tal que $|H(j\omega)|^2=S_{yy}/S_{xx}$ sea consistente — y si existe, exhibirlo. (c) sale de derivar bajo el signo de esperanza, el mismo tipo de intercambio que ya se justificó en el Hueco 1 de la Parte 1.3 del complemento.

###### **Resolución**

**a) VERDADERO.** Un retardo puro es un caso particular de filtro LTI estable ($h(t)=\delta(t-17)$ es absolutamente integrable en el sentido generalizado; $H(j\omega)=e^{-j17\omega}$, con $|H(j\omega)|=1$ para todo $\omega$). La salida es $y(t)=x(t-17)$. Como $x(t)$ es WSS:
$$R_{yy}(\tau)=E[y(t+\tau)y(t)]=E[x(t+\tau-17)x(t-17)]=R_{xx}(\tau)$$
porque la autocorrelación de un proceso WSS evaluada en dos instantes solo depende de su diferencia, y esa diferencia sigue siendo $\tau$ aunque ambos instantes se corran igual (los $17$ se cancelan). Retrasar un proceso WSS no cambia su segunda estadística.
$$\boxed{\ \text{a) Verdadero: }R_{yy}(\tau)=R_{xx}(\tau)\ }$$

**b) VERDADERO — es posible.** Necesitamos $S_{yy}(j\omega)=|H(j\omega)|^2S_{xx}(j\omega)$ con $S_{xx}(j\omega)=\mathcal F\{e^{-|\tau|}\}=\dfrac{2}{1+\omega^2}$ y target $S_{yy}(j\omega)=\mathcal F\{e^{-3|\tau|}\}=\dfrac{6}{9+\omega^2}$. Entonces
$$|H(j\omega)|^2=\frac{S_{yy}(j\omega)}{S_{xx}(j\omega)}=\frac{6/(9+\omega^2)}{2/(1+\omega^2)}=\frac{3(1+\omega^2)}{9+\omega^2}$$
Esta función es real, no negativa y acotada para todo $\omega$ (en $\omega=0$ vale $1/3$, y cuando $\omega\to\infty$ tiende a $3$): es un candidato razonable a $|H|^2$ de un filtro propio. Factorizando con $1+\omega^2=(1+j\omega)(1-j\omega)$ y $9+\omega^2=(3+j\omega)(3-j\omega)$:
$$|H(j\omega)|^2=\underbrace{\frac{\sqrt3\,(1+j\omega)}{3+j\omega}}_{H(j\omega)}\cdot\underbrace{\frac{\sqrt3\,(1-j\omega)}{3-j\omega}}_{H(j\omega)^*}$$
$$H(s)=\frac{\sqrt3\,(s+1)}{s+3}$$
tiene un polo en $s=-3$ (semiplano izquierdo: **estable y causal**) y un cero en $s=-1$: es un filtro de primer orden realizable, un "shelving filter" que atenúa las bajas frecuencias (factor $1/3$ en $\omega=0$) y deja pasar más las altas (factor $3$ para $\omega\to\infty$) — coherente con pasar de una correlación "más lenta" ($\alpha=1$) a una "más rápida" ($\alpha=3$), que tiene más contenido en alta frecuencia relativo a la baja.
$$\boxed{\ \text{b) Verdadero: existe, por ejemplo } H(s)=\dfrac{\sqrt3\,(s+1)}{s+3}\ }$$

**c) VERDADERO.** Por definición, $R_{xx}(\tau)=E[x(t+\tau)x(t)]$. Derivando respecto de $\tau$ e intercambiando derivada con esperanza (válido bajo las condiciones de regularidad estándar del capítulo — el mismo tipo de intercambio que se justifica en el Hueco 1 de la Parte 1.3 del complemento, ahí para la integral de un filtro LTI, acá para un límite de cociente incremental):
$$\frac{d}{d\tau}R_{xx}(\tau)=\frac{d}{d\tau}E[x(t+\tau)x(t)]=E\Big[\frac{\partial}{\partial\tau}x(t+\tau)\cdot x(t)\Big]=E[x'(t+\tau)\,x(t)]=E[y(t+\tau)x(t)]=R_{yx}(\tau)$$
$$\boxed{\ \text{c) Verdadero: }R_{yx}(\tau)=\dfrac{dR_{xx}(\tau)}{d\tau}\ }$$

###### **Verificación**
En (b), $|H(j0)|^2=1/3>0$ y $|H(j\omega)|^2\to3$ acotado (no diverge), consistentes con un sistema propio realizable ✓. *(Verificado numéricamente: evaluando $H(j\omega)=\sqrt3(1+j\omega)/(3+j\omega)$ en $\omega=0,1,2,5,10$ se obtiene $|H|^2=0{,}333;\,0{,}600;\,1{,}154;\,2{,}294;\,2{,}780$, que coincide exactamente con $3(1+\omega^2)/(9+\omega^2)$ evaluada en esos mismos puntos.) (En (c), verificado con el proceso $X(t)=\cos(\Omega t+\Theta)$ del Ejercicio 10: derivando la fórmula cerrada de $R_{xx}(\tau)$ numéricamente (diferencias finitas) se obtiene, en $\tau=0{,}3$ y $\tau=1$, $-0{,}6038$ y $-0{,}3525$, contra $-0{,}6039$ y $-0{,}3521$ estimados por Monte Carlo de $E[X'(t{+}\tau)X(t)]$ con $3\cdot10^6$ muestras — coinciden.)*

> [!warning] Ojo
> En (b) el punto no es "cualquier $|H|^2\geq0$ sirve": tiene que además corresponder a un filtro **estable** (polos en el semiplano izquierdo). Acá funcionó porque el factor con el cero en $s=-1$ y el polo en $s=-3$ quedó del lado correcto; si el enunciado hubiera pedido, por ejemplo, subir la potencia total sin límite (un $|H|^2$ que creciera sin cota), no habría filtro propio que lo realizara.

---

## Ejercicio 17 — Producto de una rama filtrada por una rama retardada, con entrada blanca

> [!quote] Enunciado
> 17. Para el sistema de la figura, $x(t)$ es WSS con PSD $S_{xx}(j\omega)=N_0$. Determine el valor esperado de $r(t)$, $E\{r(t)\}$, en términos de $N_0$, $t_0$ y $h(t)$.
>
> ![[ej-p10-17.png]]

###### **Idea**
La figura muestra dos ramas desde la misma entrada $x(t)$: una pasa por el filtro $h(\cdot)$ y da $g_1(t)$; la otra se retarda $t_0$ y da $g_2(t)=x(t-t_0)$. La salida es el **producto** $r(t)=g_1(t)g_2(t)$, no una suma — así que $E[r(t)]$ es una correlación cruzada entre $g_1$ y $g_2$, no una suma de PSDs. Con $S_{xx}$ constante ($N_0$), $R_{xx}(\tau)$ es un impulso, y eso colapsa la integral de convolución a una sola evaluación de $h$.

###### **Resolución**
$$g_1(t)=\int_{-\infty}^{\infty}h(\alpha)\,x(t-\alpha)\ d\alpha,\qquad g_2(t)=x(t-t_0)$$
$$E\{r(t)\}=E[g_1(t)g_2(t)]=E\Big[\int h(\alpha)\,x(t-\alpha)\ d\alpha\cdot x(t-t_0)\Big]=\int h(\alpha)\,E[x(t-\alpha)x(t-t_0)]\ d\alpha$$
Como $x$ es WSS, $E[x(t-\alpha)x(t-t_0)]=R_{xx}(t_0-\alpha)$ (la autocorrelación evaluada en la diferencia de los dos instantes, $(t-\alpha)-(t-t_0)=t_0-\alpha$):
$$E\{r(t)\}=\int_{-\infty}^{\infty}h(\alpha)\,R_{xx}(t_0-\alpha)\ d\alpha$$
Como $S_{xx}(j\omega)=N_0$ para todo $\omega$ (espectro plano — el blanco idealizado de tiempo continuo del complemento de Cap. 11), su autocorrelación es
$$R_{xx}(\tau)=\mathcal F^{-1}\{N_0\}=N_0\,\delta(\tau)$$
Sustituyendo y usando la propiedad de "peine" (*sifting*) del impulso:
$$E\{r(t)\}=\int_{-\infty}^{\infty}h(\alpha)\,N_0\,\delta(t_0-\alpha)\ d\alpha=N_0\,h(t_0)$$
$$\boxed{\ E\{r(t)\}=N_0\,h(t_0)\ }$$

###### **Verificación**
El resultado no depende de $t$ — tiene sentido, porque tanto $g_1$ como $g_2$ son (filtrados/retardos de) un proceso WSS, así que $E[g_1(t)g_2(t)]$ solo puede depender de la diferencia de retardos entre las dos ramas, que es fija. *(Verificado simbólicamente con sympy: integrando $h(\alpha)\,N_0\,\delta(t_0-\alpha)$ en $\alpha\in(-\infty,\infty)$ con `DiracDelta`, sympy devuelve exactamente `N0*h(t0)`.)*

> [!warning] Ojo
> No hay que confundir esto con $E[g_1(t)]\cdot E[g_2(t)]$: como $g_1(t)$ y $g_2(t)$ son ambas funciones de la **misma** realización de $x$, están correlacionadas, y $E[g_1g_2]\neq E[g_1]E[g_2]$ en general (acá encima $E[x(t)]$ ni siquiera está definido en el sentido usual porque $x$ es blanco idealizado). Hay que ir directo a $E[g_1(t)g_2(t)]$ como una correlación cruzada, tal como se hizo arriba.

---

## Ejercicio 18 — Autocorrelación de entrada y salida iguales: ¿implica retardo puro?

> [!quote] Enunciado
> 18. Considere un sistema LTI estable con respuesta al impulso $h(t)$, tal que si se aplica a su entrada una señal WSS $x(t)$ con autocorrelación $R_{xx}(\tau)=e^{-|\tau|}$, la salida resultante $y(t)$ tiene autocorrelación $R_{yy}(\tau)=e^{-|\tau|}$. ¿Puede escribirse siempre $y(t)$ en la forma $y(t)=\alpha\ x(t-t_0)$ para ciertas constantes $\alpha$, $t_0$? Explique.

###### **Idea**
$R_{yy}=R_{xx}$ es una condición sobre el **módulo** de $H(j\omega)$ únicamente ($|H(j\omega)|=1$ para todo $\omega$): la autocorrelación no ve la fase de $H$. Un retardo puro ($h(t)=\alpha\delta(t-t_0)$) es *un* sistema con esa propiedad, pero no es el único: cualquier filtro **pasa-todo** (*all-pass*) estable, con fase no lineal, también cumple $|H(j\omega)|=1$ sin ser un simple retardo.

###### **Resolución**
La condición $R_{yy}(\tau)=R_{xx}(\tau)$ para todo $\tau$ equivale, en frecuencia, a
$$S_{yy}(j\omega)=|H(j\omega)|^2\,S_{xx}(j\omega)=S_{xx}(j\omega)\quad\text{para todo }\omega$$
Como $S_{xx}(j\omega)=\mathcal F\{e^{-|\tau|}\}=\dfrac{2}{1+\omega^2}>0$ para todo $\omega$ (nunca se anula), se puede dividir y queda
$$|H(j\omega)|^2=1\ \ \Longleftrightarrow\ \ |H(j\omega)|=1\quad\text{para todo }\omega$$
Esto dice que $H$ es un sistema **pasa-todo**: no altera la potencia en ninguna frecuencia. Pero $|H(j\omega)|=1$ **no fija la fase** de $H(j\omega)$, y $y(t)=\alpha x(t-t_0)$ corresponde a **una elección particular** de fase (la lineal): $H(j\omega)=\alpha e^{-j\omega t_0}$.

Hay sistemas estables con $|H(j\omega)|=1$ para todo $\omega$ y fase **no lineal**. El ejemplo canónico es el pasa-todo de primer orden
$$H(s)=\frac{s-a}{s+a},\qquad a>0$$
que tiene polo en $s=-a$ (semiplano izquierdo, estable y causal) y cero en $s=+a$ (reflejado respecto del eje imaginario). Para este $H$:
$$|H(j\omega)|^2=\frac{(j\omega-a)(-j\omega-a)}{(j\omega+a)(-j\omega+a)}=\frac{\omega^2+a^2}{\omega^2+a^2}=1\quad\text{para todo }\omega$$
pero su fase $\angle H(j\omega)=\pi-2\arctan(\omega/a)$ **no** es lineal en $\omega$ (no es de la forma $-\omega t_0$), así que la salida $y(t)$ correspondiente **no** puede escribirse como $\alpha x(t-t_0)$: es una versión de $x$ con cada componente de frecuencia desfasada de manera distinta, no simplemente corrida en el tiempo.
$$\boxed{\ \text{No: }R_{yy}=R_{xx}\text{ solo garantiza }|H(j\omega)|=1\text{ (pasa-todo), no que }H\text{ sea un retardo puro}\ }$$
$$\boxed{\ \text{Contraejemplo: }H(s)=\dfrac{s-a}{s+a}\ (a>0),\ \text{estable, }|H(j\omega)|\equiv1,\ \text{fase no lineal}\ }$$

###### **Verificación**
$|H(j\omega)|=1$ para todo $\omega$ (no solo aproximadamente) ✓, condición necesaria para que valga $R_{yy}=R_{xx}$; y la fase no es proporcional a $\omega$, así que no es un retardo. *(Verificado numéricamente: con $a=2$ y $\omega\in[-20,20]$, $\max_\omega\big||H(j\omega)|-1\big|\approx4\times10^{-16}$ (cero salvo error de redondeo) — pasa-todo confirmado. La fase evaluada en $\omega=1,2,5$ da $2{,}206;\,1{,}565;\,0{,}759$ rad, que **no** es proporcional a $\omega$ (si lo fuera, la razón fase/$\omega$ sería constante; acá da $2{,}206,\ 0{,}783,\ 0{,}152$ — nada constante), confirmando que no es un retardo lineal.)*

> [!info] Conexión
> Es la misma ambigüedad del "factor espectral no único" que menciona el apunte principal en la sección de filtros blanqueadores/modeladores: multiplicar cualquier $H(z)$ (o $H(s)$) por un pasa-todo $A$ (con $|A|=1$ en toda frecuencia) da otro filtro con el mismo $|H|^2$ y por lo tanto la misma autocorrelación de salida, pero una respuesta al impulso distinta. Acá es exactamente ese fenómeno, llevado al extremo: la única información que $R_{xx}$ vs. $R_{yy}$ le da sobre $H$ es su módulo, nunca su fase.

---
