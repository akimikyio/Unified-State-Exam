'''
Шагитов М.
Откройте файл электронной таблицы, содержащий в каждой строке шесть целых чисел.
Определите количество строк таблицы, содержащих числа, для которых выполнены
оба условия:

• все числа различны;
• пятикратная сумма наименьшего и наибольшего чисел в строке больше или равна
трёхкратной сумме четырёх оставшихся чисел.

В ответе запишите только число.
'''
count = 0

for line in open('9\\9_Sha_e_1.txt'):
    a = [int(x) for x in line.split()]
    unique = [x for x in a if a.count(x) == 1]

    unique.sort()

    if len(unique) == 6 and ((5 * (unique[0] + unique[-1])) >= 3 * (unique[1] + unique[2] + unique[3] + unique[4])):
        count += 1
print(count)