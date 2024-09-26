# Автор: Онищенко Андрей, группа ИУ7-12Б

# Ввод исходных данных
import math


triangle_point1_x = float(input("Введите координату x вершины треугольника 1: "))
triangle_point1_y = float(input("Введите координату y вершины треугольника 1: "))
triangle_point2_x = float(input("Введите координату x вершины треугольника 2: "))
triangle_point2_y = float(input("Введите координату y вершины треугольника 2: "))
triangle_point3_x = float(input("Введите координату x вершины треугольника 3: "))
triangle_point3_y = float(input("Введите координату y вершины треугольника 3: "))

point_x = float(input("Введите координату x точки: "))
point_y = float(input("Введите координату y точки: "))

# Стороны треугольника
a = (
    (triangle_point2_x - triangle_point1_x) ** 2
    + (triangle_point2_y - triangle_point1_y) ** 2
) ** 0.5
b = (
    (triangle_point3_x - triangle_point1_x) ** 2
    + (triangle_point3_y - triangle_point1_y) ** 2
) ** 0.5
c = (
    (triangle_point3_x - triangle_point2_x) ** 2
    + (triangle_point3_y - triangle_point2_y) ** 2
) ** 0.5


# Является ли треугольником
if not (a + b > c and a + c > b and b + c > a):
    print("Не треугольник")
else:
    print(f"Сторона a: {a:.7g}")
    print(f"Сторона b: {b:.7g}")
    print(f"Сторона c: {c:.7g}")

    # Углы треугольника
    angle1 = abs(
        (
            math.atan2(
                triangle_point3_y - triangle_point1_y,
                triangle_point3_x - triangle_point1_x,
            )
            - math.atan2(
                triangle_point2_y - triangle_point1_y,
                triangle_point2_x - triangle_point1_x,
            )
        )
    )
    angle2 = abs(
        (
            math.atan2(
                triangle_point3_y - triangle_point2_y,
                triangle_point3_x - triangle_point2_x,
            )
            - math.atan2(
                triangle_point1_y - triangle_point2_y,
                triangle_point1_x - triangle_point2_x,
            )
        )
    )
    angle3 = abs(
        (
            math.atan2(
                triangle_point1_y - triangle_point3_y,
                triangle_point1_x - triangle_point3_x,
            )
            - math.atan2(
                triangle_point2_y - triangle_point3_y,
                triangle_point2_x - triangle_point3_x,
            )
        )
    )

    smallest_angle = min(angle1, angle2, angle3)

    # Длина медианы из наименьшего угла
    # Находим расстояние от вершины до средней точки противоположной стороны

    if smallest_angle == angle1:
        medium_x = (triangle_point2_x + triangle_point3_x) / 2
        medium_y = (triangle_point2_y + triangle_point3_y) / 2
        distance = (
            (triangle_point1_x - medium_x) ** 2 + (triangle_point1_y - medium_y) ** 2
        ) ** 0.5

    elif smallest_angle == angle2:
        medium_x = (triangle_point1_x + triangle_point3_x) / 2
        medium_y = (triangle_point1_y + triangle_point3_y) / 2
        distance = (
            (triangle_point2_x - medium_x) ** 2 + (triangle_point2_y - medium_y) ** 2
        ) ** 0.5

    elif smallest_angle == angle3:
        medium_x = (triangle_point1_x + triangle_point2_x) / 2
        medium_y = (triangle_point1_y + triangle_point2_y) / 2
        distance = (
            (triangle_point3_x - medium_x) ** 2 + (triangle_point3_y - medium_y) ** 2
        ) ** 0.5

    print(f"Длина медианы: {distance:.7g}")

    # Является ли треугольник остроугольным
    if math.degrees(max(angle1, angle2, angle3)) < 90:
        print("Треугольник остроугольный")
    else:
        print("Треугольник не остроугольный")

    # Вычисляем барицентрические координаты точки P с учетом треугольника ABC
    denominator = (triangle_point2_y - triangle_point3_y) * (
        triangle_point1_x - triangle_point3_x
    ) + (triangle_point3_x - triangle_point2_x) * (
        triangle_point1_y - triangle_point3_y
    )

    baricentric_a = (
        (triangle_point2_y - triangle_point3_y) * (point_x - triangle_point3_x)
        + (triangle_point3_x - triangle_point2_x) * (point_y - triangle_point3_y)
    ) / denominator
    baricentric_b = (
        (triangle_point3_y - triangle_point1_y) * (point_x - triangle_point3_x)
        + (triangle_point1_x - triangle_point3_x) * (point_y - triangle_point3_y)
    ) / denominator
    baricentric_c = 1 - baricentric_a - baricentric_b

    # Если все барицентрические координаты больше или равны нулю, то точка принадлежит треугольнику
    if not (baricentric_a >= 0 and baricentric_b >= 0 and baricentric_c >= 0):
        print("Точка не принадлежит треугольнику")
    else:
        print("Точка принадлежит треугольнику")

        distance_a = (
            abs(
                (triangle_point2_y - triangle_point1_y) * point_x
                - (triangle_point2_x - triangle_point1_x) * point_y
                + triangle_point2_x * triangle_point1_y
                - triangle_point2_y * triangle_point1_x
            )
            / (
                (triangle_point2_y - triangle_point1_y) ** 2
                + (triangle_point2_x - triangle_point1_x) ** 2
            )
            ** 0.5
        )
        distance_b = (
            abs(
                (triangle_point3_y - triangle_point1_y) * point_x
                - (triangle_point3_x - triangle_point1_x) * point_y
                + triangle_point3_x * triangle_point1_y
                - triangle_point3_y * triangle_point1_x
            )
            / (
                (triangle_point3_y - triangle_point1_y) ** 2
                + (triangle_point3_x - triangle_point1_x) ** 2
            )
            ** 0.5
        )
        distance_c = (
            abs(
                (triangle_point3_y - triangle_point2_y) * point_x
                - (triangle_point3_x - triangle_point2_x) * point_y
                + triangle_point3_x * triangle_point2_y
                - triangle_point3_y * triangle_point2_x
            )
            / (
                (triangle_point3_y - triangle_point2_y) ** 2
                + (triangle_point3_x - triangle_point2_x) ** 2
            )
            ** 0.5
        )

        print(
            f"Расстояние от точки до наиболее удаленной стороны треугольника: {max(distance_a, distance_b, distance_c):.7g}"
        )
