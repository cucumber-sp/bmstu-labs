"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №6 Подпрограмма 3
"""
import math



while True:
    list_ = list(map(int, input("Введите список целых чисел (минимум 3 элемента): ").split()))
    if len(list_) < 3:
        print("Лист должен быть не менее 3 элементов")
    else:
        break


required_extremum_k = int(input("Введите номер искомого экстремума: "))
if required_extremum_k < 0:
    required_extremum_k = 0

curr_extremum_k = 0
last_sign = math.copysign(1, list_[1] - list_[0])

for i in range(2, len(list_)):
    curr_sign = math.copysign(1, list_[i] - list_[i - 1])
    if curr_sign != last_sign:
        curr_extremum_k += 1
        if curr_extremum_k == required_extremum_k:
            print(f"Экстремум {required_extremum_k} имеет значение {list_[i - 1]}, индекс {i - 1}.")
            break
        last_sign = curr_sign
else:
    print("Такого экстремума не существует.")
