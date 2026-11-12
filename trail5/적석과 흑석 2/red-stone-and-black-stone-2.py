'''
1부터 C까지 번호가 매겨진 빨간 돌 C개와 1부터 N까지 번호가 매겨진 검정 돌 N개가 있습니다. 각 빨간돌에는 정수 T가 하나씩 적혀있고, 각 검정돌에는 두 개의 정수 A, B가 적혀있습니다.
i번 빨간돌의 T 값을 Ti , j번 검정돌의 A, B 값을 Aj ,Bj라 할 때, Aj ≤ Ti ≤Bj를 만족하도록 빨간돌과 검정돌을 1:1로 짝지으려 합니다.
하나의 빨간돌 혹은 검정돌은 최대 한 개의 검정돌 혹은 빨간돌과 짝지어질 수 있을 때, 짝지어지는 빨간돌과 검정돌의 쌍은 최대 몇 개인지 구하는 프로그램을 작성해보세요.
'''

import heapq

C, N = map(int, input().split())       # C - 빨간 돌 범위, N - 검정돌 범위
T = [int(input()) for _ in range(C)]   # 빨간 돌이 가진 번호
T.sort()

AB = [tuple(map(int, input().split())) for _ in range(N)]  # 검은 돌이 가진 번호
AB.sort()
A = [ab[0] for ab in AB]
B = [ab[1] for ab in AB]

# heapq 사용하기
heap = []
j = 0 # 포인터
count = 0
for t in T:
    # A <= t 인 검은 돌의 B를 heap에 넣기 (포인터 j 사용)
    while j < len(AB) and A[j] <= t:
        heapq.heappush(heap, B[j])
        j += 1
    # heap 맨 위의 B가 t보다 작으면 버리기 (반복)
    while heap and heap[0] < t:
        heapq.heappop(heap)
    #  heap에 남은 게 있으면 하나 꺼내고 count += 1
    if heap:
        heapq.heappop(heap)
        count += 1

print(count)


''' 시간 초과되는 코드
visit = [0] * N  # 검은 돌 사용 여부
for red in range(C):
    select = -1
    for black in range(N):
        if A[black] <= T[red] <= B[black] and visit[black] == 0:
            # 첫 후보는 바로 저장하고, 이후에는 B값이 더 작은 후보로 교체
            if select == -1 or B[black] < B[select]:
                select = black

    if select != -1:
        visit[select] = 1

print(visit.count(1))
'''

''' by 코드트리
from sortedcontainers import SortedSet

# 변수 선언 및 입력:
c, n = tuple(map(int, input().split()))
red_stones = [
    int(input())
    for _ in range(c)
]

black_stones = []
for _ in range(n):
    a, b = tuple(map(int, input().split()))
    black_stones.append((b, a))

# 빨간 돌을 전부 treeset에 넣어줍니다.
# 추후 검은색 돌 기준으로
# Aj보다 같거나 큰 최소 Ti값을 빠르게 찾기 위해
# treeset을 이용합니다.
red_s = SortedSet(red_stones)

# b 기준 오름차순 정렬을 진행합니다.
black_stones.sort()

# b가 작은 돌부터 보며
# a보다 같거나 큰 최소 Ti를 찾습니다.
# 이 값이 만약 b보다 같거나 작다면
# 이 돌을 선택하는 것이 최선입니다.
ans = 0
for b, a in black_stones:
    # a보다 같거나 큰 값이 있다면
    idx = red_s.bisect_left(a)
    if idx != len(red_s):
        # 최소 Ti를 선택합니다.
        ti = red_s[idx]
        # Ti가 b보다 같거나 작다면
        # 매칭을 진행합니다.
        if ti <= b:
            ans += 1
            red_s.remove(ti)

print(ans)
'''