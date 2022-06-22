################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que retorne `True` cuando un número entero es par
y `False` cuando no lo sea, sin utilizar módulo. (`%`)
"""


def valor_absoluto(numero: int) -> int:
    """
    Esta función devuelve el valor absoluto de un número.
    """
    if numero < 0:
        numero *= -1
    return numero


def es_par(numero: int) -> bool:
    """
    Esta función devuelve si un número es par o no.
    """
    contador = valor_absoluto(numero)
    while contador > 0:
        contador -= 2
    par = contador == 0
    return par


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese un numero entero: "))
    par = es_par(numero)
    if par:
        print(f"{numero} es par")
    else:
        print(f"{numero} no es par")


if __name__ == "__main__":
    principal()
