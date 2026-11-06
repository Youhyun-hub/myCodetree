n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0   # m의 개수
for num in arr:
    if num == m:
        cnt += 1

print(cnt)