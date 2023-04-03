# import pandas as pd
# df = pd.read_csv('famaly.csv'   )
# print(df)

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
age = input("Введите возраст: ")
with open("user_data.txt", "w") as file:
    file.write("Имя: " + name + "\n")
    file.write("Фамилия: " + surname + "\n")
    file.write("Возраст: " + age + "\n")
print("file")