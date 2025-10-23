x = 10  # глобальная переменная

def outer():
    x = 20  # локальная в outer
    def inner():
        # Оператор nonlocal x указывает, что x ссылается на переменную x из
        # внешней области видимости (функции outer), а не на локальную переменную внутри inner.
        nonlocal x
        x += 5
        print("inner x:", x)
    inner()
    print("outer x:", x)

def changeGlobal():
    global x
    x += 1

outer()
print("global x before:", x)
changeGlobal()
print("global x after:", x)
