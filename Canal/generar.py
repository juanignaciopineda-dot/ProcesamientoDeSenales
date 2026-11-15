"""Genera el logo, el banner y la marca de agua del canal de YouTube.

Uso:  py -3.12 Canal/generar.py
Deja logo.png (800x800), banner.png (2560x1440) y marca_de_agua.png (150x150)
en esta carpeta. Usa la paleta de Animaciones/comun/estilo.py.
"""
import math
from pathlib import Path

import cairo
import numpy as np

AQUI = Path(__file__).parent

FONDO = "#12141a"
TXT = "#e6e9f0"
INK = "#9aa3b8"
AZUL = "#4c8dff"
AMBAR = "#f0883e"
MAGENTA = "#c86bd8"
CIAN = "#39c5cf"
FUENTE = "Segoe UI"

NOMBRE = "Promoción Directa"
APELLIDO = "ACADEMY"
LEMA = "Cursos universitarios de ingeniería y computación"


def rgb(hexa):
    h = hexa.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def color(ctx, hexa, alfa=1.0):
    ctx.set_source_rgba(*rgb(hexa), alfa)


def fondo(ctx, ancho, alto):
    """Fondo oscuro con un brillo suave en el centro."""
    color(ctx, FONDO)
    ctx.paint()
    brillo = cairo.RadialGradient(ancho / 2, alto / 2, 0,
                                  ancho / 2, alto / 2, max(ancho, alto) * 0.6)
    brillo.add_color_stop_rgba(0, *rgb(AZUL), 0.16)
    brillo.add_color_stop_rgba(1, *rgb(AZUL), 0.0)
    ctx.set_source(brillo)
    ctx.paint()


def simbolo(ctx, cx, cy, lado, tono=AMBAR, punto=AZUL):
    """Un visto bueno cuya rama larga termina en flecha: aprobar y subir."""
    ctx.save()
    ctx.translate(cx, cy)
    ctx.scale(lado, lado)
    inicio, codo, punta = (-0.40, 0.04), (-0.13, 0.31), (0.40, -0.33)
    dx, dy = punta[0] - codo[0], punta[1] - codo[1]
    largo = math.hypot(dx, dy)
    ux, uy = dx / largo, dy / largo
    base = (punta[0] - ux * 0.22, punta[1] - uy * 0.22)

    color(ctx, tono)
    ctx.set_line_width(0.13)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    ctx.move_to(*inicio)
    ctx.line_to(*codo)
    ctx.line_to(*base)
    ctx.stroke()

    # punta de flecha
    ancho = 0.17
    ctx.move_to(punta[0] + ux * 0.06, punta[1] + uy * 0.06)
    ctx.line_to(base[0] - uy * ancho, base[1] + ux * ancho)
    ctx.line_to(base[0] + uy * ancho, base[1] - ux * ancho)
    ctx.close_path()
    ctx.set_line_width(0.04)
    ctx.fill_preserve()
    ctx.stroke()

    if punto:
        color(ctx, punto)
        ctx.arc(inicio[0], inicio[1], 0.085, 0, 2 * math.pi)
        ctx.fill()
    ctx.restore()


def texto(ctx, cadena, x, y, cuerpo, tono, negrita=False, espaciado=0.0, alfa=1.0):
    """Escribe con la línea base en (x, y) y devuelve el ancho."""
    ctx.select_font_face(FUENTE, cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD if negrita else cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(cuerpo)
    color(ctx, tono, alfa)
    if not espaciado:
        ctx.move_to(x, y)
        ctx.show_text(cadena)
        return ctx.text_extents(cadena).x_advance
    cursor = x
    for letra in cadena:
        ctx.move_to(cursor, y)
        ctx.show_text(letra)
        cursor += ctx.text_extents(letra).x_advance + espaciado
    return cursor - espaciado - x


def ancho_texto(ctx, cadena, cuerpo, negrita=False, espaciado=0.0):
    ctx.select_font_face(FUENTE, cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD if negrita else cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(cuerpo)
    if not espaciado:
        return ctx.text_extents(cadena).x_advance
    return sum(ctx.text_extents(l).x_advance for l in cadena) + espaciado * (len(cadena) - 1)


def curva(ctx, xs, ys, tono, grosor, alfa_de_x):
    """Traza una curva tramo a tramo, con la opacidad que diga alfa_de_x."""
    ctx.set_line_width(grosor)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    for i in range(len(xs) - 1):
        alfa = alfa_de_x(xs[i])
        if alfa <= 0.003:
            continue
        color(ctx, tono, alfa)
        ctx.move_to(xs[i], ys[i])
        ctx.line_to(xs[i + 1], ys[i + 1])
        ctx.stroke()


def logo():
    lado = 800
    lienzo = cairo.ImageSurface(cairo.FORMAT_ARGB32, lado, lado)
    ctx = cairo.Context(lienzo)
    fondo(ctx, lado, lado)
    # YouTube lo recorta en círculo: todo queda dentro del círculo central
    simbolo(ctx, lado / 2 + 4, lado / 2 + 6, 510)
    lienzo.write_to_png(str(AQUI / "logo.png"))


def marca_de_agua():
    lado = 150
    lienzo = cairo.ImageSurface(cairo.FORMAT_ARGB32, lado, lado)
    ctx = cairo.Context(lienzo)
    color(ctx, FONDO, 0.88)
    ctx.arc(lado / 2, lado / 2, lado / 2 - 2, 0, 2 * math.pi)
    ctx.fill()
    simbolo(ctx, lado / 2 + 1, lado / 2 + 1, 104)
    lienzo.write_to_png(str(AQUI / "marca_de_agua.png"))


def banner():
    ancho, alto = 2560, 1440
    # zona que se ve en todos los dispositivos: 1546 x 423, centrada
    seg_x0, seg_x1 = (ancho - 1546) / 2, (ancho + 1546) / 2
    lienzo = cairo.ImageSurface(cairo.FORMAT_ARGB32, ancho, alto)
    ctx = cairo.Context(lienzo)
    fondo(ctx, ancho, alto)

    # cuadrícula de puntos, tenue
    color(ctx, INK, 0.10)
    for x in range(40, ancho, 80):
        for y in range(40, alto, 80):
            ctx.arc(x, y, 2.2, 0, 2 * math.pi)
            ctx.fill()

    xs = np.linspace(0, ancho, 1400)
    azar = np.random.default_rng(7)
    plano = lambda x: 0.55

    # franjas de arriba y de abajo (se ven en la tele)
    for centro, signo in ((250, 1), (1190, -1)):
        curva(ctx, xs, centro + signo * 90 * np.sin(xs / 150), AZUL, 5, plano)
        curva(ctx, xs, centro + signo * 55 * np.sin(xs / 61 + 1.3), CIAN, 3, lambda x: 0.35)
        ruido = np.convolve(azar.normal(0, 1, xs.size), np.ones(9) / 9, mode="same")
        curva(ctx, xs, centro + signo * (90 * np.sin(xs / 150) + 70 * ruido),
              MAGENTA, 2.5, lambda x: 0.40)

    # franja central (ordenador): la señal se apaga antes de llegar al texto
    def bordes(x):
        dist = min(x, ancho - x)
        return 0.55 * max(0.0, 1 - dist / (seg_x0 - 70))

    ruido = np.convolve(azar.normal(0, 1, xs.size), np.ones(7) / 7, mode="same")
    curva(ctx, xs, alto / 2 + 80 * np.sin(xs / 95), AZUL, 5, bordes)
    curva(ctx, xs, alto / 2 + 80 * np.sin(xs / 95) + 75 * ruido, MAGENTA, 2.5,
          lambda x: bordes(x) * 0.8)

    # bloque central: símbolo + nombre + lema
    cuerpo_nombre, cuerpo_apellido, cuerpo_lema = 124, 50, 44
    lado_simbolo, hueco = 300, 56
    ancho_bloque = lado_simbolo + hueco + max(
        ancho_texto(ctx, NOMBRE, cuerpo_nombre, negrita=True),
        ancho_texto(ctx, LEMA, cuerpo_lema))
    assert ancho_bloque <= seg_x1 - seg_x0 - 40, "el bloque no entra en la zona segura"
    x0 = (ancho - ancho_bloque) / 2
    simbolo(ctx, x0 + lado_simbolo / 2, alto / 2 + 4, lado_simbolo)
    xt = x0 + lado_simbolo + hueco
    texto(ctx, NOMBRE, xt, alto / 2 - 32, cuerpo_nombre, TXT, negrita=True)
    texto(ctx, APELLIDO, xt + 4, alto / 2 + 44, cuerpo_apellido, AMBAR,
          negrita=True, espaciado=20)
    texto(ctx, LEMA, xt + 2, alto / 2 + 126, cuerpo_lema, INK)

    lienzo.write_to_png(str(AQUI / "banner.png"))


if __name__ == "__main__":
    logo()
    marca_de_agua()
    banner()
    for nombre in ("logo.png", "banner.png", "marca_de_agua.png"):
        print(nombre, round((AQUI / nombre).stat().st_size / 1024), "KB")
