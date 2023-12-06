def read_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = []
            for line in file:
                line = line.strip().split(' ')
                if len(line) == 2:
                    surname, birth_year = line
                    data.append((surname, int(birth_year)))
            return data
    except FileNotFoundError:
        print("File not found!")

def sort_data(data):
    data.sort(key=lambda x: x[0])  # Сортировка по фамилии
    data.sort(key=lambda x: x[1])  # Сортировка по возрасту

    return data[::-1]

def print_data(data):
    for item in data:
        print(item[0], item[1])

filename = "people.txt"
data = read_data(filename)
if data:
    sorted_data = sort_data(data)
    print_data(sorted_data)