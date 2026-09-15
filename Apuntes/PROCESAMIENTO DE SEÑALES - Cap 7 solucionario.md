Solucionario de los Ejercicios Propuestos del capítulo 7 de [[PROCESAMIENTO DE SEÑALES]]. La teoría con demostraciones está en [[PROCESAMIENTO DE SEÑALES - Cap 7 en profundidad]].

# Modelos probabilísticos — Solucionario

Todo el capítulo se resuelve con un puñado de herramientas: áreas/integrales para probabilidades e independencia de eventos, momentos de la uniforme, bilinealidad de la covarianza, el coeficiente de correlación $\rho$, combinaciones afines de gaussianas y Bayes sobre una tabla conjunta. Cada ejercicio empieza con el enunciado copiado tal cual de la guía y, cuando la guía difiere del libro, con una nota aclarando qué versión se resuelve.

###### **Índice**
| Ej. | Qué se practica | Problema del libro |
|---|---|---|
| 1 | Independencia de a pares vs. mutua | P7.1 |
| 2 | Momentos de la uniforme y de la suma de dos independientes | P7.3 |
| 3 | Ortogonalidad vs. correlación en una combinación afín de gaussiana | P7.5 |
| 4 | Covarianza y $\rho$ de combinaciones de variables no correlacionadas | P7.6 |
| 5 | Covarianza de combinaciones afines y su densidad conjunta | P7.4 |
| 6 | Bayes sobre una tabla conjunta y probabilidad de error | P7.2 |

---

## Ejercicio 1 — Independencia de a pares vs. mutua

> [!quote] Enunciado
> 1. Dos números $x$ e $y$ son seleccionados de manera aleatoria e independiente entre el intervalo $[0;1]$. Definimos los eventos $A, B, C\ y\ D$ de la siguiente manera.
> ![[Pasted image 20260810105718.png]]
>
> a) Determine en los siguientes casos si los eventos son independientes
> - $A$ y $D$
> - $C$ y $D$
> - $A$ y $B$
>
> b) Verifique si los eventos $B$, $C$ y $D$ son mutuamente independientes.

###### **Idea**
Como $x$ e $y$ son independientes y uniformes en $[0,1]$, toda probabilidad de un evento definido por regiones del cuadrado unitario es directamente su área. Independencia de dos eventos es comparar $P(\text{intersección})$ contra el producto de las probabilidades individuales; para independencia mutua de tres, hay que chequear además la intersección triple.

###### **Resolución**
**Probabilidades individuales.** Con $A=\{y>\tfrac12\}$, $B=\{y<\tfrac12\}$, $C=\{x<\tfrac12\}$ (cada uno media franja del cuadrado) y $D=\{x<\tfrac12,y<\tfrac12\}\cup\{x>\tfrac12,y>\tfrac12\}$ (los dos cuadraditos de la diagonal):
$$P(A)=P(B)=P(C)=P(D)=\tfrac12$$
($D$ es la unión de dos cuadrados de lado $\tfrac12$, área $2\cdot\tfrac14=\tfrac12$.)

**a) $A$ y $D$.** $D$ tiene dos piezas: la de abajo-izquierda ($x<\tfrac12,y<\tfrac12$) y la de arriba-derecha ($x>\tfrac12,y>\tfrac12$). Al intersecar con $A=\{y>\tfrac12\}$ sólo sobrevive la pieza de arriba-derecha (la de abajo-izquierda tiene $y<\tfrac12$, incompatible con $A$):
$$A\cap D=\{x>\tfrac12,\,y>\tfrac12\}\quad\Rightarrow\quad P(A\cap D)=\tfrac14$$
$$P(A)P(D)=\tfrac12\cdot\tfrac12=\tfrac14=P(A\cap D)$$
$$\boxed{\ A\text{ y }D\text{ SON independientes}\ }$$

**$C$ y $D$.** Ahora al intersecar $D$ con $C=\{x<\tfrac12\}$ sobrevive la pieza de abajo-izquierda:
$$C\cap D=\{x<\tfrac12,\,y<\tfrac12\}\quad\Rightarrow\quad P(C\cap D)=\tfrac14=P(C)P(D)$$
$$\boxed{\ C\text{ y }D\text{ SON independientes}\ }$$

**$A$ y $B$.** $A=\{y>\tfrac12\}$ y $B=\{y<\tfrac12\}$ son mutuamente excluyentes (no pueden pasar juntos):
$$P(A\cap B)=0\ \neq\ P(A)P(B)=\tfrac14$$
$$\boxed{\ A\text{ y }B\text{ NO son independientes}\ }$$
(de hecho son incompatibles, el extremo opuesto a la independencia.)

**b) ¿$B$, $C$ y $D$ mutuamente independientes?** Hace falta que los tres pares sean independientes **y** que $P(B\cap C\cap D)=P(B)P(C)P(D)$.

Pares: $B\cap C=\{x<\tfrac12,y<\tfrac12\}$, área $\tfrac14=P(B)P(C)$ ✓. $B\cap D$: de las dos piezas de $D$ sólo la de abajo-izquierda tiene $y<\tfrac12$, así que $B\cap D=\{x<\tfrac12,y<\tfrac12\}$, área $\tfrac14=P(B)P(D)$ ✓. $C\cap D$ ya se calculó arriba, $\tfrac14=P(C)P(D)$ ✓. **Los tres pares son independientes.**

Intersección triple: $B\cap C$ ya es exactamente el cuadradito de abajo-izquierda $\{x<\tfrac12,y<\tfrac12\}$, que está enteramente contenido en $D$. Entonces $B\cap C\cap D=B\cap C$, de área $\tfrac14$:
$$P(B\cap C\cap D)=\tfrac14\qquad\text{pero}\qquad P(B)P(C)P(D)=\left(\tfrac12\right)^3=\tfrac18$$
$$\boxed{\ \tfrac14\neq\tfrac18\ \Rightarrow\ B,C,D\text{ NO son mutuamente independientes}\ }$$
a pesar de ser independientes de a pares.

![[sol07-ej01-regiones-abcd.svg]]
*Las cuatro regiones por separado: $A$ y $B$ no se tocan ($A\cap B=\varnothing$), y $B\cap C$ —el cuadradito de abajo a la izquierda— queda enteramente adentro de $D$.*

###### **Verificación**
Todas las probabilidades caen en $[0,1]$ ✓. *(verificado numéricamente: Monte Carlo con $4\cdot10^6$ pares $(x,y)$ da $P(A\cap D)\approx0{,}2500$ y $P(A)P(D)\approx0{,}2499$; $P(C\cap D)\approx0{,}2502$ vs. $P(C)P(D)\approx0{,}2500$; $P(A\cap B)=0$ vs. $P(A)P(B)\approx0{,}2500$; y para la tripleta $P(B\cap C\cap D)\approx0{,}2502$ contra $P(B)P(C)P(D)\approx0{,}1251$ — claramente distintos, confirma la parte b).)*

> [!warning] Ojo
> Independencia **de a pares** no implica independencia **mutua**. Acá $B$, $C$ y $D$ pasan las tres pruebas de a pares y sin embargo fallan la condición conjunta, porque $B\cap C$ "vive" enteramente dentro de $D$ — hay una dependencia de orden superior que ningún par por separado detecta.

---

## Ejercicio 2 — Momentos de la uniforme y de la suma de dos independientes

> [!quote] Enunciado
> 2. La variable aleatoria V esta distribuida de manera uniforme en un intervalo $[a;b]$.
> a) Determine el valor de la media $\mu_V$, el momento cuadrado $E[V^2]$, la varianza $\sigma_V^2$.
> b) Sea una segunda variable aleatoria $W$ distribuida de la misma manera e independiente de V, hallar la media y la varianza de la variable aleatoria:
> $$Y = V+W$$
> y determine la covarianza y el coeficiente de correlación entre $Y$ y $V$.

###### **Idea**
Los momentos de $V$ salen de integrar la densidad uniforme $f_V(v)=\frac{1}{b-a}$ directamente. Para $Y=V+W$ con $W$ independiente e idéntica a $V$, medias y varianzas se suman, y la covarianza con $V$ sale de bilinealidad: $V$ es la única parte que $Y$ comparte con $V$ mismo.

###### **Resolución**
**a)** Con $f_V(v)=\dfrac{1}{b-a}$ en $[a,b]$:
$$\mu_V=\int_a^b \frac{v}{b-a}\,dv=\frac{1}{b-a}\left[\frac{v^2}{2}\right]_a^b=\frac{b^2-a^2}{2(b-a)}=\boxed{\ \frac{a+b}{2}\ }$$
$$E[V^2]=\int_a^b \frac{v^2}{b-a}\,dv=\frac{1}{b-a}\left[\frac{v^3}{3}\right]_a^b=\frac{b^3-a^3}{3(b-a)}=\boxed{\ \frac{a^2+ab+b^2}{3}\ }$$
(usando $b^3-a^3=(b-a)(a^2+ab+b^2)$). La varianza, restando el cuadrado de la media (común denominador 12):
$$\sigma_V^2=E[V^2]-\mu_V^2=\frac{a^2+ab+b^2}{3}-\frac{(a+b)^2}{4}=\frac{4(a^2+ab+b^2)-3(a+b)^2}{12}=\frac{a^2-2ab+b^2}{12}=\boxed{\ \frac{(b-a)^2}{12}\ }$$

**b)** $W$ es uniforme en el mismo $[a,b]$ e independiente de $V$, así que $\mu_W=\mu_V$ y $\sigma_W^2=\sigma_V^2$. Medias y varianzas de independientes se suman:
$$\mu_Y=\mu_V+\mu_W=\boxed{\ a+b\ }\qquad\qquad \sigma_Y^2=\sigma_V^2+\sigma_W^2=\boxed{\ \frac{(b-a)^2}{6}\ }$$
Covarianza, por bilinealidad y $\mathrm{Cov}(W,V)=0$ (independientes):
$$\mathrm{Cov}(Y,V)=\mathrm{Cov}(V+W,\,V)=\mathrm{Var}(V)+\mathrm{Cov}(W,V)=\sigma_V^2+0=\boxed{\ \frac{(b-a)^2}{12}\ }$$
Y el coeficiente de correlación:
$$\rho_{Y,V}=\frac{\mathrm{Cov}(Y,V)}{\sigma_Y\,\sigma_V}=\frac{(b-a)^2/12}{\sqrt{(b-a)^2/6}\cdot\sqrt{(b-a)^2/12}}=\frac{1/12}{\sqrt{1/72}}=\boxed{\ \frac{1}{\sqrt2}\approx0{,}707\ }$$

Notar que $\rho_{Y,V}$ **no depende** de $a$ ni $b$: es puramente el efecto de "sumarle a $V$ un ruido independiente de la misma varianza".

###### **Verificación**
$|\rho_{Y,V}|=\tfrac1{\sqrt2}\approx0{,}707<1$ ✓ (tiene sentido: $Y$ no es función determinística de $V$, así que $\rho<1$ estrictamente, pero comparten la mitad de la "energía" de $Y$). *(verificado numéricamente: con $a=-3,b=5$, Monte Carlo con $4\cdot10^6$ muestras da $\mu_V\approx1{,}00$, $E[V^2]\approx6{,}33$, $\sigma_V^2\approx5{,}33$, $\mu_Y\approx2{,}00$, $\sigma_Y^2\approx10{,}66$, $\mathrm{Cov}(Y,V)\approx5{,}33$ y $\rho_{Y,V}\approx0{,}707$ — todos coinciden con las fórmulas.)*

> [!info] Conexión
> Es exactamente el mismo resultado del Ejercicio 2 en [[PROCESAMIENTO DE SEÑALES - Cap 7 en profundidad]] (Parte 5), ahí con $V$ y $W$ exponenciales en vez de uniformes: $\rho_{Y,V}=1/\sqrt2$ de nuevo. La forma de la distribución no importa — alcanza con que $V$ y $W$ tengan la misma varianza y sean independientes para que "una variable más un ruido independiente igual de disperso" correlacione siempre a $1/\sqrt2$.

---

## Ejercicio 3 — Ortogonalidad vs. correlación en una combinación afín de gaussiana

> [!quote] Enunciado
> 3. Supongamos que $X=2+V$ e $Y=2-V$, cuando $V$ es una variable aleatoria que se distribuye de manera normal con media $\mu =0$ y varianza $\sigma^2 =4$.
> a) Determine la correlación entre $X$ e $Y$.
> b) Son $X$ e $Y$ ortogonales?
> c) Cual es la covarianza?
> d) Cual es el coeficiente de correlación?
> e) Están no correlacionadas?

###### **Idea**
Ojo con el vocabulario: acá "correlación" (a) es el momento crudo $E[XY]$, distinto de "coeficiente de correlación" (d), que se pregunta aparte. Con $E[V]=0$ todo sale de expandir productos y usar $E[V^2]=\sigma_V^2=4$.

###### **Resolución**
Medias: $E[X]=2+E[V]=2$, $E[Y]=2-E[V]=2$.

**a) Correlación $E[XY]$.**
$$E[XY]=E\big[(2+V)(2-V)\big]=E[4-V^2]=4-E[V^2]=4-\sigma_V^2=4-4$$
$$\boxed{\ E[XY]=0\ }$$

**b) ¿Ortogonales?** Ortogonalidad es exactamente $E[XY]=0$, que ya obtuvimos:
$$\boxed{\ \text{Sí, }X\text{ e }Y\text{ son ortogonales}\ }$$

**c) Covarianza.** Las constantes $+2$ no afectan la covarianza:
$$\sigma_{XY}=\mathrm{Cov}(2+V,\,2-V)=\mathrm{Cov}(V,-V)=-\mathrm{Var}(V)=\boxed{\ -4\ }$$

**d) Coeficiente de correlación.** Ni la constante ni el signo cambian una varianza: $\sigma_X^2=\mathrm{Var}(V)=4$, $\sigma_Y^2=\mathrm{Var}(-V)=\mathrm{Var}(V)=4$, así que $\sigma_X=\sigma_Y=2$:
$$\rho_{XY}=\frac{\sigma_{XY}}{\sigma_X\sigma_Y}=\frac{-4}{2\cdot2}=\boxed{\ -1\ }$$

**e) ¿No correlacionadas?** No correlacionadas significa $\rho_{XY}=0$ (equivalentemente $\sigma_{XY}=0$). Acá $\rho_{XY}=-1\neq0$:
$$\boxed{\ \text{No: están perfectamente correlacionadas (en sentido negativo)}\ }$$

###### **Verificación**
$|\rho_{XY}|=1\le1$ ✓, y es el caso límite de Cauchy-Schwarz: $Y=4-X$ es función afín exacta de $X$ (pendiente $-1$), así que $\rho=-1$ es forzoso. *(verificado numéricamente: Monte Carlo con $4\cdot10^6$ muestras de $V\sim\mathcal N(0,4)$ da $E[XY]\approx0{,}0006\approx0$, $\sigma_{XY}\approx-3{,}999$ y $\rho_{XY}\approx-0{,}99999997$.)*

> [!info] Conexión
> Es el espejo del Ejercicio 3 de [[PROCESAMIENTO DE SEÑALES - Cap 7 en profundidad]] (Parte 5): ahí $\rho=1$ pero $X,Y$ **no** son ortogonales; acá $E[XY]=0$ (ortogonales) pero $\rho=-1$ (correlación perfecta). Los dos ejemplos juntos dejan claro que ortogonalidad (sobre las variables crudas) y correlación (sobre las variables centradas) son nociones completamente independientes entre sí — una no implica nada sobre la otra.

---

## Ejercicio 4 — Covarianza y $\rho$ de combinaciones de variables no correlacionadas

> [!quote] Enunciado
> 4. Supongamos $X=Z+V;$ $Y = \beta Z+W$ donde las variables aleatorias $Z,V$ y $W$ tienen sus respectivas medias: $\mu_V; \mu_W; \mu_Z$, varianzas $\sigma^2_V; \sigma^2_W; \sigma^2_Z$ y son mutuamente no correlacionadas (tienen covarianza nula), además el valor $\beta$ es un factor de escala.
>
> a) Determine el valor de covarianza $\sigma_{XY}$ y el coeficiente de correlación $\rho_{XY}= \frac{\sigma_XY}{(\sigma_X \sigma_Y)}$ en términos de las cantidades especificadas anteriormente.
> b) Asumiendo que $\sigma^2_V = \sigma^2_W = \sigma^2_Z$ de una respuesta sobre el coeficiente de correlación respecto del punto a).

> [!warning] Nota sobre el enunciado
> El problema original (P7.6) plantea la parte b) asumiendo solo $\sigma_V^2=\sigma_W^2=\sigma^2$ (una constante común a $V$ y $W$, dejando $\sigma_Z^2$ libre) y pide explícitamente revisar los casos extremos de **$\sigma^2$ y de $\beta$**. La guía en cambio iguala las **tres** varianzas, $\sigma_V^2=\sigma_W^2=\sigma_Z^2$: con esa igualdad $\sigma^2$ se cancela por completo de $\rho_{XY}$ (queda función solo de $\beta$), y el chequeo de extremos de $\sigma^2$ que pide el libro deja de tener sentido. Resolvemos primero con la hipótesis del libro, más general e informativa, y al final mostramos que la de la guía es el caso particular $\sigma_Z^2=\sigma^2$. (De paso, el $\rho_{XY}=\sigma_{XY}/(\sigma_X\sigma_Y)$ del enunciado tiene un typo de tipeo, `\sigma_XY` en vez de $\sigma_{XY}$; es solo de formato, no afecta la resolución.)

###### **Idea**
Por bilinealidad de la covarianza, y como $Z,V,W$ son no correlacionadas de a pares, en $\mathrm{Cov}(X,Y)$ sobrevive únicamente el término que involucra la variable compartida $Z$.

###### **Resolución**
**a)** Covarianza:
$$\sigma_{XY}=\mathrm{Cov}(Z+V,\ \beta Z+W)=\beta\,\mathrm{Cov}(Z,Z)+\mathrm{Cov}(Z,W)+\beta\,\mathrm{Cov}(V,Z)+\mathrm{Cov}(V,W)=\beta\sigma_Z^2+0+0+0$$
$$\boxed{\ \sigma_{XY}=\beta\,\sigma_Z^2\ }$$
Varianzas (de nuevo, covarianzas cruzadas nulas):
$$\sigma_X^2=\mathrm{Var}(Z+V)=\sigma_Z^2+\sigma_V^2\qquad\qquad \sigma_Y^2=\mathrm{Var}(\beta Z+W)=\beta^2\sigma_Z^2+\sigma_W^2$$
$$\boxed{\ \rho_{XY}=\dfrac{\beta\,\sigma_Z^2}{\sqrt{(\sigma_Z^2+\sigma_V^2)(\beta^2\sigma_Z^2+\sigma_W^2)}}\ }$$

**b)** Con la hipótesis del libro, $\sigma_V^2=\sigma_W^2=\sigma^2$ (y $\sigma_Z^2$ libre):
$$\boxed{\ \rho_{XY}=\dfrac{\beta\,\sigma_Z^2}{\sqrt{(\sigma_Z^2+\sigma^2)(\beta^2\sigma_Z^2+\sigma^2)}}\ }$$
Casos extremos que pide el enunciado:
- **$\sigma^2\to0$** (sin ruido en $V,W$): $\rho_{XY}\to \dfrac{\beta\sigma_Z^2}{\sqrt{\sigma_Z^2\cdot\beta^2\sigma_Z^2}}=\dfrac{\beta}{|\beta|}=\mathrm{sign}(\beta)$. Correlación perfecta (con el signo de $\beta$): sin ruido, $X=Z$ e $Y=\beta Z$ son la misma variable, solo reescalada.
- **$\sigma^2\to\infty$** (el ruido domina): $\rho_{XY}\to0$. El ruido ahoga cualquier parte común entre $X$ e $Y$.
- **$\beta\to0$:** $\rho_{XY}\to0$. $Y\to W$ deja de depender de $Z$, no queda nada en común con $X$.
- **$\beta\to\infty$** (con $\beta>0$): $\rho_{XY}\to \dfrac{\sigma_Z}{\sqrt{\sigma_Z^2+\sigma^2}}$, que es exactamente $\rho_{XZ}$, la correlación entre $X$ y $Z$ solas. Tiene sentido: si $\beta$ es enorme, $Y\approx\beta Z$ queda dominada por $Z$, así que correlacionar $Y$ con $X$ es, en el límite, correlacionar $Z$ con $X$.

Si además se impone la hipótesis literal de la guía, $\sigma_Z^2=\sigma_V^2=\sigma_W^2=\sigma^2$, la fórmula anterior se simplifica —$\sigma^2$ se cancela entero—:
$$\rho_{XY}\Big|_{\sigma_Z^2=\sigma^2}=\boxed{\ \dfrac{\beta}{\sqrt{2(\beta^2+1)}}\ }$$
que ya no depende de $\sigma^2$ en absoluto (consistente con que la guía no pida revisar sus extremos).

###### **Verificación**
$|\rho_{XY}|\le1$ por Cauchy-Schwarz en todos los casos (se ve en los límites: nunca superan $\pm1$). *(verificado numéricamente: con $\sigma_Z^2=2{,}5$, $\sigma^2=1{,}7$, $\beta=-3$, la fórmula da $\rho_{XY}=-0{,}7439$ y Monte Carlo con $4\cdot10^6$ muestras gaussianas da $-0{,}7440$; los límites de $\sigma^2\to0,\infty$ y $\beta\to0,\infty$ se chequearon simbólicamente con `sympy` y coinciden con lo de arriba; la simplificación de la guía, $\beta/\sqrt{2(\beta^2+1)}$, también se confirmó con `sympy.simplify` a partir de la fórmula general.)*

---

## Ejercicio 5 — Covarianza de combinaciones afines y su densidad conjunta

> [!quote] Enunciado
> 5. Las variables aleatorias $X$ e $Y$ tienen:
> $$E(X)=1\ \  ;\ E(Y)=2\ \ ; \ E(X^2)=9\ \ ; \ E(XY)=-4\ \ ; \ E(Y^2)=7$$
> a) Calcule la covarianza $\sigma_{ZW}$ de las variables aleatorias:
> $$Z=2X-Y+5, \ \ \ W=X+ \frac{1}{2}Y-1$$
> b) Si $X$ e $Y$ se distribuyen con una distribución Gaussiana bivariada, cual es la densidad conjunta de $Z$ y $W$? (Aprovecha el hecho de que las combinaciones afines de variables aleatorias Gaussianas bivariadas son una Gaussiana bivariada.

> [!warning] Nota sobre el enunciado
> La guía dice $E(X)=1$, pero el problema original (P7.4) dice $E(X)=-1$. Con $+1$ quedaría $\sigma_{XY}=-6$ y $\rho_{XY}=-6/\sqrt{24}\approx-1{,}22$: un coeficiente de correlación fuera de $[-1,1]$, así que esos momentos no pueden ser de ningún par de variables. Resolvemos con $E(X)=-1$.

###### **Idea**
Todo sale de pasar de momentos crudos a momentos centrados ($\sigma_X^2$, $\sigma_Y^2$, $\sigma_{XY}$) y usar bilinealidad de la covarianza. Las constantes $+5$ y $-1$ no afectan covarianzas, solo medias.

###### **Resolución**
**Momentos centrados de $(X,Y)$.**
$$\sigma_X^2=E(X^2)-\mu_X^2=9-1=8,\qquad \sigma_Y^2=7-4=3,\qquad \sigma_{XY}=E(XY)-\mu_X\mu_Y=-4-(-1)(2)=-2$$

**a)** Por bilinealidad (las constantes se van):
$$\sigma_{ZW}=\text{Cov}(2X-Y,\ X+\tfrac12Y)=2\sigma_X^2+2\cdot\tfrac12\sigma_{XY}-\sigma_{XY}-\tfrac12\sigma_Y^2=16-2+2-1{,}5$$
$$\boxed{\ \sigma_{ZW}=14{,}5\ }$$

**b)** $(Z,W)$ es gaussiana bivariada (combinación afín de una gaussiana bivariada); alcanza con medias y covarianzas:
$\mu_Z=2(-1)-2+5=1$, $\mu_W=-1+1-1=-1$, $\sigma_Z^2=4\cdot8+3-4(-2)=43$, $\sigma_W^2=8+\tfrac34+(-2)=6{,}75$.
El determinante de la matriz de covarianza es $43\cdot6{,}75-14{,}5^2=80$, así que
$$\boxed{\ f_{Z,W}(z,w)=\frac{1}{2\pi\sqrt{80}}\exp\!\left(-\frac{6{,}75\,(z-1)^2-29\,(z-1)(w+1)+43\,(w+1)^2}{160}\right)\ }$$
con $\rho_{ZW}=14{,}5/\sqrt{290{,}25}\approx0{,}851$.

###### **Verificación**
$|\rho_{XY}|=2/\sqrt{24}\approx0{,}41<1$ ✓ y $|\rho_{ZW}|<1$ ✓. *(verificado numéricamente: Monte Carlo con $2\cdot10^6$ muestras da $\sigma_{ZW}\approx14{,}49$, $\sigma_Z^2\approx42{,}93$, $\sigma_W^2\approx6{,}75$.)*

---

## Ejercicio 6 — Bayes sobre una tabla conjunta y probabilidad de error

> [!quote] Enunciado
> 6. Un sistema de comunicación transmite señales etiquetadas 1, 2 y 3. La probabilidad de que se envíe el símbolo $j$ y se reciba el símbolo $k$ está listada en la siguiente tabla para cada par $(j,k)$ de símbolo enviado y recibido. Por ejemplo, la probabilidad de que se envíe un 3 y se reciba un 2 es 0.21.
>
> |             | $k$ Recibido | 1    | 2    | 3    |
> | ----------- | ------------ | ---- | ---- | ---- |
> | $j$ enviado | -            | -    | -    | -    |
> | 1           | -            | 0.05 | 0.13 | 0.12 |
> | 2           | -            | 0.10 | 0.08 | 0.07 |
> | 3           | -            | 0.09 | 0.21 | 0.15 |
>
> Calcule la probabilidad de que se haya enviado el símbolo $k$ dado que se recibió el símbolo $k$, para $k=1,2,3$. Además, calcule la probabilidad de error de transmisión de este sistema. Un error de transmisión se define como la recepción de cualquier símbolo distinto del transmitido.

###### **Idea**
La tabla ya da las probabilidades conjuntas $P(j,k)$ (los 9 valores suman 1, así que es una tabla de probabilidad conjunta completa, no condicional). Bayes es entonces directo: marginar por columnas da $P(k\text{ recibido})$, y dividir la entrada diagonal por esa marginal da $P(\text{enviado}=k\mid\text{recibido}=k)$.

###### **Resolución**
**Marginales de lo recibido** (sumar cada columna):
$$P(k{=}1)=0{,}05+0{,}10+0{,}09=0{,}24\qquad P(k{=}2)=0{,}13+0{,}08+0{,}21=0{,}42\qquad P(k{=}3)=0{,}12+0{,}07+0{,}15=0{,}34$$
(suman $1$ ✓, como debe ser.)

**Bayes**, $P(j{=}k\mid k\text{ recibido})=\dfrac{P(j{=}k,\,k)}{P(k)}$:
$$P(1\mid1)=\frac{0{,}05}{0{,}24}=\frac{5}{24}\approx0{,}2083\qquad P(2\mid2)=\frac{0{,}08}{0{,}42}=\frac{4}{21}\approx0{,}1905\qquad P(3\mid3)=\frac{0{,}15}{0{,}34}=\frac{15}{34}\approx0{,}4412$$
$$\boxed{\ P(1\mid1)\approx0{,}2083\ ,\quad P(2\mid2)\approx0{,}1905\ ,\quad P(3\mid3)\approx0{,}4412\ }$$

**Probabilidad de error.** El complemento de "se recibe lo que se envió" es sumar la diagonal de la tabla conjunta:
$$P(\text{acierto})=P(1,1)+P(2,2)+P(3,3)=0{,}05+0{,}08+0{,}15=0{,}28$$
$$\boxed{\ P(\text{error})=1-P(\text{acierto})=1-0{,}28=0{,}72\ }$$

###### **Verificación**
Todas las probabilidades caen en $[0,1]$ ✓, las marginales de $k$ suman $1$ ✓, y las tres probabilidades condicionales son consistentes con ser una partición de cada columna (p. ej. para $k=2$: $P(1\mid2)+P(2\mid2)+P(3\mid2)=\frac{0{,}13+0{,}08+0{,}21}{0{,}42}=1$). *(verificado con `py`: aritmética exacta sobre la tabla — sumas de fila/columna y traza — reproduce los mismos valores.)* Vale la pena notar lo alta que da la probabilidad de error ($0{,}72$): el canal está lejos de ser confiable, sobre todo porque el símbolo 2 recibido es más probable que haya sido un 3 enviado ($0{,}21$) que un 2 enviado ($0{,}08$).

---
