""" https://www.urionlinejudge.com.br/judge/problems/view/2243
"""

"""
Complexity analysis:
Memory: O(n) where n is the number of columns.
Speed: O(max_height * n) where max_height is the height of the
    isosleces triangle with the maximum height given the input
    wall. Notice that max_height <= N/2.
"""

n = int(input())
heights = list(map(int, input().split(' ')))

next_heights = [0] * n
max_height = 0

grew = False
if any(heights):
    grew = True

while grew:
    max_height += 1
    grew = False
    for i in range(max_height, n - max_height):
        if heights[i-1] > 0 and heights[i] > 1 and heights[i+1] > 0:
            next_heights[i] = heights[i] - 1
            grew = True
        else:
            next_heights[i] = 0
    # Swapping for efficiency. If you rather
    # be clear, use `next_heights = [0] * n`
    heights, next_heights = next_heights, heights

print(max_height)
