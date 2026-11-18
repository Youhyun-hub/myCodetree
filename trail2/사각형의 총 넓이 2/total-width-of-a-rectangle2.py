'''
이차원 평면 위에 N개의 직사각형이 주어집니다.
각 직사각형은 모든 변이 좌표축에 평행합니다.
이 직사각형들이 덮는 영역 전체의 넓이를 구하는 프로그램을 작성해보세요. 두 개 이상의 직사각형이 겹치는 부분은 한 번만 셉니다.
즉 각 직사각형 넓이의 단순 합이 아니라 합집합의 넓이를 구해야 합니다.
'''

n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

grid = [[0] * 201 for _ in range(201)]   # 정수 범위에 맞게 구성

for i in range(n):
    for r in range(x1[i], x2[i]):
        for c in range(y1[i], y2[i]):
            grid[r+100][c+100] = 1

cnt = 0
for i in range(201):
    for j in range(201):
        if grid[i][j] == 1:
            cnt += 1
 
print(cnt)