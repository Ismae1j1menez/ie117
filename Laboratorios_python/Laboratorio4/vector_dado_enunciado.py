from math import e, sqrt

class VectorError(Exception):
    """
    Clase que representa un error especial para la clase Vector
    """
    pass

class Vector:
    """
    Clase para representar vectores N-d
    """
    def __init__(self, n, values=None):
        # Nosotros definimos los atributos del objeto
        self.size = n

        # TODO: Añadir sannity checks:
        # - que values sea una lista, o tupla
        # - el tamano de values sea igual a n
        # - los valores de values sean flotantes
        if values is None:
            self.values = [0 for _ in range(n)]
        else:
            # No queremos usar el mismo objeto pasado a values (mutable)
            # Creamos una nueva lista en self.values
            self.values = [val for val in values]

    def __str__(self):
        return '[' + ','.join(
            [str(val) for val in self.values]) + ']'

    # addition
    def __add__(self, other):
        # TODO: sannity checks
        # - que los tipos de self y other sean iguales
        # - que el tamaño sea el mismo
        if len(self.values) != len(other.values):
            raise TypeError('No se pueden sumar vectores de tamanos distintos')
        newvalues = [a + b for a, b in zip(self.values, other.values)]

        return Vector(self.size, newvalues)
    
    # substraction
    def __sub__(self, other):
        # TODO: sannity checks
        # - que los tipos de self y other sean iguales
        # - que el tamaño sea el mismo
        if len(self.values) != len(other.values):
            raise TypeError('No se pueden restar vectores de tamanos distintos')
        newvalues = [a - b for a, b in zip(self.values, other.values)]

        return Vector(self.size, newvalues)
    
    # eq
    def __eq__(self, other):
        # TODO: sannity checks
        # - que los tipos de self y other sean iguales
        return self.values == other.values
    
    # []: get
    def __getitem__(self, index):
        # TODO: sannity checks
        # - index sea válido: positivo, entero
        # - index dentro del rango de self.values
        return self.values[index]
    
    # []: set
    def __setitem__(self, index, value):
        # TODO: sannity checks
        # - index positivo entero
        # - value flotante
        # - index dentro del rango de self.values
        self.values[index] = value

    # len(vector)
    def __len__(self):
        # TODO: Hacerla completa
        pass

    def distanciaACero(self):
        # TODO: Hacerla completa 
        # Ojo: caso especial 0,0,0, ... ,0
        pass
            
    
if __name__ == '__main__':
    # Esto NO será evaluado, usted puede
    # crear todas las pruebas que necesita acá
    vector1 = Vector(5, values=[1, 2, 3, 4, 5])
    vector2 = Vector(5, values=[1, 2, 3, 4, 5])

    # Metodos especiales
    # matematicos
    print('probando la suma')
    vector3 = vector1 + vector2
    print(vector3)

    print('probando la resta')
    vector4 = vector1 - vector2
    print(vector4)

    # comparativos logicos
    print(id(vector1))
    print(id(vector2))
    if vector1 == vector2:
        print('los vectores son iguales')
    else:
        print('los vectores NOOOO son iguales')

    # casting
    vector1STR = str(vector1)
    print(vector1STR)

    # Usar operador index
    print('Utilizando vector[3]')
    valor = vector1[3]
    print(valor)

    print('Utilizando vector[3] = 15')
    vector1[3] = 15
    print(vector1)

    vector1 += vector3 # vector1 = vector1 + vector3
