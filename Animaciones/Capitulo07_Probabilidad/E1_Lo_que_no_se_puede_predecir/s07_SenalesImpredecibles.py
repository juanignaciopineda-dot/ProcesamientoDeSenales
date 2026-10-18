"""Escena 07 — Las señales que importan no se conocen de antemano: señal más ruido."""
from comun.escena import *


class SenalesImpredecibles(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.bloque_no_se_conocen()
        self.bloque_mensaje()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def bloque_no_se_conocen(self):
        L = Lienzo(ancho=10.5, alto=2.4, t_rango=(0, 6), v_max=1.2, centro=(0.0, 1.8))

        with self.narrar("b1"):
            # «se conocían de antemano»
            self.en("conocidas")
            base = L.base()
            seno = seno_t(L, 1.0, 1.0, SENAL, 4.0)
            eje = eje_v7(L, -1.2, 1.2)
            self.play(Create(base), Create(eje), run_time=0.3)
            self.play(Create(seno), run_time=self.dur(1.2), rate_func=linear)

            # «lo mismo hoy que mañana»
            self.en("hoy_manana")
            d1 = Dot(L.p(0.25, 1), radius=0.1, color=AMBAR)
            d2 = Dot(L.p(3.25, 1), radius=0.1, color=AMBAR)
            igual = DashedLine(L.p(0.25, 1), L.p(3.25, 1), color=AMBAR, stroke_width=3)
            hoy = Text("Hoy", color=AMBAR).scale(0.5).move_to(L.p(0.25, 1.45))
            man = Text("Mañana", color=AMBAR).scale(0.5).move_to(L.p(3.25, 1.45))
            self.play(FadeIn(d1), FadeIn(hoy), run_time=0.25)
            self.play(Create(igual), FadeIn(d2), FadeIn(man), run_time=self.dur(0.6))

            # «dentro de un año»
            self.en("anio")
            m = L.vertical(6, VERDE, 2.5)
            fin = Dot(L.p(6, 0), radius=0.1, color=VERDE)
            et = Text("+1 año", color=VERDE, weight=BOLD).scale(0.55).move_to([5.6, 0.35, 0])
            self.play(Create(m), FadeIn(fin), FadeIn(et), run_time=self.dur(0.5))

            # «de verdad importan»
            self.en("importan")
            imp = Text("Las que importan", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, -0.3, 0])
            self.pop(imp)

            # «no son así»
            self.en("no_asi")
            cr = cruz(ROJO, 1.6).move_to([0, 1.8, 0])
            self.pop(cr)

            # «qué palabras dirás»
            self.en("palabras")
            self.play(*[FadeOut(x) for x in (base, seno, d1, d2, igual, hoy, man, m, fin, et, cr, imp)], run_time=0.3)
            tv = np.linspace(0, 6, 260)
            base2 = L.base()
            voz = L.curva(tv[:130], 1.1 * voz_valores(260)[:130], SENAL, 4.0)
            incog = VGroup(*[Text("?", color=ROJO, weight=BOLD).scale(0.9).move_to(L.p(3.6 + 0.9 * k, 0.3 * (-1) ** k))
                             for k in range(3)])
            self.play(Create(base2), run_time=0.2)
            self.play(Create(voz), run_time=self.dur(0.8), rate_func=linear)
            self.play(LaggedStart(*[FadeIn(q) for q in incog], lag_ratio=0.2), run_time=self.dur(0.5))

            # «tu próxima llamada»
            self.en("llamada")
            mov = movil7().scale(1.2).move_to([-4.4, -1.8, 0])
            ondas = VGroup(*[Arc(radius=0.4 + 0.25 * i, start_angle=-PI / 4, angle=PI / 2, color=SENAL, stroke_width=4)
                             .shift(mov.get_center() + RIGHT * 0.55) for i in range(1, 4)])
            self.pop(mov)
            self.play(LaggedStart(*[Create(o) for o in ondas], lag_ratio=0.2), run_time=self.dur(0.5))

            # «el ruido que se cuele»
            self.en("ruido")
            Lr = Lienzo(ancho=5.0, alto=1.6, t_rango=(0, 1), v_max=1.5, centro=(2.8, -2.0))
            cr_ = Lr.curva(np.linspace(0, 1, 160), serie(9, 160, 0.5), RUIDO, 3.5)
            lr = Text("Ruido", color=RUIDO, weight=BOLD).scale(0.55).move_to([2.8, -3.35, 0])
            self.play(Create(cr_), FadeIn(lr), run_time=self.dur(0.8))

            # «no haría falta enviar nada»
            self.en("nada")
            sob = sobre().scale(1.1).move_to([-1.3, -1.9, 0])
            self.pop(sob)
            self.play(FadeIn(tachar(sob)), run_time=self.dur(0.3))

    # ------------------------------------------------------------ b2
    def bloque_mensaje(self):
        t = np.linspace(0, 1, 220)
        s = np.sin(2 * np.pi * 4 * t)
        w = 0.55 * serie(12, 220, 0.4)
        y = s + w
        filas = [2.5, 0.9, -0.8]
        Ls = [Lienzo(ancho=7.0, alto=1.3, t_rango=(0, 1), v_max=1.7, centro=(-0.6, yy)) for yy in filas]

        with self.narrar("b2"):
            # «un mensaje que viaja por el aire»
            self.en("mensaje")
            self.corte()
            emi = antena().scale(1.2).move_to([-5.8, 2.5, 0])
            self.pop(emi)

            # «sale de la antena es limpio»
            self.en("limpia")
            cs = Ls[0].curva(t, s, SENAL, 4.0)
            ls = Text("Señal", color=SENAL, weight=BOLD).scale(0.5).move_to([4.2, 2.5, 0])
            self.play(Create(cs), FadeIn(ls), run_time=self.dur(0.9), rate_func=linear)

            # «se le suma ruido»
            self.en("suma")
            mas = Text("+", color=TXT, weight=BOLD).scale(0.9).move_to([-4.7, 1.7, 0])
            cw = Ls[1].curva(t, w, RUIDO, 3.5)
            self.pop(mas)
            self.play(Create(cw), run_time=self.dur(0.7), rate_func=linear)

            # «interferencias», «calor en los circuitos», «otras señales»
            self.en("interf")
            l1 = Text("Interferencias", color=RUIDO).scale(0.5).move_to([5.3, 2.0, 0])
            self.play(FadeIn(l1, shift=LEFT * 0.2), run_time=self.dur(0.3))
            self.en("calor")
            l2 = Text("Calor", color=RUIDO).scale(0.5).move_to([5.3, 1.4, 0])
            self.play(FadeIn(l2, shift=LEFT * 0.2), run_time=self.dur(0.3))
            self.en("otras")
            l3 = Text("Otras señales", color=RUIDO).scale(0.5).move_to([5.3, 0.8, 0])
            self.play(FadeIn(l3, shift=LEFT * 0.2), run_time=self.dur(0.3))

            # «lo que llega al otro lado»
            self.en("llega")
            rec = antena().scale(1.2).move_to([5.5, -1.6, 0])
            self.pop(rec)

            # «la suma de las dos cosas»
            self.en("recibida")
            ig = Text("=", color=TXT, weight=BOLD).scale(0.9).move_to([-4.7, 0.0, 0])
            cy = Ls[2].curva(t, y, MEDIDA, 4.0)
            lm = Text("Recibida", color=MEDIDA, weight=BOLD).scale(0.5).move_to([3.8, -0.8, 0])
            self.pop(ig)
            self.play(Create(cy), FadeIn(lm), run_time=self.dur(0.9), rate_func=linear)

            # «distinto cada vez»
            self.en("distinto")
            w2 = Ls[1].curva(t, 0.55 * serie(33, 220, 0.4), RUIDO, 3.5)
            w3 = Ls[1].curva(t, 0.55 * serie(47, 220, 0.4), RUIDO, 3.5)
            self.play(Transform(cw, w2), run_time=self.dur(0.5))
            self.play(Transform(cw, w3), run_time=self.dur(0.5))

            # «no se puede restar sin más»
            self.en("restar")
            rs = Text("Recibida − ruido", color=TXT, weight=BOLD).scale(0.7).move_to([0, -2.8, 0])
            self.pop(rs)
            self.play(FadeIn(tachar(rs)), run_time=self.dur(0.3))

            # «un número conocido»
            self.en("conocido")
            rc = caja("Ruido = ?", RUIDO, ancho=2.6, alto=0.8, scale=0.6).move_to([3.6, -3.35, 0])
            self.pop(rc)
