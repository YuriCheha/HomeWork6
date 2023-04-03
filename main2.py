file = input("Введите имя файла: ")
text = input("Введите текст: ").upper()

with open('file.txt', 'w', -1, 'UTF-8') as f:
    f.write(text)
