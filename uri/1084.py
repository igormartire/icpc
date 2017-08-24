N, D = tuple(map(int, input().split(' ')))
while N != 0 and D != 0:
    num = tuple(map(int, input()))
    occurs = [0] * 10 # number of occurrences of each digit so far
    removals = [0] * 10 # number of removals of each digit so far
    rm = D # remaining removals
    for i in range(N):
        digit = num[i]
        occurs[digit] += 1
        for j in range(digit):
            if occurs[j] > 0:
                if occurs[j] >= rm:
                    occurs[j] -= rm
                    removals[j] += rm
                    rm = 0
                    break
                else:
                    removals[j] += occurs[j]
                    rm -= occurs[j]
                    occurs[j] = 0
        if rm == 0:
            break

    ans = ""
    for i in range(N - rm):
        digit = num[i]
        if removals[digit] > 0:
            removals[digit] -= 1
        else:
            ans += str(digit)

    print(ans)

    N, D = tuple(map(int, input().split(' ')))