import pandas as pd
df = pd.read_csv('famaly.csv'   )
print(df)

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
age = input("Введите возраст: ")
with open("user_data.txt", "w", -1, 'utf-8') as file:
    file.write("Имя: " + name + "\n")
    file.write("Фамилия: " + surname + "\n")
    file.write("Возраст: " + age + "\n")
print("Ok")

lines = int(input('Введите число: '))

if lines <= 0:
    print('Количество строк должно быть положительным целым числом')
else:
    with open('famaly.csv', 'r') as f:
        f_lines = f.readlines()
        print('Последние', lines, 'строк файла', ':')
        for line in f_lines[-lines:]:
            print(line.strip())


str_ = input("Введите строку: ")
max_len = 0
for word in str_.split():
    if len(word) > max_len:
        max_len = len(word)
str_2 = []
for word in str_.split():
    if len(word) == max_len:
        str_2.append(word)
print(str_2)

