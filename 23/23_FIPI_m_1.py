'''
ФИПИ
Исполнитель преобразует число на экране.

У исполнителя есть три команды, которые обозначены латинскими
буквами:

А. Прибавить 1.
В. Умножить на 2.
С. Умножить на 3.

Программа для исполнителя - это последовательность команд.

Сколько существует программ, для которых при исходном числе 1
результатом является число 25, при этом траектория вычислений
содержит число 11 и не содержит 15?

Траектория вычислений программы - это последовательность
результатов выполнения всех команд программы. Например, для
программы СВА при исходном числе 7 траектория будет состоять
из чисел 21, 42, 43.
'''
def f(a, b):
    if a == b:
        return 1
    if any((a > b, a == 15)):
        return 0
    return f(a + 1, b) + f(a * 2, b) + f(a * 3, b)

print(f(1, 11) * f(11, 25))