# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
print( '{:=^30} '.format('Task 1'))
equation = 'y = -12x + 11111140.2121'
x=2.5
equal = equation.find('=')
variable_y = equation[0]
plus = equation.find('+')
number_to_multiple = float(equation[equal+1:plus-2])
number_to_plus = float(equation[plus+1:])
equation = number_to_multiple * x + number_to_plus
print(type(number_to_multiple), type(number_to_plus), type(variable_y), type(x))
# вычислите и выведите y
print("{} = {}".format(variable_y, equation))

print( '{:=^30} '.format('Task 2'))
# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

import re
#regexps
regex_day_check = re.compile(r'[0-2][0-9]|3[0-1]')
regex_month_check = re.compile(r'0[0-9]|1[0-2]')
regex_year_check = re.compile(r'\d{1,4}')
# date_sting = '11.12.2043'
# day = date_sting[:2]
# print(day)
# month = date_sting[3:5]
# print(month)
# year = date_sting[6:]
# print(year)
dates = ['01.11.1985', '01.22.1001', '1.12.1001', '-2.10.2001', '01.11.1']
for date_sting in dates:
    # print(date_sting)
    day = date_sting[:2]
    # print(day)
    month = date_sting[3:5]
    # print(month)
    year = date_sting[6:]
    # print(len(date_sting))
    if 7 < len(date_sting) > 10:
        print("{} Wrong date format, sybols count wrong".format(date_sting))
    elif not regex_day_check.match(day):
        print('{} is not valid day format'.format(day))
    elif not regex_month_check.match(month):
        print('{} is not valid month format'.format(month))
    elif not regex_year_check.match(year):
        print('{} is not valid year format'.format(year))
    else:
        print('{} date is ok'.format(date_sting))
print( '{:=^30} '.format('Task 3'))

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3