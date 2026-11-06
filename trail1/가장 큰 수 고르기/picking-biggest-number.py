arr = list(map(int, input().split()))
max_v = 0  # 가장 큰 값

for num in arr:
    if max_v < num:
        max_v = num

print(max_v)