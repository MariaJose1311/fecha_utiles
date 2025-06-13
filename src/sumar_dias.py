from datetime import timedelta
from fecha_utils.validar_fecha import convertir_fecha

def sumar_dias(fecha: str, dias: int, formato="%Y-%m-%d") -> str:
    """
    Suma una cantidad de días a una fecha.

    Args:
        fecha: Fecha en formato string.
        dias: Cantidad de días a sumar.
        formato: Formato de salida de la fecha.

    Returns:
        str: Fecha resultante en formato especificado.
    """
    fecha_inicial = convertir_fecha(fecha)
    fecha_final = fecha_inicial + timedelta(days=int(dias))
    return fecha_final.strftime(formato)