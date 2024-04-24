#!/usr/bin/python3
"""
Implementación de una clase Matrix que realiza operaciones basicas.

Esta clase permite la creación y manipulación de matrices NxM, con operaciones
como suma, resta y multiplicación de matrices. Se utiliza una clase Vector para
representar las filas de la matriz. Además, se manejan errores específicos
relacionados con matrices mediante la clase MatrixError.

Autor: Ismael Jiménez Carballo
Carné: B94009
"""

from vector import Vector


class MatrixError(Exception):
    """
    Clase que representa un error especial para la clase Vector
    """
    pass


class Matrix:
    """
    Clase para representar matrices NxM
    """
    def __init__(self, n, m, values=None):
        """Funcion constructora de la clase.

        Parameters
        ----------
        n : int
            Cantidad de filas de la matriz
        m : int
            Cantidad de columnas de la matriz
        values : list or tuple
            Valores de la matriz
        """
        if not isinstance(n, int) or not isinstance(m,
                                                    int) or n <= 0 or m <= 0:
            raise MatrixError("Ambos n y m deben ser enteros positivos")
        if values is not None:
            if not isinstance(values, (list, tuple)):
                raise MatrixError("Values debe ser una lista o tupla")
            if len(values) != n * m:
                raise MatrixError("El tamaño de values debe ser igual a n*m")
            for val in values:
                if not isinstance(val, (float, int)):
                    raise MatrixError("Los valores en values "
                                      "deben ser enteros o flotantes")

        self.rows = n
        self.cols = m

        # self.values es una lista de objetos Vector
        # (cada fila de la matriz)
        self.values = [Vector(m) for _ in range(n)]

        if values is not None:
            for row in range(self.rows):
                for col in range(self.cols):
                    val = values[row*self.cols + col]
                    if type(val) is not float and type(val) is not int:
                        raise MatrixError(
                            "Los valores de values deben ser "
                            "flotantes o enteros")
                    self.values[row][col] = values[row*self.cols + col]

    def __str__(self):
        """
        Devuelve cada fila de la matriz como un Vector convertido a cadena.
        """
        return '\n'.join([str(vec) for vec in self.values])

    def __add__(self, other):
        """
        Suma dos matrices si tienen las mismas dimensiones.
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise MatrixError("Las dimensiones de las "
                              "matrices deben ser iguales")
        data = []
        for row in range(self.rows):
            for col in range(self.cols):
                data.append(self.values[row][col] + other.values[row][col])
        return Matrix(self.rows, self.cols, values=data)

    def __sub__(self, other):
        """
        Resta dos matrices si tienen las mismas dimensiones.
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise MatrixError("Las dimensiones de las "
                              "matrices deben ser iguales")
        data = []
        for row in range(self.rows):
            for col in range(self.cols):
                data.append(self.values[row][col] - other.values[row][col])
        return Matrix(self.rows, self.cols, values=data)

    def __mul__(self, other):
        """
        Multiplica esta matriz por otra, verificando
        que ambas son compatibles dadas las dimensiones.
        """
        if self.cols != other.rows:
            raise MatrixError("Las dimensiones de las matrices "
                              "no son compatibles para la multiplicación")
        data = []
        for m in range(self.rows):
            list1 = []
            for j in range(self.cols):
                list1.append(self.values[m][j])
            for i in range(other.cols):
                list2 = [v[i] for v in other.values]
                mults = [a * b for a, b in zip(list1, list2)]
                data.append(sum(mults))
        return Matrix(self.rows, other.cols, values=data)

    def __getitem__(self, index):
        """
        Permite acceder a una fila de la matriz mediante índices.
        """
        if not isinstance(index, int) or index < 0 or index >= self.rows:
            raise MatrixError("El índice debe ser un entero "
                              "positivo en el rango válido")
        return self.values[index]

    def __setitem__(self, index, value):
        """
        Permite modificar una fila de la matriz mediante índices.
        """
        if not isinstance(index, int) or index < 0 or index >= self.rows:
            raise MatrixError("El índice debe ser"
                              "un entero positivo"
                              "dentro del rango válido")
        if not isinstance(value, Vector) or len(value) != self.cols:
            raise MatrixError("Debe ser un Vector con la longitud adecuada")
        self.values[index] = value


# Ejemplo de uso
if __name__ == '__main__':
    matriz = Matrix(2, 2, values=[1, -2, 0, 3])
    matriz1 = Matrix(2, 2, values=[4, 1, -2, 2])

    print("Matriz:")
    print(matriz)
    print("\nMatriz1:")
    print(matriz1)

    suma = matriz + matriz1
    print("\nSuma de Matriz y Matriz1:")
    print(suma)

    resta = matriz - matriz1
    print("\nResta de Matriz y Matriz1:")
    print(resta)

    multiplicacion = matriz * matriz1
    print("\nMultiplicación de Matriz y Matriz1:")
    print(multiplicacion)

    matriz[0][1] = 17
    print("\nMatriz después de modificar un elemento:")
    print(matriz)
