n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)] # 1단계: 2차원 배열 만들기

# 2단계: 열 순서로 순회하기
for i in range(n):
    if i % 2 == 0: # 짝수열  1-> n 순회
        for j in range(n):
            arr[j][i] = j + 1
    
    else:
        for j in range(n - 1, -1, -1):
            arr[j][i] = n - j

# 4단계: 출력하기
for i in range(n):
    for j in range(n):
        print(arr[i][j], end="")
    print()
