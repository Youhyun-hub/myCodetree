arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        res = arr[:i][::-1]
    else:
        res = arr[::-1]

print(*res)