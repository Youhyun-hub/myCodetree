arr = list(map(int, input().split()))
min_v = 999
max_v = 0

for num in arr:
    if num == 999 or num == -999:
        break
    if min_v > num:
        min_v = num
    if max_v < num:
        max_v = num

print(max_v, min_v)