# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных

a1 = float(input("Enter 1st digit: "))
b1 = float(input("Enter 2nd digit: "))
c1 = float(input("Enter 3rd digit: "))
print("Number of positive digits", (a1 > 0) + (b1 > 0) + (c1 > 0))
print("Number of negative digits", (a1 < 0) + (b1 < 0) + (c1 < 0))
