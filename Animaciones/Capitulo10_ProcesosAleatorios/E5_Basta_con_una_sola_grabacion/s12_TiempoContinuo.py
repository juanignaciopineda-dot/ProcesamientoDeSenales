"""Escena 12 — Tiempo continuo, y qué decide si promediar funciona."""
from comun.escena import *


class TiempoContinuo(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        Lt = Lienzo(ancho=5.4, alto=2.4, t_rango=(-1, 1), v_max=1.0, centro=(-3.5, -0.4))
        Lc = Lienzo(ancho=5.4, alto=2.4, t_rango=(-1, 1), v_max=5.0, centro=(3.5, -0.4))
        tau = np.linspace(-1, 1, 160)
        tri = Polygon(Lt.p(-1, 0), Lt.p(0, 1.0), Lt.p(1, 0), color=AMBAR, stroke_width=4).set_fill(AMBAR, 0.0)
        fd = MathTex(r"\mathrm{Var}=\frac{1}{N^2}\sum_k(N-|k|)\,C[k]", color=TXT).scale(0.9).move_to([0, 3.4, 0])
        fc = MathTex(r"\mathrm{Var}=\frac{1}{T^2}\int(T-|\tau|)\,C(\tau)\,d\tau", color=TXT).scale(0.9).move_to([0, 2.3, 0])
        ej_c = VGroup(Lc.base(), Line(Lc.p(0, -0.3), Lc.p(0, 5.0), color=INK, stroke_width=2))
        ct = MathTex(r"C(\tau)", color=INK).scale(0.8).move_to(Lc.p(0.35, 4.9))
        ej_t = VGroup(Lt.base(), Line(Lt.p(0, -0.05), Lt.p(0, 1.15), color=INK, stroke_width=2))

        with self.narrar("b1"):
            # «tiempo continuo»
            self.en("continuo")
            self.play(FadeIn(fd), Create(ej_t), Create(tri), run_time=self.dur(0.9))

            # «una integral»
            self.en("integral")
            self.play(FadeIn(fc), run_time=0.6)

            # «en lugar de la suma»
            self.en("suma")
            tach = tachar(fd)
            self.play(Create(tach), run_time=0.4)

            # «qué lo decide todo»
            self.en("decide")
            self.play(Create(ej_c), FadeIn(ct), run_time=0.5)
            self.resaltar(ct, escala=1.3)

            # «Si la autocovarianza se queda grande»
            self.en("grande")
            alta = Line(Lc.p(0, 4), Lc.p(0.3, 4), color=AMBAR, stroke_width=6)
            self.play(Create(alta), run_time=0.4)

            # «en todas las separaciones»
            self.en("todas")
            alta2 = Line(Lc.p(-1, 4), Lc.p(1, 4), color=AMBAR, stroke_width=6)
            self.play(Create(alta2), run_time=self.dur(0.8))

            # «como en la pila»
            self.en("pila")
            pl = Group(pila("+2")).scale(0.9).move_to([6.2, 1.2, 0])
            self.play(FadeIn(pl, scale=0.6), run_time=0.4)

            # «el triángulo entero pesa»
            self.en("entero")
            self.play(tri.animate.set_fill(AMBAR, 0.45), run_time=0.6)

            # «la varianza no baja»
            self.en("nobaja")
            nb = MathTex(r"\mathrm{Var}=4", color=ROJO).scale(1.3).move_to([0, -3.3, 0])
            self.pop(nb)

            # «Pero si la autocovarianza»
            self.en("pero")
            self.play(FadeOut(alta), FadeOut(alta2), FadeOut(nb), FadeOut(pl), tri.animate.set_fill(AMBAR, 0.0),
                      run_time=0.4)

            # «se va apagando»
            self.en("apaga")
            cur = Lc.curva(tau, 4.0 * np.exp(-6 * np.abs(tau)), AMBAR, 5)
            self.play(Create(cur), run_time=self.dur(1.0))
            zona = Rectangle(width=Lt.ancho * 0.22, height=0.7, color=AMBAR, stroke_width=0).set_fill(AMBAR, 0.5)
            zona.move_to(Lt.p(0, 0.0)).align_to(Lt.p(0, 0), DOWN)
            self.play(FadeIn(zona), run_time=0.4)

            # «la cosa cambia»
            self.en("cambia")
            q = self.palabra("¿?", TXT, 1.6).move_to([0, -3.3, 0])
            self.pop(q)
        self.wait(1.0)
        self.limpiar()
