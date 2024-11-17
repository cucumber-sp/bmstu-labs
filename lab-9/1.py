"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №9 Задание 1

Даны два одномерных целочисленных массива A и B. 
Сформировать матрицу M, такую что m[i][j] = a[i] * b[j]
Определить количество полных квадратов в каждой строке матрицы.
"""

import math
from tabulate import tabulate
from utility.array_input import input_int_array

def is_perfect_square(n):
    """Проверяет, является ли число полным квадратом."""
    if n < 0:
        return False
    root = int(math.sqrt(n))
    return root * root == n

def count_perfect_squares(row):
    """Подсчитывает количество полных квадратов в строке."""
    return sum(1 for x in row if is_perfect_square(x))

def create_matrix(a, b):
    """Создает матрицу M, где m[i][j] = a[i] * b[j]."""
    return [[a[i] * b[j] for j in range(len(b))] for i in range(len(a))]

def main():
    # Ввод размеров массивов
    size_a = int(input("Введите размер первого массива A: "))
    size_b = int(input("Введите размер второго массива B: "))
    
    # Ввод массивов
    print("\nВвод массива A:")
    a = input_int_array(size_a)
    if a is None:
        print("Ввод отменен")
        return
        
    print("\nВвод массива B:")
    b = input_int_array(size_b)
    if b is None:
        print("Ввод отменен")
        return

    # Создание матрицы M
    m = create_matrix(a, b)
    
    # Подсчет полных квадратов в каждой строке
    s = [count_perfect_squares(row) for row in m]
    
    # Формирование таблицы для вывода
    headers = [f"B[{i}]" for i in range(len(b))] + ["Кол-во\nквадратов"]
    table = []
    for i, row in enumerate(m):
        table.append([f"A[{i}]"] + row + [s[i]])
    
    # Вывод результата
    print("\nРезультат:")
    print(tabulate(table, headers=headers, tablefmt="rounded_grid"))

if __name__ == "__main__":
    main()
