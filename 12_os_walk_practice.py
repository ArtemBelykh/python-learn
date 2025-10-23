import os


# обновленно: Вот берем из системы путь и работаем с ним
# Создаём функцию для чтения  файлов
def list_py_files(root):
    # проходим по файлам в пути который прокинули в функцию

    for dirpath, dirnames, filenames in os.walk(root):
        # Ищём файлы только с .py
        for f in filenames:
            if f.endswith(".py"):
                print(os.path.join(dirpath, f))

if __name__ == "__main__":
    list_py_files(".")
