num = list(map(int, input().split()))

sum_v = 0

rest = []
for i in range(10):
    if num[i] == 0:
        rest = num[:i]
        break
    else:
        rest = num

cnt = 0  # 2의 배수 개수
for j in rest:
    if j % 2 == 0:
        sum_v += j
        cnt += 1

print(cnt, sum_v)