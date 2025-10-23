text = "первая строка\nвторая строка\nДесятая стркоа"

# запись
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write(text)

# чтение
with open("sample.txt", "r", encoding="utf-8") as f:
    print("read:")
    for line in f:
        print(line.strip())
