'''
Non-greedy
E.g.:

M = 117
1 9 10

Greedy choice: 117 = 11 * 10 + 7 * 1 = 18 stones
Non-greedy choice: 117 = 13 * 9 = 13 stones
Best: 117 = 9 * 10 + 3 * 9 = 12 stones
'''
min_blocks = [0] * (1000001)

T = int(input())
for _ in range(T):
    N, M = tuple(map(int, input().split(' ')))
    A = tuple(map(int, input().split(' ')))

    for Mi in range(1, M+1):
        min_for_Mi = Mi
        for a in A:
            if Mi - a >= 0:
                min_for_Mi = min(min_for_Mi, 1 + min_blocks[Mi-a])
        min_blocks[Mi] = min_for_Mi

    print(min_blocks[M])