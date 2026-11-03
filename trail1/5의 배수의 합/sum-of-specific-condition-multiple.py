a, b = map(int, input().split())

sum_v = 0
cnt = 0
if a <= b:
    for i in range(a, b+1):
        if i % 5 == 0:
            sum_v += i
else:
    for i in range(b, a+1):
        if i % 5 == 0:
            sum_v += i

print(sum_v)