#!/usr/bin/python3
# Ismael Jimenez Carballo-B94009
# Este es un codigo de python 3, donde se realiza un código para imprimir un
# triangulo normal e inverso.
# Para este programa, su centro es el ciclo while, el que tiene como objetivo
# iterar cierta cantidad de veces.

# Comienzo del codigo
# Condición para el comienzo del ciclo
Estado = "Comienzo"
while Estado == "Comienzo":
    # Caracter con el cual se imprime el triangulo
    a = input("Digite el caracter por usar: ")
    # Cantidad de caracteres de la base
    b = int(input("Digite el tamaño de la base del triangulo superior: "))

    # Impresion del triangulo
    for i in range(b+1):
        print(a * i)

    for j in reversed(range(b)):
        print(a * j)
    # Preguntar si desea imprimir mas triangulos
    e = input("Digite SALIR para salir, "
              "cualquier otra cosa para continuar...: ")

    if e == "SALIR":
        Estado = "Terminar"
    else:
        Estado = "Comienzo"
