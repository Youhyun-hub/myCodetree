n = int(input())
nums = list(map(int, input().split()))
max_v = 0
cnt = 0

for num in nums:
    if max_v < num:
        max_v = num

    elif max_v == num:   # 중복 발생시
        max_v = -1  # -1을 출력
        break
    else:  # 중복이 없으면
        continue
print(max_v)