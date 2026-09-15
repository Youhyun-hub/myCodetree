num = list(map(int, input().split()))

for i in range(1, len(num)):
    if num[i] % 3 == 0:
        print(num[i-1])
        break