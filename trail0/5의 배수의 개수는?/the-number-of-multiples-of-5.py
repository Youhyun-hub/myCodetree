matrix = []
for _ in range(4):
    row = list(map(int, input().split()))
    matrix.append(row)
cnt = 0
for i in range(4):
    for j in range(4):
        if matrix[i][j] % 5 == 0:
            cnt += 1
print(cnt)