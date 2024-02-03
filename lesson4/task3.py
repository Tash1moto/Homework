# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

n1 = int(input("Enter Max number: "))
data1 = (i for i in range(n1+1))
data2 = set(data1)
for s in data2:
    name1 = [input("Enter Name: ")]
    email1 = [input("Enter Email: ")]
    name1.extend(email1)
    ne0 = (name1, email1)
    dict1 = dict.fromkeys(data2, ne0)
print(dict1)
