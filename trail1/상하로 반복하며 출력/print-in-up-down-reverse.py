n = int(input())

for i in range(n):
    for j in range(n):
        if j % 2 != 0:  # 짝수 열
            print(n-i, end = "")
        else:  # 짝수 열
            print(i+1, end ="")
    print()
