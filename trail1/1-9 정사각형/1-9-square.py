n = int(input())

cnt = 0
for i in range(n):
    for j in range(n):
        cnt += 1
        if cnt < 10:
            print(cnt, end = "")
        if cnt >= 10:
            print(cnt % 9, end = "")
    print()