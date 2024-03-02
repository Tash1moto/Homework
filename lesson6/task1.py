# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

d = int(input("enter digit: "))


def function1():
    b = int(d, 2)
    str1 = str(b)
    return b
    return str1


def function2():
    c = int(b, 10)
    return c


print(function1())
print(function2())
