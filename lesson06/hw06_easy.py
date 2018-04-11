#! /usr/bin/python3
#-*- coding: utf-8 -*-

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math
class Triangle():
    a = ''
    b = ''
    c = ''

    def get_area(self):
        ABx = self.b['x'] - self.a['x']
        ABy =  self.b['y'] - self.a['y']
        ACx = self.c['x'] - self.a['x']
        ACy = self.c['y'] - self.a['y']
        vector_multipl = ABy*ACy - ABx*ACx
        s = 0.5*(math.sqrt(vector_multipl**2))
        return s

    def get_perimeter(self):
        AB = math.sqrt((self.b['x']-self.a['x'])**2+(self.b['y']-self.a['y'])**2)
        BC = math.sqrt((self.c['x']-self.b['x'])+(self.c['y']-self.b['y'])**2)
        AC = math.sqrt((self.c['x']-self.a['x'])+(self.c['y']-self.a['y'])**2)
        return (AB+BC+AC)

    def get_hight(self, s):
        '''
        S = 1/2bh
        h = 2S/b b - сторона, на которую опускается сторона
        :return:
        '''
        b = math.sqrt((self.c['x']-self.a['x'])+(self.c['y']-self.a['y'])**2)
        h = 2*s/b
        return h
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class trapeze():
    a = ''
    b = ''
    c = ''
    d = ''
    def sides(self):
        AB = math.sqrt((self.b['x'] - self.a['x']) ** 2 + (self.b['y'] - self.a['y']) ** 2)
        BC = math.sqrt((self.c['x'] - self.b['x']) ** 2 + (self.c['y'] - self.b['y']) ** 2)
        DC = math.sqrt((self.c['x'] - self.d['x']) ** 2 + (self.c['y'] - self.d['y']) ** 2)
        DA = math.sqrt((self.a['x'] - self.d['x']) ** 2 + (self.a['y'] - self.d['y']) **2)
        return AB,BC,DC,DA
    def is_straight(self):
        BC = math.sqrt((self.c['x'] - self.b['x']) ** 2 + (self.c['y'] - self.b['y']) ** 2)
        DA = math.sqrt((self.a['x'] - self.d['x']) ** 2 + (self.a['y'] - self.d['y']) ** 2)
        if (BC == DA):
            return True
        else:
            return False
    def perimeter(self):
        '''
        Трапеция считается равнобедренной,
        если диагонали АС и BВ равны
        '''
        AB = math.sqrt((self.b['x'] - self.a['x']) **2 + (self.b['y'] - self.a['y']) ** 2)
        BC = math.sqrt((self.c['x'] - self.b['x']) **2 + (self.c['y'] - self.b['y']) ** 2)
        DC = math.sqrt((self.c['x'] - self.d['x']) **2 + (self.c['y'] - self.d['y']) ** 2)
        DA = math.sqrt((self.a['x'] - self.d['x']) ** 2 + (self.a['y'] - self.d['y']) **2)
        return (AB+BC+DC+DA)
    def area(self):
        AB = math.sqrt((self.b['x'] - self.a['x']) ** 2 + (self.b['y'] - self.a['y']) ** 2)
        BC = math.sqrt((self.c['x'] - self.b['x']) ** 2 + (self.c['y'] - self.b['y']) ** 2)
        DC = math.sqrt((self.c['x'] - self.d['x']) ** 2 + (self.c['y'] - self.d['y']) ** 2)
        s=(AB+DC)/2*math.sqrt(BC**2-((DC-AB)**2/4))
        return s
my_triangle = Triangle()
my_triangle.a = {'x': 2, 'y': 3,} #'z': 4
my_triangle.b = {'x': 5, 'y': 6,} #'z': 7
my_triangle.c = {'x': 9, 'y': 20,} # 'z': 11
S = my_triangle.get_area()
P = my_triangle.get_perimeter()
H = my_triangle.get_hight(my_triangle.get_area())
print(f'Площадь {S}, периметр {P},высота {H}')
my_trpeze = trapeze()
my_trpeze.a = {'x': 4, 'y': 4,}
my_trpeze.b = {'x': 0, 'y': 0,} #'z': 7
my_trpeze.c = {'x': 0, 'y': 3,} # 'z': 11
my_trpeze.d = {'x': 1, 'y': 4}
print(my_trpeze.is_straight())
print(my_trpeze.perimeter())
print(my_trpeze.area())
print(my_trpeze.sides())