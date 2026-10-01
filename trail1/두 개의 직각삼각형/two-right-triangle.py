N = int(input())

for i in range(N):
    for j in range(N-i):
        print("*", end="")
    for j in range(1, i+1):
        print(" "*2, end="")
    for j in range(N-i):
        print("*", end="")
    print()