Solucionario de los Ejercicios Propuestos del capítulo 13 de [[PROCESAMIENTO DE SEÑALES]]. La teoría con demostraciones está en [[PROCESAMIENTO DE SEÑALES - Cap 13 en profundidad]].

# Detección De Señales — Solucionario

Todo el capítulo se reduce a dos herramientas: el estadístico $g=\sum r[n]s[n]$ (y su umbral $\gamma=\sigma^2\ln(p_0/p_1)+E/2$) para "¿hay señal o no?", y su generalización a "¿cuál de las $M$ señales?" con un filtro adaptado por candidato. Los cinco ejercicios recorren variaciones de esa misma idea: mediciones múltiples de una variable, dos receptores que comparar, un filtro adaptado concreto, un receptor de correlación con energía fija, y un canal con ruido tanto a la entrada como a la salida.

###### **Índice**
| Ej. | Qué se practica | Problema del libro |
|---|---|---|
| 1 | Múltiples mediciones del Ejemplo 13.1: promediar vs. usar las $K$ mediciones óptimamente | P13.1 (+ Ejemplo 13.1) |
| 2 | Dos receptores para discriminar $s_1$ y $s_2$: filtro simple vs. filtro a la diferencia | P13.5 |
| 3 | Filtro adaptado y umbral para un pulso de dos muestras | P13.2 |
| 4 | Receptor de correlación: diseño óptimo de $c[n]$ a energía fija | P13.6 |
| 5 | Canal con memoria y ruido tanto a la entrada como a la salida | P13.3 |

---

## Ejercicio 1 — Múltiples mediciones en el Ejemplo 13.1: promediar vs. usar $K$ mediciones

> [!quote] Enunciado
> 1. Este problema se refiere al escenario descrito en el Ejemplo 13.1 del libro (dos densidades condicionales uniformes, con $P(H_0)=\tfrac34$ y $P(H_1)=\tfrac14$).
>
> a) Verifique la afirmación hecha en el ejemplo: que decidir óptimamente entre las dos hipótesis a partir del **promedio** de dos mediciones independientes de $X$ da la misma probabilidad de error que usar una sola medición.
> b) Para el caso de $K$ mediciones independientes de $X$, ¿cuál es la regla de decisión óptima, y cuál es la probabilidad de error asociada?
>
> *(Planteo del Ejemplo 13.1, necesario para resolver esto: $f_{X|H_0}(x)=\tfrac14$ para $|x|<2$ y $0$ fuera de ese rango; $f_{X|H_1}(x)=\tfrac12$ para $|x|<1$ y $0$ fuera; $P(H_0)=\tfrac34$, $P(H_1)=\tfrac14$. Con una sola medición $X$, la regla MAP resulta declarar siempre 'H_0' —porque $p_1f_{X|H_1}(x)=\tfrac18<p_0f_{X|H_0}(x)=\tfrac3{16}$ en todo $|x|<1$, y $f_{X|H_1}=0$ fuera de ahí—, con $P_e=P(H_1)=\tfrac14$. Con dos mediciones independientes usadas óptimamente (comparando las densidades conjuntas, no un resumen), sale $P_e=\tfrac3{16}$.)*

###### **Idea**
En a) hay que construir la densidad de $Y=\tfrac12(X_1+X_2)$ bajo cada hipótesis (convolución de dos uniformes, reescalada) y aplicar la regla MAP de una sola medición pero sobre $Y$. En b) conviene no pasar por ningún resumen: con $K$ mediciones, la densidad conjunta bajo cada hipótesis es un producto de uniformes, así que es constante dentro de su región de soporte; ahí la regla MAP se reduce a comparar dos números.

###### **Resolución**

**a) El promedio de dos mediciones no mejora nada.**

Si $X_1,X_2$ son iid $U(-a,a)$, su suma $S=X_1+X_2$ tiene densidad triangular en $(-2a,2a)$ con pico $1/(2a)$ en el origen (convolución de dos rectángulos iguales). Escalando $Y=S/2$:
$$f_Y(y)=\frac1a\left(1-\frac{|y|}{a}\right),\qquad |y|<a$$
también triangular, con el mismo soporte que $X$ y pico $1/a$ en $y=0$. Aplicando esto con $a=2$ bajo $H_0$ y $a=1$ bajo $H_1$:
$$f_{Y|H_0}(y)=\frac12\left(1-\frac{|y|}2\right),\ |y|<2\ ;\qquad f_{Y|H_1}(y)=1-|y|,\ |y|<1$$

La regla MAP para una medición de $Y$ compara $p_1f_{Y|H_1}(y)$ contra $p_0f_{Y|H_0}(y)$. Fuera de $|y|<1$ la densidad de $H_1$ es cero, así que ahí se declara `H0` directo. Dentro de $|y|<1$:
$$p_1f_{Y|H_1}(y)=\frac14(1-|y|)\ ,\qquad p_0f_{Y|H_0}(y)=\frac34\cdot\frac12\left(1-\frac{|y|}2\right)=\frac38\left(1-\frac{|y|}2\right)$$
Restando (con $u=|y|\in[0,1)$):
$$p_1f_{Y|H_1}-p_0f_{Y|H_0}=\frac14(1-u)-\frac38\left(1-\frac u2\right)=-\frac{2+u}{16}<0\quad\text{para todo }u\geq0$$
Es decir, **incluso en $y=0$** (el punto más favorable a $H_1$, donde ambas densidades son máximas) la desigualdad favorece a $H_0$: $p_1f_{Y|H_1}(0)=\tfrac14$ mientras que $p_0f_{Y|H_0}(0)=\tfrac38$. Entonces la regla óptima basada en $Y$ es **declarar `H0' siempre**, sin importar el valor observado de $y$. Eso da exactamente la misma regla —y por lo tanto la misma probabilidad de error— que usar una sola medición:
$$\boxed{\ P_e(\text{promedio de 2})=P(H_1)=\frac14\ }$$
igual que con una sola medición. Esto confirma la afirmación del libro: promediar **no** es la forma óptima de aprovechar las dos mediciones (la forma óptima, usando la densidad conjunta sin resumir, da $P_e=\tfrac3{16}<\tfrac14$, como calcula el Ejemplo 13.1).

**b) Regla óptima y $P_e$ con $K$ mediciones.**

Con $K$ mediciones $x_1,\dots,x_K$ iid, las densidades conjuntas son productos (por independencia) y por lo tanto **constantes** dentro de su región de soporte:
$$f_{\mathbf X|H_0}(\mathbf x)=\left(\frac14\right)^K\ \text{si todo }|x_i|<2\ ;\qquad f_{\mathbf X|H_1}(\mathbf x)=\left(\frac12\right)^K\ \text{si todo }|x_i|<1$$

Si algún $|x_i|\geq1$ (pero todos dentro de $|x_i|<2$, la única región donde hay datos), $f_{\mathbf X|H_1}=0<f_{\mathbf X|H_0}$: se declara `H0'. Si **todos** los $|x_i|<1$, comparamos los dos números constantes:
$$p_1\left(\frac12\right)^K\ \underset{H_0}{\overset{H_1}{\gtrless}}\ p_0\left(\frac14\right)^K\quad\Longleftrightarrow\quad 2^K\ \underset{H_0}{\overset{H_1}{\gtrless}}\ \frac{p_0}{p_1}=3$$
(dividiendo ambos lados por $\left(\tfrac14\right)^K p_1$). Como $2^K$ es creciente en $K$ y $2^1=2<3<4=2^2$, el resultado depende de si $K=1$ o $K\geq2$:

- **$K=1$:** $2^1<3$, así que incluso dentro de $|x_1|<1$ se declara `H0'. Coincide con el caso base: **declarar `H0' siempre**, $P_e=\tfrac14$.
- **$K\geq2$:** $2^K>3$, así que dentro de la región $|x_i|<1\ \forall i$ se declara `H1'; fuera de ella (pero dentro del soporte de $H_0$), `H0'. La regla óptima es
$$\boxed{\ \text{declarar `H1' si } |x_i|<1\ \ \forall i=1,\dots,K\ ;\ \ \text{si no, `H0'}\ }$$

Para esta regla (válida para $K\geq2$): $P_{FA}=P(\text{todo }|X_i|<1\mid H_0)=\left(\tfrac12\right)^K$ (cada $X_i\sim U(-2,2)$ cae en $(-1,1)$ con probabilidad $\tfrac12$), y $P_M=0$ (bajo $H_1$, cada $X_i\sim U(-1,1)$ ya está siempre en $(-1,1)$). Entonces
$$\boxed{\ P_e(K)=P(H_0)\,P_{FA}=\frac34\left(\frac12\right)^K=3\cdot2^{-(K+2)}\ ,\quad K\geq2\ }$$
y $P_e(K)=\tfrac14$ para $K=1$. Con $K=2$: $P_e=3\cdot2^{-4}=\tfrac3{16}$, exactamente el valor del Ejemplo 13.1.

###### **Verificación**
Todas las $P_e\in[0,1]$ y decrecen con $K$ (más mediciones, mejor, siempre que se usen óptimamente) ✓. *(Verificado numéricamente con Monte Carlo, $2\cdot10^6$ muestras por $K$: la regla-región da $P_e\approx0{,}3750,\ 0{,}1876,\ 0{,}0937,\ 0{,}0467,\ 0{,}0235$ para $K=1,\dots,5$ frente a la fórmula $3\cdot2^{-(K+2)}=0{,}3750,\ 0{,}1875,\ 0{,}0938,\ 0{,}0469,\ 0{,}0234$; y para $K=1$ la regla "siempre H0" da $P_e=0{,}25<0{,}375$, confirmando que es la que conviene en ese caso.)*

> [!warning] Ojo
> Para $K=1$ la fórmula $3\cdot2^{-(K+2)}$ da $\tfrac38=0{,}375$, que **no** es la $P_e$ óptima: es la $P_e$ de la regla-región aplicada (subóptimamente) a una sola medición. La regla óptima cambia de forma en $K=1$ (siempre `H0') a $K\geq2$ (regla-región), justo donde $2^K$ cruza $p_0/p_1=3$. No hay una fórmula única válida para todo $K$: son dos regímenes.

---

## Ejercicio 2 — Dos receptores para discriminar $s_1$ y $s_2$: filtro simple vs. filtro a la diferencia

> [!quote] Enunciado
> 2. Considere un sistema de comunicación de tiempo discreto en el que se ha transmitido una de dos señales determinísticas por un canal ruidoso. La señal recibida $r[n]$ está dada por
> $$r[n]=s_i[n]+w[n], \qquad i=1 \text{ o } i=2$$
> El proceso $w[n]$ es ruido gaussiano i.i.d. de media nula y varianza $\sigma_w^2=\tfrac12$. Las probabilidades a priori de los dos pulsos $s_1[n]$ y $s_2[n]$ son ambas $\tfrac12$. Los pulsos tienen las siguientes propiedades:
> $$\sum_{n=-\infty}^{\infty}s_1^2[n]=\sum_{n=-\infty}^{\infty}s_2^2[n]=1 \qquad\text{y}\qquad \sum_{n=-\infty}^{\infty}s_1[n]s_2[n]=\frac12$$
>
> Considere los dos receptores propuestos que se muestran en la figura.
>
> ![[ej-p13-2.png]]
>
> a) En un mismo gráfico, dibuje la PDF de $G_1$ dado que $i=1$ y la PDF de $G_1$ dado que $i=2$, cuando se usa el esquema de detección 1. En un segundo gráfico, dibuje la PDF de $G_2$ dado que $i=1$ y dado que $i=2$, cuando se usa el esquema 2.
> b) Determine el valor de $\lambda_1$ que minimiza la probabilidad de error, y el valor de $\lambda_2$ que minimiza la probabilidad de error.
> c) Elija la afirmación correcta y explique clara y sucintamente su razonamiento:
> i) El esquema 1 logra menor probabilidad de error que el esquema 2.
> ii) El esquema 2 logra menor probabilidad de error que el esquema 1.
> iii) Los dos esquemas logran la misma probabilidad de error.

###### **Idea**
Ambos $G_1=\langle r,s_1\rangle$ y $G_2=\langle r,s_1-s_2\rangle$ son combinaciones lineales de gaussianas, así que son gaussianos: alcanza con calcular media y varianza bajo cada hipótesis usando bilinealidad del producto interno. $G_2$ es exactamente el estadístico óptimo del capítulo para discriminación binaria ($g=\sum r[n](s_1[n]-s_0[n])$), así que ya sabemos, sin calcular nada más, que el esquema 2 no puede ser peor que el esquema 1.

###### **Resolución**

**Medias y varianzas.** Con $\|s_1\|^2=\|s_2\|^2=1$ y $\langle s_1,s_2\rangle=\tfrac12$, y usando que $g_1[0]=\langle r,s_1\rangle$, $g_2[0]=\langle r,s_1-s_2\rangle$:

$$E(G_1|i{=}1)=\langle s_1,s_1\rangle=1\ ,\qquad E(G_1|i{=}2)=\langle s_2,s_1\rangle=\frac12$$
$$E(G_2|i{=}1)=\langle s_1,s_1-s_2\rangle=1-\frac12=\frac12\ ,\qquad E(G_2|i{=}2)=\langle s_2,s_1-s_2\rangle=\frac12-1=-\frac12$$

Para las varianzas, el ruido que entra a cada filtro es el mismo $w[n]$ proyectado sobre $s_1$ (esquema 1) o sobre $s_1-s_2$ (esquema 2); la varianza no depende de $i$ porque $w$ no depende de la hipótesis:
$$\text{Var}(G_1)=\sigma_w^2\|s_1\|^2=\frac12\cdot1=\frac12\ ,\qquad \text{Var}(G_2)=\sigma_w^2\|s_1-s_2\|^2=\frac12(1-2\cdot\tfrac12+1)=\frac12$$
(las dos varianzas dan iguales: $\|s_1-s_2\|^2=\|s_1\|^2-2\langle s_1,s_2\rangle+\|s_2\|^2=1-1+1=1$).

Entonces $G_1|i{=}1\sim\mathcal N(1,\tfrac12)$, $G_1|i{=}2\sim\mathcal N(\tfrac12,\tfrac12)$, $G_2|i{=}1\sim\mathcal N(\tfrac12,\tfrac12)$, $G_2|i{=}2\sim\mathcal N(-\tfrac12,\tfrac12)$.

**a)** Las cuatro gaussianas (mismo $\sigma=\sqrt{1/2}\approx0{,}707$, distintas medias) se ven en la figura:

![[sol13-ej02-pdfs-g1-g2.svg]]
*Izquierda: PDFs de $G_1$ (separación de medias $0{,}5$). Derecha: PDFs de $G_2$ (separación de medias $1{,}0$, el doble) — se solapan visiblemente menos.*

**b)** Con priors iguales y varianzas iguales bajo las dos hipótesis en cada esquema, el umbral óptimo es el punto medio de las medias:
$$\boxed{\ \lambda_1=\frac{1+\tfrac12}2=0{,}75\ }\ ,\qquad \boxed{\ \lambda_2=\frac{\tfrac12+(-\tfrac12)}2=0\ }$$

**c)** Para una decisión gaussiana binaria con varianzas iguales $\sigma^2$ y separación de medias $d$, con priors iguales, $P_e=Q\!\left(\dfrac{d}{2\sigma}\right)$. Acá $\sigma=\sqrt{1/2}$ en ambos esquemas, pero $d_1=0{,}5$ y $d_2=1{,}0=2d_1$. Como $Q(\cdot)$ es decreciente,
$$P_{e,1}=Q\!\left(\frac{0{,}5}{2\sqrt{0{,}5}}\right)=Q(0{,}3536)\approx0{,}3618\ >\ P_{e,2}=Q\!\left(\frac{1{,}0}{2\sqrt{0{,}5}}\right)=Q(0{,}7071)\approx0{,}2398$$
$$\boxed{\ \text{(ii) El esquema 2 logra menor probabilidad de error.}\ }$$
Tiene sentido: $G_2$ es el filtro adaptado a la **diferencia** $s_1-s_2$, que es exactamente el estadístico óptimo que deriva el capítulo para discriminación binaria de dos señales con energía y prior iguales; $G_1$ solo usa el filtro adaptado a $s_1$, ignorando la correlación con $s_2$, y por eso es estrictamente subóptimo salvo que $s_1\perp s_2$.

###### **Verificación**
Ambas varianzas dan efectivamente iguales entre sí ($\text{Var}(G_1)=\text{Var}(G_2)=\tfrac12$) ✓, y $d_2/d_1=2$ exactamente (relación limpia que viene de $\langle s_1,s_2\rangle=\tfrac12\|s_1\|\|s_2\|$, es decir $\rho_{s_1s_2}=0{,}5$). *(Verificado numéricamente: con $s_1=(1,0)$, $s_2=(\tfrac12,\tfrac{\sqrt3}2)$ —que cumplen las tres condiciones dadas— y $2\cdot10^6$ realizaciones de $w\sim\mathcal N(0,\tfrac12 I)$, Monte Carlo da $P_{e,1}\approx0{,}3618$ y $P_{e,2}\approx0{,}2397$, igual que la fórmula cerrada.)*

> [!info] Conexión
> $G_2$ es un caso particular de $g=\sum_n r[n](s_1[n]-s_0[n])$, la sección "El caso binario: on-off contra antipodal" de [[PROCESAMIENTO DE SEÑALES]] (Cap. 13). Que el esquema con el filtro a la diferencia gane es el mismo fenómeno que explica por qué antipodal ($s_1=-s_0$) le gana a on-off ($s_0=0$): lo que importa para discriminar es **en qué se diferencian** las señales, no cada una por separado.

---

## Ejercicio 3 — Filtro adaptado y umbral para un pulso de dos muestras

> [!quote] Enunciado
> 3. Considere el siguiente problema de detección, basado en mediciones de una señal recibida $r[n]$ bajo dos hipótesis posibles, $H_0$ y $H_1$:
> $$H_0:\ r[n]=-s[n]+v[n], \qquad H_1:\ r[n]=s[n]+v[n]$$
> donde $s[n]$ es un pulso conocido y las muestras de ruido $v[n]$ son variables aleatorias gaussianas independientes de media nula y varianza $\sigma^2$. En el receptor decidimos usar la estrategia de la figura.
>
> ![[ej-p13-3.png]]
>
> Acá $h[\cdot]$ es la respuesta al impulso de un sistema LTI y $\gamma$ es una constante. Suponga que el pulso $s[n]$ está dado por $s[n]=2\delta[n]-\delta[n-1]$.
>
> Determine la respuesta al impulso $h[n]$ y el valor de $\gamma$ que minimizan la probabilidad de error, primero para el caso en que $H_0$ y $H_1$ son igualmente probables a priori, y luego para el caso en que $H_1$ es el doble de probable que $H_0$. En cada caso, calcule la probabilidad de error correspondiente, expresando su respuesta en términos de la función $Q(\cdot)$ estándar,
> $$Q(x)=\frac{1}{\sqrt{2\pi}}\int_x^{\infty}e^{-z^2/2}dz$$

###### **Idea**
$H_0:r=-s+v$ y $H_1:r=s+v$ es el caso **antipodal** ($s_1=-s_0=s$). El filtro óptimo es el adaptado a la diferencia $s_1-s_0=2s$, que apunta en la misma dirección que $s$, así que alcanza con adaptar a $s$. Lo que **no** se puede copiar del caso on-off es el umbral: acá las dos medias del estadístico son $\pm E$ (simétricas respecto de $0$), no $0$ y $E$.

###### **Resolución**

**Energía.** $s[n]=2\delta[n]-\delta[n-1]$, es decir $s[0]=2,\ s[1]=-1$:
$$E=\sum_n s^2[n]=2^2+(-1)^2=5$$

**Filtro adaptado.** $h[n]=s[-n]$: como $s[0]=2$ y $s[1]=-1$, resulta $h[0]=2$ y $h[-1]=-1$:
$$\boxed{\ h[n]=2\delta[n]-\delta[n+1]\ }\qquad\text{(es decir, } h[-1]=-1,\ h[0]=2\text{)}$$
Muestreando en $n=0$: $g[0]=h[0]r[0]+h[-1]r[1]=2r[0]-r[1]=\sum_n r[n]s[n]$. (Es el filtro adaptado no causal que pide la figura al muestrear en $n=0$; una versión causal equivalente es $h_c[n]=-\delta[n]+2\delta[n-1]$ muestreada en $n=1$.)

**Distribución del estadístico.** Con $G=\sum_n r[n]s[n]$:
- bajo $H_1$: $G=\sum_n(s[n]+v[n])s[n]=E+\sum_n v[n]s[n]$, o sea $G\sim\mathcal N(E,\ \sigma^2E)=\mathcal N(5,\ 5\sigma^2)$;
- bajo $H_0$: $G=-E+\sum_n v[n]s[n]$, o sea $G\sim\mathcal N(-E,\ \sigma^2E)=\mathcal N(-5,\ 5\sigma^2)$.

**Umbral MAP.** Se declara $H_1$ si $p_1f_{G|H_1}(g)>p_0f_{G|H_0}(g)$. Tomando logaritmo del cociente de las dos gaussianas (misma varianza):
$$\ln\frac{f_{G|H_1}(g)}{f_{G|H_0}(g)}=\frac{(g+E)^2-(g-E)^2}{2\sigma^2E}=\frac{4gE}{2\sigma^2E}=\frac{2g}{\sigma^2}\ \underset{H_0}{\overset{H_1}{\gtrless}}\ \ln\frac{p_0}{p_1}
\quad\Longrightarrow\quad g\ \underset{H_0}{\overset{H_1}{\gtrless}}\ \gamma=\frac{\sigma^2}{2}\ln\frac{p_0}{p_1}$$
Las probabilidades condicionales de error, con $\sigma_G=\sigma\sqrt E$:
$$P_{FA}=P(G>\gamma\mid H_0)=Q\!\left(\frac{\gamma+E}{\sigma\sqrt E}\right),\qquad P_M=P(G<\gamma\mid H_1)=Q\!\left(\frac{E-\gamma}{\sigma\sqrt E}\right)$$

**Caso equiprobable ($p_0=p_1=\tfrac12$).** $\ln(p_0/p_1)=0$, así que el umbral queda justo en el medio de $-5$ y $5$:
$$\boxed{\ \gamma=0\ }\ ,\qquad P_e=\tfrac12P_{FA}+\tfrac12P_M=Q\!\left(\frac{E}{\sigma\sqrt E}\right)\ \Longrightarrow\ \boxed{\ P_e=Q\!\left(\frac{\sqrt E}{\sigma}\right)=Q\!\left(\frac{\sqrt5}{\sigma}\right)\ }$$

**Caso $H_1$ el doble de probable ($p_0=\tfrac13,\ p_1=\tfrac23$).** El filtro es el mismo; solo se corre el umbral:
$$\gamma=\frac{\sigma^2}{2}\ln\frac{1/3}{2/3}\quad\Longrightarrow\quad\boxed{\ \gamma=-\frac{\sigma^2\ln2}{2}\ }$$
$$\boxed{\ P_e=\frac13\,Q\!\left(\frac{5-\tfrac12\sigma^2\ln2}{\sigma\sqrt5}\right)+\frac23\,Q\!\left(\frac{5+\tfrac12\sigma^2\ln2}{\sigma\sqrt5}\right)\ }$$

###### **Verificación**
Con $p_1>p_0$ el umbral baja de $0$ a un valor negativo, así que se declara $H_1$ más seguido, como corresponde a un prior más alto para $H_1$ ✓. La distancia entre las medias es $2E$ (el doble que en on-off con la misma energía), y por eso el argumento de $Q$ es $\sqrt E/\sigma$ en vez de $\sqrt E/(2\sigma)$: la señalización antipodal gana $6$ dB ✓. *(Verificado numéricamente con $\sigma=1{,}3$ y Monte Carlo de $4\cdot10^6$ símbolos: caso equiprobable, fórmula $P_e=0{,}04271$ vs. simulación $0{,}04268$; caso $p_1=2p_0$, $\gamma=-0{,}5857$, fórmula $P_e=0{,}03970$ vs. simulación $0{,}03960$.)*

> [!warning] Ojo
> La fórmula $\gamma=\sigma^2\ln(p_0/p_1)+E/2$ es la del caso **on-off** ($H_0$: solo ruido), donde las medias de $G$ son $0$ y $E$. Si se la usa acá, con $\sigma=1{,}3$ y priors iguales, el umbral queda en $2{,}5$ y la probabilidad de error sube a $\approx0{,}10$: más del doble que la óptima.

---

## Ejercicio 4 — Receptor de correlación: diseño óptimo de $c[n]$ a energía fija

> [!quote] Enunciado
> 4. La señal transmitida en el sistema de comunicación de la figura es
> $$s[n]=A\ p[n]$$
> donde $A=0$ con probabilidad $\tfrac13$ y $A=1$ con probabilidad $\tfrac23$. Las dos hipótesis son entonces
> $$H_0:\ A=0 \qquad\text{y}\qquad H_1:\ A=1$$
> El pulso $p[n]$ tiene energía unitaria, es decir $\sum_{n=-\infty}^{+\infty}p^2[n]=1$. El ruido $w[n]$ introducido por el canal es gaussiano i.i.d. de media nula con varianza $\sigma^2$, e independiente de la señal transmitida.
>
> ![[ej-p13-4.png]]
>
> La señal recibida es $r[n]=A\ p[n]+w[n]$. El sistema que actúa sobre la señal recibida se llama **receptor de correlación** y se usa mucho en radar y comunicaciones. El pulso $c[n]$ es de energía finita, y su elección se considera en el punto c). El bloque denotado $\Sigma$ calcula
> $$R=\sum_{n=-\infty}^{+\infty}r[n]\ c[n]$$
> El detector aplica un test de umbral a la variable aleatoria $R$: $R\underset{H_0}{\overset{H_1}{\gtrless}}\gamma$.
>
> a) En términos de $p[n]$, $c[n]$ y $\sigma^2$, determine el valor esperado de $R$ bajo $H_0$ y bajo $H_1$.
> b) En términos de $p[n]$, $c[n]$ y $\sigma^2$, determine la varianza de $R$ bajo $H_0$ y bajo $H_1$.
> c) Suponga que la energía de $c[n]$ está especificada en algún valor $K$. Determine la elección de $c[n]$ que maximiza
> $$\big(E[R|H_0]-E[R|H_1]\big)^2$$
> d) ¿Su elección de $c[n]$ en c), con una elección apropiada de $\gamma$, necesariamente minimiza la probabilidad de error? Recuerde que
> $$\text{Probabilidad de error}=P(\text{`}H_0\text{'},H_1)+P(\text{`}H_1\text{'},H_0)$$
> Explique, y si su respuesta es afirmativa, determine $\gamma$ en términos de los parámetros especificados.

###### **Idea**
$R$ es lineal en $r[n]$, así que es gaussiana bajo cada hipótesis; sus momentos salen de productos internos. La parte c) es otra vez Cauchy-Schwarz, la misma herramienta que usa el capítulo para probar que el filtro adaptado maximiza el SNR de salida sin suponer nada sobre la forma del ruido.

###### **Resolución**

**a) Medias.** Bajo $H_0$ ($A=0$): $r[n]=w[n]$, así que $E[R|H_0]=\sum_n E[w[n]]c[n]=0$. Bajo $H_1$ ($A=1$): $r[n]=p[n]+w[n]$, así que
$$\boxed{\ E[R|H_0]=0\ ,\qquad E[R|H_1]=\sum_n p[n]c[n]=\langle p,c\rangle\ }$$

**b) Varianzas.** En ambos casos $A$ es una constante conocida dentro de cada hipótesis (no aporta varianza); toda la aleatoriedad de $R$ viene de $\sum_n w[n]c[n]$, con $w[n]$ i.i.d. de varianza $\sigma^2$:
$$\boxed{\ \text{Var}(R|H_0)=\text{Var}(R|H_1)=\sigma^2\sum_n c^2[n]=\sigma^2\|c\|^2\ }$$
(no dependen de $H_i$: el ruido es el mismo proceso bajo las dos hipótesis).

**c) $c[n]$ óptimo a energía fija.** Queremos maximizar $\langle p,c\rangle^2$ sujeto a $\|c\|^2=K$. Por Cauchy-Schwarz,
$$\langle p,c\rangle^2\leq\|p\|^2\|c\|^2=1\cdot K=K$$
con igualdad si y solo si $c[n]=\lambda\,p[n]$ para algún escalar $\lambda$; la restricción de energía fija $\lambda^2\|p\|^2=K$ da $\lambda=\pm\sqrt K$. Tomando el signo que hace crecer $R$ con la señal (consistente con declarar `H1' para $R$ grande):
$$\boxed{\ c[n]=\sqrt K\,p[n]\ }\qquad\text{(el receptor de correlación óptimo es, otra vez, el filtro adaptado a }p[n]\text{)}$$
con valor máximo $\langle p,c\rangle^2=K$.

**d) ¿Esa elección minimiza $P_e$?**

**Sí.** La clave es que, a energía $K$ fija, $\text{Var}(R|H_i)=\sigma^2K$ es la **misma para cualquier forma** de $c[n]$ (parte b), no solo para la óptima. Entonces maximizar $\big(E[R|H_0]-E[R|H_1]\big)^2$ con la varianza fija es exactamente maximizar la relación (separación de medias)²/varianza — el mismo cociente que en el capítulo se muestra que controla directamente $P_e$ para una decisión gaussiana binaria de varianzas iguales. Como $R$ es gaussiana bajo ambas hipótesis con la misma varianza, elegir $\gamma$ óptimamente y usar el $c[n]$ que maximiza la separación de medias **minimiza** $P_e$ entre todos los receptores de correlación con energía $K$ fija.

El umbral óptimo, repitiendo la derivación MAP del capítulo pero con $R|H_0\sim\mathcal N(0,\nu^2)$ y $R|H_1\sim\mathcal N(m,\nu^2)$ ($m=\langle p,c\rangle=\sqrt K$, $\nu^2=\sigma^2K$):
$$\gamma=\frac{\nu^2}{m}\ln\!\left(\frac{p_0}{p_1}\right)+\frac m2=\sigma^2\sqrt K\,\ln\!\left(\frac{p_0}{p_1}\right)+\frac{\sqrt K}2$$
Con $p_0=\tfrac13,\ p_1=\tfrac23$ (dato del enunciado), $\ln(p_0/p_1)=\ln(1/2)=-\ln2$:
$$\boxed{\ \gamma=\sqrt K\left(\frac12-\sigma^2\ln2\right)\ }$$

Un detalle llamativo: como $m=\sqrt K$ y $\nu=\sigma\sqrt K$ escalan igual con $K$, el cociente $m/\nu=1/\sigma$ **no depende de $K$**. Sustituyendo $\gamma$ en $P_e=p_0Q(\gamma/\nu)+p_1Q((m-\gamma)/\nu)$:
$$\boxed{\ P_e=\frac13\,Q\!\left(\frac1{2\sigma}-\sigma\ln2\right)+\frac23\,Q\!\left(\frac1{2\sigma}+\sigma\ln2\right)\ }$$
que **tampoco depende de $K$**: escalar $c[n]$ (mientras se mantenga proporcional a $p[n]$) no cambia nada, porque señal y ruido en $R$ escalan igual.

###### **Verificación**
$\text{Var}(R|H_0)=\text{Var}(R|H_1)$ en la simulación para un $c[n]$ genérico (no necesariamente óptimo), confirmando b) ✓. *(Verificado numéricamente con $\sigma=0{,}9$, $p[n]$ de norma $1$ en $\mathbb R^3$: Monte Carlo de $4\cdot10^6$ muestras confirma $E[R|H_1]=\langle p,c\rangle$ y $\text{Var}(R|H_i)=\sigma^2\|c\|^2$ para un $c$ arbitrario. Con $c=\sqrt K\,p$ y $K\in\{0{,}5;\,1;\,4;\,25\}$, la fórmula cerrada da siempre $P_e=0{,}25515$ —igual en los cuatro casos, confirmando la independencia de $K$—, y Monte Carlo con $c$ óptimo da $P_e\approx0{,}2552$ para $K=1$ y $K=4$, coincidiendo con la fórmula.)*

> [!warning] Ojo
> Que $P_e$ no dependa de $K$ no significa que $K$ sea irrelevante: solo vale mientras $c[n]$ se elige proporcional a $p[n]$ (la elección óptima de c)). Si se fija $K$ pero se usa una forma de $c[n]$ **no** adaptada, la varianza sigue siendo $\sigma^2K$ pero $\langle p,c\rangle^2<K$, y ahí sí se pierde: $P_e$ empeora.

---

## Ejercicio 5 — Canal con memoria y ruido tanto a la entrada como a la salida

> [!quote] Enunciado
> 5. El diagrama de la figura P13.5-1 representa un sistema en el que la señal $d[n]$ se transmite a través de un canal de comunicaciones ruidoso, y se recibe $r[n]$.
>
> ![[ej-p13-5a.png]]
>
> El parámetro $\alpha$ que especifica la respuesta al impulso del canal es un número conocido, de magnitud menor que $0.5$. El proceso de ruido $w[n]$ es tal que su valor en cada instante es una variable aleatoria gaussiana de media nula con varianza conocida $\sigma_w^2$, y los valores en instantes distintos son independientes entre sí; es decir, $w[n]$ es un proceso gaussiano i.i.d. de media nula con $C_{ww}[m]=\sigma_w^2\delta[m]$. El proceso de ruido $v[n]$ también es gaussiano i.i.d. de media nula, independiente del proceso $w[\cdot]$, con varianza conocida $\sigma_v^2$, es decir $C_{vv}[m]=\sigma_v^2\delta[m]$.
>
> La señal $d[n]$ puede ser $0$ para todo tiempo (hipótesis $H_0$), o la muestra unitaria (hipótesis $H_1$):
> $$H_1:\ d[n]=\delta[n] \quad P(H_1)=p_1, \qquad H_0:\ d[n]=0 \quad P(H_0)=p_0$$
>
> En cada uno de los dos casos de a) y b), usted debe diseñar un receptor que tome $r[n]$ como entrada y decida entre $H_0$ y $H_1$ con mínima probabilidad de error. El receptor óptimo en cada caso involucra los pasos mostrados en la figura P13.5-2: filtrado LTI (posiblemente no causal) de $r[n]$; muestreo de la salida $g[n]$ del filtro en algún instante apropiado $n_0$; y decisión entre $H_0$ y $H_1$ según dónde caiga el valor muestreado respecto de un umbral $\gamma$.
>
> ![[ej-p13-5b.png]]
>
> Así, para especificar el receptor de mínima probabilidad de error en cada caso, deberá especificar: i) la respuesta al impulso $h[\cdot]$ o la función de sistema $H(z)$ del filtro; ii) el instante $n_0$ en el que muestrea la salida $g[n]$ del filtro; iii) el umbral $\gamma$ contra el que compara la muestra; y iv) cuáles son las decisiones para valores por encima y por debajo del umbral.
>
> a) Suponga $\sigma_w^2=0$ y $\sigma_v^2>0$. Especifique el receptor de mínima probabilidad de error. Si la respuesta al impulso del canal cambiara de modo que la magnitud de $\alpha$ se duplicara, ¿la probabilidad de error aumentaría, disminuiría o quedaría igual? Si cree que cambiaría, ¿por qué factor habría que multiplicar la varianza $\sigma_v^2$ para volver la probabilidad de error a su valor original?
> b) Suponga $\sigma_w^2>0$ y $\sigma_v^2=0$. Especifique el receptor de mínima probabilidad de error. Halle una expresión para la probabilidad de error en el caso $\sigma_w^2=1$, escribiéndola en términos de la función $Q$ estándar. Si la respuesta al impulso del canal cambiara de modo que la magnitud de $\alpha$ se duplicara, ¿la probabilidad de error aumentaría, disminuiría o quedaría igual?

###### **Idea**
Según el diagrama, $w[n]$ se suma **antes** del canal y $v[n]$ **después**: $r[n]=c[n]*\big(d[n]+w[n]\big)+v[n]$ con $c[n]=\alpha^nu[n]$. Cuando $\sigma_w^2=0$ el ruido que queda es blanco (solo $v$) y el problema es el del capítulo tal cual, con señal objetivo $s[n]=c[n]$. Cuando $\sigma_v^2=0$, en cambio, el ruido $w[n]$ queda coloreado por el **mismo** canal que da forma a la señal — eso sugiere invertir el canal (deshacer el filtrado) antes de decidir, y volver al caso blanco.

###### **Resolución**

**a) $\sigma_w^2=0,\ \sigma_v^2>0$.**

Con $w\equiv0$: $r[n]=c[n]+v[n]=\alpha^nu[n]+v[n]$. Es exactamente el problema base del capítulo, detectar $s[n]=c[n]$ en ruido blanco $v[n]$. La energía de $s[n]$:
$$E=\sum_{n=0}^\infty(\alpha^n)^2=\sum_{n=0}^\infty\alpha^{2n}=\frac1{1-\alpha^2}\qquad(\text{converge porque }|\alpha|<1)$$
El filtro adaptado es $h[n]=s[-n]=\alpha^{-n}u[-n]$: no nulo para $n\leq0$, decreciendo geométricamente a medida que $n\to-\infty$ (estable, pero **no causal**, tal como permite el enunciado). Se muestrea en $n_0=0$ y el umbral es el del capítulo:
$$\boxed{\ H(z)=\sum_{n\leq0}\alpha^{-n}z^{-n}=\frac1{1-\alpha z}\ ,\quad n_0=0\ ,\quad \gamma=\sigma_v^2\ln\!\left(\frac{p_0}{p_1}\right)+\frac E2=\sigma_v^2\ln\!\left(\frac{p_0}{p_1}\right)+\frac1{2(1-\alpha^2)}\ }$$
declarando `H1' si $g[0]>\gamma$.

*¿Qué pasa si $|\alpha|$ se duplica?* $E=1/(1-\alpha^2)$ **crece** con $\alpha^2$, así que la energía de la señal recibida aumenta y, a $\sigma_v^2$ fijo, $P_e=p_0Q(\gamma/(\sigma_v\sqrt E))+p_1Q((E-\gamma)/(\sigma_v\sqrt E))$ **disminuye** (mejora): más SNR, menos error.

Para volver a la $P_e$ original hay que mantener la relación señal-ruido $E/\sigma_v^2$ constante (es lo único de lo que depende $P_e$, junto con los priors — la sección "el resultado más importante del capítulo"). Si $\alpha\to2\alpha$, $E\to E'=1/(1-4\alpha^2)$, así que
$$\boxed{\ \sigma_v^2\ \text{debe multiplicarse por }\ \frac{E'}{E}=\frac{1-\alpha^2}{1-4\alpha^2}\ >1\ }$$
(factor mayor que $1$: hay que **aumentar** el ruido para compensar la señal más fuerte). Nótese que la restricción $|\alpha|<0{,}5$ del enunciado es justo lo que garantiza que $|2\alpha|<1$ y que $E'$ siga siendo finita.

**b) $\sigma_w^2>0,\ \sigma_v^2=0$.**

Ahora $r[n]=c[n]*\big(d[n]+w[n]\big)$. Llamando $z[n]=d[n]+w[n]$ a la señal antes del canal, en el dominio $z$: $R(z)=C(z)Z(z)$ con $C(z)=1/(1-\alpha z^{-1})$. Como $C(z)$ es invertible (su inversa $1/C(z)=1-\alpha z^{-1}$ es estable y causal), aplicar el filtro inverso a $r[n]$ recupera $z[n]$ **exactamente**, sin pérdida de información:
$$g[n]=r[n]-\alpha\,r[n-1]\ \Longleftrightarrow\ H(z)=1-\alpha z^{-1}$$
(con $r[-1]=0$, ya que no hay nada transmitido antes de $n=0$). Entonces $g[n]=z[n]=d[n]+w[n]$: quedó un problema de detectar $s[n]=\delta[n]$ (energía $E=1$) en ruido blanco $w[n]$, idéntico en estructura a la parte a) pero sin canal de por medio. Muestreando en $n_0=0$:
$$\boxed{\ H(z)=1-\alpha z^{-1}\ \ (\text{es decir } h[n]=\delta[n]-\alpha\delta[n-1])\ ,\quad n_0=0\ ,\quad \gamma=\sigma_w^2\ln\!\left(\frac{p_0}{p_1}\right)+\frac12\ }$$
declarando `H1' si $g[0]>\gamma$.

Con $\sigma_w^2=1$: $\gamma=\ln(p_0/p_1)+\tfrac12$, y
$$\boxed{\ P_e=p_0\,Q\!\left(\ln\frac{p_0}{p_1}+\frac12\right)+p_1\,Q\!\left(\frac12-\ln\frac{p_0}{p_1}\right)\ }$$

*¿Qué pasa si $|\alpha|$ se duplica?* **No cambia nada.** El filtro $h[n]=\delta[n]-\alpha\delta[n-1]$ deshace el canal exactamente para *cualquier* $\alpha$ (mientras $|\alpha|<1$, así que el filtro inverso sea estable), recuperando siempre $z[n]=d[n]+w[n]$ sin ninguna huella de $\alpha$. El problema equivalente —detectar $\delta[n]$ en ruido blanco $\sigma_w^2$— ni se entera de qué canal hubo. Entonces:
$$\boxed{\ P_e\ \text{queda igual, sin importar el valor de }\alpha\ }$$

###### **Verificación**
En a), $E\in(1,\infty)$ para $0<|\alpha|<1$, como corresponde a una energía ✓; $\gamma$ queda entre $0$ y $E$ para priors razonables ✓. *(Verificado numéricamente con $\alpha=0{,}35$, $\sigma_v^2=0{,}8$, priors iguales, $L=20$ muestras y Monte Carlo de $2\cdot10^6$: $E=1{,}1396$ (igual a la suma infinita $1/(1-\alpha^2)$), $P_e$ fórmula $=0{,}27533$ vs. simulación $0{,}27541$; con $\alpha'=2\alpha=0{,}7$ y el mismo $\sigma_v^2$, $P_e$ baja a $0{,}2169$ —mejora, como predice la teoría—; escalando $\sigma_v^2$ por el factor $(1-\alpha^2)/(1-4\alpha^2)=1{,}7206$, $P_e$ vuelve a $0{,}27533$, exacto.)*

En b), la reconstrucción de $z[n]=d[n]+w[n]$ a partir de $g[n]=r[n]-\alpha r[n-1]$ dio error numérico $<10^{-14}$ en la simulación (es exacta, no aproximada) ✓. *(Con $\sigma_w^2=1$ y priors iguales: fórmula $P_e=0{,}30854$ vs. Monte Carlo $0{,}30877$; con priors $p_0=\tfrac13,p_1=\tfrac23$: fórmula $0{,}26980$ vs. Monte Carlo $0{,}26984$. Repitiendo con $\alpha$ duplicado, la $P_e$ de Monte Carlo da $0{,}30877$ ambas veces: idéntica, confirmando la independencia de $\alpha$.)*

> [!info] Conexión
> El filtro de b) también sale de la fórmula general de ruido coloreado de [[PROCESAMIENTO DE SEÑALES]] (Cap. 13), $H(e^{j\Omega})=\sigma_w^2 S(e^{-j\Omega})/D_{nn}(e^{j\Omega})$: acá la "señal" recibida antes del ruido de salida es $s[n]=c[n]$ (mismo $C(e^{j\Omega})$ que colorea a $w$), así que $D_{nn}(e^{j\Omega})=\sigma_w^2|C(e^{j\Omega})|^2$ y la fórmula da $H(e^{j\Omega})=\sigma_w^2C(e^{-j\Omega})/\big(\sigma_w^2|C(e^{j\Omega})|^2\big)=1/C(e^{j\Omega})$ — el mismo blanqueador que encontramos a mano. Que el resultado no dependa de $\alpha$ es el caso extremo de "blanquear no pierde información" (Parte 1.5 de [[PROCESAMIENTO DE SEÑALES - Cap 13 en profundidad]]): acá directamente cancela por completo el efecto del canal sobre el desempeño.
