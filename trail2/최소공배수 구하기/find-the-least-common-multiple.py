n, m = map(int, input().split())

# 최대공약수(GCN) 구하기
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배수(LCM) 구하기
def lcm(a, b):
    return (a * b) // gcd(a, b)

print(lcm(n, m))