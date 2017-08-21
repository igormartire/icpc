def solve(x, y):
    return min(len(set(x) - set(y)), len(set(y) - set(x)))

a, b = tuple(map(int, input().split(' ')))
while a != 0 and b != 0:
    x = tuple(map(int, input().split(' ')))
    y = tuple(map(int, input().split(' ')))
    print(solve(x,y))
    a, b = tuple(map(int, input().split(' ')))
