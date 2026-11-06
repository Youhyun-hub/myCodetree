'''
향후 N년 간의 자동차 가격 정보가 미리 주어졌을 때, 자동차를 단 한 번 사서 되팔 때의 이익을 최대화하고자 합니다.
낼 수 있는 최대 이익을 출력하는 프로그램을 작성해보세요.
단, 자동차를 사기 전에는 팔 수 없습니다.
'''

n = int(input())
price = list(map(int, input().split()))

rest = []  # 차익

for i in range(n-1):
    for j in range(i, n):
        if price[i] < price[j]:
            rest.append(price[j] - price[i])
        else:
            rest.append(0)  # 0을 최대값으로 갖도록 함
print(max(rest))            
