# Episodio 3 — Un número y un umbral

Capítulo 9 (Pruebas de hipótesis), episodio 3 de 6. Duración objetivo: ~10 min.
Texto tomado de `../guion_base.md` (escenas 11 a 15), más un gancho y un cierre nuevos.

**Estado:** **Subido a YouTube en privado** el 19/10/2026: render final 1080p60 de 11:15, título buscable, descripción con el capítulo del libro y `capitulos.txt`, subtítulos, categoría Educación (https://youtu.be/1Gq0hjcaGpI). Residuos limpiados; la caché de voz está en `media/voiceovers/`: se rehace con `python rehacer.py Capitulo09_PruebasDeHipotesis E3`. **Falta**: publicarlo (lo hace el usuario).
Momentos escritos (paso 10) y `ritmo.py` con la voz real (Azure) **sin tramos
de más de 3,9 s** (paso 11). Voz total ≈ 10:55: el usuario decidió **no
recortar** el b2 de la escena 09. Escenas `s01`–`s16` escritas (paso 12), con
piezas en `comun/figuras_c9e3.py`; todas pasan `manim --dry_run` con 0 avisos
en los informes. Borrador 480p15 renderizado (11:17, **0 avisos**) y hojas de
contacto revisadas (paso 14). Después de revisarlas se corrigieron las escenas
01, 03, 04, 05, 08, 11, 13, 14 y 15, se re-renderizaron y se unió el episodio:
borrador de **11:18 con 0 avisos**. El usuario dio el visto bueno con un único
cambio: la escena 15 ya no remite al apunte (quien mira en YouTube no sabe que
existe). **Render final 1080p60 hecho** (11:14, 0 avisos). Falta subirlo a
YouTube y limpiar residuos (paso 17).

Texto nuevo (marcado con ⭐, ya aprobado):
- ⭐ Escena 01 (gancho): «El canal, el radar, el test médico. Parecen
  problemas distintos, con criterios distintos. Pero la mejor decisión, en
  todos, es la misma operación: calcular un número y compararlo con un umbral.»
- ⭐ Escena 02 (título): «Un número y un umbral».
- ⭐ Retoque en la escena 04 (bloque b1): el guion base decía «Lo mismo que con
  las curvas escaladas»; como esas curvas son del E1, pasa a «Lo mismo que daban
  las curvas escaladas del primer episodio».
- ⭐ Escena 16 (cierre): resumen corto (un número, la razón de verosimilitud,
  contra un umbral que sale de las probabilidades a priori o del presupuesto
  de falsas alarmas) y anuncia E4 por su título, «La curva de todos los
  umbrales».

Notas:
- El cierre del E2 ya anuncia este título («Lo veremos en el próximo episodio:
  un número y un umbral»). El gancho retoma esa pregunta.
- Reparto de las escenas del guion base: 11 → escenas 03 y 04; 12 → 05 y 06;
  13 → 07, 08 y 09; 14 → 10, 11 y 12; 15 → 13, 14 y 15. Solo se partieron
  bloques enteros: el texto del guion base no cambia (salvo el retoque de arriba).
- Largo: ~1.520 palabras del guion base más ~110 de gancho, título y cierre
  ≈ 1.630 palabras, unos 10:50 de voz a 150 palabras por minuto. Si al medir con
  `ritmo.py` pasa de ~10,5 min, el primer candidato a recortarse es el bloque b2
  de la escena 09 (la nota honesta sobre la cola izquierda, bloque 13·b6 del
  guion base).
- Ejemplos con los mismos números de todo el capítulo: las dos campanas
  (centros 0 y 2, desvío 1), la medición 1,3 (alturas 0,17 y 0,31, razón
  1,82), η = 2,33 con a priori 0,7 / 0,3, umbrales 1 y 1,42; Neyman-Pearson al
  5 %: umbral 1,645, detección 0,64; al 1 %: umbral 2,33 voltios, detección
  0,37. Varianzas distintas: umbrales −2,57 y 1,24, error 0,230 → 0,227.
  Mochila: detección 0,70 contra 0,15. Recomprobados con Python.
- Ojo, dos «2,33» distintos: η = 2,33 (escenas 04 y 06, sin unidades) y el
  umbral de 2,33 voltios para el 1 % (escena 12). En pantalla, el segundo
  siempre con «V» o «Umbral».

---

# Escena 01 — Gancho

**Capítulo YouTube:** Todas las decisiones, una sola operación

## Narración

<!-- b1 -->
El canal, el radar, el test médico. Parecen problemas distintos, con criterios
distintos. Pero la mejor decisión, en todos, es la misma operación: calcular
un número y compararlo con un umbral.

- «El canal» → `canal`: entra el ícono del canal de bits, con un «0» y un «1» a cada lado
- «el radar» → `radar`: a su derecha, el radar con su barrido
- «el test médico» → `test`: a la derecha, el tubo del test médico con un «+»
- «Parecen problemas distintos» → `distintos`: los tres íconos se separan, cada uno con un «?» encima
- «con criterios distintos» → `criterios`: debajo de cada uno, una etiqueta: «Error mínimo» · «Falsa alarma fija» · «¿Creerle al positivo?»
- «Pero la mejor decisión» → `mejor`: los tres íconos se acercan un poco al centro
- «la misma operación» → `misma`: las etiquetas se apagan y de cada ícono sale una flecha hacia una caja vacía al centro
- «calcular un número» → `numero`: dentro de la caja aparece «Λ(r)»
- «compararlo con un umbral» → `umbral`: la caja se completa: «Λ(r) ≷ η»

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** Un número y un umbral

## Narración

<!-- b1 -->
Un número y un umbral.

- «Un número» → `t1`: «Un número» entra con rebote
- «y un umbral.» → `t2`: «y un umbral» entra debajo, con la etiqueta «Capítulo 9 · Pruebas de hipótesis»

---

# Escena 03 — SepararLoMedido

**Capítulo YouTube:** La razón de verosimilitud
**Objetivo:** reordenar la regla del máximo a posteriori para dejar a un lado lo
medido (la razón de verosimilitud) y al otro lo que se sabía antes (el umbral eta).

## Narración

<!-- b1 -->
En la regla del máximo a posteriori, cada lado mezcla dos cosas: lo que has
medido y lo que sabías antes. Vamos a separarlas. Para decir uno, pe uno por la
campana del uno tiene que superar a pe cero por la campana del cero. Dividimos
los dos lados entre la campana del cero y entre pe uno. Son números positivos,
así que la desigualdad no se da la vuelta.

- «la regla del máximo a posteriori» → `regla`: entra la regla de la escena 04 del E1, «p₁ · f(r | H₁) ≷ p₀ · f(r | H₀)», con «MAP» pequeño arriba
- «cada lado mezcla dos cosas» → `lados`: cada lado de la desigualdad se encierra en un recuadro
- «lo que has medido» → `medido`: las dos campanas «f(r | H₁)» y «f(r | H₀)» se tiñen de cian
- «lo que sabías antes» → `antes`: «p₁» y «p₀» se tiñen de ámbar
- «Vamos a separarlas» → `separar`: los recuadros se apagan y las piezas se despegan un poco entre sí
- «Para decir uno» → `decir1`: sobre el «>» aparece «Decir 1»
- «tiene que superar» → `superar`: se resalta el signo «>»
- «Dividimos los dos lados» → `dividir`: «f(r | H₀)» baja al denominador de la izquierda
- «y entre pe uno» → `pe1`: «p₁» baja al denominador de la derecha
- «Son números positivos» → `positivos`: debajo, el recordatorio «Dividir entre algo positivo: la desigualdad no gira»
- «no se da la vuelta» → `nogira`: el «>» destella y sigue mirando hacia el mismo lado

<!-- b2 -->
A la izquierda queda la altura de la campana del uno dividida entre la altura
de la campana del cero, en el punto medido. Es la razón de verosimilitud, y se
escribe lambda mayúscula de erre. Dice cuántas veces más compatible es el dato
con hache uno que con hache cero.

- «A la izquierda queda» → `izq`: se resalta el cociente «f(r | H₁) / f(r | H₀)»
- «la altura de la campana del uno» → `alto1`: a la derecha, las dos campanas pequeñas con una regla vertical en r; se marca la altura de la del uno
- «la altura de la campana del cero» → `alto0`: se marca la altura de la del cero
- «en el punto medido» → `punto`: la regla vertical destella
- «la razón de verosimilitud» → `razon`: delante del cociente entra «Λ(r) =» con el rótulo «Razón de verosimilitud»
- «lambda mayúscula de erre» → `lambda`: «Λ(r)» se agranda un instante y vuelve
- «cuántas veces más compatible» → `veces`: debajo, «¿Cuántas veces más compatible?»
- «con hache uno que con hache cero» → `h1h0`: se completa: «… con H₁ que con H₀»

<!-- b3 -->
A la derecha queda un número fijo, que no depende de la medición: pe cero
entre pe uno. Es el umbral, y se llama eta. Todo lo que has medido está a un
lado. Todo lo que sabías antes, al otro.

- «A la derecha queda un número fijo» → `der`: se resalta «p₀ / p₁»
- «no depende de la medición» → `nodep`: la regla vertical de las campanas se desliza y «p₀ / p₁» no cambia
- «pe cero entre pe uno» → `p0p1`: «p₀ / p₁» destella
- «se llama eta» → `eta`: a su derecha, «= η»; queda «Λ(r) ≷ p₀ / p₁ = η»
- «Todo lo que has medido» → `llave_izq`: llave bajo la izquierda: «Lo que has medido»
- «Todo lo que sabías antes» → `llave_der`: llave bajo la derecha: «Lo que sabías antes»

---

# Escena 04 — LaEvidenciaCompensa

**Capítulo YouTube:** La evidencia contra la ventaja de partida
**Objetivo:** comprobar el test con la medición de 1,3 (razón 1,82 contra η = 1
y η = 2,33) y leerlo como una balanza.

## Narración

<!-- b1 -->
Comprobémoslo con uno coma tres voltios. La razón es cero coma treinta y uno
entre cero coma diecisiete: uno coma ochenta y dos. Con ceros y unos igual de
frecuentes, eta vale uno: se dice uno. Con setenta y treinta, eta vale dos coma
treinta y tres: uno coma ochenta y dos no llega, y se dice cero. Lo mismo que
daban las curvas escaladas del primer episodio.

- «uno coma tres voltios» → `medida`: corte; las dos campanas (centros 0 y 2) con la regla vertical en «1,3»
- «cero coma treinta y uno» → `a031`: sobre la campana del uno, en la regla, «0,31»
- «cero coma diecisiete» → `a017`: sobre la del cero, «0,17»
- «uno coma ochenta y dos» → `r182`: a la derecha, «Λ(1,3) = 0,31 / 0,17 = 1,82»
- «igual de frecuentes» → `iguales`: debajo, «p₀ = p₁ = 0,5»
- «eta vale uno» → `eta1`: «η = 1»
- «se dice uno» → `decir1`: «1,82 > 1 → Decir 1» en verde
- «Con setenta y treinta» → `p73`: debajo, «p₀ = 0,7 · p₁ = 0,3»
- «eta vale dos coma treinta y tres» → `eta233`: «η = 0,7 / 0,3 = 2,33»
- «no llega» → `nollega`: «1,82 < 2,33» en rojo
- «y se dice cero» → `decir0`: «→ Decir 0»
- «las curvas escaladas» → `escaladas`: a un lado, en pequeño, las curvas escaladas del E1 con su cruce en 1,42; la regla en 1,3 cae del lado del cero

<!-- b2 -->
Y ahora se lee muy bien. Si los ceros son dos coma tres veces más frecuentes,
para decir uno el dato tiene que ser al menos dos coma tres veces más
compatible con el uno. La evidencia tiene que compensar la ventaja de partida.
Esto es el test de razón de verosimilitud, y va a aparecer en todo lo que
queda de capítulo.

- «se lee muy bien» → `lee`: todo se apaga y entra una balanza vacía
- «dos coma tres veces más frecuentes» → `frec`: en el platillo derecho cae «η = 2,33», y el platillo baja
- «para decir uno» → `paradecir`: sobre la balanza, «Decir 1»
- «al menos dos coma tres veces más compatible» → `compat`: en el platillo izquierdo cae «Λ(r) ≥ 2,33»
- «con el uno» → `conuno`: el platillo izquierdo empieza a bajar
- «La evidencia» → `evidencia`: rótulo «Evidencia» bajo el platillo izquierdo
- «la ventaja de partida» → `ventaja`: rótulo «Ventaja de partida» bajo el derecho; la balanza oscila y se equilibra
- «el test de razón de verosimilitud» → `lrt`: la balanza se reduce y entra «Λ(r) ≷ η» con el rótulo «Test de razón de verosimilitud (LRT)»
- «en todo lo que queda de capítulo» → `resto`: la caja «Λ(r) ≷ η» se enmarca en ámbar

---

# Escena 05 — LaCuentaConCampanas

**Capítulo YouTube:** La cuenta con las campanas
**Objetivo:** calcular la razón de las dos campanas paso a paso hasta e^(2r − 2).

## Narración

<!-- b1 -->
Calculemos esa razón para nuestras campanas. La campana de Gauss tiene fórmula:
una constante, por e elevado a menos la distancia al centro al cuadrado,
dividida entre dos sigma cuadrado. Aquí sigma vale uno, así que el exponente es
menos la distancia al cuadrado, entre dos.

- «para nuestras campanas» → `campanas`: corte; las dos campanas de centros 0 y 2, desvío 1
- «tiene fórmula» → `formula`: arriba empieza la fórmula: «f(r) =»
- «una constante» → `cte`: «C ·»
- «por e elevado a» → `e`: «e^(   )» con el exponente vacío
- «la distancia al centro al cuadrado» → `dist`: en el exponente, «−(r − Centro)²»; en la campana, una flecha de r al centro
- «dos sigma cuadrado» → `sigma`: el exponente se completa: «/ 2σ²»
- «sigma vale uno» → `s1`: «σ = 1» al lado
- «el exponente» → `expo`: se resalta el exponente
- «entre dos» → `entre2`: «2σ²» se transforma en «2»; queda «C · e^(−(r − Centro)² / 2)»

<!-- b2 -->
Dividimos la campana del uno entre la del cero. Las constantes son iguales y se
cancelan. Y dividir potencias del mismo número es restar los exponentes. Queda
e elevado a: menos erre menos dos al cuadrado entre dos, más erre al cuadrado
entre dos.

- «Dividimos la campana del uno» → `div`: renglón nuevo: «Λ(r) = C · e^(−(r − 2)²/2)» arriba de la raya
- «entre la del cero» → `del0`: debajo de la raya, «C · e^(−r²/2)»
- «se cancelan» → `cancel`: las dos «C» se tachan
- «dividir potencias del mismo número» → `potencias`: se resaltan las dos «e», arriba y abajo de la raya
- «restar los exponentes» → `restar`: recordatorio al costado: «eᵃ / eᵇ = eᵃ⁻ᵇ»
- «Queda e elevado a» → `queda`: renglón nuevo: «Λ(r) = e^(  )»
- «menos erre menos dos al cuadrado entre dos» → `t1`: en el exponente, «−(r − 2)²/2»
- «más erre al cuadrado entre dos» → `t2`: se completa: «+ r²/2»

<!-- b3 -->
Desarrollamos el cuadrado. Erre menos dos, al cuadrado, es erre al cuadrado,
menos cuatro erre, más cuatro. Los dos erre al cuadrado se cancelan. Queda
cuatro erre menos cuatro, entre dos: dos erre menos dos. La razón de
verosimilitud es e elevado a dos erre menos dos.

- «Desarrollamos el cuadrado» → `desarrollo`: a la derecha, «(r − 2)² =»
- «Erre menos dos, al cuadrado» → `rm2`: en el exponente se resalta «(r − 2)²»
- «es erre al cuadrado» → `r2`: «r²»
- «menos cuatro erre» → `m4r`: «− 4r»
- «más cuatro» → `mas4`: «+ 4»
- «se cancelan» → `tacha`: en el exponente, los dos «r²» se tachan en rojo
- «cuatro erre menos cuatro, entre dos» → `frac`: renglón nuevo: «(4r − 4) / 2»
- «dos erre menos dos» → `res`: «= 2r − 2»
- «es e elevado a dos erre menos dos» → `marco`: abajo, «Λ(r) = e^(2r − 2)» enmarcado en ámbar

---

# Escena 06 — UnSoloUmbral

**Capítulo YouTube:** De la razón al umbral en voltios
**Objetivo:** ver que la razón crece con r, tomar logaritmos y obtener el umbral
1 + ln(η)/2; comprobar que da 1 y 1,42.

## Narración

<!-- b1 -->
Probemos valores. En cero voltios vale cero coma ciento treinta y cinco: el
dato apoya al cero. En un voltio vale uno: empate. En dos voltios, siete coma
cuatro: apoya al uno. La razón crece siempre con erre. Por eso compararla con
eta es lo mismo que comparar erre con un umbral.

- «Probemos valores» → `ejes`: la fórmula sube a una esquina; entran unos ejes «r» y «Λ(r)»
- «En cero voltios» → `r0`: un punto sobre r = 0
- «cero coma ciento treinta y cinco» → `v0`: el punto sube a «0,135»
- «apoya al cero» → `apoya0`: junto al punto, «Apoya al 0»
- «En un voltio vale uno» → `r1`: punto en (1, 1), con «1»
- «empate» → `empate`: «Empate»
- «siete coma cuatro» → `r2`: punto en (2; 7,39), con «7,39» y «Apoya al 1»
- «crece siempre con erre» → `curva`: se dibuja la curva entera por los tres puntos, siempre subiendo
- «compararla con eta» → `eta`: una línea horizontal «η» corta la curva
- «comparar erre con un umbral» → `umbral`: desde el corte baja una vertical al eje: «Umbral»

<!-- b2 -->
Para hallarlo se toma el logaritmo natural, que es la operación inversa de la
exponencial y conserva el orden. Queda dos erre menos dos, comparado con el
logaritmo de eta. Despejando: erre comparado con uno más la mitad del logaritmo
de eta.

- «el logaritmo natural» → `ln`: a la derecha, «ln»
- «la operación inversa de la exponencial» → `inversa`: «ln(eˣ) = x»
- «conserva el orden» → `orden`: debajo, «a < b → ln a < ln b»
- «Queda dos erre menos dos» → `q`: renglón: «2r − 2»
- «comparado con el logaritmo de eta» → `lneta`: se completa: «≷ ln η»
- «Despejando» → `desp`: «2r ≷ 2 + ln η»
- «uno más la mitad del logaritmo de eta» → `fin`: «r ≷ 1 + ln(η) / 2», enmarcado

<!-- b3 -->
Con eta igual a uno, el logaritmo es cero y el umbral es un voltio. Con eta
igual a dos coma treinta y tres, el logaritmo es cero coma ochenta y cinco, y
el umbral, uno coma cuarenta y dos. Los mismos cruces de antes. Una razón que
siempre crece da un solo umbral. Pero no siempre crece.

- «Con eta igual a uno» → `eta1`: debajo, «η = 1»
- «el logaritmo es cero» → `ln0`: «ln 1 = 0»
- «el umbral es un voltio» → `u1`: «Umbral = 1»; entran las dos campanas pequeñas con una marca en 1
- «dos coma treinta y tres» → `eta233`: «η = 2,33»
- «cero coma ochenta y cinco» → `ln085`: «ln 2,33 = 0,85»
- «uno coma cuarenta y dos» → `u142`: «1 + 0,85 / 2 = 1,42»; en las campanas, otra marca en 1,42
- «Los mismos cruces de antes» → `cruces`: un tilde verde junto a cada marca
- «Una razón que siempre crece» → `siempre`: las campanas se van y vuelve la curva creciente de Λ(r)
- «da un solo umbral» → `solo`: la línea η la corta una sola vez
- «Pero no siempre crece» → `nosiempre`: un «?» rojo sobre la curva

---

# Escena 07 — MasCercaNoBasta

**Capítulo YouTube:** ¿Cero o uno en menos cuatro voltios?
**Objetivo:** pregunta con pausa: con la campana del uno más ancha, una medición
de −4 V, más cerca del cero, se decide uno.

## Narración

<!-- b1 -->
Un cambio pequeño. Supón que el uno llega con más ruido que el cero: pasa en
la fibra óptica, donde la luz encendida es más ruidosa que la apagada. La
campana del cero tiene centro cero y desvío uno. La del uno, centro dos y
desvío dos. Ceros y unos, igual de frecuentes. Mides menos cuatro voltios.
¿Cero o uno? Piénsalo un momento.

- «Un cambio pequeño» → `cambio`: corte; unos ejes vacíos
- «con más ruido» → `ruido`: arriba, dos pulsos: el del 0 casi limpio y el del 1 con mucho ruido magenta
- «la fibra óptica» → `fibra`: entra un cable de fibra
- «la luz encendida» → `encendida`: en el cable, «Encendida», temblando mucho
- «más ruidosa que la apagada» → `apagada`: «Apagada», casi quieta
- «La campana del cero» → `campana0`: el cable se va y se dibuja la campana estrecha y alta en 0
- «centro cero y desvío uno» → `c0`: su rótulo: «Cero · Desvío 1»
- «centro dos y desvío dos» → `c1`: la campana ancha y baja en 2, «Uno · Desvío 2»
- «igual de frecuentes» → `iguales`: «p₀ = p₁ = 0,5» en la esquina
- «menos cuatro voltios» → `m4`: una marca en «r = −4»
- «¿Cero o uno?» → `pregunta`: «¿Cero o uno?» con dos opciones: «Cero, está más cerca» · «Uno»
- «Piénsalo un momento» → `pausa`: un reloj de arena pequeño se vacía

<!-- b2 -->
Menos cuatro está más cerca de cero que de dos. Pero la respuesta es uno. A
cuatro desvíos de su centro, la campana estrecha prácticamente ha desaparecido:
vale una diezmilésima. La ancha está a solo tres de sus desvíos, y vale
diecisiete veces más.

- «más cerca de cero que de dos» → `cerca`: desde −4, una flecha hasta 0 («4») y otra hasta 2 («6»)
- «la respuesta es uno» → `uno`: «Cero, está más cerca» se tacha; «Uno» se marca en verde
- «A cuatro desvíos» → `cuatro`: zoom a la cola izquierda; cuatro marcas de desvío estrecho de 0 a −4
- «prácticamente ha desaparecido» → `desap`: la campana estrecha, pegada al eje en −4, se resalta
- «una diezmilésima» → `v0001`: «0,0001»
- «a solo tres de sus desvíos» → `tres`: tres marcas de desvío ancho de 2 a −4
- «diecisiete veces más» → `x17`: sobre la ancha, «0,002», y entre las dos «17 veces más»

---

# Escena 08 — LaParabolaDecide

**Capítulo YouTube:** Una parábola con dos raíces
**Objetivo:** hacer la cuenta con el logaritmo de la razón: queda una parábola
que abre hacia arriba, con raíces −2,57 y 1,24.

## Narración

<!-- b1 -->
Hagamos la cuenta con el logaritmo de la razón. Ahora las constantes no se
cancelan, porque la campana ancha es la mitad de alta: aparece el logaritmo de
un medio. Y los erre al cuadrado tampoco: uno va dividido entre dos y el otro
entre ocho.

- «el logaritmo de la razón» → `lnl`: corte; arriba, «ln Λ(r) =»
- «las constantes no se cancelan» → `ctes`: las dos campanas pequeñas, con su constante cada una
- «la mitad de alta» → `mitad`: la ancha se compara con la estrecha: una flecha marca «½» de la altura
- «el logaritmo de un medio» → `lnmedio`: la fórmula sigue: «ln ½»
- «los erre al cuadrado tampoco» → `r2`: se completa: «− (r − 2)²/8 + r²/2»
- «uno va dividido entre dos» → `div2`: se resalta «r²/2»
- «el otro entre ocho» → `div8`: se resalta «/8»; al lado, «½ − ⅛ ≠ 0»

<!-- b2 -->
Multiplicando todo por ocho y ordenando, se dice uno cuando tres erre al
cuadrado, más cuatro erre, menos nueve coma cincuenta y cinco, es positivo. Eso
es una parábola que abre hacia arriba: es positiva fuera de sus dos raíces. La
fórmula de la ecuación de segundo grado las da: menos dos coma cincuenta y
siete, y uno coma veinticuatro.

- «Multiplicando todo por ocho» → `x8`: «× 8» a la derecha de la fórmula
- «se dice uno cuando» → `cuando`: renglón nuevo: «Decir 1 si»
- «tres erre al cuadrado» → `t3r2`: «3r²»
- «más cuatro erre» → `t4r`: «+ 4r»
- «menos nueve coma cincuenta y cinco» → `t955`: «− 9,55»
- «es positivo» → `pos`: «≥ 0»
- «una parábola que abre hacia arriba» → `parab`: debajo, se dibuja la parábola
- «positiva fuera de sus dos raíces» → `fuera`: los dos tramos de afuera, sobre el eje, en verde
- «La fórmula de la ecuación de segundo grado» → `bhaskara`: al costado, «r = (−b ± √(b² − 4ac)) / 2a»
- «menos dos coma cincuenta y siete» → `raiz1`: la raíz izquierda se marca: «−2,57»
- «uno coma veinticuatro» → `raiz2`: la derecha: «1,24»

---

# Escena 09 — DosUmbrales

**Capítulo YouTube:** Dos umbrales y tres regiones
**Objetivo:** leer las tres regiones (uno · cero · uno), la regla de la campana
ancha y la lección: el umbral se calcula, no se pone a ojo.

## Narración

<!-- b1 -->
La región del uno tiene dos pedazos: las dos colas. La del cero es el intervalo
del medio. La regla general: lejos del centro, por los dos lados, gana siempre
la campana más ancha. Solo cuando las dos anchuras son iguales desaparece el
término al cuadrado y queda un único umbral.

- «La región del uno» → `reg1`: corte; vuelven las dos campanas y el eje a la izquierda de −2,57 se pinta del color del uno
- «las dos colas» → `colas`: también a la derecha de 1,24
- «el intervalo del medio» → `medio`: el tramo central, del color del cero; rótulos «Uno · Cero · Uno»
- «lejos del centro» → `lejos`: dos flechas apuntan hacia afuera, una a cada lado
- «gana siempre la campana más ancha» → `ancha`: la campana ancha se resalta en las dos colas
- «las dos anchuras son iguales» → `iguales`: la campana ancha se estrecha hasta desvío 1
- «desaparece el término al cuadrado» → `sinr2`: arriba, «3r²» se tacha
- «queda un único umbral» → `unico`: las tres regiones se vuelven dos, con una sola marca en 1

<!-- b2 -->
Siendo honestos: aquí la cola izquierda casi nunca ocurre. El error baja de
cero coma doscientos treinta a cero coma doscientos veintisiete. Pero la
lección importa: el umbral no se pone a ojo. Se calcula la razón de
verosimilitud y se mira dónde supera a eta.

- «Siendo honestos» → `honestos`: vuelven la campana ancha y los dos umbrales
- «la cola izquierda casi nunca ocurre» → `cola`: zoom a la cola izquierda; el área bajo −2,57 es diminuta
- «El error baja» → `error`: arriba, «Error»
- «cero coma doscientos treinta» → `e230`: «Solo el derecho: 0,230»
- «cero coma doscientos veintisiete» → `e227`: debajo, «Dos umbrales: 0,227»
- «la lección importa» → `leccion`: los números se apagan; quedan la campana ancha y los dos umbrales
- «el umbral no se pone a ojo» → `ojo`: un ojo tachado
- «Se calcula la razón de verosimilitud» → `calc`: «Λ(r)»
- «dónde supera a eta» → `supera`: «Λ(r) > η», enmarcado

---

# Escena 10 — SinProbabilidadesAPriori

**Capítulo YouTube:** Cuando no hay probabilidades a priori
**Objetivo:** plantear el radar sin a priori y el criterio de Neyman-Pearson:
fijar la falsa alarma y maximizar la detección.

## Narración

<!-- b1 -->
Todo lo anterior necesitaba las probabilidades a priori. En el canal las
conocemos. Pero vuelve al radar: ¿qué probabilidad hay de que ahora mismo haya
un avión delante? Nadie lo sabe. Y sin probabilidades a priori, no hay eta.

- «las probabilidades a priori» → `apriori`: corte; «η = p₀ / p₁» con «p₀» y «p₁» resaltados
- «En el canal las conocemos» → `canal`: a la izquierda, el ícono del canal con «0,7 · 0,3»
- «vuelve al radar» → `radar`: a la derecha, el radar con su barrido
- «haya un avión delante» → `avion`: un avión pequeño frente al radar, con «p₁ = ?»
- «Nadie lo sabe» → `nadie`: un «?» grande
- «no hay eta» → `noeta`: en «η = p₀ / p₁» se borran «p₀» y «p₁»; queda «η = ?»

<!-- b2 -->
Neyman y Pearson propusieron cambiar la pregunta. En vez de minimizar el error
total, se fija cuántas falsas alarmas se toleran, por ejemplo un cinco por
ciento. Y con esa condición, se busca detectar lo máximo posible.

- «Neyman y Pearson» → `np`: rótulo «Neyman-Pearson»
- «cambiar la pregunta» → `pregunta`: «η = ?» se aparta a una esquina
- «minimizar el error total» → `error`: «Mínimo error total», que se tacha
- «cuántas falsas alarmas se toleran» → `fijar`: tarjeta «Fijar: Falsa alarma ≤ …»
- «un cinco por ciento» → `cinco`: la tarjeta se completa con «5 %»
- «con esa condición» → `condicion`: la tarjeta «Fijar» se enmarca
- «detectar lo máximo posible» → `max`: segunda tarjeta, «Conseguir: La mayor detección»

---

# Escena 11 — FijarLaFalsaAlarma

**Capítulo YouTube:** Un cinco por ciento de falsas alarmas
**Objetivo:** diseñar con las campanas para 5 %: umbral 1,645 (la función Q al
revés) y detección 0,64.

## Narración

<!-- b1 -->
Hagámoslo con las campanas: el ruido solo, con centro en cero, y el eco, con
centro en dos. Buscamos el umbral que deja un cinco por ciento de cola en la
campana del ruido. Es la función cu al revés: dada un área, qué punto la deja.
Para un cinco por ciento, ese punto es uno coma seiscientos cuarenta y cinco.

- «el ruido solo» → `ruido`: corte; la campana en 0 con «Ruido solo»
- «el eco» → `eco`: la campana en 2 con «Eco»
- «Buscamos el umbral» → `buscar`: una marca de umbral entra y se desliza por el eje
- «un cinco por ciento de cola» → `cola`: la cola derecha de la campana del ruido se sombrea en rojo, «5 %»
- «en la campana del ruido» → `delruido`: la campana del ruido se resalta
- «la función cu al revés» → `qinv`: arriba, «Q(x) = 0,05 → x = ?»
- «dada un área» → `area`: el área roja destella
- «qué punto la deja» → `punto`: la marca destella
- «Para un cinco por ciento» → `para5`: «0,05» se resalta y la marca se desliza hacia la derecha
- «uno coma seiscientos cuarenta y cinco» → `u1645`: «x = 1,645»; la marca queda fija en «1,645»

<!-- b2 -->
Ahora la detección: el área de la campana del eco a la derecha de ese umbral.
El umbral queda un poco a la izquierda de su centro, así que es algo más de la
mitad: cero coma sesenta y cuatro. Vemos dos de cada tres aviones, con un cinco
por ciento de falsas alarmas.

- «Ahora la detección» → `det`: rótulo «Detección»
- «el área de la campana del eco» → `areaeco`: el área del eco a la derecha de 1,645 se rellena de verde
- «a la derecha de ese umbral» → `derumb`: la marca de 1,645 destella
- «un poco a la izquierda de su centro» → `izq`: una flecha corta de 1,645 a 2
- «algo más de la mitad» → `mitad`: una línea en el centro del eco la parte en dos; «> ½»
- «cero coma sesenta y cuatro» → `v064`: «Detección = 0,64»
- «dos de cada tres aviones» → `aviones`: tres aviones pequeños; dos se pintan de verde
- «un cinco por ciento de falsas alarmas» → `fa`: debajo, «Falsa alarma = 5 %»

---

# Escena 12 — OtrosUmbrales

**Capítulo YouTube:** Menos falsas alarmas, menos aviones
**Objetivo:** comparar con los umbrales 1 y 2,33 V y abrir la pregunta: ¿habrá
una región rara mejor que un umbral?

## Narración

<!-- b1 -->
Comparemos con otros umbrales. En un voltio: dieciséis por ciento de falsas
alarmas y ochenta y cuatro de detección. Para tolerar solo un uno por ciento,
el umbral sube a dos coma treinta y tres voltios, y la detección cae al treinta y
siete. Ninguno es mejor en abstracto: menos falsas alarmas se pagan con menos
aviones vistos.

- «Comparemos con otros umbrales» → `tabla`: las campanas suben; debajo, tabla «Umbral · Falsa alarma · Detección» con la fila «1,645 V · 5 % · 64 %»
- «En un voltio» → `u1`: la marca baja a 1; nueva fila «1 V»
- «dieciséis por ciento» → `fa16`: «16 %», y la cola roja crece
- «ochenta y cuatro de detección» → `d84`: «84 %», y el área verde crece
- «solo un uno por ciento» → `fa1`: tercera fila con «1 %»
- «dos coma treinta y tres voltios» → `u233`: la marca sube a 2,33; «2,33 V» en la fila
- «cae al treinta y siete» → `d37`: «37 %», y el área verde se encoge
- «Ninguno es mejor en abstracto» → `ninguno`: las tres filas, ninguna resaltada
- «menos falsas alarmas» → `menosfa`: una flecha hacia abajo en la columna de falsa alarma
- «menos aviones vistos» → `menosdet`: una flecha hacia abajo en la de detección

<!-- b2 -->
Pero hemos dado algo por supuesto: que la región donde se dice avión es todo lo
que queda a la derecha de un umbral. ¿Y si existiera otra región, más rara, con
el mismo cinco por ciento de falsas alarmas y más detección?

- «hemos dado algo por supuesto» → `supuesto`: la tabla se va; las campanas con la marca en 1,645
- «todo lo que queda a la derecha» → `derecha`: la región del eje a la derecha de 1,645, en ámbar
- «¿Y si existiera» → `ysi`: un «?» pequeño sobre la región ámbar
- «otra región, más rara» → `rara`: la región ámbar se rompe en varios trozos sueltos por el eje
- «el mismo cinco por ciento» → `mismo`: «Falsa alarma = 5 %»
- «y más detección?» → `mas`: «¿Detección > 0,64?» con un «?» grande

---

# Escena 13 — ElPresupuesto

**Capítulo YouTube:** La falsa alarma es un presupuesto
**Objetivo:** presentar la tabla de cinco niveles: cada nivel cuesta falsa alarma
y rinde detección.

## Narración

<!-- b1 -->
Veámoslo con un caso de juguete. Un detector entrega un nivel, de uno a cinco.
Sin avión, los niveles salen con probabilidades cero coma cuarenta, cero coma
treinta, cero coma quince, cero coma diez y cero coma cero cinco. Con avión, al
revés. Hay que elegir en qué niveles se dice avión, con un quince por ciento de
falsas alarmas como mucho.

- «un caso de juguete» → `juguete`: corte; un detector (una caja con una aguja)
- «un nivel, de uno a cinco» → `niveles`: a la derecha, cinco casillas: «Nivel 1» … «Nivel 5»
- «Sin avión» → `sin`: rótulo de fila «Sin avión»
- «cero coma cuarenta» → `n1`: «0,40» en el nivel 1
- «cero coma treinta» → `n2`: «0,30»
- «cero coma quince» → `n3`: «0,15»
- «cero coma diez» → `n4`: «0,10»
- «cero coma cero cinco» → `n5`: «0,05»
- «Con avión, al revés» → `con`: segunda fila, «Con avión»: «0,05 · 0,10 · 0,15 · 0,30 · 0,40»
- «en qué niveles se dice avión» → `elegir`: sobre cada casilla, un cuadradito de marcar vacío
- «un quince por ciento de falsas alarmas» → `limite`: abajo, «Falsa alarma ≤ 0,15»

<!-- b2 -->
Piénsalo como un presupuesto. Cada nivel que metes en la región de decir avión
cuesta su probabilidad sin avión, porque eso es falsa alarma. Y rinde su
probabilidad con avión, porque eso es detección. El nivel cinco cuesta cero
coma cero cinco y rinde cero coma cuarenta. El nivel tres cuesta cero coma
quince y rinde cero coma quince.

- «como un presupuesto» → `monedero`: «Falsa alarma ≤ 0,15» se vuelve un monedero con «Presupuesto: 0,15»
- «Cada nivel que metes» → `metes`: una casilla se ilumina
- «cuesta su probabilidad sin avión» → `cuesta`: la fila «Sin avión» pasa a llamarse «Cuesta», en rojo
- «eso es falsa alarma» → `fa`: al lado, «= Falsa alarma»
- «Y rinde su probabilidad con avión» → `rinde`: la fila «Con avión» pasa a «Rinde», en verde
- «eso es detección» → `det`: «= Detección»
- «El nivel cinco cuesta» → `c5`: se resalta la casilla 5 y su «0,05» rojo
- «rinde cero coma cuarenta» → `r5`: y su «0,40» verde
- «El nivel tres cuesta» → `c3`: se resalta la casilla 3 y su «0,15» rojo
- «rinde cero coma quince» → `r3`: y su «0,15» verde

---

# Escena 14 — LaMochila

**Capítulo YouTube:** Llenar la mochila
**Objetivo:** ver que lo que más rinde por lo que cuesta es la razón de
verosimilitud, y que llenar por ese orden da la mejor detección (0,70 contra 0,15).

## Narración

<!-- b1 -->
Es como llenar una mochila: primero, lo que más rinde por lo que cuesta. Para
el nivel cinco, ese cociente es ocho. Para el cuatro, tres. Para el tres, uno.
Para los otros dos, menos de uno. Y ese cociente, lo que rinde con avión entre
lo que cuesta sin avión, es exactamente la razón de verosimilitud.

- «llenar una mochila» → `mochila`: entra una mochila vacía bajo la tabla
- «lo que más rinde por lo que cuesta» → `cociente`: tercera fila, «Rinde / Cuesta»
- «Para el nivel cinco» → `n5`: se resalta la casilla 5
- «ese cociente es ocho» → `q5`: en el nivel 5, «8»
- «Para el cuatro, tres» → `q4`: en el 4, «3»
- «Para el tres, uno» → `q3`: en el 3, «1»
- «menos de uno» → `q12`: en el 2 y el 1, «0,33» y «0,125»
- «lo que rinde con avión» → `num`: se resalta la fila «Rinde»
- «lo que cuesta sin avión» → `den`: se resalta la fila «Cuesta»
- «la razón de verosimilitud» → `lambda`: junto a la tercera fila, «= Λ»

<!-- b2 -->
Compramos el nivel cinco y el nivel cuatro. Cuestan cero coma quince, justo el
presupuesto, y la detección es cero coma setenta. Con el mismo gasto podrías
haber comprado solo el nivel tres, y detectarías cero coma quince. Cualquier
cambio saca algo que rendía mucho para meter algo que rinde menos.

- «el nivel cinco» → `m5`: la casilla 5 vuela a la mochila
- «el nivel cuatro» → `m4`: la casilla 4, también
- «Cuestan cero coma quince» → `coste`: «Coste: 0,05 + 0,10 = 0,15»; el monedero queda vacío
- «la detección es cero coma setenta» → `d70`: «Detección: 0,40 + 0,30 = 0,70», en verde
- «Con el mismo gasto» → `gasto`: al lado, un segundo monedero lleno: «0,15»
- «solo el nivel tres» → `alt`: al lado, otra mochila con solo el nivel 3: «Coste 0,15 · Detección 0,15»
- «detectarías cero coma quince» → `tacha`: la segunda mochila se tacha
- «Cualquier cambio» → `cambio`: en la primera mochila, el nivel 4 sale y entra el 3
- «algo que rinde menos» → `menos`: la detección baja a 0,55 en rojo, y el cambio se deshace

---

# Escena 15 — ElLemaDeNeymanPearson

**Capítulo YouTube:** El lema de Neyman-Pearson
**Objetivo:** enunciar el lema y concluir que máximo a posteriori y
Neyman-Pearson son el mismo test con distinto umbral.

## Narración

<!-- b1 -->
Este es el lema de Neyman-Pearson. Para un presupuesto de falsas alarmas, la
mejor región es siempre la de razón de verosimilitud mayor que un umbral, con
eta elegido para gastar justo el presupuesto. Con mediciones continuas el
argumento es el mismo, con rebanadas finas en vez de casillas.

- «el lema de Neyman-Pearson» → `lema`: corte; rótulo «Lema de Neyman-Pearson»
- «Para un presupuesto de falsas alarmas» → `presup`: «Falsa alarma ≤ α»
- «la mejor región» → `region`: «Mejor región:»
- «mayor que un umbral» → `lr`: «Λ(r) > η»
- «gastar justo el presupuesto» → `gastar`: «η tal que Falsa alarma = α»
- «Con mediciones continuas» → `cont`: el enunciado sube; entran las dos campanas
- «rebanadas finas» → `rebanadas`: el eje se parte en rebanadas finas, cada una con su altura en las dos campanas
- «en vez de casillas» → `casillas`: las cinco casillas de la mochila, en pequeño, se funden con las rebanadas

<!-- b2 -->
En las campanas la razón crece con erre, así que esa región es todo lo que
queda a la derecha de un umbral. No había una región mejor. Y fíjate: dos
criterios distintos, el mismo test. Un número, la razón de verosimilitud, y un
umbral. Solo cambia de dónde sale el umbral.

- «la razón crece con erre» → `crece`: a un lado, la curva creciente de Λ(r) = e^(2r − 2)
- «todo lo que queda a la derecha» → `derecha`: en las campanas, la región «r ≥ 1,645» en ámbar
- «No había una región mejor» → `nohabia`: la región rota de la escena 12 aparece en pequeño y se tacha
- «dos criterios distintos» → `dos`: corte; dos tarjetas: «Máximo a posteriori: η = p₀ / p₁» y «Neyman-Pearson: η por presupuesto»
- «el mismo test» → `test`: de las dos tarjetas salen flechas a una sola caja, «Λ(r) ≷ η»
- «Un número» → `num`: se resalta «Λ(r)»
- «y un umbral» → `umb`: se resalta «η»
- «de dónde sale el umbral» → `sale`: las dos flechas que llegan a «η» destellan

---

# Escena 16 — Cierre

**Capítulo YouTube:** Lo que viene: la curva de todos los umbrales

## Narración

<!-- b1 -->
Hoy hemos visto que decidir bien es calcular un número, la razón de
verosimilitud, y compararlo con un umbral. Si conoces las probabilidades a
priori, el umbral es pe cero entre pe uno. Si no, sale del presupuesto de
falsas alarmas.

- «decidir bien» → `decidir`: la caja «Λ(r) ≷ η» al centro
- «calcular un número» → `numero`: «Λ(r)» destella
- «compararlo con un umbral» → `umbral`: «η» destella
- «Si conoces las probabilidades a priori» → `apriori`: debajo a la izquierda, «Probabilidades a priori»
- «el umbral es pe cero entre pe uno» → `p0p1`: debajo, «η = p₀ / p₁»
- «Si no» → `sino`: debajo a la derecha, el monedero
- «el presupuesto de falsas alarmas» → `presup`: bajo el monedero, «Falsa alarma ≤ 5 %»

<!-- b2 -->
Pero cada umbral da un detector distinto, con su falsa alarma y su detección.
¿Y si pudiéramos verlos todos a la vez, en un solo dibujo? Lo veremos en el
próximo episodio: la curva de todos los umbrales.

- «cada umbral da un detector distinto» → `umbrales`: corte; las dos campanas con tres marcas de umbral
- «con su falsa alarma» → `fa`: bajo cada marca, la cola roja del ruido
- «y su detección» → `det`: y el área verde del eco
- «todos a la vez» → `todos`: las marcas se multiplican hasta llenar el eje
- «en un solo dibujo» → `dibujo`: a la derecha, un plano vacío «Falsa alarma · Detección» donde van cayendo puntos
- «en el próximo episodio» → `proximo`: los puntos se unen en una curva
- «la curva de todos los umbrales» → `titulo`: el título «La curva de todos los umbrales» entra con rebote
