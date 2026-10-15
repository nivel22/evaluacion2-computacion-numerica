
import math


def punto_fijo(funcion, valor_inicial, tolerancia, maximo_iteraciones):
    valor_actual = valor_inicial
    errores = []

    for iteracion in range(1, maximo_iteraciones + 1):
        try:
            siguiente_valor = funcion(valor_actual)

            if not math.isfinite(siguiente_valor):
                return None, iteracion, errores

            error = abs(siguiente_valor - valor_actual)

            if not math.isfinite(error):
                return None, iteracion, errores

        except (ValueError, OverflowError, ZeroDivisionError, TypeError):
            return None, iteracion, errores

        errores.append(error)

        if error < tolerancia:
            return siguiente_valor, iteracion, errores

        valor_actual = siguiente_valor

    print("No se alcanzo la tolerancia")
    return None, maximo_iteraciones, errores
