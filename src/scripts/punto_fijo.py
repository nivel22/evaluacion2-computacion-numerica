
def punto_fijo(funcion, valor_inicial, tolerancia, maximo_iteraciones):

    valor_actual = valor_inicial
    errores = []

    for iteracion in range(1, maximo_iteraciones + 1):

        siguiente_valor = funcion(valor_actual)

        error = abs(siguiente_valor - valor_actual)
        errores.append(error)

        if error < tolerancia:
            return siguiente_valor, iteracion, errores

        valor_actual = siguiente_valor

    print("No se alcanzo la tolerancia")
    return None, maximo_iteraciones, errores
