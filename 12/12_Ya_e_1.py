'''
Яндекс Учебник
Дана программа для Редактора:

НАЧАЛО
ПОКА нашлось (2222) ИЛИ нашлось (7777)
  ЕСЛИ нашлось (2222)
    ТО заменить (2222, 77)
    ИНАЧЕ заменить (7777, 22)
  КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ

Определите строку, которая получится после применения этой программы к входной строке, содержащей 47 цифр «7». В ответе укажите только полученную строку.
'''

s = '7' * 47
while '2222' in s or '7777' in s:
    if '2222' in s:
        s = s.replace('2222', '77', 1)
    else:
        s = s.replace('7777', '22', 1)

print(s)
