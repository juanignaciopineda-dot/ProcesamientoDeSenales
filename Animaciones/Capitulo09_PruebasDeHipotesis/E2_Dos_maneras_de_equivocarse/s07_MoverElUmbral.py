"""Escena 07 — Con 0,7 / 0,3 el umbral pasa a 1,42: falsa alarma 0,077, fallo 0,28, error 0,139."""
from comun.escena import *
from comun.figuras_c9e2 import *


class MoverElUmbral(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.falsa_alarma()
        self.fallo()
        self.media()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def falsa_alarma(self):
        C = Campanas9()
        self.C = C
        eje = C.eje(marcas=(0, 1, 2))
        c0 = C.campana(0, 1, C0)
        c1 = C.campana(2, 1, C1)
        u = umbral9(C, 1)
        frec = MathTex(r"p_0 = 0{,}7", r"\quad", r"p_1 = 0{,}3", color=TXT).scale(0.85).move_to([-4.0, 3.3, 0])
        frec[0].set_color(C0)
        frec[2].set_color(C1)
        cruce = Dot(C.p(CRUCE9, C.f(0, CRUCE9, P0)), radius=0.1, color=ESTIMACION)
        map_t = Text("Máximo a posteriori", color=ESTIMACION, weight=BOLD).scale(0.5).move_to([3.8, 2.5, 0])
        cola_fa = C.area(0, 1, CRUCE9, 5)
        q142 = MathTex(r"Q(1{,}42)", r"=", r"0{,}077", color=TXT).scale(0.85).move_to([-4.0, 2.5, 0])
        q142[2].set_color(ERROR)
        mitad = MathTex(r"0{,}159", r"\to", r"0{,}077", color=TXT).scale(0.8).move_to([-4.3, 1.7, 0])
        baja = Arrow(UP * 0.3, DOWN * 0.3, color=VERDE, stroke_width=5, buff=0).next_to(mitad, RIGHT, buff=0.2)
        self.p = dict(eje=eje, c0=c0, c1=c1, u=u, frec=frec, cola_fa=cola_fa, q142=q142, mitad=mitad, baja=baja)

        with self.narrar("b1"):
            # «los ceros más frecuentes»
            self.en("frec")
            self.play(FadeIn(eje), Create(c0), Create(c1), FadeIn(u), run_time=self.dur(0.7))
            self.play(Write(frec), run_time=self.dur(0.6))

            # «setenta y treinta»
            self.en("escala")
            c0.save_state()
            c1.save_state()
            self.play(Transform(c0, C.campana(0, P0, C0)), Transform(c1, C.campana(2, P1, C1)), run_time=self.dur(0.8))
            self.play(FadeIn(cruce, scale=0.4), run_time=self.dur(0.3))

            # «La regla del máximo a posteriori»
            self.en("map")
            self.play(FadeIn(map_t, shift=DOWN * 0.2), run_time=self.dur(0.4))

            # «el umbral en uno coma cuarenta y dos»
            self.en("umbral")
            self.play(Restore(c0), Restore(c1), FadeOut(cruce), FadeOut(map_t),
                      u.animate.shift(RIGHT * (C.L.x(CRUCE9) - C.L.x(1))), run_time=self.dur(0.9))
            nuevo = Text("1,42", color=ESTIMACION).scale(0.45).move_to(C.p(CRUCE9) + DOWN * 0.32 + RIGHT * 0.12)
            self.play(FadeIn(nuevo), run_time=0.25)

            # «La falsa alarma es la cola»
            self.en("cola_fa")
            self.play(FadeIn(cola_fa), run_time=self.dur(0.5))

            # «cu de uno coma cuarenta y dos»
            self.en("q142")
            self.play(Write(q142[0]), run_time=self.dur(0.5))

            # «cero coma cero setenta y siete»
            self.en("v077")
            self.play(Write(q142[1:]), run_time=self.dur(0.5))

            # «Ha bajado a la mitad»
            self.en("mitad")
            self.play(Write(mitad), GrowArrow(baja), run_time=self.dur(0.6))
        self.p["nuevo"] = nuevo

    # ------------------------------------------------------------ b2
    def fallo(self):
        C = self.C
        cola_m = C.area(2, 1, -3, CRUCE9)
        dos = Dot(C.p(2), radius=0.1, color=C1)
        cota = cota9(C.p(CRUCE9) + DOWN * 0.75, C.p(2) + DOWN * 0.75, "0,58 desvíos")
        q1 = MathTex(r"\tfrac{2-1{,}42}{1} = 0{,}58", color=TXT).scale(0.8).move_to([3.6, 3.3, 0])
        q2 = MathTex(r"Q(0{,}58)", r"=", r"0{,}28", color=TXT).scale(0.85).move_to([3.6, 2.5, 0])
        q2[2].set_color(ERROR)
        doble = MathTex(r"0{,}159", r"\to", r"0{,}28", color=TXT).scale(0.8).move_to([3.3, 1.7, 0])
        sube = Arrow(DOWN * 0.3, UP * 0.3, color=ERROR, stroke_width=5, buff=0).next_to(doble, RIGHT, buff=0.2)
        self.p.update(cola_m=cola_m, dos=dos, cota=cota, q1=q1, q2=q2, doble=doble, sube=sube)

        with self.narrar("b2"):
            # «El fallo»
            self.en("fallo")
            self.play(FadeIn(cola_m), run_time=self.dur(0.5))

            # «que está en dos»
            self.en("dos")
            self.play(FadeIn(dos, scale=0.4), run_time=self.dur(0.4))

            # «cero coma cincuenta y ocho desvíos»
            self.en("cota")
            self.play(FadeIn(cota), run_time=self.dur(0.5))

            # «Cu de cero coma cincuenta y ocho»
            self.en("q058")
            self.play(Write(q1), run_time=self.dur(0.7))
            self.play(Write(q2[0]), run_time=self.dur(0.4))

            # «cero coma veintiocho»
            self.en("v028")
            self.play(Write(q2[1:]), run_time=self.dur(0.5))

            # «Casi se ha duplicado»
            self.en("doble")
            self.play(Write(doble), GrowArrow(sube), run_time=self.dur(0.6))

    # ------------------------------------------------------------ b3
    def media(self):
        p = self.p
        plano = VGroup(p["eje"], p["c0"], p["c1"], p["u"], p["cola_fa"], p["cola_m"], p["dos"], p["nuevo"])
        textos = VGroup(p["frec"], p["q142"], p["mitad"], p["baja"], p["cota"], p["q1"], p["q2"], p["doble"], p["sube"])
        f = MathTex("P_e", "=", "p_0", r"\cdot", "P_{FA}", "+", "p_1", r"\cdot", "P_M", color=TXT).scale(0.95)
        f.move_to([0, -1.2, 0])
        for i, c in ((0, ERROR), (2, C0), (4, ERROR), (6, C1), (8, ERROR)):
            f[i].set_color(c)
        t0 = MathTex(r"0{,}7 \cdot 0{,}077", color=TXT).scale(0.9).move_to([-1.6, -2.15, 0])
        t1 = MathTex(r"+\ 0{,}3 \cdot 0{,}28", color=TXT).scale(0.9).move_to([1.6, -2.15, 0])
        r0 = MathTex(r"0{,}054", color=TXT).scale(0.9).move_to([-2.4, -3.15, 0])
        r1 = MathTex(r"+\ 0{,}085", color=TXT).scale(0.9).move_to([-0.6, -3.15, 0])
        total = MathTex(r"=\ 0{,}139", color=VERDE).scale(0.95).move_to([1.6, -3.15, 0])
        marco = SurroundingRectangle(total, color=VERDE, buff=0.15, stroke_width=4)

        with self.narrar("b3"):
            # «la media ponderada»
            self.en("formula")
            self.play(FadeOut(textos), plano.animate.scale(0.7).move_to([0, 2.15, 0]), run_time=self.dur(0.7))
            self.play(Write(f), run_time=self.dur(0.8))

            # «Cero coma siete por cero coma cero setenta y siete»
            self.en("t0")
            self.play(Write(t0), run_time=self.dur(0.6))

            # «más cero coma tres por cero coma veintiocho»
            self.en("t1")
            self.play(Write(t1), run_time=self.dur(0.6))

            # «Cero coma cero cincuenta y cuatro»
            self.en("r0")
            self.play(Write(r0), run_time=self.dur(0.5))

            # «más cero coma cero ochenta y cinco»
            self.en("r1")
            self.play(Write(r1), run_time=self.dur(0.5))

            # «cero coma ciento treinta y nueve»
            self.en("total")
            self.pop(total)
            self.play(Create(marco), run_time=self.dur(0.4))
            self.sfx("exito", gain=-20)
