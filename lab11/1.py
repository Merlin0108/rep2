def is_palindrome(word):
    # Проверяем длину слова
    if len(word) < 3:
        print("Слово должно содержать как минимум 3 символа")
        return False

    stack = []  # Создаем пустой стек

    # Заполняем стек первой половиной слова
    for i in range(len(word) // 2):
        stack.append(word[i])

    # Определяем индекс, с которого нужно сравнивать элементы со стека
    if len(word) % 2 == 0:  # Если длина слова четная
        start_index = len(word) // 2
    else:  # Если длина слова нечетная
        start_index = len(word) // 2 + 1

    # Сравниваем элементы со стека с оставшейся половиной слова
    for i in range(start_index, len(word)):
        if word[i] != stack.pop():
            print("Слово не является палиндромом")
            return False

    print("Слово является палиндромом")
    return True


# Получаем ввод от пользователя
word = input("Введите слово: ")

# Проверяем, является ли слово палиндромом
is_palindrome(word)