n, k = map(int, input().split()) # n = 칸 수, k = 명령 수
c = [tuple(map(int, input().split())) for _ in range(k)]
arr = [0] * n
for a, b in c:
    for j in range(a, b+1):
        arr[j-1] += 1
print(max(arr))
        