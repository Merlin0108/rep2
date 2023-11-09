import re


def is_valid_car_number(input_str):
    try:
        if len(input_str) != 6:
            raise ValueError("Неверная длина строки. Должно быть 6 символов")

        pattern = re.compile(r'^[A-Za-z]{2}\d{3}[A-Za-z]{1}$')
        if not pattern.match(input_str):
            raise ValueError("Неверный формат строки. Должны быть 2 буквы, 3 цифры и 1 буква")

        if not input_str[:2].isalpha() or not input_str[5].isalpha():
            raise ValueError("Неверные буквы. Должны быть только латинские буквы")

        return True

    except ValueError as e:
        print(f"Ошибка: {e}")
        return False


input_str = input("Введите номер автомобиля (две буквы, три цифры, одна буква): ")

if is_valid_car_number(input_str):
    print("Введенная строка является номером автомобиля.")
else:
    print("Введенная строка не является номером автомобиля.")
