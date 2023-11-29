def read_matrix(file_name):
    matrix = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                # Читаем каждую строку из файла и удаляем лишние символы
                row = list(map(int, line.strip().split()))
                matrix.append(row)
    except IOError:
        # Обработка ошибки, если файл не найден
        print(f"Файл {file_name} не найден.")
    return matrix


def write_matrix(matrix, file_name):
    try:
        # Открываем файл для записи
        with open(file_name, 'w') as file:
            for row in matrix:
                # Преобразуем каждую строку матрицы в строку значений, разделенных пробелом
                file.write(' '.join(map(str, row)) + '\n')
    except IOError:
        # Обработка ошибки при записи в файл
        print(f"Ошибка при записи в файл {file_name}.")


def transpose_matrix(matrix):
    transposed = []
    for col in range(len(matrix[0])):
        # Создаем новую матрицу, где строки становятся столбцами и наоборот
        transposed.append([matrix[row][col] for row in range(len(matrix))])
    return transposed


input_file = 'input2.txt'
output_file = 'output2.txt'

matrix = read_matrix(input_file)
if matrix:
    transposed_matrix = transpose_matrix(matrix)
    write_matrix(transposed_matrix, output_file)
    print("Ваша транспонированная матрица записана в output2.txt")