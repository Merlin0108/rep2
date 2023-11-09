import re


def remove_all_but_last_occurrence(first_string, second_string):
    if not first_string or not second_string:
        return ("Введены пустые строки")
    pattern = re.escape(second_string)
    result = re.sub(pattern, '', first_string)
    return result



first_string = input("Введите первую строку: ")
second_string = input("Введите вторую строку: ")

result = remove_all_but_last_occurrence(first_string, second_string)
print("Результат:", result)
