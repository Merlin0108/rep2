import numpy as np
import matplotlib.pyplot as plt

plt.figure()

plt.grid()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Произведение матрицы на вектор')
# Матрица линейного оператора
n = 2
m = 2
u = 1
num_vectors = int(input("Введите количество векторов: "))
print("Введите матрицу:")
matrix = np.empty((n, m))
for i in range(n):
    matrix[i] = np.array(list(map(float, input().split())))
vectors = []
for v in range(num_vectors):
    print(f"Введите вектор {v + 1}:")
    vector = np.array(list(map(float, input().split())))
    vectors.append(vector)
# Вычисление произведения матрицы на вектор
for vector in vectors:
    result = np.dot(matrix, vector)
    if u == 1:
        plt.plot([0, vector[0]], [0, vector[1]], label='Вектор', color='red')
        plt.plot([0, result[0]], [0, result[1]], label='Матр*вект', color='blue')
        u = 0
    else:
        plt.plot([0, vector[0]], [0, vector[1]], color='red')
        plt.plot([0, result[0]], [0, result[1]], color='blue')
    plt.legend()
    print("Результат умножения матрицы на вектор:")
    print(result[0], result[1])
plt.show()