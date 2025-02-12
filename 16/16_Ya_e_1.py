'''
Яндекс Учебник
Алгоритм вычисления значения функции F(n), где n — целое число, задан так:

F(n)=1 при n⩽1
F(n)=F(n−1)+n/3, если n>1 и n кратно 3
F(n)=F(n−1)+F(n−2) иначе

Чему равно значение выражения F(54)−F(52)−F(50)?
'''

f = [0] * 60

for n in range(len(f)):
    if n <= 1:
        f[n] = 1
    if n > 1 and n % 3 == 0:
        f[n] = f[n-1] + n/3
    else:
        f[n] = f[n-1] + f[n-2]

r = f[54] - f[52] - f[50]
print(int(r))