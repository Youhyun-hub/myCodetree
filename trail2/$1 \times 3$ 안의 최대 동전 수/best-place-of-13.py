'''
N×N 크기의 격자 정보가 주어집니다.
이때 해당 위치에 동전이 있다면 1, 없다면 0이 주어집니다.
N×N 격자를 벗어나지 않도록 1×3 크기의 직사각형을 적절하게 잘 잡아서 해당 범위 안에 들어 있는 동전의 개수를 최대로 하는 프로그램을 작성해보세요.
단, 1×3 크기의 직사각형은 세로로는 길이 1, 가로로는 길이 3으로만 이루어지게 잡아야 하며, 회전시킬 수 없음에 유의합니다.
'''

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_cnt = 0
for i in range(n):
    for j in range(n-2):
        cnt = 0
        for k in range(j, j+3):
            if grid[i][k] == 1:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt

print(max_cnt)
