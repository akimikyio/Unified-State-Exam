'''
Яндекс Учебник
Значение арифметического выражения

18 * 7**108 - 5 * 49**76 + 343**35 - 50

записали в системе счисления с основанием 49.

Для найденного значения выражения вычислите сумму цифр и укажите её в ответе
в десятичной системе счисления.
'''


f = 18 * 7**108 - 5 * 49**76 + 343**35 - 50
f = -f  # т.к. число получалось отрицательным, то я его инвертировал, 
        # чтобы стало возможно действие деления с остатком

summ = 0

while f:
    summ += f % 49
    f //= 49
print(summ)
