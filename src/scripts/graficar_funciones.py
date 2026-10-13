
import numpy as np
import matplotlib.pyplot as plt

from funciones import polinomica_simple
from funciones import polinomica_doble
from funciones import logaritmica
from funciones import exponencial
from funciones import trigonometrica
from funciones import mixta


nombres = [
    "polinomica_simple",
    "polinomica_doble",
    "logaritmica",
    "exponencial",
    "trigonometrica",
    "mixta"
]

funciones = [
    polinomica_simple,
    polinomica_doble,
    logaritmica,
    exponencial,
    trigonometrica,
    mixta
]

limites_inferiores = [1, 1.2, 2, 0, 0, 0.1]
limites_superiores = [2, 2.8, 3, 1, 1, 1]

raices = [
    1.5213797068,
    2,
    2.9262710624,
    0.5671432904,
    0.7390851332,
    0.6417143709
]


for numero in range(6):

    nombre = nombres[numero]
    funcion = funciones[numero]

    limite_inferior = limites_inferiores[numero]
    limite_superior = limites_superiores[numero]
    raiz = raices[numero]

    valores_x = np.linspace(limite_inferior, limite_superior, 200)
    valores_y = funcion(valores_x)

    plt.figure(figsize=(8, 5))

    plt.plot(valores_x, valores_y, label="f(x)")
    plt.axhline(0, color="black", linewidth=1)

    plt.plot(
        raiz,
        funcion(raiz),
        "ro",
        label="Raiz"
    )

    plt.title("Funcion " + nombre.replace("_", " "))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)

    nombre_archivo = "src/assets/" + nombre + ".png"

    plt.savefig(nombre_archivo)
    plt.close()

    print("Grafico generado:", nombre_archivo)


print()
print("Se generaron los seis graficos")
