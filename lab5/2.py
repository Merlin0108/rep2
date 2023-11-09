import re


def get_input():
    try:
        user_input = input("Введите строку: ")
        return user_input
    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем.")
        exit()


def clean_whitespace(input_str):
    cleaned_str = input_str.strip()
    return cleaned_str


def format_sentence(sentence):
    sentence = sentence.lower()
    sentence = sentence.capitalize()
    if not sentence.endswith('.'):
        sentence += '.'
    return sentence


def process_input(input_str):
    cleaned_str = clean_whitespace(input_str)
    sentences = re.split(r'(?<=[.!?])\s+', cleaned_str)
    formatted_sentences = [format_sentence(sentence) for sentence in sentences]
    result_str = ' '.join(formatted_sentences)
    return result_str


try:
    user_input = get_input()
    result = process_input(user_input)
    print("Отформатированная строка:", result)
except Exception as e:
    print("Ошибка:", e)
