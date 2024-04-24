#!/usr/bin/python3
"""
Nombre del Programa: Gestión de Vectores N-Dimensionales

Descripción:
Este programa define una clase 'Vector' para representar y
manipular vectores en un espacio N-dimensional.
Incluye funcionalidades para sumar, restar, comparar vectores,
y calcular la distancia euclidiana al origen.
Se proporcionan métodos para acceder y modificar elementos
individuales del vector y se manejan errores
específicos a través de una clase de excepción
personalizada.

Autor: Ismael Jimenez Carballo
Matrícula: B94009
"""

from math import sqrt


class VectorError(Exception):
    """
    Clase que representa un error especial para la clase Vector
    """
    pass


class Vector:
    """
    Clase para representar vectores N-dimensionales.

    Atributos:
        size (int): El número de dimensiones del vector.
        values (list): Lista de valores que representan el vector.
    """

    def __init__(self, n, values=None):
        """
        Inicializa un objeto Vector.

        Parámetros:
            n (int): El número de dimensiones del vector.
            values (list | tuple, opcional): Una lista o tupla con los
            valores iniciales del vector.

        Sanity check:
            VectorError: Si 'n' no es un entero positivo,
                         si 'values' no es una lista o tupla,
                         si la longitud de 'values' no coincide
                         con 'n', o si algún valor en 'values'
                         no es un número entero o flotante.
        """
        if not isinstance(n, int) or n <= 0:
            raise VectorError("El tamaño 'n' debe ser un entero positivo.")
        self.size = n

        if values is None:
            self.values = [0.0 for _ in range(n)]
        else:
            if not isinstance(values, (list, tuple)):
                raise VectorError("Los valores deben ser una lista o tupla.")
            if len(values) != n:
                raise VectorError("El número de valores debe coincidir "
                                  "con el tamaño 'n'.")
            if not all(isinstance(val, (int, float)) for val in values):
                raise VectorError("Todos los valores deben ser números "
                                  "enteros o flotantes.")

            self.values = [val for val in values]

    def __str__(self):
        """
        Devuelve una representación en cadena del vector.

        Retorna:
            str: Una representación de cadena del vector.
        """
        return '[' + ','.join([str(val) for val in self.values]) + ']'

    def __add__(self, other):
        """
        Suma este vector con otro vector y devuelve el resultado.

        Parámetros:
            other (Vector): Otro vector para sumar.

        Retorna:
            Vector: Un nuevo vector que es la suma de este vector y 'other'.

        Sanity check:
            VectorError: Si 'other' no es una instancia de
            Vector o si los tamaños de los vectores son distintos.
        """
        if not isinstance(other, Vector):
            raise VectorError("El objeto con el que se intenta "
                              "sumar no es una instancia de Vector")
        if self.size != other.size:
            raise VectorError("No se pueden "
                              "sumar vectores de tamaños distintos")

        newvalues = [a + b for a, b in zip(self.values, other.values)]
        return Vector(self.size, newvalues)

    def __sub__(self, other):
        """
        Resta otro vector de este vector y devuelve el resultado.

        Parámetros:
            other (Vector): Otro vector para restar.

        Retorna:
            Vector: Un nuevo vector que es la resta de este vector y 'other'.

        Sanity check:
            VectorError: Si 'other' no es una instancia de
            Vector o si los tamaños de los vectores son distintos.
        """
        if not isinstance(other, Vector):
            raise VectorError("El objeto con el que se intenta "
                              "restar no es una instancia de Vector")
        if self.size != other.size:
            raise VectorError("No se pueden restar "
                              "vectores de tamaños distintos")

        newvalues = [a - b for a, b in zip(self.values, other.values)]
        return Vector(self.size, newvalues)

    def __eq__(self, other):
        """
        Comprueba si este vector es igual a otro vector.

        :param other: Otro objeto Vector.
        :return: True si ambos vectores son iguales, False en caso contrario.
        """
        # Comprueba si 'other' es una instancia
        # de Vector y compara los valores.
        if not isinstance(other, Vector):
            return NotImplemented
        return self.values == other.values

    def __getitem__(self, index):
        """
        Devuelve el valor en un índice específico del vector.

        :param index: Índice del valor a obtener.
        :return: El valor en el índice especificado.
        """
        # Verifica que el índice sea un entero y esté dentro del rango válido.
        if not isinstance(index, int):
            raise TypeError("El índice debe ser un entero")
        if not 0 <= index < self.size:
            raise IndexError("Índice fuera de rango")
        return self.values[index]

    def __setitem__(self, index, value):
        """
        Asigna un nuevo valor en un índice específico del vector.

        :param index: Índice donde se asignará el valor.
        :param value: Valor a asignar.
        """
        # Verifica que el índice y el valor sean de
        # tipos apropiados y el índice en rango.
        if not isinstance(index, int):
            raise TypeError("El índice debe ser un entero")
        if not isinstance(value, (int, float)):
            raise TypeError("El valor debe ser un número entero o flotante")
        if not 0 <= index < self.size:
            raise IndexError("Índice fuera de rango")
        self.values[index] = value

    def __len__(self):
        """
        Devuelve el tamaño (número de elementos) del vector.

        :return: El tamaño del vector.
        """
        return self.size

    def distanciaACero(self):
        """
        Calcula la distancia euclidiana de este vector al origen.

        :return: La distancia euclidiana al origen.
        """
        # Calcula y devuelve la raíz cuadrada
        # de la suma de los cuadrados de los valores.
        return sqrt(sum(val ** 2 for val in self.values))


if __name__ == '__main__':
    # Creación de instancias de la clase Vector
    vector1 = Vector(5, values=[1, 2, 3, 4, 5])
    vector2 = Vector(5, values=[1, 2, 3, 4, 5])
    vector_diferente_tamaño = Vector(3, values=[1, 2, 3])

    # Prueba de la representación en string (__str__)
    print('Probando representación string:')
    print(vector1)  # Debe mostrar la representación en string del vector1

    # Prueba de la suma de dos vectores del mismo tamaño
    print('Probando la suma de vectores del mismo tamaño:')
    try:
        vector3 = vector1 + vector2
        print(vector3)
    except VectorError as err:
        print(f"Error: {err}")

    # Prueba de la suma de dos vectores de diferente tamaño
    print('Probando la suma con vectores de tamaño diferente:')
    try:
        vector3 = vector1 + vector_diferente_tamaño
    except VectorError as err:
        print(f"Error: {err}")

    # Prueba de la resta de dos vectores
    print('Probando la resta de vectores:')
    try:
        vector4 = vector1 - vector2
        print(vector4)
    except VectorError as err:
        print(f"Error: {err}")

    # Comparación de dos vectores
    print('Comparando vectores:')
    print('Iguales' if vector1 == vector2 else 'No iguales')

    # Prueba de acceso y modificación de un elemento del vector por índice
    print('Probando acceso y modificación por índice:')
    try:
        print('Valor antes:', vector1[3])
        vector1[3] = 15
        print('Valor después:', vector1[3])
    except (TypeError, IndexError) as err:
        print(f"Error: {err}")

    # Prueba de acceso a un elemento del vector con un índice fuera de rango
    print('Probando acceso con índice inválido:')
    try:
        print(vector1[10])
    except IndexError as err:
        print(f"Error: {err}")

    # Prueba de asignación de un valor incorrecto a un elemento del vector
    print('Probando asignación con tipo de dato incorrecto:')
    try:
        vector1[2] = "no un número"
    except TypeError as err:
        print(f"Error: {err}")

    # Prueba de la longitud del vector (__len__)
    print('Probando longitud del vector:')
    print(len(vector1))  # Debe mostrar la longitud del vector1

    # Prueba del método distanciaACero
    print('Probando método distanciaACero:')
    print(vector1.distanciaACero())
    # Debe mostrar la distancia al cuadrado del vector1 al origen

    # Prueba del manejo de excepciones en el constructor
    print('Probando constructor con argumentos inválidos:')
    try:
        vector_invalido = Vector(-1)
    except VectorError as err:
        print(f"Error: {err}")
