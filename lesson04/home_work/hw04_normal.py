import random
import re
# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
#
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

regex_uppercase = re.compile(r'[^A-Z]+')
matched_text = regex_uppercase.findall(line)
print(matched_text)

def find_uppercase(input_sting):
       list = []
       counter = ''
       for i in range(len(input_sting)):
              if not input_sting[i].isupper():
                     counter += input_sting[i]
                     #Для случаев, когда последние буквы в нижнем регистре
                     if i == len(input_sting)-1:
                            list.append (counter)
              else:
                     if not counter:
                            pass
                     else:
                            list.append(counter)
                            counter = ''
       return list
print(find_uppercase(line))

print(find_uppercase("mtMmEZUOmcq"))
print(regex_uppercase.findall("mtMmEZUOmcq"))

print(len(regex_uppercase.findall("mtMmEZUOmcq")))
print(len(find_uppercase("mtMmEZUOmcq")))

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
#
line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

regex_upper_task_2 = re.compile(r'([a-z]{2})([A-Z]+)([A-Z]{2})')
founded_groups = regex_upper_task_2.findall(line_2)
result_list = [x[1] for x in founded_groups]
print(result_list)
print(len(result_list))

def find_uppercase_advanced(input_sting):
    list = []
    counter_is_lower = 0
    # counter_is_upper = 0
    upper_to_print = ''
    for i in input_sting:
        # print(i)
        if counter_is_lower >= 2:
            if i.isupper():
                # print(i)
                upper_to_print+=i
            else:
                if len(upper_to_print) > 2:
                    list.append(upper_to_print[:-2])
                    # print(upper_to_print)
                    upper_to_print = ''
                    # counter_is_upper = 0
                    counter_is_lower = 1
                else:
                    if len(upper_to_print):
                        upper_to_print = ''
                        counter_is_lower = 1
                    else:
                        pass
        elif i.islower():
            # print(i)
            counter_is_lower += 1
        else:
            counter_is_lower = 0
    return list
print(find_uppercase_advanced(line_2))
print(len((find_uppercase_advanced(line_2))))
print(find_uppercase_advanced("GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"))
founded_groups_test = regex_upper_task_2.findall("GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec")
result_list_test = [x[1] for x in founded_groups_test]
print(result_list_test)
# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

# make a random list
random_list = [random.randint(1, 5) for i in range(2500)]

# print(random_list)
str_random_list = ''.join([str(x) for x in random_list])
print(str_random_list)
print(len(str_random_list))
#making txt file with string of numbers
with open('random_string.txt', 'w') as r:
    r.write(str_random_list)
counter = ''
sorted_and_grouped = []
for i in range(len(str_random_list)-1):
    # if items repeat, append them to a string
    if str_random_list[i] == str_random_list[i+1]:
        counter += str(str_random_list[i])
    else:
        #if not repeats append lonely (we always append here/ because [5556] --> 5!= 6, but we have to append it
        counter += str(str_random_list[i])
        sorted_and_grouped.append(counter)
        counter = ''
# print(sorted_and_grouped)
# We are counting length of every item in the list
# list_lengthes == sorted_and_groepd by indexes, nubbers are different, but indexes THE SAME
list_lengthes = (list(map(len, sorted_and_grouped)))
# print(list_lengthes)
print(f'len of list_lenthes= {len(list_lengthes)} == len of sorted_and_grouped= {len(sorted_and_grouped)}')
#find the biggest length
max_number_of_repeats = max(list_lengthes)
print(f'max number repeats= {max_number_of_repeats}')
#find out index of the biggest repeat
index_of_max_repeats = list_lengthes.index(max_number_of_repeats)
#ask for a final longest string by its index
biggest_number = sorted_and_grouped[index_of_max_repeats]
print(f'The biggest number= {biggest_number}')
# new_list = [str(x) for x in list_lengthes]
# print(list(map(max, new_list)))