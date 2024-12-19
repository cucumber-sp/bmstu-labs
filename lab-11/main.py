import random
import time
from tabulate import tabulate

# Функция сортировки вставками с бинарным поиском
def binary_insertion_sort(arr):
    def binary_search(sub_arr, target):
        left, right = 0, len(sub_arr)
        while left < right:
            mid = (left + right) // 2
            if sub_arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        insert_position = binary_search(arr[:i], key)
        arr = arr[:insert_position] + [key] + arr[insert_position:i] + arr[i + 1:]
        comparisons += i - insert_position
    return arr, comparisons

# Функция для измерения времени сортировки с усреднением
def measure_sort_time_and_swaps(sort_func, arr, runs=5):
    total_time = 0
    total_swaps = 0
    for _ in range(runs):
        start_time = time.perf_counter()  # Более точное измерение времени
        _, swaps = sort_func(arr[:])  # Копируем массив перед сортировкой
        end_time = time.perf_counter()
        total_time += end_time - start_time
        total_swaps += swaps
    return total_time / runs, total_swaps // runs

# Генерация данных для таблицы
def generate_table(sort_func, sizes, runs=5):
    results = []
    for size in sizes:
        ordered = list(range(size))
        random_list = random.sample(range(size * 10), size)
        reverse_ordered = list(range(size, 0, -1))

        # Сбор данных
        t1, k1 = measure_sort_time_and_swaps(sort_func, ordered, runs)
        t2, k2 = measure_sort_time_and_swaps(sort_func, random_list, runs)
        t3, k3 = measure_sort_time_and_swaps(sort_func, reverse_ordered, runs)

        # Формирование строки для каждого размера
        results.append([(t1, k1), (t2, k2), (t3, k3)])
    return results

# Основная программа
if __name__ == "__main__":
    # Этап 1: Ввод массива для проверки
    print("Введите массив целых чисел через пробел:")
    user_array = list(map(int, input().split()))
    sorted_array, comparisons = binary_insertion_sort(user_array)
    print("Отсортированный массив:", sorted_array)
    print("Количество перестановок:", comparisons)

    # Этап 2: Ввод размеров массивов для замеров
    print("\nВведите три размера массива для замеров:")
    sizes = [int(input(f"Размер {i+1}: ")) for i in range(3)]

    # Генерация данных
    table_data = generate_table(binary_insertion_sort, sizes, runs=1)  # 10 прогонов для усреднения

    # Создание таблицы
    rows = []
    for i, row_name in enumerate(["Упорядоченный список", "Случайный список", "Обратный порядок"]):
        rows.append([
            row_name,
            f"{table_data[0][i][0]:.6f}", table_data[0][i][1],
            f"{table_data[1][i][0]:.6f}", table_data[1][i][1],
            f"{table_data[2][i][0]:.6f}", table_data[2][i][1],
        ])

    # Заголовки таблицы
    headers = [
        "Тип массива",
        f"N={sizes[0]} Время", f"N={sizes[0]} Перестановки",
        f"N={sizes[1]} Время", f"N={sizes[1]} Перестановки",
        f"N={sizes[2]} Время", f"N={sizes[2]} Перестановки"
    ]

    # Вывод таблицы
    print("\nРезультаты замеров времени и перестановок:\n")
    print(tabulate(rows, headers=headers, tablefmt="rounded_grid"))
