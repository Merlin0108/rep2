def count_unique_characters(text):
    try:
        if not text:
            raise ValueError("Пустая строка")
        unique_characters = set(text)
        return len(unique_characters)
    except ValueError as e:
        print(e)
        return 0


text = input("Введите строку текста: ")
count = count_unique_characters(text)
print("Количество уникальных символов:", count)
