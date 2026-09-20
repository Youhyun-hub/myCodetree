n = int(input())  # 명령 수
commands = [tuple(input().split()) for _ in range(n)]
x = []  # 이동 수
dir = []  # 방향
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# L => 흰색, R => 검은색, 겹치는 구간 => 회색
cur = 0  # 현 위치
tiles = [[0] * (2*sum(x)+1) for _ in range(n)]

# 순서 따지기 & 회색으로 바꾸기
white = [0] * (2*sum(x)+1)  # 흰색
black = [0] * (2*sum(x)+1)  # 검은색
gray = [0] * (2*sum(x)+1)  # 회색

for i in range(n):
    if dir[i] == "L":  # 왼쪽
        start = cur
        end = cur - x[i]
        cur = end
        for j in range(min(start, end), max(start, end)):
            # 각 두번 이상 나오지 않으면
            if white[i] + black[i] < 3:
               

    else:  # 오른쪽
        start = cur
        end = cur + x[i]
        cur = end
        for j in range(min(start, end), max(start, end)):
            tiles[i][j+sum(x)] = "black"

print(tiles)

for i in range(n):
    for j in range(len(tiles[i])):
        if tiles[i][j] == "white":
            cnt_w[j] += 1
        elif tiles[i][j] == "black":
            cnt_b[j] += 1
        
        # # 회색 처리
        # if cnt_w[j] >= 2 and cnt_b[j] >= 2:
        #     cnt_g[j] += 1
        # elif cnt_w[j] < 2 and cnt_b[j] < 2: # 다음에 나온 색으로 바꾸기
        #     if cnt_w[j] !=0 and cnt_b[j] != 0:
print(cnt_w, cnt_b)
    
# print(cnt_w, cnt_b, cnt_g)