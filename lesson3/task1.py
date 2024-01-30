# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

text = str(input("Enter text:"))
text1 = text.split(sep=" ")
text11 = str("-".join(text1))
text2 = str(text.replace(" ", "-"))
print("case1: ", text11)
print("case2: ", text2)
