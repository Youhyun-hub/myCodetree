n = int(input())
arr = [[0] * n for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        cnt += 1
        arr[i][j] = cnt

    if i % 2 != 0:  # 짝수 행
        arr[i] = arr[i][::-1]

for i in range(n):
    for j in range(n): 
        print(arr[i][j], end=" ")
    print()