"""Escena 13 — La covarianza solo ve lo que va en línea recta."""
from comun.escena import *


class SoloLoLineal(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        ax, et = ejes((-1.3, 1.3, 1), (-0.2, 1.3, 1), ancho=7.0, alto=4.6, x_label="x", y_label="y")
        g = VGroup(ax, et).move_to([-2.8, -0.6, 0])
        curva = ax.plot(lambda x: x * x, x_range=[-1, 1, 0.02], color=SENAL, stroke_width=4)
        pts = VGroup(*[Dot(ax.c2p(x, x * x), radius=0.07, color=SENAL) for x in np.linspace(-1, 1, 33)])
        with self.narrar("b1"):
            # «Dependencia total»
            self.en("dep_total")
            s = sello("Dependencia total", ROJO).scale(1.1).move_to([4.5, 2.9, 0])
            self.pop(s)

            # «covarianza cero»
            self.en("cov_cero")
            c0 = formula(r"\sigma_{XY}", "=", "0", escala=1.7, colores={0: AMBAR, 2: AMBAR}).move_to([4.5, 1.5, 0])
            self.pop(c0)

            # «¿Cómo puede ser?»
            self.en("como")
            q = Text("?", color=AMBAR, weight=BOLD).scale(2.6).move_to([4.5, 0.0, 0])
            self.pop(q)

            # «Mira la parábola»
            self.en("mira")
            self.play(FadeOut(q), Create(g), run_time=self.dur(0.5))
            self.play(Create(curva), FadeIn(pts), run_time=self.dur(0.9))

            # «En la mitad izquierda»
            self.en("mitad_izq")
            fi = Arrow(ax.c2p(-0.95, 0.9), ax.c2p(-0.3, 0.09), color=ROJO, stroke_width=8, buff=0)
            self.play(GrowArrow(fi), run_time=self.dur(0.6))

            # «i griega baja»
            self.en("baja_y")
            lb = Text("Baja la y", color=ROJO).scale(0.6).move_to(ax.c2p(-0.38, 0.72))
            self.play(FadeIn(lb), run_time=self.dur(0.4))

            # «En la mitad derecha»
            self.en("mitad_der")
            fd = Arrow(ax.c2p(0.3, 0.09), ax.c2p(0.95, 0.9), color=VERDE, stroke_width=8, buff=0)
            self.play(GrowArrow(fd), run_time=self.dur(0.6))

            # «i griega sube»
            self.en("sube_y")
            ls = Text("Sube la y", color=VERDE).scale(0.6).move_to(ax.c2p(0.38, 0.72))
            self.play(FadeIn(ls), run_time=self.dur(0.4))

            # «solo pregunta si»
            self.en("pregunta")
            p = Text("¿Suben o bajan juntas?", color=AMBAR).scale(0.65).move_to([4.5, -1.1, 0])
            self.play(FadeIn(p, shift=UP * 0.2), run_time=self.dur(0.6))

            # «en conjunto»
            self.en("conjunto")
            self.resaltar(fi, fd, color=AMBAR, escala=1.05)

            # «Y las dos mitades»
            self.en("mitades")
            self.resaltar(lb, ls, color=AMBAR, escala=1.2)

            # «se cancelan»
            self.en("cancelan")
            cero = Text("0", color=AMBAR, weight=BOLD).scale(2.4).move_to([4.5, -2.7, 0])
            self.play(fi.animate.set_opacity(0.3), fd.animate.set_opacity(0.3), run_time=self.dur(0.4))
            self.pop(cero)

            # «no hay una tendencia en línea recta»
            self.en("plana")
            plana = Line(ax.c2p(-1.2, 1 / 3), ax.c2p(1.2, 1 / 3), color=ESTIMACION, stroke_width=5)
            self.play(Create(plana), run_time=self.dur(0.7))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        rot = Text("Covarianza = relación en línea recta", color=AMBAR).scale(0.8).move_to([0, 3.4, 0])
        ax, et = ejes((-3, 3, 1), (-3, 3, 1), ancho=5.4, alto=4.2, x_label="x", y_label="y")
        g = VGroup(ax, et).move_to([-3.2, -0.5, 0])
        a, b = puntos_corr(0.85, 28, 21)
        nube = VGroup(*[Dot(ax.c2p(np.clip(x, -2.4, 2.4), np.clip(y, -2.4, 2.4)), radius=0.09, color=SENAL)
                        for x, y in zip(a, b)])
        recta = Line(ax.c2p(-2.7, -2.7), ax.c2p(2.7, 2.7), color=ESTIMACION, stroke_width=5)
        ax2, et2 = ejes((-1.3, 1.3, 1), (-0.2, 1.3, 1), ancho=5.4, alto=4.2, x_label="x", y_label="y")
        g2 = VGroup(ax2, et2).move_to([-3.2, -0.5, 0])
        par = VGroup(*[Dot(ax2.c2p(x, x * x), radius=0.08, color=SENAL) for x in np.linspace(-1, 1, 33)],
                     ax2.plot(lambda x: x * x, x_range=[-1, 1, 0.02], color=SENAL, stroke_width=4))
        with self.narrar("b2"):
            # «la covarianza solo detecta»
            self.en("detecta")
            self.play(*[FadeOut(m) for m in list(self.mobjects) if m is not self.camera.frame], run_time=0.3)
            self.play(FadeIn(rot, shift=DOWN * 0.2), Create(g), FadeIn(nube), run_time=self.dur(0.7))

            # «la parte en línea recta»
            self.en("recta")
            self.play(Create(recta), run_time=self.dur(0.7))

            # «Si la relación es una curva»
            self.en("curva")
            self.play(FadeOut(VGroup(g, nube, recta)), Create(g2), FadeIn(par), run_time=self.dur(0.9))

            # «puede no verla en absoluto»
            self.en("no_ve")
            o = ojo().scale(1.1).move_to([3.8, -1.6, 0])
            self.play(FadeIn(o), run_time=self.dur(0.4))
            self.play(Create(tachar(o)), run_time=self.dur(0.4))

            # «Por eso»
            self.en("por_eso")
            self.resaltar(rot, color=TXT, escala=1.03)

            # «covarianza cero se dice»
            self.en("se_dice")
            c0 = formula(r"\sigma_{XY}", "=", "0", escala=1.3, colores={0: AMBAR, 2: AMBAR}).move_to([3.4, 2.85, 0])
            self.pop(c0)

            # «no correlacionadas»
            self.en("no_corr")
            nc = Text("No correlacionadas", color=AMBAR, weight=BOLD).scale(0.8).move_to([3.4, 1.9, 0])
            self.pop(nc)

            # «independientes»
            self.en("no_indep")
            ni = Text("Independientes", color=TXT, weight=BOLD).scale(0.8).move_to([3.4, 0.4, 0])
            self.play(FadeIn(ni), Create(tachar(ni)), run_time=self.dur(0.5))

            # «No es lo mismo»
            self.en("distinto")
            ne = MathTex(r"\neq", color=ROJO).scale(1.8).move_to([3.4, 1.15, 0])
            self.pop(ne)
