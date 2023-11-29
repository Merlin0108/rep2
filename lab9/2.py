import re
def count_words(sentence):
    # Функция для подсчета количества слов в предложении
    words = sentence.split()
    return len(words)


def extract_sentences(input_file, output_file, min_words):
    try:
        with open(input_file, 'r') as file:
            text = file.read().replace('\n', '')

            # Разделим текст на предложения с помощью символов ".", "?", "!"
            sentences = re.split('[.!?]', text)

            with open(output_file, 'w') as file:
                for sentence in sentences:
                    # Проверяем количество слов в предложении
                    if count_words(sentence) > min_words:
                        file.write(sentence + '\n')

    except FileNotFoundError:
        print("Файл не найден.")


# Пример использования функции
input_file = 'input1.txt'
output_file = 'output1.txt'
try:
    min_words = int(input())
    extract_sentences(input_file, output_file, min_words)
    print("Ваша транспонированная матрица записана в output1.txt")
except ValueError:
    print("Введено не число")
