# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
class Student:
    def __init__(self, name, surname, birth_date, school, class_room, teacher, mother, father, education):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.school = school
        self.class_room = class_room
        self.teacher = teacher
        self.mother = mother
        self.father = father
        self.education = education
    def name_surname(self):
        return f'{self.name} {self.surname}'
    def student_info(self,student_name):
        if self.teacher == "Иванов" and (self.class_room == "5А" or self.class_room == "6Б"):
            return f'Учитель {self.teacher} не может преподавать у {self.class_room}'
        else:
            return f'{student_name} {self.class_room} {self.teacher} {self.education}'
    def parents_name(self, name):
        return f'{self.mother}'


student_list = [Student("Александр", "Иванов", '10.11.1998', "8 гимназия", "5А", "Иванов", "Мамс", "Папс", "Физра, ИЗО"), Student("Петр", "Сидоров", '10.01.1995', "8 гимназия", "8Б", "Учитель", "Маааммм", "Пааапппп", "Физика, математика")]
for student in student_list:
    print(student.name_surname())
for student in student_list:
    print(student.student_info(student.name_surname()))
print(student_list[0].parents_name())