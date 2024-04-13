def arithmetic_progression_nth_term(a, d, n):
    if n == 0:
        return a
    return a + d * (n - 1)


try:
    a = float(input("Введите первый элемент: "))
    r = float(input("Введите разнсть: "))
    n = int(input("Введите количество членов: "))
    # Арифметическая прогрессия
    nth_term_arithmetic = arithmetic_progression_nth_term(a, r, n)
except ValueError:
    print("Ошибка ввода. Пожалуйста, введите корректные числа.")
    quit()
except ZeroDivisionError:
    print("Ошибка: деление на ноль.")
    quit()
print(f"{n}-й член арифметической прогрессии: {nth_term_arithmetic}")
