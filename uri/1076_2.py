T = int(input())
for _ in range(T):
    start_node = int(input())
    num_nodes, num_edges = tuple(map(int, input().split(' ')))
    N = []
    for _ in range(num_nodes):
        N.append(set([]))
    for _ in range(num_edges):
        v1, v2 = tuple(map(int, input().split(' ')))
        N[v1].add(v2)
        N[v2].add(v1)
    # BEGIN DFS
    visited = [False] * num_nodes
    visited_edges_count = 0
    stack = []
    stack.append(start_node)
    while stack:
        v1 = stack.pop()
        visited[v1] = True
        for v2 in N[v1]:
            if not visited[v2]:
                visited_edges_count += 1
                stack.append(v2)
    # END DFS
    print(visited_edges_count * 2)
