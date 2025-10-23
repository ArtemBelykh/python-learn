# Типы данных и функция type
values = [42, 3.14, "hello", True, None, [1, 2], (3, 4), {5, 6}, {"k": "v"}]
for v in values:
    print(f"Данные {v!r} -> соответствует типу {type(v)}")
