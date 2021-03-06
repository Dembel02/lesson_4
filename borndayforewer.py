"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

import random
writers = {'Пушкин А.С.': '23.06.1799', 'Толстой Л.Н.': '20.11.1828',
           'Достоевский Ф.М.': '11.11.1821','Максим Горький': '28.03.1868',
           'Лермонтов М.Ю.': '15.10.1814', 'Ломоносов М.В.': '19.11.1711',
           'Пришвин М.М.': '04.02.1873', 'Гоголь Н.В.': '01.04.1809',
           'Маяковский В.В': '19.07.1893', 'Ахматова А.А': '23.06.1889'}
days = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое',
        '05': 'пятое', '06': 'шестое', '07': 'седьмое', '08': 'восьмое',
        '09': 'девятое', '10': 'десятое', '11': 'одинадцатое', '12': 'двенадцатое',
        '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое', '16': 'шестнадцатое',
        '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое',
        '21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье',
        '24': 'двадцать четвертое', '25': 'двадцать пятое', '26': 'двадцать шестое',
        '27': 'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое',
        '30' : 'тридцатое', '31': 'тридцать первое'}
months = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля',
          '05': 'мая', '06': 'июня', '07': 'июля', '08': 'августа',
          '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'}
result = random.sample(writers.keys(), 5)
#result = random.choices(list(writers.keys()), k=5) # Проблема с повторяющимися знаменитостями
answer = ()
count = 0
def function_date(date):
    day, month, year = date.split('.')
    print("правильный ответ :", days[day], months[month], year, 'года')

for man in result:
    print("знаменитость ", man)
    answer = input('Введите день рождения ')
    if answer == writers[man]:
        print('Вы ввели верно')
        count += 1
    else:
        date = writers[man]
        function_date(date)
        # day, month, year = date.split('.')
        # print("правильный ответ :", days[day], months[month], year, 'года')
print("Вы правильно ответили на ", count, "вопросов")
print("Количество неправильных ответов составило :", len(result) - count)
print("Процент правильных ответов составил :", count * 100 / len(result), "%")
print("Процент неправильных ответов составил :", (len(result) - count) * 100 / len(result), "%")