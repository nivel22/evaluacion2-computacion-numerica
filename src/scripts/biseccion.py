
def biseccion(funcion, limite_inferior, limite_superior, tolerancia, maximo_iteraciones):
    valor_inferior = funcion(limite_inferior)
    valor_superior = funcion(limite_superior)

    if abs(valor_inferior) < tolerancia:
        return limite_inferior, 0, []

    if abs(valor_superior) < tolerancia:
        return limite_superior, 0, []

    if valor_inferior * valor_superior > 0:
        print("No hay cambio de signo en el intervalo")
        return None, 0, []

    errores = []
    raiz_anterior = limite_inferior

    for iteracion in range(1, maximo_iteraciones + 1):
        raiz = (limite_inferior + limite_superior) / 2
        valor_raiz = funcion(raiz)

        error = abs(raiz - raiz_anterior)
        errores.append(error)

        if abs(valor_raiz) < tolerancia:
            return raiz, iteracion, errores

        if error < tolerancia:
            return raiz, iteracion, errores

        if valor_inferior * valor_raiz < 0:
            limite_superior = raiz
            valor_superior = valor_raiz
        else:
            limite_inferior = raiz
            valor_inferior = valor_raiz

        raiz_anterior = raiz

    print("No se alcanzo la tolerancia")
    return None, maximo_iteraciones, errores
