arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        res = arr[:i]
        break
for x in range(len(res)):
    if res[x] % 2 != 0:  # 홀수
        res[x] += 3
    else:  # 짝수
        res[x] //= 2

print(*res)