"""Escena 13 — El módulo acentúa donde hay señal; el ruido, de fase al azar, no se alinea."""
from comun.escena import *


class ElRuidoDesordenado(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        L = Lienzo(ancho=9.0, alto=2.8, t_rango=(0, 1), v_max=1.2, centro=(0, 0.0))
        base = L.base(INK, 2.0)
        bulto = lambda x: np.exp(-((np.asarray(x) - 0.3) / 0.11) ** 2)
        h_cur = curva_f(L, lambda x: 0.85 * bulto(x), 0.0, 1.0, ESTIMACION, 4.0)
        s_cur = curva_f(L, lambda x: 0.4 * bulto(x), 0.0, 1.0, SENAL, 4.0)
        s_alta = curva_f(L, lambda x: 0.85 * 0.4 * bulto(x) * 2.0, 0.0, 1.0, SENAL, 4.0)
        r_lin = Line(L.p(0.0, 0.25), L.p(1.0, 0.25), color=RUIDO, stroke_width=4)
        r_lin2 = Line(L.p(0.0, 0.27), L.p(1.0, 0.27), color=RUIDO, stroke_width=4)
        l_h = MathTex(r"|H|", color=ESTIMACION).scale(0.9).move_to(L.p(0.5, 1.12))
        l_ru = etiqueta("ruido blanco", RUIDO, 0.5).move_to(L.p(0.85, -0.3))
        area = area_f(L, lambda x: 0.85 * bulto(x), 0.1, 0.5, AMBAR, 0.3)
        baja = Arrow(L.p(0.78, 0.5), L.p(0.78, 0.05), color=AMBAR, buff=0, stroke_width=4, max_tip_length_to_length_ratio=0.25)
        sube = Arrow(L.p(0.3, 0.9), L.p(0.3, 1.1), color=AMBAR, buff=0, stroke_width=4, max_tip_length_to_length_ratio=0.4)
        l_sen = etiqueta("señal", SENAL, 0.5).move_to(L.p(0.3, -0.3))
        # segundo bloque
        pl = plano_c(centro=(-3.5, 0.3), radio=1.5)
        o = pl.o
        angs = (20, 95, 170, 250, 320)
        largos = (0.9, 0.9, 0.9, 0.9, 0.9)
        giros = (55, 105, -130, 50, -190)
        ang2 = [a + g for a, g in zip(angs, giros)]
        fl = [flecha_c(o, l, a, RUIDO, 5) for a, l in zip(angs, largos)]
        girar = [Rotate(f, angle=np.deg2rad(g), about_point=o) for f, g in zip(fl, giros)]
        cadena = []
        p = o.copy()
        for a, l in zip(ang2, largos):
            cadena.append(flecha_c(p, l, a, RUIDO, 5))
            p = p + l * np.array([np.cos(np.deg2rad(a)), np.sin(np.deg2rad(a)), 0.0])
        corta = Arrow(o, p, color=AMBAR, buff=0, stroke_width=6, max_tip_length_to_length_ratio=0.2)
        rl = reloj().scale(1.1).move_to([-3.4, 1.9, 0])
        esp = campana_mini(centro=(3.4, 1.9), ancho=1.8, alto=1.1, color=SENAL)
        base_e = Line([2.4, 1.35, 0], [4.4, 1.35, 0], color=INK, stroke_width=2)
        pico = Tallos(AUT13, centro=(-3.4, -0.3), paso=0.4, unidad=0.14, color=AMBAR)
        alin = VGroup(*[flecha_c([2.3 + 0.55 * i, -0.4, 0], 0.5, 0, SENAL, 5) for i in range(3)])
        desor = VGroup(*[flecha_c([2.4 + 0.55 * i, -1.9, 0], 0.5, g, RUIDO, 5) for i, g in enumerate((20, 140, 250, 330, 80))])

        with self.narrar("b1"):
            # «el módulo hace su parte»
            self.en("modulo")
            self.play(Create(base), run_time=self.dur(0.3))
            self.play(Create(s_cur), FadeIn(l_sen), run_time=self.dur(0.6))
            self.play(Create(h_cur), FadeIn(l_h), run_time=self.dur(0.8))

            # «amplifica las frecuencias donde la señal tiene contenido»
            self.en("ampl")
            self.play(FadeIn(area), run_time=self.dur(0.5))

            # «atenúa donde no lo tiene»
            self.en("atenua")
            self.play(Create(baja), run_time=self.dur(0.5))

            # «El ruido blanco es plano»
            self.en("plano")
            self.play(Create(r_lin), FadeIn(l_ru), run_time=self.dur(0.6))

            # «lo mismo en todas las frecuencias»
            self.en("todas")
            self.play(Indicate(r_lin, color=RUIDO, scale_factor=1.0), run_time=self.dur(0.7))

            # «Así que amplificar»
            self.en("asique")
            self.play(Create(sube), run_time=self.dur(0.4))

            # «gana señal sin ganar tanto ruido»
            self.en("gana")
            self.play(Transform(s_cur, s_alta), Transform(r_lin, r_lin2), run_time=self.dur(1.0))

        with self.narrar("b2"):
            # «¿Y el ruido?»
            self.en("ruido")
            self.corte()
            self.play(FadeIn(pl), run_time=self.dur(0.4))

            # «ángulos al azar»
            self.en("azar")
            self.play(LaggedStart(*[GrowArrow(f) for f in fl], lag_ratio=0.3), run_time=self.dur(1.2))

            # «Al girarlas»
            self.en("girar")
            self.play(*girar, run_time=self.dur(1.0))

            # «no se suman»
            self.en("nosuma")
            self.play(FadeOut(VGroup(*fl)), run_time=0.2)
            self.play(LaggedStart(*[GrowArrow(c) for c in cadena], lag_ratio=0.3), run_time=self.dur(1.2))

            # «una flecha corta»
            self.en("corta")
            self.play(GrowArrow(corta), run_time=self.dur(0.5))

            # «Las dos lecturas»
            self.en("dos")
            self.corte()
            self.play(FadeIn(rl), FadeIn(base_e), Create(esp), run_time=self.dur(0.8))

            # «en el tiempo, el filtro busca parecidos»
            self.en("tiempo")
            self.play(FadeIn(pico), run_time=self.dur(0.6))

            # «en la frecuencia, pone la señal en fase»
            self.en("fase")
            self.play(LaggedStart(*[GrowArrow(a) for a in alin], lag_ratio=0.25), run_time=self.dur(0.8))

            # «deja al ruido desordenado»
            self.en("desorden")
            self.play(LaggedStart(*[GrowArrow(a) for a in desor], lag_ratio=0.2), run_time=self.dur(0.9))
        self.wait(1.0)
        self.limpiar()
