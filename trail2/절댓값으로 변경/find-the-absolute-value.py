n = int(input())
arr = list(map(int, input().split()))

def get_abs(row):
    for i in range(len(row)):
        row[i] = abs(row[i])
    print(*row)

get_abs(arr)
