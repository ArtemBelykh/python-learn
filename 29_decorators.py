import time
from functools import wraps

def timing(fn):
    # копирует метаданные исходной функции в функцию-обертку
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            return fn(*args, **kwargs)
        finally:
            print(f"{fn.__name__} заняла {time.time() - start:.4f}s")
    return wrapper
# измеряет время выполнения обёрнутой функции
@timing
def work(n):
    total = 0
    for i in range(n):
        total += i*i
    return total

print(work(1_000_00))
