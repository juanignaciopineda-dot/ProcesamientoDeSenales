"""Escena 01 — Gancho: los ruidos tienen color y el color depende de cuánto recuerdan."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        with self.narrar("b1"):
            # «Hay ruidos con color»
            self.en("color")
            L = Lienzo(ancho=5.0, alto=2.2, t_rango=(0, 2), v_max=2.4, centro=(-4.0, 0.9))
            t = np.linspace(0, 2, 150)
            ruido = L.curva(t, 0.9 * serie(5, 150, 0.0), RUIDO, 3)
            esp = Espectro(w_max=6, y_max=1.2, ancho=5.2, alto=2.6, centro=(3.5, -0.4))
            graf = esp.curva(tele_S)
            arco = esp.arcoiris(graf)
            self.play(Create(L.base()), Create(ruido), run_time=self.dur(0.8))
            self.play(Create(esp.ejes), FadeIn(arco), Create(graf), run_time=self.dur(0.8))

            # «igual que la luz»
            self.en("luz")
            pri = prisma().scale(0.85).move_to([-3.0, -2.6, 0])
            self.pop(pri)

            # «el color de un ruido»
            self.en("forma")
            self.corte()
            xs = (-4.6, 0.0, 4.6)
            Lm = [Lienzo(ancho=3.2, alto=1.6, t_rango=(-3, 3), v_max=1.2, centro=(x, 1.6)) for x in xs]
            w = np.linspace(-3, 3, 100)
            vals = (np.full(100, 0.8), tele_S(w * 2.0) * 0.9, np.exp(-(w * 2.2) ** 2 / 2) * 1.0)
            curvas = VGroup(*[Lm[i].curva(w, vals[i], AMBAR, 4) for i in range(3)])
            bases = VGroup(*[Lm[i].base() for i in range(3)])
            self.play(FadeIn(bases), Create(curvas), run_time=self.dur(0.8))

            # «cuánto recuerda»
            self.en("recuerda")
            La = [Lienzo(ancho=3.2, alto=1.6, t_rango=(-3, 3), v_max=1.2, centro=(x, -1.7)) for x in xs]
            tt = np.linspace(-3, 3, 150)
            autos = (np.where(np.abs(tt) < 0.05, 1.0, 0.0), np.exp(-2 * np.abs(tt)),
                     np.cos(2 * tt) * np.exp(-0.15 * np.abs(tt)))
            cur_a = VGroup(*[La[i].curva(tt, autos[i], SENAL, 4) for i in range(3)])
            bas_a = VGroup(*[La[i].base() for i in range(3)])
            self.play(FadeIn(bas_a), Create(cur_a), run_time=self.dur(0.9))

            # «Hoy vemos por qué»
            self.en("porque")
            q = Text("¿por qué?", color=AMBAR, weight=BOLD).scale(0.9).move_to([0, 3.5, 0])
            self.pop(q)
        self.wait(0.6)
        self.limpiar()
