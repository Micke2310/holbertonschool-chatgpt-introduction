#!/usr/bin/python3
import sys

def factorial(n):
    """Calcula el factorial de un número entero no negativo n""" 
    if n < 0:
        return "Error: n debe ser un número entero no negativo"
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    try:
        # Intenta convertir el argumento de la línea de comandos a un entero
        num = int(sys.argv[1]);
    except (IndexError, ValueError):
        # Maneja los casos en que no se proporcionan argumentos o no se pueden convertir a entero.
        print("Error: Debes proporcionar un número entero no negativo como argumento");
        sys.exit(1);  # Sale del programa indicando que hubo un error.

    # Calcula e imprime el factorial.
    f = factorial(num);
    print(f);
