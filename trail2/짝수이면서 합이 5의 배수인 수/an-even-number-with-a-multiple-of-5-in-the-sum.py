n = int(input())

def mul_ten(N):
    a, b = n//10, n%10
    if N % 2 == 0 and (a+b) % 5 == 0:
        print("Yes")
    else:
        print("No")

mul_ten(n)