# a = input()
# while a.isalpha():
#     a = input("enter txt")
# else:
#     print("finish")
#
# txt = input()
# objs = []
# for i in txt:
#     objs.append(i.upper())
# print(objs)

try:
    a = int(input())
    b = int(input())
    c = a / b
except ValueError:  # except (ValueError, ZeroDivisionError):
    print("not number")
except ZeroDivisionError:
    print("division by zero")
else:
    print("not exception")
finally:
    print("always")
