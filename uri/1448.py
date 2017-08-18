t = int(input())
for i in range(t):
    f, t1, t2 = input(), input(), input()
    print("Instancia " + str(i + 1))
    s1 = s2 = 0
    for j in range(len(f)):
        if t1[j] == f[j]:
            s1 += 1
        if t2[j] == f[j]:
            s2 += 1
    print("empate" if s1 == s2 else ("time 1" if s1 > s2 else "time 2"))
    print()