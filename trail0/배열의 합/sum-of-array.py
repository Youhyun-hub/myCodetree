matrix = []
for _ in range(4):
    row = list(map(int, input().split()))
    matrix.append(row)
for i in range(4):
    total = 0
    for j in range(4):
        total += matrix[i][j]
    print(total)