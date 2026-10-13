
from funciones import polinomica_doble
from funciones import derivada_polinomica_doble
from funciones import segunda_derivada_polinomica_doble
from funciones import punto_fijo_polinomica_doble

from biseccion import biseccion
from falsa_posicion import falsa_posicion
from punto_fijo import punto_fijo
from secante import secante
from newton_raphson import newton_raphson
from newton_mejorado import newton_mejorado


limite_inferior = 1.2
limite_superior = 2.5
valor_inicial = 1.2
segundo_valor = 2.5

tolerancia = 0.000001
maximo_iteraciones = 100
raiz_exacta = 2

valor_inferior = polinomica_doble(limite_inferior)
valor_superior = polinomica_doble(limite_superior)

print("Funcion: (x - 2)**2")
print("Limite inferior:", limite_inferior)
print("Limite superior:", limite_superior)
print("Tolerancia:", tolerancia)
print("Raiz exacta:", raiz_exacta)
print("Valor en limite inferior:", valor_inferior)
print("Valor en limite superior:", valor_superior)

print()
print("Comprobacion de la raiz doble")
print("Valor de la funcion en x = 2:", polinomica_doble(2))
print("Primera derivada en x = 2:", derivada_polinomica_doble(2))
print("Segunda derivada en x = 2:", segunda_derivada_polinomica_doble(2))

print()
print("Metodo de biseccion")

if valor_inferior * valor_superior < 0:
    raiz, iteraciones, errores = biseccion(
        polinomica_doble,
        limite_inferior,
        limite_superior,
        tolerancia,
        maximo_iteraciones
    )
    print("Raiz encontrada:", raiz)
    print("Iteraciones:", iteraciones)
else:
    print("No aplica porque no existe cambio de signo")

print()
print("Metodo de falsa posicion")

if valor_inferior * valor_superior < 0:
    raiz, iteraciones, errores = falsa_posicion(
        polinomica_doble,
        limite_inferior,
        limite_superior,
        tolerancia,
        maximo_iteraciones
    )
    print("Raiz encontrada:", raiz)
    print("Iteraciones:", iteraciones)
else:
    print("No aplica porque no existe cambio de signo")


raiz, iteraciones, errores = punto_fijo(
    punto_fijo_polinomica_doble,
    valor_inicial,
    tolerancia,
    maximo_iteraciones
)

print()
print("Metodo de punto fijo")
print("Valor inicial:", valor_inicial)
print("Aproximacion:", raiz)
print("Iteraciones:", iteraciones)
print("Valor de la funcion:", polinomica_doble(raiz))
print("Error final:", errores[-1])
print("Distancia a la raiz:", abs(raiz - raiz_exacta))

if errores[-1] < tolerancia:
    print("Cumplio el criterio de parada")
else:
    print("Llego al maximo de iteraciones")


raiz, iteraciones, errores = secante(
    polinomica_doble,
    valor_inicial,
    segundo_valor,
    tolerancia,
    maximo_iteraciones
)

print()
print("Metodo de secante")
print("Primer valor:", valor_inicial)
print("Segundo valor:", segundo_valor)

if raiz is not None:
    print("Aproximacion:", raiz)
    print("Iteraciones:", iteraciones)
    print("Valor de la funcion:", polinomica_doble(raiz))
    print("Error final:", errores[-1])
    print("Distancia a la raiz:", abs(raiz - raiz_exacta))
else:
    print("No se encontro la raiz")


raiz, iteraciones, errores = newton_raphson(
    polinomica_doble,
    derivada_polinomica_doble,
    valor_inicial,
    tolerancia,
    maximo_iteraciones
)

print()
print("Metodo de Newton-Raphson")
print("Valor inicial:", valor_inicial)

if raiz is not None:
    print("Aproximacion:", raiz)
    print("Iteraciones:", iteraciones)
    print("Valor de la funcion:", polinomica_doble(raiz))
    print("Error final:", errores[-1])
    print("Distancia a la raiz:", abs(raiz - raiz_exacta))
else:
    print("No se encontro la raiz")


raiz, iteraciones, errores = newton_mejorado(
    polinomica_doble,
    derivada_polinomica_doble,
    segunda_derivada_polinomica_doble,
    valor_inicial,
    tolerancia,
    maximo_iteraciones
)

print()
print("Metodo de Newton-Raphson mejorado")
print("Valor inicial:", valor_inicial)

if raiz is not None:
    print("Aproximacion:", raiz)
    print("Iteraciones:", iteraciones)
    print("Valor de la funcion:", polinomica_doble(raiz))
    print("Error final:", errores[-1])
    print("Distancia a la raiz:", abs(raiz - raiz_exacta))
else:
    print("No se encontro la raiz")
