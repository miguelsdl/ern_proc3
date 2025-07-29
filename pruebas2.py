import logging
import ast
import re
import json


def escape_inner_apostrophes(s):
    """
    Escapa los apóstrofes internos en strings entre comillas simples.
    """
    def replacer(match):
        inner = match.group(1)
        # Solo escapamos apóstrofes simples que están en el medio del string
        escaped = inner.replace("'", "\\'")
        return f"'{escaped}'"

    # Este regex detecta contenidos entre comillas simples
    pattern = re.compile(r"'((?:[^'\\]|\\.)*)'")
    return pattern.sub(replacer, s)

def safe_parse(s):
    final = []
    try:
        # Paso 1: Reemplazo JS-style
        s = s.replace('true', 'True').replace('false', 'False').replace('null', "None")

        # Paso 2: Escapamos apóstrofes internos
        s = escape_inner_apostrophes(s)

        # Paso 3: Evaluación segura
        parsed = ast.literal_eval(s)

        # Paso 4: Convertimos a lista si es necesario
        if isinstance(parsed, (list, tuple)):
            final = list(parsed)
        else:
            final = [parsed]

    except Exception as e:
        logging.error("Error en safe_parse(), string original: {} Exception: {}".format(s, e))
        final = []

    return final

s = "('Children's Music', true, 430558)"
print(safe_parse(s))