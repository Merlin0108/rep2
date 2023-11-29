import math


def get_angle():
    while True:
        try:
            angle = float(input("Введите угол в градусах: "))
            return angle
        except ValueError:
            print("Ошибка! Введите число.")


def convert_to_radians(angle):
    return math.radians(angle)


def calculate_trigonometry(angle):
    sin_value = math.sin(angle)
    cos_value = math.cos(angle)
    tan_value = math.tan(angle)
    return sin_value, cos_value, tan_value


def print_trigonometry(sin_value, cos_value, tan_value):
    print(f"Синус угла: {sin_value}")
    print(f"Косинус угла: {cos_value}")
    print(f"Тангенс угла: {tan_value}")


angle = get_angle()
angle_radians = convert_to_radians(angle)
sin_value, cos_value, tan_value = calculate_trigonometry(angle_radians)
print_trigonometry(sin_value, cos_value, tan_value)
