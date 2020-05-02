def del_symbols(text: str):
    text = [i for i in text.split()]
    for i in range(len(text)):
        text[i] = text[i].strip('.,:-()!?;)')
    return ' '.join(text)

print(del_symbols(input('Введите текст:\n')))