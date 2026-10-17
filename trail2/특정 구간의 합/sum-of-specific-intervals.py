'''
N개의 원소로 이루어진 수열 A가 주어지고, 이어서 M개의 질의가 주어집니다. 각 질의는 두 정수 a1, a2로 이루어지며,
수열 A의 a1번째 원소부터 a2번째 원소까지의 합을 묻습니다.
M개의 질의에 대해 각각의 구간 합을 구해 출력하는 프로그램을 작성해보세요.
단, 수열 A를 전역 변수로 표현하여 문제를 해결해보세요.
'''

n, m = map(int, input().split())  # N - 원소 수, M - 질의 수
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]


def get_sum():
    for a, b in queries:
        total = 0
        for i in range(a-1, b):
            total += arr[i]
        print(total)
    return total

get_sum()