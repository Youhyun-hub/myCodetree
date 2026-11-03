N = int(input())

sum_v = 0
for i in range(1, 101):
    sum_v += i
    if sum_v >= N:
        print(i)
        break