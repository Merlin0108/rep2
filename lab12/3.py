def binary_representation(decimal_number):
    if decimal_number == 0:
        return ""
    return binary_representation(decimal_number // 2) + str(decimal_number % 2)


try:
    a = float(input("Введите нулевой элемент: "))
    # Двоичное представление десятичного числа
    binary = binary_representation(int(a))
except ValueError:
    print("Ошибка ввода. Пожалуйста, введите корректные числа.")
    quit()
except ZeroDivisionError:
    print("Ошибка: деление на ноль.")
    quit()
print(f"Двоичное представление десятичного числа {int(a)}: {binary}")
