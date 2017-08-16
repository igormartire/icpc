H, L = map(int, input().split(' '))
M = []
for i in range(H):
    M.append(list(map(int, input().split(' '))))

visited = []
for i in range(H):
    visited.append([False] * L)

min_area = H * L

def flood(l, c, color):
    if l < 0 or l >= H or c < 0 or c >= L:
        return 0
    if M[l][c] != color or visited[l][c]:
        return 0
    visited[l][c] = True
    return 1 + (flood(l-1, c, color) +
               flood(l, c-1, color) +
               flood(l+1, c, color) +
               flood(l, c+1, color))

for l in range(H):
    for c in range(L):
        if not visited[l][c]:
            area = flood(l, c, M[l][c])
            min_area = min(min_area, area)

print(min_area)