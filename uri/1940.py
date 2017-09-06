J, R = list(map(int, input().split(' ')))
pt = list(map(int, input().split(' ')))

j = [0] * J

for i in range(J * R):
    j[i % J] += pt[i]

m = max(j)

for i in range(J-1, -1, -1):
    if j[i] == m:
        print(i+1)
        break