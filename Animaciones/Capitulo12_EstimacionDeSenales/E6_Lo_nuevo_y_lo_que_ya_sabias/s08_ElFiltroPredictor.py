"""Escena 08 — El predictor como filtro: H = (1/F)[zF]₊ con el eco da H = 0,6."""
from comun.escena import *


class ElFiltroPredictor(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.parte_secuencia()
        self.wait(0.6)
        self.parte_cuenta()
        self.wait(1.0)
        self.limpiar()

    def parte_secuencia(self):
        H = formula("H", "=", r"\tfrac{1}{F}", r"\left[\,zF\,\right]_{+}", escala=1.0,
                    colores={0: ESTIMACION}).move_to([0, 3.0, 0])
        oculta(H)
        nota_e4 = etiqueta("la del episodio 4", INK, 0.5).move_to([5.0, 3.0, 0])

        vals = [0, 1, 0.6, 0.36, 0.216, 0.13]
        T = Tallos(vals, centro=(0, -0.4), paso=0.95, unidad=1.5, color=AZUL, k0=-1, indices=True, extra=1)
        txt_v = ["", "1", r"0{,}6", r"0{,}36", r"0{,}216", r"0{,}13"]
        etqs = VGroup(*[MathTex(s, color=TXT).scale(0.55).move_to(T.pos(i) + UP * 0.3)
                        for i, s in enumerate(txt_v) if s])
        # las etiquetas de los valores acompañan a su palito: la de índice i está en etqs[i-1]
        pal = [T.palito(i) for i in range(1, 6)]
        mover = VGroup(*[VGroup(p, e) for p, e in zip(pal, etqs)])
        l_F = MathTex(r"F:", color=AZUL).scale(0.8).move_to([-4.2, 0.4, 0])
        tj = tijeras().scale(0.5).move_to(T.pos(1) + LEFT * 0.0 + UP * 1.5)
        suspensivos = MathTex(r"\cdots", color=INK).scale(0.9).move_to([T.x(5) + 0.8, -0.2, 0])
        l_causal = etiqueta("la parte causal", VERDE, 0.65).move_to([0, -2.6, 0])

        with self.narrar("b1"):
            # «Escribámoslo como filtro»
            self.en("filtro")
            self.add(H)
            self.play(*revelar(H[0], H[1]), run_time=self.dur(0.5))

            # «la fórmula causal de los episodios anteriores»
            self.en("formulaant")
            self.play(FadeIn(nota_e4), run_time=self.dur(0.4))

            # «Blanquear con uno entre F»
            self.en("blanq")
            self.play(*revelar(H[2]), run_time=self.dur(0.5))

            # «Adelantar F una muestra»
            self.en("adel")
            self.play(*revelar(H[3]), run_time=self.dur(0.5))

            # «es uno, cero coma seis»
            self.en("tallos")
            self.play(Create(T.base), FadeIn(T.ks), FadeIn(l_F), run_time=self.dur(0.5))
            self.play(LaggedStart(*[FadeIn(m) for m in mover], lag_ratio=0.25), run_time=self.dur(1.6))

            # «adelantada»
            self.en("adelantada")
            self.play(mover.animate.shift(LEFT * 0.95), run_time=self.dur(0.9))

            # «el uno sale por la izquierda»
            self.en("sale")
            self.play(mover[0].animate.set_color(ERROR), run_time=self.dur(0.4))

            # «a la posición menos uno»
            self.en("menos1")
            self.play(FadeIn(tj, scale=0.7), run_time=self.dur(0.4))
            self.resaltar(T.ks[0], color=ERROR)

            # «y queda cero coma seis»
            self.en("queda")
            self.play(FadeOut(mover[0]), FadeOut(tj), run_time=self.dur(0.5))
            self.play(*[m.animate.set_color(VERDE) for m in mover[1:]], run_time=self.dur(0.4))

            # «y así»
            self.en("yasi")
            self.play(FadeIn(suspensivos), run_time=self.dur(0.3))

            # «la parte que ya se sabe»
            self.en("yasabe")
            self.play(FadeIn(l_causal), run_time=self.dur(0.4))

    def parte_cuenta(self):
        pal = Tallos([0.6, 0.36, 0.216, 0.13], centro=(-4.9, 2.1), paso=0.6, unidad=1.0, color=VERDE, k0=0)
        sec = MathTex(r"=", color=TXT).scale(0.9).move_to([-2.9, 2.1, 0])
        fr = fraccion(MathTex(r"0{,}6", color=TXT).scale(0.9), MathTex(r"1-0{,}6\,z^{-1}", color=TXT).scale(0.9))
        fr.move_to([-1.2, 2.1, 0])
        oculta(fr)
        h_ig = MathTex(r"H=", color=ESTIMACION).scale(1.0).move_to([-5.3, 0.4, 0])
        bq = MathTex(r"\left(1-0{,}6\,z^{-1}\right)", color=TXT).scale(0.85).move_to([-2.4, 0.4, 0])
        l_bq = etiqueta("blanqueador", INK, 0.5).next_to(bq, DOWN, buff=0.3)
        punto = MathTex(r"\cdot", color=TXT).scale(1.0).move_to([-0.4, 0.4, 0])
        fr2 = fraccion(MathTex(r"0{,}6", color=TXT).scale(0.9), MathTex(r"1-0{,}6\,z^{-1}", color=TXT).scale(0.9))
        fr2.move_to([1.5, 0.4, 0])
        tach1 = Line(bq.get_corner(DL), bq.get_corner(UR), color=ROJO, stroke_width=6)
        tach2 = Line(fr2.den.get_corner(DL), fr2.den.get_corner(UR), color=ROJO, stroke_width=6)
        fila_b = VGroup(h_ig, bq, l_bq, punto, fr2, tach1, tach2)
        grande = formula("H", "=", r"0{,}6", escala=1.7, colores={0: ESTIMACION, 2: ESTIMACION}).move_to([0, 0.4, 0])
        cx = MathTex(r"x[n]", color=MEDIDA).scale(1.0).move_to([-3.8, -1.8, 0])
        cf = Arrow([-2.8, -1.8, 0], [2.4, -1.8, 0], color=INK, buff=0, stroke_width=4, max_tip_length_to_length_ratio=0.12)
        cm = MathTex(r"\times\,0{,}6", color=ESTIMACION).scale(0.9).move_to([-0.2, -1.4, 0])
        cy = MathTex(r"\hat{x}[n+1]", color=ESTIMACION).scale(1.0).move_to([4.0, -1.8, 0])
        tk = tilde(VERDE, 0.7).move_to([5.8, 0.4, 0])
        l_yw = etiqueta("= Yule-Walker", VERDE, 0.6).move_to([5.3, -0.3, 0])
        lin = Line([-5.0, -2.9, 0], [5.0, -2.9, 0], color=INK, stroke_width=4)

        with self.narrar("b2"):
            # «Esa secuencia»
            self.en("sec")
            self.corte()
            self.play(Create(pal.base), run_time=self.dur(0.3))
            self.play(LaggedStart(*[FadeIn(pal.palito(i)) for i in range(4)], lag_ratio=0.2), run_time=self.dur(0.7))

            # «cero coma seis entre uno menos»
            self.en("frac")
            self.add(fr)
            self.play(FadeIn(sec), *revelar(fr), run_time=self.dur(1.0))

            # «cero coma seis zeta a la menos uno»
            self.en("den")
            self.resaltar(fr.den, color=AMBAR)

            # «Y el filtro»
            self.en("elfiltro")
            self.play(FadeIn(h_ig), run_time=self.dur(0.4))

            # «el blanqueador»
            self.en("bl")
            self.play(FadeIn(bq), FadeIn(l_bq), run_time=self.dur(0.6))

            # «multiplicado por ella»
            self.en("mult")
            self.play(FadeIn(punto), FadeIn(fr2), run_time=self.dur(0.6))

            # «se cancela todo»
            self.en("cancela")
            self.play(Create(tach1), Create(tach2), run_time=self.dur(0.6))

            # «queda cero coma seis»
            self.en("quedaseis")
            self.play(FadeOut(fila_b), run_time=self.dur(0.3))
            self.pop(grande)

            # «multiplicar la última muestra»
            self.en("ultima")
            self.play(FadeIn(cx), GrowArrow(cf), FadeIn(cy), run_time=self.dur(0.7))

            # «por cero coma seis»
            self.en("por06")
            self.play(FadeIn(cm, shift=DOWN * 0.15), run_time=self.dur(0.4))

            # «Es justo lo que dieron las ecuaciones de Yule-Walker»
            self.en("yw")
            self.play(FadeIn(tk), FadeIn(l_yw), run_time=self.dur(0.5))

            # «en una línea»
            self.en("linea")
            self.play(Create(lin), run_time=self.dur(0.5))
