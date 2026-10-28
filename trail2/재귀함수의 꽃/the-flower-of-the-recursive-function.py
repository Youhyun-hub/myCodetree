'''
N이 주어지면 재귀함수를 단 하나만 이용하여 다음과 같이 출력하는 프로그램을 작성해보세요.

N에서 1까지 1씩 감소하며 하나씩 출력했다가, 다시 1부터 N까지 1씩 증가하며 출력합니다.

ex) N N−1 N−2 N−3 … 2 1 1 2 … N−1 N
'''

N = int(input())

def count_num1(N):
    if N == 0:
        return
    
    print(N, end=" ")
    count_num1(N-1)

count_num1(N)


def count_num2(N):
    if N == 0:
        return
    
    count_num2(N-1)
    print(N, end=" ")

count_num2(N)

