"""
Автор: Онищенко Андрей
Группа: ИУ7-12Б
Лабораторная работа №14 "База данных в бинарном файле"

База данных фильмов с полями:
- Название фильма (строка, 40 символов)
- Год выпуска (целое число)
- Рейтинг (число с плавающей точкой)
- Режиссер (строка, 40 символов)
"""

import os
import struct

# Константы
MIN_YEAR = 1888
CURRENT_YEAR = 2024
TITLE_SIZE = 40
DIRECTOR_SIZE = 40
FIELDS = ["Название фильма", "Год выпуска", "Рейтинг", "Режиссер"]

# Формат записи для struct:
# - Название фильма: 40 символов (кодировка utf-8, дополненная нулями)
# - Год выпуска: целое число (4 байта)
# - Рейтинг: число с плавающей точкой (4 байта)
# - Режиссер: 40 символов (кодировка utf-8, дополненная нулями)
RECORD_FORMAT = f'={TITLE_SIZE}sif{DIRECTOR_SIZE}s'
RECORD_SIZE = struct.calcsize(RECORD_FORMAT)

INITIAL_RECORDS = [
    ("Inception", 2010, 8.8, "Christopher Nolan"),
    ("The Shawshank Redemption", 1994, 9.3, "Frank Darabont"),
    ("The Dark Knight", 2008, 9.0, "Christopher Nolan"),
    ("Pulp Fiction", 1994, 8.9, "Quentin Tarantino")
]

def clear_screen():
    """Очищает экран консоли."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pad_string(s, size):
    """Дополняет строку нулями до указанного размера."""
    encoded = s.encode('utf-8')
    return encoded[:size].ljust(size, b'\0')

def unpad_string(s):
    """Убирает нули из строки и декодирует её."""
    return s.decode('utf-8').rstrip('\0')

def pack_record(title, year, rating, director):
    """Упаковывает запись в бинарный формат."""
    return struct.pack(RECORD_FORMAT,
                      pad_string(title, TITLE_SIZE),
                      year,
                      rating,
                      pad_string(director, DIRECTOR_SIZE))

def unpack_record(binary_data):
    """Распаковывает запись из бинарного формата."""
    title, year, rating, director = struct.unpack(RECORD_FORMAT, binary_data)
    return (unpad_string(title), year, rating, unpad_string(director))

def get_valid_input(prompt, validator, error_msg):
    """Получает валидный ввод от пользователя."""
    while True:
        try:
            value = input(prompt).strip()
            if validator(value):
                return value
            print(error_msg)
        except ValueError:
            print(error_msg)

def get_record_count(file):
    """Возвращает количество записей в файле."""
    file.seek(0, 2)  # Перемещаемся в конец файла
    return file.tell() // RECORD_SIZE

def init_database(filename):
    """Инициализирует базу данных начальными записями."""
    try:
        with open(filename, 'wb') as f:
            for title, year, rating, director in INITIAL_RECORDS:
                f.write(pack_record(title, year, rating, director))
        print("\nБаза данных успешно инициализирована!")
    except Exception as e:
        print(f"\nОшибка при инициализации базы данных: {e}")

def display_database(filename):
    """Выводит содержимое базы данных в виде таблицы."""
    try:
        with open(filename, 'rb') as f:
            # Определяем ширину столбцов
            widths = [len(field) for field in FIELDS]
            records = []
            
            # Читаем все записи и определяем максимальную ширину
            while True:
                data = f.read(RECORD_SIZE)
                if not data:
                    break
                if len(data) < RECORD_SIZE:
                    print("\nОшибка: файл поврежден!")
                    return
                
                record = unpack_record(data)
                records.append(record)
                formatted_record = [format_field(field) for field in record]
                widths = [max(w, len(str(field))) for w, field in zip(widths, formatted_record)]
            
            if not records:
                print("\nБаза данных пуста!")
                return
            
            # Выводим таблицу
            row_format = ' | '.join(f'{{:<{w}}}' for w in widths)
            print('\n' + row_format.format(*FIELDS))
            print('-' * (sum(widths) + 3 * (len(widths) - 1)))
            
            for i, record in enumerate(records, 1):
                formatted_record = [format_field(field) for field in record]
                print(f"{i}. " + row_format.format(*formatted_record))
    
    except FileNotFoundError:
        print("\nФайл базы данных не найден!")
    except Exception as e:
        print(f"\nОшибка при чтении базы данных: {e}")

def add_record(filename):
    """Добавляет новую запись в указанную позицию базы данных."""
    if not os.path.exists(filename):
        print("\nФайл базы данных не найден!")
        return
    
    try:
        with open(filename, 'rb+') as f:
            record_count = get_record_count(f)
            
            # Получаем позицию для вставки
            while True:
                try:
                    pos = int(input(f"\nВведите позицию для вставки (1-{record_count + 1}): "))
                    if 1 <= pos <= record_count + 1:
                        break
                    print(f"Позиция должна быть от 1 до {record_count + 1}!")
                except ValueError:
                    print("Введите корректное число!")
            
            # Получаем данные новой записи
            title = get_valid_input("Название фильма: ",
                                  lambda x: bool(x) and len(x.encode('utf-8')) <= TITLE_SIZE,
                                  f"Название должно быть непустым и не длиннее {TITLE_SIZE} байт!")
            
            year = int(get_valid_input("Год выпуска: ",
                                     lambda x: x.isdigit() and MIN_YEAR <= int(x) <= CURRENT_YEAR,
                                     f"Год должен быть между {MIN_YEAR} и {CURRENT_YEAR}!"))
            
            rating = float(get_valid_input("Рейтинг (0-10): ",
                                         lambda x: x.replace('.', '').isdigit() and 0 <= float(x) <= 10,
                                         "Рейтинг должен быть от 0 до 10!"))
            
            director = get_valid_input("Режиссер: ",
                                     lambda x: bool(x) and len(x.encode('utf-8')) <= DIRECTOR_SIZE,
                                     f"Имя режиссера должно быть непустым и не длиннее {DIRECTOR_SIZE} байт!")
            
            # Создаем новую запись
            new_record = pack_record(title, year, rating, director)
            
            # Вставляем запись в указанную позицию
            pos = pos - 1  # Преобразуем в индекс (0-based)
            f.seek(0, 2)  # Перемещаемся в конец файла
            file_size = f.tell()
            
            # Сдвигаем существующие записи
            for i in range(file_size - RECORD_SIZE, pos * RECORD_SIZE - 1, -RECORD_SIZE):
                f.seek(i)
                data = f.read(RECORD_SIZE)
                f.seek(i + RECORD_SIZE)
                f.write(data)
            
            # Записываем новую запись
            f.seek(pos * RECORD_SIZE)
            f.write(new_record)
            
            print("\nЗапись успешно добавлена!")
    
    except Exception as e:
        print(f"\nОшибка при добавлении записи: {e}")

def delete_record(filename):
    """Удаляет запись из указанной позиции базы данных."""
    if not os.path.exists(filename):
        print("\nФайл базы данных не найден!")
        return
    
    try:
        with open(filename, 'rb+') as f:
            record_count = get_record_count(f)
            if record_count == 0:
                print("\nБаза данных пуста!")
                return
            
            # Получаем номер удаляемой записи
            while True:
                try:
                    pos = int(input(f"\nВведите номер удаляемой записи (1-{record_count}): "))
                    if 1 <= pos <= record_count:
                        break
                    print(f"Номер должен быть от 1 до {record_count}!")
                except ValueError:
                    print("Введите корректное число!")
            
            pos = pos - 1  # Преобразуем в индекс (0-based)
            
            # Сдвигаем записи влево
            for i in range((pos + 1) * RECORD_SIZE, record_count * RECORD_SIZE):
                f.seek(i)
                data = f.read(RECORD_SIZE)
                f.seek(i - RECORD_SIZE)
                f.write(data)
            
            # Обрезаем файл
            f.truncate((record_count - 1) * RECORD_SIZE)
            print("\nЗапись успешно удалена!")
    
    except Exception as e:
        print(f"\nОшибка при удалении записи: {e}")

def float_equals(a, b, epsilon=0.1):
    """Сравнивает два числа с плавающей точкой с учетом погрешности."""
    try:
        return abs(float(a) - float(b)) < epsilon
    except ValueError:
        return False

def search_records(filename, field_indices, search_values):
    """Общая функция поиска записей."""
    if not os.path.exists(filename):
        print("\nФайл базы данных не найден!")
        return
    
    try:
        found = False
        with open(filename, 'rb') as f:
            record_num = 1
            while True:
                data = f.read(RECORD_SIZE)
                if not data:
                    break
                if len(data) < RECORD_SIZE:
                    print("\nОшибка: файл поврежден!")
                    return
                
                record = unpack_record(data)
                matches = []
                
                for idx, search_value in zip(field_indices, search_values):
                    field = record[idx]
                    if idx == 1:  # Год выпуска (целое число)
                        try:
                            matches.append(int(field) == int(search_value))
                        except ValueError:
                            matches.append(False)
                    elif idx == 2:  # Рейтинг (число с плавающей точкой)
                        matches.append(float_equals(field, search_value))
                    else:  # Текстовые поля
                        matches.append(search_value.lower() in str(field).lower())
                
                if all(matches):
                    if not found:
                        print("\nНайденные записи:")
                        found = True
                    formatted_record = [format_field(field) for field in record]
                    print(f"{record_num}. {' | '.join(formatted_record)}")
                
                record_num += 1
        
        if not found:
            print("\nЗаписи не найдены!")
    
    except Exception as e:
        print(f"\nОшибка при поиске: {e}")

def get_search_params(num_fields):
    """Получает параметры поиска от пользователя."""
    indices = []
    values = []
    
    for i in range(num_fields):
        print("\nВыберите поле для поиска:")
        for idx, field in enumerate(FIELDS, 1):
            print(f"{idx}. {field}")
        
        while True:
            try:
                choice = int(input(f"Поле {i + 1}: "))
                if choice in range(1, len(FIELDS) + 1) and (choice - 1) not in indices:
                    indices.append(choice - 1)
                    break
                print("Некорректный выбор!")
            except ValueError:
                print("Введите число!")
        
        values.append(input("Введите значение для поиска: ").strip())
    
    return indices, values

def format_field(field):
    """Форматирует поле для вывода."""
    if isinstance(field, float):
        return f"{field:.1f}"
    return str(field)

def main():
    """Основная функция программы."""
    current_file = None
    
    while True:
        clear_screen()
        print(f"{'Текущий файл: ' + current_file if current_file else 'Файл не выбран'}")
        
        print("\nМеню:")
        print("1. Выбрать файл для работы")
        print("2. Инициализировать базу данных")
        print("3. Вывести содержимое базы данных")
        print("4. Добавить запись")
        print("5. Удалить запись")
        print("6. Поиск по одному полю")
        print("7. Поиск по двум полям")
        print("0. Выход")
        
        try:
            choice = input("\nВыберите пункт меню: ")
            
            if choice == '0':
                print("\nДо свидания!")
                break
            elif choice == '1':
                current_file = get_valid_input("\nВведите путь к файлу: ",
                                             lambda x: bool(x.strip()),
                                             "Путь не может быть пустым!")
                current_file = os.path.abspath(current_file)
                print(f"\nВыбран файл: {current_file}")
            elif not current_file:
                print("\nСначала выберите файл!")
            elif choice == '2':
                init_database(current_file)
            elif choice == '3':
                display_database(current_file)
            elif choice == '4':
                add_record(current_file)
            elif choice == '5':
                delete_record(current_file)
            elif choice == '6':
                indices, values = get_search_params(1)
                search_records(current_file, indices, values)
            elif choice == '7':
                indices, values = get_search_params(2)
                search_records(current_file, indices, values)
            else:
                print("\nНекорректный выбор!")
            
            input("\nНажмите Enter для продолжения...")
        except Exception as e:
            print(f"\nПроизошла ошибка: {e}")
            input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
