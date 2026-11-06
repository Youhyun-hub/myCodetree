N = int(input())
arr = list(map(int, input().split()))
cnt = [0] * 9  # 카운트 배열

for i in range(N):
    cnt[arr[i]-1] += 1

for i in range(9):
    print(cnt[i])
