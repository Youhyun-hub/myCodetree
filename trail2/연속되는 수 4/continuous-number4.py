n = int(input())
arr = [int(input()) for _ in range(n)]

max_cnt = 0
cnt = 1
for i in range(n-1):
    if arr[i] < arr[i+1]:
        cnt += 1
    else:
        cnt = 1
    max_cnt = max(max_cnt, cnt)
    
print(max_cnt)