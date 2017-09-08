N, M = list(map(int, input().split(' ')))
cont = 0
for _ in range(N):
    if all(map(int, input().split(' '))):
        cont += 1
print(cont)