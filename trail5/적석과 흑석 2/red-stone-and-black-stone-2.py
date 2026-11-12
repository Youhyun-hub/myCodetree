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

'''  초과되는 코드
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
