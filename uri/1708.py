import math

X, Y = [int(n) for n in input().split(' ')]

print(math.ceil(X/(Y-X)) + 1)