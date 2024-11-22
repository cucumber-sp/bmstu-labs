"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №9 Задание защита
"""

def input_matrix():
    # Ввод размеров матрицы
    n = int(input("Введите количество строк матрицы: "))
    m = int(input("Введите количество столбцов матрицы: "))
    
    # Ввод матрицы
    matrix = []
    print("Введите матрицу (0 и 1):")
    for i in range(n):
        while True:
            row = input().split()
            if len(row) == m and all(x in '01' for x in row):
                matrix.append(row)
                break
            print("Ошибка! Введите строку заново (только 0 и 1)")
    return matrix

def process_row(row):
    # Обработка одной строки
    n = len(row)
    result = row.copy()
    
    # Находим позиции единиц
    ones_positions = []
    for i in range(n):
        if row[i] == '1':
            ones_positions.append(i)
    
    # Заменяем нули между единицами на точки
    for i in range(len(ones_positions)-1):
        for j in range(ones_positions[i]+1, ones_positions[i+1]):
            if result[j] == '0':
                result[j] = '.'
    
    return result

def main():
    # Ввод матрицы
    matrix = input_matrix()
    
    # Обработка каждой строки
    processed_matrix = []
    for row in matrix:
        processed_row = process_row(row)
        processed_matrix.append(processed_row)
    
    # Вывод результата
    print("\nРезультат:")
    for row in processed_matrix:
        print(' '.join(row))

if __name__ == "__main__":
    main()
