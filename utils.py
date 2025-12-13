"""Funciones de utilidad y validación."""
from typing import Any, Union


def validar_numero(min_val: int, max_val: int, prompt: str) -> int:
    """Valida entrada numérica con rango específico."""
    while True:
        try:
            valor = int(input(prompt))
            if min_val <= valor <= max_val:
                return valor
            print(f"❌ Debe estar entre {min_val} y {max_val}")
        except ValueError:
            print("❌ Ingrese un número válido")


def validar_confirmacion(prompt: str = "¿Confirmar? (s/n): ") -> bool:
    """Valida confirmación sí/no con respuestas múltiples."""
    while True:
        respuesta = input(prompt).strip().lower()
        if respuesta in ['s', 'si', 'y', 'yes', 'sí']:
            return True
        elif respuesta in ['n', 'no']:
            return False
        print("❌ Ingrese 's' (sí) o 'n' (no)")


def formatear_precio(precio: float) -> str:
    """Formatea precio con separadores de miles."""
    return f"${precio:,.0f}"


def mostrar_banner(titulo: str) -> None:
    """Muestra banner formateado."""
    print("\n" + "="*50)
    print(titulo.center(50))
    print("="*50)
