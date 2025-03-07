'''
Шастин Л.
Исполнитель преобразует число на экране.

У исполнителя есть три команды, которым присвоены номера:

А. Прибавить 2.
В. Прибавить 5.
С. Умножить на 2.

Программа для исполнителя - это последовательность команд.
Сколько существует программ, для которых при исходном числе 8
результатом является число 40, а последняя в них команда - А или В?
'''
def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a + 2, b) + f(a + 5, b) + f(a * 2, b)

print(f(8, 38) * f(38, 40) + f(8, 35) * f(35, 40))