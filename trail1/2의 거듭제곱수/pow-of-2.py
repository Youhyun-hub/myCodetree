'''
2의 거듭제곱수 중 하나인 N을 입력받아,
N=2^x를 만족하는 x 값을 구하는 코드를 작성해보세요.
'''


N = int(input())
cnt = 1  # 연산 횟수 = 거듭제곱수

while N > 2:
    N //= 2
    cnt += 1
        
print(cnt)