fat = [1, 1]
for i in range(2, 9):
    fat.append(fat[-1] * i)

N = int(input())

if N == 0:
    print(1)

cont = 0
for i in range(8, 0, -1):
    while N >= fat[i]:
        cont += 1
        N -= fat[i]
print(cont)
