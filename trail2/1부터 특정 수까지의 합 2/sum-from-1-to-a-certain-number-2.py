'''
정수 N이 주어지면 재귀함수를 이용하여 1부터 N까지의 합을 구하여 출력하는 프로그램을 작성해보세요.
'''

N = int(input())

def add_num(N):
    if N == 1:  # 종료 조건
        return 1

    return add_num(N-1) + N  # 재귀

print(add_num(N))