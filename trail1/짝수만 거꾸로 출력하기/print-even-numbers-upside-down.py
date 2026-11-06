N = int(input())
arr = list(map(int, input().split()))

ans = []
for i in arr:
    if i % 2 == 0:
        ans.append(i)

print(*ans[::-1])