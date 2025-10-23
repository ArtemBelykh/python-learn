data = [5, 3, 8, 3, 1]
# Вставляем 10 в объект
data.append(10)
data.insert(1, 99)

data.remove(3)   # удалит первое вхождение 3
popped = data.pop()  # удалит последний элемент
data.sort()
print("Данные:", data, "| Элемент массива:", popped, "| count(3):", data.count(3))
print("index(99):", data.index(99))
