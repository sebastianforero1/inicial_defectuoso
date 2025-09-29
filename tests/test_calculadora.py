# tests/test_calculadora.py (mínimo para dejar cobertura baja)

from src.calculadora import saludar_usuario

def test_saludar_usuario():
    assert saludar_usuario("Sebas") == "¡Hola, Sebas!"
