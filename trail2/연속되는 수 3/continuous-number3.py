N = int(input())
arr = [int(input()) for _ in range(N)]

max_v = 0
cnt = 1

for i in range(N-1):
    if (arr[i+1] > 0 and arr[i] > 0) or arr[i+1] < 0 and arr[i] < 0:
        cnt += 1
    else:
        cnt = 1

    max_v = max(max_v, cnt)

print(max_v)