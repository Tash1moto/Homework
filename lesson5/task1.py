# Вывести первые N чисел кратные M и больше K

a = int(input("Enter First Digit: "))
m = int(input("Enter Multiplicity: "))
k = int(input("Previous value should be more than: "))
n = int(input("Enter displayed number of values: "))
c = 0
# for a in range(9999):
#     while not a % m and c < n:
#         if a > k:
#             c += 1
#             print(a)
#             a += 1
#         elif a < k or a == k:
#             a += 1
#         else:
#             print('Condition is reached')
#             break

while c < n:
    if not a % m and a > k:
        print(a)
        c += 1
        a += 1
    else:
        if c < n:
            a += 1
        else:
            break
