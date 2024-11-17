import os


def get_lab_number(file_path):
    # Extract lab number from path
    parts = file_path.split("/")
    for part in parts:
        if part.startswith("lab-"):
            return part[4:]
    return None


def get_task_number(filename):
    # Extract task number from filename
    name = os.path.splitext(filename)[0]
    if name.isdigit():
        return name
    elif name == "main":
        return "1"
    elif name == "defense" or name == "def":
        return "защита"
    return name


def create_docstring(lab_num, task_num):
    return f'''"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №{lab_num} {"Подпрограмма " + task_num if lab_num == "8" else "Задание " + task_num}
"""
'''


def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if file already has a proper docstring
    if content.lstrip().startswith('"""'):
        return

    lab_num = get_lab_number(file_path)
    task_num = get_task_number(os.path.basename(file_path))

    if lab_num and task_num:
        docstring = create_docstring(lab_num, task_num)

        # Remove any existing header comments
        lines = content.split("\n")
        while lines and (not lines[0].strip() or lines[0].strip().startswith("#")):
            lines.pop(0)

        new_content = docstring + "\n".join(lines)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated docstring in {file_path}")


def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py") and file != os.path.basename(__file__):
                file_path = os.path.join(root, file)
                process_file(file_path)


if __name__ == "__main__":
    main()
