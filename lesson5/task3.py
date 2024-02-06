# **Вывести четные числа от 2 до N по 5 в строку

n = int(input('Enter MAX: '))
s = 2
c = 0
list1 = []
while s < n or s == n:
    if c < 5:
        s += 1
        list1.append(s)
        c += 1
    elif c == 5:
        print(list1)
        c = 0
        list1 = []
    else:
        break
