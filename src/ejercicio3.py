################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Desarrollar una función que indique el grado de superposición entre dos listas.
Siendo 0 sin superposición y uno para cada elemento superpuesto.
"""


def calcular_superposicion(sec_1, sec_2):
    """
    Esta función se encarga de calcular cuántos elementos se
    encuentran superpuestos en dos secuencias.
    """
    elementos_superpuestos = 0
    len_1 = len(sec_1)
    i = 0
    while i < len_1:
        try:
            if sec_1[i] == sec_2[i]:
                elementos_superpuestos += 1
            i += 1
        except IndexError:
            i = len_1
    return elementos_superpuestos


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    sec_1 = input("Ingrese una frase: ")
    sec_1 = list(sec_1)
    sec_2 = input("Ingrese otra frase: ")
    sec_2 = list(sec_2)
    suppos = calcular_superposicion(sec_1, sec_2)
    print(f"{sec_1} y {sec_2} tienen una superposicion de {suppos} elementos")


if __name__ == "__main__":
    principal()
