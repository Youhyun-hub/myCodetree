'''
N개의 집이 x=1에서 x=N까지 순서대로 놓여 있고, i번째 집에는 Ai명의 사람이 살고 있습니다.
(1≤i≤N) 이들은 회의를 위해 N개의 집 중 한 곳에 전부 모이려고 합니다.
적절한 집을 선택하여 모든 사람들의 이동 거리의 합이 최소가 되도록 하는 프로그램을 작성해보세요.
'''

N = int(input())
arr = list(map(int, input().split()))


min_v = 1000000  # 이동 거리 합 최소
for i in range(N):
    v = 0  # 이동 거리 합
    for j in range(N):
        if i == j:
            continue
        else:
            v += arr[j] * abs(j - i)
    if min_v > v:
        min_v = v

print(min_v)