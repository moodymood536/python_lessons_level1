# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
import math
lesson_2_norm_task1 = [2, -5, 8, 9, -25, 25, 4, 999, 125852, 1024, 121, 169, 225, 0, -25898]
new_lesson_2_norm_task1 = []
for i in range(len(lesson_2_norm_task1)):
    try:
        if math.sqrt(lesson_2_norm_task1[i]) == int(math.sqrt(lesson_2_norm_task1[i])):
            new_lesson_2_norm_task1.append(int(math.sqrt(lesson_2_norm_task1[i])))
    except ValueError:
        print('Из числа {} сложновато извлечь корень.'.format(lesson_2_norm_task1[i]))
print(new_lesson_2_norm_task1)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

import re
days = {'01': 'Первое', '02': 'Второе', '03': 'Третье', '04': 'Четвертое', '05': 'Пятое', '06': 'Шестое', '07': 'Седьмое', '08': 'Восьмое', '09': 'Девятое', '10': 'Десятое', '11': 'Одиннадцатое', '12': 'Двенадцатое', '12': 'Тринадцатое', '14': 'Четырнадцатое' }
month = {'01': 'Января', '02': 'Февраля', '03': 'Марта', '04': 'Апреля', '05': 'Мая', '06': 'Июня', '07': 'Июля', '11': 'Ноября',}
date_regexp = re.compile(r'[0-3][0-9]\.0[0-9]\.\d{4}|[0-3][0-9]\.1[1-2]\.\d{4}')
# date_regexp = re.compile(r'[0-3][0-9]\.0[0-9]\.\d{4}|[0-3][0-9]\.1[1-2]\.\d{4}')
date = "02.11.2013, 05.03.2025,, dsdfsdfdsf, 436y5fgs, 09.08.3695, "
find_date = date_regexp.findall(date)
result = date_regexp.findall(date)
print(result)
for i in range(len(result)):
    print(days.get(result[i][:2]), month.get(result[i][3:5]), result[i][6:10], 'года')
# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
random_list = []
for i in range(-100, 100):
    random_list.append(random.randint(-100,100))
print(random_list)
print(len(random_list))
# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [6, 2,1, 2, 4, 5,  5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
#a
lst2 = list(set(random_list))
lst_example = [6, 2, 1, 2, 4, 5,  5, 2]
lst_example2 = list(set(lst_example))
print(lst2)
print(lst_example2)
#b

not_repeated_items = []
lstb = [1 , 2, 4, 5, 6, 2, 5, 2]
lstb.sort()
print(lstb)
for i in range(len(lstb)):
    if lstb[i] != lstb[i+1]:
        not_repeated_items.append(lstb[i])
        print('Task 4b', not_repeated_items)


