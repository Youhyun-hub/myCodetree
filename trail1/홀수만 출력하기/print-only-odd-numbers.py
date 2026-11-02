N = int(input())

for x in range(N):
    x = int(input())
    
    if x % 3 == 0 and x % 2 != 0:
        print(x)