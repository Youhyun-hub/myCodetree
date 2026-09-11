n = int(input())

def f(N):
    total = sum([_ for _ in range(1, N+1)])
    return total // 10

print(f(n))