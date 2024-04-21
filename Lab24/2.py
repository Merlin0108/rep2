import os


def get_directory_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size


try:
    path = input("Введите путь до заархивированной директории: ")
    if not os.path.exists(path):
        raise FileNotFoundError("Указанная директория не существует")

    total_size = get_directory_size(path)
    print(f"Суммарный размер файлов в директории {path}: {total_size} байт")

except Exception as e:
    print(f"Произошла ошибка: {e}")
