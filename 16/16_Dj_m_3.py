'''
Джобс Е.
Алгоритм вычисления значения функции F(n), где n — натуральное число, задан следующими соотношениями:

F(0)=1,
F(1)=3;
F(n)=F(n−1)−F(n−2)+3n при n>1.

Чему равно значение функции F(40)? В ответе запишите только целое число.
'''
f = [0] * 50

for n in range(len(f)):
    if n == 0:
        f[n] = 1
    if n == 1:
        f[n] = 3
    else:
        f[n] = f[n-1] - f[n-2] + 3*n

print(f[40])