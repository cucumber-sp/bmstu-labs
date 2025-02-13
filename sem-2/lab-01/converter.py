"""
Автор: Онищенко Андрей
Группа: ИУ7-22Б
Лабораторная работа №1 "Калькулятор систем счисления"
Логическая часть программы - конвертация между системами счисления
"""


def decimal_to_base7(decimal_num):
    """
    Конвертирует десятичное число в систему счисления с основанием 7.

    Args:
        decimal_num (float): Десятичное число

    Returns:
        str: Строка, представляющая число в системе счисления с основанием 7
    """
    if decimal_num == 0:
        return "0"

    integer_part = int(abs(decimal_num))
    fractional_part = abs(decimal_num) - integer_part

    integer_result = ""
    while integer_part > 0:
        integer_result = str(integer_part % 7) + integer_result
        integer_part //= 7

    if not integer_result:
        integer_result = "0"

    fractional_result = ""
    precision = 10

    while fractional_part > 0 and len(fractional_result) < precision:
        fractional_part *= 7
        digit = int(fractional_part)
        fractional_result += str(digit)
        fractional_part -= digit

    result = integer_result
    if fractional_result:
        result += "." + fractional_result

    if decimal_num < 0:
        result = "-" + result

    return result


def base7_to_decimal(base7_num):
    """
    Конвертирует число из системы счисления с основанием 7 в десятичную.

    Args:
        base7_num (str): Строка, представляющая число в системе счисления с основанием 7

    Returns:
        float: Десятичное число
    """
    if not base7_num or base7_num == "0":
        return 0.0

    is_negative = base7_num.startswith("-")
    if is_negative:
        base7_num = base7_num[1:]

    parts = base7_num.split(".")
    integer_part = parts[0]
    fractional_part = parts[1] if len(parts) > 1 else ""

    decimal_result = 0
    for i, digit in enumerate(reversed(integer_part)):
        if not digit.isdigit() or int(digit) >= 7:
            raise ValueError("Неверный формат числа")
        decimal_result += int(digit) * (7**i)

    for i, digit in enumerate(fractional_part, 1):
        if not digit.isdigit() or int(digit) >= 7:
            raise ValueError("Неверный формат числа")
        decimal_result += int(digit) * (7**-i)

    return -decimal_result if is_negative else decimal_result


def validate_base7(number_str):
    """
    Проверяет, является ли строка корректным числом в системе счисления с основанием 7.

    Args:
        number_str (str): Проверяемая строка

    Returns:
        bool: True если строка представляет корректное число, False иначе
    """
    if not number_str:
        return False

    if number_str.startswith("-"):
        number_str = number_str[1:]

    parts = number_str.split(".")
    if len(parts) > 2:
        return False

    for part in parts:
        if not part:
            return False
        for digit in part:
            if not digit.isdigit() or int(digit) >= 7:
                return False

    return True
