def input_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Пожалуйста, введите целое число.")


M = input_integer("Введите первое число M: ")
N = input_integer("Введите второе число N: ")

digits_M = len(str(abs(M)))
digits_N = len(str(abs(N)))

if digits_M > digits_N:
    print("В числе M больше цифр.")
elif digits_N > digits_M:
    print("В числе N больше цифр.")
else:
    print("В числах M и N одинаковое количество цифр.")
