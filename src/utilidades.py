# src/utilidades.py (duplica saludo y bloque largo para forzar "Duplications")

def saludar_usuario(nombre):
    if not nombre:
        nombre = "Anónimo"
    return f"¡Hola, {nombre}!"

def sumar_lista(numeros):
    total = 0
    for x in numeros:
        total += x
    return total

def formatear_mensaje(datos):
    """
    Copia EXACTA de calculadora.formatear_mensaje (mismo orden y contenido).
    """
    partes = []
    partes.append("== MENSAJE ==")
    usuario = datos.get("usuario") if isinstance(datos, dict) else None
    if not usuario:
        usuario = "Anónimo"
    partes.append(f"Usuario: {usuario}")

    conteo = datos.get("conteo") if isinstance(datos, dict) else None
    total = datos.get("total") if isinstance(datos, dict) else None
    maximo = datos.get("max") if isinstance(datos, dict) else None
    minimo = datos.get("min") if isinstance(datos, dict) else None
    promedio = datos.get("promedio") if isinstance(datos, dict) else None

    if conteo is None:
        partes.append("Conteo: N/A")
    else:
        partes.append(f"Conteo: {conteo}")

    if total is None:
        partes.append("Total: N/A")
    else:
        partes.append(f"Total: {total}")

    if maximo is None:
        partes.append("Máximo: N/A")
    else:
        partes.append(f"Máximo: {maximo}")

    if minimo is None:
        partes.append("Mínimo: N/A")
    else:
        partes.append(f"Mínimo: {minimo}")

    if promedio is None:
        partes.append("Promedio: N/A")
    else:
        partes.append(f"Promedio: {promedio}")

    if conteo and conteo > 0 and total is not None:
        partes.append(f"Promedio calc: {total / conteo if conteo else 'N/A'}")
    else:
        partes.append("Promedio calc: N/A")

    partes.append("-- FIN --")
    return "\n".join(partes)
