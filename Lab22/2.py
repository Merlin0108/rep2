import csv


def read_csv_file(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


def write_csv_file(filename, data):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)


def filter_countries_by_income(data, min_income, max_income):
    filtered_countries = [country for country in data if min_income <= float(country[2]) <= max_income]
    return filtered_countries


def sort_countries_by_inflation(data):
    sorted_countries = sorted(data, key=lambda x: float(x[3]))
    return sorted_countries


try:
    filename = 'countries.csv'
    output_filename_1 = 'countries_by_income.csv'
    output_filename_2 = 'countries_by_inflation.csv'
    countries_data = read_csv_file(filename)
    print(countries_data)
    # a. Создание CSV-файла с данными о странах по показателю доходов
    min_income = float(input("Введите минимальный показатель доходов: "))
    max_income = float(input("Введите максимальный показатель доходов: "))
    filtered_countries_income = filter_countries_by_income(countries_data, min_income, max_income)
    write_csv_file(output_filename_1, filtered_countries_income)
    print(f"Данные о странах с показателем доходов от {min_income} до {max_income} записаны в файл {output_filename_1}")

    # b. Создание CSV-файла с данными о странах, упорядоченных по показателю инфляции
    sorted_countries_inflation = sort_countries_by_inflation(countries_data)
    write_csv_file(output_filename_2, sorted_countries_inflation)
    print(f"Данные о странах, упорядоченные по показателю инфляции, записаны в файл {output_filename_2}")

except Exception as e:
    print(f"Произошла ошибка: {e}")
