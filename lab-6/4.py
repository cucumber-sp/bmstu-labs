"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №6 Подпрограмма 4
"""


list_ = list(map(int, input("Введите список целых чисел: ").split()))

# поиск максимально длинной подподпоследовательности удовлетворяющей Возрастающая последовательность отрицательных чисел, модуль которых является простым числом.

max_subsequence_length = 0
max_subsequence_index = -1

for i, num in enumerate(list_):
    if i < max_subsequence_index:
        continue
    curr_subsequence_length = 1
    abs_num = abs(num)
    is_prime = True
    for d in range(2, int(abs_num ** 0.5) + 1):
        if abs_num % d == 0:
            is_prime = False
            break
    for j, next_num in enumerate(list_[i + 1:], start=i + 1):
        if not is_prime or next_num >= 0 or next_num < num:
            break
        curr_subsequence_length += 1
    if curr_subsequence_length > max_subsequence_length:
        max_subsequence_length = curr_subsequence_length
        max_subsequence_index = i

print(f"Максимальная подпоследовательность: {list_[max_subsequence_index:max_subsequence_index + max_subsequence_length]}")
