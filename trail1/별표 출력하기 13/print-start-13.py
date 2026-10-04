N = int(input())

for i in range(N*2):
    if i % 2 == 0:  # 홀수 행
        for _ in range(N-i//2):
            print("*", end=" ")
        print()
    else:  # 짝수 행
        for _ in range(i//2+1):
            print("*", end=" ")
        print()