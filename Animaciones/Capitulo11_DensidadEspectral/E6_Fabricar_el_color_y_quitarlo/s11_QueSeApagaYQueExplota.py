"""Escena 11 — Invertir los dos modeladores: la respuesta al impulso del primero se apaga, la del segundo explota."""
from comun.escena import *


class QueSeApagaYQueExplota(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        b1 = caja("(2, 1) / √5", SENAL, ancho=3.0, alto=0.9, scale=0.6).move_to([-3.5, 3.1, 0])
        b2 = caja("(1, 2) / √5", AMBAR, ancho=3.0, alto=0.9, scale=0.6).move_to([3.5, 3.1, 0])
        ok1 = tilde(VERDE, 0.4).move_to([-5.7, 3.1, 0])
        ok2 = tilde(VERDE, 0.4).move_to([5.7, 3.1, 0])
        q1 = MathTex("?", color=AMBAR).scale(1.0).move_to([-5.7, 3.1, 0])
        q2 = MathTex("?", color=AMBAR).scale(1.0).move_to([5.7, 3.1, 0])
        v1 = CurvedArrow([-2.0, 2.5, 0], [-5.0, 2.5, 0], angle=-TAU / 8, color=AMBAR, stroke_width=3)
        v2 = CurvedArrow([5.0, 2.5, 0], [2.0, 2.5, 0], angle=-TAU / 8, color=AMBAR, stroke_width=3)
        f = formula("w[n]", "=", r"\frac{\sqrt5\,y[n]-w[n-1]}{2}", escala=1.0, colores={0: RUIDO}).move_to([-3.5, 1.3, 0])
        ent = Tallos([1, 0, 0, 0, 0], centro=(-3.5, -0.4), paso=0.8, unidad=0.9, color=SENAL)
        t_imp = etiqueta("impulso", SENAL, 0.5).move_to([-6.0, -0.2, 0])
        sal = Tallos([1, -0.5, 0.25, -0.125, 0.0625], centro=(-3.5, -2.6), paso=0.8, unidad=1.2, color=VERDE)
        rot = [("1", 0), ("½", 1), ("−¼", 2), ("⅛", 3), ("−1/16", 4)]
        etqs = [etiqueta(s, TXT, 0.5).move_to(sal.pos(i) + (UP if i % 2 == 0 else DOWN) * 0.33) for s, i in rot]
        t_mit = etiqueta("× (−½)", AMBAR, 0.55).move_to([-3.5, -1.2, 0])
        with self.narrar("b1"):
            # «sirven como modelador»
            self.en("modelador")
            self.play(FadeIn(b1), FadeIn(b2), FadeIn(ok1), FadeIn(ok2), run_time=self.dur(0.6))

            # «Veamos si sirven como blanqueador»
            self.en("veamos")
            self.play(ReplacementTransform(ok1, q1), ReplacementTransform(ok2, q2), run_time=self.dur(0.6))

            # «recuperar la moneda a partir de la salida»
            self.en("recuperar")
            self.play(Create(v1), Create(v2), run_time=self.dur(0.8))

            # «Con el primero, despejando»
            self.en("primero")
            self.play(FadeOut(b2), FadeOut(q2), FadeOut(v2), FadeIn(f[0:2]), run_time=self.dur(0.6))

            # «cada moneda es la salida»
            self.en("cadamoneda")
            self.play(FadeIn(f[2]), run_time=self.dur(0.9))

            # «dividido entre dos»
            self.en("entredos")
            self.resaltar(f[2], color=AMBAR)

            # «único impulso»
            self.en("impulso")
            self.play(Create(ent.base), FadeIn(ent.palito(0)), FadeIn(t_imp), run_time=self.dur(0.7))

            # «un medio, menos un cuarto, un octavo»
            self.en("barras")
            self.play(Create(sal.base), run_time=0.3)
            for i in range(5):
                self.play(FadeIn(sal.palito(i)), FadeIn(etqs[i]), run_time=self.dur(0.5))

            # «cada vez la mitad»
            self.en("mitad")
            self.pop(t_mit)

            # «Se apaga»
            self.en("apaga")
            self.play(*[sal.palito(i).animate.set_opacity(0.5) for i in range(5)], run_time=0.5)

            # «Funciona»
            self.en("funciona")
            self.pop(tilde(VERDE, 0.8).move_to([1.5, -2.2, 0]))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        blq = caja("(1, 2) / √5", AMBAR, ancho=3.0, alto=0.9, scale=0.6).move_to([0, 3.2, 0])
        f = formula("w[n]", "=", r"\sqrt5\,y[n]-2\,w[n-1]", escala=1.1, colores={0: RUIDO}).move_to([0, 1.8, 0])
        ent = Tallos([1, 0, 0, 0, 0], centro=(-4.5, 0.0), paso=0.8, unidad=0.7, color=SENAL)
        t_imp = etiqueta("impulso", SENAL, 0.5).move_to([-4.5, 0.9, 0])
        sal = Tallos([1, -2, 4, -8, 16], centro=(-0.5, -2.3), paso=1.1, unidad=0.12, color=ROJO)
        et = [etiqueta(s, TXT, 0.5).move_to(sal.pos(i) + (UP if v > 0 else DOWN) * 0.35)
              for i, (s, v) in enumerate([("1", 1), ("−2", -1), ("4", 1), ("−8", -1), ("16", 1)])]
        t_dob = etiqueta("× (−2)", ROJO, 0.55).move_to([-0.5, 0.0, 0])
        dest = Rectangle(width=6.4, height=4.6, color=ROJO, stroke_width=0).set_fill(ROJO, 0.3).move_to([0.5, -1.3, 0])
        t_inest = self.palabra("inestable", ROJO, 0.9).move_to([4.8, 1.2, 0])
        eps = Dot(np.array([-2.7, -0.9, 0.0]), radius=0.07, color=AMBAR)
        t_err = etiqueta("pequeño error", AMBAR, 0.5).move_to([-5.2, -1.0, 0])
        inf = MathTex(r"\infty", color=ROJO).scale(1.4).move_to([4.8, -0.6, 0])
        ok = tilde(VERDE, 0.5).move_to([2.0, 3.2, 0])
        x = cruz(ROJO, 0.7).move_to([2.0, 3.2, 0])
        with self.narrar("b2"):
            # «Con el segundo»
            self.en("segundo")
            self.corte()
            self.play(FadeIn(blq), run_time=0.5)

            # «la salida menos dos veces la moneda anterior»
            self.en("formula")
            self.play(FadeIn(f), run_time=self.dur(1.2))

            # «Ahora el impulso da»
            self.en("ahora")
            self.play(Create(ent.base), FadeIn(ent.palito(0)), FadeIn(t_imp), run_time=self.dur(0.7))

            # «uno, menos dos, cuatro, menos ocho, dieciséis»
            self.en("barras")
            self.play(Create(sal.base), run_time=0.3)
            for i in range(5):
                self.play(FadeIn(sal.palito(i)), FadeIn(et[i]), run_time=self.dur(0.55))

            # «cada vez el doble»
            self.en("doble")
            self.pop(t_dob)

            # «Explota»
            self.en("explota")
            self.sfx("error")
            self.play(FadeIn(dest, rate_func=there_and_back), run_time=0.6)

            # «inestable»
            self.en("inestable")
            self.pop(t_inest)

            # «cualquier pequeño error»
            self.en("error")
            self.play(FadeIn(t_err), FadeIn(eps), run_time=self.dur(0.6))

            # «se multiplica hasta el infinito»
            self.en("infinito")
            self.play(eps.animate.scale(3).set_color(ROJO), FadeIn(inf), run_time=self.dur(1.2))

            # «El filtro modela bien»
            self.en("modela")
            self.play(FadeIn(ok), run_time=0.4)

            # «no se puede deshacer»
            self.en("nodeshacer")
            self.play(ReplacementTransform(ok, x), run_time=0.5)
