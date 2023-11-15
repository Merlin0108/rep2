def scalar_product(vector1, vector2):
    if len(vector1) != len(vector2):
        return print("Размеры вектора не равны")
    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    return result


def input_vector():
    vector = []
    n = int(input("Введите размер вектора: "))
    for i in range(n):
        value = int(input(f"Введите {i + 1}й элемент вектора: "))
        vector.append(value)
    return vector


vector1 = input_vector()
vector2 = input_vector()
product = scalar_product(vector1, vector2)
print("Скалярное произведение двух векторов равно:", product)
