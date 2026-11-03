sum_v = 0
cnt = 0

for _ in range(10):
    n = int(input())

    if 0<=n<=200:
        sum_v += n
        cnt += 1

print(sum_v, f"{sum_v/cnt:.1f}")