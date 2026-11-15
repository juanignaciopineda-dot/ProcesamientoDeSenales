"""Escena 16 — Wiener contra adaptado: estimar la forma frente a decidir si hay señal; los dos blanquean primero."""
from comun.escena import *


class WienerContraAdaptado(EscenaCurso):
    ESCENA = "16"

    def construct(self):
        cw = caja("Wiener · capítulo 12", AMBAR, ancho=4.8, alto=0.9, scale=0.55).move_to([-3.6, 3.2, 0])
        ca = caja("adaptado · capítulo 13", AMBAR, ancho=4.8, alto=0.9, scale=0.55).move_to([3.6, 3.2, 0])
        dbl = DoubleArrow([-1.0, 3.2, 0], [1.0, 3.2, 0], color=INK, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.25)
        neq = MathTex(r"\neq", color=ERROR).scale(1.3).move_to([0, 2.65, 0])
        # columna izquierda: seguir la forma
        n = 40
        t = np.arange(n)
        x = 0.8 * serie(5, n, 0.8)
        est = suavizada(x, 0.5)
        Lw = Lienzo(ancho=5.2, alto=1.8, t_rango=(0, n - 1), v_max=2.0, centro=(-3.6, 1.2))
        c_sig = Lw.curva(t, x, MEDIDA, 2.5, 0.8)
        c_est = Lw.curva(t, est, AMBAR, 4)
        pts = VGroup(*[Dot(Lw.p(k, est[k]), radius=0.06, color=AMBAR) for k in range(0, n, 3)])
        err = MathTex(r"\min\ E[e^2]", color=ERROR).scale(1.1).move_to([-3.6, -0.5, 0])
        # columna derecha: ¿hay?
        pul = pulso7([2, 2, 1], centro=(2.6, 1.2), color=SENAL, paso=0.6, unidad=0.4)
        hay = Text("¿hay?", color=AMBAR, weight=BOLD).scale(0.8).move_to([4.8, 1.2, 0])
        g = MathTex(r"g=10", color=AMBAR).scale(1.3).move_to([3.6, -0.5, 0])
        flecha_g = Arrow([3.6, 0.35, 0], [3.6, -0.0, 0], buff=0, color=INK, stroke_width=3, max_tip_length_to_length_ratio=0.5)
        # ruido con color y blanqueo
        Lr = Lienzo(ancho=6.0, alto=1.0, t_rango=(0, 80), v_max=2.0, centro=(0, -1.8))
        rcol = Lr.curva(np.arange(80), serie(9, 80, 0.9), RUIDO, 3)
        bl_caja = RoundedRectangle(corner_radius=0.12, width=3.2, height=0.8, color=CIAN, stroke_width=3).set_fill(CIAN, 0.12)
        bl_caja.move_to([0, -3.3, 0])
        bl_txt = Text("blanquear", color=TXT, weight=BOLD).scale(0.6).move_to(bl_caja)
        a_l = Arrow([-1.0, -2.4, 0], [-1.0, -2.9, 0], buff=0, color=INK, stroke_width=3, max_tip_length_to_length_ratio=0.5)
        a_r = Arrow([1.0, -2.4, 0], [1.0, -2.9, 0], buff=0, color=INK, stroke_width=3, max_tip_length_to_length_ratio=0.5)
        with self.narrar("b1"):
            # «Este capítulo y el anterior»
            self.paso("capitulos", cw, ca, t=0.7)
            # «se parecen mucho»
            self.paso("parecen", GrowArrow(dbl), t=0.6)
            # «no confundirlos»
            self.paso("confundir", neq, t=0.5)
            # «El filtro de Wiener»
            self.en("wiener")
            self.resaltar(cw, run_time=0.5)
            # «estima la forma de una señal aleatoria»
            self.en("forma")
            self.play(Create(c_sig), Create(c_est), run_time=self.dur(1.0))
            # «muestra a muestra»
            self.paso("muestra", pts, t=0.6)
            # «minimizando el error cuadrático»
            self.paso("error", err, t=0.6)
            # «El filtro adaptado»
            self.en("adapt")
            self.resaltar(ca, run_time=0.5)
            # «decide si hay una señal conocida»
            self.paso("decide", pul, hay, t=0.7)
            # «un solo número»
            self.paso("unnumero", GrowArrow(flecha_g), g, t=0.6)
            # «cuando el ruido tiene color»
            self.en("color")
            self.play(Create(rcol), run_time=self.dur(0.9))
            # «hacen lo mismo primero»
            self.paso("primero", bl_caja, GrowArrow(a_l), GrowArrow(a_r), t=0.6)
            # «blanquear»
            self.en("blanquear")
            self.pop(bl_txt)
        self.wait(1.0)
        self.limpiar()
