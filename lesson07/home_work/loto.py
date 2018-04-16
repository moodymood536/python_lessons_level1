#!/usr/bin/python3
import random
from collections import Counter

class Ticket:
    def cards_generator(self):
        card = []
        choice_list = [x for x in range (1, 91)]
        for i in range (3):
            five_numbers = random.sample (list (choice_list), 5)
            choice_list = set (choice_list) - set (five_numbers)
            line_1 = list (five_numbers) + [' '] * (9 - len (five_numbers))
            random.shuffle (line_1)
            card.append (line_1)
        return card

    def __init__(self):
        self.numbers = self.cards_generator ()

    def __str__(self):
        ticket_str = ""
        for i in range (3):
            ticket_str += str (self.numbers[i]) + "\n"
        return ticket_str

    def cross(self, r_item):
        print ("R item is: " + str (r_item))
        for i in range (len (self.numbers)):
            for j in range (len (self.numbers[i])):
                # print(self.numbers[i][j])
                if str (self.numbers[i][j]) == str (r_item):
                    self.numbers[i][j] = '-'
                    return self.numbers

    def has_number(self, r_item):
        for i in range (len (self.numbers)):
            for j in range (len (self.numbers[i])):
                # print(self.numbers[i][j])
                if str (self.numbers[i][j]) == str (r_item):
                    return True
        else:
            return False

    def skip(self, r_item):
        for i in range (len (self.numbers)):
            for j in range (len (self.numbers[i])):
                # print(self.numbers[i][j])
                if str (self.numbers[i][j]) == str (r_item):
                    return False
        else:
            return True

    def check_winner(self):
        count = 0
        for i in self.numbers:
            counter = Counter(i)
            count += counter['-']
            if count == 15:
                return True

class Player (Ticket):

    def cross(self, cross_num):
        self.ticket.cross (cross_num)
        return str (self.ticket)

    def __init__(self):
        self.ticket = Ticket ()
        # self.is_person = is_person

    def __str__(self):
        return 'Tiket is ' + str (self.ticket)

user = Player()
print ('Карточка игрока', '\n', str (user.ticket))
computer = Player()
print ('Карточка компьютера', '\n', computer.ticket)
cross_list = [str(x) for x in range(1, 91)]
while True:
    cross = random.choice(cross_list)
    print(cross)
    cross_list.remove (cross)
    answer = input ('Do you have this number? y/n: ')
    if answer == 'y':
        if user.ticket.has_number(cross) is True:
            print ('Карточка игрока', '\n', user.cross(cross))
            is_user_winner = user.ticket.check_winner()
            if is_user_winner is True:
                print (f'user is winner')
                break
        else:
            print (f'Ты проиграл')
            break
    elif answer == 'n':
        if user.ticket.skip (cross) is True:
            print ('Карточка игрока', '\n', str (user.ticket))
        else:
            print (f'Ты проиграл')
            break
    if computer.ticket.has_number (cross) is True:
        print ('Карточка компьютера', '\n', computer.cross (cross))
        is_computer_winner = computer.ticket.check_winner ()
        if is_computer_winner is True:
            print(f'computer is winner')
            break
    else:
        computer.ticket.skip (cross)
        print ('Карточка компьютера', '\n', str (computer.ticket))

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
