"""Escena 07 — El filtro de Wiener aplicado al sensor: S_yx = S_yy, S_xx = S_yy + 1 y las tres densidades."""
from comun.escena import *


class DensidadesDelSensor(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        fr0 = fraccion(MathTex(r"S_{yx}", color=TXT), MathTex(r"S_{xx}", color=MEDIDA)).scale(0.85)
        fh0 = MathTex("H=", color=ESTIMACION).scale(1.0)
        top = VGroup(fh0, fr0).arrange(RIGHT, buff=0.2).move_to([0, 3.0, 0])
        tm = termometro(alto=1.4, color=ROJO, nivel=0.6).move_to([-6.3, 1.2, 0])
        Ly = Lienzo(ancho=3.0, alto=0.7, t_rango=(0, 1), v_max=2.5, centro=(-3.7, 1.7))
        Lv = Lienzo(ancho=3.0, alto=0.7, t_rango=(0, 1), v_max=2.5, centro=(-3.7, 0.4))
        t = np.linspace(0, 1, 100)
        y, v, x = registro_e3(100, 21)
        ty = Ly.curva(t, y * 0.6, SENAL, 3)
        tv = Lv.curva(t, v * 0.7, RUIDO, 2.5)
        norel = Text("sin ninguna relación", color=AMBAR).scale(0.6).move_to([-3.7, -0.6, 0])
        rowA = formula(r"S_{yx}", "=", r"S_{yy}", "+", r"S_{yv}", escala=1.0,
                       colores={2: SENAL, 4: RUIDO}).move_to([3.0, 1.7, 0])
        rowB = formula(r"S_{xx}", "=", r"S_{yy}", "+", r"S_{vv}", escala=1.0,
                       colores={0: MEDIDA, 2: SENAL, 4: RUIDO}).move_to([3.0, 0.4, 0])
        barra_s = Rectangle(width=1.8, height=0.5, color=SENAL, stroke_width=0).set_fill(SENAL, 0.8)
        barra_r = Rectangle(width=1.1, height=0.5, color=RUIDO, stroke_width=0).set_fill(RUIDO, 0.8)
        suma_b = VGroup(barra_s, barra_r).arrange(RIGHT, buff=0).move_to([3.0, -0.9, 0])
        marco_b = Rectangle(width=2.9, height=0.7, color=MEDIDA, stroke_width=3).move_to(suma_b)
        fh2 = MathTex(r"H(\Omega)=", color=ESTIMACION).scale(1.2)
        fr2 = fraccion(MathTex(r"S_{yy}", color=SENAL), MathTex(r"S_{yy}+1", color=MEDIDA)).scale(1.1)
        res = VGroup(fh2, fr2).arrange(RIGHT, buff=0.25).move_to([0, -2.5, 0])
        with self.narrar("b1"):
            self.en("aplica")                                # «Apliquemos la fórmula»
            self.play(FadeIn(top), run_time=0.5)
            self.en("alsensor")                              # «al sensor»
            self.pop(tm)
            self.en("tyr")                                   # «La temperatura y el ruido»
            self.play(Create(ty), Create(tv), run_time=0.8)
            self.en("norel")                                 # «ninguna relación»
            self.pop(norel)
            self.en("cruz")                                  # «la densidad cruzada entre i griega y equis»
            self.resaltar(fr0.num, color=AMBAR)
            self.en("sola")                                  # «solo la de la temperatura»
            self.play(FadeIn(rowA[0:3]), run_time=0.5)
            self.en("noaporta")                              # «el ruido no aporta»
            self.play(FadeIn(rowA[3:5]), run_time=0.4)
            self.play(Create(tachar(rowA[4], ROJO)), run_time=0.3)
            self.en("medido")                                # «la densidad de lo medido»
            self.resaltar(fr0.den, color=AMBAR)
            self.en("suma")                                  # «la de la temperatura más la del ruido»
            self.play(FadeIn(rowB), run_time=0.7)
            self.en("potsuma")                               # «las potencias de dos señales sin relación se suman»
            self.play(FadeIn(barra_s, shift=RIGHT * 0.4), FadeIn(barra_r, shift=LEFT * 0.4), run_time=0.6)
            self.play(Create(marco_b), run_time=0.4)
            self.en("queda")                                 # «El filtro queda»
            self.play(FadeIn(fh2), FadeIn(fr2.num), run_time=0.5)
            self.en("final")                                 # «entre esa densidad más uno»
            self.play(Create(fr2.barra), FadeIn(fr2.den), run_time=0.5)
            self.resaltar(res, color=AMBAR, escala=1.05)

    def parte_b2(self):
        self.limpiar()
        L = lienzo_omega(ancho=6.4, alto=6.4, v_max=18.0, centro=(3.2, -2.2))
        eje = eje_omega(L, 17.5, escala=0.75)
        curva = curva_f(L, s_senal, 0.0, np.pi, SENAL, 5, n=220)
        barra_s = Rectangle(width=2.2, height=0.5, color=SENAL, stroke_width=0).set_fill(SENAL, 0.8)
        barra_r = Rectangle(width=1.0, height=0.5, color=RUIDO, stroke_width=0).set_fill(RUIDO, 0.8)
        bar = VGroup(barra_s, barra_r).arrange(RIGHT, buff=0).move_to([-3.6, 3.1, 0])
        marco = Rectangle(width=2.4, height=0.72, color=AMBAR, stroke_width=4).move_to(barra_s)
        l_par = Text("la parte que es señal", color=AMBAR).scale(0.6).next_to(bar, DOWN, buff=0.3)
        fs = MathTex(r"S_{yy}(\Omega)=", color=SENAL).scale(1.1)
        den = MathTex("|", "1-0{,}6", r"e^{-j\Omega}", "|^{2}", color=TXT).scale(0.9)
        fr = fraccion(MathTex("2{,}56", color=TXT), den)
        eco = VGroup(fs, fr).arrange(RIGHT, buff=0.2).move_to([-3.6, 0.8, 0])
        l_eco = Text("la del eco del Cap. 11", color=INK).scale(0.55).move_to([3.2, 2.5, 0])
        d0 = Dot(L.p(0, 16), radius=0.1, color=AMBAR)
        t0 = Text("16", color=AMBAR, weight=BOLD).scale(0.65).next_to(d0, UP, buff=0.15)
        d1 = Dot(L.p(np.pi / 2, s_senal(np.pi / 2)), radius=0.1, color=AMBAR)
        t1 = Text("1,88", color=AMBAR, weight=BOLD).scale(0.65).next_to(d1, UP, buff=0.15)
        d2 = Dot(L.p(np.pi, 1.0), radius=0.1, color=AMBAR)
        t2 = Text("1", color=AMBAR, weight=BOLD).scale(0.65).next_to(d2, RIGHT, buff=0.2)
        ruido = Line(L.p(0, 1.0), L.p(np.pi, 1.0), color=RUIDO, stroke_width=4)
        t_r = MathTex(r"S_{vv}=1", color=RUIDO).scale(0.7).next_to(L.p(2.2, 1.0), DOWN, buff=0.15)
        with self.narrar("b2"):
            self.en("parte")                                 # «la parte de lo medido que es señal»
            self.play(FadeIn(bar), Create(marco), FadeIn(l_par), run_time=0.7)
            self.en("dtemp")                                 # «La densidad de la temperatura»
            self.play(FadeIn(fs), run_time=0.4)
            self.en("eco")                                   # «la del eco del capítulo once»
            self.play(Create(eje.h), Create(eje.v), FadeIn(eje.rotulos), run_time=0.4)
            self.play(Create(curva), FadeIn(l_eco), run_time=self.dur(1.0))
            self.en("num")                                   # «dos coma cinco seis»
            self.play(FadeIn(fr.num), Create(fr.barra), run_time=0.5)
            self.en("den")                                   # «el módulo al cuadrado»
            self.play(FadeIn(den[0]), FadeIn(den[3]), run_time=0.4)
            self.en("unomenos")                              # «uno menos cero coma seis»
            self.play(FadeIn(den[1]), run_time=0.4)
            self.en("expo")                                  # «e elevado a menos jota omega»
            self.play(FadeIn(den[2]), run_time=0.4)
            self.en("v16")                                   # «En omega cero vale dieciséis»
            self.play(FadeIn(d0, scale=2), FadeIn(t0), run_time=0.4)
            self.en("v188")                                  # «En pi medios, uno coma ocho ocho»
            self.play(FadeIn(d1, scale=2), FadeIn(t1), run_time=0.4)
            self.en("v1")                                    # «En pi, uno»
            self.play(FadeIn(d2, scale=2), FadeIn(t2), run_time=0.4)
            self.en("ruido")                                 # «El ruido vale uno en todas»
            self.play(Create(ruido), FadeIn(t_r), run_time=0.6)
