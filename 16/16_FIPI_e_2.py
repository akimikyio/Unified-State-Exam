'''
ФИПИ
Алгоритм вычисления значения функции F(n), где n, - натуральное число, задан
следующими соотношениями:

F(n) = 1, при n = 1,
F(n) = n+F(n -1) если n - чётно,
F(n) = 2 x F(n - 2), если n > 1 и при этом n - нечётно.

Чему равно значение функции F(24)?
'''

F = [0] * 200

for n in range(len(F)):
    if n == 1:
        F[n] = 1
        continue
    if n % 2 == 0:
        F[n] = n + F[n-1]
    else:
        F[n] = 2 * F[n-2]

print(F[24])
