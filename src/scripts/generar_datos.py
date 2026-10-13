
import csv
import numpy as np

from funciones import polinomica_simple
from funciones import polinomica_doble
from funciones import logaritmica
from funciones import exponencial
from funciones import trigonometrica
from funciones import mixta


def guardar_datos(nombre_archivo, funcion, limite_inferior, limite_superior):

    valores = np.linspace(limite_inferior, limite_superior, 100)

    with open(nombre_archivo, "w", newline="") as archivo:

        escribir = csv.writer(archivo)
        escribir.writerow(["x", "f(x)"])

        for valor in valores:
            resultado = funcion(valor)
            escribir.writerow([valor, resultado])

    print("Archivo generado:", nombre_archivo)


guardar_datos(
    "src/data/polinomica_simple.csv",
    polinomica_simple,
    1,
    2
)

guardar_datos(
    "src/data/polinomica_doble.csv",
    polinomica_doble,
    1.2,
    2.8
)

guardar_datos(
    "src/data/logaritmica.csv",
    logaritmica,
    2,
    3
)

guardar_datos(
    "src/data/exponencial.csv",
    exponencial,
    0,
    1
)

guardar_datos(
    "src/data/trigonometrica.csv",
    trigonometrica,
    0,
    1
)

guardar_datos(
    "src/data/mixta.csv",
    mixta,
    0.1,
    1
)
