# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

n1 = int(input("Enter Max number of records: "))
dict1 = {x: {"Name": input("Enter Name: "), "Email": input("Enter Email: ")} for x in range(n1)}

print(dict1)

data2 = {}
for i in range(n1):
        data2[i] = {
                "Name": input(),
                "Email": input()
        }
