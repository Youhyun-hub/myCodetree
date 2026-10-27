'''
N개의 정점이 존재하고 M개의 간선의 양 끝 정점과 가중치가 주어질 때,
1번 정점에서 다른 모든 정점으로 가는 최단 경로를 구하는 프로그램을 작성해보세요.
이때 주어지는 정점과 간선들로 구성되는 그래프는 단방향 그래프라고 가정합니다.
'''

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graph = [[0] * (n+1) for _ in range(n+1)]
visit = [0] * (n+1)
dis = [float('inf')] * (n+1)  # 거리 변수

# 인접 행렬 만들기
for x, y, z in edges:
    graph[x][y] = z

# 시작 위치는 거리 0
dis[1] = 0

for i in range(1, n+1):
    min_idx = 0  # -1 정점 초기화
    for j in range(1, n+1):  # 미방문 정점 찾기
        if visit[j]:
            continue
        
        if min_idx == 0 or dis[min_idx] > dis[j]:  # 더 짧은 거리 찾으면 갱신
            min_idx = j
    
    visit[min_idx] = 1
    
    for j in range(1, n+1):  # 최소 거리 정점 찾기
        if graph[min_idx][j] == 0:
            continue  # 정점 간 연결이 없을 경우
        
        dis[j] = min(dis[j], dis[min_idx] + graph[min_idx][j])  # 목적지 j로 가기 위한 최소 거리 찾기


for i in range(2, n+1):
    print(dis[i])
