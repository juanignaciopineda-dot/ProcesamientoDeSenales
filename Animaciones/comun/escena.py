"""Clase base de todas las escenas del curso.

    from comun.escena import *

    class Gancho(EscenaCurso):
        ESCENA = "01"
        def construct(self):
            with self.narrar("b1"):
                self.en("linea")
                self.play(Create(linea), run_time=0.6)

Trae: voz + guion ya cargados, espera por marcas, efectos de sonido,
tipografía cinética y cámara móvil (MovingCameraScene).
"""
from __future__ import annotations

import inspect
import json
from contextlib import contextmanager
from pathlib import Path

from manim import *
from manim_voiceover import VoiceoverScene

from comun import sfx as _sfx
from comun.estilo import *
from comun.figuras import *
from comun.guion import Guion
from comun.iconos import *
from comun.voz import servicio_voz


def _nombre(m: Mobject) -> str:
    """Cómo se nombra un objeto en el informe de controles."""
    return getattr(m, "text", None) or getattr(m, "tex_string", None) or type(m).__name__


class EscenaCurso(VoiceoverScene, MovingCameraScene):
    ESCENA: str = ""      # número de escena en el guion.md de la carpeta
    # La imagen tiene que llegar un poco ANTES que la palabra: si la animación
    # arranca justo cuando empieza la palabra, termina de verse después y se
    # percibe que la voz "se adelanta".
    ANTICIPO: float = 0.3

    def setup(self):
        super().setup()
        configurar()
        self.set_speech_service(servicio_voz())
        if not self.ESCENA:
            raise ValueError(f"{type(self).__name__}: falta definir ESCENA = 'NN'")
        archivo = inspect.getfile(type(self))
        self._carpeta = Path(archivo).resolve().parent
        self.G = Guion(archivo, self.ESCENA)
        self._bloque = None
        self._orden: list[str] = []
        self._ultima: str | None = None
        self._informe = {"retrasos": [], "silencios": [], "encimados": [], "fuera_de_cuadro": []}
        self._vistos: set = set()

    # ------------------------------------------------------------ voz

    @contextmanager
    def narrar(self, bloque: str):
        """Lee un bloque del guion. Dentro del `with` se anima con `self.en()`;
        al salir se espera a que termine el audio del bloque."""
        self._bloque = bloque
        self._orden = [m.marca for m in self.G.marcas(bloque)]
        self._ultima = None
        with self.voiceover(text=self.G.texto(bloque),
                            subcaption=self.G.subtitulo(bloque)) as t:
            yield t
            # si las animaciones se pasaron del audio, el bloque siguiente
            # arranca tarde: queda un silencio de voz
            exceso = float(self.renderer.time) - t.end_t
            if exceso > 0.3:
                self._informe["silencios"].append(
                    {"bloque": bloque, "t": round(t.end_t, 2), "segundos": round(exceso, 2)})

    def en(self, marca: str) -> None:
        """Espera hasta que la voz llega a la frase anclada a `marca`.
        Si la animación ya viene atrasada, lo anota en el informe."""
        tracker = self.current_tracker
        tracker._check_bookmarks()
        if marca not in tracker.bookmark_times:
            raise KeyError(f"escena {self.ESCENA} {self._bloque}: no existe la marca '{marca}'")
        t_marca = tracker.bookmark_times[marca]
        atraso = float(self.renderer.time) - t_marca
        if atraso > 0.2:
            self._informe["retrasos"].append({"bloque": self._bloque, "marca": marca,
                                              "t": round(t_marca, 2), "segundos": round(atraso, 2)})
        self._ultima = marca
        self.safe_wait(t_marca - self.ANTICIPO - float(self.renderer.time))

    def paso(self, marca: str, *anims, t: float = 0.6, sonido: str | None = None) -> None:
        """Atajo: espera la marca y reproduce `anims` (un Mobject suelto se entra con `FadeIn`)."""
        self.en(marca)
        if sonido:
            self.sfx(sonido)
        self.play(*[FadeIn(a) if isinstance(a, Mobject) else a for a in anims], run_time=self.dur(t))

    def margen(self, minimo: float = 0.2) -> float:
        """Segundos disponibles hasta la próxima marca del bloque (o hasta el
        final del audio). Sirve para dimensionar animaciones sin atrasarse."""
        tracker = self.current_tracker
        siguientes = self._orden[self._orden.index(self._ultima) + 1:] if self._ultima in self._orden else self._orden
        if siguientes:
            return max(minimo, tracker.time_until_bookmark(siguientes[0]))
        return max(minimo, tracker.get_remaining_duration())

    def dur(self, x: float, holgura: float = 0.12) -> float:
        """`run_time` de una animación: `x` segundos como mucho, sin pasar de la próxima marca."""
        return max(0.25, min(x, self.margen() - holgura))

    # ------------------------------------------------------------ controles automáticos

    def play(self, *args, **kwargs):
        super().play(*args, **kwargs)
        self._revisar_encimados()

    def _revisar_encimados(self) -> None:
        """Busca texto tocado parcialmente por otra forma (dibujos que se
        pisan) y texto que se sale del cuadro. Contener por completo un texto
        (texto dentro de una caja) no cuenta.

        Las fórmulas (`MathTex`, `Tex`) cuentan como texto, cada una entera:
        sus partes internas y los dígitos de un `DecimalNumber` (que Manim
        arma con `SingleStringMathTex`) no se comparan entre sí."""
        familia = [m for top in self.mobjects if top is not self.camera.frame for m in top.get_family()]

        def opacidad(m):
            # un MathTex es un contenedor sin relleno propio: lo visible son sus letras
            partes = m.get_family() if isinstance(m, SingleStringMathTex) else [m]
            return max(max(x.get_fill_opacity(), x.get_stroke_opacity()) for x in partes)

        visibles = [m for m in familia if isinstance(m, (Text, DecimalNumber, SingleStringMathTex))
                    and opacidad(m) > 0.1]
        internos = {id(x) for m in visibles for x in m.get_family()[1:]}
        textos = [m for m in visibles if id(m) not in internos]
        letras = {id(x) for t in textos for x in t.get_family()}
        # lo marcado con `permitir_encima` (una lupa que pasa sobre un texto) no cuenta
        tolerados = {id(x) for m in familia if getattr(m, "permitir_encima", False) for x in m.get_family()}
        formas = [m for m in familia
                  if isinstance(m, VMobject) and id(m) not in letras and id(m) not in tolerados
                  and m.get_num_points() > 0
                  and not isinstance(m, (Line, DashedVMobject, FullScreenRectangle))
                  and max(m.get_fill_opacity(), m.get_stroke_opacity()) >= 0.1]

        def caja(m):
            return m.get_corner(DL)[:2], m.get_corner(UR)[:2]

        def area(a, b):
            return max(0.0, b[0] - a[0]) * max(0.0, b[1] - a[1])

        t_ahora = round(float(self.renderer.time), 1)
        fw, fh = self.camera.frame.width / 2, self.camera.frame.height / 2
        cx, cy = self.camera.frame.get_center()[:2]
        for t in textos:
            ta, tb = caja(t)
            at = area(ta, tb)
            if at <= 0:
                continue
            nombre = _nombre(t)
            sin_zoom = abs(self.camera.frame.width - config.frame_width) < 0.01
            if sin_zoom and not getattr(t, "permitir_fuera", False) and (
                    ta[0] < cx - fw - 0.05 or tb[0] > cx + fw + 0.05 or ta[1] < cy - fh - 0.05 or tb[1] > cy + fh + 0.05):
                clave = ("fuera", nombre)
                if clave not in self._vistos:
                    self._vistos.add(clave)
                    self._informe["fuera_de_cuadro"].append({"t": t_ahora, "texto": nombre})
            propios = {id(x) for x in t.get_family()}
            for o in textos + formas:
                if id(o) in propios or id(t) in {id(x) for x in o.get_family()}:
                    continue
                oa, ob = caja(o)
                inter = area(np.maximum(ta, oa), np.minimum(tb, ob))
                if inter > 0.004 and inter < 0.95 * at:
                    otro = _nombre(o)
                    clave = ("enc", nombre, otro)
                    if clave not in self._vistos:
                        self._vistos.add(clave)
                        self._informe["encimados"].append(
                            {"t": t_ahora, "texto": nombre, "con": otro, "solape": round(inter / at, 2)})

    def tear_down(self):
        super().tear_down()
        destino = self._carpeta / "media" / "informes" / f"{type(self).__name__}.json"
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(json.dumps(self._informe, ensure_ascii=False, indent=1), encoding="utf-8")

    # ------------------------------------------------------------ sonido

    def sfx(self, nombre: str, gain: float = -14, offset: float = 0.0) -> None:
        """Efecto de sonido en el instante actual (+ `offset` segundos)."""
        self.add_sound(str(_sfx.ruta(nombre)), time_offset=offset, gain=gain)

    def rafaga(self, teclas: VGroup, n: int = 14, run_time: float = 1.4, color=AMBAR,
               semilla: int = 3) -> None:
        """Teclas que se encienden y apagan en ráfaga, con sonido de tecleo."""
        rng = np.random.default_rng(semilla)
        # sin repetir: dos animaciones a la vez sobre la misma tecla se pisan
        n = min(n, len(teclas))
        elegidas = [teclas[int(i)] for i in rng.choice(len(teclas), size=n, replace=False)]
        for i in range(n):
            self.sfx("tecla", gain=-18, offset=i * run_time / n)
        self.play(LaggedStart(*[k.animate(rate_func=there_and_back).set_fill(color, 1)
                                for k in elegidas], lag_ratio=0.35), run_time=run_time)

    # ------------------------------------------------------------ tipografía cinética

    def palabra(self, txt: str, color=AMBAR, escala: float = 1.0) -> Text:
        """Palabra clave grande, centrada, lista para `pop`."""
        return Text(txt, color=color, weight=BOLD).scale(escala)

    def pop(self, *mobs: Mobject, run_time: float = 0.45, sonido: str | None = "pop") -> None:
        """Entrada con rebote: crece desde 0 pasando por 115% (efecto 'pop')."""
        if sonido:
            self.sfx(sonido)
        anims = []
        for m in mobs:
            m.save_state()
            m.scale(0.01)
            anims.append(Restore(m, rate_func=rate_functions.ease_out_back))
        self.play(*anims, run_time=run_time)

    def fuera(self, *mobs: Mobject, run_time: float = 0.3) -> None:
        """Salida rápida (encoge y se desvanece)."""
        self.play(*[FadeOut(m, scale=0.6) for m in mobs], run_time=run_time)

    def resaltar(self, *mobs: Mobject, color=AMBAR, escala: float = 1.1, run_time: float = 0.5) -> None:
        """Llama la atención sobre algo ya presente: crece y se le colorea SOLO
        el borde, ida y vuelta.

        Usar esto y NO `Indicate` sobre cajas con texto: Indicate tiñe todo el
        grupo (relleno y letras) del mismo color y el texto se vuelve una mancha.
        """
        self.play(*[m.animate(rate_func=there_and_back).scale(escala).set_stroke(color=color)
                    for m in mobs], run_time=run_time)

    def destello(self, m: Mobject, color=AMBAR, run_time: float = 0.6) -> None:
        """Alias de `resaltar` (compatibilidad)."""
        self.resaltar(m, color=color, run_time=run_time)

    def flotar(self, m: Mobject, amp: float = 0.07, periodo: float = 2.6) -> Mobject:
        """Movimiento sutil (sube y baja) para que un plano no quede quieto
        mientras la voz sigue. OJO: antes de volver a mover `m` con una
        animación, llamar `m.clear_updaters()`."""
        t0 = self.renderer.time
        base = m.get_center().copy()
        m.add_updater(lambda mob: mob.move_to(
            base + UP * amp * np.sin(2 * PI * (self.renderer.time - t0) / periodo)))
        return m

    def texto_centrado(self, *lineas: str, color=TXT, escala: float = 1.0, bold: bool = True) -> VGroup:
        """Varias líneas de texto centradas entre sí (Text con \\n las alinea a la izquierda)."""
        return VGroup(*[Text(l, color=color, weight=BOLD if bold else NORMAL).scale(escala)
                        for l in lineas]).arrange(DOWN, buff=0.18)

    def corte(self, *mantener: Mobject) -> None:
        """Corte seco a plano nuevo: vacía la escena (salvo `mantener`).

        Usar esto y NO `self.remove(grupo)`: cuando se anima una parte de un
        grupo (ej. una tecla), Manim saca esa parte a la lista de la escena y
        `remove(grupo)` ya no la encuentra.
        """
        self.clear()
        self.add(*mantener)

    def limpiar(self, run_time: float = 0.35) -> None:
        """Saca todo lo que hay en pantalla (corte a plano nuevo)."""
        mobs = [m for m in self.mobjects if m is not self.camera.frame]
        if mobs:
            self.play(*[FadeOut(m) for m in mobs], run_time=run_time)

    # ------------------------------------------------------------ cámara

    def zoom(self, objetivo: Mobject | np.ndarray, ancho: float, run_time: float = 0.8) -> None:
        """Mueve la cámara para encuadrar `objetivo` con el ancho dado."""
        centro = objetivo.get_center() if isinstance(objetivo, Mobject) else objetivo
        self.play(self.camera.frame.animate.move_to(centro).set(width=ancho), run_time=run_time)

    def zoom_reset(self, run_time: float = 0.8) -> None:
        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=config.frame_width),
                  run_time=run_time)
