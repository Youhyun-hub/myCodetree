N = int(input())
arr = list(map(int, input().split()))

diff = []  # 두 정수의 차
for i in range(N-1):
    for j in range(i, N):
        if arr[i] < arr[j]:
            diff.append(arr[j] - arr[i])

print(min(diff))