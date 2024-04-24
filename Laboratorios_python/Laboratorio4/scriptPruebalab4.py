from Laboratorios.vector import Vector, VectorError
from random import randint

if __name__ == '__main__':
    print('\n\n*********************************************************\n\n')
    print('Probando creación de Vector con tamaño aleatorio, sin values')
    size = randint(2, 20)
    vector = Vector(size)
    assert len(vector) == size, 'El '
    'tamaño del vector no es el esperado. '
    'Esperado: {}. Obtenido: {}'.format(size, len(vector))
    assert all([vector[ind] == 0 for ind in range(size)])

    print('\n\n*********************************************************\n\n')
    print('Probando creación de Vector con tamaño aleatorio, con values')
    size = randint(0, 20)
    values = [randint(0, 100) for _ in range(size)]
    vector = Vector(size, values=values)
    assert len(vector) == size, 'El '
    'tamaño del vector no es el esperado. '
    'Esperado: {}. Obtenido: {}'.format(size, len(vector))
    assert all([values[ind] == vector[ind] for ind in range(size)]), 'Los '
    'valores no corresponden.\n'
    'Esperados: {}\n'
    'Obtenidos: {}'.format(
        values,
        [vector[ind] for ind in range(size)]
    )

    print('\n\n*********************************************************\n\n')
    print('Probando asignación manual de elementos (setitem)')
    size = randint(0, 20)
    values = [randint(0, 100) for _ in range(size)]
    vector = Vector(size)

    for ind in range(size):
        vector[ind] = values[ind]
    assert all([values[ind] == vector[ind] for ind in range(size)]), 'Los '
    'valores no corresponden.\n'
    'Esperados: {}\n'
    'Obtenidos: {}'.format(
        values,
        [vector[ind] for ind in range(size)]
    )

    print('\n\n*********************************************************\n\n')
    print('Probando creación de vectores con errores en parámetros')
    print('Tamaño de values incorrecto')
    try:
        values = [randint(0, 100) for _ in range(5, randint(6, 10))]
        vector = Vector(4, values=values)
        raise ValueError('no debió ser exitoso')
    except VectorError:
        print(
            'Se obtuvo VectorError al usar '
            'values de mayor tamaño que size... muy bien')
    except Exception as e:
        print(
            'ERROR: al usar values de mayor tamaño que size '
            'no se levantó la excepción '
            'esperada: \'VectorError\', '
            'se obtuvo: \'{}\''.format(type(e)))
            
    try:
        values = [randint(0, 100) for _ in range(randint(0, 9))]
        vector = Vector(10, values=values)
        raise ValueError('no debió ser exitoso')
    except VectorError:
        print(
            'Se obtuvo VectoError al usar '
            'values de menor tamaño que size... muy bien')
    except Exception as e:
        print(
            'ERROR: al usar values de menor tamaño que size '
            'no se levantó la excepción '
            'esperada: \'VectorError\', '
            'se obtuvo: \'{}\''.format(type(e)))
            
    print('\n\n*********************************************************\n\n')
    print('Probando representación como string')
    size = randint(0, 20)
    values = [randint(0, 100) for _ in range(size)]
    vector = Vector(size, values=values)

    vectorSTR = str(vector)
    esperado = '[' + ','.join([str(val) for val in values]) + ']'
    assert esperado == vectorSTR, 'No '
    'se obtuvo la representación como string esperada.\n'
    'Esperado: {}\n'
    'Obtenido: {}'.format(
        esperado, vectorSTR
    )

    print('\n\n*********************************************************\n\n')
    print('Probando suma y resta')
    size = randint(0, 5)
    values1 = [randint(0, 100) for _ in range(size)]
    vector1 = Vector(size, values=values1)
    values2 = [randint(0, 100) for _ in range(size)]
    vector2 = Vector(size, values=values2)

    sumaEsperada = [val1 + val2 for val1, val2 in zip(values1, values2)]
    vectorSumado = vector1 + vector2
    assert all([
        sumaEsperada[ind] == vectorSumado[ind]
        for ind in range(size)
    ]), 'Vector sumado no es el esperado\n'
    'Esperado: {}\n'
    'Obtenido: {}'.format(sumaEsperada, vectorSumado)

    restaEsperada = [val1 - val2 for val1, val2 in zip(values1, values2)]
    vectorRestado = vector1 - vector2
    assert all([
        restaEsperada[ind] == vectorRestado[ind]
        for ind in range(size)
    ]), 'Vector restado no es el esperado\n'
    'Esperado: {}\n'
    'Obtenido: {}'.format(restaEsperada, vectorRestado)

    print('\n\n*********************************************************\n\n')
    print('Revisando sumas y restas con tamaños no compatibles')
    vector1 = Vector(randint(1, 10))
    vector2 = Vector(randint(11, 20))

    try:
        vectorError = vector1 + vector2
        raise ValueError('no se debe llegar a esta linea')
    except Exception as e:
        if type(e) is not VectorError:
            print(
                'ERROR: al sumar vectores de tamano incompatible '
                'no se levantó la excepción '
                'esperada: \'VectorError\', '
                'se obtuvo: \'{}\''.format(type(e)))
            
    try:
        vectorError = vector1 - vector2
        raise ValueError('no se debe llegar a esta linea')
    except Exception as e:
        if type(e) is not VectorError:
            print(
                'ERROR: al restar vectores de tamano incompatible '
                'no se levantó la excepción '
                'esperada: \'VectorError\', '
                'se obtuvo: \'{}\''.format(type(e)))

    print('\n\n*********************************************************\n\n')
    print('Probando eq')
    size = randint(0, 20)
    values1 = [randint(0, 100) for _ in range(size)]
    values2 = tuple(values1)
    vector1 = Vector(size, values=values1)
    vector2 = Vector(size, values=values2)

    assert vector1 == vector2, 'Al comparar vectores iguales no se obtuvo TRUE'

    print('\n\n*********************************************************\n\n')
    print('Probando distanciaACero')
    vector = Vector(randint(2, 10))
    assert vector.distanciaACero() == 0, 'Para '
    'vector de 0s no se obtuvo una distanciaACero de 0'

    size = 2
    values = [1, 2]
    vector = Vector(size, values=values)
    distanciaEsperada = 2.23606797749979
    assert all([
        vector.distanciaACero() >= distanciaEsperada*0.97,
        vector.distanciaACero() <= distanciaEsperada*1.03
    ]), 'No se obtuvo '
    'distanciaACero esperada.\n'
    'Esperada: {}\n'
    'Obtenido: {}'.format(
        distanciaEsperada,
        vector.distanciaACero()
    )

    print('\n\n*********************************************************\n\n')
    print('FIN')



