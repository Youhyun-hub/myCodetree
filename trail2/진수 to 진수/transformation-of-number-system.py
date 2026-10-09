'''
정수 A와 B가 주어지고, A진수로 표현된 어떤 수 N이 주어지면, N을 B진수로 변환하여 출력하는 프로그램을 작성해보세요.
2 <= a, b <= 9
1 <= n의 자릿수 <= 9
'''


a, b = map(int, input().split())  # a진수 -> 10진수 -> b진수
n = list(map(int, input()))

num = 0  # a진수 -> 10진수

for i in range(len(n)):
    num = num * a + 1

digits = []
while num > 0:
    digits.append(num % b)
    num //= b

for k in digits[::-1]:
    print(k, end = "")



