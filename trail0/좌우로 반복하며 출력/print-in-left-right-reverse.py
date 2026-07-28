n = int(input())


for i in range(n):
    cnt = 0
    row = []
    
    for j in range(n):
        cnt += 1
        row.append(cnt)

    if i % 2 != 0:  # 홀수 행일 때
        for j in range(n-1, -1, -1):
            print(row[j], end= "")
    
    else:
        for j in range(n):
            print(row[j], end= "")
    
    print()