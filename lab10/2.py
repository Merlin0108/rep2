def count_a(word):
    return word.count("а")


try:
    file_name = "1.txt"
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("Ошибка! Файл не найден!")

lines.sort(key=count_a, reverse=True)
print("Отсортированные строки:")
for line in lines:
    print(line.strip())
