# Берём кортеж и распаковываем его
point = (10, 20)
# Значение переменной point
x, y = point
print("x:", x, "y:", y)

# проверяет имеет ли объект point метод __setitem__, используется для установки элементов по индексу
print("immutable:", hasattr(point, "__setitem__"))
