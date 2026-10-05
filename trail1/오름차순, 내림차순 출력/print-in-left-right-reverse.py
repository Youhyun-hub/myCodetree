n = int(input())

for i in range(n):
    for j in range(n):
        if i % 2 != 0:  # 짝수 행
            print(n-j, end = "")
        else:
            print(j+1, end = "")
    print()