'''
정수 N이 주어지고, 바꿀 진수 B가 주어지면, 10진수인 정수 N을 B진수로 변경하여 출력하는 프로그램을 작성해보세요.
단, B로 주어지는 진수는 4, 8로 2가지가 있습니다.
'''

N, B = map(int, input().split())
digits = []

while N > 0:
    digits.append(N % B)
    N //= B

for i in digits[::-1]:
    print(i, end = "")