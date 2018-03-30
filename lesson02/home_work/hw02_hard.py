# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
print( '{:=^30} '.format('Task 1'))
equation = 'y = -12x + 11111140.2121'
equation_items = equation.split()[2:]
print(equation_items)
x=2.5
variable_y = equation[0]
number_to_multiple = float(equation_items[0][:-1])
number_to_plus = float(equation_items[2])
equation = number_to_multiple * x + number_to_plus
# вычислите и выведите y
print(f"{variable_y} = {equation}")

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
regex_day_check = re.compile(r'[1-9]|[1-2][0-9]|3[0-1]')
regex_month_check = re.compile(r'0[0-9]|1[0-2]')
regex_year_check = re.compile(r'\d{1,4}')
# date_sting = '11.12.2043'
# day = date_sting[:2]
# print(day)
# month = date_sting[3:5]
# print(month)
# year = date_sting[6:]
# print(year)
months = {
    # month: days count
    1: 31, 2: 30, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31,
}
dates = ['1.11.1985', '1.22.1001', '1.12.1001', '-2.10.2001', '1.11.1', '31.09.1001']
for date_sting in dates:
    day, month, year = date_sting.split('.')
    print(day, month, year)
    # print(f'Month: {month}, Days in month: {months[month]}')
    # print(day, month, year)
    if 7 < len(date_sting) > 10:
        print(f'{date_sting} Wrong date format, sybols count wrong')
    elif not regex_month_check.match(month):
        print(f'{month} is not valid month format')
    elif not regex_day_check.match(day):
        print(f'{day} is not valid day format')
    elif int(day) > months[int(month)]:
        print (f'Given {day} days, but in this month #{month} should be less days - {months[int(month)]}')
    elif not regex_year_check.match(year):
        print(f'{year} is not valid year format')
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
room = 13
if room > 0 and room <=  2000000000:
    loop_index = 1
    floor_index = 1
    room_index = 1

    #start global loop
    while room_index <= room:
        print('----------')
        #generate floors
        for _ in range(loop_index):
            new_floor = []
            #generate rooms
            for x in range(loop_index):
                new_floor.append(room_index)
                room_index+=1
            #show floor content
            print(f'Floor #{floor_index}, contains {loop_index} rooms: {new_floor}')
            #check rooms exist
            if room in new_floor:
                room_position = new_floor.index(room)+1
                print(f'Room #{room} was founded on #{floor_index} floor at {room_position} position')
                break
            floor_index+=1
        loop_index+=1
else:
    print('invalid room number')