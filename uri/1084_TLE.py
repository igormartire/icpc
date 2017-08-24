N, D = tuple(map(int, input().split(' ')))
while N != 0 and D != 0:
    ans = ""
    num = tuple(map(int, input()))
    remaining_num_start_idx = 0
    remaining_rm = D
    while remaining_rm > 0:
        len_remaining_num = N - remaining_num_start_idx
        if len_remaining_num == remaining_rm:
            remaining_rm = 0
            remaining_num_start_idx = N
        else:
            keep_idx = remaining_num_start_idx
            if num[keep_idx] < 9:
                for i in range(remaining_num_start_idx + 1, remaining_num_start_idx + remaining_rm + 1):
                    if num[i] > num[keep_idx]:
                        keep_idx = i
                        if num[i] == 9:
                            break
            remaining_rm -= keep_idx
            ans += str(num[keep_idx])
            remaining_num_start_idx = keep_idx + 1
    print(ans + ''.join(map(str, num[remaining_num_start_idx:])))
    N, D = tuple(map(int, input().split(' ')))