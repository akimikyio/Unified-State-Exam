'''
Джобс Е.
Откройте файл электронной таблицы, содержащей в каждой строке пять натуральных
чисел. Определите количество строк таблицы, содержащих числа, для которых
выполняется ровно одно из двух условий:

• сумма всех нечётных значений больше суммы чётных значений (если чисел
с определенным признаком чётности нет, то считаем сумму равной нулю);
• в строке одно число повторяется дважды, остальные числа различны.

В ответе запишите только число.
'''

count = 0

for line in open('9\\9_Dj_h_1.txt'):
    a = [int(x) for x in line.split()]
    repeat_2 = [x for x in a if a.count(x) == 2]
    unique = [x for x in a if a.count(x) == 1]

    sum_even = 0
    sum_odd = 0

    even = [x for x in a if x % 2 == 0]
    odd = [x for x in a if x % 2 != 0]

    if len(even) != 0:
        sum_even = sum(even)
    if len(odd) != 0:
        sum_odd = sum(odd)
    
    if (sum_odd > sum_even) + (len(repeat_2) == 2 and len(unique) == 3) == 1:
        count += 1
print(count)
