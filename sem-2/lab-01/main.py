"""
Автор: Онищенко Андрей
Группа: ИУ7-12Б
Лабораторная работа №1 "Калькулятор систем счисления"
Интерфейсная часть программы - калькулятор перевода чисел
"""

import tkinter as tk
from tkinter import ttk, messagebox
from converter import decimal_to_base7, base7_to_decimal, validate_base7


class NumberSystemCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор систем счисления")
        self.root.geometry("600x400")

        self.create_menu()
        self.create_widgets()
        self.bind_keys()

    def create_menu(self):
        """Создает главное меню программы"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        action_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Действия", menu=action_menu)
        action_menu.add_command(
            label="Перевести в 7-ую СС", command=self.convert_to_base7
        )
        action_menu.add_command(
            label="Перевести в 10-ую СС", command=self.convert_to_decimal
        )
        action_menu.add_separator()
        action_menu.add_command(label="Выход", command=self.root.quit)

        clear_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Очистка", menu=clear_menu)
        clear_menu.add_command(label="Очистить поле ввода", command=self.clear_input)
        clear_menu.add_command(label="Очистить поле вывода", command=self.clear_output)
        clear_menu.add_command(label="Очистить все поля", command=self.clear_all)

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Справка", menu=help_menu)
        help_menu.add_command(label="О программе", command=self.show_about)

    def create_widgets(self):
        """Создает элементы интерфейса"""
        input_frame = ttk.LabelFrame(self.root, text="Ввод числа", padding="10")
        input_frame.pack(fill="x", padx=10, pady=5)

        self.input_var = tk.StringVar()
        self.input_entry = ttk.Entry(input_frame, textvariable=self.input_var, width=40)
        self.input_entry.pack(side="left", padx=5)

        ttk.Button(input_frame, text="⌫", command=self.backspace).pack(
            side="left", padx=2
        )
        ttk.Button(input_frame, text="C", command=self.clear_input).pack(
            side="left", padx=2
        )

        digits_frame = ttk.Frame(self.root, padding="10")
        digits_frame.pack(fill="x", padx=10)

        for i in range(7):
            btn = ttk.Button(
                digits_frame, text=str(i), command=lambda x=i: self.add_digit(str(x))
            )
            btn.pack(side="left", padx=2)

        ttk.Button(digits_frame, text=".", command=lambda: self.add_digit(".")).pack(
            side="left", padx=2
        )
        ttk.Button(digits_frame, text="-", command=lambda: self.add_digit("-")).pack(
            side="left", padx=2
        )

        conv_frame = ttk.Frame(self.root, padding="10")
        conv_frame.pack(fill="x", padx=10)

        ttk.Button(conv_frame, text="→ 7-ая СС", command=self.convert_to_base7).pack(
            side="left", padx=5
        )
        ttk.Button(conv_frame, text="→ 10-ая СС", command=self.convert_to_decimal).pack(
            side="left", padx=5
        )

        output_frame = ttk.LabelFrame(self.root, text="Результат", padding="10")
        output_frame.pack(fill="x", padx=10, pady=5)

        self.output_var = tk.StringVar()
        self.output_entry = ttk.Entry(
            output_frame, textvariable=self.output_var, width=40, state="readonly"
        )
        self.output_entry.pack(side="left", padx=5)

        ttk.Button(output_frame, text="C", command=self.clear_output).pack(
            side="left", padx=2
        )

    def bind_keys(self):
        """Привязывает обработчики клавиш"""
        self.root.bind("<Key>", self.handle_key)
        self.root.bind("<BackSpace>", lambda e: self.backspace())
        self.root.bind("<Return>", lambda e: self.convert_to_base7())

    def handle_key(self, event):
        """Обрабатывает нажатия клавиш"""
        if event.char in "0123456.-":
            self.add_digit(event.char)

    def add_digit(self, digit):
        """Добавляет цифру или символ в поле ввода"""
        current = self.input_var.get()

        if digit == "-" and current:
            return
        if digit == "." and "." in current:
            return
        if digit == "." and not current:
            self.input_var.set("0.")
            return

        self.input_var.set(current + digit)

    def backspace(self):
        """Удаляет последний символ из поля ввода"""
        current = self.input_var.get()
        self.input_var.set(current[:-1])

    def clear_input(self):
        """Очищает поле ввода"""
        self.input_var.set("")

    def clear_output(self):
        """Очищает поле вывода"""
        self.output_var.set("")

    def clear_all(self):
        """Очищает все поля"""
        self.clear_input()
        self.clear_output()

    def convert_to_base7(self):
        """Конвертирует число из 10-ой СС в 7-ую"""
        try:
            decimal_num = float(self.input_var.get())
            result = decimal_to_base7(decimal_num)
            self.output_var.set(result)
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное десятичное число")

    def convert_to_decimal(self):
        """Конвертирует число из 7-ой СС в 10-ую"""
        number = self.input_var.get()
        if not validate_base7(number):
            messagebox.showerror(
                "Ошибка", "Введите корректное число в 7-ой системе счисления"
            )
            return

        try:
            result = base7_to_decimal(number)
            self.output_var.set(str(result))
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def show_about(self):
        """Показывает информацию о программе"""
        about_text = """Калькулятор систем счисления

Программа выполняет перевод чисел:
- из десятичной системы в семеричную
- из семеричной системы в десятичную

Автор: Онищенко Андрей
Группа: ИУ7-12Б"""
        messagebox.showinfo("О программе", about_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberSystemCalculator(root)
    root.mainloop()
