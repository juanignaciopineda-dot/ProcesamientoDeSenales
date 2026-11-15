"""Escena 12 — Cierre: repaso del sensor de punta a punta y anuncio del episodio 6."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        # el tren de piezas del episodio
        piezas = VGroup(caja("densidad", MEDIDA, ancho=2.0, alto=0.8, scale=0.45),
                        caja("F(z)", AMBAR, ancho=1.6, alto=0.8, scale=0.5),
                        caja("cola cortada", ERROR, ancho=2.4, alto=0.8, scale=0.45),
                        caja("filtro", VERDE, ancho=1.7, alto=0.8, scale=0.5)).arrange(RIGHT, buff=0.45)
        piezas.move_to([0, 2.9, 0])
        # tres iconos: ecuación, tijera, división
        ic_ec = formula(r"\rho^2-6{,}53\rho+1", escala=0.85, colores={0: AMBAR}).move_to([-4.2, 0.9, 0])
        ic_ec.set_color(AMBAR)
        ic_tj = tijeras().scale(0.7).move_to([-1.0, 0.9, 0])
        ic_div = formula(r"\times\ 1/F", escala=1.1, colores={0: VERDE}).move_to([1.9, 0.9, 0])
        ic_div.set_color(VERDE)
        # un solo polo
        pz = PlanoZ(centro=(5.3, 1.0), radio=1.0)
        polo = marca_x(pz.p(0.157), AMBAR)
        # dos multiplicaciones
        c1 = caja("× 0,157", ESTIMACION, ancho=1.9, alto=0.8, scale=0.5).move_to([-4.6, -1.0, 0])
        c2 = caja("× 0,7386", ESTIMACION, ancho=2.1, alto=0.8, scale=0.5).move_to([-2.3, -1.0, 0])
        # el límite de los filtros finitos
        be = barras_error([4, 0.8, 0.7401, 0.7387, 0.7386], ["0", "1", "2", "3", "∞"], centro=(2.0, -1.8), ancho=3.6,
                          alto=1.8, v_max=4.0)
        # siete por ciento
        total = Rectangle(width=3.2, height=0.45, color=ESTIMACION, stroke_width=0).set_fill(ESTIMACION, 0.8).move_to([5.0, -1.4, 0])
        gana = Rectangle(width=3.2 * 0.0712, height=0.45, color=VERDE, stroke_width=0).set_fill(VERDE, 0.95)
        gana.align_to(total, RIGHT).align_to(total, DOWN)
        l_7 = formula(r"7\,\%", escala=1.0, colores={0: VERDE}).next_to(total, UP, buff=0.15).align_to(total, RIGHT)
        l_7.set_color(VERDE)
        # la muestra de ahora frente al futuro
        L = Lienzo(ancho=8.0, alto=0.2, t_rango=(0, 8), v_max=1.0, centro=(-1.2, -3.3))
        linea = L.base(INK, 2.5)
        muestras = VGroup(*[Dot(L.p(t, 0), radius=0.1, color=MEDIDA) for t in (0.8, 1.9, 3.0, 4.1)])
        ahora = Dot(L.p(4.6, 0), radius=0.2, color=MEDIDA)
        futuro = VGroup(*[Dot(L.p(t, 0), radius=0.1, color=INK) for t in (5.7, 6.7, 7.7)]).set_opacity(0.3)
        nueva = MathTex("?", color=AMBAR).scale(1.6).move_to(L.p(4.6, 0) + UP * 0.9)
        puerta = VGroup(Rectangle(width=1.3, height=2.3, color=AMBAR, stroke_width=4).set_fill(AMBAR, 0.15),
                        Circle(radius=0.07, color=AMBAR).set_fill(AMBAR, 1)).move_to([6.2, -3.1, 0])
        puerta[1].move_to(puerta[0].get_center() + RIGHT * 0.4)
        titulo_e6 = self.palabra("Lo nuevo y lo que ya sabías", AMBAR, 0.95).move_to([0, 0.0, 0])
        with self.narrar("b1"):
            # «Hoy hemos recorrido el sensor de punta a punta»
            self.en("recorrido")
            self.play(LaggedStart(*[FadeIn(p, shift=RIGHT * 0.4) for p in piezas], lag_ratio=0.25), run_time=self.dur(1.6))

            # «Factorizamos, cortamos y deshicimos»
            self.en("tres")
            self.play(FadeIn(ic_ec, scale=0.6), run_time=0.4)
            self.play(FadeIn(ic_tj, scale=0.6), run_time=0.4)
            self.play(FadeIn(ic_div, scale=0.6), run_time=0.4)

            # «un solo polo»
            self.en("unpolo")
            self.play(Create(pz), run_time=0.4)
            self.play(Create(polo), run_time=0.4)

            # «dos multiplicaciones»
            self.en("dos")
            self.play(FadeIn(c1, shift=UP * 0.2), FadeIn(c2, shift=UP * 0.2), run_time=self.dur(0.6))

            # «el límite de todos los filtros finitos»
            self.en("limite")
            self.play(Create(be.base), *[FadeIn(e) for e in be.etiquetas],
                      LaggedStart(*[GrowFromEdge(b, DOWN) for b in be.barras], lag_ratio=0.2), run_time=self.dur(1.5))

            # «cuesta un siete por ciento»
            self.en("siete")
            self.play(FadeIn(total), run_time=0.3)
            self.play(FadeIn(gana), FadeIn(l_7), run_time=self.dur(0.6))

            # «la muestra de ahora parece valer mucho más»
            self.en("ahora")
            self.play(self.camera.frame.animate.set_width(config.frame_width), run_time=0.01)
            self.play(*[FadeOut(m) for m in (c1, c2, ic_ec, ic_tj, ic_div, pz, polo, piezas)], run_time=0.3)
            self.play(Create(linea), FadeIn(muestras), FadeIn(futuro), run_time=0.5)
            self.play(FadeIn(ahora, scale=0.3), run_time=0.3)
            self.play(Flash(ahora, color=MEDIDA, flash_radius=0.6), run_time=0.5)

            # «¿Cuánta información nueva trae cada muestra?»
            self.en("nueva")
            self.pop(nueva)

            # «Lo vemos en el próximo episodio»
            self.en("proximo")
            self.play(FadeIn(puerta, shift=LEFT * 0.3), run_time=self.dur(0.7))

            # «Lo nuevo y lo que ya sabías»
            self.en("titulo")
            self.play(*[FadeOut(m) for m in (be, total, gana, l_7, linea, muestras, futuro, ahora, nueva, puerta)],
                      run_time=0.3)
            self.pop(titulo_e6)

        self.wait(1.0)
        self.limpiar()
