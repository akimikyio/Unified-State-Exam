'''
Грачев Н.
Дана программа для Редактора:

НАЧАЛО
    ПОКА нашлось (31) ИЛИ нашлось(32) ИЛИ нашлось(30)
        ЕСЛИ нашлось(31)
            ТО заменить(31, 223)
        КОНЕЦ ЕСЛИ
        ЕСЛИ нашлось(32)
            ТО заменить(32, 23)
        КОНЕЦ ЕСЛИ

        ЕСЛИ нашлось(30)
            ТО заменить(30, 13)
        КОНЕЦ ЕСЛИ

    КОНЕЦ ПОКА

    заменить (3,0)
КОНЕЦ

На вход приведённой выше программе поступает строка, начинающаяся с тройки,
а затем содержащая 40 цифр «О», n цифр «1» и 40 цифр «2».

Определите наименьшее значение п, при котором сумма числовых значений цифр
строки, получившейся в результате выполнения программы, является трехзначным
числом, состоящим из трёх одинаковых цифр.
'''

for n in range(0, 1000):
    s = '3' + '0' * 40 + '1' * n + '2' * 40
    while '31' in s or '32' in s or '30' in s:
        if '31' in s:
            s = s.replace('31', '223', 1)
        if '32' in s:
            s = s.replace('32', '23', 1)
        if '30' in s:
            s = s.replace('30', '13', 1)
    s = s.replace('3', '0', 1)

    summ = sum(map(int, s))

    if (len(str(summ)) == 3) and (str(summ)[0] == str(summ)[1] == str(summ)[2]):
        print(n)
        break