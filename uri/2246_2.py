H, L = map(int, input().split(' '))
M = []
for i in range(H):
    M.append(list(map(int, input().split(' '))))

visited = []
for i in range(H):
    visited.append([False] * L)

min_area = H * L

def flood(l, c):
    color = M[l][c]
    stack = [(l, c)]
    area = 0
    while stack:
        l, c = stack.pop()
        if l < 0 or l >= H or c < 0 or c >= L:
            continue
        if M[l][c] != color or visited[l][c]:
            continue
        visited[l][c] = True
        area += 1
        stack += [(l-1, c), (l, c-1), (l+1, c), (l, c+1)]
    return area

for l in range(H):
    for c in range(L):
        if not visited[l][c]:
            area = flood(l, c)
            min_area = min(min_area, area)

print(min_area)