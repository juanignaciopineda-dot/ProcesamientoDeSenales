"""Escena 15 — La uniforme: todos los valores del intervalo igual de probables."""
from comun.escena import *


class Uniforme(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        g, huecos, centros = huecos_tres(["Bernoulli"])
        self.add(g)
        ax = Axes(x_range=[0, 5, 1], y_range=[0, 1.0, 0.25], x_length=7.4, y_length=3.0,
                  axis_config={"color": INK, "stroke_width": 2, "include_ticks": False,
                               "tip_width": 0.16, "tip_height": 0.16}).move_to([-1.6, -1.1, 0])
        a, b = 1.0, 4.0
        h = 1 / (b - a)
        rect = Rectangle(width=ax.c2p(b, 0)[0] - ax.c2p(a, 0)[0], height=ax.c2p(0, h)[1] - ax.c2p(0, 0)[1],
                         stroke_color=SENAL, stroke_width=4, fill_color=SENAL, fill_opacity=0.3)
        rect.move_to([(ax.c2p(a, 0)[0] + ax.c2p(b, 0)[0]) / 2, (ax.c2p(0, 0)[1] + ax.c2p(0, h)[1]) / 2, 0])

        with self.narrar("b1"):
            self.en("uniforme")                               # «la uniforme»
            nom = Text("Uniforme", color=AMBAR, weight=BOLD).scale(0.65).move_to(centros[1])
            self.pop(nom)
            self.en("entre")                                  # «entre a y b»
            ta = formula("a", colores={0: AMBAR}).next_to(ax.c2p(a, 0), DOWN, buff=0.15)
            tb = formula("b", colores={0: VERDE}).next_to(ax.c2p(b, 0), DOWN, buff=0.15)
            self.play(Create(ax), FadeIn(ta), FadeIn(tb), run_time=self.dur(0.8))
            self.en("iguales")                                # «igual de probables»
            xs = [1.4, 2.0, 2.7, 3.5]
            pts = VGroup(*[Dot(ax.c2p(x, h), radius=0.1, color=AMBAR) for x in xs])
            self.play(LaggedStart(*[FadeIn(p, scale=2) for p in pts], lag_ratio=0.25), run_time=self.dur(1.2))
            self.en("rect")                                   # «un rectángulo plano»
            self.play(FadeOut(pts), Create(rect), run_time=self.dur(0.9))
            self.en("altura")                                 # «¿Qué altura tiene?»
            alt = formula("h", "=", "?", escala=1.0, colores={0: AMBAR, 2: AMBAR}).next_to(rect, UP, buff=0.25)
            self.play(Write(alt), run_time=self.dur(0.7))
            self.en("area_uno")                               # «El área total tiene que ser uno»
            au = Text("Área = 1", color=AMBAR, weight=BOLD).scale(0.55).move_to(rect)
            self.play(FadeIn(au), run_time=self.dur(0.5))
            self.en("ancho_alto")                             # «ancho por alto»
            f1 = formula("(b-a)", r"\cdot", "h", "=", "1", escala=1.2, colores={0: VERDE, 2: AMBAR})
            f1.move_to([2.6, 0.9, 0])
            self.play(LaggedStart(*[Write(p) for p in f1], lag_ratio=0.2), run_time=self.dur(1.5))
            self.en("division")                               # «uno dividido entre el ancho»
            f2 = formula("h", "=", r"\frac{1}{b-a}", escala=1.2, colores={0: AMBAR, 2: VERDE}).move_to([2.6, 0.9, 0])
            hh = formula(r"\frac{1}{b-a}", escala=0.9, colores={0: AMBAR}).move_to(alt).shift(UP * 0.3)
            self.play(ReplacementTransform(f1, f2), ReplacementTransform(alt, hh), FadeOut(au), run_time=self.dur(1.2))
            self.en("b_menos_a")                              # «b menos a»
            br = Brace(Line(ax.c2p(a, 0), ax.c2p(b, 0)), DOWN, color=VERDE, buff=0.55)
            self.play(Create(br), run_time=self.dur(0.6))
            self.en("aparece")                                # «Aparece cuando»
            todo = VGroup(ax, rect, ta, tb, hh, br)
            self.play(FadeOut(f2), todo.animate.scale(0.78).move_to([-3.6, -1.2, 0]), run_time=self.dur(0.8))
            self.en("sitio")                                  # «cualquier sitio»
            punto = Dot(rect.get_left() + RIGHT * 0.2, radius=0.1, color=AMBAR)
            self.add(punto)
            for fr in (0.8, 0.3, 0.6):
                self.play(punto.animate.move_to(rect.get_left() + RIGHT * rect.width * fr), run_time=self.dur(0.4))
            self.en("redondear")                              # «redondear una señal»
            L = Lienzo(ancho=6.0, alto=2.6, t_rango=(0, 1), v_max=1.3, centro=(3.0, -1.0))
            t = np.linspace(0, 1, 160)
            v = np.sin(2 * np.pi * t)
            q = np.round(v * 3) / 3
            sen = L.curva(t, v, SENAL, 4)
            esc = L.curva(t, q, AMBAR, 3)
            err = VGroup(*[Line(L.p(tt, vv), L.p(tt, qq), color=RUIDO, stroke_width=2.5)
                           for tt, vv, qq in zip(t[::6], v[::6], q[::6])])
            self.play(FadeOut(punto), Create(sen), run_time=self.dur(0.7))
            self.play(Create(esc), FadeIn(err), run_time=self.dur(1.0))
        self.wait(1.0)
        self.limpiar()
