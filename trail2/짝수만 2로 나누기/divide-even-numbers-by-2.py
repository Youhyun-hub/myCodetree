n = int(input())
arr = list(map(int, input().split()))

def get_twos(num, row):
    for i in range(num):
        if row[i] % 2 == 0:
            row[i] = row[i] // 2
    print(*row)

get_twos(n, arr)