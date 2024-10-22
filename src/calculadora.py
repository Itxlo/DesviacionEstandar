import math

class NoSePuedeCalcular(Exception):
    pass

def calcular_promedio(elementos):
    if not elementos:
        raise NoSePuedeCalcular("Lista vacía.")
    if any(not isinstance(x, (int, float)) for x in elementos):
        raise TypeError("Todos los elementos deben ser numéricos.")
    return sum(elementos) / len(elementos)

def calcular_desviacion_estandar(elementos):
    if not elementos:
        raise NoSePuedeCalcular("Lista vacía.")
    if any(not isinstance(x, (int, float)) for x in elementos):
        raise TypeError("Todos los elementos deben ser numéricos.")
    if len(elementos) == 1:
        return 0
    promedio = calcular_promedio(elementos)
    varianza = sum((x - promedio) ** 2 for x in elementos) / len(elementos)  # División entre n (población)
    return math.sqrt(varianza)


