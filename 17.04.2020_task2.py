name = input('Как Вас зовут? ').title()
hello = ('Hello', 'Привет')
start = input('Напишите Привет или Hello: ')

while start.title() not in hello:
    start = input('Напишите Привет или Hello: ')

print(f'Hello, {name}!\n')

offices = {'KZ': 'google_kazakstan.txt', 'PS': 'google_paris.txt,', 'UAR': 'google_uar.txt',
        'KG': 'google_kyrgystan.txt', 'SF': 'google_san_francisco.txt', 'DE': 'google_germany.txt', 
        'MC': 'google_moscow.txt', 'SE': 'google_sweden.txt'}

select_text = '''
KZ - Казахстан
PS - Париж
UAR - ЮАР
KG - Кыргызстан
SF - Сан-Франциско
DE - Германия
MC - Москва
SE - Швеция
'''

select = input(f'Выберите, в какой офис Гугл Вы хотите обратиться:{select_text}').upper()
complain = input('Напишите Ваш отзыв:\n')
with open(offices[select], 'a') as f:
    f.write(f'{name}: {complain}\n')