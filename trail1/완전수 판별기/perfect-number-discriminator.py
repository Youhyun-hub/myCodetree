'''
정수 N이 주어졌을 때, N이 완전수인지 판단하는 프로그램을 작성해보세요.
완전수란 자기 자신을 제외한 약수의 합이 자신이 되는 수를 나타냅니다.
예를 들어 6의 경우 1+2+3=6 이기 때문에 완전수입니다.
'''

n = int(input())

ans = 'N'
div = []  # 약수 모음

for i in range(1, n):  # 약수 구하기
    if n % i == 0:
        div.append(i)

sum_v = 0  # 약수 합
for j in div:
    sum_v += j
    
if sum_v == n:
    ans = 'P'

print(ans)


