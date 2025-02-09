def to5(n):
    s = ''
    while n:
        s = str(n % 5) + s
        n //= 5
    return s

f = 7 * 5 ** 123 + 6*5**111 - 5*25**50 + 4*125**30 - 3*5**10

count = 0

f_5 = to5(f)


print(f_5.count('4'))
