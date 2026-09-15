n = int(input())
num = list(map(int, input().split()))

for i in range(len(num)):
    print(num[i]**2, end=" ")