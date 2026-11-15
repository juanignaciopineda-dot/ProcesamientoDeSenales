"""Escena 06 — Con ruido el máximo puede caer en un vecino; y la amplitud es desconocida."""
from comun.escena import *

RUIDOSA = [1.1, -0.8, 1.6, 3.5, 7.8, 8.6, 9.6, 3.1, 1.4, -1.0]


class ConRuidoSeComplica(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        with self.narrar("b1"):
            self.parte_a()
            self.parte_b()
        self.wait(1.0)
        self.limpiar()

    def parte_a(self):
        sal = Tallos([0, 0, 0, 2, 6, 9, 6, 2, 0, 0], centro=(0.0, -0.4), paso=0.8, unidad=0.27, color=ESTIMACION,
                     indices=True)
        L = Lienzo(ancho=4.0, alto=1.2, t_rango=(0, 1), v_max=1.0, centro=(-4.3, 2.4))
        onda = ruido_t(L, semilla=7, amp=0.4, color=RUIDO)
        mas = Text("+ ruido", color=RUIDO, weight=BOLD).scale(0.6).move_to([-4.3, 3.5, 0])
        nueva = Tallos(RUIDOSA, centro=(0.0, -0.4), paso=0.8, unidad=0.27, color=MEDIDA, indices=True)
        for t_ in (sal, nueva):
            t_.ks.shift(DOWN * 0.35)
        vec = Circle(radius=0.22, color=ROJO, stroke_width=4).move_to(nueva.pos(6))
        ver = Circle(radius=0.22, color=VERDE, stroke_width=4).move_to(nueva.pos(5))
        mal = formula("D", "=", "4", escala=1.1, colores={0: ROJO, 2: ROJO}).move_to([3.6, 2.4, 0])
        cr = cruz(ROJO, 0.5).next_to(mal, RIGHT, buff=0.2)
        # «Con ruido»
        self.en("ruido")
        self.play(FadeIn(sal), run_time=self.dur(0.6))
        self.play(FadeIn(mas), run_time=0.3)
        # «la historia se complica»
        self.en("complica")
        self.play(Create(onda), run_time=self.dur(0.9))
        # «A la salida se le suma ruido»
        self.en("suma")
        self.play(Transform(sal, nueva), run_time=self.dur(1.0))
        # «el máximo puede caer»
        self.en("cae")
        self.play(Create(vec), run_time=self.dur(0.5))
        # «en una posición vecina»
        self.en("vecina")
        self.play(Create(ver), run_time=0.4)
        # «medimos mal el retardo»
        self.en("mal")
        self.play(FadeIn(mal), FadeIn(cr), run_time=self.dur(0.6))
        self.pausa = (sal, onda, mas, vec, ver, mal, cr)

    def parte_b(self):
        Z = (-1.5, -0.2)
        eco = Tallos([2, 2, 1], centro=Z, paso=0.9, unidad=0.7, color=SENAL)
        dos = Text("2", color=AMBAR, weight=BOLD).scale(1.6).move_to([-5.5, 2.4, 0])
        A = MathTex("A", color=AMBAR).scale(0.9).move_to([-3.6, 0.6, 0])
        fa = DoubleArrow([-3.2, -0.2, 0], [-3.2, 1.2, 0], color=AMBAR, buff=0, stroke_width=4)
        desc = formula("A", "=", "?", escala=1.3, colores={0: AMBAR, 2: AMBAR}).move_to([3.7, 2.0, 0])
        av = avion(AZUL).scale(0.8).move_to([4.6, -1.2, 0])
        umb = DashedLine([-3.6, 1.6, 0], [1.2, 1.6, 0], color=ERROR, stroke_width=4)
        q = Text("?", color=ERROR, weight=BOLD).scale(0.9).move_to([1.9, 1.6, 0])
        # «un segundo problema»
        self.en("segundo")
        self.play(*[FadeOut(m) for m in self.pausa], run_time=0.3)
        self.pop(dos)
        # «la amplitud del eco»
        self.en("amplitud")
        self.play(FadeIn(eco), run_time=self.dur(0.5))
        self.play(GrowArrow(fa), FadeIn(A), run_time=0.4)
        # «también es desconocida»
        self.en("desconocida")
        self.play(FadeIn(desc), run_time=self.dur(0.6))
        # «un avión lejano»
        self.en("lejano")
        self.play(FadeIn(av), run_time=self.dur(0.5))
        # «un eco más débil»
        self.en("debil")
        self.play(eco.animate.stretch(0.5, 1, about_point=eco.base.get_center()),
                  fa.animate.scale(0.5, about_point=fa.get_start()), run_time=self.dur(0.8))
        # «el umbral no se puede fijar a ojo»
        self.en("umbral")
        self.play(FadeIn(umb), FadeIn(q), run_time=0.4)
        self.play(umb.animate.shift(UP * 0.8), q.animate.shift(UP * 0.8), run_time=self.dur(0.6))
        self.play(umb.animate.shift(DOWN * 1.2), q.animate.shift(DOWN * 1.2), run_time=self.dur(0.6))
