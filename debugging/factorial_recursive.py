#!/usr/bin/python3
import sys

# Descripción de la función:
# Esta función calcula el factorial de un número dado. El factorial de un número es el producto de todos los números enteros positivos desde 1 hasta el número dado.
# Por ejemplo, el factorial de 5 (denotado como 5!) es 1*2*3*4*5 = 120.
def factorial(n):
    # Parámetros:
    # n: Un número entero para el cual se calculará el factorial.

    # Si el número es 0, el factorial es 1 por definición.
    if n == 0:
        return 1
    else:
        # Si el número no es 0, se calcula el factorial multiplicando el número por el factorial de (n-1).
        return n * factorial(n-1)

# Retorna:
# El factorial del número dado.

# Se toma el primer argumento de la línea de comandos, se convierte a un entero y se calcula su factorial.
f = factorial(int(sys.argv[1]))

# Se imprime el factorial del número dado.
print(f)
