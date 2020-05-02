def text_counter(text_file):
    text = text_file.readlines()
    strings = len(text)
    words = 0
    letters = 0
    for i in text:
        for j in i.split():
            letters += len(j.strip('.,:-()!?;)"\' \n'))
        words += len([w for w in i.split()])
    return strings, words, letters

file_path = input('Укажите путь к файлу: ')
with open(file_path, 'r') as f:
    res = text_counter(f)

print('Кол-во строк в тесктовом файле:', res[0])
print('Кол-во слов в тесктовом файле:', res[1])
print('Кол-во символов в тесктовом файле:', res[2])