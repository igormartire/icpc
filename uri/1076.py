t = 0
N = []
visited = []

def dfs(v1):
    global t, N, visited
    t += 1
    visited[v1] = True
    for v2 in N[v1]:
        if not visited[v2]:
            dfs(v2)
    t += 1

T = int(input())
for _ in range(T):
    t = 0
    start_node = int(input())
    num_nodes, num_edges = tuple(map(int, input().split(' ')))
    N = []
    visited = [False] * num_nodes
    for _ in range(num_nodes):
        N.append([])
    for _ in range(num_edges):
        v1, v2 = tuple(map(int, input().split(' ')))
        N[v1].append(v2)
        N[v2].append(v1)
    dfs(start_node)
    print(t - 2)
