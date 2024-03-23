import csv


def foo():
    name1 = input("input Name: ")
    age1 = input("input AGE: ")
    data1 = [('Name', 'Age'), (name1, age1)]
    return data1


print(foo())
with open('CSV_file.csv', 'w', newline='') as f:
    csv.writer(f).writerows(foo())
