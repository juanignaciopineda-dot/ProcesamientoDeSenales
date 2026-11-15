"""Escena 04 — Un filtro adaptado por señal: M filtros en paralelo y la cuenta a mano con tres señales."""
from comun.escena import *

COLS = [SENAL, AZUL_C7, CIAN]
S_VALS = [(1, 1, 0, 0), (0, 0, 1, 1), (1, -1, 0, 0)]
R_VALS = ["0,4", "1", "0,9", "0,7"]
SUMAS = [r"0{,}4+1=1{,}4", r"0{,}9+0{,}7=1{,}6", r"0{,}4-1=-0{,}6"]
GS = [r"g_0=1{,}4", r"g_1=1{,}6", r"g_2=-0{,}6"]
XC = [-3.6, -2.5, -1.4, -0.3]


def casillas(y, textos, color, lado=0.9, rel=0.1):
    g = VGroup()
    for x, t in zip(XC, textos):
        r = Square(side_length=lado, color=color, stroke_width=2.5).set_fill(color, rel).move_to([x, y, 0])
        g.add(r, Text(t, color=TXT, weight=BOLD).scale(0.5).move_to(r))
    return g


class FiltrosEnParalelo(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.paralelo()
        self.wait(0.6)
        self.cuenta()
        self.wait(1.0)
        self.limpiar()

    def paralelo(self):
        R = formula(r"\sum r\,s_i", r"+\sigma^2\ln p_i", r"-\frac{E_i}{2}", escala=1.2,
                    colores={0: MEDIDA, 1: AMBAR, 2: SENAL}).move_to([0, 3.0, 0])
        ys = [1.3, 0.1, -1.1]
        cajas = [caja(f"filtro adaptado a s{'₀₁₂'[i]}", COLS[i], ancho=3.8, alto=0.8, scale=0.5).move_to([-0.8, ys[i], 0])
                 for i in range(3)]
        r_in = MathTex("r", color=MEDIDA).scale(1.2).move_to([-6.2, 0.1, 0])
        ent = [Arrow([-5.8, 0.1, 0], [-2.7, ys[i], 0], buff=0.05, color=INK, stroke_width=3,
                     max_tip_length_to_length_ratio=0.1) for i in range(3)]
        eleg = caja("elegir el mayor", AMBAR, ancho=2.6, alto=2.7, scale=0.5).move_to([4.7, 0.1, 0])
        sal = [Arrow([1.1, ys[i], 0], [3.35, 0.1 + (ys[i] - 0.1) * 0.5, 0], buff=0.05, color=INK, stroke_width=3,
                     max_tip_length_to_length_ratio=0.1) for i in range(3)]
        gs = [MathTex(f"g_{i}", color=COLS[i]).scale(0.75).move_to([2.3, ys[i] + 0.35 - (ys[i] - 0.1) * 0.0, 0])
              for i in range(3)]
        igual_e = etiqueta("igual en las tres", INK, 0.42).move_to([R[2].get_center()[0], 2.1, 0])
        igual_p = etiqueta("igual en las tres", INK, 0.42).move_to([R[1].get_center()[0] - 0.4, 2.1, 0])
        gana = Arrow([1.1, ys[1], 0], [3.35, 0.1, 0], buff=0.05, color=VERDE, stroke_width=6,
                     max_tip_length_to_length_ratio=0.1)
        with self.narrar("b1"):
            # «Se implementa»
            self.paso("implementa", R, t=0.6)
            # «tantos filtros adaptados como señales»
            self.paso("filtros", *cajas, t=0.7)
            # «en paralelo»
            self.en("paralelo")
            self.play(FadeIn(r_in), *[GrowArrow(a) for a in ent], run_time=self.dur(0.7))
            # «un bloque que elige la salida mayor»
            self.en("elige")
            self.play(FadeIn(eleg), *[GrowArrow(a) for a in sal], *[FadeIn(g) for g in gs], run_time=self.dur(0.8))
            # «Y si todas las señales»
            self.en("ysi")
            self.resaltar(eleg, run_time=0.5)
            # «la misma energía»
            self.en("igualenergia")
            self.play(FadeIn(igual_e), run_time=0.4)
            # «la misma probabilidad»
            self.en("igualprior")
            self.play(FadeIn(igual_p), run_time=0.4)
            # «son iguales para todas»
            self.en("iguales")
            self.play(R[1].animate.fade(0.7), R[2].animate.fade(0.7), FadeOut(igual_e), FadeOut(igual_p),
                      run_time=self.dur(0.6))
            # «gana el filtro con la salida más grande»
            self.en("gana")
            self.play(GrowArrow(gana), run_time=self.dur(0.6))
        self.corte()

    def cuenta(self):
        r_rot = MathTex("r=", color=MEDIDA).scale(1.0).move_to([-5.4, 2.6, 0])
        r_cas = casillas(2.6, R_VALS, MEDIDA)
        sig = MathTex(r"\sigma^2=1", color=RUIDO).scale(1.0).move_to([5.0, 2.6, 0])
        rots = [MathTex(f"s_{i}", color=COLS[i]).scale(1.0).move_to([-5.4, y, 0]) for i, y in enumerate([1.1, -0.2, -1.5])]
        filas = [casillas(y, [str(v) for v in S_VALS[i]], COLS[i], rel=0.05) for i, y in enumerate([1.1, -0.2, -1.5])]
        for f in filas:
            for k in range(1, len(f), 2):
                f[k].set_color(INK)
        sumas = [MathTex(SUMAS[i], color=TXT).scale(0.9).move_to([2.6, y, 0]) for i, y in enumerate([1.1, -0.2, -1.5])]
        gs = [MathTex(GS[i], color=COLS[i]).scale(1.0).move_to([5.9, y, 0]) for i, y in enumerate([1.1, -0.2, -1.5])]
        marco = SurroundingRectangle(VGroup(filas[1], sumas[1], gs[1]), color=VERDE, buff=0.18, stroke_width=4)
        marco.permitir_encima = True
        poco = etiqueta("por poco: 1,6 contra 1,4", AMBAR, 0.55).move_to([0, -2.8, 0])
        with self.narrar("b2"):
            # «Con números»
            self.paso("numeros", r_rot, r_cas[0::2], t=0.6)
            # «sigma cuadrado igual a uno»
            self.paso("sigma", sig, t=0.5)
            # «cero coma cuatro, uno»
            self.paso("recibido", r_cas[1], r_cas[3], t=0.5)
            # «cero coma nueve, cero coma siete»
            self.paso("recibido2", r_cas[5], r_cas[7], t=0.5)
            # «Primera señal»
            self.paso("primera", rots[0], filas[0], t=0.6)
            # «uno coma cuatro»
            self.paso("g0", sumas[0], gs[0], t=0.6)
            # «Segunda»
            self.paso("segunda", rots[1], filas[1], t=0.6)
            # «uno coma seis»
            self.paso("g1", sumas[1], gs[1], t=0.6)
            # «Tercera»
            self.paso("tercera", rots[2], filas[2], t=0.6)
            # «menos cero coma seis»
            self.paso("g2", sumas[2], gs[2], t=0.6)
            # «Gana la segunda»
            self.en("ganalasegunda")
            self.play(Create(marco), run_time=self.dur(0.6))
            # «por poco»
            self.paso("porpoco", poco, t=0.5)
