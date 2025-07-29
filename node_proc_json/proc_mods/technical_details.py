# ¡OJO!: este metodo no tiene self porque no se llama directamente en _case_filter,
# sino que se llama desde sound_recording.

def technical_details(data, **kwargs):
    """Procesa el nodo TechnicalDetails, devolviendo un dict por TechnicalResourceDetailsReference."""
    items = data if isinstance(data, list) else [data]
    result = {}

    for entry in items:
        ref = entry.get("TechnicalResourceDetailsReference")
        if ref:
            result[ref] = entry

    return result