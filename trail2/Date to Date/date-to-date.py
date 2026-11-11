'''
2011년 m1월 d1일부터 2011년 m2월 d2일까지는 총 며칠이 있는지를 계산하는 프로그램을 작성해보세요.
2011년은 윤년이 아닌 해이기 때문에 2월은 28일까지 있습니다.
단, 날짜를 셀 때에는 시작하는 날과 끝나는 날을 모두 포함하여 세도록 합니다.
'''

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

'''
[코트트리 풀이]
# 변수를 선언하고 입력을 받습니다.
m1, d1, m2, d2 = tuple(map(int, input().split()))


def num_of_days(m, d):
    # 계산 편의를 위해 각 달에 며칠이 있는지를 적어줍니다.
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0

    # 1월부터 (m - 1)월까지는 전부 꽉 채워져 있습니다.
    for i in range(1, m):
        total_days += days[i]

    # m월의 경우에는 정확히 d일만 있습니다.
    total_days += d

    return total_days


# 결과를 출력합니다.
total_days = num_of_days(m2, d2) - num_of_days(m1, d1) + 1
print(total_days)


'''