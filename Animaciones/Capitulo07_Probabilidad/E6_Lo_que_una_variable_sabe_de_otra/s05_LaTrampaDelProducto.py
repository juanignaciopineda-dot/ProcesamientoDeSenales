"""Escena 05 — La esperanza del producto no es el producto de las esperanzas."""
from comun.escena import *


class LaTrampaDelProducto(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    def bloque1(self):
        self.tri = aviso_triangulo(ROJO).scale(0.9).move_to([0, 3.5, 0])
        self.e1 = formula("E[SR]", escala=1.8, colores={0: AMBAR}).move_to([-3.6, 2.4, 0])
        self.ne = MathTex(r"\neq", color=ROJO).scale(2.0).move_to([0, 2.4, 0])
        self.e2 = formula("E[S]", r"\cdot", "E[R]", escala=1.8, colores={0: SENAL, 2: MEDIDA}).move_to([3.4, 2.4, 0])
        self.ms = formula("E[S]", "=", "0{,}3", escala=1.4, colores={0: SENAL}).move_to([1.4, 1.3, 0])
        self.mr = formula("E[R]", "=", "0{,}34", escala=1.4, colores={0: MEDIDA}).move_to([5.0, 1.3, 0])
        self.pm = formula("0{,}3", r"\cdot", "0{,}34", "=", "0{,}102", escala=1.4).move_to([3.4, -0.2, 0])
        self.c27 = formula("E[SR]", "=", "0{,}27", escala=1.4, colores={0: AMBAR, 2: AMBAR}).move_to([-3.6, 1.3, 0])
        with self.narrar("b1"):
            # «atención a una trampa»
            self.en("trampa")
            self.pop(self.tri, sonido="alarma")

            # «La esperanza del producto»
            self.en("e_prod")
            self.play(FadeIn(self.e1), run_time=self.dur(0.5))

            # «no es el producto de las esperanzas»
            self.en("prod_e")
            self.play(FadeIn(self.e2), FadeIn(self.ne), run_time=self.dur(0.6))

            # «de las esperanzas»
            self.en("esper")
            self.resaltar(self.e2, color=AMBAR, escala=1.1)

            # «La media de lo enviado»
            self.en("media_env")
            self.lab_s = Text("Lo enviado", color=SENAL).scale(0.55).next_to(self.ms, DOWN, buff=0.15)
            self.play(FadeIn(self.lab_s), run_time=self.dur(0.4))

            # «cero coma tres»
            self.en("m_s")
            self.play(FadeIn(self.ms), run_time=self.dur(0.5))

            # «la de lo recibido»
            self.en("media_rec")
            self.lab_r = Text("Lo recibido", color=MEDIDA).scale(0.55).next_to(self.mr, DOWN, buff=0.15)
            self.play(FadeIn(self.lab_r), run_time=self.dur(0.4))

            # «cero coma treinta y cuatro»
            self.en("m_r")
            self.play(FadeIn(self.mr), run_time=self.dur(0.5))

            # «cero coma uno cero dos»
            self.en("p_med")
            self.play(FadeIn(self.pm), run_time=self.dur(0.7))

            # «cero coma veintisiete»
            self.en("corr27")
            self.play(FadeIn(self.c27), run_time=self.dur(0.6))

            # «bastante más»
            self.en("mas")
            self.larga = Rectangle(width=5.4, height=0.6, color=AMBAR, fill_opacity=0.7, stroke_width=0)
            self.larga.move_to([-6.4 + 2.7, -1.0, 0])
            self.corta = Rectangle(width=2.04, height=0.6, color=INK, fill_opacity=0.7, stroke_width=0)
            self.corta.move_to([-6.4 + 1.02, -1.9, 0])
            self.t_larga = Text("0,27", color=AMBAR).scale(0.7).next_to(self.larga, RIGHT, buff=0.2)
            self.t_corta = Text("0,102", color=INK).scale(0.7).next_to(self.corta, RIGHT, buff=0.2)
            self.play(FadeOut(self.tri), GrowFromEdge(self.larga, LEFT), GrowFromEdge(self.corta, LEFT),
                      FadeIn(self.t_larga), FadeIn(self.t_corta), run_time=self.dur(0.9))

    def bloque2(self):
        x_c = self.corta.get_right()[0]
        x_l = self.larga.get_right()[0]
        llave = BraceBetweenPoints([x_c, -2.4, 0], [x_l, -2.4, 0], direction=DOWN, color=INK)
        et = Text("Información", color=AMBAR).scale(0.75).next_to(llave, DOWN, buff=0.12)
        ok = tilde(VERDE, 0.5).next_to(et, RIGHT, buff=0.3)
        with self.narrar("b2"):
            # «Esa diferencia»
            self.en("dif")
            self.play(GrowFromCenter(llave), run_time=self.dur(0.6))

            # «no es un error»
            self.en("no_error")
            self.play(Create(ok), run_time=self.dur(0.5))

            # «es la información que buscamos»
            self.en("info")
            self.play(llave.animate.set_color(AMBAR), FadeIn(et), run_time=self.dur(0.6))

            # «El producto de las medias»
            self.en("medias")
            self.resaltar(self.corta, color=TXT, escala=1.15)

            # «por libre»
            self.en("libre")
            arriba = VGroup(self.e1, self.ne, self.e2, self.ms, self.mr, self.pm, self.c27, self.lab_s, self.lab_r)
            rielS = Line([-3.0, 3.3, 0], [-3.0, 0.3, 0], color=INK, stroke_width=2)
            rielR = Line([2.4, 3.3, 0], [2.4, 0.3, 0], color=INK, stroke_width=2)
            dS = Dot([-3.0, 1.8, 0], radius=0.22, color=SENAL)
            dR = Dot([2.4, 1.8, 0], radius=0.22, color=MEDIDA)
            tS = Text("S", color=SENAL, weight=BOLD).scale(0.8).next_to(rielS, UP, buff=0.1)
            tR = Text("R", color=MEDIDA, weight=BOLD).scale(0.8).next_to(rielR, UP, buff=0.1)
            rieles = VGroup(rielS, rielR, dS, dR, tS, tR)
            self.play(FadeOut(arriba), run_time=0.3)
            self.play(FadeIn(rieles), run_time=0.3)
            self.play(dS.animate.move_to([-3.0, 3.0, 0]), dR.animate.move_to([2.4, 0.6, 0]),
                      run_time=self.dur(0.6))
            self.play(dS.animate.move_to([-3.0, 0.6, 0]), dR.animate.move_to([2.4, 2.7, 0]),
                      run_time=self.dur(0.6))

            # «Si la correlación es mayor»
            self.en("mayor")
            self.resaltar(self.larga, color=TXT, escala=1.1)

            # «cuando se envía un uno»
            self.en("envia1")
            T = TablaCanal(centro=(3.4, 1.5), lado=1.7, esc=0.7)
            self.play(FadeOut(rieles), run_time=0.25)
            self.play(FadeIn(T.armazon()), FadeIn(T.probs()), run_time=self.dur(0.5))
            self.play(T.enc_f[1].animate.set_color(AMBAR), run_time=self.dur(0.3))

            # «suele recibirse un uno»
            self.en("recibe1")
            m = T.marco(1, 1, AMBAR)
            self.play(Create(m), T.enc_c[1].animate.set_color(AMBAR), run_time=self.dur(0.6))

            # «más de lo que harían por casualidad»
            self.en("casualidad")
            self.resaltar(llave, color=TXT, escala=1.15)
