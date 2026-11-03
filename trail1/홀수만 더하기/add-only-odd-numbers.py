N = int(input())

sum_v = 0
for i in range(N):
    num = int(input())
    if num % 2 != 0 and num % 3 == 0:
        sum_v += num

print(sum_v)