'''
КомпЕГЭ
Откройте файл электронной таблицы, содержащей в каждой строке семь натуральных
чисел. Определите количество строк таблицы, для чисел которых выполнены оба
условия:

• в строке есть ровно одно число, которое повторяется дважды, и пять чисел без
повторений;
• произведение трёх наименьших среди неповторяющихся чисел строки больше
квадрата повторяющегося числа.

В ответе запишите только число.
'''

count = 0

for line in open('9\\9_ke_e_1.txt'):
    a = [int(x) for x in line.split()]
    repeat_2 = [x for x in a if a.count(x) == 2]
    unique = [x for x in a if a.count(x) == 1]
    unique_sorted = sorted(unique)


    product = 0
    if len(unique_sorted) == 5:
        product = unique_sorted[0] * unique_sorted[1] * unique_sorted[2]
    
    if len(repeat_2) == 2 and len(unique) == 5:
        square = repeat_2[0]**2
        if product > square:
            count += 1

print(count)
