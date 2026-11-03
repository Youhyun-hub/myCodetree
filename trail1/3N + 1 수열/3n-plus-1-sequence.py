N = int(input())
cnt = 0  # 연산 횟수

while N > 1:
    if N % 2 == 0:
        N //= 2
        cnt += 1
    else:
        N = (N * 3) + 1
        cnt += 1

print(cnt)
