def check_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Пожалуйста, введите корректное число.")


employees = []
total_bonus = 0

for i in range(3):
    name = input(f"Введите имя {i + 1}-го сотрудника: ")
    salary = check_input(f"Введите размер оклада для {name}: ")

    bonus = (2 / 3) * salary
    net_salary = salary + bonus - (0.13 * (salary + bonus))

    employees.append((name, bonus, net_salary))
    total_bonus += bonus

print("\nИнформация о премиях:")
for employee in employees:
    print(f"Сотрудник: {employee[0]}, Премия: {employee[1]}, На руки: {employee[2]}")

print(f"\nОбщая сумма премий: {total_bonus}")
