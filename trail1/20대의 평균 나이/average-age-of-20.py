sum_v = 0  # 나이 합
cnt = 0  # 사람 수

while True:
    n = int(input())
    if n < 30:
        sum_v += n
        cnt += 1
    else:
        print(f"{sum_v / cnt:.2f}")
        break
    