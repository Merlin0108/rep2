def geometric_progression_nth_term(a, r, n):
    if n == 1:
        return a
    return geometric_progression_nth_term(a, r, n - 1) * r


def geometric_progression_sum(a, r, n):
    if n == 0:
        return 0
    return a + geometric_progression_sum(a * r, r, n - 1)


try:
    a = float(input("Введите первый элемент: "))
    r = float(input("Введите знаменатель: "))
    n = int(input("Введите количество членов: "))

    # Геометрическая прогрессия
    nth_term = geometric_progression_nth_term(a, r, n)
    progression_sum = geometric_progression_sum(a, r, n)

except ValueError:
    print("Ошибка ввода. Пожалуйста, введите корректные числа.")
except ZeroDivisionError:
    print("Ошибка: деление на ноль.")
    quit()

print(f"{n}-й член геометрической прогрессии: {nth_term}")
print(f"Сумма {n} членов геометрической прогрессии: {progression_sum}")
