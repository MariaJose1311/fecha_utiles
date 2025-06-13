from fecha_utiles.validar_fecha import convertir_fecha

def dias_entre_fechas(fecha1: str, fecha2: str, formato="%Y-%m-%d"):
    """
    Calcula la cantidad de días entre dos fechas.

    Args:
        fecha1 (str): Fecha inicial en formato string.
        fecha2 (str): Fecha final en formato string.
        formato (str): Formato de entrada de las fechas. Por defecto "%Y-%m-%d".

    Returns:
        int: Días de diferencia entre ambas fechas.
    """
    f1 = convertir_fecha(fecha1)
    f2 = convertir_fecha(fecha2)
    diferencia = abs((f2 - f1).days)
    return diferencia