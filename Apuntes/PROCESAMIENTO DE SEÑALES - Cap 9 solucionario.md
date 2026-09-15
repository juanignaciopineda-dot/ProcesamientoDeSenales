Solucionario de los Ejercicios Propuestos del capítulo 9 de [[PROCESAMIENTO DE SEÑALES]]. La teoría con demostraciones está en [[PROCESAMIENTO DE SEÑALES - Cap 9 en profundidad]].

# Pruebas De Hipótesis — Solucionario

Estos ocho ejercicios recorren lo esencial del capítulo: regla MAP (con dos y con tres hipótesis, discretas y continuas), test de razón de verosimilitud, diseño y lectura de curvas ROC, y el caso límite en que el prior es tan desparejo que conviene ignorar la medición. Cada resolución cierra con una verificación numérica (Monte Carlo o cálculo directo con `sympy`/`scipy`) hecha en un script aparte, no incluido acá.

###### **Índice**
| Ej. | Qué se practica | Problema del libro |
|---|---|---|
| 1 | MAP con dos preguntas condicionalmente independientes | P9.6 |
| 2 | Umbral MAP con gaussianas de igual varianza | P9.3 |
| 3 | MAP con densidades de Cauchy; regiones de $P_{FA}$ y $P_M$ | P9.1 |
| 4 | Regla de umbral sobre $\|r\|$ vs. la regla óptima (uniforme vs. Laplace) | P9.8 |
| 5 | Definiciones básicas, MAP y ROC con ruido uniforme | P9.2 |
| 6 | Tres horarios de trenes: MAP con tres hipótesis uniformes | P9.5 |
| 7 | Punto de operación óptimo sobre una ROC dada | P9.4 |
| 8 | Canal binario: receptor óptimo y canal equivalente | P9.7 |

---

## Ejercicio 1 — MAP con dos preguntas condicionalmente independientes

> [!quote] Enunciado
> 1. Una estudiante está rindiendo un examen y es igualmente probable que no haya estudiado (hipótesis $H_0$) o que sí haya estudiado (hipótesis $H_1$).
>
> El examen consta de dos problemas, $a$ y $b$. Si la estudiante responde correctamente el problema $a$ (respectivamente $b$) diremos que ocurrió el evento $A$ (respectivamente $B$), y en caso contrario diremos que ocurrió el evento $\bar A$ (respectivamente $\bar B$). Asuma que el desempeño de la estudiante en el problema $a$ es independiente del desempeño en el problema $b$, tanto si no estudió como si estudió.
>
> Suponga que $P(A|H_1)=0.8$, $P(B|H_1)=0.6$, $P(A|H_0)=0.5$ y $P(B|H_0)=0.2$.
>
> a) Para cada resultado posible del examen (cada combinación posible de $A$ o $\bar A$ con $B$ o $\bar B$), encuentre la decisión de mínima probabilidad de error.
> b) Para la regla de decisión obtenida en a), encuentre la probabilidad condicional de declarar que la estudiante no estudió ($\text{`}H_0\text{'}$), dado que en realidad sí estudió ($H_1$).

###### **Idea**
La medición acá no es un número sino un par de eventos discretos $(A/\bar A,\ B/\bar B)$. Como $A$ y $B$ son condicionalmente independientes dado $H$, la verosimilitud conjunta es el producto de las marginales. Con priors iguales ($p_0=p_1=0{,}5$), MAP se reduce a comparar directamente $P(\text{resultado}|H_1)$ contra $P(\text{resultado}|H_0)$.

###### **Resolución**
**a)** Por independencia condicional, $P(A\cap B\,|\,H_i)=P(A|H_i)\,P(B|H_i)$, y análogamente con los complementos. Como $p_0=p_1$, alcanza con comparar las verosimilitudes (el factor común $0{,}5$ se cancela):

| Resultado | $P(\cdot|H_1)$ | $P(\cdot|H_0)$ | Decisión MAP |
|---|---|---|---|
| $A,B$ | $0{,}8\cdot0{,}6=0{,}48$ | $0{,}5\cdot0{,}2=0{,}10$ | $\text{`}H_1\text{'}$ |
| $A,\bar B$ | $0{,}8\cdot0{,}4=0{,}32$ | $0{,}5\cdot0{,}8=0{,}40$ | $\text{`}H_0\text{'}$ |
| $\bar A,B$ | $0{,}2\cdot0{,}6=0{,}12$ | $0{,}5\cdot0{,}2=0{,}10$ | $\text{`}H_1\text{'}$ |
| $\bar A,\bar B$ | $0{,}2\cdot0{,}4=0{,}08$ | $0{,}5\cdot0{,}8=0{,}40$ | $\text{`}H_0\text{'}$ |

$$\boxed{\ \text{Decide `}H_1\text{' si ocurrió }B\text{ (con o sin }A\text{); decide `}H_0\text{' si ocurrió }\bar B\ }$$

> [!info] Por qué la regla ignora a $A$
> Fijate que la decisión termina dependiendo **solo de si respondió bien $b$**, sin importar qué pasó con $a$: en las dos columnas, $B$ multiplica por $0{,}6$ contra $0{,}2$ (una razón $3:1$ a favor de $H_1$), mientras que $A$ multiplica por $0{,}8$ contra $0{,}5$ (razón $1{,}6:1$, más floja). $A$ nunca alcanza a dar vuelta lo que ya decidió $B$: incluso en el caso más favorable a $H_0$ ($\bar A$, que empuja $1{,}6\times$ más fuerte a favor de $H_0$), el $3\times$ de $B$ sigue ganando. Es la misma lógica de "quién tiene más pendiente" que aparece en los test de razón de verosimilitud, pero con factores discretos en vez de una densidad continua.

**b)** Con la regla de a), se declara $\text{`}H_0\text{'}$ exactamente cuando ocurre $\bar B$ (sin importar $A$). Entonces:
$$P(\text{`}H_0\text{'}\,|\,H_1)=P(\bar B\,|\,H_1)=1-P(B|H_1)=1-0{,}6$$
$$\boxed{\ P(\text{`}H_0\text{'}\,|\,H_1)=0{,}4\ }$$

###### **Verificación**
Es una probabilidad, cae en $[0,1]$ ✓. *(Verificado numéricamente: simulando $4\times10^6$ exámenes con $A,B$ Bernoulli independientes según $H_1$ y aplicando la regla de a), la fracción que declara $\text{`}H_0\text{'}$ da $0{,}3997$, contra el $0{,}4$ exacto.)*

---

## Ejercicio 2 — Umbral MAP con gaussianas de igual varianza

> [!quote] Enunciado
> 2. Al elegir con mínima probabilidad de error entre la hipótesis $H_0$ de que una medición dada $x$ proviene de una distribución normal (Gaussiana) con media $0$ y varianza $4$, y la hipótesis $H_1$ de que esta medición proviene de una distribución normal con media $1$ y varianza $4$, sabemos que el test óptimo declara $H_1$ si $x$ supera cierto umbral $\gamma$. Determine $\gamma$ en cada uno de los siguientes casos: i) la probabilidad condicional de falsa alarma es $P_{FA}=0.5$; y ii) la probabilidad condicional de miss es $P_M=0.5$.

###### **Idea**
Con varianzas iguales el test MAP siempre da un único umbral sobre $x$ (es el caso "$\sigma_1=\sigma_0$" de la tabla que resume el signo de la cuadrática en [[PROCESAMIENTO DE SEÑALES - Cap 9 en profundidad]], Parte 2.1: ahí el término en $r^2$ se cancela y queda lineal). Acá no piden el umbral MAP con priors dados, sino el $\gamma$ que produce ciertos valores de $P_{FA}$ o $P_M$ — y ambos casos se resuelven por simetría de la Gaussiana, sin necesitar priors.

###### **Resolución**
$X|H_0\sim N(0,4)$ (o sea $\sigma=2$), $X|H_1\sim N(1,4)$. La regla es $x\underset{H_0}{\overset{H_1}{\gtrless}}\gamma$.

**i)** $$P_{FA}=P(X>\gamma\,|\,H_0)=Q\!\left(\frac{\gamma-0}{2}\right)=0{,}5$$
$Q(z)=0{,}5$ exactamente cuando $z=0$ (por simetría de la Gaussiana estándar alrededor de su media). Entonces $\gamma/2=0$:
$$\boxed{\ \gamma=0\ }$$
Tiene sentido: con $\gamma=0$, la mitad de la masa de $H_0$ (centrada en $0$) queda del lado $x>0$.

**ii)** $$P_M=P(X\leq\gamma\,|\,H_1)=1-Q\!\left(\frac{\gamma-1}{2}\right)=0{,}5\ \Longrightarrow\ Q\!\left(\frac{\gamma-1}{2}\right)=0{,}5$$
Otra vez por simetría, $(\gamma-1)/2=0$:
$$\boxed{\ \gamma=1\ }$$
Acá el umbral coincide exactamente con la media de $H_1$: la mitad de esa Gaussiana cae por debajo, dando el miss que se pide.

###### **Verificación**
Los dos resultados son intuitivos por simetría: $P_{FA}=0{,}5$ exige que el umbral parta la densidad de $H_0$ por la mitad, y como es simétrica respecto de su media, el umbral tiene que ser la media, $0$. Mismo argumento para $P_M=0{,}5$ con la media de $H_1$, que es $1$. *(Verificado con `scipy.stats.norm`: `norm.isf(0.5, loc=0, scale=2) = 0.0` y `norm.ppf(0.5, loc=1, scale=2) = 1.0`.)*

> [!warning] Ojo
> No confundir con la regla MAP "de verdad": si te dieran $p_0,p_1$, el umbral saldría de $\ln\Lambda(\gamma)=\ln(p_0/p_1)$ y en general **no** coincidiría con ninguna de estas dos medias. Acá el enunciado pide umbrales que logran valores *específicos* de $P_{FA}$ o $P_M$, no el óptimo bayesiano.

---

## Ejercicio 3 — MAP con densidades de Cauchy; regiones de $P_{FA}$ y $P_M$

> [!quote] Enunciado
> 3. Considere un problema de prueba de hipótesis binaria en el que se observa una variable aleatoria $X$ con las siguientes PDFs condicionales (ver figura):
> $$f_{X|H}(x|H_0) = \frac{1}{\pi(x^2+1)} \quad \text{y} \quad f_{X|H}(x|H_1) = \frac{2}{\pi(x^2+4)}.$$
> Suponga que las hipótesis $H_0$ y $H_1$ tienen probabilidades a priori $P(H_0)=0.4$ y $P(H_1)=0.6$, respectivamente. Se busca diseñar una regla de decisión para declarar $H_0$ o $H_1$, y analizar su desempeño.
>
> ![[ej-p9-3.png]]
>
> a) Encuentre la regla de decisión de mínima probabilidad de error, es decir, la que minimiza $P(H_0,\text{`}H_1\text{'}) + P(H_1,\text{`}H_0\text{'})$. Simplifique su respuesta tanto como sea posible.
> b) Indique, sombreando las regiones apropiadas de los gráficos de las densidades condicionales, cómo calcularía: i) la probabilidad condicional de falsa alarma, $P_{FA}$; y ii) la probabilidad condicional de miss, $P_M$.

###### **Idea**
Las dos densidades son Cauchy centradas en $0$: $f_0$ con parámetro de escala $b_0=1$, $f_1$ con $b_1=2$ (más ancha). Es exactamente la situación del ejercicio 3 de la Parte 5 del complemento (ahí con Laplace): cuando dos densidades simétricas respecto del mismo centro difieren solo en cuán "abiertas" están, la razón de verosimilitud depende de $x$ únicamente a través de $|x|$, y la de cola más pesada ($H_1$, acá) termina ganando lejos del origen.

###### **Resolución**
**a)** Regla MAP: decidir $\text{`}H_1\text{'}$ cuando $p_1 f_{X|H}(x|H_1) > p_0 f_{X|H}(x|H_0)$:
$$0{,}6\cdot\frac{2}{\pi(x^2+4)} \ >\ 0{,}4\cdot\frac{1}{\pi(x^2+1)}$$
Cancelando $\pi$ y reacomodando:
$$\frac{1{,}2}{x^2+4} > \frac{0{,}4}{x^2+1} \quad\Longrightarrow\quad 1{,}2\,(x^2+1) > 0{,}4\,(x^2+4) \quad\Longrightarrow\quad 0{,}8\,x^2 > 0{,}4$$
$$x^2 > \frac12 \quad\Longrightarrow\quad |x| > \frac{1}{\sqrt2}$$
$$\boxed{\ \text{Decide `}H_1\text{' si } |x|>\tfrac{1}{\sqrt2}\approx0{,}707;\ \ \text{decide `}H_0\text{' si } |x|\leq\tfrac{1}{\sqrt2}\ }$$
Tiene la forma "dos colas para $H_1$, centro para $H_0$" — el mismo patrón geométrico que en el ejemplo 2.1 del complemento (ahí con Gaussianas): la hipótesis de mayor dispersión ($H_1$, $b_1=2>b_0=1$) domina en los extremos porque su densidad cae más lento.

**b)** Con $a=1/\sqrt2$ como umbral, y llamando $D_1=\{|x|>a\}$, $D_0=\{|x|\leq a\}$:
- **$P_{FA}=P(\text{`}H_1\text{'}|H_0)$**: es el área bajo $f_{X|H}(x|H_0)$ en las **dos colas** $|x|>a$ (sombrear $x<-a$ y $x>a$ en el gráfico de $f_0$).
- **$P_M=P(\text{`}H_0\text{'}|H_1)$**: es el área bajo $f_{X|H}(x|H_1)$ en el **intervalo central** $-a\leq x\leq a$ (sombrear esa franja en el gráfico de $f_1$).

![[sol09-ej03-cauchy-regiones.svg]]
*Arriba, $f_0$ con las colas sombreadas ($P_{FA}$); abajo, $f_1$ con la franja central sombreada ($P_M$). El umbral $\pm1/\sqrt2$ es el mismo en los dos gráficos.*

Aunque el enunciado solo pide indicar las regiones, las áreas salen en forma cerrada usando que $\int \frac{b\,dx}{\pi(x^2+b^2)}=\frac{1}{\pi}\arctan(x/b)$:
$$P_{FA}=1-\frac{2}{\pi}\arctan(a)=1-\frac{2}{\pi}\arctan\!\left(\tfrac{1}{\sqrt2}\right)\approx0{,}608 \qquad P_M=\frac{2}{\pi}\arctan\!\left(\tfrac{a}{2}\right)=\frac{2}{\pi}\arctan\!\left(\tfrac{1}{2\sqrt2}\right)\approx0{,}216$$

###### **Verificación**
$P_{FA},P_M\in[0,1]$ ✓, y con priors $p_0=0{,}4,p_1=0{,}6$ la probabilidad de error resulta $P_e=p_0P_{FA}+p_1P_M\approx0{,}373$ — alta, esperable porque las dos Cauchy se solapan mucho (son anchas). *(Verificado numéricamente: Monte Carlo con $4\times10^6$ muestras de cada Cauchy da $P_{FA}=0{,}6082$ y $P_M=0{,}2164$, contra $0{,}6082$ y $0{,}2163$ exactos.)*

---

## Ejercicio 4 — Regla de umbral sobre $|r|$ vs. la regla óptima (uniforme vs. Laplace)

> [!quote] Enunciado
> 4. Se observa una variable aleatoria $R$ y se sabe que con probabilidad $p_0=\frac13$ su PDF es $f_0(r)$, y con probabilidad $p_1=(1-p_0)=\frac23$ su PDF es $f_1(r)$, especificadas como:
> $$f_0(r) = \begin{cases} \frac12, & -1\leq r\leq 1 \\ 0, & \text{en otro caso} \end{cases} \qquad f_1(r) = \frac12 e^{-|r|}.$$
>
> Observamos el valor de $R$ y, a partir de esto, decidimos si $f_0(r)$ es la PDF subyacente o si lo es $f_1(r)$: una caja de decisión toma $R$ y devuelve "decidir $f_0$" o "decidir $f_1$".
>
> Para los puntos a) y b) solamente, asuma que la caja de decisión está especificada de la siguiente manera:
> $$\text{si } |r|>\gamma \text{ decida } f_0(r), \qquad \text{si } |r|\leq \gamma \text{ decida } f_1(r).$$
>
> a) Para $\gamma=\frac12$, determine la probabilidad de error. Muestre claramente su razonamiento.
> b) Realice un gráfico cuidadosamente etiquetado de la ROC para esta caja de decisión, a medida que $\gamma$ varía de $0$ a $+\infty$. Muestre claramente su razonamiento.
> c) Determine el diseño de la caja de decisión que minimiza la probabilidad de error. Muestre claramente su razonamiento.
> d) Para esta parte del problema, $p_0$ y $p_1$ ya no están restringidos a los valores $\frac13,\frac23$, pero $p_0$ no puede ser ni $0$ ni $1$. ¿Para qué valor(es) de $p_0$, $0<p_0<1$, la regla de decisión que minimiza la probabilidad de error decide siempre la misma hipótesis, sin importar el valor de $R$ observado? Explique.

###### **Idea**
$f_0$ (uniforme en $[-1,1]$) tiene soporte acotado; $f_1$ (Laplace) tiene soporte infinito pero más masa cerca de $0$. La caja de decisión de a)-b) es una regla *ad hoc* razonable (decide $f_1$ cerca del origen, donde su densidad es más alta) pero no es necesariamente la óptima — eso se verifica recién en c), comparando con la regla MAP de verdad.

###### **Resolución**
**a)** Con $\gamma=\tfrac12$, hay dos formas de equivocarse:
- $f_0$ verdadera pero $|R|\leq\gamma$ (se decide $f_1$): bajo $f_0$, $R\sim\text{Unif}(-1,1)$, así que $P(|R|\leq\tfrac12\,|\,f_0)=\tfrac12\cdot1=\tfrac12$ (densidad $\tfrac12$ por longitud $1$).
- $f_1$ verdadera pero $|R|>\gamma$ (se decide $f_0$): bajo $f_1$ (Laplace, escala $1$), $P(|R|>\gamma\,|\,f_1)=e^{-\gamma}=e^{-1/2}$.

$$P_e = p_0\,P(|R|\leq\gamma|f_0) + p_1\,P(|R|>\gamma|f_1) = \frac13\cdot\frac12 + \frac23\cdot e^{-1/2}$$
$$\boxed{\ P_e = \frac16+\frac23 e^{-1/2}\approx0{,}571\ }$$

**b)** Para $\gamma$ general, definiendo "decidir $f_1$" como el análogo de $\text{`}H_1\text{'}$:
$$P_D(\gamma)=P(|R|\leq\gamma\,|\,f_1)=1-e^{-\gamma}\qquad(\text{para todo }\gamma\geq0,\text{ sin techo, porque }f_1\text{ tiene soporte infinito})$$
$$P_{FA}(\gamma)=P(|R|\leq\gamma\,|\,f_0)=\min(\gamma,1)\qquad(\text{se satura en }1\text{ apenas }\gamma\geq1,\text{ porque }f_0\text{ vive solo en }[-1,1])$$
Entonces, mientras $\gamma$ va de $0$ a $1$, el punto $(P_{FA},P_D)=(\gamma,\,1-e^{-\gamma})$ recorre una curva cóncava desde $(0,0)$ hasta $(1,\,1-e^{-1})\approx(1,\,0{,}632)$; a partir de ahí, para $\gamma>1$, $P_{FA}$ queda clavado en $1$ mientras $P_D$ sigue subiendo (asintóticamente) hacia $1$ a medida que $\gamma\to\infty$.

![[sol09-ej04-roc.svg]]
*La ROC no es una curva "de punta a punta": tiene el tramo curvo hasta $\gamma=1$ y después un tramo vertical pegado a $P_{FA}=1$. Ese quiebre en $\gamma=1$ es exactamente donde $f_0$ se queda sin soporte.*

**c)** La regla óptima (MAP) no tiene por qué coincidir con la forma "$|r|\gtrless\gamma$" que impusieron a)-b); hay que derivarla desde cero. Se decide $\text{`}f_1\text{'}$ cuando $p_1f_1(r)>p_0f_0(r)$:

- *Para $|r|\leq1$* (donde $f_0\neq0$): $\ \tfrac23\cdot\tfrac12e^{-|r|} > \tfrac13\cdot\tfrac12 \ \Longleftrightarrow\ 2e^{-|r|}>1 \ \Longleftrightarrow\ |r|<\ln2\approx0{,}693$.
- *Para $|r|>1$* (donde $f_0=0$): $p_1f_1(r)>0=p_0f_0(r)$ siempre que $f_1(r)>0$, que es siempre. **Se decide $f_1$ automáticamente**, sin importar qué tan lejos esté $r$: fuera de $[-1,1]$, $f_0$ es imposible, así que cualquier observación ahí delata a $f_1$ con certeza.

$$\boxed{\ \text{Decide `}f_1\text{' si } |r|<\ln2 \ \text{ o } \ |r|>1;\quad\text{decide `}f_0\text{' si } \ln2\leq|r|\leq1\ }$$

Es la topología opuesta a la de a)-b): ahí $f_0$ vivía en las colas y $f_1$ en el centro; acá $f_0$ solo puede ganar en una **franja intermedia acotada** $[\ln2,\,1]$, porque es la única región donde compite con algo de chance y además tiene soporte.

**d)** Repitiendo la cuenta de c) con $p_0$ genérico (y $p_1=1-p_0$): para $|r|\leq1$, se decide $f_1$ cuando
$$e^{-|r|} > \frac{p_0}{1-p_0}$$
El lado izquierdo vale como máximo $1$ (en $r=0$) y como mínimo $e^{-1}$ (en $|r|=1$). Si $p_0/(1-p_0) < e^{-1}$, la desigualdad se cumple para **todo** $|r|\leq1$, y para $|r|>1$ ya sabíamos que siempre se decide $f_1$ (porque ahí $f_0=0$). Es decir: si
$$\frac{p_0}{1-p_0} < e^{-1} \quad\Longleftrightarrow\quad p_0 < \frac{1}{1+e}$$
la regla óptima decide $\text{`}f_1\text{'}$ **para todo valor de $R$**, sin necesitar mirar la medición.
$$\boxed{\ 0<p_0<\dfrac{1}{1+e}\approx0{,}269 \ \Longrightarrow\ \text{siempre se decide } f_1\ }$$
No existe un umbral análogo del lado de $f_0$: por más grande que sea $p_0$ (mientras $p_0<1$), fuera de $[-1,1]$ siempre gana $f_1$ (ahí $f_0=0$ estrictamente), así que jamás se puede "decidir siempre $f_0$".

###### **Verificación**
$P_e$ de a) ($\approx0{,}571$) es mayor que el $P_e$ de la regla óptima de c) — tiene que serlo, porque la regla de c) es la que minimiza $P_e$ por construcción. *(Verificado numéricamente: Monte Carlo con $4\times10^6$ muestras da $P_e=0{,}5711$ para la regla de a) y $P_e=0{,}3191$ para la regla óptima de c), con $P_{FA}=0{,}693$ y $P_M=0{,}132$ — coherente con que $\ln2\approx0{,}693$. Y $1/(1+e)=0{,}26894$, valor que separa "siempre $f_1$" de "regla con franja intermedia" en la simulación de d).)*

---

## Ejercicio 5 — Definiciones básicas, MAP y ROC con ruido uniforme

> [!quote] Enunciado
> 5. Considere el siguiente problema de prueba de hipótesis. Bajo las dos hipótesis $H_0$ y $H_1$, la observación $Y$ es
> $$H_0: Y=s_0+N, \qquad H_1: Y=s_1+N.$$
> Acá $s_0$ y $s_1$ son constantes conocidas, y $N$ es una variable aleatoria con la PDF $f_N(\alpha)$ mostrada en la figura.
>
> ![[ej-p9-5.png]]
>
> Como recordatorio, a continuación las definiciones asociadas a la regla de decisión:
> i) $P_0$ y $P_1$ son las probabilidades a priori de $H_0$ y $H_1$ respectivamente;
> ii) $P_{FA}$ es $P(\text{`}H_1\text{'}|H_0)$;
> iii) $P_M$ es $P(\text{`}H_0\text{'}|H_1)$;
> iv) $P_D$ es $P(\text{`}H_1\text{'}|H_1)$; y
> v) $P(\text{error}) = P(H_0,\text{`}H_1\text{'}) + P(H_1,\text{`}H_0\text{'})$, es decir, la probabilidad de que la hipótesis declarada sea distinta de la verdadera.
>
> a) ¿$P_{FA}$ y $P_D$ deben sumar $1$ para toda regla de decisión? Justifique brevemente su respuesta.
> b) Suponga $P_0=\frac14$ y que para una regla de decisión particular se tiene $P_{FA}=\frac14$ y $P_D=\frac34$. Determine la probabilidad $P(\text{`}H_1\text{'})$ de que el detector decida $H_1$.
> c) Asuma los siguientes valores: $P_0=\frac14$, $s_0=0$, $s_1=1$. Determine el (los) rango(s) de valores de la observación $y$ para los cuales decidiría $\text{`}H_1\text{'}$ de manera que se minimice la probabilidad de error.
> d) Asuma los siguientes valores: $s_0=-\frac12$, $s_1=\frac12$. La regla de decisión es
> $$y \underset{H_0}{\overset{H_1}{\gtrless}} \gamma.$$
> Dibuje la ROC representando $P_D$ en función de $P_{FA}$ a medida que $\gamma$ varía de $-\infty$ a $+\infty$.

La figura muestra $f_N(\alpha)=\tfrac12$ para $-1\leq\alpha\leq1$ (y $0$ fuera de ese intervalo): el mismo ruido uniforme que ya apareció como $f_0(r)$ en el ejercicio 4.

###### **Idea**
a) es conceptual: $P_D=1-P_M$, así que $P_{FA}+P_D=1$ equivale a $P_{FA}=P_M$, que no tiene por qué darse. c) es MAP directo con $N$ uniforme desplazado por $s_0$ o $s_1$ — conviene pensar en soportes que se solapan parcialmente. d) es otra ROC con soportes uniformes desplazados, análoga en espíritu a la del ejercicio 4 pero acá **ambas** densidades están acotadas (ninguna tiene cola infinita), lo que da una ROC totalmente poligonal.

###### **Resolución**
**a)** No. Por definición $P_D=1-P_M$, así que $P_{FA}+P_D=1 \Leftrightarrow P_{FA}=P_M$. Eso solo pasa en reglas particulares (p. ej. el punto de la ROC donde se cruza con la antidiagonal), no en general.
$$\boxed{\ \text{No: basta un contraejemplo. La regla trivial "siempre declarar }H_0\text{" tiene }P_{FA}=P_D=0,\text{ que suman }0\neq1\ }$$

**b)** Condicionando en la hipótesis verdadera (regla de probabilidad total):
$$P(\text{`}H_1\text{'}) = P(H_0)\,P(\text{`}H_1\text{'}|H_0) + P(H_1)\,P(\text{`}H_1\text{'}|H_1) = P_0\,P_{FA}+P_1\,P_D$$
Con $P_0=\tfrac14$, $P_1=\tfrac34$, $P_{FA}=\tfrac14$, $P_D=\tfrac34$:
$$P(\text{`}H_1\text{'})=\frac14\cdot\frac14+\frac34\cdot\frac34=\frac{1}{16}+\frac{9}{16}$$
$$\boxed{\ P(\text{`}H_1\text{'})=\frac{10}{16}=0{,}625\ }$$

**c)** Con $s_0=0$: $Y|H_0=N\sim\text{Unif}(-1,1)$, densidad $\tfrac12$ en $[-1,1]$. Con $s_1=1$: $Y|H_1=1+N\sim\text{Unif}(0,2)$, densidad $\tfrac12$ en $[0,2]$. Los dos soportes se solapan en $[0,1]$.
Comparando $p_1f_{Y|H}(y|H_1)$ contra $p_0f_{Y|H}(y|H_0)$ con $p_0=\tfrac14,\ p_1=\tfrac34$:
- $y\in[-1,0)$: solo $f_0\neq0$ ($f_0=\tfrac12$, $f_1=0$) → decide $\text{`}H_0\text{'}$.
- $y\in[0,1]$: ambas densidades valen $\tfrac12$. Comparando $p_1\cdot\tfrac12=\tfrac38$ contra $p_0\cdot\tfrac12=\tfrac18$: gana $H_1$ → decide $\text{`}H_1\text{'}$.
- $y\in(1,2]$: solo $f_1\neq0$ ($f_1=\tfrac12$, $f_0=0$) → decide $\text{`}H_1\text{'}$.

$$\boxed{\ \text{Decide `}H_1\text{' para } 0\leq y\leq2 \ \ (\text{y `}H_0\text{' para } -1\leq y<0)\ }$$
Igual que en el ejercicio 4c, apenas la observación cae donde una de las dos densidades es idénticamente cero, la decisión es automática: acá $y<0$ delata a $H_0$ sin ambigüedad, y $y>1$ delata a $H_1$.

**d)** Con $s_0=-\tfrac12$: $Y|H_0\sim\text{Unif}(-1{,}5,\ 0{,}5)$. Con $s_1=\tfrac12$: $Y|H_1\sim\text{Unif}(-0{,}5,\ 1{,}5)$. Ambos intervalos tienen longitud $2$ y se solapan en $[-0{,}5,\,0{,}5]$.
Para la regla $y\gtrless\gamma$:
$$P_{FA}(\gamma)=P(Y>\gamma|H_0)=\text{clip}\!\left(\frac{0{,}5-\gamma}{2},\,0,\,1\right) \qquad P_D(\gamma)=P(Y>\gamma|H_1)=\text{clip}\!\left(\frac{1{,}5-\gamma}{2},\,0,\,1\right)$$
Analizando por tramos de $\gamma$:
- $\gamma\leq-1{,}5$: $P_{FA}=P_D=1$ (siempre se decide $H_1$).
- $-1{,}5\leq\gamma\leq-0{,}5$: $P_D=1$ todavía (porque $\gamma\leq-0{,}5$ es todo el soporte de $H_1$), pero $P_{FA}$ baja linealmente de $1$ a $0{,}5$.
- $-0{,}5\leq\gamma\leq0{,}5$: ahora **ambas** bajan juntas y en paralelo, porque $\gamma$ recorre la zona de solapamiento: $P_D=P_{FA}+0{,}5$, de $(0{,}5,\,1)$ a $(0,\,0{,}5)$.
- $0{,}5\leq\gamma\leq1{,}5$: $P_{FA}=0$ ya (todo el soporte de $H_0$ quedó por debajo de $\gamma$), y $P_D$ baja de $0{,}5$ a $0$.
- $\gamma\geq1{,}5$: $P_{FA}=P_D=0$.

$$\boxed{\ \text{ROC poligonal: } (1,1)\ \to\ (0{,}5,\,1)\ \to\ (0,\,0{,}5)\ \to\ (0,0),\ \text{con el tramo del medio sobre la recta } P_D=P_{FA}+0{,}5\ }$$

![[sol09-ej05-roc.svg]]
*Tramo horizontal arriba (soporte de $H_1$ ya cubierto del todo), tramo diagonal a $45°$ mientras $\gamma$ cruza la zona de solapamiento, tramo vertical abajo (soporte de $H_0$ ya vacío). Es el análogo poligonal — con las dos colas acotadas — de la ROC "curva + vertical" del ejercicio 4b, donde solo una de las dos densidades tenía soporte infinito.*

###### **Verificación**
En b), $P(\text{`}H_1\text{'})=0{,}625\in[0,1]$ ✓. En d), los tres puntos de quiebre son exactamente los bordes de los soportes desplazados ($-1{,}5,\,-0{,}5,\,0{,}5,\,1{,}5$), y la ROC queda **por encima** de la diagonal en todo punto salvo los extremos — consistente con que el test es informativo. *(Verificado numéricamente evaluando $P_{FA}(\gamma)$ y $P_D(\gamma)$ en una grilla fina de $\gamma\in[-2,2]$ y confirmando que coinciden con las fórmulas por tramos.)*

---

## Ejercicio 6 — Tres horarios de trenes: MAP con tres hipótesis uniformes

> [!quote] Enunciado
> 6. Cualquier día en particular, los trenes subterráneos que llegan a una estación arriban según uno de tres horarios igualmente probables: $H_1$, $H_2$ y $H_3$. Cuando el horario $H_i$ está en efecto ($i=1,2,3$), el tiempo entre arribos de primer orden $Y$, es decir, el tiempo entre un par de arribos consecutivos seleccionado al azar, está distribuido de manera uniforme en el intervalo $[0,i]$.
>
> Supongamos que realizamos una única observación, es decir, medimos el tiempo entre arribos de un par de trenes consecutivos seleccionado al azar; sea este tiempo medido $Y=y$. Queremos decidir qué horario está en efecto.
>
> a) Determine la regla de decisión de mínima probabilidad de error basada en esta observación.
> b) Encuentre la probabilidad de error para la regla de decisión obtenida en a).

###### **Idea**
Tres hipótesis, priors iguales: MAP se reduce a elegir, para cada $y$, el $i$ que maximiza $f_{Y|H}(y|H_i)=\tfrac1i\,\mathbb{1}\{0\leq y\leq i\}$. Como todas las densidades son "mesetas" de altura $1/i$ sobre $[0,i]$, y una meseta más angosta es más alta, conviene pensar la comparación como "la hipótesis con el intervalo más chico que todavía contiene a $y$ es la que gana".

###### **Resolución**
**a)** Para un $y$ dado, $f_{Y|H}(y|H_i)=1/i$ si $y\leq i$, y $0$ si $y>i$ (recordar $H_1\to[0,1]$, $H_2\to[0,2]$, $H_3\to[0,3]$). Como los priors son iguales, MAP elige el $i$ que maximiza $1/i$ **entre los que todavía tienen $y$ en su soporte** — es decir, el horario más "angosto" que alcanza a explicar la observación:

- Si $y\in[0,1]$: los tres horarios son compatibles ($1/1>1/2>1/3$) → gana $H_1$.
- Si $y\in(1,2]$: $H_1$ queda descartado ($f=0$); entre $H_2$ y $H_3$, $1/2>1/3$ → gana $H_2$.
- Si $y\in(2,3]$: solo $H_3$ es compatible → gana $H_3$.
- $y>3$ es un evento de probabilidad nula bajo cualquier hipótesis (no puede observarse).

$$\boxed{\ \text{Decide } H_1 \text{ si } 0\leq y\leq1;\quad H_2 \text{ si } 1<y\leq2;\quad H_3 \text{ si } 2<y\leq3\ }$$

> [!info] Conexión
> Es la misma lógica de "el más angosto gana en su propio territorio, pero pierde toda chance fuera de él" que aparece en el ejercicio 4c de esta guía: acá con tres uniformes anidadas en vez de dos.

**b)** El error, promediando sobre las tres hipótesis (equiprobables):
$$P_e=\frac13\Big[P(\text{error}|H_1)+P(\text{error}|H_2)+P(\text{error}|H_3)\Big]$$

- **Bajo $H_1$** ($Y\sim\text{Unif}[0,1]$): la regla siempre acierta en $[0,1]$, así que $P(\text{correcto}|H_1)=1$ y $P(\text{error}|H_1)=0$.
- **Bajo $H_2$** ($Y\sim\text{Unif}[0,2]$): acierta si $Y\in(1,2]$, que tiene probabilidad $\tfrac{2-1}{2}=\tfrac12$. Entonces $P(\text{error}|H_2)=1-\tfrac12=\tfrac12$.
- **Bajo $H_3$** ($Y\sim\text{Unif}[0,3]$): acierta si $Y\in(2,3]$, que tiene probabilidad $\tfrac{3-2}{3}=\tfrac13$. Entonces $P(\text{error}|H_3)=1-\tfrac13=\tfrac23$.

$$P_e=\frac13\left[0+\frac12+\frac23\right]=\frac13\cdot\frac{7}{6}$$
$$\boxed{\ P_e=\frac{7}{18}\approx0{,}389\ }$$

###### **Verificación**
$P_e\in[0,1]$ ✓, y crece con $i$ (a $H_3$ le va peor: su intervalo es el más ancho, así que "pierde" contra $H_1$ y $H_2$ en toda la zona donde estos son compatibles). *(Verificado numéricamente: Monte Carlo con $4\times10^6$ repeticiones —sorteando $H\in\{1,2,3\}$ equiprobable y $Y|H\sim\text{Unif}[0,H]$, aplicando la regla de a)— da $P_e=0{,}3886$, contra $7/18=0{,}3889$ exacto.)*

---

## Ejercicio 7 — Punto de operación óptimo sobre una ROC dada

> [!quote] Enunciado
> 7. Considere un problema de prueba de hipótesis binaria en el cual un receptor observa una variable aleatoria $R$. A partir de esta observación, el receptor decide cuál de dos hipótesis —denotadas $H_0$ y $H_1$— declarar como verdadera. El receptor puede ajustarse para operar en cualquier punto de la curva ROC, que para este receptor está dada por $P_D=\sqrt{P_{FA}}$, donde $P_D=P(\text{`}H_1\text{'}|H_1)$ y $P_{FA}=P(\text{`}H_1\text{'}|H_0)$. (Como recordatorio, la probabilidad de error $P_e$ del receptor se define como la probabilidad de declarar $\text{`}H_0\text{'}$ y que $H_1$ sea verdadera, o declarar $\text{`}H_1\text{'}$ y que $H_0$ sea verdadera.)
>
> a) Para esta parte, suponga que la probabilidad a priori de que la hipótesis $H_0$ sea verdadera es $P(H_0)=\frac34$ y que el receptor está ajustado para operar en el punto $P_D=\frac12$ de la curva ROC. Determine $P_{FA}$ y la probabilidad de error $P_e$ en ese punto de operación.
> b) Para la probabilidad a priori de $H_0$ dada en a) (es decir, $P(H_0)=\frac34$), existe un punto de operación en la curva ROC que minimiza la probabilidad de error total $P_e$. Determine $P_D$ si el receptor opera en ese punto.
> c) Ahora sea $P(H_0)=\frac14$. Determine $P_D$ y $P_{FA}$ en la curva ROC y el $P_e$ correspondiente de manera que $P_e$ sea mínimo.

###### **Idea**
No conocemos las densidades $f_{R|H}$, solo la forma de la ROC. Pero eso alcanza: [[PROCESAMIENTO DE SEÑALES - Cap 9 en profundidad]] (Parte 1.4) muestra que el punto de $P_e$ mínimo sobre una ROC es aquel donde la **pendiente** $dP_D/dP_{FA}$ iguala $\eta=p_0/p_1$ (el umbral MAP). Es la misma herramienta que usa el ejercicio 5 de la Parte 5 del complemento, con otra ROC.

###### **Resolución**
Sea $p_0=P(H_0)$, $p_1=1-p_0$. En cualquier punto de la ROC, $P_M=1-P_D$, así que
$$P_e(P_{FA})=p_0\,P_{FA}+p_1\,(1-P_D)=p_0\,P_{FA}+p_1\left(1-\sqrt{P_{FA}}\right)$$

**a)** $p_0=\tfrac34,\ p_1=\tfrac14$. En $P_D=\tfrac12$: como $P_D=\sqrt{P_{FA}}$,
$$P_{FA}=P_D^2=\left(\frac12\right)^2$$
$$\boxed{\ P_{FA}=\frac14\ }$$
$$P_e=p_0P_{FA}+p_1(1-P_D)=\frac34\cdot\frac14+\frac14\cdot\frac12=\frac{3}{16}+\frac{2}{16}$$
$$\boxed{\ P_e=\frac{5}{16}=0{,}3125\ }$$

**b)** Con el mismo $p_0=\tfrac34$ (así que $\eta=p_0/p_1=3$), el óptimo está donde la pendiente de la ROC vale $\eta$:
$$\frac{dP_D}{dP_{FA}}=\frac{d}{dP_{FA}}\sqrt{P_{FA}}=\frac{1}{2\sqrt{P_{FA}}}\ \overset{!}{=}\ \eta=3 \quad\Longrightarrow\quad \sqrt{P_{FA}}=\frac16 \quad\Longrightarrow\quad P_{FA}=\frac{1}{36}$$
$$\boxed{\ P_D=\sqrt{P_{FA}}=\frac16\approx0{,}167\ }$$
(y de paso, $P_e=\tfrac34\cdot\tfrac{1}{36}+\tfrac14\cdot\tfrac56=\tfrac{1}{48}+\tfrac{10}{48}=\tfrac{11}{48}\approx0{,}229$, mejor que el $0{,}3125$ de a) — como tiene que ser, porque a) no estaba en el punto óptimo).

**c)** Ahora $p_0=\tfrac14,\ p_1=\tfrac34$, así que $\eta=p_0/p_1=\tfrac13$. Igualando la pendiente:
$$\frac{1}{2\sqrt{P_{FA}}}=\frac13 \quad\Longrightarrow\quad \sqrt{P_{FA}}=\frac32 \quad\Longrightarrow\quad P_{FA}=\frac94$$
Pero $P_{FA}$ tiene que estar en $[0,1]$, y $9/4>1$: **no hay ningún punto de la ROC con esa pendiente**. La pendiente de $P_D=\sqrt{P_{FA}}$ es $\tfrac{1}{2\sqrt{P_{FA}}}$, que sobre $P_{FA}\in(0,1]$ toma valores en $[\tfrac12,\infty)$ — nunca baja de $\tfrac12$. Como el $\eta=\tfrac13$ buscado es menor que ese mínimo, la pendiente de la ROC es **siempre mayor** que $\eta$ en todo el dominio válido, lo que significa que $P_e(P_{FA})=p_0P_{FA}+p_1(1-\sqrt{P_{FA}})$ es **decreciente en todo $[0,1]$** (su derivada $p_0-p_1/(2\sqrt{P_{FA}})$ es negativa en todo el rango). El mínimo cae entonces en el borde del dominio, $P_{FA}=1$:
$$\boxed{\ P_{FA}=1,\quad P_D=\sqrt1=1,\quad P_e=p_0\cdot1+p_1\cdot0=p_0=\frac14=0{,}25\ }$$

> [!warning] Ojo
> Esto es un caso borde real, no un error de cuenta: cuando el prior de $H_0$ es chico ($p_0=\tfrac14$) y la ROC de este receptor en particular es "poco pronunciada" cerca de $P_{FA}=1$ (pendiente mínima $\tfrac12$, todavía relativamente alta), el mejor punto de operación termina siendo el trivial "declarar siempre $H_1$" ($P_{FA}=P_D=1$), con $P_e=p_0$. No siempre existe un punto interior donde la pendiente iguale a $\eta$: hay que chequear que $\eta$ caiga dentro del rango de pendientes que ofrece la ROC (acá, $[\tfrac12,\infty)$) antes de resolver la ecuación a ciegas.

###### **Verificación**
En b), $P_e\approx0{,}229$ es menor que el $P_e\approx0{,}3125$ de un punto no óptimo con el mismo prior (a) — consistente. En c), $P_e=0{,}25$ es el mínimo posible dado que ninguna regla puede hacer mejor que "ignorar todo y declarar la hipótesis de mayor prior" cuando la ROC no ofrece un punto con pendiente $\leq p_0/p_1$. *(Verificado numéricamente: barriendo $P_{FA}$ en una grilla fina de $(0,1]$ con `scipy.optimize.minimize_scalar`, el mínimo de b) da $P_{FA}=0{,}02778$, $P_e=0{,}22917$ — coincide con $1/36$ y $11/48$ — y el de c) converge a $P_{FA}=1$, $P_e=0{,}25$, confirmando que $P_e(P_{FA})$ es monótona decreciente en ese caso.)*

---

## Ejercicio 8 — Canal binario: receptor óptimo y canal equivalente

> [!quote] Enunciado
> 8. Considere un sistema de comunicación digital en el cual un flujo de bits (1s y 0s) independientes e idénticamente distribuidos (i.i.d.) $s[n]$ es transmitido a través de un canal defectuoso y sin memoria. $P_0$ denota la probabilidad de que se envíe un $0$ y $P_1$ denota la probabilidad de que se envíe un $1$, con $P_1=1-P_0$. La probabilidad de que un $1$ sea recibido como un $0$ es $\frac14$ y la probabilidad de que un $0$ sea recibido como un $1$ es $\frac14$. Luego procesamos la señal recibida $r[n]$ a través de un sistema sin memoria, posiblemente no lineal, $H$, para obtener una estimación $\hat s[n]$ de $s[n]$ a partir de $r[n]$. El sistema completo se representa en la figura.
>
> ![[ej-p9-8a.png]]
>
> a) Determine el sistema $H$ en términos de $P_0$ de modo que se minimice la probabilidad de error $P_e$, donde $P_e$ se define como la probabilidad de que $\hat s[n]$ sea distinto de $s[n]$ en un índice de tiempo dado $n$.
> b) En esta parte, asuma que el sistema $H$ ya fue diseñado y que, según el fabricante, tiene $P_M=\frac{1}{10}$ y una ROC especificada por
> $$\text{ROC}: \ \ P_D = (P_{FA})^{1/10}$$
> donde
> $$P_D = \text{Prob(declarar que se envió un 1} \mid \text{se envió un 1)};$$
> $$P_{FA} = \text{Prob(declarar que se envió un 1} \mid \text{se envió un 0)};$$
> $$P_M = \text{Prob(declarar que se envió un 0} \mid \text{se envió un 1)}.$$
> El sistema completo de la figura puede representarse entonces como un nuevo canal binario sin memoria, como se muestra a continuación. Determine las nuevas probabilidades $P_a$, $P_b$, $P_c$ y $P_d$.
>
> ![[ej-p9-8b.png]]

###### **Idea**
$a)$ es MAP binario con una observación discreta $r\in\{0,1\}$: para cada valor recibido, comparar $P_1\,P(r|s=1)$ contra $P_0\,P(r|s=0)$. Como el canal es simétrico (cruzan $1/4$ en los dos sentidos), la razón de verosimilitud toma solo dos valores (uno para $r=0$, otro para $r=1$), así que el sistema óptimo termina siendo uno de tres tipos según qué tan parejo sea $P_0$: identidad, o "ignorar todo y declarar siempre lo mismo". Para b), alcanza con la definición de $P_D,P_{FA},P_M$ y la ecuación de la ROC — no hace falta releer el canal físico de a).

###### **Resolución**
**a)** El canal cruza con probabilidad $\tfrac14$ en cada sentido: $P(r{=}0|s{=}1)=\tfrac14,\ P(r{=}1|s{=}1)=\tfrac34,\ P(r{=}1|s{=}0)=\tfrac14,\ P(r{=}0|s{=}0)=\tfrac34$. La regla MAP para cada valor recibido: declarar $\hat s=1$ si $P_1\,P(r|s{=}1) > P_0\,P(r|s{=}0)$.

- **Si $r=1$:** $P_1\cdot\tfrac34 \gtrless P_0\cdot\tfrac14 \ \Longleftrightarrow\ 3P_1\gtrless P_0 \ \Longleftrightarrow\ 3(1-P_0)\gtrless P_0 \ \Longleftrightarrow\ P_0\lessgtr\tfrac34$. Declara $\hat s=1$ si $P_0<\tfrac34$.
- **Si $r=0$:** $P_1\cdot\tfrac14 \gtrless P_0\cdot\tfrac34 \ \Longleftrightarrow\ P_1\gtrless3P_0 \ \Longleftrightarrow\ 1-P_0\gtrless3P_0 \ \Longleftrightarrow\ P_0\lessgtr\tfrac14$. Declara $\hat s=1$ si $P_0<\tfrac14$.

Combinando los dos casos según en qué franja cae $P_0$:

$$\boxed{\begin{aligned}
0<P_0<\tfrac14&:\quad H(r)=1 \ \ \text{para todo } r \ \ (\text{ignora la medición, declara siempre "1"})\\
\tfrac14\leq P_0\leq\tfrac34&:\quad H(r)=r \ \ (\text{pasa directo: declara lo que llegó})\\
\tfrac34<P_0<1&:\quad H(r)=0 \ \ \text{para todo } r \ \ (\text{ignora la medición, declara siempre "0"})
\end{aligned}}$$

> [!warning] Ojo
> El primer y tercer caso no son un error: si $P_0$ es muy chico (el $0$ es raro), incluso al recibir $r=0$ —que "normalmente" delataría un $0$— el prior tan bajo de que se haya enviado un $0$ pesa más que la evidencia del canal, y la jugada óptima es declarar "1" igual. Es exactamente el mismo fenómeno del ejercicio 4d (y del 7c): cuando el prior está muy desparejo, puede convenir ignorar la medición del todo. Acá el umbral que separa "ignorar" de "usar el canal" es $P_0=\tfrac14$ (y por simetría, $P_0=\tfrac34$ del otro lado).

**b)** $P_M=\tfrac{1}{10}$ da $P_D=1-P_M=\tfrac{9}{10}$. De la ROC, $P_D=(P_{FA})^{1/10}$, así que
$$P_{FA}=P_D^{\,10}=\left(\frac{9}{10}\right)^{10}$$
Con las definiciones de la figura ($P_a=P(\hat s{=}1|s{=}1)$, $P_b=P(\hat s{=}0|s{=}1)$, $P_c=P(\hat s{=}1|s{=}0)$, $P_d=P(\hat s{=}0|s{=}0)$):
$$\boxed{\ P_a=P_D=0{,}9\ ,\quad P_b=P_M=0{,}1\ ,\quad P_c=P_{FA}=(0{,}9)^{10}\approx0{,}3487\ ,\quad P_d=1-P_{FA}\approx0{,}6513\ }$$

###### **Verificación**
$P_a+P_b=1$ y $P_c+P_d=1$ ✓ (cada fila del canal equivalente es una PMF completa sobre $\{0,1\}$). Los umbrales de a) son simétricos alrededor de $P_0=\tfrac12$ ($\tfrac14$ y $\tfrac34$), como corresponde a un canal con cruces simétricos. *(Verificado numéricamente: $(0{,}9)^{10}=0{,}34867844$, y comparando $P_e$ de las tres políticas —identidad, "siempre 1", "siempre 0"— en una grilla de $P_0$, el cambio de política óptima ocurre justo en $P_0=0{,}25$ y $P_0=0{,}75$.)*

---
