# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

n1 = int(input("Enter Max number of records: "))
dict1 = {x for x in range(n1)}
dict2 = {}
dict0 = {"Name": "NA", "Email": "NA"}
for key in dict1:
    name1 = input("Enter Name: ")
    dict0["Name"] = name1
    email1 = input("Enter Email: ")
    dict0["Email"] = email1
    dict2[key] = dict0
print(dict2)
