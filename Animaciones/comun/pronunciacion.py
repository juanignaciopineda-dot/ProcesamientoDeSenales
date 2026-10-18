"""Reemplazos que solo afectan al audio (no a los subtítulos ni al guion).

Solo va aquí lo que el usuario eligió de oído (ver voces_prueba/). No
inventar grafías "fonéticas" sin probarlas: a veces suenan peor que la
palabra original (en Programación Concurrente pasó con "softgüer").

Las fórmulas NO van aquí: la narración del guion ya las escribe en palabras
(«R sub equis equis de tau»), ver README §9.

Aprobado tal cual, sin reemplazo: (todavía nada).
Con fonemas (elegido de oído, voces_prueba/probar_fourier_ipa.py, variante 5): Fourier → «fu-ri-ér».
Las grafías «Furiér» y «Fuhriér» se descartaron.

Reemplazado (elegido de oído, voces_prueba/probar_bayes.py, variante 5): Bayes → «Báyes».
Reemplazado (elegido de oído, voces_prueba/probar_bernoulli.py, variante 3): Bernoulli → «Bernulí».
Reemplazado (elegido de oído, voces_prueba/probar_cauchy.py, variante 3): Cauchy-Schwarz → «Coshi-Shuarts».
Narración (no reemplazo): «u y v» se escribe «la u y la ve» (voces_prueba/probar_u_ve.py, variante 2).

Cambiar un reemplazo cambia el texto que se sintetiza: solo esas frases se
vuelven a generar (el caché de audio se indexa por el texto).
"""
import re

# (patrón, reemplazo). Se aplican en orden, sin distinguir mayúsculas.
REEMPLAZOS: list[tuple[str, str]] = [
    (r"\bBayes\b", "Báyes"),   # variante 5 de voces_prueba/probar_bayes.py
    (r"\bBernoulli\b", "Bernulí"),   # variante 3 de voces_prueba/probar_bernoulli.py
    (r"\bCauchy-Schwarz\b", "Coshi-Shuarts"),   # variante 3 de voces_prueba/probar_cauchy.py
]

# palabra -> fonemas IPA. La palabra queda igual en el texto (y en los límites
# de palabra); solo Azure Speech la pronuncia así (edge-tts no acepta SSML).
FONEMAS: dict[str, str] = {
    "Fourier": "fu.ɾiˈeɾ",   # variante 5 de voces_prueba/probar_fourier_ipa.py
}


def fonemas_en(texto: str) -> dict[str, str]:
    """Los fonemas que le tocan a un texto (entran en la clave del caché de audio)."""
    return {p: f for p, f in FONEMAS.items() if re.search(rf"\b{p}\b", texto, flags=re.IGNORECASE)}


def con_fonemas(texto_escapado: str) -> str:
    """Envuelve en <phoneme> las palabras de FONEMAS de un texto ya escapado para SSML."""
    for palabra, fonemas in FONEMAS.items():
        texto_escapado = re.sub(
            rf"\b{palabra}\b",
            lambda m, f=fonemas: f'<phoneme alphabet="ipa" ph="{f}">{m.group()}</phoneme>',
            texto_escapado, flags=re.IGNORECASE)
    return texto_escapado


def aplicar(texto: str) -> str:
    """Aplica los reemplazos de pronunciación a un texto de narración."""
    for patron, reemplazo in REEMPLAZOS:
        texto = re.sub(patron, reemplazo, texto, flags=re.IGNORECASE)
    return texto
