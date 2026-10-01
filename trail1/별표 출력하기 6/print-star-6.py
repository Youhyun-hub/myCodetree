N = int(input())

for i in range(N):
    for j in range(i):
        print(" ", end = " ")
    for j in range((N+N-1)-i*2):
        print("*", end = " ")
    print()
for i in range(N-1):
    for j in range(N-i-2):
        print(" ", end = " ")
    for j in range(3+(2*i)):
        print("*", end = " ")
    print()