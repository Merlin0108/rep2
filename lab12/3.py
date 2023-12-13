def binary_representation(decimal_number):
    if decimal_number == 0:
        return ""
    return binary_representation(decimal_number // 2) + str(decimal_number % 2)


a = float(input("Введите нулевой элемент: "))
# Двоичное представление десятичного числа
binary = binary_representation(int(a))
print(f"d) Двоичное представление десятичного числа {int(a)}: {binary}")
