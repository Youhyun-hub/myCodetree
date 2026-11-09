'''
자연수 N이 주어집니다.
N에서 시작하여 N이 짝수면 2로 나누고, N이 홀수면 3을 곱하고 1을 더하는 것을 N이 1이 되기 전까지 계속 반복하려고 합니다. 총 몇 번을 반복해야 1이 되는지를 계산하는 프로그램을 작성해보세요.
단, 재귀함수를 이용하여 문제를 해결해주세요.
'''

n = int(input())
cnt = 0

def f(n):
    global cnt    
    if n == 1:
        return cnt
    
    if n % 2 == 0:   # 짝수이면
        cnt += 1
        return f(n//2)
    
    elif n % 2 != 0:  # 홀수이면
        cnt += 1
        return f((3 * n) + 1)

print(f(n))