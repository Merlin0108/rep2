def invert_string(string):
    stack = []
    inverted_string = ''
    for char in string:
        stack.append(char)
    while stack:
        inverted_string += stack.pop()
    return inverted_string


try:
    input_string = input("Введите строку: ")
    inverted = invert_string(input_string)
    print("Инвертированная строка:", inverted)
except:
    print("Ошибка при обработке строки.")
