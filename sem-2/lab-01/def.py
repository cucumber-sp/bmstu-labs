"""
Автор: Онищенко Андрей
Группа: ИУ7-22Б
Лабораторная работа №1 "Калькулятор систем счисления"
Защита - вычисление дополнительного кода отрицательного числа
"""

from tkinter import *
from tkinter import messagebox

def get_min_bits(n):
    """Определяет минимальное количество бит для представления числа"""
    bits = 1
    while (1 << (bits - 1)) <= abs(n):
        bits += 1
    return bits + 1

def to_binary(n, bits):
    """Преобразует число в двоичное представление заданной размерности"""
    if n >= 0:
        return format(n, f'0{bits}b')
    
    abs_bin = format(abs(n), f'0{bits}b')
    inv = ''.join('1' if b == '0' else '0' for b in abs_bin)
    return bin(int(inv, 2) + 1)[2:].zfill(bits)

def calculate():
    try:
        n = int(inp.get())
        if n >= 0:
            messagebox.showerror("Ошибка", "Число должно быть отрицательным!")
            return
        
        bits = get_min_bits(n)
        add_code = to_binary(n, bits)
        
        res.set(add_code)
        bits_label.config(text=f"Кол-во бит: {bits}")
    except ValueError:
        messagebox.showerror("Ошибка", "Нужно число!")

root = Tk()
root.title("Доп код")
root.geometry("300x250")

Label(root, text="Введите отрицательное число:").pack(pady=5)
inp = Entry(root, width=20)
inp.pack(pady=5)

Button(root, text="Вычислить", command=calculate).pack(pady=5)

bits_label = Label(root, text="Кол-во бит: -")
bits_label.pack(pady=5)

Label(root, text="Результат:").pack(pady=5)
res = StringVar()
Label(root, textvariable=res).pack(pady=5)

root.mainloop() 