"""Escena 20 — Neyman-Pearson (2): de «una falsa alarma por minuto» a la probabilidad y al umbral."""
from comun.escena import *
from comun.figuras_lora import *


def _expo(x0, y0, ancho, alto, t_max=6.0, desde=0.0):
    """Puntos de e^(−t) sobre un eje que empieza en (x0, y0)."""
    t = np.linspace(desde, t_max, 80)
    return [np.array([x0 + v / t_max * ancho, y0 + alto * np.exp(-v), 0.0]) for v in t]


def _curva(pts, color=RUIDO, grosor=4):
    m = VMobject(stroke_color=color, stroke_width=grosor).set_fill(opacity=0)
    m.set_points_as_corners(pts)
    m.permitir_encima = True
    return m


class CuantasFalsasAlarmas(EscenaCurso):
    ESCENA = "20"

    def construct(self):
        self.por_minuto()
        self.probabilidad()
        self.por_que_no_cero()
        self.umbral()
        self.wait(1.0)
        self.limpiar()

    def por_minuto(self):
        q = MathTex("P_{FA}", "=", "?", color=TXT).scale(1.8).move_to([-0.3, 2.9, 0])
        q[0].set_color(ERROR)
        q2 = Text("?", color=AMBAR, weight=BOLD).scale(1.4).move_to([1.9, 2.9, 0])
        rel = reloj().scale(1.5).move_to([-5.3, 2.8, 0])
        pts = VGroup(*[Dot([-5.5 + i, 0.5, 0], radius=0.12, color=MEDIDA) for i in range(12)])
        pregs = VGroup(*[Text("?", color=AMBAR, weight=BOLD).scale(0.55).next_to(p, UP, buff=0.15) for p in pts])
        khz = MathTex("B", "=", r"125\ \mathrm{kHz}", color=TXT).scale(1.1).move_to([4.7, 2.9, 0])
        seg = Text("125.000 pruebas / s", color=TXT, weight=BOLD).scale(0.9).move_to([0, -1.1, 0])
        mnt = Text("× 60 = 7.500.000 / min", color=AMBAR, weight=BOLD).scale(0.9).move_to([0, -2.4, 0])
        with self.narrar("b1"):
            # «cuántas tolerar»
            self.en("cuantas")
            self.play(Write(q), run_time=self.dur(0.9))
            # «no dice mucho»
            self.en("nodice")
            self.pop(q2)
            # «pensarlo en tiempo»
            self.en("tiempo")
            self.pop(rel)
            # «una prueba por cada muestra»
            self.en("prueba")
            self.play(LaggedStart(*[FadeIn(VGroup(p, r), shift=LEFT * 0.3) for p, r in zip(pts, pregs)], lag_ratio=0.12),
                      run_time=self.dur(2.0))
            # «ciento veinticinco kilohercios»
            self.en("khz")
            self.play(Write(khz), run_time=self.dur(0.8))
            # «ciento veinticinco mil pruebas por segundo»
            self.en("seg")
            self.pop(seg)
            # «siete millones y medio por minuto»
            self.en("min")
            self.pop(mnt)

    def probabilidad(self):
        L = Lienzo(ancho=12.0, alto=1.5, t_rango=(0, 1), v_max=1.0, centro=(0, 2.5))
        g = np.random.default_rng(9)
        t = np.linspace(0, 1, 500)
        v = 0.3 * g.normal(0, 1, t.size)
        v[330] = 0.95
        ruido = L.curva(t, v, RUIDO, 2)
        ruido.permitir_encima = True
        fallo = Circle(radius=0.22, color=ERROR, stroke_width=5).move_to(L.p(t[330], 0.95))
        fallo.permitir_encima = True
        una = Text("1 falsa alarma por minuto", color=TXT, weight=BOLD).scale(0.85).move_to([0, 0.6, 0])
        f = MathTex("P_{FA}", "=", r"\frac{1}{7.500.000}", "=", r"1{,}3\cdot 10^{-7}", color=TXT).scale(1.5).move_to([0, -1.6, 0])
        f[0].set_color(ERROR)
        f[4].set_color(AMBAR)
        with self.narrar("b2"):
            # «escuchando solo ruido»
            self.en("solo")
            self.corte()
            self.play(Create(ruido, rate_func=linear), run_time=self.dur(1.4))
            # «que se equivoque»
            self.en("equivoque")
            self.play(Create(fallo), run_time=self.dur(0.5))
            self.sfx("error")
            # «una vez por minuto»
            self.en("una")
            self.pop(una)
            # «una vez de cada siete millones y medio»
            self.en("frac")
            self.play(Write(f[2]), run_time=self.dur(1.2))
            # «la probabilidad de falsa alarma»
            self.en("prob")
            self.play(FadeIn(f[0]), FadeIn(f[1]), run_time=self.dur(0.5))
            # «uno coma tres por diez a la menos siete»
            self.en("pfa")
            self.play(FadeIn(f[3]), run_time=0.2)
            self.pop(f[4])

    def por_que_no_cero(self):
        cero = MathTex("P_{FA}", "=", "0", color=TXT).scale(1.5).move_to([-4.4, 3.1, 0])
        tac = tachar(cero)
        x0, y0, an, al = -6.4, -0.4, 5.6, 2.6
        eje = Line([x0, y0, 0], [x0 + an + 0.2, y0, 0], color=INK, stroke_width=2.5)
        curva = _curva(_expo(x0, y0, an, al))
        cola = area_bajo(_expo(x0, y0, an, al, desde=2.0), y0, ERROR, 0.85)
        cola.permitir_encima = True
        um = Line([x0 + 2 / 6 * an, y0, 0], [x0 + 2 / 6 * an, y0 + 1.6, 0], color=TXT, stroke_width=4)
        coste = Text("Coste", color=AMBAR, weight=BOLD).scale(1.0).move_to([3.7, 3.1, 0])
        dem = bloque("Demodulador", AZUL, ancho=3.2, alto=0.95, escala=0.6).move_to([3.7, 1.7, 0])
        basura = Text("137 · 52 · 201 · 9 …", color=INK, weight=BOLD).scale(0.6).move_to([3.7, 0.7, 0])
        trama = VGroup(Rectangle(width=2.2, height=0.7, color=SENAL, stroke_width=3).set_fill(SENAL, 0.35))
        trama.add(Text("Trama", color=TXT, weight=BOLD).scale(0.5).move_to(trama[0]))
        trama.move_to([-5.6, -2.3, 0])
        elig = Text("1 por minuto", color=TXT, weight=BOLD).scale(0.75).move_to([3.7, -0.5, 0])
        dis = Text("Decisión de diseño", color=AMBAR, weight=BOLD).scale(0.65).move_to([3.7, -1.3, 0])
        with self.narrar("b3"):
            # «pedir cero»
            self.en("cero")
            self.corte()
            self.play(Write(cero), run_time=0.5)
            self.play(Create(tac), run_time=self.dur(0.4))
            # «nunca llega a cero»
            self.en("cola")
            self.play(Create(eje), Create(curva, rate_func=linear), run_time=self.dur(1.2))
            # «ninguna falsa alarma»
            self.en("ninguna")
            self.play(FadeIn(cola), FadeIn(um), run_time=self.dur(0.6))
            # «perder también las tramas»
            self.en("perder")
            self.play(um.animate.shift(RIGHT * 3.6), FadeOut(cola), run_time=self.dur(1.5))
            # «un coste»
            self.en("coste")
            self.pop(coste)
            # «demodular ruido»
            self.en("demod")
            self.play(FadeIn(dem, shift=DOWN * 0.2), run_time=0.4)
            self.play(FadeIn(basura, shift=DOWN * 0.2), run_time=self.dur(0.6))
            # «una de verdad»
            self.en("verdad")
            self.play(trama.animate.shift(RIGHT * 11.2), run_time=self.dur(1.8), rate_func=linear)
            # «la tolerancia que eligió el cuaderno»
            self.en("eligio")
            self.pop(elig)
            # «decisión de diseño»
            self.en("diseno")
            self.pop(dis)

    def umbral(self):
        conv = MathTex("P_{FA}", r"\ \to\ ", r"\eta", color=TXT).scale(1.6).move_to([-4.0, 3.1, 0])
        conv[0].set_color(ERROR)
        conv[2].set_color(AMBAR)
        x0, y0, an, al = -6.4, -1.6, 5.2, 3.0
        eje = Line([x0, y0, 0], [x0 + an + 0.2, y0, 0], color=INK, stroke_width=2.5)
        curva = _curva(_expo(x0, y0, an, al))
        xe = x0 + 2.2 / 6 * an
        cola = area_bajo(_expo(x0, y0, an, al, desde=2.2), y0, ERROR, 0.85)
        cola.permitir_encima = True
        um = Line([xe, y0, 0], [xe, y0 + 1.7, 0], color=AMBAR, stroke_width=4)
        re = MathTex(r"\eta", color=AMBAR).scale(1.2).move_to([xe, y0 + 2.05, 0])
        f = MathTex(r"P(T > \eta \mid H_0)", "=", r"e^{-\eta / 8\sigma^{2}}", "=", "P_{FA}", color=TXT).scale(1.1)
        f.move_to([2.9, 2.6, 0])
        f[4].set_color(ERROR)
        fl = Arrow([2.9, 1.95, 0], [2.9, 1.2, 0], color=INK, stroke_width=5, buff=0)
        e = MathTex(r"\eta", "=", r"-8\sigma^{2}\,\ln P_{FA}", color=TXT).scale(1.4).move_to([2.9, 0.4, 0])
        e[0].set_color(AMBAR)
        num = MathTex("P_{FA}", "=", r"1{,}3\cdot 10^{-7}", color=INK).scale(0.95).move_to([2.9, -0.9, 0])
        ln = MathTex(r"\ln P_{FA}", "=", "-15{,}8", color=TXT).scale(1.1).move_to([2.9, -1.8, 0])
        fin = MathTex(r"\eta", r"\approx", r"16 \times \text{Media}", color=VERDE).scale(1.4).move_to([2.9, -3.1, 0])
        with self.narrar("b4"):
            # «convertir esa probabilidad en un umbral»
            self.en("convertir")
            self.corte()
            self.play(Write(conv), run_time=self.dur(0.9))
            # «la cola es fácil»
            self.en("cola")
            self.play(Create(eje), Create(curva, rate_func=linear), run_time=0.8)
            self.play(FadeIn(um), FadeIn(re), FadeIn(cola), run_time=self.dur(0.6))
            # «e elevado a menos ese valor dividido por la media»
            self.en("formula")
            self.play(Write(f[:3]), run_time=self.dur(1.5))
            # «La igualamos»
            self.en("iguala")
            self.play(FadeIn(f[3]), run_time=0.2)
            self.pop(f[4], sonido=None)
            # «despejamos»
            self.en("despeja")
            self.play(GrowArrow(fl), run_time=self.dur(0.5))
            # «menos la media por el logaritmo»
            self.en("eta")
            self.play(Write(e), run_time=self.dur(1.2))
            # «Con nuestros números»
            self.en("numeros")
            self.play(FadeIn(num, shift=UP * 0.15), run_time=self.dur(0.5))
            # «menos quince coma ocho»
            self.en("ln")
            self.play(Write(ln), run_time=self.dur(0.9))
            # «dieciséis veces»
            self.en("dieciseis")
            self.pop(fin, sonido="exito")
