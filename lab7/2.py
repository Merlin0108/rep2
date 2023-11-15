def find_unique_chars(first_string, second_string):
    try:
        first_set = set(first_string)
        second_set = set(second_string)
        unique_chars = first_set - second_set
        for char in unique_chars:
            print(char, end='')
    except Exception as e:
        print("Ошибка:", str(e))


first_string = input("Введите первую строку: ")
second_string = input("Введите вторую строку: ")
find_unique_chars(first_string, second_string)
