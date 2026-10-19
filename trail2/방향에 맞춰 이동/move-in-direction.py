'''
(0, 0)에서 시작하여 총 N번 움직여보려고 합니다. N번에 걸쳐 움직이려는 방향과 움직일 거리가 주어졌을 때, 최종 위치를 출력하는 프로그램을 작성해보세요.
단, dx, dy 테크닉을 활용하여 문제를 해결해주세요.
'''

n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

ci = 0
cj = 0
for k in range(n):
    if dir[k] == 'N':
        ci += dist[k]
    elif dir[k] == 'S':
        ci -= dist[k]
    elif dir[k] == 'E':
        cj += dist[k]
    else:
        cj -= dist[k]

print(cj, ci)