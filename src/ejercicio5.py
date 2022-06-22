################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una función que determine si una cadena con
corchetes está balanceada.
"""

def esta_balanceada(cadena, posicion = 0, abre = False):
    """
    Esta función se encarga de revisar si una cadena
    está balanceada.
    """
    longitud = len(cadena)
    balanceada = False
    if longitud == 0:
        balanceada = True
    while posicion < longitud:
        if cadena[posicion] == '[':
            abre = True
            cierra, posicion = esta_cerrada(cadena, posicion + 1, abre)
            if cierra:
                abre = False
                balanceada = True
        elif cadena[posicion] == ']':
            if abre:
                balanceada = True
            else:
                balanceada = False
                posicion = longitud
        posicion += 1
    return balanceada
                

def esta_cerrada(cadena, posicion = 0, abre = False):
    if cadena[posicion] == '[':
        abre = True
        cierra, posicion = esta_cerrada(cadena, posicion + 1, abre)
        if cierra:
            abre = False
            cerrada = True
    elif cadena[posicion] == ']':
        if abre:
            cerrada = True
        else:
            cerrada = False
            posicion = longitud
    return cerrada, posicion


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cadena = input("Ingrese una cadena de corchetes: ")
    balanceada = esta_balanceada(cadena)
    print(f"{cadena} está balanceada: {balanceada}")


if __name__ == "__main__":
    principal()
