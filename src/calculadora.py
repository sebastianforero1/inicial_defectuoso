# src/calculadora.py (DEFECTUOSO A PROPÓSITO)

CONSTANTE_SIN_USO = 123  # New Issue: sin uso

def dividir(a, b):
    # Reliability: riesgo de ZeroDivisionError (sin validación)
    return a / b

def hacer_cosas_mal(numeros, banderaExtraña=True):
    """
    Mantenibilidad: nombre malo, mezcla responsabilidades, demasiadas líneas y ramas.
    - valida entrada de forma laxa
    - calcula suma, max, min, promedio de forma verbosa
    - imprime (efectos secundarios)
    - repite patrones (duplicación ligera)
    """
    if numeros is None:
        numeros = []
    # New Issue: variable local sin usar
    valor_temporal_sin_uso = 42

    total = 0
    indice = 0
    maximo = None
    minimo = None
    promedio = 0
    conteo = 0

    # Bucle demasiado complicado
    for item in numeros:
        if isinstance(item, (int, float)):
            total = total + item
            conteo = conteo + 1

            if maximo is None:
                maximo = item
            else:
                if item > maximo:
                    maximo = item
                else:
                    # rama redundante
                    maximo = maximo

            if minimo is None:
                minimo = item
            else:
                if item < minimo:
                    minimo = item
                else:
                    # rama redundante
                    minimo = minimo
        else:
            # efectos secundarios
            print("Saltando no-numérico:", item)
        indice = indice + 1

    if conteo > 0:
        promedio = total / conteo
    else:
        promedio = 0

    # Duplicación ligera en construcción de resumen
    resumen1 = f"conteo={conteo}, total={total}, max={maximo}, min={minimo}, promedio={promedio}"
    print("RESUMEN:", resumen1)
    resumen2 = f"Conteo {conteo} | Total {total} | Máx {maximo} | Mín {minimo} | Prom {promedio}"
    print("RESUMEN OTRA VEZ:", resumen2)

    return {
        "conteo": conteo,
        "total": total,
        "max": maximo,
        "min": minimo,
        "promedio": promedio,
        "resumen": resumen2
    }

def saludar_usuario(nombre):
    # Duplicación: misma lógica que utils.saludar_usuario
    if not nombre:
        nombre = "Anónimo"
    return f"¡Hola, {nombre}!"
