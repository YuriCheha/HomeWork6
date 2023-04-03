# import pandas as pd
# df = pd.read_csv('famaly.csv'   )
# print(df)

# name = input("Введите имя: ")
# surname = input("Введите фамилию: ")
# age = input("Введите возраст: ")
# with open("user_data.txt", "w", -1, 'utf-8') as file:
#     file.write("Имя: " + name + "\n")
#     file.write("Фамилия: " + surname + "\n")
#     file.write("Возраст: " + age + "\n")
# print("Ok")

ilename = 'famaly.txt'
lines = int(input('Введите число: '))

if lines <= 0:
    print('Количество строк должно быть положительным целым числом')
else:
    try:
        with open('famaly.csv', 'r') as file:
            file_lines = file.readlines()
            print('Последние', lines, 'строк файла', ':')
            for line in file_lines[-lines:]:
                print(line.strip())
    except FileNotFoundError:
        print('Файл не найден')