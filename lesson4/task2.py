# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

text = input("Enter original text: ")
text = text.replace(" ", "")
text_l = text.casefold()
data1 = set(text_l)
for i in data1:
    k = text.count(i)
    dict1 = dict.fromkeys(i, k)
    print(dict1)
