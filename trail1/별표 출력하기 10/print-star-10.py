n = int(input())

for i in range(2*n):
    if i % 2 == 0:  # 홀수 행 - 오름차순
        for j in range(i//2+1):
            print("*", end = " ")
        print()
    else:  # 짝수 행 - 내림차순    
        for j in range(n-i//2-1, -1, -1):
            print("*", end = " ")
        print()