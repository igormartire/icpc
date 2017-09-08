P = int(input())

l = list(range(1, P, 2))
l += list(range(0, P, 2))

i = 0
cont = 0
while l[i] != 0:
    i = l[i]
    cont += 1

print(cont + 1)