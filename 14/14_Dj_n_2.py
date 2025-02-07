'''
Джобс Е.
Известно, что значение выражения 36x53_8 - 4y3_8 является положительным
и минимальным. Известно, что х и у - допустимые комбинации из одной или более
цифр.

Определите значение выражения. В качестве ответа запишите полученное число в
десятичной системе счисления. Основание системы счисления указывать не нужно.
'''

numbers = []
last = [0, 1, 2, 3, 4, 5, 6, 7]


for x in range(80): # я предположил, что мне хватит рассмотреть все чсла от 0 до 77 в восьмеричной системе счисления для решения задачи
    for y in range(80):
        if x % 10 not in last or y % 10 not in last: # проверка на то, что последняя цифра входит в восьмеричную систему
            continue
        f1 = '36' + str(x) + '53'
        f2 = '4' + str(y) + '3'
        f1_10 = int(f1, 8)
        f2_10 = int(f2, 8)
        diff = f1_10 - f2_10

        if diff > 0:
            numbers.append(diff)
print(min(numbers))
        
