n = int(input())

cnt = 0
mul = []
# 5의 배수 카운트
for i in range(1, n*5*2+1):
    mul.append(i*n)
    if i*n % 5 == 0:
        cnt += 1
        if cnt == 2:
            break
print(*mul)