### Calcular días entre fechas

from fecha_utiles import dias_entre_fechas, sumar_dias, es_fin_de_semana

# Queremos calcular los días entre dos fechas dadas.
fecha1 = "2025-01-01"
fecha2 = "2025-11-30"
# Nota: Formato de fechas: Las funciones aceptan automáticamente fechas en formato `YYYY-MM-DD` o `DD-MM-YYYY`. Si el formato es incorrecto, se lanzará una excepción `FechaInvalidaError`.

# Realiza la operación para calcular la cantidad de días entre dos fechas
diferencia = dias_entre_fechas(fecha1, fecha2)
print(diferencia)  # 333

### Sumar días a una fecha

# Queremos sumar días a una fecha dada.
fecha_inicial = "2025-01-01"
cantidad_dias = 10

# Realiza la operación para calcular la fecha luego de los días deseados
fecha_final = sumar_dias(fecha_inicial, cantidad_dias)
print(fecha_final)  # "2025-01-11"

### Fin de semana

# Queremos saber si una fecha es sábado o domingo.
fecha_dada = "2025-01-01"

# Mediante booleanos, verifica si la fecha dada es fin de semana o no, devuelve True o False.
if es_fin_de_semana(fecha_dada):
    print(f"{fecha_dada} es fin de semana.")  # True
else:
    print(f"{fecha_dada} no es fin de semana.")  # False