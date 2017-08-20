t = int(input())
for _ in range(t):
    top = input()
    mid = input().split(' ')
    bot = input()
    pairs = [(top, bot), (mid[0], mid[2]), (mid[1], mid[3])]
    stars_pairs_count = 0
    for p in pairs:
        if p[0] == '*' and p[1] == '*':
            stars_pairs_count += 1
    if stars_pairs_count == 0:
        print(1)
    elif stars_pairs_count == 1:
        print(2)
    elif stars_pairs_count == 2:
        print(8)
    elif stars_pairs_count == 3:
        print(48)