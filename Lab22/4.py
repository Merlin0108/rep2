N = int(input("Введите целое неотрицательное число: "))

if N < 0:
    print("Ошибка: введено отрицательное число.")
else:
    factorial = 1
    if N == 0:
        print("Факториал числа 0 равен 1")
    else:
        for i in range(1, N + 1):
            factorial *= i
        print(f"Факториал числа {N} равен {factorial}")
