################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
La sucesión de Fibonacci es una sucesión infinita donde cada elemento es
la suma de los dos anteriores. En la misma, los dos primeros términos
son 1. (En algunos lugares se toma el primer término en 0 y el segundo en 1)
Implementar una función que permita obtener el n-esimo termino de la
sucesión de Fibonacci. Siendo este número un entero positivo mayor a 2.
"""


def fibonacci(numero: int) -> int:
    """
    Esta función devuelve el n-ésimo elemento de la serie de Fibonacci.
    """
    num_0 = 1
    num_1 = 1
    i = 1
    while i < numero:
        num_2 = num_0 + num_1
        num_0 = num_1
        num_1 = num_2
        i += 1
    return num_1


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese un numero entero positivo: "))
    fibonacci_n = fibonacci(numero)
    print(f"El termino {numero} de la serie de Fibonacci es {fibonacci_n}")


if __name__ == "__main__":
    principal()
