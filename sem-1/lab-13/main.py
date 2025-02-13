"""
Автор: Онищенко Андрей
Группа: ИУ7-12Б
Лабораторная работа №13 "База данных в текстовом файле"

База данных фильмов с полями:
- Название фильма
- Год выпуска
- Рейтинг
- Режиссер
"""

import os

SEPARATOR = "|"
ESCAPE_CHAR = "\\"
MIN_YEAR = 1888
CURRENT_YEAR = 2024
FIELDS = ["Название фильма", "Год выпуска", "Рейтинг", "Режиссер"]
INITIAL_RECORDS = [
    ("Inception|The Dream", 2010, 8.8, "Christopher Nolan"),
    ("The Shawshank Redemption", 1994, 9.3, "Frank Darabont"),
    ("The Dark Knight", 2008, 9.0, "Christopher Nolan"),
    ("Pulp Fiction", 1994, 8.9, "Quentin Tarantino"),
]


def clear_screen():
    """Очищает экран консоли."""
    os.system("cls" if os.name == "nt" else "clear")


def escape_field(field):
    """Экранирует специальные символы в поле."""
    return str(field).replace(SEPARATOR, ESCAPE_CHAR + SEPARATOR)


def unescape_field(field):
    """Убирает экранирование специальных символов из поля."""
    return field.replace(ESCAPE_CHAR + SEPARATOR, SEPARATOR)


def parse_line(line):
    """Разбирает строку на поля с учетом экранирования."""
    fields = []
    current_field = ""
    i = 0
    while i < len(line):
        if line[i] == ESCAPE_CHAR and i + 1 < len(line):
            current_field += line[i + 1]
            i += 2
        elif line[i] == SEPARATOR:
            fields.append(current_field)
            current_field = ""
            i += 1
        else:
            current_field += line[i]
            i += 1
    fields.append(current_field)
    return fields


def format_record(fields):
    """Форматирует поля в строку записи."""
    return SEPARATOR.join(escape_field(f) for f in fields)


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


def init_database(filename):
    """Инициализирует базу данных начальными записями."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(SEPARATOR.join(FIELDS) + "\n")
            for record in INITIAL_RECORDS:
                f.write(format_record(record) + "\n")
        print("\nБаза данных успешно инициализирована!")
    except Exception as e:
        print(f"\nОшибка при инициализации базы данных: {e}")


def display_database(filename):
    """Выводит содержимое базы данных в виде таблицы."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            header = f.readline().strip().split(SEPARATOR)
            lines = f.readlines()

            # Определяем ширину столбцов
            widths = [len(h) for h in header]
            for line in lines:
                fields = [unescape_field(f) for f in parse_line(line.strip())]
                widths = [max(w, len(str(f))) for w, f in zip(widths, fields)]

            # Выводим таблицу
            row_format = " | ".join(f"{{:<{w}}}" for w in widths)
            print("\n" + row_format.format(*header))
            print("-" * (sum(widths) + 3 * (len(widths) - 1)))
            for line in lines:
                fields = [unescape_field(f) for f in parse_line(line.strip())]
                print(row_format.format(*fields))
    except FileNotFoundError:
        print("\nФайл базы данных не найден!")
    except Exception as e:
        print(f"\nОшибка при чтении базы данных: {e}")


def add_record(filename):
    """Добавляет новую запись в конец базы данных."""
    if not os.path.exists(filename):
        print("\nФайл базы данных не найден!")
        return

    try:
        # Получаем данные с валидацией
        title = get_valid_input(
            "Название фильма: ", lambda x: bool(x), "Название не может быть пустым!"
        )

        year = int(
            get_valid_input(
                "Год выпуска: ",
                lambda x: x.isdigit() and MIN_YEAR <= int(x) <= CURRENT_YEAR,
                f"Год должен быть между {MIN_YEAR} и {CURRENT_YEAR}!",
            )
        )

        rating = float(
            get_valid_input(
                "Рейтинг (0-10): ",
                lambda x: x.replace(".", "").isdigit() and 0 <= float(x) <= 10,
                "Рейтинг должен быть от 0 до 10!",
            )
        )

        director = get_valid_input(
            "Режиссер: ", lambda x: bool(x), "Имя режиссера не может быть пустым!"
        )

        # Записываем новую запись
        record = format_record([title, year, rating, director])
        with open(filename, "a", encoding="utf-8") as f:
            f.write(record + "\n")
        print("\nЗапись успешно добавлена!")
    except Exception as e:
        print(f"\nОшибка при добавлении записи: {e}")


def search_records(filename, field_indices, search_values):
    """Общая функция поиска записей."""
    if not os.path.exists(filename):
        print("\nФайл базы данных не найден!")
        return

    try:
        found = False
        with open(filename, "r", encoding="utf-8") as f:
            f.readline()  # Пропускаем заголовок
            for line in f:
                fields = parse_line(line.strip())
                matches = []

                for idx, search_value in zip(field_indices, search_values):
                    field = fields[idx]
                    if idx in [1, 2]:  # Числовые поля
                        try:
                            matches.append(float(field) == float(search_value))
                        except ValueError:
                            matches.append(False)
                    else:  # Текстовые поля
                        matches.append(
                            search_value.lower() in unescape_field(field).lower()
                        )

                if all(matches):
                    print(" | ".join(unescape_field(f) for f in fields))
                    found = True

        if not found:
            print("Записи не найдены!")
    except Exception as e:
        print(f"Ошибка при поиске: {e}")


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


def main():
    """Основная функция программы."""
    current_file = None

    while True:
        clear_screen()
        print(
            f"{'Текущий файл: ' + current_file if current_file else 'Файл не выбран'}"
        )

        print("\nМеню:")
        print("1. Выбрать файл для работы")
        print("2. Инициализировать базу данных")
        print("3. Вывести содержимое базы данных")
        print("4. Добавить запись в конец базы данных")
        print("5. Поиск по одному полю")
        print("6. Поиск по двум полям")
        print("0. Выход")

        try:
            choice = input("\nВыберите пункт меню: ")

            if choice == "0":
                print("\nДо свидания!")
                break
            elif choice == "1":
                current_file = get_valid_input(
                    "\nВведите путь к файлу: ",
                    lambda x: bool(x.strip()),
                    "Путь не может быть пустым!",
                )
                current_file = os.path.abspath(current_file)
                print(f"\nВыбран файл: {current_file}")
            elif not current_file:
                print("\nСначала выберите файл!")
            elif choice == "2":
                init_database(current_file)
            elif choice == "3":
                display_database(current_file)
            elif choice == "4":
                add_record(current_file)
            elif choice == "5":
                indices, values = get_search_params(1)
                search_records(current_file, indices, values)
            elif choice == "6":
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
