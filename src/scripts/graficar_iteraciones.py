
import csv
import numpy as np
import matplotlib.pyplot as plt


nombres_funciones = [
    "Polinomica simple",
    "Polinomica doble",
    "Logaritmica",
    "Exponencial",
    "Trigonometrica",
    "Mixta"
]

nombres_metodos = [
    "Biseccion",
    "Falsa posicion",
    "Punto fijo",
    "Secante",
    "Newton-Raphson",
    "Newton mejorado"
]

datos = []

with open("src/data/resumen_convergencia.csv", "r") as archivo:
    leer = csv.DictReader(archivo)

    for fila in leer:
        datos.append(fila)


posiciones = np.arange(6)
ancho_barra = 0.13

plt.figure(figsize=(13, 6))

for numero_metodo in range(6):

    metodo = nombres_metodos[numero_metodo]
    iteraciones = []
    estados = []

    for numero_funcion in range(6):

        nombre = nombres_funciones[numero_funcion]
        cantidad = 0
        estado = "No aplica"

        for fila in datos:

            if fila["Funcion"] == nombre and fila["Metodo"] == metodo:

                if fila["Iteraciones"] != "":
                    cantidad = int(fila["Iteraciones"])

                estado = fila["Estado"]
                break

        iteraciones.append(cantidad)
        estados.append(estado)

    posicion_barras = posiciones + (numero_metodo - 2.5) * ancho_barra

    plt.bar(
        posicion_barras,
        iteraciones,
        ancho_barra,
        label=metodo
    )

    for numero_funcion in range(6):

        if estados[numero_funcion] == "No convergio":
            plt.text(
                posicion_barras[numero_funcion],
                iteraciones[numero_funcion] + 2,
                "NC",
                ha="center",
                fontsize=8
            )


plt.xticks(
    posiciones,
    ["Pol. simple", "Pol. doble", "Logaritmica",
     "Exponencial", "Trigonometrica", "Mixta"],
    rotation=15
)

plt.xlabel("Funciones")
plt.ylabel("Iteraciones")
plt.title("Comparacion de iteraciones por metodo")
plt.ylim(0, 115)
plt.legend()
plt.grid(True, axis="y")
plt.tight_layout()

plt.savefig("src/assets/comparacion_iteraciones.png")
plt.close()

print("Grafico generado: src/assets/comparacion_iteraciones.png")
print("NC significa que el metodo no convergio")
