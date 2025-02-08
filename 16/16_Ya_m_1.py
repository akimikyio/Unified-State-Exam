'''
Яндекс Учебник
Алгоритм вычисления значения функции F(n), где n - натуральное число, задан
следующими соотношениями:

F(n) = 42 при п > 10 000;
F(n)=2*n+F(n+3)+F(n+4)+F(n+6), ecли n <= 10 000 и n - чётное;
F(n) = -(n + F(n+1)+F(n+3)), если n <= 10 000 и n - нечётное.
Чему равно значение выражения F(9996) - F(9994)?
'''

f = [0] * 10050

for n in range(10001, len(f)):
    if n > 10000:
        f[n] = 42
for n in range(10000, 0, -1):
    if n % 2 == 0:
        f[n] = 2 * n + f[n+3] + f[n+4] + f[n+6]
    else:
        f[n] = -(n + f[n+1] + f[n+3])

print(f[9996] - f[9994])