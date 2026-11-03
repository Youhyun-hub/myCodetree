'''
팩토리얼이란 차례로 곱한다는 뜻으로, 1부터 어떤 양의 정수 N까지의 정수를 모두 곱한 것을 N!로 나타냅니다.
재귀함수를 이용하여 N! 값을 구하는 프로그램을 작성해보세요.
'''

N = int(input())

def fact(N):
    if N == 1:
        return 1
    return N * fact(N-1)

print(fact(N))