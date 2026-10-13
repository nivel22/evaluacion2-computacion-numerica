
import csv

from funciones import *
from biseccion import biseccion
from falsa_posicion import falsa_posicion
from punto_fijo import punto_fijo
from secante import secante
from newton_raphson import newton_raphson
from newton_mejorado import newton_mejorado


tolerancia = 0.000001
maximo_iteraciones = 100

nombres = [
    "Polinomica simple",
    "Polinomica doble",
    "Logaritmica",
    "Exponencial",
    "Trigonometrica",
    "Mixta"
]

funciones = [
    polinomica_simple,
    polinomica_doble,
    logaritmica,
    exponencial,
    trigonometrica,
    mixta
]

derivadas = [
    derivada_polinomica_simple,
    derivada_polinomica_doble,
    derivada_logaritmica,
    derivada_exponencial,
    derivada_trigonometrica,
    derivada_mixta
]

segundas_derivadas = [
    segunda_derivada_polinomica_simple,
    segunda_derivada_polinomica_doble,
    segunda_derivada_logaritmica,
    segunda_derivada_exponencial,
    segunda_derivada_trigonometrica,
    segunda_derivada_mixta
]

funciones_punto_fijo = [
    punto_fijo_polinomica_simple,
    punto_fijo_polinomica_doble,
    punto_fijo_logaritmica,
    punto_fijo_exponencial,
    punto_fijo_trigonometrica,
    punto_fijo_mixta
]

limites_inferiores = [1, 1.2, 2, 0, 0, 0.1]
limites_superiores = [2, 2.5, 3, 1, 1, 1]

valores_iniciales = [1.5, 1.2, 2.5, 0.5, 0.5, 0.5]
segundos_valores = [2, 2.5, 3, 1, 1, 1]


with open("src/data/resumen_convergencia.csv", "w", newline="") as archivo:

    escribir = csv.writer(archivo)

    escribir.writerow([
        "Funcion",
        "Metodo",
        "Iteraciones",
        "Raiz",
        "Error",
        "Valor_funcion",
        "Estado"
    ])

    for numero in range(6):

        nombre = nombres[numero]
        funcion = funciones[numero]
        derivada = derivadas[numero]
        segunda_derivada = segundas_derivadas[numero]
        funcion_punto_fijo = funciones_punto_fijo[numero]

        limite_inferior = limites_inferiores[numero]
        limite_superior = limites_superiores[numero]
        valor_inicial = valores_iniciales[numero]
        segundo_valor = segundos_valores[numero]

        print()
        print("Funcion:", nombre)

        if funcion(limite_inferior) * funcion(limite_superior) < 0:

            raiz, iteraciones, errores = biseccion(
                funcion,
                limite_inferior,
                limite_superior,
                tolerancia,
                maximo_iteraciones
            )

            if raiz is not None:
                error = errores[-1]
                valor_funcion = abs(funcion(raiz))

                if error < tolerancia or valor_funcion < tolerancia:
                    estado = "Convergencia"
                else:
                    estado = "No convergio"
            else:
                error = ""
                valor_funcion = ""
                estado = "No convergio"

            escribir.writerow([
                nombre, "Biseccion", iteraciones, raiz,
                error, valor_funcion, estado
            ])

            raiz, iteraciones, errores = falsa_posicion(
                funcion,
                limite_inferior,
                limite_superior,
                tolerancia,
                maximo_iteraciones
            )

            if raiz is not None:
                error = errores[-1] if errores else ""
                valor_funcion = abs(funcion(raiz))

                if error != "" and (error < tolerancia or valor_funcion < tolerancia):
                    estado = "Convergencia"
                else:
                    estado = "No convergio"
            else:
                error = ""
                valor_funcion = ""
                estado = "No convergio"

            escribir.writerow([
                nombre, "Falsa posicion", iteraciones, raiz,
                error, valor_funcion, estado
            ])

        else:

            escribir.writerow([
                nombre, "Biseccion", 0, "", "", "", "No aplica"
            ])

            escribir.writerow([
                nombre, "Falsa posicion", 0, "", "", "", "No aplica"
            ])

        raiz, iteraciones, errores = punto_fijo(
            funcion_punto_fijo,
            valor_inicial,
            tolerancia,
            maximo_iteraciones
        )

        if raiz is not None:
            error = errores[-1]
            valor_funcion = abs(funcion(raiz))
            estado = "Convergencia"
        else:
            error = errores[-1] if errores else ""
            valor_funcion = ""
            estado = "No convergio"

        escribir.writerow([
            nombre, "Punto fijo", iteraciones, raiz,
            error, valor_funcion, estado
        ])

        raiz, iteraciones, errores = secante(
            funcion,
            valor_inicial,
            segundo_valor,
            tolerancia,
            maximo_iteraciones
        )

        if raiz is not None:
            error = errores[-1] if errores else ""
            valor_funcion = abs(funcion(raiz))

            if error != "" and (error < tolerancia or valor_funcion < tolerancia):
                estado = "Convergencia"
            else:
                estado = "No convergio"
        else:
            error = ""
            valor_funcion = ""
            estado = "No convergio"

        escribir.writerow([
            nombre, "Secante", iteraciones, raiz,
            error, valor_funcion, estado
        ])

        raiz, iteraciones, errores = newton_raphson(
            funcion,
            derivada,
            valor_inicial,
            tolerancia,
            maximo_iteraciones
        )

        if raiz is not None:
            error = errores[-1] if errores else ""
            valor_funcion = abs(funcion(raiz))

            if error != "" and (error < tolerancia or valor_funcion < tolerancia):
                estado = "Convergencia"
            else:
                estado = "No convergio"
        else:
            error = ""
            valor_funcion = ""
            estado = "No convergio"

        escribir.writerow([
            nombre, "Newton-Raphson", iteraciones, raiz,
            error, valor_funcion, estado
        ])

        raiz, iteraciones, errores = newton_mejorado(
            funcion,
            derivada,
            segunda_derivada,
            valor_inicial,
            tolerancia,
            maximo_iteraciones
        )

        if raiz is not None:
            error = errores[-1] if errores else ""
            valor_funcion = abs(funcion(raiz))

            if error != "" and (error < tolerancia or valor_funcion < tolerancia):
                estado = "Convergencia"
            else:
                estado = "No convergio"
        else:
            error = ""
            valor_funcion = ""
            estado = "No convergio"

        escribir.writerow([
            nombre, "Newton mejorado", iteraciones, raiz,
            error, valor_funcion, estado
        ])

        print("Resultados guardados")


print()
print("Archivo generado: src/data/resumen_convergencia.csv")
