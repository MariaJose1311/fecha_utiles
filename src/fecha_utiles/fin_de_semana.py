from fecha_utiles.validar_fecha import convertir_fecha

def es_fin_de_semana(fecha: str) -> bool:
    """
    Verifica si una fecha es sábado o domingo.

    Args:
        fecha: Fecha a verificar (como string en formato válido).

    Returns:
        bool: True si es fin de semana, False si no.
    """
    fecha_dada = convertir_fecha(fecha)
    return fecha_dada.weekday() >= 5  # 5 = sábado, 6 = domingo 