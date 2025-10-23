# создаём генератор  который на первом шаге вычисляет next(gen)

gen = (n*n for n in range(5))
print(next(gen))
print(sum(gen)) # а затем суммирует оставшиеся элементы
