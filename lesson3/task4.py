# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных

a1 = str(input("Enter 1st digit: "))
b1 = str(input("Enter 2nd digit: "))
c1 = str(input("Enter 3rd digit: "))
text1 = a1+b1+c1
print("Number of negative digits",text1.count("-"))
