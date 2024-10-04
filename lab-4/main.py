# Автор: Онищенко Андрей, группа ИУ7-12Б

# Ввод исходных данных
x = float(input("Введите значение x: "))

precision = float(input("Введите точность вычислений: "))
precision = abs(precision)

max_iterations = float(input("Введите максимальное количество итераций: "))
if max_iterations <= 0 or max_iterations - int(max_iterations) != 0:
    raise ValueError("Максимальное количество итераций должно быть целым положительным числом.")

print_step = float(input("Введите шаг печати: "))
if print_step <= 0 or print_step - int(print_step) != 0:
    raise ValueError("Шаг печати должен быть целым положительным числом.")

n = 0
total_res = 0

print('-' * 52)
print(f'| {'№ итерации':^11}|{'t':^18}|{'s':^18}|')
print('-' * 52)

while n < max_iterations:
    res = (-1)**n * (2*n + 1) * x**(2*n)
    total_res += res

    if n % print_step == 0:
        print(f'| {(n + 1):<11}| {res:<17.10g}| {total_res:<17.10g}|')

    if abs(res) < precision:
        break

    n += 1
else:
    n -= 1

print('-' * 52)

print(f'Сумма бесконечного ряда - {total_res:.12g}, вычислена за {n + 1} итераций.')
