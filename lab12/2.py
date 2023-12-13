def arithmetic_progression_nth_term(a, d, n):
    if n == 0:
        return a
    return a + d * (n - 1)


a = float(input("Введите нулевой элемент: "))
r = float(input("Введите знаменатель: "))
n = int(input("Введите количество членов: "))
# Арифметическая прогрессия
nth_term_arithmetic = arithmetic_progression_nth_term(a, r, n)
print(f"c) {n}-й член арифметической прогрессии: {nth_term_arithmetic}")
