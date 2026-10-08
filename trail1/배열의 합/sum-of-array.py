arr = [list(map(int, input().split())) for _ in range(4)]

for i in range(4):
    for _ in range(4):
        row_sum = sum(arr[i])
    print(row_sum)