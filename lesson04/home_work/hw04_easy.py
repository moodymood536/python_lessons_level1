# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
simple_list = [1, 2, 4, 0]
squares_list = [x**2 for x in simple_list]
print(squares_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruit_list_1 = ['apple', 'orange', 'watermelon']
fruit_list_2 = ['orange', 'pineapple', 'peach', 'apple',]
summary = [x for x in fruit_list_2 if x in fruit_list_1]
print(summary)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random
random_list = [random.randint(-100,100) for _ in range(30)]
print(random_list)
cleared_random = [x for x in random_list if x >= 0 and x % 3 == 0 or x >= 0 and x %4 == 0]
print(cleared_random)
