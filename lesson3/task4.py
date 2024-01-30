# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных

a1 = input("Enter 1st digit: ")
b1 = input("Enter 2nd digit: ")
c1 = input("Enter 3rd digit: ")
text1 = a1+b1+c1
neg1 = text1.count("-")
pos1 = 3-neg1
print("Number of negative digits", neg1)
print("Number of positive digits", pos1)
