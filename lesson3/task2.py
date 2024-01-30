# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3

a1 = float(input("Enter 1st digit: "))
b1 = float(input("Enter 2nd digit: "))
c1 = float(input("Enter 3rd digit: "))
sum1 = float(a1+b1+c1)
result1 = f"{(sum1/3):.3f}"
print(result1)
