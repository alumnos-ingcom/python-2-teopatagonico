################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una función que obtenga los máximos, mínimos y promedio de
una secuencia con números, retornando los valores como una `tuple`.

Sin utilizar lazos `for` o las funciones integradas del lenguaje
que procesan secuencias.
"""


class ListaVaciaException(Exception):
    """
    Esta excepción es utilizada cuando la lista está vacía.
    """
    pass


def extraer_maximo(secuencia):
    """
    Esta función extrae el valor máximo de una secuencia.
    """
    longitud = len(secuencia)
    if longitud != 0:
        maximo = secuencia[0]
    else:
        raise ListaVaciaException("La lista está vacía")
    i = 1
    while i < longitud:
        if secuencia[i] > maximo:
            maximo = secuencia[i]
        i = i + 1
    return maximo


def extraer_minimo(secuencia):
    """
    Esta función extrae el valor mínimo de una secuencia.
    """
    longitud = len(secuencia)
    if longitud != 0:
        minimo = secuencia[0]
    else:
        raise ListaVaciaException("La lista está vacía")
    i = 1
    while i < longitud:
        if secuencia[i] < minimo:
            minimo = secuencia[i]
        i = i + 1
    return minimo


def extraer_promedio(secuencia):
    """
    Esta función extrae el promedio de una secuencia.
    """
    longitud = len(secuencia)
    if longitud != 0:
        promedio = 0
    else:
        raise ListaVaciaException("La lista está vacía")
    i = 0
    while i < longitud:
        promedio = promedio + secuencia[i]
        i = i + 1
    promedio = promedio / longitud
    return promedio


def procesar_secuencia(secuencia):
    """
    Esta función procesa la secuencia, extrayendo
    los valores máximo, mínimo y promedio.
    """
    maximo = extraer_maximo(secuencia)
    minimo = extraer_minimo(secuencia)
    promedio = extraer_promedio(secuencia)
    return (maximo, minimo, promedio)


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    secuencia = [1, 5, 6, 3, 7, 8, 10, 500, -8]
    try:
        secuencia = procesar_secuencia(secuencia)
        print(secuencia)
    except ListaVaciaException as exc:
        print(exc)


if __name__ == "__main__":
    principal()
