T = int(input())
# T = 10000
for _ in range(T):
    s = list(reversed(input()))
    # s = ['a'] * 1000
    for i in range(len(s)):
        o = ord(s[i])
        if 65 <= o <= 90 or 97 <= o <= 122: # upper or lowercase
            s[i] = chr(o + 3)
    half_index = len(s) // 2
    s[half_index:] = [chr(ord(s[i]) - 1) for i in range(half_index, len(s))]
    print(''.join(s))
