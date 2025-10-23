nums = [1,2,3,4,5]
squares = [n*n for n in nums] # Список, созданный из чисел в nums, возведенных в квадрат
evens = {n for n in range(10) if n % 2 == 0} # Множество четных чисел от 0 до 9
index_map = {ch: i for i, ch in enumerate("abc")} # Словарь, где ключи это символы из строки "abc", а значения — их индексы

print("squares:", squares)
print("evens:", evens)
print("index_map:", index_map)
