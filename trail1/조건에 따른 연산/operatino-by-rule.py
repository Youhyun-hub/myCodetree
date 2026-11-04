N = int(input())
cnt = 0  # 연산 횟수

while N < 1000:
    if N % 2 == 0:    # 짝수
        N = N * 3 + 1
        cnt += 1
    else:             # 홀수
        N = N * 2 + 2
        cnt += 1

print(cnt)
