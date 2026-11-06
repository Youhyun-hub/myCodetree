n = int(input())
a = list(map(int, input().split()))

min_v = 100  # 주어진 정수 범위 중 가장 큰 값

for num in a:
    if min_v > num:
        min_v = num
        
min_cnt = 0

for num in a:
    if min_v == num:
        min_cnt += 1

print(min_v, min_cnt)