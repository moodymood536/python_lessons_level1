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
        '''
        s=1/2|(x1-x3)(y2-y3)-(x2-x3)(y1-y3)|
        :return:
        '''
        ACx = self.a['x'] - self.c['x']
        ACy = self.a['y'] - self.c['y']
        BCx = self.b['x'] - self.b['x']
        BCy = self.b['y'] - self.c['y']
        return int(0.5*math.fabs(ACx*BCy-BCx*ACy))

    def get_perimeter(self):
        AB = math.sqrt((self.b['x']-self.a['x'])**2+(self.b['y']-self.a['y'])**2)
        BC = math.sqrt((self.c['x']-self.b['x'])+(self.c['y']-self.b['y'])**2)
        AC = math.sqrt((self.c['x']-self.a['x'])+(self.c['y']-self.a['y'])**2)
        return int(AB+BC+AC)




my_triangle = Triangle()
my_triangle.a = {'x': 2, 'y': 3,} #'z': 4
my_triangle.b = {'x': 5, 'y': 6,} #'z': 7
my_triangle.c = {'x': 9, 'y': 10,} # 'z': 11
S = my_triangle.get_area()
P = my_triangle.get_perimeter()
print(S, P)