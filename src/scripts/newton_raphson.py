import math


def newton_raphson(funcion, derivada, valor_inicial, tolerancia, maximo_iteraciones):
    valor_actual = valor_inicial
    errores = []

    for iteracion in range(1, maximo_iteraciones + 1):
        try:
            resultado = funcion(valor_actual)

            if not math.isfinite(resultado):
                return None, iteracion, errores

            if abs(resultado) < tolerancia:
                return valor_actual, iteracion - 1, errores

            resultado_derivada = derivada(valor_actual)

            if not math.isfinite(resultado_derivada):
                return None, iteracion, errores

            if resultado_derivada == 0:
                print("No se puede dividir por cero")
                return None, iteracion, errores

            siguiente_valor = valor_actual - resultado / resultado_derivada

            if not math.isfinite(siguiente_valor):
                return None, iteracion, errores

            error = abs(siguiente_valor - valor_actual)
            errores.append(error)

            if abs(funcion(siguiente_valor)) < tolerancia:
                return siguiente_valor, iteracion, errores

            if error < tolerancia:
                return siguiente_valor, iteracion, errores

            valor_actual = siguiente_valor

        except (ValueError, OverflowError, ZeroDivisionError, TypeError):
            return None, iteracion, errores

    return None, maximo_iteraciones, errores