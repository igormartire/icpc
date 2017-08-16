a, b, c = map(int, input().split(' '))

if a == b or a == c or b == c:
    print('S')
elif a == b + c or a + b == c or a + c == b:
    print('S')
else:
    print('N')