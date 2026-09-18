n = int(input())  # 명령 수
x = []  # 이동 수
dir = [] # 방향
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)


ranges = []  # 범위 튜플 넣을 리스트
lines = [[] for _ in range(n)]  # 선분 안의 모든 좌표
cnt = [0] * (2*sum(x)+1)  # 0까지 포함
cur = 0   # 현 위치
total = 0  # 좌표 개수
for i in range(n):
    if dir[i] == "L":
        start = cur
        end = cur - x[i]
        cur = end
        ranges.append((start, end))
        

    else:
        start = cur
        end = cur + x[i]
        cur = end
        ranges.append((start, end))
    
for i in range(n):
    a, b = ranges[i]
    for j in range(min(a, b), max(a, b)):
        lines[i].append(j)

for i in range(n):
    for k in lines[i]:
        cnt[k+sum(x)] += 1
        if cnt[k+sum(x)] == 2:
            total += 1

print(total)