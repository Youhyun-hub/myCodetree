N = int(input())
arr = list(map(int, input().split()))


min_v = 1000000  # 이동 거리 합 최소
for i in range(N):
    v = 0  # 이동 거리 합
    for j in range(N):
        if i == j:
            continue
        else:
            v += arr[j] * abs(j - i)
    if min_v > v:
        min_v = v

print(min_v)