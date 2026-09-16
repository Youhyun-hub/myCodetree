n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
arr = [0] * 100

cnt = 0
for a, b in segments:
    for i in range(a, b+1):
        arr[i-1] += 1
    cnt = max(arr)
print(cnt)