'''
N개의 정수가 주어졌을 때, 중복하여 등장하지 않는 정수 중 최댓값을 구하는 프로그램을 작성해보세요.
'''

n = int(input())
num = list(map(int, input().split()))
max_v = max(num)
cnt = 0  # 중복 횟수

num.sort()

ans = []
for i in range(n):
    if num.count(num[i]) == 1:  # count가 하나뿐이면
        ans.append(num[i])
    else:
        ans.append(-1)



print(max(ans))