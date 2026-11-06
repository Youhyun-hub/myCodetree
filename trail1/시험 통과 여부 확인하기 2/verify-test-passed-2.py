N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0  # pass 학생 수
for i in range(N):
    scores = 0    # 학생 별 점수 합
    for j in range(4):  # 과목 수
        scores += arr[i][j]
    avg = scores // 4
        
    if avg >= 60:
        cnt += 1
        print("pass")
    else:
        print("fail")

print(cnt)