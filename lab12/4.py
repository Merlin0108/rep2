def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


try:
    a = float(input("Введите нулевой элемент: "))
    # Наименьшее общее кратное
    b = float(input("Введите второе натуральное число для нахождения НОК: "))
    least_common_multiple = lcm(int(a), int(b))
except ValueError:
    print("Ошибка ввода. Пожалуйста, введите корректные числа.")
    quit()
except ZeroDivisionError:
    print("Ошибка: деление на ноль.")
    quit()
print(f"Наименьшее общее кратное {int(a)} и {int(b)}: {least_common_multiple}")
