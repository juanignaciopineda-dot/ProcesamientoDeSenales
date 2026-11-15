"""Escena 03 — El sensor con su cable ruidoso: las letras y, v y x."""
from comun.escena import *


class ElSensorConRuido(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.promesa_y_sensor()
        self.cable_y_letras()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def promesa_y_sensor(self):
        t, y, v, x = sensor12(40)
        # la promesa del capítulo 11
        Lv = Lienzo(ancho=5.4, alto=1.4, t_rango=(0, 1), v_max=1.5, centro=(-3.6, 1.2))
        Lm = Lienzo(ancho=5.4, alto=1.4, t_rango=(0, 1), v_max=1.5, centro=(-3.6, -0.7))
        voz = voz_t(Lv, SENAL, 3.0)
        mur = ruido_t(Lm, 3, 0.6, RUIDO, 2.4)
        promesa = self.palabra("promesa", AMBAR, 1.0).move_to([3.7, 2.2, 0])
        px = Dot([3.0, -0.5, 0], radius=0.14, color=MEDIDA)
        py = Dot([4.7, -0.5, 0], radius=0.14, color=SENAL)
        lx = MathTex("x", color=MEDIDA).scale(0.8).next_to(px, DOWN, buff=0.2)
        ly = MathTex("y", color=SENAL).scale(0.8).next_to(py, DOWN, buff=0.2)
        eje = Line([2.4, -0.5, 0], [5.3, -0.5, 0], color=INK, stroke_width=2)
        fl = Arrow(px.get_center() + RIGHT * 0.2, py.get_center() + LEFT * 0.2, buff=0, color=AMBAR,
                   stroke_width=5, max_tip_length_to_length_ratio=0.3).shift(UP * 0.4)
        interr = Text("?", color=AMBAR, weight=BOLD).scale(0.7).next_to(fl, UP, buff=0.1)
        ok = tilde(VERDE, 0.9).next_to(promesa, RIGHT, buff=0.25)
        # el sensor
        L = Lienzo(ancho=8.0, alto=3.2, t_rango=(0, 39), v_max=7, centro=(1.0, -0.4))
        termo = termometro(2.0, ROJO, 0.6).move_to([-4.6, -0.4, 0])
        curva = L.curva(t, y, SENAL, 4)
        media = DashedLine(L.p(0, 0), L.p(39, 0), color=INK, stroke_width=2.2)
        lm = Text("20 °C", color=INK).scale(0.45).next_to(L.p(0, 0), LEFT, buff=0.12)
        banda = Rectangle(width=8.0, height=float(L.y(2) - L.y(-2)), stroke_width=0).set_fill(SENAL, 0.14)
        banda.move_to(L.p(19.5, 0))
        s2 = MathTex(r"\sigma^2 = 4", color=SENAL).scale(0.85).move_to([3.6, 2.7, 0])
        a = Dot(L.p(10, y[10]), radius=0.1, color=AMBAR)
        b = Dot(L.p(11, y[11]), radius=0.1, color=AMBAR)
        par = Arrow(a.get_center(), b.get_center(), buff=0.12, color=AMBAR, stroke_width=4,
                    max_tip_length_to_length_ratio=0.35)
        mem = MathTex(r"\times\, 0{,}6", color=AMBAR).scale(0.85).move_to([float(L.p(10.5, 0)[0]), 2.7, 0])

        with self.narrar("b1"):
            # «una promesa»
            self.en("promesa")
            self.pop(promesa)
            self.play(Create(voz), Create(mur), run_time=self.dur(0.9))

            # «dos procesos son dos variables aleatorias»
            self.en("dos")
            self.play(Create(eje), FadeIn(px), FadeIn(py), FadeIn(lx), FadeIn(ly), run_time=self.dur(0.7))

            # «y separar la voz del murmullo»
            self.en("separar")
            self.resaltar(voz, mur, color=AMBAR, escala=1.05)

            # «estimar una variable a partir de otra»
            self.en("estimar")
            self.play(GrowArrow(fl), FadeIn(interr), run_time=self.dur(0.7))

            # «Hoy la cumplimos»
            self.en("cumplimos")
            self.sfx("exito")
            self.play(Create(ok), run_time=self.dur(0.4))

            # «un ejemplo que ya conoces»
            self.en("ejemplo")
            self.corte()
            self.play(FadeIn(termo, shift=RIGHT * 0.3), run_time=self.dur(0.5))

            # «El sensor de temperatura»
            self.en("sensor")
            self.play(Create(curva), run_time=self.dur(1.0))

            # «media de veinte grados»
            self.en("media")
            self.play(Create(media), FadeIn(lm), run_time=self.dur(0.5))

            # «varianza cuatro»
            self.en("varianza")
            self.play(FadeIn(banda), run_time=self.dur(0.4))
            self.pop(s2)

            # «memoria de cero coma seis por paso»
            self.en("memoria")
            self.play(FadeIn(a), FadeIn(b), GrowArrow(par), run_time=self.dur(0.5))
            self.pop(mem)
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def cable_y_letras(self):
        t, y, v, x = sensor12(40)
        termo = termometro(2.0, ROJO, 0.6).move_to([-5.2, 0.2, 0])
        pc = ordenador().scale(1.6).move_to([5.2, 0.2, 0])
        cable = Line([-4.6, 0.2, 0], [4.2, 0.2, 0], color=INK, stroke_width=6)
        Lc = Lienzo(ancho=6.0, alto=1.0, t_rango=(0, 39), v_max=3, centro=(0.0, 1.5))
        rn = Lc.curva(t, v, RUIDO, 2.6)
        tallos = Tallos(v[:14], centro=(0.0, 1.5), paso=0.35, unidad=0.4, color=RUIDO)
        var1 = MathTex(r"\sigma^2 = 1", color=RUIDO).scale(0.8).move_to([3.7, 1.6, 0])
        Lb = Lienzo(ancho=2.0, alto=1.0, t_rango=(0, 39), v_max=7, centro=(-4.5, 1.5))
        mini_y = Lb.curva(t, y, SENAL, 3)
        perp = MathTex(r"\perp", color=AMBAR).scale(1.0).move_to([-3.0, 1.5, 0])
        Lp = Lienzo(ancho=1.9, alto=0.7, t_rango=(0, 39), v_max=7, centro=tuple(pc.pantalla.get_center()[:2]))
        en_pc = Lp.curva(t, x, MEDIDA, 2.6)
        # la suma
        cs = [(-4.4, y, SENAL, 7), (0.0, v, RUIDO, 4), (4.4, x, MEDIDA, 7)]
        curvas = []
        for cx, dato, col, vm in cs:
            Lk = Lienzo(ancho=3.4, alto=1.8, t_rango=(0, 39), v_max=vm, centro=(cx, 0.5))
            curvas.append(VGroup(Lk.base(INK, 1.4), Lk.curva(t, dato, col, 3.2)))
        mas = MathTex("+", color=TXT).scale(1.2).move_to([-2.2, 0.5, 0])
        igual = MathTex("=", color=TXT).scale(1.2).move_to([2.2, 0.5, 0])
        arr = Arrow([4.4, -1.1, 0], [-4.4, -1.1, 0], buff=0, color=AMBAR, stroke_width=5,
                    max_tip_length_to_length_ratio=0.06)
        interr = Text("?", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, -1.7, 0])
        antes = Text("antes: s, d, r", color=INK).scale(0.55).move_to([0, 3.0, 0])
        tach = Line(antes.get_left() + LEFT * 0.1, antes.get_right() + RIGHT * 0.1, color=ROJO, stroke_width=5)
        ly = MathTex("y[n]", color=SENAL).scale(0.9).move_to([-4.4, 1.95, 0])
        lv = MathTex("v[n]", color=RUIDO).scale(0.9).move_to([0.0, 1.95, 0])
        lx = MathTex("x[n]", color=MEDIDA).scale(0.9).move_to([4.4, 1.95, 0])
        ecu = formula("x[n]", "=", "y[n]", "+", "v[n]", escala=1.3, colores={0: MEDIDA, 2: SENAL, 4: RUIDO})
        ecu.move_to([0, -2.4, 0])

        with self.narrar("b2"):
            # «el cable»
            self.en("cable")
            self.corte()
            self.play(FadeIn(termo), FadeIn(pc), Create(cable), run_time=self.dur(0.6))

            # «un ruido»
            self.en("ruido")
            self.play(Create(rn), run_time=self.dur(0.7))

            # «blanco, sin memoria»
            self.en("blanco")
            self.play(FadeOut(rn), FadeIn(tallos), run_time=self.dur(0.5))

            # «de varianza uno»
            self.en("var1")
            self.pop(var1)

            # «sin relación con la temperatura»
            self.en("sinrel")
            self.play(Create(mini_y), FadeIn(perp), run_time=self.dur(0.6))

            # «Lo que llega al ordenador»
            self.en("llega")
            self.play(Create(en_pc), run_time=self.dur(0.6))

            # «la temperatura más el ruido»
            self.en("suma")
            self.corte()
            self.play(FadeIn(curvas[0]), run_time=0.4)
            self.play(FadeIn(mas), FadeIn(curvas[1]), run_time=0.4)
            self.play(FadeIn(igual), FadeIn(curvas[2]), run_time=0.4)

            # «Y queremos recuperarla»
            self.en("recuperar")
            self.play(GrowArrow(arr), FadeIn(interr), run_time=self.dur(0.7))

            # «Cambiamos las letras»
            self.en("letras")
            self.play(FadeOut(arr), FadeOut(interr), FadeIn(antes), run_time=self.dur(0.4))
            self.play(Create(tach), run_time=self.dur(0.3))

            # «para coincidir con el libro»
            self.en("libro")
            self.resaltar(antes, color=AMBAR, escala=1.1)

            # «i griega de ene»
            self.en("y")
            self.pop(ly)

            # «en azul»
            self.en("azul")
            self.resaltar(curvas[0], color=SENAL, escala=1.05)

            # «uve de ene»
            self.en("v")
            self.pop(lv)

            # «en magenta»
            self.en("magenta")
            self.resaltar(curvas[1], color=RUIDO, escala=1.05)

            # «equis de ene»
            self.en("x")
            self.pop(lx)

            # «la suma de las dos»
            self.en("xsuma")
            self.play(FadeIn(ecu, shift=UP * 0.2), run_time=self.dur(0.8))
