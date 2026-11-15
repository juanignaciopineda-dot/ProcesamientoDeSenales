"""Escena 03 — Dos grabaciones de ruido, a las 10 y a las 17: distintas, pero con la misma estadística."""
from comun.escena import *


class DosGrabaciones(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        t = np.linspace(0, 1, 260)
        L1 = Lienzo(ancho=9.0, alto=2.0, t_rango=(0, 1), v_max=2.6, centro=(-1.3, 1.7))
        L2 = Lienzo(ancho=9.0, alto=2.0, t_rango=(0, 1), v_max=2.6, centro=(-1.3, -0.7))
        b1, b2 = L1.base(), L2.base()
        c1 = L1.curva(t, serie(21, 260, 0.8), RUIDO, 3.2)
        c2 = L2.curva(t, serie(22, 260, 0.8), RUIDO, 3.2)
        r1, r2 = reloj().move_to([5.6, 1.9, 0]), reloj().move_to([5.6, -0.5, 0])
        h1 = etiqueta("10:00", TXT, 0.5).next_to(r1, DOWN, buff=0.12)
        h2 = etiqueta("17:00", TXT, 0.5).next_to(r2, DOWN, buff=0.12)
        r2.minutero.rotate(PI / 3, about_point=r2.aro.get_center())
        bandas = [Rectangle(width=9.0, height=1.53, color=AMBAR, stroke_width=0).set_fill(AMBAR, 0.12).move_to(L.p(0.5, 0))
                  for L in (L1, L2)]

        with self.narrar("b1"):
            # «hoy a las diez»
            self.en("diez")
            self.play(Create(b1), FadeIn(r1), FadeIn(h1), run_time=0.3)
            self.play(Create(c1), run_time=self.dur(1.3), rate_func=linear)

            # «mañana a las cinco»
            self.en("cinco")
            self.play(Create(b2), FadeIn(r2), FadeIn(h2), run_time=0.3)
            self.play(Create(c2), run_time=self.dur(1.3), rate_func=linear)

            # «distintas»
            self.en("distintas")
            neq = Text("≠", color=ROJO, weight=BOLD).scale(1.5).move_to([5.6, 0.7, 0])
            self.pop(neq)

            # «el mismo murmullo»
            self.en("murmullo")
            recs = [Rectangle(width=1.7, height=1.5, color=AMBAR, stroke_width=3.5).move_to(L.p(0.45, 0)) for L in (L1, L2)]
            self.play(*[Create(r) for r in recs], run_time=self.dur(0.5))

            # «igual de fuerte»
            self.en("fuerte")
            self.play(*[FadeIn(b) for b in bandas], run_time=self.dur(0.5))

            # «la misma textura»
            self.en("textura")
            self.resaltar(c1, c2, escala=1.02)

            # «no depende de la hora»
            self.en("hora")
            self.play(Rotate(r1.minutero, angle=-2 * PI, about_point=r1.aro.get_center()),
                      Rotate(r2.minutero, angle=-2 * PI, about_point=r2.aro.get_center()),
                      run_time=self.dur(1.4), rate_func=linear)

            # «las mires»
            self.en("mires")
            o = ojo().scale(0.5).move_to([6.3, 0.7, 0])
            o.permitir_encima = True
            self.play(FadeIn(o), run_time=0.3)

            # «estacionariedad»
            self.en("estac")
            p = self.palabra("estacionariedad", AMBAR, 1.1).move_to([0, -2.5, 0])
            self.pop(p)

            # «dos versiones»
            self.en("dos_v")
            ca = caja("estricta", AZUL, ancho=2.8, alto=0.7).move_to([-2.2, -3.45, 0])
            cb = caja("amplia", VERDE, ancho=2.8, alto=0.7).move_to([2.2, -3.45, 0])
            self.play(FadeIn(ca, shift=UP * 0.2), FadeIn(cb, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)
        self.limpiar()
