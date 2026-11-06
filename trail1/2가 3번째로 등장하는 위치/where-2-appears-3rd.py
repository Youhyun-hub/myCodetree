'''
N개의 정수가 주어졌을 때, 2 가 3 번째로 등장할 때 몇 번째 위치의 글자인지 출력하는 프로그램을 작성해보세요.
'''

N = int(input())
arr = list(map(int, input().split()))
cnt = 0  # 2가 나온 횟수

for i in range(N):
    if arr[i] == 2:
        cnt += 1

        if cnt == 3:
            print(i+1)  # 1번째부터 시작