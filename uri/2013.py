s = input()
n = [int(c) for c in s]

fix_mode = False

stock = [2]*10
for i in range(len(n)):
	num = n[i]
	if stock[num]:
		stock[num] -= 1
	else:
		stock[num] -= 1
		fix_mode = True
		break

barrier = i

if fix_mode:
	for i in range(barrier, -1, -1):
		num = n[i]
		stock[num] += 1
		found = False
		for j in range(num-1, -1, -1):
			if stock[j]:
				found = True
				n[i] = j
				if i != 0 or j != 0:
					stock[j] -= 1
				break
		if found:
			break
	start = i+1
	for i in range(start, len(n)):
		for j in range(9, -1, -1):
			if stock[j]:
				n[i] = j
				stock[j] -= 1
				break

print(int(''.join(map(str, n))))