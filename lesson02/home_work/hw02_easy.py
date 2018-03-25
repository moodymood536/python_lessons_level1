# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
fruits = ['apple', 'avocado', 'apricot', 'banana', 'date']
for i in range(len(fruits)):
    print('{}{:.>20}'.format(i+1, fruits[i]))
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

fruits = [12345, 6789, 'apple', 'avocado', 'apricot', 'banana', 'date', 'apple']
fruits_2 = [12345, '6789', 'apple', 'avocadddo', 'apdddricot', 'bdddanana', 'date']

print(list(set(fruits)-set(fruits_2)))
print(fruits)
print(fruits_2)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

task_3_list = [4, 6, 8, 9, 1, 3, 7]
new_task_3_list = []
for i in range(len(task_3_list)):
    if task_3_list[i] % 2 == 0:
        new_task_3_list.append(task_3_list[i]/4)
    else:
        new_task_3_list.append(task_3_list[i]*2)
print(new_task_3_list)