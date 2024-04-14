import json

# Чтение данных из файла
with open('animals.json') as f:
    data = json.load(f)


# Функция для фильтрации данных по типу
def filter_animals(data, animal_type):
    return [animal for animal in data['animals'] if animal['animal_type'] == animal_type]


# Функция для подсчета количества животных с указанным признаком
def count_animals(data, attribute, value):
    return len([animal for animal in data['animals'] if animal[attribute] == value])


# Функция для поиска животного с наименьшим весом
def find_min_weight_animal(data):
    return min(data['animals'], key=lambda x: x['weight_min'])


birds = filter_animals(data, 'Bird')
print('Данные о птицах:')
for bird in birds:
    print(bird)

diurnal_count = count_animals(data, 'active_time', 'Diurnal')
print('Количество дневных животных:', diurnal_count)

animal_with_min_weight = find_min_weight_animal(data)
print('Животное с наименьшим весом:', animal_with_min_weight)
