Solucionario de los Ejercicios Propuestos del capítulo 11 de [[PROCESAMIENTO DE SEÑALES]]. La teoría con demostraciones está en [[PROCESAMIENTO DE SEÑALES - Cap 11 en profundidad]].

# Densidad Espectral De Potencia — Solucionario

Estos ejercicios trabajan con las herramientas centrales del capítulo: el criterio de Bochner/Herglotz para decidir si una función puede ser autocorrelación, el efecto del muestreo y el aliasing sobre la PSD, el filtrado de procesos blancos y coloreados con las relaciones $S_{yx}=H\,S_{xx}$ (y $S_{xy}=H^*S_{xx}$), $S_{yy}=|H|^2S_{xx}$, y en la segunda mitad la factorización espectral: filtros modeladores, blanqueadores y fase mínima. Cada enunciado está cotejado contra el libro; donde la guía difiere, hay una nota antes de la resolución.

###### **Índice**
| Ej. | Qué se practica | Problema del libro |
|---|---|---|
| 1 | Producto de procesos independientes; retardo y correlación cruzada | P11.13 |
| 2 | Candidatas a autocorrelación (Bochner) y construcción vía blanco $\pm1$ | P11.1 |
| 3 | Muestreo de un proceso WSS: aliasing en la PSD | P11.9 |
| 4 | Filtro pasa-altos ideal sobre ruido blanco | P11.15 |
| 5 | Verdadero o falso: varianza de salida y distribución de potencia | P11.16 |
| 6 | Suma de procesos no correlacionados: separar espectros | P11.7 |
| 7 | Filtro FIR de tres términos: covarianzas y PSD de salida | P11.3 |
| 8 | Densidad espectral cruzada dada por un gráfico: ¿es realizable? | P11.5 |
| 9 | Verdadero o falso sobre espectro cruzado y autoespectros | P11.4 |
| 10 | Densidad cruzada a través de un filtro pasatodo | P11.2 |
| 11 | Densidad cruzada de dos filtrados del mismo proceso | P11.6 |
| 12 | AR(1): estabilidad, PSD, autocovarianza y predicción LMMSE | P11.10 |
| 13 | Fase mínima no es necesaria para modelar, sí para invertir | P11.12 |
| 14 | Factorización espectral de una PSD racional de primer orden | P11.11 |
| 15 | Factorización espectral en tiempo continuo, con y sin fase mínima | P11.14 |
| 16 | Sistema de tres coeficientes: incógnitas, tipo de filtro, blanqueador imposible | P11.17 |
| 17 | Filtro blanqueador y su unicidad | P11.8 |

---

## Ejercicio 1 — Producto de procesos independientes y correlación cruzada de un retardo

> [!quote] Enunciado
> 1. a) Suponga que $x(\cdot)$ e $y(\cdot)$ son procesos aleatorios independientes, y cada uno es WSS. Muestre que $z(t)=x(t)y(t)$ también es WSS, y escriba su PSD en términos de las PSD $S_{xx}(j\omega)$ y $S_{yy}(j\omega)$.
> b) Suponga que $x(t)$ es un proceso WSS e $y(t)=x(t-1)$. ¿Es $C_{yx}(1)\geq C_{yx}(\tau)$ para todo $\tau$? Exprese $S_{yx}(j\omega)$ en términos de $S_{xx}(j\omega)$.

###### **Idea**
Para a), independencia entre procesos completos implica independencia entre cualquier función de $x(\cdot)$ y cualquier función de $y(\cdot)$; multiplicar en el tiempo es convolucionar en frecuencia. Para b), $C_{yx}(\tau)$ termina siendo $C_{xx}$ evaluada en otro lag, y ahí entra la propiedad "el máximo de una autocovarianza está en el origen".

###### **Resolución**
**a)** Media: por independencia, $E[z(t)]=E[x(t)y(t)]=E[x(t)]E[y(t)]=\mu_x\mu_y$, constante.

Autocorrelación: $z(t_1)z(t_2)=\big[x(t_1)x(t_2)\big]\big[y(t_1)y(t_2)\big]$. Como los procesos $x(\cdot)$ e $y(\cdot)$ son independientes, la variable $x(t_1)x(t_2)$ (función solo de $x$) es independiente de $y(t_1)y(t_2)$ (función solo de $y$), así que
$$R_{zz}(t_1,t_2)=E[x(t_1)x(t_2)]\,E[y(t_1)y(t_2)]=R_{xx}(t_1,t_2)\,R_{yy}(t_1,t_2)$$
Como $x$ e $y$ son WSS, $R_{xx}$ y $R_{yy}$ dependen solo de $\tau=t_1-t_2$, así que $R_{zz}(t_1,t_2)=R_{xx}(\tau)R_{yy}(\tau)$ también depende solo de $\tau$. Con media constante y autocorrelación función de $\tau$: **$z(t)$ es WSS**, con
$$R_{zz}(\tau)=R_{xx}(\tau)\,R_{yy}(\tau)$$
Multiplicar en el tiempo es convolucionar en frecuencia (con el $1/2\pi$ de la convención de Fourier del apunte):
$$\boxed{\ S_{zz}(j\omega)=\frac{1}{2\pi}\,S_{xx}(j\omega)*S_{yy}(j\omega)\ }$$

**b)** $C_{yx}(\tau)=\text{Cov}(y(t+\tau),x(t))$. Con $y(t)=x(t-1)$, resulta $y(t+\tau)=x(t+\tau-1)$, así que
$$C_{yx}(\tau)=\text{Cov}\big(x(t+\tau-1),x(t)\big)=C_{xx}(\tau-1)$$
Por la propiedad "el máximo de la autocovarianza está en el origen" ($|C_{xx}(s)|\leq C_{xx}(0)$ para todo $s$), tomando $s=\tau-1$:
$$C_{yx}(\tau)=C_{xx}(\tau-1)\leq C_{xx}(0)=C_{yx}(1)$$
$$\boxed{\ \text{Sí: } C_{yx}(1)\geq C_{yx}(\tau)\ \text{para todo }\tau\ }$$

Para $S_{yx}$: $y=x*h$ con $h(t)=\delta(t-1)$, cuya respuesta en frecuencia es $H(j\omega)=e^{-j\omega}$. Por el resultado del capítulo 10 ($S_{yx}(j\omega)=H(j\omega)S_{xx}(j\omega)$, con $y$ como "salida" de filtrar $x$):
$$\boxed{\ S_{yx}(j\omega)=e^{-j\omega}\,S_{xx}(j\omega)\ }$$

###### **Verificación**
*(verificado numéricamente: dos procesos AR(1) gaussianos independientes, simulados con $2\cdot10^6$ muestras cada uno, dan $R_{zz}[m]$ que coincide con $R_{xx}[m]\cdot R_{yy}[m]$ dentro de un $0{,}3\%$ para $m=0,\dots,3$; y con $y[n]=x[n-1]$, $C_{yx}(\tau)$ resulta máxima exactamente en $\tau=1$ entre $\tau=-2,\dots,3$.)*

> [!info] Conexión
> El resultado de a) es el análogo de la propiedad de modulación de Fourier, pero para PSDs: la misma idea aparece en el Ejercicio 2 de la Parte 5 de [[PROCESAMIENTO DE SEÑALES - Cap 11 en profundidad]] (ahí se modula con un coseno determinístico en vez de con un proceso aleatorio, y la convolución con dos impulsos da el corrimiento de espectro).

---

## Ejercicio 2 — Candidatas a autocorrelación, tiempo continuo y discreto

> [!quote] Enunciado
> 2. a) La figura muestra tres candidatas (etiquetadas [A], [B] y [C]) para la función de autocorrelación $R_{xx}(\tau)$ de un proceso aleatorio WSS de tiempo continuo $x(t)$. Para cada candidata, indique si es una función de autocorrelación posible para un proceso aleatorio WSS $x(t)$. Justifique brevemente sus respuestas.
>
> ![[ej-p11-2.png]]
>
> b) Para cada una de las siguientes funciones $R[m]$, indique si puede ser la función de autocorrelación de un proceso aleatorio WSS de tiempo discreto, donde $m$ denota el lag. Si no puede serlo, explique por qué. Si puede, explique en detalle cómo obtendría tal proceso filtrando adecuadamente un proceso de Bernoulli que toma en cada instante los valores $+1$ o $-1$ con igual probabilidad.
> i) $R[m]=1$ para $m=0$; $0.7$ para $|m|=1$; y $0$ en el resto.
> ii) $R[m]=2$ para $m=0$; $-1$ para $|m|=1$; y $0$ en el resto.

###### **Idea**
El criterio es siempre el mismo (Bochner/Herglotz): transformar y comprobar no negatividad. [B] y [C] son exactamente el contraejemplo y el ejemplo que ya trabajó el apunte (rectángulo vs. triángulo); [A] agrega un tren de impulsos.

###### **Resolución**
**a) [A]:** tren de impulsos $R_{xx}(\tau)=\delta(\tau+\tau_o)+2\delta(\tau)+\delta(\tau-\tau_o)$ (áreas $1,2,1$). Transformando cada impulso ($\mathcal F\{\delta(\tau-\tau_o)\}=e^{-j\omega\tau_o}$):
$$S_A(j\omega)=e^{j\omega\tau_o}+2+e^{-j\omega\tau_o}=2+2\cos(\omega\tau_o)=4\cos^2\!\left(\frac{\omega\tau_o}{2}\right)\geq0$$
Real, par, no negativa $\Rightarrow$ **[A] es válida**.

**[B]:** rectángulo $R_{xx}(\tau)=K$ para $|\tau|<\tau_o$. Es exactamente el contraejemplo del apunte: su transformada es una sinc, que se hace negativa $\Rightarrow$ **[B] no es válida**.

**[C]:** triángulo de altura $1$ y base $[-\tau_o,\tau_o]$. Integrando directamente,
$$S_C(j\omega)=2\int_0^{\tau_o}\left(1-\frac{\tau}{\tau_o}\right)\cos(\omega\tau)\,d\tau=\tau_o\left[\frac{\sin(\omega\tau_o/2)}{\omega\tau_o/2}\right]^2=\tau_o\,\text{sinc}^2\!\left(\frac{\omega\tau_o}{2}\right)$$
(con $\text{sinc}(x)=\sin(x)/x$), que es $\geq0$ siempre $\Rightarrow$ **[C] es válida** (mismo caso que la función triangular del apunte).

**b) i)** $S(e^{j\Omega})=1+1.4\cos\Omega$. Su mínimo está en $\Omega=\pi$: $S(e^{j\pi})=1-1.4=-0.4<0$.
$$\boxed{\ \text{No puede ser una autocorrelación}\ }$$

**ii)** $S(e^{j\Omega})=2-2\cos\Omega=\big|1-e^{-j\Omega}\big|^2\geq0$ para todo $\Omega$.
$$\boxed{\ \text{Sí es válida}\ }$$
**Construcción:** si $x[n]$ es Bernoulli $\pm1$, $R_{xx}[m]=\delta[m]$ (porque $E[x^2]=1$ y las muestras son independientes). Filtrando con $h[n]=\delta[n]-\delta[n-1]$, o sea $y[n]=x[n]-x[n-1]$, la autocorrelación de salida es $R_{yy}=R_{hh}*R_{xx}=R_{hh}$, con
$$R_{hh}[0]=1^2+(-1)^2=2,\qquad R_{hh}[\pm1]=(1)(-1)=-1,\qquad R_{hh}[m]=0 \text{ en otro caso}$$
que coincide exactamente con el $R[m]$ pedido.

###### **Verificación**
*(verificado con sympy: $S_A(j\omega)-4\cos^2(\omega\tau_o/2)=0$ y $S_C(j\omega)-\tau_o\,\text{sinc}^2(\omega\tau_o/2)=0$ simbólicamente; y el mínimo de $1+1.4\cos\Omega$ en $[0,2\pi]$ da $-0.4$ exacto.)*

---

## Ejercicio 3 — Muestreo de un proceso WSS con PSD triangular: aliasing

> [!quote] Enunciado
> 3. La figura P11.3-1 muestra un sistema de muestreo cuya entrada $x_c(t)$ es un proceso aleatorio WSS de media nula con la PSD mostrada en la figura P11.3-2. Asuma que el bloque continuo-a-discreto (C/D) es un muestreador ideal cuya salida es $x_d[n]=x_c(nT)$.
>
> ![[ej-p11-3.png]]
>
> a) Determine $E[x_c^2(t)]$, el valor cuadrático medio del proceso de entrada $x_c(t)$.
> b) Muestre que $R_{x_dx_d}[m]=R_{x_cx_c}(\tau)\big|_{\tau=mT}$. Indique si hay restricciones sobre el valor de $T$ para que esto sea cierto y, en tal caso, cuáles son.
> c) i) Determine y grafique $S_{x_dx_d}(e^{j\Omega})$ para $\frac1T=40$ kHz.
> ii) Determine y grafique $S_{x_dx_d}(e^{j\Omega})$ para $\frac1T=15$ kHz.

###### **Idea**
b) sale directo de la definición y de que $x_c$ es WSS, sin restricción alguna. c) es la fórmula de aliasing del muestreo: $S_{x_dx_d}(e^{j\Omega})=\frac1T\sum_k S_{x_cx_c}\big(j\frac{\Omega-2\pi k}{T}\big)$. Conviene comparar el semiancho de la PSD, $\omega_o=2\pi\times10^4$ rad/s, contra $\pi/T$ para saber si las réplicas se superponen.

###### **Resolución**
La PSD dada es un triángulo: $S_{x_cx_c}(j\omega)=1-\dfrac{|\omega|}{\omega_o}$ para $|\omega|\leq\omega_o=2\pi\times10^4$ rad/s, y $0$ fuera.

**a)** $E[x_c^2(t)]=R_{x_cx_c}(0)=\dfrac{1}{2\pi}\displaystyle\int S_{x_cx_c}(j\omega)\,d\omega=\dfrac{1}{2\pi}\times(\text{área del triángulo})=\dfrac{1}{2\pi}\times\omega_o$
$$\boxed{\ E[x_c^2(t)]=\frac{\omega_o}{2\pi}=10^4=10\,000\ }$$

**b)** Por definición y usando que $x_c$ es WSS (su correlación depende solo de la diferencia de tiempos):
$$R_{x_dx_d}[m]=E\big[x_d[n+m]x_d[n]\big]=E\big[x_c((n+m)T)\,x_c(nT)\big]=R_{x_cx_c}\big((n+m)T-nT\big)=R_{x_cx_c}(mT)$$
$$\boxed{\ \text{Vale para cualquier } T>0\text{, sin restricción}\ }$$
La igualdad es automática: es solo evaluar la definición en los instantes muestreados. Las restricciones sobre $T$ aparecen recién cuando se quiere relacionar $S_{x_dx_d}$ con $S_{x_cx_c}$ *sin aliasing* — que es justo lo que se explora en c).

**c) i) $1/T=40$ kHz** ($T=1/40\,000$ s). El semiancho de cada réplica en $\Omega$ es $\omega_oT=2\pi\times10^4/40\,000=\pi/2<\pi$: **no hay aliasing**, solo sobrevive la réplica $k=0$ dentro de $|\Omega|\leq\pi$:
$$\boxed{\ S_{x_dx_d}(e^{j\Omega})=40\,000\left(1-\frac{2}{\pi}|\Omega|\right)\ \text{para}\ |\Omega|\leq\frac\pi2,\qquad 0\ \text{para}\ \frac\pi2<|\Omega|\leq\pi\ }$$
Un triángulo que llega exactamente a $0$ en $\Omega=\pm\pi/2$ y se queda en $0$ hasta $\pm\pi$.

![[sol11-ej03-aliasing-40khz.svg]]
*(mirá que el triángulo toca cero antes de llegar a $\Omega=\pi$: hay "margen" de Nyquist de sobra.)*

**ii) $1/T=15$ kHz** ($T=1/15\,000$ s). Ahora $\omega_oT=2\pi\times10^4/15\,000=4\pi/3>\pi$: **hay aliasing**, las réplicas vecinas ($k=\pm1$) invaden la banda base. Sumando la réplica $k=0$ con la $k=1$ (y por simetría $k=-1$) dentro de $|\Omega|\leq\pi$, las dos rampas se cancelan parcialmente y dejan una meseta constante:
$$\boxed{\ S_{x_dx_d}(e^{j\Omega})=15\,000\left(1-\frac{3|\Omega|}{4\pi}\right)\ \text{para}\ |\Omega|\leq\frac{2\pi}{3},\qquad 7\,500\ \text{(constante)}\ \text{para}\ \frac{2\pi}{3}<|\Omega|\leq\pi\ }$$

![[sol11-ej03-aliasing-15khz.svg]]
*(a diferencia del caso i), acá el espectro NO llega a cero en $\Omega=\pi$: se aplana en $7\,500$ por el solapamiento de las réplicas — esa meseta es la firma visual del aliasing.)*

###### **Verificación**
*(verificado numéricamente: la suma de réplicas trasladadas, calculada con $\pm5$ términos, coincide con ambas fórmulas cerradas con error $<10^{-10}$; en el caso ii) la rampa y la meseta empalman exactamente en $\Omega=2\pi/3$ con valor $7\,500$, confirmando continuidad.)*

> [!warning] Ojo
> El resultado de b) (la igualdad $R_{x_dx_d}[m]=R_{x_cx_c}(mT)$ vale para cualquier $T$) no contradice que en c) sí importe el valor de $T$: lo que cambia con $T$ es si esas muestras de $R_{x_cx_c}$, vistas en el dominio $\Omega$, generan una PSD discreta que *coincide sin distorsión* con una versión comprimida de la continua (caso i) o si aparece aliasing que la deforma (caso ii). La igualdad temporal siempre vale; lo que se rompe es la ausencia de solapamiento espectral.

---

## Ejercicio 4 — Filtro pasa-altos ideal sobre ruido blanco

> [!quote] Enunciado
> 4. Se nos da un sistema LTI de tiempo discreto cuya respuesta en frecuencia $H(e^{j\Omega})$ sobre el intervalo $[-\pi,\pi]$ vale $1$ para $\pi/4<|\Omega|\leq\pi$, y $0$ para $|\Omega|\leq\pi/4$; en otras palabras, este sistema funciona como un filtro pasa-altos ideal. La entrada al sistema es un proceso de ruido blanco $w[n]$ con $E\{w^2[n]\}=10$. Si $v[n]$ denota la salida del sistema, ¿cuánto vale $E\{v^2[n]\}$?

###### **Idea**
Blanco $\Rightarrow$ PSD plana igual a la varianza. Filtrar multiplica la PSD por $|H|^2$ (que acá es una indicadora $0/1$), e integrar sobre la banda de paso da la potencia de salida.

###### **Resolución**
Ruido blanco con $E\{w^2[n]\}=10$: $S_{ww}(e^{j\Omega})=10$ para todo $\Omega$.
$$S_{vv}(e^{j\Omega})=|H(e^{j\Omega})|^2S_{ww}(e^{j\Omega})=\begin{cases}10 & \pi/4<|\Omega|\leq\pi\\ 0 & |\Omega|\leq\pi/4\end{cases}$$
$$E\{v^2[n]\}=R_{vv}[0]=\frac{1}{2\pi}\int_{-\pi}^{\pi}S_{vv}(e^{j\Omega})\,d\Omega=\frac{1}{2\pi}\cdot10\cdot\underbrace{2\left(\pi-\frac\pi4\right)}_{\text{medida de la banda}}=\frac{1}{2\pi}\cdot10\cdot\frac{3\pi}{2}$$
$$\boxed{\ E\{v^2[n]\}=7{,}5\ }$$

###### **Verificación**
*(verificado numéricamente: integral trapezoidal con $2\cdot10^6$ puntos sobre $[-\pi,\pi]$ da $7{,}499999...$, coincide con $7{,}5$.)*

---

## Ejercicio 5 — Verdadero o falso: varianza de salida y distribución de potencia

> [!quote] Enunciado
> 5. Para cada uno de los siguientes puntos, indique si la afirmación es verdadera o falsa, y dé una explicación breve.
>
> a) Considere un sistema LTI de tiempo discreto cuya respuesta en frecuencia es $H(e^{j\Omega})=2$ para $|\Omega|<\frac\pi2$, y $0$ en el resto del intervalo $[-\pi,\pi]$. Si el sistema es excitado por una señal de entrada i.i.d. $x[n]$ que toma los valores $\pm1$ con igual probabilidad, entonces la salida $y[n]$ del sistema tiene varianza unitaria, es decir $\sigma_{y[n]}^2=1$.
> b) Si la función de autocorrelación de un proceso aleatorio WSS $x[n]$ está dada por
> $$R_{xx}[m]=\delta[m]-0.3\big(\delta[m-1]+\delta[m+1]\big)$$
> entonces la distribución en frecuencia de la potencia instantánea esperada del proceso está más concentrada en bajas frecuencias que en altas.

###### **Idea**
Mismo mecanismo que el Ejercicio 4 (integrar $|H|^2S_{xx}$) para a); para b) alcanza con comparar $S(e^{j0})$ contra $S(e^{j\pi})$.

###### **Resolución**
**a)** $x[n]$ i.i.d. $\pm1$ equiprobable $\Rightarrow$ media $0$, $E[x^2]=1$, muestras independientes $\Rightarrow$ blanco: $S_{xx}(e^{j\Omega})=1$.
$$S_{yy}(e^{j\Omega})=|H|^2S_{xx}=\begin{cases}4 & |\Omega|<\pi/2\\ 0 & \text{resto}\end{cases}$$
$$\sigma_y^2=\frac{1}{2\pi}\int_{-\pi}^{\pi}S_{yy}\,d\Omega=\frac{1}{2\pi}\cdot4\cdot\pi=2$$
Como $\sigma_y^2=2\neq1$:
$$\boxed{\ \text{FALSO}\ }$$

**b)** $S_{xx}(e^{j\Omega})=1-0.3(e^{-j\Omega}+e^{j\Omega})=1-0.6\cos\Omega$.
$$S_{xx}(e^{j0})=1-0.6=0.4 \qquad(\text{baja frecuencia})$$
$$S_{xx}(e^{j\pi})=1+0.6=1.6 \qquad(\text{alta frecuencia, Nyquist})$$
Como $S(e^{j\pi})>S(e^{j0})$, la potencia está más concentrada en **altas** frecuencias, no en bajas:
$$\boxed{\ \text{FALSO}\ }$$
Tiene sentido: $R_{xx}[\pm1]<0$ significa muestras consecutivas anticorrelacionadas, o sea la señal tiende a oscilar rápido de signo — comportamiento típico de un proceso con energía concentrada cerca de Nyquist.

###### **Verificación**
*(verificado numéricamente: integral de a) da $\sigma_y^2\approx1{,}999998$; sympy confirma $S(e^{j0})=0{,}4$ y $S(e^{j\pi})=1{,}6$ exactos.)*

---

## Ejercicio 6 — Suma de procesos no correlacionados: separar espectros

> [!quote] Enunciado
> 6. Suponga que los procesos aleatorios WSS $g[\cdot]$ y $v[\cdot]$ son de media nula y están no correlacionados. Sea $x[n]=g[n]+v[n]$. Se nos dice que la PSD compleja de esta suma es
> $$S_{xx}(z)=\frac{\left(1-\tfrac13 z\right)\left(1-\tfrac13 z^{-1}\right)}{\left(1-\tfrac12 z\right)\left(1-\tfrac12 z^{-1}\right)}$$
> y que la autocorrelación de $v[n]$ es $R_{vv}[m]=\tfrac23\delta[m]$. Determine $S_{gg}(z)$ y $S_{gx}(z)$.

###### **Idea**
Cuando dos procesos de media nula están no correlacionados, la PSD de la suma es la suma de las PSD individuales, sin términos cruzados. Restando lo blanco aísla $S_{gg}$; $S_{gx}$ sale directo de la definición.

###### **Resolución**
Como $g$ y $v$ son de media nula y no correlacionados, $R_{gv}[m]=0$ para todo $m$, así que $S_{gv}(z)=S_{vg}(z)=0$ y
$$S_{xx}(z)=S_{gg}(z)+S_{vv}(z)$$
Con $R_{vv}[m]=\tfrac23\delta[m]$ (blanco): $S_{vv}(z)=\tfrac23$.

Expandiendo numerador y denominador de $S_{xx}(z)$:
$$\text{num}=1-\tfrac13 z-\tfrac13 z^{-1}+\tfrac19=\tfrac{10}{9}-\tfrac13(z+z^{-1}), \qquad \text{den}=\tfrac54-\tfrac12(z+z^{-1})$$
Restando $\tfrac23$ y simplificando (los términos en $(z+z^{-1})$ se cancelan exactamente entre numerador y el $\tfrac23\cdot$denominador):
$$S_{gg}(z)=S_{xx}(z)-\frac23=\frac{\tfrac{10}{9}-\tfrac23\cdot\tfrac54}{\tfrac54-\tfrac12(z+z^{-1})}=\frac{5/18}{\left(1-\tfrac12z\right)\left(1-\tfrac12z^{-1}\right)}$$
$$\boxed{\ S_{gg}(z)=\dfrac{5/18}{\left(1-\tfrac12z\right)\left(1-\tfrac12z^{-1}\right)}\ }$$

Para $S_{gx}(z)$: $R_{gx}[m]=E[g[n+m]x[n]]=E[g[n+m](g[n]+v[n])]=R_{gg}[m]+R_{gv}[m]=R_{gg}[m]$ (el segundo término es cero por no correlación). Como es la misma secuencia:
$$\boxed{\ S_{gx}(z)=S_{gg}(z)=\dfrac{5/18}{\left(1-\tfrac12z\right)\left(1-\tfrac12z^{-1}\right)}\ }$$

###### **Verificación**
*(verificado con sympy: $S_{xx}(z)-2/3-S_{gg}(z)$ simplifica simbólicamente a $0$; evaluado en varios puntos del círculo unidad, $S_{gg}(z)$ y la forma candidata coinciden hasta $10^{-15}$. Chequeo de sanidad en $z=1$: $S_{xx}(1)=16/9$, $S_{vv}=2/3$, $S_{gg}(1)=16/9-2/3=10/9$, que coincide con evaluar la forma cerrada en $z=1$.)*

---

## Ejercicio 7 — Filtro FIR de tres términos: covarianzas y PSD de salida

> [!quote] Enunciado
> 7. Suponga que $w[n]$ es un proceso aleatorio WSS de media nula, con $C_{ww}[m]=\sigma^2\delta[m]$. Si $w[n]$ es la entrada de un sistema causal cuya salida $y[n]$ satisface
> $$y[n]=w[n]+w[n-1]+w[n-2]$$
> determine la respuesta al impulso $h[\cdot]$ del sistema, y también las funciones de covarianza $C_{yw}[m]$ y $C_{yy}[m]$ en términos de $\sigma^2$. Luego calcule y grafique la PSD $S_{yy}(e^{j\Omega})$ de la salida, para $|\Omega|\leq\pi$ y tomando $\sigma^2=1$.

###### **Idea**
$h[n]$ sale directo de la ecuación de diferencias. $C_{yw}$ es la convolución de $h$ con $C_{ww}$, que al ser un impulso deja $C_{yw}=\sigma^2h$. $C_{yy}$ es $\sigma^2$ veces la autocorrelación determinística de $h$ consigo mismo, y la PSD sale de $|H|^2$.

###### **Resolución**
$$h[n]=\delta[n]+\delta[n-1]+\delta[n-2],\qquad\text{o sea } h[n]=1 \text{ para } n=0,1,2,\ \ 0 \text{ en el resto}$$

**$C_{yw}[m]$:** como $w$ tiene media nula (y por tanto $y$ también),
$$C_{yw}[m]=E[y[n+m]w[n]]=E\big[(w[n+m]+w[n+m-1]+w[n+m-2])\,w[n]\big]=\sigma^2\big(\delta[m]+\delta[m-1]+\delta[m-2]\big)$$
$$\boxed{\ C_{yw}[m]=\sigma^2\big(\delta[m]+\delta[m-1]+\delta[m-2]\big)\ \ (\text{vale }\sigma^2\text{ en }m=0,1,2)\ }$$

**$C_{yy}[m]$:** $C_{yy}[m]=\sigma^2R_{hh}[m]$, con $R_{hh}[m]=\sum_k h[k]h[k+m]$ la autocorrelación determinística de $h=[1,1,1]$:
$$R_{hh}[0]=3,\qquad R_{hh}[\pm1]=2,\qquad R_{hh}[\pm2]=1,\qquad 0 \text{ fuera de } |m|\leq2$$
$$\boxed{\ C_{yy}[m]=\sigma^2\big(3\delta[m]+2\delta[m-1]+2\delta[m+1]+\delta[m-2]+\delta[m+2]\big)\ }$$

**PSD:** $S_{yy}(e^{j\Omega})=\sigma^2|H(e^{j\Omega})|^2$, con $H(e^{j\Omega})=1+e^{-j\Omega}+e^{-j2\Omega}=e^{-j\Omega}(1+2\cos\Omega)$, así que $|H|^2=(1+2\cos\Omega)^2$. Con $\sigma^2=1$:
$$\boxed{\ S_{yy}(e^{j\Omega})=(1+2\cos\Omega)^2,\qquad |\Omega|\leq\pi\ }$$
Vale $9$ en $\Omega=0$, se anula en $\Omega=2\pi/3$ (donde $1+2\cos\Omega=0$) y vale $1$ en $\Omega=\pi$.

![[sol11-ej07-psd-salida.svg]]
*(el cero en $2\pi/3$ no es casual: es la frecuencia donde las tres muestras del promedio móvil se cancelan entre sí por interferencia destructiva — el filtro $h=[1,1,1]$ es un pasa-bajos con ese "hueco".)*

###### **Verificación**
*(verificado con sympy: $|H(e^{j\Omega})|^2$ expandido y simplificado coincide exactamente con $(1+2\cos\Omega)^2$; $R_{hh}$ calculada con `np.correlate` da $[1,2,3,2,1]$ para $m=-2,\dots,2$, igual que a mano.)*

---

## Ejercicio 8 — Densidad espectral cruzada dada por un gráfico: ¿es realizable?

> [!quote] Enunciado
> 8. Suponga que $x(\cdot)$ e $y(\cdot)$ son dos procesos aleatorios reales conjuntamente WSS. La autocorrelación de $x(t)$ es $R_{xx}(\tau)=e^{-|\tau|}$. Indique si es posible especificar una elección de $y(t)$ tal que la densidad espectral cruzada $S_{xy}(j\omega)$ sea la mostrada en la figura. Note que la amplitud en $\omega=1$ es $j=\sqrt{-1}$. Si su respuesta es no, explique por qué. Si es sí, explique cómo especificaría o construiría $y(t)$.
>
> ![[ej-p11-8.png]]

###### **Idea**
La vía más directa para construir un $y$ con densidad cruzada prescrita es pasar $x$ por un filtro LTI y ajustar $H$ para que reproduzca exactamente el $S_{xy}$ pedido. Como $S_{xx}(j\omega)$ nunca se anula, ese $H$ queda bien definido en todo $\omega$. Ojo con la convención: la relación correcta es $S_{xy}(j\omega)=H(j\omega)^*S_{xx}(j\omega)$, no $H(j\omega)S_{xx}(j\omega)$ — se deduce combinando $R_{xy}(\tau)=R_{yx}(-\tau)$ con $S_{yx}=HS_{xx}$.

###### **Resolución**
$S_{xx}(j\omega)=\mathcal F\{e^{-|\tau|}\}=\dfrac{2}{1+\omega^2}$, que nunca se anula (siempre $>0$).

De la figura, $S_{xy}(j\omega)=jf(\omega)$ es puramente imaginaria, con
$$f(\omega)=\begin{cases}\omega & 0\leq\omega\leq1\\ 2-\omega & 1\leq\omega\leq2\\ 0 & \omega>2\end{cases}\qquad f(-\omega)=-f(\omega)\ \ (\text{impar})$$

**Chequeo de consistencia.** Como $x,y$ son reales, $R_{xy}(\tau)$ es real, lo que exige simetría conjugada $S_{xy}(-j\omega)=S_{xy}(j\omega)^*$. Con $S_{xy}=jf(\omega)$ y $f$ impar: $S_{xy}(-j\omega)=jf(-\omega)=-jf(\omega)=\big(jf(\omega)\big)^*=S_{xy}(j\omega)^*$ ✓. La figura es geométricamente consistente con procesos reales.

**Construcción.** Definimos $y(t)$ como la salida de pasar $x(t)$ por un filtro LTI real $k(t)$, $y=k*x$. Usando $R_{xy}(\tau)=R_{yx}(-\tau)$ y $S_{yx}(j\omega)=K(j\omega)S_{xx}(j\omega)$, se obtiene $S_{xy}(j\omega)=S_{yx}(-j\omega)=K(-j\omega)S_{xx}(j\omega)$; y como $k(t)$ es real, $K(-j\omega)=K(j\omega)^*$, así que
$$S_{xy}(j\omega)=K(j\omega)^*\,S_{xx}(j\omega)\quad\Longrightarrow\quad K(j\omega)^*=\frac{jf(\omega)}{S_{xx}(j\omega)}=jf(\omega)\frac{1+\omega^2}{2}\quad\Longrightarrow\quad K(j\omega)=-jf(\omega)\frac{1+\omega^2}{2}$$
Explícitamente:
$$K(j\omega)=\begin{cases}-j\,\omega\,\dfrac{1+\omega^2}{2} & 0\leq\omega\leq1\\[4pt] -j\,(2-\omega)\,\dfrac{1+\omega^2}{2} & 1\leq\omega\leq2\\[4pt] 0 & |\omega|>2\end{cases}$$
y $K(-j\omega)=K(j\omega)^*$ (impar × real, coherente con que $k(t)$ sea real).

$$\boxed{\ \text{Sí es posible: } y(t)=(k*x)(t)\ \text{con el } K(j\omega) \text{ de arriba}\ }$$

Con esta elección, $S_{yy}(j\omega)=|K(j\omega)|^2S_{xx}(j\omega)=f(\omega)^2\dfrac{1+\omega^2}{2}$, que es real, par y no negativa (PSD válida por Bochner). La desigualdad cruzada $|S_{xy}|^2\leq S_{xx}S_{yy}$ se satura con **igualdad** en todo $\omega$: $y$ resulta ser exactamente una versión filtrada de $x$, sin componente independiente (coherencia de módulo $1$ en toda frecuencia donde $S_{xy}\neq0$).

###### **Verificación**
*(verificado numéricamente en 13 frecuencias entre $-3$ y $3$: $\text{conj}(K(j\omega))\cdot S_{xx}(j\omega)$ coincide exactamente con $jf(\omega)$, y por separado $|S_{xy}(j\omega)|^2=S_{xx}(j\omega)S_{yy}(j\omega)$ con diferencia $0$, como corresponde a esta construcción por filtrado puro.)*

> [!warning] Ojo
> Si uno usa ingenuamente $S_{xy}=H\,S_{xx}$ (la fórmula de $S_{yx}$, sin el conjugado) el filtro sale con el signo de $j$ invertido. La diferencia importa acá porque $S_{xy}$ es imaginaria pura: con el signo equivocado el $y(t)$ construido sigue siendo "válido" en el sentido de que reproduce $|S_{xy}|$, pero **no** el $S_{xy}(j\omega)$ exacto que pide el enunciado (con $+j$ en $\omega=1$).

> [!info] Conexión
> Esta construcción es el mismo mecanismo del Ejercicio 7 ("Coherencia máxima") de la Parte 5 de [[PROCESAMIENTO DE SEÑALES - Cap 11 en profundidad]]: cuando la desigualdad cruzada se satura, el filtro que iguala $S_{xy}$ es, frecuencia por frecuencia, el filtro de Wiener no causal del capítulo 12 con error cuadrático medio nulo.

---

## Ejercicio 9 — Verdadero o falso sobre espectro cruzado y autoespectros

> [!quote] Enunciado
> 9. La figura representa un sistema LTI estable con entrada $x[n]$ y salida $y[n]$, que son procesos aleatorios reales conjuntamente WSS con PSD $S_{xx}(e^{j\Omega})$ y $S_{yy}(e^{j\Omega})$ y densidad espectral cruzada $S_{xy}(e^{j\Omega})$.
>
> ![[ej-p11-9.png]]
>
> Para cada una de las afirmaciones siguientes, indique si es verdadera o falsa. Muestre claramente su razonamiento.
> a) En cualquier valor de $\Omega$ para el cual $S_{yy}(e^{j\Omega})$ no es cero, $S_{xy}(e^{j\Omega})$ necesariamente no es cero.
> b) En cualquier valor de $\Omega$ para el cual $S_{xy}(e^{j\Omega})$ no es cero, $S_{xx}(e^{j\Omega})$ necesariamente no es cero.
> c) En cualquier valor de $\Omega$ para el cual $S_{yy}(e^{j\Omega})$ es cero, $S_{xy}(e^{j\Omega})$ es necesariamente cero.
> d) La parte real de la densidad espectral cruzada $S_{xy}(e^{j\Omega})$ debe ser siempre no negativa.

###### **Idea**
Todo sale de dos identidades del capítulo 10, adaptadas a $S_{xy}$ igual que en el Ejercicio 8: $S_{yy}(e^{j\Omega})=|H(e^{j\Omega})|^2S_{xx}(e^{j\Omega})$ y $S_{xy}(e^{j\Omega})=H(e^{j\Omega})^*S_{xx}(e^{j\Omega})$ (el conjugado aparece porque el sistema — real, ya que $x,y$ son reales — tiene $H(e^{-j\Omega})=H(e^{j\Omega})^*$). Como el sistema es estable, $H$ es finito en todo $\Omega$, así que **ambas** expresiones se anulan exactamente bajo la misma condición.

###### **Resolución**
Para a), b), c) alcanza con mirar magnitudes: $|S_{xy}(\Omega)|=|H(\Omega)|\,S_{xx}(\Omega)$ (con $S_{xx}\geq0$ real), igual que $S_{yy}(\Omega)=|H(\Omega)|^2S_{xx}(\Omega)$. Ambas son cero exactamente cuando $H(\Omega)=0$ o $S_{xx}(\Omega)=0$ — **la misma condición**:
$$S_{xy}(\Omega)=0 \iff H(\Omega)=0 \text{ o } S_{xx}(\Omega)=0 \iff S_{yy}(\Omega)=0$$

**a)** $S_{yy}(\Omega)\neq0\Rightarrow$ (por la equivalencia) $S_{xy}(\Omega)\neq0$.
$$\boxed{\ \text{VERDADERO}\ }$$

**b)** Si $S_{xx}(\Omega)=0$, entonces $S_{xy}(\Omega)=H(\Omega)^*\cdot0=0$ ($H$ finito por estabilidad). Contrapositivo: $S_{xy}(\Omega)\neq0\Rightarrow S_{xx}(\Omega)\neq0$.
$$\boxed{\ \text{VERDADERO}\ }$$

**c)** $S_{yy}(\Omega)=0\Rightarrow$ (por la misma equivalencia) $S_{xy}(\Omega)=0$.
$$\boxed{\ \text{VERDADERO}\ }$$

**d)** **FALSO.** La fase de $H$ puede rotar $S_{xy}$ a cualquier valor complejo. **Contraejemplo:** retardo puro $y[n]=x[n-1]$, estable, $H(e^{j\Omega})=e^{-j\Omega}$, $H(e^{j\Omega})^*=e^{j\Omega}$. En $\Omega=\pi$: $H(e^{j\pi})^*=e^{j\pi}=-1$, así que
$$S_{xy}(e^{j\pi})=-S_{xx}(e^{j\pi})$$
que es real **negativo** si $S_{xx}(e^{j\pi})>0$ (por ejemplo con $x$ blanco, $S_{xx}=\text{cte}>0$). Entonces $\text{Re}\{S_{xy}(e^{j\pi})\}<0$, contradiciendo la afirmación.
$$\boxed{\ \text{FALSO}\ }$$

###### **Verificación**
*(verificado con un filtro FIR aleatorio de 4 taps y dos señales simuladas con $2\cdot10^5$ muestras usando un periodograma promediado: la razón estimada $\hat S_{xy}(\Omega)/\hat S_{xx}(\Omega)$ coincide con $H(e^{j\Omega})^*$ del filtro dentro del error esperado de estimación espectral, y $\hat S_{yy}\approx|H|^2\hat S_{xx}$ en los bines chequeados.)*

> [!warning] Ojo
> Es tentador escribir directamente $S_{xy}=HS_{xx}$ (sin el conjugado) porque es la fórmula que aparece explícita en el apunte — pero esa es la fórmula de $S_{yx}$, no de $S_{xy}$. En este ejercicio la distinción no cambia ninguna respuesta: en a), b) y c) solo importa dónde se anula $H$, y $H$ y $H^*$ se anulan en los mismos $\Omega$; en d) el contraejemplo se evalúa en $\Omega=\pi$, donde $e^{-j\pi}=e^{j\pi}=-1$ es real. Pero en cualquier $\Omega$ donde $H$ no sea real, usar $H$ en vez de $H^*$ da la fase de $S_{xy}$ equivocada (es lo que pasa en el Ejercicio 8).

## Ejercicio 10 — Densidad cruzada a través de un filtro pasatodo

> [!quote] Enunciado
> 10. Suponga que $q_1(t)$ se obtiene de $x_1(\cdot)$ filtrando a través de un sistema estable con respuesta en frecuencia $\frac{1-j\omega}{1+j\omega}$, y que $q_2(t)$ se obtiene de $x_2(\cdot)$ filtrando a través de otro sistema estable con la misma respuesta en frecuencia $\frac{1-j\omega}{1+j\omega}$. Exprese la densidad espectral cruzada $S_{q_1q_2}(j\omega)$ en términos de $S_{x_1x_2}(j\omega)$. Asuma que $x_1(\cdot)$ y $x_2(\cdot)$ son conjuntamente WSS.

###### **Idea**
Cuando dos procesos conjuntamente WSS se filtran cada uno con su propio LTI (con respuestas al impulso $h_1,h_2$ reales), la densidad cruzada de las salidas es $S_{y_1y_2}(j\omega)=H_1(j\omega)H_2^*(j\omega)\,S_{x_1x_2}(j\omega)$ — la generalización natural de $S_{yy}=|H|^2S_{xx}$ del capítulo 10 a dos filtros distintos. Acá $h_1=h_2=h$, y $H$ es **pasatodo** ($|H(j\omega)|=1$ para todo $\omega$), así que conviene mirar qué le hace específicamente ese caso particular.

###### **Resolución**
Escribimos $q_1(t)=\int h(a)\,x_1(t-a)\,da$ y $q_2(t)=\int h(b)\,x_2(t-b)\,db$. Entonces
$$R_{q_1q_2}(\tau)=E\{q_1(t+\tau)q_2(t)\}=\int\!\!\int h(a)h(b)\,E\{x_1(t+\tau-a)x_2(t-b)\}\,da\,db=\int\!\!\int h(a)h(b)\,R_{x_1x_2}(\tau-a+b)\,da\,db$$
Esto es una doble convolución: primero convolucionamos $R_{x_1x_2}$ con $h(\cdot)$ en la variable $\tau$, y después con $h(-\cdot)$ (el signo de $b$ entra invertido). Transformando —la convolución se vuelve producto— y usando que $h$ es real, por lo que $\mathcal F\{h(-t)\}=H(-j\omega)=H^*(j\omega)$:
$$S_{q_1q_2}(j\omega)=H(j\omega)\,H^*(j\omega)\,S_{x_1x_2}(j\omega)=|H(j\omega)|^2\,S_{x_1x_2}(j\omega)$$

Ahora calculamos $|H(j\omega)|^2$ para $H(j\omega)=\dfrac{1-j\omega}{1+j\omega}$. Como $\omega$ es real, $1+j\omega$ es exactamente el conjugado de $1-j\omega$, así que numerador y denominador tienen el mismo módulo:
$$|H(j\omega)|^2=\frac{(1-j\omega)(1+j\omega)}{(1+j\omega)(1-j\omega)}=1\qquad\text{para todo }\omega$$
Este es el sistema pasatodo canónico de primer orden de Señales y Sistemas: polo en $s=-1$, cero en $s=+1$, reflejados uno del otro respecto del eje imaginario, con ganancia unitaria en toda frecuencia (solo cambia la fase).

$$\boxed{\ S_{q_1q_2}(j\omega)=S_{x_1x_2}(j\omega)\ }$$

Un pasatodo aplicado a ambos procesos deja la densidad cruzada **completamente intacta**: le cambia la fase a cada componente en frecuencia, pero como el módulo es $1$ en todos lados, no altera el reparto de potencia (cruzada) entre bandas.

###### **Verificación**
Con sympy: $H(j\omega)\cdot\overline{H(j\omega)}$ simplifica simbólicamente a $1$, sin aproximación, para todo $\omega$ real *(verificado con sympy: `simplify` da exactamente 1)*.

> [!info] Conexión
> Es el mismo hecho que $S_{yy}=|H|^2S_{xx}$ del capítulo 10, pero cruzado entre dos procesos distintos filtrados con el mismo sistema. La Parte 2.3 de [[PROCESAMIENTO DE SEÑALES - Cap 11 en profundidad]] usa la misma idea de "solo importa $|H|^2$" para la ambigüedad de la factorización espectral.

---

## Ejercicio 11 — Densidad cruzada de dos filtrados del mismo proceso

> [!quote] Enunciado
> 11. Sea $x(t)$ un proceso WSS real de media nula con autocorrelación $R_{xx}(\tau)$; la transformada de Fourier de esta autocorrelación es la PSD $S_{xx}(j\omega)$. Suponga que $x(t)$ es procesado por un par de sistemas LTI estables como se muestra en la figura. Se sabe que las respuestas al impulso son reales.
>
> ![[ej-p11-11.png]]
>
> a) Halle $R_{y_1y_2}(\tau)$ y $S_{y_1y_2}(j\omega)$ en términos de $R_{xx}(\tau)$, $h_1(t)$, $h_2(t)$, $S_{xx}(j\omega)$, $H_1(j\omega)$ y $H_2(j\omega)$.
> b) Muestre que si $H_1(j\omega)$ y $H_2(j\omega)$ ocupan bandas de frecuencia disjuntas, entonces $y_1(\cdot)$ e $y_2(\cdot)$ están no correlacionados. ¿Están además garantizadamente independientes estadísticamente?

###### **Idea**
Es la misma cuenta que el Ejercicio 10, pero ahora con **un solo** proceso de entrada $x(t)$ pasado por **dos** filtros distintos $h_1\neq h_2$, y se pide dejar la deducción explícita (no solo usarla).

###### **Resolución**
**a)** Con $y_1(t)=\int h_1(a)x(t-a)\,da$ y $y_2(t)=\int h_2(b)x(t-b)\,db$:
$$R_{y_1y_2}(\tau)=E\{y_1(t+\tau)y_2(t)\}=\int\!\!\int h_1(a)h_2(b)\,E\{x(t+\tau-a)x(t-b)\}\,da\,db$$
$$\boxed{\ R_{y_1y_2}(\tau)=\int_{-\infty}^{\infty}\!\!\int_{-\infty}^{\infty} h_1(a)\,h_2(b)\,R_{xx}(\tau-a+b)\ da\,db\ }$$
que se puede leer como una doble convolución: primero convolucionar $R_{xx}$ con $h_1(\cdot)$, después con $h_2(-\cdot)$. Transformando en $\tau$ (la convolución se vuelve producto) y usando que $h_2$ es real, por lo que $\mathcal F\{h_2(-t)\}(j\omega)=H_2(-j\omega)=H_2^*(j\omega)$:
$$\boxed{\ S_{y_1y_2}(j\omega)=H_1(j\omega)\,H_2^*(j\omega)\,S_{xx}(j\omega)\ }$$

**b)** Si $H_1(j\omega)$ y $H_2(j\omega)$ ocupan bandas disjuntas, entonces en **cada** $\omega$ al menos uno de los dos vale cero, así que el producto $H_1(j\omega)H_2^*(j\omega)$ es idénticamente nulo, y por lo tanto
$$S_{y_1y_2}(j\omega)\equiv0\ \ \text{para todo }\omega\quad\Longrightarrow\quad R_{y_1y_2}(\tau)=\frac{1}{2\pi}\int_{-\infty}^{\infty}S_{y_1y_2}(j\omega)\,e^{j\omega\tau}\,d\omega=0\ \ \text{para todo }\tau$$
Como $x$ es de media nula y el filtrado es lineal, $y_1$ e $y_2$ también son de media nula, así que $C_{y_1y_2}(\tau)=R_{y_1y_2}(\tau)=0$:
$$\boxed{\ y_1(\cdot)\ \text{e}\ y_2(\cdot)\ \text{no están correlacionados}\ }$$

¿Independientes? **No necesariamente.** "No correlacionado" es una condición de **segundo orden únicamente**; independencia es mucho más fuerte (involucra todos los órdenes de momentos, o directamente las densidades conjuntas). La implicación "no correlacionado $\Rightarrow$ independiente" solo vale bajo hipótesis extra —la más común, que $x(t)$ (y por lo tanto $y_1,y_2$, al ser combinaciones lineales) sea **gaussiano**—, y acá no se asume nada de eso.

###### **Verificación**
Simulé numéricamente: generé $x[n]$ como un AR(1) (análogo de tiempo discreto, para poder simular), lo filtré con dos FIR arbitrarios $h_1=[1,\,0.5,\,-0.3]$ y $h_2=[0.2,\,-1,\,0.7,\,0.1]$, y comparé la correlación cruzada empírica contra $\sum_a\sum_b h_1[a]h_2[b]R_{xx}[m-a+b]$: coinciden a las centésimas para $m=-3,\dots,3$ (p. ej. $m=0$: teórico $-0{,}620$, empírico $-0{,}619$; $m=-1$: teórico $-0{,}590$, empírico $-0{,}589$).

> [!info] Conexión
> Es el mismo resultado del Ejercicio 10, escrito para dos filtros distintos sobre el mismo proceso en lugar de un filtro igual sobre dos procesos distintos. Compará también con $S_{yy}=|H|^2S_{xx}$ del capítulo 10 (caso particular $h_1=h_2$, $S_{y_1y_2}\to S_{yy}$, que sale real y $\geq0$ como corresponde a una PSD propia).

---

## Ejercicio 12 — Proceso AR(1): estabilidad, PSD y predicción LMMSE

> [!quote] Enunciado
> 12. Suponga que la salida $y[n]$ y la entrada $w[n]$ de un sistema LTI causal de tiempo discreto están relacionadas por
> $$y[n]=\lambda\ y[n-1]+w[n]$$
> para todo instante $n$.
>
> a) ¿Cuál es la respuesta al impulso $h[n]$ de este sistema, y qué condición sobre $\lambda$ asegura que el sistema sea BIBO estable?
>
> Asuma para el resto del problema que se cumple la condición de estabilidad del punto a). Además, suponga que la entrada $w[n]$ es en realidad un proceso WSS cuya PSD $S_{ww}(e^{j\Omega})$ es constante e igual a algún valor $M>0$ para toda frecuencia $\Omega$.
>
> b) ¿Cuál es el valor medio $\mu_w$ de la entrada $w[n]$? ¿Y cuál es la autocovarianza $C_{ww}[m]$ de $w[n]$?
>
> Todas las respuestas restantes deben expresarse en términos de $\lambda$ y $M$.
>
> c) Determine la PSD $S_{yy}(e^{j\Omega})$ de la salida. Asumiendo $\lambda>0$, determine en qué frecuencias del rango $|\Omega|\leq\pi$ esta PSD toma sus valores máximo y mínimo, y halle esos valores.
> d) Por el método que prefiera, determine $C_{yy}[0]$ y $C_{yy}[1]$, donde $C_{yy}[m]$ denota la autocovarianza de la salida.
> e) Determine el estimador LMMSE
> $$\hat y[4]=c\ y[3]+d$$
> de $y[4]$ en términos de $y[3]$, es decir, halle las constantes $c$ y $d$ que minimizan el error cuadrático medio $E[(y[4]-\hat y[4])^2]$. Determine además el error cuadrático medio asociado.
> f) Determine el estimador LMMSE $\hat y[3]$ de $y[3]$ en términos de $y[4]$, y el error cuadrático medio asociado.
> g) Determine el estimador LMMSE de $y[4]$ en términos de todos los valores pasados $y[k]$, $k\leq3$, y determine el error cuadrático medio asociado. *(Pista: usá lo que sabés de la relación entre $y[n]$ y $w[n]$ para conjeturar una forma para este estimador, y después verificá que se cumplan las condiciones de ortogonalidad requeridas.)*

###### **Idea**
Es un AR(1) causal excitado por blanco. Todo sale de: (a) resolver la ecuación en diferencias para $h[n]$; (b) usar que un espectro constante y finito en **toda** frecuencia (sin impulso en $\Omega=0$) obliga a media nula; (c)-(d) aplicar $S_{yy}=|H|^2S_{ww}$ y la fórmula de autocovarianza de la salida de un filtro estable excitado por blanco; (e)-(g) son LMMSE escalar del capítulo 8 aplicado a pares de muestras de $y$, explotando que $y[n]-\lambda y[n-1]=w[n]$ es exactamente la "innovación".

###### **Resolución**
**a)** Reescribimos la ecuación en diferencias: $y[n]-\lambda y[n-1]=w[n]$. Transformando: $Y(z)(1-\lambda z^{-1})=W(z)\Rightarrow H(z)=\dfrac{1}{1-\lambda z^{-1}}$. Como el sistema es causal, expandimos en serie de potencias de $z^{-1}$ (ROC $|z|>|\lambda|$):
$$\boxed{\ h[n]=\lambda^n\,u[n]\ }$$
BIBO estable $\Leftrightarrow$ $h[\cdot]$ absolutamente sumable $\Leftrightarrow$ $\sum_n|\lambda|^n<\infty$:
$$\boxed{\ |\lambda|<1\ }$$

**b)** $S_{ww}(e^{j\Omega})=M$ para **toda** $\Omega$, sin ningún impulso. Recordando la relación entre PSD y FSD del capítulo 11, $S_{ww}(e^{j\Omega})=D_{ww}(e^{j\Omega})+2\pi\mu_w^2\sum_k\delta(\Omega-2\pi k)$: si $\mu_w\neq0$ habría un impulso infinito en $\Omega=0$, incompatible con que $S_{ww}$ sea **finita e igual a $M$ ahí**. Entonces
$$\boxed{\ \mu_w=0\ }$$
Con media nula, $C_{ww}[m]$ es la transformada inversa del espectro plano:
$$C_{ww}[m]=\frac{1}{2\pi}\int_{-\pi}^{\pi}M\,e^{j\Omega m}\,d\Omega=M\,\delta[m]\quad\Longrightarrow\quad\boxed{\ C_{ww}[m]=M\,\delta[m]\ }$$
o sea, $w[n]$ es blanco de intensidad $M$.

**c)** $S_{yy}(e^{j\Omega})=|H(e^{j\Omega})|^2S_{ww}(e^{j\Omega})=\dfrac{M}{|1-\lambda e^{-j\Omega}|^2}=\dfrac{M}{1-2\lambda\cos\Omega+\lambda^2}$.

Con $\lambda>0$, el denominador $1-2\lambda\cos\Omega+\lambda^2$ es **mínimo** en $\Omega=0$ (ahí $\cos\Omega=1$, denominador $=(1-\lambda)^2$) y **máximo** en $\Omega=\pm\pi$ (ahí $\cos\Omega=-1$, denominador $=(1+\lambda)^2$). Como $S_{yy}$ es el recíproco del denominador, pasa lo contrario:
$$\boxed{\ S_{yy}\Big|_{\text{máx}}=S_{yy}(0)=\frac{M}{(1-\lambda)^2}\ ,\qquad S_{yy}\Big|_{\text{mín}}=S_{yy}(\pm\pi)=\frac{M}{(1+\lambda)^2}\ }$$

**d)** Como $y$ es la salida de un filtro estable y causal excitado por blanco de intensidad $M$, su autocovarianza es
$$C_{yy}[m]=M\sum_{k=0}^{\infty}h[k]\,h[k+|m|]=M\sum_{k=0}^{\infty}\lambda^{2k+|m|}=\frac{M\lambda^{|m|}}{1-\lambda^2}$$
$$\boxed{\ C_{yy}[0]=\frac{M}{1-\lambda^2}\ ,\qquad C_{yy}[1]=\frac{M\lambda}{1-\lambda^2}\ }$$

**e)** El estimador LMMSE afín de $y[4]$ a partir de $y[3]$ (capítulo 8), con $\mu_y=0$ (filtro LTI aplicado a entrada de media nula):
$$c=\frac{C_{yy}[1]}{C_{yy}[0]}=\lambda\ ,\qquad d=\mu_y(1-c)=0$$
$$\boxed{\ \hat y[4]=\lambda\,y[3]\ }$$
con error $\text{MSE}=C_{yy}[0](1-\rho^2)$, $\rho=C_{yy}[1]/C_{yy}[0]=\lambda$:
$$\boxed{\ \text{MSE}=\frac{M}{1-\lambda^2}(1-\lambda^2)=M\ }$$
Tiene sentido a ojo: $y[4]=\lambda y[3]+w[4]$, y $w[4]$ es independiente de $y[3]$ (que solo depende de $w[k]$, $k\leq3$). El mejor predictor lineal reconstruye exactamente la parte $\lambda y[3]$, y lo que queda de error es, literalmente, $w[4]$ — cuya varianza es $M$.

**f)** Por la misma fórmula, ahora estimando $y[3]$ desde $y[4]$ (y usando que $C_{yy}[-1]=C_{yy}[1]$ por ser $y$ real WSS):
$$\hat y[3]=\frac{C_{yy}[1]}{C_{yy}[0]}\,y[4]=\lambda\,y[4]\ ,\qquad\text{MSE}=C_{yy}[0](1-\lambda^2)=M$$
$$\boxed{\ \hat y[3]=\lambda\,y[4]\ ,\qquad\text{MSE}=M\ }$$
Mismo coeficiente y mismo error que en e). Esto puede sorprender: el LMMSE de un paso solo depende de $\rho[1]=C_{yy}[1]/C_{yy}[0]$, que es el mismo mirando "para adelante" o "para atrás" porque $y$ es estacionario ($C_{yy}$ es par). **Ojo:** esto no significa que $\hat y[3]=y[4]/\lambda$ (despejando ingenuamente la ecuación en diferencias) — esa NO es en general la proyección lineal óptima; acá coincide con $\lambda y[4]$ solo porque salió así de la cuenta, no por haber "invertido" la recursión.

**g)** Conjeturamos, guiados por la estructura autorregresiva, que el mejor predictor usando **todo** el pasado es el mismo que usando solo la muestra más reciente:
$$\hat y[4]=\lambda\,y[3]$$
Para confirmarlo hay que verificar ortogonalidad: el error $e=y[4]-\lambda y[3]=w[4]$ tiene que ser no correlacionado con $y[k]$ para **todo** $k\leq3$. Escribiendo $y[k]=\sum_{j=0}^{\infty}h[j]\,w[k-j]$:
$$E\{w[4]\,y[k]\}=\sum_{j=0}^{\infty}h[j]\,E\{w[4]\,w[k-j]\}=\sum_{j=0}^{\infty}h[j]\,M\,\delta[4-(k-j)]$$
El delta pide $k-j=4$, o sea $j=k-4$. Para $k\leq3$ eso da $j\leq-1<0$, fuera del rango de la suma ($j\geq0$). Entonces $E\{w[4]\,y[k]\}=0$ para todo $k\leq3$: la ortogonalidad se cumple, y la conjetura queda verificada.
$$\boxed{\ \hat y[4]=\lambda\,y[3]\ ,\qquad\text{MSE}=M\ }$$
Coincide exactamente con e): en un AR(1), toda la memoria útil para predecir un paso adelante ya está contenida en la última muestra — el pasado más lejano no agrega nada (a diferencia del ejemplo "bandeado" del capítulo 12, donde muestras no correlacionadas con el objetivo sí ayudaban).

###### **Verificación**
Simulé $2\times10^6$ muestras de este AR(1) con $\lambda=0{,}6$, $M=2$ (descartando transitorio): $C_{yy}[0]$ teórico $3{,}125$ vs. simulado $3{,}123$; $C_{yy}[1]$ teórico $1{,}875$ vs. simulado $1{,}873$; varianza del residuo $y[n]-\lambda y[n-1]$ teórica $M=2$ vs. simulada $1{,}999$ — todo dentro del error de muestreo esperable.

> [!info] Conexión
> Es el mismo "Caso 1: proceso exponencialmente correlacionado" de la sección de predicción FIR del capítulo 12 del apunte ($C_{xx}[m]=C_0\alpha^{|m|}\Rightarrow$ solo importa la última muestra), aplicado acá de punta a punta con números concretos y con la verificación de ortogonalidad hecha explícita.

---

## Ejercicio 13 — Fase mínima no es necesaria para modelar, sí para invertir

> [!quote] Enunciado
> 13. Queremos producir un proceso estocástico WSS $y[n]$ con una función de autocorrelación $R_{yy}[m]$ especificada. El enfoque es aplicar un filtro LTI a un proceso aleatorio blanco $x[n]$ como se indica en la figura.
>
> ![[ej-p11-13.png]]
>
> El proceso $x[n]$ tiene media nula y función de autocorrelación
> $$R_{xx}[m]=\delta[m]=\begin{cases}1 & m=0\\ 0 & m\neq0\end{cases}$$
> Elegiremos la función de transferencia $H(z)$ del filtro de modo que $R_{yy}[m]=0.5^{|m|}$, con PSD correspondiente
> $$S_{yy}(e^{j\Omega})=\frac{1}{\left(1-\tfrac12 e^{-j\Omega}\right)\left(1-\tfrac12 e^{j\Omega}\right)}=\frac{3}{5-4\cos\Omega}$$
>
> a) Elija la afirmación correcta y explique su razonamiento. Para obtener el $y[n]$ deseado, $H(z)$ debe representar un sistema:
> i) estable y de fase mínima;
> ii) estable, pero que no necesita ser de fase mínima;
> iii) que no necesita ser ni estable ni de fase mínima.
> b) Elija la afirmación correcta y explique su razonamiento. De lo dado, podemos decir que $x[n]$ y $x[n+k]$, $k\neq0$, son:
> i) definitivamente independientes;
> ii) definitivamente no independientes;
> iii) pueden ser independientes.
> c) Elija la afirmación correcta y explique su razonamiento. De lo dado, podemos decir que $y[n]$ e $y[n+k]$, $k\neq0$, son:
> i) definitivamente independientes;
> ii) definitivamente no independientes;
> iii) pueden ser independientes.
> d) Determine una elección de $H(z)$ (incluyendo su región de convergencia) que produzca un proceso $y[n]$ con la $R_{yy}[m]$ deseada.

> [!warning] Nota sobre el enunciado
> La igualdad intermedia que escribe la guía, $\dfrac{1}{\left(1-\frac12e^{-j\Omega}\right)\left(1-\frac12e^{j\Omega}\right)}=\dfrac{3}{5-4\cos\Omega}$, **no es cierta**: el lado izquierdo, desarrollado, da $\dfrac{4}{5-4\cos\Omega}$ (verificado con sympy), no $\dfrac{3}{5-4\cos\Omega}$. El original (P11.12) no escribe un producto sino una **suma** de dos términos de un solo polo cada uno —la descomposición causal + anticausal de $\rho^{|m|}$—:
> $$S_{yy}(e^{j\Omega})=\frac{1}{1-\frac12e^{-j\Omega}}+\frac{\frac12e^{j\Omega}}{1-\frac12e^{j\Omega}}=\frac{3}{5-4\cos\Omega}$$
> y esa sí cierra exactamente (verificado con sympy). El target final, $R_{yy}[m]=0{,}5^{|m|}$ con $S_{yy}(e^{j\Omega})=\dfrac{3}{5-4\cos\Omega}$, es el mismo en la guía y en el libro, y es el que se usa de acá en más — el error de transcripción está solo en esa fórmula intermedia "ilustrativa", y no afecta ninguna de las respuestas a a)-d).

###### **Idea**
a)-c) son conceptuales, sobre qué información alcanza para concluir qué; d) es una factorización espectral.

###### **Resolución**
**a)** Solo necesitamos que $H(z)$, filtrando blanco, produzca una salida con $|H(e^{j\Omega})|^2=S_{yy}(e^{j\Omega})$ dado. Esa condición fija **únicamente el módulo** de $H$ sobre el círculo unidad: cualquier elección de fase —cualquier factor pasatodo multiplicando— da el mismo $|H|^2$ y por lo tanto la **misma** $R_{yy}[m]$, porque la autocorrelación de la salida depende solo de $|H(e^{j\Omega})|^2$ (Ejercicio 10). Lo único indispensable es que $H(z)$ sea **estable** (si no, $y[n]$ ni siquiera queda bien definido como proceso WSS con esa PSD). No hace falta fase mínima: nadie pide acá que $H$ sea invertible causalmente, solo que **genere** el proceso correcto.
$$\boxed{\text{ii) estable, pero no necesita ser de fase mínima}}$$

**b)** Lo único que se dio de $x[n]$ es $R_{xx}[m]=\delta[m]$: blanco, es decir **no correlacionado**. Eso es información de segundo orden únicamente. No correlacionado no implica independiente en general —hace falta una hipótesis extra, típicamente gaussianidad, que acá no está—, así que con lo dado no se puede afirmar ni negar la independencia:
$$\boxed{\text{iii) pueden ser independientes}}$$

**c)** Acá $R_{yy}[m]=0{,}5^{|m|}\neq0$ para todo $m$ finito: $y[n]$ e $y[n+k]$ están correlacionados para cualquier $k$. Independencia siempre implica no correlación (sin hipótesis extra); por contrarrecíproco, correlación no nula implica que **no** pueden ser independientes:
$$\boxed{\text{ii) definitivamente no independientes}}$$

**d)** Factorizamos $S_{yy}(z)=\dfrac{3}{5-4\cos\Omega}$. Usando $(1-\tfrac12z^{-1})(1-\tfrac12z)=\tfrac54-\cos\Omega=\tfrac14(5-4\cos\Omega)$:
$$S_{yy}(z)=\frac{3}{4\left(1-\tfrac12z^{-1}\right)\left(1-\tfrac12z\right)}=\underbrace{\frac{\sqrt3/2}{1-\tfrac12z^{-1}}}_{F(z)}\cdot\underbrace{\frac{\sqrt3/2}{1-\tfrac12z}}_{F(z^{-1})}$$
Elegimos el factor causal y estable (polo en $z=\tfrac12$, dentro del círculo unidad):
$$\boxed{\ H(z)=\frac{\sqrt3/2}{1-\tfrac12z^{-1}}\ ,\qquad\text{ROC: }|z|>\tfrac12\ }$$
Por lo visto en a), esta no es la única elección válida (cualquier pasatodo multiplicándola sirve igual), pero sí es una elección concreta y, de yapa, de fase mínima.

###### **Verificación**
sympy confirma que $\left|\dfrac{\sqrt3/2}{1-\frac12e^{-j\Omega}}\right|^2=\dfrac{3}{5-4\cos\Omega}$ exactamente para todo $\Omega$ (diferencia simbólica nula), y que la fórmula-suma del libro (nota de arriba) también simplifica exactamente a $\dfrac{3}{5-4\cos\Omega}$.

---

## Ejercicio 14 — Factorización espectral de una PSD racional de primer orden

> [!quote] Enunciado
> 14. La entrada a un sistema estable y causal de primer orden particular, con función de transferencia $H(z)$, es un proceso de ruido blanco de intensidad unitaria $w[n]$, es decir, un proceso con PSD $S_{ww}(e^{j\Omega})=1$. La salida correspondiente $y[n]$ es un proceso WSS con PSD
> $$S_{yy}(e^{j\Omega})=16\ \frac{(1-3z^{-1})(1-3z)}{(1-4z^{-1})(1-4z)}\Bigg|_{z=e^{j\Omega}}$$
>
> a) Grafique esta PSD como función de $\Omega$ para $|\Omega|\leq\pi$.
> b) Suponga que sabemos que el sistema tiene una inversa estable y causal, también de primer orden. Halle una elección de $H(z)$ consistente con esta información.

###### **Idea**
a) es evaluar/graficar la PSD dada. b) es factorización espectral con la condición extra de que la inversa también sea estable y causal: fase mínima.

###### **Resolución**
**a)** Con $z=e^{j\Omega}$ y $z+z^{-1}=2\cos\Omega$:
$$(1-3z^{-1})(1-3z)=1-3z-3z^{-1}+9=10-6\cos\Omega\ ,\qquad(1-4z^{-1})(1-4z)=17-8\cos\Omega$$
$$\boxed{\ S_{yy}(e^{j\Omega})=\frac{16(10-6\cos\Omega)}{17-8\cos\Omega}\ }$$
En $\Omega=0$: $S_{yy}=16\cdot\tfrac{4}{9}=\tfrac{64}{9}\approx7{,}11$. En $\Omega=\pm\pi$: $S_{yy}=16\cdot\tfrac{16}{25}=\tfrac{256}{25}=10{,}24$.

![[sol11-ej14-psd-salida.svg]]
La curva crece monótonamente de $\Omega=0$ a $\Omega=\pm\pi$ (mínimo y máximo en los extremos del intervalo): el ruido de entrada era plano, pero el filtro le da forma, dejando pasar algo más de potencia relativa en alta frecuencia.

**b)** Buscamos $H(z)$ estable y causal de primer orden, con inversa **también** estable y causal de primer orden —o sea, de fase mínima—, tal que $H(z)H(z^{-1})=S_{yy}(z)/S_{ww}(z)=S_{yy}(z)$.

Igual que en a), sacamos factor común: $1-3z=-3z(1-\tfrac13z^{-1})$ y $1-4z=-4z(1-\tfrac14z^{-1})$, de donde $|1-3e^{-j\Omega}|^2=9\left|1-\tfrac13e^{-j\Omega}\right|^2$ y $|1-4e^{-j\Omega}|^2=16\left|1-\tfrac14e^{-j\Omega}\right|^2$. Reemplazando:
$$S_{yy}(e^{j\Omega})=16\cdot\frac{9\left|1-\tfrac13e^{-j\Omega}\right|^2}{16\left|1-\tfrac14e^{-j\Omega}\right|^2}=9\left|\frac{1-\tfrac13e^{-j\Omega}}{1-\tfrac14e^{-j\Omega}}\right|^2$$
El polo de $\dfrac{1-\frac13z^{-1}}{1-\frac14z^{-1}}$ está en $z=\tfrac14$ (dentro del círculo: estable y causal); su cero está en $z=\tfrac13$ (dentro también, así que la inversa tiene su polo en $z=\tfrac13$: también estable y causal). Fase mínima ✓. Con la constante $\sqrt9=3$:
$$\boxed{\ H(z)=3\,\frac{1-\tfrac13z^{-1}}{1-\tfrac14z^{-1}}\ ,\qquad\text{ROC: }|z|>\tfrac14\ }$$
La rama alternativa (polo y/o cero afuera del círculo) daría, si se exige causalidad, un sistema o una inversa inestables — ninguna de las dos sirve acá.

###### **Verificación**
sympy confirma $|H(e^{j\Omega})|^2=\dfrac{16(10-6\cos\Omega)}{17-8\cos\Omega}$ exactamente para todo $\Omega$ (diferencia simbólica nula), y que $S_{yy}(0)=64/9$, $S_{yy}(\pi)=256/25$ como en a).

---

## Ejercicio 15 — Factorización espectral en tiempo continuo, con y sin fase mínima

> [!quote] Enunciado
> 15. Una PSD medida para un proceso aleatorio de tiempo continuo se modela como
> $$S(j\omega)=\frac{\omega^2+1}{\omega^2+100}$$
> Queremos representar el proceso como la salida de un filtro LTI con función de transferencia $H(s)$ excitado por un proceso de ruido blanco $w(t)$, donde $S_{ww}(j\omega)=1$.
>
> a) Asuma que $H(s)$ es de fase mínima. Determine una elección para $H(s)$.
> b) Asuma que $H(s)$ solo está restringido a ser causal y estable, en lugar de fase mínima. Suponga que además se sabe que $h(t)$ decae asintóticamente como $e^{-t}$ cuando $t\to\infty$, es decir, que para $t\to\infty$ $h(t)$ es aproximadamente proporcional a $e^{-t}$. Determine una elección para $H(s)$.

###### **Idea**
Factorización espectral en tiempo continuo: buscamos $H(s)$ tal que $H(s)H(-s)\big|_{s=j\omega}=S(j\omega)$. La parte a) es la elección de fase mínima (todo adentro del semiplano izquierdo). La parte b) pide una elección que **no** sea de fase mínima pero con un decaimiento asintótico específico, lo que obliga a "importar" un polo lento con un pasatodo — la misma jugada que la Actividad — Ejercicio 12.16 del apunte, pero usada al revés.

###### **Resolución**
**a)** Sustituyendo $s=j\omega$ (o sea $\omega^2=-s^2$): $\omega^2+1=1-s^2=(1-s)(1+s)$ y $\omega^2+100=100-s^2=(10-s)(10+s)$. Probamos $H(s)=\dfrac{s+1}{s+10}$:
$$H(j\omega)H(-j\omega)=\frac{(j\omega+1)(-j\omega+1)}{(j\omega+10)(-j\omega+10)}=\frac{1+\omega^2}{100+\omega^2}=S(j\omega)\ ✓$$
Polo en $s=-10$ (semiplano izquierdo: estable y causal); cero en $s=-1$ (también izquierdo, así que $1/H(s)$ tiene su único polo en $s=-1$: estable y causal). Fase mínima ✓.
$$\boxed{\ H(s)=\frac{s+1}{s+10}\ }$$

**b)** Ahora no pedimos fase mínima, pero sí que $h(t)\sim e^{-t}$ cuando $t\to\infty$. El único polo de un $H(s)$ causal-estable de **primer orden** con esta $S(j\omega)$ está forzado a $s=-10$ (la otra raíz del denominador, $s=+10$, está en el semiplano derecho y da un sistema inestable si se usa como polo causal) — así que un $H(s)$ de primer orden nunca puede tener un polo en $s=-1$, y su $h(t)$ decae siempre como $e^{-10t}$, no como $e^{-t}$. Para conseguir el decaimiento pedido hace falta **subir el orden**, agregando un polo en $s=-1$ sin tocar $|H(j\omega)|^2$.

Partimos de la rama de fase **no** mínima de a) (cero en $s=+1$ en lugar de $s=-1$):
$$H_0(s)=\frac{1-s}{s+10}\ ,\qquad H_0(j\omega)H_0(-j\omega)=\frac{(1-j\omega)(1+j\omega)}{(10+j\omega)(10-j\omega)}=\frac{1+\omega^2}{100+\omega^2}=S(j\omega)\ ✓$$
(sigue siendo estable y causal: el único polo sigue en $s=-10$; pero ya no es de fase mínima, porque su cero quedó en $s=+1$, afuera).

Multiplicamos por el pasatodo estable $A(s)=\dfrac{s-1}{s+1}$ (polo en $s=-1$, cero en $s=+1$; $|A(j\omega)|=1$ para todo $\omega$ real, porque numerador y denominador son conjugados sobre el eje imaginario). El cero de $H_0$ está en $s=+1$, el mismo lugar que el cero de $A$ —no el polo—, así que no hay cancelación con el polo nuevo de $A$ (que está en $s=-1$, un lugar libre):
$$H(s)=H_0(s)\,A(s)=\frac{1-s}{s+10}\cdot\frac{s-1}{s+1}=\frac{-(s-1)^2}{(s+10)(s+1)}$$
Como $|A(j\omega)|=1$, $|H(j\omega)|^2=|H_0(j\omega)|^2=S(j\omega)$ sigue intacto (el signo y la escala son libres; tomamos el signo positivo):
$$\boxed{\ H(s)=\frac{(s-1)^2}{(s+1)(s+10)}\ }$$
Polos en $s=-1$ y $s=-10$ (ambos estables: causal-estable ✓), cero doble en $s=+1$ (no es de fase mínima, como se pedía). En fracciones parciales:
$$H(s)=1-\frac{121/9}{s+10}+\frac{4/9}{s+1}\quad\Longrightarrow\quad h(t)=\delta(t)-\frac{121}{9}e^{-10t}u(t)+\frac49e^{-t}u(t)$$
Para $t\to\infty$ el término $e^{-10t}$ se apaga mucho antes que $e^{-t}$, así que $h(t)\to\tfrac49e^{-t}$: **$h(t)$ es efectivamente asintóticamente proporcional a $e^{-t}$**, tal como pedía el enunciado.
$$\boxed{\ H(s)=\frac{(s-1)^2}{(s+1)(s+10)}\ }$$

###### **Verificación**
sympy confirma $|H(j\omega)|^2=\dfrac{\omega^2+1}{\omega^2+100}$ exactamente para las elecciones de a) y de b) (diferencia simbólica nula en ambos casos), y la descomposición en fracciones parciales de b) coincide con la de arriba: $1-\dfrac{121/9}{s+10}+\dfrac{4/9}{s+1}$.

> [!info] Conexión
> Es la misma jugada que la pista de la Actividad — Ejercicio 12.16 del apunte, usada al revés: ahí se corregía un cero "del lado que no toca" multiplicando por un pasatodo; acá usamos el pasatodo para **importar** un polo lento que termine dominando el decaimiento asintótico de $h(t)$.

---

## Ejercicio 16 — Filtro de tres taps: incógnitas, tipo de filtro y un blanqueador imposible

> [!quote] Enunciado
> 16. Considere el sistema LTI mostrado en la figura P11.16-1. Acá $x[n]$ es un proceso i.i.d. con media $\mu_x=1$ y varianza $\sigma_x^2=\frac14$. La respuesta al impulso $h[n]$ del sistema se da en la figura P11.16-2.
>
> ![[ej-p11-16.png]]
>
> El proceso $y[n]$ a la salida tiene media nula y varianza $\sigma_y^2=\frac32$. El espectro cruzado $S_{yx}(e^{j\Omega})$ entre la entrada y la salida del sistema es una función real de $\Omega$.
>
> a) Determine los valores de $a$, $b$ y $c$ consistentes con la información dada.
> b) Determine y grafique el espectro $S_{yy}(e^{j\Omega})$ del proceso $y[n]$ para $\Omega\in[-\pi,\pi]$. ¿Qué tipo de filtro es $h[n]$ (pasa-bajos, pasa-altos, pasa-banda, elimina-banda, pasa-todo)?
> c) Si es posible, halle la respuesta al impulso $g[n]$ de un sistema LTI causal y estable cuya salida $w[\cdot]$ sea un proceso blanco cuando su entrada es el proceso $y[\cdot]$. Si no es posible, explique por qué.

###### **Idea**
Primero hay que despejar $a,b,c$ de tres condiciones (media nula de $y$, varianza de $y$, $S_{yx}$ real), después clasificar el filtro por su respuesta en frecuencia, y por último decidir si existe un blanqueador estable y causal para $y[n]$.

###### **Resolución**
**a)** De la figura, $h[n]$ es no nulo solo en $n=-1,0,1$: $h[-1]=a$, $h[0]=b$, $h[1]=c$.

*Media de $y$.* Con $y[n]=\sum_kh[k]x[n-k]$ y $x$ i.i.d. de media $\mu_x=1$: $\mu_y=\mu_x\sum_kh[k]=\mu_x(a+b+c)$. Con $\mu_y=0$ y $\mu_x=1\neq0$:
$$a+b+c=0$$

*$S_{yx}$ real.* Igual que en el capítulo 12 del apunte, $C_{yx}[m]=\sigma_x^2\,h[m]$ (la salida de un filtro sobre blanco tiene covarianza cruzada proporcional a $h$), así que $S_{yx}(e^{j\Omega})=\sigma_x^2H(e^{j\Omega})$, y pedir $S_{yx}$ real equivale a pedir $H(e^{j\Omega})$ real. Con
$$H(e^{j\Omega})=ae^{j\Omega}+b+ce^{-j\Omega}=b+(a+c)\cos\Omega+j(a-c)\sin\Omega$$
la parte imaginaria se anula para **todo** $\Omega$ solo si
$$a=c$$

*Varianza de $y$.* Con $\mu_y=0$: $\sigma_y^2=C_{yy}[0]=\sigma_x^2\sum_kh[k]^2=\sigma_x^2(a^2+b^2+c^2)$. Con $\sigma_x^2=\tfrac14$, $\sigma_y^2=\tfrac32$:
$$a^2+b^2+c^2=6$$

Con $a=c$ y $b=-2a$ (de $a+b+c=0$): $a^2+4a^2+a^2=6a^2=6\Rightarrow a^2=1\Rightarrow a=\pm1$.
$$\boxed{\ (a,b,c)=(1,-2,1)\quad\text{o, equivalentemente,}\quad(a,b,c)=(-1,2,-1)\ }$$
Los datos dados (media, varianza, $S_{yx}$ real) solo fijan $a=c$ y $a^2=1$: no alcanzan para fijar el signo global. Tomamos $(1,-2,1)$ para lo que sigue; con $(-1,2,-1)$ da exactamente lo mismo, porque de acá en más todo depende de $h[n]$ únicamente a través de $|H(e^{j\Omega})|^2$.

**b)** Con $a=1,b=-2,c=1$:
$$H(e^{j\Omega})=e^{j\Omega}-2+e^{-j\Omega}=2\cos\Omega-2=-4\sin^2(\Omega/2)$$
real (como se impuso), $\leq0$ siempre, con un cero doble en $\Omega=0$. Como $\mu_y=0$, no hay impulso en $\Omega=0$ y $S_{yy}=D_{yy}=\sigma_x^2|H|^2$:
$$\boxed{\ S_{yy}(e^{j\Omega})=\frac14(2\cos\Omega-2)^2=(\cos\Omega-1)^2\ }$$

![[sol11-ej16-psd-pasaaltos.svg]]
Vale $0$ en $\Omega=0$ y crece hasta $4$ en $\Omega=\pm\pi$:
$$\boxed{\ h[n]\ \text{es un filtro \textbf{pasa-altos}}\ }$$
(de hecho $h[n]=\delta[n+1]-2\delta[n]+\delta[n-1]$ es la segunda diferencia discreta —el "laplaciano" de una dimensión—, que anula la continua y realza los cambios rápidos).

**c)** Buscamos $g[n]$ causal y estable tal que $w=g*y$ sea blanco: eso es pedirle a $g$ que sea el **blanqueador** de $y$, es decir $1/F(z)$ con $F(z)$ el factor de fase mínima de $S_{yy}$.

Con $z=e^{j\Omega}$, $(1-z^{-1})(1-z)=2-z-z^{-1}=-2(\cos\Omega-1)$, así que $\cos\Omega-1=-\tfrac12(1-z^{-1})(1-z)$ y
$$S_{yy}(z)=(\cos\Omega-1)^2=\tfrac14(1-z^{-1})^2(1-z)^2$$
que ya queda factorizada como $F(z)F(z^{-1})$ con $F(z)=\tfrac12(1-z^{-1})^2$: es FIR, así que **siempre estable y causal**. Pero su cero está en $z=1$, **justo sobre** el círculo unidad (no estrictamente adentro). Entonces la inversa $1/F(z)=2/(1-z^{-1})^2$ tiene un **polo doble en $z=1$**, sobre el círculo unidad: no es absolutamente sumable, **no es estable**.

$$\boxed{\text{No es posible: no existe un blanqueador causal y estable para }y[n]}$$

En criollo: $h[n]=[1,-2,1]$ (la segunda diferencia) **mata exactamente** la componente continua de la entrada. $S_{yy}$ no es solo chica cerca de $\Omega=0$: es **idénticamente cero** ahí. Ningún filtro estable puede entregar ganancia infinita en un único punto para "reconstruir" algo que el filtro anterior borró sin dejar rastro.

> [!warning] Ojo
> Esto no contradice Paley-Wiener del capítulo 11 ("no podés blanquear lo que no existe" solo prohíbe que $S_{xx}$ se anule en **toda una banda**, no en un punto aislado). Acá el cero es un único punto, y de hecho el factor modelador $F(z)$ sí existe (es causal y estable). Lo que falla es más sutil: cuando el cero de $F$ cae **justo sobre** el círculo unidad en vez de estrictamente adentro, $F$ deja de ser invertible de forma estable, aunque siga siendo un modelador perfectamente válido.

###### **Verificación**
sympy confirma que $\dfrac{1}{2\pi}\displaystyle\int_{-\pi}^{\pi}S_{yy}(e^{j\Omega})\,d\Omega=\tfrac32$ (coincide con $\sigma_y^2$ dado), y que $S_{yy}(0)=0$, $S_{yy}(\pi)=4$, consistente con el gráfico.

---

## Ejercicio 17 — Blanqueador único: cuando la ambigüedad del pasatodo desaparece

> [!quote] Enunciado
> 17. Considere un proceso aleatorio WSS $x[n]$ cuya PSD compleja es
> $$S_{xx}(z)=\frac{\left(1-\tfrac13 z\right)\left(1-\tfrac13 z^{-1}\right)}{\left(1-\tfrac12 z\right)\left(1-\tfrac12 z^{-1}\right)}$$
> Encuentre un filtro blanqueador $H_w(z)$ para el proceso $x[n]$, eligiéndolo estable y causal, y con inversa estable y causal. ¿Es su respuesta única salvo un factor de escala constante? Si lo es, explique por qué. Si no, construya un segundo filtro blanqueador.

###### **Idea**
Ya factorizamos una $S_{xx}(z)$ de esta misma forma en la Parte 2.3 de [[PROCESAMIENTO DE SEÑALES - Cap 11 en profundidad]] (con otros números): acá repetimos el método y, además, hay que decidir si el blanqueador es único —que es una pregunta más fina que la del filtro modelador de esa sección.

###### **Resolución**
**Ceros y polos de $S_{xx}(z)$.** $1-\tfrac13z=0\Rightarrow z=3$; $1-\tfrac13z^{-1}=0\Rightarrow z=\tfrac13$. $1-\tfrac12z=0\Rightarrow z=2$; $1-\tfrac12z^{-1}=0\Rightarrow z=\tfrac12$. Ceros en $\{\tfrac13,3\}$, polos en $\{\tfrac12,2\}$: pares recíprocos, como siempre que $R_{xx}$ es real y par.

**Factor de fase mínima (modelador).** Nos quedamos con lo que está adentro del círculo unidad:
$$F(z)=\frac{1-\tfrac13z^{-1}}{1-\tfrac12z^{-1}}$$
Polo en $\tfrac12$ (adentro: estable y causal ✓); cero en $\tfrac13$ (adentro: la inversa $1/F(z)=\dfrac{1-\tfrac12z^{-1}}{1-\tfrac13z^{-1}}$ tiene su polo en $\tfrac13$, adentro también: estable y causal ✓).

El blanqueador es la inversa de $F$:
$$\boxed{\ H_w(z)=\frac{1}{F(z)}=\frac{1-\tfrac12z^{-1}}{1-\tfrac13z^{-1}}\ ,\qquad\text{ROC: }|z|>\tfrac13\ }$$

**¿Es única salvo escala?** Acá la pregunta es más fina que en la Parte 2.3 del complemento, donde solo se pedía un factor **modelador** (una sola condición de estabilidad). Acá $H_w$ tiene que cumplir **dos** condiciones a la vez: ser estable y causal, **y** tener inversa estable y causal. Eso exige que tanto el polo de $H_w$ como su cero estén estrictamente adentro del círculo unidad — exactamente la definición fuerte de fase mínima, aplicada al propio $H_w$.

$|H_w(e^{j\Omega})|^2$ fija el par $\{$polo, cero$\}$ salvo la elección de cuál miembro de cada par recíproco usar. El polo de $H_w$ tiene que salir del par $\{\tfrac13,3\}$: el único que da $H_w$ causal-estable es $z=\tfrac13$ (el otro, $z=3$, daría un $H_w$ causal inestable). **No hay libertad ahí.** El cero de $H_w$ tiene que salir del par $\{\tfrac12,2\}$: el único que hace que $1/H_w$ sea causal-estable es $z=\tfrac12$ (si el cero quedara en $z=2$, la inversa tendría su polo ahí, afuera del círculo: inestable). **Tampoco hay libertad ahí.**

Un segundo blanqueador $G(z)=H_w(z)A(z)$ con $A$ un pasatodo no trivial —la fuente habitual de la ambigüedad, como en la Parte 2.3 del complemento— **siempre** mueve un polo o un cero de adentro hacia afuera: un pasatodo real de primer orden $A(z)=\dfrac{z^{-1}-p}{1-pz^{-1}}$ tiene su polo en $p$ y su cero en $1/p$, en lados **opuestos** del círculo unidad. Si $A$ agrega un polo nuevo adentro (en $p$, para no romper la estabilidad de $G$), regala también un cero nuevo **afuera** (en $1/p$), y entonces $1/G$ deja de ser estable. No hay forma de estirar ninguno de los dos pares sin romper alguna de las dos condiciones.

$$\boxed{\text{Sí, es única salvo un factor de escala real: acá no hay lugar para la ambigüedad del pasatodo.}}$$

###### **Verificación**
sympy confirma $|H_w(e^{j\Omega})|^2=1/S_{xx}(e^{j\Omega})$ exactamente para todo $\Omega$ (diferencia simbólica nula). Además simulé $2\times10^6$ muestras: generé $x[n]$ filtrando blanco unitario con $F(z)$, y después blanqueé con $H_w(z)$. La autocorrelación normalizada de $x$ decae geométricamente (lags $0$ a $4$: $1{,}000$ — $0{,}177$ — $0{,}089$ — $0{,}044$ — $0{,}021$, consistente con el polo en $\tfrac12$), y la de la salida blanqueada da esencialmente $\delta[m]$ (lags $0$ a $4$: $1{,}000$; $-0{,}001$; $0{,}000$; $0{,}000$; $-0{,}001$), con varianza $\approx1$.

> [!info] Conexión
> Compará con la Parte 2.3 de [[PROCESAMIENTO DE SEÑALES - Cap 11 en profundidad]]: ahí, para una $S_{xx}(z)$ de la misma forma (con otros números), se construye explícitamente un segundo factor $G(z)$ válido multiplicando por un pasatodo —pero ese $G$ sirve como filtro **modelador** (solo necesita ser estable y causal), no como blanqueador, porque el pasatodo le manda un cero afuera y su inversa deja de ser estable—. Es exactamente la distinción que hace única la respuesta acá: pedir la inversa estable y causal, y no solo el modelador, es lo que mata la ambigüedad del pasatodo.
