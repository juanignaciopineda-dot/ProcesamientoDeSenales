"""Escena 14 — La raíz del coseno alzado: el reparto entre transmisor y receptor, y las dos exigencias a la vez."""
from comun.escena import *

T = np.linspace(-3, 3, 300)


class RaizDeCosenoAlzado(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        self.reparto()
        self.wait(0.5)
        self.exigencias()
        self.wait(1.0)
        self.limpiar()

    def reparto(self):
        p2 = MathTex("|P|^2", color=SENAL).scale(1.5).move_to([-5.4, 3.2, 0])
        L = Lienzo(ancho=5.2, alto=2.2, t_rango=(-3, 3), v_max=1.3, centro=(-3.6, 0.9))
        base = L.base()
        curva = L.curva(T, np.sinc(T), VERDE, 4)
        ceros = VGroup(*[Dot(L.p(t, 0.0), radius=0.08, color=VERDE) for t in (-2, -1, 1, 2)])
        t_co = etiqueta("coseno alzado", AMBAR, 0.6, BOLD).move_to([-3.6, 2.45, 0])
        tx = caja("transmisor", SENAL, ancho=2.5, alto=0.8, scale=0.5).move_to([1.6, 1.4, 0])
        rx = caja("receptor", AMBAR, ancho=2.5, alto=0.8, scale=0.5).move_to([5.3, 1.4, 0])
        ar = Arrow([2.9, 1.4, 0], [4.0, 1.4, 0], buff=0.05, color=INK, stroke_width=3)
        medios = VGroup(MathTex(r"\tfrac{1}{2}", color=AMBAR).scale(1.0).move_to([1.6, 2.4, 0]),
                        MathTex(r"\tfrac{1}{2}", color=AMBAR).scale(1.0).move_to([5.3, 2.4, 0]))
        raices = VGroup(MathTex(r"\sqrt{\text{pulso}}", color=AMBAR).scale(0.9).move_to([1.6, 0.4, 0]),
                        MathTex(r"\sqrt{\text{pulso}}", color=AMBAR).scale(0.9).move_to([5.3, 0.4, 0]))
        rcos = Text("raíz de coseno alzado", color=AMBAR, weight=BOLD).scale(0.8).move_to([3.5, -0.7, 0])
        mods = VGroup(modem7(INK).scale(0.7), modem7(INK).scale(0.7), modem7(INK).scale(0.7))
        mods.arrange(RIGHT, buff=0.6).move_to([-4.6, -2.7, 0])
        suma = MathTex(r"\tfrac{1}{2}+\tfrac{1}{2}=1", color=AMBAR).scale(1.2).move_to([3.5, -2.2, 0])
        with self.narrar("b1"):
            # «Una consecuencia práctica»
            self.paso("practica", p2, t=0.6)
            # «el pulso deseado, el que cumple Nyquist»
            self.en("deseado")
            self.play(FadeIn(base), Create(curva), FadeIn(ceros), run_time=self.dur(1.0))
            # «es un coseno alzado»
            self.paso("coseno", t_co, t=0.5)
            # «el transmisor y el receptor»
            self.en("reparten")
            self.play(FadeIn(tx), FadeIn(rx), GrowArrow(ar), run_time=self.dur(0.7))
            # «se reparten el trabajo»
            self.paso("trabajo", medios, t=0.6)
            # «cada uno aplica la raíz de ese pulso»
            self.paso("raiz", raices, t=0.8)
            # «Es el filtro»
            self.en("filtro")
            self.resaltar(raices[0], raices[1], run_time=0.5)
            # «raíz de coseno alzado»
            self.en("rcos")
            self.pop(rcos)
            # «casi todos los módems»
            self.paso("todos", mods, t=0.7)
            # «La mitad del conformado»
            self.paso("mitad", suma, t=0.6)
            # «en el transmisor»
            self.en("tx")
            self.resaltar(tx, run_time=0.5)
            # «la otra mitad, en el receptor»
            self.en("rx")
            self.resaltar(rx, run_time=0.5)
        self.corte()

    def exigencias(self):
        unico = caja("un solo reparto", AMBAR, ancho=4.4, alto=0.9, scale=0.6).move_to([0, 3.0, 0])
        c1 = RoundedRectangle(corner_radius=0.15, width=5.4, height=1.2, color=INK, stroke_width=2).move_to([-3.4, 1.2, 0])
        c2 = RoundedRectangle(corner_radius=0.15, width=5.4, height=1.2, color=INK, stroke_width=2).move_to([3.4, 1.2, 0])
        t1 = etiqueta("máxima SNR", MEDIDA, 0.7, BOLD).move_to([-3.7, 1.2, 0])
        t2 = etiqueta("cero interferencia", SENAL, 0.7, BOLD).move_to([3.6, 1.2, 0])
        v1 = tilde(VERDE, 0.7).move_to([-5.6, 1.2, 0])
        v2 = tilde(VERDE, 0.7).move_to([1.2, 1.2, 0])
        pa = caja("filtro adaptado", AMBAR, ancho=3.4, alto=0.9, scale=0.5).move_to([-4.2, -1.4, 0])
        pm = caja("muestrear en el pico", AMBAR, ancho=3.8, alto=0.9, scale=0.5).move_to([0.2, -1.4, 0])
        pu = caja("umbral", AMBAR, ancho=2.2, alto=0.9, scale=0.5).move_to([4.2, -1.4, 0])
        f1 = Arrow([-2.5, -1.4, 0], [-1.7, -1.4, 0], buff=0.05, color=INK, stroke_width=3)
        f2 = Arrow([2.2, -1.4, 0], [3.0, -1.4, 0], buff=0.05, color=INK, stroke_width=3)
        det = etiqueta("el detector", AMBAR, 0.6, BOLD).move_to([0, 0.05, 0])
        marco = RoundedRectangle(corner_radius=0.2, width=12.6, height=1.9, color=AMBAR, stroke_width=3,
                                 stroke_opacity=0.6).move_to([0, -1.4, 0])
        marco.permitir_encima = True
        with self.narrar("b2"):
            # «con un solo reparto»
            self.paso("reparto", unico, t=0.6)
            # «dos exigencias a la vez»
            self.paso("dos", c1, c2, t=0.6)
            # «la máxima relación señal-ruido»
            self.paso("snr", t1, v1, t=0.7)
            # «ninguna interferencia entre símbolos»
            self.paso("noisi", t2, v2, t=0.7)
            # «No hay que elegir»
            self.en("noelegir")
            self.resaltar(c1, c2, color=VERDE, run_time=0.7)
            # «todas las piezas del detector»
            self.en("piezas")
            self.play(FadeIn(pa), FadeIn(pm), FadeIn(pu), GrowArrow(f1), GrowArrow(f2), run_time=self.dur(0.9))
            # «mirar el conjunto»
            self.en("conjunto")
            self.play(Create(marco), FadeIn(det), run_time=self.dur(0.7))
