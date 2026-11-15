"""Escena 17 — Cierre del capítulo y anuncio del E1 del Cap. 13, «Más datos no bastan»."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "17"

    def construct(self):
        self.repaso()
        self.wait(0.6)
        self.detectar()
        self.wait(1.0)
        self.limpiar()

    def repaso(self):
        cw = caja("Wiener", AZUL, ancho=2.6, alto=1.0).move_to([-3.4, 2.5, 0])
        ck = caja("Kalman", AMBAR, ancho=2.6, alto=1.0).move_to([3.4, 2.5, 0])
        eq = MathTex("=", color=VERDE).scale(1.2).move_to([0, 2.5, 0])
        F, R = flechas_xy(origen=(-6.0, -2.7), largo=2.6, angulo=45)
        P = ParabolaJ(centro=(1.8, -1.6), ancho=3.6, alto=2.2)
        pt = P.punto(-0.1, AZUL, 0.11)
        cq = formula("C_{xx}", "=", "?", escala=0.9, colores={0: MEDIDA, 2: AMBAR}).move_to([5.6, 0.2, 0])
        tc = tachar(cq)
        with self.narrar("b1"):
            # «Wiener y Kalman»
            self.en("wk")
            self.play(FadeIn(cw), FadeIn(ck), run_time=self.dur(0.8))
            # «el mismo filtro»
            self.en("mismo")
            self.play(FadeIn(eq), cw.animate.shift(RIGHT * 1.3), ck.animate.shift(LEFT * 1.3), run_time=self.dur(0.7))
            # «todo era una proyección»
            self.en("proy")
            self.play(GrowArrow(F.presente), GrowArrow(F.futuro), Create(F.sombra), Create(F.error), Create(F.recto),
                      run_time=self.dur(1.0))
            # «el LMS llega al mismo sitio»
            self.en("lms")
            self.play(Create(P.eje), Create(P.curva), FadeIn(P.vertice), FadeIn(pt), run_time=0.6)
            self.play(pt.animate.move_to(P.p(0.8)), run_time=self.dur(1.0))
            # «sin conocer las correlaciones»
            self.en("sin")
            self.play(FadeIn(cq), run_time=0.3)
            self.play(Create(tc), run_time=self.dur(0.5))

    def detectar(self):
        L = Lienzo(ancho=3.6, alto=1.0, t_rango=(0, 4), v_max=1.0, centro=(-3.6, 3.0))
        tr = L.curva(np.linspace(0, 4, 160), 0.7 * serie(6, 160, 0.9), RUIDO, 2.4)
        ar = Arrow([-5.6, 2.0, 0], [-4.3, 2.0, 0], color=ESTIMACION, buff=0, stroke_width=5)
        yh = MathTex("\\hat y", color=ESTIMACION).scale(1.0).move_to([-3.7, 2.0, 0])
        cu = etiqueta("¿cuánto?", INK, 0.7).move_to([-3.6, 0.7, 0])
        tcu = tachar(cu)
        sn = etiqueta("¿sí o no?", AMBAR, 0.7, BOLD).move_to([1.8, 0.7, 0])
        rad = Circle(radius=0.9, color=VERDE, stroke_width=4).set_fill(VERDE, 0.06).move_to([-5.0, -1.8, 0])
        rad2 = Circle(radius=0.45, color=VERDE, stroke_width=2).move_to(rad)
        dot = Dot([-4.6, -1.5, 0], radius=0.1, color=ERROR)
        rad_ = VGroup(rad, rad2)
        mchs = VGroup(*[Dot([-5.0 + 0.55 * np.cos(a), -1.8 + 0.6 * np.sin(a), 0], radius=0.05, color=RUIDO)
                        for a in np.linspace(0, 6.0, 9)])
        val = MathTex("\\hat y=2{,}4", color=ESTIMACION).scale(0.8).move_to([-1.9, -1.8, 0])
        tv = tachar(val)
        sino = caja("sí / no", AMBAR, ancho=1.8, alto=0.8, scale=0.55).move_to([1.2, -1.8, 0])
        x1 = cruz(ROJO, 0.22).move_to([0.5, -2.5, 0])
        x2 = cruz(ROJO, 0.22).move_to([1.9, -2.5, 0])
        tit = self.palabra("Detección de señales", INK, 0.8).move_to([0, 2.6, 0])
        broma = etiqueta("¿en serio?", INK, 0.6).move_to([0, 0.6, 0])
        t13 = self.palabra("Más datos no bastan", AMBAR, 1.2).move_to([0, -0.8, 0])
        antes = [L, tr, ar, yh, cu, tcu, sn, rad_, dot, mchs, val, tv, sino, x1, x2]
        with self.narrar("b2"):
            # «adivinar lo mejor posible»
            self.en("adivinar")
            self.corte()
            self.play(GrowArrow(ar), FadeIn(yh), run_time=self.dur(0.7))
            # «un valor que no vemos limpio»
            self.en("limpio")
            self.play(Create(L.base()), Create(tr), run_time=self.dur(1.0))
            # «no es cuánto, sino sí o no»
            self.en("sino")
            self.play(FadeIn(cu), run_time=0.3)
            self.play(Create(tcu), run_time=0.4)
            self.play(FadeIn(sn), run_time=self.dur(0.5))
            # «un avión en el radar»
            self.en("radar")
            self.play(FadeIn(rad_), FadeIn(dot), run_time=self.dur(0.7))
            # «solo ruido»
            self.en("solo")
            self.play(FadeOut(dot), FadeIn(mchs), run_time=self.dur(0.6))
            # «acertar un valor»
            self.en("acertar")
            self.play(FadeIn(val), run_time=0.3)
            self.play(Create(tv), run_time=self.dur(0.4))
            # «decidir»
            self.en("decidir")
            self.play(FadeIn(sino), run_time=self.dur(0.5))
            # «dos maneras distintas»
            self.en("dos")
            self.play(FadeIn(x1), FadeIn(x2), run_time=self.dur(0.6))
            # «Eso es detectar»
            self.en("detect")
            self.play(*[FadeOut(m) for m in self.mobjects if m is not self.camera.frame], run_time=0.3)
            self.play(FadeIn(tit), run_time=self.dur(0.5))
            # «una idea que suena a broma»
            self.en("broma")
            self.play(FadeIn(broma), run_time=self.dur(0.5))
            # «más datos no bastan»
            self.en("titulo13")
            self.pop(t13)
