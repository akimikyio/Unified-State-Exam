'''
Джобс Е.
Исполнитель преобразует число на экране.
У исполнителя есть две команды, которым присвоены номера:

1. Прибавить 1
2. Умножить на 2

Первая команда увеличивает число на экране на 1, вторая умножает его
на 2. Программа для исполнителя - это последовательность команд.

Сколько существует программ, для которых при исходном числе 1
результатом является число 30, при этом траектория вычислений
не проходит через 10?

Траектория вычислений программы - это последовательность
результатов выполнения всех команд программы. Например, для
программы 121 при исходном числе 7 траектория будет состоять
из чисел 8, 16, 17.
'''

def f(a, b):
    if a == b:
        return 1
    if any((a > b, a == 10)):
        return 0
    return f(a + 1, b) + f(a * 2, b)
print(f(1, 30))