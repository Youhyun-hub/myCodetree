'''
이진수로 표현된 자연수 N이 주어집니다.
이 수를 십진수로 바꿔 17배를 한 뒤, 그 결과를 다시 이진수로 나타내어 출력하는 프로그램을 작성해 보세요.
'''

N = list(map(int, input()))
num = 0

for i in range(len(N)):
    num = num * 2 + N[i]

new_v = num * 17 # 10진수로 변환하고 17 곱함
digits = []

while new_v > 0:
    digits.append(new_v % 2)
    new_v //= 2

for k in digits[::-1]:
    print(k, end = "")
