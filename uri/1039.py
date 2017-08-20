import math

def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

while True:
    try:
        r1, x1, y1, r2, x2, y2 = list(map(int, input().split(' ')))
        p1, p2 = (x1, y1), (x2, y2)
        print("RICO" if dist(p1, p2) + r2 <= r1 else "MORTO")
    except EOFError:
        break