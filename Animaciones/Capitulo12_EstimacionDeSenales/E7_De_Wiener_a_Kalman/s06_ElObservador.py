"""Escena 06 — El observador: una copia del modelo que predice y se corrige con la sorpresa."""
from comun.escena import *


class ElObservador(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.observador()
        self.wait(0.6)
        self.eleccion()
        self.wait(1.0)
        self.limpiar()

    def observador(self):
        planta = caja("planta", AZUL, ancho=2.4, alto=0.8, scale=0.5).move_to([-4.6, 2.6, 0])
        copia = caja("copia: q̂", AMBAR, ancho=2.4, alto=0.8, scale=0.5).move_to([-4.6, 0.3, 0])
        ord_ = ordenador().scale(0.8).move_to([-6.3, -1.5, 0])
        f = formula("\\hat q[n+1]", "=", "0{,}6\\,\\hat q[n]", "+", "G", "\\,(", "x[n]-\\hat q[n]", ")",
                    escala=0.8, colores={0: ESTIMACION, 2: ESTIMACION, 4: ESTIMACION}).move_to([2.6, 2.6, 0])
        sorp = formula("x[n]-\\hat q[n]", escala=0.9, colores={0: MEDIDA}).move_to([2.6, 1.1, 0])
        etq = etiqueta("sorpresa", AMBAR, 0.5).move_to([2.6, 0.45, 0])
        cero = MathTex("0", color=VERDE).scale(1.1).move_to([2.6, 1.1, 0])
        linea = Line([0.6, -1.0, 0], [5.0, -1.0, 0], color=INK, stroke_width=4)
        knob = Dot([0.6, -1.0, 0], radius=0.16, color=ESTIMACION)
        l0 = MathTex("0", color=INK).scale(0.6).move_to([0.6, -1.5, 0])
        l1 = MathTex("1", color=INK).scale(0.6).move_to([5.0, -1.5, 0])
        lg = MathTex("G", color=ESTIMACION).scale(0.8).move_to([2.8, -0.45, 0])
        ign = etiqueta("ignora las medidas", INK, 0.5).move_to([2.8, -2.4, 0])
        fia = etiqueta("se fía del dato", MEDIDA, 0.5).move_to([2.8, -2.4, 0])
        with self.narrar("b1"):
            # «una copia del modelo»
            self.en("copia")
            self.play(FadeIn(planta), FadeIn(copia, shift=DOWN * 0.3), run_time=self.dur(0.7))
            # «dentro del ordenador»
            self.en("ord")
            self.play(FadeIn(ord_), run_time=self.dur(0.5))
            # «Predice con el modelo»
            self.en("predice")
            self.play(FadeIn(f[0]), FadeIn(f[1]), FadeIn(f[2]), run_time=self.dur(0.8))
            # «cero coma seis por su estimación de ahora»
            self.en("seis")
            self.resaltar(f[2], run_time=0.6)
            # «se corrige con la sorpresa»
            self.en("sorpresa")
            self.play(FadeIn(sorp), FadeIn(etq), run_time=self.dur(0.7))
            # «multiplicado por una ganancia»
            self.en("gan")
            self.play(FadeIn(f[3]), FadeIn(f[4]), FadeIn(f[5]), FadeIn(f[6]), FadeIn(f[7]), run_time=self.dur(0.8))
            # «Si lo medido coincide con lo esperado»
            self.en("coincide")
            self.play(Transform(sorp, cero), run_time=self.dur(0.6))
            # «no hay corrección»
            self.en("nocorr")
            self.play(VGroup(f[3], f[4], f[5], f[6], f[7]).animate.fade(0.8), run_time=self.dur(0.6))
            # «Con ge igual a cero»
            self.en("g0")
            self.play(Create(linea), FadeIn(knob), FadeIn(l0), FadeIn(l1), FadeIn(lg), FadeIn(ign),
                      run_time=self.dur(0.7))
            # «con ge igual a uno»
            self.en("g1")
            self.play(knob.animate.move_to([5.0, -1.0, 0]), Transform(ign, fia), run_time=self.dur(1.0))

    def eleccion(self):
        self.corte()
        top = formula("G", "=", "?", escala=1.7, colores={0: ESTIMACION, 2: AMBAR}).move_to([0, 2.7, 0])
        f = formula("\\hat q[n+1]", "=", "(", "0{,}6-G", ")", "\\,\\hat q[n]", "+", "G\\,x[n]", escala=0.9,
                    colores={0: ESTIMACION, 3: ESTIMACION}).move_to([-1.0, 0.9, 0])
        pz = plano_c([4.9, -1.3], radio=1.3)
        p_ini = Dot([4.9 + 1.3 * 0.4, -1.3, 0], radius=0.12, color=AZUL)
        objetivo = Circle(radius=0.17, color=ESTIMACION, stroke_width=4).move_to([4.9 + 1.3 * 0.157, -1.3, 0])
        v = formula("G", "=", "0{,}6", "-", "0{,}157", "=", "?", escala=0.95,
                    colores={0: ESTIMACION}).move_to([-3.3, -1.5, 0])
        lz = MathTex("0{,}443", color=ESTIMACION)
        with self.narrar("b2"):
            # «¿Qué ganancia elegir?»
            self.en("pregunta")
            self.play(FadeIn(top[0]), FadeIn(top[1]), run_time=0.3)
            self.pop(top[2])
            # «un polo en cero coma seis menos ge»
            self.en("polo")
            self.play(FadeIn(f), Create(pz), FadeIn(p_ini), run_time=self.dur(1.0))
            # «Si queremos que caiga justo»
            self.en("caiga")
            self.play(p_ini.animate.move_to([4.9 + 1.3 * 0.6, -1.3, 0]), run_time=0.7)
            self.play(p_ini.animate.move_to([4.9 + 1.3 * 0.3, -1.3, 0]), run_time=self.dur(0.7))
            # «el cero coma uno cinco siete de la factorización»
            self.en("objetivo")
            self.play(Create(objetivo), run_time=self.dur(0.6))
            # «ge tiene que valer»
            self.en("valer")
            self.play(FadeIn(v[0]), FadeIn(v[1]), run_time=self.dur(0.5))
            # «cero coma seis menos cero coma uno cinco siete»
            self.en("resta")
            self.play(FadeIn(v[2]), FadeIn(v[3]), FadeIn(v[4]), run_time=self.dur(1.0))
            # «Haz la cuenta antes de seguir»
            self.en("cuenta")
            self.play(FadeIn(v[5]), FadeIn(v[6]), run_time=self.dur(0.5))
            # «cero coma cuatro cuatro tres»
            self.en("r443")
            lz.move_to(v[6])
            self.play(Transform(v[6], MathTex("0{,}443", color=ESTIMACION).scale(0.95).next_to(v[5], RIGHT, buff=0.15)),
                      Transform(top[2], MathTex("0{,}443", color=ESTIMACION).scale(1.7).next_to(top[1], RIGHT, buff=0.2)),
                      p_ini.animate.move_to([4.9 + 1.3 * 0.157, -1.3, 0]), run_time=self.dur(0.8))
            # «¿Te suena ese número?»
            self.en("suena")
            self.resaltar(top, color=AMBAR, run_time=0.8)
