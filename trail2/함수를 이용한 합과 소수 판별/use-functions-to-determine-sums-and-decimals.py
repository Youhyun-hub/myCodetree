a, b = map(int, input().split())

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_primes(A, B):
    cnt = 0
    for i in range(A, B+1):
        if is_prime(i) and ((i//10 + i%10) % 2 == 0):
            cnt += 1
    return cnt

print(get_primes(a, b))
     
