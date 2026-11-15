"""Escena 13 — La voz y el murmullo otra vez: la coherencia decide qué deja pasar el colador."""
from comun.escena import *


class ElColadorDeVuelta(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        t = np.linspace(0, 4, 200)
        L1 = Lienzo(ancho=4.6, alto=1.2, t_rango=(0, 4), v_max=1.0, centro=(-3.2, 2.7))
        L2 = Lienzo(ancho=4.6, alto=1.0, t_rango=(0, 4), v_max=1.0, centro=(-3.2, 1.2))
        voz = L1.curva(t, 0.8 * voz_valores(200), SENAL, 2.6)
        mur = ruido_t(L2, semilla=4, amp=0.22, color=RUIDO)
        pers = persona(AZUL).scale(1.0).move_to([-6.4, 2.7, 0])
        # coherencia a lo largo de ω
        Lc = Lienzo(ancho=6.2, alto=2.2, t_rango=(0, 1), v_max=1.0, centro=(3.7, 1.0))
        f = lambda u: 0.12 + 0.8 * np.exp(-((u - 0.28) / 0.12) ** 2) + 0.12 * np.exp(-((u - 0.75) / 0.2) ** 2)
        cur = curva_f(Lc, f, 0.0, 1.0, AMBAR, 4.0)
        eje = Lc.base(INK, 2.5)
        l_w = MathTex(r"\omega", color=INK).scale(0.6).move_to([6.95, 0.75, 0])
        alta = area_f(Lc, f, 0.12, 0.45, VERDE, 0.5)
        baja = area_f(Lc, f, 0.55, 0.95, ROJO, 0.5)
        l_alta = etiqueta("alta", VERDE, 0.55).move_to(Lc.p(0.28, 1.15))
        l_baja = etiqueta("baja", ROJO, 0.55).move_to(Lc.p(0.75, 0.5))
        col = colador(CIAN, 1.3, 1.0).move_to([-3.0, -1.6, 0])
        paso = Dot([-6.0, -1.6, 0], radius=0.12, color=AZUL)
        gan = Lienzo(ancho=6.2, alto=1.4, t_rango=(0, 1), v_max=1.0, centro=(3.7, -2.0))
        cop = curva_f(gan, f, 0.0, 1.0, CIAN, 4.0)
        l_gan = etiqueta("ganancia del colador", CIAN, 0.5).move_to([3.7, -3.4, 0])
        antes = etiqueta("¿y si la coherencia miente?", ROJO, 0.55).move_to([-3.0, -3.3, 0])
        lp = lupa(TXT).scale(1.6).move_to([5.3, 1.1, 0])
        with self.narrar("b1"):
            # «la voz y el murmullo»
            self.en("vozmurmullo")
            self.corte()
            self.play(FadeIn(pers), Create(L1.base()), Create(voz), Create(L2.base()), Create(mur),
                      run_time=self.dur(1.5), rate_func=linear)

            # «Donde la coherencia es alta»
            self.en("alta")
            self.play(Create(eje), FadeIn(l_w), Create(cur), run_time=self.dur(1.0))
            self.play(FadeIn(alta), FadeIn(l_alta), run_time=self.dur(0.6))

            # «déjalo pasar»
            self.en("pasa")
            self.play(FadeIn(col, scale=0.7), FadeIn(paso), run_time=self.dur(0.5))
            self.play(paso.animate.move_to([-0.2, -1.6, 0]), run_time=self.dur(1.2))

            # «Donde es baja»
            self.en("baja")
            self.play(FadeIn(baja), FadeIn(l_baja), run_time=self.dur(0.6))
            paso.move_to([-6.0, -1.6, 0]).set_color(MAGENTA)

            # «atenúalo»
            self.en("atenua")
            self.play(paso.animate.move_to([-3.6, -1.6, 0]).scale(0.4), run_time=self.dur(0.8))

            # «el colador que buscábamos»
            self.en("colador")
            self.play(FadeOut(paso), Create(gan.base()), Create(cop), FadeIn(l_gan), run_time=self.dur(1.2))

            # «Pero antes de usar la coherencia»
            self.en("antes")
            self.play(FadeIn(antes), run_time=self.dur(0.6))

            # «estimarla sin engañarse»
            self.en("estimar")
            self.play(FadeIn(lp, scale=0.6), run_time=self.dur(0.5))
            self.play(lp.animate.shift(LEFT * 1.5 + UP * 0.2), run_time=self.dur(1.0))

        self.wait(1.0)
        self.limpiar()
