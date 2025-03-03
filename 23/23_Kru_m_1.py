'''
Крючков М.
Исполнитель Калькулятор преобразует число на экране. У исполнителя
есть три пронумерованных команды:

1. Прибавить 3
2. Умножить на 2
3. Умножить на 5

Первая команда увеличивает число на экране на 3, вторая увеличивает
число на экране в два раза, третья увеличивает число на экране в пять
раз.

Программа для исполнителя - это последовательность команд.

Сколько существует программ, для которых при исходном числе 7
результат - число 961? При этом траектория вычислений должна
содержать число 169, но не содержать 321.

Траектория вычислений программы - это последовательность
результатов выполнения всех команд программы. Например, для
программы 132 при исходном числе 5 траектория будет состоять
из чисел 8, 40, 80.
'''
def f(a, b):
    if a == b:
        return 1
    if a > b or a == 321:
        return 0
    return f(a + 3, b) + f(a*2, b) + f(a*5, b)

print(f(7, 169) * f(169, 961))