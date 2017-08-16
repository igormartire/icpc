r, g, b = map(lambda s: int(s, 16), (input(), input(), input()))
cnt_r = 1
cnt_g = (r//g) ** 2
cnt_b = ((g//b) ** 2) * cnt_g
print('%x' % (cnt_r + cnt_g + cnt_b))
