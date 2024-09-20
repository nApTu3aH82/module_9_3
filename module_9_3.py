# -*- coding: utf-8 -*-

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = ((len(string_1) - len(string_2)) for string_1, string_2 in zip(first, second)
                if len(string_1) != len(string_2))
second_result = ((len(first[count]) == len(second[count])) for count in range(0, len(first)))
print(list(first_result))
print(list(second_result))
