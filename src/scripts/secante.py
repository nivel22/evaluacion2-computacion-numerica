
def secante(funcion, valor_inicial, segundo_valor, tolerancia, maximo_iteraciones):

    valor_anterior = valor_inicial
    valor_actual = segundo_valor
    errores = []

    for iteracion in range(1, maximo_iteraciones + 1):

        resultado_anterior = funcion(valor_anterior)
        resultado_actual = funcion(valor_actual)

        denominador = resultado_actual - resultado_anterior

        if denominador == 0:
            print("No se puede dividir por cero")
            return None, iteracion, errores

        siguiente_valor = valor_actual - resultado_actual * (valor_actual - valor_anterior) / denominador

        error = abs(siguiente_valor - valor_actual)
        errores.append(error)

        if abs(funcion(siguiente_valor)) < tolerancia:
            return siguiente_valor, iteracion, errores

        if error < tolerancia:
            return siguiente_valor, iteracion, errores

        valor_anterior = valor_actual
        valor_actual = siguiente_valor

    return None, maximo_iteraciones, errores
