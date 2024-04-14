num = int(input("Введите сумму цифр: "))

if num < 1 or num > 27:
    print("Некорректная сумма цифр")
else:
    for i in range(100, 1000):
        if sum(int(digit) for digit in str(i)) == num:
            print(i)