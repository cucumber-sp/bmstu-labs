"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №9 Задание 7

Ввести трёхмерный массив (массив матриц размера X*Y*Z). Вывести срез
массива по большему измерению, индекс среза – середина размерности с
округлением в меньшую сторону.
"""

from tabulate import tabulate
from utility.matrix_input import input_int_matrix

def create_3d_array(x, y, z):
    """Создает трехмерный массив, заполняя его введенными значениями."""
    array_3d = []
    
    for i in range(x):
        print(f"\nВвод матрицы {i + 1} из {x}:")
        matrix = input_int_matrix(y, z)
        if matrix is None:
            return None
        array_3d.append(matrix)
    
    return array_3d

def get_slice(array_3d, x, y, z):
    """Получает срез по наибольшему измерению."""
    # Находим наибольшее измерение
    max_dim = max(x, y, z)
    mid_index = max_dim // 2  # Округление в меньшую сторону
    
    if max_dim == x:  # Срез по X (фиксированная матрица)
        return array_3d[mid_index], "X", mid_index
    elif max_dim == y:  # Срез по Y (строки из каждой матрицы)
        slice_matrix = [[array_3d[i][mid_index][j] for j in range(z)] for i in range(x)]
        return slice_matrix, "Y", mid_index
    else:  # Срез по Z (столбцы из каждой матрицы)
        slice_matrix = [[array_3d[i][j][mid_index] for j in range(y)] for i in range(x)]
        return slice_matrix, "Z", mid_index

def print_3d_array(array_3d, x, y, z):
    """Выводит трехмерный массив как набор матриц."""
    for i in range(x):
        print(f"\nМатрица {i + 1}:")
        headers = [f"[{j}]" for j in range(z)]
        table = [[f"[{j}]"] + array_3d[i][j] for j in range(y)]
        print(tabulate(table, headers=[""] + headers, tablefmt="rounded_grid"))

def print_slice(slice_matrix, axis, index):
    """Выводит срез массива."""
    print(f"\nСрез по оси {axis} с индексом {index}:")
    headers = [f"[{i}]" for i in range(len(slice_matrix[0]))]
    table = [[f"[{i}]"] + row for i, row in enumerate(slice_matrix)]
    print(tabulate(table, headers=[""] + headers, tablefmt="rounded_grid"))

def main():
    # Ввод размерностей
    x = int(input("Введите размер X (количество матриц): "))
    y = int(input("Введите размер Y (количество строк в матрице): "))
    z = int(input("Введите размер Z (количество столбцов в матрице): "))
    
    # Создание трехмерного массива
    array_3d = create_3d_array(x, y, z)
    if array_3d is None:
        print("Ввод отменен")
        return
    
    # Вывод исходного массива
    print("\nИсходный трехмерный массив:")
    print_3d_array(array_3d, x, y, z)
    
    # Получение и вывод среза
    slice_matrix, axis, index = get_slice(array_3d, x, y, z)
    print_slice(slice_matrix, axis, index)

if __name__ == "__main__":
    main()
