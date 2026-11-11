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