
import csv

from funciones import polinomica_simple
from funciones import derivada_polinomica_simple

from biseccion import biseccion
from newton_raphson import newton_raphson


tolerancia = 0.000001
maximo_iteraciones = 100

resultados = []

print("Experimento de valores iniciales")
print("Funcion: x**3 - x - 2")
print("Tolerancia:", tolerancia)

print()
print("Metodo de biseccion")

limites_inferiores = [1, 1.4, 1.5]
limites_superiores = [2, 1.6, 1.55]

for numero in range(3):

    limite_inferior = limites_inferiores[numero]
    limite_superior = limites_superiores[numero]

    valor_inferior = polinomica_simple(limite_inferior)
    valor_superior = polinomica_simple(limite_superior)

    if valor_inferior * valor_superior < 0:

        raiz, iteraciones, errores = biseccion(
            polinomica_simple,
            limite_inferior,
            limite_superior,
            tolerancia,
            maximo_iteraciones
        )

        print()
        print("Intervalo:", limite_inferior, limite_superior)
        print("Raiz:", raiz)
        print("Iteraciones:", iteraciones)
        print("Valor de la funcion:", abs(polinomica_simple(raiz)))

        resultados.append([
            "Biseccion",
            limite_inferior,
            limite_superior,
            iteraciones,
            raiz,
            abs(polinomica_simple(raiz))
        ])

    else:
        print("No existe cambio de signo")


print()
print("Metodo de Newton-Raphson")

valores_iniciales = [1, 1.5, 2]

for valor_inicial in valores_iniciales:

    raiz, iteraciones, errores = newton_raphson(
        polinomica_simple,
        derivada_polinomica_simple,
        valor_inicial,
        tolerancia,
        maximo_iteraciones
    )

    print()
    print("Valor inicial:", valor_inicial)
    print("Raiz:", raiz)
    print("Iteraciones:", iteraciones)

    if raiz is not None:

        valor_funcion = abs(polinomica_simple(raiz))
        print("Valor de la funcion:", valor_funcion)

        resultados.append([
            "Newton-Raphson",
            valor_inicial,
            "",
            iteraciones,
            raiz,
            valor_funcion
        ])

    else:
        print("No se encontro la raiz")


with open("src/data/experimentos.csv", "w", newline="") as archivo:

    escribir = csv.writer(archivo)

    escribir.writerow([
        "Metodo",
        "Valor_inicial_o_limite_inferior",
        "Limite_superior",
        "Iteraciones",
        "Raiz",
        "Valor_funcion"
    ])

    for resultado in resultados:
        escribir.writerow(resultado)


print()
print("Archivo generado: src/data/experimentos.csv")
