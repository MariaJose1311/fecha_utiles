# Fechas

Una librería Python que implementa diferentes tipos de actividades con fechas, como el cálculo de días entre dos fechas, sumar días a una fecha o saber si esa fecha es fin de semana.

## Instalación

```bash
pip install fechas_utils
```


## Características

### Calcular días entre fechas
- Realiza la resta entre dos fechas y nos dice cuántos días de diferencia hay entre ellas.

### Sumar días a una fecha
- Realiza la suma de una cantidad de días deseada a una fecha dada.

### Fin de semana
- Nos dice si una fecha dada es fin de semana (Sábado o Domingo).

## Estructura del Proyecto

```
fecha_utiles/
├── scripts/
│       ├── main.py
├── src/
│       ├── __init__.py
│       ├── calculo_dias.py
│       ├── fin_de_semana.py
│       └── sumar_dias.py
│       └── validar_fecha.py
├── tests/
│   └── test_fechas.py
├── setup.py
├── requirements.txt
└── README.md
```

## Uso

### Calcular días entre fechas
```python

from fecha_utils import dias_entre_fechas

# Queremos calcular los días entre dos fechas dadas.

# El usuario escribe las dos fechas
fecha1 = "2025-01-01"
fecha2 = "2025-11-30"
# Nota: Formato de fechas: Las funciones aceptan automáticamente fechas en formato `YYYY-MM-DD` o `DD-MM-YYYY`. Si el formato es incorrecto, se lanzará una excepción `FechaInvalidaError`.

# Realiza la operación para calcular la cantidad de días entre dos fechas
diferencia = dias_entre_fechas(fecha1, fecha2)
print(diferencia)  # 333
```

### Sumar días a una fecha
```python
from fechas_utils import sumar_dias

#Queremos sumar días a una fecha dada.


# El usuario escribe la fecha y la cantidad de días que quiere sumarle
fecha_inicial = "2025-01-01"
cantidad_dias = 10
# Nota: Formato de fechas: Las funciones aceptan automáticamente fechas en formato `YYYY-MM-DD` o `DD-MM-YYYY`. Si el formato es incorrecto, se lanzará una excepción `FechaInvalidaError`.

# Realiza la operación para calcular la fecha luego de los días deseados
fecha_final = sumar_dias("2025-01-01", 10)
print(fecha_final)  # "2025-01-11"
```

### Fin de semana
```python
from fecha_utils import es_fin_de_semana

# Queremos saber si una fecha es sábado o domingo.

# El usuario escribe la fecha
fecha_dada = "2025-01-01"
# Nota: Formato de fechas: Las funciones aceptan automáticamente fechas en formato `YYYY-MM-DD` o `DD-MM-YYYY`. Si el formato es incorrecto, se lanzará una excepción `FechaInvalidaError`.

# Mediante booleanos, verifica si la fecha dada es fin de semana o no, devuelve True o False.
if es_fin_de_semana(fecha_dada):
    print(f"{fecha_dada} es fin de semana.")  # True
else:
    print(f"{fecha_dada} no es fin de semana.")  # False
    #Retorna False
```

## Desarrollo

1. Clona este repositorio
2. Crea un entorno virtual:
   ```bash
   python -m venv fecha_utils_env
   .\fecha_utils_env\Scripts\activate  
   ```
3. Instala las dependencias de desarrollo:
   ```bash
   pip install -r requirements.txt
   ```
4. Instala el paquete en modo desarrollo:
   ```bash
   pip install -e .
   ```

## Ejecutar Pruebas

```bash
python -m unittest tests/test_fechas.py
```

## Buenas Prácticas Implementadas

1. **Programación Orientada a Objetos**: Uso de herencia y clases abstractas
2. **Modularidad**: Separación de responsabilidades en módulos
3. **Documentación**: Docstrings detallados para clases y métodos
4. **Tipado**: Uso de type hints para mejor mantenibilidad
5. **Pruebas**: Cobertura completa de pruebas unitarias
6. **Manejo de Errores**: Validación de entrada y manejo de excepciones
7. **Encapsulamiento**: Uso de propiedades para acceso controlado
8. **Código Limpio**: Nombres descriptivos y estructura clara

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.