import matplotlib.pyplot as plt

from biseccion import biseccion
from falsa_posicion import falsa_posicion
from punto_fijo import punto_fijo
from secante import secante
from newton_raphson import newton_raphson
from newton_mejorado import newton_mejorado

from funciones import (
    polinomica_simple,
    polinomica_doble,
    logaritmica,
    exponencial,
    trigonometrica,
    mixta,
    derivada_polinomica_simple,
    derivada_polinomica_doble,
    derivada_logaritmica,
    derivada_exponencial,
    derivada_trigonometrica,
    derivada_mixta,
    segunda_derivada_polinomica_simple,
    segunda_derivada_polinomica_doble,
    segunda_derivada_logaritmica,
    segunda_derivada_exponencial,
    segunda_derivada_trigonometrica,
    segunda_derivada_mixta,
    punto_fijo_polinomica_simple,
    punto_fijo_polinomica_doble,
    punto_fijo_logaritmica,
    punto_fijo_exponencial,
    punto_fijo_trigonometrica,
    punto_fijo_mixta
)

tolerancia = 1e-6
maximo_iteraciones = 100


def guardar_grafico_convergencia(nombre_archivo, titulo, nombres_metodos, errores_metodos):
    plt.figure(figsize=(8, 5))

    se_dibujo_alguna_curva = False

    for indice in range(len(nombres_metodos)):
        nombre_metodo = nombres_metodos[indice]
        errores = errores_metodos[indice]

        if len(errores) > 0:
            iteraciones = list(range(1, len(errores) + 1))
            plt.plot(iteraciones, errores, marker="o", label=nombre_metodo)
            se_dibujo_alguna_curva = True

    if se_dibujo_alguna_curva:
        plt.yscale("log")
        plt.title(titulo)
        plt.xlabel("Iteracion")
        plt.ylabel("Error absoluto")
        plt.grid(True)
        plt.legend()
        plt.savefig(nombre_archivo)
        plt.close()
        print("Grafico generado:", nombre_archivo)
    else:
        print("No se pudo generar:", nombre_archivo)


def agregar_resultado(nombre_metodo, errores, nombres_metodos, errores_metodos):
    if errores is not None and len(errores) > 0:
        nombres_metodos.append(nombre_metodo)
        errores_metodos.append(errores)


def procesar_funcion(
    nombre_funcion,
    funcion,
    derivada,
    segunda_derivada,
    funcion_punto_fijo,
    limite_inferior,
    limite_superior,
    valor_inicial,
    segundo_valor
):
    print()
    print("Procesando funcion:", nombre_funcion)

    nombres_metodos = []
    errores_metodos = []

    if funcion(limite_inferior) * funcion(limite_superior) < 0:
        raiz, iteraciones, errores = biseccion(
            funcion,
            limite_inferior,
            limite_superior,
            tolerancia,
            maximo_iteraciones
        )
        agregar_resultado("Biseccion", errores, nombres_metodos, errores_metodos)

        raiz, iteraciones, errores = falsa_posicion(
            funcion,
            limite_inferior,
            limite_superior,
            tolerancia,
            maximo_iteraciones
        )
        agregar_resultado("Falsa posicion", errores, nombres_metodos, errores_metodos)
    else:
        print("Biseccion y falsa posicion no aplican por falta de cambio de signo")

    raiz, iteraciones, errores = punto_fijo(
        funcion_punto_fijo,
        valor_inicial,
        tolerancia,
        maximo_iteraciones
    )
    agregar_resultado("Punto fijo", errores, nombres_metodos, errores_metodos)

    raiz, iteraciones, errores = secante(
        funcion,
        valor_inicial,
        segundo_valor,
        tolerancia,
        maximo_iteraciones
    )
    agregar_resultado("Secante", errores, nombres_metodos, errores_metodos)

    raiz, iteraciones, errores = newton_raphson(
        funcion,
        derivada,
        valor_inicial,
        tolerancia,
        maximo_iteraciones
    )
    agregar_resultado("Newton-Raphson", errores, nombres_metodos, errores_metodos)

    raiz, iteraciones, errores = newton_mejorado(
        funcion,
        derivada,
        segunda_derivada,
        valor_inicial,
        tolerancia,
        maximo_iteraciones
    )
    agregar_resultado("Newton mejorado", errores, nombres_metodos, errores_metodos)

    nombre_archivo = "src/assets/convergencia_" + nombre_funcion + ".png"
    titulo = "Convergencia - " + nombre_funcion.replace("_", " ")

    guardar_grafico_convergencia(
        nombre_archivo,
        titulo,
        nombres_metodos,
        errores_metodos
    )


procesar_funcion(
    "polinomica_simple",
    polinomica_simple,
    derivada_polinomica_simple,
    segunda_derivada_polinomica_simple,
    punto_fijo_polinomica_simple,
    1,
    2,
    1.5,
    2
)

procesar_funcion(
    "polinomica_doble",
    polinomica_doble,
    derivada_polinomica_doble,
    segunda_derivada_polinomica_doble,
    punto_fijo_polinomica_doble,
    1.2,
    2.8,
    1.2,
    2.5
)

procesar_funcion(
    "logaritmica",
    logaritmica,
    derivada_logaritmica,
    segunda_derivada_logaritmica,
    punto_fijo_logaritmica,
    2,
    3,
    2.5,
    3
)

procesar_funcion(
    "exponencial",
    exponencial,
    derivada_exponencial,
    segunda_derivada_exponencial,
    punto_fijo_exponencial,
    0,
    1,
    0.5,
    1
)

procesar_funcion(
    "trigonometrica",
    trigonometrica,
    derivada_trigonometrica,
    segunda_derivada_trigonometrica,
    punto_fijo_trigonometrica,
    0,
    1,
    0.5,
    1
)

procesar_funcion(
    "mixta",
    mixta,
    derivada_mixta,
    segunda_derivada_mixta,
    punto_fijo_mixta,
    0.1,
    1,
    0.5,
    1
)

print()
print("Se generaron los graficos de convergencia")