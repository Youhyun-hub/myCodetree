'''
0이 아닌 N개의 정수가 주어졌을 때, 부호가 동일한 정수로만 이루어진 연속 부분 수열 중 최대 길이를 구하는 프로그램을 작성해보세요.

연속 부분 수열이란, 어떤 수열에서 연속한 구간에 속하는 정수를 모두 뽑았을 때 나오는 부분 수열을 의미합니다.
'''


N = int(input())
arr = [int(input()) for _ in range(N)]

max_v = 1
cnt = 1

for i in range(N-1):
    if (arr[i+1] > 0 and arr[i] > 0) or arr[i+1] < 0 and arr[i] < 0:
        cnt += 1
    else:
        cnt = 1

    max_v = max(max_v, cnt)

print(max_v)