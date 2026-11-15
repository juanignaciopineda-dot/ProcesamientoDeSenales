"""Escena 14 — La pregunta: coherencia de dos grabaciones sin relación, con un solo trozo."""
from comun.escena import *


class LaTrampaDeUnSoloTrozo(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        # el registro partido en trozos que se promedian
        Lr = Lienzo(ancho=8.0, alto=1.2, t_rango=(0, 4), v_max=1.0, centro=(-1.6, 2.6))
        reg = ruido_t(Lr, semilla=3, amp=0.22, color=CIAN, puntos=240)
        cortes = VGroup(*[Line([Lr.x(x), 3.25, 0], [Lr.x(x), 1.95, 0], color=INK, stroke_width=2) for x in (1, 2, 3)])
        prom = caja("promedio", AMBAR, ancho=2.2, alto=0.8, scale=0.5).move_to([5.1, 2.6, 0])
        fl = flecha([2.5, 2.6, 0], [3.9, 2.6, 0])
        aviso = Triangle(color=ROJO, stroke_width=6).scale(0.5).set_fill(ROJO, 0.2).move_to([6.2, 0.4, 0])
        adm = Text("!", color=ROJO, weight=BOLD).scale(0.6).move_to(aviso.get_center() + DOWN * 0.05)
        # dos grabaciones sin relación
        L1 = Lienzo(ancho=8.0, alto=1.2, t_rango=(0, 4), v_max=1.0, centro=(-1.6, 0.9))
        L2 = Lienzo(ancho=8.0, alto=1.2, t_rango=(0, 4), v_max=1.0, centro=(-1.6, -0.5))
        g1 = ruido_t(L1, semilla=7, amp=0.22, color=CIAN, puntos=240)
        g2 = ruido_t(L2, semilla=12, amp=0.22, color=MAGENTA, puntos=240)
        sinrel = etiqueta("sin relación", INK, 0.55).move_to([5.4, 0.2, 0])
        marcos = VGroup(*[Rectangle(width=2.0, height=1.0, color=AMBAR, stroke_width=4).move_to([Lr.x(0.5), y, 0])
                          for y in (0.9, -0.5)])
        opciones = VGroup(*[caja(t, c, ancho=1.5, alto=0.9, scale=0.7) for t, c in
                            [("0", AZUL), ("0,5", CIAN), ("1", ROJO)]]).arrange(RIGHT, buff=0.9).move_to([-1.6, -2.4, 0])
        pausa = Circle(radius=0.4, color=AMBAR, stroke_width=5).move_to([-1.6, -3.5, 0])
        l_p = Text("piénsalo", color=INK).scale(0.4).move_to([0.2, -3.5, 0])
        with self.narrar("b1"):
            # «partiendo en trozos y promediando»
            self.en("trozos")
            self.corte()
            self.play(Create(Lr.base()), Create(reg), run_time=self.dur(1.0), rate_func=linear)
            self.play(Create(cortes), run_time=0.4)
            self.play(GrowArrow(fl), FadeIn(prom), run_time=self.dur(0.6))

            # «una trampa»
            self.en("trampa")
            self.play(FadeIn(aviso), FadeIn(adm), run_time=self.dur(0.5))
            self.sfx("alarma", gain=-20)

            # «dos grabaciones»
            self.en("dos")
            self.corte()
            self.play(Create(L1.base()), Create(g1), Create(L2.base()), Create(g2),
                      run_time=self.dur(1.3), rate_func=linear)

            # «nada que ver»
            self.en("sinrel")
            self.play(FadeIn(sinrel), run_time=self.dur(0.5))

            # «con un solo trozo»
            self.en("uno")
            self.play(Create(marcos), run_time=self.dur(0.6))

            # «¿Qué sale»
            self.en("encuesta")
            self.play(LaggedStart(*[FadeIn(o) for o in opciones], lag_ratio=0.3), run_time=self.dur(0.9))

            # «cero, cero coma cinco, o uno»
            self.en("opciones")
            for o in opciones:
                self.resaltar(o, color=AMBAR, run_time=0.5)

            # «Piénsalo»
            self.en("piensa")
            self.play(Create(pausa), FadeIn(l_p), run_time=self.dur(5.0), rate_func=linear)

        self.wait(1.0)
        self.limpiar()
