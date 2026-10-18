"""Lee el guion.md de un episodio: narración por bloque + momentos anclados.

Formato (detalle en README.md §6):

    # Escena 01 — NombreClase

    **Capítulo YouTube:** Título del capítulo
    ...

    ## Narración

    <!-- b1 -->
    Texto que lee la voz.

    - «frase literal» → `marca`: qué se ve en ese momento

Para cada bloque, `Guion.texto(b)` devuelve la narración con
`<bookmark mark="marca"/>` insertado antes de cada frase anclada y con los
reemplazos de pronunciación aplicados (solo fuera de las etiquetas);
`Guion.subtitulo(b)` devuelve la narración original, para los subtítulos.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from comun.pronunciacion import aplicar

_RE_ESCENA = re.compile(r"^#\s*Escena\s*0*(?P<num>\d+)\s*—\s*(?P<clase>\w+)\s*$", re.MULTILINE)
_RE_MARCA_BLOQUE = re.compile(r"<!--\s*(b\d+)\s*-->")
_RE_MOMENTO = re.compile(r"^\s*-\s*«(?P<frase>.+?)»\s*→\s*`(?P<marca>[a-z0-9_]+)`\s*:?\s*(?P<desc>.*)$")
_RE_CAPITULO = re.compile(r"^\*\*Capítulo YouTube:\*\*\s*(.+?)\s*$", re.MULTILINE)
_RE_BOOKMARK = re.compile(r"(<bookmark mark=\"\w+\"/>)")


@dataclass
class Momento:
    frase: str
    marca: str
    descripcion: str


@dataclass
class Bloque:
    clave: str
    narracion: str
    momentos: list[Momento] = field(default_factory=list)


@dataclass
class InfoEscena:
    numero: str          # "01"
    clase: str           # nombre de la clase de Manim
    capitulo: str | None  # título para capitulos.txt de YouTube


# --------------------------------------------------------------------------- lectura

def escenas_del_guion(guion_md: Path) -> list[InfoEscena]:
    """Todas las escenas del guion, en orden. La usa render.py."""
    texto = Path(guion_md).read_text(encoding="utf-8")
    matches = list(_RE_ESCENA.finditer(texto))
    escenas = []
    for i, m in enumerate(matches):
        fin = matches[i + 1].start() if i + 1 < len(matches) else len(texto)
        cap = _RE_CAPITULO.search(texto, m.end(), fin)
        escenas.append(InfoEscena(m.group("num").zfill(2), m.group("clase"),
                                  cap.group(1) if cap else None))
    return escenas


def _seccion_escena(texto: str, numero: str, ruta: Path) -> str:
    matches = list(_RE_ESCENA.finditer(texto))
    if not matches:
        raise ValueError(f"{ruta}: no hay ninguna '# Escena NN — Clase'")
    objetivo = str(int(numero)).zfill(2)
    for i, m in enumerate(matches):
        if m.group("num").zfill(2) == objetivo:
            fin = matches[i + 1].start() if i + 1 < len(matches) else len(texto)
            return texto[m.end():fin]
    raise ValueError(f"{ruta}: no existe la escena {objetivo}")


def _leer_bloques(seccion: str, numero: str, ruta: Path) -> dict[str, Bloque]:
    idx = seccion.find("## Narración")
    if idx == -1:
        raise ValueError(f"{ruta}: la escena {numero} no tiene '## Narración'")
    seccion = seccion[idx + len("## Narración"):]
    # un separador '---' o un encabezado cierra la narración de la escena
    seccion = re.split(r"^(?:---|#)", seccion, maxsplit=1, flags=re.MULTILINE)[0]

    partes = _RE_MARCA_BLOQUE.split(seccion)
    # partes = [antes, 'b1', cuerpo1, 'b2', cuerpo2, ...]
    bloques: dict[str, Bloque] = {}
    for clave, cuerpo in zip(partes[1::2], partes[2::2]):
        lineas_narracion, momentos = [], []
        for linea in cuerpo.splitlines():
            m = _RE_MOMENTO.match(linea)
            if m:
                momentos.append(Momento(m.group("frase"), m.group("marca"), m.group("desc")))
            elif linea.strip():
                lineas_narracion.append(linea.strip())
        narracion = " ".join(" ".join(lineas_narracion).split())
        bloques[clave] = Bloque(clave, narracion, momentos)
    if not bloques:
        raise ValueError(f"{ruta}: la escena {numero} no tiene bloques '<!-- bN -->'")
    return bloques


def _insertar_marcas(bloque: Bloque, numero: str, ruta: Path) -> str:
    """Narración con <bookmark/> antes de cada frase anclada, en orden."""
    texto = bloque.narracion
    salida, cursor = [], 0
    vistas = set()
    for mom in bloque.momentos:
        if mom.marca in vistas:
            raise ValueError(f"{ruta}: escena {numero} {bloque.clave}: marca repetida '{mom.marca}'")
        vistas.add(mom.marca)
        pos = texto.find(mom.frase, cursor)
        if pos == -1:
            antes = texto.find(mom.frase)
            detalle = ("está antes que el momento anterior (los momentos van en orden)"
                       if antes != -1 else "no aparece literal en la narración")
            raise ValueError(f"{ruta}: escena {numero} {bloque.clave}: la frase «{mom.frase}» {detalle}")
        salida.append(texto[cursor:pos])
        salida.append(f'<bookmark mark="{mom.marca}"/>')
        cursor = pos
    salida.append(texto[cursor:])
    return "".join(salida)


def _pronunciar(texto_con_marcas: str) -> str:
    """Aplica los reemplazos de pronunciación sin tocar las etiquetas."""
    partes = _RE_BOOKMARK.split(texto_con_marcas)
    return "".join(p if _RE_BOOKMARK.fullmatch(p) else aplicar(p) for p in partes)


# --------------------------------------------------------------------------- API

class Guion:
    """Narración y momentos de UNA escena, leídos del guion.md de la carpeta
    del archivo de la escena (o de `ruta_guion`)."""

    def __init__(self, archivo_escena: str, numero_escena: str,
                 ruta_guion: str | Path | None = None):
        carpeta = Path(archivo_escena).resolve().parent
        self._ruta = Path(ruta_guion) if ruta_guion else carpeta / "guion.md"
        self.numero = str(int(numero_escena)).zfill(2)
        seccion = _seccion_escena(self._ruta.read_text(encoding="utf-8"), self.numero, self._ruta)
        self._bloques = _leer_bloques(seccion, self.numero, self._ruta)
        # se valida todo al cargar: un guion roto falla antes de renderizar
        self._textos = {c: _pronunciar(_insertar_marcas(b, self.numero, self._ruta))
                        for c, b in self._bloques.items()}

    def _bloque(self, clave: str) -> Bloque:
        try:
            return self._bloques[clave]
        except KeyError:
            raise KeyError(f"{self._ruta}: escena {self.numero} no tiene el bloque '{clave}'. "
                           f"Hay: {list(self._bloques)}")

    def texto(self, clave: str) -> str:
        """Texto para la voz: con marcas y con reemplazos de pronunciación."""
        self._bloque(clave)
        return self._textos[clave]

    def subtitulo(self, clave: str) -> str:
        """Texto original del guion, para los subtítulos."""
        return self._bloque(clave).narracion

    def marcas(self, clave: str) -> list[Momento]:
        return list(self._bloque(clave).momentos)

    # compatibilidad con la versión anterior
    def crudo(self, clave: str) -> str:
        return self.subtitulo(clave)

    def __getitem__(self, clave: str) -> str:
        return self.texto(clave)

    def __iter__(self):
        return iter(self._bloques)

    def __len__(self) -> int:
        return len(self._bloques)
