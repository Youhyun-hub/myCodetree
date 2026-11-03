cnt = 0
while cnt < 3:
    n = int(input())
    if n % 2 == 0:
        n //= 2
        print(n)
        cnt += 1
    else:  # 홀수면
        continue
    