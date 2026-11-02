'''
두 정수 A와 B가 주어집니다.

실수 A/B의 값을 소수점 21번째 자리에서 내림하여 출력하는 프로그램을 작성해보세요.
'''

a, b = map(int, input().split())

print(f"{a//b}.", end="")
for _ in range(20):
    a = a % b * 10  # 나머지에 10을 곱해서 다음 나누는 값으로 두기
    print(a//b, end="")
