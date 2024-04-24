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
        # TODO: Añadir sannity checks:  
        # - que values sea una lista, o tupla
        # - que n y m sean enteros positivos
        # - el tamano de values sea igual a nxm
        # - los valores de values sean flotantes
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
                            'Los valores de values deben ser flotantes o enteros')
                    self.values[row][col] = values[row*self.cols + col]

    def __str__(self):
        pass

    def __add__(self, other):
        pass
        
    
    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass
        
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
        # - value tiene que ser Vector
        # - index dentro del rango de self.values
        self.values[index] = value
