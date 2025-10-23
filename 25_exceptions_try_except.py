def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("Ошибка:", e)
        return None
    finally:
        print("finally: завершаем деление")

print(safe_div(10, 2))
print(safe_div(5, 0))
