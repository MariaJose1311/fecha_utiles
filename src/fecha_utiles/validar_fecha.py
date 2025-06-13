from datetime import datetime

class FechaInvalidaError(Exception):
    """Excepción personalizada para errores en formato de fecha."""
    pass

def convertir_fecha(fecha_str: str) -> datetime:
    """
    Convierte un string de fecha a objeto datetime, aceptando múltiples formatos.

    Args:
        fecha_str (str): La fecha en formato string.

    Returns:
        datetime: Fecha convertida correctamente.

    Raises:
        FechaInvalidaError: Si ningún formato coincide.
    """
    formatos = ["%Y-%m-%d", "%d-%m-%Y"]
    for fmt in formatos:
        try:
            return datetime.strptime(fecha_str, fmt)
        except ValueError:
            continue
    raise FechaInvalidaError(f"Formato de fecha inválido: '{fecha_str}'")