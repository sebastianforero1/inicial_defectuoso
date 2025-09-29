# src/utilidades.py (duplica la lógica de saludo para gatillar "Duplications")

def saludar_usuario(nombre):
    if not nombre:
        nombre = "Anónimo"
    return f"¡Hola, {nombre}!"

def sumar_lista(numeros):
    total = 0
    for x in numeros:
        total += x
    return total
