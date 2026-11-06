'''
두 정수 A,B가 주어지면, A를 B로 나눈 몫을 A에 계속해서 저장하는 것을 반복하려고 합니다.

A가 1이하가 되기 전 까지 나눗셈을 반복한다고 할 때, 각 나눗셈 연산마다 나온 나머지들이 등장한 횟수를 제곱하여 그 합을 출력하는 프로그램을 작성해보세요.
'''

a, b = map(int, input().split())
cnt = [0] * b  # 나머지 등장 횟수

while a > 1:
    rest = a % b
    a = a // b
    cnt[rest] += 1

ans = 0  # 나머지 제곱합
for i in cnt:
    ans += i ** 2

print(ans)
    