'''
10개의 정수를 입력받아 500 미만의 수 중 가장 큰 수와 500 초과의 수 중 가장 작은 수를 출력하는 프로그램을 작성해보세요.
'''

num = list(map(int, input().split()))
num.sort()

before_500 = []  # 500이전의 수 배열

for n in num:
    while n < 500:
        around_min = n
        before_500.append(n)
        break


around_min = before_500[-1]
around_max = num[len(before_500)]        # 500 근처 값중 가장 크거나 작은 수

print(around_min, around_max)