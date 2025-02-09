'''
Джобс Е.
Черепахе был дан для исполнения следующий алгоритм:
Повтори 15 [Повтори 20 [Вперёд 40 Направо 90] Налево 90]

Определите количество точек с целочисленными положительными координатами,
которые лежат внутри полученного контура и при этом не лежат на оставленном
черепахой следе.
'''

from turtle import *

scale = 20
coords = 60

screensize(3000, 3000)


tracer(0)
left(90)



for _ in range(15):
    for __ in range(20):
        fd(40*scale)
        right(90)
    left(90)

pu()
for x in range(-coords, coords):
    for y in range(-coords, coords):
        goto(x*scale, y*scale)
        dot(5)


done();