a, b = map(int, input().split())

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def sum_prime(A, B):
    total = 0
    for i in range(A, B+1):
        if is_prime(i):
            total += i
    return total

print(sum_prime(a, b))

