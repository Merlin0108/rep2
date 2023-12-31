from datetime import datetime


def check_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d %H:%M')
        return True
    except ValueError:
        return False


while True:
    departure_date = input("Введите дату и время отправления в формате 'YYYY-MM-DD HH:MM': ")
    if check_date(departure_date):
        break
    else:
        print("Некорректный формат даты! Попробуйте снова.")

while True:
    arrival_date = input("Введите дату и время прибытия в формате 'YYYY-MM-DD HH:MM': ")
    if check_date(arrival_date):
        break
    else:
        print("Некорректный формат даты! Попробуйте снова.")

duration = arrival_date - departure_date

print("Время поезда в пути:", duration)
