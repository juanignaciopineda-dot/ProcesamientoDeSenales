"""Piezas del especial de LoRa (`Especial_LoRa/`): la modulación del artículo de Vangelista,
el receptor del cuaderno del trabajo práctico y el ADALM-Pluto.

Las escenas hacen `from comun.figuras_lora import *` después de `from comun.escena import *`.

La parte de señal (`chirp_lora`, `chirp_una_pasada`, `deschirpear`, `casillas_fft`,
`preambulo_lora`, `correlacion_preambulo`) es la del paquete `lora` del trabajo práctico
(`tx.modulator`, `tx.integrated_modulator`, `rx.dechirp_fft`, `tx.preamble`,
`detection.preamble_correlation`), copiada aquí para que el episodio no dependa de él.
Los números medidos (`BER_*`, `FER_*`, `ATEN_*`, `TERMICO_*`) salen de correr ese paquete y
las capturas del Pluto: ver `Especial_LoRa/E1_Del_articulo_a_la_radio/datos/generar_datos.py`.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
from manim import *

from comun.estilo import *
from comun.figuras import Lienzo, traza

# ============================================================ señal (paquete `lora` del TP)

M7 = 128          # muestras por símbolo con SF = 7
S_EJEMPLO = 20    # el símbolo que atraviesa el episodio (bits de peso 4 y 16)
BITS_EJEMPLO = (0, 0, 1, 0, 1, 0, 0)   # w_0 … w_6 del símbolo 20


def chirp_lora(s: int, M: int = M7, L: int = 1) -> np.ndarray:
    """Ec. 2 del artículo para el símbolo `s`, con `L` puntos por muestra (`tx.modulator`)."""
    k = np.arange(M * L) / L
    return np.exp(2j * np.pi * (s + k) * k / M) / np.sqrt(M)


def chirp_una_pasada(s: int, M: int = M7, L: int = 1) -> np.ndarray:
    """El chirp cuya frecuencia es ((s + k) mod M)·B/M: una pasada por símbolo
    (`tx.integrated_modulator`)."""
    k = np.arange(M * L) / L
    fase = (s + k / 2) * k / M - np.maximum(k - (M - s), 0)
    return np.exp(2j * np.pi * fase) / np.sqrt(M)


def deschirpear(r: np.ndarray, M: int = M7, L: int = 1) -> np.ndarray:
    """r · e^{−j2πk²/M}: el producto por el chirp que baja (`rx.dechirp`)."""
    k = np.arange(M * L) / L
    return r.reshape(-1, M * L) * np.exp(-2j * np.pi * k ** 2 / M)


def casillas_fft(r: np.ndarray, M: int = M7) -> np.ndarray:
    """|⟨r, c_q⟩|² para cada casilla q: deshacer el chirp y FFT unitaria (Ec. 16)."""
    return np.abs(np.fft.fft(deschirpear(r, M), norm="ortho")) ** 2


def ruido_complejo(n: int, potencia: float, semilla: int = 1) -> np.ndarray:
    """Ruido blanco gaussiano complejo de la potencia dada (por muestra)."""
    g = np.random.default_rng(semilla)
    s = np.sqrt(potencia / 2)
    return g.normal(0, s, n) + 1j * g.normal(0, s, n)


def recibido(s: int = S_EJEMPLO, snr_db: float = -10.0, M: int = M7, semilla: int = 5) -> np.ndarray:
    """Un símbolo de la Ec. 2 más ruido blanco con la relación señal a ruido pedida."""
    c = chirp_lora(s, M)
    return c + ruido_complejo(M, (1 / M) / 10 ** (snr_db / 10), semilla)


def preambulo_lora(M: int, n_sube: int = 8, n_baja: float = 2.25) -> np.ndarray:
    """Preámbulo: `n_sube` chirps del símbolo 0 y `n_baja` chirps que bajan (`tx.preamble`)."""
    sube = np.tile(chirp_lora(0, M), n_sube)
    baja = np.conj(np.tile(chirp_lora(0, M), int(np.ceil(n_baja))))[: int(n_baja * M)]
    return np.concatenate([sube, baja])


def correlacion_preambulo(r: np.ndarray, M: int, n_sube: int = 8) -> np.ndarray:
    """T[k] = |⟨r_k, p⟩|² con los `n_sube` chirps del preámbulo (`detection.preamble_correlation`)."""
    plantilla = np.tile(chirp_lora(0, M), n_sube)
    return np.abs(np.correlate(r, plantilla, mode="valid")) ** 2


# ---- números medidos con el paquete `lora` (semilla 0) y las capturas del Pluto ----------
BER_SNR = (-12, -11, -10, -9, -8, -7, -6)
BER_PLANO = (0.1016, 0.0511, 0.0197, 0.00505, 0.000877, 0.0000971, 0.00000857)
BER_ECO = (0.1653, 0.1026, 0.0550, 0.0238, 0.00936, 0.00367, 0.00174)

# FER de los tres detectores (SF = 8, canal plano, 600 tramas por punto como mucho)
FER3_SNR = tuple(range(-24, -10))
FER3_COMPLETO = (0.968, 0.938, 0.769, 0.526, 0.448, 0.227, 0.195, 0.157, 0.0787, 0.0701, 0.0333, 0.0067,
                 0.015, 0.0017)
FER3_PICOS = (0.968, 1.0, 1.0, 0.938, 0.857, 0.577, 0.395, 0.370, 0.214, 0.146, 0.098, 0.0559, 0.0233, 0.0083)
FER3_DEMOD = (1.0, 0.968, 1.0, 1.0, 0.938, 0.938, 0.75, 0.556, 0.345, 0.248, 0.151, 0.0483, 0.0167, 0.01)

# Pluto: SNR medido según la atenuación del TX (con el AGC) y ganancia que eligió el AGC
ATEN_DB = (-10, -30, -50, -70, -89)
ATEN_SNR = (16.4, 14.0, 14.1, 14.0, 10.6)
ATEN_GANANCIA = (15, 35, 53, 72, 73)

# Pluto: FER por el aire con la atenuación al máximo y las muestras escaladas (200 tramas por punto)
TERMICO_SNR = (-22.7, -20.8, -17.7, -15.7, -13.7, -11.6)
TERMICO_FER = (0.925, 0.69, 0.185, 0.04, 0.02, 0.01)
# FER simulado con el mismo detector y los mismos parámetros (SF = 8, canal plano)
FER_SIM_SNR = tuple(range(-24, -9))
FER_SIM = (1.0, 1.0, 0.9375, 0.732, 0.556, 0.280, 0.229, 0.140, 0.102, 0.063, 0.0422, 0.0233, 0.009, 0.004,
           0.001)

_DATOS = Path(__file__).resolve().parent.parent / "Especial_LoRa" / "E1_Del_articulo_a_la_radio" / "datos"


def captura_pluto() -> tuple[np.ndarray, int]:
    """Recorte de una captura real del Pluto (SF = 8, B = 1 MHz, SNR medido de −13,7 dB):
    muestras complejas del ADC y la muestra donde empieza la trama."""
    with np.load(_DATOS / "captura_pluto.npz") as z:
        iq = z["iq"].astype(float)
        return iq[:, 0] + 1j * iq[:, 1], int(z["inicio"])


# ============================================================ plano tiempo-frecuencia

class PlanoTF(VGroup):
    """Plano tiempo-frecuencia de `n` símbolos de ancho y de 0 a `f_max`·B de alto.

        P = PlanoTF(centro=(0, 0), ancho=5, alto=2.4, n=1)
        r = P.rampa(20)            # la rampa del símbolo 20 (da la vuelta al llegar a B)
    Atributos: `.marco`, `.rot_t` («Tiempo»), `.rot_f` («Frecuencia»), `.cero` y `.tope` («0» y «B»),
    `.rotulos` (los cuatro). `p(t, f)`: punto de pantalla, con `t` en símbolos y `f` en unidades de B.
    Todo lo que dibuja son `Line`: no cuenta para el control de encimados.
    """

    def __init__(self, centro=(0.0, 0.0), ancho: float = 5.0, alto: float = 2.4, n: float = 1,
                 f_max: float = 1.0, rotulos: bool = True, escala: float = 0.4, tope: str = "B"):
        super().__init__()
        self.cx, self.cy, self.ancho, self.alto, self.n, self.f_max = centro[0], centro[1], ancho, alto, n, f_max
        self.marco = Rectangle(width=ancho, height=alto, color=INK, stroke_width=2).move_to([self.cx, self.cy, 0])
        self.add(self.marco)
        self.rot_t = Text("Tiempo", color=INK).scale(escala).next_to(self.marco, DOWN, buff=0.12)
        self.rot_f = Text("Frecuencia", color=INK).scale(escala).rotate(PI / 2).next_to(self.marco, LEFT, buff=0.42)
        self.cero = Text("0", color=INK).scale(escala).next_to(self.p(0, 0), LEFT, buff=0.1)
        self.tope = Text(tope, color=INK).scale(escala).next_to(self.p(0, f_max), LEFT, buff=0.1)
        self.rotulos = VGroup(self.rot_t, self.rot_f, self.cero, self.tope)
        if rotulos:
            self.add(self.rotulos)

    def p(self, t: float, f: float) -> np.ndarray:
        return np.array([self.cx - self.ancho / 2 + t / self.n * self.ancho,
                         self.cy - self.alto / 2 + f / self.f_max * self.alto, 0.0])

    def tramos(self, s: float, i: float = 0.0, M: int = M7, pend: float = 1.0, dur: float = 1.0):
        """Tramos rectos de f = (s/M + pend·t) mod 1 para t de 0 a `dur` símbolos:
        lista de ((t0, f0), (t1, f1)), con t medido desde el principio del plano."""
        f, t, out = (s / M) % 1.0, 0.0, []
        while t < dur - 1e-9:
            if pend > 0:
                dt = min((1.0 - f) / pend, dur - t)
                f1 = f + pend * dt
            else:
                if f <= 1e-9:
                    f = 1.0
                dt = min(f / -pend, dur - t)
                f1 = f + pend * dt
            if dt > 1e-9:
                out.append(((i + t, f), (i + t + dt, f1)))
            t += dt
            f = 0.0 if pend > 0 else 1.0
        return out

    def rampa(self, s: float, i: float = 0.0, M: int = M7, color=AMBAR, grosor: float = 5.0,
              pend: float = 1.0, dur: float = 1.0) -> VGroup:
        """La rampa del símbolo `s` en el símbolo número `i` del plano (un `Line` por tramo)."""
        return VGroup(*[Line(self.p(*a), self.p(*b), color=color, stroke_width=grosor)
                        for a, b in self.tramos(s, i, M, pend, dur)])

    def bajada(self, i: float = 0.0, dur: float = 1.0, color=CIAN, grosor: float = 5.0) -> VGroup:
        """Chirp que baja de B a 0 (el del preámbulo y el que deshace el chirp)."""
        return self.rampa(0, i, color=color, grosor=grosor, pend=-1.0, dur=dur)

    def tono(self, s: float, i: float = 0.0, M: int = M7, color=AMBAR, grosor: float = 5.0) -> Line:
        """Frecuencia constante s·B/M durante el símbolo `i`."""
        return Line(self.p(i, s / M), self.p(i + 1, s / M), color=color, stroke_width=grosor)

    def salto(self, s: float, i: float = 0.0, M: int = M7, color=INK) -> DashedLine:
        """Línea de trazos de B a 0 donde la rampa del símbolo `s` da la vuelta."""
        t = i + (M - s) / M
        return DashedLine(self.p(t, 1), self.p(t, 0), color=color, stroke_width=2, dash_length=0.08)

    def division(self, i: float, color=INK, opacidad: float = 0.5) -> Line:
        """Línea vertical fina en el borde del símbolo `i`."""
        return Line(self.p(i, 0), self.p(i, self.f_max), color=color, stroke_width=1.5, stroke_opacity=opacidad)

    def nivel(self, f: float, color=INK) -> DashedLine:
        """Línea horizontal de trazos a la altura `f`."""
        return DashedLine(self.p(0, f), self.p(self.n, f), color=color, stroke_width=2.5, dash_length=0.1)


def trama_tf(P: PlanoTF, i0: float, simbolos, M: int = 256, grosor: float = 3.0) -> tuple[VGroup, VGroup, VGroup]:
    """Una trama sobre `P` a partir del símbolo `i0`: (ocho chirps, dos y cuarto que bajan, datos)."""
    sube = VGroup(*[P.rampa(0, i0 + j, M, AMBAR, grosor) for j in range(8)])
    baja = VGroup(P.bajada(i0 + 8, 1, CIAN, grosor), P.bajada(i0 + 9, 1, CIAN, grosor),
                  P.bajada(i0 + 10, 0.25, CIAN, grosor))
    datos = VGroup(*[P.rampa(s, i0 + 10.25 + j, M, AZUL, grosor) for j, s in enumerate(simbolos)])
    return sube, baja, datos


# ============================================================ casillas de la FFT

class CasillasFFT(VGroup):
    """Las casillas de la FFT como barras finas sobre un eje.

        C = CasillasFFT(valores, centro=(0, -2), ancho=10, alto=2, v_max=1.1)
    Atributos: `.base`, `.barras` (una `Line` por casilla), `.rots` («0», último índice y «Casilla»).
    `x(q)`, `cima(q)`, `pie(q)`; `pintar(q, color)` cambia el color de una barra.
    """

    def __init__(self, valores, centro=(0.0, 0.0), ancho: float = 10.0, alto: float = 2.0,
                 v_max: float | None = None, color=INK, grosor: float = 3.0, rotulo: str = "Casilla",
                 escala: float = 0.38):
        super().__init__()
        self.v = np.asarray(valores, dtype=float)
        self.cx, self.cy, self.ancho, self.alto = centro[0], centro[1], ancho, alto
        self.v_max = float(self.v.max()) if v_max is None else v_max
        n = len(self.v)
        self.base = Line([self.cx - ancho / 2 - 0.1, self.cy, 0], [self.cx + ancho / 2 + 0.1, self.cy, 0],
                         color=INK, stroke_width=2)
        self.barras = VGroup(*[Line(self.pie(q), self.cima(q), color=color, stroke_width=grosor)
                               for q in range(n)])
        c0 = Text("0", color=INK).scale(escala).next_to(self.pie(0), DOWN, buff=0.1)
        c1 = Text(str(n - 1), color=INK).scale(escala).next_to(self.pie(n - 1), DOWN, buff=0.1)
        rot = Text(rotulo, color=INK).scale(escala).move_to([self.cx, c0.get_center()[1], 0])
        self.rots = VGroup(c0, c1, rot)
        self.add(self.base, self.barras, self.rots)

    def x(self, q: float) -> float:
        n = len(self.v)
        return self.cx - self.ancho / 2 + (q + 0.5) / n * self.ancho

    def pie(self, q: float) -> np.ndarray:
        return np.array([self.x(q), self.cy, 0.0])

    def cima(self, q: int) -> np.ndarray:
        h = max(float(self.v[q]) / self.v_max * self.alto, 0.012)
        return np.array([self.x(q), self.cy + h, 0.0])

    def y(self, v: float) -> float:
        return self.cy + v / self.v_max * self.alto

    def pintar(self, q: int, color=AMBAR, grosor: float = 5.0) -> Line:
        self.barras[q].set_stroke(color=color, width=grosor)
        return self.barras[q]


# ============================================================ ejes para curvas medidas

class EjesXY:
    """Ejes hechos con líneas para curvas contra el SNR (el eje vertical puede ser logarítmico).

        E = EjesXY(centro=(0, 0), ancho=6, alto=3.4, x=(-12, -6), y=(1e-5, 1), log_y=True,
                   x_marcas=(-12, -10, -8, -6), y_marcas=(1e-1, 1e-3, 1e-5), rot_x="SNR (dB)", rot_y="BER")
    `.ejes` (las dos rectas), `.marcas` (números), `.rots` (rótulos), `.todo` (VGroup de todo).
    `p(x, y)`, `curva(xs, ys, color)` (salta los ceros si es logarítmico), `punto(x, y, color)`.
    """

    def __init__(self, centro=(0.0, 0.0), ancho: float = 6.0, alto: float = 3.4, x=(0.0, 1.0), y=(0.0, 1.0),
                 log_y: bool = False, x_marcas=(), y_marcas=(), rot_x: str = "", rot_y: str = "",
                 escala: float = 0.38):
        self.cx, self.cy, self.ancho, self.alto = centro[0], centro[1], ancho, alto
        self.x0, self.x1 = x
        self.log_y = log_y
        self.y0, self.y1 = (np.log10(y[0]), np.log10(y[1])) if log_y else y
        o = self.p(self.x0, y[0])
        self.ejes = VGroup(Line(o, o + RIGHT * (ancho + 0.2), color=INK, stroke_width=2),
                           Line(o, o + UP * (alto + 0.2), color=INK, stroke_width=2))
        self.marcas = VGroup()
        self.guias = VGroup()
        for xm in x_marcas:
            t = MathTex(str(xm).replace(".", "{,}"), color=INK).scale(escala * 1.4)
            self.marcas.add(t.next_to(self.p(xm, y[0]), DOWN, buff=0.12))
        for ym in y_marcas:
            if log_y:
                e = int(round(np.log10(ym)))
                tex = "1" if e == 0 else rf"10^{{{e}}}"
            else:
                tex = str(ym).replace(".", "{,}")
            t = MathTex(tex, color=INK).scale(escala * 1.4)
            self.marcas.add(t.next_to(self.p(self.x0, ym), LEFT, buff=0.12))
            self.guias.add(Line(self.p(self.x0, ym), self.p(self.x1, ym), color=INK, stroke_width=1,
                                stroke_opacity=0.3))
        self.rots = VGroup()
        if rot_x:
            self.rots.add(Text(rot_x, color=INK).scale(escala).next_to(self.p((self.x0 + self.x1) / 2, y[0]),
                                                                       DOWN, buff=0.5))
        if rot_y:
            self.rots.add(Text(rot_y, color=INK).scale(escala).next_to(o + UP * (alto + 0.2), UP, buff=0.1))
        self.todo = VGroup(self.guias, self.ejes, self.marcas, self.rots)

    def p(self, x: float, y: float) -> np.ndarray:
        yy = np.log10(max(y, 1e-12)) if self.log_y else y
        return np.array([self.cx - self.ancho / 2 + (x - self.x0) / (self.x1 - self.x0) * self.ancho,
                         self.cy - self.alto / 2 + (yy - self.y0) / (self.y1 - self.y0) * self.alto, 0.0])

    def curva(self, xs, ys, color=SENAL, grosor: float = 4.0) -> VMobject:
        pts = [self.p(a, b) for a, b in zip(xs, ys) if not (self.log_y and b <= 0)]
        m = VMobject(stroke_color=color, stroke_width=grosor).set_fill(opacity=0)
        m.set_points_as_corners(pts)
        return m

    def punto(self, x: float, y: float, color=AMBAR, radio: float = 0.09) -> Dot:
        return Dot(self.p(x, y), radius=radio, color=color)

    def puntos(self, xs, ys, color=AMBAR, radio: float = 0.09) -> VGroup:
        return VGroup(*[self.punto(a, b, color, radio) for a, b in zip(xs, ys) if not (self.log_y and b <= 0)])


# ============================================================ bits y bloques

def fila_bits(bits, centro=(0.0, 0.0), lado: float = 0.8, color=INK, escala: float = 0.7) -> VGroup:
    """Casillas cuadradas con un bit cada una. `.cas` (cuadrados), `.nums` (dígitos), `x(i)`."""
    cas = VGroup(*[Square(side_length=lado, color=color, stroke_width=2.5) for _ in bits])
    cas.arrange(RIGHT, buff=0.12).move_to([centro[0], centro[1], 0])
    nums = VGroup(*[Text(str(b), color=TXT, weight=BOLD).scale(escala * lado / 0.8).move_to(c)
                    for b, c in zip(bits, cas)])
    g = VGroup(cas, nums)
    g.cas, g.nums = cas, nums
    g.x = lambda i: float(cas[i].get_center()[0])
    return g


def bloque(txt: str, color=AZUL, ancho: float | None = None, alto: float = 0.8, escala: float = 0.45) -> VGroup:
    """Caja de un bloque de la cadena (es `caja` de `estilo.py` con el tamaño del episodio)."""
    return caja(txt, color, ancho=ancho, alto=alto, scale=escala)


def fila_bloques(textos, colores=None, centro=(0.0, 0.0), hueco: float = 0.5, alto: float = 0.8,
                 escala: float = 0.42, ancho: float | None = None):
    """Bloques en fila unidos por flechas. Devuelve (cajas, flechas)."""
    colores = colores or [AZUL] * len(textos)
    cajas = [bloque(t, c, ancho, alto, escala) for t, c in zip(textos, colores)]
    VGroup(*cajas).arrange(RIGHT, buff=hueco).move_to([centro[0], centro[1], 0])
    fl = [Arrow(a.get_right(), b.get_left(), color=INK, stroke_width=3, buff=0.06,
                max_tip_length_to_length_ratio=0.35) for a, b in zip(cajas[:-1], cajas[1:])]
    return cajas, fl


def cota(p_a, p_b, texto: str, color=INK, lado=UP, escala: float = 0.42, sep: float = 0.12,
         tex: bool = False) -> VGroup:
    """Cota entre dos puntos, con topes y un texto al lado (`tex=True`: el texto es LaTeX).
    `.linea`, `.rot`."""
    a, b = np.array(p_a, dtype=float), np.array(p_b, dtype=float)
    d = (b - a) / np.linalg.norm(b - a)
    n = np.array([-d[1], d[0], 0.0]) * 0.1
    linea = VGroup(Line(a, b, color=color, stroke_width=2.5), Line(a - n, a + n, color=color, stroke_width=2.5),
                   Line(b - n, b + n, color=color, stroke_width=2.5))
    rot = MathTex(texto, color=color).scale(escala * 1.6) if tex else Text(texto, color=color).scale(escala)
    rot.next_to((a + b) / 2, lado, buff=sep)
    g = VGroup(linea, rot)
    g.linea, g.rot = linea, rot
    return g


# ============================================================ íconos

def pluto(color=AZUL) -> VGroup:
    """El ADALM-Pluto: una caja con dos antenas. `.cuerpo`, `.ant_tx`, `.ant_rx`, `.rot`;
    `punta_tx()` y `punta_rx()` dan la punta de cada antena."""
    cuerpo = RoundedRectangle(corner_radius=0.12, width=2.2, height=1.1, color=color,
                              stroke_width=3.5).set_fill(color, 0.15)
    rot = Text("Pluto", color=TXT, weight=BOLD).scale(0.42).move_to(cuerpo)

    def _antena(x):
        palo = Line([x, 0.55, 0], [x, 1.35, 0], color=TXT, stroke_width=5)
        base = Rectangle(width=0.22, height=0.14, color=TXT, stroke_width=0).set_fill(TXT, 1).move_to([x, 0.6, 0])
        return VGroup(palo, base)

    g = VGroup(cuerpo, rot, _antena(-0.7), _antena(0.7))
    g.cuerpo, g.rot, g.ant_tx, g.ant_rx = cuerpo, rot, g[2], g[3]
    g.punta_tx = lambda: g.ant_tx[0].get_end()
    g.punta_rx = lambda: g.ant_rx[0].get_end()
    return g


def sensor_campo(color=VERDE) -> VGroup:
    """Sensor pequeño con antena, clavado en el suelo. `.cuerpo`, `.punta()`."""
    estaca = Line([0, -0.6, 0], [0, -0.2, 0], color=INK, stroke_width=5)
    cuerpo = RoundedRectangle(corner_radius=0.08, width=0.7, height=0.55, color=color,
                              stroke_width=3.5).set_fill(color, 0.2).move_to([0, 0.05, 0])
    luz = Dot([0.18, 0.12, 0], radius=0.06, color=AMBAR)
    ant = Line([-0.2, 0.32, 0], [-0.2, 0.8, 0], color=TXT, stroke_width=4)
    g = VGroup(estaca, cuerpo, luz, ant)
    g.cuerpo = cuerpo
    g.punta = lambda: ant.get_end()
    return g


def antena_simple(color=TXT, alto: float = 1.2) -> VGroup:
    """Antena de varilla con una V arriba (para los extremos de un diagrama de bloques)."""
    palo = Line([0, 0, 0], [0, alto, 0], color=color, stroke_width=4)
    v = VGroup(Line([0, alto * 0.6, 0], [-0.3, alto, 0], color=color, stroke_width=4),
               Line([0, alto * 0.6, 0], [0.3, alto, 0], color=color, stroke_width=4))
    return VGroup(palo, v)


def cuaderno_lora(color=AMBAR) -> VGroup:
    """Ventana del cuaderno del trabajo práctico (`LoRa.ipynb`), con tres renglones de código."""
    marco = RoundedRectangle(width=2.4, height=1.6, corner_radius=0.08, color=color,
                             stroke_width=2.5).set_fill(FONDO, 1)
    barra = Rectangle(width=2.4, height=0.3, stroke_width=0).set_fill(color, 0.6).align_to(marco, UP)
    nombre = Text("LoRa.ipynb", color=TXT).scale(0.28).move_to(barra)
    reng = VGroup(*[Line([-0.9, y, 0], [x, y, 0], color=c, stroke_width=4)
                    for y, x, c in ((0.25, 0.5, CIAN), (-0.05, 0.85, INK), (-0.35, 0.2, VERDE))])
    reng.shift(marco.get_center() + DOWN * 0.12)
    g = VGroup(marco, barra, nombre, reng)
    g.marco = marco
    return g


def oscilador(color=AMBAR, radio: float = 0.38) -> VGroup:
    """Oscilador local: un círculo con un ciclo de seno dentro."""
    c = Circle(radius=radio, color=color, stroke_width=3).set_fill(color, 0.12)
    t = np.linspace(-1, 1, 40)
    s = traza(t * radio * 0.6, np.sin(np.pi * t) * radio * 0.4, color, 3)
    return VGroup(c, s)


def onda_radio(p_a, p_b, color=CIAN, ciclos: int = 6, amp: float = 0.18, grosor: float = 3.0) -> VMobject:
    """Onda senoidal dibujada entre dos puntos (lo que viaja por el aire)."""
    a, b = np.array(p_a, dtype=float), np.array(p_b, dtype=float)
    d = b - a
    largo = np.linalg.norm(d)
    u = d / largo
    n = np.array([-u[1], u[0], 0.0])
    t = np.linspace(0, 1, 30 * ciclos)
    pts = [a + u * largo * x + n * amp * np.sin(2 * np.pi * ciclos * x) for x in t]
    m = VMobject(stroke_color=color, stroke_width=grosor).set_fill(opacity=0)
    m.set_points_as_corners(pts)
    return m


def traza_ruidosa(L: Lienzo, semilla: int = 5, snr_db: float = -10.0, color=MEDIDA, grosor: float = 2.2,
                  s: int = S_EJEMPLO) -> VMobject:
    """Parte real de un símbolo recibido con ruido (el del gancho), sobre un `Lienzo` con t de 0 a 1."""
    r = recibido(s, snr_db, M7, semilla).real
    return L.curva(np.linspace(0, 1, r.size), r, color, grosor)

# ============================================================ segunda parte: FSK, umbral y plantilla
# (lo que sigue lo usan las escenas 16 y 18 a 22)

# BER con eco de FSCM y de FSK (SF = 7, 200.000 símbolos por punto). La FSK no está en el cuaderno:
# es una simulación hecha para el vídeo (tono e^(j2πsk/M), mismo canal, misma FFT y máximo).
FSK_SNR = (-12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2)
FSCM_ECO = (0.165, 0.102, 0.0545, 0.024, 0.00937, 0.00393, 0.00165, 0.000624, 0.00021, 3.86e-05, 4.29e-06)
FSK_ECO = (0.171, 0.136, 0.107, 0.0807, 0.0576, 0.0386, 0.0231, 0.0116, 0.00499, 0.00153, 0.000326)
FSK_FALLA_S0, FSK_FALLA_S64 = 0.0, 0.58     # símbolos errados a −8 dB con eco

# Probabilidad de detectar la trama (inicio dentro del preámbulo) y de acertar la muestra exacta,
# según el largo de la plantilla (SF = 8, canal plano, 300 tramas por punto, misma P_FA)
PDET_SNR = (-26, -24, -22, -20, -18, -16, -14, -12, -10, -8)
PDET = {"1": (0.0, 0.0, 0.0, 0.0, 0.0433, 0.23, 0.87, 1.0, 1.0, 1.0), "2": (0.0, 0.00667, 0.01, 0.137, 0.403, 0.91, 0.997, 0.997, 1.0, 1.0), "4": (0.00667, 0.0233, 0.1, 0.443, 0.88, 0.99, 0.993, 1.0, 1.0, 1.0),
        "8": (0.0133, 0.0633, 0.283, 0.71, 0.9, 0.963, 0.997, 0.997, 1.0, 1.0), "10,25": (0.0233, 0.16, 0.573, 0.92, 0.99, 0.99, 0.993, 1.0, 1.0, 1.0)}
EXACTA_M8 = {"1": 0.54, "2": 0.34, "4": 0.24, "8": 1.00, "10,25": 1.00}

# Tiempo medido de la correlación sobre 64 símbolos (16.384 muestras), en ms: directa y por FFT
TIEMPO_CHIRPS = (1, 2, 4, 8, 10.25)
TIEMPO_DIRECTA_MS = (1.1, 1.8, 3.6, 7.5, 10.3)
TIEMPO_FFT_MS = (0.5, 0.5, 0.5, 0.5, 0.5)

# Umbrales (SF = 8, 125 kHz, una falsa alarma por minuto): P_FA por muestra y por símbolo,
# −ln(P_FA por muestra), umbral del detector de picos sobre σ² y umbral del de ceros
P_FA_MUESTRA, P_FA_SIMBOLO = 1 / 7_500_000, 3.4e-5
LN_PFA = 15.83
ETA_PICOS_SOBRE_SIGMA2 = 31.7
K_CEROS = 3

M_DEMO = 64       # muestras por símbolo en los dibujos de la detección (SF = 6: curvas ligeras)
DATOS_DEMO = (37, 9, 52, 20, 60, 14, 45, 3, 28, 50)


def senal_demo(n0: int = 5, total: int = 26, snr_db: float = -14.0, semilla: int = 3, datos=DATOS_DEMO):
    """`n0` símbolos de silencio, una trama (preámbulo + datos) y ruido blanco: (r, σ²)."""
    M = M_DEMO
    trama = np.concatenate([preambulo_lora(M), np.concatenate([chirp_lora(s, M) for s in datos])])
    x = np.concatenate([np.zeros(n0 * M), trama, np.zeros(total * M - n0 * M - trama.size)])
    sigma2 = (1 / M) / 10 ** (snr_db / 10)
    return x + ruido_complejo(x.size, sigma2, semilla), sigma2


def umbral_demo(sigma2: float) -> float:
    """η = −8σ² ln(P_FA por muestra): el umbral de Neyman-Pearson del detector de preámbulo completo."""
    return 8 * sigma2 * LN_PFA


def ganancia_eco(f):
    """|H(f)|² del canal con eco √0,8 δ[n] + √0,2 δ[n−1], con f en vueltas por muestra (0 a 1)."""
    return 1 + 0.8 * np.cos(2 * np.pi * np.asarray(f, dtype=float))


def densidad_h1(t, lam: float):
    """Densidad de T/(8σ²) cuando hay preámbulo: |a + n|² con |a|² = `lam` y n ruido de potencia 1."""
    t = np.asarray(t, dtype=float)
    x = 2 * np.sqrt(lam * t)
    return np.exp(-(t + lam) + x) * np.i0(x) * np.exp(-x)


def flecha_v(a, b, color=SENAL, grosor: float = 5.0, punta: float = 0.22) -> Arrow:
    """Flecha (un número complejo, una correlación) entre dos puntos."""
    return Arrow(np.array(a, dtype=float), np.array(b, dtype=float), color=color, stroke_width=grosor, buff=0,
                 max_tip_length_to_length_ratio=punta)


def insignia(n, color=INK, radio: float = 0.34, escala: float = 0.6) -> VGroup:
    """Número dentro de un círculo. `.aro`, `.num`."""
    g = VGroup(Circle(radius=radio, color=color, stroke_width=3), Text(str(n), color=TXT, weight=BOLD).scale(escala))
    g.aro, g.num = g[0], g[1]
    return g


def area_bajo(pts, y0: float, color=ERROR, opacidad: float = 0.55) -> VMobject:
    """Área entre una lista de puntos de una curva y la altura `y0` (un polígono relleno)."""
    pts = [np.array(p, dtype=float) for p in pts]
    if len(pts) < 2:
        pts = [np.array([0.0, y0, 0.0]), np.array([0.001, y0, 0.0])]
    borde = [np.array([pts[0][0], y0, 0.0])] + pts + [np.array([pts[-1][0], y0, 0.0])]
    m = VMobject(stroke_width=0).set_fill(color, opacidad)
    m.set_points_as_corners(borde + [borde[0]])
    return m


# El factor de ensanchamiento como dial (B = 125 kHz): bits por segundo SF·B/2^SF y SNR mínimo para
# BER = 10⁻³ en canal plano (simulado con 6.000 a 12.000 símbolos por punto; ver generar_datos.py)
SF_DIAL = (7, 8, 9, 10, 11, 12)
SF_BPS = (6836, 3906, 2197, 1221, 671, 366)
SF_SNR_MIN = (-8.2, -10.8, -13.7, -16.5, -19.3, -22.1)


class Dial(VGroup):
    """Dial semicircular con las marcas de SF 7 a 12 y una aguja. `.aguja`; `angulo(sf)` da el ángulo
    de la aguja para ese factor y `girar(sf)` la animación que la lleva hasta él."""

    def __init__(self, centro=(0.0, 0.0), radio: float = 1.8, sf: float = 7):
        super().__init__()
        self.c = np.array([centro[0], centro[1], 0.0])
        self.radio, self.sf = radio, sf
        arco = Arc(radius=radio, start_angle=0, angle=PI, color=INK, stroke_width=4).shift(self.c)
        marcas, nums = VGroup(), VGroup()
        for v in SF_DIAL:
            a = self.angulo(v)
            u = np.array([np.cos(a), np.sin(a), 0.0])
            marcas.add(Line(self.c + u * radio * 0.88, self.c + u * radio, color=INK, stroke_width=4))
            nums.add(Text(str(v), color=TXT, weight=BOLD).scale(0.5 * radio / 1.8).move_to(self.c + u * radio * 1.2))
        a = self.angulo(sf)
        self.aguja = Line(self.c, self.c + radio * 0.8 * np.array([np.cos(a), np.sin(a), 0.0]), color=AMBAR, stroke_width=7)
        eje = Dot(self.c, radius=0.1, color=AMBAR)
        rot = Text("SF", color=AMBAR, weight=BOLD).scale(0.6 * radio / 1.8).move_to(self.c + DOWN * 0.45 * radio / 1.8)
        self.add(arco, marcas, nums, self.aguja, eje, rot)

    @staticmethod
    def angulo(sf: float) -> float:
        return PI - (sf - 7) / 5 * PI * 0.86 - PI * 0.07

    def girar(self, sf: float):
        d = self.angulo(sf) - self.angulo(self.sf)
        self.sf = sf
        return Rotate(self.aguja, angle=d, about_point=self.c)


# Ec. 2 (dos pasadas) contra la modulación corregida (una pasada, fase con k/2): FER del detector de
# preámbulo completo (SF = 8, canal plano, hasta 2.000 tramas por punto) y errores del inicio a −18 dB
# en 1.500 tramas. Salen de correr el paquete `lora` del cuaderno (Ec. 2) y el de la rama corregida.
CMP_SNR = (-24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10)
CMP_FER_EC2 = (0.968, 0.938, 0.845, 0.698, 0.465, 0.243, 0.161, 0.136, 0.101, 0.0522, 0.0308, 0.021, 0.0085, 0.001, 0.001)
CMP_FER_CORR = (0.984, 0.857, 0.723, 0.496, 0.247, 0.118, 0.0587, 0.0313, 0.0165, 0.005, 0.002, 0.001, 0.0, 0.0, 0.0)
CMP_M18 = {"ec2": {"no": 12, "mal": 295, "medio": 227}, "corr": {"no": 11, "mal": 75, "medio": 0}}
CMP_PLUTO_MEDIO = {"ec2": 81, "corr": 0}     # tramas con el inicio a ±128 muestras en las capturas


def peine_preambulo(corregida: bool, M: int = 64, n: int = 8) -> np.ndarray:
    """Parecido T[k] sin ruido de un preámbulo de `n` chirps con su plantilla, normalizado al pico,
    para k de −3 a +3 símbolos alrededor del inicio (6·M + 1 valores)."""
    c = chirp_una_pasada(0, M) if corregida else chirp_lora(0, M)
    pl = np.tile(c, n)
    x = np.concatenate([np.zeros(3 * M, complex), pl, np.zeros(3 * M, complex)])
    T = np.abs(np.correlate(x, pl, mode="valid")) ** 2
    return T / T[3 * M]
