# Заполнить список степенями числа 2 (от 2^1 до 2^n)

n = int(input("Enter max power for digit '2': "))
a = [pow(2, i+1) for i in range(n)]
print(a)

# ----------------(от 2^0 до 2^n)------------------
# n = int(input("Enter max power for digit '2': "))
# a = [pow(2, i) for i in range(n+1)]
# print(a)
