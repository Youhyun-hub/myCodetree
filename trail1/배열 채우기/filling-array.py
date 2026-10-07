arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        arr.pop(i)
        res = arr[::-1]
    else:
        res = arr[::-1]

print(*res)