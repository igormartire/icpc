"""
Done: prune <=0 subtrees

INCOMPLETE - Received *Wrong Answer (50%)*
"""

class Node:

    def __init__(self):
        self.edges = []
        self.visited = False

    def add_neighbor(self, Id, node, beauty):
        self.edges.append(Edge(Id, node, beauty))

class Edge:

    def __init__(self, Id, node, beauty):
        self.Id = Id
        self.node = node
        self.beauty = beauty

def beautify(v1):
    v1.prunes = []
    v1.beauty = 0
    v1.visited = True
    for edge in v1.edges:
        v2 = edge.node
        if not v2.visited:
            # v2 is v1's child
            beautify(v2)
            branch_beauty = v2.beauty + edge.beauty
            if branch_beauty <= 0:
                v1.prunes.append(edge.Id)
            else:
                v1.beauty += branch_beauty
                v1.prunes += v2.prunes

N = int(input())
nodes = []
for _ in range(N):
    nodes.append(Node())

for _ in range(N - 1):
    d, a, b, w = tuple(map(int, input().split(' ')))
    nodes[a].add_neighbor(d, nodes[b], w)
    nodes[b].add_neighbor(d, nodes[a], w)

root = nodes[0]
beautify(root)
print(root.beauty, len(root.prunes))
if root.prunes:
    print(' '.join(map(str, root.prunes)))