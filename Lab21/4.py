def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        return "Некорректные данные"

    bmi = weight / (height ** 2)
    return bmi


# Рассчет для человека с данными значениями
weight1 = 108.85
height1 = 1.85
bmi1 = calculate_bmi(weight1, height1)
print(f"Индекс массы тела для человека с ростом {height1} м и весом {weight1} кг: {bmi1}")

# Ввод пользователем и рассчет ИМТ
weight_user = float(input("Введите свой вес в килограммах: "))
height_user = float(input("Введите свой рост в метрах: "))
bmi_user = calculate_bmi(weight_user, height_user)
print(f"Индекс массы тела для вас с ростом {height_user} м и весом {weight_user} кг: {bmi_user}")