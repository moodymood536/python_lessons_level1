
__author__ = 'Мартынов Никита Сергеевич'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
x = 537234524687659
i = 0
biggest = 0
while i < len(str(x)):
    if biggest < int(str(x)[i]):
        biggest = int(str(x)[i])
    i+=1
print('Using while', biggest)
# use for
for i in range(len(str(x))):
    if biggest < int(str(x)[i]):
        biggest = int(str(x)[i])
print('Using for', biggest)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
a = 32 #   0100000
b = 56 #   0111000
a = a ^ b # new a       0100000^011100=0011000 = 24
b = b ^ a # newa*oldb   0011000^011100=0100000 = 32 = a
a = a ^ b # newa*newb   0011000^010000=0111000 = 56
print('Using XOR', a, b)
a=999
b=5009090   # ---------|--------------|----------|
            #          a   difference b         summ
a=a+b #now a = 86 - summ
b=a-b #now b=a=9 - summ-b=a
a=a-b #summ-a=b
print('using math', a,b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
import math
a=int(input("Input arg a "))
b=int(input("Input arg b "))
c=int(input("Input arg c "))
#ax^2+bx+c=0
#d - discrement
d = pow(b,2)-4*a*c
print('discrement counted', d)
if d < 0:
    print("no roots, finish")
elif d == 0:
    print("one root")
    x_one = ((-b + math.sqrt(d)) / 2 * a)
    print("root ", x_one)
else:
    print("two roots")
    x_one = ((-b + math.sqrt(d))/2*a)
    x_two = ((-b - math.sqrt(d))/2*a)
    print("root1 ", int(x_one), "root2 ", int(x_two))
