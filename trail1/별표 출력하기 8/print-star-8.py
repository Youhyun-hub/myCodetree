n = int(input())

for i in range(n):
    if i % 2  == 0:  # 홀수 행
        print("*")
    else:  # 짝수 행
        print("* " * (i+1))