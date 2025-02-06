'''
Горбачёв С.
Откройте файл электронной таблицы, содержащей в каждой строке семь натуральных
чисел. Найдите наибольший номер строки таблицы, для чисел которой выполнены оба
условия:

• в строке есть одно число, которое повторяется трижды, остальные числа
различны;
• количество чётных чисел превышает количество нечётных.

В ответе запишите только число.
'''

for i, line in enumerate(open('9\\9_Gorb_m_1.txt'), start=1):
    a = [int(x) for x in line.split()]
    repeat_3 = [x for x in a if a.count(x) == 3]
    unique = [x for x in a if a.count(x) == 1]

    even = [x for x in a if x % 2 == 0]
    odd = [x for x in a if x % 2 != 0]

    if len(repeat_3) == 3 and len(unique) == 4 and len(even) > len(odd):
        print(i, a)


