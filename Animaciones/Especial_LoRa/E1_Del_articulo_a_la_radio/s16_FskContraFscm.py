"""Escena 16 — Por qué el eco castiga más a la FSK que al chirp de LoRa (FSCM)."""
from comun.escena import *
from comun.figuras_lora import *

U = 3.0     # unidades de pantalla por unidad de amplitud (las flechas de las dos copias)


class FskContraFscm(EscenaCurso):
    ESCENA = "16"

    def construct(self):
        self.que_es()
        self.dos_copias()
        self.suma_y_resta()
        self.respuesta()
        self.chirp()
        self.razon()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def que_es(self):
        fsk = Text("FSK", color=RUIDO, weight=BOLD).scale(1.0).move_to([-3.6, 3.3, 0])
        Pf = PlanoTF(centro=(-3.6, 0.7), ancho=4.6, alto=3.6, escala=0.42)
        s = ValueTracker(64)
        linea = always_redraw(lambda: Pf.tono(s.get_value(), color=RUIDO, grosor=6))
        rot = MathTex("s", "=", color=TXT).scale(1.1).move_to([-4.0, -1.95, 0])
        num = Integer(64, group_with_commas=False, color=RUIDO).scale(1.1).next_to(rot, RIGHT, buff=0.15)
        num.add_updater(lambda m: m.set_value(round(s.get_value())).next_to(rot, RIGHT, buff=0.15))
        fscm = Text("FSCM", color=CIAN, weight=BOLD).scale(1.0).move_to([3.6, 3.3, 0])
        Pc = PlanoTF(centro=(3.6, 0.7), ancho=4.6, alto=3.6, rotulos=False)
        rampa = Pc.rampa(S_EJEMPLO, color=CIAN, grosor=6)
        rx = Text("FFT → Máximo", color=TXT, weight=BOLD).scale(0.7).move_to([0.6, -2.0, 0])
        ig = MathTex("=", color=AMBAR).scale(2.4).move_to([0, 0.7, 0])
        orto = Text("Ortogonales", color=VERDE, weight=BOLD).scale(0.7).move_to([-2.6, -3.2, 0])
        ener = Text("Misma energía", color=VERDE, weight=BOLD).scale(0.7).move_to([2.6, -3.2, 0])
        with self.narrar("b1"):
            # «qué es la FSK»
            self.en("fsk")
            self.pop(fsk)
            # «un tono de frecuencia fija»
            self.en("tono")
            self.play(FadeIn(Pf), run_time=0.3)
            self.add(linea)
            luz0 = Pf.tono(64, color=TXT, grosor=10)
            self.play(Create(luz0), run_time=self.dur(0.4))
            self.play(FadeOut(luz0), run_time=0.2)
            # «El símbolo cero»
            self.en("s0")
            self.add(rot, num)
            self.play(s.animate.set_value(0), run_time=self.dur(0.9))
            # «el veinte»
            self.en("s20")
            self.play(s.animate.set_value(20), run_time=self.dur(0.8))
            # «hasta el ciento veintisiete»
            self.en("s127")
            self.play(s.animate.set_value(127), run_time=self.dur(1.2))
            self.play(s.animate.set_value(64), run_time=self.dur(0.8))
            # «no hay rampas»
            self.en("norampas")
            self.play(FadeIn(fscm), FadeIn(Pc), Create(rampa), run_time=self.dur(0.8))
            # «líneas horizontales»
            self.en("lineas")
            luz = Pf.tono(64, color=TXT, grosor=10)
            self.play(Create(luz), run_time=self.dur(0.6))
            self.play(FadeOut(luz), run_time=0.3)
            # «una transformada y buscar el pico»
            self.en("rx")
            self.pop(rx)
            # «las dos modulaciones empatan»
            self.en("empatan")
            self.pop(ig)
            # «ortogonales»
            self.en("orto")
            self.pop(orto)
            # «la misma energía»
            self.en("ener")
            self.pop(ener)
        num.clear_updaters()
        linea.clear_updaters()

    # ---------------------------------------------------------------- b2
    def dos_copias(self):
        O = np.array([-4.6, 1.2, 0])
        larga = flecha_v(O, O + RIGHT * 0.894 * U, SENAL, 7, 0.14)
        O2 = O + DOWN * 1.3
        corta = flecha_v(O2, O2 + RIGHT * 0.447 * U, CIAN, 7, 0.25)
        a1 = MathTex("0{,}89", color=SENAL).scale(1.2).next_to(larga, UP, buff=0.2)
        a2 = MathTex("0{,}45", color=CIAN).scale(1.2).next_to(corta, DOWN, buff=0.25)
        r1 = Text("Directa", color=SENAL, weight=BOLD).scale(0.55).next_to(larga, RIGHT, buff=0.3)
        r2 = Text("Eco", color=CIAN, weight=BOLD).scale(0.55).move_to([-1.2, O2[1], 0])
        tono = Text("Tono", color=RUIDO, weight=BOLD).scale(1.0).move_to([3.6, 2.6, 0])
        L = Lienzo(ancho=5.0, alto=1.0, t_rango=(0, 1), v_max=1.0, centro=(3.6, 1.3))
        t = np.linspace(0, 1, 200)
        onda = L.curva(t, np.cos(2 * np.pi * 5 * t), RUIDO, 3)
        dep = Text("El giro depende de f", color=AMBAR, weight=BOLD).scale(0.75).move_to([3.4, -1.6, 0])
        with self.narrar("b2"):
            # «dos copias sumadas»
            self.en("dos")
            self.corte()
            self.play(GrowArrow(larga), FadeIn(r1), run_time=self.dur(0.7))
            # «cero coma ocho nueve»
            self.en("a1")
            self.pop(a1, sonido=None)
            # «otra retrasada una muestra»
            self.en("retr")
            self.play(GrowArrow(corta), FadeIn(r2), run_time=self.dur(0.7))
            # «cero coma cuatro cinco»
            self.en("a2")
            self.pop(a2, sonido=None)
            # «un tono»
            self.en("tono")
            self.pop(tono)
            self.play(Create(onda, rate_func=linear), run_time=self.dur(0.9))
            # «con la fase corrida»
            self.en("fase")
            self.play(FadeOut(r2), Rotate(corta, angle=100 * DEGREES, about_point=O2), run_time=self.dur(1.2))
            # «depende de la frecuencia»
            self.en("depende")
            self.pop(dep)

    # ---------------------------------------------------------------- b3
    def suma_y_resta(self):
        f0 = MathTex("f", "=", "0", color=TXT).scale(1.4).move_to([-3.7, 3.2, 0])
        A = np.array([-6.3, 1.8, 0])
        l1 = flecha_v(A, A + RIGHT * 0.894 * U, SENAL, 7, 0.14)
        c1 = flecha_v(A + DOWN * 0.7, A + DOWN * 0.7 + RIGHT * 0.447 * U, CIAN, 7, 0.25)
        v134 = MathTex("0{,}89", "+", "0{,}45", "=", "1{,}34", color=TXT).scale(1.1).move_to([-3.7, 0.2, 0])
        p18 = Text("Potencia: 1,8", color=VERDE, weight=BOLD).scale(0.85).move_to([-3.7, -0.8, 0])
        fb = MathTex("f", "=", "B/2", color=TXT).scale(1.4).move_to([3.5, 3.2, 0])
        B = np.array([1.6, 1.8, 0])
        l2 = flecha_v(B, B + RIGHT * 0.894 * U, SENAL, 7, 0.14)
        c2 = flecha_v(B + DOWN * 0.7, B + DOWN * 0.7 + RIGHT * 0.447 * U, CIAN, 7, 0.25)
        v045 = MathTex("0{,}89", "-", "0{,}45", "=", "0{,}45", color=TXT).scale(1.1).move_to([3.5, 0.2, 0])
        p02 = Text("Potencia: 0,2", color=ERROR, weight=BOLD).scale(0.85).move_to([3.5, -0.8, 0])
        nueve = MathTex(r"\div\, 9", color=AMBAR).scale(2.0).move_to([0, -2.6, 0])
        with self.narrar("b3"):
            # «frecuencia baja»
            self.en("baja")
            self.corte()
            self.pop(f0)
            # «la fase casi no avanza»
            self.en("casi")
            self.play(GrowArrow(l1), GrowArrow(c1), run_time=self.dur(0.7))
            # «apuntan igual y se suman»
            self.en("suman")
            self.play(c1.animate.shift(l1.get_end() - c1.get_start()), run_time=self.dur(0.8))
            # «Uno coma tres cuatro»
            self.en("v134")
            self.play(Write(v134), run_time=self.dur(0.9))
            # «uno coma ocho de potencia»
            self.en("p18")
            self.pop(p18)
            # «en mitad de la banda»
            self.en("mitad")
            self.pop(fb)
            self.play(GrowArrow(l2), GrowArrow(c2), run_time=self.dur(0.6))
            # «media vuelta»
            self.en("media")
            self.play(Rotate(c2, angle=PI, about_point=c2.get_center()), run_time=self.dur(1.0))
            # «resta»
            self.en("resta")
            self.play(c2.animate.shift(l2.get_end() + UP * 0.3 - c2.get_start()), run_time=self.dur(0.6))
            # «cero coma cuatro cinco de amplitud»
            self.en("v045")
            self.play(Write(v045), run_time=self.dur(0.9))
            # «cero coma dos de potencia»
            self.en("p02")
            self.pop(p02)
            # «Nueve veces menos»
            self.en("nueve")
            self.pop(nueve, sonido="impacto")

    # ---------------------------------------------------------------- b4 y b5
    def respuesta(self):
        E = self.E = EjesXY(centro=(-1.7, 0.5), ancho=8.0, alto=4.0, x=(0, 1), y=(0, 2), y_marcas=(0.2, 1, 1.8),
                            rot_y="Potencia que pasa", escala=0.45)
        E.rots[0].shift(RIGHT * 1.0)
        ex = VGroup(Text("0", color=INK).scale(0.45).next_to(E.p(0, 0), DOWN, buff=0.15),
                    Text("B", color=INK).scale(0.45).next_to(E.p(1, 0), DOWN, buff=0.15),
                    Text("Frecuencia", color=INK).scale(0.45).next_to(E.p(0.5, 0), DOWN, buff=0.15))
        f = np.linspace(0, 1, 200)
        curva = self.curva = E.curva(f, ganancia_eco(f), CIAN, 5)
        curva.permitir_encima = True
        pb = VGroup(E.punto(0, 1.8, VERDE, 0.13), E.punto(1, 1.8, VERDE, 0.13))
        pc = E.punto(0.5, 0.2, ERROR, 0.13)
        sel = Text("Selectivo en frecuencia", color=AMBAR, weight=BOLD).scale(0.5).move_to([4.9, 3.1, 0])
        simbolos = (0, 20, 64, 100)
        tallos = self.tallos = VGroup(*[Line(E.p(s / 128, 0), E.p(s / 128, ganancia_eco(s / 128)), color=c, stroke_width=6)
                                        for s, c in zip(simbolos, (VERDE, INK, ERROR, INK))])
        d7 = MathTex(r"-7\ \mathrm{dB}", color=ERROR).scale(1.0).move_to(E.p(0.5, 0.75))
        m8 = MathTex(r"\mathrm{SNR} = -8\ \mathrm{dB}", color=TXT).scale(0.9).move_to([4.9, 2.0, 0])
        nunca = Text("s = 0: falla 0 %", color=VERDE, weight=BOLD).scale(0.55).move_to([4.9, 1.1, 0])
        mas = Text("s = 64: falla 58 %", color=ERROR, weight=BOLD).scale(0.55).move_to([4.9, 0.3, 0])
        self.col = (sel, m8, nunca, mas, d7, pb, pc)
        with self.narrar("b4"):
            # «todas las frecuencias»
            self.en("todas")
            self.corte()
            self.play(FadeIn(E.todo), FadeIn(ex), run_time=self.dur(0.7))
            # «la respuesta del canal»
            self.en("resp")
            self.play(Create(curva, rate_func=linear), run_time=self.dur(1.4))
            # «uno coma ocho en los bordes»
            self.en("bordes")
            self.pop(pb)
            # «cero coma dos en el centro»
            self.en("centro")
            self.pop(pc)
            # «selectivo en frecuencia»
            self.en("selectivo")
            self.pop(sel)
            # «no trata igual a todas»
            self.en("notrata")
            self.play(curva.animate(rate_func=there_and_back).set_stroke(width=10), run_time=self.dur(0.9))
            # «Cada símbolo vive en una sola frecuencia»
            self.en("vive")
            self.play(LaggedStart(*[Create(t) for t in tallos], lag_ratio=0.3), run_time=self.dur(1.4))
            # «salen reforzados»
            self.en("reforz")
            self.play(tallos[0].animate(rate_func=there_and_back).set_stroke(width=12), run_time=self.dur(0.7))
            # «pierden siete decibelios»
            self.en("siete")
            self.play(tallos[2].animate(rate_func=there_and_back).set_stroke(width=12), FadeIn(d7), run_time=self.dur(0.7))
            # «con menos ocho decibelios»
            self.en("m8")
            self.play(Write(m8), run_time=self.dur(0.7))
            # «el símbolo cero no falla nunca»
            self.en("nunca")
            self.pop(nunca)
            # «falla más de la mitad»
            self.en("mas")
            self.pop(mas)
            # «mala suerte»
            self.en("suerte")
            self.play(tallos[2].animate(rate_func=there_and_back).set_stroke(width=12), run_time=self.dur(0.8))

    def chirp(self):
        E, curva = self.E, self.curva
        punto = Dot(E.p(0, 1.8), radius=0.16, color=AMBAR)
        punto.permitir_encima = True
        # casillas 10 a 29, ampliadas
        x0, paso, y0, alto = 3.3, 0.17, -3.1, 2.0
        base = Line([x0 - 0.1, y0, 0], [x0 + 20 * paso + 0.1, y0, 0], color=INK, stroke_width=2)
        xq = lambda q: x0 + (q - 10 + 0.5) * paso
        b20 = Line([xq(20), y0, 0], [xq(20), y0 + alto * 0.8, 0], color=AMBAR, stroke_width=7)
        b18 = Line([xq(18), y0, 0], [xq(18), y0 + alto * 0.2, 0], color=CIAN, stroke_width=7)
        n20 = Text("20", color=AMBAR, weight=BOLD).scale(0.45).move_to([xq(20) + 0.1, y0 - 0.3, 0])
        n18 = Text("18", color=CIAN, weight=BOLD).scale(0.45).move_to([xq(18) - 0.25, y0 - 0.3, 0])
        rc = Text("Casilla", color=INK).scale(0.42).move_to([x0 + 16.5 * paso, y0 - 0.3, 0])
        p08 = MathTex("0{,}8", color=AMBAR).scale(1.0).move_to([xq(20) + 0.6, y0 + alto * 0.8 - 0.2, 0])
        p02 = MathTex("0{,}2", color=CIAN).scale(1.0).move_to([xq(18) - 0.6, y0 + alto * 0.2 + 0.1, 0])
        mismo = Text("Todos los símbolos: × 0,8", color=VERDE, weight=BOLD).scale(0.5).move_to([4.9, 3.1, 0])
        undb = MathTex(r"-1\ \mathrm{dB}", color=VERDE).scale(1.2).move_to([4.5, 2.2, 0])
        ok = tilde(VERDE, 0.7).move_to([6.0, 2.2, 0])
        with self.narrar("b5"):
            # «recorre toda la banda»
            self.en("recorre")
            self.play(FadeOut(self.tallos), *[FadeOut(m) for m in self.col], FadeIn(punto), run_time=0.3)
            self.play(MoveAlongPath(punto, curva, rate_func=linear), run_time=self.dur(1.6))
            # «la zona buena y por la mala»
            self.en("zonas")
            self.play(MoveAlongPath(punto, curva, rate_func=lambda t: 1 - t), run_time=self.dur(2.2))
            # «Al deshacer el chirp»
            self.en("des")
            self.play(Create(base), FadeIn(rc), run_time=self.dur(0.6))
            # «la casilla del símbolo»
            self.en("c20")
            self.play(Create(b20), FadeIn(n20), run_time=self.dur(0.6))
            # «cero coma ocho de la potencia»
            self.en("p08")
            self.pop(p08, sonido=None)
            # «dos más abajo»
            self.en("c18")
            self.play(Create(b18), FadeIn(n18), run_time=self.dur(0.6))
            # «el cero coma dos restante»
            self.en("p02")
            self.pop(p02, sonido=None)
            # «pierden lo mismo»
            self.en("mismo")
            self.pop(mismo)
            # «un decibelio»
            self.en("undb")
            self.pop(undb)
            # «Ninguno tiene mala suerte»
            self.en("ninguno")
            self.play(Create(ok), run_time=self.dur(0.5))
            self.sfx("exito")

    # ---------------------------------------------------------------- b6
    def razon(self):
        una = Text("FSK: una frecuencia por símbolo", color=RUIDO, weight=BOLD).scale(0.56).move_to([-3.7, 2.6, 0])
        mer = Text("Depende de dónde caiga", color=INK, weight=BOLD).scale(0.56).move_to([-3.7, 1.9, 0])
        rep = Text("FSCM: toda la banda", color=CIAN, weight=BOLD).scale(0.56).move_to([-3.7, 0.5, 0])
        pro = Text("Solo pierde el promedio", color=INK, weight=BOLD).scale(0.56).move_to([-3.7, -0.2, 0])
        E = EjesXY(centro=(3.6, -0.3), ancho=5.4, alto=5.2, x=(-12, -2), y=(1e-4, 1), log_y=True,
                   x_marcas=(-12, -8, -4), y_marcas=(1, 1e-1, 1e-2, 1e-3, 1e-4), rot_x="SNR (dB)", rot_y="BER",
                   escala=0.45)
        n = 9      # FSCM con eco baja de 10⁻⁴ después de −4 dB
        c_fscm = E.curva(FSK_SNR[:n], FSCM_ECO[:n], CIAN, 5)
        c_fsk = E.curva(FSK_SNR, FSK_ECO, RUIDO, 5)
        c_fscm.permitir_encima = c_fsk.permitir_encima = True     # la cota «≈ 3 dB» va entre las dos
        mil = DashedLine(E.p(-12, 1e-3), E.p(-2, 1e-3), color=TXT, stroke_width=2.5, dash_length=0.1)
        tres = cota(E.p(-5.5, 1e-3), E.p(-2.7, 1e-3), "≈ 3 dB", AMBAR, DOWN, 0.5, 0.15)
        with self.narrar("b6"):
            # «la razón teórica»
            self.en("razon")
            self.corte()
            # «cada símbolo en una frecuencia»
            self.en("una")
            self.pop(una)
            # «a merced del canal»
            self.en("merced")
            self.play(FadeIn(mer, shift=UP * 0.15), run_time=self.dur(0.5))
            # «reparte cada símbolo por todas»
            self.en("reparte")
            self.pop(rep)
            # «el promedio»
            self.en("promedio")
            self.play(FadeIn(pro, shift=UP * 0.15), run_time=self.dur(0.5))
            # «Las curvas lo confirman»
            self.en("curvas")
            self.play(FadeIn(E.todo), run_time=0.4)
            self.play(Create(c_fscm, rate_func=linear), Create(c_fsk, rate_func=linear), run_time=self.dur(1.2))
            # «uno en mil»
            self.en("mil")
            self.play(Create(mil), run_time=self.dur(0.7))
            # «tres decibelios más»
            self.en("tres")
            self.pop(tres)
