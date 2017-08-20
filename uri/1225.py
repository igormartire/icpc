n = int(input())
try:
    while n != 0:
        notes = list(map(int, input().split(' ')))
        mean = sum(notes) / n
        if not mean.is_integer():
            print(-1)
        else:
            count = 0
            for i in notes:
                count += abs(mean - i)
            print(int(1 + count / 2))
        n = int(input())
except EOFError:
    pass