file = input("Введите имя файла: ")
text = input("Введите текст: ").upper()

with open('file.txt', 'w') as f:
    f.write(text)
    print(f)