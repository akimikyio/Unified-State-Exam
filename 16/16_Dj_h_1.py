'''
Джобс Е.
Алгоритмы вычисления значения функций
F(n) и G(n), где n — натуральное число, задан следующими соотношениями:

G(n)=F(n)=1 при n<3;
F(n)=G(n)+F(n−1) при n>2 и n чётно;
F(n)=F(n−2)−2⋅G(n+1) при n>2 и n нечётно;
G(n)=F(n−3)+F(n−2) при n>2 и n чётно;
G(n)=F(n+1)−G(n−1) при n>2 и n нечётно.

Чему равно значение функции G(120)? В ответе запишите только целое число.
'''

from functools import lru_cache

@lru_cache()
def f(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return g(n) + f(n-1)
    if n > 2 and n % 2 != 0:
        return f(n-2) - 2 * g(n+1)

@lru_cache()
def g(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return f(n-3) + f(n-2)
    if n > 2 and n % 2 != 0:
        return f(n+1) - g(n-1)

print(g(120))

