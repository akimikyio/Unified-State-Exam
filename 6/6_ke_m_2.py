'''
КомпЕГЭ
Черепахе был дан для исполнения следующий алгоритм:

Повтори 2 [Вперёд 23 Налево 90 Назад 27 Налево 90]
Поднять хвост
Назад 5 Направо 90 Вперёд 11 Налево 90
Опустить хвост
Повтори 2 [Вперёд 26 Направо 90 Вперёд 32 Направо 90]

Определите, сколько точек с целочисленными координатами будут находиться внутри
объединения фигур, ограниченного заданными алгоритмом линиями, включая точки
на линиях.
'''
from turtle import *

tracer(0)
left(90)
s = 20 # масштаб
c = 60 # координаты


for _ in range(2):
    fd(23*s)
    lt(90)
    bk(27*s)
    lt(90)
pu()
bk(5*s)
rt(90)
fd(11*s)
lt(90)
pd()
for _ in range(2):
    fd(26*s)
    rt(90)
    fd(32*s)
    rt(90)
pu()

for x in range(-c, c):
    for y in range(-c, c):
        goto(x*s, y*s)
        dot(5)
done()