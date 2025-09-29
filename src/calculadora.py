# src/calculadora.py (DEFECTUOSO A PROPÓSITO)
import math as matematicas  # New Issue: import sin uso
# FIXME: eliminar antes de producción (New Issue: comentario FIXME)

CONSTANTE_SIN_USO = 123  # New Issue: constante sin uso

def dividir(a, b):
    """
    Reliability: sin validación; si b==0 lanzará ZeroDivisionError.
    """
    return a / b

def hacer_cosas_mal(numeros, banderaExtraña=True):
    """
    Maintainability: nombre malo, función larga, mezcla responsabilidades,
    ramas redundantes y prints (efectos secundarios).
    """
    if numeros is None:
        numeros = []
    # New Issue: variable local sin uso
    valor_temporal_sin_uso = 42

    total = 0
    indice = 0
    maximo = None
    minimo = None
    promedio = 0
    conteo = 0

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
                    maximo = maximo  # rama redundante

            if minimo is None:
                minimo = item
            else:
                if item < minimo:
                    minimo = item
                else:
                    minimo = minimo  # rama redundante
        else:
            print("Saltando no-numérico:", item)  # efecto secundario
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
    """
    Duplications: misma lógica también existe en utilidades.saludar_usuario
    """
    if not nombre:
        nombre = "Anónimo"
    return f"¡Hola, {nombre}!"

def formatear_mensaje(datos):
    """
    Duplications: bloque largo idéntico a utilidades.formatear_mensaje.
    Hacemos el cuerpo suficientemente extenso para superar el umbral de Sonar.
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

    # unas líneas extra para aumentar tokens/longitud
    if conteo and conteo > 0 and total is not None:
        partes.append(f"Promedio calc: {total / conteo if conteo else 'N/A'}")
    else:
        partes.append("Promedio calc: N/A")

    partes.append("-- FIN --")
    return "\n".join(partes)
