
def newton_raphson(funcion, derivada, valor_inicial, tolerancia, maximo_iteraciones):

    valor_actual = valor_inicial
    errores = []

    for iteracion in range(1, maximo_iteraciones + 1):

        resultado = funcion(valor_actual)
        resultado_derivada = derivada(valor_actual)

        if resultado_derivada == 0:
            print("No se puede dividir por cero")
            return None, iteracion, errores

        siguiente_valor = valor_actual - resultado / resultado_derivada

        error = abs(siguiente_valor - valor_actual)
        errores.append(error)

        if abs(funcion(siguiente_valor)) < tolerancia:
            return siguiente_valor, iteracion, errores

        if error < tolerancia:
            return siguiente_valor, iteracion, errores

        valor_actual = siguiente_valor

    return valor_actual, maximo_iteraciones, errores
