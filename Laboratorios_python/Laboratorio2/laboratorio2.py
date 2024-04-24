#!/usr/bin/python3

# Ismael Jimenez Carballo-B94009
# Programa para determinar el índice donde insertar un número 'm' en una
# lista ordenada para que la lista siga estando ordenada.
# Se pueden probar diferentes valores en una misma lista,
# hasta que el usuario desee dejar de probar valores.

def get_integer_input(incert_value):
    while True:
        try:
            value = int(input(incert_value))
            return value
        except ValueError:
            print('Por favor, inserte un número entero.')


# Solicitar números para la lista
amount_lista = get_integer_input('Introduce la cantidad de '
                                 'dígitos que quiere introducir en'
                                 'la lista: ')
numeros = []
for i in range(amount_lista):
    numero = get_integer_input('Introduce un número para la lista: ')
    numeros.append(numero)

# Ordenar la lista
numeros.sort()
print(f'Lista ordenada: {numeros}')

# Preguntar por el número 'm'
while True:
    m = get_integer_input('Inserte el número que '
                          'quiere ordenar en la lista: ')
    for i, num in enumerate(numeros):
        if m <= num:
            indice = i
            break
    else:
        indice = len(numeros)

    print(f'm ({m}) debe ser insertado en el índice {indice}.')

    continuar = input('¿Desea probar con '
                      'otro número? (s/n): ').strip().lower()
    if continuar != 's':
        break
