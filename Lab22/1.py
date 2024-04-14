def is_valid_number(num):
    return num.isdigit() and len(num) == 6


while True:
    N = input("Введите меньший номер билета (шестизначное число): ")
    if is_valid_number(N):
        break
    else:
        print("Некорректный ввод. Повторите попытку.")

while True:
    M = input("Введите больший номер билета (шестизначное число): ")
    if is_valid_number(M):
        break
    else:
        print("Некорректный ввод. Повторите попытку.")

count = 0
for num in range(int(N), int(M) + 1):
    str_num = str(num)
    if sum(map(int, str_num[:3])) == sum(map(int, str_num[3:])):
        count += 1

print(f"Количество счастливых билетов на катушке: {count}")
