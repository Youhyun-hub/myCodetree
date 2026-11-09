'''
세 자리로 이루어진 정수 3개가 주어지면 그 세 수들을 곱한 후,
그 결과값의 각 자리 수의 합을 구하여 출력하는 프로그램을 재귀 함수를 이용하여 작성해보세요.
'''

a, b, c = map(int, input().split())
num = list(str(a * b * c))
idx = len(num)  # 자리 수 길이
total = 0  # 각 자리수의 합

def f(idx, total):
    if idx == 0:     # 종료 조건
        return total

    return f(idx-1, total + int(num[idx-1]))


print(f(idx, total))
    
    
