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
print('{:=^30} '.format('Task 1'))
# Подсказка: воспользоваться методом .format()
fruits = ['apple', 'avocado', 'apricot', 'banana', 'date']
max_items_len = len(max(fruits, key=len))
for i in range(len(fruits)):
    print('{} {:.>{}}'.format(i+1, fruits[i], max_items_len))
#try 2
print( '{:*^30} '.format('Task 1 try 2'))
for k, fruit in enumerate(fruits):
    print('{} {:.>{}}'.format(k+1, fruit, max_items_len))
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
print('{:=^30} '.format('Task 2'))
fruits = [12345, 6789, 'apple', 'avocado', 'apricot', 'banana', 'date', 'apple']
fruits_2 = [12345, '6789', 'apple', 'avocadddo', 'apdddricot', 'bdddanana', 'date']
for item in fruits_2:
    if item in fruits:
        fruits.remove(item)
print(fruits)
# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
print('{:=^30} '.format('Task 3'))
task_3_list = [4, 6, 8, 9, 1, 3, 7]
new_task_3_list = []
for i in range(len(task_3_list)):
    if task_3_list[i] % 2 == 0:
        new_task_3_list.append(int(task_3_list[i]/4))
    else:
        new_task_3_list.append(task_3_list[i]*2)
print(new_task_3_list)