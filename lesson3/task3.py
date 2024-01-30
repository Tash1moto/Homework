# Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами

name1 = input("Enter First Name: ")
age1 = input("Enter your age: ")
city1 = input("Enter city where you from: ")
data1 = {"fn": name1, "ua": age1, "cf": city1}
print("Hello %s %s from %s" % (name1, age1, city1))
print("Hello %(fn)s %(ua)s from %(cf)s" % data1)
print(f"Hello {name1} {age1} from {city1}")
print("Hello {} {} from {}".format(name1, age1, city1))
