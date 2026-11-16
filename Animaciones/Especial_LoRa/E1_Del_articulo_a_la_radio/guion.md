# Episodio 1 — LoRa: del artículo a la radio

Especial (trabajo práctico de la materia), episodio único. Duración: unos 29 min (especial, sin el límite de 10).
No sale de un `guion_base.md`: todo el texto es nuevo. Fuentes:
- L. Vangelista, «Frequency Shift Chirp Modulation: The LoRa Modulation», *IEEE Signal
  Processing Letters*, 2017 (Ec. 1, 2, 4 a 9, 10 y 16, y las conclusiones sobre el BER);
- el cuaderno `LoRa.ipynb` y el paquete `lora` del trabajo práctico (los números de este
  guion salen de correrlo: ver `datos/generar_datos.py` y `datos/comparar_modulaciones.py`);
- la rama `lora-phy` del trabajo, que usa en todos lados la modulación corregida (escena 28);
- las capturas del ADALM-Pluto del laboratorio (`captures/` del trabajo práctico) y el
  material del laboratorio de SDR (diagrama de bloques del Pluto).

**Estado:** `guion.md` con 29 escenas y momentos; escenas `s01`–`s29` animadas; render
1080p60 de 28:48 con 0 avisos, **hecho con la voz sin red** (`CURSO_VOZ_SIN_RED=1`: mudo, con
tiempos de palabra estimados), porque la sesión en la que se hizo no tenía salida a Azure Speech
ni a edge-tts. `ritmo.py --max 4.6` con esos tiempos: 0 huecos. Es un especial: pasa a propósito
del límite de 10 minutos (pedido del usuario).
Falta: el visto bueno del usuario a todo el texto ⭐ (regla 7 del README); las pronunciaciones
de oído; renderizar con la voz real (`python render.py Especial_LoRa/E1_Del_articulo_a_la_radio
--calidad qh`, sin `CURSO_VOZ_SIN_RED`) y, con los tiempos reales, volver a pasar `ritmo.py`,
los controles y las hojas de contacto; el visto bueno al mp4 (paso 15).

Texto nuevo, para revisar (marcado con ⭐): **todo el episodio** (es un especial sin guion
base). Lo más delicado:
- ⭐ Escena 01 (gancho) y escena 29 (cierre; no anuncia episodio siguiente).
- ⭐ Escena 08, «La letra pequeña»: resume el hallazgo del cuaderno (la Ec. 2 tomada al pie
  de la letra barre de 0 a 2B y, muestreada a B, da dos pasadas por símbolo).
- ⭐ Escena 16, FSK contra FSCM con eco: **no está en el cuaderno**; la simulación de FSK se
  escribió para el vídeo (mismo canal de eco y mismo receptor por FFT).
- ⭐ Escena 17, el factor de ensanchamiento como dial: los umbrales de SNR por factor se
  simularon para el vídeo.
- ⭐ Escenas 19 a 21, Neyman-Pearson: las cuentas (7.500.000 pruebas por minuto, umbral de
  126,6 σ²) salen de las fórmulas de `lora/detection.py`.
- ⭐ Escena 22, coste y rendimiento según el largo de la plantilla: simulado para el vídeo
  (el cuaderno solo usa la plantilla de 8 chirps).
- ⭐ Escena 28, la Ec. 2 contra la modulación corregida: compara el paquete `lora` del
  trabajo práctico (Ec. 2) con el de la rama `lora-phy` (fase con k/2), con
  `datos/comparar_modulaciones.py`. La demodulación rinde igual; la diferencia está en los
  picos laterales a medio símbolo de la correlación con el preámbulo.
- ⭐ Escenas 25 a 27: cómo se llevó la señal por debajo del ruido térmico en el Pluto.
- Un número que no coincide con el cuaderno: el BER simulado a −7 dB sale ≈ 10⁻⁴ y la
  observación del cuaderno dice 4·10⁻⁵.

Ejemplo que atraviesa el episodio: factor de ensanchamiento 7 (128 muestras por símbolo),
ancho de banda de 125 kHz y **el símbolo 20** (bits de peso 4 y 16). Para la detección y el
Pluto se usa el factor 8, como en el cuaderno.

Pronunciaciones a probar de oído (§9 del README): LoRa, chirp, Vangelista, Pluto,
Neyman-Pearson, «kilohercios», «megahercios». Las siglas no se dicen: SF, FFT, BER, FER,
SDR, AGC y FSK solo aparecen en pantalla.

Bucles con el curso: el chirp del radar (Cap. 13, E6 → escena 06), las flechas y la
ortogonalidad (Caps. 7 y 8 → escena 09), el ruido blanco (Caps. 10 y 11 → escenas 10 y 14),
«¿Cuál de ellas mandaron?» (Cap. 13, E7 → escena 11), el filtro adaptado (Cap. 13, E4 →
escena 16) y Neyman-Pearson (Cap. 9 → escena 16).

---

# Escena 01 — Gancho

**Capítulo YouTube:** Un mensaje debajo del ruido

## Narración

<!-- b1 -->
Aquí dentro hay un mensaje. No lo ves, porque el ruido tiene diez veces más potencia que la señal. Dos operaciones después, aparece: un pico limpio, en la posición que dice el dato. Así funciona LoRa. Hoy la construimos entera: del artículo que la explicó a una radio de verdad.

- «Aquí dentro hay un mensaje» → `senal`: una traza ruidosa en cian cruza la pantalla
- «No lo ves» → `nolo`: un «?» grande sobre la traza
- «diez veces más potencia» → `diez`: «Ruido × 10» en magenta
- «Dos operaciones después» → `dos`: dos cajas, «× Chirp que baja» y «FFT», con flechas
- «un pico limpio» → `pico`: debajo, las 128 casillas con un pico ámbar que sobresale
- «la posición que dice el dato» → `dato`: el rótulo «20» sobre el pico
- «Así funciona LoRa» → `lora`: la palabra «LoRa»
- «del artículo» → `articulo`: un documento
- «a una radio de verdad» → `radio`: el Pluto con sus dos antenas

---

# Escena 02 — TituloEpisodio

**Capítulo YouTube:** LoRa: del artículo a la radio

## Narración

<!-- b1 -->
LoRa: del artículo a la radio.

- «LoRa» → `t1`: «LoRa» entra con rebote
- «del artículo a la radio» → `t2`: «Del artículo a la radio» entra debajo, con la etiqueta «Especial · Trabajo práctico»

---

# Escena 03 — QueEsLoRa

**Capítulo YouTube:** Qué es LoRa y quién la explicó
**Objetivo:** para qué sirve LoRa (alcance a cambio de velocidad) y qué aporta el artículo de Vangelista.

## Narración

<!-- b1 -->
Piensa en un sensor en mitad del campo. Funciona con una pila, está a kilómetros de cualquier antena y solo tiene que mandar unos pocos números al día. No necesita velocidad: necesita alcance y gastar muy poco. Para eso existe LoRa, de long range, largo alcance: cambia velocidad por distancia.

- «un sensor en mitad del campo» → `sensor`: un sensor pequeño sobre una línea de suelo
- «una pila» → `pila`: una pila junto al sensor
- «a kilómetros» → `km`: lejos, a la derecha, una torre de antena y una cota «10 km»
- «unos pocos números al día» → `numeros`: tres números pequeños viajan del sensor a la antena
- «No necesita velocidad» → `veloc`: la palabra «Velocidad», tachada
- «alcance» → `alcance`: la palabra «Alcance» en verde
- «gastar muy poco» → `poco`: «Poco consumo» en verde
- «LoRa» → `lora`: «LoRa» grande
- «largo alcance» → `largo`: debajo, «Long Range»
- «cambia velocidad por distancia» → `cambia`: «Velocidad → Distancia»

<!-- b2 -->
El problema es que la modulación de LoRa está patentada, y durante años nadie la describió con ecuaciones. Hasta dos mil diecisiete, cuando Lorenzo Vangelista publicó un artículo de cuatro páginas con la primera descripción rigurosa. Y le puso un nombre mejor: modulación por desplazamiento de frecuencia de un chirp.

- «está patentada» → `patente`: un candado cerrado
- «nadie la describió con ecuaciones» → `nadie`: «c(t) = ?»
- «dos mil diecisiete» → `anio`: «2017»
- «Lorenzo Vangelista» → `autor`: «L. Vangelista»
- «cuatro páginas» → `paginas`: cuatro documentos en fila
- «la primera descripción rigurosa» → `rigurosa`: una tilde verde junto a los documentos
- «un nombre mejor» → `nombre`: el candado y lo demás salen
- «desplazamiento de frecuencia» → `fs`: «Frequency Shift»
- «de un chirp» → `chirp`: «Chirp Modulation» y, debajo, las siglas «FSCM»

---

# Escena 04 — DosParametros

**Capítulo YouTube:** Ancho de banda y factor de ensanchamiento
**Objetivo:** los dos números que fijan todo: B (una muestra cada 1/B) y SF (2^SF muestras por símbolo).

## Narración

<!-- b1 -->
Todo depende de dos números. El primero es el ancho de banda: el trozo de espectro que ocupamos. Con ciento veinticinco kilohercios, mandamos una muestra cada ocho microsegundos. A cada muestra, el artículo la llama chip.

- «dos números» → `dos`: dos huecos vacíos, uno al lado del otro
- «el ancho de banda» → `banda`: en el primer hueco, «B»
- «el trozo de espectro» → `trozo`: un eje de frecuencia con una franja azul de ancho B
- «ciento veinticinco kilohercios» → `khz`: «B = 125 kHz»
- «una muestra cada ocho microsegundos» → `muestra`: una fila de puntos separados y «T = 1/B = 8 µs»
- «A cada muestra» → `cada`: uno de los puntos se resalta en ámbar
- «chip» → `chip`: la palabra «Chip» sobre un punto

<!-- b2 -->
El segundo es el factor de ensanchamiento. Con un factor de siete, cada símbolo lleva siete bits y dura dos elevado a siete muestras: ciento veintiocho. Es decir, algo más de un milisegundo por cada siete bits. Lento a propósito.

- «el factor de ensanchamiento» → `sf`: en el segundo hueco, «SF»
- «un factor de siete» → `siete`: «SF = 7»
- «siete bits» → `bits`: siete casillas de bits
- «dos elevado a siete muestras» → `pot`: «2⁷»
- «ciento veintiocho» → `n128`: «= 128 muestras»
- «algo más de un milisegundo» → `ms`: «Tₛ = 128 · 8 µs = 1,024 ms»
- «Lento a propósito» → `lento`: «Lento a propósito» en ámbar

---

# Escena 05 — DeBitsASimbolo

**Capítulo YouTube:** Ecuación 1: de siete bits a un símbolo
**Objetivo:** el codificador lee SF bits como un número binario; el ejemplo es el símbolo 20.

## Narración

<!-- b1 -->
Primer paso: el codificador. Toma siete bits y los lee como un número en binario. Cada bit tiene un peso: uno, dos, cuatro, ocho, y así hasta sesenta y cuatro. Si están encendidos el del cuatro y el del dieciséis, el símbolo es veinte. Con siete bits salen ciento veintiocho símbolos posibles, del cero al ciento veintisiete.

- «el codificador» → `cod`: una caja «Codificador»
- «siete bits» → `bits`: siete casillas vacías en fila
- «un número en binario» → `bin`: las casillas se llenan: 0 0 1 0 1 0 0
- «Cada bit tiene un peso» → `pesos`: debajo de cada casilla, un hueco para su peso
- «uno, dos, cuatro, ocho» → `p1`: aparecen los pesos 1, 2, 4, 8
- «sesenta y cuatro» → `p64`: aparecen 16, 32 y 64
- «el del cuatro y el del dieciséis» → `enc`: las casillas del 4 y del 16 se encienden en ámbar
- «el símbolo es veinte» → `veinte`: «4 + 16 = 20»
- «ciento veintiocho símbolos posibles» → `total`: «128 símbolos»
- «del cero al ciento veintisiete» → `rango`: «0 … 127»

<!-- b2 -->
Esa es la ecuación uno del artículo: el símbolo es la suma de cada bit por su potencia de dos.

- «la ecuación uno» → `ec1`: el rótulo «Ec. 1»
- «el símbolo» → `s`: «s =»
- «la suma» → `suma`: el signo de sumatoria, de h = 0 a SF − 1
- «cada bit» → `bit`: «w_h»
- «su potencia de dos» → `pot`: «· 2^h»

---

# Escena 06 — ElChirp

**Capítulo YouTube:** La onda base: un chirp
**Objetivo:** la onda base es un barrido de frecuencia de 0 a B a lo largo del símbolo; en el plano tiempo-frecuencia es una rampa.

## Narración

<!-- b1 -->
Segundo paso: convertir ese número en una onda. La onda base de LoRa es un chirp: una oscilación cuya frecuencia sube sin parar, desde cero hasta el ancho de banda, a lo largo del símbolo. Es el mismo barrido de frecuencia del radar. Si dibujamos la frecuencia contra el tiempo, es una rampa.

- «convertir ese número en una onda» → `onda`: «20» y una flecha hacia una onda todavía sin dibujar
- «un chirp» → `chirp`: la palabra «Chirp»
- «cuya frecuencia sube sin parar» → `sube`: se dibuja la onda, cada vez más apretada
- «desde cero» → `cero`: «0» bajo el principio de la onda
- «hasta el ancho de banda» → `hastab`: «B» bajo el final
- «a lo largo del símbolo» → `simbolo`: una cota «Tₛ» de punta a punta
- «del radar» → `radar`: el radar del capítulo 13
- «la frecuencia contra el tiempo» → `ft`: abajo, un plano con «Tiempo» y «Frecuencia»
- «una rampa» → `rampa`: en el plano se traza una recta de 0 a B

---

# Escena 07 — ElDatoEsElDesplazamiento

**Capítulo YouTube:** Ecuación 2: el dato desplaza el chirp
**Objetivo:** el símbolo fija la frecuencia de partida; la rampa sube, da la vuelta en B y sigue. Se construye la Ec. 2.

## Narración

<!-- b1 -->
¿Y dónde va el dato? En el punto de partida. El símbolo cero arranca en la frecuencia cero. El símbolo veinte arranca veinte escalones más arriba. La rampa sube igual, y cuando llega al tope del ancho de banda, vuelve a cero y sigue subiendo hasta completar el símbolo.

- «¿Y dónde va el dato?» → `donde`: el plano tiempo-frecuencia vacío, con un «?»
- «En el punto de partida» → `partida`: un punto ámbar en el borde izquierdo
- «El símbolo cero» → `s0`: la rampa del símbolo 0 y el rótulo «s = 0»
- «El símbolo veinte» → `s20`: el rótulo pasa a «s = 20»
- «veinte escalones más arriba» → `escal`: el punto de partida sube y la rampa con él
- «La rampa sube igual» → `igual`: la rampa se resalta
- «llega al tope» → `tope`: un punto en el borde de arriba, donde la rampa toca B
- «vuelve a cero» → `vuelve`: una línea de trazos baja hasta 0
- «hasta completar el símbolo» → `completa`: el segundo tramo de la rampa se resalta

<!-- b2 -->
Cada símbolo es la misma rampa, desplazada. Por eso Vangelista dice que el chirp hace de portadora y que la información está en el desplazamiento de frecuencia. Aquí van tres símbolos seguidos: cero, treinta y dos y ochenta.

- «la misma rampa, desplazada» → `misma`: el símbolo barre de 20 a 100 y vuelve, y la rampa se desplaza en vivo
- «el chirp hace de portadora» → `porta`: «Chirp = Portadora»
- «la información está en el desplazamiento» → `info`: «Dato = Desplazamiento»
- «Aquí van» → `aqui`: los dos rótulos salen
- «tres símbolos seguidos» → `tres`: el plano se ensancha a tres símbolos
- «cero» → `c0`: la rampa del símbolo 0
- «treinta y dos» → `c32`: la rampa del símbolo 32
- «ochenta» → `c80`: la rampa del símbolo 80

<!-- b3 -->
La ecuación dos lo resume. Una exponencial compleja, que es una flecha que gira. Su frecuencia es el símbolo más el índice de la muestra, con la vuelta a cero al llegar al tope. Y un factor delante para que cada símbolo tenga energía uno.

- «La ecuación dos» → `ec2`: el rótulo «Ec. 2» y «c(nTₛ + kT) =»
- «Una exponencial compleja» → `exp`: «e^{j2π … k/2^SF}»
- «una flecha que gira» → `flecha`: una flecha que da vueltas en un círculo
- «el símbolo más el índice de la muestra» → `smask`: dentro del exponente, «(s + k)»
- «la vuelta a cero» → `mod`: «mod 2^SF»
- «un factor delante» → `factor`: «1/√(2^SF)»
- «energía uno» → `e1`: «Energía = 1»

---

# Escena 08 — LaLetraPequena

**Capítulo YouTube:** La letra pequeña de la ecuación 2
**Objetivo:** lo que encontró el cuaderno: la fase de la Ec. 2 crece con k², la frecuencia real barre de 0 a 2B y, muestreada a B, se repliega en dos pasadas por símbolo.

## Narración

<!-- b1 -->
Aquí hay letra pequeña, y el cuaderno del trabajo la encontró. En la ecuación dos, esa frecuencia que crece está multiplicada por el tiempo, que también crece. La fase avanza entonces con el cuadrado del índice, y la frecuencia real sube el doble de rápido: de cero a dos veces el ancho de banda.

- «letra pequeña» → `letra`: una lupa
- «el cuaderno del trabajo» → `cuaderno`: una ventana «LoRa.ipynb»
- «esa frecuencia que crece» → `frec`: el exponente de la Ec. 2, con «(s + k)» en ámbar
- «multiplicada por el tiempo» → `tiempo`: el factor «k» en cian
- «que también crece» → `crece`: una flecha hacia arriba junto a «k»
- «La fase avanza» → `fase`: la palabra «Fase»
- «el cuadrado del índice» → `cuad`: debajo, «Fase ∝ k²»
- «el doble de rápido» → `doble`: en un plano que llega hasta 2B, una rampa con el doble de pendiente
- «dos veces el ancho de banda» → `dosb`: el rótulo «2B» arriba del todo

<!-- b2 -->
Como muestreamos al ritmo del ancho de banda, lo que pasa de ese tope se repliega: es el aliasing. Y en el espectrograma aparecen dos pasadas por símbolo en lugar de una. El cuaderno compara las dos versiones y se queda con la ecuación dos tal cual, porque sobre ella el artículo demuestra todo lo que sigue.

- «muestreamos al ritmo» → `muest`: una línea horizontal de trazos a la altura B
- «se repliega» → `replieg`: la mitad de arriba de la rampa baja y queda como una segunda rampa de 0 a B
- «aliasing» → `alias`: la palabra «Aliasing»
- «dos pasadas por símbolo» → `dospas`: el rótulo «Ec. 2: dos pasadas»
- «en lugar de una» → `una`: al lado, un plano con una sola rampa y «Descripción: una pasada»
- «compara las dos versiones» → `compara`: un «≠» entre los dos planos
- «se queda con la ecuación dos» → `queda`: un marco verde rodea el plano de las dos pasadas
- «tal cual» → `talcual`: el otro plano se atenúa
- «el artículo demuestra» → `demuestra`: un documento con una tilde
- «todo lo que sigue» → `sigue`: «Ortogonalidad · Receptor · BER»

---

# Escena 09 — OndasOrtogonales

**Capítulo YouTube:** Ecuaciones 4 a 9: ondas ortogonales
**Objetivo:** las 2^SF ondas son ortogonales: producto interno 0 entre distintas, 1 consigo misma. Se ve con flechas que cierran un polígono.

## Narración

<!-- b1 -->
Tenemos ciento veintiocho ondas, una por símbolo. Para que el receptor no las confunda, el artículo demuestra que son ortogonales. ¿Qué quiere decir? Que si multiplicas dos ondas distintas muestra a muestra, una de ellas conjugada, y sumas, da cero. Es el producto interno: mide cuánto se parecen.

- «ciento veintiocho ondas» → `ondas`: una pila de rampas desplazadas, una por símbolo
- «una por símbolo» → `unapor`: los rótulos «s = 0», «s = 1», «s = 2», «…»
- «no las confunda» → `confunda`: un «?» junto a la pila
- «ortogonales» → `orto`: la palabra «Ortogonales»
- «multiplicas dos ondas distintas» → `mult`: «c_i · c_q*»
- «muestra a muestra» → `mam`: el índice «k» bajo el producto
- «sumas» → `sumas`: el signo de sumatoria delante
- «da cero» → `cero`: «= 0»
- «producto interno» → `pi`: «⟨c_i, c_q⟩»
- «cuánto se parecen» → `parecen`: «Parecido»

<!-- b2 -->
Se ve con flechas. Cada producto es una flecha, y de una muestra a la siguiente gira un ángulo fijo. A lo largo del símbolo da vueltas completas, así que las flechas, puestas una detrás de otra, cierran un polígono y vuelven al origen. Suma cero.

- «Se ve con flechas» → `flechas`: la fórmula sube y queda un punto de origen
- «Cada producto es una flecha» → `una`: una flecha azul sale del origen
- «gira un ángulo fijo» → `gira`: una segunda flecha, girada 45 grados, con su arco
- «vueltas completas» → `vueltas`: las ocho flechas en abanico, como un reloj
- «una detrás de otra» → `detras`: las flechas se encadenan punta con cola
- «cierran un polígono» → `cierran`: el octágono se cierra
- «Suma cero» → `suma0`: «Suma = 0»

<!-- b3 -->
En cambio, una onda consigo misma no gira nada: todas las flechas apuntan igual y suman uno. Cero con las demás, uno consigo misma. Eso es una base ortogonal, y es lo que hace posible el receptor.

- «consigo misma» → `misma`: «⟨c_i, c_i⟩»
- «todas las flechas apuntan igual» → `igual`: ocho flechas en fila, todas hacia la derecha
- «suman uno» → `uno`: «= 1»
- «Cero con las demás» → `ceros`: una tabla pequeña con ceros fuera de la diagonal
- «uno consigo misma» → `unos`: unos en la diagonal
- «una base ortogonal» → `base`: «Base ortogonal»
- «el receptor» → `rx`: «→ Receptor»

---

# Escena 10 — ElCanalConRuido

**Capítulo YouTube:** Ecuación 10: el canal mete ruido
**Objetivo:** r = c + w con ruido blanco gaussiano; qué significa −10 dB.

## Narración

<!-- b1 -->
Por el aire, a la onda se le suma ruido. El modelo del artículo es el más sencillo: lo recibido es lo transmitido más ruido blanco gaussiano. Blanco quiere decir que reparte su potencia por igual en todas las frecuencias. Con una relación señal a ruido de menos diez decibelios, el ruido tiene diez veces la potencia de la señal, y el chirp ya no se reconoce.

- «Por el aire» → `aire`: dos antenas enfrentadas
- «se le suma ruido» → `suma`: entre ellas, una traza de ruido magenta
- «lo recibido» → `r`: «r =»
- «lo transmitido» → `c`: «c»
- «más ruido blanco gaussiano» → `w`: «+ w»
- «Blanco» → `blanco`: la palabra «Blanco»
- «por igual en todas las frecuencias» → `plano`: un espectro plano, rectangular
- «una relación señal a ruido» → `snr`: «SNR =»
- «menos diez decibelios» → `db`: «−10 dB»
- «diez veces la potencia» → `diez`: dos barras: «Señal 1» y «Ruido 10»
- «ya no se reconoce» → `noreco`: el chirp limpio se convierte en la traza recibida

---

# Escena 11 — ElReceptorOptimo

**Capítulo YouTube:** El receptor óptimo
**Objetivo:** con símbolos equiprobables de igual energía en ruido blanco, lo óptimo es correlar con las 2^SF ondas y elegir la mayor; el coste es 2^SF · 2^SF.

## Narración

<!-- b1 -->
¿Cómo se decide qué símbolo llegó? Con símbolos igual de probables, la misma energía y ruido blanco, el receptor óptimo es el que ya conocemos: comparar lo recibido con cada onda posible y quedarse con la que más se parece. Ciento veintiocho productos internos, y gana el mayor.

- «qué símbolo llegó» → `que`: «r» a la izquierda y «ŝ = ?» a la derecha
- «igual de probables» → `prob`: una ficha «Equiprobables»
- «la misma energía» → `ener`: una ficha «Igual energía»
- «ruido blanco» → `ruido`: una ficha «Ruido blanco»
- «el receptor óptimo» → `optimo`: «Receptor óptimo»
- «con cada onda posible» → `cada`: una columna de cajas «⟨r, c₀⟩», «⟨r, c₁⟩», «⋮», «⟨r, c₁₂₇⟩»
- «la que más se parece» → `parece`: una barra junto a cada caja; una mucho más larga
- «Ciento veintiocho productos internos» → `n128`: una llave «128»
- «gana el mayor» → `mayor`: «ŝ = arg max» y una flecha desde la barra larga

<!-- b2 -->
Pero cada producto interno son ciento veintiocho multiplicaciones. En total, más de dieciséis mil por símbolo. Y con un factor de doce, casi diecisiete millones. Hace falta un atajo.

- «ciento veintiocho multiplicaciones» → `mult`: «128 × 128»
- «más de dieciséis mil» → `mil`: «= 16.384»
- «un factor de doce» → `doce`: «SF = 12»
- «casi diecisiete millones» → `millones`: «4096 × 4096 = 16.777.216»
- «un atajo» → `atajo`: la palabra «Atajo» con un rayo

---

# Escena 12 — DeshacerElChirp

**Capítulo YouTube:** Ecuación 16: deshacer el chirp
**Objetivo:** multiplicar por el chirp que baja convierte el chirp del símbolo s en un tono de s vueltas por símbolo.

## Narración

<!-- b1 -->
El atajo es la ecuación dieciséis, y tiene dos pasos. Primero, multiplicar lo recibido por un chirp al revés, uno que baja en lugar de subir. La subida y la bajada se cancelan, y lo único que sobrevive es el desplazamiento. El chirp del símbolo veinte se convierte en un tono puro: una sinusoide que da exactamente veinte vueltas por símbolo.

- «la ecuación dieciséis» → `ec16`: el rótulo «Ec. 16»
- «dos pasos» → `dos`: dos huecos numerados, «1» y «2»
- «multiplicar lo recibido» → `mult`: tres planos en fila; en el primero, la rampa del símbolo 20
- «un chirp al revés» → `reves`: en el segundo plano, tras un «×», una rampa que baja
- «que baja en lugar de subir» → `baja`: la rampa que baja se resalta
- «se cancelan» → `cancel`: un «=» y el tercer plano, vacío
- «el desplazamiento» → `despl`: en el tercer plano, una línea horizontal a la altura 20
- «El chirp del símbolo veinte» → `s20`: abajo, la onda del chirp
- «un tono puro» → `tono`: la onda se transforma en una sinusoide regular
- «veinte vueltas por símbolo» → `v20`: «20 vueltas»

---

# Escena 13 — UnaSolaTransformada

**Capítulo YouTube:** Una sola transformada rápida
**Objetivo:** correlar con los 2^SF tonos es una DFT; la FFT da las 128 correlaciones de una vez y el pico cae en la casilla del símbolo.

## Narración

<!-- b1 -->
Segundo paso. Comparar con ciento veintiocho tonos de frecuencias uno, dos, tres… es justo lo que hace la transformada discreta de Fourier. Y la transformada rápida calcula las ciento veintiocho comparaciones de una vez. El resultado es un pico en la casilla veinte y nada en las demás. El receptor solo tiene que buscar el máximo.

- «Segundo paso» → `paso2`: el hueco «2» y, arriba, el tono de 20 vueltas
- «ciento veintiocho tonos» → `tonos`: a la izquierda, tres tonos de muestra apilados y puntos suspensivos
- «uno, dos, tres» → `unodos`: los rótulos 1, 2 y 3 junto a los tonos
- «la transformada discreta de Fourier» → `dft`: «DFT»
- «la transformada rápida» → `fft`: una caja «FFT» recibe el tono
- «las ciento veintiocho comparaciones» → `comp`: «128 a la vez»
- «de una vez» → `vez`: de la caja sale una flecha hacia abajo
- «un pico en la casilla veinte» → `pico`: las 128 casillas; solo la 20 tiene altura
- «nada en las demás» → `nada`: una llave sobre las casillas vacías con «0»
- «buscar el máximo» → `max`: «ŝ = 20» y una flecha al pico

<!-- b2 -->
Multiplicar por el chirp que baja, transformar y elegir el máximo. De dieciséis mil multiplicaciones pasamos a una transformada rápida por símbolo.

- «Multiplicar por el chirp que baja» → `m1`: una cadena de tres cajas; la primera, «× Chirp que baja»
- «transformar» → `m2`: la segunda, «FFT»
- «elegir el máximo» → `m3`: la tercera, «Máximo»
- «dieciséis mil multiplicaciones» → `antes`: «16.384», tachado
- «una transformada rápida por símbolo» → `ahora`: «1 FFT por símbolo» en verde

---

# Escena 14 — PorQueAguantaElRuido

**Capítulo YouTube:** Por qué aguanta tanto ruido
**Objetivo:** la señal se concentra en una casilla y el ruido blanco se reparte en 2^SF: ganancia de 21 dB con SF = 7.

## Narración

<!-- b1 -->
Ahora se entiende el principio del vídeo. Al deshacer el chirp, toda la energía del símbolo cae en una sola casilla. El ruido, en cambio, es blanco: multiplicarlo por el chirp no lo cambia, y la transformada lo reparte por igual entre las ciento veintiocho casillas. La señal se concentra y el ruido se diluye.

- «el principio del vídeo» → `principio`: la traza ruidosa del gancho
- «toda la energía del símbolo» → `energia`: abajo, el eje de las casillas
- «en una sola casilla» → `casilla`: el pico ámbar en la casilla 20
- «El ruido, en cambio, es blanco» → `blanco`: «Ruido blanco» en magenta
- «multiplicarlo por el chirp» → `multi`: «× Chirp»
- «no lo cambia» → `nocambia`: «Sigue blanco»
- «lo reparte por igual» → `reparte`: un piso de ruido magenta en todas las casillas
- «ciento veintiocho casillas» → `n128`: una cota «128 casillas»
- «La señal se concentra» → `concentra`: el pico se resalta
- «el ruido se diluye» → `diluye`: una línea de trazos marca el nivel medio del ruido

<!-- b2 -->
La ganancia es el número de casillas: ciento veintiocho veces, veintiún decibelios. Con menos diez decibelios por muestra, el pico queda once decibelios por encima del ruido de su casilla. Por eso se ve. Y cada punto que sube el factor de ensanchamiento duplica las casillas: tres decibelios más, a cambio de tardar el doble.

- «el número de casillas» → `num`: «Ganancia = 2^SF»
- «ciento veintiocho veces» → `veces`: «= 128»
- «veintiún decibelios» → `db21`: «= 21 dB»
- «menos diez decibelios por muestra» → `m10`: «−10 dB»
- «once decibelios por encima» → `db11`: «+ 21 dB = +11 dB»
- «Por eso se ve» → `seve`: el pico se resalta otra vez
- «duplica las casillas» → `duplica`: «SF 7 → 8: 128 → 256»
- «tres decibelios más» → `db3`: «+3 dB»
- «tardar el doble» → `doble`: «Tₛ × 2»

---

# Escena 15 — LaCurvaDeErrores

**Capítulo YouTube:** Decodificador y tasa de error de bit
**Objetivo:** el decodificador deshace la Ec. 1; la curva de BER contra SNR del cuaderno reproduce la del artículo, en canal plano y con eco.

## Narración

<!-- b1 -->
El último bloque, el decodificador, deshace la ecuación uno: del número veinte vuelven a salir los siete bits. Y para medir todo el sistema se cuentan los bits equivocados sobre los enviados: la tasa de error de bit.

- «el decodificador» → `deco`: una caja «Decodificador»
- «del número veinte» → `veinte`: «20» entra en la caja
- «los siete bits» → `bits`: salen las siete casillas 0 0 1 0 1 0 0
- «los bits equivocados» → `equiv`: «Bits erróneos»
- «sobre los enviados» → `sobre`: una raya de fracción y «Bits enviados»
- «la tasa de error de bit» → `ber`: «BER =»

<!-- b2 -->
El cuaderno la simula para muchos niveles de ruido y reproduce la curva del artículo. Con menos doce decibelios falla uno de cada diez bits. Con menos siete, uno de cada diez mil. Cinco decibelios separan un enlace inútil de uno casi perfecto.

- «para muchos niveles de ruido» → `niveles`: ejes: «SNR (dB)» de −12 a −6 y «BER» en escala logarítmica
- «la curva del artículo» → `curva`: se traza la curva del canal plano
- «menos doce decibelios» → `m12`: un punto en −12 dB
- «uno de cada diez bits» → `diez`: «1 de cada 10»
- «Con menos siete» → `m7`: un punto en −7 dB
- «uno de cada diez mil» → `mil`: «1 de cada 10.000»
- «Cinco decibelios» → `cinco`: una cota «5 dB» entre los dos puntos
- «casi perfecto» → `perfecto`: una tilde verde

<!-- b3 -->
El artículo prueba también un canal con eco, donde llega una segunda copia de la señal retrasada una muestra. Ahí hace falta algo más de señal para el mismo error. Y lo compara con la modulación clásica de tonos fijos, la FSK: en un canal plano rinden igual, pero con eco la de LoRa gana con claridad. ¿Por qué?

- «un canal con eco» → `eco`: dos tallos: uno alto y uno bajo
- «una segunda copia» → `copia`: el tallo bajo se resalta
- «retrasada una muestra» → `retras`: los valores «√0,8» y «√0,2»
- «algo más de señal» → `mas`: una segunda curva, en cian, a la derecha de la primera
- «la modulación clásica de tonos fijos» → `fsk`: la palabra «FSK»
- «rinden igual» → `igual`: «Canal plano: FSCM = FSK»
- «gana con claridad» → `mejor`: «Con eco: FSCM gana»
- «¿Por qué?» → `porque`: «¿Por qué?» en ámbar

---

# Escena 16 — FskContraFscm

**Capítulo YouTube:** Por qué el eco castiga más a la FSK
**Objetivo:** la razón teórica: el eco hace un canal con ganancia distinta en cada frecuencia; la FSK pone cada símbolo en una frecuencia y algunos caen en el hueco; el chirp reparte cada símbolo por toda la banda y todos pierden lo mismo (un 20 %).

## Narración

<!-- b1 -->
Primero, qué es la FSK. Es la idea más simple: cada símbolo es un tono de frecuencia fija. El símbolo cero, la frecuencia más baja; el veinte, veinte escalones más arriba; y así hasta el ciento veintisiete. En el plano de tiempo y frecuencia no hay rampas: hay líneas horizontales. El receptor es el mismo, una transformada y buscar el pico. Y sin eco las dos modulaciones empatan, porque en las dos las ondas son ortogonales y tienen la misma energía.

- «qué es la FSK» → `fsk`: la palabra «FSK»
- «un tono de frecuencia fija» → `tono`: un plano tiempo-frecuencia con una línea horizontal
- «El símbolo cero» → `s0`: la línea baja a la frecuencia 0, con «s = 0»
- «el veinte» → `s20`: la línea sube a la altura 20
- «hasta el ciento veintisiete» → `s127`: la línea sube hasta arriba del todo
- «no hay rampas» → `norampas`: al lado, el plano de LoRa con su rampa, con el rótulo «FSCM»
- «líneas horizontales» → `lineas`: la línea de la FSK se resalta
- «una transformada y buscar el pico» → `rx`: debajo, «FFT → Máximo»
- «las dos modulaciones empatan» → `empatan`: un «=» grande entre los dos planos
- «ortogonales» → `orto`: «Ortogonales»
- «la misma energía» → `ener`: «Misma energía»

<!-- b2 -->
Ahora el eco. Al receptor le llegan dos copias sumadas: la directa, con amplitud cero coma ocho nueve, y otra retrasada una muestra, con amplitud cero coma cuatro cinco. Si lo que se envía es un tono, la copia retrasada es el mismo tono, pero con la fase corrida. Y cuánto se corre depende de la frecuencia del tono.

- «dos copias sumadas» → `dos`: dos flechas que salen del mismo punto: una larga azul y una corta cian
- «cero coma ocho nueve» → `a1`: «0,89» junto a la larga
- «otra retrasada una muestra» → `retr`: la flecha corta aparece un instante después
- «cero coma cuatro cinco» → `a2`: «0,45» junto a la corta
- «un tono» → `tono`: «Tono»
- «con la fase corrida» → `fase`: la flecha corta gira un ángulo
- «depende de la frecuencia» → `depende`: «El giro depende de f»

<!-- b3 -->
Con un tono de frecuencia baja, en una muestra la fase casi no avanza: las dos flechas apuntan igual y se suman. Uno coma tres cuatro de amplitud, que al cuadrado es uno coma ocho de potencia. Con un tono en mitad de la banda, en una muestra la fase avanza media vuelta: la copia llega al revés y resta. Queda cero coma cuatro cinco de amplitud: cero coma dos de potencia. Nueve veces menos.

- «frecuencia baja» → `baja`: a la izquierda, el rótulo «f = 0»
- «la fase casi no avanza» → `casi`: la pareja de flechas, las dos hacia la derecha
- «apuntan igual y se suman» → `suman`: la flecha corta se pone a continuación de la larga
- «Uno coma tres cuatro» → `v134`: «0,89 + 0,45 = 1,34»
- «uno coma ocho de potencia» → `p18`: «Potencia: 1,8» en verde
- «en mitad de la banda» → `mitad`: a la derecha, el rótulo «f = B/2»
- «media vuelta» → `media`: otra pareja de flechas; la corta gira media vuelta
- «resta» → `resta`: la corta queda encima de la larga, hacia atrás
- «cero coma cuatro cinco de amplitud» → `v045`: «0,89 − 0,45 = 0,45»
- «cero coma dos de potencia» → `p02`: «Potencia: 0,2» en rojo
- «Nueve veces menos» → `nueve`: «÷ 9»

<!-- b4 -->
Si hacemos esa cuenta para todas las frecuencias, sale la respuesta del canal: una curva que vale uno coma ocho en los bordes de la banda y se hunde hasta cero coma dos en el centro. Por eso se llama selectivo en frecuencia: no trata igual a todas. Y aquí está el problema de la FSK. Cada símbolo vive en una sola frecuencia. Los de los bordes salen reforzados; los del centro pierden siete decibelios. En la simulación, con menos ocho decibelios, el símbolo cero no falla nunca y el sesenta y cuatro falla más de la mitad de las veces. Esos pocos símbolos con mala suerte arruinan la tasa de error.

- «todas las frecuencias» → `todas`: ejes: frecuencia de 0 a B y «Potencia que pasa»
- «la respuesta del canal» → `resp`: se traza la curva
- «uno coma ocho en los bordes» → `bordes`: «1,8» en los dos extremos
- «cero coma dos en el centro» → `centro`: «0,2» en el fondo del hueco
- «selectivo en frecuencia» → `selectivo`: «Selectivo en frecuencia»
- «no trata igual a todas» → `notrata`: la curva se resalta
- «Cada símbolo vive en una sola frecuencia» → `vive`: tallos verticales en los símbolos 0, 20, 64 y 100, cada uno hasta la curva
- «salen reforzados» → `reforz`: el tallo del símbolo 0 en verde
- «pierden siete decibelios» → `siete`: el tallo del símbolo 64 en rojo y «−7 dB»
- «con menos ocho decibelios» → `m8`: «SNR = −8 dB»
- «el símbolo cero no falla nunca» → `nunca`: «s = 0: falla 0 %»
- «falla más de la mitad» → `mas`: «s = 64: falla 58 %»
- «mala suerte» → `suerte`: el tallo del 64 se resalta

<!-- b5 -->
El chirp de LoRa hace lo contrario: cada símbolo recorre toda la banda. Pasa por la zona buena y por la mala, sea cual sea el dato. Al deshacer el chirp, la copia directa cae en la casilla del símbolo, con cero coma ocho de la potencia, y el eco cae en otra casilla, dos más abajo, con el cero coma dos restante. Todos los símbolos pierden lo mismo: un veinte por ciento, un decibelio. Ninguno tiene mala suerte.

- «recorre toda la banda» → `recorre`: los tallos salen y un punto ámbar recorre la curva de punta a punta
- «la zona buena y por la mala» → `zonas`: el punto vuelve a recorrerla
- «Al deshacer el chirp» → `des`: debajo, el eje de las casillas
- «la casilla del símbolo» → `c20`: un pico en la casilla 20
- «cero coma ocho de la potencia» → `p08`: «0,8» sobre ese pico
- «dos más abajo» → `c18`: un pico pequeño en la casilla 18
- «el cero coma dos restante» → `p02`: «0,2» sobre el pico pequeño
- «pierden lo mismo» → `mismo`: «Todos los símbolos: × 0,8»
- «un decibelio» → `undb`: «−1 dB»
- «Ninguno tiene mala suerte» → `ninguno`: una tilde verde

<!-- b6 -->
Esa es la razón teórica: la FSK pone cada símbolo en una frecuencia y queda a merced del canal en ese punto; el chirp reparte cada símbolo por todas, y el canal solo le quita el promedio. Las curvas lo confirman: con eco, para un error de uno en mil, la FSK necesita unos tres decibelios más.

- «la razón teórica» → `razon`: plano nuevo, vacío
- «cada símbolo en una frecuencia» → `una`: «FSK: una frecuencia por símbolo»
- «a merced del canal» → `merced`: debajo, «Depende de dónde caiga»
- «reparte cada símbolo por todas» → `reparte`: «FSCM: toda la banda»
- «el promedio» → `promedio`: debajo, «Solo pierde el promedio»
- «Las curvas lo confirman» → `curvas`: ejes «SNR (dB)» y «BER»; la curva de FSCM con eco en cian y la de FSK con eco en magenta
- «uno en mil» → `mil`: una línea horizontal de trazos en 10⁻³
- «tres decibelios más» → `tres`: una cota «≈ 3 dB» entre las dos curvas

---

# Escena 17 — ElDialDelFactor

**Capítulo YouTube:** El factor de ensanchamiento como dial
**Objetivo:** subir el SF en uno da un bit más por símbolo, el doble de duración y 3 dB más de ganancia: la velocidad casi se parte por la mitad y la señal mínima baja casi 3 dB. Es el dial para cambiar velocidad por alcance.

## Narración

<!-- b1 -->
Volvamos al factor de ensanchamiento, porque es el dial con el que LoRa se adapta a cada enlace. Sube el factor en uno y pasan tres cosas. El símbolo lleva un bit más. Pero dura el doble de muestras: el doble de tiempo en el aire. Y la transformada tiene el doble de casillas, así que la señal se concentra el doble frente al ruido: tres decibelios más de ganancia.

- «el dial» → `dial`: un dial semicircular con las marcas 7 a 12 y una aguja en el 7
- «Sube el factor en uno» → `sube`: la aguja pasa del 7 al 8
- «un bit más» → `bit`: «Bits por símbolo: 7 → 8»
- «el doble de muestras» → `muestras`: «Muestras: 128 → 256»
- «el doble de tiempo en el aire» → `tiempo`: «Duración: 1,02 → 2,05 ms»
- «el doble de casillas» → `casillas`: «Casillas: 128 → 256»
- «tres decibelios más de ganancia» → `db3`: «Ganancia: 21 → 24 dB», en verde

<!-- b2 -->
Veamos primero la velocidad. Los bits por segundo son los bits de cada símbolo divididos por lo que dura el símbolo. Con factor siete: siete bits cada milisegundo, unos seis mil ochocientos bits por segundo. Con factor ocho, ocho bits pero en el doble de tiempo: tres mil novecientos. Cada paso casi parte la velocidad por la mitad. Con factor doce quedan trescientos sesenta y seis bits por segundo: diecinueve veces más lento.

- «la velocidad» → `vel`: la palabra «Velocidad»
- «los bits de cada símbolo divididos por lo que dura» → `formula`: «R_b = SF / T_s = SF · B / 2^SF»
- «Con factor siete» → `f7`: el rótulo «SF 7»
- «seis mil ochocientos» → `v7`: una barra larga: «6.836 bit/s»
- «Con factor ocho» → `f8`: el rótulo «SF 8»
- «tres mil novecientos» → `v8`: una barra de algo más de la mitad: «3.906»
- «casi parte la velocidad por la mitad» → `mitad`: las barras de SF 9, 10 y 11: 2.197, 1.221 y 671
- «Con factor doce» → `f12`: el rótulo «SF 12»
- «trescientos sesenta y seis» → `v12`: una barra mínima: «366 bit/s»
- «diecinueve veces más lento» → `x19`: «÷ 19»

<!-- b3 -->
Ahora la otra cara. ¿Cuánta señal hace falta para equivocarse solo en un bit de cada mil? Con factor siete, la señal puede estar ocho decibelios por debajo del ruido. Con cada paso, casi tres decibelios más abajo. Con factor doce, veintidós decibelios por debajo del ruido: ciento sesenta veces menos potencia que el ruido, y sigue funcionando. No son exactamente tres por paso, porque al haber más casillas también hay más sitios donde el ruido puede ganar.

- «la otra cara» → `otra`: ejes: «SF» de 7 a 12 y «SNR mínimo (dB)»
- «un bit de cada mil» → `mil`: «BER = 10⁻³»
- «Con factor siete» → `s7`: un punto en SF 7
- «ocho decibelios por debajo» → `d8`: «−8,2 dB»
- «casi tres decibelios más abajo» → `paso`: los puntos de SF 8 a 11, cada uno más abajo
- «Con factor doce» → `s12`: el punto de SF 12
- «veintidós decibelios» → `d22`: «−22,1 dB»
- «ciento sesenta veces menos potencia» → `x160`: «Señal = Ruido ÷ 160»
- «No son exactamente tres» → `notres`: una cota entre dos puntos vecinos
- «más sitios donde el ruido puede ganar» → `sitios`: «≈ 2,8 dB por paso»

<!-- b4 -->
¿Y qué se hace con esos decibelios? Distancia. Al alejarse, la señal se debilita: en espacio libre, seis decibelios cada vez que se duplica la distancia. Los catorce decibelios que separan el factor siete del doce son unas cinco veces más alcance. O la misma distancia con más ruido, con paredes de por medio o con menos potencia de transmisión.

- «Distancia» → `dist`: la palabra «Distancia»
- «la señal se debilita» → `debil`: una onda que sale de una antena y se va apagando
- «seis decibelios» → `seis`: «Distancia × 2 → −6 dB»
- «catorce decibelios» → `catorce`: «SF 7 → SF 12: 14 dB»
- «cinco veces más alcance» → `cinco`: dos barras de alcance: la de SF 12, cinco veces más larga, y «× 5»
- «más ruido» → `ruido`: «Más ruido»
- «paredes de por medio» → `paredes`: «Paredes»
- «menos potencia de transmisión» → `potencia`: «Menos potencia»

<!-- b5 -->
Por eso es un dial. Cerca de la antena o con poco ruido, factor bajo: rápido, poco tiempo en el aire y poca batería. Lejos o con mucho ruido, factor alto: lento, pero llega. Cada transmisor elige el punto justo, y el precio siempre es el mismo: tiempo.

- «un dial» → `dial`: el dial otra vez, en el centro
- «Cerca de la antena» → `cerca`: a la izquierda, «Cerca · Poco ruido»
- «factor bajo» → `bajo`: la aguja va al 7
- «rápido» → `rapido`: «Rápido»
- «poca batería» → `bateria`: «Poca batería»
- «Lejos o con mucho ruido» → `lejos`: a la derecha, «Lejos · Mucho ruido»
- «factor alto» → `alto`: la aguja va al 12
- «lento, pero llega» → `llega`: «Lento, pero llega»
- «el punto justo» → `justo`: la aguja se queda en un punto intermedio
- «tiempo» → `tiempo`: «El precio: tiempo»

---

# Escena 18 — EncontrarLaTrama

**Capítulo YouTube:** ¿Dónde empieza la trama?
**Objetivo:** el preámbulo y el detector por correlación con el preámbulo completo (filtro adaptado). El umbral se desarrolla en las tres escenas siguientes.

## Narración

<!-- b1 -->
Todo esto supone que el receptor sabe dónde empieza cada símbolo. En la práctica no lo sabe: escucha ruido y, de pronto, llega una trama. Para eso cada trama empieza con un preámbulo: ocho chirps del símbolo cero, seguidos de dos y cuarto que bajan. Después va la carga con los datos.

- «dónde empieza cada símbolo» → `donde`: una tira larga tiempo-frecuencia, vacía, con un «?»
- «escucha ruido» → `ruido`: la parte izquierda de la tira se llena de puntos de ruido
- «llega una trama» → `trama`: una llave «Trama» sobre el resto de la tira
- «un preámbulo» → `pre`: el rótulo «Preámbulo»
- «ocho chirps del símbolo cero» → `ocho`: ocho rampas iguales seguidas
- «dos y cuarto que bajan» → `bajan`: dos rampas y cuarto que bajan, en cian
- «la carga con los datos» → `carga`: rampas desplazadas, cada una distinta, y el rótulo «Datos»

<!-- b2 -->
El detector del cuaderno desliza los ocho chirps del preámbulo sobre lo recibido, muestra a muestra, y mide el parecido. Es un filtro adaptado: detectar una señal conocida en ruido. Donde el preámbulo encaja, el parecido se dispara. Ese máximo dice a la vez que hay trama y en qué muestra empieza.

- «desliza los ocho chirps» → `desliza`: un marco ámbar del ancho de ocho chirps entra por la izquierda de la tira
- «muestra a muestra» → `mam`: el marco avanza hacia la derecha
- «mide el parecido» → `parecido`: debajo, una curva T[k] se va trazando a medida que el marco avanza
- «un filtro adaptado» → `adaptado`: «Filtro adaptado»
- «una señal conocida en ruido» → `conocida`: «Señal conocida + Ruido»
- «Donde el preámbulo encaja» → `encaja`: el marco sigue avanzando hacia el preámbulo
- «el parecido se dispara» → `dispara`: el marco llega al preámbulo y la curva sube en un pico
- «hay trama» → `hay`: una tilde junto al pico
- «en qué muestra empieza» → `empieza`: una línea vertical une el pico con el inicio de la trama

<!-- b3 -->
Pero el ruido también produce parecido. ¿Cuánto hace falta para decir que sí hay trama? Esa decisión merece ir despacio.

- «el ruido también produce parecido» → `ruidop`: la plantilla sigue avanzando y la curva baja por el otro lado del pico
- «¿Cuánto hace falta» → `cuanto`: un «?» grande junto a la curva
- «ir despacio» → `despacio`: «Sí / No»

---

# Escena 19 — DosManerasDeEquivocarse

**Capítulo YouTube:** Neyman-Pearson: dos maneras de equivocarse
**Objetivo:** las dos hipótesis, cómo se reparte el parecido con solo ruido (exponencial de media 8σ²) y con trama, el umbral, la falsa alarma y la pérdida como áreas, y qué fija el criterio de Neyman-Pearson.

## Narración

<!-- b1 -->
En cada posición, el detector tiene que contestar una pregunta de sí o no. Hipótesis cero: aquí solo hay ruido. Hipótesis uno: aquí empieza un preámbulo. Y solo tiene un número para decidir: el parecido.

- «una pregunta de sí o no» → `pregunta`: «¿Hay trama?»
- «Hipótesis cero» → `h0`: la casilla «H₀ · Solo ruido», en magenta
- «Hipótesis uno» → `h1`: la casilla «H₁ · Empieza un preámbulo», en azul
- «un número para decidir» → `numero`: «T» grande, en ámbar

<!-- b2 -->
Cuando solo hay ruido, el parecido no vale cero: vale algo al azar, distinto cada vez. Si anotamos miles de valores y los apilamos, aparece su forma: casi siempre son pequeños, y muy de vez en cuando sale uno grande. Es una distribución exponencial, y su media es ocho veces la potencia del ruido, porque la plantilla tiene ocho chirps de energía uno.

- «no vale cero» → `nocero`: un eje horizontal «T» con el 0 a la izquierda
- «algo al azar» → `azar`: caen puntos magenta sobre el eje, en sitios distintos
- «miles de valores» → `miles`: los puntos se convierten en un histograma
- «casi siempre son pequeños» → `peq`: las barras altas de la izquierda se resaltan
- «uno grande» → `grande`: una flecha señala la cola, a la derecha
- «una distribución exponencial» → `expo`: la curva exponencial sobre el histograma
- «su media» → `media`: una marca en el eje: «Media = 8σ²»
- «ocho veces la potencia del ruido» → `ochoveces`: el «8σ²» se resalta
- «ocho chirps de energía uno» → `ocho`: ocho rampas pequeñas

<!-- b3 -->
Cuando sí hay un preámbulo, el parecido es mucho mayor, pero tampoco es fijo: el ruido puede sumarle o restarle. Con menos veinte decibelios queda repartido alrededor de veinte veces la media del ruido. Las dos formas se solapan, y por eso no hay decisión perfecta.

- «sí hay un preámbulo» → `h1`: una segunda forma, azul, más a la derecha
- «tampoco es fijo» → `nofijo`: la forma azul tiembla a izquierda y derecha
- «sumarle o restarle» → `sumres`: dos flechas, a izquierda y a derecha, sobre la forma azul
- «menos veinte decibelios» → `m20`: «SNR = −20 dB»
- «veinte veces la media» → `veinte`: la marca «20» en el eje
- «se solapan» → `solapan`: la zona donde se cruzan las dos formas se resalta
- «no hay decisión perfecta» → `noperf`: «Sin decisión perfecta»

<!-- b4 -->
La regla es un umbral: si el parecido lo supera, decimos que hay trama. Y hay dos maneras de equivocarse. Falsa alarma: solo había ruido, pero superó el umbral. Es el área de la cola del ruido a la derecha. Pérdida: había trama, pero el parecido quedó por debajo. Es el área de la otra forma a la izquierda. Si subes el umbral, hay menos falsas alarmas y más pérdidas. Si lo bajas, al revés. No se pueden bajar las dos a la vez.

- «un umbral» → `umbral`: una línea vertical con «η»
- «decimos que hay trama» → `decimos`: «T > η → Hay trama»
- «dos maneras de equivocarse» → `dos`: dos rótulos vacíos, arriba
- «Falsa alarma» → `fa`: «Falsa alarma», en rojo
- «el área de la cola» → `cola`: el área de la forma del ruido a la derecha del umbral, en rojo
- «Pérdida» → `perdida`: «Pérdida», en ámbar
- «quedó por debajo» → `debajo`: el área de la forma azul a la izquierda del umbral, en ámbar
- «Si subes el umbral» → `subes`: el umbral se mueve a la derecha: el área roja se encoge y la ámbar crece
- «Si lo bajas» → `bajas`: el umbral se mueve a la izquierda: al revés
- «No se pueden bajar las dos» → `nodos`: «Una baja, la otra sube»

<!-- b5 -->
El criterio de Neyman-Pearson resuelve el dilema así: primero se decide cuántas falsas alarmas se toleran, y se pone el umbral justo donde la cola del ruido vale eso. Con ese precio fijado, este detector da la menor cantidad posible de pérdidas.

- «Neyman-Pearson» → `np`: «Neyman-Pearson»
- «cuántas falsas alarmas se toleran» → `tolera`: «1.º Fijar la falsa alarma»
- «justo donde la cola del ruido vale eso» → `justo`: el umbral se coloca y el área roja queda marcada
- «Con ese precio fijado» → `precio`: el área roja se resalta
- «la menor cantidad posible de pérdidas» → `menor`: «2.º Pérdidas: las mínimas»

---

# Escena 20 — CuantasFalsasAlarmas

**Capítulo YouTube:** Qué significa una falsa alarma por minuto
**Objetivo:** de una tolerancia en tiempo (una falsa alarma por minuto escuchando solo ruido) a una probabilidad por prueba (1 de cada 7,5 millones) y de ahí al umbral: η = −8σ² ln P_FA, unas 16 veces la media.

## Narración

<!-- b1 -->
¿Y cuántas tolerar? Una probabilidad suelta no dice mucho; es más fácil pensarlo en tiempo. El detector hace una prueba por cada muestra que llega. Con ciento veinticinco kilohercios, son ciento veinticinco mil pruebas por segundo: siete millones y medio por minuto.

- «cuántas tolerar» → `cuantas`: «P_FA = ?»
- «no dice mucho» → `nodice`: un «?» más
- «pensarlo en tiempo» → `tiempo`: un reloj
- «una prueba por cada muestra» → `prueba`: una fila de puntos, cada uno con un «?» encima
- «ciento veinticinco kilohercios» → `khz`: «B = 125 kHz»
- «ciento veinticinco mil pruebas por segundo» → `seg`: «125.000 pruebas / s»
- «siete millones y medio por minuto» → `min`: «× 60 = 7.500.000 / min»

<!-- b2 -->
Imagina el receptor escuchando solo ruido. Si aceptamos que se equivoque, de media, una vez por minuto, cada prueba puede fallar una vez de cada siete millones y medio. Esa es la probabilidad de falsa alarma: uno coma tres por diez a la menos siete.

- «escuchando solo ruido» → `solo`: una traza de ruido
- «que se equivoque» → `equivoque`: un punto rojo sobre la traza
- «una vez por minuto» → `una`: «1 falsa alarma por minuto»
- «una vez de cada siete millones y medio» → `frac`: la fracción «1 / 7.500.000»
- «la probabilidad de falsa alarma» → `prob`: «P_FA =»
- «uno coma tres por diez a la menos siete» → `pfa`: «P_FA = 1,3 · 10⁻⁷»

<!-- b3 -->
¿Por qué no pedir cero? Porque la cola del ruido nunca llega a cero: para no tener ninguna falsa alarma habría que subir el umbral hasta perder también las tramas. Y cada falsa alarma tiene un coste: el receptor cree que empieza una trama, se pone a demodular ruido y, mientras tanto, se le puede pasar una de verdad. Una por minuto es la tolerancia que eligió el cuaderno; es una decisión de diseño.

- «pedir cero» → `cero`: «P_FA = 0», tachado
- «nunca llega a cero» → `cola`: la cola de la exponencial, que se acerca al eje sin tocarlo
- «ninguna falsa alarma» → `ninguna`: el área de la cola se resalta
- «perder también las tramas» → `perder`: el umbral se va a la derecha del todo
- «un coste» → `coste`: «Coste»
- «demodular ruido» → `demod`: una caja «Demodulador» de la que salen números sin sentido
- «una de verdad» → `verdad`: una trama pasa por debajo sin que nadie la marque
- «la tolerancia que eligió el cuaderno» → `eligio`: «1 por minuto»
- «decisión de diseño» → `diseno`: «Decisión de diseño»

<!-- b4 -->
Falta convertir esa probabilidad en un umbral. Para la exponencial, la cola es fácil: la probabilidad de superar un valor es e elevado a menos ese valor dividido por la media. La igualamos a la probabilidad tolerada, despejamos, y sale el umbral: menos la media por el logaritmo de la probabilidad. Con nuestros números, el logaritmo vale menos quince coma ocho. El umbral queda dieciséis veces por encima del parecido medio del ruido.

- «convertir esa probabilidad en un umbral» → `convertir`: «P_FA → η»
- «la cola es fácil» → `cola`: la exponencial con el área de la cola en rojo y el umbral «η»
- «e elevado a menos ese valor dividido por la media» → `formula`: «P(T > η | H₀) = e^(−η / 8σ²)»
- «La igualamos» → `iguala`: «= P_FA»
- «despejamos» → `despeja`: una flecha hacia abajo
- «menos la media por el logaritmo» → `eta`: «η = −8σ² · ln P_FA»
- «Con nuestros números» → `numeros`: «P_FA = 1,3 · 10⁻⁷»
- «menos quince coma ocho» → `ln`: «ln(1,3 · 10⁻⁷) = −15,8»
- «dieciséis veces» → `dieciseis`: «η ≈ 16 × Media»

---

# Escena 21 — ElUmbralEnAccion

**Capítulo YouTube:** El umbral, en acción
**Objetivo:** sobre la curva T[k]: los bultos de ruido bajo el umbral no son falsas alarmas; el cruce y la subida al máximo; qué pasa con el umbral demasiado bajo (falsas alarmas en puro ruido) y demasiado alto (pérdida).

## Narración

<!-- b1 -->
Volvamos a la curva del parecido, ahora con el umbral dibujado. Fíjate en los bultos del ruido: suben y bajan, pero no llegan al umbral. No son falsas alarmas: el detector los ignora. Solo cuando llega el preámbulo la curva cruza el umbral, y ahí se declara la trama.

- «la curva del parecido» → `curva`: la trama arriba y la curva T[k] debajo, entera
- «el umbral dibujado» → `umbral`: la línea horizontal «η», de trazos
- «los bultos del ruido» → `bultos`: una llave bajo el tramo de solo ruido
- «no llegan al umbral» → `nollegan`: una cota vertical entre el bulto más alto y el umbral
- «No son falsas alarmas» → `nofa`: «No son falsas alarmas»
- «los ignora» → `ignora`: el tramo de ruido se atenúa
- «cruza el umbral» → `cruza`: un punto verde donde la curva cruza la línea
- «se declara la trama» → `declara`: «Trama»

<!-- b2 -->
Un detalle: el parecido no salta de golpe. Va creciendo a medida que la plantilla cubre más chirps del preámbulo, y cruza el umbral un poco antes del inicio, cuando ya cubre casi todos. Por eso el detector no se queda con el cruce: desde ahí busca el máximo en los ocho símbolos siguientes. Ese máximo es el inicio.

- «Va creciendo» → `crece`: una línea de trazos sigue la subida de los picos hasta el máximo
- «cubre más chirps del preámbulo» → `cubre`: sobre la trama, la plantilla de ocho chirps, puesta unos símbolos antes del inicio
- «cruza el umbral» → `cruce`: el punto verde del cruce se resalta
- «un poco antes del inicio» → `antes`: una línea vertical marca el inicio verdadero, algo a la derecha
- «cuando ya cubre casi todos» → `casi`: la plantilla avanza hasta la posición del cruce
- «no se queda con el cruce» → `noqueda`: el punto verde se atenúa
- «busca el máximo» → `busca`: una flecha trepa desde el cruce hasta el pico
- «los ocho símbolos siguientes» → `ocho`: una franja de ocho símbolos de ancho a partir del cruce
- «Ese máximo es el inicio» → `inicio`: un punto ámbar en el pico, sobre la línea del inicio

<!-- b3 -->
¿Qué sería entonces una falsa alarma? Bajemos el umbral, como si toleráramos muchas. Ahora un bulto de puro ruido lo cruza, lejos de cualquier trama. El detector declara una trama donde no la hay y se pone a demodular ruido. Con el umbral bien puesto, eso pasa una vez por minuto; con este, a cada rato.

- «una falsa alarma» → `pregunta`: «¿Falsa alarma?»
- «Bajemos el umbral» → `bajemos`: la línea del umbral baja
- «un bulto de puro ruido lo cruza» → `cruza`: un círculo rojo en el bulto que ahora supera la línea
- «lejos de cualquier trama» → `lejos`: una cota desde ese bulto hasta el inicio de la trama
- «donde no la hay» → `nohay`: «Falsa alarma», en rojo
- «demodular ruido» → `demod`: salen números sin sentido: «201 · 37 · 5»
- «una vez por minuto» → `minuto`: «Bien puesto: 1 por minuto»
- «a cada rato» → `rato`: más círculos rojos en otros bultos que también cruzan

<!-- b4 -->
Y si lo subimos demasiado, ni el pico del preámbulo llega: la trama pasa y nadie la ve. Eso es una pérdida. El umbral de Neyman-Pearson está entre los dos extremos, en el punto exacto que fija la tolerancia.

- «lo subimos demasiado» → `subimos`: lo rojo sale y la línea sube por encima del pico
- «ni el pico del preámbulo llega» → `nollega`: una cota entre el pico y la línea
- «una pérdida» → `perdida`: «Pérdida», en ámbar
- «entre los dos extremos» → `entre`: la línea vuelve a su sitio
- «la tolerancia» → `tol`: «1 falsa alarma por minuto»

---

# Escena 22 — CuantoCuestaLaPlantilla

**Capítulo YouTube:** Cuánto cuesta alargar la plantilla
**Objetivo:** el tiempo y la memoria de la correlación crecen en proporción al largo de la plantilla; lo que se gana (3 dB por cada duplicación), la ambigüedad de las plantillas cortas y los dos atajos del cuaderno.

## Narración

<!-- b1 -->
¿Y por qué ocho chirps y no uno, o los diez y cuarto del preámbulo entero? Veamos el coste. Calcular el parecido en una posición es multiplicar cada muestra de la plantilla por una muestra recibida y sumar. Con un chirp de factor ocho son doscientas cincuenta y seis multiplicaciones. Con ocho chirps, dos mil cuarenta y ocho. Con el preámbulo entero, dos mil seiscientas veinticuatro. Y eso, por cada muestra que llega: a ciento veinticinco mil por segundo, la plantilla de ocho son doscientos cincuenta y seis millones de multiplicaciones cada segundo.

- «ocho chirps y no uno» → `pregunta`: tres plantillas dibujadas: de 1 chirp, de 8 y de 10,25
- «los diez y cuarto del preámbulo entero» → `entero`: la plantilla de 10,25 se resalta
- «el coste» → `coste`: la palabra «Coste»
- «multiplicar cada muestra de la plantilla» → `mult`: dos filas de puntos, plantilla y recibido, unidas por «×»
- «sumar» → `suma`: un «Σ» a la derecha
- «doscientas cincuenta y seis multiplicaciones» → `n256`: una barra corta: «1 chirp: 256»
- «dos mil cuarenta y ocho» → `n2048`: una barra ocho veces más larga: «8 chirps: 2.048»
- «dos mil seiscientas veinticuatro» → `n2624`: la barra más larga: «10,25 chirps: 2.624»
- «por cada muestra que llega» → `cada`: «× cada muestra»
- «ciento veinticinco mil por segundo» → `seg`: «× 125.000 por segundo»
- «doscientos cincuenta y seis millones» → `millones`: «256.000.000 por segundo»
- «cada segundo» → `cadaseg`: la cifra se resalta

<!-- b2 -->
El tiempo crece en proporción al largo de la plantilla: el doble de chirps, el doble de cuentas. Y la memoria también: hay que guardar la plantilla y las últimas muestras recibidas, tantas como mide. Ocho chirps de factor ocho son dos mil muestras; con factor doce, treinta y dos mil.

- «en proporción al largo» → `prop`: «Tiempo ∝ Largo»
- «el doble de chirps, el doble de cuentas» → `doble`: «× 2 → × 2»
- «la memoria también» → `mem`: «Memoria ∝ Largo»
- «las últimas muestras recibidas» → `ultimas`: una tira de casillas que se desplaza
- «tantas como mide» → `tantas`: la tira y la plantilla, del mismo largo
- «dos mil muestras» → `dosmil`: «SF 8: 2.048 muestras»
- «treinta y dos mil» → `tmil`: «SF 12: 32.768 muestras»

<!-- b3 -->
¿Qué se compra con ese gasto? Sensibilidad. Los chirps de la plantilla se suman en fase: con ocho, la señal crece ocho veces en amplitud, sesenta y cuatro en energía, mientras que el ruido solo crece ocho. Ganancia: ocho, nueve decibelios. Cada vez que se duplica la plantilla se ganan tres decibelios y se paga el doble. Los dos chirps y cuarto que bajan añaden un decibelio más.

- «Sensibilidad» → `sens`: la palabra «Sensibilidad»
- «se suman en fase» → `fase`: ocho flechas en fila, todas hacia la derecha
- «ocho veces en amplitud» → `amp8`: una cota bajo las flechas: «8»
- «sesenta y cuatro en energía» → `e64`: «Señal: 8² = 64»
- «el ruido solo crece ocho» → `r8`: «Ruido: 8»
- «nueve decibelios» → `db9`: «64 / 8 = 8 → 9 dB»
- «tres decibelios» → `tres`: una tabla: 1 → 0 dB, 2 → 3 dB, 4 → 6 dB, 8 → 9 dB
- «se paga el doble» → `doble`: «Coste × 2» bajo la tabla
- «un decibelio más» → `uno`: la fila «10,25 → 10,1 dB»

<!-- b4 -->
La simulación lo muestra: la probabilidad de detectar la trama, según el nivel de señal, para plantillas de uno, dos, cuatro y ocho chirps, y para el preámbulo entero. Cada curva queda a la izquierda de la anterior: detecta con menos señal.

- «La simulación lo muestra» → `sim`: ejes «SNR (dB)» y «Probabilidad de detectar»
- «la probabilidad de detectar la trama» → `prob`: el rótulo del eje vertical se resalta
- «según el nivel de señal» → `nivel`: el rótulo del eje horizontal se resalta
- «uno» → `c1`: la curva de 1 chirp
- «dos» → `c2`: la de 2
- «cuatro» → `c4`: la de 4
- «ocho chirps» → `c8`: la de 8, en ámbar
- «el preámbulo entero» → `c10`: la de 10,25, en verde
- «a la izquierda de la anterior» → `izq`: una flecha hacia la izquierda
- «con menos señal» → `menos`: «Menos señal»

<!-- b5 -->
Pero hay una sorpresa. Con una plantilla corta, el detector sabe que hay trama y no sabe dónde empieza. El preámbulo son ocho chirps iguales: un solo chirp encaja igual de bien en cualquiera de ellos. En la simulación, con señal de sobra, la plantilla de un chirp acierta la muestra exacta solo la mitad de las veces. Hace falta la plantilla de ocho para que haya un único punto donde encaja entera.

- «una sorpresa» → `sorpresa`: «!»
- «sabe que hay trama» → `sabe`: «¿Hay trama?» con una tilde verde
- «no sabe dónde empieza» → `nosabe`: «¿Dónde empieza?» con un «?»
- «ocho chirps iguales» → `iguales`: la tira del preámbulo, con sus ocho rampas
- «encaja igual de bien en cualquiera» → `cualquiera`: un marco de un chirp salta de rampa en rampa
- «con señal de sobra» → `sobra`: «SNR = −8 dB»
- «la plantilla de un chirp» → `unchirp`: el marco pequeño se resalta
- «solo la mitad de las veces» → `mitad`: «1 chirp: acierta el 54 %»
- «la plantilla de ocho» → `ocho`: un marco de ocho chirps cubre el preámbulo
- «un único punto» → `unico`: «8 chirps: acierta el 100 %»

<!-- b6 -->
El cuaderno usa dos atajos para no pagar todo ese coste. Uno: calcular la correlación de toda la grabación de una vez con transformadas rápidas. Así el tiempo casi no depende del largo de la plantilla, pero hay que tener la grabación entera en memoria. Dos: como el preámbulo repite el mismo chirp, basta correlar con un solo chirp y sumar ocho resultados separados un símbolo. Esa idea lleva a los otros dos detectores.

- «dos atajos» → `atajos`: «1» y «2»
- «toda la grabación de una vez» → `toda`: una tira larga, entera
- «con transformadas rápidas» → `fft`: junto al «1», «Correlación por FFT»
- «casi no depende del largo» → `nodep`: barras de tiempo medido: la directa crece de 1,1 a 10,3 ms; la de FFT se queda en 0,5 ms
- «la grabación entera en memoria» → `entera`: «Necesita toda la grabación»
- «el mismo chirp» → `mismo`: junto al «2», una rampa
- «correlar con un solo chirp» → `uno`: «256»
- «sumar ocho resultados» → `sumar`: «+ 8 sumas»
- «los otros dos detectores» → `otros`: una flecha hacia «Detectores 2 y 3»

---

# Escena 23 — TresDetectores

**Capítulo YouTube:** Los tres detectores, por dentro
**Objetivo:** cómo decide cada detector del cuaderno (suma coherente, suma no coherente, demodular y contar), de dónde sale el umbral de cada uno y cómo quedan en tramas perdidas y en coste.

## Narración

<!-- b1 -->
El cuaderno compara tres detectores. El primero ya lo conocemos: correlación con el preámbulo completo. Por dentro son ocho correlaciones, una por chirp. Cada una es una flecha. Como los chirps llegan en fase, las ocho flechas apuntan igual: se suman, y al final se mide el largo. Ocho de largo, sesenta y cuatro al cuadrado. Sumar primero y medir después se llama integración coherente.

- «tres detectores» → `tres`: tres números, 1, 2 y 3, arriba
- «correlación con el preámbulo completo» → `full`: «1 · Preámbulo completo» en ámbar
- «ocho correlaciones» → `ocho`: ocho rampas en fila
- «Cada una es una flecha» → `flecha`: bajo cada rampa, una flecha pequeña
- «llegan en fase» → `enfase`: las flechas se resaltan, todas con el mismo ángulo
- «apuntan igual» → `igual`: las ocho flechas se ponen una detrás de otra, en línea recta
- «se mide el largo» → `largo`: una cota bajo la fila: «8»
- «sesenta y cuatro al cuadrado» → `v64`: «T = 8² = 64»
- «Sumar primero y medir después» → `sumarprimero`: «Σ → | |²»
- «integración coherente» → `coh`: «Coherente: sumar y después medir»

<!-- b2 -->
El segundo, la búsqueda de ocho picos, cambia el orden: primero mide el largo de cada flecha, lo eleva al cuadrado, y después suma. Ocho veces uno: ocho. La señal ya no se multiplica por sesenta y cuatro, pero tiene una ventaja: no necesita que la fase se mantenga durante ocho símbolos. Si el oscilador deriva y las flechas giran un poco entre chirp y chirp, la suma coherente se encoge; esta no. Es integración no coherente.

- «la búsqueda de ocho picos» → `picos`: «2 · Ocho picos» en cian
- «cambia el orden» → `orden`: «Medir y después sumar»
- «el largo de cada flecha» → `cada`: ocho flechas sueltas, cada una con «1²» debajo
- «después suma» → `suma`: signos «+» entre ellas
- «Ocho veces uno» → `v8`: «S = 8 × 1 = 8»
- «ya no se multiplica por sesenta y cuatro» → `no64`: «64», tachado
- «una ventaja» → `ventaja`: «Ventaja»
- «no necesita que la fase se mantenga» → `nofase`: «No depende de la fase»
- «Si el oscilador deriva» → `deriva`: un oscilador pequeño
- «las flechas giran un poco» → `giran`: cada flecha gira un poco más que la anterior
- «la suma coherente se encoge» → `encoge`: encadenadas, las flechas se curvan y la suma queda corta, en rojo
- «esta no» → `estano`: «S sigue valiendo 8» en verde
- «integración no coherente» → `nocoh`: «No coherente»

<!-- b3 -->
Su umbral también sale de Neyman-Pearson, pero el ruido ahora es la suma de ocho exponenciales, una distribución gamma, y su cola no se despeja con una fórmula: el cuaderno la busca probando valores, por bisección. Sale unas cuatro veces la media del ruido.

- «también sale de Neyman-Pearson» → `np`: «Mismo criterio, misma tolerancia»
- «la suma de ocho exponenciales» → `suma8`: ocho exponenciales pequeñas en fila
- «una distribución gamma» → `gamma`: una curva con joroba, en magenta
- «no se despeja con una fórmula» → `nodesp`: «η = ?»
- «probando valores» → `probando`: marcas que caen sobre el eje
- «por bisección» → `bisec`: sobre el eje, un intervalo que se parte por la mitad tres veces
- «cuatro veces la media» → `cuatro`: «η ≈ 4 × Media»

<!-- b4 -->
El tercero trabaja en frecuencia. Corta lo recibido en ventanas de un símbolo y demodula cada una, como si fueran datos: deshacer el chirp, transformada, casilla del máximo. Un chirp del preámbulo es el símbolo cero, así que durante el preámbulo salen ceros seguidos. El detector cuenta cuántos ceros hay en ocho ventanas.

- «trabaja en frecuencia» → `frec`: «3 · Demodular y contar» en magenta
- «ventanas de un símbolo» → `ventanas`: una tira partida en ventanas: ruido y después las ocho rampas
- «demodula cada una» → `demod`: bajo la tira, «× Chirp que baja → FFT → Máximo»
- «deshacer el chirp» → `des`: la primera caja de la cadena se resalta
- «casilla del máximo» → `casilla`: un número bajo cada ventana; en el ruido, cualquiera: 137, 52, 201
- «Un chirp del preámbulo es el símbolo cero» → `simb0`: «Rampa = símbolo 0»
- «ceros seguidos» → `ceros`: bajo las ocho rampas, ocho ceros en ámbar
- «cuenta cuántos ceros» → `cuenta`: «V = 8 ceros»

<!-- b5 -->
¿Y su umbral? Con solo ruido, el máximo cae en cualquiera de las doscientas cincuenta y seis casillas: sale cero una vez de cada doscientas cincuenta y seis. Que salgan dos ceros en ocho ventanas por casualidad pasa demasiado a menudo para nuestra tolerancia; que salgan tres, tres veces en un millón. El umbral es tres ceros de ocho. Es el más barato: una transformada por símbolo en vez de una correlación por muestra. Pero al quedarse solo con la casilla ganadora tira información.

- «Con solo ruido» → `ruido`: «Solo ruido»
- «cualquiera de las doscientas cincuenta y seis casillas» → `cualq`: unas casillas con el máximo saltando de una a otra
- «una vez de cada doscientas cincuenta y seis» → `p256`: «P(cero) = 1 / 256»
- «dos ceros» → `dos`: «2 ceros o más: 4 · 10⁻⁴», con una cruz roja
- «demasiado a menudo» → `amenudo`: «Tolerancia: 3,4 · 10⁻⁵ por símbolo»
- «tres, tres veces en un millón» → `tres`: «3 ceros o más: 3 · 10⁻⁶», con una tilde verde
- «tres ceros de ocho» → `k3`: «Umbral: 3 de 8»
- «el más barato» → `barato`: «El más barato»
- «una transformada por símbolo» → `fft`: «1 FFT por símbolo»
- «una correlación por muestra» → `corr`: «en vez de 1 correlación por muestra»
- «la casilla ganadora» → `ganadora`: «Solo el máximo»
- «tira información» → `tira`: «Pierde información»

<!-- b6 -->
Midiendo las tramas perdidas, quedan en ese orden, con unos dos decibelios entre cada uno. Cuanta más información de la señal usa el detector, la fase, la amplitud, menos señal necesita; y más cuentas hace.

- «las tramas perdidas» → `fer`: ejes «SNR (dB)» y «FER»
- «en ese orden» → `orden`: las tres curvas, de izquierda a derecha: ámbar, cian y magenta
- «dos decibelios entre cada uno» → `db2`: dos cotas a la altura de FER = 0,5 y «≈ 2 dB cada salto»
- «Cuanta más información» → `info`: «Información usada»
- «la fase» → `fase`: a la izquierda, «1 · Fase y amplitud»
- «la amplitud» → `amp`: «2 · Solo amplitud» y «3 · Solo el máximo»
- «más cuentas hace» → `cuentas`: junto a cada uno, multiplicaciones por muestra: «≈ 2.048», «≈ 264» y «≈ 8»

---

# Escena 24 — LaRadioDefinidaPorSoftware

**Capítulo YouTube:** El Pluto: una radio hecha de muestras
**Objetivo:** qué es un SDR y cómo son por dentro los caminos de transmisión y de recepción del ADALM-Pluto.

## Narración

<!-- b1 -->
Hasta aquí todo era simulación. Para probarlo de verdad se usa una radio definida por software: una radio en la que la forma de la señal la decide el ordenador. El ordenador calcula las muestras, que son números complejos, y la radio las convierte en una onda. La del laboratorio es un Pluto, de Analog Devices.

- «todo era simulación» → `sim`: un ordenador
- «una radio definida por software» → `sdr`: las siglas «SDR»
- «la forma de la señal» → `forma`: una onda pequeña sobre el ordenador
- «la decide el ordenador» → `orden`: el ordenador se resalta
- «calcula las muestras» → `muestras`: del ordenador sale una fila de puntos
- «números complejos» → `complejos`: «I + jQ»
- «las convierte en una onda» → `onda`: los puntos llegan a una caja y sale una onda
- «un Pluto» → `pluto`: la caja pasa a ser el Pluto, con dos antenas, y el rótulo «ADALM-Pluto»

<!-- b2 -->
Por dentro tiene dos caminos. Para transmitir, cada muestra compleja son dos números, la parte real y la imaginaria. Un conversor los pasa a tensión, un filtro los suaviza y un mezclador los sube a la frecuencia de la portadora, aquí novecientos cinco megahercios. Un amplificador, y a la antena.

- «dos caminos» → `dos`: dos filas vacías, con los rótulos «TX» y «RX»
- «Para transmitir» → `tx`: la fila de arriba se resalta
- «la parte real y la imaginaria» → `iq`: a la izquierda, «I, Q»
- «Un conversor» → `dac`: la caja «DAC»
- «un filtro» → `filtro`: la caja «Filtro»
- «un mezclador» → `mez`: la caja «Mezclador»
- «la frecuencia de la portadora» → `porta`: debajo del mezclador, un oscilador «OL»
- «novecientos cinco megahercios» → `mhz`: «905 MHz»
- «Un amplificador» → `amp`: la caja «Ampl.»
- «a la antena» → `antena`: una antena al final de la fila

<!-- b3 -->
Para recibir, el camino inverso: la antena, un amplificador de bajo ruido, el mezclador que baja la señal a banda base, el filtro y un conversor de doce bits, que entrega otra vez muestras complejas. El chirp entra como números y sale como números; en medio ha sido una onda de radio.

- «el camino inverso» → `inv`: la fila de abajo se resalta y aparece su antena
- «un amplificador de bajo ruido» → `lna`: la caja «LNA»
- «baja la señal a banda base» → `baja`: la caja «Mezclador», unida al mismo oscilador
- «el filtro» → `filtro`: la caja «Filtro»
- «un conversor de doce bits» → `adc`: la caja «ADC 12 bits»
- «muestras complejas» → `muestras`: a la izquierda, «I, Q»
- «entra como números» → `entra`: un punto recorre la fila de arriba
- «sale como números» → `sale`: un punto recorre la fila de abajo
- «una onda de radio» → `radio`: entre las dos antenas, una onda

---

# Escena 25 — ElExperimento

**Capítulo YouTube:** El experimento y el lazo digital
**Objetivo:** el montaje (un solo Pluto, buffer cíclico de tramas con silencios al azar) y la primera prueba, en lazo digital.

## Narración

<!-- b1 -->
En el experimento, el mismo Pluto transmite y recibe. Así los dos lados comparten oscilador y no hay desajuste de frecuencia. El transmisor repite sin parar un bloque de tramas, cada una precedida de un silencio de largo al azar. El receptor graba y busca las tramas sin saber dónde están.

- «el mismo Pluto transmite y recibe» → `mismo`: el Pluto, con una flecha de su antena de transmisión a la de recepción
- «comparten oscilador» → `osc`: «Un solo oscilador»
- «no hay desajuste de frecuencia» → `desaj`: «Δf = 0»
- «repite sin parar» → `repite`: una flecha circular
- «un bloque de tramas» → `bloque`: una tira con cuatro tramas
- «un silencio de largo al azar» → `silencio`: los huecos entre tramas, de largos distintos, se marcan
- «El receptor graba» → `graba`: debajo, una segunda tira, desplazada, con ruido encima
- «sin saber dónde están» → `sinsaber`: un «?» sobre cada trama de la segunda tira

<!-- b2 -->
Primera prueba: el lazo digital. El Pluto devuelve las muestras sin pasar por la parte analógica, sin ruido. Tienen que encontrarse todas las tramas en la muestra exacta. Diez de diez: el programa funciona.

- «el lazo digital» → `lazo`: «Lazo digital»
- «sin pasar por la parte analógica» → `sinana`: una caja «Analógico», atenuada y tachada
- «sin ruido» → `sinruido`: la tira recibida queda limpia
- «en la muestra exacta» → `exacta`: una línea vertical en el inicio de cada trama
- «Diez de diez» → `diez`: «10 / 10»
- «el programa funciona» → `funciona`: una tilde verde

---

# Escena 26 — BajarLaSenal

**Capítulo YouTube:** Cómo meter la señal debajo del ruido
**Objetivo:** con cualquier atenuación el SNR medido no baja de 10 dB (el AGC compensa); la solución es escalar las muestras con la atenuación al máximo.

## Narración

<!-- b1 -->
Segunda prueba, por el aire. Aquí aparece un problema: la señal llega demasiado bien. Aunque se atenúe el transmisor desde diez hasta ochenta y nueve decibelios, la relación señal a ruido medida no baja de diez. El control automático de ganancia del receptor sube lo mismo que baja la señal.

- «por el aire» → `aire`: dos antenas y una onda entre ellas
- «llega demasiado bien» → `bien`: «Demasiado bien»
- «se atenúe el transmisor» → `atenua`: ejes: «Atenuación del TX (dB)» y «SNR (dB)»
- «desde diez hasta ochenta y nueve decibelios» → `rango`: las marcas −10, −30, −50, −70 y −89
- «la relación señal a ruido medida» → `snr`: el eje vertical se resalta
- «no baja de diez» → `nobaja`: los cinco puntos medidos: 16,4 · 14 · 14,1 · 14 · 10,6
- «El control automático de ganancia» → `agc`: «AGC»
- «sube lo mismo que baja la señal» → `sube`: bajo cada punto, la ganancia: 15, 35, 53, 72 y 73 dB

<!-- b2 -->
Y lo interesante pasa entre menos veintidós y menos diez decibelios. La solución del cuaderno: dejar la atenuación al máximo y, además, encoger las muestras antes de transmitirlas. La señal baja, pero el ruido térmico del receptor se queda donde estaba. Ese es el ruido de verdad.

- «entre menos veintidós y menos diez» → `zona`: una banda roja, abajo, entre −22 y −10 dB
- «La solución del cuaderno» → `solucion`: la ventana «LoRa.ipynb»
- «la atenuación al máximo» → `max`: el punto de −89 dB se resalta
- «encoger las muestras» → `encoger`: «Muestras × escala»
- «La señal baja» → `baja`: desde el punto de −89 dB, una flecha baja hasta la banda
- «el ruido térmico del receptor» → `termico`: «Ruido térmico del RX»
- «se queda donde estaba» → `queda`: «No cambia»
- «el ruido de verdad» → `verdad`: una tilde verde

---

# Escena 27 — MedidoContraSimulado

**Capítulo YouTube:** Lo medido contra lo simulado
**Objetivo:** una captura real con la trama 14 dB bajo el ruido, y el FER medido sobre la curva simulada.

## Narración

<!-- b1 -->
Esto es una captura real del conversor del Pluto. Ahí dentro hay una trama, catorce decibelios por debajo del ruido. Se le pasa el detector, y el pico aparece justo donde empieza el preámbulo.

- «una captura real» → `captura`: la traza de la captura, en cian
- «del conversor del Pluto» → `adc`: «Niveles del ADC»
- «hay una trama» → `trama`: una llave «Trama» sobre el tramo donde está
- «por debajo del ruido» → `debajo`: «SNR = −14 dB»
- «Se le pasa el detector» → `detector`: debajo, se traza T[k]
- «el pico aparece» → `pico`: el pico se marca en ámbar
- «donde empieza el preámbulo» → `inicio`: una línea vertical une el pico con el inicio de la trama

<!-- b2 -->
Repetido con doscientas tramas por punto, la fracción de tramas perdidas medida por el aire cae sobre la curva simulada: de nueve de cada diez con menos veintitrés decibelios, a una de cada cien con menos doce. El ruido de la radio se comporta como el ruido blanco del modelo.

- «doscientas tramas por punto» → `n200`: «200 tramas por punto»
- «la fracción de tramas perdidas» → `fer`: ejes «SNR (dB)» y «FER»
- «cae sobre la curva simulada» → `sobre`: la curva simulada, en azul, y los puntos medidos, en ámbar
- «nueve de cada diez» → `nueve`: el primer punto se resalta, con «0,9»
- «menos veintitrés decibelios» → `m23`: una marca en −23 dB
- «una de cada cien» → `una`: el punto de «0,01» se resalta
- «menos doce» → `m12`: una marca en −12 dB
- «como el ruido blanco del modelo» → `modelo`: «Medido ≈ Simulado»

---

# Escena 28 — DosPasadasContraUna

**Capítulo YouTube:** Por qué la ecuación 2 sincroniza peor que el chirp de una pasada
**Objetivo:** con la modulación corregida (una pasada, fase con k/2) la demodulación rinde igual, pero la detección del inicio mejora: el chirp de la Ec. 2 se repite cada medio símbolo y deja picos falsos al 88 % a medio símbolo del verdadero; el de una pasada, no.

## Narración

<!-- b1 -->
Queda una cuenta pendiente: la letra pequeña de la ecuación dos. Tomada al pie de la letra, el chirp recorre la banda dos veces por símbolo. En una versión del cuaderno se probó la otra, la corregida, con una sola pasada: la misma ecuación, con el índice dividido por dos dentro de la fase. ¿Cambia algo en el rendimiento?

- «la letra pequeña» → `letra`: la lupa
- «la ecuación dos» → `ec2`: el rótulo «Ec. 2»
- «al pie de la letra» → `pie`: debajo, un plano tiempo-frecuencia vacío
- «dos veces por símbolo» → `dos`: dos rampas en el plano
- «la corregida» → `corr`: al lado, un plano con una sola rampa y el rótulo «Corregida»
- «el índice dividido por dos» → `k2`: bajo cada plano, su fase: «2π (s + k) k / 2^SF» y «2π (s + k/2) k / 2^SF»
- «¿Cambia algo» → `cambia`: un «?» entre los dos

<!-- b2 -->
En la demodulación, nada. Las dos familias de ondas son ortogonales y tienen la misma energía, que es lo único que usa el receptor óptimo. Al deshacer el chirp, cada una con su chirp que baja, queda el mismo tono en la misma casilla. La tasa de error de bit simulada coincide, en canal plano y con eco.

- «En la demodulación, nada» → `nada`: «Demodulación: igual»
- «ortogonales» → `orto`: «Ortogonales», bajo los dos planos
- «la misma energía» → `ener`: «Misma energía»
- «el receptor óptimo» → `optimo`: el bloque «Receptor óptimo»
- «Al deshacer el chirp» → `deshacer`: los planos dejan su lugar a dos ejes de casillas, uno por versión
- «el mismo tono en la misma casilla» → `tono`: el mismo pico en la casilla 20 de los dos
- «coincide» → `coincide`: «BER a −9 dB: 0,005 = 0,005»

<!-- b3 -->
La diferencia aparece al buscar el inicio de la trama. Miremos el chirp de la ecuación dos del símbolo cero, el del preámbulo. Como hace dos pasadas, su segunda mitad es idéntica a la primera: la onda se repite cada medio símbolo. Así que el preámbulo no son ocho chirps iguales: son dieciséis medios chirps iguales.

- «al buscar el inicio» → `inicio`: «Inicio de la trama»
- «el chirp de la ecuación dos» → `chirp`: un plano tiempo-frecuencia grande
- «el del preámbulo» → `pre`: sus dos rampas y el rótulo «Símbolo 0»
- «su segunda mitad es idéntica a la primera» → `mitad`: una copia de la primera rampa se desliza y cae justo sobre la segunda
- «se repite cada medio símbolo» → `repite`: «c[k + M/2] = c[k]»
- «ocho chirps iguales» → `ocho`: abajo, la tira del preámbulo, ocho símbolos
- «dieciséis medios chirps» → `dieciseis`: sus dieciséis rampas y el rótulo «16»

<!-- b4 -->
Ahora desliza la plantilla. Si la corres medio símbolo, sigue encajando en quince de los dieciséis trozos: el parecido solo baja al ochenta y ocho por ciento del máximo. Es un pico falso pegado al verdadero, y con ruido basta muy poco para que lo supere. El detector encuentra la trama, pero la coloca medio símbolo corrida. Y un inicio mal puesto es una trama perdida.

- «desliza la plantilla» → `desliza`: un marco ámbar cubre los ocho símbolos
- «medio símbolo» → `medio`: el marco se corre medio símbolo a la izquierda
- «quince de los dieciséis» → `quince`: «15 de 16»
- «ochenta y ocho por ciento» → `p88`: el peine del parecido sin ruido: un pico central y otro a cada lado, a medio símbolo, de altura 0,88
- «un pico falso pegado al verdadero» → `falso`: los picos de ±½ símbolo en rojo
- «con ruido basta muy poco» → `ruido`: una banda magenta de ruido a la altura de los picos
- «encuentra la trama» → `encuentra`: «Trama detectada», en verde
- «medio símbolo corrida» → `corrida`: una flecha del pico central al vecino
- «una trama perdida» → `perdida`: «Trama perdida»

<!-- b5 -->
Con el chirp de una sola pasada eso no ocurre. Corrido medio símbolo, es el mismo chirp pero desplazado media banda en frecuencia, y dos ondas así son ortogonales: el parecido es cero. Los picos falsos más cercanos quedan a un símbolo entero, y son más bajos: setenta y siete por ciento.

- «una sola pasada» → `una`: un plano con la rampa de una pasada
- «Corrido medio símbolo» → `corrido`: la misma rampa, corrida medio símbolo, en cian
- «desplazado media banda» → `media`: una cota vertical entre las dos rampas: «B/2»
- «ortogonales» → `orto`: «Ortogonales»
- «el parecido es cero» → `cero`: el peine de la versión corregida: nada a medio símbolo
- «a un símbolo entero» → `entero`: los picos a ±1 símbolo se resaltan
- «setenta y siete por ciento» → `p77`: «0,77»

<!-- b6 -->
Los números lo confirman. Con menos dieciocho decibelios, en mil quinientas tramas simuladas, las dos versiones dejan sin detectar las mismas: una docena. Pero la ecuación dos coloca mal doscientas noventa y cinco, casi todas medio símbolo corridas; la corregida, setenta y cinco. En la curva de tramas perdidas son unos dos decibelios y medio de diferencia. Y las capturas del Pluto muestran lo mismo: con la ecuación dos hay inicios corridos ciento veintiocho muestras; con la corregida, ninguno.

- «menos dieciocho decibelios» → `m18`: «SNR = −18 dB»
- «mil quinientas tramas» → `n1500`: una tabla con dos columnas, «Ec. 2» y «Corregida», y «1.500 tramas»
- «sin detectar las mismas» → `mismas`: la fila «No detectadas: 12 · 11»
- «doscientas noventa y cinco» → `v295`: la fila «Mal colocadas: 295», en rojo
- «medio símbolo corridas» → `medias`: debajo, «227 a medio símbolo»
- «setenta y cinco» → `v75`: en la otra columna, «75», en verde
- «dos decibelios y medio» → `curvas`: a la derecha, las dos curvas de FER y una cota «≈ 2,5 dB»
- «las capturas del Pluto» → `pluto`: el Pluto
- «con la ecuación dos hay» → `conec2`: «Ec. 2:»
- «ciento veintiocho muestras» → `c128`: «81 tramas a ±128 muestras»
- «ninguno» → `ninguno`: «Corregida: 0»

<!-- b7 -->
Así que la respuesta exacta es esta: la ecuación dos no demodula peor; sincroniza peor. Su chirp se repite a mitad de símbolo y eso le regala al ruido un pico falso al ochenta y ocho por ciento. Con una pasada, cada símbolo tiene una sola forma de encajar.

- «no demodula peor» → `nodemod`: «Demodular: igual»
- «sincroniza peor» → `sinc`: «Sincronizar: peor», en rojo
- «se repite a mitad de símbolo» → `repite`: el plano con las dos rampas
- «un pico falso» → `pico`: «Pico falso: 88 %»
- «Con una pasada» → `pasada`: el plano con una sola rampa
- «una sola forma de encajar» → `unica`: una tilde verde

---

# Escena 29 — Cierre

**Capítulo YouTube:** Toda la cadena, de un vistazo

## Narración

<!-- b1 -->
Recapitulemos la cadena. Los bits se agrupan en un número. El número desplaza un chirp. El aire le suma ruido. El receptor deshace el chirp, transforma y busca el pico. Y un preámbulo le dice dónde empezar.

- «Los bits se agrupan en un número» → `bits`: la caja «Bits → 20»
- «El número desplaza un chirp» → `chirp`: la caja «Chirp desplazado», con su rampa
- «El aire le suma ruido» → `ruido`: la caja «+ Ruido»
- «deshace el chirp» → `des`: la caja «× Chirp que baja»
- «transforma» → `fft`: la caja «FFT»
- «busca el pico» → `pico`: la caja «Máximo → 20»
- «un preámbulo» → `pre`: debajo de la cadena, «Preámbulo: 8 chirps» con ocho rampas

<!-- b2 -->
Cuatro páginas de ecuaciones, un cuaderno que las convierte en código y una radio que confirma que funcionan. Estimar, detectar, filtros adaptados y densidad espectral: todo lo del curso, dentro de un sensor que funciona con una pila.

- «Cuatro páginas de ecuaciones» → `paginas`: cuatro documentos
- «un cuaderno» → `cuaderno`: la ventana «LoRa.ipynb»
- «una radio» → `radio`: el Pluto
- «Estimar» → `est`: «Estimar»
- «detectar» → `det`: «Detectar»
- «filtros adaptados» → `fa`: «Filtro adaptado»
- «densidad espectral» → `psd`: «Densidad espectral»
- «un sensor que funciona con una pila» → `sensor`: el sensor del principio, con su pila
