Solucionario de los Ejercicios Propuestos del capítulo 8 de [[PROCESAMIENTO DE SEÑALES]]. La teoría con demostraciones está en [[PROCESAMIENTO DE SEÑALES - Cap 8 en profundidad]].

# Estimación — Solucionario

Todo sale de tres herramientas: el MMSE sin datos ($\hat y=E[Y]$), el MMSE condicional ($\hat y(x)=E[Y\mid X=x]$, óptimo sin restricciones) y el LMMSE ($\hat Y_\ell=\mu_Y+\rho\frac{\sigma_Y}{\sigma_X}(X-\mu_X)$, óptimo entre los estimadores afines). Cuando el enunciado da una densidad conjunta uniforme sobre una región, casi siempre conviene arrancar por los momentos ($\mu_X,\mu_Y,\sigma_X^2,\sigma_Y^2,\sigma_{XY}$) antes de meterse con la condicional completa.

###### **Índice**
| Ej. | Qué se practica | Problema del libro |
|---|---|---|
| 1 | V/F: MSE del LMMSE y correlación desde una pendiente condicional | P8.9 |
| 2 | V/F: LMMSE constante, $Y=X^2$, aditividad con mediciones no correlacionadas | P8.10 |
| 3 | Independencia a partir de un MMSE constante | P8.12 |
| 4 | Gaussiana bivariada: MMSE lineal en ambas direcciones | P8.1 |
| 5 | LMMSE con variables estandarizadas y transformaciones afines | P8.3 |
| 6 | MMSE sobre una franja diagonal (densidad uniforme) | P8.11 |
| 7 | MMSE, sesgo y LMMSE sobre un triángulo | P8.4 |
| 8 | MMSE y LMMSE sobre una región en dos cuadrados | P8.6 |
| 9 | LMMSE vs. MMSE sobre una región con agujero y muesca | P8.5 |
| 10 | LMMSE con dos mediciones de una sinusoide aleatoria | P8.8 |
| 11 | MMSE en un canal binario sin memoria | P8.2 |
| 12 | Canal con ganancia aleatoria multiplicativa | P8.7 |

---

## Ejercicio 1 — Verdadero o falso: MSE del LMMSE y correlación desde una pendiente condicional

> [!quote] Enunciado
> 1. Para cada uno de los siguientes puntos, indique si la afirmación dada es verdadera o falsa. Para una afirmación verdadera, dé una explicación breve pero convincente; para una falsa, dé un contraejemplo o una explicación convincente.
>
> a) Si $\hat Y$ es el estimador LMMSE de $Y$ en términos de otra variable aleatoria $X$, entonces el MMSE correspondiente $E[(Y-\hat Y)^2]$ puede expresarse como
> $$E[(Y-\hat Y)^2] = E[Y^2] - E[Y\hat Y].$$
> b) Supongamos que $X$ e $Y$ son variables aleatorias con media $0$ y la misma varianza $\sigma^2$, y supongamos que se sabe que $E[Y|X=x] = \frac{1}{3}x$ para todos los valores $x$ que puede tomar la variable aleatoria $X$. El coeficiente de correlación entre $X$ e $Y$ debe ser entonces $\frac13$.

###### **Idea**
Las dos partes salen de la regla de ortogonalidad ([[PROCESAMIENTO DE SEÑALES - Cap 8 en profundidad]], Parte 1.3): el error del LMMSE es ortogonal a $1$ y a $X$, y por lo tanto a cualquier combinación afín de ellos (en particular, a $\hat Y$ mismo).

###### **Resolución**
**a) Verdadero.** Sea $e=Y-\hat Y$. Como $\hat Y=aX+b$ es una función afín de $X$, y $e$ es ortogonal tanto a $1$ como a $X$ (regla de ortogonalidad del LMMSE), también es ortogonal a cualquier combinación afín de ambos:
$$E[e\,\hat Y] = E[e\,(aX+b)] = a\,\underbrace{E[eX]}_{0} + b\,\underbrace{E[e]}_{0} = 0 \ \implies\ E[Y\hat Y]=E[\hat Y^2]$$
Entonces
$$E[e^2]=E[e\,(Y-\hat Y)]=E[eY]-\underbrace{E[e\hat Y]}_{0}=E[eY]=E[(Y-\hat Y)Y]=E[Y^2]-E[Y\hat Y]$$
$$\boxed{\ E[(Y-\hat Y)^2] = E[Y^2] - E[Y\hat Y]\ \text{(verdadero, para todo par }X,Y\text{)}\ }$$

**b) Verdadero** (y no es obvio a primera vista). La clave es que $E[Y\mid X=x]=\tfrac13 x$ ya es **lineal** en $x$. El estimador MMSE sin restricciones, $E[Y\mid X]$, satisface la regla de ortogonalidad *completa* (ortogonal a *cualquier* función de $X$, no solo a las afines); en particular es ortogonal a $1$ y a $X$. Pero esas son exactamente las dos ecuaciones que caracterizan —de forma única— al LMMSE. Como $E[Y\mid X]=\tfrac13X$ ya es afín y cumple esas ecuaciones, **tiene que ser** el LMMSE mismo:
$$\hat Y_\ell(X) = \frac13 X = \mu_Y + \rho\frac{\sigma_Y}{\sigma_X}(X-\mu_X) = \rho\,X \quad(\text{con }\mu_X=\mu_Y=0,\ \sigma_X=\sigma_Y=\sigma)$$
Igualando pendientes, $\rho = \dfrac13$.
$$\boxed{\ \rho_{XY}=\tfrac13\ \text{(verdadero, es consecuencia forzosa de que la condicional ya sea lineal)}\ }$$

###### **Verificación**
En (a), la identidad vale para *cualquier* $X,Y$ con varianza finita, no hace falta gaussianidad. En (b), $|\rho|=1/3<1$ ✓. *(verificado numéricamente: con $X\sim\mathcal N(0,1)$ y $Y=\tfrac13X+N$, $N\perp X$ con $\mathrm{Var}(N)=8/9$ (para que $\sigma_Y^2=\sigma_X^2=1$), Monte Carlo con $4\cdot10^6$ muestras da $\hat\rho_{XY}\approx0{,}334$ y, promediando $Y$ por bines de $X$, $E[Y\mid X=x]\approx x/3$.)*

> [!warning] Ojo
> El resultado de (b) es una implicación en un solo sentido: que $E[Y\mid X]$ sea lineal fuerza a que coincida con el LMMSE. Si la condicional **no** fuera lineal, no habría manera de deducir $\rho$ sin más información —el LMMSE seguiría existiendo, pero ya no coincidiría con $E[Y\mid X]$.

---

## Ejercicio 2 — Verdadero o falso: LMMSE constante, $Y=X^2$ y aditividad con mediciones no correlacionadas

> [!quote] Enunciado
> 2. Para cada uno de los siguientes puntos, indique si la afirmación dada es verdadera o falsa. Para una afirmación verdadera, dé una explicación breve pero convincente; para una falsa, dé un contraejemplo o una explicación convincente.
>
> a) Supongamos que el estimador LMMSE $\hat Y$ de la variable aleatoria $Y$ en términos de $X$ es simplemente la media de $Y$, es decir, $\hat Y = \mu_Y$. Entonces $X$ e $Y$ deben ser independientes.
> b) Supongamos que la variable aleatoria $X$ está distribuida de manera uniforme en el intervalo $[-1,1]$, y sea $Y=X^2$ (de modo que $Y$ queda completamente determinada por $X$). El estimador LMMSE $\hat Y$ de $Y$ en términos de $X$ es $0$.
> c) Supongamos que $X_1$ y $X_2$ son variables aleatorias no correlacionadas. Entonces el estimador LMMSE de $Y$ en términos de $X_1$ y $X_2$ está dado por $\hat Y = \hat Y_1 + \hat Y_2$, donde $\hat Y_1$ es el estimador LMMSE de $Y$ en términos de solo $X_1$, y de manera similar $\hat Y_2$ es el estimador LMMSE de $Y$ en términos de solo $X_2$.

###### **Idea**
(a) y (b) son la misma trampa clásica: $\hat Y_\ell=\mu_Y$ solo dice $\rho_{XY}=0$ (no correlación), y no correlación no implica independencia. (c) es la trampa de las ecuaciones normales de la Parte 1.6 del complemento: los **pesos** se desacoplan cuando $\rho_{12}=0$, pero el término independiente $a_0=\mu_Y-\sum_j a_j\mu_{X_j}$ no se puede simplemente duplicar.

###### **Resolución**
**a) Falso.** $\hat Y_\ell=\mu_Y$ equivale a pendiente $a=\rho\,\sigma_Y/\sigma_X=0$, es decir $\rho_{XY}=0$: $X$ e $Y$ **no están correlacionadas**, pero no correlación no implica independencia. El contraejemplo de (b) sirve acá también: con $X\sim U[-1,1]$ y $Y=X^2$, $Y$ queda *completamente determinada* por $X$ (dependencia total) y sin embargo $\sigma_{XY}=0$ por simetría, así que $\hat Y_\ell=\mu_Y$.

**b) Falso.** Con $f_X(x)=\tfrac12$ en $[-1,1]$: $\mu_X=0$, $\mu_Y=E[X^2]=\sigma_X^2=\tfrac13$ (varianza de una uniforme en $[-1,1]$), y
$$\sigma_{XY}=E[XY]-\mu_X\mu_Y=E[X^3]-0=\int_{-1}^1 x^3\cdot\tfrac12\,dx=0$$
($x^3$ es impar). Entonces $a=\sigma_{XY}/\sigma_X^2=0$ y $b=\mu_Y-a\mu_X=\mu_Y=\tfrac13$:
$$\boxed{\ \hat Y_\ell = \frac13 \ \ (\text{no } 0)\ }$$
El estimador es constante, sí, pero esa constante es $\mu_Y=1/3$, no $0$. Que la guía proponga $0$ es simplemente falso.

**c) Falso en general.** Por la Parte 1.6 del complemento, con $\rho_{12}=0$ los pesos se calculan por separado: $a_i=\sigma_{YX_i}/\sigma_{X_i}^2$, el mismo valor que si $Y$ se estimara solo con $X_i$. Pero el término constante del estimador conjunto es
$$a_0=\mu_Y-a_1\mu_{X_1}-a_2\mu_{X_2} \implies \hat Y_\ell=\mu_Y+a_1(X_1-\mu_{X_1})+a_2(X_2-\mu_{X_2})$$
mientras que sumar los dos estimadores individuales,
$$\hat Y_1+\hat Y_2=\big[\mu_Y+a_1(X_1-\mu_{X_1})\big]+\big[\mu_Y+a_2(X_2-\mu_{X_2})\big]=2\mu_Y+a_1(X_1-\mu_{X_1})+a_2(X_2-\mu_{X_2})$$
duplica la media: $\hat Y_1+\hat Y_2=\hat Y_\ell+\mu_Y$. La relación correcta es
$$\boxed{\ \hat Y_\ell=\hat Y_1+\hat Y_2-\mu_Y\ }$$
que coincide con $\hat Y_1+\hat Y_2$ solo en el caso particular $\mu_Y=0$.

###### **Verificación**
*(verificado numéricamente: en (b), con $10^6$ puntos de $X\sim U[-1,1]$, $Y=X^2$, la regresión lineal da pendiente $\approx 0$ y ordenada $\approx0{,}333$. En (c), con $X_1\sim\mathcal N(2,1)$, $X_2\sim\mathcal N(-1,1{,}5^2)$ independientes y $Y=5+0{,}7X_1-0{,}3X_2+\text{ruido}$ ($\mu_Y\approx6{,}70$), Monte Carlo con $3\cdot10^6$ muestras da pendientes conjuntas $(0{,}7003,-0{,}3003)$ casi idénticas a las individuales $(0{,}7005,-0{,}3005)$, pero $\hat Y_1+\hat Y_2\approx13{,}40=\hat Y_\ell+\mu_Y$, no $\hat Y_\ell\approx6{,}70$.)*

> [!warning] Ojo
> (a)-(b) son el mismo error conceptual que "no correlación $\Rightarrow$ independencia", uno de los tropiezos más comunes del capítulo 7. (c) es más sutil: la propiedad que sí es cierta con $\rho_{12}=0$ es que los **pesos** de cada medición no compiten entre sí (ver Cap 8 en profundidad, Ejercicio 4); pero eso no alcanza para que los estimadores completos (con su ordenada al origen) se sumen sin corregir.

---

## Ejercicio 3 — Independencia a partir de un MMSE constante

> [!quote] Enunciado
> 3. $X$ e $Y$ son dos variables aleatorias con PDFs desconocidas. $X$ tiene media nula. El estimador MMSE $\hat Y$ de $Y$ dado $X$ es $\hat Y = 5$. A partir de la información dada, especifique si $X$ e $Y$ son definitivamente estadísticamente independientes, definitivamente no independientes, o si no puede determinarse con la información dada. Explique.

###### **Idea**
$\hat Y_{\text{MMSE}}(X)=E[Y\mid X=x]=5$ para todo $x$ es una afirmación sobre la **media condicional** únicamente. Independencia es una afirmación mucho más fuerte: exige que **toda** la distribución condicional $f_{Y\mid X}(y\mid x)$ sea igual a $f_Y(y)$, no solo su media.

###### **Resolución**
**No puede determinarse.**

Que $E[Y\mid X=x]=5$ para todo $x$ sí implica $\mu_Y=E_X[E[Y\mid X]]=5$ (por la ley de la esperanza iterada), pero no dice nada de cómo cambian con $x$ los momentos de orden superior de $Y\mid X=x$ (varianza, asimetría, etc.). Es perfectamente posible construir un par dependiente con esta propiedad: sean $X$ y $Z$ independientes, ambas de media $0$, y definamos
$$Y = 5 + XZ$$
Entonces $E[Y\mid X=x] = 5 + x\,E[Z] = 5$ para todo $x$ (cumple el dato), pero
$$\operatorname{Var}(Y\mid X=x) = x^2\operatorname{Var}(Z)$$
depende de $x$: la dispersión de $Y$ cambia según el valor de $X$, así que $X$ e $Y$ **no son independientes** en este ejemplo. Por otro lado, también es consistente con el dato que $Y=5+N$ con $N\perp X$ de media $0$: ahí sí serían independientes. Como ambos casos (dependiente y independiente) son compatibles con "$\hat Y_{\text{MMSE}}=5$", la información dada no alcanza para decidir.
$$\boxed{\ \text{No se puede determinar}\ }$$

###### **Verificación**
*(verificado numéricamente: con $X\sim\mathcal N(0,1)$, $Z\sim\mathcal N(0,1)$ independientes y $Y=5+XZ$, Monte Carlo con $3\cdot10^6$ muestras da $E[Y\mid X=x]\approx5$ para todo bin de $x$ (desvíos $<0{,}03$), mientras que $\operatorname{Var}(Y\mid X=x)$ crece de $\approx0{,}08$ en $x\approx0$ a $\approx7{,}2$ en $x\approx\pm3$, y $\operatorname{corr}(X^2,(Y-5)^2)\approx0{,}50$: clara dependencia pese al MMSE constante.)*

> [!warning] Ojo
> No confundir "$E[Y\mid X]$ es constante" con "$Y\perp X$". La independencia completa sí implica MMSE constante (porque $f_{Y\mid X}=f_Y$), pero la recíproca es falsa: MMSE constante solo dice que la dependencia, si existe, es "invisible" para la media condicional (por ejemplo, vive en la varianza, como en el ejemplo de arriba).

---

## Ejercicio 4 — Gaussiana bivariada: qué fuerza un MMSE constante

> [!quote] Enunciado
> 4. Considere el par de variables aleatorias Gaussianas bivariadas $X$ e $Y$, donde $\mu_X=0$. El estimador MMSE para $Y$ en términos de $X$ es $\hat Y_{MMSE}(X)=2$.
>
> a) ¿Cuál es $E[Y]$?
> b) Especifique si $X$ e $Y$ están correlacionadas, no correlacionadas, o si no hay información suficiente para determinarlo. Explique.
> c) Especifique si $X$ e $Y$ son independientes, dependientes, o si no hay información suficiente para determinarlo. Explique.
> d) ¿Cuál es el estimador MMSE de $X$ en términos de $Y$, $\hat X_{MMSE}(Y)$?

###### **Idea**
Para gaussianas bivariadas el MMSE **es** lineal: $E[Y\mid X=x]=\mu_Y+\rho\frac{\sigma_Y}{\sigma_X}(x-\mu_X)$ (Cap 8 en profundidad, Parte 4 conecta esto con el capítulo 7). Que el enunciado diga que ese estimador es la constante $2$ para *todo* $x$ obliga a que el coeficiente de $x$ sea cero.

###### **Resolución**
Con $\mu_X=0$: $E[Y\mid X=x]=\mu_Y+\rho\dfrac{\sigma_Y}{\sigma_X}\,x$. Que esto sea $\equiv 2$ para todo $x$ (una recta constante) fuerza, comparando coeficientes:
$$\rho\,\frac{\sigma_Y}{\sigma_X}=0 \qquad\text{y}\qquad \mu_Y=2$$

**a)** Del término independiente:
$$\boxed{\ E[Y]=2\ }$$

**b)** Como $\sigma_X\neq0$ (si no, $X$ no sería una variable aleatoria propiamente dicha) y $\sigma_Y$ es finita, la única forma de que $\rho\,\sigma_Y/\sigma_X=0$ es $\rho=0$:
$$\boxed{\ X\text{ e }Y\text{ están \textbf{no correlacionadas}}\ }$$
(no es "no se puede determinar": el dato lo fuerza).

**c)** Acá es donde la gaussianidad hace la diferencia con el Ejercicio 3: para variables **conjuntamente gaussianas**, no correlación **sí** implica independencia (es la única familia donde vale la recíproca de "independencia $\Rightarrow$ no correlación"). Como $(X,Y)$ es gaussiana bivariada y $\rho=0$:
$$\boxed{\ X\text{ e }Y\text{ son \textbf{independientes}}\ }$$

**d)** Si $X$ e $Y$ son independientes, la condicional de $X$ dado $Y=y$ es la marginal de $X$: $f_{X\mid Y}(x\mid y)=f_X(x)$ para todo $y$. Entonces
$$\boxed{\ \hat X_{\text{MMSE}}(Y) = E[X\mid Y=y] = E[X] = \mu_X = 0\ }$$

###### **Verificación**
Sanity check de (b): $|\rho|=0\le1$ ✓. *(verificado numéricamente: generando $X\sim\mathcal N(0,2)$ e $Y\sim\mathcal N(2,1{,}7^2)$ independientes, Monte Carlo con $2\cdot10^6$ muestras da $\operatorname{corr}(X,Y)\approx-0{,}0005\approx0$ y $E[Y\mid X=x]\approx2{,}00$ en todos los bines de $x$ probados, consistente con la recta constante que pide el enunciado.)*

> [!info] Conexión
> Contrastar con el Ejercicio 3: ahí "$\hat Y_{\text{MMSE}}=5$ constante" **no** alcanzaba para concluir independencia, porque no se sabía nada de la forma de las distribuciones. Acá sí alcanza, exclusivamente porque el enunciado impone gaussianidad conjunta desde el arranque: ahí no correlación e independencia son la misma cosa.

---

## Ejercicio 5 — LMMSE con variables estandarizadas y transformaciones afines

> [!quote] Enunciado
> 5. Supongamos que $X$ e $Y$ son variables aleatorias de media nula y varianza unitaria. Si el estimador LMMSE $\hat y(X)$ de $Y$ en términos de $X$ está dado por
> $$\hat y(X) = \frac34 X,$$
> ¿cuál es su error cuadrático medio? Además, supongamos que la variable aleatoria $Q$ se define como $Q=Y+3$; ¿cuál es el estimador LMMSE $\hat q(X)$ de $Q$ en términos de $X$, y cuál es su error cuadrático medio? Finalmente, ¿cuál es el estimador LMMSE $\hat x(Y)$ de $X$ en términos de $Y$, y cuál es su error cuadrático medio?

###### **Idea**
Con $\mu_X=\mu_Y=0$ y $\sigma_X=\sigma_Y=1$, la pendiente del LMMSE **es directamente** $\rho_{XY}$ (Cap 8 en profundidad, Parte 1.4: $a=\rho\,\sigma_Y/\sigma_X$). Para $Q=Y+3$, el LMMSE de una suma con una constante es la suma del LMMSE más esa constante (linealidad de la proyección). Para $\hat x(Y)$, la simetría $\sigma_X=\sigma_Y$ hace que la pendiente "de vuelta" sea la misma $\rho$.

###### **Resolución**
**Extraer $\rho$.** Comparando $\hat y(X)=\tfrac34X$ con $\hat Y_\ell=\rho\dfrac{\sigma_Y}{\sigma_X}X=\rho X$ (ya que $\sigma_X=\sigma_Y=1$):
$$\rho_{XY}=\frac34$$

**MSE de $\hat y(X)$.** Por la fórmula general $\sigma_Y^2(1-\rho^2)$ (Parte 1.4/1.5 del complemento):
$$\boxed{\ \text{MMSE}_{\hat y}=1\cdot\left(1-\frac{9}{16}\right)=\frac{7}{16}=0{,}4375\ }$$

**LMMSE de $Q=Y+3$.** El error a minimizar es $E[(Q-aX-b)^2]=E[((Y+3)-aX-b)^2]=E[(Y-aX-(b-3))^2]$: es el mismo problema que estimar $Y$, con la ordenada corrida en $3$. La pendiente óptima no cambia ($a=3/4$), y la nueva ordenada es $b=3$ (la vieja ordenada de $\hat y$, que era $0$, más el corrimiento):
$$\boxed{\ \hat q(X) = \frac34 X + 3\ }$$
El error es el mismo que antes, porque restar una constante conocida ($3$) no afecta la dispersión del error:
$$\boxed{\ \text{MMSE}_{\hat q}=\frac{7}{16}=0{,}4375\ }$$

**LMMSE de $X$ en términos de $Y$.** Por simetría de la fórmula ($a'=\rho\,\sigma_X/\sigma_Y$) y $\sigma_X=\sigma_Y=1$:
$$\boxed{\ \hat x(Y) = \frac34 Y\ },\qquad \boxed{\ \text{MMSE}_{\hat x}=\sigma_X^2(1-\rho^2)=\frac{7}{16}=0{,}4375\ }$$

###### **Verificación**
$|\rho|=3/4<1$ ✓, y los tres MMSE son iguales entre sí y menores que la varianza total ($7/16<1$) ✓ — tiene sentido, ya que estimar $X$ desde $Y$ o $Y$ desde $X$ con variables estandarizadas es geométricamente simétrico (mismo ángulo $\theta=\arccos(3/4)$ entre los vectores centrados). *(verificado numéricamente: con $(X,Y)$ gaussiana bivariada, media $0$, varianza $1$, $\rho=0{,}75$, Monte Carlo con $3\cdot10^6$ muestras y regresión lineal da $\hat y(X)$: pendiente $0{,}7500$, MSE $0{,}4377$; $\hat q(X)$: pendiente $0{,}7500$, ordenada $3{,}0004$, MSE $0{,}4377$; $\hat x(Y)$: pendiente $0{,}7491$, MSE $0{,}4371$ — los tres coinciden con $7/16=0{,}4375$ dentro del error de muestreo.)*

---

## Ejercicio 6 — MMSE sobre una franja diagonal (densidad uniforme)

> [!quote] Enunciado
> 6. Las variables aleatorias $X$ e $Y$ están distribuidas de manera uniforme en la región sombreada mostrada en la figura.
>
> ![[Pasted image 20260814133929.png|311]]
>
> a) Determine y grafique el estimador MMSE $\hat Y_{MMSE}(X)$ de $Y$ dado $X$.
> b) Determine y grafique el estimador MMSE $\hat X_{MMSE}(Y)$ de $X$ dado $Y$.

> [!warning] Nota sobre el enunciado
> La figura de la guía es una versión escaneada de la Figura P8.11 del libro; para no perder precisión se midieron las coordenadas exactas sobre la figura original del libro. La región es la franja diagonal
> $$R=\{(x,y): 0\le x\le1,\ \ 0{,}75x\le y\le 0{,}75x+0{,}25\}$$
> con densidad constante $f_{X,Y}(x,y)=4$ adentro (el "Height $=4$" de la figura es justamente ese valor: el área de la franja es $0{,}25$, y $4\times0{,}25=1$).

###### **Idea**
Para cada $x$ fijo, $Y\mid X=x$ es uniforme en un intervalo de ancho constante $0{,}25$ (la franja tiene ancho perpendicular constante), así que su media condicional es simplemente el punto medio: **lineal en $x$**. Para $Y$ fijo, en cambio, el intervalo de $X$ compatible cambia de ancho según $y$ (angosto cerca de los bordes $y=0$ e $y=1$, constante en el medio): la condicional de $X$ dado $Y=y$ ya no da una recta.

###### **Resolución**
**a) $\hat Y_{MMSE}(X)$.** Para $x\in[0,1]$, $Y\mid X=x\sim U[0{,}75x,\ 0{,}75x+0{,}25]$, así que su media es el punto medio del intervalo:
$$\boxed{\ \hat y_{MMSE}(x) = 0{,}75x + 0{,}125\ ,\qquad 0\le x\le1\ }$$
Es lineal en todo el dominio — de hecho coincide con el LMMSE, porque la franja es simplemente $Y=0{,}75X+U$ con $U\sim U[0,0{,}25]$ independiente de $X\sim U[0,1]$.

![[sol08-ej06-mmse-y-dado-x.svg]]
*(la franja gris es la región donde $f_{X,Y}=4$; la recta azul es $\hat y_{MMSE}(x)$, pasando siempre por el medio del ancho vertical.)*

**b) $\hat X_{MMSE}(Y)$.** Hay que integrar primero la marginal $f_Y(y)$, que resulta trapezoidal (para $y$ fijo, el segmento de $x$ compatible es $\left[\max\!\big(0,\tfrac{4y-1}{3}\big),\ \min\!\big(1,\tfrac{4y}{3}\big)\right]$), y dentro de él $X\mid Y=y$ es uniforme, así que su media es el punto medio de ese intervalo. Quedan tres tramos:
$$
\hat x_{MMSE}(y)=
\begin{cases}
\dfrac{2}{3}\,y, & 0\le y< \tfrac14 \quad\text{(borde inferior: el segmento arranca en }x=0\text{)}\\[4pt]
\dfrac{4}{3}\,y-\dfrac16, & \tfrac14\le y\le\tfrac34 \quad\text{(tramo central: segmento de ancho }\tfrac13\text{)}\\[4pt]
\dfrac{2}{3}\,y+\dfrac13, & \tfrac34< y\le1 \quad\text{(borde superior: el segmento termina en }x=1\text{)}
\end{cases}
$$
$$\boxed{\ \hat x_{MMSE}(y)\ \text{es lineal a trozos, con pendiente } \tfrac23 \text{ en los bordes y } \tfrac43\text{ en el medio}\ }$$
Se verifica que las tres piezas empalman sin saltos: en $y=\tfrac14$ dan $\tfrac16$ las dos fórmulas vecinas, y en $y=\tfrac34$ dan $\tfrac56$ ambas.

![[sol08-ej06-mmse-x-dado-y.svg]]
*(la curva no es una sola recta: cerca de $y=0$ e $y=1$ el segmento de $x$ disponible es angosto y asimétrico — el promedio se "pega" más al extremo cercano — mientras que en el tramo central, donde el ancho de $x$ es constante, la pendiente es mayor.)*

###### **Verificación**
$fX(x)$ integra a $1$ en $[0,1]$ (verificado con sympy: `integrate(4,(y,0.75x,0.75x+0.25))=1`). $f_Y(y)$ (trapezoidal, con tramos $\tfrac{16}{3}y$, $\tfrac43$, $\tfrac{16}{3}(1-y)$) integra a $1/6+2/3+1/6=1$ ✓. *(verificado numéricamente con sympy: para cada uno de los tres tramos de $y$, `integrate(4,(x,x_lo,x_hi))` y `integrate(4x,(x,x_lo,x_hi))/fY` reproducen exactamente las fórmulas de arriba —incluida la pendiente $4/3$ del tramo central y $2/3$ en los bordes.)*

> [!info] Conexión
> El contraste entre (a) —lineal, porque el ancho condicional de $Y$ es constante— y (b) —lineal a trozos, porque el ancho condicional de $X$ no lo es— es el mismo fenómeno que en el Ejercicio 2 del complemento (densidad triangular): ahí la condicional también salía lineal porque el soporte crecía linealmente con $x$. Acá el soporte de $X\mid Y$ crece, se estabiliza y decrece, y esa forma trapezoidal es la que rompe la linealidad.

---

## Ejercicio 7 — MMSE, sesgo y LMMSE sobre un triángulo

> [!quote] Enunciado
> 7. Supongamos que dos variables aleatorias $X$ e $Y$ tienen una PDF conjunta $f_{X,Y}(x,y)$ que es constante en la región sombreada mostrada en la figura, y nula en el resto:
>
> ![[Pasted image 20260814133944.png|211]]
>
> a) Realice gráficos completamente etiquetados de las densidades $f_X(x)$ y $f_{Y|X}(y|\tfrac13)$.
> b) ¿Son $X$ e $Y$ estadísticamente independientes? Explique.
> c) Determine y realice un gráfico completamente etiquetado (en función de $x$) de $\hat y_{MMSE}(X)$, el estimador MMSE de $Y$ basado en observar $X$.
> d) Para evaluar qué tan bien se desempeñará en promedio el estimador del punto c), determine el error cuadrático medio $e^2$ y el sesgo $b$ asociados al estimador:
> $$e^2 = E\left[\left(\hat y_{MMSE}(X)-Y\right)^2\right], \quad \text{y} \quad b = E[\hat y_{MMSE}(X)-Y],$$
> donde la esperanza se toma sobre $X$ e $Y$ conjuntamente.
> e) Determine $\hat y_{LMMSE}(X)$, el estimador MMSE lineal de $Y$, y su MMSE asociado.

###### **Idea**
La región es el triángulo $\{0\le y\le x\le1\}$. Como el área es $\tfrac12$, la densidad constante vale $f_{X,Y}=2$. Para cada $x$, la condicional $Y\mid X=x$ es uniforme en $[0,x]$ (ancho creciente con $x$): de ahí sale todo, incluido que acá el MMSE y el LMMSE terminan coincidiendo (mismo fenómeno que en Cap 8 en profundidad, Ejercicio 2).

###### **Resolución**
**a)** Integrando la constante $2$ sobre $y\in[0,x]$:
$$\boxed{\ f_X(x) = 2x\ ,\quad 0\le x\le1\ }$$
Para $f_{Y\mid X}(y\mid x)=\dfrac{f_{X,Y}}{f_X(x)}=\dfrac{2}{2x}=\dfrac1x$ en $[0,x]$; en $x=\tfrac13$: $f_X(\tfrac13)=\tfrac23$, así que
$$\boxed{\ f_{Y\mid X}\!\left(y\mid\tfrac13\right) = 3\ ,\quad 0\le y\le\tfrac13\ }$$
(uniforme, como era de esperar: dado $X=x$, $Y$ siempre es uniforme en $[0,x]$).

![[sol08-ej07-densidades.svg]]

**b) No son independientes.** El soporte mismo es triangular ($0\le y\le x\le1$): para $x=0{,}2$, $Y$ solo puede valer entre $0$ y $0{,}2$, pero para $x=0{,}9$ puede llegar hasta $0{,}9$. Que el rango posible de $Y$ dependa de $X$ ya alcanza para descartar independencia (ni hace falta comparar las densidades: $f_{X,Y}(x,y)=2\ne f_X(x)f_Y(y)=2x\cdot2(1-y)$).

**c)** Al ser $Y\mid X=x$ uniforme en $[0,x]$, su media es el punto medio:
$$\boxed{\ \hat y_{MMSE}(x) = \frac{x}{2}\ ,\quad 0\le x\le1\ }$$

![[sol08-ej07-estimador-mmse.svg]]

**d)** El estimador MMSE, por construcción (regla de ortogonalidad completa, Parte 1.2/1.3 del complemento), siempre tiene sesgo cero y error cuadrático medio igual a $E_X[\operatorname{Var}(Y\mid X)]$:
$$\operatorname{Var}(Y\mid X=x)=\frac{x^2}{12}\quad(\text{varianza de una uniforme de ancho }x)$$
$$e^2 = \int_0^1 \frac{x^2}{12}\cdot 2x\,dx = \frac{1}{6}\int_0^1 x^3\,dx=\boxed{\ \frac{1}{24}\approx0{,}0417\ }$$
$$b = E\!\left[\frac{X}{2}-Y\right] = \frac{\mu_X}{2}-\mu_Y = \frac{2/3}{2}-\frac13=\frac13-\frac13=\boxed{\ 0\ }$$
(con $\mu_X=\int_0^1 x\cdot2x\,dx=\tfrac23$ y $\mu_Y=\int_0^1 y\cdot2(1-y)\,dy=\tfrac13$, usando $f_Y(y)=2(1-y)$).

**e)** Los momentos centrados: $\sigma_X^2=E[X^2]-\mu_X^2=\tfrac12-\tfrac49=\tfrac1{18}$, $\sigma_Y^2=E[Y^2]-\mu_Y^2=\tfrac16-\tfrac19=\tfrac1{18}$, $\sigma_{XY}=E[XY]-\mu_X\mu_Y=\tfrac14-\tfrac29=\tfrac{1}{36}$ (con $E[XY]=\int_0^1\!\int_0^x xy\cdot2\,dy\,dx=\tfrac14$). Entonces $a=\sigma_{XY}/\sigma_X^2=\tfrac12$, $b=\mu_Y-a\mu_X=\tfrac13-\tfrac12\cdot\tfrac23=0$:
$$\boxed{\ \hat y_{LMMSE}(x) = \frac{x}{2}\ \ (\text{idéntico al MMSE})\ },\qquad \rho_{XY}=\frac{\sigma_{XY}}{\sigma_X\sigma_Y}=\frac12$$
$$\boxed{\ \text{MMSE}_{LMMSE}=\sigma_Y^2(1-\rho^2)=\frac1{18}\cdot\frac34=\frac1{24}\ \ (\text{igual al de (d)})\ }$$

###### **Verificación**
$f_X$ y $f_Y$ integran a $1$; $\operatorname{Var}(Y\mid X)\ge0$ ✓; $|\rho|=1/2<1$ ✓; el MMSE del LMMSE coincide exactamente con el $e^2$ de (d), como debía ser. *(verificado con sympy: `integrate(2,(y,0,x))=2x`; `integrate(y*2,(y,0,x))/fX = x/2`; `integrate((y-x/2)**2*2,(y,0,x))/fX = x**2/12`; integrando esto último contra $f_X$ en $[0,1]$ da $1/24$ exacto; el sesgo integrado da $0$ exacto; $\sigma_X^2=\sigma_Y^2=1/18$, $\sigma_{XY}=1/36$, $\rho=1/2$, MMSE del LMMSE $=1/24$.)*

> [!info] Conexión
> Es el mismo triángulo que el Ejercicio 2 de [[PROCESAMIENTO DE SEÑALES - Cap 8 en profundidad]] (Parte 5), con los mismos números: ahí ya se explica por qué no hace falta gaussianidad para que LMMSE = MMSE, alcanza con que la regresión $E[Y\mid X=x]$ ya sea una recta.

---

## Ejercicio 8 — MMSE y LMMSE sobre una región en dos cuadrados

> [!quote] Enunciado
> 8. Dos variables aleatorias $X$ e $Y$ tienen una PDF conjunta $f_{X,Y}(x,y)$ que es igual a una constante $K$ en la región sombreada mostrada en la figura, y es igual a cero en el resto.
>
> ![[Pasted image 20260814134002.png|267]]
>
> a) i) Encuentre $K$.
>    ii) Realice un gráfico etiquetado de la PDF marginal $f_Y(y)$.
>    iii) Realice un gráfico etiquetado de la PDF condicional $f_{Y|X}(y|\tfrac14)$.
> b) Encuentre la estimación MMSE de $Y$ dado que se observó $X=x$, es decir, la media condicional $E(Y|X=x)$, donde $x$ puede ser cualquier valor entre $0$ y $2$.
> c) Encuentre la estimación LMMSE de $Y$ dado que se observó $X=x$, donde $x$ puede ser cualquier valor entre $0$ y $2$. Note que $E(XY)=\tfrac34$ para la función de densidad de probabilidad conjunta mostrada en la figura.

###### **Idea**
La región son dos cuadrados de lado $1$ **opuestos** por una esquina: $[0,1]\times[1,2]$ (arriba a la izquierda) y $[1,2]\times[0,1]$ (abajo a la derecha). Es clave notar que para cualquier $x$ fijo, el segmento vertical de $Y$ compatible cae **entero** dentro de uno solo de los dos cuadrados: por eso $E[Y\mid X=x]$ va a ser una función escalón, no una recta.

###### **Resolución**
**a-i)** Área total $=1+1=2$, así que
$$\boxed{\ K=\frac12\ }$$

**a-ii)** Para $y\in[0,1]$ el segmento de $x$ compatible es $[1,2]$ (cuadrado de abajo), y para $y\in[1,2]$ es $[0,1]$ (cuadrado de arriba); en ambos casos el ancho es $1$:
$$\boxed{\ f_Y(y) = \frac12\ ,\quad 0\le y\le2\quad(\text{uniforme})\ }$$

![[sol08-ej08-densidades.svg]]

**a-iii)** $x=\tfrac14\in[0,1]$ cae en el cuadrado de arriba, donde $y\in[1,2]$. Ahí $f_X(\tfrac14)=\int_1^2 \tfrac12\,dy=\tfrac12$, así que
$$\boxed{\ f_{Y\mid X}\!\left(y\mid\tfrac14\right) = \frac{K}{f_X(1/4)}=1\ ,\quad 1\le y\le2\quad(\text{uniforme})\ }$$

**b)** Como el segmento de $y$ compatible con cada $x$ cae íntegro en un solo cuadrado, la condicional es uniforme en ese segmento y su media es el punto medio:
$$
\hat y_{MMSE}(x)=E[Y\mid X=x]=
\begin{cases}
1{,}5\,, & 0\le x<1 \quad(\text{cuadrado de arriba: } Y\mid X\sim U[1,2])\\[2pt]
0{,}5\,, & 1<x\le2 \quad(\text{cuadrado de abajo: } Y\mid X\sim U[0,1])
\end{cases}
$$
$$\boxed{\ \hat y_{MMSE}(x)\ \text{es un escalón, con un salto de } 1{,}5\text{ a }0{,}5\text{ en } x=1\ }$$

**c)** Por la simetría de la región (invariante ante $x\leftrightarrow y$, $x\to x$ reflejado respecto de $x=1$), $X$ e $Y$ son ambas uniformes en $[0,2]$: $\mu_X=\mu_Y=1$, $\sigma_X^2=\sigma_Y^2=\dfrac{2^2}{12}=\dfrac13$. Con el dato $E(XY)=\tfrac34$:
$$\sigma_{XY}=E(XY)-\mu_X\mu_Y=\frac34-1=-\frac14$$
$$a=\frac{\sigma_{XY}}{\sigma_X^2}=\frac{-1/4}{1/3}=-\frac34\,,\qquad b=\mu_Y-a\mu_X=1+\frac34=\frac74$$
$$\boxed{\ \hat y_{LMMSE}(x) = -\frac34\,x+\frac74\ ,\quad 0\le x\le2\ }$$
En $x=1$ da $\hat y_{LMMSE}(1)=1$, exactamente el promedio de los dos escalones del MMSE ($1{,}5$ y $0{,}5$) — tiene sentido: la recta que mejor aproxima un escalón simétrico pasa por el punto medio en el centro de simetría.

![[sol08-ej08-mmse-lmmse.svg]]
*(verde: el MMSE real, a escalones; ámbar: el LMMSE, la mejor recta. Se cruzan en $x=1$.)*

###### **Verificación**
$f_Y$ integra a $1$ ✓; $\sigma_{XY}$ negativo tiene sentido: cuando $X$ es chico ($<1$) $Y$ tiende a ser grande ($>1$), y viceversa — correlación negativa, consistente con $a<0$. $|\rho|=|\sigma_{XY}|/\sigma_X\sigma_Y=(1/4)/(1/3)=3/4<1$ ✓. *(verificado con sympy: `K=1/2` de integrar sobre ambos cuadrados; `muX=muY=1`, `sigX2=1/3` de integrar $x^2 f_X$; con `E[XY]=3/4` dado se recupera `sigXY=-1/4`, `a=-3/4`, `b=7/4` exactos, coincidiendo con la cuenta a mano.)*

> [!warning] Ojo
> El MMSE real es una función escalón, **no** una recta: acá el LMMSE no coincide con el MMSE (a diferencia del Ejercicio 7). Es el ejemplo típico de cuánto puede perder un estimador lineal cuando la verdadera regresión tiene un salto: en $x$ apenas mayor que $1$, el MMSE ya vale $0{,}5$, pero el LMMSE recién llega a $1$.

---

## Ejercicio 9 — LMMSE vs. MMSE sobre una región con agujero y muesca

> [!quote] Enunciado
> 9. Supongamos que $X$ e $Y$ son variables aleatorias con PDF conjunta $f_{X,Y}(x,y)$ que es constante en el área sombreada mostrada en la figura, y nula en el resto.
>
> ![[Pasted image 20260814134021.png|303]]
>
> a) Encuentre el estimador LMMSE de $Y$ a partir de medir $X$.
> b) Para $x$ en el rango de $-2$ a $2$, realice un gráfico completamente etiquetado del estimador MMSE de $Y$. ¿Cómo se compara el estimador correspondiente con el del punto a)?

> [!warning] Nota sobre el enunciado
> La figura de la guía (recortada de la Figura P8.5 del libro) se midió con precisión sobre la versión original: es el cuadrado $[-2,2]\times[-2,2]$ al que se le quitan dos piezas: un **agujero** rectangular $[-1,0]\times[-1,1]$ (no centrado: pegado al eje $y$, del lado negativo de $x$) y una **muesca** $[1,2]\times[-2,-1]$ en la esquina inferior derecha. El área que queda es $16-2-1=13$, así que $f_{X,Y}(x,y)=\dfrac{1}{13}$ en la región.

###### **Idea**
Como la región no es simétrica (el agujero está corrido hacia $x<0$, la muesca solo afecta $x>0$), no hay atajo de simetría: hay que integrar por tramos de $x$. Conviene partir el dominio en cuatro franjas verticales según qué "recorte" atraviesan:

| Tramo de $x$ | Segmento(s) de $y$ disponibles | Ancho total |
|---|---|---|
| $[-2,-1)$ | $[-2,2]$ completo | $4$ |
| $[-1,0]$ | $[-2,-1]\cup[1,2]$ (el agujero parte el segmento en dos) | $2$ |
| $(0,1)$ | $[-2,2]$ completo | $4$ |
| $[1,2]$ | $(-1,2]$ (la muesca corta el tramo $[-2,-1]$) | $3$ |

###### **Resolución**
**a) LMMSE.** Integrando $x$, $y$, $x^2$ y $xy$ tramo por tramo (con $f=1/13$):
$$\mu_X=-\frac{1}{26}\approx-0{,}0385\,,\qquad \mu_Y=\frac{3}{26}\approx0{,}1154$$
$$E[X^2]=\frac{55}{39}\ \implies\ \sigma_X^2=\frac{55}{39}-\frac{1}{676}=\frac{2857}{2028}\approx1{,}4088$$
$$E[XY]=\frac{9}{52}\ \implies\ \sigma_{XY}=\frac{9}{52}-\left(-\frac{1}{26}\right)\!\left(\frac{3}{26}\right)=\frac{30}{169}\approx0{,}1775$$
$$a=\frac{\sigma_{XY}}{\sigma_X^2}=\frac{360}{2857}\approx0{,}1260\,,\qquad b=\mu_Y-a\mu_X\approx0{,}1202$$
$$\boxed{\ \hat y_{LMMSE}(x)\approx 0{,}126\,x+0{,}120\ ,\quad -2\le x\le2\ }$$
La pendiente da positiva y chica: la muesca (que vive en $x>0,y<0$) le quita masa a los $y$ negativos justo del lado derecho, así que $Y$ tiende a ser (apenas) más grande cuando $X$ es más grande — pero es una asimetría leve, de ahí la pendiente chica.

**b) MMSE.** En los tramos donde el segmento de $y$ es simétrico respecto de $y=0$ (los tramos $[-2,-1)$, $[-1,0]$ y $(0,1)$: en el del agujero, $[-2,-1]$ y $[1,2]$ tienen igual longitud y son reflejo uno del otro), la media condicional da $0$. Solo en el tramo de la muesca, $x\in[1,2]$, el segmento $(-1,2]$ no es simétrico y su punto medio es $\dfrac{-1+2}{2}=0{,}5$:
$$
\hat y_{MMSE}(x)=E[Y\mid X=x]=
\begin{cases}
0\,, & -2\le x<1\\[2pt]
0{,}5\,, & 1\le x\le2
\end{cases}
$$
$$\boxed{\ \hat y_{MMSE}(x)\ \text{es un escalón: } 0 \text{ hasta } x=1\text{, después salta a } 0{,}5\ }$$

![[sol08-ej09-mmse-lmmse.svg]]

**Comparación.** El LMMSE (recta ámbar) es una aproximación *global* y suave a un fenómeno que en realidad es puramente *local*: toda la "información" que separa a $Y$ de la media nula está concentrada en el pedacito $x\in[1,2]$ (el $23\%$ del rango de $x$), y ni siquiera ahí el salto es grande ($0$ a $0{,}5$, mientras $\sigma_Y\approx1{,}9$). El LMMSE, al no poder ver el escalón, reparte ese efecto en una pendiente chica a lo largo de *todo* el rango — subestima $\hat y$ en $x$ cercano a $2$ y lo sobreestima levemente en $x$ cercano a $-2$.

###### **Verificación**
$\sigma_X^2>0$ ✓, $|\rho_{XY}|=|\sigma_{XY}|/\sqrt{\sigma_X^2\sigma_Y^2}<1$ (se puede chequear que da $\approx0{,}134$). El área de la región integra $13$ ✓. *(verificado numéricamente: Monte Carlo con $2\cdot10^7$ puntos uniformes en $[-2,2]^2$, descartando los que caen en el agujero o la muesca, da área efectiva $\approx13{,}00$, $\mu_X\approx-0{,}0387$, $\mu_Y\approx0{,}1149$, $\sigma_X^2\approx1{,}4087$, $\sigma_{XY}\approx0{,}1776$ — todos coinciden con las fracciones exactas de arriba. Agrupando por bines de $X$, $E[Y\mid X{=}x]$ da $\approx0$ en todo $x<1$ y $\approx0{,}500$ en $x\in[1,2]$, confirmando el escalón.)*

---

## Ejercicio 10 — LMMSE con dos mediciones de una sinusoide aleatoria

> [!quote] Enunciado
> 10. Considere una señal sinusoidal de la forma
> $$X(t) = A\cos(\omega_0 t + \Theta)$$
> donde $\omega_0$ se asume conocido, mientras que $A$ y $\Theta$ son variables aleatorias estadísticamente independientes, con la PDF de $\Theta$ uniforme en el intervalo $[0,2\pi]$. Supongamos que se desea construir un estimador LMMSE para $X(t_2)$ a partir de las mediciones $X(t_0)$ y $X(t_1)$, es decir, un estimador de la forma
> $$\hat X(t_2) = a_0 X(t_0) + a_1 X(t_1) + b$$
> que minimiza el error cuadrático medio
> $$E\left[\left(X(t_2)-\hat X(t_2)\right)^2\right].$$
>
> a) Determine el valor óptimo de $b$.
> b) Plantee en detalle las ecuaciones específicas que necesitaría resolver para obtener los valores óptimos de $a_0$ y $a_1$, y utilícelas para calcular $a_0$ y $a_1$. Verifique que sus respuestas tomen valores razonables para los siguientes dos casos: i) $t_2=t_1$; ii) $t_2=t_0$. Para manejar estos cálculos de forma prolija, puede ser útil recordar que la inversa de una matriz $2\times2$ de la forma
> $$\begin{pmatrix} p & q \ r & s\end{pmatrix}$$
> es
> $$\frac{1}{ps-qr}\begin{pmatrix} s & -q \ -r & p\end{pmatrix},$$
> afirmación que puede verificar directamente multiplicando ambas matrices entre sí.
> c) Muestre que el MMSE asociado a este estimador lineal es cero.

###### **Idea**
Primero hay que caracterizar el proceso: con $\Theta\sim U[0,2\pi]$ independiente de $A$, $X(t)$ resulta de media nula y con autocorrelación que depende solo de la diferencia de tiempos —el fasor aleatorio "gira" y promedia la fase absoluta—. Con eso, todo el problema es aplicar las ecuaciones normales de la Parte 1.6 del complemento con $L=2$ mediciones.

###### **Resolución**
**Caracterización del proceso.** $E[X(t)]=E[A]\,E[\cos(\omega_0t+\Theta)]=0$ (el coseno promedia a $0$ sobre una fase uniforme en un período completo), para todo $t$. Para la correlación:
$$R_{XX}(t_1,t_2)=E[A^2]\,E[\cos(\omega_0t_1+\Theta)\cos(\omega_0t_2+\Theta)]=\frac{E[A^2]}{2}\Big[\cos(\omega_0(t_1-t_2))+\underbrace{E[\cos(\omega_0(t_1+t_2)+2\Theta)]}_{0}\Big]$$
(el segundo término se anula porque $2\Theta$ también barre un número entero de períodos completos al promediar sobre $\Theta$). Definiendo la potencia media $P=E[A^2]/2$:
$$R(\tau)=P\cos(\omega_0\tau)$$

**a)** Con medias todas nulas, $b=\mu_{X(t_2)}-a_0\mu_{X(t_0)}-a_1\mu_{X(t_1)}$ (Parte 1.6 del complemento):
$$\boxed{\ b=0\ }$$

**b)** Las ecuaciones normales $C_{XX}\mathbf a=\mathbf c_{XY}$, con $C_{XX}$ la covarianza de $(X(t_0),X(t_1))$ y $\mathbf c_{XY}$ las covarianzas cruzadas con $X(t_2)$ (covarianzas = correlaciones, porque las medias son cero):
$$\begin{pmatrix}R(0) & R(t_0-t_1)\ R(t_1-t_0) & R(0)\end{pmatrix}\begin{pmatrix}a_0\a_1\end{pmatrix}=\begin{pmatrix}R(t_0-t_2)\R(t_1-t_2)\end{pmatrix}$$
Sea $\alpha=\omega_0(t_1-t_0)$. Como $R(\tau)=P\cos(\omega_0\tau)$ es par, la matriz es $P\begin{pmatrix}1&\cos\alpha\\cos\alpha&1\end{pmatrix}$, y el vector del lado derecho es $P\begin{pmatrix}\cos(\omega_0(t_2-t_0))\\cos(\omega_0(t_2-t_1))\end{pmatrix}$ (coseno par). La potencia $P$ se cancela al invertir y multiplicar. Usando la fórmula de la inversa $2\times2$ dada, con $\det=1-\cos^2\alpha=\sin^2\alpha$:
$$\begin{pmatrix}a_0\a_1\end{pmatrix}=\frac{1}{\sin^2\alpha}\begin{pmatrix}1&-\cos\alpha\-\cos\alpha&1\end{pmatrix}\begin{pmatrix}\cos\theta_0\\cos\theta_1\end{pmatrix},\qquad \theta_0=\omega_0(t_2-t_0),\ \theta_1=\omega_0(t_2-t_1)$$
Usando $\theta_0=\theta_1+\alpha$ y las identidades de suma de ángulos, los numeradores se simplifican notablemente ($\cos\theta_0-\cos\alpha\cos\theta_1=-\sin\alpha\sin\theta_1$, y de forma análoga para la otra fila) hasta quedar:
$$\boxed{\ a_0 = \frac{\sin\big(\omega_0(t_1-t_2)\big)}{\sin\big(\omega_0(t_1-t_0)\big)}\ ,\qquad a_1 = \frac{\sin\big(\omega_0(t_2-t_0)\big)}{\sin\big(\omega_0(t_1-t_0)\big)}\ }$$
(válido siempre que $\sin(\omega_0(t_1-t_0))\ne0$, es decir que $t_0$ y $t_1$ no estén separados por un múltiplo exacto de medio período).

*Casos límite.* **i)** $t_2=t_1$: $a_0=\sin(0)/\sin\alpha=0$, $a_1=\sin(\alpha)/\sin\alpha=1$. El estimador da $\hat X(t_1)=X(t_1)$: tiene sentido, si ya se está estimando el mismo instante que se mide, el peso tiene que caer entero sobre esa medición. **ii)** $t_2=t_0$: por simetría, $a_0=1$, $a_1=0$, y $\hat X(t_0)=X(t_0)$: mismo razonamiento.

**c)** Con $\omega_0$ conocido, $X(t)=A\cos\Theta\cos(\omega_0t)-A\sin\Theta\sin(\omega_0t)=u\cos(\omega_0t)-v\sin(\omega_0t)$, donde $u=A\cos\Theta$, $v=A\sin\Theta$ son dos variables aleatorias fijas (no dependen de $t$). Conocer $X(t_0)$ y $X(t_1)$ es un sistema lineal $2\times2$ en $(u,v)$:
$$X(t_0)=u\cos(\omega_0t_0)-v\sin(\omega_0t_0),\qquad X(t_1)=u\cos(\omega_0t_1)-v\sin(\omega_0t_1)$$
que —siempre que $\sin(\omega_0(t_1-t_0))\ne0$— tiene solución única para $(u,v)$ en términos de $X(t_0),X(t_1)$. Y como $X(t_2)=u\cos(\omega_0t_2)-v\sin(\omega_0t_2)$ es a su vez lineal en esos mismos $(u,v)$, **$X(t_2)$ queda determinado exactamente** (para *cada* realización de $A,\Theta$, no solo en promedio) por la misma combinación lineal $a_0X(t_0)+a_1X(t_1)$ hallada en (b). El error es entonces idénticamente cero, no solo de esperanza nula:
$$\boxed{\ \text{MMSE} = E\big[(X(t_2)-\hat X(t_2))^2\big] = 0\ }$$

###### **Verificación**
*(verificado numéricamente: con $\omega_0=2{,}3$, $t_0=0{,}3$, $t_1=1{,}1$, $t_2=2{,}7$, la fórmula da $a_0\approx0{,}5319$, $a_1\approx-0{,}7171$ — coincide exactamente con resolver $C_{XX}\mathbf a=\mathbf c_{XY}$ numéricamente. Generando $2\cdot10^5$ pares $(A,\Theta)$ con $A\sim U[0{,}5,3]$, $\Theta\sim U[0,2\pi]$, el error máximo $|X(t_2)-a_0X(t_0)-a_1X(t_1)|$ da $\approx5\times10^{-15}$ —cero salvo error de redondeo de punto flotante—, y los casos límite $t_2=t_1$ y $t_2=t_0$ reproducen $(a_0,a_1)=(0,1)$ y $(1,0)$ exactos.)*

> [!info] Conexión
> Este es el germen del filtro de Wiener no causal del capítulo 12: acá, con solo dos muestras de una sinusoide de frecuencia conocida, ya alcanza para predecir *cualquier* otra muestra sin error, porque el proceso vive en un espacio de dimensión $2$ (los "fasores" $u,v$). En procesos con más contenido espectral hacen falta más muestras (o un filtro completo) y el MMSE deja de ser cero.

---

## Ejercicio 11 — MMSE en un canal binario sin memoria

> [!quote] Enunciado
> 11. Considere un sistema de comunicación digital en el cual un flujo de bits (1s y 0s) independientes e idénticamente distribuidos (i.i.d.) $s[n]$ es transmitido a través de un canal defectuoso y sin memoria, con 1s y 0s equiprobables. La probabilidad de que un 1 sea recibido como un 0 es $1/8$ y la probabilidad de que un 0 sea recibido como un 1 es $1/4$. Este tipo de canal se conoce como canal binario sin memoria y se representa en la figura.
>
> ![[Pasted image 20260814134042.png|316]]
>
> a) Para cualquier índice de tiempo $n$, determine la PMF conjunta $P(r,s)$ y la PMF marginal $P(r)$.
> b) Para obtener una estimación $\hat s[n]$ de $s[n]$ a partir de $r[n]$, la señal recibida puede procesarse a través de un sistema sin memoria, posiblemente no lineal, $F$. El sistema sin memoria $F$ (ver figura) debe diseñarse para minimizar el error cuadrático medio definido como:
> $$\epsilon = E\left[(s[n]-\hat s[n])^2\right].$$
> Determine el sistema $F$.
> c) Con el sistema obtenido en b), determine el valor $\hat s[n]$ que minimiza
> $$E\left[(s[n]-\hat s[n])^2 \mid r[n]=r\right].$$
> ![[Pasted image 20260814134144.png|258]]
> Además, determine la probabilidad de que, en un índice de tiempo arbitrario $n_0$, la estimación $\hat s[n_0]$ y el valor verdadero $s[n_0]$ sean iguales.

###### **Idea**
$s[n]$ es binaria, así que "diseñar el sistema $F$ que minimiza el MSE" es ni más ni menos que hallar el estimador MMSE sin restricciones $\hat s[n]=E[s[n]\mid r[n]]$: como $r[n]$ solo toma dos valores, $F$ queda determinado por dos números, $F(0)$ y $F(1)$.

###### **Resolución**
**a)** Con $P(s{=}1)=P(s{=}0)=\tfrac12$, $P(r{=}0\mid s{=}1)=\tfrac18$, $P(r{=}1\mid s{=}1)=\tfrac78$, $P(r{=}1\mid s{=}0)=\tfrac14$, $P(r{=}0\mid s{=}0)=\tfrac34$:

| | $s=0$ | $s=1$ |
|---|---|---|
| $r=0$ | $\tfrac12\cdot\tfrac34=\tfrac{6}{16}$ | $\tfrac12\cdot\tfrac18=\tfrac{1}{16}$ |
| $r=1$ | $\tfrac12\cdot\tfrac14=\tfrac{2}{16}$ | $\tfrac12\cdot\tfrac78=\tfrac{7}{16}$ |

$$\boxed{\ P(r,s):\ P(0,0)=\tfrac{6}{16},\ P(0,1)=\tfrac1{16},\ P(1,0)=\tfrac{2}{16},\ P(1,1)=\tfrac{7}{16}\ }$$
Sumando por filas:
$$\boxed{\ P(r{=}0)=\frac{6+1}{16}=\frac{7}{16}\,,\qquad P(r{=}1)=\frac{2+7}{16}=\frac{9}{16}\ }$$

**b)** El estimador MMSE de una variable a partir de otra es la media condicional, sin importar que $s$ sea binaria:
$$F(r) = \hat s_{MMSE}(r) = E[s\mid r]=P(s{=}1\mid r)$$
Por Bayes, $P(s{=}1\mid r)=\dfrac{P(r,s{=}1)}{P(r)}$:
$$F(0)=P(s{=}1\mid r{=}0)=\frac{1/16}{7/16}=\frac17\,,\qquad F(1)=P(s{=}1\mid r{=}1)=\frac{7/16}{9/16}=\frac79$$
$$\boxed{\ F(r)=\begin{cases}\dfrac17\approx0{,}143\,, & r=0\\[4pt] \dfrac79\approx0{,}778\,, & r=1\end{cases}\ }$$
Notar que $F$ **no** es un decisor binario "duro" (no devuelve $0$ o $1$): el MMSE sin restricciones para una variable binaria es una probabilidad, y esa probabilidad ya "sabe" que el canal es más confiable transmitiendo $1$ ($7/9$, más cerca de $1$) que transmitiendo $0$ ($1/7$, más cerca de $0$ pero no tanto, porque el canal es más ruidoso de $0\to1$).

**c)** Para cada $r$ fijo, minimizar $E[(s-\hat s)^2\mid r]$ sobre la constante $\hat s$ es exactamente el problema de la Parte 1.1 del complemento (sin datos, pero condicionado a $r$): el mínimo se alcanza en la media condicional, que es la misma $F(r)$ de (b):
$$\boxed{\ \hat s[n] = F(r[n]) = \begin{cases}1/7\,, & r[n]=0\\ 7/9\,, & r[n]=1\end{cases}\ }$$
(no hay nada nuevo que calcular: (b) y (c) piden lo mismo, y la coherencia entre ambas partes es justamente la prueba de que $F$ del punto (b) es óptimo *para cada* valor de $r$, no solo en promedio.)

Para la probabilidad de acierto exacto: $\hat s[n_0]$ solo puede valer $1/7$ o $7/9$, mientras que $s[n_0]\in\{0,1\}$. Como $1/7\ne0,1$ y $7/9\ne0,1$, **nunca** hay igualdad exacta:
$$\boxed{\ P\big(\hat s[n_0]=s[n_0]\big) = 0\ }$$

###### **Verificación**
Las probabilidades conjuntas suman $1$: $6/16+1/16+2/16+7/16=1$ ✓; $P(r{=}0)+P(r{=}1)=7/16+9/16=1$ ✓; $F(r)\in[0,1]$ para ambos valores ✓ (tiene que estarlo, es una probabilidad condicional). *(verificado numéricamente: simulando $2\cdot10^7$ bits i.i.d. con el canal descripto, Monte Carlo da $P(s{=}0,r{=}0)\approx0{,}3749$ ($6/16=0{,}375$), $P(s{=}1,r{=}1)\approx0{,}4376$ ($7/16=0{,}4375$), $P(r{=}1)\approx0{,}5626$ ($9/16=0{,}5625$), $E[s\mid r{=}1]\approx0{,}7777$ ($7/9=0{,}7778$), $E[s\mid r{=}0]\approx0{,}1429$ ($1/7=0{,}1429$), y $P(\hat s=s)\approx0$ exacto sobre las $2\cdot10^7$ muestras.)*

> [!warning] Ojo
> No confundir el MMSE sin restricciones (que acá da valores fraccionarios, $1/7$ y $7/9$) con el detector MAP del capítulo 9 (que sí daría una decisión dura $0$ o $1$, minimizando la *probabilidad de error* en vez del *error cuadrático medio*). Son dos criterios distintos que en general llevan a estimadores distintos; para variables binarias casi nunca coinciden.

---

## Ejercicio 12 — Canal con ganancia aleatoria multiplicativa

> [!quote] Enunciado
> 12. Considere un sistema de comunicación en el cual la variable aleatoria $Y$ es transmitida a través de un canal con una ganancia aleatoria $W$, de modo que la variable recibida es $X=WY$. Asuma que $Y$ y $W$ son independientes, y que ambas están distribuidas de manera uniforme en el rango $[1,2]$.
>
> a) Suponga que usted está en el receptor y quiere estimar el valor transmitido $Y$ a partir de una medición del valor recibido $X$, utilizando el estimador LMMSE $\hat Y = d_1 X + d_2$. Determine cuáles deben ser $d_1$ y $d_2$, y calcule el MMSE asociado.
> b) Suponga en cambio que usted está en el transmisor y quiere estimar cuál será el valor recibido $X$ a partir de una medición del valor transmitido $Y$. Encuentre el estimador MMSE (sin restricciones) $\hat X(Y)$.

###### **Idea**
$Y$ y $W$ son uniformes en $[1,2]$ e independientes, con $E[Y]=E[W]=1{,}5$ y $\operatorname{Var}(Y)=\operatorname{Var}(W)=\tfrac{1}{12}$ (varianza de una uniforme de ancho $1$). Para (a) hace falta $\operatorname{Var}(X)$ y $\operatorname{Cov}(X,Y)$, que salen de que $X=WY$ con $W\perp Y$. Para (b), la clave es que condicionar en $Y=y$ dentro de $X=WY$ deja a $y$ como una constante: $X\mid Y=y = yW$, así que su media condicional es simplemente $y\,E[W]$ — automáticamente **lineal**, sin que haga falta imponerlo.

###### **Resolución**
**Momentos de $X$.** Con $E[W^2]=E[Y^2]=\int_1^2t^2\,dt=\tfrac73$ (por independencia, $E[W^kY^k]=E[W^k]E[Y^k]$):
$$\mu_X=E[WY]=E[W]E[Y]=1{,}5\times1{,}5=2{,}25$$
$$E[X^2]=E[W^2]E[Y^2]=\left(\frac73\right)^2=\frac{49}{9}\ \implies\ \sigma_X^2=\frac{49}{9}-\left(\frac94\right)^2=\frac{49}{9}-\frac{81}{16}=\frac{55}{144}\approx0{,}3819$$
$$\sigma_{XY}=E[XY]-\mu_X\mu_Y=E[W]E[Y^2]-\mu_X\mu_Y=1{,}5\cdot\frac73-2{,}25\times1{,}5=3{,}5-3{,}375=\frac18=0{,}125$$

**a)** Ecuaciones del LMMSE (Parte 1.4 del complemento):
$$d_1=\frac{\sigma_{XY}}{\sigma_X^2}=\frac{1/8}{55/144}=\frac{144}{8\cdot55}=\frac{18}{55}\approx0{,}3273$$
$$d_2=\mu_Y-d_1\mu_X=1{,}5-\frac{18}{55}\cdot2{,}25=\frac{165}{110}-\frac{81}{110}=\frac{84}{110}=\frac{42}{55}\approx0{,}7636$$
$$\boxed{\ \hat Y_\ell = \frac{18}{55}X+\frac{42}{55}\ \approx\ 0{,}3273\,X+0{,}7636\ }$$
$$\text{MMSE}=\sigma_Y^2-d_1\sigma_{XY}=\frac{1}{12}-\frac{18}{55}\cdot\frac18=\frac{1}{12}-\frac{9}{220}=\boxed{\ \frac{7}{165}\approx0{,}0424\ }$$

**b)** Fijado $Y=y$ (una constante), $X=Wy$ es simplemente $W$ reescalado, así que su media condicional es
$$\hat X_{MMSE}(y)=E[X\mid Y=y]=E[Wy\mid Y=y]=y\,E[W\mid Y=y]\overset{W\perp Y}{=}y\,E[W]$$
$$\boxed{\ \hat X_{MMSE}(Y) = \frac32\,Y\ ,\quad 1\le Y\le2\ }$$
Sale lineal automáticamente —no porque se lo haya restringido a serlo, sino porque la estructura multiplicativa con factores independientes lo fuerza—, así que acá el MMSE sin restricciones coincide con lo que daría un LMMSE.

###### **Verificación**
$\sigma_X^2>0$, $\text{MMSE}=7/165\approx0{,}042<\sigma_Y^2=1/12\approx0{,}083$ ✓ (la medición ayuda, pero no mucho: $\rho_{XY}^2=\sigma_{XY}^2/(\sigma_X^2\sigma_Y^2)=(1/8)^2/((55/144)(1/12))=27/55\approx0{,}491$, la mitad de la varianza explicada). *(verificado numéricamente: Monte Carlo con $6\cdot10^6$ muestras de $Y,W\sim U[1,2]$ independientes, $X=WY$, da $\mu_X\approx2{,}2498$, $\sigma_X^2\approx0{,}3820$, $\sigma_{XY}\approx0{,}1250$, $d_1\approx0{,}3271$, $d_2\approx0{,}7639$, MMSE$\approx0{,}0424$ — todos coinciden con las fracciones exactas. Agrupando por bines de $Y$, $E[X\mid Y{=}y]$ reproduce $1{,}5y$ dentro del error esperado por el ancho de bin.)*

---
