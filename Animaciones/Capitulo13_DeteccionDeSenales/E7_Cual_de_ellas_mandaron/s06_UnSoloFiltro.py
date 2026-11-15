"""Escena 06 — Con dos señales basta un filtro adaptado a la diferencia (y el ejemplo con el pulso del capítulo)."""
from comun.escena import *


class UnSoloFiltro(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.filtro()
        self.wait(0.6)
        self.ejemplo()
        self.wait(1.0)
        self.limpiar()

    def filtro(self):
        b0 = caja("adaptado a s₀", AZUL_C7, ancho=3.4, alto=0.8, scale=0.5).move_to([-2.4, 2.6, 0])
        b1 = caja("adaptado a s₁", SENAL, ancho=3.4, alto=0.8, scale=0.5).move_to([-2.4, 1.4, 0])
        uno = caja("filtro adaptado", AMBAR, ancho=3.4, alto=1.0, scale=0.55).move_to([-2.4, 2.0, 0])
        r_in = MathTex("r", color=MEDIDA).scale(1.2).move_to([-6.2, 2.0, 0])
        a_in = Arrow([-5.8, 2.0, 0], [-4.1, 2.0, 0], buff=0.05, color=INK, stroke_width=3)
        a_out = Arrow([-0.7, 2.0, 0], [0.8, 2.0, 0], buff=0.05, color=INK, stroke_width=3)
        dif = MathTex("s_1", "-", "s_0", color=AMBAR).scale(1.0).move_to([-2.4, 0.5, 0])
        g1 = formula("g", "=", r"\sum r\,", escala=1.2, colores={0: AMBAR, 2: MEDIDA}).move_to([-3.6, -0.9, 0])
        g2 = MathTex("(s_1-s_0)", color=AMBAR).scale(1.2).next_to(g1, RIGHT, buff=0.12)
        s1 = pulso7([2, 2, 1], centro=(4.0, 2.0), color=SENAL, paso=0.65, unidad=0.4)
        s0 = pulso7([2, -1, -2], centro=(4.0, 0.2), color=AZUL_C7, paso=0.65, unidad=0.4)
        n1 = MathTex("s_1", color=SENAL).scale(0.9).move_to([2.2, 2.3, 0])
        n0 = MathTex("s_0", color=AZUL_C7).scale(0.9).move_to([2.2, 0.5, 0])
        marco = Rectangle(width=0.7, height=3.9, color=INK, stroke_width=2).set_fill(INK, 0.15).move_to([s1.x(0), 1.1, 0])
        marco.permitir_encima = True
        no = etiqueta("no ayuda", INK, 0.5).move_to([s1.x(0), -1.2, 0])
        with self.narrar("b1"):
            # «Con dos señales»
            self.paso("dos", b0, b1, t=0.6)
            # «la regla se simplifica mucho»
            self.en("simplifica")
            self.play(ReplacementTransform(VGroup(b0, b1), uno), run_time=self.dur(0.7))
            # «un único filtro adaptado»
            self.paso("unico", r_in, GrowArrow(a_in), GrowArrow(a_out), t=0.6)
            # «a la diferencia entre las dos»
            self.paso("difs", dif, t=0.6)
            # «Ge es la suma de recibido»
            self.paso("ge", g1, t=0.6)
            # «por la señal uno menos la señal cero»
            self.paso("uno_menos_cero", g2, t=0.6)
            # «no es cada señal por separado»
            self.paso("separado", s1, s0, n1, n0, t=0.7)
            # «en qué se distinguen»
            self.en("distinguen")
            self.play(s1.tallos[1].animate.set_color(AMBAR), s1.puntos[1].animate.set_color(AMBAR),
                      s1.tallos[2].animate.set_color(AMBAR), s1.puntos[2].animate.set_color(AMBAR),
                      s0.tallos[1].animate.set_color(AMBAR), s0.puntos[1].animate.set_color(AMBAR),
                      s0.tallos[2].animate.set_color(AMBAR), s0.puntos[2].animate.set_color(AMBAR),
                      run_time=self.dur(0.6))
            # «la parte que tienen en común»
            self.paso("comun", marco, t=0.5)
            # «no ayuda a decidir»
            self.en("noayuda")
            self.play(FadeIn(no), s1.tallos[0].animate.set_color(INK), s1.puntos[0].animate.set_color(INK),
                      s0.tallos[0].animate.set_color(INK), s0.puntos[0].animate.set_color(INK), run_time=self.dur(0.6))
        self.corte()

    def ejemplo(self):
        t1 = pulso7([2, 2, 1], centro=(-2.0, 2.5), color=SENAL, paso=0.9, unidad=0.34)
        t0 = pulso7([2, -1, -2], centro=(-2.0, 1.0), color=AZUL_C7, paso=0.9, unidad=0.34)
        td = pulso7([0, 3, 3], centro=(-2.0, -1.8), color=AMBAR, paso=0.9, unidad=0.34)
        v1, v0, vd = valores_sobre13(t1, escala=0.5), valores_sobre13(t0, escala=0.5), valores_sobre13(td, escala=0.5)
        n1 = MathTex("s_1", color=SENAL).scale(1.1).move_to([-5.2, 2.5, 0])
        n0 = MathTex("s_0", color=AZUL_C7).scale(1.1).move_to([-5.2, 1.0, 0])
        nd = MathTex("s_1-s_0", color=AMBAR).scale(1.0).move_to([-5.5, -1.8, 0])
        ej = etiqueta("ejemplo", INK, 0.55).move_to([-5.4, 3.5, 0])
        e1 = MathTex("E=4+4+1=9", color=AMBAR).scale(0.85).move_to([2.6, 2.5, 0])
        e0 = MathTex("E=4+1+4=9", color=AMBAR).scale(0.85).move_to([2.6, 1.0, 0])
        marco = Rectangle(width=0.9, height=5.2, color=INK, stroke_width=2).set_fill(INK, 0.12).move_to([td.x(0), 0.6, 0])
        marco.permitir_encima = True
        lon = MathTex(r"\|s_1-s_0\|", color=AMBAR).scale(1.0).move_to([3.0, -0.7, 0])
        raiz = MathTex(r"=\sqrt{0+9+9}=\sqrt{18}", color=TXT).scale(1.0).move_to([3.5, -1.6, 0])
        c24 = MathTex(r"=4{,}24", color=AMBAR).scale(1.3).move_to([3.0, -2.6, 0])
        with self.narrar("b2"):
            # «Un ejemplo»
            self.paso("ejemplo", ej, t=0.4)
            # «La señal uno»
            self.paso("uno", t1, v1, n1, t=0.7)
            # «La señal cero»
            self.paso("cero", n0, t=0.4)
            # «menos uno, menos dos»
            self.paso("negativas", t0, v0, t=0.7)
            # «energía nueve»
            self.paso("nueve", e1, e0, t=0.6)
            # «Su diferencia»
            self.paso("diferencia", nd, t=0.5)
            # «cero, tres, tres»
            self.paso("cerotrestres", td, vd, t=0.7)
            # «la primera muestra, que tienen igual»
            self.paso("primera", marco, t=0.5)
            # «desaparece»
            self.en("desaparece")
            self.play(FadeOut(marco), td.tallos[0].animate.set_stroke(opacity=0.2), run_time=self.dur(0.5))
            # «La longitud de la diferencia»
            self.paso("longitud", lon, t=0.5)
            # «raíz de dieciocho»
            self.paso("raiz", raiz, t=0.7)
            # «cuatro coma dos cuatro»
            self.en("cuatro24")
            self.pop(c24)
