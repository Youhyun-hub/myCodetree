'''
정수 N이 주어집니다.
N이 짝수이면 2로 나누고, 홀수이면 3으로 나눈 몫을 취하는 작업을 반복하다가 그 값이 1이 되면 그때까지 진행한 작업의 횟수를 구하는 프로그램을 재귀 함수를 이용하여 작성해보세요.
'''

N = int(input())

def f(N):
    if N == 1:
        return 0
    cnt = 1  # 작업 횟수
    if N % 2 == 0:
        return f(N // 2) + cnt
    else:
        return f(N // 3) + cnt

print(f(N))