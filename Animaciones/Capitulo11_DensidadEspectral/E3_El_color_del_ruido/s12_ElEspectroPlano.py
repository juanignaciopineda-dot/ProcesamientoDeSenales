"""Escena 12 — El espectro plano, la constante K, y el nombre: ruido blanco frente a ruido coloreado."""
from comun.escena import *


def _bote():
    cuerpo = RoundedRectangle(corner_radius=0.1, width=1.3, height=1.3, color=TXT, stroke_width=3).set_fill(TXT, 0.85)
    tapa = RoundedRectangle(corner_radius=0.06, width=1.5, height=0.2, color=TXT, stroke_width=3).set_fill(INK, 1)
    tapa.next_to(cuerpo, UP, buff=0)
    t = Text("blanco", color=FONDO, weight=BOLD).scale(0.35).move_to(cuerpo)
    return VGroup(cuerpo, tapa, t)


class ElEspectroPlano(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.plano()
        self.colores()
        self.ingrediente()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def plano(self):
        ks = list(range(-4, 5))
        pal = Palitos(ks, [1.0 if k == 0 else 0.0 for k in ks], ancho=5.4, alto=2.2, v_max=1.6, color=SENAL,
                      centro=(-3.7, -1.9), rotulo="m")
        esp = Espectro(w_max=3.4, y_max=1.6, ancho=5.4, alto=2.2, centro=(3.7, -1.9), x_label=None)
        plano = esp.curva(lambda w: 1.0, AMBAR, a=-np.pi, b=np.pi)
        barras = VGroup(*[Line(esp.p(w, 0), esp.p(w, 1.0), color=AMBAR, stroke_width=5) for w in np.linspace(-3, 3, 15)])
        t_sin = Text("memoria cero", color=SENAL, weight=BOLD).scale(0.6).move_to([-3.7, 1.4, 0])
        t_plano = Text("espectro plano", color=AMBAR, weight=BOLD).scale(0.6).move_to([3.7, 1.4, 0])
        self.add(pal, esp.ejes)
        with self.narrar("b1"):
            # «completamente plano»
            self.en("plano")
            self.play(Create(plano), run_time=self.dur(0.8))
            # «la misma potencia en todas las frecuencias»
            self.en("misma")
            self.play(Create(barras), run_time=self.dur(1.2))
            # «Esa era la respuesta»
            self.en("respuesta")
            ok = tilde().scale(1.1).move_to([6.2, 1.4, 0])
            self.play(FadeIn(t_sin), FadeIn(t_plano), FadeIn(ok), run_time=self.dur(0.6))
            # «memoria cero, espectro plano»
            self.en("regla")
            fl = DoubleArrow([-1.7, 1.4, 0], [1.4, 1.4, 0], buff=0, color=INK, stroke_width=5)
            self.play(GrowFromCenter(fl), run_time=self.dur(0.5))
            # «cada muestra»
            self.en("muestra")
            mu = tira_pm1([1, -1, 1], lado=0.55, escala_txt=0.35).move_to([-1.6, 2.8, 0])
            self.play(FadeIn(mu), run_time=self.dur(0.4))
            # «varianza ka»
            self.en("ka")
            kk = MathTex(r"\sigma^2 = K", color=AMBAR).scale(1.0).move_to([0.8, 2.8, 0])
            self.play(FadeIn(kk), run_time=self.dur(0.5))
            # «plano a altura ka»
            self.en("alturaka")
            plano2 = esp.curva(lambda w: 1.4, AMBAR, a=-np.pi, b=np.pi)
            barras2 = VGroup(*[Line(esp.p(w, 0), esp.p(w, 1.4), color=AMBAR, stroke_width=5) for w in np.linspace(-3, 3, 15)])
            self.play(Transform(plano, plano2), Transform(barras, barras2), run_time=self.dur(0.7))
            # «Una barra de altura ka en el tiempo»
            self.en("barrak")
            self.play(pal.tallos[ks.index(0)].animate.put_start_and_end_on(pal.pos(0, 0), pal.pos(0, 1.4)),
                      pal.puntos[ks.index(0)].animate.move_to(pal.pos(0, 1.4)), run_time=self.dur(0.7))
            # «una línea de altura ka en frecuencia»
            self.en("lineak")
            f = MathTex(r"C_{xx}[m] = K\,\delta[m]", r"\longleftrightarrow", r"D_{xx} = K", color=TXT).scale(0.9).move_to([0, -3.7, 0])
            f[2].set_color(AMBAR)
            self.play(FadeIn(f), run_time=self.dur(0.7))
        self.limpiar()

    # ------------------------------------------------------------ b2
    def colores(self):
        pri = prisma().scale(0.85).move_to([-4.3, 1.6, 0])
        barras = VGroup(*[Rectangle(width=0.5, height=1.4, color=c, stroke_width=0).set_fill(c, 0.8)
                          for c in ARCOIRIS]).arrange(RIGHT, buff=0.06).move_to([3.8, 1.5, 0])
        anchos = (3.4, 3.4, 3.4)
        xs = (-4.6, 0.0, 4.6)
        espec = []
        for x in xs:
            espec.append(Espectro(w_max=3.2, y_max=1.3, ancho=3.4, alto=1.6, centro=(x, -3.3), x_label=None))
        curvas = [
            espec[0].curva(lambda w: 0.2 + 0.9 * np.exp(-((w - 0.7) / 0.8) ** 2), AMBAR, a=-np.pi, b=np.pi),
            espec[1].curva(lambda w: tele_S(w * 2.0) * 1.0, AMBAR, a=-np.pi, b=np.pi),
            espec[2].curva(lambda w: (1 + 0.8 * np.cos(w)) / 1.8 * 1.1, AMBAR, a=-np.pi, b=np.pi),
        ]
        with self.narrar("b2"):
            # «ruido blanco»
            self.en("blanco")
            tb = Text("ruido blanco", color=TXT, weight=BOLD).scale(0.8).move_to([0, 3.4, 0])
            self.pop(tb)
            # «la luz blanca»
            self.en("luz")
            self.play(FadeIn(pri), run_time=self.dur(0.7))
            # «todos los colores con la misma intensidad»
            self.en("colores")
            self.play(LaggedStart(*[FadeIn(b) for b in barras], lag_ratio=0.15), run_time=self.dur(1.2))
            # «Un proceso cuyo espectro»
            self.en("procesoesp")
            self.play(Create(espec[0].ejes), run_time=self.dur(0.5))
            # «tiene forma»
            self.en("forma")
            self.play(Create(curvas[0]), run_time=self.dur(0.8))
            # «más potencia en unas frecuencias que en otras»
            self.en("unasyotras")
            alta = espec[0].area(curvas[0], 0.2, 1.4, VERDE, 0.5)
            baja = espec[0].area(curvas[0], -3, -1.8, ROJO, 0.5)
            self.play(FadeIn(alta), FadeIn(baja), run_time=self.dur(0.6))
            # «coloreado»
            self.en("coloreado")
            tcol = Text("coloreado", color=AMBAR, weight=BOLD).scale(0.6).move_to([-4.6, -1.3, 0])
            self.pop(tcol)
            # «La onda telegráfica»
            self.en("tele")
            self.play(Create(espec[1].ejes), Create(curvas[1]), run_time=self.dur(0.8))
            # «rho igual a cero coma cuatro»
            self.en("rho04")
            self.play(Create(espec[2].ejes), Create(curvas[2]), run_time=self.dur(0.8))
            # «ruidos coloreados»
            self.en("rotulo")
            tcol2 = Text("coloreados", color=AMBAR, weight=BOLD).scale(0.6).move_to([2.3, -1.3, 0])
            self.pop(tcol2)
        self.limpiar()

    # ------------------------------------------------------------ b3
    def ingrediente(self):
        bote = _bote().move_to([-5.2, 1.4, 0])
        filtro = caja("filtro", MAGENTA, ancho=2.0, alto=0.9, scale=0.55).move_to([-1.4, 1.4, 0])
        f1 = flecha([-4.3, 1.4, 0], [-2.5, 1.4, 0], INK)
        esp = Espectro(w_max=3.2, y_max=1.3, ancho=3.4, alto=1.6, centro=(3.5, 0.8), x_label=None)
        rho = esp.curva(lambda w: (1 + 0.8 * np.cos(w)) / 1.8 * 1.1, AMBAR, a=-np.pi, b=np.pi)
        f2 = flecha([-0.2, 1.4, 0], [1.4, 1.4, 0], INK)
        rho_t = MathTex(r"\rho = 0{,}4", color=AMBAR).scale(0.8).move_to([3.5, -0.5, 0])
        cajas = VGroup(caja("?", AMBAR, ancho=3.4, alto=2.4, scale=0.9).move_to([-3.2, -1.8, 0]),
                       caja("?", AMBAR, ancho=3.4, alto=2.4, scale=0.9).move_to([3.2, -1.8, 0]))
        curvas = VGroup(*[
            traza(np.linspace(-1.3, 1.3, 60) + 0.0, y0 + 0.35 * np.sin(np.linspace(0, 3.4 * (i + 1), 60) + i) * np.linspace(1, 0.4, 60), c, 4)
            for i, (y0, c) in enumerate(((0.4, AZUL), (0.0, VERDE), (-0.4, MAGENTA)))]).move_to([3.0, 1.4, 0])
        with self.narrar("b3"):
            # «el ingrediente básico»
            self.en("ingred")
            self.play(FadeIn(bote), run_time=self.dur(0.6))
            # «el proceso del episodio anterior»
            self.en("anterior")
            self.play(Create(f1), FadeIn(filtro), run_time=self.dur(0.6))
            self.play(Create(f2), Create(esp.ejes), Create(rho), FadeIn(rho_t), run_time=self.dur(0.8))
            # «cualquier otro color»
            self.en("otro")
            self.play(*[FadeOut(m) for m in (f2, esp.ejes, rho, rho_t)], FadeIn(curvas), run_time=self.dur(0.6))
            # «dos sorpresas»
            self.en("sorpresas")
            self.play(*[FadeOut(m) for m in (bote, f1, filtro, curvas)], FadeIn(cajas), run_time=self.dur(0.7))
            # «una de ellas»
            self.en("unadeellas")
            self.resaltar(cajas[1], run_time=self.dur(0.6))
            # «no existe»
            self.en("noexiste")
            self.play(cajas[1].animate.fade(0.7), Create(tachar(cajas[1])), run_time=self.dur(0.6))
