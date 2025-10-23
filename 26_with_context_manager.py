from contextlib import contextmanager

# Я так понял он управляет ресурсами
# гарантирует выполнение определённого кода перед входом в блок и после его выхода
@contextmanager
def chdir(path):
    import os
    prev = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(prev)

print("текущий каталог до:", __import__("os").getcwd())
with chdir("."):
    print("текущий каталог внутри:", __import__("os").getcwd())
print("текущий каталог после:", __import__("os").getcwd())
