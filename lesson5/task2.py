# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе число

fd = float(input("Enter 1st digit: "))
fa = input("Enter 1st action: ")
sd = float(input("Enter 2nd digit: "))
if fa == '+':
    print(fd + sd)
elif fa == '-':
    print(fd - sd)
elif fa == '*':
    print(fd * sd)
elif fa == '/':
    print(fd / sd)
elif fa == '^':
    print(fd ** sd)
elif fa == '%':
    print(fd % sd)
else:
    print('unsupported action')
