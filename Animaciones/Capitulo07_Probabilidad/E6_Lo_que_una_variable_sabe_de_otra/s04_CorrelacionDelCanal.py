"""Escena 04 — La correlación del canal: solo cuenta la casilla del uno y uno."""
from comun.escena import *


class CorrelacionDelCanal(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        T = TablaCanal(centro=(-2.9, -0.7), lado=2.5, esc=0.9)
        prods = {(i, j): T.texto(i, j, f"{i} · {j} = {i * j}", TXT, 0.7) for i in range(2) for j in range(2)}
        pes = {(i, j): T.texto(i, j, f"{i * j} · {num(CANAL6[i][j])}", TXT, 0.7) for i in range(2) for j in range(2)}
        with self.narrar("b1"):
            # «Calculémosla con el canal»
            self.en("tabla")
            self.play(FadeIn(T.armazon()), run_time=self.dur(0.6))
            self.play(FadeIn(T.probs()), run_time=self.dur(0.5))

            # «multiplicar lo enviado por lo recibido»
            self.en("mult")
            self.play(LaggedStart(*[FadeIn(p, shift=DOWN * 0.1) for p in prods.values()], lag_ratio=0.2),
                      run_time=self.dur(1.0))

            # «en cada casilla»
            self.en("casillas")
            self.play(LaggedStart(*[c.animate(rate_func=there_and_back).set_stroke(AMBAR, 6)
                                    for fila in T.cel for c in fila], lag_ratio=0.25), run_time=self.dur(1.0))

            # «pesarlo con su probabilidad»
            self.en("pesar")
            self.play(*[ReplacementTransform(prods[k], pes[k]) for k in prods], run_time=self.dur(0.8))

            # «si alguno de los dos es cero»
            self.en("cero")
            tres = [pes[(0, 0)], pes[(0, 1)], pes[(1, 0)]]
            self.play(*[t.animate.set_color(ROJO) for t in tres], run_time=self.dur(0.5))

            # «el producto es cero»
            self.en("prod_cero")
            z = formula(r"\times\, 0", "=", "0", colores={0: ROJO, 2: ROJO}, escala=1.8).move_to([4.4, 2.2, 0])
            self.pop(z)

            # «solo cuenta la casilla»
            self.en("cuenta")
            m = T.marco(1, 1, AMBAR)
            self.play(Create(m), run_time=self.dur(0.5))

            # «se envió un uno y se recibió un uno»
            self.en("uno_uno")
            self.play(T.enc_f[1].animate.set_color(AMBAR).scale(1.2), T.enc_c[1].animate.set_color(AMBAR).scale(1.2),
                      run_time=self.dur(0.6))

            # «uno por uno por cero coma veintisiete»
            self.en("cuenta_f")
            f = formula("1", r"\cdot", "1", r"\cdot", "0{,}27", escala=1.8, colores={4: AMBAR}).move_to([4.4, 0.6, 0])
            oculta(f)
            self.add(f)
            self.play(LaggedStart(*revelar(*f), lag_ratio=0.25), run_time=self.dur(1.6))

            # «La correlación es cero coma veintisiete»
            self.en("resultado")
            r = formula(r"E[SR]", "=", "0{,}27", escala=1.7, colores={0: AMBAR, 2: AMBAR}).move_to([4.0, -1.4, 0])
            self.pop(r)
        self.wait(1.0)
        self.limpiar()
