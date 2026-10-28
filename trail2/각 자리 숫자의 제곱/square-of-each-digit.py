'''
8자리 이하의 정수 N이 주어지면 재귀함수를 이용하여 각 자리 숫자의 제곱의 합을 출력하는 프로그램을 작성해보세요.
'''

N = int(input())

def f(N):
    if N < 10:
        return N ** 2
    
    return f(N // 10) + (N % 10) ** 2

print(f(N))