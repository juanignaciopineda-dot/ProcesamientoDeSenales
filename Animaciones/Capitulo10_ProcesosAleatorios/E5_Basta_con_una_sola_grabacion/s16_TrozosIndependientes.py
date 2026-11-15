"""Escena 16 — Una grabación larga son muchos trozos casi independientes."""
from comun.escena import *


class TrozosIndependientes(EscenaCurso):
    ESCENA = "16"

    def construct(self):
        L = Lienzo(ancho=11.0, alto=2.2, t_rango=(0, 1), v_max=3.0, centro=(0, 1.8))
        n = 300
        t = np.linspace(0, 1, n)
        s = 1.1 * serie(12, n, 0.6)
        colores = [AZUL, CIAN, VERDE, AMBAR, MAGENTA]
        cortes = np.linspace(0, n, 6).astype(int)
        trozos = VGroup(*[traza(L.x(t[a:b]), L.y(s[a:b]), colores[i], 4) for i, (a, b) in enumerate(zip(cortes[:-1], cortes[1:]))])
        entera = L.curva(t, s, SENAL, 3.5)
        doc = documento().scale(2.2).move_to([0, 0.5, 0])

        with self.narrar("b1"):
            # «La cuenta completa»
            self.en("cuenta")
            lim = MathTex(r"\lim_{N\to\infty}\mathrm{Var}=0", color=TXT).scale(0.9).move_to([0, 3.4, 0])
            self.play(FadeIn(doc, scale=0.7), FadeIn(lim), run_time=0.6)

            # «en el apunte en profundidad»
            self.en("apunte")
            ap = etiqueta("apunte en profundidad", INK, 0.7, BOLD).move_to([0, -1.4, 0])
            self.play(FadeIn(ap), run_time=0.4)

            # «la intuición es sencilla»
            self.en("intuicion")
            self.play(FadeOut(doc), FadeOut(lim), FadeOut(ap), run_time=0.3)
            self.play(Create(L.base()), Create(entera), run_time=self.dur(1.3))

            # «muy separadas»
            self.en("separadas")
            d1 = Dot(L.p(0.12, float(s[36])), radius=0.14, color=AMBAR)
            d2 = Dot(L.p(0.88, float(s[264])), radius=0.14, color=AMBAR)
            c0 = MathTex(r"C\approx0", color=AMBAR).scale(0.9).move_to([0, 0.2, 0])
            self.play(FadeIn(d1, scale=0.5), FadeIn(d2, scale=0.5), FadeIn(c0), run_time=0.5)

            # «se olvidan unas de otras»
            self.en("olvidan")
            hilo = DashedLine(d1.get_center(), d2.get_center(), color=INK, stroke_width=3)
            self.play(Create(hilo), run_time=0.5)
            tach = cruz(ROJO, 0.4).move_to(hilo.get_center())
            self.play(FadeIn(tach, scale=0.5), run_time=0.3)

            # «trozos»
            self.en("trozos")
            self.play(FadeOut(hilo), FadeOut(tach), FadeOut(c0), FadeOut(d1), FadeOut(d2),
                      FadeOut(entera), FadeIn(trozos), run_time=0.6)

            # «casi como realizaciones independientes»
            self.en("indep")
            anims = []
            for i, tr in enumerate(trozos):
                x0 = float(L.x(t[cortes[i]]))
                anims.append(tr.animate.shift(LEFT * (x0 - (-5.5)) + DOWN * (0.9 * i + 0.3)))
            self.play(*anims, run_time=self.dur(1.6))

            # «Promediar en el tiempo»
            self.en("promediar")
            fl = Arrow([-5.6, -3.6, 0], [0.4, -3.6, 0], color=AMBAR, buff=0, stroke_width=5)
            self.play(Create(fl), run_time=self.dur(0.8))

            # «en el fondo»
            self.en("fondo")
            self.play(*[tr.animate.set_stroke(width=6) for tr in trozos], run_time=0.5)

            # «muchas realizaciones disfrazadas de una sola»
            self.en("disfraz")
            back = []
            for i, tr in enumerate(trozos):
                x0 = float(L.x(t[cortes[i]]))
                back.append(tr.animate.shift(RIGHT * (x0 - (-5.5)) + UP * (0.9 * i + 0.3)))
            self.play(FadeOut(fl), *back, run_time=self.dur(1.6))
        self.wait(1.0)
        self.limpiar()
