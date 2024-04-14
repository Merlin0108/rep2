def check_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False

    sides = [a, b, c]
    sides.sort()

    if sides[0] + sides[1] > sides[2]:
        if sides[0] ** 2 + sides[1] ** 2 > sides[2] ** 2:
            return "Треугольник остроугольный"
        elif sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
            return "Треугольник прямоугольный"
        else:
            return "Треугольник тупоугольный"
    else:
        return False


a = int(input("Введите длинну стороны a: "))
b = int(input("Введите длинну стороны b: "))
c = int(input("Введите длинну стороны c: "))

result = check_triangle(a, b, c)

if result:
    print("Треугольнык со сторанами {}, {} и {} существует.".format(a, b, c))
    print(result)
else:
    print("Треугольнык со сторанами {}, {} и {} не существует.".format(a, b, c))
