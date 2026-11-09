'''
n개의 원소 A1, A2 ,…, An 중 최댓값을 구하는 프로그램을 작성해보세요.
단, 재귀함수를 이용하여 문제를 해결해주세요.
'''


n = int(input())
arr = list(map(int, input().split()))

# 일반 함수로 풀기
'''
def f(n):
    max_v = 0
    i = 0
    while i < n:
        if max_v < arr[i]:
            max_v = arr[i]
        i += 1
    return max_v

print(f(n))
'''

# 재귀로 풀기
def f(n):
    if n == 1:         # 종료 조건
        return arr[0]
    
    pre_max = f(n-1)   # 재귀 호출

    if pre_max < arr[n-1]:
        pre_max = arr[n-1]
    
    return pre_max

print(f(n))