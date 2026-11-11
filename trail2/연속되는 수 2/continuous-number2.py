'''
N개의 정수가 주어졌을 때,
같은 정수가 연속하여 나오는 횟수 중 최댓값을 구하는 프로그램을 작성해보세요.
'''

n = int(input())
arr = [int(input()) for _ in range(n)]

cnt = 1
for i in range(n-1):
    if arr[i] == arr[i+1]:
        cnt += 1

print(cnt)