# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

text = input("Enter original text: ")
text = text.replace(" ", "")
text_l = text.casefold()
data1 = set(text_l)
for s_symbol in data1:
    k = text.count(s_symbol)
    dict1 = dict.fromkeys(s_symbol, k)
    print(dict1)
