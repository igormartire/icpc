""" https://www.urionlinejudge.com.br/judge/problems/view/2243
"""

"""
Complexity analysis:
Memory: O(n) where n is the number of columns.
Speed: O(n)
"""

n = int(input())
heights = list(map(int, input().split(' ')))

max_from_left = [0] * n
max_from_right = [0] * n
local_max = [0] * n

max_from_left[0] = min(1, heights[0])
for i in range(1, n):
    max_from_left[i] = min(max_from_left[i-1] + 1, heights[i])

max_from_right[n-1] = min(1, heights[n-1])
for i in range(n-2, -1, -1):
    max_from_right[i] = min(max_from_right[i+1] + 1, heights[i])

for i in range(n):
    local_max[i] = min(max_from_left[i], max_from_right[i])

print(max(local_max))
