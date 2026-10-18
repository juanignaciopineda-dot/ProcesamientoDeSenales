"""Escena 06 — No independientes: par y «más de tres» en un solo dado."""
from comun.escena import *


class NoIndependientes(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.contraejemplo()
        self.moraleja()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def contraejemplo(self):
        e = EspacioDado07(centro=(0, 1.9), lado=0.9)
        av = aviso_triangulo().scale_to_fit_height(1.1).move_to([-5.6, 1.9, 0])
        aros_par = e.aros([2, 4, 6], AMBAR, 0.08)
        aros_gr = e.aros([4, 5, 6], AZUL, 0.17)
        et_par = Text("Par", color=AMBAR, weight=BOLD).scale(0.65).move_to([-3.4, 0.55, 0])
        et_gr = Text("Más de 3", color=AZUL, weight=BOLD).scale(0.65).move_to([3.4, 0.55, 0])
        p_par = formula(r"P(\text{par})", "=", r"\tfrac12", escala=1.3).move_to([-3.4, -0.45, 0])
        p_gr = formula(r"P(>3)", "=", r"\tfrac12", escala=1.3).move_to([3.4, -0.45, 0])
        asumo = MathTex(r"\tfrac12\cdot\tfrac12", color=TXT).scale(1.5).move_to([-3.4, -2.0, 0])
        cuarto = MathTex(r"=\tfrac14", color=ESTIMACION).scale(1.5).next_to(asumo, RIGHT, buff=0.2)
        inter = e.aros([4, 6], ERROR, 0.0)
        dos_de_seis = MathTex(r"\tfrac26", color=TXT).scale(1.5).move_to([3.0, -2.0, 0])
        tercio = MathTex(r"=\tfrac13", color=VERDE).scale(1.5).next_to(dos_de_seis, RIGHT, buff=0.2)
        dist = MathTex(r"\neq", color=ERROR).scale(2.0).move_to([0, -2.0, 0])
        sube = MathTex(r"P(>3\mid \text{par})=\tfrac23", color=AMBAR).scale(1.4).move_to([0, -3.4, 0])

        with self.narrar("b1"):
            # «no todo es independiente»
            self.en("cuidado")
            self.pop(av, sonido="error")

            # «Con un solo dado»
            self.en("solo_dado")
            self.play(FadeIn(e), run_time=self.dur(0.6))

            # «sale par, y sale más de tres»
            self.en("dos_eventos")
            self.play(Create(aros_par), Create(aros_gr), FadeIn(et_par), FadeIn(et_gr), run_time=self.dur(0.8))

            # «Cada uno tiene probabilidad»
            self.en("cada")
            self.play(FadeIn(p_par[0]), FadeIn(p_gr[0]), run_time=self.dur(0.4))

            # «un medio»
            self.en("medio")
            self.play(FadeIn(p_par[1]), FadeIn(p_par[2]), FadeIn(p_gr[1]), FadeIn(p_gr[2]), run_time=self.dur(0.5))

            # «Si fueran independientes»
            self.en("fueran")
            self.play(FadeIn(asumo), run_time=self.dur(0.5))

            # «valdría un cuarto»
            self.en("cuarto")
            self.play(FadeIn(cuarto), run_time=self.dur(0.4))

            # «los números pares mayores que tres»
            self.en("pares_mayores")
            self.play(Create(inter), run_time=self.dur(0.5))

            # «el cuatro y el seis»
            self.en("cuatro_seis")
            self.resaltar(e.caras[3], e.caras[5], color=ERROR)

            # «dos de seis caras»
            self.en("dos_de_seis")
            self.play(FadeIn(dos_de_seis), run_time=self.dur(0.4))

            # «un tercio»
            self.en("tercio")
            self.play(FadeIn(tercio), run_time=self.dur(0.4))

            # «No es un cuarto»
            self.en("no_cuarto")
            self.play(FadeIn(dist), Create(tachar(VGroup(asumo, cuarto))), run_time=self.dur(0.6))
            self.sfx("error")

            # «hace más probable que sea grande»
            self.en("grande")
            self.pop(sube)

    # ------------------------------------------------------------ b2
    def moraleja(self):
        indep = Text("Independencia", color=AMBAR, weight=BOLD).scale(1.3).move_to([0, 2.6, 0])
        interr = Text("?", color=ERROR, weight=BOLD).scale(1.6).next_to(indep, RIGHT, buff=0.3)
        f1 = caja("Se comprueba", VERDE, ancho=3.6, alto=0.9, scale=0.7).move_to([-2.4, 0.9, 0])
        f2 = caja("Se justifica", AZUL, ancho=3.6, alto=0.9, scale=0.7).move_to([2.4, 0.9, 0])
        ok = tilde(VERDE, 0.7).next_to(indep, RIGHT, buff=0.3)
        mal = cruz(ERROR, 0.9).next_to(indep, RIGHT, buff=0.3)
        prod = formula(r"P(A\cap B)", "=", "P(A)", r"\cdot", "P(B)", escala=1.6, colores={}).move_to([0, -0.7, 0])
        sorp = MathTex(r"P(A\mid B)", color=AMBAR).scale(1.8).move_to([-1.0, -2.3, 0])
        adm = Text("¡!", color=ERROR, weight=BOLD).scale(1.8).next_to(sorp, RIGHT, buff=0.4)
        gente = VGroup(*[persona(AZUL).scale_to_fit_height(1.2) for _ in range(6)]).arrange(RIGHT, buff=0.5)
        gente.move_to([-1.4, -0.6, 0])
        globos = VGroup(*[Text("99 %", color=VERDE, weight=BOLD).scale(0.75).next_to(p, UP, buff=0.25) for p in gente])
        med = cruz_hospital().scale_to_fit_height(1.7).move_to([5.6, -0.6, 0])

        with self.narrar("b2"):
            # «no se supone porque sí»
            self.en("supone")
            self.corte()
            self.pop(indep)
            self.play(FadeIn(interr), run_time=self.dur(0.3))

            # «se comprueba o se justifica»
            self.en("comprueba")
            self.play(FadeIn(f1, shift=UP * 0.2), FadeIn(f2, shift=UP * 0.2), run_time=self.dur(0.6))

            # «Cuando la tengamos»
            self.en("cuando")
            self.play(ReplacementTransform(interr, ok), run_time=self.dur(0.4))

            # «las cuentas se simplificarán»
            self.en("simplifica")
            self.play(FadeIn(prod), run_time=self.dur(0.7))

            # «muchísimo»
            self.en("muchisimo")
            self.resaltar(prod, color=VERDE, escala=1.15)

            # «cuando no la tengamos»
            self.en("sin")
            self.play(ReplacementTransform(ok, mal), run_time=self.dur(0.4))

            # «sorpresas enormes»
            self.en("sorpresas")
            self.play(FadeIn(sorp), run_time=self.dur(0.4))
            self.pop(adm, sonido="error")

            # «engaña a casi todo el mundo»
            self.en("engana")
            self.corte()
            self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.2) for p in gente], lag_ratio=0.12),
                      FadeIn(globos), run_time=self.dur(1.0))

            # «muchos médicos»
            self.en("medicos")
            self.pop(med)
