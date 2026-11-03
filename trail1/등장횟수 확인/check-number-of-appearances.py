cnt = 0 # 짝수 등장 횟수

for _ in range(5):
    n = int(input())

    if n % 2 == 0:
        cnt += 1

print(cnt)