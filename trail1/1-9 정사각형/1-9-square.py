n = int(input())

cnt = 0
for i in range(n):
    for j in range(n):
        cnt += 1
        if cnt < 10:
            print(cnt, end = "")
        elif cnt >= 10:
            if cnt % 9 != 0:
                print(cnt % 9, end = "")
            else:  # cnt % 9 == 0
                cnt = 9
                print(cnt, end = "")
    print()