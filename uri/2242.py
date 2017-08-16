vowels = list(filter(lambda c: c in 'aeiou', input()))
if vowels == list(reversed(vowels)):
    print('S')
else:
    print('N')
