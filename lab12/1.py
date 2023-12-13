def geometric_progression_nth_term(a, r, n):
    if n == 0:
        return a
    return r * geometric_progression_nth_term(a, r, n - 1)

def geometric_progression_sum(a, r, n):
    if n == 0:
        return 0
    return geometric_progression_nth_term(a, r, n - 1) + geometric_progression_sum(a, r, n - 1)
try:
    a = float(input("Введите нулевой элемент: "))
    r = float(input("Введите разность: "))
    n = int(input("Введите количество членов: "))

    # Геометрическая прогрессия
    nth_term = geometric_progression_nth_term(a, r, n)
    progression_sum = geometric_progression_sum(a, r, n)

except ValueError:
    print("Ошибка ввода. Пожалуйста, введите корректные числа.")
except ZeroDivisionError:
    print("Ошибка: деление на ноль.")

print(f"a) {n}-й член геометрической прогрессии: {nth_term}")
print(f"b) Сумма {n} членов геометрической прогрессии: {progression_sum}")