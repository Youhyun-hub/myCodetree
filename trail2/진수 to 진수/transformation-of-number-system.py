'''
정수 A와 B가 주어지고, A진수로 표현된 어떤 수 N이 주어지면, N을 B진수로 변환하여 출력하는 프로그램을 작성해보세요.
2 <= a, b <= 9
1 <= n의 자릿수 <= 9
N이 두 자리 이상이면 맨 앞자리는 0이 아닙니다. 한 자리인 경우에만 N이 0일 수 있습니다.

'''


a, b = map(int, input().split())  # a진수 -> 10진수 -> b진수
n = list(map(int, input()))

num = 0  # a진수 -> 10진수

for i in range(len(n)):
    num = num * a + n[i]

digits = []
if num == 0:  #  0인 경우
    print(0)
else:
    while num > 0:
        digits.append(num % b)
        num //= b

for k in digits[::-1]:
    print(k, end = "")



