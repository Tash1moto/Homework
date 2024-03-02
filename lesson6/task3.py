# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

set1 = [1, 2, 3, 4, 5, 6, 7]
n1 = int(input("Enter Digit: "))
c1 = list.count(set1)


def function1():
    n2 = c1-n1
    for n2 in set1:
        a1 = set1.pop(n2)
        return a1

print(function1())