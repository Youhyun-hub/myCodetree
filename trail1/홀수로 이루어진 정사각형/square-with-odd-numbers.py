n = int(input())

for i in range(n):
    for j in range(0, n*2-1, 2):
        print(11+2*i+j, end=" ")
    print()