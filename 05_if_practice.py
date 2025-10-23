# Калькулятор скидки

# Задаём цену и скидки
price = 2190
discount = 0

# Делаем условие если  скидка больше или равна 1000 то скидку делаем 15%
if price >= 1000:
    discount = 0.15
#     Иначе если цена скидки больше или равно 500 то 10% скидки
elif price >= 500:
    discount = 0.10
#     Выводим всё
final_price = price * (1 - discount)
print("final_price:", final_price)
