"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №10 Задание 1
"""

from abc import ABC, abstractmethod
from typing import Optional, List, Tuple
from dataclasses import dataclass
from tabulate import tabulate


class FunctionBase(ABC):
    @abstractmethod
    def get_y(self, x: float) -> float:
        """Возвращает значение функции в точке x"""
        pass
    
    @abstractmethod
    def get_antiderivative(self, x: float) -> float:
        """Возвращает значение первообразной функции в точке x"""
        pass
    
    @abstractmethod
    def exists_at(self, x: float) -> bool:
        """Проверяет существование функции в точке x"""
        pass


class CubicFunction(FunctionBase):
    """Кубическая функция вида ax³ + bx² + cx + d"""
    
    def __init__(self, a: float, b: float, c: float, d: float):
        """
        Конструктор кубической функции
        :param a: коэффициент при x³
        :param b: коэффициент при x²
        :param c: коэффициент при x
        :param d: свободный член
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def get_y(self, x: float) -> float:
        """Вычисляет значение функции ax³ + bx² + cx + d в точке x"""
        return self.a * x**3 + self.b * x**2 + self.c * x + self.d
    
    def get_antiderivative(self, x: float) -> float:
        """Вычисляет значение первообразной (ax⁴/4 + bx³/3 + cx²/2 + dx) в точке x"""
        return (self.a * x**4) / 4 + (self.b * x**3) / 3 + (self.c * x**2) / 2 + self.d * x
    
    def exists_at(self, x: float) -> bool:
        """Кубическая функция существует при любом значении x"""
        return True


class IntegrationMethod(ABC):
    """Базовый класс для методов интегрирования"""
    
    @abstractmethod
    def integrate(self, func: FunctionBase, a: float, b: float, n: int) -> Optional[float]:
        """
        Вычисляет определенный интеграл функции
        :param func: интегрируемая функция
        :param a: нижний предел интегрирования
        :param b: верхний предел интегрирования
        :param n: количество участков разбиения
        :return: значение интеграла или None, если метод неприменим
        """
        pass

    @abstractmethod
    def get_name(self) -> str:
        """Возвращает название метода"""
        pass


class LeftRectangleMethod(IntegrationMethod):
    """Метод левых прямоугольников"""
    
    def get_name(self) -> str:
        return "Метод левых прямоугольников"
    
    def integrate(self, func: FunctionBase, a: float, b: float, n: int) -> Optional[float]:
        if n <= 0:
            return None
        
        h = (b - a) / n
        result = 0.0
        
        for i in range(n):
            x = a + i * h
            if not func.exists_at(x):
                return None
            result += func.get_y(x)
            
        return result * h


class ParabolicMethod(IntegrationMethod):
    """Метод парабол (Симпсона)"""
    
    def get_name(self) -> str:
        return "Метод парабол"
    
    def integrate(self, func: FunctionBase, a: float, b: float, n: int) -> Optional[float]:
        # Метод парабол требует четного количества участков
        if n <= 0 or n % 2 != 0:
            return None
            
        h = (b - a) / n
        result = func.get_y(a) + func.get_y(b)
        
        # Проверяем существование функции во всех точках
        for i in range(n + 1):
            x = a + i * h
            if not func.exists_at(x):
                return None
        
        # Чётные узлы (коэффициент 2)
        for i in range(2, n, 2):
            result += 2 * func.get_y(a + i * h)
            
        # Нечётные узлы (коэффициент 4)
        for i in range(1, n, 2):
            result += 4 * func.get_y(a + i * h)
            
        return result * h / 3


@dataclass
class IntegrationResult:
    """Результат интегрирования"""
    value: Optional[float]
    absolute_error: Optional[float]
    relative_error: Optional[float]


def calculate_errors(computed: Optional[float], actual: float) -> Tuple[Optional[float], Optional[float]]:
    """
    Вычисляет абсолютную и относительную погрешности
    :param computed: вычисленное значение
    :param actual: точное значение
    :return: (абсолютная погрешность, относительная погрешность)
    """
    if computed is None:
        return None, None
    
    abs_error = abs(computed - actual)
    rel_error = abs_error / abs(actual) if actual != 0 else None
    return abs_error, rel_error


def find_required_segments(method: IntegrationMethod, func: FunctionBase, 
                         a: float, b: float, epsilon: float, 
                         max_iterations: int = 20) -> Tuple[Optional[float], Optional[int]]:
    """
    Находит необходимое количество отрезков для достижения заданной точности
    :param method: метод интегрирования
    :param func: интегрируемая функция
    :param a: нижний предел
    :param b: верхний предел
    :param epsilon: требуемая точность
    :param max_iterations: максимальное количество итераций
    :return: (значение интеграла, количество отрезков) или (None, None) если не удалось достичь точности
    """
    n = 2  # Начальное количество отрезков
    
    print(f"\nПоиск необходимого количества отрезков:")
    print(f"{'N':>10} | {'Разница':>15} | {'Требуемая точность':>15}")
    print("-" * 45)
    
    for i in range(max_iterations):
        i_n = method.integrate(func, a, b, n)
        i_2n = method.integrate(func, a, b, 2 * n)
        
        if i_n is None or i_2n is None:
            return None, None
        
        diff = abs(i_n - i_2n)
        print(f"{n:>10} | {diff:>15.2e} | {epsilon:>15.2e}")
        
        if diff < epsilon:
            return i_2n, 2 * n
        
        # Увеличиваем n в 4 раза вместо 2 для более быстрого поиска
        n *= 4
        
        if n > 1e6:  # Ограничение на максимальное количество отрезков
            print("\nПревышено максимальное количество отрезков (1e6)")
            return None, None
    
    return None, None


def get_float_input(prompt: str) -> float:
    """Получение вещественного числа от пользователя"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число")

def get_int_input(prompt: str, min_value: int = None) -> int:
    """
    Получение целого числа от пользователя
    :param prompt: приглашение к вводу
    :param min_value: минимальное допустимое значение
    """
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value <= min_value:
                print(f"Ошибка: введите число больше {min_value}")
                continue
            return value
        except ValueError:
            print("Ошибка: введите корректное целое число")

def get_epsilon_input(prompt: str) -> float:
    """
    Получение значения точности от пользователя
    :param prompt: приглашение к вводу
    :return: значение точности > 0
    """
    while True:
        try:
            eps = float(input(prompt))
            if eps <= 0:
                print("Ошибка: точность должна быть положительным числом")
                continue
            return eps
        except ValueError:
            print("Ошибка: введите корректное число")

def format_number(value: Optional[float]) -> str:
    """Форматирует число для вывода"""
    if value is None:
        return "---"
    if abs(value) > 1e5 or abs(value) < 1e-5:
        return f"{value:.2e}"
    return f"{value:.6f}"

def validate_integration_bounds(a: float, b: float) -> bool:
    """Проверяет корректность пределов интегрирования"""
    if abs(b - a) > 1e4:
        print("\nПредупреждение: большой интервал интегрирования может привести к потере точности!")
        return False
    return True

def main():
    # Создаем тестовую функцию (x³ - 2x² + 3x - 5)
    func = CubicFunction(1, -2, 3, -5)
    
    # Методы интегрирования
    methods = [LeftRectangleMethod(), ParabolicMethod()]
    
    # Ввод параметров интегрирования
    print("\nВвод пределов интегрирования:")
    while True:
        a = get_float_input("Введите нижний предел интегрирования: ")
        b = get_float_input("Введите верхний предел интегрирования: ")
        if a > b:
            a, b = b, a
            print("Примечание: пределы интегрирования были переставлены местами")
        if validate_integration_bounds(a, b):
            break
        print("Рекомендуется выбрать меньший интервал интегрирования")
        if input("Продолжить с текущими значениями? (y/n): ").lower() != 'y':
            continue
        break
    
    print("\nВвод количества участков разбиения:")
    n1 = get_int_input("Введите N1 (количество участков разбиения): ", 0)
    n2 = get_int_input("Введите N2 (количество участков разбиения): ", 0)
    
    # Точное значение интеграла (через первообразную)
    exact_value = func.get_antiderivative(b) - func.get_antiderivative(a)
    
    # Вычисляем интегралы разными методами
    results = []
    for method in methods:
        method_results = []
        for n in [n1, n2]:
            value = method.integrate(func, a, b, n)
            abs_err, rel_err = calculate_errors(value, exact_value)
            method_results.append(IntegrationResult(value, abs_err, rel_err))
        results.append(method_results)
    
    # Формируем таблицы для вывода
    headers = ["Метод", f"N1 = {n1}", f"N2 = {n2}"]
    
    # Таблица значений
    values_table = []
    for method, method_results in zip(methods, results):
        row = [method.get_name()]
        for result in method_results:
            row.append(format_number(result.value))
        values_table.append(row)
    
    # Таблица абсолютных погрешностей
    abs_errors_table = []
    for method, method_results in zip(methods, results):
        row = [method.get_name()]
        for result in method_results:
            row.append(format_number(result.absolute_error))
        abs_errors_table.append(row)
    
    # Таблица относительных погрешностей
    rel_errors_table = []
    for method, method_results in zip(methods, results):
        row = [method.get_name()]
        for result in method_results:
            if result.relative_error is not None:
                row.append(f"{result.relative_error:.2%}")
            else:
                row.append("---")
        rel_errors_table.append(row)
    
    # Выводим таблицы
    print("\nТаблица результатов интегрирования:")
    print(tabulate(values_table, headers=headers, tablefmt="rounded_grid"))
    
    print(f"\nТочное значение интеграла: {format_number(exact_value)}")
    
    print("\nАбсолютные погрешности:")
    print(tabulate(abs_errors_table, headers=headers, tablefmt="rounded_grid"))
    
    print("\nОтносительные погрешности:")
    print(tabulate(rel_errors_table, headers=headers, tablefmt="rounded_grid"))
    
    # Находим наиболее точный метод
    min_error = float('inf')
    best_method = None
    best_n = None
    
    for method, method_results in zip(methods, results):
        for n, result in zip([n1, n2], method_results):
            if result.absolute_error is not None and result.absolute_error < min_error:
                min_error = result.absolute_error
                best_method = method
                best_n = n
    
    print(f"\nНаиболее точный метод: {best_method.get_name()} при N = {best_n}")
    print(f"Абсолютная погрешность: {format_number(min_error)}")
    
    # Для менее точного метода находим количество отрезков для заданной точности
    print("\nВвод требуемой точности:")
    epsilon = get_epsilon_input("Введите требуемую точность (0 < ε): ")
    worse_method = methods[1] if best_method == methods[0] else methods[0]
    
    print(f"\nПоиск количества отрезков для метода {worse_method.get_name()}")
    print(f"Требуемая точность: {epsilon:.2e}")
    
    integral_value, required_n = find_required_segments(worse_method, func, a, b, epsilon)
    
    if integral_value is not None:
        print(f"\nРезультаты поиска:")
        print(f"Требуемое количество отрезков: {required_n}")
        print(f"Значение интеграла: {format_number(integral_value)}")
        print(f"Абсолютная погрешность: {format_number(abs(integral_value - exact_value))}")
    else:
        print("\nНе удалось достичь заданной точности")


if __name__ == "__main__":
    main()
