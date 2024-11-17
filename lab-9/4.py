"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №9 Задание 4

Задана матрица D и массив I, содержащий номера строк, для которых
необходимо определить максимальный элемент. Значения максимальных
элементов запомнить в массиве R. Определить среднее арифметическое
вычисленных максимальных значений.
"""

from tabulate import tabulate
from utility.matrix_input import input_int_matrix
from utility.array_input import input_int_array

def find_max_elements(matrix, row_indices):
    """Находит максимальные элементы в указанных строках матрицы."""
    max_elements = []
    for idx in row_indices:
        if 0 <= idx < len(matrix):  # Проверка корректности индекса
            max_elements.append(max(matrix[idx]))
    return max_elements

def calculate_mean(numbers):
    """Вычисляет среднее арифметическое списка чисел."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def print_matrix(matrix, title):
    """Выводит матрицу с заголовком."""
    print(f"\n{title}:")
    headers = [f"[{i}]" for i in range(len(matrix[0]))]
    table = [[f"[{i}]"] + row for i, row in enumerate(matrix)]
    print(tabulate(table, headers=[""] + headers, tablefmt="rounded_grid"))

def print_array(array, title):
    """Выводит массив с заголовком."""
    print(f"\n{title}:")
    headers = [f"[{i}]" for i in range(len(array))]
    print(tabulate([array], headers=headers, tablefmt="rounded_grid"))

def main():
    # Ввод размеров матрицы
    rows = int(input("Введите количество строк матрицы D: "))
    cols = int(input("Введите количество столбцов матрицы D: "))
    
    # Ввод матрицы D
    print("\nВвод матрицы D:")
    matrix_d = input_int_matrix(rows, cols)
    if matrix_d is None:
        print("Ввод отменен")
        return
    
    # Ввод количества индексов
    n_indices = int(input("\nВведите количество индексов строк: "))
    
    # Ввод массива индексов I
    print("\nВвод массива индексов I:")
    indices = input_int_array(n_indices)
    if indices is None:
        print("Ввод отменен")
        return
    
    # Проверка корректности индексов и преобразование в 0-based
    indices = [i - 1 for i in indices]  # Преобразуем в 0-based индексы
    if any(i < 0 or i >= rows for i in indices):
        print("\nОшибка: некоторые индексы выходят за пределы матрицы")
        return
    
    # Находим максимальные элементы
    max_elements = find_max_elements(matrix_d, indices)
    
    # Вычисляем среднее арифметическое
    mean_value = calculate_mean(max_elements)
    
    # Выводим результаты
    print_matrix(matrix_d, "Матрица D")
    print_array([i + 1 for i in indices], "Массив индексов I")  # Выводим 1-based индексы
    print_array(max_elements, "Массив максимальных элементов R")
    print(f"\nСреднее арифметическое максимальных элементов: {mean_value:.2f}")

if __name__ == "__main__":
    main()
