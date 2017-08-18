import itertools

d = {}

ps = list(itertools.permutations('01234567'))
for p in ps:
    h = hash(','.join(p))
    if p in d:
        print(d[p])
        print(p)
    else:
        d[p] = p
print("End")
