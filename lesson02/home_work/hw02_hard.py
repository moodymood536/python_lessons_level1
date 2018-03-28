# equation = 'y = -12x + 11111140.2121'
# x=2.5
# y = int('11111140.2121', 16)
print( '{:=^30} '.format('Task 2'))
import re
#regexps
regex_day_check = re.compile(r'[0-2][0-9]|3[0-1]')
regex_month_check = re.compile(r'0[0-9]|1[0-2]')
regex_year_check = re.compile(r'\d{1,4}')
# date_sting = '11.12.2043'
# day = date_sting[:2]
# print(day)
# month = date_sting[3:5]
# print(month)
# year = date_sting[6:]
# print(year)
dates = ['01.11.1985', '01.22.1001', '1.12.1001', '-2.10.2001', '01.11.1']
for date_sting in dates:
    # print(date_sting)
    day = date_sting[:2]
    # print(day)
    month = date_sting[3:5]
    # print(month)
    year = date_sting[6:]
    # print(len(date_sting))
    if 7 < len(date_sting) > 10:
        print("{} Wrong date format, sybols count wrong".format(date_sting))
    elif not regex_day_check.match(day):
        print('{} is not valid day format'.format(day))
    elif not regex_month_check.match(month):
        print('{} is not valid month format'.format(month))
    elif not regex_year_check.match(year):
        print('{} is not valid year format'.format(year))
    else:
        print('{} date is ok'.format(date_sting))
print( '{:=^30} '.format('Task 3'))
n = 122
i =1
k=1
# for i in range(1,100):

    # print(res)

# for i in range(1, 10):
res = [i for i in range(1,2)]
print(res)
res2 = [i for i in range(2,6)]
print(res2*2)
#     if i == k*k

    # res = [x for x in range(i, i*i)]

    # print(res)
    # if i ==1 or i ==1:
    #     i+=1
    # i = i*i
 # 9  10 11
 # 6  7  8
 #  4   5
 #  2   3
 #    1