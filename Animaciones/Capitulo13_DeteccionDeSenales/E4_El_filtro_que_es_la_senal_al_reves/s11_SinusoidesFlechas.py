"""Escena 11 — Segunda lectura, en la frecuencia: sinusoides como flechas y por qué conviene alinearlas."""
from comun.escena import *

COMPS = [(1.0, 1.0, -90.0), (0.7, 2.0, -60.0), (0.5, 3.0, -150.0)]   # amplitud, frecuencia, fase (grados)


class SinusoidesFlechas(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        tit = self.palabra("Segunda lectura: la frecuencia", AMBAR, 0.7).move_to([0, 3.4, 0])
        c_sys = caja("Señales y Sistemas", INK, ancho=3.0, alto=0.6, scale=0.4).move_to([-5.2, 3.4, 0])
        t = np.linspace(0, 1, 160)
        Ls = [Lienzo(ancho=4.6, alto=0.95, t_rango=(0, 1), v_max=1.3, centro=(-3.6, y)) for y in (1.9, 0.5, -0.9)]
        comps = [L.curva(t, cos13(t, a, f, ph), INK, 2.6) for L, (a, f, ph) in zip(Ls, COMPS)]
        bases = [L.base(INK, 1.4) for L in Ls]
        Ls2 = Lienzo(ancho=4.2, alto=2.4, t_rango=(0, 1), v_max=2.3, centro=(3.6, 0.6))
        total = sum(cos13(t, a, f, ph) for a, f, ph in COMPS)
        suma = Ls2.curva(t, total, SENAL, 3.4)
        base_s = Ls2.base(INK, 1.6)
        sig = MathTex(r"=", color=TXT).scale(1.2).move_to([-0.55, 0.6, 0])
        flecha_amp = DoubleArrow(Ls[0].p(0.25, 0), Ls[0].p(0.25, 1.0), color=AMBAR, buff=0, stroke_width=3, tip_length=0.15)
        flecha_des = Arrow(Ls[0].p(0, 1.15), Ls[0].p(0.25, 1.15), color=AMBAR, buff=0, stroke_width=3, tip_length=0.15)
        c_11 = caja("capítulo 11", INK, ancho=2.4, alto=0.6, scale=0.4).move_to([5.3, 3.4, 0])
        pl = plano_c(centro=(4.2, -2.0), radio=0.8)
        fl = flecha_c(pl.o, 0.8, 40, AMBAR, 6)
        l_long = etiqueta("longitud: la amplitud", AMBAR, 0.45).move_to([1.3, -2.4, 0])
        arco = Arc(radius=0.4, start_angle=0, angle=np.deg2rad(40), color=AMBAR, stroke_width=4).move_arc_center_to(pl.o)
        l_ang = etiqueta("ángulo: la fase", AMBAR, 0.45).move_to([1.3, -3.0, 0])

        with self.narrar("b1"):
            # «Segunda lectura, en la frecuencia»
            self.en("lectura")
            self.pop(tit)

            # «De Señales y Sistemas»
            self.en("sys")
            self.play(FadeIn(c_sys), run_time=self.dur(0.4))

            # «una suma de sinusoides»
            self.en("suma")
            self.play(LaggedStart(*[FadeIn(VGroup(b, c)) for b, c in zip(bases, comps)], lag_ratio=0.35),
                      run_time=self.dur(1.2))
            self.play(FadeIn(sig), FadeIn(base_s), Create(suma), run_time=self.dur(1.2))

            # «una amplitud y una fase»
            self.en("ampfase")
            self.play(comps[0].animate.set_color(AMBAR), run_time=0.3)
            self.play(Create(flecha_amp), run_time=self.dur(0.4))

            # «un desplazamiento»
            self.en("desp")
            self.play(Create(flecha_des), run_time=self.dur(0.5))

            # «el capítulo once»
            self.en("cap11")
            self.play(FadeIn(c_11), run_time=self.dur(0.4))

            # «una flecha»
            self.en("flecha")
            self.play(FadeIn(pl), run_time=0.3)
            self.play(GrowArrow(fl), run_time=self.dur(0.5))

            # «una longitud, la amplitud»
            self.en("long")
            self.play(FadeIn(l_long), run_time=self.dur(0.4))

            # «un ángulo, la fase»
            self.en("ang")
            self.play(Create(arco), FadeIn(l_ang), run_time=self.dur(0.5))

        # segunda parte: cuándo se suman al máximo
        L2 = Lienzo(ancho=4.6, alto=2.4, t_rango=(0, 1), v_max=2.3, centro=(4.4, 0.4))
        suma2 = L2.curva(t, total, SENAL, 3.4)
        base2 = L2.base(INK, 1.6)
        p2 = plano_c(centro=(-2.6, 0.2), radio=1.0)
        q = interrogante13(AMBAR, 1.6).move_to([-2.6, 2.6, 0])
        t0 = 0.0
        mues = L2.vertical(t0, color=AMBAR, ancho=3.0)
        mues_l = MathTex(r"n=2", color=AMBAR).scale(0.7).next_to(mues, UP, buff=0.1)
        u = 1.2
        misma = VGroup(flecha_c(p2.o, u * 0.8, 30, SENAL, 5), flecha_c(p2.o, u * 1.2, 30, SENAL, 5),
                       flecha_c(p2.o, u * 1.6, 30, SENAL, 5))
        a1, a2, a3 = [flecha_c(p2.o, u, g, AMBAR, 6) for g in (0, 120, 240)]
        l0 = MathTex(r"0^\circ", color=TXT).scale(0.6).move_to(p2.o + np.array([u + 0.45, 0.0, 0.0]))
        l120 = MathTex(r"120^\circ", color=TXT).scale(0.6).move_to(p2.o + 1.55 * np.array([np.cos(np.deg2rad(120)), np.sin(np.deg2rad(120)), 0.0]))
        l240 = MathTex(r"240^\circ", color=TXT).scale(0.6).move_to(p2.o + 1.55 * np.array([np.cos(np.deg2rad(240)), np.sin(np.deg2rad(240)), 0.0]))
        o = p2.o
        dir1 = np.array([u, 0.0, 0.0])
        dir2 = u * np.array([np.cos(np.deg2rad(120)), np.sin(np.deg2rad(120)), 0.0])
        dir3 = u * np.array([np.cos(np.deg2rad(240)), np.sin(np.deg2rad(240)), 0.0])
        a2_enc = flecha_c(o + dir1, u, 120, AMBAR, 6)
        a3_enc = flecha_c(o + dir1 + dir2, u, 240, AMBAR, 6)
        z0 = MathTex(r"\sum=0", color=VERDE).scale(1.1).move_to([-2.6, -2.2, 0])
        al2 = flecha_c(o + dir1, u, 0, AMBAR, 6)
        al3 = flecha_c(o + 2 * dir1, u, 0, AMBAR, 6)
        z3 = MathTex(r"\sum=3", color=VERDE).scale(1.1).move_to([-2.6, -2.2, 0])

        with self.narrar("b2"):
            # «qué haría falta»
            self.en("falta")
            self.corte()
            self.play(FadeIn(p2), FadeIn(base2), Create(suma2), run_time=self.dur(0.9))
            self.pop(q)

            # «se sumaran lo más posible»
            self.en("sumar")
            self.resaltar(suma2, color=AMBAR, escala=1.05)

            # «instante de muestreo»
            self.en("muestreo")
            self.play(Create(mues), FadeIn(mues_l), run_time=self.dur(0.5))

            # «apuntaran en la misma dirección»
            self.en("misma")
            self.play(FadeOut(q), LaggedStart(*[GrowArrow(a) for a in misma], lag_ratio=0.25), run_time=self.dur(1.0))

            # «tres flechas de longitud uno»
            self.en("tres")
            self.play(FadeOut(misma), FadeOut(suma2), FadeOut(base2), FadeOut(mues), FadeOut(mues_l),
                      run_time=self.dur(0.4))
            self.play(GrowArrow(a1), GrowArrow(a2), GrowArrow(a3), run_time=self.dur(0.7))

            # «en ángulos cero»
            self.en("a0")
            self.play(FadeIn(l0), run_time=0.3)

            # «ciento veinte»
            self.en("c120")
            self.play(FadeIn(l120), run_time=0.3)

            # «doscientos cuarenta grados»
            self.en("c240")
            self.play(FadeIn(l240), run_time=0.3)

            # «suman cero»
            self.en("cero")
            self.play(FadeOut(l0), FadeOut(l120), FadeOut(l240), FadeOut(a2), FadeOut(a3), run_time=0.3)
            self.play(GrowArrow(a2_enc), run_time=self.dur(0.5))
            self.play(GrowArrow(a3_enc), run_time=self.dur(0.5))
            self.play(FadeIn(z0), run_time=0.3)

            # «Alineadas, suman tres»
            self.en("alin")
            self.play(FadeOut(a2_enc), FadeOut(a3_enc), FadeOut(z0), run_time=0.3)
            self.play(GrowArrow(al2), run_time=self.dur(0.4))
            self.play(GrowArrow(al3), run_time=self.dur(0.4))
            self.play(FadeIn(z3), run_time=0.3)
        self.wait(1.0)
        self.limpiar()
