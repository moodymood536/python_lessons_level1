# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    before_dot, after_dot = str(number).split('.')
    if ndigits == len(after_dot):
        print("Кол-во знаков десятичной дроби равно числу округления")
        return number
    elif ndigits > len(after_dot):
        print("Кол-во знаков десятичной дроби меньше числа округления")
        return number
    else:
        int_after_dot_to_compare = int(after_dot[ndigits])
        int_after_dot = int(after_dot[:ndigits])
        if int_after_dot_to_compare >= 5:
            new_int_after_dot = int(int_after_dot + 1)
            if new_int_after_dot == 10**ndigits:
                new_before_dot = int(before_dot) + 1
                return float(new_before_dot)
            else:
                return float(f'{before_dot}.{new_int_after_dot}')
        else:
            return float(f'{before_dot}.{int_after_dot}')
# print(my_round(2.1234567, 5))
# print(my_round(2.1999967, 5))
# print(my_round(2.9999967, 5))
# print(my_round(2.987654321, 5))
# print(my_round(2.99, 1))
# print(my_round(2.96, 1))
# print(my_round(3.95, 1))
# print(my_round(4.94, 1))
# print(my_round(2.99, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) > 6:
        print('Your ticket is fake')
        return ticket_number
    elif ticket_number == 0:
        return False
    elif len(str(ticket_number)) < 6:
        new_ticket_number = str(ticket_number).zfill(6)
        ticket_list = []
        for i in new_ticket_number:
            ticket_list.append(int(i))

        if sum(ticket_list[:3]) == sum(ticket_list[3:]):
            return True
        else:
            return False
    else:
        ticket_list = []
        for i in str(ticket_number):
            ticket_list.append(int(i))
        if sum(ticket_list[:3]) == sum(ticket_list[3:]):
            return True
        else:
            return False
print(lucky_ticket(6006))
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(0))


# print(list(map(sum, [1, 2, 3, 0, 0, 6])))
# print(sum([1, 2, 3, 0, 0, 6]))