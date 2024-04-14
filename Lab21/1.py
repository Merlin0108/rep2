def filter_words(start_string, words):
    try:
        if not isinstance(start_string, str) or not isinstance(words, str):
            raise Exception("Введены некорректные данные. Пожалуйста, введите строки.")

        control_word = start_string.strip()
        if len(control_word) == 0:
            raise Exception("Контрольная строка не должна быть пустой.")

        word_list = words.split(';')
        filtered_words = [word.strip() for word in word_list if word.strip().startswith(control_word)]

        return filtered_words

    except Exception as e:
        return f"Ошибка: {str(e)}"


words_input = input("Введите 10 слов, разделенных точкой с запятой: ")
control_input = input("Введите контрольную строку: ")

result = filter_words(control_input, words_input)
print(result)