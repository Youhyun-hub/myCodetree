N = int(input())

for i in range(N):
    for j in range(N-i):
        print("*", end =" ")
    print()

for i in range(1, N):
    for j in range(-1, i):
        print("*", end = " ")
    print()