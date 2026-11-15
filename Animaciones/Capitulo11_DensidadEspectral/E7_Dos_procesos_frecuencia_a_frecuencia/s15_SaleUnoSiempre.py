"""Escena 15 — Con un solo trozo la coherencia da uno siempre: es una identidad."""
from comun.escena import *


class SaleUnoSiempre(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        opciones = VGroup(*[caja(t, c, ancho=1.2, alto=0.7, scale=0.6) for t, c in
                            [("0", AZUL), ("0,5", CIAN), ("1", ROJO)]]).arrange(RIGHT, buff=0.6).move_to([-2.2, 3.3, 0])
        trozo = Rectangle(width=2.2, height=0.8, color=AMBAR, stroke_width=4).move_to([3.2, 3.3, 0])
        l_trozo = etiqueta("un solo trozo", AMBAR, 0.5).move_to([5.4, 3.3, 0])
        oX = np.array([-4.4, 0.6, 0.0])
        oY = np.array([-0.7, 0.6, 0.0])
        pX, pY = plano_c((oX[0], oX[1]), radio=1.5), plano_c((oY[0], oY[1]), radio=2.0)
        zX, zY = flecha_c(oX, 1.5, 35, SENAL), flecha_c(oY, 2.0, 120, MEDIDA)
        lX, lY = MathTex("X", color=SENAL).scale(0.8).move_to(oX + np.array([-1.9, 1.5, 0])), \
            MathTex("Y", color=MEDIDA).scale(0.8).move_to(oY + np.array([-2.4, 2.0, 0]))
        mX = formula(r"|X|=3", escala=0.9, colores={0: SENAL}).move_to([-4.4, -2.3, 0])
        mY = formula(r"|Y|=4", escala=0.9, colores={0: MEDIDA}).move_to([-0.7, -2.7, 0])
        arriba = oculta(formula(r"|X\,Y^*|=12", escala=1.0, colores={0: AMBAR}).move_to([4.8, 1.6, 0]))
        abajo = oculta(formula(r"\sqrt{9\cdot 16}=12", escala=1.0).move_to([4.8, 0.2, 0]))
        igual = MathTex("=", color=VERDE).scale(0.9).move_to([4.8, 0.9, 0])
        uno12 = oculta(formula(r"\frac{12}{12}=1", escala=1.4, colores={0: AMBAR}).move_to([4.8, -1.4, 0]))
        otro = formula(r"\frac{2\cdot5}{\sqrt{4\cdot 25}}=1", escala=0.9).move_to([4.8, -3.0, 0])
        with self.narrar("b1"):
            # «Sale uno»
            self.en("uno")
            self.corte()
            self.add(arriba, abajo, uno12)
            self.play(FadeIn(opciones), run_time=0.4)
            self.play(opciones[2][0].animate.set_stroke(ROJO).set_fill(ROJO, 0.5), run_time=0.3)

            # «Siempre»
            self.en("siempre")
            self.resaltar(opciones[2], color=ROJO)

            # «Con un solo trozo»
            self.en("trozo")
            self.play(Create(trozo), FadeIn(l_trozo), run_time=self.dur(0.6))

            # «un número complejo para cada señal»
            self.en("complejos")
            self.play(Create(pX), Create(pY), GrowArrow(zX), GrowArrow(zY), FadeIn(lX), FadeIn(lY),
                      run_time=self.dur(1.2))

            # «sus módulos son tres y cuatro»
            self.en("mod")
            self.play(FadeIn(mX), FadeIn(mY), run_time=self.dur(0.8))

            # «Arriba, el módulo del producto: doce»
            self.en("arriba")
            self.play(*revelar(arriba), run_time=self.dur(0.8))

            # «Abajo, la raíz de nueve por dieciséis: doce»
            self.en("abajo")
            self.play(*revelar(abajo), run_time=self.dur(0.8))

            # «Doce entre doce, uno»
            self.en("uno12")
            self.play(*revelar(uno12), run_time=self.dur(0.6))
            self.sfx("impacto")

            # «cualquier otro par de números»
            self.en("otro")
            self.play(FadeIn(otro), run_time=self.dur(0.8))

            # «es el mismo número»
            self.en("igual")
            self.pop(igual)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        F = formula(r"\frac{|X\,Y^*|}{\sqrt{|X|^2|Y|^2}}", r"\equiv", "1", escala=1.1,
                    colores={1: AMBAR}).move_to([-3.6, 2.4, 0])
        sinrel = etiqueta("aunque no haya relación", INK, 0.55).move_to([-3.6, 1.1, 0])
        aviso = Triangle(color=ROJO, stroke_width=6).scale(0.4).set_fill(ROJO, 0.2).move_to([-6.2, 0.0, 0])
        adm = Text("!", color=ROJO, weight=BOLD).scale(0.5).move_to(aviso.get_center() + DOWN * 0.04)
        aviso2 = Triangle(color=ROJO, stroke_width=6).scale(0.4).set_fill(ROJO, 0.2).move_to([5.8, -2.6, 0])
        adm2 = Text("!", color=ROJO, weight=BOLD).scale(0.5).move_to(aviso2.get_center() + DOWN * 0.04)
        p1, p2 = Dot([3.0, -0.3, 0], radius=0.1, color=SENAL), Dot([4.8, 1.3, 0], radius=0.1, color=SENAL)
        recta = Line([2.0, -1.2, 0], [5.8, 2.2, 0], color=AMBAR, stroke_width=3)
        pm1 = formula(r"\rho=\pm 1", escala=1.0, colores={0: AMBAR}).move_to([3.9, -2.6, 0])
        l_dos = etiqueta("dos puntos", INK, 0.5).move_to([6.0, -0.3, 0])
        nube = nube_puntos(centro=(3.9, 0.5), n=26, ancho=3.0, semilla=4)
        oj = ojo(TXT).scale(0.7).move_to([6.2, 3.1, 0])
        with self.narrar("b2"):
            # «una identidad»
            self.en("identidad")
            self.corte()
            self.play(FadeIn(F), run_time=self.dur(1.0))

            # «aunque las señales no tengan ninguna relación»
            self.en("sinrel")
            self.play(FadeIn(sinrel), run_time=self.dur(0.6))

            # «Es la misma trampa»
            self.en("trampa")
            self.play(FadeIn(aviso), FadeIn(adm), run_time=self.dur(0.5))

            # «un rho calculado con dos puntos»
            self.en("dospuntos")
            self.corte()
            self.play(FadeIn(p1), FadeIn(p2), FadeIn(l_dos), run_time=self.dur(0.7))

            # «siempre vale uno o menos uno»
            self.en("pm1")
            self.pop(pm1)

            # «por dos puntos siempre pasa una recta»
            self.en("recta")
            self.play(Create(recta), run_time=self.dur(0.8))

            # «Otra vez»
            self.en("otra")
            self.play(FadeIn(aviso2), FadeIn(adm2), run_time=0.3)

            # «mira la nube antes que el número»
            self.en("nube")
            self.play(FadeIn(nube, lag_ratio=0.1), FadeIn(oj), run_time=self.dur(1.2))
