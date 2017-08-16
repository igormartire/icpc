import math

a, b, c, d = map(int, input().split(' '))

found = False

for n in range(a, int(math.sqrt(c) + 1)):
    if n % a == 0 and n % b > 0 and c % n == 0 and d % n > 0:
        found = True
        break

if found:
    print(int(n))
else:
    start = math.sqrt(c)
    if start % 1 == 0:
        start -= 1
    for i in range(int(start), 0, -1):
        div = c / i
        if div % 1 == 0:
            n = div
            if n % a == 0 and n % b > 0 and d % n > 0:
                found = True
                break
    if found:
        print(int(n))
    else:
        print(-1)

'''
n % A == 0, A <= n
n % B > 0
C % n == 0, n <= C
D % n > 0
'''