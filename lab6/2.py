def get_matrix_dimensions():
    while True:
        try:
            m = int(input("Enter the number of rows for the first matrix: "))
            k = int(input(
                "Enter the number of columns for the first matrix and the number of rows for the second matrix: "))
            n = int(input("Enter the number of columns for the second matrix: "))

            if m > 0 and k > 0 and n > 0:
                return m, k, n
            else:
                raise ValueError
        except ValueError:
            print("Invalid dimensions. Please enter positive integers only.")


def get_matrix_values(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    value = float(input(f"Enter the value for element ({i + 1, j + 1}): "))
                    row.append(value)
                    break
                except ValueError:
                    print("Invalid value. Please enter a valid float number.")
        matrix.append(row)
    return matrix


def multiply_matrices(matrix1, matrix2):
    m = len(matrix1)
    k = len(matrix1[0])
    n = len(matrix2[0])

    result_matrix = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for h in range(k):
                result_matrix[i][j] += matrix1[i][h] * matrix2[h][j]

    return result_matrix


def display_matrix(matrix):
    for row in matrix:
        print(row)


m, k, n = get_matrix_dimensions()

print("Enter the values for the first matrix:")
matrix1 = get_matrix_values(m, k)

print("Enter the values for the second matrix:")
matrix2 = get_matrix_values(k, n)

try:
    result_matrix = multiply_matrices(matrix1, matrix2)
    print("The product of the matrices is:")
    display_matrix(result_matrix)
except ValueError:
    print("Matrix multiplication is not possible.")
