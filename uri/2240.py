class Node:
    def __init__(self):
        self.side = None
        self.center = None
        self.longest_trunk = 1

N = int(input())
nodes = [None] * (N + 1)
for i in range(1, N + 1):
    nodes[i] = Node()
for _ in range(N):
    i, l, k = tuple(map(int, input().split(' ')))
    nodes[i].side = nodes[l]
    nodes[i].center = nodes[k]

stack = []
stack.append(nodes[1])
left_handed_tree_longest_trunk = 1
while stack:
    node = stack.pop()
    if node.longest_trunk > left_handed_tree_longest_trunk:
        left_handed_tree_longest_trunk = node.longest_trunk 
    if node.center:
        node.center.longest_trunk += node.longest_trunk
        stack.append(node.center)
    if node.side:
        stack.append(node.side)

left_handed_tree_longest_trunk_from_root = 0
node = nodes[1]
while node:
    left_handed_tree_longest_trunk_from_root += 1
    node = node.center

M = int(input())
nodes = [None] * (M + 1)
for i in range(1, M + 1):
    nodes[i] = Node()
for _ in range(M):
    p, q, r = tuple(map(int, input().split(' ')))
    nodes[p].center = nodes[q]
    nodes[p].side = nodes[r]

stack.append(nodes[1])
right_handed_tree_longest_trunk = 1
while stack:
    node = stack.pop()
    if node.longest_trunk > right_handed_tree_longest_trunk:
        right_handed_tree_longest_trunk = node.longest_trunk 
    if node.center:
        node.center.longest_trunk += node.longest_trunk
        stack.append(node.center)
    if node.side:
        stack.append(node.side)

right_handed_tree_longest_trunk_from_root = 0
node = nodes[1]
while node:
    right_handed_tree_longest_trunk_from_root += 1
    node = node.center

print(N + M - max(
    min(left_handed_tree_longest_trunk_from_root, right_handed_tree_longest_trunk),
    min(left_handed_tree_longest_trunk, right_handed_tree_longest_trunk_from_root)
))
