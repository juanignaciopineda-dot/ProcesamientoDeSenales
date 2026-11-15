"""Escena 12 — El filtro adaptativo (LMS) baja rodando por la parábola del error del E1."""
from comun.escena import *


class BajarPorLaParabola(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        P = ParabolaJ(centro=(-3.2, -0.9), ancho=6.0, alto=3.4)
        via = etiqueta("otra vía", AMBAR, 0.6, BOLD).move_to([-4.6, 3.5, 0])
        cq = formula("C_{xx}", "=", "?", escala=0.9, colores={0: MEDIDA, 2: AMBAR}).move_to([-1.0, 3.5, 0])
        tc = tachar(cq)
        jh = formula("J(h)", "=", "4-8h+5h^2", escala=0.95, colores={0: AMBAR}).move_to([3.8, 3.0, 0])
        lj = etiqueta("error", ERROR, 0.45).move_to([-3.2, 1.1, 0])
        adapt = caja("filtro adaptativo", AZUL, ancho=3.4, alto=0.8, scale=0.5).move_to([3.8, 1.9, 0])
        pt = P.punto(-0.1, AZUL)
        ver = formula("\\text{pendiente}", "=", "-2\\,E[e\\,x]", escala=0.85, colores={2: ERROR}
                      ).move_to([3.8, 0.8, 0])
        sola = formula("-2\\,e[n]\\,x[n]", escala=0.95, colores={0: ERROR}).move_to([3.8, -0.4, 0])
        lms = formula("h", "\\leftarrow", "h", "+", "\\mu\\,e\\,x", escala=0.95, colores={4: AMBAR}).move_to([3.8, -1.7, 0])
        etq_lms = etiqueta("LMS", AMBAR, 0.6, BOLD).move_to([3.8, -2.4, 0])
        tv = tachar(ver[2], ROJO)
        marcas = VGroup(*[Line([-6.2 + 0.7 * i, -3.7, 0], [-6.2 + 0.7 * i, -3.45, 0], color=MEDIDA, stroke_width=3)
                          for i in range(9)])
        with self.narrar("b1"):
            # «otra vía»
            self.en("via")
            self.pop(via)
            # «no necesita estimar correlaciones»
            self.en("noncorr")
            self.play(FadeIn(cq), run_time=0.3)
            self.play(Create(tc), run_time=self.dur(0.5))
            # «la parábola del error»
            self.en("parab")
            self.play(Create(P.eje), Create(P.curva), FadeIn(P.vertice), FadeIn(lj), run_time=self.dur(1.0))
            # «cuatro menos ocho hache más cinco hache al cuadrado»
            self.en("jh")
            self.play(FadeIn(jh), run_time=self.dur(1.2))
            # «El filtro adaptativo»
            self.en("adapt")
            self.play(FadeIn(adapt), run_time=self.dur(0.6))
            # «baja rodando por ella»
            self.en("baja")
            self.play(FadeIn(pt), run_time=0.3)
            self.play(pt.animate.move_to(P.p(0.4)), run_time=self.dur(1.0))
            # «en cada muestra»
            self.en("muestra")
            self.play(FadeIn(marcas, lag_ratio=0.3), run_time=self.dur(0.9))
            # «mueve hache un poco en contra de la pendiente»
            self.en("contra")
            tan = P.pendiente(0.4, 1.8)
            fle = Arrow(P.p(0.4) + UP * 0.35, P.p(0.4) + UP * 0.35 + RIGHT * 0.9 + DOWN * 0.45, buff=0, color=VERDE,
                        stroke_width=5, max_tip_length_to_length_ratio=0.3)
            self.play(Create(tan), GrowArrow(fle), run_time=self.dur(0.8))
            # «La pendiente verdadera»
            self.en("verdadera")
            self.play(FadeIn(ver), run_time=self.dur(0.8))
            # «la media del error por el dato»
            self.en("media")
            self.resaltar(ver[2], color=AMBAR, run_time=0.6)
            # «usar la de esta sola muestra»
            self.en("sola")
            self.play(FadeIn(sola), run_time=self.dur(0.7))
            # «sin la media»
            self.en("sinmedia")
            self.play(Create(tv), run_time=self.dur(0.5))
            # «el algoritmo LMS»
            self.en("lms")
            self.play(FadeIn(lms), FadeIn(etq_lms), run_time=self.dur(0.8))
        self.wait(0.6)
        self.play(*[FadeOut(m) for m in (cq, tc, via, jh, adapt, ver, sola, lms, etq_lms, tan, fle, marcas, tv)], run_time=0.4)
        self.segunda(P, pt)
        self.wait(1.0)
        self.limpiar()

    def segunda(self, P, pt):
        pt.move_to(P.p(0.0))
        pv = P.vertice
        mu = formula("\\mu", "=", "0{,}1", escala=0.85, colores={0: AMBAR}).move_to([3.4, 2.9, 0])
        x2 = MathTex("x=2", color=MEDIDA).scale(0.8).move_to([2.6, 2.0, 0])
        y15 = MathTex("y=1{,}5", color=SENAL).scale(0.8).move_to([5.0, 2.0, 0])
        e15 = MathTex("e=1{,}5-0\\cdot2=1{,}5", color=ERROR).scale(0.75).move_to([4.0, 1.2, 0])
        h03 = MathTex("h=0+0{,}1\\cdot1{,}5\\cdot2=0{,}3", color=AMBAR).scale(0.75).move_to([4.0, 0.4, 0])
        xm1 = MathTex("x=-1", color=MEDIDA).scale(0.8).move_to([2.6, -0.6, 0])
        ym08 = MathTex("y=-0{,}8", color=SENAL).scale(0.8).move_to([5.0, -0.6, 0])
        em05 = MathTex("e=-0{,}8-0{,}3\\cdot(-1)=-0{,}5", color=ERROR).scale(0.75).move_to([4.0, -1.4, 0])
        h035 = MathTex("h=0{,}3+0{,}1\\cdot(-0{,}5)\\cdot(-1)=0{,}35", color=AMBAR).scale(0.75).move_to([4.0, -2.2, 0])
        with self.narrar("b2"):
            # «un paso de cero coma uno»
            self.en("mu")
            self.play(FadeIn(mu), run_time=self.dur(0.6))
            # «empezando en cero»
            self.en("cero")
            self.play(pt.animate.move_to(P.p(0.0)), run_time=self.dur(0.6))
            # «Llega equis igual a dos»
            self.en("x2")
            self.play(FadeIn(x2, shift=LEFT * 0.3), run_time=self.dur(0.5))
            # «la temperatura era uno coma cinco»
            self.en("y15")
            self.play(FadeIn(y15), run_time=self.dur(0.5))
            # «el error es uno coma cinco»
            self.en("e15")
            self.play(FadeIn(e15), run_time=self.dur(0.7))
            # «hache pasa a cero coma tres»
            self.en("h03")
            self.play(FadeIn(h03), pt.animate.move_to(P.p(0.3)), run_time=self.dur(0.9))
            # «Llega menos uno»
            self.en("xm1")
            self.play(FadeIn(xm1, shift=LEFT * 0.3), run_time=self.dur(0.5))
            # «la temperatura era menos cero coma ocho»
            self.en("ym08")
            self.play(FadeIn(ym08), run_time=self.dur(0.5))
            # «el error es menos cero coma cinco»
            self.en("em05")
            self.play(FadeIn(em05), run_time=self.dur(0.7))
            # «hache sube a cero coma tres cinco»
            self.en("h035")
            self.play(FadeIn(h035), pt.animate.move_to(P.p(0.35)), run_time=self.dur(0.9))
            # «al cero coma ocho que sabemos»
            self.en("optimo")
            self.play(Indicate(pv, color=VERDE, scale_factor=2.0), run_time=self.dur(0.8))
