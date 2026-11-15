"""Escena 14 — La tabla de errores del sensor: sin datos 4, predicción 2,826, filtrado 0,7386, suavizado 0,686."""
from comun.escena import *


def mini(estado: str, cx: float, cy: float) -> VGroup:
    """Ventana en miniatura: cinco casillas (pasado, pasado, pasado, ahora, futuro).
    estado: 'ninguna', 'pasado', 'hasta_ahora' o 'todo'. `.cas`."""
    activas = {"ninguna": 0, "pasado": 3, "hasta_ahora": 4, "todo": 5}[estado]
    g = VGroup()
    g.cas = []
    for i in range(5):
        c = Square(side_length=0.4, stroke_width=2.5, color=MEDIDA if i < activas else INK)
        c.set_fill(MEDIDA if i < activas else INK, 0.5 if i < activas else 0.1)
        c.move_to([cx + (i - 2) * 0.44, cy, 0])
        g.cas.append(c)
        g.add(c)
    return g


class LaTabla(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        ys = [2.0, 0.7, -0.6, -1.9]
        x0, esc = 0.6, 1.0
        guias = VGroup(*[Line([-6.6, y - 0.65, 0], [6.6, y - 0.65, 0], color=INK, stroke_width=1.5, stroke_opacity=0.4)
                         for y in ys])
        nombres = ["sin datos", "predicción", "filtrado", "suavizado"]
        rots = [Text(n, color=TXT, weight=BOLD).scale(0.55).move_to([-5.5, y, 0]) for n, y in zip(nombres, ys)]
        wins = [mini(k, -2.6, y) for k, y in zip(["ninguna", "pasado", "hasta_ahora", "todo"], ys)]
        vals = [4.0, 2.826, 0.7386, 0.686]
        colores = [INK, ERROR, ESTIMACION, VERDE]
        barras = [barra_h(v, y, x0, esc, c) for v, y, c in zip(vals, ys, colores)]
        txt_v = [r"4", r"2{,}826", r"0{,}7386", r"0{,}686"]
        etqs = [MathTex(s, color=c).scale(0.75).next_to(b, RIGHT, buff=0.2) for s, b, c in zip(txt_v, barras, colores)]
        tach = tachar(wins[1].cas[3])
        de4 = Arrow([5.5, ys[0] - 0.1, 0], [5.5, ys[1] + 0.1, 0], color=INK, buff=0, stroke_width=4,
                    max_tip_length_to_length_ratio=0.3)
        pct = [MathTex(s, color=c).scale(0.8).move_to([6.3, y, 0])
               for s, c, y in zip([r"29\,\%", r"82\,\%", r"83\,\%"], [ERROR, ESTIMACION, VERDE], ys[1:])]
        # los porcentajes van a la derecha de cada fila; la flecha entre las dos primeras filas queda en x = 5,9

        with self.narrar("b1"):
            # «La tabla»
            self.en("tabla")
            self.corte()
            self.play(Create(guias), run_time=self.dur(0.6))

            # «Sin usar ningún dato»
            self.en("sindatos")
            self.play(FadeIn(rots[0]), FadeIn(wins[0]), run_time=self.dur(0.5))

            # «la varianza, cuatro»
            self.en("var4")
            self.play(GrowFromEdge(barras[0], LEFT), FadeIn(etqs[0]), run_time=self.dur(0.6))

            # «Prediciendo con todo el pasado»
            self.en("fila2")
            self.play(FadeIn(rots[1]), FadeIn(wins[1]), run_time=self.dur(0.5))

            # «sin la muestra de ahora»
            self.en("sinahora")
            self.play(Create(tach), run_time=self.dur(0.4))

            # «dos coma ocho dos seis»
            self.en("p2826")
            self.play(GrowFromEdge(barras[1], LEFT), FadeIn(etqs[1]), run_time=self.dur(0.6))

            # «Filtrando»
            self.en("filt")
            self.play(FadeIn(rots[2]), FadeIn(wins[2]), run_time=self.dur(0.5))

            # «cero coma siete tres ocho seis»
            self.en("f07386")
            self.play(GrowFromEdge(barras[2], LEFT), FadeIn(etqs[2]), run_time=self.dur(0.6))

            # «Suavizando, con todo el registro»
            self.en("suav")
            self.play(FadeIn(rots[3]), FadeIn(wins[3]), run_time=self.dur(0.5))

            # «cero coma seis ocho seis»
            self.en("s0686")
            self.play(GrowFromEdge(barras[3], LEFT), FadeIn(etqs[3]), run_time=self.dur(0.6))

            # «De cuatro a dos coma ocho»
            self.en("de4")
            self.play(GrowArrow(de4), run_time=self.dur(0.5))

            # «el veintinueve por ciento»
            self.en("p29")
            self.pop(pct[0])

            # «el ochenta y dos»
            self.en("p82")
            self.pop(pct[1])

            # «el ochenta y tres»
            self.en("p83")
            self.pop(pct[2])

        self.wait(1.0)
        self.limpiar()
