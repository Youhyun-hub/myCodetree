n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []

for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

    cur = 0  # 현 위치
    tile = [0] * (2*sum(x)+1)
    # left = [0] * (2*sum(x)+1)
    # right = [0] * (2*sum(x)+1)

for i in range(n):
    if dir[i] == "L":
        start = cur
        end = cur - x[i] + 1
        cur = end
        for j in range(min(start, end), max(start, end)+1):
            # left[j] += 1
            tile[j] = "L"
    else:  # 오른쪽
        start = cur
        end = cur + x[i] - 1
        cur = end
        for j in range(min(start, end), max(start, end)+1):
            # right[j] += 1
            tile[j] = "R"
            
print(tile.count("L"), tile.count("R"))