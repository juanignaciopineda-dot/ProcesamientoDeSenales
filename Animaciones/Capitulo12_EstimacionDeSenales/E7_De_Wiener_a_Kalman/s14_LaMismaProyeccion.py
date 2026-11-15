"""Escena 14 — Todo era una proyección: el mismo dibujo de los capítulos 7 y 8, con un plano que crece."""
from comun.escena import *


class LaMismaProyeccion(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        self.proyeccion()
        self.wait(0.6)
        self.resumen()
        self.wait(1.0)
        self.limpiar()

    def proyeccion(self):
        c7 = caja("capítulo 7", INK, ancho=2.6, alto=0.7, scale=0.45).move_to([-4.6, 3.4, 0])
        c8 = caja("capítulo 8", INK, ancho=2.6, alto=0.7, scale=0.45).move_to([-1.6, 3.4, 0])
        c12 = caja("capítulo 12", AMBAR, ancho=2.6, alto=0.7, scale=0.45).move_to([1.4, 3.4, 0])
        F, R = flechas_xy(origen=(-5.6, -2.3), largo=3.6, angulo=45)
        arco = Arc(radius=0.8, start_angle=0, angle=np.deg2rad(45), color=AMBAR, arc_center=F.o, stroke_width=4)
        rho = MathTex("\\rho=\\cos\\theta", color=AMBAR).scale(0.8).move_to([-1.3, -1.2, 0])
        esq = [F.o + [-0.6, -0.5, 0], F.o + [4.6, -0.5, 0], F.o + [5.0, 1.5, 0], F.o + [-0.2, 1.5, 0]]
        plano = VGroup(Polygon(*esq, stroke_width=0, stroke_opacity=0).set_fill(INK, 0.08),
                       *[Line(esq[i], esq[(i + 1) % 4], color=INK, stroke_width=2) for i in range(4)])
        fila = FilaMuestras(["x[n-3]", "x[n-2]", "x[n-1]", "x[n]", "x[n+1]"], centro=(3.9, 1.7), lado=0.95, escala=0.5)
        marco = fila.marco(1, 3, AMBAR)
        tfir = formula("x[n],\\dots,x[n-L+1]", escala=0.8, colores={0: MEDIDA}).move_to([3.9, 0.3, 0])
        tcau = formula("x[n-k],\\ k\\ge 0", escala=0.8, colores={0: MEDIDA}).move_to([3.9, -0.6, 0])
        tnc = formula("x[n-k],\\ \\text{todo }k", escala=0.8, colores={0: MEDIDA}).move_to([3.9, -1.5, 0])
        with self.narrar("b1"):
            # «desde arriba»
            self.en("arriba")
            self.corte()
            self.play(FadeIn(c7), FadeIn(c8), FadeIn(c12), run_time=self.dur(0.8))
            # «las variables eran flechas»
            self.en("flechas")
            self.play(GrowArrow(F.presente), GrowArrow(F.futuro), FadeIn(R["x"]), FadeIn(R["y"]), run_time=self.dur(0.9))
            self.resaltar(c7, run_time=0.5)
            # «el coseno de un ángulo»
            self.en("coseno")
            self.play(Create(arco), FadeIn(rho), run_time=self.dur(0.8))
            # «En el capítulo ocho»
            self.en("ocho")
            self.resaltar(c8, run_time=0.5)
            # «proyectar una flecha»
            self.en("proyectar")
            self.play(FadeOut(arco), FadeOut(rho), Create(F.sombra), FadeIn(R["yh"]), run_time=self.dur(0.8))
            # «el plano de las mediciones»
            self.en("plano")
            self.play(FadeIn(plano), run_time=self.dur(0.7))
            # «el error en ángulo recto»
            self.en("recto")
            self.play(Create(F.error), Create(F.recto), FadeIn(R["e"]), run_time=self.dur(0.8))
            # «un plano que ha crecido»
            self.en("crecido")
            self.resaltar(c12, run_time=0.5)
            self.play(plano.animate.scale(1.25, about_point=F.o), run_time=self.dur(0.7))
            # «las muestras de la ventana»
            self.en("ventana")
            self.play(FadeIn(fila), FadeIn(marco), run_time=self.dur(0.8))
            # «finito en el FIR»
            self.en("fir")
            self.play(FadeIn(tfir), run_time=self.dur(0.6))
            # «hacia el pasado en el causal»
            self.en("causal")
            self.play(FadeIn(tcau), marco.animate.stretch_to_fit_width(4 * 0.95 + 0.1).move_to(
                [(fila.x(0) + fila.x(3)) / 2, fila.cy, 0]), run_time=self.dur(0.7))
            # «hacia los dos lados en el no causal»
            self.en("nocausal")
            self.play(FadeIn(tnc), marco.animate.stretch_to_fit_width(5 * 0.95 + 0.1).move_to(
                [(fila.x(0) + fila.x(4)) / 2, fila.cy, 0]), run_time=self.dur(0.7))

    def resumen(self):
        self.corte()
        term = termometro(1.4).move_to([-6.0, -2.4, 0])
        x0, esc = -3.6, 0.9
        filas = [(2.8, 4.0, ERROR, "sin datos", "4"), (1.7, 0.8, AMBAR, "una muestra", "0,8"),
                 (0.6, 0.7386, VERDE, "filtro causal", "0,7386"), (-0.5, 0.686, VERDE, "todo el registro", "0,686")]
        barras = [barra_h(v, y, x0, esc, c) for y, v, c, _, _ in filas]
        rots = [etiqueta(t, INK, 0.45).move_to([-6.0, y, 0]).align_to([-6.6, 0, 0], LEFT) for y, _, _, t, _ in filas]
        vals = [MathTex(s.replace(",", "{,}"), color=TXT).scale(0.75).next_to(b, RIGHT, buff=0.2)
                for b, (_, _, _, _, s) in zip(barras, filas)]
        eti = etiqueta("todo el registro:", INK, 0.45).move_to([-3.5, -0.5, 0])
        col = colador(CIAN, 1.4, 1.1).move_to([2.2, 3.1, 0])
        voz = persona(AZUL).scale(0.7).move_to([4.2, 3.1, 0])
        mur = ruido_t(Lienzo(ancho=1.6, alto=0.6, t_rango=(0, 4), v_max=1.0, centro=(5.9, 3.1)), semilla=4, amp=0.25,
                      color=RUIDO)
        Lc = Lienzo(ancho=5.4, alto=2.0, t_rango=(0, np.pi), v_max=1.0, centro=(4.1, -1.6))
        H = lambda w: (lambda S: S / (S + 1))(2.56 / (1.36 - 1.2 * np.cos(w)))
        cur = curva_f(Lc, H, 0, np.pi, CIAN, 4.0)
        ejeH = Lc.base()
        lw = MathTex("\\Omega", color=INK).scale(0.6).move_to([7.0, -2.6, 0])
        mk = Dot(Lc.p(0, H(0.0)), radius=0.1, color=AMBAR)
        fia = etiqueta("me fío", VERDE, 0.5).move_to(Lc.p(0.5, 1.15))
        with self.narrar("b2"):
            # «Recuerda el sensor»
            self.en("sensor")
            self.play(FadeIn(term), run_time=self.dur(0.5))
            # «sin datos, cuatro»
            self.en("s4")
            self.play(FadeIn(rots[0]), GrowFromEdge(barras[0], LEFT), FadeIn(vals[0]), run_time=self.dur(0.8))
            # «Con una muestra, cero coma ocho»
            self.en("s08")
            self.play(FadeIn(rots[1]), GrowFromEdge(barras[1], LEFT), FadeIn(vals[1]), run_time=self.dur(0.8))
            # «Con el filtro causal, cero coma siete tres ocho seis»
            self.en("s7386")
            self.play(FadeIn(rots[2]), GrowFromEdge(barras[2], LEFT), FadeIn(vals[2]), run_time=self.dur(0.8))
            # «Con todo el registro»
            self.en("registro")
            self.play(FadeIn(rots[3]), run_time=self.dur(0.5))
            # «cero coma seis ocho seis»
            self.en("s686")
            self.play(GrowFromEdge(barras[3], LEFT), FadeIn(vals[3]), run_time=self.dur(0.8))
            # «Y aquel colador»
            self.en("colador")
            self.play(FadeIn(col, scale=0.7), run_time=self.dur(0.5))
            # «separar la voz del murmullo»
            self.en("voz")
            self.play(FadeIn(voz), Create(mur), run_time=self.dur(0.8))
            # «es esta curva»
            self.en("curva")
            self.play(Create(ejeH), Create(cur), FadeIn(lw), run_time=self.dur(1.2))
            # «en cada frecuencia»
            self.en("cadafrec")
            self.play(FadeIn(mk), run_time=0.2)
            self.play(MoveAlongPath(mk, cur), run_time=self.dur(1.6), rate_func=linear)
            # «cuánto fiarse de lo medido»
            self.en("fiarse")
            self.play(FadeIn(fia), run_time=self.dur(0.6))
