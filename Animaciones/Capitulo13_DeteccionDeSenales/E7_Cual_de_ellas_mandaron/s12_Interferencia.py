"""Escena 12 — Pulsos que se pisan: PAM, interferencia entre símbolos, Nyquist y el filtro adaptado con ruido."""
from comun.escena import *

TS = [1.0, 2.0, 3.0]
SG = [1.0, 1.0, 1.0]
T = np.linspace(0, 4, 300)


def gauss(t0, sg):
    return lambda t: np.exp(-0.5 * ((t - t0) / sg) ** 2)


def sinc_p(t0):
    return lambda t: np.sinc(t - t0)


class Interferencia(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.pulsos()
        self.wait(0.5)
        self.con_ruido()
        self.wait(1.0)
        self.limpiar()

    def pulsos(self):
        L = Lienzo(ancho=10.0, alto=2.8, t_rango=(0, 4), v_max=1.6, centro=(0.0, -0.7))
        base = L.base()
        mod = modem7(INK).scale(0.9).move_to([-5.6, 2.9, 0])
        mini = traza(np.linspace(-4.4, -3.2, 40), 2.7 + 0.5 * np.exp(-0.5 * ((np.linspace(-4.4, -3.2, 40) + 3.8) / 0.18) ** 2),
                     SENAL, 3.5)
        sal = Arrow([-4.9, 2.75, 0], [-4.5, 2.75, 0], buff=0, color=INK, stroke_width=3, max_tip_length_to_length_ratio=0.5)
        sim = VGroup(*[MathTex("+1" if s > 0 else "-1", color=SENAL if s > 0 else AZUL_C7).scale(0.95)
                       .move_to([L.x(t), 1.15, 0]) for t, s in zip(TS, SG)])

        def pulso(f, t0, s, col):
            return L.curva(T, s * f(T), col, 4)

        angosto = [pulso(gauss(t, 0.14), t, s, SENAL if s > 0 else AZUL_C7) for t, s in zip(TS, SG)]
        anchos = [pulso(gauss(t, 0.5), t, s, SENAL if s > 0 else AZUL_C7) for t, s in zip(TS, SG)]
        total = L.curva(T, sum(s * gauss(t, 0.5)(T) for t, s in zip(TS, SG)), AMBAR, 5)
        sampling = L.vertical(2.0, AMBAR, 3.0, mitad=1.25)
        # colas de los vecinos en el instante del símbolo central
        colas = VGroup(*[Dot(L.p(2.0, gauss(t, 0.5)(2.0)), radius=0.11, color=ERROR) for t in (1.0, 3.0)])
        isi = etiqueta("interferencia entre símbolos", ERROR, 0.6, BOLD).move_to([3.0, 2.9, 0])
        nyq = etiqueta("criterio de Nyquist", AMBAR, 0.6, BOLD).move_to([3.0, 2.2, 0])
        sincs = [pulso(sinc_p(t), t, s, SENAL if s > 0 else AZUL_C7) for t, s in zip(TS, SG)]
        total_s = L.curva(T, sum(s * np.sinc(T - t) for t, s in zip(TS, SG)), AMBAR, 5)
        uno = VGroup(Dot(L.p(2.0, 1.0), radius=0.11, color=VERDE),
                     MathTex("1", color=VERDE).scale(1.0).move_to(L.p(2.0, 1.0) + RIGHT * 0.6 + UP * 0.35))
        ceros = VGroup(*[Dot(L.p(t, 0.0), radius=0.11, color=VERDE) for t in (1.0, 3.0)])
        with self.narrar("b1"):
            # «Un módem envía un pulso»
            self.en("envia")
            self.play(FadeIn(mod), FadeIn(sal), Create(mini), FadeIn(base), run_time=self.dur(0.8))
            # «por cada símbolo»
            self.paso("simbolo", sim, t=0.6)
            # «uno detrás de otro»
            self.en("detras")
            self.play(*[Create(p) for p in angosto], run_time=self.dur(1.0))
            # «PAM»
            self.en("pam")
            self.pop(Text("PAM", color=AMBAR, weight=BOLD).scale(0.9).move_to([-4.4, 1.9, 0]))
            # «si los pulsos son largos»
            self.en("largos")
            self.play(*[ReplacementTransform(a, b) for a, b in zip(angosto, anchos)], run_time=self.dur(0.8))
            # «se solapan»
            self.paso("solapan", total, t=0.7)
            # «cada símbolo se mezcla con sus vecinos»
            self.en("mezcla")
            self.play(Create(sampling), FadeIn(colas), run_time=self.dur(0.7))
            # «interferencia entre símbolos»
            self.paso("isi", isi, t=0.6)
            # «El criterio de Nyquist»
            self.paso("nyquist", nyq, t=0.6)
            # «valga uno en su instante de muestreo»
            self.en("uno")
            self.play(FadeOut(colas), *[ReplacementTransform(a, b) for a, b in zip(anchos, sincs)],
                      ReplacementTransform(total, total_s), FadeIn(uno), run_time=self.dur(1.0))
            # «cero en los instantes de todos los demás»
            self.paso("cero", ceros, t=0.6)
        self.corte()

    def con_ruido(self):
        # sin ruido: un pulso limpio con ceros; luego el ruido; después la cadena y el filtro adaptado
        Ls = Lienzo(ancho=4.4, alto=1.6, t_rango=(0, 4), v_max=1.2, centro=(-3.6, 2.6))
        limpio = Ls.curva(T, np.sinc(T - 2.0), SENAL, 4)
        base_s = Ls.base()
        ceros = VGroup(*[Dot(Ls.p(t, 0.0), radius=0.07, color=VERDE) for t in (1.0, 3.0)])
        lap = lapiz(AMBAR).scale(0.8).move_to([-1.0, 2.0, 0])
        sin_r = etiqueta("sin ruido", INK, 0.5).move_to([-3.6, 3.65, 0])
        Lr = Lienzo(ancho=4.4, alto=1.6, t_rango=(0, 4), v_max=1.2, centro=(3.6, 2.6))
        rr = ruido_t(Lr, semilla=7, amp=0.35, color=RUIDO)
        con_r = etiqueta("con ruido", INK, 0.5).move_to([3.6, 3.65, 0])
        base_r = Lr.base()
        r_curva = Lr.curva(T, np.sinc(T - 2.0), SENAL, 3)
        # cadena transmisor → canal → receptor
        tx = caja("transmisor", SENAL, ancho=2.4, alto=0.8, scale=0.5).move_to([-5.0, -0.6, 0])
        ca = caja("canal", INK, ancho=1.8, alto=0.8, scale=0.5).move_to([-0.8, -0.6, 0])
        rx = caja("receptor", AMBAR, ancho=2.4, alto=0.8, scale=0.5).move_to([4.2, -0.6, 0])
        a1 = Arrow([-3.75, -0.6, 0], [-1.75, -0.6, 0], buff=0.05, color=INK, stroke_width=3)
        a2 = Arrow([0.15, -0.6, 0], [2.95, -0.6, 0], buff=0.05, color=INK, stroke_width=3)
        t_p = MathTex("P", color=SENAL).scale(1.0).move_to([-5.0, 0.35, 0])
        t_h = MathTex("H_c", color=INK).scale(1.0).move_to([-0.8, 0.35, 0])
        t_ph = MathTex(r"P\,H_c", color=SENAL).scale(1.0).move_to([1.55, -0.05, 0])
        t_cj = MathTex(r"\overline{P\,H_c}", color=AMBAR).scale(1.0).move_to([4.2, -1.65, 0])
        adapt = etiqueta("filtro adaptado", AMBAR, 0.55, BOLD).move_to([4.2, 0.25, 0])
        llega = etiqueta("el pulso que llega", SENAL, 0.5).move_to([1.55, -1.5, 0])
        fl_llega = Arrow([1.55, -1.25, 0], [1.55, -0.9, 0], buff=0, color=SENAL, stroke_width=3,
                         max_tip_length_to_length_ratio=0.5)
        with self.narrar("b2"):
            # «Sin ruido»
            self.en("sinruido")
            self.play(FadeIn(sin_r), FadeIn(base_s), Create(limpio), FadeIn(ceros), run_time=self.dur(0.9))
            # «diseñando un pulso»
            self.paso("disenando", lap, t=0.6)
            # «Con ruido»
            self.en("conruido")
            self.play(FadeOut(lap), FadeIn(con_r), FadeIn(base_r), Create(r_curva), Create(rr), run_time=self.dur(0.9))
            # «el receptor óptimo»
            self.paso("optimo", rx, t=0.6)
            # «el filtro adaptado»
            self.paso("adaptado", adapt, t=0.5)
            # «al pulso que llega»
            self.en("llega")
            self.play(FadeIn(llega), GrowArrow(fl_llega), run_time=self.dur(0.6))
            # «un pulso pe»
            self.en("pe")
            self.play(FadeIn(tx), GrowArrow(a1), FadeIn(t_p), run_time=self.dur(0.7))
            # «una respuesta hache de ce»
            self.paso("hc", ca, GrowArrow(a2), t_h, t=0.7)
            # «el pulso que llega es el producto»
            self.paso("producto", t_ph, t=0.6)
            # «El receptor tiene su conjugado»
            self.paso("conjugado", t_cj, t=0.7)
