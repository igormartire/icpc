fib = [0] * 40
num_calls = [0] * 40

fib[0] = 0
fib[1] = 1

num_calls[0] = num_calls[1] = 0

for i in range(2, 40):
    fib[i] = fib[i-1] + fib[i-2]
    num_calls[i] = 2 + num_calls[i-1] + num_calls[i-2]


X = int(input())
for _ in range(X):
    n = int(input())
    print("fib({0}) = {1} calls = {2}".format(n, num_calls[n], fib[n]))