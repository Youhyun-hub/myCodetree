matrix = []
for _ in range(4):
    row = list(map(int, input().split()))
    matrix.append(row)

total = 0
for i in range(4):
    for j in range(i+1):
        total += matrix[i][j]
print(total)