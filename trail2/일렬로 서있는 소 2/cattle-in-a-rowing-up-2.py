'''
N마리의 소가 위치 1부터 위치 N까지 순서대로 한 줄로 서 있습니다.
위치 i에 서 있는 소의 키는 Ai이며, 예를 들어 첫 번째 위치에 서 있는 소의 키는 Ai입니다.
서로 다른 세 소의 위치를 (i, j, k)라고 했을 때, i<j<k와 Ai≤Aj≤Ak를 동시에 만족하는 (i, j, k)의 개수를 구하는 프로그램을 작성해보세요.
'''

N = int(input())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if A[i] <= A[j] <= A[k]:
                cnt += 1

print(cnt)