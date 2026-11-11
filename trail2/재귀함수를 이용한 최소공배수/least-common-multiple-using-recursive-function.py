'''
n개의 수가 주어졌을 때 이 수들의 최소공배수를 구하는 프로그램을 작성해보세요.
단, 재귀함수를 이용하여 문제를 해결해주세요.
'''

n = int(input())
arr = list(map(int, input().split()))

# 최대공약수 구하기
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def f(n):
    if n == 1:
        return arr[0]

    prev = f(n-1)   # 앞의 n - 1개 숫자의 최소공배수

    return (prev * arr[n-1]) // gcd(prev, arr[n-1])

print(f(n))