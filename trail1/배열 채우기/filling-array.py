arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        res = arr[:i]
        res = res[::-1]
    else:
        res = arr[::-1]

print(*res)