#!/usr/bin/env python3
"""
Programa para la detección de palíndromos y
caracteres únicos en un archivo de texto.

Este script lee un archivo de texto,
identifica y muestra todos los palíndromos,
así como los caracteres únicos y sus respectivos
índices en el texto.

Autor: Ismael Jimenez Carballo - B94009

"""


class InvalidFile(Exception):
    """

    Excepción personalizada para
    indicar un error al abrir un archivo.

    """
    pass


def check_text_palindrome():
    """

    Busca y muestra palíndromos en un
    archivo de texto, junto con sus índices.

    """
    # Intenta abrir el archivo de texto
    try:
        texto_open = open('entrada.txt', 'r')
    except Exception as e:
        # Levanta una excepción personalizada si falla la apertura del archivo
        raise InvalidFile(f"No se puede abrir el archivo: {e}")

    # Lee el contenido del archivo y lo cierra
    texto = texto_open.read()
    texto_open.close()

    # Divide el texto en palabras
    palabras = texto.split(' ')
    # Diccionario para almacenar palíndromos encontrados y sus índices
    palindromos_encontrados = {}
    # Índice global para rastrear la posición en el texto
    indice_global = -1

    # Itera sobre cada palabra en el texto
    for palabra in palabras:
        # Limpia la palabra de caracteres no alfabéticos
        palabra_limpia = ''.join(filter(str.isalpha, palabra))
        # Convierte la palabra limpia a minúsculas para detectar palíndromos
        palabra_limpia_lower = palabra_limpia.lower()

        # Busca palíndromos dentro de la palabra
        for i in range(len(palabra_limpia_lower) + 1):
            for j in range(i + 2, len(palabra_limpia_lower) + 1):
                # Extrae subcadenas de la palabra
                subcadena_lower = palabra_limpia_lower[i:j]
                # Verifica si la subcadena es un palíndromo
                if subcadena_lower == subcadena_lower[::-1]:
                    # Calcula el índice del palíndromo en el texto original
                    indice_palindromo = indice_global + i
                    # Extrae el palíndromo del texto original
                    subcadena_original = texto[indice_palindromo + 1:
                                               indice_palindromo + j - i + 1]
                    # Almacena el palíndromo y su índice en el diccionario
                    if subcadena_original not in palindromos_encontrados:
                        palindromos_encontrados[
                            subcadena_original] = [indice_palindromo]
                    else:
                        palindromos_encontrados[
                            subcadena_original].append(indice_palindromo)

        # Actualiza el índice global para la siguiente palabra
        indice_global += len(palabra) + 1

    # Imprime los palíndromos encontrados y sus índices
    print(f"{texto} tiene los siguientes palíndromos internos:")
    for palindromo, indices in palindromos_encontrados.items():
        print(f"{palindromo}: índice(s) {indices}")


def check_text_alone_char():
    """

    Busca y muestra caracteres únicos en un
    archivo de texto, junto con sus índices.

    """
    # Intenta abrir el archivo de texto
    try:
        texto_open = open('entrada.txt', 'r')
    except Exception as e:
        # Levanta una excepción personalizada si falla la apertura del archivo
        raise InvalidFile(f"No se puede abrir el archivo: {e}")

    # Lee el contenido del archivo y lo cierra
    texto = texto_open.read()
    texto_open.close()

    # Divide el texto en palabras
    palabras = texto.split(' ')
    # Diccionario para almacenar caracteres únicos y sus índices
    char_lone = {}
    # Índice global para rastrear la posición en el texto
    indice_global = -1

    # Itera sobre cada palabra en el texto
    for palabra in palabras:
        # Itera sobre cada carácter en la palabra
        for i, char in enumerate(palabra):
            # Verifica si el carácter es único y alfabético
            if char.isalpha() and len(palabra) == 1:
                # Calcula el índice del carácter en el texto original
                indice_char = indice_global + i - 1
                # Almacena el carácter y su índice en el diccionario
                if char not in char_lone:
                    char_lone[char] = [indice_char]
                else:
                    char_lone[char].append(indice_char)

        # Actualiza el índice global para la siguiente palabra
        indice_global += len(palabra) + 1

    # Imprime los caracteres únicos encontrados y sus índices
    for char, indices in char_lone.items():
        print(f"_{char}_: índice(s) {indices}")


if __name__ == "__main__":
    # Bloque principal para ejecutar las funciones y manejar excepciones
    try:
        check_text_palindrome()
    except InvalidFile as error:
        print(error)

    try:
        check_text_alone_char()
    except InvalidFile as error:
        print(error)
