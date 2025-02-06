'''
Яндекс Учебник
Откройте файл электронной таблицы, в каждой строке которой четыре натуральных
числа. Определите количество строк таблицы с числами, для которых выполнено
строго одно из условий:

• в строке есть повторяющиеся числа
· в строке есть ровно три нечётных числа

В ответе запишите только число.
'''

count = 0

for line in open('9\\9_Ya_m_1.txt'):
    a = [int(x) for x in line.split()]
    repeat = [x for x in a if a.count(x) > 1]
    odd = [x for x in a if x % 2 != 0]

    if (len(odd) == 3) + (len(repeat) != 0) == 1:
        count += 1
print(count)