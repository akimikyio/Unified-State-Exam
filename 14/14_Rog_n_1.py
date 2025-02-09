'''
Рогов А.
Операнды арифметического выражения записаны в системе счисления
с основанием 17.

149x3_17 + x612_17 - x54x_17

В записи чисел переменной х обозначена неизвестная цифра из алфавита 17-ричной
системы счисления. Определите сумму всех значений х, при которых значение данного
арифметического выражения кратно 7. В ответе укажите значение суммы в десятичной
системе счисления. Основание системы счисления в ответе указывать не нужно.
'''

alph = '0123456789ABCDEFG'

summ = 0

for x in alph:
    f1 = '149' + x + '3'
    f2 = x + '612'
    f3 = x + '54' + x

    if (int(f1, 17) + int(f2, 17) - int(f3, 17)) % 7 == 0:
        summ += int(x, 17)
print(summ)