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
    def all_teachers(self, class_room):
        if class_room == self.class_room:
            return self.teacher
    def name_surname(self):
        return f'{self.name} {self.surname}'
    def student_info(self,student_name):
        if self.teacher == "Иванов" and (self.class_room == "5А" or self.class_room == "6Б"):
            return f'Учитель {self.teacher} не может преподавать у {self.class_room}'
        else:
            return f'{student_name} {self.class_room} {self.teacher} {self.education}'
    def parents_name(self):
        return f'{self.mother} и {self.father}'


def list_teachers_by_class(class_number):
    teachers_list = []
    for student in student_list:
        temp = student.all_teachers(class_number)
        if temp and temp not in teachers_list:
            teachers_list.append(temp)
    print(f'В классе {class_number} работают следующие учителя {" ".join(teachers_list)}')


student_list = [Student("Александр", "Иванов", '10.11.1998', "8 гимназия", "5А", "Иванов", "Мамс", "Папс", "Физра, ИЗО"),
                Student("Петр", "Сидоров", '10.01.1995', "8 гимназия", "8Б", "Учитель", "Маааммм", "Пааапппп", "Физика, математика"),
                Student("Александр", "Петров", '10.11.1998', "8 гимназия", "5А", "Иванов", "Мамс", "Папс","Физра, ИЗО"),
                Student("Петр", "Сидоров", '10.01.1995', "8 гимназия", "8Б", "МУчитель", "Маааммм", "Пааапппп",
                        "Физика, математика")]
all_class = []
all_students = []
for student in student_list:
    if student.class_room not in all_class:
        all_class.append(student.class_room)
    all_students.append(student.name_surname())
print(f'Все ученики школы {all_students},\nвсе классы школы {all_class}')

for student in student_list:
    print(student.student_info(student.name_surname()))
print(student_list[0].parents_name())

list_teachers_by_class("8Б")
list_teachers_by_class("5А")

# teachers_list = []
# for student in student_list:
#     if student.class_room() == '5А' or student.class_room() == ''