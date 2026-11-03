a, b = map(int, input().split())

sum_v = 0
cnt = 0
for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum_v += i
        cnt += 1

print(sum_v, f"{sum_v/cnt:.1f}")