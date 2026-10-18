"""Escena 08 — Marginales de la colina (aplastarla contra un eje) y el centro de masa de la nube."""
from comun.escena import *


class AplastarLaColina(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        colina = Colina(centro=(-1.4, 0.7), rho=0.82, ancho=5.4, prof=2.6, alto=2.4, n=17)
        tabla = Tabla2x2(centro=(5.3, 0.2), lado=1.2)
        tvals = [[tabla.valor(i, j, v, VERDE, 0.7) for j, v in enumerate(f)]
                 for i, f in enumerate([[r"0{,}63", r"0{,}07"], [r"0{,}03", r"0{,}27"]])]
        for f in tabla.rot_f + tabla.rot_c:
            f.scale(0.7)
        llaves = [Brace(VGroup(tabla.cel[i][0], tabla.cel[i][1]), RIGHT, color=SENAL, buff=0.08) for i in range(2)]
        corte = colina.corte_u(0.6, AMBAR, 5)
        recorrido = Arrow(colina.P(0.6, -colina.r) + DOWN * 0.25, colina.P(0.6, colina.r) + DOWN * 0.25,
                          color=AMBAR, buff=0, stroke_width=5, max_tip_length_to_length_ratio=0.1)
        fxf = formula("f_X(x)", "=", r"\int", r"f_{XY}(x,y)", r"\,dy", escala=1.0,
                      colores={0: SENAL}).move_to([0, 3.4, 0])
        x0 = float(colina.P(0, 0)[0])
        yb = -3.0
        xs = np.linspace(-colina.r, colina.r, 100)
        fx = traza(x0 + xs / colina.r * 2.7, yb + 1.9 * gaussiana(xs, 0, 1) / gaussiana(0, 0, 1), SENAL, 5)
        base_x = Line([x0 - 2.9, yb, 0], [x0 + 2.9, yb, 0], color=INK, stroke_width=2)
        fy = traza(-5.9 + 1.2 * gaussiana(xs, 0, 1.2) / gaussiana(0, 0, 1.2) * 0.9,
                   0.7 + xs / colina.r * 2.2, MEDIDA, 5)
        base_y = Line([-5.9, 0.7 - 2.4, 0], [-5.9, 0.7 + 2.4, 0], color=INK, stroke_width=2)
        with self.narrar("b1"):
            # «Las marginales»
            self.en("marginales")
            self.play(FadeIn(colina.base), run_time=0.2)
            self.play(LaggedStart(*[AnimationGroup(FadeIn(r[0]), FadeIn(r[1])) for r in colina.filas],
                                  lag_ratio=0.04), run_time=self.dur(1.0))
            pal = self.palabra("marginales", AMBAR, 1.0).move_to([4.6, 3.4, 0])
            self.pop(pal)

            # «sumábamos cada fila»
            self.en("filas")
            self.play(Create(VGroup(*[c for f in tabla.cel for c in f])), FadeIn(VGroup(*tabla.rot_f, *tabla.rot_c)),
                      FadeIn(VGroup(*[v for f in tvals for v in f])), run_time=self.dur(0.7))
            self.play(*[GrowFromCenter(l) for l in llaves], run_time=self.dur(0.5))

            # «para cada valor de equis»
            self.en("cada_x")
            self.play(FadeOut(VGroup(tabla, *[v for f in tvals for v in f], *llaves)), run_time=0.3)
            self.play(Create(corte), run_time=self.dur(0.6))

            # «a lo largo de i griega»
            self.en("a_lo_largo")
            self.play(GrowArrow(recorrido), run_time=self.dur(0.7))

            # «integramos»
            self.en("integramos")
            self.play(FadeIn(fxf[0:2], shift=DOWN * 0.15), run_time=self.dur(0.5))
            self.play(FadeIn(fxf[2:], shift=DOWN * 0.15), run_time=self.dur(0.7))

            # «aplastar la colina»
            self.en("aplastar")
            self.play(FadeOut(corte), FadeOut(recorrido), run_time=0.2)
            copia = colina.copy()
            self.add(copia)
            self.play(copia.animate.stretch_to_fit_height(0.25).move_to([x0, yb + 0.2, 0]),
                      run_time=self.dur(1.2))

            # «la densidad de equis sola»
            self.en("fx")
            self.play(FadeOut(copia), Create(base_x), run_time=0.3)
            self.play(Create(fx), run_time=self.dur(1.0))
            lx = MathTex("f_X", color=SENAL).scale(1.0).move_to([x0 + 3.1, yb + 1.0, 0])
            self.play(FadeIn(lx), run_time=0.3)

            # «contra el otro eje»
            self.en("fy")
            self.play(Create(base_y), run_time=0.3)
            self.play(Create(fy), run_time=self.dur(1.0))
            ly = MathTex("f_Y", color=MEDIDA).scale(1.0).move_to([-4.8, 3.3, 0])
            self.play(FadeIn(ly), run_time=0.3)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        ax, lab = ejes([-1, 4.5, 1], [-1, 4.5, 1], ancho=6.2, alto=4.6, x_label="x", y_label="y")
        g = VGroup(ax, lab).move_to([0, 0.5, 0])
        px, py = nube_xy7(110, 4)
        px, py = px + 1.8, py + 1.8
        puntos = VGroup(*[Dot(ax.c2p(a, b), radius=0.06, color=SENAL) for a, b in zip(px, py)])
        filo = Triangle(color=INK, stroke_width=3).set_fill(INK, 0.25).scale(0.45).move_to(ax.c2p(1.8, -1) + DOWN * 0.45)
        centro = Dot(ax.c2p(1.8, 1.8), radius=0.15, color=AMBAR)
        aro = Circle(radius=0.3, color=AMBAR, stroke_width=4).move_to(centro)
        gx = DashedLine(ax.c2p(1.8, 1.8), ax.c2p(1.8, -1), color=AMBAR, stroke_width=3)
        gy = DashedLine(ax.c2p(1.8, 1.8), ax.c2p(-1, 1.8), color=AMBAR, stroke_width=3)
        mx = MathTex("E[X]", color=AMBAR).scale(0.9).move_to(ax.c2p(2.55, -0.45))
        my = MathTex("E[Y]", color=AMBAR).scale(0.9).next_to(ax.c2p(-1, 1.8), LEFT, buff=0.15)
        for p in puntos:
            p.permitir_encima = True
        interr = Text("?", color=AMBAR, weight=BOLD).scale(2.2).move_to(ax.c2p(3.0, 3.6))
        corte = DashedLine(ax.c2p(3.2, -1), ax.c2p(3.2, 4.5), color=AMBAR, stroke_width=4)
        banda = Rectangle(width=0.5, height=float(ax.c2p(0, 4.5)[1] - ax.c2p(0, -1)[1]), stroke_width=0
                          ).set_fill(AMBAR, 0.25).move_to([float(ax.c2p(3.2, 0)[0]), float(ax.c2p(0, 1.75)[1]), 0])
        with self.narrar("b2"):
            # «punto de equilibrio»
            self.en("equilibrio")
            self.corte()
            self.play(Create(ax), FadeIn(lab), run_time=self.dur(0.5))
            self.play(LaggedStart(*[FadeIn(p, scale=0.3) for p in puntos], lag_ratio=0.02), run_time=self.dur(0.9))
            self.play(FadeIn(filo), run_time=0.3)

            # «el centro de masa»
            self.en("centro")
            self.play(FadeIn(centro, scale=0.3), Create(aro), run_time=self.dur(0.5))

            # «la media de equis en un eje»
            self.en("mx")
            self.play(Create(gx), FadeIn(mx), run_time=self.dur(0.6))

            # «la media de i griega en el otro»
            self.en("my")
            self.play(Create(gy), FadeIn(my), run_time=self.dur(0.6))

            # «lo más interesante»
            self.en("interesante")
            self.play(FadeOut(VGroup(centro, aro, gx, gy, mx, my, filo)), run_time=0.3)
            interr.permitir_encima = True
            self.pop(interr)

            # «cuando ya sabes cuánto vale»
            self.en("sabes")
            self.play(FadeOut(interr), run_time=0.2)
            self.play(Create(corte), FadeIn(banda), run_time=self.dur(0.7))
            val = MathTex(r"X=x", color=AMBAR).scale(1.0).move_to([float(ax.c2p(3.2, 0)[0]) + 0.1, 3.4, 0])
            self.pop(val)
