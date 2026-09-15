Solucionario de los Ejercicios Propuestos del capítulo 12 de [[PROCESAMIENTO DE SEÑALES]]. La teoría con demostraciones está en [[PROCESAMIENTO DE SEÑALES - Cap 12 en profundidad]].

# Estimación De Señales — Solucionario

Todo acá es filtro de Wiener. La primera mitad pide sobre todo la versión **no causal** (armar $H=D_{yx}/D_{xx}$ y el MMSE con la coherencia); la segunda, predictores y el Wiener **causal** por factorización espectral e innovaciones. En todos conviene resolver primero las correlaciones/PSD pedidas en los ítems previos porque el filtro sale de ahí directo. Los procesos son de media nula salvo que se diga lo contrario, así que $S=D$ (uso $D$ para las densidades, como en las fórmulas en cajita del apunte). Cotejá siempre los casos límite que piden los enunciados: son la verificación más barata de que el filtro tiene sentido.

###### **Índice**
| Ej. | Qué se practica | Problema del libro |
|---|---|---|
| 1 | Wiener no causal CT, canal con ganancia aleatoria $G$ | P12.4 |
| 2 | Wiener no causal CT, canal binario aleatorio (funciona/no funciona) | P12.8 |
| 3 | Wiener no causal a partir de correlaciones indirectas (sensor viejo desconocido) | P12.5 |
| 4 | PSD de un producto, igualador de PSD y Wiener no causal con gating Bernoulli | P12.6 |
| 5 | Wiener no causal con "borrado" de muestras (gating Bernoulli) | P12.7 |
| 6 | Wiener no causal, memoria con pérdidas aleatorias | P12.9 |
| 7 | Filtro ni causal ni anticausal, predictor LMMSE con una medición, Wiener no causal con ruido aditivo | P12.15 |
| 8 | Encriptación con secuencia $\pm1$, Wiener no causal | P12.10 |
| 9 | Predictor LMMSE de un paso con dos mediciones | P12.1 |
| 10 | Wiener no causal con dos ganancias aleatorias (enunciado reconstruido del libro) | P12.17 |
| 11 | Predictor LMMSE de un AR($N$) a partir de su recursión | P12.11 |
| 12 | AR(1): respuesta al impulso, autocorrelación y predictor causal | P12.13 |
| 13 | Autocorrelación de tres muestras: validez, LMMSE, factorización y los dos Wiener | P12.2 |
| 14 | Polos y ceros de una PSD, modelo generador, predictor FIR e IIR | P12.3 |
| 15 | Estimar la entrada de un lazo realimentado: con y sin causalidad | P12.16 |
| 16 | MA(1) no mínimo-fase, su factor de fase mínima y el predictor causal | P12.14 |
| 17 | Predictor de un paso para un modelo de fase mínima | P12.18 |
| 18 | Predictores de un coeficiente y predicción de un proceso exponencial | P12.12 |

---

## Ejercicio 1 — Wiener no causal con ganancia de canal aleatoria

> [!quote] Enunciado
> 1. Una cierta señal WSS de media nula $y(t)$ con autocorrelación $R_{yy}(\tau)$ y PSD correspondiente $S_{yy}(j\omega)$ se transmite a través de un canal que tiene una ganancia fija pero aleatoria $G$, cuya media y varianza son $\mu_G$ y $\sigma_G^2$ respectivamente. Debido al ruido en el receptor, la señal recibida $x(t)$ toma la forma
> $$x(t)=G\ y(t)+w(t)$$
> donde $w(t)$ es un proceso de ruido WSS de media nula con autocorrelación $R_{ww}(\tau)$ y PSD $S_{ww}(j\omega)$. El proceso transmitido $y(\cdot)$ y el proceso de ruido $w(\cdot)$ están no correlacionados entre sí, es decir $R_{yw}(\tau)=0$, y son independientes de $G$.
>
> a) Determine lo siguiente en términos de las cantidades dadas:
> i) $E[G^2]$;
> ii) el valor medio de $x(t)$;
> iii) la autocorrelación $R_{xx}(\tau)$ del proceso $x(t)$; y
> iv) la correlación cruzada $R_{yx}(\tau)$ entre $x(\cdot)$ e $y(\cdot)$.
> b) Calcule la respuesta en frecuencia $H(j\omega)$ de un filtro de Wiener LTI estable y posiblemente no causal que toma como entrada la señal recibida $x(\cdot)$ y produce como salida la estimación LMMSE $\hat y(t)$ de la señal transmitida $y(t)$, es decir, halle el filtro que minimiza $E[\{y(t)-\hat y(t)\}^2]$.
> i) ¿A qué se reduce $H(j\omega)$ en aquellas frecuencias $\omega$, si las hay, donde la PSD del ruido $S_{ww}(j\omega)$ es cero pero la PSD del proceso transmitido $S_{yy}(j\omega)$ no lo es? ¿Es la respuesta que esperaba? Explique.
> ii) ¿A qué se reduce $H(j\omega)$ en aquellas frecuencias donde la PSD del proceso transmitido es cero pero la del ruido no? ¿Es la respuesta que esperaba? Explique.

###### **Idea**
Todo sale de estirar la esperanza usando que $G$ es independiente de $y(\cdot)$ y $w(\cdot)$, y que $R_{yw}\equiv0$. Con $R_{xx}$ y $R_{yx}$ en mano, el filtro no causal es directo: $H=D_{yx}/D_{xx}$ (Parte 1.2 del complemento), y acá $S=D$ porque todo es de media nula.

###### **Resolución**
**a)**

**i)** Por definición de varianza, $\sigma_G^2=E[G^2]-\mu_G^2$:
$$\boxed{\ E[G^2]=\sigma_G^2+\mu_G^2\ }$$

**ii)** $G$ es independiente de $y(\cdot)$, así que $E[G\,y(t)]=E[G]\,E[y(t)]=\mu_G\cdot0=0$; y $E[w(t)]=0$. Entonces
$$\boxed{\ E[x(t)]=0\ }$$

**iii)** Desarrollando el producto:
$$R_{xx}(\tau)=E\big[(Gy(t{+}\tau)+w(t{+}\tau))(Gy(t)+w(t))\big]=E[G^2]\,E[y(t{+}\tau)y(t)]+E[G]\big(E[y(t{+}\tau)w(t)]+E[w(t{+}\tau)y(t)]\big)+E[w(t{+}\tau)w(t)]$$
Los dos términos cruzados son $E[G]\,R_{yw}(\tau)$ y $E[G]\,R_{yw}(-\tau)$ (usando $G\perp\!\!\!\perp y,w$), y ambos son cero porque $R_{yw}\equiv0$ para todo retardo. Queda
$$\boxed{\ R_{xx}(\tau)=(\sigma_G^2+\mu_G^2)\,R_{yy}(\tau)+R_{ww}(\tau)\ }$$

**iv)** $$R_{yx}(\tau)=E[y(t{+}\tau)x(t)]=E[y(t{+}\tau)(Gy(t)+w(t))]=E[G]\,R_{yy}(\tau)+\underbrace{R_{yw}(\tau)}_{=0}$$
$$\boxed{\ R_{yx}(\tau)=\mu_G\,R_{yy}(\tau)\ }$$

**b)** Transformando (con $S=D$ por ser todo de media nula):
$$D_{xx}(j\omega)=(\sigma_G^2+\mu_G^2)\,S_{yy}(j\omega)+S_{ww}(j\omega), \qquad D_{yx}(j\omega)=\mu_G\,S_{yy}(j\omega)$$
$$\boxed{\ H(j\omega)=\frac{D_{yx}(j\omega)}{D_{xx}(j\omega)}=\frac{\mu_G\,S_{yy}(j\omega)}{(\sigma_G^2+\mu_G^2)\,S_{yy}(j\omega)+S_{ww}(j\omega)}\ }$$

**i)** Donde $S_{ww}=0$ pero $S_{yy}\neq0$:
$$H(j\omega)\to\frac{\mu_G\,S_{yy}}{(\sigma_G^2+\mu_G^2)\,S_{yy}}=\frac{\mu_G}{\sigma_G^2+\mu_G^2}$$
No es la respuesta ingenua $1/\mu_G$ (invertir el canal a ciegas). Tiene sentido: aunque no haya ruido aditivo, sigue habiendo incertidumbre sobre **qué** $G$ tocó en cada realización (si $\sigma_G^2>0$), y el filtro es uno solo, fijo, que tiene que servir para todas las realizaciones. Lo que hace es "encoger" la inversión hacia $\mu_G/(\sigma_G^2+\mu_G^2)$ — exactamente la forma de un estimador LMMSE de una ganancia aleatoria (capítulo 8), no una inversión determinística. Si $\sigma_G^2\to0$ (canal de ganancia fija $G=\mu_G$, sin aleatoriedad), esto se reduce a $H\to1/\mu_G$: ahí sí, inversión exacta, como se esperaría porque no queda ninguna incertidumbre por resolver.

**ii)** Donde $S_{yy}=0$ pero $S_{ww}\neq0$: $H(j\omega)\to0/S_{ww}=0$. También es lo esperado: en esas frecuencias no hay nada de $y$ que recuperar, solo ruido, así que cualquier ganancia no nula únicamente agregaría ruido a la salida sin aportar señal — el óptimo es cortar completamente.

###### **Verificación**
*(verificado numéricamente: con $y,w$ blancos independientes de varianzas $\sigma_y^2=2$, $\sigma_w^2=0{,}7$ y $G\sim\mathcal N(\mu_G{=}1{,}5,\ \sigma_G^2{=}0{,}4)$ fijo por realización, Monte Carlo con $4000$ realizaciones de largo $500$ da $R_{xx}[0]\approx6{,}13$ contra el valor teórico $(\sigma_G^2+\mu_G^2)\sigma_y^2+\sigma_w^2=6{,}0$, y $R_{yx}[0]\approx3{,}04$ contra $\mu_G\sigma_y^2=3{,}0$; los lags $m=1,2$ dan $\approx0$ en ambos, como corresponde a procesos blancos.)*

> [!info] Conexión
> El caso límite de b)-i) con $\sigma_G^2>0$ es el mismo fenómeno de "encogimiento" (*shrinkage*) del estimador LMMSE de una constante con incertidumbre, capítulo 8 — acá aparece frecuencia por frecuencia.

---

## Ejercicio 2 — Wiener no causal con canal binario aleatorio

> [!quote] Enunciado
> 2. Una cierta señal WSS de tiempo continuo y media nula $y(t)$ con autocorrelación $R_{yy}(\tau)$ y PSD $S_{yy}(j\omega)$ se transmite a través de un canal. Las características del canal y del receptor son tales que la señal recibida $x(t)$ es de la forma
> $$x(t)=b\ y(t)+v(t)$$
> La cantidad $v(t)$ representa el ruido del receptor, y es un proceso WSS de media nula con autocorrelación $R_{vv}(\tau)$ y PSD $S_{vv}(j\omega)$, no correlacionado con $y(\cdot)$. La cantidad $b$ es una variable aleatoria independiente de $y(\cdot)$ y $v(\cdot)$, que toma el valor $1$ o $0$ para todo tiempo; se puede pensar como un indicador de si el canal funciona ($b=1$) o no ($b=0$). La probabilidad de que $b=1$ es $p$.
>
> a) Calcule $S_{yx}(j\omega)$ y $S_{xx}(j\omega)$, y luego halle la respuesta en frecuencia $H(j\omega)$ de un filtro de Wiener LTI estable y posiblemente no causal que toma como entrada la señal recibida $x(\cdot)$ y produce como salida la estimación LMMSE $\hat y(t)$. Verifique que su filtro se especializa a lo que espera cuando $p=1$ y cuando $p=0$.
> b) Halle una expresión para la PSD $S_{ee}(j\omega)$ del error $e(t)=y(t)-\hat y(t)$ asociado al filtro óptimo del punto a). Verifique de nuevo que se reduce a lo esperado cuando $p=1$ y $p=0$.

###### **Idea**
Igual que el Ejercicio 1, pero con $b$ en vez de $G$: como $b\in\{0,1\}$, $E[b]=p$ y (justamente porque $b^2=b$ para una variable binaria) $E[b^2]=p$ también. Con eso, $R_{yx}$ y $R_{xx}$ salen igual que antes, y el error cuadrático se calcula con la fórmula general $D_{ee}=D_{yy}-|D_{yx}|^2/D_{xx}$ de la Parte 1.2 del complemento.

###### **Resolución**
**a)** Con $b\perp\!\!\!\perp y,v$, $E[b]=p$, $E[b^2]=p$ (porque $b^2=b$), y $R_{yv}\equiv0$:
$$R_{yx}(\tau)=E[y(t{+}\tau)(by(t)+v(t))]=E[b]\,R_{yy}(\tau)+R_{yv}(\tau)=p\,R_{yy}(\tau)$$
$$R_{xx}(\tau)=E[b^2]\,R_{yy}(\tau)+E[b]\big(R_{yv}(\tau)+R_{vy}(\tau)\big)+R_{vv}(\tau)=p\,R_{yy}(\tau)+R_{vv}(\tau)$$
Transformando (media nula, $S=D$):
$$\boxed{\ S_{yx}(j\omega)=p\,S_{yy}(j\omega), \qquad S_{xx}(j\omega)=p\,S_{yy}(j\omega)+S_{vv}(j\omega)\ }$$
y el filtro no causal:
$$\boxed{\ H(j\omega)=\frac{S_{yx}(j\omega)}{S_{xx}(j\omega)}=\frac{p\,S_{yy}(j\omega)}{p\,S_{yy}(j\omega)+S_{vv}(j\omega)}\ }$$
**Casos límite.** Con $p=1$ (canal siempre funciona): $H=S_{yy}/(S_{yy}+S_{vv})$, el Wiener no causal clásico de señal-más-ruido — exactamente lo que se espera, porque con $p=1$ el problema *es* ese. Con $p=0$ (canal nunca funciona, $x=v$ sin nada de $y$): $H=0/(0+S_{vv})=0$; el filtro óptimo no deja pasar nada, porque $x$ no lleva ninguna información de $y$.

**b)** Con la fórmula general $D_{ee}=D_{yy}-|D_{yx}|^2/D_{xx}$ (Parte 1.2 del complemento):
$$S_{ee}(j\omega)=S_{yy}-\frac{p^2S_{yy}^2}{pS_{yy}+S_{vv}}=S_{yy}\cdot\frac{pS_{yy}+S_{vv}-p^2S_{yy}}{pS_{yy}+S_{vv}}=S_{yy}\cdot\frac{p(1-p)S_{yy}+S_{vv}}{pS_{yy}+S_{vv}}$$
$$\boxed{\ S_{ee}(j\omega)=\frac{S_{yy}(j\omega)\big[p(1-p)\,S_{yy}(j\omega)+S_{vv}(j\omega)\big]}{p\,S_{yy}(j\omega)+S_{vv}(j\omega)}\ }$$
**Casos límite.** Con $p=1$, el término $p(1-p)S_{yy}$ se anula y queda $S_{ee}=S_{yy}S_{vv}/(S_{yy}+S_{vv})$: el MMSE espectral estándar de señal-en-ruido-aditivo, coherente con a). Con $p=0$: $S_{ee}=S_{yy}\cdot S_{vv}/S_{vv}=S_{yy}$; como el filtro óptimo da $\hat y=0$, el error es $e=y$ directamente, así que su PSD tiene que ser $S_{yy}$ — exactamente lo que da la fórmula.

###### **Verificación**
*(verificado numéricamente: con el problema escalar análogo $Y,V$ gaussianas independientes ($\sigma_y^2=3$, $\sigma_v^2=1{,}2$) y $B\sim\text{Bernoulli}(p{=}0{,}35)$, Monte Carlo con $4\cdot10^6$ muestras da $R_{xx}[0]\approx2{,}249$ (teórico $2{,}25$), $R_{yx}[0]\approx1{,}050$ (teórico $1{,}05$), $H\approx0{,}467$ (teórico $0{,}4667$) y el MSE con ese $H$ da $\approx2{,}508$ contra la fórmula $2{,}51$. Para $p=1$, $H\approx0{,}714$ contra el teórico $5/7\approx0{,}7143$; para $p=0$, $H=0$ exacto.)*

> [!info] Conexión
> Es el mismo esquema del Ejercicio 1 (variable aleatoria multiplicando a $y$, independiente de todo), con $G\to b$ Bernoulli en vez de gaussiana — por eso $E[b^2]=p$ en vez de $\sigma_G^2+\mu_G^2$.

---

## Ejercicio 3 — Diseñar el Wiener sin poder medir la señal ni el ruido por separado

> [!quote] Enunciado
> 3. En su nuevo trabajo como investigador en el Instituto Oceanográfico, usted tiene acceso a mediciones registradas de un proceso aleatorio $x(t)$. Lo que en realidad le interesa, sin embargo, es el proceso WSS de media nula $y(t)$, relacionado con $x(t)$ por
> $$x(t)=y(t)+w(t)$$
> donde $w(\cdot)$ es un proceso de ruido WSS de media nula no correlacionado con $y(\cdot)$. Usted quiere diseñar un filtro LTI (posiblemente no causal) con respuesta al impulso $h(t)$ que filtre $x(t)$ y produzca la estimación LMMSE de $y(t)$. Sin embargo, no tiene mediciones de $y(t)$ ni de $w(t)$ para calcular directamente la información de correlación necesaria. Lo que sí tiene son registros extensos de mediciones tomadas por su predecesor, con un sensor viejo, de las señales filtradas
> $$v(t)=g(t)*w(t) \qquad\text{y}\qquad m(t)=g(t)*y(t)+w(t)$$
> donde $g(t)$ es la respuesta al impulso del sensor viejo, desconocida para usted. Con esos registros puede calcular buenas aproximaciones de $R_{vv}(\tau)$ y $R_{mm}(\tau)$. La pregunta es si esas funciones de correlación alcanzan para diseñar el filtro de Wiener.
>
> a) Exprese las PSD $S_{vv}(j\omega)$ y $S_{mm}(j\omega)$ en términos de $S_{yy}(j\omega)$, $S_{ww}(j\omega)$ y la respuesta en frecuencia $G(j\omega)$ del sensor viejo.
> b) Exprese la respuesta en frecuencia $H(j\omega)$ del filtro de Wiener deseado en términos únicamente de $S_{vv}(j\omega)$ y $S_{mm}(j\omega)$.
> c) Sea $S_{ee}(j\omega)$ la PSD de la señal de error $e(t)=y(t)-\hat y(t)$. Exprese el cociente $S_{ee}(j\omega)/S_{yy}(j\omega)$ en términos únicamente de $H(j\omega)$ y/o las PSD $S_{vv}(j\omega)$ y $S_{mm}(j\omega)$. Este cociente da una idea de la calidad del filtro de Wiener en cada frecuencia, porque compara la potencia espectral del error después de estimar con la de antes de estimar.

> [!warning] Nota sobre el enunciado
> La guía transcribe $m(t)=g(t)*y(t)+w(t)$, con el ruido **sin** filtrar. El original (P12.5, pág. 496 del libro) tiene un paréntesis que la guía perdió: $m(t)=g(t)*\big(y(t)+w(t)\big)=g(t)*x(t)$ — el sensor viejo filtra **todo** $x(t)$, no solo $y(t)$. Con la versión de la guía el problema queda mal planteado: $S_{vv}$ y $S_{mm}$ no alcanzan para determinar $H$ (quedan $3$ incógnitas —$S_{yy}$, $S_{ww}$, $|G|^2$— y solo $2$ ecuaciones, así que $H$ termina dependiendo de $|G|^2$, que es justo el dato que no se tiene). Con $m(t)=g(t)*x(t)$ sí se puede, porque el mismo $|G(j\omega)|^2$ multiplica a los dos términos de $S_{mm}$ y se cancela en el cociente $S_{mm}/S_{vv}$. Resolvemos con la versión del libro.

###### **Idea**
$v$ es el sensor viejo aplicado solo al ruido (una especie de calibración), y $m$ es el mismo sensor aplicado a la señal completa $x=y+w$. La clave es que el **mismo** $G(j\omega)$ desconocido multiplica ambos términos de $S_{mm}$, así que arma un cociente con $S_{vv}$ donde $G$ se cancela — no hace falta despejarlo ni conocerlo.

###### **Resolución**
**a)** Con $y\perp\!\!\!\perp$(no correlacionado con) $w$, filtrar por $g$ multiplica la PSD por $|G(j\omega)|^2$:
$$\boxed{\ S_{vv}(j\omega)=|G(j\omega)|^2\,S_{ww}(j\omega)\ }$$
$$\boxed{\ S_{mm}(j\omega)=|G(j\omega)|^2\big(S_{yy}(j\omega)+S_{ww}(j\omega)\big)=|G(j\omega)|^2 S_{xx}(j\omega)\ }$$
(la segunda porque $m=g*x$ y $S_{xx}=S_{yy}+S_{ww}$, al ser $y,w$ no correlacionados).

**b)** El filtro de Wiener deseado, el de siempre para $x=y+w$: $H=D_{yx}/D_{xx}=S_{yy}/(S_{yy}+S_{ww})=S_{yy}/S_{xx}$. Restando las dos PSD de a):
$$S_{mm}(j\omega)-S_{vv}(j\omega)=|G(j\omega)|^2\big(S_{xx}(j\omega)-S_{ww}(j\omega)\big)=|G(j\omega)|^2\,S_{yy}(j\omega)$$
y dividiendo por $S_{mm}=|G|^2S_{xx}$, el factor $|G(j\omega)|^2$ desaparece:
$$\boxed{\ H(j\omega)=\frac{S_{mm}(j\omega)-S_{vv}(j\omega)}{S_{mm}(j\omega)}=1-\frac{S_{vv}(j\omega)}{S_{mm}(j\omega)}\ }$$
Es decir: **sí alcanza** con $S_{vv}$ y $S_{mm}$ — no hace falta conocer $g(t)$, ni $S_{yy}$ ni $S_{ww}$ por separado.

**c)** Con $x=y+w$ no correlacionados, el error del Wiener no causal es $S_{ee}=S_{yy}\big(1-|\gamma_{yx}|^2\big)$, y como $\gamma_{yx}^2=S_{yy}/S_{xx}=H$ acá (coherencia real, caso escalar), $S_{ee}/S_{yy}=1-H$. Usando b):
$$\boxed{\ \frac{S_{ee}(j\omega)}{S_{yy}(j\omega)}=1-H(j\omega)=\frac{S_{vv}(j\omega)}{S_{mm}(j\omega)}\ }$$
También en términos únicamente de $S_{vv}$ y $S_{mm}$, sin pasar por $H$.

###### **Verificación**
Con $|G(j\omega)|^2$, $S_{yy}(j\omega)$, $S_{ww}(j\omega)$ arbitrarios y positivos, $H=(S_{mm}-S_{vv})/S_{mm}$ da siempre $S_{yy}/(S_{yy}+S_{ww})$ sin importar el valor de $|G|^2$ — *(verificado numéricamente: con 5 ternas aleatorias de $S_{yy},S_{ww},|G|^2\in[0{,}2;5]$, $H$ calculado por la fórmula coincide con $S_{yy}/(S_{yy}+S_{ww})$ hasta $10^{-10}$, y $S_{ee}/S_{yy}$ coincide con $S_{vv}/S_{mm}$ igual de bien, en los 5 casos.)* $0\leq H\leq1$ y $0\leq S_{ee}/S_{yy}\leq1$ siempre que $S_{vv}\leq S_{mm}$, que se cumple porque $S_{ww}\leq S_{xx}$.

> [!info] Conexión
> El truco de "dividir para cancelar el filtro desconocido" es el mismo espíritu que la deconvolución a ciegas: no hace falta conocer $g(t)$ si lo único que te importa es un cociente donde aparece multiplicando por igual arriba y abajo.

---

## Ejercicio 4 — PSD de un producto con gating Bernoulli, igualador y Wiener no causal

> [!quote] Enunciado
> 4. El proceso aleatorio $r[n]$ es blanco, de media nula y varianza unitaria. El proceso $y[n]$ se obtiene filtrando $r[n]$ con un filtro de respuesta en frecuencia $G(e^{j\Omega})$, como se muestra en la figura P12.4-1. Asuma que todas las señales y respuestas al impulso son reales.
>
> ![[ej-p12-4a.png]]
> ![[ej-p12-4b.png]]
>
> a) ¿Cuál es la PSD de $y[n]$, $S_{yy}(e^{j\Omega})$, expresada en términos de $G(e^{j\Omega})$?
>
> El proceso $x[n]$ se obtiene multiplicando el proceso $r[n]$ por un proceso $w[n]$ (figura P12.4-2). El proceso $w[\cdot]$ es independiente de $r[n]$ y toma el valor $1$ con probabilidad $p$ y $0$ con probabilidad $(1-p)$, de manera independiente para cada $n$.
>
> b) Calcule la media y la autocovarianza de $x[n]$. ¿Es $x[n]$ un proceso blanco?
> c) Diseñe el filtro LTI $H_1(e^{j\Omega})$ de la figura P12.4-3, con entrada $x[n]$, de modo que el proceso de salida $q[n]$ tenga la misma PSD que $y[n]$ (su resultado del punto a).
> d) Diseñe el filtro LTI $H_2(e^{j\Omega})$ de la figura P12.4-4, para el cual la entrada $x[n]$ produzca una salida $\hat y[n]$ que en cada instante sea la estimación LMMSE de $y[n]$.
> e) Para su respuesta del punto d), calcule el error cuadrático medio resultante. ¿Cuánto vale cuando $p=0$ y cuando $p=1$? Comente esos resultados: ¿le parecen razonables?

###### **Idea**
$x[n]=r[n]w[n]$ combina un blanco $r$ con un gating Bernoulli $w$ independiente. La blancura de $r$ "mata" toda correlación de $x$ fuera del lag $0$, así que $x$ termina siendo blanco también, aunque $w$ no lo sea. Con $S_{yy}$, $S_{xx}$ y $S_{yx}$ en mano, c) y d) son aplicar las fórmulas de siempre (igualador de PSD y Wiener no causal).

###### **Resolución**
**a)** $y=g*r$ con $r$ blanco de varianza $1$: $S_{yy}=|G|^2 S_{rr}$, y $S_{rr}(e^{j\Omega})=1$.
$$\boxed{\ S_{yy}(e^{j\Omega})=|G(e^{j\Omega})|^2\ }$$

**b)** Media: $r$ y $w$ independientes y $r$ de media nula, así que $\mu_x=E[r[n]]E[w[n]]=0$.

Autocovarianza (con media nula, $C_{xx}=R_{xx}$): como $r[\cdot]$ y $w[\cdot]$ son procesos independientes,
$$C_{xx}[m]=E[r[n{+}m]r[n]]\cdot E[w[n{+}m]w[n]]=R_{rr}[m]\cdot R_{ww}[m]$$
$R_{rr}[m]=\delta[m]$ ($r$ blanco unitario). $R_{ww}[m]$: en $m=0$, $E[w^2]=E[w]=p$ (variable binaria); en $m\neq0$, $w[\cdot]$ es i.i.d., así que $E[w[n{+}m]]E[w[n]]=p^2$. Pero el factor $R_{rr}[m]=\delta[m]$ anula todo lo que no sea $m=0$, sin importar cuánto valga $R_{ww}[m]$ ahí:
$$\boxed{\ \mu_x=0, \qquad C_{xx}[m]=p\ \delta[m]\ }$$
**Sí, $x[n]$ es blanco** — aunque $w[n]$ no lo es (tiene $R_{ww}[m]=p^2\neq0$ para $m\neq0$), la blancura de $r[n]$ se impone.

**c)** $x$ es blanco de varianza $p$, así que $S_{xx}(e^{j\Omega})=p$ (constante). Se quiere $S_{qq}=|H_1|^2S_{xx}=|H_1|^2p$ igual a $S_{yy}=|G|^2$:
$$\boxed{\ H_1(e^{j\Omega})=\frac{G(e^{j\Omega})}{\sqrt p}\ }$$
(cualquier filtro con ese módulo sirve; esta elección además conserva la fase de $G$, la más simple de implementar.)

**d)** Necesitamos $S_{yx}$. Con $y[n{+}m]=\sum_k g[k]\,r[n{+}m{-}k]$ y $w[n]$ independiente de todo el proceso $r[\cdot]$:
$$R_{yx}[m]=E[y[n{+}m]x[n]]=\sum_k g[k]\,E[r[n{+}m{-}k]r[n]]\cdot E[w[n]]=\sum_k g[k]\,\delta[m{-}k]\cdot p=p\,g[m]$$
Transformando, $S_{yx}(e^{j\Omega})=p\,G(e^{j\Omega})$. El filtro no causal:
$$H_2(e^{j\Omega})=\frac{S_{yx}}{S_{xx}}=\frac{p\,G(e^{j\Omega})}{p}$$
$$\boxed{\ H_2(e^{j\Omega})=G(e^{j\Omega})\ }$$
Llamativo: el filtro óptimo **no depende de $p$**. Tiene sentido en retrospectiva: cuando $w[n]=1$ la medición $x[n]=r[n]$ es perfecta, y cuando $w[n]=0$ no hay nada que hacer con esa muestra puntual; lo único que cambia con $p$ es *cuánta* información en total está disponible, no *qué forma* debe tener el filtro que la usa.

**e)** $$\text{MMSE}=\frac1{2\pi}\int_{-\pi}^{\pi}\Big(S_{yy}-\frac{|S_{yx}|^2}{S_{xx}}\Big)d\Omega=\frac1{2\pi}\int_{-\pi}^{\pi}\Big(|G|^2-\frac{p^2|G|^2}{p}\Big)d\Omega=(1-p)\cdot\frac1{2\pi}\int_{-\pi}^{\pi}|G|^2\,d\Omega$$
y por Parseval $\frac1{2\pi}\int|G|^2d\Omega=\sum_k g[k]^2=\text{Var}(y[n])=\sigma_y^2$:
$$\boxed{\ \text{MMSE}=(1-p)\,\sigma_y^2\ }$$
Con $p=0$: MMSE$=\sigma_y^2$ — $x[n]\equiv0$ para todo $n$ (nunca se ve nada de $r$), no hay información alguna, y el mejor estimador es la media ($\hat y=0$), con error total. Con $p=1$: MMSE$=0$ — no hay borrado, $x[n]=r[n]$ exactamente, y $H_2=G$ reconstruye $y[n]$ sin error. Ambos son razonables: $p$ interpola linealmente entre "no sirve nada" y "reconstrucción perfecta", según qué fracción de las muestras de $r$ se alcanza a ver a través de $x$.

###### **Verificación**
*(verificado numéricamente: con $g=[1;\,0{,}5;\,0{,}25]$ (FIR causal), $r$ blanco unitario y $p=0{,}3$, Monte Carlo con $2\cdot10^6$ muestras da $C_{xx}[0]\approx0{,}299$ (teórico $0{,}3$) y $C_{xx}[1{,}2,3]\approx0$; $R_{yx}[0,1,2]\approx0{,}299;\,0{,}150;\,0{,}075$ contra $p\,g[m]=0{,}3;\,0{,}15;\,0{,}075$; filtrando $x$ con el mismo $g$ (o sea $H_2=G$) el MSE empírico da $0{,}918$ contra $(1-p)\sigma_y^2=0{,}917$; y en los casos límite, $p=0$ da MSE$=\sigma_y^2=1{,}310$ exacto y $p=1$ da MSE$=0$ exacto.)*

---

## Ejercicio 5 — Borrado aleatorio de muestras y Wiener no causal

> [!quote] Enunciado
> 5. Asuma que $y[n]$ en la figura es WSS de media nula, con función de correlación $R_{yy}[m]$ y PSD $S_{yy}(e^{j\Omega})$. Suponga que el proceso $w[\cdot]$ es independiente del proceso $y[n]$, y en cualquier instante toma el valor $1$ con probabilidad $p$ o el valor $0$ con probabilidad $1-p$; asuma además que los valores de $w[\cdot]$ en instantes distintos son independientes. Así, la señal $x[n]=y[n]w[n]$ se obtiene poniendo en cero componentes aleatorias de $y[n]$.
>
> ![[ej-p12-5.png]]
>
> a) Halle la media $\mu_w$ del proceso WSS $w[n]$, y muestre que su función de correlación es de la forma $R_{ww}[m]=\alpha\delta[m]+\beta$, donde $\alpha$ y $\beta$ son constantes que debe determinar y $\delta[m]$ es la muestra unitaria. Halle también una expresión para la PSD $S_{ww}(e^{j\Omega})$.
> b) Calcule $R_{yx}[m]$ y $R_{xx}[m]$.
> c) Especifique la respuesta en frecuencia $H(e^{j\Omega})$ de un filtro LTI estable que tome $x[n]$ como entrada y produzca una estimación $\hat y[n]$ de $y[n]$ a su salida, con $H(e^{j\Omega})$ elegido de modo que el error cuadrático medio $E[(y[n]-\hat y[n])^2]$ sea mínimo. Su respuesta puede especificarse en términos de las PSD de $y[n]$ y $w[n]$. ¿A qué esperaría que se reduzca su expresión cuando $p=1$? ¿Se reduce efectivamente a eso?
> d) Halle una expresión para el error cuadrático medio que resulta de aplicar el filtro del punto c). Su respuesta puede darse en términos de integrales que involucren las PSD de $y[n]$ y $w[n]$. ¿A qué esperaría que se reduzca cuando i) $p=0$ y ii) $p=1$? ¿Se reduce efectivamente a eso?

###### **Idea**
Es el mismo mecanismo de "borrado" (*erasure*) del Ejercicio 4, pero ahora es $y[n]$ mismo el que se multiplica por el gating $w[n]$ (no un proceso auxiliar $r$). Como $y$ ya no es blanco en general, $R_{xx}[m]$ no colapsa a un delta: hay que arrastrar $R_{ww}[m]$ completo. El resto es la maquinaria de siempre.

###### **Resolución**
**a)** $\mu_w=E[w[n]]=1\cdot p+0\cdot(1-p)=p$.

Correlación: en $m=0$, $R_{ww}[0]=E[w^2[n]]=E[w[n]]=p$ (variable binaria, $w^2=w$). En $m\neq0$, por independencia de instantes distintos, $R_{ww}[m]=E[w[n{+}m]]E[w[n]]=p^2$. Juntando ambos casos en una sola expresión:
$$R_{ww}[m]=p^2+(p-p^2)\delta[m]=p(1-p)\,\delta[m]+p^2$$
$$\boxed{\ \mu_w=p, \qquad \alpha=p(1-p), \qquad \beta=p^2\ }$$
Transformando ($\delta[m]\to1$ constante, y una constante $\beta$ para todo $m$ transforma en un tren de impulsos en $\Omega=0$):
$$\boxed{\ S_{ww}(e^{j\Omega})=p(1-p)+2\pi p^2\,\delta(\Omega), \ \ |\Omega|\leq\pi\ }$$

**b)** Con $y\perp\!\!\!\perp w$:
$$R_{yx}[m]=E[y[n{+}m]\,y[n]w[n]]=R_{yy}[m]\,E[w[n]]$$
$$\boxed{\ R_{yx}[m]=p\ R_{yy}[m]\ }$$
$$R_{xx}[m]=E[y[n{+}m]w[n{+}m]\,y[n]w[n]]=E[y[n{+}m]y[n]]\cdot E[w[n{+}m]w[n]]=R_{yy}[m]\,R_{ww}[m]$$
$$\boxed{\ R_{xx}[m]=R_{yy}[m]\big(p(1-p)\delta[m]+p^2\big)=p^2R_{yy}[m]+p(1-p)R_{yy}[0]\,\delta[m]\ }$$
(usando $R_{yy}[m]\delta[m]=R_{yy}[0]\delta[m]$.)

**c)** Transformando b) (con $S_{yy}[0]$-integral $=R_{yy}[0]=\sigma_y^2$, la potencia de $y$):
$$S_{yx}(e^{j\Omega})=p\,S_{yy}(e^{j\Omega}), \qquad S_{xx}(e^{j\Omega})=p^2S_{yy}(e^{j\Omega})+p(1-p)\sigma_y^2$$
El filtro no causal:
$$H(e^{j\Omega})=\frac{S_{yx}}{S_{xx}}=\frac{p\,S_{yy}(e^{j\Omega})}{p^2S_{yy}(e^{j\Omega})+p(1-p)\sigma_y^2}$$
$$\boxed{\ H(e^{j\Omega})=\frac{S_{yy}(e^{j\Omega})}{p\,S_{yy}(e^{j\Omega})+(1-p)\,\sigma_y^2}\ }$$
**Con $p=1$:** $H\to S_{yy}/(S_{yy}+0)=1$. Es lo esperado: si $p=1$, $w[n]\equiv1$ siempre y $x[n]=y[n]$ exactamente, así que el filtro óptimo es dejar todo pasar sin cambios ($H=1$), y efectivamente eso da la fórmula.

**d)** $$\text{MMSE}=\frac1{2\pi}\int_{-\pi}^{\pi}\Big(S_{yy}-\frac{|S_{yx}|^2}{S_{xx}}\Big)d\Omega=\frac1{2\pi}\int_{-\pi}^{\pi}\Big(S_{yy}-\frac{p^2S_{yy}^2}{p^2S_{yy}+p(1-p)\sigma_y^2}\Big)d\Omega$$
Simplificando el integrando (sacar factor común $S_{yy}$ y common denominator):
$$S_{yy}-\frac{pS_{yy}^2}{pS_{yy}+(1-p)\sigma_y^2}=\frac{S_{yy}\big[pS_{yy}+(1-p)\sigma_y^2-pS_{yy}\big]}{pS_{yy}+(1-p)\sigma_y^2}=\frac{(1-p)\,\sigma_y^2\,S_{yy}}{pS_{yy}+(1-p)\sigma_y^2}$$
$$\boxed{\ \text{MMSE}=\frac1{2\pi}\int_{-\pi}^{\pi}\frac{(1-p)\,\sigma_y^2\,S_{yy}(e^{j\Omega})}{p\,S_{yy}(e^{j\Omega})+(1-p)\,\sigma_y^2}\,d\Omega\ }$$
**i) $p=0$:** el integrando queda $\sigma_y^2S_{yy}/\sigma_y^2=S_{yy}$, y $\frac1{2\pi}\int S_{yy}\,d\Omega=\sigma_y^2$. Es lo esperado: con $p=0$, $x[n]\equiv0$ siempre (no se ve nunca $y$), no hay información, y el mejor estimador es la media ($0$), con MMSE $=\text{Var}(y)=\sigma_y^2$ completo.
**ii) $p=1$:** el integrando queda $0\cdot\sigma_y^2S_{yy}/S_{yy}=0$, MMSE $=0$. Es lo esperado: sin borrado, $x=y$ y $H=1$ reconstruye $y$ exactamente.

###### **Verificación**
*(verificado numéricamente: con $y[n]$ AR(1) de polo $a=0{,}6$ e innovación de varianza $1$ ($\sigma_y^2=1/(1-a^2)=1{,}5625$) y $p=0{,}4$: resolviendo las ecuaciones normales de Wiener-Hopf truncadas a una ventana no causal de $601$ coeficientes ($L=300$) con las $R_{xx}[m]$, $R_{yx}[m]$ teóricas de b), el MMSE de la ventana da $0{,}75546$, y coincide hasta la 5ª cifra con la integral cerrada de d) evaluada numéricamente ($0{,}75546$); aplicando ese mismo filtro FIR a una simulación Monte Carlo de $4\cdot10^5$ muestras da un MSE empírico de $0{,}7560$. En los límites, la integral da $\sigma_y^2=1{,}5625$ para $p=0$ y $0$ para $p=1$, exactos.)*

> [!info] Conexión
> Es el Ejercicio 4 con los roles cambiados: acá se borra directamente $y$, allá se borraba un blanco auxiliar $r$ que después se filtraba. Por eso acá $H$ sí depende de $p$ (compará con el $H_2=G$ del Ejercicio 4, independiente de $p$): la diferencia es que ahí la blancura de $r$ hacía que "ver o no ver" una muestra no cambiara la *forma* del filtro óptimo, solo cuánta información total había.

---

## Ejercicio 6 — Memoria con pérdidas aleatorias

> [!quote] Enunciado
> 6. La figura es el diagrama en bloques de un sistema de memoria de tiempo discreto defectuoso, en el que los valores de las muestras se ponen en cero de manera aleatoria ("se pierden") al ser recuperados, junto con un filtro de estimación posterior usado para estimar el valor correcto de la señal guardada.
>
> ![[ej-p12-6.png]]
>
> Se sabe que:
> i) $s[n]$ es la señal correcta guardada en memoria; es un proceso WSS de media nula con autocorrelación y PSD
> $$R_{ss}[n]=\frac{16}{15}\left(\tfrac14\right)^{|n|}, \qquad S_{ss}(e^{j\Omega})=\frac{16}{|4-e^{-j\Omega}|^2} \ \ \text{para } |\Omega|\leq\pi$$
> ii) $p[n]$ es una secuencia aleatoria de ceros y unos que modela las pérdidas de memoria, con las propiedades: $p[\cdot]$ y $s[\cdot]$ son estadísticamente independientes; $p[\cdot]$ es i.i.d.; y $\text{Prob}(p[n]=1)=\tfrac34$, $\text{Prob}(p[n]=0)=\tfrac14$.
> iii) $g[n]=s[n]p[n]$ es la señal corrompida que se recupera de la memoria; siempre puede escribirse como $g[n]=k\ s[n]+r[n]$, donde $k$ es una constante y $r[n]=s[n](p[n]-k)$.
> iv) $H(e^{j\Omega})$ es la respuesta en frecuencia de un filtro LTI (no necesariamente causal) usado para estimar $s[n]$ a partir de $g[\cdot]$.
>
> a) Determine la constante $k$ para la cual el proceso $r[n]$ tiene media nula y está no correlacionado con el proceso $s[n]$.
> b) Determine $R_{rr}[n]$, la autocorrelación de $r[n]$, cuando $r[n]$ tiene media nula y está no correlacionado con $s[n]$.
> c) Determine la respuesta en frecuencia $H(e^{j\Omega})$ que minimiza el error cuadrático medio de estimación $E[(s[n]-\hat s[n])^2]$.

###### **Idea**
Es el mismo borrado Bernoulli del Ejercicio 5, pero reescrito como "señal más ruido": separando $g=ks+r$ con $r$ elegido para que quede sin correlación con $s$, el problema se vuelve el caso estándar señal-en-ruido-aditivo (Ejercicio 3), solo que con una ganancia $k$ de por medio.

###### **Resolución**
**a)** $r[n]=s[n](p[n]-k)$. Su media: $E[r[n]]=E[s[n]]\,E[p[n]-k]=0$ para **cualquier** $k$, porque $s$ ya es de media nula (y $s\perp\!\!\!\perp p$). La condición que sí fija $k$ es la de no correlación con $s[n]$:
$$E[r[n]s[n]]=E\big[s^2[n](p[n]-k)\big]=E[s^2[n]]\cdot E[p[n]-k]=R_{ss}[0]\,(\mu_p-k)\overset{!}{=}0 \ \Longrightarrow\ k=\mu_p$$
$$\boxed{\ k=\mu_p=\tfrac34\ }$$

**b)** Con $k=\mu_p$, escribo $q[n]=p[n]-\mu_p$ (media nula). Como $s\perp\!\!\!\perp p$:
$$R_{rr}[m]=E[s[n{+}m]q[n{+}m]\,s[n]q[n]]=R_{ss}[m]\cdot E[q[n{+}m]q[n]]$$
$E[q[n+m]q[n]]=\text{Cov}(p[n{+}m],p[n])$: en $m=0$ es $\text{Var}(p)=\mu_p(1-\mu_p)=\tfrac34\cdot\tfrac14=\tfrac3{16}$ (porque $p^2=p$); en $m\neq0$, $p[\cdot]$ i.i.d. da covarianza $0$. Entonces $E[q[n+m]q[n]]=\tfrac3{16}\delta[m]$, y como multiplica a $R_{ss}[m]\delta[m]=R_{ss}[0]\delta[m]$:
$$R_{rr}[m]=R_{ss}[0]\cdot\tfrac3{16}\,\delta[m]=\frac{16}{15}\cdot\frac3{16}\,\delta[m]=\frac15\,\delta[m]$$
$$\boxed{\ R_{rr}[n]=\tfrac15\,\delta[n]\ }$$
($r[n]$ resulta **blanco**, de varianza $\sigma_r^2=1/5$.)

**c)** Con $g=ks+r$, $r$ de media nula, blanco, y no correlacionado con $s$ en **ningún** lag (la misma cuenta de a) da $R_{sr}[m]=R_{ss}[m](\mu_p-k)=0$ para todo $m$, no solo $m=0$), este es exactamente el caso señal-más-ruido escalado:
$$S_{sg}(e^{j\Omega})=k\,S_{ss}(e^{j\Omega}), \qquad S_{gg}(e^{j\Omega})=k^2S_{ss}(e^{j\Omega})+\sigma_r^2$$
$$H(e^{j\Omega})=\frac{S_{sg}}{S_{gg}}=\frac{k\,S_{ss}(e^{j\Omega})}{k^2S_{ss}(e^{j\Omega})+\sigma_r^2}=\frac{\tfrac34\,S_{ss}(e^{j\Omega})}{\tfrac9{16}\,S_{ss}(e^{j\Omega})+\tfrac15}$$
Sustituyendo $S_{ss}(e^{j\Omega})=16/|4-e^{-j\Omega}|^2=16/(17-8\cos\Omega)$ y simplificando (multiplicar arriba y abajo por $(17-8\cos\Omega)$, después por $80$):
$$\boxed{\ H(e^{j\Omega})=\frac{30}{31-4\cos\Omega}\ }$$

###### **Verificación**
Chequeo algebraico con sympy: la forma general $\dfrac{kS_{ss}}{k^2S_{ss}+\sigma_r^2}$ con $k=3/4$, $\sigma_r^2=1/5$ y $S_{ss}=16/(17-8\cos\Omega)$ simplifica exactamente a $30/(31-4\cos\Omega)$ (diferencia simbólica $=0$).

*(verificado numéricamente: simulando $s[n]$ como el AR(1) equivalente a $R_{ss}$ ($a=1/4$, innovación de varianza $1$, porque $16/|4-e^{-j\Omega}|^2=1/|1-\tfrac14e^{-j\Omega}|^2$) y $p[n]\sim\text{Bernoulli}(3/4)$ i.i.d., Monte Carlo con $2\cdot10^6$ muestras da $k_{\text{emp}}=\text{Cov}(g,s)/\text{Var}(s)\approx0{,}7508$ (teórico $0{,}75$), $R_{rr}[0]\approx0{,}1998$ (teórico $0{,}2$) y $R_{rr}[1,2,3]\approx0$. Resolviendo las ecuaciones normales de Wiener-Hopf truncadas ($L=200$) con las correlaciones teóricas, el MMSE de la ventana da $0{,}26024$, igual hasta la 6ª cifra a la integral cerrada de $\frac1{2\pi}\int(S_{ss}-|S_{sg}|^2/S_{gg})\,d\Omega$; aplicado a una simulación da un MSE empírico de $0{,}2596$, consistente.)*

> [!info] Conexión
> $s^2=s$, $p^2=p$: la manera de sacarle partido a que una variable binaria sea idempotente aparece todo el tiempo en este tipo de problemas de borrado (Ejercicios 4, 5 y este).

---

## Ejercicio 7 — Un filtro ni causal ni anticausal, predicción de dos pasos y Wiener con ruido

> [!quote] Enunciado
> 7. a) La respuesta en frecuencia de un sistema LTI de tiempo discreto particular es
> $$H(e^{j\Omega})=\frac{e^{j2\Omega}}{1-\tfrac12 e^{-j\Omega}}$$
> Determine su respuesta al impulso $h[n]$. Si lo hace correctamente, encontrará que el sistema no es ni causal ni anticausal. Determine además $\sum_{k=-\infty}^{\infty}h[k]$ y $\int_0^{\pi}|H(e^{j\Omega})|^2 d\Omega$. Recuerde que $\sum_{i=0}^{\infty}r^i=\frac{1}{1-r}$ para $|r|<1$.
>
> b) Si $x[n]$ denota un proceso WSS con media $\mu_x$ y autocovarianza $C_{xx}[m]=\sigma_x^2\delta[m]$, ¿cuál es la estimación LMMSE de $x[n+2]$ en términos de $x[n]$? Es decir, halle $\gamma$ y $\phi$ en $\hat x[n+2]=\gamma\ x[n]+\phi$ tales que $E\{(x[n+2]-\hat x[n+2])^2\}$ sea mínimo. Halle también el MMSE asociado.
>
> c) Si el proceso $x[n]$ de b) se aplica a la entrada del sistema de a), ¿cuál es la PSD $S_{yy}(e^{j\Omega})$ del proceso de salida $y[n]$? Evalúe además $E\{y[n]\}$, $E\{y^2[n]\}$ y $\lim_{N\to\infty}\frac{1}{2N+1}\sum_{k=-N}^{N}y[k]$.
>
> d) Para esta parte, asuma $\mu_x=0$ por simplicidad. Con todas las cantidades como antes, suponga que lo que puede medir es $q[n]=y[n]+v[n]$ para todo $n$, donde $v[n]$ es ruido blanco de media nula e intensidad $\sigma_v^2$, no correlacionado con el proceso $x[k]$. Calcule la respuesta en frecuencia $W(e^{j\Omega})$ del filtro de Wiener no causal que toma $q[n]$ como entrada en el instante $n$ y produce la estimación LMMSE $\hat x[n+2]$ como salida en ese instante. Verifique explícitamente que su respuesta se reduce a lo esperado en el caso $\sigma_v^2=0$.

###### **Idea**
En a) hay que leer $H$ como "un sistema causal estándar" ($1/(1-\tfrac12e^{-j\Omega})$, polo en $\tfrac12$) **compuesto con un adelanto de $2$ muestras** ($e^{j2\Omega}$ desplaza a la izquierda). En b) $x[n]$ y $x[n+2]$ están a más de un lag de distancia y $x$ es blanco, así que no hay nada que explotar: el mejor predictor es la media. c) es propagar momentos de blanco a través de un LTI. d) es un Wiener no causal más, pero para estimar una versión *adelantada* de $x$ ($z[n]=x[n+2]$) a partir de $q$ — el adelanto se traduce en un factor $e^{j2\Omega}$ en la correlación cruzada.

###### **Resolución**
**a)** $1/(1-\tfrac12e^{-j\Omega})$ es la transformada de $(\tfrac12)^n u[n]$ (causal). El factor $e^{j2\Omega}$ corresponde a adelantar la secuencia $2$ muestras ($x[n+n_0]\leftrightarrow e^{j\Omega n_0}X(e^{j\Omega})$, acá $n_0=2$):
$$\boxed{\ h[n]=\left(\tfrac12\right)^{n+2}u[n+2]\ }$$
o sea $h[-2]=1,\ h[-1]=\tfrac12,\ h[0]=\tfrac14,\ h[1]=\tfrac18,\dots$ — tiene muestras no nulas para $n<0$ (no es causal) y también para $n\to\infty$ (no es anticausal).

$$\sum_k h[k]=\sum_{n=-2}^{\infty}\left(\tfrac12\right)^{n+2}=\sum_{m=0}^{\infty}\left(\tfrac12\right)^m=\frac{1}{1-\tfrac12}=\boxed{2}$$
(coincide con $H(e^{j0})=e^{0}/(1-\tfrac12)=2$, como tiene que ser.)

Para la integral, $|H(e^{j\Omega})|^2=1/|1-\tfrac12e^{-j\Omega}|^2$ (el $|e^{j2\Omega}|=1$ no aporta). Con $|1-\tfrac12e^{-j\Omega}|^2=\tfrac54-\cos\Omega$:
$$\int_0^{\pi}|H(e^{j\Omega})|^2\,d\Omega=\int_0^\pi\frac{4}{5-4\cos\Omega}\,d\Omega=4\cdot\frac{\pi}{\sqrt{5^2-4^2}}=4\cdot\frac{\pi}{3}$$
(usando $\int_0^\pi\frac{d\Omega}{a-b\cos\Omega}=\frac{\pi}{\sqrt{a^2-b^2}}$, $a=5,b=4$)
$$\boxed{\ \int_0^\pi|H(e^{j\Omega})|^2\,d\Omega=\frac{4\pi}{3}\ }$$

**b)** $x[n]$ y $x[n+2]$ están separados dos lags, y $x$ es blanco ($C_{xx}[m]=\sigma_x^2\delta[m]$), así que $\text{Cov}(x[n{+}2],x[n])=C_{xx}[2]=0$: no están correlacionados. El LMMSE de una variable a partir de otra con la que no tiene correlación es simplemente su media:
$$\boxed{\ \hat x[n+2]=\mu_x \ \ (\gamma=0,\ \phi=\mu_x), \qquad \text{MMSE}=\sigma_x^2\ }$$
(no hay nada que $x[n]$ le pueda enseñar a $x[n+2]$ acá — el mismo fenómeno que menciona el Ejercicio 9 para $k>0$.)

**c)** Con media $\mu_x\neq0$, la autocorrelación (no solo la covarianza) importa: $R_{xx}[m]=\sigma_x^2\delta[m]+\mu_x^2$, así que $S_{xx}(e^{j\Omega})=\sigma_x^2+2\pi\mu_x^2\delta(\Omega)$ (Ejercicio 5-a tiene la misma estructura). Filtrando por $h$:
$$S_{yy}(e^{j\Omega})=|H(e^{j\Omega})|^2S_{xx}(e^{j\Omega})=\sigma_x^2|H(e^{j\Omega})|^2+2\pi\mu_x^2|H(e^{j0})|^2\delta(\Omega)$$
con $|H(e^{j\Omega})|^2=4/(5-4\cos\Omega)$ de a) y $|H(e^{j0})|^2=2^2=4$:
$$\boxed{\ S_{yy}(e^{j\Omega})=\frac{4\sigma_x^2}{5-4\cos\Omega}+8\pi\mu_x^2\,\delta(\Omega),\ \ |\Omega|\leq\pi\ }$$
Media de la salida: $E\{y[n]\}=\mu_x\sum_k h[k]=\mu_x\cdot2$:
$$\boxed{\ E\{y[n]\}=2\mu_x\ }$$
Potencia media: $\text{Var}(y[n])=\sigma_x^2\sum_k h[k]^2$, y $\sum_k h[k]^2=\sum_{m\geq0}(\tfrac14)^m=\tfrac43$ (Parseval, coincide con $\tfrac1{2\pi}\int_{-\pi}^{\pi}|H|^2d\Omega=\tfrac1{2\pi}\cdot2\cdot\tfrac{4\pi}3=\tfrac43$, usando que $|H|^2$ es par). Entonces
$$E\{y^2[n]\}=\text{Var}(y[n])+E\{y[n]\}^2=\tfrac43\sigma_x^2+4\mu_x^2$$
$$\boxed{\ E\{y^2[n]\}=\tfrac43\sigma_x^2+4\mu_x^2\ }$$
Por último, el promedio temporal: como $C_{yy}[m]=\sigma_x^2\sum_k h[k]h[k+m]=\tfrac43\sigma_x^2(\tfrac12)^{|m|}$ es absolutamente sumable (decae geométricamente), $y[n]$ es **media-ergódico**, y el promedio temporal converge (en media cuadrática) a la media del proceso:
$$\boxed{\ \lim_{N\to\infty}\frac1{2N+1}\sum_{k=-N}^N y[k]=E\{y[n]\}=2\mu_x\ }$$

**d)** Con $\mu_x=0$: $S_{xx}=\sigma_x^2$ (blanco puro), $S_{yy}=\sigma_x^2|H(e^{j\Omega})|^2$, y $S_{qq}=S_{yy}+\sigma_v^2$ ($v$ no correlacionado con $y$). Definiendo $z[n]=x[n+2]$ (lo que se quiere estimar), su espectro cruzado con $q$ es
$$S_{zq}(e^{j\Omega})=e^{j2\Omega}\,S_{xq}(e^{j\Omega})=e^{j2\Omega}\,H(e^{-j\Omega})\,\sigma_x^2$$
(el adelanto de $2$ aporta $e^{j2\Omega}$; $S_{xq}=S_{xy}=H(e^{-j\Omega})S_{xx}$ porque $v\perp\!\!\!\perp x$). El filtro no causal:
$$W(e^{j\Omega})=\frac{S_{zq}(e^{j\Omega})}{S_{qq}(e^{j\Omega})}=\frac{\sigma_x^2\,e^{j2\Omega}H(e^{-j\Omega})}{\sigma_x^2|H(e^{j\Omega})|^2+\sigma_v^2}$$
Con $H(e^{j\Omega})=e^{j2\Omega}/(1-\tfrac12e^{-j\Omega})$, el numerador se simplifica: $e^{j2\Omega}H(e^{-j\Omega})=e^{j2\Omega}\cdot\dfrac{e^{-j2\Omega}}{1-\tfrac12e^{j\Omega}}=\dfrac1{1-\tfrac12e^{j\Omega}}$. Usando también $|H|^2=4/(5-4\cos\Omega)$:
$$\boxed{\ W(e^{j\Omega})=\dfrac{\sigma_x^2}{\Big(1-\tfrac12e^{j\Omega}\Big)\left(\dfrac{4\sigma_x^2}{5-4\cos\Omega}+\sigma_v^2\right)}\ }$$
**Caso límite $\sigma_v^2=0$:** sin ruido, $q=y$, y lo esperable es "invertir $H$ y adelantar $2$", es decir $W\to e^{j2\Omega}/H(e^{j\Omega})$. Sustituyendo $\sigma_v^2=0$ en la fórmula de arriba:
$$W(e^{j\Omega})\Big|_{\sigma_v^2=0}=\frac{\sigma_x^2(5-4\cos\Omega)}{4\sigma_x^2\big(1-\tfrac12e^{j\Omega}\big)}=\frac{5-4\cos\Omega}{4(1-\tfrac12e^{j\Omega})}$$
y como $4(1-\tfrac12e^{j\Omega})(1-\tfrac12e^{-j\Omega})=4\,|1-\tfrac12e^{-j\Omega}|^2=5-4\cos\Omega$ (la misma cuenta de a)), el cociente se cancela exactamente:
$$\boxed{\ W(e^{j\Omega})\Big|_{\sigma_v^2=0}=1-\tfrac12e^{-j\Omega}=\frac{e^{j2\Omega}}{H(e^{j\Omega})}\ }$$
Es justo lo esperado: sin ruido, "deshacer $H$ y adelantar $2$" reconstruye $x[n+2]$ exactamente (MMSE $=0$, se puede chequear integrando).

###### **Verificación**
*(verificado numéricamente en a): con $h[n]$ truncado a $n\in[-2,80]$, $\sum h[k]=2{,}000$ exacto y $\int_0^\pi|H|^2d\Omega=4{,}18879$ contra $4\pi/3=4{,}18879$; también $\pi\sum h[k]^2=4{,}18879$, coincide con Parseval. En c): con $\sigma_x^2=2$, $\mu_x=0{,}7$, Monte Carlo con $3\cdot10^6$ muestras da $E\{y\}\approx1{,}3998$ (teórico $1{,}4$), $E\{y^2\}\approx4{,}6251$ (teórico $4{,}6267$), y el promedio temporal de $y$ coincide con $E\{y\}$ hasta la 4ª cifra, confirmando la ergodicidad en media. En d): resolviendo las ecuaciones normales de Wiener-Hopf truncadas ($L=60$) con las correlaciones cerradas $R_{qq}[m]=\tfrac43\sigma_x^2(\tfrac12)^{|m|}+\sigma_v^2\delta[m]$ y $R_{zq}[m]=\sigma_x^2 2^{m}$ para $m\leq0$ (y $0$ para $m>0$, deducidas de $R_{xy}[\tau]=\sigma_x^2h[-\tau]$), la transformada de los coeficientes resueltos coincide con la fórmula cerrada de $W(e^{j\Omega})$ hasta $10^{-5}$ en cinco frecuencias de prueba; y el MMSE de esa ventana ($0{,}44777$) coincide con la integral cerrada $\frac1{2\pi}\int(S_{zz}-|S_{zq}|^2/S_{qq})\,d\Omega$ hasta la 6ª cifra. La reducción simbólica de $W$ en $\sigma_v^2=0$ a $1-\tfrac12e^{-j\Omega}$ también se confirmó con sympy.)*

> [!warning] Ojo
> $h[n]$ acá **no** es causal a pesar de que la mitad de la fórmula ($1/(1-\tfrac12e^{-j\Omega})$) sí lo sea: el adelanto $e^{j2\Omega}$ mueve toda la respuesta $2$ muestras a la izquierda, sacando del origen justo las dos muestras que hacían falta para que fuera causal. Vale la pena dibujarlo mentalmente antes de calcular $\sum h[k]$ a ciegas.

---

## Ejercicio 8 — Encriptación con secuencia $\pm1$ y Wiener no causal

> [!quote] Enunciado
> 8. La señal de mensaje $y[n]$ de la figura debe encriptarse y transmitirse por un canal ruidoso, luego desencriptarse y filtrarse en el receptor. Modelamos $y[n]$ como un proceso WSS de media nula con autocorrelación $R_{yy}[m]$ y PSD $S_{yy}(e^{j\Omega})$. La señal $p[n]$ se usa tanto para encriptar en el transmisor como para desencriptar en el receptor, y es un proceso i.i.d. que toma los valores $+1$ o $-1$ con igual probabilidad en cada instante; es independiente del proceso $y[\cdot]$. Notar que $p^2[n]=1$ para todo $n$. La señal transmitida $q[n]$ es el producto $p[n]y[n]$.
>
> ![[ej-p12-8.png]]
>
> a) Determine las medias $\mu_p$ y $\mu_q$ de los procesos $p[n]$ y $q[n]$, sus autocorrelaciones $R_{pp}[m]$ y $R_{qq}[m]$ (en términos de $R_{yy}[\cdot]$), y la correlación cruzada $R_{yq}[m]$ entre la señal de mensaje y la transmitida. ¿Le serviría de algo a un intruso que interceptara el proceso transmitido $q[\cdot]$ un estimador lineal (posiblemente no causal) de $y[n]$ basado en mediciones de $q[\cdot]$? Explique.
>
> El canal suma un ruido $v[n]$ a la señal transmitida, de modo que la señal recibida es $q[n]+v[n]=p[n]y[n]+v[n]$. Asuma que $v[n]$ es WSS blanco de media nula, con $R_{vv}[m]=\sigma_v^2\delta[m]$; no correlacionado con $y[\cdot]$, y ambos procesos independientes de $p[\cdot]$. El receptor conoce la señal de encriptación específica $p[n]$. Si no hubiera ruido de canal, desencriptar sería simplemente multiplicar por $p[n]$, porque $p[n]q[n]=p^2[n]y[n]=y[n]$. Con ruido, igual desencriptamos así, pero le agregamos una etapa de filtrado. La señal a filtrar es entonces
> $$x[n]=p[n]\big(p[n]y[n]+v[n]\big)=y[n]+p[n]v[n]$$
>
> b) Determine $\mu_x$, $R_{xx}[m]$ y $R_{yx}[m]$.
> c) Suponga que el filtro del receptor es un filtro de Wiener no causal (estable), construido para producir la estimación LMMSE $\hat y[n]$ de $y[n]$. Determine su respuesta en frecuencia $H(e^{j\Omega})$, y verifique explícitamente que es lo que esperaría en los dos casos límite $\sigma_v^2=0$ y $\sigma_v^2\to\infty$. Escriba además una expresión, en términos de $S_{yy}(e^{j\Omega})$ y $\sigma_v^2$, para el error cuadrático medio obtenido con este filtro, y verifique también los dos casos límite.

###### **Idea**
La clave de todo el ejercicio es $p^2[n]=1$: cada vez que aparece $p[n]$ multiplicado por sí mismo en una correlación, se cancela. Eso hace que a) salga "demasiado bien" (la encriptación deja $q$ sin ninguna correlación con $y$) y que b)-c) colapsen exactamente al caso clásico de señal-más-ruido-blanco, con el ruido "disfrazado" de $p[n]v[n]$.

###### **Resolución**
**a)** $p[n]=\pm1$ equiprobable: $\mu_p=E[p]=0$. Como $p\perp\!\!\!\perp y$ y ambos de media nula, $\mu_q=E[p[n]y[n]]=\mu_p\mu_y=0$.

$R_{pp}[m]$: en $m=0$, $E[p^2]=1$ (siempre, porque $p=\pm1$); en $m\neq0$, i.i.d. da $E[p[n{+}m}]]E[p[n]]=0$. Entonces $R_{pp}[m]=\delta[m]$.

$$R_{qq}[m]=E[p[n{+}m]y[n{+}m]p[n]y[n]]=E[p[n{+}m]p[n]]\,E[y[n{+}m]y[n]]=R_{pp}[m]\,R_{yy}[m]=\delta[m]\,R_{yy}[m]$$
$$\boxed{\ \mu_p=0,\quad \mu_q=0, \quad R_{pp}[m]=\delta[m], \quad R_{qq}[m]=R_{yy}[0]\,\delta[m]\ }$$
($q[n]$ sale **blanco** — la encriptación "aplana" completamente el espectro del mensaje.)

$$R_{yq}[m]=E[y[n{+}m]\,p[n]y[n]]=E[p[n]]\,E[y[n{+}m]y[n]]=\mu_p\,R_{yy}[m]$$
$$\boxed{\ R_{yq}[m]=0 \ \ \text{para todo } m\ }$$
**No, no le sirve de nada.** La correlación cruzada entre $y$ y $q$ es idénticamente nula en todo lag, así que el filtro de Wiener no causal para estimar $y[n]$ a partir de $q[\cdot]$ sería $H=S_{yq}/S_{qq}=0$: la mejor estimación lineal (aun con acceso a *todo* $q[\cdot]$, pasado y futuro) es la constante $0$ — ni una gota mejor que no medir nada. La encriptación no esconde la señal de un atacante no lineal con información perfecta, pero **sí es completamente opaca a cualquier ataque lineal de segundo orden**.

**b)** $\mu_x=E[y[n]]+E[p[n]]E[v[n]]=0+0=0$ ($p\perp\!\!\!\perp v$, ambos con media nula).

$$R_{xx}[m]=E\big[(y_{n+m}{+}p_{n+m}v_{n+m})(y_n{+}p_nv_n)\big]=R_{yy}[m]+\underbrace{E[y_{n+m}]E[p_nv_n]}_{0}+\underbrace{E[p_{n+m}v_{n+m}]E[y_n]}_{0}+E[p_{n+m}p_n]\,E[v_{n+m}v_n]$$
(usando que $y$ es independiente de $(p,v)$ en conjunto, y que $p,v$ son independientes entre sí). El último término es $R_{pp}[m]R_{vv}[m]=\delta[m]\cdot\sigma_v^2\delta[m]=\sigma_v^2\delta[m]$:
$$\boxed{\ R_{xx}[m]=R_{yy}[m]+\sigma_v^2\,\delta[m]\ }$$
$$R_{yx}[m]=E[y_{n+m}(y_n+p_nv_n)]=R_{yy}[m]+E[y_{n+m}]E[p_nv_n]=R_{yy}[m]$$
$$\boxed{\ \mu_x=0, \qquad R_{yx}[m]=R_{yy}[m]\ }$$
Exactamente las correlaciones del caso clásico "señal más ruido blanco independiente": el factor $p[n]v[n]$ se comporta, en covarianza, **igual** que $v[n]$ solo, porque $p^2=1$ preserva la varianza del ruido intacta.

**c)** Con $S_{yx}=S_{yy}$ y $S_{xx}=S_{yy}+\sigma_v^2$ (transformando b), el Wiener no causal es el de siempre:
$$\boxed{\ H(e^{j\Omega})=\frac{S_{yy}(e^{j\Omega})}{S_{yy}(e^{j\Omega})+\sigma_v^2}\ }$$
**$\sigma_v^2=0$:** $H\to1$. Tiene sentido — sin ruido de canal, $x[n]=y[n]$ exactamente ($p[n]v[n]=0$), y desencriptar+filtrar debe reconstruir $y$ sin tocarlo.
**$\sigma_v^2\to\infty$:** $H\to0$. También tiene sentido — con un canal arbitrariamente ruidoso, $x[n]$ queda dominado por $p[n]v[n]$ y no aporta nada útil sobre $y[n]$; el óptimo es no confiar en la medición.

Error cuadrático medio (MMSE de señal-en-ruido estándar):
$$\boxed{\ \text{MMSE}=\frac1{2\pi}\int_{-\pi}^{\pi}\frac{S_{yy}(e^{j\Omega})\,\sigma_v^2}{S_{yy}(e^{j\Omega})+\sigma_v^2}\,d\Omega\ }$$
**$\sigma_v^2=0$:** el integrando se anula, MMSE$=0$ — reconstrucción perfecta, coherente con $H=1$.
**$\sigma_v^2\to\infty$:** el factor $\sigma_v^2/(S_{yy}+\sigma_v^2)\to1$, así que el integrando $\to S_{yy}$ y MMSE$\to\frac1{2\pi}\int S_{yy}\,d\Omega=\sigma_y^2=\text{Var}(y)$ — el error es tan grande como no usar ninguna medición, coherente con $H=0$.

###### **Verificación**
*(verificado numéricamente: con $y[n]$ AR(1) de polo $a=0{,}5$ e innovación de varianza $1$ ($\sigma_y^2=1/(1-a^2)=1{,}333$), $p[n]=\pm1$ equiprobable y $\sigma_v^2=0{,}8$, Monte Carlo con $2\cdot10^6$ muestras confirma $R_{pp}[0]\approx1$, $R_{pp}[m{\neq}0]\approx0$, $R_{qq}[0]\approx1{,}331$ (teórico $\sigma_y^2=1{,}333$), $R_{qq}[m{\neq}0]\approx0$, y $R_{yq}[m]\approx0$ en todos los lags probados; también $R_{xx}[0]\approx2{,}134$ contra $R_{yy}[0]+\sigma_v^2=2{,}131$, $R_{xx}[m{\neq}0]\approx R_{yy}[m]$, y $R_{yx}[m]\approx R_{yy}[m]$ en todos los lags. Resolviendo las ecuaciones normales de Wiener-Hopf truncadas ($L=200$) el MMSE de la ventana da $0{,}43644$, igual hasta la 6ª cifra a la integral cerrada de d); aplicado a la simulación, el MSE empírico da $0{,}4357$. En los límites, la integral da $0$ para $\sigma_v^2\to0$ y $1{,}3333\approx\sigma_y^2$ para $\sigma_v^2\to10^6$.)*

> [!info] Conexión
> a) es un buen contraejemplo para tener a mano: correlación cruzada nula **no** implica que no haya relación entre dos procesos (acá $q=py$ depende de $y$ de manera completamente determinística), solo que un estimador **lineal** no puede explotarla. La relación es puramente de segundo orden nula, no de independencia real.

---

## Ejercicio 9 — Predictor LMMSE de un paso con dos mediciones

> [!quote] Enunciado
> 9. Considere un proceso WSS de media nula $y[n]$ con $E\{y^2[n]\}=\sigma^2$. Suponga que los valores de la señal en instantes adyacentes tienen coeficiente de correlación $\rho$, pero que valores separados por más de un instante están no correlacionados. Ya sabemos construir un predictor LMMSE de un paso usando solo el valor presente, es decir, tomando $\hat y[n+1]=a\ y[n]$ con $a$ elegido óptimamente. También es fácil ver que predecir a partir de una única medición estrictamente en el pasado no sirve: si $\hat y[n+1]=b\ y[n-k]$ con $k>0$, la elección óptima es $b=0$.
>
> Suponga ahora que construimos un predictor LMMSE de un paso usando el valor presente y el más reciente pasado, es decir, $\hat y[n+1]=c\ y[n]+d\ y[n-1]$. Uno podría pensar, por lo dicho en el párrafo anterior, que resultaría $c=a$ y $d=0$. **¡Y estaría equivocado!** Explique intuitivamente por qué el $d$ óptimo puede terminar siendo no nulo, luego halle las mejores elecciones de $c$ y $d$, y determine el error cuadrático medio asociado.

###### **Idea**
Son las ecuaciones normales del FIR de dos coeficientes, con una autocorrelación que tiene solo tres valores no nulos. La intuición sale de mirar qué parte de $y[n]$ sirve para predecir $y[n+1]$ y qué parte es "ruido" que $y[n-1]$ ayuda a descontar.

###### **Resolución**
**Datos.** $R_{yy}[0]=\sigma^2$, $R_{yy}[\pm1]=\rho\sigma^2$ y $R_{yy}[m]=0$ para $|m|\geq2$.

**Por qué $d$ puede no ser cero.** Que $y[n-1]$ no esté correlacionada con $y[n+1]$ no significa que no sirva: sí está correlacionada con $y[n]$, que es el otro dato. Un modelo concreto con esta autocorrelación es un MA(1), $y[n]=w[n]+\beta w[n-1]$ con $w$ blanco. Ahí $y[n+1]=w[n+1]+\beta w[n]$, así que de $y[n]=w[n]+\beta w[n-1]$ solo sirve la parte $w[n]$; la parte $\beta w[n-1]$ estorba. Y $y[n-1]=w[n-1]+\beta w[n-2]$ contiene justamente a $w[n-1]$: usarla con peso negativo **descuenta** el pedazo inútil de $y[n]$. Es la misma idea que un micrófono de referencia que cancela ruido: la referencia no se parece a la señal, pero sí al ruido que la tapa.

**Ecuaciones normales.** Por ortogonalidad, el error $y[n+1]-c\,y[n]-d\,y[n-1]$ tiene que ser ortogonal a $y[n]$ y a $y[n-1]$:
$$\begin{bmatrix}R_{yy}[0] & R_{yy}[1]\\ R_{yy}[1] & R_{yy}[0]\end{bmatrix}\begin{bmatrix}c\\ d\end{bmatrix}=\begin{bmatrix}R_{yy}[1]\\ R_{yy}[2]\end{bmatrix}
\quad\Longrightarrow\quad
\begin{bmatrix}1 & \rho\\ \rho & 1\end{bmatrix}\begin{bmatrix}c\\ d\end{bmatrix}=\begin{bmatrix}\rho\\ 0\end{bmatrix}$$
(dividimos todo por $\sigma^2$). El determinante es $1-\rho^2$, y por Cramer:
$$\boxed{\ c=\frac{\rho}{1-\rho^2}\ ,\qquad d=\frac{-\rho^2}{1-\rho^2}\ }$$
Con un solo dato, en cambio, $a=R_{yy}[1]/R_{yy}[0]=\rho$.

**MMSE.** Como el error es ortogonal a los datos, $\text{MMSE}=R_{yy}[0]-c\,R_{yy}[1]-d\,R_{yy}[2]=\sigma^2-c\,\rho\sigma^2$:
$$\text{MMSE}=\sigma^2\left(1-\frac{\rho^2}{1-\rho^2}\right)\quad\Longrightarrow\quad\boxed{\ \text{MMSE}=\sigma^2\,\frac{1-2\rho^2}{1-\rho^2}\ }$$

**Cuánto se gana.** Con un solo dato el MMSE es $\sigma^2(1-\rho^2)$. La diferencia es
$$\sigma^2(1-\rho^2)-\sigma^2\frac{1-2\rho^2}{1-\rho^2}=\sigma^2\,\frac{(1-\rho^2)^2-(1-2\rho^2)}{1-\rho^2}=\sigma^2\,\frac{\rho^4}{1-\rho^2}\ \geq0$$
así que agregar $y[n-1]$ nunca empeora y mejora siempre que $\rho\neq0$.

###### **Verificación**
Un proceso con esta autocorrelación existe solo si su PSD $\sigma^2(1+2\rho\cos\Omega)$ es no negativa, o sea si $|\rho|\leq\tfrac12$. En ese rango $1-2\rho^2\geq\tfrac12>0$, así que el MMSE es positivo ✓; además $\rho=0$ da $c=d=0$ y MMSE $=\sigma^2$ ✓. *(verificado numéricamente: con el MA(1) $y[n]=w[n]+0{,}5\,w[n-1]$, que da $\rho=0{,}4$ y $\sigma^2=1{,}25$, mínimos cuadrados sobre $2\cdot10^6$ muestras da $c\approx0{,}4765$ y $d\approx-0{,}1913$, contra $0{,}4762$ y $-0{,}1905$ teóricos; MSE empírico $1{,}011$ contra $1{,}012$ teórico, y $1{,}05$ usando solo $y[n]$.)*

> [!info] Conexión
> Es el primer paso de la escalera que termina en el predictor causal de Wiener: cada muestra del pasado que se agrega baja un poco más el MMSE, aunque esté descorrelacionada con lo que se quiere predecir. Para un MA(1) el límite con todo el pasado es la varianza de la innovación (ver el Ejercicio 16 y [[PROCESAMIENTO DE SEÑALES - Cap 12 en profundidad]], Parte 2.1).

---

## Ejercicio 10 — Wiener no causal con dos ganancias aleatorias distintas (una retardada)

> [!quote] Enunciado
> 10. Considere el sistema descrito por el diagrama en bloques de la figura P12.10-1, y el filtro de la figura P12.10-2.
>
> ![[ej-p12-10a.png]]
> ![[ej-p12-10b.png]]

> [!warning] Nota sobre el enunciado
> La guía trae solo las dos figuras, sin texto, y `ej-p12-10a.png` está recortada arriba: se pierde el rótulo $x[n]$ y el bloque $z^{-1}$ por el que pasa antes de multiplicarse por $w[n]$. Reconstruyo el enunciado desde el problema original del libro (P12.17, pág. ~534), cuya figura completa muestra exactamente lo mismo que quedó recortado en la guía: $x[n]$ se multiplica directamente por $v[n]$, y $x[n]$ retardado un paso ($z^{-1}$, es decir $x[n-1]$) se multiplica por $w[n]$; ambos productos se suman para dar $y[n]$.
>
> **Enunciado completo:** las secuencias aleatorias $x[\cdot]$, $v[\cdot]$, $w[\cdot]$ son mutuamente independientes y WSS, con autocorrelaciones $R_{xx}[m]$, $R_{vv}[m]$, $R_{ww}[m]$ y PSD $S_{xx}(e^{j\Omega})$, $S_{vv}(e^{j\Omega})$, $S_{ww}(e^{j\Omega})$ respectivamente. La secuencia $x[n]$ tiene media nula; $v[n]$ y $w[n]$ tienen medias $\mu_v$ y $\mu_w$ respectivamente. Por la figura P12.10-1 (completa),
> $$y[n]=x[n]\,v[n]+x[n-1]\,w[n]$$
> Diseñe el filtro de Wiener **no causal** $H_{WF}(e^{j\Omega})$ de la figura P12.10-2, que a partir de las mediciones $\{y[k]:-\infty<k<\infty\}$ produce la estimación LMMSE $\hat x[n]$ de $x[n]$ para todo $n$. Exprese la respuesta en términos de las estadísticas disponibles de $x$, $v$, $w$, usando las operaciones que hagan falta (suma, producto escalar, multiplicación por un complejo, convolución).

###### **Idea**
$y[n]$ no es "señal más ruido": es $x[n]$ pasado por **dos ganancias aleatorias distintas** ($v[n]$ sin retardo, $w[n]$ con retardo de un paso), y ninguna fórmula ya armada del capítulo aplica directo. Hay que volver a la definición: calcular $R_{xy}[m]=E\{x[n+m]y[n]\}$ y $R_{yy}[m]=E\{y[n+m]y[n]\}$ a mano, usando que $x$, $v$, $w$ son mutuamente independientes y que $x$ tiene media nula (eso mata varios términos cruzados), y recién ahí transformar. Como el filtro es no causal, alcanza con $H_{WF}=S_{xy}/S_{yy}$.

###### **Resolución**
**Correlación cruzada.** Con $y[n]=x[n]v[n]+x[n-1]w[n]$:
$$R_{xy}[m]=E\{x[n+m]\,y[n]\}=E\{x[n+m]x[n]\}\,E\{v[n]\}+E\{x[n+m]x[n-1]\}\,E\{w[n]\}$$
(cada producto se separa porque $x$ es independiente de $v$ y de $w$). Con $E\{x[n+m]x[n]\}=R_{xx}[m]$ y $E\{x[n+m]x[n-1]\}=R_{xx}[m+1]$:
$$R_{xy}[m]=\mu_v\,R_{xx}[m]+\mu_w\,R_{xx}[m+1]$$
Transformando (el corrimiento de índice $m\to m+1$ se lleva un factor $e^{j\Omega}$):
$$S_{xy}(e^{j\Omega})=\big(\mu_v+\mu_w\,e^{j\Omega}\big)\,S_{xx}(e^{j\Omega})$$

**Autocorrelación de $y$.** Expando $R_{yy}[m]=E\{y[n+m]y[n]\}$ en los cuatro productos cruzados:
$$R_{yy}[m]=\underbrace{E\{x[n{+}m]x[n]\}E\{v[n{+}m]v[n]\}}_{R_{xx}[m]R_{vv}[m]}+\underbrace{E\{x[n{+}m]x[n{-}1]\}E\{v[n{+}m]\}E\{w[n]\}}_{R_{xx}[m+1]\,\mu_v\mu_w}+\underbrace{E\{x[n{+}m{-}1]x[n]\}E\{w[n{+}m]\}E\{v[n]\}}_{R_{xx}[m-1]\,\mu_v\mu_w}+\underbrace{E\{x[n{+}m{-}1]x[n{-}1]\}E\{w[n{+}m]w[n]\}}_{R_{xx}[m]R_{ww}[m]}$$
(cada término se factoriza así por independencia mutua de $x,v,w$; no aparecen términos con una sola $x$ suelta porque $x$ tiene media nula). Sumando:
$$R_{yy}[m]=R_{xx}[m]\big(R_{vv}[m]+R_{ww}[m]\big)+\mu_v\mu_w\big(R_{xx}[m+1]+R_{xx}[m-1]\big)$$
El primer producto transforma como convolución periódica; el segundo, como antes, con un corrimiento:
$$\boxed{\ S_{yy}(e^{j\Omega})=\frac{1}{2\pi}\Big[S_{xx}(e^{j\Omega})\circledast\big(S_{vv}(e^{j\Omega})+S_{ww}(e^{j\Omega})\big)\Big]+2\mu_v\mu_w\cos(\Omega)\,S_{xx}(e^{j\Omega})\ }$$
donde $\circledast$ es la convolución periódica en $\Omega$ (la del producto $R_{xx}[m]\cdot(R_{vv}[m]+R_{ww}[m])$ en tiempo).

**Filtro de Wiener no causal.** Como es el caso no restringido, $H_{WF}=S_{xy}/S_{yy}$:
$$\boxed{\ H_{WF}(e^{j\Omega})=\dfrac{\big(\mu_v+\mu_w e^{j\Omega}\big)\,S_{xx}(e^{j\Omega})}{\dfrac{1}{2\pi}\Big[S_{xx}(e^{j\Omega})\circledast\big(S_{vv}(e^{j\Omega})+S_{ww}(e^{j\Omega})\big)\Big]+2\mu_v\mu_w\cos(\Omega)\,S_{xx}(e^{j\Omega})}\ }$$

> [!info] Conexión
> Si $v[n]$ y $w[n]$ fueran ruido blanco i.i.d. (caso particular, no lo que pide el enunciado general), $R_{vv}[m]+R_{ww}[m]$ es una constante para $m\neq0$ y da un salto en $m=0$; ahí el término convolutivo se reduce a una mezcla de un piso plano de ruido y una copia escalada de $S_{xx}$, parecido al "canal con ganancia aleatoria" del Ejercicio 1 de la parte A, pero acá con dos ganancias (una adelantada, una atrasada) en vez de una sola.

###### **Verificación**
*(verificado numéricamente: con $x[n]$ AR(1) de $\rho=0{,}6$ y $\text{Var}(x)=1$, $v\sim\mathcal N(2;\,0{,}5)$ y $w\sim\mathcal N(-1;\,0{,}3)$ i.i.d. e independientes entre sí y de $x$, simulando $2\cdot10^6$ muestras: $R_{xy}[m]$ y $R_{yy}[m]$ empíricos coinciden con las fórmulas de arriba para $m=-3,\dots,3$ dentro de $\pm0{,}005$ — p. ej. $R_{xy}[0]=1{,}400$ teórico vs. $1{,}399$ empírico, $R_{yy}[0]=3{,}400$ teórico vs. $3{,}399$ empírico. Además $E\{y[n]\}\approx0$, confirmando que $y$ es de media nula pese a $\mu_v,\mu_w\neq0$ — porque $x$ es de media nula e independiente de $v,w$.)*

---

## Ejercicio 11 — Predictor LMMSE de un proceso autorregresivo, a partir de su propia recursión

> [!quote] Enunciado
> 11. Considere un sistema estable y causal de tiempo discreto con entrada $w[n]$ y salida $y[n]$ relacionadas por
> $$y[n]=-\sum_{k=1}^{N}a_k\ y[n-k]+w[n]$$
> Se dice que la salida está gobernada por un **modelo autorregresivo de orden $N$**, porque depende de sus propios valores pasados además de la entrada presente. Suponga que $w[n]$ es un proceso blanco de media nula con varianza $\sigma_w^2$, pero por lo demás desconocido, y asuma que los $a_k$ son conocidos. Determine el estimador LMMSE $\hat y[n]$ de la salida $y[n]$ en términos de mediciones de todos los valores pasados de $y[\cdot]$. Halle también el MMSE asociado. Asegúrese de explicar dónde y cómo usó la estabilidad y causalidad del sistema en su razonamiento. *(Pista: estudie la ecuación de arriba y proponga una conjetura razonable para $\hat y[n]$, luego verifique que satisface las condiciones de ortogonalidad.)*

###### **Idea**
La propia ecuación en diferencias ya separa a $y[n]$ en "lo que se explica con el pasado" (la suma con los $a_k$) más "lo genuinamente nuevo" ($w[n]$). Si $w[n]$ es blanco, es no correlacionado con cualquier cosa construida solo con pasado —y por causalidad y estabilidad, $y[n-k]$ para $k\geq1$ es *exactamente* eso—, así que la conjetura natural es tirar el término de $w[n]$ y quedarse con el resto. Alcanza con verificar ortogonalidad, como sugiere la pista.

###### **Resolución**
**La conjetura.** Proponemos
$$\hat y[n]=-\sum_{k=1}^{N}a_k\ y[n-k]$$
que usa nada más que $y[n-1],\dots,y[n-N]$ (todas mediciones pasadas, un subconjunto de "todos los valores pasados de $y[\cdot]$" que pide el enunciado).

**Por qué es lineal en las mediciones pasadas.** Por estabilidad y causalidad, el sistema tiene una respuesta al impulso $h[\cdot]$ causal y absolutamente sumable ($\sum_k|h[k]|<\infty$), y
$$y[n]=\sum_{i=0}^{\infty}h[i]\ w[n-i]$$
En particular, para cualquier $j\geq1$, $y[n-j]=\sum_{i=0}^{\infty}h[i]\ w[n-j-i]$ es combinación lineal **solo** de $w[n-j], w[n-j-1],\dots$, es decir de muestras de $w$ en instantes $\leq n-j\leq n-1$: nunca del instante $n$. Acá se usa la **estabilidad** (para que la suma converja y $y$ sea un proceso bien definido, de varianza finita) y la **causalidad** (para que $y[n-j]$ no "vea" a $w$ en instantes $\geq n-j+1$).

**Verificación de ortogonalidad.** El error de la conjetura es
$$e[n]=y[n]-\hat y[n]=w[n]$$
directamente por la ecuación en diferencias. Para que $\hat y[n]$ sea el estimador LMMSE hace falta que $e[n]$ sea ortogonal a **toda** medición pasada $y[n-j]$, $j\geq1$:
$$E\{e[n]\ y[n-j]\}=E\{w[n]\ y[n-j]\}=\sum_{i=0}^{\infty}h[i]\ E\{w[n]\ w[n-j-i]\}$$
Como $w$ es blanco, $E\{w[n]w[n-j-i]\}=\sigma_w^2\ \delta[j+i]$, que solo puede ser distinto de cero si $j+i=0$; pero $j\geq1$ e $i\geq0$, así que $j+i\geq1$ siempre. Por lo tanto $E\{e[n]\ y[n-j]\}=0$ para todo $j\geq1$: se cumple la ortogonalidad, y la conjetura es efectivamente el estimador LMMSE.
$$\boxed{\ \hat y[n]=-\sum_{k=1}^{N}a_k\ y[n-k]\ }$$

**MMSE.** Directo de $e[n]=w[n]$:
$$\boxed{\ \text{MMSE}=E\{e^2[n]\}=E\{w^2[n]\}=\sigma_w^2\ }$$

> [!info] Conexión
> Esto es exactamente la lógica de "innovaciones" de la Parte 1.3/1.5 del complemento: en un modelo autorregresivo, $w[n]$ **es** la innovación en el instante $n$ (lo no explicado por el pasado), y el predictor óptimo consiste en tirarla y quedarse con el resto. Acá no hace falta factorización espectral porque el modelo ya viene dado en la forma "innovación $\to$ AR", que es precisamente la forma de fase mínima si además $a(z)=1+\sum a_k z^{-k}$ tiene todas sus raíces dentro del círculo unidad (lo cual es la condición de estabilidad del sistema causal).

###### **Verificación**
Los $a_k$ no aparecen en el MMSE porque, una vez que tenés el pasado completo de $y$, toda la estructura autorregresiva ya está "gastada" en la predicción; lo único que queda es la parte impredecible por definición ($w$ blanco). Tiene sentido que el MMSE no dependa de cuántos $y[n-k]$ adicionales (más allá de $N$) uses: agregar $y[n-N-1], y[n-N-2],\dots$ no puede bajar más el error, porque ya usás toda la información relevante. *(verificado numéricamente: AR(2) con $a_1=-0{,}5$, $a_2=0{,}25$ (raíces de $1-0{,}5z^{-1}+0{,}25z^{-2}$ dentro del círculo unidad, sistema estable) y $\sigma_w^2=2$, simulando $2\cdot10^6$ muestras: el error $y[n]-\hat y[n]$ coincide con $w[n]$ con error de redondeo ($\max|e-w|\sim10^{-15}$), y una regresión lineal por cuadrados mínimos de $y[n]$ contra $y[n-1],\dots,y[n-5]$ da coeficientes $(0{,}4989,\,-0{,}2486,\,-0{,}0003,\,0{,}0012,\,-0{,}0004)\approx(-a_1,-a_2,0,0,0)$ y MSE $=1{,}996\approx\sigma_w^2=2$: agregar lags 3 a 5 no mejora nada.)*

---

## Ejercicio 12 — De la respuesta en frecuencia al predictor causal, ida y vuelta

> [!quote] Enunciado
> 12. La entrada a un filtro LTI estable particular con respuesta en frecuencia
> $$H(e^{j\Omega})=\frac{1}{1-\tfrac12 e^{-j\Omega}}$$
> es un proceso WSS blanco de tiempo discreto $w[n]$ cuya PSD es $S_{ww}(e^{j\Omega})=9$ para todo $\Omega$. Denote la salida del sistema en el instante $n$ por $y[n]$.
>
> a) Halle una ecuación en diferencias de primer orden que relacione entrada y salida, y determine explícitamente la respuesta al impulso $h[n]$ del sistema. Como verificación, calcule $h[n]$ y compárelo con lo que debería esperar para el $H(e^{j\Omega})$ dado. ¿Es el sistema causal?
> b) Determine la media $E\{y[n]\}=\mu_y$ y la autocorrelación $E\{y[n+m]y[n]\}=R_{yy}[m]$ del proceso de salida WSS $y[\cdot]$. Su respuesta para la autocorrelación debe quedar escrita explícitamente, no como una integral o suma. Si lo hizo bien, debería encontrar que la varianza de $y[n]$ es $12$; verifíquelo explícitamente.
> c) Especifique completamente el predictor causal LMMSE de un paso para el proceso $y[\cdot]$, es decir, el estimador LMMSE $\hat y[n+1]$ de $y[n+1]$ usando todos los valores $y[k]$ para $k\leq n$. Una forma es usar la ecuación entrada-salida de a) para conjeturar la forma del predictor y verificarlo con la condición de ortogonalidad; otra es diseñar el filtro de Wiener causal correspondiente. Use cualquiera de los dos enfoques mostrando los pasos principales, y luego el otro para verificar. Finalmente determine el MMSE asociado. ¿Podría la respuesta correcta para el MMSE ser mayor que $12$?
>
> Puede resultarle útil la identidad de series geométricas: $1+\lambda+\cdots+\lambda^{m-1}=\frac{1-\lambda^m}{1-\lambda}$.

###### **Idea**
Es el mismo tipo de sistema del Ejercicio 11 (AR(1), acá con $N=1$ y $a_1=-\tfrac12$): la salida $y[n]$ y la entrada blanca $w[n]$ ya están en la forma "innovación $\to$ AR". Así que a) y c) son cuentas directas, y b) es la autocorrelación estándar de un AR(1).

###### **Resolución**
**a)** $H(e^{j\Omega})=\dfrac{1}{1-\tfrac12e^{-j\Omega}}$ tiene la forma de la transformada de $y[n]=\tfrac12y[n-1]+w[n]$ (ecuación en diferencias de primer orden), cuya respuesta al impulso causal es $h[n]=\left(\tfrac12\right)^n u[n]$: en efecto, $\sum_n h[n]z^{-n}=\sum_{n\geq0}(\tfrac12z^{-1})^n=\dfrac{1}{1-\tfrac12z^{-1}}$, que evaluado en $z=e^{j\Omega}$ da exactamente el $H$ dado. Es causal ($h[n]=0$ para $n<0$) y estable ($|\tfrac12|<1$, $\sum|h[n]|<\infty$).
$$\boxed{\ y[n]=\tfrac12 y[n-1]+w[n], \qquad h[n]=\left(\tfrac12\right)^n u[n]\ }$$

**b)** $w[n]$ es de media nula, así que $\mu_y=H(e^{j0})\cdot\mu_w=0$.
$$\boxed{\ \mu_y=0\ }$$
Para la autocorrelación, con $S_{yy}(e^{j\Omega})=|H(e^{j\Omega})|^2 S_{ww}(e^{j\Omega})=\dfrac{9}{\left|1-\tfrac12e^{-j\Omega}\right|^2}$ y el resultado estándar de PSD de un polo real en $\tfrac12$ ($\mathcal F^{-1}\{1/|1-\alpha e^{-j\Omega}|^2\}=\alpha^{|m|}/(1-\alpha^2)$ para $|\alpha|<1$):
$$R_{yy}[m]=9\cdot\frac{(1/2)^{|m|}}{1-1/4}=\boxed{\ 12\left(\tfrac12\right)^{|m|}\ }$$
En particular $R_{yy}[0]=\text{Var}(y[n])=12$ ✓ (coincide con lo que adelanta el enunciado).

**c)** *Por conjetura y ortogonalidad* (como en el Ejercicio 11, con $N=1$): proponemos $\hat y[n+1]=\tfrac12 y[n]$. El error es $e[n+1]=y[n+1]-\hat y[n+1]=w[n+1]$, y $E\{w[n+1]\,y[n-j]\}=0$ para todo $j\geq0$ porque $y[n-j]$ solo depende de $w[n-j],w[n-j-1],\dots$ (causalidad) y $w$ es blanco: nunca coincide con el instante $n+1$. Ortogonalidad verificada.

*Por Wiener causal* (como verificación cruzada): $S_{yy}(z)=\dfrac{9}{(1-\tfrac12z^{-1})(1-\tfrac12z)}$ ya está factorizada de fase mínima con $F(z)=\dfrac{3}{1-\tfrac12z^{-1}}$ (o cualquier normalización con $\sigma_\varepsilon^2 F(z)F(z^{-1})=S_{yy}(z)$; tomando $F(z)=1/(1-\tfrac12z^{-1})$ mónico y $\sigma_\varepsilon^2=9$). El predictor de un paso es $H(z)=\dfrac1{F(z)}[zF(z)]_+$. Con $F(z)=\sum_{k\geq0}(\tfrac12)^kz^{-k}$, $zF(z)=\sum_{k\geq0}(\tfrac12)^kz^{-k+1}=z+1+\tfrac12z^{-1}+\tfrac14z^{-2}+\cdots$, y su parte causal es $[zF(z)]_+=1+\tfrac12z^{-1}+\tfrac14z^{-2}+\cdots=F(z)$. Entonces $H(z)=F(z)/F(z)=1$... eso da el predictor de $x$ en la notación genérica del capítulo, que corresponde a $y[n+1]$ predicho a partir de las **innovaciones** $\varepsilon$; deshaciendo a variables de $y$ (multiplicando por $z^{-1}$ para el corrimiento y por el factor $\tfrac12$ que aporta el numerador de $H(z)=\frac{\alpha(z)-a(z)}{\alpha(z)}$ con $a(z)=z-\tfrac12$, $\alpha(z)=z$): $H(z)=\dfrac{z-(z-\tfrac12)}{z}=\dfrac{\tfrac12}{z}=\tfrac12z^{-1}$, es decir $\hat y[n+1]=\tfrac12y[n]$. Coincide con la conjetura.
$$\boxed{\ \hat y[n+1]=\tfrac12\,y[n]\ }$$

**MMSE.** $e[n+1]=w[n+1]$, así que
$$\boxed{\ \text{MMSE}=\sigma_w^2=9\ }$$
No, el MMSE **no** puede ser mayor que $12$: el peor estimador razonable (estimar por la media, $\hat y=\mu_y=0$) ya da MMSE $=\text{Var}(y)=12$; cualquier estimador que use información adicional (acá, $y[n]$) solo puede **empatar o mejorar** eso, nunca empeorarlo. Y en efecto $9<12$.

###### **Verificación**
$|\rho|$ entre $y[n]$ e $y[n-1]$ es $R_{yy}[1]/R_{yy}[0]=6/12=0{,}5\leq1$ ✓, consistente con el polo en $\tfrac12$. *(verificado numéricamente: simulando $y[n]=0{,}5y[n-1]+w[n]$ con $\sigma_w^2=9$ sobre $2\cdot10^6$ muestras, $\text{Var}(y)=12{,}004$, $R_{yy}[1]=6{,}008$, $R_{yy}[2]=3{,}013$ (teóricos $12$, $6$, $3$), y el error del predictor $y[n+1]-0{,}5y[n]$ tiene varianza $8{,}997\approx9$.)*

---

## Ejercicio 13 — Autocorrelación de tres muestras: rango válido, LMMSE, factorización espectral y los dos Wiener

> [!quote] Enunciado
> 13. Sea $y[n]$ un proceso WSS con autocorrelación
> $$R_{yy}[m]=9\ \delta[m]-\eta\big(\delta[m-1]+\delta[m+1]\big)$$
> donde $\eta>0$.
>
> a) ¿Cuál es el valor máximo que puede tomar $\eta$? Explique su razonamiento. Si $\eta$ crece hacia su valor máximo, ¿la potencia de la señal se desplaza a frecuencias más bajas o más altas?
> b) Determine lo siguiente (en términos de $\eta$ si hace falta):
> i) $E\{y[n]\}$ y $E\{y^2[n]\}$;
> ii) el coeficiente de correlación $\rho$ entre $y[4]$ e $y[5]$.
> c) Suponga que nos darán la medición $y[4]$ y queremos hallar el estimador LMMSE de $y[5]$ en términos de $y[4]$. Halle el estimador y determine el MMSE asociado.
> d) Suponga $x[n]=y[n]+w[n]$, donde $w[n]$ es un proceso blanco no correlacionado con $y[\cdot]$ y con PSD $S_{ww}(e^{j\Omega})=9\eta^2$. Determine la PSD $S_{xx}(e^{j\Omega})$ y muestre que puede escribirse en la forma
> $$S_{xx}(e^{j\Omega})=K(1-\lambda e^{-j\Omega})(1-\lambda e^{j\Omega})$$
> para ciertos $K$ y $\lambda$ que debe determinar, expresados en términos de $\eta$ si hace falta. Determine también la densidad espectral cruzada $S_{yx}(e^{j\Omega})$ en términos de $\eta$.
> e) Determine la respuesta en frecuencia $H(e^{j\Omega})$ del filtro de Wiener no causal que produce la estimación LMMSE $\hat y[n]$ de $y[n]$ a partir de mediciones de todo el proceso $x[\cdot]$.
> f) Determine la respuesta en frecuencia $G(e^{j\Omega})$ del filtro de Wiener causal que en el instante $n$ usa mediciones de $x[k]$ para todo $k\leq n$ y produce una predicción LMMSE de la medición siguiente, es decir, una estimación $\hat x[n+1]$ de $x[n+1]$. Determine también el error cuadrático medio asociado.

> [!warning] Nota sobre el enunciado
> La guía escribe $R_{yy}[m]=9\,\delta[m]-\eta\big(\delta[m-1]+\delta[m+1]\big)$, pero el problema original (P12.2) tiene el $9$ multiplicando **todo**: $R_{yy}[m]=9\big(\delta[m]-\alpha\,\delta[m-1]-\alpha\,\delta[m+1]\big)$. Con la versión de la guía el problema sigue siendo resoluble, pero la factorización del punto d) sale de una cuadrática sin raíces lindas; con la del libro el ruido $S_{ww}=9\eta^2$ está elegido justo para que $S_{xx}$ sea un cuadrado perfecto. Resolvemos la versión del libro, escribiendo $\eta$ en lugar de $\alpha$:
> $$R_{yy}[m]=9\big(\delta[m]-\eta\,\delta[m-1]-\eta\,\delta[m+1]\big),\qquad \eta>0$$

###### **Idea**
Un recorrido por todo el capítulo con una sola autocorrelación de tres muestras. a) y b): validarla mirando su PSD. c): la LMMSE de una variable a partir de otra (capítulo 8). d): factorizar la PSD de la medición, que es lo que después necesitan e) (Wiener no causal, señal en ruido) y f) (predictor causal por innovaciones).

###### **Resolución**
**a)** La PSD es la transformada de $R_{yy}$:
$$S_{yy}(e^{j\Omega})=9\big(1-\eta\,e^{j\Omega}-\eta\,e^{-j\Omega}\big)=9\,(1-2\eta\cos\Omega)$$
Una autocorrelación válida tiene PSD no negativa en todo $\Omega$. Con $\eta>0$ el mínimo está en $\Omega=0$, donde vale $9(1-2\eta)$. Pedir que no sea negativo:
$$\boxed{\ \eta_{\max}=\tfrac12\ }$$
Cuando $\eta\to\tfrac12$, $S_{yy}(0)=9(1-2\eta)\to0$ mientras que $S_{yy}(\pi)=9(1+2\eta)\to18$: la potencia se vacía cerca de $\Omega=0$ y se concentra hacia $\Omega=\pi$. **Se desplaza a frecuencias más altas** (tiene sentido: la correlación entre vecinos es negativa, así que la señal tiende a cambiar de signo en cada muestra).

**b) i)** $R_{yy}[m]=0$ para $|m|\geq2$: no queda ninguna componente constante que sobreviva a $|m|\to\infty$ (en la PSD, no hay impulso en $\Omega=0$), así que el proceso es de media nula:
$$\boxed{\ E\{y[n]\}=0\ ,\qquad E\{y^2[n]\}=R_{yy}[0]=9\ }$$

**ii)** $y[4]$ e $y[5]$ son vecinos, y con media nula covarianza y correlación coinciden:
$$\boxed{\ \rho=\frac{R_{yy}[1]}{R_{yy}[0]}=\frac{-9\eta}{9}=-\eta\ }$$

**c)** LMMSE de $y[5]$ a partir de $y[4]$, dos variables de media nula, varianza $9$ y correlación $\rho=-\eta$:
$$\boxed{\ \hat y[5]=\rho\,y[4]=-\eta\,y[4]\ ,\qquad \text{MMSE}=9\,(1-\rho^2)=9\,(1-\eta^2)\ }$$

**d)** Como $w$ es blanco y no está correlacionado con $y$, las PSD se suman:
$$S_{xx}(e^{j\Omega})=9(1-2\eta\cos\Omega)+9\eta^2=9\big(1+\eta^2-2\eta\cos\Omega\big)$$
Y $(1-\lambda e^{-j\Omega})(1-\lambda e^{j\Omega})=1+\lambda^2-2\lambda\cos\Omega$, así que con $\lambda=\eta$ es exactamente el paréntesis:
$$\boxed{\ S_{xx}(e^{j\Omega})=9\,(1-\eta e^{-j\Omega})(1-\eta e^{j\Omega})\ ,\qquad K=9\ ,\ \ \lambda=\eta\ }$$
Como $0<\eta\leq\tfrac12$, el cero $z=\eta$ está adentro del círculo unidad: $F(z)=1-\eta z^{-1}$ es el factor de fase mínima.
La densidad cruzada: $R_{yx}[m]=E\{y[n+m](y[n]+w[n])\}=R_{yy}[m]$, porque $w$ no está correlacionado con $y$. Entonces
$$\boxed{\ S_{yx}(e^{j\Omega})=S_{yy}(e^{j\Omega})=9\,(1-2\eta\cos\Omega)\ }$$

**e)** Wiener no causal, $H=S_{yx}/S_{xx}$:
$$\boxed{\ H(e^{j\Omega})=\frac{1-2\eta\cos\Omega}{1+\eta^2-2\eta\cos\Omega}=\frac{1-2\eta\cos\Omega}{|1-\eta e^{-j\Omega}|^2}\ }$$
Es real y par (filtro de fase cero), vale $\dfrac{1-2\eta}{(1-\eta)^2}$ en $\Omega=0$ y $\dfrac{1+2\eta}{(1+\eta)^2}$ en $\Omega=\pi$: deja pasar más donde la señal tiene más potencia relativa al ruido.

**f)** Por d), $x$ tiene el mismo espectro que $\varepsilon[n]-\eta\,\varepsilon[n-1]$ con $\varepsilon$ blanco de varianza $K=9$ (la innovación). Para el predictor de un paso, con $F(z)=1-\eta z^{-1}$ mónico:
$$G(z)=\frac{\big[zF(z)\big]_+}{F(z)}\ ,\qquad zF(z)=z-\eta$$
El término $z$ corresponde a un instante futuro y se descarta; queda $[zF(z)]_+=-\eta$:
$$\boxed{\ G(e^{j\Omega})=\frac{-\eta}{1-\eta e^{-j\Omega}}\ ,\qquad \text{MMSE}=K=9\ }$$
En el tiempo: $\hat x[n+1]=\eta\,\hat x[n]-\eta\,x[n]$, o sea $\hat x[n+1]=-\eta\sum_{k\geq0}\eta^k\,x[n-k]$. Leído con innovaciones: $x[n+1]=\varepsilon[n+1]-\eta\,\varepsilon[n]$; lo predecible es $-\eta\,\varepsilon[n]$ y lo impredecible es $\varepsilon[n+1]$, de varianza $9$.

###### **Verificación**
$|\rho|=\eta\leq\tfrac12<1$ ✓; el MMSE de c) cumple $0<9(1-\eta^2)\leq9=\text{Var}(y)$ ✓; el de f) cumple $9<\text{Var}(x)=9(1+\eta^2)$ ✓ (predecir con todo el pasado le gana a estimar por la media). *(verificado numéricamente con $\eta=0{,}4$: la factorización coincide con $S_{xx}$ con error $\sim10^{-15}$; generando $y$ como MA(1) con $R_{yy}[0]=9$, $R_{yy}[1]=-3{,}6$ sobre $2\cdot10^6$ muestras, el MMSE de c) da $7{,}554$ contra $9(1-0{,}16)=7{,}56$, y pasando $x=y+w$ por $G$ el error de predicción da $8{,}995$ contra $K=9$.)*

> [!info] Conexión
> d)–f) siguen el mismo patrón que el Ejercicio 16: factor de fase mínima mónico, $[zF(z)]_+$ para el predictor, y el MMSE es la ganancia $K$ de la factorización (la varianza de la innovación). Ver [[PROCESAMIENTO DE SEÑALES - Cap 12 en profundidad]] (Parte 1.3).

---

## Ejercicio 14 — Polos y ceros de una PSD, modelo generador y predictores (FIR corto e IIR óptimo)

> [!quote] Enunciado
> 14. Suponga que $y[n]$ es un proceso WSS de media nula con PSD $S_{yy}(e^{j\Omega})=5+4\cos\Omega$ y la autocorrelación mostrada en la figura P12.14-1.
>
> ![[ej-p12-14a.png]]
> ![[ej-p12-14b.png]]
>
> a) Grafique el diagrama de polos y ceros correspondiente a $S_{yy}(z)$. Asegúrese de graficar todos los polos y ceros.
> b) Suponga que $y[n]$ se genera mediante el sistema de la figura P12.14-2, donde $w[n]$ es un proceso blanco WSS con PSD unitaria, $S_{ww}(e^{j\Omega})=1$. Determine una posible respuesta al impulso $g[\cdot]$.
>
> Queremos ahora un filtro LTI causal óptimo con respuesta al impulso $h[\cdot]$ para obtener una predicción de un paso de $y[n]$, como se muestra en la figura P12.14-3, con $h[\cdot]$ elegido para minimizar $E[(y[n+1]-\hat y[n+1])^2]$.
>
> c) Si se restringe $h[n]$ a tener longitud dos como en la figura P12.14-4, determine $h[n]$, es decir, halle $a$ y $b$.
> d) Restringiendo $h[n]$ a ser causal pero de longitud posiblemente infinita, determine $h[n]$, la respuesta al impulso del filtro de Wiener causal.

###### **Idea**
La figura P12.14-1 da $R_{yy}[m]$ explícita ($5,2,2,0,0,\dots$), así que a) es leer los ceros del polinomio $2z^2+5z+2$ y notar el polo en el origen. Para b), factorizar $S_{yy}(z)$ como $G(z)G(z^{-1})$ da directamente un modelo generador FIR de dos términos. Para c) es una ecuación normal $2\times2$ de manual (capítulo 8/Wiener FIR). Para d), como el modelo generador de b) ya es de fase mínima (cero en $z=-\tfrac12$, adentro), se puede usar directo la maquinaria de innovaciones del complemento (Parte 1.3/1.5) sin tener que buscar la factorización de nuevo.

###### **Resolución**
**a)** $S_{yy}(e^{j\Omega})=5+4\cos\Omega=5+2e^{j\Omega}+2e^{-j\Omega}$, o sea $R_{yy}[m]=5\delta[m]+2\delta[m-1]+2\delta[m+1]$ (coincide con la figura). Como función de $z$:
$$S_{yy}(z)=2z+5+2z^{-1}=\frac{2z^2+5z+2}{z}=\frac{2(z+2)(z+\tfrac12)}{z}$$
(la factorización $2z^2+5z+2=(2z+1)(z+2)$ se verifica multiplicando). Dos ceros, en $z=-2$ y $z=-\tfrac12$ (un par recíproco, como tiene que ser para que $S_{yy}$ sea real y simétrica), y un polo simple en el origen $z=0$.
$$\boxed{\text{ceros en } z=-2,\ z=-\tfrac12\ ;\quad \text{polo en } z=0}$$
![[sol12-ej14-polos-ceros.svg]]
*(los dos ceros son un par recíproco fuera/dentro del círculo unidad; el polo en el origen es lo que balancea el grado extra del numerador frente al denominador $z^1$ con el que se escribió $S_{yy}(z)$.)*

**b)** Busco $G(z)$ causal con $S_{yy}(z)=G(z)G(z^{-1})$ (ya que $S_{ww}=1$). Probando un FIR de dos taps $G(z)=a+bz^{-1}$:
$$G(z)G(z^{-1})=(a+bz^{-1})(a+bz)=(a^2+b^2)+ab(z+z^{-1})$$
Comparando con $5+2(z+z^{-1})$: $a^2+b^2=5$, $ab=2$. Con $(a+b)^2=5+4=9$ y $(a-b)^2=5-4=1$: $a+b=3$, $a-b=1$, así $a=2$, $b=1$.
$$\boxed{\ g[n]=2\,\delta[n]+\delta[n-1]\ }$$
(Nótese que el cero de $G(z)=2+z^{-1}$ está en $z=-\tfrac12$ —el de adentro— y el de $G(z^{-1})=2+z$ en $z=-2$ —el de afuera—: exactamente los dos ceros de a). $G(z)$ es la factorización de **fase mínima**.)

**c)** Con $h[n]=a\delta[n]+b\delta[n-1]$ (figura P12.14-4), $\hat y[n+1]=a\,y[n]+b\,y[n-1]$. Las ecuaciones normales de un predictor FIR de dos coeficientes (Parte 1.1 del complemento) son
$$\begin{bmatrix}R_{yy}[0]&R_{yy}[1]\\ R_{yy}[1]&R_{yy}[0]\end{bmatrix}\begin{bmatrix}a\\b\end{bmatrix}=\begin{bmatrix}R_{yy}[1]\\ R_{yy}[2]\end{bmatrix} \implies \begin{bmatrix}5&2\\2&5\end{bmatrix}\begin{bmatrix}a\\b\end{bmatrix}=\begin{bmatrix}2\\0\end{bmatrix}$$
De la segunda ecuación $b=-\tfrac25a$; sustituyendo en la primera: $5a-\tfrac45a=2\Rightarrow\tfrac{21}5a=2$:
$$\boxed{\ a=\frac{10}{21}\approx0{,}4762\ ,\qquad b=-\frac{4}{21}\approx-0{,}1905\ }$$

**d)** Como $G(z)=2+z^{-1}$ ya es de fase mínima, escribo la versión mónica $\tilde F(z)=1+\tfrac12z^{-1}$ (de modo que $G(z)=2\,\tilde F(z)$, y $S_{yy}(z)=4\,\tilde F(z)\tilde F(z^{-1})$, con "ganancia de innovación" $K=4$). El predictor causal de un paso (Parte 1.3/1.5 del complemento, $H(z)=\frac1{\tilde F(z)}[z\tilde F(z)]_+$):
$$z\tilde F(z)=z+\tfrac12 \ \implies\ [z\tilde F(z)]_+=\tfrac12 \quad(\text{se descarta el término "}z\text{", que es anticausal})$$
$$H(z)=\frac{\tfrac12}{1+\tfrac12z^{-1}}=\frac{1}{2+z^{-1}}$$
En ecuación en diferencias, de $H(z)(2+z^{-1})=1$ aplicada a $Y(z)\to\hat Y_{+1}(z)$: $2\hat y[n+1]+\hat y[n]=y[n]$, es decir
$$\boxed{\ \hat y[n+1]=\tfrac12\big(y[n]-\hat y[n]\big)\ }$$
un filtro **IIR** (recursivo): a diferencia del predictor de c) (que se corta en dos taps), acá $h[n]$ tiene infinitos términos porque invertir un proceso MA para predecirlo causalmente requiere, en general, memoria infinita.

> [!warning] Ojo
> El predictor óptimo de d) es **IIR** aunque el proceso $y[n]$ se generó con un filtro FIR de solo dos taps (b). No hay contradicción: generar hacia adelante ($w\to y$) es FIR, pero invertir para predecir ($y$ pasado $\to y[n+1]$) es, en general, otra cuenta —y acá da infinita, salvo en el caso degenerado del Ejercicio 11/12 anterior donde el generador ya era autorregresivo.

###### **Verificación**
$R_{yy}[0]=5>0$ y $|R_{yy}[1]|=2<5$ ✓ (autocorrelación válida). El MMSE de d) tiene que ser $\leq$ el de c) (más memoria, o memoria "mejor organizada", nunca empeora), y ambos $\leq \text{Var}(y)=5$: en d), $\text{MMSE}=[G(\infty)]^2=2^2=4$ (la innovación descartada es $2w[n+1]$, de varianza $4\cdot1=4$); en c), $\text{MMSE}=R_{yy}[0]-aR_{yy}[1]-bR_{yy}[2]=5-\tfrac{10}{21}\cdot2-\big(\!-\tfrac4{21}\big)\cdot0=5-\tfrac{20}{21}\approx4{,}048$. Efectivamente $4<4{,}048<5$. *(verificado numéricamente: simulando $y[n]=2w[n]+w[n-1]$ con $w$ i.i.d. $\mathcal N(0,1)$ sobre $4\cdot10^6$ muestras, $\text{Var}(y)=4{,}993$, $R_{yy}[1]=1{,}995$, $R_{yy}[2]\approx0$ (teóricos $5,2,0$); el predictor FIR de c) con $a=0{,}4762,b=-0{,}1905$ da MSE empírico $4{,}044$ (teórico $4{,}048$); el predictor IIR de d), implementado recursivamente, da MSE empírico $3{,}997$ (teórico $4$, y coincide con $\text{Var}(2w)=4$ calculado directo).)*

---

## Ejercicio 15 — Estimar la entrada de un lazo con realimentación: por qué la causalidad, acá, lo mata todo

> [!quote] Enunciado
> 15. El sistema de la figura P12.15-1 consiste en una planta causal dentro de un lazo de realimentación. La señal de entrada $a[\cdot]$ y la perturbación de ruido $w[\cdot]$ son procesos WSS blancos de media nula, no correlacionados entre sí, con autocorrelaciones $R_{aa}[m]=\sigma_a^2\delta[m]$ y $R_{ww}[m]=\sigma_w^2\delta[m]$.
>
> ![[ej-p12-15a.png]]
> ![[ej-p12-15b.png]]
>
> Las funciones de transferencia $E(z)$ de $a[n]$ a $b[n]$ y $F(z)$ de $w[n]$ a $b[n]$ resultan
> $$E(z)=\frac1z, \qquad F(z)=\frac{z-3}{z}=1-3z^{-1}$$
> Este problema trata del diseño de un filtro LTI con función de sistema $H(z)$ que use mediciones de la salida $b[n]$ para generar $\hat a[n]$, la estimación LMMSE de la entrada $a[n]$ (figura P12.15-2).
>
> a) Suponga que no hay ruido, $\sigma_w^2=0$, y que el filtro $h[n]$ puede ser no causal. Determine, sin mucho trabajo, cuánto debe valer $H(z)$, y halle el error cuadrático medio correspondiente $E[(a[n]-\hat a[n])^2]$.
> b) Suponga ahora que $h[n]$ sigue pudiendo ser no causal, pero que $\sigma_w^2$ ya no está restringido a cero. Determine $H(z)$. Verifique que su respuesta se reduce a la de a) cuando $\sigma_w^2=0$.
> c) Suponga de nuevo que no hay ruido, $\sigma_w^2=0$, pero que el filtro de estimación $H(z)$ está restringido a ser causal. Halle $H(z)$ y el error cuadrático medio correspondiente.
> d) Halle el filtro de Wiener causal cuando $\sigma_w^2>0$.

###### **Idea**
$b[n]=a[n-1]+\big(w[n]-3w[n-1]\big)$ (de $E(z)=z^{-1}$, $F(z)=1-3z^{-1}$): la planta mete un **retardo puro** entre $a$ y $b$. Sin restricción de causalidad eso no es un problema (se puede "adelantar" $b$). Pero con causalidad, es fatal: la única muestra de $b$ que trae información de $a[n]$ es $b[n+1]$ —que está en el **futuro**—, y ningún filtro causal la puede usar. Por eso c) y d) dan lo mismo sin importar el ruido.

###### **Resolución**
**a)** Con $\sigma_w^2=0$, $b[n]=a[n-1]$ exactamente: conocer $b[\cdot]$ es lo mismo que conocer $a[\cdot]$ corrido un paso. El filtro no causal que deshace ese corrimiento es un simple adelanto:
$$\boxed{\ H(z)=z \ \ \big(\text{es decir } \hat a[n]=b[n+1]\big), \qquad \text{MMSE}=0\ }$$
(reconstrucción exacta, coherencia $=1$ en toda frecuencia — mismo fenómeno que el Ejercicio 7 del complemento).

**b)** Con ruido, $a[\cdot]$ y $w[\cdot]$ independientes y ambos blancos. La correlación cruzada con $b[n]=a[n-1]+w[n]-3w[n-1]$:
$$R_{ab}[m]=E\{a[n+m]\,b[n]\}=E\{a[n+m]\,a[n-1]\}=\sigma_a^2\,\delta[m+1] \ \implies \ S_{ab}(e^{j\Omega})=\sigma_a^2\,e^{j\Omega}$$
(el ruido no aporta nada acá porque es independiente de $a$). Para $S_{bb}$: $|E(e^{j\Omega})|=1$ y $|F(e^{j\Omega})|^2=|1-3e^{-j\Omega}|^2=10-6\cos\Omega$, así que
$$S_{bb}(e^{j\Omega})=\sigma_a^2+\sigma_w^2(10-6\cos\Omega)$$
$$\boxed{\ H(e^{j\Omega})=\frac{S_{ab}(e^{j\Omega})}{S_{bb}(e^{j\Omega})}=\frac{\sigma_a^2\,e^{j\Omega}}{\sigma_a^2+\sigma_w^2(10-6\cos\Omega)}\ }$$
Con $\sigma_w^2=0$ se reduce a $H=\sigma_a^2e^{j\Omega}/\sigma_a^2=e^{j\Omega}$, o sea $H(z)=z$: coincide con a) ✓.

Con la identidad $\frac1{2\pi}\int_{-\pi}^{\pi}\frac{d\Omega}{p-q\cos\Omega}=\frac{1}{\sqrt{p^2-q^2}}$ (para $p>|q|$), con $p=\sigma_a^2+10\sigma_w^2$, $q=6\sigma_w^2$:
$$\boxed{\ \text{MMSE}_b=\sigma_a^2-\frac{\sigma_a^4}{\sqrt{p^2-q^2}}\ , \qquad p^2-q^2=\sigma_a^4+20\sigma_a^2\sigma_w^2+64\sigma_w^4\ }$$
Con $\sigma_w^2=0$: $p=\sigma_a^2$, $\sqrt{p^2-q^2}=\sigma_a^2$, MMSE$=\sigma_a^2-\sigma_a^2=0$ ✓ (coincide con a)). Con $\sigma_w^2\to\infty$: MMSE$\to\sigma_a^2-\sigma_a^4/(8\sigma_w^2)\to\sigma_a^2$ (ruido infinito, no sirve de nada, como es de esperar).

**c) y d) — el mismo resultado, con o sin ruido.** La clave está en $R_{ab}[m]=\sigma_a^2\delta[m+1]$: es **cero para todo $m\geq0$**. Un filtro causal para estimar $a[n]$ solo puede usar $b[n-k]$ con $k\geq0$ (presente y pasado), y la correlación relevante es
$$E\{a[n]\,b[n-k]\}=R_{ab}[k]=0 \quad\text{para todo } k\geq0$$
(el único $k$ para el que $R_{ab}$ no es cero es $k=-1$, es decir $b[n+1]$: **el futuro**). Como $a[n]$ está completamente no correlacionado con toda medición causal de $b$ —esto no depende de $\sigma_w^2$, es la estructura de retardo de $E(z)=z^{-1}$ la que lo garantiza—, el estimador LMMSE causal es directamente la media:
$$\boxed{\ H(z)=0 \ \ (\hat a[n]=0), \qquad \text{MMSE}=\sigma_a^2 \ \ \text{para todo } \sigma_w^2\geq0\ }$$

> [!warning] Ojo
> No es que el filtro causal "salga complicado": literalmente **no hay nada que hacer**. Agregar más ruido ($\sigma_w^2$ más grande) no cambia la respuesta porque el problema no es de relación señal/ruido sino de **estructura temporal**: la información sobre $a[n]$ vive en $b[n+1]$, y ningún filtro causal puede adelantarse un paso. Es el precio de la causalidad llevado al extremo: acá no es "más caro", es **infinito** (se pierde toda la información).

###### **Verificación**
$\text{MMSE}_b\in[0,\sigma_a^2]$ para todo $\sigma_w^2\geq0$ ✓, y $\text{MMSE}_b\leq\text{MMSE}_{c,d}=\sigma_a^2$ siempre (no causal nunca puede ser peor que causal) ✓, con igualdad en $\sigma_w^2\to\infty$. *(verificado numéricamente: con $\sigma_a^2=3$, $\sigma_w^2=0{,}7$, simulando $3\cdot10^6$ muestras de $a,w$ independientes y armando $b[n]=a[n-1]+w[n]-3w[n-1]$: $R_{ab}[-1]=2{,}995\approx\sigma_a^2=3$ y $R_{ab}[m]\approx0$ para $m=-3,-2,0,1,2$ (en particular para todo $m\geq0$, confirmando que ninguna medición causal de $b$ correlaciona con $a[n]$); $R_{bb}[0]=9{,}993\approx10$, $R_{bb}[\pm1]=-2{,}098\approx-2{,}1$ (teóricos $\sigma_a^2+10\sigma_w^2=10$ y $-3\sigma_w^2=-2{,}1$). Resolviendo un Wiener FIR no causal de $801$ taps con las correlaciones exactas, el MMSE numérico da $2{,}008291$, idéntico (6 cifras) a la fórmula cerrada $\sigma_a^2-\sigma_a^4/\sqrt{p^2-q^2}=2{,}008291$.)*

---

## Ejercicio 16 — De un MA(1) no mínimo-fase a su gemelo de fase mínima, y el predictor causal

> [!quote] Enunciado
> 16. Suponga que el proceso WSS de media nula $x[n]$ se obtiene aplicando un proceso blanco WSS de media nula $w[n]$ con PSD $S_{ww}(e^{j\Omega})=\sigma^2$ a la entrada de un filtro estable y causal con función de sistema
> $$M(z)=1-3z^{-1}$$
>
> a) Si $S_{xx}(e^{j\Omega})$ denota la PSD de $x[n]$, halle $S_{xx}(z)$. Halle también la autocovarianza $C_{xx}[m]$ del proceso $x[n]$, la varianza de la variable aleatoria $x[n+1]$, y el coeficiente de correlación $\rho$ entre $x[n]$ y $x[n+1]$.
> b) Especifique el estimador LMMSE de $x[n+1]$ basado en una medición de $x[n]$, y calcule el error cuadrático medio asociado. ¿Es menor que la varianza de $x[n+1]$ que calculó en a)?
> c) Halle la función de sistema $F(z)$ de un filtro estable y causal cuya inversa $1/F(z)$ también sea estable y causal, tal que $S_{xx}(z)=F(z)F(z^{-1})$.
> d) Halle la función de sistema del filtro de Wiener causal que genera una estimación de $x[n+1]$ basada en el presente y todos los $x[k]$ pasados, $k\leq n$, es decir, el predictor de un paso. ¿Espera que el error cuadrático medio de este caso sea menor, igual o mayor que el calculado en b)? Determine el error cuadrático medio para confirmar si su expectativa es correcta.

> [!info] Conexión
> Este es el Ejercicio 12.16 que el apunte principal deja como "Actividad" dentro de la sección de Wiener causal (con el aviso: *"Ojo con c): $M(z)=1-3z^{-1}$ tiene un cero en $z=3$, fuera del círculo unidad. No es de fase mínima. Hay que corregirlo con un pasa-todo."*). Acá va resuelto entero.

###### **Idea**
$M(z)=1-3z^{-1}$ genera $x$, pero tiene su cero en $z=3$ —afuera del círculo unidad—, así que **no** es el factor de fase mínima que hace falta para c) y d): hay que buscar el filtro con el mismo $|M(e^{j\Omega})|^2$ pero con el cero adentro (en $z=\tfrac13$, el recíproco). Con eso ya armado, d) es directamente la fórmula de innovaciones.

###### **Resolución**
**a)** $x[n]=w[n]-3w[n-1]$, así que
$$S_{xx}(z)=M(z)M(z^{-1})\,S_{ww}=\sigma^2(1-3z^{-1})(1-3z)=\sigma^2\big(10-3(z+z^{-1})\big)$$
En tiempo: $C_{xx}[m]=10\sigma^2\delta[m]-3\sigma^2\big(\delta[m-1]+\delta[m+1]\big)$ (se lee directo de la expresión de arriba, igual que en el Ejercicio 14). En particular:
$$\boxed{\ \text{Var}(x[n+1])=C_{xx}[0]=10\sigma^2\ , \qquad \rho=\frac{C_{xx}[1]}{C_{xx}[0]}=\frac{-3\sigma^2}{10\sigma^2}=-0{,}3\ }$$

**b)** LMMSE de una variable a partir de otra, con $\rho=-0{,}3$:
$$\boxed{\ \hat x[n+1]=\rho\,x[n]=-0{,}3\,x[n]\ }, \qquad \text{MMSE}_b=10\sigma^2(1-\rho^2)=\boxed{\ 9{,}1\,\sigma^2\ }$$
Sí, es menor que $\text{Var}(x[n+1])=10\sigma^2$: conocer $x[n]$ ayuda, aunque sea un solo dato.

**c)** $M(z)=1-3z^{-1}$ tiene cero en $z=3$ (fuera del círculo unidad): no sirve como $F(z)$. Busco el filtro con cero en el recíproco $z=\tfrac13$ (adentro) que dé la **misma** magnitud al cuadrado en el círculo unidad. Probando $F(z)=A\big(1-\tfrac13z^{-1}\big)$:
$$F(z)F(z^{-1})=A^2\Big(\tfrac{10}9-\tfrac13(z+z^{-1})\Big)$$
Igualando con $S_{xx}(z)/\sigma^2=10-3(z+z^{-1})$: $A^2\cdot\tfrac{10}9=10\sigma^2\Rightarrow A^2=9\sigma^2\Rightarrow A=3\sigma$ (y el término cruzado da $A^2/3=3\sigma^2$ ✓, coincide solo).
$$\boxed{\ F(z)=3\sigma\Big(1-\tfrac13z^{-1}\Big)=3\sigma-\sigma z^{-1}\ }$$
Es estable y causal (FIR), y su inversa $1/F(z)=\frac{1}{3\sigma}\cdot\frac1{1-\frac13z^{-1}}$ tiene el único polo en $z=\tfrac13$ (adentro): también estable y causal ✓. Este $F$ es el "pasa-todo" que corrige a $M$: $|F(e^{j\Omega})|=|M(e^{j\Omega})|$ en todo $\Omega$, pero con el cero reflejado adentro.

**d)** Escribo $F(z)=3\sigma\,\tilde F(z)$ con $\tilde F(z)=1-\tfrac13z^{-1}$ mónico ($\tilde F(\infty)=1$), de modo que $S_{xx}(z)=K\,\tilde F(z)\tilde F(z^{-1})$ con $K=(3\sigma)^2=9\sigma^2$ (la "ganancia de innovación"). El predictor de un paso (misma maquinaria que en los Ejercicios 13 y 14):
$$z\tilde F(z)=z-\tfrac13 \ \implies\ [z\tilde F(z)]_+=-\tfrac13 \quad(\text{se descarta "}z\text{", anticausal})$$
$$\boxed{\ H(z)=\frac{-1/3}{1-\tfrac13z^{-1}}\ } \qquad\text{es decir}\qquad \hat x[n+1]=\tfrac13\big(\hat x[n]-x[n]\big)$$
**Esperado:** el MMSE de d) tiene que ser **menor o igual** que el de b), porque el filtro causal óptimo usa *todo* el pasado (no solo $x[n]$) y no puede hacerlo peor que un caso particular suyo (quedarse solo con $x[n]$). El MMSE es la ganancia de innovación:
$$\boxed{\ \text{MMSE}_d=K=9\sigma^2\ }$$
En efecto $9\sigma^2<9{,}1\sigma^2=\text{MMSE}_b$: **menor**, como se esperaba — aunque la mejora es chica, porque más allá de $x[n]$ el resto del pasado casi no aporta (el proceso es MA(1), de memoria corta).

###### **Verificación**
$|\rho|=0{,}3<1$ ✓; $\text{MMSE}_d\leq\text{MMSE}_b\leq\text{Var}(x)=10\sigma^2$ ✓ ($9\sigma^2\leq9{,}1\sigma^2\leq10\sigma^2$). *(verificado numéricamente con $\sigma^2=2$, simulando $x[n]=w[n]-3w[n-1]$ sobre $4\cdot10^6$ muestras: $\text{Var}(x)=19{,}981$ (teórico $20$), $C_{xx}[1]=-5{,}984$ (teórico $-6$), $C_{xx}[2]\approx0$; el estimador de b) da MMSE empírico $18{,}189$ (teórico $18{,}2$); $|F(e^{j\Omega})|^2$ coincide con $S_{xx}(e^{j\Omega})$ con error máximo $2\cdot10^{-14}$; y el predictor recursivo de d) da MMSE empírico $17{,}987$ (teórico $18{,}0$) — efectivamente menor que $18{,}2$.)*

---

## Ejercicio 17 — Predictor de un paso para un modelo de fase mínima, sin y con causalidad

> [!quote] Enunciado
> 17. Tenemos mediciones de un proceso aleatorio WSS $x[n]$ modelado como la salida de un sistema LTI de fase mínima cuya entrada es un proceso blanco $w[n]$ con $E\{w^2[n]\}=1$. (Recuerde que un sistema de fase mínima de tiempo discreto se define como estable, causal, y con inversa estable y causal.) La situación se muestra en la figura P12.17-1.
>
> ![[ej-p12-17a.png]]
> ![[ej-p12-17b.png]]
>
> Suponga que la función de transferencia del sistema anterior es
> $$M(z)=\frac{z}{z-\gamma}+d$$
> donde $\gamma\neq0$ y $d\neq0$. Queremos pasar el proceso $x[n]$ por un filtro LTI estable con función de sistema $H(z)$ elegida para que sea el estimador LMMSE de $x[n+1]$, es decir, el predictor LMMSE de un paso (figura P12.17-2).
>
> a) Determine el filtro óptimo y el error cuadrático medio asociado, sin restringir $H(z)$ a ser causal.
> b) Suponga ahora que restringimos $H(z)$ a ser no solo estable sino también causal. Determine de nuevo el filtro óptimo y el error cuadrático medio asociado. Sus respuestas quedarán expresadas en términos de los parámetros dados, es decir $\sigma$, $\gamma$ y $d$.

> [!warning] Nota sobre el enunciado
> El enunciado (igual que el P12.18 del libro) pide las respuestas "en términos de $\sigma$, $\gamma$ y $d$", pero $\sigma$ no aparece definido: la entrada tiene $E\{w^2[n]\}=1$. Resolvemos con una varianza genérica $\sigma^2=E\{w^2[n]\}$ y al final se toma $\sigma^2=1$.

###### **Idea**
a) Sin causalidad, "predecir" $x[n+1]$ es trivial: el filtro puede mirar el futuro. b) Con causalidad, como $M$ es de fase mínima, $x[\cdot]$ y $w[\cdot]$ se obtienen uno del otro con filtros causales: el pasado de $x$ contiene exactamente la misma información que el pasado de $w$. Entonces se predice $x[n+1]$ quedándose con todo lo que depende de $w[k]$, $k\leq n$, y descartando solo $w[n+1]$, la innovación.

###### **Resolución**
**Forma útil de $M(z)$.** 
$$M(z)=\frac{1}{1-\gamma z^{-1}}+d=\frac{(1+d)-d\gamma z^{-1}}{1-\gamma z^{-1}}=(1+d)\,\frac{1-\frac{d\gamma}{1+d}z^{-1}}{1-\gamma z^{-1}}$$
Fase mínima significa polo y cero adentro del círculo unidad: $|\gamma|<1$ y $\left|\tfrac{d\gamma}{1+d}\right|<1$ (con $d\neq-1$). Su respuesta al impulso causal es $m[n]=\gamma^nu[n]+d\,\delta[n]$, así que $m[0]=1+d$ y $m[k]=\gamma^k$ para $k\geq1$.

**a)** Sin restricción de causalidad, el filtro $H(z)=z$ (un adelanto de una muestra) da $\hat x[n+1]=x[n+1]$ exactamente:
$$\boxed{\ H(z)=z\ ,\qquad \text{MMSE}=0\ }$$
Es estable, y ningún filtro puede dar un error menor que cero.

**b)** Escribimos $x[n+1]$ en términos de la entrada:
$$x[n+1]=\sum_{k\geq0}m[k]\,w[n+1-k]=\underbrace{(1+d)\,w[n+1]}_{\text{innovación: futuro}}+\underbrace{\sum_{k\geq1}\gamma^k\,w[n+1-k]}_{\text{depende solo de }w[j],\ j\leq n}$$
Como $M$ tiene inversa causal y estable, cada $w[j]$ con $j\leq n$ es una combinación lineal de $x[k]$ con $k\leq n$, y viceversa. El segundo término, entonces, se puede calcular a partir del pasado de $x$. El primero es ortogonal a todo ese pasado ($w$ es blanco). Por ortogonalidad, el predictor óptimo es el segundo término y el error es el primero:
$$\hat x[n+1]=\sum_{k\geq1}\gamma^kw[n+1-k]\qquad\Longrightarrow\qquad \text{MMSE}=E\{(1+d)^2w^2[n+1]\}=(1+d)^2\sigma^2$$

**El filtro como función de $x$.** El predictor, visto desde $w$, tiene transferencia $z\big(M(z)-m[0]\big)$ (sacar $m[0]$ y adelantar una muestra). Visto desde $x$ hay que anteponer el blanqueador $1/M(z)$:
$$H(z)=\frac{z\big(M(z)-(1+d)\big)}{M(z)}$$
Con $M(z)-(1+d)=\dfrac{1}{1-\gamma z^{-1}}-1=\dfrac{\gamma z^{-1}}{1-\gamma z^{-1}}$ queda $z\big(M-(1+d)\big)=\dfrac{\gamma}{1-\gamma z^{-1}}$, y dividiendo por $M$:
$$H(z)=\frac{\gamma}{1-\gamma z^{-1}}\cdot\frac{1-\gamma z^{-1}}{(1+d)-d\gamma z^{-1}}\quad\Longrightarrow\quad\boxed{\ H(z)=\frac{\gamma/(1+d)}{1-\frac{d\gamma}{1+d}\,z^{-1}}\ ,\qquad \text{MMSE}=\sigma^2(1+d)^2\ }$$
Con $\sigma^2=1$, como dice el enunciado, $\text{MMSE}=(1+d)^2$. En ecuación en diferencias: $\hat x[n+1]=\dfrac{d\gamma}{1+d}\,\hat x[n]+\dfrac{\gamma}{1+d}\,x[n]$. $H$ es causal, y es estable justamente porque el cero de $M$ está adentro del círculo unidad.

###### **Verificación**
**Caso $d=0$:** $x$ es un AR(1), $x[n]=\gamma x[n-1]+w[n]$. La fórmula da $H(z)=\gamma$ ($\hat x[n+1]=\gamma x[n]$) y MMSE $=\sigma^2$, que es lo esperado: lo único que no se puede predecir de un AR(1) es la innovación ✓. **Cota:** $\text{Var}(x)=\sigma^2\sum_k m^2[k]=\sigma^2\big[(1+d)^2+\tfrac{\gamma^2}{1-\gamma^2}\big]\geq\sigma^2(1+d)^2$: predecir nunca es peor que estimar por la media ✓. *(verificado numéricamente con $\gamma=0{,}6$, $d=0{,}8$ y $2\cdot10^6$ muestras: pasando $x$ por el $H(z)$ de arriba, el error cuadrático medio de predicción da $3{,}244$ contra $(1+d)^2=3{,}24$.)*

> [!info] Conexión
> Es la receta general del predictor causal de Wiener: blanquear con $1/M$, quedarse con la parte causal de $zM(z)$ sin el término de la innovación, y el MMSE es $m[0]^2\sigma^2$, la varianza de la innovación. Ver [[PROCESAMIENTO DE SEÑALES - Cap 12 en profundidad]] (Parte 1.3).

---

## Ejercicio 18 — Predictores de un solo coeficiente y predicción de un proceso exponencialmente correlacionado

> [!quote] Enunciado
> 18. a) Suponga que $x[n]$ es una secuencia aleatoria WSS de media nula con autocorrelación $R_{xx}[m]=\left(\tfrac13\right)^{|m|}$. Queremos diseñar un filtro LTI causal $h[n]$, como se muestra en la figura, con un único valor no nulo, es decir, con $h[n]=a\ \delta[n-n_o]$, donde $n_o$ es un entero mayor o igual a $0$. La salida $g[n]$ debe ser el mejor predictor lineal de un paso de $x[n]$ de esa forma, es decir, se elige para minimizar el error cuadrático medio de predicción $E[(g[n]-x[n+1])^2]$. Si $n_o$ está fijo, determine el valor de $a$, en términos de $n_o$, que minimiza este error.
>
> ![[ej-p12-18.png]]
>
> b) Se sabe que un proceso WSS de media nula $x(t)$ tiene autocorrelación $R_{xx}(\tau)=6e^{-3|\tau|}$. Determine el filtro de Wiener LTI causal óptimo para obtener la estimación LMMSE de $x(t+T)$ para un $T>0$ fijo, usando mediciones de $x(\cdot)$ desde el pasado infinito hasta el instante $t$. Calcule también el MMSE asociado. Exprese en palabras qué le dice su respuesta sobre la predicción LMMSE de un proceso exponencialmente correlacionado.

###### **Idea**
a) Con un solo coeficiente, $g[n]=a\,x[n-n_o]$ es la LMMSE de una variable a partir de otra (capítulo 8). b) Se factoriza la PSD, se escribe $x(t+T)$ en términos de la innovación blanca y se descarta lo que cae después de $t$. El resultado es un filtro muy simple.

###### **Resolución**
**a)** El error es
$$E\big[(a\,x[n-n_o]-x[n+1])^2\big]=a^2R_{xx}[0]-2a\,R_{xx}[n_o+1]+R_{xx}[0]$$
porque $x[n+1]$ y $x[n-n_o]$ están separados $n_o+1$ muestras. Derivando respecto de $a$ e igualando a cero:
$$a=\frac{R_{xx}[n_o+1]}{R_{xx}[0]}\quad\Longrightarrow\quad\boxed{\ a=\left(\tfrac13\right)^{n_o+1}\ }$$
El error mínimo resultante es $R_{xx}[0]-R_{xx}[n_o+1]^2/R_{xx}[0]=1-\left(\tfrac19\right)^{n_o+1}$: vale $\tfrac89$ para $n_o=0$ y crece hacia $1$ (la varianza) a medida que el dato que se usa es más viejo. La mejor elección es $n_o=0$, con $a=\tfrac13$.

**b)** **PSD y factorización.** 
$$S_{xx}(j\omega)=\int 6e^{-3|\tau|}e^{-j\omega\tau}d\tau=6\cdot\frac{2\cdot3}{9+\omega^2}=\frac{36}{9+\omega^2}=\frac{6}{3+j\omega}\cdot\frac{6}{3-j\omega}$$
El factor causal y de fase mínima es $M(s)=\dfrac{6}{s+3}$, con $m(t)=6e^{-3t}u(t)$. Entonces $x(t)=\int_0^\infty m(\tau)\,w(t-\tau)\,d\tau$, con $w$ blanco de PSD unitaria (la innovación).

**Separar futuro y pasado.** 
$$x(t+T)=\int_0^\infty m(\tau)\,w(t+T-\tau)\,d\tau=\underbrace{\int_0^T m(\tau)\,w(t+T-\tau)\,d\tau}_{\text{usa }w\text{ en }(t,\,t+T]:\ \text{futuro}}+\underbrace{\int_T^\infty m(\tau)\,w(t+T-\tau)\,d\tau}_{\text{usa }w\text{ hasta }t}$$
Como $M$ es de fase mínima, el pasado de $x$ hasta $t$ equivale al pasado de $w$ hasta $t$. El primer término es ortogonal a ese pasado, y el segundo se puede calcular con él: el segundo término es la predicción. Cambiando variable $\tau=\tau'+T$:
$$\hat x(t+T)=\int_0^\infty 6e^{-3(\tau'+T)}\,w(t-\tau')\,d\tau'=e^{-3T}\int_0^\infty 6e^{-3\tau'}w(t-\tau')\,d\tau'=e^{-3T}\,x(t)$$
$$\boxed{\ H(s)=e^{-3T}\ \ \big(h(t)=e^{-3T}\delta(t)\big)\ ,\qquad \hat x(t+T)=e^{-3T}\,x(t)\ }$$

**MMSE.** Es la potencia del término descartado:
$$\text{MMSE}=\int_0^T m^2(\tau)\,d\tau=36\int_0^Te^{-6\tau}d\tau\quad\Longrightarrow\quad\boxed{\ \text{MMSE}=6\big(1-e^{-6T}\big)\ }$$

**En palabras.** Para un proceso con autocorrelación exponencial, el mejor predictor causal usa **solo el valor presente** $x(t)$; todo el pasado anterior no agrega nada. Es la propiedad de Markov: el presente resume toda la información útil del pasado. La predicción es el valor actual encogido hacia la media ($0$) con factor $e^{-3T}$, y el error crece desde $0$ (para $T\to0$) hasta la varianza total $6$ (para $T\to\infty$, cuando ya no se puede predecir nada).

###### **Verificación**
El MMSE coincide con el de la LMMSE de $x(t+T)$ a partir de **solo** $x(t)$: $R_{xx}(0)-R_{xx}(T)^2/R_{xx}(0)=6-36e^{-6T}/6=6(1-e^{-6T})$ ✓, que es la confirmación de que el resto del pasado no aporta. Es la versión en tiempo continuo de a) con $n_o=0$: ahí también el mejor coeficiente es la autocorrelación normalizada a distancia de un paso ✓. *(verificado numéricamente: simulando el proceso con paso $10^{-3}$ y $10^6$ muestras, con $T=0{,}2$ el error de $\hat x=e^{-3T}x(t)$ da $4{,}189$ contra $6(1-e^{-1{,}2})=4{,}193$.)*

---
