c, n = input().split()
n = int(n)

if c == 'A':
    for i in range(1, n+1):
        print(i, end=" ")
else:  # 'D'일 때
    for i in range(n, 0, -1):
        print(i, end=" ")