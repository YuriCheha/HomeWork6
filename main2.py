import pandas as pd
df = pd.read_csv('famaly.csv')
json_data = df.to_json(orient='records')
with open('famaly.json', 'w') as f:
    f.write(json_data)

# file = input("Введите имя файла: ")
# text = input("Введите текст: ").upper()
#
# with open('file.txt', 'w', -1, 'UTF-8') as f:
#     f.write(text)
