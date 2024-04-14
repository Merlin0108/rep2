while True:
    try:
        salary = float(input("Введите размер оклада сотрудника: "))
        break
    except ValueError:
        print("Ошибка. Введите корректное число.")

bonus = salary * 2 / 3
net_salary = salary + bonus - (salary + bonus) * 0.13

print(f"Квартальная премия: {bonus}")
print(f"Сумма на руки с учётом налога: {net_salary}")
