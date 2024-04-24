from matrix import Matrix
from random import randint

if __name__ == '__main__':
    print('\n\n*********************************************************\n\n')
    print('Probando creación de Matrix cuadrada con tamaño aleatorio, sin values')
    size = randint(2, 20)
    matrix = Matrix(size, size)
    assert all([matrix[row][col] == 0 for row in range(size) for col in range(size)])

    print('\n\n*********************************************************\n\n')
    print('Probando creación de Vector con tamaño aleatorio, con values')
    cols = randint(2, 20)
    rows = randint(2, 20)
    values = [randint(0, 100) for _ in range(cols*rows)]
    matrix = Matrix(rows, cols, values=values)
    assert all([values[row*cols + col] == matrix[row][col] for row in range(rows) for col in range(cols)]), 'Los '
    'valores no corresponden.\n'
    'Esperados: {}\n'
    'Obtenidos: {}'.format(
        values,
        [matrix[row][col] for row in range(rows) for col in range(cols)]
    )

    print('\n\n*********************************************************\n\n')
    print('Probando impresión de la matriz')
    valuesStr = ''
    for row in range(rows):
        valuesStr += ' '.join([str(val) for val in values[row*cols:row*cols + cols]]) + '\n'
    print('Valor esperado:\n{}\nValor obtenido:\n{}\n'.format(
        valuesStr,
        str(matrix)
    ))

    print('\n\n*********************************************************\n\n')
    print('Probando asignación manual de elementos (setitem)')
    values = [randint(0, 100) for _ in range(cols*rows)]

    for row in range(rows):
        for col in range(cols):
            matrix[row][col] = values[row*cols+col]

    assert all([values[row*cols + col] == matrix[row][col] for row in range(rows) for col in range(cols)]), 'Los '
    'valores no corresponden.\n'
    'Esperados: {}\n'
    'Obtenidos: {}'.format(
        values,
        [matrix[row][col] for row in range(rows) for col in range(cols)]
    )

    print('\n\n*********************************************************\n\n')
    print('Probando suma y resta')
    cols = randint(2, 20)
    rows = randint(2, 20)
    values1 = [randint(0, 100) for _ in range(cols*rows)]
    values2 = [randint(0, 100) for _ in range(cols*rows)]
    matrix1 = Matrix(rows, cols, values=values1)
    matrix2 = Matrix(rows, cols, values=values2)

    sumaEsperada = [val1 + val2 for val1, val2 in zip(values1, values2)]
    matrizSumada = matrix1 + matrix2
    restaEsperada = [val1 - val2 for val1, val2 in zip(values1, values2)]
    matrizRestada = matrix1 - matrix2

    print(matrix1)
    print('+')
    print(matrix2)
    print('Suma obtenida:')
    print(matrizSumada)
    print('----------------------')
    print(matrix1)
    print('-')
    print(matrix2)
    print('Resta obtenida:')
    print(matrizRestada)

    assert all([
        sumaEsperada[row*cols + col] == matrizSumada[row][col] for row in range(rows) for col in range(cols)
    ]), 'Los '
    'valores sumados no corresponden.\n'
    'Esperados: {}\n'
    'Obtenidos: {}'.format(
        sumaEsperada,
        [matrizSumada[row][col] for row in range(rows) for col in range(cols)]
    )

    assert all([
        restaEsperada[row*cols + col] == matrizRestada[row][col] for row in range(rows) for col in range(cols)
    ]), 'Los '
    'valores restados no corresponden.\n'
    'Esperados: {}\n'
    'Obtenidos: {}'.format(
        restaEsperada,
        [matrizRestada[row][col] for row in range(rows) for col in range(cols)]
    )

    print('\n\n*********************************************************\n\n')
    print('Probando multiplicación')
    cols = randint(2, 5)
    rows = randint(2, 5)
    values1 = [randint(-5, 5) for _ in range(cols*rows)]
    values2 = [randint(-5, 5) for _ in range(cols*rows)]
    matrix1 = Matrix(rows, cols, values=values1)
    matrix2 = Matrix(cols, rows, values=values2)

    print(matrix1)
    print('X')
    print(matrix2)
    print('Resultado obtenido:')
    matrizMultiplicada = matrix1 * matrix2
    print(matrizMultiplicada)

    multiplicacionEsperada = [
        [0 for _ in range(rows)]
        for _ in range(rows)
    ]
    for row in range(rows):
        for col in range(rows):
            for subcol in range(cols):
                multiplicacionEsperada[row][col] += matrix1[row][subcol] * matrix2[subcol][col]
            
    assert all([
        multiplicacionEsperada[row][col] == matrizMultiplicada[row][col] for row in range(rows) for col in range(rows)
    ]), 'Los '
    'valores sumados no corresponden.\n'
    'Esperados: {}\n'
    'Obtenidos: {}'.format(
        [multiplicacionEsperada[row][col] for row in range(rows) for col in range(rows)],
        [matrizMultiplicada[row][col] for row in range(rows) for col in range(rows)]
    )

    print('\n\n*********************************************************\n\n')
    print('FIN')