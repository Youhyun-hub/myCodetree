m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

if m2 - m1 > 0:  # 비교 날짜가 같지 않아야 함
    diff = d2 + month[m1] - d1 + 1
    if m2 - m1 > 1:  # 상동
        for i in range(m1+1, m2):
            diff += month[i]
else:
    diff = d2 - d1 + 1

print(diff)