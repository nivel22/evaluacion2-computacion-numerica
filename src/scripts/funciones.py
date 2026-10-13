
import numpy as np


def polinomica_simple(x):
    resultado = x**3 - x - 2
    return resultado


def polinomica_doble(x):
    resultado = (x - 2)**2
    return resultado


def logaritmica(x):
    resultado = np.log(x) + x - 4
    return resultado


def exponencial(x):
    resultado = np.exp(-x) - x
    return resultado


def trigonometrica(x):
    resultado = np.cos(x) - x
    return resultado


def mixta(x):
    resultado = np.sqrt(x) - np.cos(x)
    return resultado


def derivada_polinomica_simple(x):
    resultado = 3*x**2 - 1
    return resultado


def derivada_polinomica_doble(x):
    resultado = 2*(x - 2)
    return resultado


def derivada_logaritmica(x):
    resultado = 1/x + 1
    return resultado


def derivada_exponencial(x):
    resultado = -np.exp(-x) - 1
    return resultado


def derivada_trigonometrica(x):
    resultado = -np.sin(x) - 1
    return resultado


def derivada_mixta(x):
    resultado = 1/(2*np.sqrt(x)) + np.sin(x)
    return resultado


def segunda_derivada_polinomica_simple(x):
    resultado = 6*x
    return resultado


def segunda_derivada_polinomica_doble(x):
    resultado = 2
    return resultado


def segunda_derivada_logaritmica(x):
    resultado = -1/x**2
    return resultado


def segunda_derivada_exponencial(x):
    resultado = np.exp(-x)
    return resultado


def segunda_derivada_trigonometrica(x):
    resultado = -np.cos(x)
    return resultado


def segunda_derivada_mixta(x):
    resultado = -1/(4*x**(3/2)) + np.cos(x)
    return resultado


def punto_fijo_polinomica_simple(x):
    resultado = np.cbrt(x + 2)
    return resultado


def punto_fijo_logaritmica(x):
    resultado = 4 - np.log(x)
    return resultado


def punto_fijo_exponencial(x):
    resultado = np.exp(-x)
    return resultado


def punto_fijo_trigonometrica(x):
    resultado = np.cos(x)
    return resultado


def punto_fijo_mixta(x):
    resultado = np.cos(x)**2
    return resultado


def punto_fijo_polinomica_doble(x):
    resultado = x + (x - 2)**2 / 2
    return resultado
