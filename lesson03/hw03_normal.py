# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fibonacci_list_easy = [1,1]
    fibonacci_list = [x for x in range(n - 2, m + 1)]
    if m==1 and n==1:
        print(fibonacci_list_easy)
    elif n==0:
        print('fibonacci cannoot starts from 0')
    elif n == 1:
        fibonacci_list.pop(0)
        fibonacci_list.pop(0)
        fibonacci_list.insert(0,1)
        for i in range(2, len(fibonacci_list)):
            count = fibonacci_list[i-2] + fibonacci_list[i-1]
            fibonacci_list.pop(i)
            fibonacci_list.insert(i,count)
        print(fibonacci_list)
    else:
        for i in range(2, len(fibonacci_list)):
            count = fibonacci_list[i-2] + fibonacci_list[i-1]
            fibonacci_list.pop(i)
            fibonacci_list.insert(i,count)
        print(fibonacci_list)
fibonacci(1,4)
fibonacci(1,1)
fibonacci(0,1)
fibonacci(0,0)
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    balls_counter = len(origin_list)-1
    for j in range(len(origin_list)-1):
        for i in range(balls_counter):
            if origin_list[i] > origin_list[i+1]:
                temp_value = origin_list[i]
                origin_list[i] = origin_list[i+1]
                origin_list[i + 1] = temp_value
        balls_counter -= 1
        # i = 0
    print(origin_list)
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_filter(func, list):
    filtered_list = []
    for i in list:
        if func(i) is True:
            filtered_list.append(i)
    return filtered_list
mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
print(my_filter(lambda x: x == 'мак', mixed))
print(my_filter(lambda x: x > 5,  [2, 10, -10, 8, 2, 0, 14]))
print(list(filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14])))
print(my_filter(len, ['', 'not null', 'bla', '', '10']))
print(list(filter(len, ['', 'not null', 'bla', '', '10'])))
print(len(''))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
# У параллелограмма стороны попарно равны
def is_parallelogram(a,b,c,d):
    ab = (b[0]-a[0])**2 + (b[1]-a[1])**2
    cd = (d[0]-c[0])**2 + (d[1]-c[1])**2
    ad = (d[0]-a[0])**2 + (d[1]-a[1])**2
    bc = (b[0]-c[0])**2 + (b[1]-c[1])**2
    if ab == cd and ad == bc:
        return True
    else:
        return False
a,b,c,d = (1,3),(4,7),(2,8),(-1,4)
print(is_parallelogram(a,b,c,d))
a,b,c,d = (1,3),(5,7),(2,6),(-1,5)
print(is_parallelogram(a,b,c,d))
