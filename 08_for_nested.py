# Таблица умножения 1..5

# Берём чила от 1 до 6 это сетка таблицы берем по осям x y вствавляем данные перемножая их
for i in range(1, 6):
    row = []
    for j in range(1, 6):
        row.append(i * j)
    print("\t".join(map(str, row)))
