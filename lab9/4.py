def generate_table_of_contents(input_file_path, output_file_path):
    try:
        # Проверяем существование файла
        with open(input_file_path, 'r') as input_file:
            # Читаем текст из файла
            text = input_file.read()

        # Разделяем текст на строки
        lines = text.split('\n')
        # Открываем файл для записи оглавления
        with open(output_file_path, 'w') as output_file:
            # Обрабатываем каждую строку текста
            for line in lines:
                line = line.strip()

                # Если строка начинается со слова "Глава" или "Chapter"
                if line.startswith('Глава') or line.startswith('Chapter'):
                    # Проверяем, что это действительно строка с номером главы
                    try:
                        # Получаем номер главы
                        chapter_number = int(line.split()[1])
                    except ValueError:
                        # Пропускаем строку, если она не содержит номер главы
                        continue

                    # Получаем название главы на следующей строке
                    chapter_title = lines[lines.index(line) + 1]

                    # Записываем информацию о главе в файл оглавления
                    output_file.write(f"Глава {chapter_number}. {chapter_title}\n")

    except FileNotFoundError:
        print("Файл не найден")


# Пример использования
generate_table_of_contents('input3.txt', 'output3.txt')
